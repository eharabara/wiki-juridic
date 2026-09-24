"""Ingerarea Deciziei de punere in aplicare (UE) 2021/914 (clauzele contractuale standard pentru
transferul de date cu caracter personal catre state terte), text integral, din Cellar, in
raw/papers/moldova-legal/. Creat 2026-09-24, punctul 6 ramas din
_meta/plans/2026-09-21-perimetru-protectia-datelor.md.

Structura diferita de ingest_eu_dataprotection.py: o decizie de punere in aplicare are putine
articole proprii (art. 1-4) si tot continutul normativ greu sta in ANEXA (div id="anx_1"), care nu
e ea insasi impartita in <div id="art_N">, ci e o secventa plata de <p class="oj-ti-grseq-1">
(titluri: SECTIUNEA, Clauza N, titlul clauzei, MODULUL X, subsectiuni N.M) urmate de <p
class="oj-normal"> sau <table> (continut). Extractorul parcurge copiii lui anx_1 in ordinea
documentului si clasifica fiecare titlu dupa forma textului lui, nu dupa o eticheta de clasa
separata (toate titlurile din anexa au aceeasi clasa CSS).

Sursa: GET https://publications.europa.eu/resource/celex/<CELEX> cu Accept: application/xhtml+xml
si Accept-Language: ron, urmand redirectul 303 (spre deosebire de ingest_eu_dataprotection.py,
care nu are nevoie de -L pentru actele acelea; aici Cellar redirectioneaza explicit catre
document-ul propriu-zis).

Rulare:  python _meta/imports/eu/ingest_eu_scc.py
"""
import hashlib, re, sys, urllib.request, datetime
from pathlib import Path
from lxml import etree

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'raw' / 'papers' / 'moldova-legal'
CACHE = ROOT / '_meta' / 'imports' / 'eu' / 'cellar'
TODAY = datetime.date.today().isoformat()

STEM = 'UE-2021-914'
CELEX = '32021D0914'
LABEL = ('Decizia de punere in aplicare (UE) 2021/914 a Comisiei din 4 iunie 2021 privind '
         'clauzele contractuale standard pentru transferul de date cu caracter personal catre '
         'tari terte in temeiul Regulamentului (UE) 2016/679 al Parlamentului European si al '
         'Consiliului')

SECTIUNE_RE = re.compile(r'^SEC[TȚ]IUNEA\s')
CLAUZA_RE = re.compile(r'^Clauza\s+\d+')
MODUL_RE = re.compile(r'^MODULUL\s')
SUBSECT_RE = re.compile(r'^\d+\.\d+\.?\s')


def fetch():
    CACHE.mkdir(parents=True, exist_ok=True)
    path = CACHE / f'{CELEX}.xhtml'
    if not path.exists() or path.stat().st_size == 0:
        req = urllib.request.Request(
            f'https://publications.europa.eu/resource/celex/{CELEX}',
            headers={'User-Agent': 'Mozilla/5.0', 'Accept': 'application/xhtml+xml',
                     'Accept-Language': 'ron'})
        opener = urllib.request.build_opener(urllib.request.HTTPRedirectHandler)
        with opener.open(req, timeout=180) as r:
            path.write_bytes(r.read())
    return path


def tx(el):
    return re.sub(r'\s+', ' ', ''.join(el.itertext())).strip()


def cell_direct_text(td):
    """Textul unei celule, din <p>-urile ei directe, EXCLUZIND orice <table> imbricat: unele
    celule ale acestei decizii contin un paragraf introductiv (litera a), b)...) urmat de un
    tabel imbricat pentru sub-punctele (i), (ii)...; daca tx() ar lua tot td-ul cu itertext,
    sub-punctele ar aparea o data in randul-parinte si inca o data cind tabelul imbricat e
    procesat separat mai jos — de-a asta functia asta se opreste la <p>, nu coboara in <table>."""
    parts = []
    for ch in td:
        tag = etree.QName(ch).localname if isinstance(ch.tag, str) else ''
        if tag == 'p':
            t = tx(ch)
            if t:
                parts.append(t)
    return ' '.join(parts) if parts else tx_no_table(td)


def tx_no_table(el):
    """Ca tx(), dar opreste coborirea in orice <table> imbricat (pentru celule fara <p> propriu,
    unde textul sta direct sub <td>, ca la unele randuri simple)."""
    texts = []
    if el.text:
        texts.append(el.text)
    for ch in el:
        tag = etree.QName(ch).localname if isinstance(ch.tag, str) else ''
        if tag != 'table':
            texts.append(tx(ch))
        if ch.tail:
            texts.append(ch.tail)
    return re.sub(r'\s+', ' ', ' '.join(texts)).strip()


