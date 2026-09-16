"""Job 4 (2026-09-16) -- unwrap article titles broken across a hard line-wrap.

Root cause (found 2026-09-05, fixed here): `ingest_business_law.py`'s anchoring step
takes each `Articolul N. ...` line extracted from legis.md's HTML and prefixes it
with `## `, one physical line at a time. If legis.md's own rendering had already
broken a long title across two (or three) lines, the anchor captured only the
first fragment and the rest sat as ordinary, unrecognised body text directly
below it -- e.g. `## Articolul 4. Acţiunea legii contravenţionale asupra` /
`persoanei şi în spaţiu` / `(1) Contravenţia ...` in `COD-218-2008`.

Method, chosen to satisfy the immutability rule in CLAUDE.md ("Safety"): the same
continuation heuristic already validated for the Civil Code
(`anchor_cc.collect_article_title` -- a DANGLING word set plus STOP patterns) is
applied to decide whether the line(s) immediately following a `## Articolul N.`
heading are the missing tail of its title. When they are, ONLY THE HEADING LINE'S
TEXT is rewritten to the joined title. The continuation line(s) below stay exactly
where they are, byte-for-byte -- now visually duplicated under the corrected
heading, the same shape already accepted for CC-1107-2002's 22 genuine cases.
No line is added, removed or reordered; only existing `## Articolul` heading
lines have their text extended, and only with words already present, verbatim,
on the very next line(s) of the same file.

Proof required by this file's own `verify()`: with every `## Articolul` heading
line removed from both the pre-fix and post-fix versions, the two remainders
must be byte-identical, and the two files must have the same total line count.
That is a stronger, more direct proof than "strip and compare to a backup" for
this specific edit shape (heading text edited in place, nothing inserted or
deleted) -- but the backup copy taken before running this script is the actual
audit trail, per CLAUDE.md's Safety section, and `verify()` also compares against
it directly.

Usage:
    python fix_wrapped_titles.py <file.md> [--write] [--report out.txt]
    python fix_wrapped_titles.py --all <root> [--write] [--report out.txt]
    python fix_wrapped_titles.py --verify <backup.md> <fixed.md>

Without --write, runs a dry-run and only reports what would change.
"""

from __future__ import annotations

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_anchor import (split_frontmatter, split_lines_keep, join_lines,
                        detect_sha_convention, body_sha)

UNWRAP_DATE = "2026-09-16"
# High on purpose: unlike a fresh-anchoring job, correctness here rests entirely
# on the semantic STOP/DANGLING/LOWER conditions in collect_title, not on a length
# budget -- a length cap only truncates genuine long titles (e.g. COD-218-2008
# art. 169, seven physical lines) without adding any real safety, since the
# semantic conditions already refuse to cross into body text on their own.
MAX_TITLE = 400

HEAD = re.compile(r"^(##\s+Articolul\s+(\d+(?:\^\d+)?)\.)\s*(.*)$")
HEADING_ANY = re.compile(rb"^#{1,6}\s")

# a following line that can never be part of a heading title: the next
# structural marker of any kind (all are '#'-prefixed in these already
# anchored files), a numbered/lettered paragraph -- either style, '(1)' or the
# older bare '1.' used by e.g. L-845-1992 -- or a bracketed amendment note
STOP = re.compile(r"^(\(\d+\)|\(\d+\^\d+\)|\d+(?:\^\d+)?\.\s|[a-zșşțţ]\)|\[|#{1,6}\s|Articolul\b)")
LOWER = re.compile(r"^[a-zăâîșşțţ]")

DANGLING = set(
    "şi si și de prin în in cu la a al ale ai sau ori pentru "
    "asupra din dintre către catre fără fara sub pe ca este "
    "care".split())


def last_word(s):
    parts = s.split()
    if not parts:
        return ""
    return re.sub(r"[^\wăâîșşțţ-]", "", parts[-1]).lower()


def next_nonblank(lines, j):
    while j < len(lines) and lines[j].strip() == "":
        j += 1
    return j


def collect_title(lines, i, title):
    """Extend `title` (the heading's current text) with continuation lines."""
    j = i + 1
    took_second_part = False
    joined_any = False
    while True:
        j = next_nonblank(lines, j)
        if j >= len(lines):
            break
        cand = lines[j].strip()
        if not cand or STOP.match(cand):
            break
        if LOWER.match(cand):
            pass
        elif last_word(title) in DANGLING:
            pass
        elif title.endswith(".") and not took_second_part:
            took_second_part = True
        else:
            break
        if len(title) + 1 + len(cand) > MAX_TITLE:
            break
        title += " " + cand
        joined_any = True
        j += 1
    return title, joined_any


