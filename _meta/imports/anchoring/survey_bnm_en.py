"""Survey the BNM English corpus before anchoring it.

The headline figure of ~3,555 line-initial 'Article N' markers is an upper bound
and mostly noise. Four things have to be separated first:

  1. genuine headings vs cross-references. A heading is 'Article 12. Repealed'
     or 'Article 1. - (1) ...'; a wrapped cross-reference is 'Article 231;' or
     'Article 2 of the Law no.179/2016'. Requiring a period straight after the
     number splits them cleanly.

  2. a table of contents. Law 92/2022 lists all 124 articles with dot leaders
     before the body starts, so every heading appears twice. Anchoring the ToC
     would produce duplicate anchors and destroy ascending order.

  3. flattened superscripts, exactly as in the Romanian corpus. In Law 232/2016
     'Article 602, 603, 604 ... 6010' sit between arts. 60 and 61: they are
     60^1 ... 60^10. Law 548/1995 has 11^3 stored as 113, Law 202/2017 has 52^1
     as 521. Some files keep the real Unicode superscript ('Article 5¹'), so
     both forms occur.

  4. duplicate documents. Most laws are present twice, as .pdf.md and .docx.md
     of the same source, with different extraction quality.

Reads only; prints what anchoring would do.

Usage: python survey_bnm_en.py [--verbose]
"""

import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_anchor import split_frontmatter, split_lines_keep
import lib_superscript

ROOT = "raw/papers/bnm"
# a heading: number, optional Unicode superscript, period, then content
HEAD = re.compile(r"^Article\s+(\d+)([¹²³⁴])?\s*\.\s+\S")
NUM = re.compile(r"^Article\s+(\d+)([¹²³⁴])?")
SUPMAP = {"¹": "1", "²": "2", "³": "3", "⁴": "4"}
DOTS = re.compile(r"\.{5,}")


def headings(lines):
    out = []
    for i, l in enumerate(lines):
        if not HEAD.match(l):
            continue
        m = NUM.match(l)
        out.append({"line": i, "num": int(m.group(1)),
                    "usup": SUPMAP.get(m.group(2) or "", ""),
                    "dots": bool(DOTS.search(l)), "text": l})
    return out


def split_toc(hs):
    """Return (toc, body). A ToC is a leading block that restarts at a low
    number, or a leading block carrying dot leaders."""
    if not hs:
        return [], []
    dotted = sum(1 for h in hs if h["dots"])
    if dotted >= 5:
        # everything up to the last dot-leader line is contents
        last = max(k for k, h in enumerate(hs) if h["dots"])
        return hs[:last + 1], hs[last + 1:]
    # otherwise look for a restart: a long ascending run followed by a drop to 1
    for k in range(1, len(hs)):
        if hs[k]["num"] == 1 and hs[k - 1]["num"] > 5:
            return hs[:k], hs[k:]
    return [], hs


def main():
    verbose = "--verbose" in sys.argv
    rows = []
    for p in sorted(glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True)):
        d = open(p, "rb").read()
        try:
            fm, b = split_frontmatter(d)
        except ValueError:
            b = d
        lines = [t.decode("utf-8", "replace") for t, _ in split_lines_keep(b)]
        hs = headings(lines)
        if len(hs) < 5:
            continue
        toc, body = split_toc(hs)
        nums = [h["num"] for h in body]
        cands = lib_superscript.detect(nums)
        supmap = {c["index"]: c["normalised"] for c in cands
                  if c["confidence"] != "unresolved"}
        unresolved = [c for c in cands if c["confidence"] == "unresolved"]
        labels = []
        for k, h in enumerate(body):
            if h["usup"]:
                labels.append("%d^%s" % (h["num"], h["usup"]))
            elif k in supmap:
                labels.append(supmap[k])
            else:
                labels.append(str(h["num"]))
        keyed = [(int(x.split("^")[0]), int(x.split("^")[1]) if "^" in x else 0)
                 for x in labels]
        desc = sum(1 for k in range(1, len(keyed)) if keyed[k] <= keyed[k - 1])
        rows.append({"path": p.replace(os.sep, "/"), "all": len(hs),
                     "toc": len(toc), "body": len(body),
                     "usup": sum(1 for h in body if h["usup"]),
                     "flat": len(supmap), "unres": len(unresolved),
                     "desc": desc, "labels": labels})

    rows.sort(key=lambda r: -r["body"])
    print("%5s %5s %5s %5s %5s %5s  %s"
          % ("all", "toc", "body", "uni^", "flat^", "desc", "file"))
    print("-" * 104)
    for r in rows:
        print("%5d %5d %5d %5d %5d %5d  %s"
              % (r["all"], r["toc"], r["body"], r["usup"], r["flat"],
                 r["desc"], os.path.basename(r["path"])[:58]))
    print("-" * 104)
    print("files worth anchoring : %d" % len(rows))
    print("headings to anchor    : %d" % sum(r["body"] for r in rows))
    print("table-of-contents rows skipped: %d" % sum(r["toc"] for r in rows))
    print("superscripts: %d already Unicode, %d flattened and recovered"
          % (sum(r["usup"] for r in rows), sum(r["flat"] for r in rows)))
    bad = [r for r in rows if r["desc"]]
    print("files still not strictly ascending after normalisation: %d" % len(bad))
    for r in bad:
        print("   %-58s %d descents" % (os.path.basename(r["path"])[:56],
                                        r["desc"]))


if __name__ == "__main__":
    main()
