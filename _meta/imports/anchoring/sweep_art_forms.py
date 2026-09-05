"""Job 2 sweep -- find every raw file with the same 'Art.N.' anchoring defect.

The defect: a file holds full legal text but declares "articole detectate: 0"
(or carries no article anchors) because the ingest regex only matched the modern
'Articolul N.' form and the act uses the pre-2000 'Art.N. - ' form instead.

Reports, per file: the declared article count, how many line-initial article
markers of each form are actually present, and how many '## Articolul' anchors
exist. Anything where markers exist but anchors do not is a candidate.

Usage: python sweep_art_forms.py [root ...]
"""

import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_anchor import split_frontmatter, split_lines_keep

# pre-2000 form: 'Art.1. - ', 'Art. 20. - '
ARTDASH = re.compile(r"^Art\.\s*\d+\s*\.\s*[–—-]\s")
# amending laws number their own articles in Roman: 'Art. I. - ', 'Art. II. - '
ARTROMAN = re.compile(r"^Art\.\s*([IVXLC]+)\s*\.\s*[–—-]\s")
# other line-initial 'Art.' shapes worth seeing (notes, plain 'Art.5 ')
ARTOTHER = re.compile(r"^Art\.\s*\d+")
ARTICOLUL = re.compile(r"^Articolul\s+\d+")
ANCHOR = re.compile(r"^#{1,6}\s+Articolul\s+\d+")
DECLARED = re.compile(r"articole detectate:?\**\s*(\d+)", re.I)


def scan(path):
    data = open(path, "rb").read()
    try:
        fm, body = split_frontmatter(data)
    except ValueError:
        fm, body = b"", data
    text = data.decode("utf-8", "replace")
    lines = [t.decode("utf-8", "replace") for t, _ in split_lines_keep(body)]
    m = DECLARED.search(text)
    return {
        "path": path,
        "declared": int(m.group(1)) if m else None,
        "artdash": sum(1 for l in lines if ARTDASH.match(l)),
        "artroman": sum(1 for l in lines if ARTROMAN.match(l)),
        "roman_list": [ARTROMAN.match(l).group(1) for l in lines
                       if ARTROMAN.match(l)],
        "artother": sum(1 for l in lines if ARTOTHER.match(l)
                        and not ARTDASH.match(l)),
        "articolul": sum(1 for l in lines if ARTICOLUL.match(l)),
        "anchors": sum(1 for l in lines if ANCHOR.match(l)),
        "chars": len(body.decode("utf-8", "replace")),
    }


def main():
    roots = sys.argv[1:] or ["raw/papers"]
    rows = []
    for root in roots:
        for p in glob.glob(os.path.join(root, "**", "*.md"), recursive=True):
            if os.path.basename(p).startswith("_manifest"):
                continue
            rows.append(scan(p))

    print("scanned %d files under %s\n" % (len(rows), ", ".join(roots)))

    hits = [r for r in rows if r["artdash"] and r["anchors"] < r["artdash"]]
    print("=" * 100)
    print("A. DEFECT MATCH -- pre-2000 'Art.N. -' markers present, anchors missing")
    print("=" * 100)
    if not hits:
        print("   none")
    for r in sorted(hits, key=lambda r: -r["artdash"]):
        print("   %-52s declared=%-5s Art.N.-=%-4d anchors=%-4d chars=%d"
              % (r["path"].replace(os.sep, "/"), r["declared"], r["artdash"],
                 r["anchors"], r["chars"]))

    print()
    print("=" * 100)
    print("B. OTHER line-initial 'Art.N' forms (not the 'Art.N. -' pattern)")
    print("=" * 100)
    other = [r for r in rows if r["artother"]]
    if not other:
        print("   none")
    for r in sorted(other, key=lambda r: -r["artother"])[:25]:
        print("   %-52s declared=%-5s other Art.N=%-4d anchors=%-4d"
              % (r["path"].replace(os.sep, "/"), r["declared"], r["artother"],
                 r["anchors"]))

    print()
    print("=" * 100)
    print("C. DECLARED ZERO or NONE, with substantial text")
    print("=" * 100)
    zero = [r for r in rows
            if (r["declared"] in (0, None)) and r["chars"] > 5000]
    for r in sorted(zero, key=lambda r: -r["chars"])[:40]:
        note = ""
        if r["artdash"]:
            note = "  <-- 'Art.N. -' form present"
        elif r["articolul"] or r["anchors"]:
            note = "  <-- 'Articolul' markers present"
        print("   %-52s declared=%-5s chars=%-8d Art.N.-=%-4d Articolul=%-4d anchors=%-4d%s"
              % (r["path"].replace(os.sep, "/"), r["declared"], r["chars"],
                 r["artdash"], r["articolul"], r["anchors"], note))

    print()
    print("=" * 100)
    print("E. ROMAN-NUMERAL article forms ('Art. I. -') -- amending laws")
    print("=" * 100)
    rom = [r for r in rows if r["artroman"]]
    if not rom:
        print("   none")
    for r in sorted(rom, key=lambda r: -r["artroman"]):
        print("   %-52s declared=%-5s Art.<Roman>=%-4d anchors=%-4d  %s"
              % (r["path"].replace(os.sep, "/"), r["declared"], r["artroman"],
                 r["anchors"], ", ".join(r["roman_list"])))

    print()
    print("=" * 100)
    print("D. ANCHOR COVERAGE GAP -- 'Articolul N.' markers present, fewer anchors")
    print("=" * 100)
    gap = [r for r in rows if r["articolul"] > r["anchors"]]
    if not gap:
        print("   none")
    for r in sorted(gap, key=lambda r: -(r["articolul"] - r["anchors"]))[:25]:
        print("   %-52s Articolul=%-5d anchors=%-5d gap=%d"
              % (r["path"].replace(os.sep, "/"), r["articolul"], r["anchors"],
                 r["articolul"] - r["anchors"]))


if __name__ == "__main__":
    main()
