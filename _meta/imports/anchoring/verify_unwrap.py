"""Verify the unwrap pass changed whitespace and nothing else.

The check deliberately compares against the PRE-ANCHORING backup, not against
the anchored file, so a single comparison covers both passes: heading insertion
and line rejoining. If this passes, no character of legal text has changed since
the original PyMuPDF extraction.

  1. whitespace-only  -- strip every whitespace character from the unwrapped
     body (minus the inserted heading lines) and from the pre-anchoring body;
     the two must be byte-identical.
  2. anchors intact   -- the article anchors still number 2,657 and still
     ascend.
  3. no merged paragraphs -- a paragraph marker '(N)' appearing mid-line right
     after a finished sentence would mean two paragraphs were run together.
     Genuine cross-references ('alin. (1)', 'art. 139 alin. (2)') are excluded.
  4. frontmatter records the pass and its sha256 reproduces the new body.

Usage: python verify_unwrap.py <pre_anchoring.md> <unwrapped.md>
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_anchor import split_frontmatter, split_lines_keep, detect_sha_convention

HEADING = re.compile(r"^#{1,6}\s")
ART_HEAD = re.compile(r"^#{1,6}\s+Articolul\s+(\d+)(?:\^(\d+))?")
WS = re.compile(rb"\s+")
PARA = re.compile(r"\(\d+\)")
# A paragraph number introduced by a reference word is a cross-reference, not a
# new paragraph. Matched against the text immediately preceding the marker.
REF = re.compile(r"(alin|art|lit|pct|par|sec|cap|litera|alineatul|articolul|"
                 r"punctul|capitolul)\.?\s*(?:\d+\s*)?$", re.I)
SENT_END = re.compile(r"[.;]\s$")


def strip_ws(b):
    return WS.sub(b"", b)


def main():
    pre = open(sys.argv[1], "rb").read()
    now = open(sys.argv[2], "rb").read()
    _, pre_body = split_frontmatter(pre)
    nfm, now_body = split_frontmatter(now)
    ok = True

    # --- 1. whitespace-only, chained through both passes --------------------
    kept = [t for t, _ in split_lines_keep(now_body)
            if not HEADING.match(t.decode("utf-8", "replace"))]
    a = strip_ws(pre_body)
    b = strip_ws(b"\n".join(kept))
    same = a == b
    ok &= same
    print("1. whitespace-only   : %s"
          % ("PASS - every non-whitespace character identical to the "
             "pre-anchoring body" if same else "FAIL"))
    print("   compared %d non-whitespace bytes" % len(a))
    if not same:
        print("   lengths: pre %d, now %d" % (len(a), len(b)))
        for n in range(min(len(a), len(b))):
            if a[n] != b[n]:
                print("   first difference at non-whitespace byte %d" % n)
                print("     pre: %r" % a[max(0, n - 60):n + 60])
                print("     now: %r" % b[max(0, n - 60):n + 60])
                break

    # --- 2. anchors intact --------------------------------------------------
    lines = [t.decode("utf-8") for t, _ in split_lines_keep(now_body)]
    labels = []
    for l in lines:
        m = ART_HEAD.match(l)
        if m:
            labels.append((int(m.group(1)), int(m.group(2) or 0)))
    asc = all(labels[i] > labels[i - 1] for i in range(1, len(labels)))
    good_anchors = len(labels) == 2657 and asc
    ok &= good_anchors
    print("2. anchors intact    : %s (%d article anchors, ascending: %s)"
          % ("PASS" if good_anchors else "FAIL", len(labels), asc))

    # --- 3. no paragraph markers swallowed mid-line -------------------------
    bad = []
    for i, l in enumerate(lines):
        if HEADING.match(l) or not l.strip():
            continue
        for m in PARA.finditer(l):
            if m.start() == 0:
                continue
            before = l[:m.start()]
            if REF.search(before):
                continue
            if SENT_END.search(before):
                bad.append((i, l[max(0, m.start() - 70):m.start() + 14]))
                break
    ok &= not bad
    print("3. merged paragraphs : %s (%d suspicious lines)"
          % ("PASS - none" if not bad else "REVIEW", len(bad)))
    for i, ctx in bad[:12]:
        print("     line %-6d ...%s" % (i, ctx))

    # --- 4. frontmatter -----------------------------------------------------
    conv, rec = detect_sha_convention(now)
    good = conv in ("raw", "LF")
    ok &= good
    print("4. frontmatter sha256: %s (convention %s)"
          % ("PASS - reproduces the unwrapped body" if good else "FAIL", conv))
    t = nfm.decode("utf-8")
    for f in ["sha256_pre_anchoring", "sha256_pre_unwrap", "unwrap_date",
              "unwrap_convention"]:
        present = re.search(r"^%s:" % f, t, re.M) is not None
        ok &= present
        print("   %-22s %s" % (f, "present" if present else "MISSING"))

    print("\nOVERALL: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
