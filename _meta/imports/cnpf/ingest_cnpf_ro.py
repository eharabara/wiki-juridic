"""Ingerarea actelor subordonate ale CNPF (hotariri CNPF cu regulamente anexate) din legis.md in
raw/papers/cnpf/, perimetrul CNPF. Creat 2026-09-09.

Invelis subtire peste _meta/imports/bnm/ingest_bnm_ro.py, care la rindul lui refoloseste
resolve_superscripts, extract_doc si make_raw din ingest_business_law.py: formatul fisierelor
(frontmatter, antet, ancore, hash) este identic cu al celorlalte acte legis.md din corpus. Se
schimba doar destinatia (raw/papers/cnpf/), cache-ul HTML (_meta/imports/cnpf/legis-md-consolidated/,
acelasi ca al legilor CNPF reimprospatate la 2026-09-04) si lista DOCS.

De ce nu legis_md_consolidated_ingest.py din acelasi folder: acela este scriptul din iulie, cu
curl direct (blocat de Cloudflare din 2026-09-05), cu arhivare si editare de pagini de entitate
in acelasi pas; formatul lui de fisier nu este cel actual.

Descarcare: HTML-ul se ia din Chrome-ul lui Eugen dupa ce el trece verificarea Cloudflare, prin
fetch same-origin si blob (octetii serverului), si se pune in META_DIR ca showdetails-<doc_id>.html.

Rulare:  python _meta/imports/cnpf/ingest_cnpf_ro.py --precheck
         python _meta/imports/cnpf/ingest_cnpf_ro.py HCNPF-14-5-2016
Verificare: python _meta/imports/cnpf/verify_cnpf_ro.py
"""
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
_spec = importlib.util.spec_from_file_location(
    "ibr", str(ROOT / "_meta" / "imports" / "bnm" / "ingest_bnm_ro.py"))
ibr = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ibr)

RAW_DIR = ROOT / "raw" / "papers" / "cnpf"
META_DIR = ROOT / "_meta" / "imports" / "cnpf" / "legis-md-consolidated"

# Identificatorul urmeaza codul legis.md al actului (HCNPF14/5/2016 -> HCNPF-14-5-2016), cum fac
# HG-, DCA- si HBN-.
DOCS = {
    # ---- 2026-09-09, la cererea lui Eugen: actul la care trimit pct. 12 din HBN-130-2013 si
    # procedura de decontare a DCU ("documentele necesare" la transferul in afara pietei
    # reglementate, inclusiv prin succesiune, "se prezinta documentele specificate in Regulamentul
    # CNPF nr. 14/5/2016"). Gasit prin cautare in titlu "circulatia valorilor mobiliare pe piata de
    # capital" (3 rinduri: HCNPF14/5/2016 "Modificat", HCNPF20/6/2020, HCNPF14/15/2022). Versiuni:
    # 92094 (2016), 112260 si 112261 (2018), 121705 (2020), 127708 (2021), 131276 (06.05.2022,
    # curenta, HCNPF14/15/2022). Cinci modificari in fisa; fara abrogare. Hotarire CNPF cu regulament
    # anexat, structurat pe PUNCTE: zero ancore de articol, "pct. N" NU este ancorat. 13 <sup>,
    # fara span CSS, fara CUPRINS, 7 marcaje "in vigoare", ~29 mii de caractere.
    'HCNPF-14-5-2016': {'doc_id': '131276',
                        'title': 'Hotarirea CNPF nr. 14/5/2016 referitor la aprobarea Regulamentului '
                                 'privind circulatia valorilor mobiliare pe piata de capital'},
    # ---- 2026-09-09, la cererea lui Eugen: actul la care trimit codurile de transfer din anexa
    # nr. 1 a procedurii de decontare a DCU ("tipurile de tranzactii stabilite de F7 din anexa la
    # Hotarirea CNPF nr.38/5 din 03.07.2015"). DENUMIRE SCHIMBATA: adoptata ca "Instructiunea cu
    # privire la raportarile persoanelor licentiate si autorizate pe piata de capital", azi
    # "Instructiunea cu privire la sistemul de raportare in domeniul pietei de capital"; legis.md
    # nu o gaseste dupa numar (nici "38/5", nici in text), ci dupa titlul VECHI, "raportarile
    # persoanelor licentiate", 6 rinduri, actul de baza cu marcajul "Modificat" si titlul nou.
    # Noua versiuni: 84522 (2015), 98160 (2017), 104809 si 112274 (2018), 113939 (2019), 120605
    # (2020), 132598 (2022), 137955 (2023), 147834 (01.10.2025, curenta, HCNPF12/4/2025). Sase
    # modificari in fisa; fara abrogare. Structurata pe PUNCTE, zero ancore de articol; 8 <sup>,
    # fara span CSS, 12 marcaje "in vigoare", ~50 mii de caractere; formularele F1-F33 probabil nu
    # sint in text (de verificat la ingest). legis.md a dat 524 in dupa-amiaza de 9 septembrie
    # si a revenit in aceeasi zi.
    'HCNPF-38-5-2015': {'doc_id': '147834',
                        'title': 'Hotarirea CNPF nr. 38/5/2015 privind aprobarea Instructiunii cu '
                                 'privire la sistemul de raportare in domeniul pietei de capital'},
}

# Se refolosesc functiile invelisului bancar cu directoarele acestui perimetru.
ibr.RAW_DIR = RAW_DIR
ibr.META_DIR = META_DIR
ibr.DOCS = DOCS

if __name__ == '__main__':
    ibr.main()
