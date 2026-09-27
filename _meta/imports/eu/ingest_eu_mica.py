"""Ingerarea Regulamentului (UE) 2023/1114 (MiCA, piata criptoactivelor) in romana, TEXT INTEGRAL
(articole si considerente), din Cellar (publications.europa.eu), in raw/papers/moldova-legal/.
Creat 2026-09-27, pentru comparatia termen cu termen cu L-180-2026 (Legea 180/2026 privind piata
criptoactivelor), ramasa deschisa in entities/L-180-2026.md.

Acelasi model ca _meta/imports/eu/ingest_eu_dataprotection.py (GDPR): text integral, nu extras,
pentru ca orice concluzie de divergenta trebuie citita la sursa.

Sursa: GET https://publications.europa.eu/resource/celex/<CELEX> cu Accept: application/xhtml+xml
si Accept-Language: ron (pagina EUR-Lex propriu-zisa da 202 fara corp).

Rulare:  python _meta/imports/eu/ingest_eu_mica.py
"""
import hashlib, re, sys, urllib.request, datetime
from pathlib import Path
from lxml import etree

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'raw' / 'papers' / 'moldova-legal'
CACHE = ROOT / '_meta' / 'imports' / 'eu' / 'cellar'
TODAY = datetime.date.today().isoformat()

DOCS = {
    'UE-2023-1114': {'celex': '32023R1114', 'kind': 'regulament',
                      'label': 'MiCA, Regulamentul (UE) 2023/1114 (piata criptoactivelor)'},
}


def fetch(celex):
    CACHE.mkdir(parents=True, exist_ok=True)
    path = CACHE / f'{celex}.xhtml'
    if not path.exists():
        req = urllib.request.Request(
            f'https://publications.europa.eu/resource/celex/{celex}',
            headers={'User-Agent': 'Mozilla/5.0', 'Accept': 'application/xhtml+xml',
                     'Accept-Language': 'ron'})
        with urllib.request.urlopen(req, timeout=180) as r:
            path.write_bytes(r.read())
    return path


def tx(el):
    return re.sub(r'\s+', ' ', ''.join(el.itertext())).strip()


def lines_of(el, out):
    """Paragrafele unui articol/considerent, in ordinea documentului; un tabel (lista de litere) devine
    cate o linie pe rand, cu celulele unite prin spatiu."""
    for ch in el:
        tag = etree.QName(ch).localname if isinstance(ch.tag, str) else ''
        if tag == 'p':
            t = tx(ch)
            if t:
                out.append(t)
        elif tag == 'table':
            for tr in ch.iter('{*}tr'):
                cells = [tx(td) for td in tr if isinstance(td.tag, str)]
                t = ' '.join(c for c in cells if c)
                if t:
                    out.append(t)
        elif tag == 'div':
            cls = ch.get('class', '')
            if 'eli-title' in cls:
                continue
            lines_of(ch, out)


def parse(path):
    root = etree.parse(str(path), etree.XMLParser(recover=True, resolve_entities=False, load_dtd=False)).getroot()
    arts, rcts = [], []
    for el in root.iter('{*}div'):
        i = el.get('id', '')
        if re.fullmatch(r'art_\d+[A-Za-z]?', i):
            head = title = ''
            for ch in el.iter('{*}p'):
                c = ch.get('class', '')
                if 'oj-ti-art' in c and not head:
                    head = tx(ch)
                elif 'oj-sti-art' in c and not title:
                    title = tx(ch)
            body = []
            lines_of(el, body)
            body = [b for b in body if b != head and b != title]
            arts.append((i[4:], head, title, body))
        elif re.fullmatch(r'rct_\d+', i):
            body = []
            lines_of(el, body)
            rcts.append((i[4:], body))
    return arts, rcts


def build(stem, spec):
    path = fetch(spec['celex'])
    arts, rcts = parse(path)
    if not arts or not rcts:
        raise SystemExit(f'{stem}: nu s-au gasit articole/considerente')
    nums = [int(re.match(r'\d+', a[0]).group()) for a in arts]
    if nums != list(range(1, max(nums) + 1)):
        raise SystemExit(f'{stem}: numerotare articole neregulata: {nums}')
    rn = [int(r[0]) for r in rcts]
    if rn != list(range(1, max(rn) + 1)):
        raise SystemExit(f'{stem}: numerotare considerente neregulata')
    eurlex = f"https://eur-lex.europa.eu/legal-content/RO/TXT/?uri=CELEX:{spec['celex']}"
    parts = [f"# {stem} — {spec['label']}", '',
             '> **TEXT INTEGRAL RO — nu extras.** Sursa primara este EUR-Lex / Publicatii UE; textul de aici vine '
             'din Cellar (XHTML, actul de baza). Articolele sint sub `###`, nu sub `##`, ca la celelalte fisiere UE-*: '
             'un citat se face `[' + stem + ' art.N]` si se verifica prin deschiderea fisierului. Preambulul '
             '(citarile) nu este pastrat; considerentele da.', '',
             f"- **CELEX:** {spec['celex']}", f"- **tip:** {spec['kind']}", f'- **link EUR-Lex:** {eurlex}',
             f'- **articole:** {len(arts)}; **considerente:** {len(rcts)}', '',
             '## Articole', '']
    for num, head, title, body in arts:
        parts.append(f"### Articolul {num}" + (f' — {title}' if title else ''))
        parts.append('')
        parts.extend(l + '\n' for l in body)
    parts += ['## Considerente', '']
    for num, body in rcts:
        parts.append(f'### Considerentul {num}')
        parts.append('')
        parts.extend(l + '\n' for l in body)
    body = '\n'.join(parts).rstrip() + '\n'
    sha = hashlib.sha256(('\n' + body).encode('utf-8')).hexdigest()  # corpul incepe cu linia goala de dupa frontmatter
    fm = '\n'.join(['---', f'source_url: {eurlex}',
                    f"cellar_xhtml: https://publications.europa.eu/resource/celex/{spec['celex']}",
                    f'ingested: {TODAY}', f'sha256: {sha}', 'source_type: legal-text',
                    'publisher: EUR-Lex / Publications Office of the European Union', 'language: ro',
                    f"celex: {spec['celex']}", f"base_celex: {spec['celex']}", f'instrument_id: {stem}',
                    f"document_type: {spec['kind']}", 'consolidation_date: n/a — act de baza',
                    'extract: false', 'full_text: true', '---', ''])
    out = OUT / f'{stem}.md'
    out.write_text(fm + '\n' + body, encoding='utf-8', newline='\n')
    print(f'{stem}: {len(arts)} articole, {len(rcts)} considerente, {len(body)} caractere -> {out.relative_to(ROOT).as_posix()}')


if __name__ == '__main__':
    only = [a for a in sys.argv[1:] if not a.startswith('-')]
    for stem, spec in DOCS.items():
        if not only or stem in only:
            build(stem, spec)
