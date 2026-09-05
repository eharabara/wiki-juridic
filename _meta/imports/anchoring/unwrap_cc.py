"""Second pass on CC-1107-2002 -- rejoin lines the PDF extraction hard-wrapped.

This is the only pass in the anchoring work that touches body text, so the
guarantee is stated in terms of characters rather than lines:

    ONLY WHITESPACE CHANGES.

Every join removes a line break and inserts a single space. No character other
than whitespace is added, removed or reordered. The verifier proves this by
stripping all whitespace from the result and comparing against the same
stripping of the PRE-ANCHORING backup, so the check chains through both the
anchoring pass and this one, back to the original extraction.

Why not use line length. The wrapped width has no clean cut-off: line lengths
form a smooth hump from 80 to 98 characters, and 727 lines of 88+ characters end
a paragraph while 13,068 shorter ones continue. So the rule never guesses from
length. It joins only when the current line is grammatically unfinished -- no
terminal punctuation -- and the next line does not start a new unit.

That is deliberately conservative. A paragraph whose internal sentence boundary
happened to land on a wrap point stays split across two lines. Each resulting
line is then at least a whole sentence, which is what makes a quoted passage
usable; it never merges two paragraphs that should stay apart.

Usage: python unwrap_cc.py <src.md> <dst.md> [--report r.txt]
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_anchor import (split_frontmatter, split_lines_keep, join_lines,
                        detect_sha_convention, body_sha)

UNWRAP_DATE = "2026-09-04"

HEADING = re.compile(r"^#{1,6}\s")
# structural marker lines keep their title on the following line, matching the
# anchored corpus ('## Capitolul I' then 'DISPOZIŢII GENERALE')
STRUCT = re.compile(r"^(Cartea|Capitolul|Sec[ţț]iunea|Subsec[ţț]iunea|"
                    r"T\s+i\s+t\s+l\s+u\s+l|§)\b")
# a line that begins a new unit and must never be pulled onto the previous one
NEWUNIT = re.compile(r"^(\(\d+\)|[a-zșşțţ]\)|\[|Articolul\b|Cartea\b|"
                     r"Capitolul\b|Sec[ţț]iunea\b|Subsec[ţț]iunea\b|"
                     r"T\s+i\s+t\s+l\s+u\s+l\b|§)")
TERMINAL = re.compile(r"[.;:!?][\)\"”]?$")
# ...but these end in a full stop and still continue onto the next line
ABBREV = re.compile(r"\b(art|alin|lit|pct|cap|sec|par|nr|etc|ex)\.$", re.I)
ARTLINE = re.compile(r"^Articolul\s+(\d+(?:\^\d+)?)\.\s")
ARTHEAD = re.compile(r"^#{1,6}\s+(Articolul\s+\d+(?:\^\d+)?\..*)$")


def is_terminal(text):
    t = text.rstrip()
    if ABBREV.search(t):
        return False
    return bool(TERMINAL.search(t))


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
    terms = [t for _, t in pairs]
    nl = b"\r\n" if terms.count(b"\r\n") >= terms.count(b"\n") else b"\n"

    # the preamble (publication data, the list of amending laws) is a column of
    # short unpunctuated lines that must not be run together; leave it alone
    start = next((i for i, l in enumerate(lines) if l.startswith("Cartea")), 0)

    # map each article body line to the title recorded in the heading above it,
    # so a title that wraps is rejoined exactly as far as the anchor says and no
    # further -- this is what keeps art. 23's provision out of its own title
    head_title = {}
    for i, l in enumerate(lines):
        m = ARTHEAD.match(l)
        if m:
            j = i + 1
            while j < len(lines) and lines[j].strip() == "":
                j += 1
            if j < len(lines) and ARTLINE.match(lines[j]):
                head_title[j] = m.group(1).strip()

    out = []           # list of (text, terminator)
    joins = 0
    blanks_absorbed = 0
    title_breaks = 0
    long_lines = []

    i = 0
    while i < len(lines):
        line = lines[i]
        if i < start or HEADING.match(line) or line.strip() == "":
            out.append((line.encode("utf-8"), terms[i]))
            i += 1
            continue

        buf = line
        buf_term = terms[i]
        title = head_title.get(i)
        consumed = i

        while True:
            inside_title = False
            if title is not None:
                if buf.strip() == title:
                    title_breaks += 1
                    break                   # anchor says the title ends here
                if title.startswith(buf.strip()):
                    # still inside a title the anchor recorded in full. Keep
                    # joining even past a full stop: 19 articles carry
                    # two-sentence titles ('Articolul 57. Tutorele supleant si
                    # curatorul supleant. Tutorele special ...').
                    inside_title = True
            if STRUCT.match(buf) and consumed == i:
                break                       # marker keeps its title separate
            if not inside_title and is_terminal(buf):
                break
            j = consumed + 1
            skipped = 0
            while j < len(lines) and lines[j].strip() == "":
                j += 1
                skipped += 1
            if j >= len(lines):
                break
            nxt = lines[j]
            if HEADING.match(nxt) or NEWUNIT.match(nxt):
                break
            buf = buf.rstrip() + " " + nxt.strip()
            buf_term = terms[j]
            blanks_absorbed += skipped
            consumed = j
            joins += 1

        if len(buf) > 4000:
            long_lines.append((i, len(buf)))
        out.append((buf.encode("utf-8"), buf_term))
        i = consumed + 1

    new_body = join_lines(out)

    fm_text = fm.decode("utf-8")
    new_sha = body_sha(new_body, conv)
    prev = re.search(r"^sha256: (\w+)", fm_text, re.M).group(1)
    fm_text = re.sub(r"^sha256: .*$", "sha256_pre_unwrap: %s" % prev,
                     fm_text, count=1, flags=re.M)
    add = [
        "sha256: %s" % new_sha,
        "unwrap_date: '%s'" % UNWRAP_DATE,
        "unwrap_convention: >-",
        "  Hard-wrapped body lines rejoined. Only whitespace changed: each join",
        "  replaces a line break with one space. A line is joined to the next",
        "  only when it ends without terminal punctuation (or ends in a legal",
        "  abbreviation such as 'art.') and the next line does not start a new",
        "  unit. Sentence-boundary wraps are left split, so no two paragraphs",
        "  are ever merged. Article titles are rejoined exactly as far as the",
        "  '## Articolul N.' anchor records, keeping the provision out of the",
        "  title. Strip all whitespace to compare against sha256_pre_anchoring.",
    ]
    fm_nl = "\r\n" if "\r\n" in fm_text else "\n"
    fm_text = fm_text.rstrip("\r\n")
    assert fm_text.endswith("---")
    fm_text = (fm_text[:-3].rstrip("\r\n") + fm_nl + fm_nl.join(add)
               + fm_nl + "---" + fm_nl)

    open(dst, "wb").write(fm_text.encode("utf-8") + new_body)

    o = []
    p = o.append
    p("source              : %s" % src)
    p("output              : %s" % dst)
    p("sha256 pre-unwrap   : %s" % prev)
    p("sha256 post         : %s" % new_sha)
    p("body lines before   : %d" % len(lines))
    p("body lines after    : %d" % len(out))
    p("line breaks removed : %d" % joins)
    p("blank lines absorbed: %d" % blanks_absorbed)
    p("article titles closed by their anchor: %d" % title_breaks)
    p("lines over 4000 chars: %d %s" % (len(long_lines), long_lines[:5]))
    txt = "\n".join(o)
    print(txt)
    if report_path:
        open(report_path, "w", encoding="utf-8").write(txt + "\n")


if __name__ == "__main__":
    main()
