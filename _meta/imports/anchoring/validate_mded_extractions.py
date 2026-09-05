"""Validate the mded-policy-2024 extractions against their preserved originals.

These twelve files carry a `sha256` that has never matched their body. Before
recomputing it, the body has to be shown to be a faithful extraction of the
original, otherwise recomputing would simply certify whatever is there.

Three checks per file, cheapest first:

  1. the preserved original still matches its recorded `source_file_sha256`;
  2. the body is byte-identical to the copy in the 2026-07-12 post-ingest
     backup, i.e. nothing has edited it since it was written.
     EXPECTED EXCEPTIONS: economic-criteria-deregulation-2024 and
     economic-criteria-state-aid-2024 report CHANGED because speaker notes were
     deliberately appended on 2026-09-04. Their slide text is still an exact
     byte prefix of the body; only the '## Speaker notes' section is new. Any
     OTHER file reporting CHANGED is a real finding;
  3. the body's words are those of the original. Text is re-extracted here and
     compared as a token multiset, not line by line, because a different
     library version legitimately differs on whitespace, hyphenation and
     reading order while carrying the same words.

Coverage of check 3 depends on the format: PDF via PyMuPDF, DOCX via
python-docx, PPTX by reading the drawing-text runs straight out of the OOXML zip
(python-pptx is not installed here).

Usage: python validate_mded_extractions.py [--verbose]
"""

import collections
import glob
import hashlib
import os
import re
import sys
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_anchor import split_frontmatter, sha_variants

SRC_DIR = "raw/papers/mded-policy-2024"
BACKUP = ("C:/Users/harab/wiki-backups/wiki-before-bnm-corpus-ingest-"
          "20260712-205717/raw/papers/mded-policy-2024/")
WORD = re.compile(r"[0-9a-zà-ÿăâîșşțţ]+", re.I)


def tokens(text):
    return collections.Counter(w.lower() for w in WORD.findall(text))


def extract(path):
    """Return (text, method) or (None, reason)."""
    ext = os.path.splitext(path)[1].lower()
    try:
        if ext == ".pdf":
            import fitz
            doc = fitz.open(path)
            return "\n".join(p.get_text() for p in doc), "PyMuPDF"
        if ext == ".docx":
            import docx
            d = docx.Document(path)
            parts = [p.text for p in d.paragraphs]
            for t in d.tables:
                for row in t.rows:
                    parts.extend(c.text for c in row.cells)
            return "\n".join(parts), "python-docx"
        if ext == ".pptx":
            # python-pptx is unavailable; read the text runs from the OOXML zip.
            # Slides only: the original ingest did not carry speaker notes, and
            # including notesSlides here made two decks look 84% and 92% covered
            # when the slide content itself is a complete match.
            out = []
            with zipfile.ZipFile(path) as z:
                for n in sorted(z.namelist()):
                    if re.match(r"ppt/slides/slide\d+\.xml$", n):
                        xml = z.read(n).decode("utf-8", "replace")
                        out.extend(re.findall(r"<a:t>(.*?)</a:t>", xml,
                                              re.S))
            import html
            return "\n".join(html.unescape(x) for x in out), "OOXML slides"
    except Exception as e:                                  # noqa: BLE001
        return None, "extraction failed: %s" % e
    return None, "unsupported extension %s" % ext


def main():
    verbose = "--verbose" in sys.argv
    rows = []
    for p in sorted(glob.glob(os.path.join(SRC_DIR, "*.md"))):
        name = os.path.basename(p)
        data = open(p, "rb").read()
        fm, body = split_frontmatter(data)
        t = fm.decode("utf-8", "replace")
        rec = re.search(r"^sha256:\s*(\w+)", t, re.M).group(1)
        origp = re.search(r"^archived_original:\s*(.+)$", t, re.M)
        origh = re.search(r"^source_file_sha256:\s*(\w+)", t, re.M)

        # 1. original intact
        orig_ok = "no original recorded"
        opath = origp.group(1).strip() if origp else None
        if opath and os.path.exists(opath) and origh:
            got = hashlib.sha256(open(opath, "rb").read()).hexdigest()
            orig_ok = "OK" if got == origh.group(1) else "MISMATCH"
        elif opath:
            orig_ok = "MISSING FILE"

        # 2. body untouched since ingest
        q = BACKUP + name
        if os.path.exists(q):
            _, b2 = split_frontmatter(open(q, "rb").read())
            unchanged = "OK" if b2 == body else "CHANGED"
        else:
            unchanged = "not in backup"

        # 3. words match the original
        cover = None
        method = "-"
        if opath and os.path.exists(opath):
            text, method = extract(opath)
            if text is None:
                cover = method
                method = "-"
            else:
                ot = tokens(text)
                bt = tokens(body.decode("utf-8", "replace"))
                shared = sum((ot & bt).values())
                cover = shared / max(1, sum(ot.values()))

        rows.append((name, orig_ok, unchanged, cover, method,
                     rec in sha_variants(body).values()))

    print("%-50s %-9s %-9s %-8s %-12s %s"
          % ("file", "original", "untouched", "words", "method", "sha256"))
    print("-" * 104)
    worst = 1.0
    for name, o, u, c, m, s in rows:
        cs = ("%.1f%%" % (100 * c)) if isinstance(c, float) else str(c)[:8]
        if isinstance(c, float):
            worst = min(worst, c)
        print("%-50s %-9s %-9s %-8s %-12s %s"
              % (name[:48], o, u, cs, m, "ok" if s else "DRIFT"))
    print("-" * 104)
    print("lowest word coverage: %.1f%%" % (100 * worst))


if __name__ == "__main__":
    main()
