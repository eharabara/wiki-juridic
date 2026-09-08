"""Recensamint al referintelor la hotaririle Curtii Constitutionale (HCC) in textele brute.

Citeste fiecare act din raw/papers/{cnpf,moldova-legal,bnm/legal-ro}, sare UE-* si traducerile,
si extrage:
  - rindurile HCC din blocul de istoric al modificarilor (fisa), forma "HCCnn din dd.mm.yy, MO..."
  - marcajele inline "[Art.N ... prin HCCnn din dd.mm.yy ...]" cu articolul atins
  - mentiunile "neconstitutional" in corp, ca numar
Scrie _meta/plans/hcc-census-<data>.json si .md. Nu modifica nimic altceva.
"""
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DIRS = ["raw/papers/cnpf", "raw/papers/moldova-legal", "raw/papers/bnm/legal-ro"]

HCC_ID = re.compile(r"HCC\s*(\d+)\s+din\s+(\d{2}\.\d{2}\.\d{2,4})")
INLINE = re.compile(r"\[([^\[\]]*?HCC[^\[\]]*?)\]")
ART_IN_MARK = re.compile(r"^\s*(Art\.\s*\d+(?:\^\d+)?(?:/\d+)?[^,;]*)", re.I)


def frontmatter(text):
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    fm = {}
    for line in text[3:end].splitlines():
        m = re.match(r"^([A-Za-z_0-9]+):\s*(.*)$", line)
        if m:
            fm[m.group(1)] = m.group(2).strip().strip("'\"")
    return fm, text[end + 4:]


def norm_date(d):
    dd, mm, yy = d.split(".")
    if len(yy) == 2:
        yy = ("19" if int(yy) > 50 else "20") + yy
    return f"{yy}-{mm}-{dd}"


def scan(path):
    text = path.read_text(encoding="utf-8")
    fm, body = frontmatter(text)
    if fm.get("source_type") == "translation":
        return None
    lines = body.splitlines()
    fisa, inline = [], []
    for i, line in enumerate(lines, 1):
        marks = [m.group(1) for m in INLINE.finditer(line)]
        st = line.strip()
        # forma a doua a marcajului: linie "*Notă: ..." sau "*Art.N ..." cu HCC si "neconstitu"
        if not marks and st.startswith("*") and HCC_ID.search(st) and re.search(r"neconstitu", st, re.I):
            marks = [st.lstrip("*").strip()]
        for mark in marks:
            ids = [(n, norm_date(d)) for n, d in HCC_ID.findall(mark)]
            art = ART_IN_MARK.match(mark) or re.match(r"^\s*Not[aă]:\s*(Articolul\s+\d+(?:\^\d+)?[^–-]*)", mark, re.I)
            inline.append({"line": i, "article": art.group(1).strip() if art else None,
                           "hcc": ids, "text": mark[:300]})
        if not marks:
            for n, d in HCC_ID.findall(line):
                fisa.append({"line": i, "hcc": [n, norm_date(d)], "text": st[:200]})
    neconst = sum(1 for l in lines if re.search(r"neconstitu", l, re.I))
    return {
        "act": path.stem, "file": str(path.relative_to(ROOT)).replace("\\", "/"),
        "doc_id": fm.get("doc_id"), "consolidation": fm.get("consolidation_date") or fm.get("consolidated"),
        "fisa_hcc": fisa, "inline_hcc": inline, "neconstitutional_lines": neconst,
    }


def main():
    out = []
    for d in DIRS:
        for p in sorted((ROOT / d).glob("*.md")):
            if p.name.startswith("_") or p.name.startswith("UE-"):
                continue
            r = scan(p)
            if r and (r["fisa_hcc"] or r["inline_hcc"] or r["neconstitutional_lines"]):
                out.append(r)
    today = date.today().isoformat()
    base = ROOT / "_meta/plans" / f"hcc-census-{today}"
    base.with_suffix(".json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")

    all_hcc = {}
    for r in out:
        for f in r["fisa_hcc"]:
            all_hcc.setdefault(tuple(f["hcc"]), set()).add(r["act"])
        for m in r["inline_hcc"]:
            for h in m["hcc"]:
                all_hcc.setdefault(tuple(h), set()).add(r["act"])

    md = [f"# Recensamint HCC in textele brute, {today}", "",
          f"Generat de `_meta/plans/hcc_census.py`. {len(out)} acte cu cel putin o referinta; "
          f"{len(all_hcc)} hotariri distincte (numar + data).", "",
          "| act | doc_id | consolidare | rinduri HCC in fisa | marcaje inline | linii 'neconstitutional' |",
          "|---|---|---|---:|---:|---:|"]
    for r in out:
        md.append(f"| `{r['act']}` | {r['doc_id']} | {r['consolidation']} | {len(r['fisa_hcc'])} | "
                  f"{len(r['inline_hcc'])} | {r['neconstitutional_lines']} |")
    md += ["", "## Marcaje inline (articolul atins, hotarirea)", ""]
    for r in out:
        if not r["inline_hcc"]:
            continue
        md.append(f"### `{r['act']}`")
        for m in r["inline_hcc"]:
            ids = ", ".join(f"HCC{n}/{d}" for n, d in m["hcc"]) or "-"
            md.append(f"- l.{m['line']} **{m['article'] or '?'}** — {ids} — {m['text'][:160]}")
        md.append("")
    md += ["## Hotariri distincte si actele pe care le ating", "",
           "| HCC | data | acte |", "|---|---|---|"]
    for (n, d), acts in sorted(all_hcc.items(), key=lambda kv: kv[0][1]):
        md.append(f"| HCC {n} | {d} | {', '.join(sorted(acts))} |")
    base.with_suffix(".md").write_text("\n".join(md) + "\n", encoding="utf-8", newline="\n")
    print(f"{len(out)} acte, {len(all_hcc)} hotariri distincte -> {base}.md/.json")


if __name__ == "__main__":
    main()
