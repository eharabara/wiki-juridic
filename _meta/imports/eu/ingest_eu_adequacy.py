"""Ingests the 16 European Commission adequacy decisions named by CNPDCP Decision 41/2026.

Uses EU Publications Office Cellar in Romanian. The Isle of Man source uses the available
consolidated CELEX resource (02004D0411-20161217), rather than the unavailable base resource.
Run: python _meta/imports/eu/ingest_eu_adequacy.py
"""
from __future__ import annotations

import datetime as dt
import hashlib
import re
import urllib.request
from pathlib import Path

from lxml import etree

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "raw" / "papers" / "moldova-legal"
CACHE = ROOT / "_meta" / "imports" / "eu" / "cellar"
TODAY = dt.date.today().isoformat()

# The order and the referenced acts reproduce DCNPDCP-41-2026, preamble points 1–16.
ACTS = (
    ("UE-2010-625", "32010D0625", "32010D0625", "Andorra"),
    ("UE-2003-490", "32003D0490", "32003D0490", "Argentina"),
    ("UE-2002-2", "32002D0002", "32002D0002", "Canada"),
    ("UE-2010-146", "32010D0146", "32010D0146", "Insulele Feroe"),
    ("UE-2003-821", "32003D0821", "32003D0821", "Guernsey"),
    ("UE-2011-61", "32011D0061", "32011D0061", "Israel"),
    ("UE-2004-411", "32004D0411", "02004D0411-20161217", "Insula Man"),
    ("UE-2019-419", "32019D0419", "32019D0419", "Japonia"),
    ("UE-2008-393", "32008D0393", "32008D0393", "Jersey"),
    ("UE-2013-65", "32013D0065", "32013D0065", "Noua Zeelandă"),
    ("UE-2022-254", "32022D0254", "32022D0254", "Republica Coreea"),
    ("UE-2000-518", "32000D0518", "32000D0518", "Elveția"),
    ("UE-2012-484", "32012D0484", "32012D0484", "Uruguay"),
    ("UE-2021-1772", "32021D1772", "32021D1772", "Regatul Unit"),
    ("UE-2026-179", "32026D0179", "32026D0179", "Brazilia"),
    ("UE-2025-1382", "32025D1382", "32025D1382", "Organizația Europeană de Brevete"),
)


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def fetch(resource_celex: str) -> bytes:
    CACHE.mkdir(parents=True, exist_ok=True)
    cache = CACHE / f"{resource_celex}.xhtml"
    if not cache.exists() or not cache.stat().st_size:
        request = urllib.request.Request(
            f"https://publications.europa.eu/resource/celex/{resource_celex}",
            headers={
                "User-Agent": "Mozilla/5.0",
                "Accept": "application/xhtml+xml",
                "Accept-Language": "ron",
            },
        )
        with urllib.request.urlopen(request, timeout=180) as response:
            cache.write_bytes(response.read())
    return cache.read_bytes()


def body_text(xhtml: bytes) -> str:
    document = etree.fromstring(xhtml)
    body = document.xpath("//*[local-name()='body']")
    if not body:
        raise ValueError("XHTML without body")
    # Paragraph-level preservation maintains reading order and table text without rewriting legal text.
    blocks = body[0].xpath(
        ".//*[local-name()='p' or local-name()='h1' or local-name()='h2' or "
        "local-name()='h3' or local-name()='h4' or local-name()='li' or local-name()='td']"
    )
    parts: list[str] = []
    for block in blocks:
        text = norm("".join(block.itertext()))
        if text and (not parts or text != parts[-1]):
            parts.append(text)
    result = "\n\n".join(parts).strip() + "\n"
    if len(result) < 1000:
        raise ValueError(f"suspiciously short legal extraction: {len(result)} chars")
    return result


def title(text: str) -> str:
    for paragraph in text.split("\n\n"):
        if "DECIZ" in paragraph.upper() and len(paragraph) > 30:
            return paragraph[:700]
    return text.split("\n\n", 1)[0][:700]


def write(stem: str, base_celex: str, resource_celex: str, place: str) -> tuple[Path, int]:
    xhtml = fetch(resource_celex)
    text = body_text(xhtml)
    raw_body = (
        f"# raw/{stem} — decizia Comisiei privind caracterul adecvat: {place}\n\n"
        "> **TEXT OFICIAL UE.** Act enumerat expres în preambulul "
        "[[DCNPDCP-41-2026]], pct. corespunzător din lista celor 16 evaluări de adecvare. "
        "Textul este extras din resursa Cellar în română; nu se deduce din această păstrare, singură, "
        "statutul juridic al unor modificări sau revizuiri ulterioare.\n\n"
        "## Text extras din Cellar\n\n"
        f"{text}"
    )
    source_url = f"https://publications.europa.eu/resource/celex/{resource_celex}"
    eurlex_url = f"https://eur-lex.europa.eu/legal-content/RO/TXT/?uri=CELEX:{base_celex}"
    meta = "\n".join((
        "---",
        f"source_url: {source_url}",
        f"eurlex_url: {eurlex_url}",
        f"ingested: '{TODAY}'",
        f"sha256: {hashlib.sha256(raw_body.encode()).hexdigest()}",
        "sha256_convention: LF",
        f"source_file_sha256: {hashlib.sha256(xhtml).hexdigest()}",
        f"source_file_bytes: {len(xhtml)}",
        "source_type: legal-text",
        "publisher: Publications Office of the European Union / European Commission",
        "language: ro",
        f"celex: {base_celex}",
        f"cellar_resource_celex: {resource_celex}",
        f"instrument_id: {stem}",
        f"official_title_detected: {title(text)}",
        "full_text: true",
        "extract_method: 'Cellar XHTML, paragrafe și celule de tabel în ordinea documentului; fără rescriere de fond'",
        "---",
        "",
    ))
    output = OUT / f"{stem}.md"
    output.write_text(meta + raw_body, encoding="utf-8", newline="\n")
    return output, len(text)


if __name__ == "__main__":
    results = [write(*spec) for spec in ACTS]
    for path, chars in results:
        print(f"{path.relative_to(ROOT)}: {chars} chars")
    print(f"ingested: {len(results)}")
