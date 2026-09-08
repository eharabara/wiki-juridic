"""Ingerarea Regulilor Depozitarului central unic (dcu.md, PDF) in raw/papers/bnm/legal-ro/.

Ruta este alta decit cea a actelor de pe legis.md (ingest_bnm_ro.py): sursa este un PDF publicat de
DCU pe pagina sa, cum cere art. 25 alin. (2) din Legea 234/2016, nu un showdetails HTML. Regulile
au fost cautate pe legis.md la 2026-09-08 ("regulile depozitarului central unic", "depozitarului
central unic", cautare in titlu) si nu sint acolo; nici hotarirea BNM de aprobare finala nu apare.

Ce face:
  1. citeste PDF-ul din _meta/imports/bnm/dcu/, il hashuieste (source_file_sha256);
  2. extrage textul cu PyMuPDF, pagina cu pagina, get_text(); liniile se curata de spatiile de
     capat si liniile goale se elimina; NIMIC altceva nu se schimba (nici numerele de pagina
     "N din 62", nici cuprinsul, nici nota de copyright);
  3. insereaza titluri SINTETICE "## Articolul N. Titlu" si "## Capitolul R. Titlu" DEASUPRA liniilor
     originale. Sursa scrie "Art.N." (uneori singur pe rind, cu titlul pe rindul urmator) si
     "Capitolul R.", deci titlul de ancora nu este copia unei linii, ci e construit din una-doua
     linii-sursa. Liniile originale ramin neatinse; verify() le recupereaza stergind liniile "## ".
  4. ancoreaza numai in corp (dupa cuprins) si numai in ordinea numerotarii: o linie "Art.66." care
     apare dupa art. 59 este o trimitere rupta de la capat de rind ("... stabilit de / Art.66."),
     nu un titlu; la fel "Capitolul XII." intre VII si VIII. Un numar cu o cifra in plus fata de cel
     asteptat ("Art.821." dupa art. 82) este un exponent turtit de extractie; se ancoreaza ca
     "Articolul 82^1" numai daca PDF-ul poarta cifra ca exponent (flag de superscript in span).

Rulare:  python _meta/imports/bnm/ingest_dcu_rules.py --precheck   (afiseaza ancorele, nu scrie)
         python _meta/imports/bnm/ingest_dcu_rules.py              (scrie fisierul)
         python _meta/imports/bnm/ingest_dcu_rules.py --verify     (re-extrage si compara)
"""
import datetime, hashlib, re, sys
from pathlib import Path

import fitz
import yaml

ROOT = Path(__file__).resolve().parents[3]
STEM = 'DCU-REGULI-2026'
SRC = ROOT / '_meta' / 'imports' / 'bnm' / 'dcu' / 'Reguli_DCU_v3.pdf'
OUT = ROOT / 'raw' / 'papers' / 'bnm' / 'legal-ro' / f'{STEM}.md'
SOURCE_URL = 'https://www.dcu.md/doc/Reguli_DCU_v3.pdf'
SOURCE_PAGE = 'https://www.dcu.md/ro/reglementari/regulile-dcu'
IN_FORCE = '2026-04-08'
TODAY = datetime.date.today().isoformat()
TEXT_MARKER = '## Text integral extras din PDF (dcu.md)'

ROMAN_VAL = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}


def roman_to_int(s):
    total, prev = 0, 0
    for ch in reversed(s):
        v = ROMAN_VAL[ch]
        total += -v if v < prev else v
        prev = max(prev, v)
    return total


def extract(pdf_path):
    doc = fitz.open(str(pdf_path))
    lines = []
    for page in doc:
        for raw in page.get_text().split('\n'):
            line = raw.strip()
            if line:
                lines.append(line)
    return doc, lines


def superscript_evidence(doc):
    """Liniile PDF care incep cu 'Art.N' si poarta o cifra cu flag de superscript: {'82': '1'}."""
    found = {}
    for page in doc:
        for block in page.get_text('dict')['blocks']:
            for line in block.get('lines', []):
                spans = line['spans']
                text = ''.join(s['text'] for s in spans).strip()
                m = re.match(r'^Art\.(\d+)', text)
                if not m:
                    continue
                for s in spans:
                    t = s['text'].strip()
                    if t.isdigit() and (s['flags'] & 1):
                        base = re.match(r'^Art\.(\d+)', ''.join(
                            x['text'] for x in spans[:spans.index(s)]).strip())
                        if base:
                            found[base.group(1)] = t
    return found


