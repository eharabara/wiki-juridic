"""Ingerarea ordinelor CNPDCP (protectia datelor cu caracter personal) din legis.md in
raw/papers/moldova-legal/. Creat 2026-09-21, pasul 1 din _meta/plans/2026-09-21-perimetru-protectia-datelor.md.

Invelis subtire peste _meta/imports/bnm/ingest_bnm_ro.py, ca _meta/imports/cnpf/ingest_cnpf_ro.py:
formatul fisierelor (frontmatter, antet, ancore, hash) este cel al celorlalte acte legis.md din
corpus. Se schimba destinatia (raw/papers/moldova-legal/, CNPDCP nu este perimetru CNPF/BNM),
cache-ul HTML si lista DOCS.

Descarcare: din Chrome-ul lui Eugen, dupa ce Cloudflare a lasat pagina sa treaca, prin fetch
same-origin (cu X-Requested-With) si POST catre un receptor local pe 127.0.0.1 care scrie octetii
serverului ca showdetails-<doc_id>.html. Descarcarea prin blob a mers doar pentru primul fisier.

Rulare:  python _meta/imports/cnpdcp/ingest_cnpdcp_ro.py --precheck
         python _meta/imports/cnpdcp/ingest_cnpdcp_ro.py OCNPDCP-27-2022
"""
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
_spec = importlib.util.spec_from_file_location(
    "ibr", str(ROOT / "_meta" / "imports" / "bnm" / "ingest_bnm_ro.py"))
ibr = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ibr)

RAW_DIR = ROOT / "raw" / "papers" / "moldova-legal"
META_DIR = ROOT / "_meta" / "imports" / "cnpdcp" / "legis-md"

# Identificatorul urmeaza codul legis.md (OCNPDCP27/2022 -> OCNPDCP-27-2022).
DOCS = {
    # Versiunea CURENTA (23.08.2026), consolidata cu Ordinul 39/2026: aceasta este cea care leaga.
    # Versiunea anterioara, 131047 (22.04.2022), nu se ingereaza.
    'OCNPDCP-27-2022': {'doc_id': '155870',
                        'title': 'Ordinul CNPDCP nr. 27/2022 privind aprobarea Listei tipurilor de '
                                 'operatiuni de prelucrare care fac obiectul cerintei de efectuare a '
                                 'unei evaluari a impactului asupra protectiei datelor'},
    # Actul modificator: il muta pe 27/2022 de pe Legea 133/2011 pe Legea 195/2024. Se tine separat
    # pentru ca temeiul lui arata daca 27/2022 supravietuieste sub art. 90 alin. (5) din L-195-2024.
    'OCNPDCP-39-2026': {'doc_id': '155868',
                        'title': 'Ordinul CNPDCP nr. 39/2026 cu privire la modificarea Ordinului '
                                 'Directorului CNPDCP nr. 27/2022'},
    'OCNPDCP-31-2026': {'doc_id': '155738',
                        'title': 'Ordinul CNPDCP nr. 31/2026 privind aprobarea Contractului standard '
                                 'pentru transferul de date cu caracter personal catre state care nu '
                                 'asigura un nivel adecvat de protectie'},
    'OCNPDCP-40-2026': {'doc_id': '156020',
                        'title': 'Ordinul CNPDCP nr. 40/2026 privind aprobarea Formularului tipizat al '
                                 'notificarii incalcarii securitatii datelor cu caracter personal'},
    # Decizie, nu ordin (antetul spune DECIZIE).
    'DCNPDCP-41-2026': {'doc_id': '156021',
                        'title': 'Decizia CNPDCP nr. 41/2026 privind caracterul adecvat al nivelului de '
                                 'protectie a datelor cu caracter personal al unor state, teritorii si '
                                 'organizatii internationale'},
    # Decizie, nu ordin. Din vechiul regim (2015). Statutul sub art. 90 alin. (5) din L-195-2024 se stabileste din
    # preambul la citire, nu se presupune.
    'DCNPDCP-581-2015': {'doc_id': '135821',
                         'title': 'Decizia CNPDCP nr. 581/2015 cu privire la aprobarea formularului '
                                  'tipizat de informare privind efectuarea supravegherii prin mijloace video'},
    # ---- Pasul 2 din plan: legea care aduce Protocolul 108+ (STCE 223) in ordinea juridica interna.
    # Lege organica, 4 articole ("Art. 1. -"). Protocolul insusi este anexat ca imagine (Acord_ro.pdf,
    # 20 pagini, fara strat de text; Acord_en.pdf, 37 pagini) si NU este ingerat pana nu exista OCR;
    # PDF-urile sint pastrate in legis-md/. In vigoare 23.08.2026, ca L-195-2024.
    'L-36-2026': {'doc_id': '153723',
                  'title': 'Legea nr. 36/2026 privind ratificarea Protocolului de amendare a Conventiei '
                           'pentru protectia persoanelor referitor la prelucrarea automatizata a datelor '
                           'cu caracter personal'},
    # Gasit 2026-09-24, din pagina "Decizii/Ordine" a datepersonale.md: raspunde chiar la
    # intrebarea lui Eugen din 21 septembrie despre "ordinul 48 din septembrie", pe care planul
    # nu il gasise. Adoptat 09.09.2026, publicat 16.09.2026 (dupa data planului), abroga Ordinul
    # 25/2024 (regulamentul de control anterior). Structurat in puncte (67), fara articole.
    'OCNPDCP-48-2026': {'doc_id': '156385',
                        'title': 'Ordinul CNPDCP nr. 48/2026 cu privire la aprobarea Regulamentului '
                                 'privind efectuarea investigatiei'},
}

ibr.RAW_DIR = RAW_DIR
ibr.META_DIR = META_DIR
ibr.DOCS = DOCS

if __name__ == '__main__':
    ibr.main()
