"""Produce a representative unified diff between the original and anchored file.

A full diff of the Civil Code is 3,000+ hunks, so this samples the regions that
actually exercise the heading rules, named on the command line or defaulted to
the interesting cases for CC-1107-2002.

Usage: python sample_diff.py <original.md> <anchored.md> [--regions a:b,c:d]
"""

import os
import re
import sys
import difflib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_anchor import split_frontmatter, split_lines_keep

# (label, first original line, last original line) -- 0-based body line numbers
DEFAULT_REGIONS = [
    ("book / title / chapter / first articles", 46, 70),
    ("section + article with plain body (no paragraph numbering)", 345, 356),
    ("subsection nesting", 880, 890),
    ("two-part title split by a full stop (art. 57)", 772, 778),
    ("title wrapping over five lines, capitalised continuation (art. 305)",
     4308, 4320),
    ("paragraph-sign subdivision", 1102, 1110),
    ("SOURCE DEFECT: title and body merged on one line (art. 723)", 9426, 9432),
    ("repeal gap: arts. 2171-2172 struck out", 26680, 26692),
    ("repeal gap: section-level repeal covering arts. 2047-2054", 25196, 25206),
    ("end of file", 31770, 31785),
]


def main():
    orig_path, anch_path = sys.argv[1], sys.argv[2]
    regions = DEFAULT_REGIONS
    if "--regions" in sys.argv:
        spec = sys.argv[sys.argv.index("--regions") + 1]
        regions = []
        for part in spec.split(","):
            a, b = part.split(":")
            regions.append(("region %s" % part, int(a), int(b)))

    _, obody = split_frontmatter(open(orig_path, "rb").read())
    _, abody = split_frontmatter(open(anch_path, "rb").read())
    olines = [t.decode("utf-8") for t, _ in split_lines_keep(obody)]
    alines = [t.decode("utf-8") for t, _ in split_lines_keep(abody)]

    # map original line index -> index in the anchored file
    amap = []
    j = 0
    for i in range(len(olines)):
        while j < len(alines) and alines[j].startswith("#"):
            j += 1
        amap.append(j)
        j += 1

    out = []
    for label, lo, hi in regions:
        lo = max(0, lo)
        hi = min(len(olines) - 1, hi)
        a_lo = amap[lo]
        a_hi = amap[hi] if hi < len(amap) else len(alines) - 1
        left = olines[lo:hi + 1]
        right = alines[a_lo:a_hi + 1]
        out.append("")
        out.append("=" * 78)
        out.append("%s   [original lines %d-%d]" % (label.upper(), lo, hi))
        out.append("=" * 78)
        for line in difflib.unified_diff(left, right, lineterm="",
                                         fromfile="raw (before)",
                                         tofile="anchored (after)", n=3):
            out.append(line)
    txt = "\n".join(out)
    print(txt)
    return txt


if __name__ == "__main__":
    main()
