"""Ingerarea GDPR (Regulamentul (UE) 2016/679) si a Directivei (UE) 2016/680 in romana, TEXT INTEGRAL
(articole si considerente), din Cellar (publications.europa.eu), in raw/papers/moldova-legal/.
Creat 2026-09-21, pasul 3 din _meta/plans/2026-09-21-perimetru-protectia-datelor.md.

Diferenta fata de fisierele UE-* din raw/papers/cnpf/ (extrase: cuprins + articole-cheie): aici se
tine tot textul, pentru ca planul cere ca orice concluzie de divergenta sa fie citita la sursa, nu
dintr-un extras. Frontmatterul urmeaza extrasele, cu extract: false si full_text: true.

Sursa: GET https://publications.europa.eu/resource/celex/<CELEX> cu Accept: application/xhtml+xml
si Accept-Language: ron (pagina EUR-Lex propriu-zisa da 202 fara corp, verificare WAF; Cellar nu).
Se ia actul de baza, nu o consolidare: nici unul dintre cele doua nu are o consolidare cu text nou.

Rulare:  python _meta/imports/eu/ingest_eu_dataprotection.py [UE-2016-679 UE-2016-680]
"""
import hashlib, re, sys, urllib.request, datetime
from pathlib import Path
from lxml import etree

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'raw' / 'papers' / 'moldova-legal'
CACHE = ROOT / '_meta' / 'imports' / 'eu' / 'cellar'
TODAY = datetime.date.today().isoformat()

DOCS = {
    'UE-2016-679': {'celex': '32016R0679', 'kind': 'regulament',
                    'label': 'GDPR, Regulamentul (UE) 2016/679 (protectia datelor cu caracter personal)'},
    'UE-2016-680': {'celex': '32016L0680', 'kind': 'directiva',
                    'label': 'Directiva (UE) 2016/680 (protectia datelor in materie penala)'},
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
