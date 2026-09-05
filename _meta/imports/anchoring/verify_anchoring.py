"""Verification required by the anchoring brief, for any anchored file.

Checks, in order:
  1. strip-and-compare  -- remove every inserted heading line and confirm the
     remainder is byte-identical to the pre-anchoring original.
  2. anchor count       -- '## Articolul N' headings == line-initial article
     markers in the original.
  3. ascending numbers  -- article numbers strictly ascending, every gap listed
     so it can be matched against a recorded repeal.
  4. frontmatter        -- parses, records the expected fields, and the stated
     sha256 reproduces the anchored body under the file's own convention.

Usage: python verify_anchoring.py <original.md> <anchored.md> [--marker REGEX]
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_anchor import (split_frontmatter, split_lines_keep, join_lines,
                        detect_sha_convention, body_sha)

import lib_superscript

HEADING = re.compile(rb"^#{1,6} ")
# a heading label may carry a normalised superscript: 'Articolul 13^1.'
ART_HEAD = re.compile(r"^#{1,6}\s+Articolul\s+(\d+|[IVXLC]+)(?:\^(\d+))?")
ART_SRC = re.compile(r"^Articolul\s+(\d+)")

ROMAN = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def roman_to_int(s):
    total = 0
    for i, ch in enumerate(s):
        v = ROMAN[ch]
        if i + 1 < len(s) and v < ROMAN[s[i + 1]]:
            total -= v
        else:
            total += v
    return total


def sort_key(label):
    """Order 13 < 13^1 < 14, and I < II < III for amending laws."""
    base, _, sup = label.partition("^")
    n = int(base) if base.isdigit() else roman_to_int(base)
    return (n, int(sup) if sup else 0)


def main():
    orig_path, anch_path = sys.argv[1], sys.argv[2]
    marker = HEADING
    if "--marker" in sys.argv:
        marker = re.compile(sys.argv[sys.argv.index("--marker") + 1].encode())

    orig = open(orig_path, "rb").read()
    anch = open(anch_path, "rb").read()
    _, obody = split_frontmatter(orig)
    afm, abody = split_frontmatter(anch)

    ok = True

    # --- 1. strip and compare ------------------------------------------------
    kept = [(t, term) for t, term in split_lines_keep(abody)
            if not marker.match(t)]
    stripped = join_lines(kept)
    same = stripped == obody
    ok &= same
    print("1. strip-and-compare : %s" % ("PASS - byte-identical" if same
                                         else "FAIL"))
    if not same:
        print("     original %d bytes, stripped %d bytes"
              % (len(obody), len(stripped)))
        for n in range(min(len(obody), len(stripped))):
            if obody[n] != stripped[n]:
                print("     first difference at byte %d" % n)
                print("     orig: %r" % obody[max(0, n - 60):n + 60])
                print("     strp: %r" % stripped[max(0, n - 60):n + 60])
                break

    # --- 2. anchor count -----------------------------------------------------
    olines = [t.decode("utf-8") for t, _ in split_lines_keep(obody)]
    alines = [t.decode("utf-8") for t, _ in split_lines_keep(abody)]
    src_pat = ART_SRC
    if "--source-pattern" in sys.argv:
        src_pat = re.compile(sys.argv[sys.argv.index("--source-pattern") + 1])
    src_toks = [src_pat.match(l).group(1) for l in olines if src_pat.match(l)]
    src_nums = [int(t) for t in src_toks if t.isdigit()]
    # the source may carry flattened superscripts; normalise them the same way
    # the anchoring script did, so the two lists are comparable
    sup = {c["number"]: c["normalised"] for c in lib_superscript.detect(src_nums)}
    src_arts = [sup.get(int(t), t) if t.isdigit() else t for t in src_toks]
    head_arts = [m.group(1) + ("^" + m.group(2) if m.group(2) else "")
                 for m in (ART_HEAD.match(l) for l in alines) if m]
    match = src_arts == head_arts
    ok &= match
    print("2. anchor count      : %s (source %d, headings %d)"
          % ("PASS" if match else "FAIL", len(src_arts), len(head_arts)))
    if not match:
        for a, b in list(zip(src_arts, head_arts))[:10]:
            if a != b:
                print("     first mismatch: source %r vs heading %r" % (a, b))
                break

    # --- 3. ascending --------------------------------------------------------
    keys = [sort_key(x) for x in head_arts]
    desc = [(head_arts[i - 1], head_arts[i]) for i in range(1, len(keys))
            if keys[i] <= keys[i - 1]]
    asc = not desc
    ok &= asc
    gaps = []
    for i in range(1, len(keys)):
        if keys[i][1] == 0 and keys[i][0] > keys[i - 1][0] + 1:
            gaps.append((head_arts[i - 1], head_arts[i]))
    print("3. strictly ascending: %s"
          % ("PASS" if asc else "FAIL " + str(desc[:10])))
    print("   numbering gaps (%d): %s" % (len(gaps), gaps))
    if sup:
        print("   superscript articles normalised: %s"
              % ", ".join("%d -> %s" % (k, v) for k, v in sorted(sup.items())))

    # --- 4. frontmatter ------------------------------------------------------
    fmt = afm.decode("utf-8")
    conv, recorded = detect_sha_convention(anch)
    digest_ok = conv in ("raw", "LF")
    ok &= digest_ok
    print("4. frontmatter sha256: %s (convention %s)"
          % ("PASS - reproduces the anchored body" if digest_ok else "FAIL", conv))
    for field in ["sha256_pre_anchoring", "articole detectate",
                  "anchoring_date", "anchor_convention"]:
        present = re.search(r"^%s:" % re.escape(field), fmt, re.M) is not None
        ok &= present
        print("   %-22s %s" % (field, "present" if present else "MISSING"))

    print("\nOVERALL: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
