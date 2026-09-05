"""Ingerarea legilor bancare in romana din legis.md in raw/papers/bnm/legal-ro/ (P8, decizia D3).

Invelis subtire peste _meta/imports/moldova-legal/ingest_business_law.py: refoloseste exact
resolve_superscripts, extract_doc si make_raw, deci formatul fisierelor (frontmatter, antet,
ancore, hash) este identic cu cel al celorlalte acte legis.md din corpus. Se schimba doar:

  1. destinatia: raw/papers/bnm/legal-ro/, perimetrul BNM, nu moldova-legal/;
  2. pasul de descarcare. La 2026-09-05 dupa-amiaza legis.md a pus o verificare Cloudflare pe
     toate endpoint-urile, care blocheaza curl. HTML-ul a fost luat din Chrome-ul lui Eugen,
     dupa ce el a trecut verificarea, prin serializarea DOM-ului (document.documentElement
     .outerHTML) si descarcare ca fisier. Consecinta: fisierele showdetails-*.html de aici sint
     DOM-ul serializat de Chrome, nu octetii serverului; etichetele <sup> si structura
     #contentdoc sint pastrate, ceea ce este tot ce cere extractorul.

Rulare:  python _meta/imports/bnm/ingest_bnm_ro.py            (toate cele sase)
         python _meta/imports/bnm/ingest_bnm_ro.py L-160-2023  (numai actele numite)
         python _meta/imports/bnm/ingest_bnm_ro.py --precheck  (doar controlul HTML-ului, nu scrie)
Verificare dupa rulare: python _meta/imports/bnm/verify_bnm_ro.py
"""
import importlib.util, io, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
_spec = importlib.util.spec_from_file_location(
    "ibl", str(ROOT / "_meta" / "imports" / "moldova-legal" / "ingest_business_law.py"))
ibl = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ibl)

RAW_DIR = ROOT / "raw" / "papers" / "bnm" / "legal-ro"
META_DIR = ROOT / "_meta" / "imports" / "bnm" / "legis-md-ro"
ibl.META_DIR = META_DIR   # make_raw nu il foloseste, dar il tinem coerent

# doc_id-urile au fost gasite la 2026-09-05 prin cautare in titlu (search_type=1, fara
# diacritice), din Chrome. Rindul actului de baza apare cu marcajul "Modificat" si numarul
# LP<nr>/<an>; rindurile de modificare si de interpretare au alte numere si nu se ingereaza.
DOCS = {
    # 34 <sup>, fara CUPRINS, ultima modificare LP144/2025 in vigoare 20.09.25.
    'L-202-2017': {'doc_id': '151445',
                   'title': 'Legea nr. 202/2017 privind activitatea bancilor'},
    # 90 <sup>, fara CUPRINS. Republicata in MO 297-300/2015; ultima modificare LP45/2026
    # (guvernanta institutionala), in vigoare 23.04.26.
    'L-548-1995': {'doc_id': '154046',
                   'title': 'Legea nr. 548/1995 cu privire la Banca Nationala a Moldovei'},
    # 128 <sup>, fara CUPRINS. ATENTIE: ultima modificare LP128/2026 intra in vigoare
    # 01.01.27, deci consolidarea este VIITOARE; fisierul poarta avertismentul standard.
    'L-114-2012': {'doc_id': '155331',
                   'title': 'Legea nr. 114/2012 cu privire la serviciile de plata si moneda electronica'},
    # 90 <sup>, fara CUPRINS, ultima modificare LP314/2024 in vigoare 28.02.25.
    'L-232-2016': {'doc_id': '146912',
                   'title': 'Legea nr. 232/2016 privind redresarea si rezolutia bancilor'},
    # 70 <sup>, fara CUPRINS. Titlul oficial poarta un asterisc ("reglementarea valutara*"),
    # semn de republicare (MO 423-429/2016). Ultima modificare LP327/2025 in vigoare 31.12.25.
    'L-62-2008': {'doc_id': '152953',
                  'title': 'Legea nr. 62/2008 privind reglementarea valutara'},
    # INLOCUIESTE Legea 575/2003 din lista D3. legis.md arata 575/2003 (doc_id 137950) ca
    # ABROGATA; actul curent este Legea 160/2023, in vigoare din 01.10.2023, nemodificata,
    # care transpune partial Directiva 2014/49/UE. Punctul deschis 4 din plan, decis de Eugen
    # la 2026-09-05: se ingereaza inlocuitorul. 1 <sup>, fara CUPRINS.
    'L-160-2023': {'doc_id': '137939',
                   'title': 'Legea nr. 160/2023 cu privire la garantarea depozitelor in banci'},
}