def title_after(lines, i, rest):
    """Titlul ancorei: partea de dupa numar de pe aceeasi linie sau linia urmatoare, plus cel mult
    doua linii de continuare care incep cu minuscula (titlu rupt la capat de rind: 'sau MTF',
    'participantului', 'mobiliare'). O linie care incepe cu '(' sau cu 'a)' este corp, nu titlu."""
    parts = []
    j = i + 1
    if rest:
        parts.append(rest.strip())
    else:
        if j < len(lines) and not re.match(r'^[\(\[]|^[a-z]\)', lines[j]):
            parts.append(lines[j])
            j += 1
    extra = 0
    while j < len(lines) and extra < 2 and re.match(r'^[a-zăâîșțş]', lines[j]) \
            and not re.match(r'^[a-z]\)', lines[j]):
        parts.append(lines[j])
        j += 1
        extra += 1
    return ' '.join(parts).strip()


def anchor(lines, sup_evidence):
    """Intoarce (linii_cu_ancore, raport). Ancorele se insereaza deasupra liniei originale."""
    cup = next(i for i, l in enumerate(lines) if l.upper().startswith('CUPRINS'))
    cap1 = [i for i, l in enumerate(lines) if l == 'Capitolul I.']
    if len(cap1) < 2:
        raise RuntimeError('nu gasesc "Capitolul I." de doua ori (cuprins + corp)')
    body_start = cap1[1]
    out, report = [], {'articles': [], 'chapters': [], 'skipped': [], 'sup': []}
    next_art, next_cap = 1, 1
    for i, l in enumerate(lines):
        if i >= body_start:
            m = re.match(r'^Capitolul ([IVXLC]+)\.(?:\s+(.*))?$', l)
            if m and roman_to_int(m.group(1)) == next_cap:
                title = title_after(lines, i, m.group(2))
                out += [f"## Capitolul {m.group(1)}. {title}"]
                report['chapters'].append((i, m.group(1), title))
                next_cap += 1
                out.append(l)
                continue
            elif m:
                report['skipped'].append((i, l, f'capitol asteptat {next_cap}'))
            m = re.match(r'^Art\.(\d+)\.(?:\s+(.*))?$', l)
            if m:
                n = int(m.group(1))
                label = None
                if n == next_art:
                    label = str(n)
                    next_art += 1
                else:
                    # Exponent turtit: "821" poate fi 81^1 (dupa art. 81, inainte de 82) sau 82^1
                    # (dupa art. 82). Sursa v3 are "Art.82¹" ASEZAT intre art. 81 si art. 82, deci
                    # se admit ambele baze; dovada este flagul de superscript din PDF, pe baza.
                    s = str(n)
                    hit = None
                    for base in (str(next_art - 1), str(next_art)):
                        if n > next_art and s.startswith(base) and len(s) == len(base) + 1 \
                                and sup_evidence.get(base) == s[len(base):]:
                            hit = f"{base}^{s[len(base):]}"
                    if hit:
                        label = hit
                        report['sup'].append((i, l, label))
                    elif n > next_art and any(s.startswith(b) and len(s) == len(b) + 1
                                              for b in (str(next_art - 1), str(next_art))):
                        report['skipped'].append((i, l, f'exponent fara dovada in PDF, asteptat {next_art}'))
                    else:
                        report['skipped'].append((i, l, f'articol asteptat {next_art}'))
                if label:
                    title = title_after(lines, i, m.group(2))
                    out += [f"## Articolul {label}. {title}"]
                    report['articles'].append((i, label, title))
        out.append(l)
    report['body_start'] = body_start
    report['cuprins'] = cup
    return out, report


def body_hash(text):
    blob = text.encode('utf-8')
    fence = re.search(rb'^---\s*$', blob[3:], re.M)
    return hashlib.sha256(blob[3 + fence.end():]).hexdigest()


