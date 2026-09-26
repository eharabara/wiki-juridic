#!/usr/bin/env python3
"""Registrul act cu act al corpusului juridic (2026-09-26, auditul din aceeasi zi, constatarea A3).

Manifestul moldova-legal descrie loturile (sectiunile AV, AX), nu fiecare act. Datele pe act stau
in frontmatter-ul fisierelor raw si in paginile de entitate; scriptul le aduna intr-un tabel
generat, ca sa nu se scrie de mina si sa nu ramina in urma. Citeste si graful de citare (cite acte
citeaza fiecare act), pentru coada de citire a paginilor mecanice.

    python _meta/coverage/build_act_register.py          scrie _meta/coverage/act-register.md
    python _meta/coverage/build_act_register.py --check  iese 1 daca fisierul e invechit
"""
import glob
import os
import re
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "_meta", "coverage", "act-register.md")
ROOTS = ["raw/papers/cnpf", "raw/papers/moldova-legal", "raw/papers/bnm/legal-ro"]
GRAPH = os.path.join(ROOT, "_meta", "graph", "citation-graph.md")


def front(path):
    t = open(path, encoding="utf-8", errors="replace").read()
    m = re.match(r"---\r?\n(.*?)\r?\n---\r?\n", t, re.S)
    if not m:
        return {}, t
    try:
        return (yaml.safe_load(m.group(1)) or {}), t[m.end():]
    except yaml.YAMLError:
        return {}, t


def cited_by():
    out = {}
    if not os.path.exists(GRAPH):
        return out
    for line in open(GRAPH, encoding="utf-8"):
        m = re.match(r"^\| `([^`]+)` \| (\d+) \| (\d+) \| (\d+) \|", line)
        if m:
            out[m.group(1)] = int(m.group(4))
    return out


def route(fm):
    em = str(fm.get("extract_method", ""))
    if em.startswith("curl showdetails"):
        return "showdetails"
    if "web_extract" in em:
        return "web_extract"
    if "pdf" in em.lower():
        return "pdf"
    return (em[:24] or "-")


def build():
    cites = cited_by()
    ents = {}
    for p in glob.glob(os.path.join(ROOT, "entities", "*.md")):
        fm, body = front(p)
        stem = os.path.basename(p)[:-3]
        ents[stem] = {"confidence": fm.get("confidence", "-"),
                      "mechanical": "Pagină mecanică" in body or "Pagina mecanica" in body}
    rows, fut = [], []
    for r in ROOTS:
        for p in sorted(glob.glob(os.path.join(ROOT, r, "*.md"))):
            stem = os.path.basename(p)[:-3]
            if stem.startswith("_") or stem.startswith(("UE-", "AA-")):
                continue
            fm, body = front(p)
            if fm.get("source_type") != "legal-text":
                continue
            anchors = len(re.findall(r"^#{2,3} Art", body, re.M))
            e = ents.get(stem)
            rows.append((stem, r.split("/")[-1], fm.get("doc_id", "-"), fm.get("consolidation_date", "-"),
                         str(fm.get("refreshed") or fm.get("ingested") or "-"), route(fm), anchors,
                         (e["confidence"] + (" (mecanic)" if e["mechanical"] else "")) if e else "fara pagina",
                         cites.get(stem, 0)))
    for p in sorted(glob.glob(os.path.join(ROOT, "raw/papers/moldova-legal/viitor", "*.md"))):
        fm, _ = front(p)
        fut.append((os.path.basename(p)[:-3], fm.get("future_version_of", "-"), fm.get("applies_from", "-"),
                    fm.get("doc_id", "-")))
    L = ["---",
         "title: Registrul act cu act al corpusului juridic",
         "type: summary",
         "generated_by: _meta/coverage/build_act_register.py",
         "---", "",
         "# Registrul act cu act",
         "",
         "**Fisier generat. Nu se editeaza manual.** Rulati `python _meta/coverage/build_act_register.py`. "
         "Sursa: frontmatter-ul fisierelor raw, paginile de entitate si graful de citare.", "",
         f"{len(rows)} acte cu text legal, {len(fut)} versiuni viitoare. Coloana *ruta* arata cum a intrat actul: "
         "`showdetails` (extractorul standard, cu verificare pe HTML), `web_extract` sau `pdf` (rute fara "
         "verificarea aceea; vezi regula `raw.unanchored-article`). *Citat de* = cite acte detinute il citeaza, "
         "din graf.", "",
         "## Actele", "",
         "| Act | Radacina | doc_id | Consolidare | Ingerat/refacut | Ruta | Ancore | Pagina de entitate | Citat de |",
         "|---|---|---|---|---|---|---:|---|---:|"]
    for r in rows:
        L.append("| `%s` | %s | %s | %s | %s | %s | %d | %s | %d |" % r)
    L += ["", "## Coada de citire a paginilor mecanice", "",
          "Paginile de entitate marcate *Pagina mecanica* (actul nu a fost citit integral), in ordinea "
          "numarului de acte care il citeaza. Un act citat des inchide mai multe lanturi de citare.", "",
          "| Act | Citat de | Consolidare |", "|---|---:|---|"]
    mech = [r for r in rows if "(mecanic)" in r[7]]
    for r in sorted(mech, key=lambda x: (-x[8], x[0])):
        L.append(f"| `{r[0]}` | {r[8]} | {r[3]} |")
    L += ["", "## Versiunile viitoare (`viitor/`)", "",
          "Nu se citeaza ca drept in vigoare. Vezi `concepts/consolidari-viitoare-ingerate.md`.", "",
          "| Fisier | Versiune a lui | Se aplica de la | doc_id |", "|---|---|---|---|"]
    for f in fut:
        L.append("| `%s` | `%s` | %s | %s |" % f)
    return "\n".join(L) + "\n"


def main():
    text = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8", newline="").read() if os.path.exists(OUT) else ""
        if cur.replace("\r\n", "\n") == text:
            print("registrul act cu act este la zi")
            return 0
        print("registrul act cu act este invechit; rulati build_act_register.py")
        return 1
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print(f"registrul act cu act scris ({text.count(chr(10))} linii)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
