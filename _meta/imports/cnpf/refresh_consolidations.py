"""Reimprospatarea celor trei consolidari expirate din perimetrul CNPF.

L-308-2017, L-92-2022 si L-171-2012 erau tinute la versiuni vechi de 3-8 ani, desi
ancorarea lor era curata, deci pareau de incredere. doc_id-urile curente au fost
gasite si verificate la 2026-09-04.

Operatiunea suprascrie text legal existent, asa ca face trei lucruri inainte:
  1. arhiveaza versiunea curenta in _archive/raw/;
  2. pastreaza lantul de provenienta in frontmatter (doc_id si sha256 anterioare);
  3. calculeaza delta la nivel de articol, fiindca 29 de pagini citeaza L-171-2012.

Exponentii sint rezolvati la sursa, ca la ingerarea din moldova-legal.
"""
from pathlib import Path
import importlib.util, io, re, shutil, datetime, hashlib

ROOT = Path(r"C:\Users\harab\wiki")
RAW = ROOT / "raw" / "papers" / "cnpf"
HTML_DIR = ROOT / "_meta" / "imports" / "cnpf" / "legis-md-consolidated"
TODAY = datetime.date.today().isoformat()
STAMP = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
ARCHIVE = ROOT / "_archive" / "raw" / f"cnpf-legis-md-before-refresh-{STAMP}"

_spec = importlib.util.spec_from_file_location(
    "ibl", str(ROOT / "_meta" / "imports" / "moldova-legal" / "ingest_business_law.py"))
ibl = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ibl)

TARGETS = {
    'L-308-2017': {'old': '110418', 'new': '155856',
                   'title': 'Legea nr. 308/2017 cu privire la prevenirea si combaterea '
                            'spalarii banilor si finantarii terorismului'},
    'L-92-2022':  {'old': '134551', 'new': '151081',
                   'title': 'Legea nr. 92/2022 privind activitatea de asigurare sau de reasigurare'},
    'L-171-2012': {'old': '121985', 'new': '156016',
                   'title': 'Legea nr. 171/2012 privind piata de capital'},
}


def articles(md_text):
    """Numerele de articol ancorate, de baza si cu exponent, in ordinea din fisier."""
    plain = re.findall(r'^## Articolul (\d+)\.', md_text, re.M)
    sup = re.findall(r'^## Articolul (\d+\^\d+)', md_text, re.M)
    return set(plain), set(sup)


def old_frontmatter(md_text):
    fm = {}
    if md_text.startswith('---'):
        block = md_text.split('---', 2)[1]
        for key in ('sha256', 'consolidation_date', 'doc_id', 'ingested'):
            m = re.search(rf"^{key}:\s*'?([^'\n]+)'?", block, re.M)
            if m:
                fm[key] = m.group(1).strip()
    return fm


