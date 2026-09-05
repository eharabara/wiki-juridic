"""Job 1 -- anchor CC-1107-2002 (Codul civil) to article level.

Method: heading lines are INSERTED above the original lines. No existing line is
modified, reordered or re-wrapped, so the body stays byte-identical and the
strip-and-compare check reduces to "remove every line starting with '#'".
The source file contains zero '#' lines, which makes that check exact.

Usage:  python anchor_cc.py <src.md> <dst.md> [--report report.txt]
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_anchor import (split_frontmatter, split_lines_keep, join_lines,
                        detect_sha_convention, body_sha)

ANCHOR_DATE = "2026-09-04"
MAX_TITLE = 200
REPORT_OVER = 150

ART = re.compile(r"^Articolul\s+(\d+)\.\s")
# both diacritic encodings occur in this PDF extraction (cedilla and comma-below)
CARTEA = re.compile(r"^Cartea\b")
TITLUL = re.compile(r"^T\s+i\s+t\s+l\s+u\s+l\b")
CAPITOLUL = re.compile(r"^Capitolul\b")
SECTIUNEA = re.compile(r"^Sec[ţț]iunea\b")
SUBSECTIUNEA = re.compile(r"^Subsec[ţț]iunea\b")
PARAGRAF = re.compile(r"^§")

STRUCT = [(SUBSECTIUNEA, "subsectiunea"), (SECTIUNEA, "sectiunea"),
          (CAPITOLUL, "capitolul"), (TITLUL, "titlul"), (CARTEA, "cartea"),
          (PARAGRAF, "paragraf")]

# a following line that can never be part of a heading title
STOP = re.compile(r"^(\(\d+\)|\(\d+\^\d+\)|[a-zșşțţ]\)|\[|"
                  r"Articolul\b|Cartea\b|Capitolul\b|Sec[ţț]iunea\b|"
                  r"Subsec[ţț]iunea\b|T\s+i\s+t\s+l\s+u\s+l\b|§)")
LOWER = re.compile(r"^[a-zăâîșşțţ]")

# words that leave a title grammatically unfinished, so the next line continues
# it even when that line starts with a capital (e.g. art. 305 -> "Republicii Moldova")
DANGLING = set(
    "şi si și de prin în in cu la a al ale ai sau ori pentru "
    "asupra din dintre către catre fără fara sub pe ca este "
    "care".split())


# Hand-corrected headings, agreed 2026-09-04.
#
# The PyMuPDF extraction merged the tail of an article title and the head of its
# body onto ONE physical line, so no line-based rule can find the boundary:
#
#   9428  Articolul 723. Dispoziții generale cu privire la drepturile
#   9429  și obligațiile părților
#   9430  la contractul de gaj Debitorul gajist și creditorul gajist sînt liberi ...
#
# Only the inserted heading is corrected; line 9430 stays byte-identical. A scan
# of all 2,657 collected titles for this signature found no other instance.
HAND_CORRECTIONS = {
    723: "Articolul 723. Dispoziții generale cu privire la drepturile "
         "și obligațiile părților la contractul de gaj",
}


def norm_marker(text):
    """Collapse PDF letter-spacing in an inserted anchor (source line untouched)."""
    return re.sub(r"^T\s+i\s+t\s+l\s+u\s+l\b", "Titlul", text)


def next_nonblank(lines, j):
    while j < len(lines) and lines[j].strip() == "":
        j += 1
    return j


def last_word(s):
    parts = s.split()
    if not parts:
        return ""
    return re.sub(r"[^\wăâîșşțţ-]", "",
                  parts[-1]).lower()


def collect_article_title(lines, i):
    """Join hard-wrapped continuation lines onto the 'Articolul N.' line."""
    title = lines[i].strip()
    j = i + 1
    took_second_part = False
    while True:
        j = next_nonblank(lines, j)
        if j >= len(lines):
            break
        cand = lines[j].strip()
        if STOP.match(cand):
            break
        if LOWER.match(cand):
            pass                                    # mid-phrase wrap
        elif last_word(title) in DANGLING:
            pass                                    # phrase grammatically open
        elif title.endswith(".") and not took_second_part:
            took_second_part = True                 # two-sentence title
        else:
            break                                   # body text -> stop
        if len(title) + 1 + len(cand) > MAX_TITLE:
            break
        title += " " + cand
        j += 1
    return title


def collect_struct_title(lines, i, limit=4):
    """Title of a structural marker sits on the following line(s)."""
    parts = []
    j = i + 1
    while len(parts) < limit:
        j = next_nonblank(lines, j)
        if j >= len(lines):
            break
        cand = lines[j].strip()
        if STOP.match(cand) or any(rx.match(cand) for rx, _ in STRUCT):
            break
        parts.append(cand)
        j += 1
    return " ".join(parts)


def build(lines):
    """Return (out, stats, long_headings). lines: str without terminators."""
    out = []          # list of (text, is_inserted)
    stats = {"articles": 0, "cartea": 0, "titlul": 0, "capitolul": 0,
             "sectiunea": 0, "subsectiunea": 0, "paragraf": 0}
    long_headings = []
    corrected = []

    for i, line in enumerate(lines):
        heading = None
        m = ART.match(line)
        if m:
            title = collect_article_title(lines, i)
            fix = HAND_CORRECTIONS.get(int(m.group(1)))
            if fix is not None:
                # fail loudly if the source ever changes under a stale correction
                assert title.startswith(fix), (
                    "hand correction for art. %s no longer matches the "
                    "extracted title:\n  collected: %r\n  correction: %r"
                    % (m.group(1), title, fix))
                title = fix
                corrected.append((i, title))
            heading = "## " + title
            stats["articles"] += 1
        else:
            for rx, kind in STRUCT:
                if rx.match(line):
                    if kind == "paragraf":
                        heading = "##### " + line.strip()
                    elif kind in ("cartea", "capitolul", "titlul"):
                        # brief's convention: marker only, title stays in body
                        heading = "## " + norm_marker(line.strip())
                    else:
                        lvl = "###" if kind == "sectiunea" else "####"
                        t = collect_struct_title(lines, i)
                        base = line.strip()
                        heading = "%s %s%s" % (lvl, base, (". " + t) if t else "")
                        if len(heading) > MAX_TITLE:
                            heading = heading[:MAX_TITLE].rstrip()
                    stats[kind] += 1
                    break
        if heading is not None:
            if len(heading) > REPORT_OVER:
                long_headings.append((i, heading))
            out.append((heading, True))
        out.append((line, False))
    return out, stats, long_headings, corrected


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
    terms = [term for _, term in pairs]
    body_term = b"\r\n" if terms.count(b"\r\n") >= terms.count(b"\n") else b"\n"

    out, stats, long_headings, corrected = build(lines)

    # re-emit, preserving each original line's own terminator
    new_pairs = []
    orig_idx = 0
    for text, inserted in out:
        if inserted:
            new_pairs.append((text.encode("utf-8"), body_term))
        else:
            new_pairs.append((pairs[orig_idx][0], pairs[orig_idx][1]))
            orig_idx += 1
    assert orig_idx == len(pairs), "line accounting mismatch"
    new_body = join_lines(new_pairs)

    # --- frontmatter surgery -------------------------------------------------
    fm_text = fm.decode("utf-8")
    new_sha = body_sha(new_body, conv)

    fm_text = re.sub(r"^sha256: .*$",
                     "sha256_pre_anchoring: %s" % recorded, fm_text, count=1,
                     flags=re.M)
    add = [
        "sha256: %s" % new_sha,
        "sha256_convention: %s" % conv,
        "articole detectate: %d" % stats["articles"],
        "anchoring_date: '%s'" % ANCHOR_DATE,
        "anchor_convention: >-",
        "  Headings inserted above the original lines; no source line altered.",
        "  Articles at '## Articolul N. <title>'; Cartea/Titlul/Capitolul at '##';",
        "  Sectiunea at '###'; Subsectiunea at '####'; paragraf-sign at '#####'.",
        "  Hard-wrapped titles are joined into the inserted heading only; the body",
        "  stays hard-wrapped. Strip every line starting with '#' to recover the",
        "  pre-anchoring body byte-for-byte.",
    ]
    fm_text = fm_text.rstrip("\n")
    assert fm_text.endswith("---")
    fm_text = fm_text[:-3].rstrip("\n") + "\n" + "\n".join(add) + "\n---\n"

    open(dst, "wb").write(fm_text.encode("utf-8") + new_body)

    o = []
    p = o.append
    p("source            : %s" % src)
    p("output            : %s" % dst)
    p("sha256 convention : %s" % conv)
    p("sha256 pre        : %s" % recorded)
    p("sha256 post       : %s" % new_sha)
    p("")
    p("headings inserted:")
    for k in ["cartea", "titlul", "capitolul", "sectiunea", "subsectiunea",
              "paragraf", "articles"]:
        p("   %-14s %d" % (k, stats[k]))
    p("   %-14s %d" % ("TOTAL", sum(stats.values())))
    p("")
    p("hand-corrected headings: %d" % len(corrected))
    for i, h in corrected:
        p("   line %6d %s" % (i, h))
    p("")
    p("headings longer than %d chars: %d" % (REPORT_OVER, len(long_headings)))
    for i, h in long_headings:
        p("   line %6d (%3d chars) %s" % (i, len(h), h))
    txt = "\n".join(o)
    print(txt)
    if report_path:
        open(report_path, "w", encoding="utf-8").write(txt + "\n")


if __name__ == "__main__":
    main()