def table_rows(table_el):
    """Randurile directe ale unui <table> (prin <tbody> daca exista), fara sa coboare in tabele
    imbricate — cele se proceseaza separat, dupa randul care le contine, ca sa nu se dubleze."""
    rows = [c for c in table_el if etree.QName(c).localname == 'tr']
    if rows:
        return rows
    for c in table_el:
        if etree.QName(c).localname == 'tbody':
            return [cc for cc in c if etree.QName(cc).localname == 'tr']
    return []


def para_lines(el):
    """Textul unui <p> normal sau, pentru un <table> (litere a)/b).../cifre romane), o linie pe
    rand — cu tabelele imbricate intr-o celula redate ca linii separate, dupa linia care le
    contine, nu combinate in ea."""
    tag = etree.QName(el).localname if isinstance(el.tag, str) else ''
    out = []
    if tag == 'p':
        t = tx(el)
        if t:
            out.append(t)
    elif tag == 'table':
        for tr in table_rows(el):
            tds = [td for td in tr if isinstance(td.tag, str)]
            cells = [cell_direct_text(td) for td in tds]
            t = ' '.join(c for c in cells if c)
            if t:
                out.append(t)
            for td in tds:
                for nested in td:
                    if etree.QName(nested).localname == 'table':
                        out.extend(para_lines(nested))
    return out


def get_div(root, div_id):
    for el in root.iter('{*}div'):
        if el.get('id', '') == div_id:
            return el
    return None


def walk_body(el, head_seen):
    """Colecteaza recursiv liniile de continut ale unui element (articol/considerent), incluzind
    alineatele care stau in <div> proprii (cazul art. 1 si art. 4 ale acestei decizii), sarind
    peste titlul <p class="oj-ti-art"> intilnit o singura data."""
    out = []
    for ch in el:
        tag = etree.QName(ch).localname if isinstance(ch.tag, str) else ''
        cls = ch.get('class', '') if isinstance(ch.tag, str) else ''
        if tag == 'p' and 'oj-ti-art' in cls:
            head_seen[0] = True
            continue
        if tag in ('p', 'table'):
            out.extend(para_lines(ch))
        elif tag == 'div':
            out.extend(walk_body(ch, head_seen))
    return out


def extract_articles(root):
    arts = []
    for el in root.iter('{*}div'):
        i = el.get('id', '')
        if re.fullmatch(r'art_\d+', i):
            head = ''
            for ch in el.iter():
                tag = etree.QName(ch).localname if isinstance(ch.tag, str) else ''
                cls = ch.get('class', '') if isinstance(ch.tag, str) else ''
                if tag == 'p' and 'oj-ti-art' in cls and not head:
                    head = tx(ch)
            body = walk_body(el, [False])
            arts.append((i[4:], head, body))
    arts.sort(key=lambda a: int(a[0]))
    return arts


def extract_recitals(root):
    rcts = []
    for el in root.iter('{*}div'):
        i = el.get('id', '')
        if re.fullmatch(r'rct_\d+', i):
            body = []
            for ch in el:
                body.extend(para_lines(ch))
            rcts.append((int(i[4:]), body))
    rcts.sort(key=lambda r: r[0])
    return rcts


def extract_annex(anx):
    """Intoarce o lista de linii markdown, urmarind SECTIUNEA > Clauza N + titlu > MODULUL >
    subsectiune N.M ca nivele de titlu descrescatoare, restul ca text simplu."""
    lines = ['### Anexa — Clauze contractuale standard', '']
    pending_clauza = None  # numarul clauzei citite, asteapta titlul de pe linia urmatoare
    for ch in anx:
        tag = etree.QName(ch).localname if isinstance(ch.tag, str) else ''
        cls = ch.get('class', '') if isinstance(ch.tag, str) else ''
        if tag == 'p' and 'oj-doc-ti' in cls:
            continue  # "ANEXA" - deja in titlul sectiunii
        if tag == 'p' and 'grseq' in cls:
            t = tx(ch)
            if t == 'CLAUZE CONTRACTUALE STANDARD':
                continue
            if SECTIUNE_RE.match(t):
                lines += ['', f'#### {t}', '']
                pending_clauza = None
            elif CLAUZA_RE.match(t):
                pending_clauza = t
            elif pending_clauza:
                lines += ['', f'##### {pending_clauza} — {t}', '']
                pending_clauza = None
            elif MODUL_RE.match(t):
                lines += ['', f'**{t}**', '']
            elif SUBSECT_RE.match(t):
                lines += ['', f'**{t}**', '']
            else:
                # titlu de clauza fara subtitlu pe linia urmatoare (ex. "Clauza 5" e urmat direct
                # de "Ierarhie" mai sus, deci ajunge aici doar cazul rar cu titlu unic pe linie)
                lines += ['', f'##### {t}', '']
            continue
        for l in para_lines(ch):
            lines.append(l + '\n')
    return lines