def main():
    ARCHIVE.mkdir(parents=True, exist_ok=True)
    report = []
    for stem, spec in TARGETS.items():
        path = RAW / f"{stem}.md"
        before = io.open(path, encoding='utf-8').read()
        prev = old_frontmatter(before)
        plain_b, sup_b = articles(before)

        # 1. archive the version we are about to replace
        shutil.copy2(path, ARCHIVE / f"{stem}.md")

        # 2. fetch and extract the current consolidation
        # 2026-09-06: curl este blocat de verificarea Cloudflare de pe legis.md. Se foloseste
        # ibl.fetch, care incearca curl intr-un fisier .part si, daca nu iese documentul, cade
        # pe cache-ul de pe disc (HTML luat din Chrome); vechiul curl direct suprascria cache-ul
        # cu pagina de verificare. Cache-ul este folderul HTML_DIR al lotului curent.
        ibl.META_DIR = HTML_DIR
        url, data, out = ibl.fetch(spec['new'])
        resolved = ibl.resolve_superscripts(data)
        if '<sup' in resolved:
            raise RuntimeError(f"superscripts unresolved for {stem}")
        parsed = ibl.extract_doc(resolved)

        # 3. build the new file, carrying the provenance chain forward
        text = ibl.make_raw(stem, {'doc_id': spec['new'], 'title': spec['title']},
                            parsed, url)
        chain = (f"refreshed: '{TODAY}'\n"
                 f"doc_id_previous: '{spec['old']}'\n"
                 f"consolidation_date_previous: '{prev.get('consolidation_date','?')}'\n"
                 f"sha256_previous: {prev.get('sha256','?')}\n"
                 f"ingested_previous: '{prev.get('ingested','?')}'\n"
                 f"archived_previous_at: _archive/raw/{ARCHIVE.name}/{stem}.md\n")

        # O consolidare poate fi datata in VIITOR: legis.md serveste textul care va fi in
        # vigoare la o data ulterioara, incorporand modificari inca neintrate in vigoare.
        # Este o capcana mai rea decat vechimea, fiindca fisierul pare curent. Se marcheaza
        # explicit, cu lista dispozitiilor afectate.
        cdate = parsed['consolidation_date']
        pending = []
        if cdate > TODAY:
            dmy = f"{cdate[8:10]}.{cdate[5:7]}.{cdate[2:4]}"
            for line in parsed['lines']:
                if f"în vigoare {dmy}" in line and line.lstrip().startswith('['):
                    pending.append(re.sub(r'\s+', ' ', line).strip())
            chain += (f"consolidation_is_future: true\n"
                      f"in_force_warning: >-\n"
                      f"  Consolidarea este datata {cdate}, ulterioara zilei de {TODAY}. "
                      f"Fisierul contine modificari care NU sint inca in vigoare. "
                      f"Dispozitii afectate: {len(pending)}.\n")
        text = text.replace('---\n', '---\n' + chain, 1)

        if pending:
            warn = ['', f"> **ATENTIE, CONSOLIDARE VIITOARE.** Textul de mai jos este versiunea "
                        f"care va fi in vigoare la **{cdate}**, nu cea de astazi, {TODAY}. "
                        f"Urmatoarele {len(pending)} dispozitii apar modificate sau abrogate, "
                        f"dar modificarea **nu a intrat inca in vigoare**:", '']
            warn += [f"> - `{p}`" for p in pending]
            warn += ['', '> Verificati data de intrare in vigoare inainte de a cita oricare '
                         'dintre ele.', '']
            text = text.replace('## Fișa actului juridic', '\n'.join(warn) + '\n## Fișa actului juridic', 1)
        report_pending = pending

        # Recalculeaza sha256 DUPA asamblarea completa. make_raw() il calculeaza pe corpul
        # de dinainte ca noi sa inseram lantul de provenienta si avertismentul, deci valoarea
        # lui ramine in urma. Defect real, prins de fix_sha_drift.py al celuilalt fir la
        # 2026-09-04. Conventia corpusului este cea din lib_anchor.sha_variants: hash peste
        # octetii corpului de dupa fence-ul de frontmatter, exact asa cum sint scrisi.
        raw_bytes = text.encode('utf-8')
        fm_end = re.search(rb'^---\s*$', raw_bytes[3:], re.M)
        body_bytes = raw_bytes[3 + fm_end.end():]
        text = re.sub(r'^sha256:\s*\w+',
                      'sha256: ' + hashlib.sha256(body_bytes).hexdigest(),
                      text, count=1, flags=re.M)

        path.write_text(text, encoding='utf-8', newline='\n')

        plain_a, sup_a = articles(text)
        report.append({
            'stem': stem, 'old': spec['old'], 'new': spec['new'],
            'date_before': prev.get('consolidation_date', '?'),
            'date_after': parsed['consolidation_date'],
            'bytes_before': len(before), 'bytes_after': len(text),
            'plain_before': len(plain_b), 'plain_after': len(plain_a),
            'sup_before': len(sup_b), 'sup_after': len(sup_a),
            'added': sorted(plain_a - plain_b, key=int),
            'removed': sorted(plain_b - plain_a, key=int),
            'sup_added': sorted(sup_a - sup_b, key=lambda x: tuple(int(i) for i in x.split('^'))),
            'sup_removed': sorted(sup_b - sup_a, key=lambda x: tuple(int(i) for i in x.split('^'))),
            'pending': report_pending,
        })

    for r in report:
        print(f"\n{'=' * 76}\n{r['stem']}   doc_id {r['old']} -> {r['new']}\n{'=' * 76}")
        print(f"  consolidation : {r['date_before']}  ->  {r['date_after']}")
        print(f"  size          : {r['bytes_before']:,} -> {r['bytes_after']:,} bytes")
        print(f"  base articles : {r['plain_before']} -> {r['plain_after']}")
        print(f"  superscripts  : {r['sup_before']} -> {r['sup_after']}")
        if r['added']:
            print(f"  ADDED  ({len(r['added'])}): {', '.join(r['added'])}")
        if r['removed']:
            print(f"  REMOVED ({len(r['removed'])}): {', '.join(r['removed'])}")
        if r['sup_added']:
            print(f"  superscripts added  : {', '.join(r['sup_added'])}")
        if r['sup_removed']:
            print(f"  superscripts removed: {', '.join(r['sup_removed'])}")
        if r['pending']:
            print(f"  !! FUTURE CONSOLIDATION: {len(r['pending'])} provisions not yet in force")
            for p in r['pending']:
                print(f"       {p[:110]}")
    print(f"\narchive: _archive/raw/{ARCHIVE.name}/")


if __name__ == '__main__':
    main()
