"""Verificare dupa ingerarea actelor CNPDCP. GENERAT din
_meta/imports/bnm/verify_bnm_ro.py la 2026-09-24, cu trei inlocuiri: DOCS din
ingest_cnpdcp_ro.py, RAW = raw/papers/moldova-legal, META = _meta/imports/cnpdcp/legis-md.
Testul de fond este acelasi: se scot liniile de structura adaugate si restul se compara
linie cu linie cu extractia simpla din acelasi HTML.
"""

import importlib.util, io, re
from pathlib import Path
from lxml import html

spec = importlib.util.spec_from_file_location(
    "ibl", str(Path(__file__).parents[1] / "moldova-legal" / "ingest_business_law.py"))
_w = importlib.util.spec_from_file_location("w", str(Path(__file__).parent / "ingest_cnpdcp_ro.py"))
w = importlib.util.module_from_spec(_w)
_w.loader.exec_module(w)
ibl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ibl)

RAW = w.RAW_DIR
META = w.META_DIR

fail = 0
for stem, doc in w.DOCS.items():
    md_path = RAW / f"{stem}.md"
    if not md_path.exists():
        print(f"\n{stem}: SARIT (neingerat inca)")
        continue
    print(f"\n{'=' * 74}\n{stem}  (doc_id {doc['doc_id']})\n{'=' * 74}")
    md = io.open(md_path, encoding='utf-8').read()

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

print(f"\n{'=' * 74}\nFAILURES: {fail}\n{'=' * 74}")