def build(lines, anchored, report, doc, pdf_sha, plain_sha):
    n_art = len(report['articles'])
    sup_arts = [lab for _, lab, _ in report['articles'] if '^' in lab]
    head = [
        f"# raw/{STEM} — Regulile Depozitarului central unic, textul in vigoare (dcu.md)", '',
        '> **TEXT DCU.MD RO — extras din PDF-ul publicat de Depozitarul central unic și păstrat '
        'pentru audit.** Nu corectez și nu armonizez tăcut textul; liniile care încep cu `## ` în '
        'secțiunea de text sînt titluri sintetice inserate deasupra liniilor originale, nu copii ale '
        'lor; șterse, rămîne extracția octet cu octet (`sha256_extraction`).', '',
        f"- **Sursă de referință:** {SOURCE_PAGE}",
        f"- **Fișier-sursă:** {SOURCE_URL} ({SRC.stat().st_size} octeți, sha256 `{pdf_sha}`), "
        f"arhivat la `{SRC.relative_to(ROOT).as_posix()}`",
        f"- **Versiune:** v3, în vigoare din **{IN_FORCE}**; aprobare prealabilă Hotărârea CS DCU nr. 49 din "
        '9 decembrie 2025; avizul CNPF, Hotărârea nr. 11/1 din 3 martie 2026; aprobare finală BNM, '
        'Hotărârea CE BNM nr. 89 din 8 aprilie 2026. Înlocuiește v2 (1 mai 2019 – 8 aprilie 2026) '
        'și v1 (31 iulie 2018 – 1 mai 2019), publicate separat pe aceeași pagină ca abrogate.',
        '- **Temei:** art. 25 din Legea nr. 234/2016 cu privire la Depozitarul central unic al valorilor '
        'mobiliare; regulile se publică pe pagina DCU, nu în Monitorul Oficial și nu pe legis.md '
        '(verificat 2026-09-08).',
        f"- **articole detectate:** {n_art}",
        f"- **capitole detectate:** {len(report['chapters'])}",
        f"- **pagini PDF:** {doc.page_count}; **linii nevide extrase:** {len(lines)}",
        f"- **exponenți de articol păstrați ca `^N`:** {', '.join(sup_arts) if sup_arts else 'niciunul'}. "
        'Extractorul PDF turtește exponenții ("Art.821."); ancora îl reface numai cu dovada flagului de '
        'superscript din PDF; linia-sursă rămîne cum a ieșit din extractor.',
        '- **linii-sursă care încep cu "Art.N." sau "Capitolul R." dar nu sînt titluri:** '
        + (', '.join(f"linia {i} `{l}`" for i, l, _ in report['skipped']) if report['skipped'] else 'niciuna')
        + '. Sînt trimiteri rupte la capăt de rînd; nu poartă ancoră.',
        '', '## Fișa actului — din pagina de titlu a PDF-ului și din pagina dcu.md', '',
        '| Câmp | Valoare |', '|---|---|',
        '| Denumirea | REGULILE Depozitarului Central Unic al Valorilor Mobiliare |',
        '| Emitent | Depozitarul Central Unic al Valorilor Mobiliare S.A. |',
        f"| Data intrării în vigoare | 8 aprilie 2026 |",
        '| Decizia de aprobare prealabilă | Hotărârea CS DCU nr.49 din 9 decembrie 2025 |',
        '| Aviz CNPF | Hotărârea CNPF nr.11/1 din 3 martie 2026 |',
        '| Decizia de aprobare finală | Hotărârea BNM nr.89 din 8 aprilie 2026 |',
        '| Versiuni abrogate | v2: 1 mai 2019 – 8 aprilie 2026 (Hotărârea CS DCU nr.14 din 19 aprilie 2019, '
        'abrogată prin Hotărârea CS DCU nr.7 din 8 aprilie 2026); v1: 31 iulie 2018 – 1 mai 2019 |',
        f"| Fișier PDF | creat 10.04.2026 cu Acrobat PDFMaker pentru Word, {doc.page_count} de pagini |",
        '', TEXT_MARKER, '',
    ]
    body_text = '\n'.join(head + anchored).strip() + '\n'
    fm = {
        'source_url': SOURCE_URL,
        'source_page': SOURCE_PAGE,
        'ingested': TODAY,
        'sha256': 'x',
        'sha256_extraction': plain_sha,
        'source_file': SRC.relative_to(ROOT).as_posix(),
        'source_file_sha256': pdf_sha,
        'source_type': 'legal-text',
        'publisher': 'Depozitarul Central Unic al Valorilor Mobiliare (dcu.md); aprobare finală BNM, '
                     'Hotărârea CE nr. 89 din 08.04.2026',
        'language': 'ro',
        'instrument_id': STEM,
        'official_title_detected': 'REGULILE Depozitarului Central Unic al Valorilor Mobiliare',
        'version': 'v3',
        'consolidation_date': IN_FORCE,
        'latest_modification_line': 'Versiune v3 în vigoare din 08.04.2026 (aprobare finală BNM, '
                                    'Hotărârea CE nr. 89 din 08.04.2026); înlocuiește v2 '
                                    '(01.05.2019 – 08.04.2026)',
        'full_text': True,
        'extract_method': 'PyMuPDF get_text() pagina cu pagina; spatii de capat si linii goale eliminate; '
                          'titluri sintetice "## Articolul N. Titlu" / "## Capitolul R. Titlu" inserate '
                          'deasupra liniilor originale, numai in corp si numai in ordinea numerotarii',
        'anchor_convention': 'Liniile care incep cu "## " de sub marcajul "' + TEXT_MARKER +
                             '" sint sintetice: sterse, ramine extractia, al carei hash este '
                             'sha256_extraction. Nicio linie-sursa nu este modificata.',
        'superscript_articles': sup_arts,
        'pages': doc.page_count,
    }
    fm_text = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False).strip()
    out = '---\n' + fm_text + '\n---\n\n' + body_text
    return re.sub(r'^sha256:\s*\S+', 'sha256: ' + body_hash(out), out, count=1, flags=re.M)


