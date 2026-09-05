"""Verification for job 3, where heading lines are MODIFIED, not inserted.

  1. non-heading lines byte-identical between original and fixed file;
  2. heading count unchanged, and every heading either identical or differing
     only by its number token changing from the flattened form to 'P^S';
  3. the resulting article sequence is strictly ascending under (base, suffix);
  4. frontmatter records the change and its sha256 reproduces the new body.

Usage: python verify_superscripts.py <original.md> <fixed.md>
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_anchor import (split_frontmatter, split_lines_keep, join_lines,
                        detect_sha_convention)

HEADING = re.compile(r"^#{1,6}\s")
ART = re.compile(r"^(#{1,6}\s+Articolul\s+)(\d+(?:\^\d+)?)(.*)$", re.S)


def key(label):
    b, _, s = label.partition("^")
    return (int(b), int(s) if s else 0)


def main():
    orig = open(sys.argv[1], "rb").read()
    fixed = open(sys.argv[2], "rb").read()
    _, ob = split_frontmatter(orig)
    ffm, fb = split_frontmatter(fixed)
    ol = split_lines_keep(ob)
    fl = split_lines_keep(fb)
    ok = True

    # --- 1. non-heading lines identical ------------------------------------
    on = [(t, x) for t, x in ol if not HEADING.match(t.decode("utf-8", "replace"))]
    fn = [(t, x) for t, x in fl if not HEADING.match(t.decode("utf-8", "replace"))]
    same = join_lines(on) == join_lines(fn)
    ok &= same
    print("1. non-heading lines : %s" % ("PASS - byte-identical" if same
                                         else "FAIL"))

    # --- 2. headings differ only in the number token ------------------------
    oh = [t.decode("utf-8") for t, _ in ol if HEADING.match(t.decode("utf-8", "replace"))]
    fh = [t.decode("utf-8") for t, _ in fl if HEADING.match(t.decode("utf-8", "replace"))]
    count_ok = len(oh) == len(fh)
    ok &= count_ok
    changed, bad = [], []
    if count_ok:
        for a, b in zip(oh, fh):
            if a == b:
                continue
            ma, mb = ART.match(a), ART.match(b)
            if not (ma and mb) or ma.group(1) != mb.group(1) \
                    or ma.group(3) != mb.group(3):
                bad.append((a, b))
                continue
            flat, norm = ma.group(2), mb.group(2)
            if "^" not in norm or norm.replace("^", "") != flat:
                bad.append((a, b))
                continue
            changed.append((flat, norm))
    ok &= not bad
    print("2. heading integrity : %s (headings %d -> %d, changed %d)"
          % ("PASS" if count_ok and not bad else "FAIL", len(oh), len(fh),
             len(changed)))
    for a, b in bad[:5]:
        print("     UNEXPECTED CHANGE:\n       %r\n       %r" % (a, b))
    for flat, norm in changed:
        print("     %-8s -> %-9s (digits preserved: %s)"
              % (flat, norm, "yes" if norm.replace("^", "") == flat else "NO"))

    # --- 3. ascending -------------------------------------------------------
    labels = [ART.match(h).group(2) for h in fh if ART.match(h)]
    keys = [key(x) for x in labels]
    desc = [(labels[i - 1], labels[i]) for i in range(1, len(keys))
            if keys[i] <= keys[i - 1]]
    ok &= not desc
    print("3. strictly ascending: %s" % ("PASS" if not desc else "FAIL %s" % desc[:6]))
    # Gaps must be measured on BASE numbers. A superscript run bridges the
    # sequence visually (79 -> 88^1..88^4 -> 89) and would otherwise hide that
    # arts. 80-88 are absent.
    bases = []
    for lab in labels:
        b = key(lab)[0]
        if not bases or bases[-1] != b:
            bases.append(b)
    gaps = [(bases[i - 1], bases[i]) for i in range(1, len(bases))
            if bases[i] > bases[i - 1] + 1]
    print("   numbering gaps on base numbers (%d): %s" % (len(gaps), gaps))
    for lo, hi in gaps:
        missing = list(range(lo + 1, hi))
        print("      arts. %s absent between art. %d and art. %d"
              % (", ".join(str(x) for x in missing), lo, hi))
    # a base that appears only as a superscript prefix is itself absent
    present = {key(l)[0] for l in labels if key(l)[1] == 0}
    prefix_only = sorted({key(l)[0] for l in labels if key(l)[1] > 0} - present)
    if prefix_only:
        print("   base article absent, exists only as superscript prefix: %s"
              % ", ".join("art. %d" % x for x in prefix_only))

    # --- 4. frontmatter -----------------------------------------------------
    conv, rec = detect_sha_convention(fixed)
    good = conv in ("raw", "LF")
    ok &= good
    print("4. frontmatter sha256: %s (convention %s)"
          % ("PASS - reproduces the fixed body" if good else "FAIL", conv))
    t = ffm.decode("utf-8")
    for f in ["sha256_pre_anchoring", "superscript_articles"]:
        present = re.search(r"^%s:" % f, t, re.M) is not None
        ok &= present
        print("   %-22s %s" % (f, "present" if present else "MISSING"))

    print("\nOVERALL: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
