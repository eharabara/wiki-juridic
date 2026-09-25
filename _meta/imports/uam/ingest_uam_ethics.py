"""Ingest the Union of Lawyers' official ethics-code PDF with a reproducible source check.

The source is the PDF linked from the Union's current ``Cadrul legal`` page.  It is
not on legis.md, so the PDF itself is retained under ``source/`` and is the immutable
comparison target.  The text is deliberately left without synthetic legal anchors:
its internal numbering is chapter/point based and citations remain unanchored.

Run:
  python _meta/imports/uam/ingest_uam_ethics.py --precheck
  python _meta/imports/uam/ingest_uam_ethics.py
  python _meta/imports/uam/ingest_uam_ethics.py --verify
"""
from __future__ import annotations

import datetime
import hashlib
import re
import sys
from pathlib import Path

import fitz
import yaml


ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "_meta" / "imports" / "uam" / "source" / "codul_deontologic_5358927.pdf"
OUT = ROOT / "raw" / "papers" / "moldova-legal" / "UA-COD-DEONTOLOGIC-2016.md"
SOURCE_PAGE = "https://uam.md/despre-noi/cadrul-legal/"
SOURCE_URL = "https://uam.md/wp-content/uploads/2024/02/codul_deontologic_5358927.pdf"
MARKER = "## Text integral extras din PDF (uam.md)"
TITLE = "Codul deontologic al avocaților din Republica Moldova"


def source_lines() -> tuple[int, list[str]]:
    doc = fitz.open(SOURCE)
    try:
        lines = [line.strip() for page in doc for line in page.get_text().split("\n") if line.strip()]
        return doc.page_count, lines
    finally:
        doc.close()


def body_hash(markdown: str) -> str:
    closing = re.search(r"^---\s*$", markdown[3:], re.M)
    assert closing, "frontmatter closing fence absent"
    body = markdown[3 + closing.end():]
    return hashlib.sha256(body.encode("utf-8")).hexdigest()


def extraction_hash(lines: list[str]) -> str:
    return hashlib.sha256(("\n".join(lines) + "\n").encode("utf-8")).hexdigest()


def build() -> str:
    pages, lines = source_lines()
    source_sha = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    metadata = {
        "source_url": SOURCE_URL,
        "source_page": SOURCE_PAGE,
        "ingested": datetime.date.today().isoformat(),
        "sha256": "x",
        "sha256_extraction": extraction_hash(lines),
        "source_file": SOURCE.relative_to(ROOT).as_posix(),
        "source_file_sha256": source_sha,
        "source_type": "legal-text",
        "publisher": "Uniunea Avocaților din Republica Moldova (uam.md)",
        "language": "ro",
        "instrument_id": "UA-COD-DEONTOLOGIC-2016",
        "official_title_detected": TITLE,
        "adoption_history": "Congresul Avocaților: 20.12.2002; modificări 23.03.2007 și 01.07.2016",
        "full_text": True,
        "extract_method": "PyMuPDF get_text() pagină cu pagină; spații de capăt și linii goale eliminate; fără ancore sintetice",
        "pages": pages,
    }
    header = [
        f"# raw/UA-COD-DEONTOLOGIC-2016 — {TITLE}",
        "",
        "> **TEXT UAM.MD RO — extras din PDF-ul oficial legat de pagina curentă «Cadrul legal» a Uniunii Avocaților și păstrat pentru audit.** Nu corectez și nu armonizez tăcut textul. Fără ancore sintetice: structura este pe capitole și puncte, iar citarea pe punct nu este ancorată.",
        "",
        f"- **Pagina de referință:** {SOURCE_PAGE}",
        f"- **Fișier-sursă:** {SOURCE_URL} ({SOURCE.stat().st_size} octeți, sha256 `{source_sha}`), arhivat la `{SOURCE.relative_to(ROOT).as_posix()}`",
        "- **Statut de publicare:** pagina oficială îl prezintă ca parte a cadrului legal al profesiei; textul PDF indică adoptarea de Congres și modificările din 2007 și 2016. O hotărâre de adoptare ori o consolidare ulterioară nu este publicată cu acest fișier și nu se presupune.",
        "- **articole detectate:** 0; structură pe capitole și puncte, fără ancore de articol.",
        f"- **pagini PDF:** {pages}; **linii nevide extrase:** {len(lines)}",
        "",
        MARKER,
        "",
    ]
    body = "\n".join(header + lines).strip() + "\n"
    frontmatter = yaml.safe_dump(metadata, allow_unicode=True, sort_keys=False).strip()
    markdown = f"---\n{frontmatter}\n---\n\n{body}"
    return re.sub(r"^sha256:\s*\S+", f"sha256: {body_hash(markdown)}", markdown, count=1, flags=re.M)


def verify() -> int:
    if not OUT.exists():
        print(f"FAIL: lipseste {OUT.relative_to(ROOT)}")
        return 1
    pages, lines = source_lines()
    markdown = OUT.read_text(encoding="utf-8")
    frontmatter = yaml.safe_load(markdown.split("---", 2)[1])
    failures = 0
    checks = {
        "pdf sha256": frontmatter["source_file_sha256"] == hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "sha256 extraction": frontmatter["sha256_extraction"] == extraction_hash(lines),
        "sha256 body": frontmatter["sha256"] == body_hash(markdown),
        "pages": frontmatter["pages"] == pages,
    }
    written = [line for line in markdown.split(MARKER, 1)[1].split("\n") if line]
    checks["text integrity"] = written == lines
    checks["article anchors"] = not re.search(r"^## Articolul ", markdown, re.M)
    for name, ok in checks.items():
        print(f"{name:20}: {'PASS' if ok else 'FAIL'}")
        failures += not ok
    if written != lines:
        for index, (actual, expected) in enumerate(zip(written, lines), start=1):
            if actual != expected:
                print(f"prima divergență, linia {index}: {actual!r} != {expected!r}")
                break
    print(f"FAILURES: {failures}")
    return failures


def main() -> None:
    if "--verify" in sys.argv:
        raise SystemExit(verify())
    pages, lines = source_lines()
    print(f"pagini={pages}; linii={len(lines)}; sha256 PDF={hashlib.sha256(SOURCE.read_bytes()).hexdigest()}")
    if "--precheck" not in sys.argv:
        OUT.write_text(build(), encoding="utf-8", newline="\n")
        print(f"scris: {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