def plain_text(lines):
    return '\n'.join(lines) + '\n'


def verify():
    md = OUT.read_text(encoding='utf-8')
    doc, lines = extract(SRC)
    fails = 0
    pdf_sha = hashlib.sha256(SRC.read_bytes()).hexdigest()
    fm = yaml.safe_load(md.split('---', 2)[1])
    print(f"  pdf sha256              : {'PASS' if fm['source_file_sha256'] == pdf_sha else 'FAIL'}")
    fails += fm['source_file_sha256'] != pdf_sha
    text_part = md.split(TEXT_MARKER, 1)[1]
    written = [l for l in text_part.split('\n') if l and not l.startswith('## ')]
    same = written == lines
    print(f"  text integrity          : {'PASS' if same else 'FAIL'} ({len(written)} lines written vs {len(lines)} reference)")
    if not same:
        fails += 1
        for i, (a, b) in enumerate(zip(written, lines)):
            if a != b:
                print(f"    first divergence at {i}:\n      written  : {a[:110]!r}\n      reference: {b[:110]!r}")
                break
    ex_sha = hashlib.sha256(plain_text(lines).encode('utf-8')).hexdigest()
    print(f"  sha256_extraction       : {'PASS' if fm['sha256_extraction'] == ex_sha else 'FAIL'}")
    fails += fm['sha256_extraction'] != ex_sha
    print(f"  sha256 (body)           : {'PASS' if fm['sha256'] == body_hash(md) else 'FAIL'}")
    fails += fm['sha256'] != body_hash(md)
    arts = re.findall(r'^## Articolul (\d+(?:\^\d+)?)\. ', md, re.M)
    plain = [int(a) for a in arts if '^' not in a]
    gaps = [n for n in range(1, max(plain) + 1) if n not in plain] if plain else []
    dupes = sorted({n for n in plain if plain.count(n) > 1})
    print(f"  article anchors         : {len(arts)}  range 1-{max(plain) if plain else 0}  gaps={gaps or 'none'}  duplicates={dupes or 'none'}")
    fails += bool(gaps) + bool(dupes)
    caps = re.findall(r'^## Capitolul ([IVXLC]+)\. ', md, re.M)
    seq = [roman_to_int(c) for c in caps]
    ok = seq == list(range(1, len(seq) + 1))
    print(f"  chapter anchors         : {len(caps)}  in order: {'PASS' if ok else 'FAIL'}")
    fails += not ok
    # Cuprinsul sta intre primul "Capitolul I." (din cuprins) si prima ancora sintetica de capitol,
    # care precede "Capitolul I." din corp. Nicio linie "## " nu are voie inauntru.
    text_part = md.split(TEXT_MARKER, 1)[1]
    toc_from = text_part.index('\nCapitolul I.\n')
    toc_to = text_part.index('\n## Capitolul I. ')
    toc = text_part[toc_from:toc_to]
    print(f"  no anchors in cuprins   : {'PASS' if '\\n## ' not in toc else 'FAIL'}")
    fails += '\n## ' in toc
    print(f"\nFAILURES: {fails}")
    return fails


def main():
    args = sys.argv[1:]
    if '--verify' in args:
        sys.exit(1 if verify() else 0)
    doc, lines = extract(SRC)
    sup_evidence = superscript_evidence(doc)
    anchored, report = anchor(lines, sup_evidence)
    print(f"{STEM}: pagini={doc.page_count} linii={len(lines)} cuprins@{report['cuprins']} "
          f"corp@{report['body_start']} articole={len(report['articles'])} capitole={len(report['chapters'])} "
          f"exponenti(dovada)={sup_evidence} ancore-exponent={[x[2] for x in report['sup']]}")
    for i, l, why in report['skipped']:
        print(f"  sarit  linia {i}: {l[:70]!r}  ({why})")
    if '--precheck' in args:
        for i, r, t in report['chapters']:
            print(f"  CAP {r:>5}  @{i:<5} {t}")
        for i, lab, t in report['articles']:
            print(f"  ART {lab:>5}  @{i:<5} {t}")
        return
    pdf_sha = hashlib.sha256(SRC.read_bytes()).hexdigest()
    plain_sha = hashlib.sha256(plain_text(lines).encode('utf-8')).hexdigest()
    out = build(lines, anchored, report, doc, pdf_sha, plain_sha)
    OUT.write_bytes(out.encode('utf-8'))
    print(f"  -> {OUT.relative_to(ROOT).as_posix()}: {len(report['articles'])} ancore de articol, "
          f"{len(report['chapters'])} de capitol")


if __name__ == '__main__':
    main()
