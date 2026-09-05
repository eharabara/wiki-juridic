"""Job 3 -- normalise flattened superscript article numbers in existing anchors.

Unlike jobs 1 and 2, these files ALREADY carry '## Articolul N.' anchors, so
this pass MODIFIES heading lines rather than inserting new ones. Exactly one
token changes per affected line: the article number. Everything else on the
line, and every non-heading line, is untouched.

Verification is therefore:
  * every non-heading line byte-identical, and
  * heading lines identical except for the number token on the changed ones.

Usage: python fix_superscripts.py <src.md> <dst.md> [--report r.txt]
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_anchor import (split_frontmatter, split_lines_keep, join_lines,
                        detect_sha_convention, body_sha)
import lib_superscript

ANCHOR_DATE = "2026-09-04"
HEAD = re.compile(r"^(#{1,6}\s+Articolul\s+)(\d+)(.*)$", re.S)


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

    heads = [(i, HEAD.match(l)) for i, l in enumerate(lines) if HEAD.match(l)]
    nums = [int(m.group(2)) for _, m in heads]
    cands = [c for c in lib_superscript.detect(nums)
             if c["confidence"] != "unresolved"]
    unresolved = [c for c in lib_superscript.detect(nums)
                  if c["confidence"] == "unresolved"]

    changes = []
    new_pairs = list(pairs)
    for c in cands:
        li, m = heads[c["index"]]
        old_line = lines[li]
        new_line = "%s%s%s" % (m.group(1), c["normalised"], m.group(3))
        new_pairs[li] = (new_line.encode("utf-8"), pairs[li][1])
        changes.append((li, old_line, new_line, c))

    new_body = join_lines(new_pairs)

    fm_text = fm.decode("utf-8")
    new_sha = body_sha(new_body, conv)
    fm_text = re.sub(r"^sha256: .*$", "sha256_pre_anchoring: %s" % recorded,
                     fm_text, count=1, flags=re.M)
    add = ["sha256: %s" % new_sha, "sha256_convention: %s" % conv]
    if changes:
        add.append("superscript_articles:")
        for _, _, _, c in changes:
            add.append("  - normalised: '%s'" % c["normalised"])
            add.append("    flattened_as: %d" % c["number"])
            add.append("    run_of: %d" % c["run_len"])
            add.append("    between: 'art. %s and art. %s'"
                       % (c["before"], c["after"]))
            add.append("    base_article_present: %s"
                       % ("true" if c["base_present"] else "false"))
            add.append("    evidence: positional only -- the extraction kept no"
                       " caret form, no unicode superscript and no amendment"
                       " note for this number anywhere in the file")
    add += [
        "superscript_normalised_date: '%s'" % ANCHOR_DATE,
        "anchor_convention: >-",
        "  Article anchors already existed. This pass only NORMALISES flattened",
        "  superscript numbers in the heading line: '## Articolul 1461.' becomes",
        "  '## Articolul 146^1.'. Exactly one token changes per affected line;",
        "  every other heading, and every non-heading line, is byte-identical.",
    ]
    fm_nl = "\r\n" if "\r\n" in fm_text else "\n"
    fm_text = fm_text.rstrip("\r\n")
    assert fm_text.endswith("---"), repr(fm_text[-20:])
    fm_text = (fm_text[:-3].rstrip("\r\n") + fm_nl + fm_nl.join(add)
               + fm_nl + "---" + fm_nl)

    open(dst, "wb").write(fm_text.encode("utf-8") + new_body)

    o = []
    p = o.append
    p("source            : %s" % src)
    p("output            : %s" % dst)
    p("sha256 convention : %s" % conv)
    p("sha256 pre        : %s" % recorded)
    p("sha256 post       : %s" % new_sha)
    p("anchors in file   : %d" % len(heads))
    p("headings changed  : %d" % len(changes))
    p("")
    for li, old, new, c in changes:
        p("  line %-6d %s" % (li, old.strip()[:96]))
        p("       ->      %s" % new.strip()[:96])
        p("       run of %d between art. %s and art. %s; base art. %d %s; %s"
          % (c["run_len"], c["before"], c["after"], c["prefix"],
             "present" if c["base_present"] else "ABSENT", c["confidence"]))
    if unresolved:
        p("")
        p("UNRESOLVED anomalies (reported, not changed):")
        for c in unresolved:
            p("   art. %s between art. %s and art. %s"
              % (c["number"], c["before"], c["after"]))
    txt = "\n".join(o)
    print(txt)
    if report_path:
        open(report_path, "w", encoding="utf-8").write(txt + "\n")


if __name__ == "__main__":
    main()
