"""Remove the article-title line duplicated immediately under its own anchor.

After anchoring and unwrapping, each article title exists twice: once as the
inserted anchor '## Articolul 23. Noţiunea de persoană fizică' and once as the
body line directly beneath it, now byte-identical because the unwrap pass
rejoined the title exactly as far as the anchor records.

This pass deletes the body copy. It is the only pass that removes text, so it
is deliberately narrow and provably reversible:

  * a line is deleted ONLY when it is byte-identical to the anchor immediately
    above it (the anchor text with its '## ' prefix removed), and only when it
    is the very next line;
  * nothing else is touched;
  * re-inserting the anchor text as a body line under every anchor reproduces
    the input byte-for-byte, which the verifier checks.

Art. 723 is not deduplicated: the PDF put the end of its title and the start of
its provision on one physical line, so the body line carries text the anchor
does not, and deleting it would lose the provision's opening words.

Usage: python dedup_titles.py <src.md> <dst.md> [--report r.txt]
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_anchor import (split_frontmatter, split_lines_keep, join_lines,
                        detect_sha_convention, body_sha)

DEDUP_DATE = "2026-09-04"
ANCHOR = re.compile(r"^##\s+(Articolul\s+\d+(?:\^\d+)?\..*)$")


def main():
    src, dst = sys.argv[1], sys.argv[2]
    report_path = None
    if "--report" in sys.argv:
        report_path = sys.argv[sys.argv.index("--report") + 1]

    data = open(src, "rb").read()
    fm, body = split_frontmatter(data)
    conv, recorded = detect_sha_convention(data)
    pairs = split_lines_keep(body)
    lines = [t.decode("utf-8") for t, _ in pairs]

    drop = set()
    kept_reasons = []
    for i, l in enumerate(lines):
        m = ANCHOR.match(l)
        if not m:
            continue
        if i + 1 < len(lines) and lines[i + 1] == m.group(1):
            drop.add(i + 1)
        else:
            nxt = lines[i + 1] if i + 1 < len(lines) else ""
            kept_reasons.append((i, m.group(1), nxt))

    new_pairs = [p for k, p in enumerate(pairs) if k not in drop]
    new_body = join_lines(new_pairs)

    fm_text = fm.decode("utf-8")
    new_sha = body_sha(new_body, conv)
    prev = re.search(r"^sha256: (\w+)", fm_text, re.M).group(1)
    fm_text = re.sub(r"^sha256: .*$", "sha256_pre_dedup: %s" % prev,
                     fm_text, count=1, flags=re.M)
    add = [
        "sha256: %s" % new_sha,
        "dedup_date: '%s'" % DEDUP_DATE,
        "dedup_convention: >-",
        "  The article title line that duplicated its own anchor has been",
        "  removed. A line was deleted only where it was byte-identical to the",
        "  '## Articolul N.' anchor immediately above it. The title is fully",
        "  recoverable from the anchor: re-inserting each anchor's text as a body",
        "  line beneath it reproduces the pre-dedup body byte-for-byte. Art. 723",
        "  is retained, because the extraction put the end of its title and the",
        "  start of its provision on the same physical line.",
    ]
    fm_nl = "\r\n" if "\r\n" in fm_text else "\n"
    fm_text = fm_text.rstrip("\r\n")
    assert fm_text.endswith("---")
    fm_text = (fm_text[:-3].rstrip("\r\n") + fm_nl + fm_nl.join(add)
               + fm_nl + "---" + fm_nl)

    open(dst, "wb").write(fm_text.encode("utf-8") + new_body)

    o = []
    p = o.append
    p("source            : %s" % src)
    p("output            : %s" % dst)
    p("sha256 pre-dedup  : %s" % prev)
    p("sha256 post       : %s" % new_sha)
    p("body lines before : %d" % len(lines))
    p("body lines after  : %d" % len(new_pairs))
    p("duplicate title lines removed: %d" % len(drop))
    p("")
    p("anchors whose next line was NOT an exact duplicate (kept): %d"
      % len(kept_reasons))
    for i, h, nxt in kept_reasons:
        p("   line %-6d anchor : %s" % (i, h[:92]))
        p("   %-11s body   : %s" % ("", nxt[:92]))
    txt = "\n".join(o)
    print(txt)
    if report_path:
        open(report_path, "w", encoding="utf-8").write(txt + "\n")


if __name__ == "__main__":
    main()