def build():
    path = fetch()
    root = etree.parse(str(path), etree.XMLParser(recover=True, resolve_entities=False, load_dtd=False)).getroot()
    arts = extract_articles(root)
    rcts = extract_recitals(root)
    anx = get_div(root, 'anx_1')
    app = get_div(root, 'app_1')
    if not arts or not rcts or anx is None:
        raise SystemExit(f'{STEM}: structura neasteptata — art {len(arts)}, rct {len(rcts)}, anexa {anx is not None}')
    if [int(a[0]) for a in arts] != [1, 2, 3, 4]:
        raise SystemExit(f'{STEM}: articole neasteptate: {[a[0] for a in arts]}')

    eurlex = f'https://eur-lex.europa.eu/legal-content/RO/TXT/?uri=CELEX:{CELEX}'
    parts = [f'# {STEM} — {LABEL}', '',
             '> **TEXT INTEGRAL RO — nu extras.** Sursa primara este EUR-Lex / Publicatii UE; '
             'textul de aici vine din Cellar (XHTML, actul de baza, redirect 303 urmat). '
             'Articolele proprii ale deciziei (art. 1-4) sint sub `###`, ca la celelalte fisiere '
             'UE-* cu text integral. **Anexa este continutul normativ greu** (clauzele '
             'contractuale standard propriu-zise): structurata `SECTIUNEA` (`####`), `Clauza N — '
             'titlu` (`#####`), cu `MODULUL` si subsectiunile numerice (N.M) ca text bold, nu '
             'titluri Markdown separate, pentru ca patru module paralele repeta aceleasi '
             'subsectiuni (8.1-8.9 etc.) si titluri Markdown identice repetate ar sparge orice '
             'cautare pe titlu. Un citat se face `[UE-2021-914 anexa, Clauza N]`, nu `art.N` '
             '(art. 1-4 sint clauze procedurale ale deciziei, nu ale SCC-urilor).', '',
             f'- **CELEX:** {CELEX}', '- **tip:** decizie de punere in aplicare',
             f'- **link EUR-Lex:** {eurlex}',
             f'- **articole proprii:** {len(arts)}; **considerente:** {len(rcts)}; '
             '**anexa:** patru module (operator-operator, operator-persoana imputernicita, '
             'persoana imputernicita-persoana imputernicita, persoana imputernicita-operator) '
             'plus apendice (Anexele I-III, sabloane de completat de parti, necompletate aici)',
             '', '## Articole', '']
    for num, head, body in arts:
        parts.append(f'### Articolul {num}')
        parts.append('')
        parts.extend(l + '\n' for l in body)
    parts += ['## Considerente', '']
    for num, body in rcts:
        parts.append(f'### Considerentul {num}')
        parts.append('')
        parts.extend(l + '\n' for l in body)
    parts += ['']
    parts += extract_annex(anx)
    if app is not None:
        app_body = []
        for ch in app:
            app_body.extend(para_lines(ch))
        parts += ['', '### Apendice — nota explicativa', '']
        parts.extend(l + '\n' for l in app_body)
        parts += ['', '> Anexele I-III propriu-zise (Lista partilor, Masuri tehnice si '
                       'organizatorice, Lista subcontractantilor) sint sabloane necompletate, cu '
                       'cimpuri de genul „a se completa de parti"; nu sint transcrise linie cu '
                       'linie aici — continutul lor normativ e deja in clauzele 6-9 de mai sus, '
                       'care il descriu. Nota asta e explicita, nu o omisiune tacuta.']

    body_text = '\n'.join(parts).rstrip() + '\n'
    sha = hashlib.sha256(('\n' + body_text).encode('utf-8')).hexdigest()
    fm = '\n'.join(['---', f'source_url: {eurlex}',
                    f'cellar_xhtml: https://publications.europa.eu/resource/celex/{CELEX}',
                    f'ingested: {TODAY}', f'sha256: {sha}', 'source_type: legal-text',
                    'publisher: EUR-Lex / Publications Office of the European Union', 'language: ro',
                    f'celex: {CELEX}', f'base_celex: {CELEX}', f'instrument_id: {STEM}',
                    'document_type: decizie', 'consolidation_date: n/a — act de baza',
                    'extract: false', 'full_text: true', '---', ''])
    out = OUT / f'{STEM}.md'
    out.write_text(fm + '\n' + body_text, encoding='utf-8', newline='\n')
    print(f'{STEM}: {len(arts)} articole, {len(rcts)} considerente, anexa '
          f'{len(extract_annex(anx))} linii, {len(body_text)} caractere -> '
          f'{out.relative_to(ROOT).as_posix()}')


if __name__ == '__main__':
    build()
