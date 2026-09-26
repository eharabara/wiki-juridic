#!/usr/bin/env python3
"""Candidati pentru amanari de intrare in vigoare scrise in proza (2026-09-26).

Registrul in-force (`build_inforce_register.py`) citeste numai marcajele intre paranteze de amendament
(`[Art.N ... in vigoare DD.MM.YY]`). CLAUDE.md, intrebarea deschisa 9, a documentat zece cazuri in care amanarea sta in
proza articolului final al unei legi (`L-9-2026`, `L-66-2017`, `L-72-2025`, `L-22-2025`, `L-227-2025`, `L-317-2025`...)
si registrul nu o poate vedea. Scriptul nu o poate vedea nici el in sens juridic, dar gaseste CANDIDATII: articolele din
sfirsitul unui act (ultimele 6 articole) care spun `intra in vigoare` / `se aplica` impreuna cu o data, un termen sau o
conditie, si care nu sint deja acoperite de o intrare din registrul in-force. Un om decide daca este o amanare.

    python _meta/inforce/build_prose_deferral_candidates.py           scrie prose-deferral-candidates.md
    python _meta/inforce/build_prose_deferral_candidates.py --check   iese 1 daca fisierul e invechit
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "_meta", "inforce", "prose-deferral-candidates.md")
ROOTS = ["raw/papers/cnpf", "raw/papers/moldova-legal", "raw/papers/bnm/legal-ro"]
TRIGGER = re.compile(r"(intr[aă]\s+[iî]n\s+vigoare|se\s+aplic[aă]\s+(?:de\s+la|[iî]ncep[aâ]nd|dup[aă]|p[iî]n[aă])|se\s+pune\s+[iî]n\s+aplicare)", re.I)
CONDITION = re.compile(r"(cu\s+excep[tț]ia|la\s+expirarea|dup[aă]\s+(?:crearea|aprobarea|implementarea|publicarea|expirarea|trecerea)|"
                       r"p[iî]n[aă]\s+la\s+(?:data|implementarea|crearea)|[iî]ncep[aâ]nd\s+cu|de\s+la\s+data\s+de|"
                       r"\b\d{1,2}\s+(?:ianuarie|februarie|martie|aprilie|mai|iunie|iulie|august|septembrie|octombrie|noiembrie|decembrie)\s+20\d\d|"
                       r"(?:un|doi|trei|\d+)\s+(?:an|ani|luni|zile)\s+de\s+la|\bla\s+\d{1,2}\.\d{1,2}\.20\d\d)", re.I)
ANCHOR = re.compile(r"^#{2,3} Art", re.M)
EXCEPTION = re.compile(r"(cu\s+excep[tț]ia|care\s+(?:va\s+)?intr[aă]|dup[aă]\s+(?:crearea|aprobarea|implementarea|adoptarea)|p[iî]n[aă]\s+la\s+(?:data|implementarea|crearea)|"
                       r"la\s+data\s+adopt[aă]rii|dup[aă]\s+ce)", re.I)
MONTHS = {m: i + 1 for i, m in enumerate("ianuarie februarie martie aprilie mai iunie iulie august septembrie octombrie noiembrie decembrie".split())}
TODAY = (2026, 9, 26)


def has_future_date(para):
    for d, mo, y in re.findall(r"\b(\d{1,2})\s+(ianuarie|februarie|martie|aprilie|mai|iunie|iulie|august|septembrie|octombrie|noiembrie|decembrie)\s+(20\d\d)", para, re.I):
        if (int(y), MONTHS[mo.lower()], int(d)) > TODAY:
            return True
    for d, mo, y in re.findall(r"\b(\d{1,2})\.(\d{1,2})\.(20\d\d)", para):
        if (int(y), int(mo), int(d)) > TODAY:
            return True
    return False


def front_body(path):
    t = open(path, encoding="utf-8", errors="replace").read()
    m = re.match(r"---\r?\n(.*?)\r?\n---\r?\n", t, re.S)
    return (m.group(1) if m else ""), (t[m.end():] if m else t)


def registered():
    """Actele care apar deja in registrul in-force (dupa stem)."""
    p = os.path.join(ROOT, "_meta", "inforce", "in-force-register.md")
    if not os.path.exists(p):
        return set()
    return {m.split("--")[0] for m in re.findall(r"^\| ([A-Z][A-Za-z0-9\-]+(?:--[0-9\-]+)?) \|", open(p, encoding="utf-8").read(), re.M)}


def build():
    reg = registered()
    rows = []
    for r in ROOTS:
        for p in sorted(glob.glob(os.path.join(ROOT, r, "*.md"))):
            stem = os.path.basename(p)[:-3]
            if stem.startswith(("_", "UE-", "AA-")):
                continue
            fm, body = front_body(p)
            if "source_type: legal-text" not in fm:
                continue
            parts = re.split(r"(?m)^(?=#{2,3} Art)", body)
            arts = [x for x in parts if ANCHOR.match(x)]
            for blk in arts[-6:]:
                head = blk.split("\n", 1)[0].strip()
                for para in blk.split("\n")[1:]:
                    if TRIGGER.search(para) and (EXCEPTION.search(para) or has_future_date(para)):
                        # nu numara notele de tip "[... in vigoare DD.MM.YY]", care sint marcaje de amendament
                        if para.strip().startswith("["):
                            continue
                        rows.append((stem, head[:70], re.sub(r"\s+", " ", para.strip())[:230], stem in reg))
    return rows


def render(rows):
    L = ["---", "title: Candidati pentru amanari de intrare in vigoare scrise in proza", "type: summary",
         "generated_by: _meta/inforce/build_prose_deferral_candidates.py", "---", "",
         "# Amanari in proza: candidati", "",
         "**Fisier generat. Nu se editeaza manual.** Registrul in-force citeste numai marcajele intre paranteze; amanarile scrise in proza "
         "articolului final (CLAUDE.md, intrebarea 9) ii scapa. Aici sint paragrafele din ultimele 6 articole ale fiecarui act care spun "
         "`intra in vigoare` sau `se aplica` impreuna cu o exceptie, o conditie sau o data viitoare (dupa 2026-09-26); datele simple deja trecute nu se listeaza. **Sint candidati, nu constatari**: multe sint "
         "simple date de intrare in vigoare deja trecute. Coloana *in registru* spune daca actul are deja o intrare in registrul in-force.", "",
         f"{len(rows)} paragrafe in {len({r[0] for r in rows})} acte.", "",
         "| Act | Articol | in registru | Paragraf |", "|---|---|---|---|"]
    for stem, head, para, inreg in rows:
        L.append(f"| `{stem}` | {head.replace('|', '/')} | {'da' if inreg else 'nu'} | {para.replace('|', '/')} |")
    return "\n".join(L) + "\n"


def main():
    text = render(build())
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8", newline="").read().replace("\r\n", "\n") if os.path.exists(OUT) else ""
        print("candidatii de amanari in proza sint la zi" if cur == text else "candidatii de amanari in proza sint invechiti")
        return 0 if cur == text else 1
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print(f"candidati de amanari in proza scrisi ({text.count(chr(10))} linii)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
