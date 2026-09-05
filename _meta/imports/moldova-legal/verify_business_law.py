"""Verificare dupa ingerarea L-135/2007 si L-220/2007.

Testul de fond: se scot liniile de structura adaugate de noi si se compara restul,
linie cu linie, cu extractia simpla din acelasi HTML. Daca cele doua coincid exact,
inseamna ca am adaugat doar ancore si nu am atins textul legal.
"""
import importlib.util, io, re, sys
from pathlib import Path
from lxml import html

spec = importlib.util.spec_from_file_location("ibl", str(Path(__file__).parent / "ingest_business_law.py"))
ibl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ibl)

RAW = Path(r"C:\Users\harab\wiki\raw\papers\moldova-legal")
META = Path(r"C:\Users\harab\wiki\_meta\imports\moldova-legal\legis-md-business")

fail = 0
for stem, doc in ibl.DOCS.items():
    print(f"\n{'=' * 74}\n{stem}  (doc_id {doc['doc_id']})\n{'=' * 74}")
    md = io.open(RAW / f"{stem}.md", encoding='utf-8').read()

    # 1. reference extraction straight from the archived HTML
    raw_html = io.open(META / f"showdetails-{doc['doc_id']}.html", encoding='utf-8',
                       errors='replace').read()
    resolved = ibl.resolve_superscripts(raw_html)
    content = html.fromstring(resolved).xpath('//*[@id="contentdoc"]')[0]
    reference = [x for x in (ibl.clean_line(x) for x in content.text_content().splitlines()) if x]

    # 2. the body we wrote, with our added structure stripped back off
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

    # 3. no unresolved superscript markup anywhere
    body_only = md.split('---', 2)[2] if md.count('---') >= 2 else md
    leftover = '<sup' in body_only.lower()
    print(f"  no <sup> markup left    : {'PASS' if not leftover else 'FAIL'}")
    fail += leftover

    # 4. superscript anchors present in caret form
    # forma cu bara, Articolul 54^1/1 din Codul fiscal, este un articol distinct de 54^1;
    # daca regexul se opreste la 54^1 apare un fals duplicat
    sup_anchors = re.findall(r'^## Articolul (\d+\^\d+(?:/\d+)?)', md, re.M)
    # "Articolul" si numarul pot sta in elemente separate:
    #   <strong>Articolul</strong>&nbsp;<strong>45<sup>1</sup>.</strong>
    # text_content() le uneste corect, deci ancora e buna; regexul de control trebuie sa
    # tolereze etichetele si entitatile dintre ele, altfel raporteaza fals-pozitive.
    # Continutul lui <sup> nu este intotdeauna doar cifre. In corpus apar
    #   <sup>10.</sup>   punctul inauntrul exponentului   (Codul contraventional, art. 423^10)
    #   <sup>1&nbsp;</sup>  spatiu insecabil in coada     (Codul de procedura penala, art. 296^1)
    # resolve_superscripts() le normalizeaza, deci ancora este corecta; controlul trebuie sa
    # faca aceeasi normalizare, altfel raporteaza fals-pozitive.
    _sup = re.compile(r'Articolul(?:\s|&nbsp;|<[^>]*>)*(\d+)<sup>(.*?)</sup>(/\d+)?', re.S)
    _found = set()
    for a, b, c in _sup.findall(raw_html):
        inner = ibl.ihtml.unescape(re.sub(r'<[^>]*>', '', b)).replace(chr(160), ' ').strip()
        m = re.match(r'(\d+)', inner)
        if m:
            _found.add(f"{a}^{m.group(1)}{c}")
    sup_source = sorted(_found,
                        key=lambda x: (int(x.split('^')[0]),
                                       int(x.split('^')[1].split('/')[0]),
                                       x))
    match = sorted(sup_anchors, key=lambda x: (int(x.split('^')[0]),
                                               int(x.split('^')[1].split('/')[0]),
                                               x)) == sup_source
    print(f"  superscript articles    : {'PASS' if match else 'FAIL'}  "
          f"{len(sup_anchors)} anchored -> {', '.join(sup_anchors)}")
    if not match:
        fail += 1
        print(f"    source expects: {', '.join(sup_source)}")

    # 5. body-level superscripts survived too (paragraphs, letters)
    body_carets = len(re.findall(r'\(\d+\^\d+\)', md)) + len(re.findall(r'[a-z]\^\d+\)', md))
    print(f"  body-level ^N kept      : {body_carets} occurrences "
          f"(alineate si litere)")

    # 6. article numbering: gaps and duplicates
    # Punctul de dupa numar NU este obligatoriu in sursa. Un articol fara titlu se scrie
    # `Articolul 28`, curat: asa apare in L-284-2004, unde art. 28 este articolul de
    # dispozitii finale. Prima versiune a contorului cerea punct, deci il rata si raporta
    # "27, range 1-27", ceea ce se citeste drept lacuna la 28, desi ancora exista si
    # numerotarea este completa. Este aceeasi clasa de eroare ca `Aricolul 78` din Codul de
    # procedura civila, cu deosebirea ca acolo sursa e gresita, aici era contorul.
    # Forma de mai jos accepta punct, spatiu sau sfirsit de linie dupa numar si continua sa
    # excluda articolele cu exponent (`Articolul 25^1.`), fiindca dupa cifre urmeaza `^`,
    # care nu este niciunul dintre cele trei. Exclude si formele cu litera (`Articolul 12a`),
    # ca inainte.
    plain = [int(x) for x in re.findall(r'^## Articolul (\d+)(?=[.\s]|$)', md, re.M)]
    untitled = re.findall(r'^## Articolul (\d+)\s*$', md, re.M)
    dupes = sorted({n for n in plain if plain.count(n) > 1})
    gaps = [n for n in range(1, max(plain) + 1) if n not in plain] if plain else []
    print(f"  plain articles          : {len(plain)}  range 1-{max(plain) if plain else 0}")
    if untitled:
        print(f"  fara punct dupa numar   : {', '.join(untitled)}  (articole fara titlu in sursa)")
    print(f"  duplicates              : {dupes if dupes else 'none'}")
    print(f"  numbering gaps          : {gaps if gaps else 'none'}")

    # 7. frontmatter sanity
    fm = md.split('---', 2)[1]
    for key in ('doc_id', 'consolidation_date', 'sha256', 'instrument_id', 'superscript_articles'):
        present = re.search(rf'^{key}:', fm, re.M) is not None
        if not present:
            print(f"  frontmatter MISSING     : {key}")
            fail += 1
    dc = re.search(r'^doc_id:\s*[\'"]?(\d+)', fm, re.M)
    print(f"  frontmatter doc_id      : {dc.group(1) if dc else '?'} "
          f"({'PASS' if dc and dc.group(1) == doc['doc_id'] else 'FAIL'})")

print(f"\n{'=' * 74}\nFAILURES: {fail}\n{'=' * 74}")
sys.exit(1 if fail else 0)
