"""Ingerarea Legii nr. 183/2016 (caracterul definitiv al decontarii) din legis.md in
raw/papers/cnpf/, perimetrul CNPF/BNM. Creat 2026-09-17, la cererea lui Eugen dupa consultarea
cozii de ingerare din _meta/graph/citation-graph.md: actul cu cele mai multe mentiuni din vault
inca neingerate (25 mentiuni, 7 acte citatoare, cel mai des chiar din DCU-REGULI-2026, 9 ori).

Invelis subtire peste _meta/imports/moldova-legal/ingest_business_law.py, ca ingest_bnm_ro.py si
ingest_cnpf_ro.py: refoloseste exact resolve_superscripts, extract_doc si make_raw. Se schimba
doar destinatia (raw/papers/cnpf/) si lista DOCS.

Descarcare: legis.md blocat pentru curl (Cloudflare interactiv) la ora ingerarii; HTML-ul a fost
luat prin fetch same-origin din pagina (browser-ul din panoul Claude, nu Chrome-ul lui Eugen),
deci octetii sint cei ai serverului, exact ce asteapta extractorul.

Rulare:  python _meta/imports/cnpf/ingest_payment_finality.py
"""
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
_spec = importlib.util.spec_from_file_location(
    "ibl", str(ROOT / "_meta" / "imports" / "moldova-legal" / "ingest_business_law.py"))
ibl = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ibl)

RAW_DIR = ROOT / "raw" / "papers" / "cnpf"
META_DIR = ROOT / "_meta" / "imports" / "cnpf" / "legis-md-payment"
ibl.RAW_DIR = RAW_DIR
ibl.META_DIR = META_DIR

# doc_id gasit 2026-09-17 prin cautare in titlu (search_type=1, fara diacritice), din browser-ul
# intern: "caracterul definitiv al decontarii", 5 rinduri, actul de baza LP183/2016 cu marcajul
# "Modificat". Fisa: Data abrogarii "-" (in vigoare), trei modificari (LP58/2017, LP32/2020,
# LP292/2023), ultima in vigoare 21.10.23. 1 <sup>, fara CUPRINS, 17 articole, act mic.
DOCS = {
    'L-183-2016': {'doc_id': '139645',
                   'title': 'Legea nr. 183/2016 cu privire la caracterul definitiv al decontarii '
                            'in sistemele de plati si de decontare a instrumentelor financiare'},
}
ibl.DOCS = DOCS

if __name__ == '__main__':
    ibl.main()