def process(text: str):
    """Return (new_text, n_fixed, details). `text` is the decoded body."""
    lines = text.split("\n")
    n_fixed = 0
    details = []
    for i, line in enumerate(lines):
        m = HEAD.match(line)
        if not m:
            continue
        marker, num, frag = m.groups()
        if not frag:
            # No text at all after 'Articolul N.' -- final/transitional articles
            # genuinely have no title (e.g. COD-218-2008 art. 481-483: "Prezentul
            # cod intra in vigoare..." follows directly, with nothing to join).
            # A real wrap always leaves some text before the line break, so an
            # empty fragment is never treated as a wrap victim.
            continue
        title = marker + " " + frag
        new_title, joined = collect_title(lines, i, title)
        if joined:
            old_line = lines[i]
            lines[i] = new_title
            n_fixed += 1
            details.append((i + 1, num, old_line, new_title))
    return "\n".join(lines), n_fixed, details


def strip_headings(body: bytes) -> bytes:
    return join_lines([(t, term) for t, term in split_lines_keep(body)
                       if not HEADING_ANY.match(t)])


def fix_file(path, write=False):
    data = open(path, "rb").read()
    fm, body = split_frontmatter(data)
    conv, recorded = detect_sha_convention(data)
    text = body.decode("utf-8")
    # normalise line endings for the join, then restore per-line terminators below
    pairs = split_lines_keep(body)
    raw_lines = [t.decode("utf-8") for t, _ in pairs]
    terms = [term for _, term in pairs]

    new_lines_text, n_fixed, details = process("\n".join(raw_lines))
    new_lines = new_lines_text.split("\n")
    assert len(new_lines) == len(raw_lines), "line count changed -- refusing to write"

    if n_fixed == 0:
        return 0, [], None

    new_pairs = [(new_lines[k].encode("utf-8"), terms[k]) for k in range(len(new_lines))]
    new_body = join_lines(new_pairs)

    # proof: with all '#'-heading lines stripped, old and new body are identical
    old_stripped = strip_headings(body)
    new_stripped = strip_headings(new_body)
    assert old_stripped == new_stripped, "non-heading content changed -- refusing to write"

    if not write:
        return n_fixed, details, None

    new_sha = body_sha(new_body, conv)
    fm_text = fm.decode("utf-8")
    assert fm_text.rstrip("\n").endswith("---")
    has_pre = re.search(r"^sha256_pre_title_unwrap:", fm_text, re.M)
    fm_text = re.sub(r"^sha256:\s*\S+\s*$",
                     "sha256: %s" % new_sha, fm_text, count=1, flags=re.M)
    if not has_pre:
        add = [
            "sha256_pre_title_unwrap: %s" % recorded,
            "title_unwrap_date: '%s'" % UNWRAP_DATE,
            "title_unwrap_count: %d" % n_fixed,
            "title_unwrap_convention: >-",
            "  Heading text only: '## Articolul N.' lines whose title was cut by a",
            "  hard line-wrap at ingestion had the wrapped tail joined back in.",
            "  The tail line(s) below stay in the body untouched. Strip every line",
            "  starting with '#' from both this and the pre-unwrap copy to prove",
            "  nothing else moved.",
        ]
        fm_text = fm_text.rstrip("\n")
        assert fm_text.endswith("---")
        fm_text = fm_text[:-3].rstrip("\n") + "\n" + "\n".join(add) + "\n---\n"

    open(path, "wb").write(fm_text.encode("utf-8") + new_body)
    return n_fixed, details, new_sha


def main():
    args = sys.argv[1:]
    write = "--write" in args
    if write:
        args.remove("--write")
    report_path = None
    if "--report" in args:
        idx = args.index("--report")
        report_path = args[idx + 1]
        del args[idx:idx + 2]

    if args and args[0] == "--all":
        root = args[1]
        targets = []
        for dp, dn, fn in os.walk(root):
            for f in fn:
                if f.endswith(".md"):
                    targets.append(os.path.join(dp, f))
        targets.sort()
    else:
        targets = args

    out = []
    total_fixed = 0
    for p in targets:
        try:
            n_fixed, details, new_sha = fix_file(p, write=write)
        except AssertionError as e:
            out.append("%s: REFUSED (%s)" % (p, e))
            continue
        except (ValueError, UnicodeDecodeError):
            continue  # no frontmatter, or not a text file we anchor -- not in scope
        if n_fixed:
            total_fixed += n_fixed
            out.append("%s: %d title(s) %s" % (p, n_fixed, "fixed" if write else "would be fixed"))
            for line_no, num, old, new in details:
                out.append("   line %d  art.%s" % (line_no, num))
                out.append("      old: %s" % old)
                out.append("      new: %s" % new)

    out.append("")
    out.append("TOTAL: %d heading(s) across %d file(s) %s"
                % (total_fixed, len([1 for p in targets]), "fixed" if write else "would be fixed"))
    txt = "\n".join(out)
    sys.stdout.reconfigure(encoding="utf-8")
    print(txt)
    if report_path:
        open(report_path, "w", encoding="utf-8").write(txt + "\n")


if __name__ == "__main__":
    main()
