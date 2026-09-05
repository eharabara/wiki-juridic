"""Append the presenter's notes to a PPTX-derived extraction.

The 2026-07-12 ingest captured slide text only, so any substance the presenter
put in the notes pane never entered the wiki. For the bilateral-screening decks
that matters: one note carries the state-aid series' comparability caveat, which
changes how the figures on the slide itself may be read.

The notes are appended under their own heading, never merged into the slide
text, so a reader can always tell what was on the slide from what was said
beside it. Slide text is not touched.

Empty notes panes are skipped: PowerPoint writes a notesSlide part for every
slide whether or not anything was typed into it, so presence of the part means
nothing on its own.

Usage: python add_pptx_speaker_notes.py <file.md> [--apply]
"""

import html
import os
import re
import sys
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_anchor import split_frontmatter, sha_variants

NOTES_DATE = "2026-09-04"
NOTE_PART = re.compile(r"ppt/notesSlides/notesSlide(\d+)\.xml$")
RUN = re.compile(r"<a:t>(.*?)</a:t>", re.S)


def real_content(text):
    """PowerPoint leaves the slide number behind in an otherwise empty pane."""
    return len(re.sub(r"[\s\d]", "", text)) > 3


def read_notes(pptx):
    out = []
    with zipfile.ZipFile(pptx) as z:
        parts = sorted(
            (int(NOTE_PART.search(n).group(1)), n)
            for n in z.namelist() if NOTE_PART.search(n))
        for num, name in parts:
            xml = z.read(name).decode("utf-8", "replace")
            text = " ".join(html.unescape(r) for r in RUN.findall(xml))
            text = re.sub(r"\s+", " ", text).strip()
            # the pane usually ends with the bare slide number; drop it
            text = re.sub(r"\s*\b%d\s*$" % num, "", text).strip()
            if real_content(text):
                out.append((num, text))
    return out


def main():
    path = sys.argv[1]
    apply_ = "--apply" in sys.argv

    data = open(path, "rb").read()
    fm, body = split_frontmatter(data)
    fmt = fm.decode("utf-8")
    orig = re.search(r"^archived_original:\s*(.+)$", fmt, re.M).group(1).strip()
    notes = read_notes(orig)

    print("%s" % os.path.basename(path))
    print("   original : %s" % os.path.basename(orig))
    print("   notes with content: %d" % len(notes))
    for n, t in notes:
        print("      slide %-3d %d chars" % (n, len(t)))
    if not notes:
        print("   nothing to add -- every notes pane is empty")
        return 0
    if re.search(r"^## Speaker notes", body.decode("utf-8"), re.M):
        print("   already present -- not adding again")
        return 0

    nl = "\r\n" if b"\r\n" in body else "\n"
    block = [
        "", "## Speaker notes",
        "",
        "Presenter's notes from the source deck, extracted %s. The 2026-07-12"
        % NOTES_DATE,
        "ingest captured slide text only. These are what was said alongside the"
        " slides,",
        "not what was shown on them, and are kept separate for that reason."
        " Slide text",
        "above is unchanged.",
        "",
    ]
    for n, t in notes:
        block += ["### Notes to slide %d" % n, "", t, ""]
    new_body = body + nl.join(block).encode("utf-8") + nl.encode("utf-8")

    prev = re.search(r"^sha256: (\w+)", fmt, re.M).group(1)
    assert "sha256_pre_notes" not in fmt, "already carries sha256_pre_notes"
    conv = "LF" if body.count(b"\r\n") == 0 else "raw"
    new_sha = sha_variants(new_body)[conv]
    fmt2 = re.sub(r"^sha256: .*$", "sha256_pre_speaker_notes: %s" % prev, fmt,
                  count=1, flags=re.M)
    add = [
        "sha256: %s" % new_sha,
        "speaker_notes_added: '%s'" % NOTES_DATE,
        "speaker_notes_convention: >-",
        "  The presenter's notes were absent from the 2026-07-12 ingest, which",
        "  read slide text only. They are appended under '## Speaker notes' and",
        "  never merged into the slide text. Slides with an empty notes pane are",
        "  skipped. Slide text above the heading is byte-identical to the",
        "  original extraction (sha256_pre_speaker_notes).",
    ]
    fnl = "\r\n" if "\r\n" in fmt2 else "\n"
    fmt2 = fmt2.rstrip("\r\n")
    assert fmt2.endswith("---")
    fmt2 = (fmt2[:-3].rstrip("\r\n") + fnl + fnl.join(add) + fnl + "---" + fnl)

    print("   slide text : %d bytes (unchanged)" % len(body))
    print("   notes added: %d bytes" % (len(new_body) - len(body)))
    print("   sha256     : %s -> %s" % (prev[:16], new_sha[:16]))
    if not apply_:
        print("   dry run -- pass --apply to write")
        return 0

    open(path, "wb").write(fmt2.encode("utf-8") + new_body)
    d2 = open(path, "rb").read()
    f2, b2 = split_frontmatter(d2)
    assert b2.startswith(body), "slide text changed -- aborting"
    rec = re.search(rb"^sha256:\s*(\w+)", f2, re.M).group(1).decode()
    ok = rec in sha_variants(b2).values()
    print("   verified   : %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