def load(doc_id):
    path = META_DIR / f"showdetails-{doc_id}.html"
    data = io.open(path, encoding='utf-8', errors='replace').read()
    if 'id="contentdoc"' not in data or 'Just a moment' in data[:3000]:
        raise RuntimeError(f"{path.name}: nu contine documentul (pagina de verificare?)")
    return f"https://www.legis.md/cautare/showdetails/{doc_id}", data, path


def precheck(stem, spec, data):
    """Controlul de dinainte de rulare, acelasi ca in comentariile din DOCS ale scriptului-mama."""
    sup = len(re.findall(r'<sup(?:\s[^>]*)?>', data, flags=re.I))
    css = len(re.findall(r'<span[^>]*top:\s*-[0-9.]+em', data, flags=re.I))
    resolved = ibl.resolve_superscripts(data)
    parsed = ibl.extract_doc(resolved)
    anchors = [l for l in parsed['text_markdown'].split('\n') if l.startswith('## Articolul')]
    nums = re.findall(r'^## Articolul (\d+)(?=[.\s]|$)', parsed['text_markdown'], re.M)
    ints = [int(n) for n in nums]
    dupes = sorted({n for n in ints if ints.count(n) > 1})
    gaps = [n for n in range(1, max(ints) + 1) if n not in ints] if ints else []
    cup = any(l.replace(' ', '').upper() == 'CUPRINS' for l in parsed['lines'])
    print(f"{stem}: <sup>={sup} css-raised={css} cuprins={cup} ancore={len(anchors)} "
          f"de baza={len(ints)} (1-{max(ints) if ints else 0}) duplicate={dupes or 'none'} "
          f"lacune={gaps or 'none'} consolidare={parsed['consolidation_date']}"
          f"{' VIITOARE' if parsed['consolidation_date'] > ibl.TODAY else ''}"
          f" titlu={parsed['official_title'][:70]!r}")
    return parsed


def main():
    args = sys.argv[1:]
    only = [a for a in args if not a.startswith('-')]
    targets = {k: v for k, v in DOCS.items() if not only or k in only}
    if only and not targets:
        raise SystemExit(f"nimic de ingerat; alege dintre: {', '.join(DOCS)}")
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    for stem, spec in targets.items():
        show_url, data, path = load(spec['doc_id'])
        parsed = precheck(stem, spec, data)
        # Titlul din fisa vine dintr-o celula de tabel si poate purta un rind nou (L-114-2012,
        # L-160-2023). Este metadata, nu text legal: se aduce pe un singur rind.
        parsed['official_title'] = re.sub(r'\s+', ' ', parsed['official_title']).strip()
        if '--precheck' in args:
            continue
        resolved = ibl.resolve_superscripts(data)
        if '<sup' in resolved:
            raise RuntimeError('resolve_superscripts nu a rezolvat exponentii')
        out = RAW_DIR / f"{stem}.md"
        out.write_text(ibl.make_raw(stem, spec, parsed, show_url), encoding='utf-8', newline='\n')
        print(f"  -> {out.relative_to(ROOT).as_posix()}: {parsed['article_count']} ancore, "
              f"HTML {path.name}")


if __name__ == '__main__':
    main()
