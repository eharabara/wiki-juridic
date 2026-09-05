"""End-to-end provenance check for CC-1107-2002.

Three passes now sit between the file and the original PyMuPDF extraction:

    anchoring   -- heading lines inserted above the source lines
    unwrap      -- hard-wrapped lines rejoined (whitespace only)
    dedup       -- the article title copy under each anchor removed

This script undoes all three in reverse and compares what comes back against the
pre-anchoring original. It is the single check worth running before trusting the
file: if it passes, no character of legal text has been altered since extraction,
and every deletion is recoverable.

    dedup file
      -> re-insert each anchor's text as a body line   (undoes dedup)
      -> drop every heading line                       (undoes anchoring)
      -> strip all whitespace                          (undoes unwrap)
      == the original extraction, byte for byte

Usage: python verify_chain.py <pre_anchoring.md> <current.md>
"""

import hashlib
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_anchor import split_frontmatter, split_lines_keep, join_lines

ANCHOR_TEXT = re.compile(r"^#{1,6}\s+(.*)$")
HEADING = re.compile(r"^#{1,6}\s")
WS = re.compile(rb"\s+")

# 'Titlul' is the one anchor kind that is NOT a copy of the line beneath it: the
# anchoring pass normalised the PDF's letter-spaced 'T i t l u l I' to
# 'Titlul I', so the source form survives only in the body and was never
# deleted. Re-inserting it would fabricate a line that never existed.
NEVER_DEDUPED = re.compile(r"^Titlul\b")


def marker_of(text):
    """The part of an anchor that the body line would repeat verbatim.

    An anchor may carry a title the body line does not ('### Secțiunea a 2-a.
    Respectul datorat...' sits above a bare 'Secțiunea a 2-a'), so presence of
    the body copy is tested on the marker, not on the whole anchor.
    """
    head, sep, _ = text.partition(". ")
    return head if sep else text


def main():
    orig_path, cur_path = sys.argv[1], sys.argv[2]
    _, orig = split_frontmatter(open(orig_path, "rb").read())
    _, cur = split_frontmatter(open(cur_path, "rb").read())

    pairs = split_lines_keep(cur)
    lines = [t.decode("utf-8") for t, _ in pairs]

    # undo dedup: put every removed title copy back
    reb = []
    for k, (t, term) in enumerate(pairs):
        reb.append((t, term))
        m = ANCHOR_TEXT.match(lines[k])
        if not m or NEVER_DEDUPED.match(m.group(1)):
            continue
        text = m.group(1)
        nxt = lines[k + 1] if k + 1 < len(lines) else ""
        if nxt.startswith(marker_of(text)):
            continue                       # copy still present, nothing removed
        reb.append((text.encode("utf-8"), term))
    restored = join_lines(reb)

    # undo anchoring: drop the inserted headings
    kept = [t for t, _ in split_lines_keep(restored)
            if not HEADING.match(t.decode("utf-8", "replace"))]

    # undo unwrap: line breaks became spaces, so compare without whitespace
    got = WS.sub(b"", b"\n".join(kept))
    want = WS.sub(b"", orig)

    hg = hashlib.sha256(got).hexdigest()
    hw = hashlib.sha256(want).hexdigest()
    ok = got == want

    print("chain: %s" % cur_path)
    print("   against original: %s" % orig_path)
    print("   non-whitespace bytes  original %d, recovered %d" % (len(want), len(got)))
    print("   sha256 original       %s" % hw)
    print("   sha256 recovered      %s" % hg)
    print("   RESULT: %s" % ("PASS - the legal text is unchanged since extraction"
                             if ok else "FAIL"))
    if not ok:
        for n in range(min(len(want), len(got))):
            if want[n] != got[n]:
                print("   first difference at non-whitespace byte %d" % n)
                print("     original  : %r" % want[max(0, n - 70):n + 70])
                print("     recovered : %r" % got[max(0, n - 70):n + 70])
                break
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
