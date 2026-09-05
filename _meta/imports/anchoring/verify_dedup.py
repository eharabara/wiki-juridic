"""Prove the title-deduplication pass is exactly reversible.

The deletion is only safe if the removed text is fully recoverable. So the check
does not merely count lines: it RECONSTRUCTS the pre-dedup body by re-inserting
each anchor's text as a body line beneath it, and requires the result to be
byte-identical to the pre-dedup file.

  1. reconstruction  -- rebuild and compare byte-for-byte against the pre-dedup
     body.
  2. anchors intact  -- still 2,657 article anchors, still ascending.
  3. no stray copies -- no article title line survives immediately under its
     anchor, except the one deliberately retained (art. 723).
  4. frontmatter     -- records the pass and its sha256 reproduces the new body.

Usage: python verify_dedup.py <pre_dedup.md> <dedup.md>
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_anchor import (split_frontmatter, split_lines_keep, join_lines,
                        detect_sha_convention)

ANCHOR = re.compile(r"^##\s+(Articolul\s+\d+(?:\^\d+)?\..*)$")
ART_HEAD = re.compile(r"^#{1,6}\s+Articolul\s+(\d+)(?:\^(\d+))?")
RETAINED = {"723"}


def main():
    pre = open(sys.argv[1], "rb").read()
    now = open(sys.argv[2], "rb").read()
    _, pre_body = split_frontmatter(pre)
    nfm, now_body = split_frontmatter(now)
    ok = True

    pre_pairs = split_lines_keep(pre_body)
    now_pairs = split_lines_keep(now_body)
    now_lines = [t.decode("utf-8") for t, _ in now_pairs]

    # --- 1. reconstruction ---------------------------------------------------
    rebuilt = []
    for k, (t, term) in enumerate(now_pairs):
        rebuilt.append((t, term))
        m = ANCHOR.match(now_lines[k])
        if not m:
            continue
        nxt = now_lines[k + 1] if k + 1 < len(now_lines) else ""
        # A body copy survives when the following line still opens with the
        # anchor text. That covers both an exact duplicate left in place and
        # art. 723, whose line continues past the title into the provision.
        if nxt.startswith(m.group(1)):
            continue
        rebuilt.append((m.group(1).encode("utf-8"), term))
    same = join_lines(rebuilt) == pre_body
    ok &= same
    print("1. reconstruction    : %s"
          % ("PASS - re-inserting every anchor's text rebuilds the pre-dedup "
             "body byte-for-byte" if same else "FAIL"))
    if not same:
        a, b = pre_body, join_lines(rebuilt)
        print("   lengths: pre %d, rebuilt %d" % (len(a), len(b)))
        for n in range(min(len(a), len(b))):
            if a[n] != b[n]:
                print("   first difference at byte %d" % n)
                print("     pre     : %r" % a[max(0, n - 70):n + 70])
                print("     rebuilt : %r" % b[max(0, n - 70):n + 70])
                break

    # --- 2. anchors intact ---------------------------------------------------
    labels = []
    for l in now_lines:
        m = ART_HEAD.match(l)
        if m:
            labels.append((int(m.group(1)), int(m.group(2) or 0)))
    asc = all(labels[i] > labels[i - 1] for i in range(1, len(labels)))
    good = len(labels) == 2657 and asc
    ok &= good
    print("2. anchors intact    : %s (%d anchors, ascending: %s)"
          % ("PASS" if good else "FAIL", len(labels), asc))

    # --- 3. no stray duplicate copies ---------------------------------------
    stray = []
    for k, l in enumerate(now_lines):
        m = ANCHOR.match(l)
        if not m:
            continue
        nxt = now_lines[k + 1] if k + 1 < len(now_lines) else ""
        if nxt == m.group(1):
            num = re.match(r"Articolul\s+(\d+)", m.group(1)).group(1)
            if num not in RETAINED:
                stray.append((k, m.group(1)[:80]))
    ok &= not stray
    print("3. no stray copies   : %s (%d unexpected duplicates)"
          % ("PASS" if not stray else "FAIL", len(stray)))
    for k, h in stray[:8]:
        print("     line %-6d %s" % (k, h))

    # --- 4. frontmatter ------------------------------------------------------
    conv, rec = detect_sha_convention(now)
    fine = conv in ("raw", "LF")
    ok &= fine
    print("4. frontmatter sha256: %s (convention %s)"
          % ("PASS - reproduces the deduplicated body" if fine else "FAIL", conv))
    t = nfm.decode("utf-8")
    for f in ["source_file_sha256", "sha256_pre_anchoring", "sha256_pre_unwrap",
              "sha256_pre_dedup", "dedup_date", "dedup_convention"]:
        present = re.search(r"^%s:" % f, t, re.M) is not None
        ok &= present
        print("   %-22s %s" % (f, "present" if present else "MISSING"))

    print("\nOVERALL: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
