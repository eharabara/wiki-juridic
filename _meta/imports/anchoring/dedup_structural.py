"""Remove the structural marker line duplicated under its own anchor.

Companion to dedup_titles.py, for the three anchor kinds whose body line is an
exact copy of the anchor:

    ## Cartea a doua        -> body 'Cartea a doua'
    ## Capitolul IV         -> body 'Capitolul IV'
    ##### § 1. Dispozitii   -> body '§ 1. Dispozitii'

Three kinds are deliberately NOT handled, because their anchor is not a copy of
the line beneath it and deleting that line would lose text:

    Titlul       -- the anchor normalises the PDF's letter-spaced 'T i t l u l I'
                    to 'Titlul I', so the source form exists only in the body.
    Sectiunea    -- the anchor joins the marker and its title ('### Sectiunea a
    Subsectiunea    2-a. <title>'), while the body keeps them on separate lines.

One repair happens first. Five paragraph-sign anchors are TRUNCATED: job 1 took
the '§' line verbatim, but the PDF had wrapped the paragraph's own title, so the
anchor holds only its first line while the body (after the unwrap pass) holds the
whole thing. Those anchors are completed from the body line before the body line
is removed, so no text is lost and the anchor stops under-reporting its title.

Usage: python dedup_structural.py <src.md> <dst.md> [--report r.txt]
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_anchor import (split_frontmatter, split_lines_keep, join_lines,
                        detect_sha_convention, body_sha)

DEDUP_DATE = "2026-09-04"
KINDS = [
    (re.compile(r"^(##)\s+(Cartea\b.*)$"), "Cartea"),
    (re.compile(r"^(##)\s+(Capitolul\b.*)$"), "Capitolul"),
    (re.compile(r"^(#####)\s+(§.*)$"), "paragraf"),
    # Sectiunea and Subsectiunea anchors normally carry a title the marker line
    # does not, so the exact-match test simply never fires for them and they are
    # left alone. The one exception is a section with no title of its own --
    # 'Sectiunea a 3-a- abrogata' -- where the anchor does equal the source line.
    (re.compile(r"^(###)\s+(Sec[ţț]iunea\b.*)$"), "Sectiunea"),
    (re.compile(r"^(####)\s+(Subsec[ţț]iunea\b.*)$"), "Subsectiunea"),
]


def main():
    src, dst = sys.argv[1], sys.argv[2]
    report_path = None
    if "--report" in sys.argv:
        report_path = sys.argv[sys.argv.index("--report") + 1]

    data = open(src, "rb").read()
    fm, body = split_frontmatter(data)
    conv, recorded = detect_sha_convention(data)
    pairs = list(split_lines_keep(body))
    lines = [t.decode("utf-8") for t, _ in pairs]

    drop = set()
    completed = []
    kept = []
    counts = {k: 0 for _, k in KINDS}

    for i, line in enumerate(lines):
        for rx, kind in KINDS:
            m = rx.match(line)
            if not m:
                continue
            level, anchor_text = m.group(1), m.group(2)
            nxt = lines[i + 1] if i + 1 < len(lines) else ""
            if nxt == anchor_text:
                drop.add(i + 1)
                counts[kind] += 1
            elif nxt.startswith(anchor_text) and nxt.strip() != "":
                # truncated anchor: the body carries the full title
                new_anchor = "%s %s" % (level, nxt)
                pairs[i] = (new_anchor.encode("utf-8"), pairs[i][1])
                drop.add(i + 1)
                counts[kind] += 1
                completed.append((i, anchor_text, nxt))
            else:
                kept.append((i, kind, anchor_text, nxt))
            break

    new_pairs = [p for k, p in enumerate(pairs) if k not in drop]
    new_body = join_lines(new_pairs)

    # Each run must record its predecessor hash under a DISTINCT key. Reusing a
    # key on a second run produces duplicate YAML keys, where the loader keeps
    # only the last value and the earlier link silently drops out of the chain.
    stage = "dedup_structural"
    if "--stage" in sys.argv:
        stage = sys.argv[sys.argv.index("--stage") + 1]

    fm_text = fm.decode("utf-8")
    new_sha = body_sha(new_body, conv)
    prev = re.search(r"^sha256: (\w+)", fm_text, re.M).group(1)
    assert not re.search(r"^sha256_pre_%s:" % re.escape(stage), fm_text, re.M), (
        "frontmatter already carries sha256_pre_%s; pass a distinct --stage "
        "so the provenance chain is not overwritten" % stage)
    fm_text = re.sub(r"^sha256: .*$", "sha256_pre_%s: %s" % (stage, prev),
                     fm_text, count=1, flags=re.M)
    add = [
        "sha256: %s" % new_sha,
        "%s_date: '%s'" % (stage, DEDUP_DATE),
        "%s_convention: >-" % stage,
        "  The Cartea, Capitolul and paragraph-sign marker lines that duplicated",
        "  their own anchors have been removed, on the same exact-match rule used",
        "  for article titles. Titlul, Sectiunea and Subsectiunea are untouched:",
        "  their anchors are not copies of the line beneath them. Five",
        "  paragraph-sign anchors were truncated by the original anchoring pass",
        "  and have been completed from the body line before it was removed.",
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
    p("sha256 pre        : %s" % prev)
    p("sha256 post       : %s" % new_sha)
    p("body lines before : %d" % len(lines))
    p("body lines after  : %d" % len(new_pairs))
    p("")
    p("duplicate marker lines removed:")
    for _, k in KINDS:
        p("   %-12s %d" % (k, counts[k]))
    p("   %-12s %d" % ("TOTAL", sum(counts.values())))
    p("")
    p("truncated anchors completed from the body line: %d" % len(completed))
    for i, old, new in completed:
        p("   line %-6d was : %s" % (i, old))
        p("   %-11s now : %s" % ("", new))
    p("")
    p("anchors left alone (anchor is not a copy of the next line): %d" % len(kept))
    for i, kind, a, n in kept[:10]:
        p("   line %-6d %-10s anchor %r" % (i, kind, a[:60]))
        p("   %-11s %-10s next   %r" % ("", "", n[:60]))
    txt = "\n".join(o)
    print(txt)
    if report_path:
        open(report_path, "w", encoding="utf-8").write(txt + "\n")


if __name__ == "__main__":
    main()
