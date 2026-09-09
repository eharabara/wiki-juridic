"""Verificare dupa ingerarea actelor subordonate CNPF (ingest_cnpf_ro.py). GENERAT din
_meta/imports/bnm/verify_bnm_ro.py la 2026-09-09, cu trei inlocuiri: DOCS din ingest_cnpf_ro.py,
RAW = raw/papers/cnpf, META = _meta/imports/cnpf/legis-md-consolidated. Testul de fond este acelasi:
se scot liniile de structura adaugate si restul se compara linie cu linie cu extractia simpla din
acelasi HTML.
"""
import importlib.util, io, re, sys
from pathlib import Path
from lxml import html

ROOT = Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location(
    "ibl", str(ROOT / "_meta" / "imports" / "moldova-legal" / "ingest_business_law.py"))
ibl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ibl)
_w = importlib.util.spec_from_file_location("w", str(Path(__file__).parent / "ingest_cnpf_ro.py"))
w = importlib.util.module_from_spec(_w)
_w.loader.exec_module(w)

RAW = w.RAW_DIR
META = w.META_DIR

fail = 0
for stem, doc in w.DOCS.items():
    print(f"\n{'=' * 74}\n{stem}  (doc_id {doc['doc_id']})\n{'=' * 74}")
    md = io.open(RAW / f"{stem}.md", encoding='utf-8').read()

    raw_html = io.open(META / f"showdetails-{doc['doc_id']}.html", encoding='utf-8',
                       errors='replace').read()
    resolved = ibl.resolve_superscripts(raw_html)
    content = html.fromstring(resolved).xpath('//*[@id="contentdoc"]')[0]
    reference = [x for x in (ibl.clean_line(x) for x in content.text_content().splitlines()) if x]

    marker = '## Text integral extras din legis.md'
    body = md.split(marker, 1)[1]
    written = []
    for line in body.split('\n'):
        line = line.strip()
        if not line:
            continue
        written.append(re.sub(r'^#{2,3}\s+', '', line))

    same = written == reference
    print(f"  text integrity          : {'PASS' if same else 'FAIL'} "
          f"({len(written)} lines written vs {len(reference)} reference)")
    if not same:
        fail += 1
        for i, (a, b) in enumerate(zip(written, reference)):
            if a != b:
                print(f"    first divergence at {i}:\n      written  : {a[:110]!r}\n"
                      f"      reference: {b[:110]!r}")
                break

    body_only = md.split('---', 2)[2] if md.count('---') >= 2 else md
    leftover = '<sup' in body_only.lower()
    print(f"  no <sup> markup left    : {'PASS' if not leftover else 'FAIL'}")
    fail += leftover

    sup_anchors = re.findall(r'^## Articolul (\d+\^\d+(?:/\d+)?)', md, re.M)
    _sup = re.compile(r'Articolul(?:\s|&nbsp;|<[^>]*>)*(\d+)<sup>(.*?)</sup>(/\d+)?', re.S)
    _found = set()
    for a, b, c in _sup.findall(raw_html):
        inner = ibl.ihtml.unescape(re.sub(r'<[^>]*>', '', b)).replace(chr(160), ' ').strip()
        m = re.match(r'(\d+)', inner)
        if m:
            _found.add(f"{a}^{m.group(1)}{c}")
    match = sorted(sup_anchors) == sorted(_found)
    print(f"  superscript articles    : {'PASS' if match else 'FAIL'}  "
          f"{len(sup_anchors)} anchored -> {', '.join(sup_anchors)}")
    if not match:
        fail += 1
        print(f"    source expects: {', '.join(sorted(_found))}")

    body_carets = len(re.findall(r'\(\d+\^\d+\)', md)) + len(re.findall(r'[a-z]\^\d+\)', md))
    print(f"  body-level ^N kept      : {body_carets} occurrences (alineate, litere, puncte)")

    plain = [int(x) for x in re.findall(r'^## Articolul (\d+)(?=[.\s]|$)', md, re.M)]
    dupes = sorted({n for n in plain if plain.count(n) > 1})
    gaps = [n for n in range(1, max(plain) + 1) if n not in plain] if plain else []
    print(f"  plain articles          : {len(plain)}  range 1-{max(plain) if plain else 0}")
    print(f"  duplicates              : {dupes if dupes else 'none'}")
    print(f"  numbering gaps          : {gaps if gaps else 'none'}")

    fm = md.split('---', 2)[1]
    for key in ('doc_id', 'consolidation_date', 'sha256', 'instrument_id', 'superscript_articles'):
        if re.search(rf'^{key}:', fm, re.M) is None:
            print(f"  frontmatter MISSING     : {key}")
            fail += 1
    dc = re.search(r'^doc_id:\s*[\'"]?(\d+)', fm, re.M)
    print(f"  frontmatter doc_id      : {dc.group(1) if dc else '?'} "
          f"({'PASS' if dc and dc.group(1) == doc['doc_id'] else 'FAIL'})")

print(f"\n{'=' * 74}\nFAILURES: {fail}\n{'=' * 74}")
sys.exit(1 if fail else 0)
