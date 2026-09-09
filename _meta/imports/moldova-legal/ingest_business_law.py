"""Ingerare L-135/2007 si L-220/2007 din legis.md in raw/papers/moldova-legal/.

Conventiile de format (frontmatter, antet, ancore) sint cele din
_meta/imports/cnpf/legis_md_consolidated_ingest.py. Diferenta de fond: aici
exponentii din HTML sint rezolvati INAINTE de extractia textului, ca sa nu se
lipeasca cifrele (Articolul 27<sup>1</sup> -> 271).

Plasare: aceste doua legi sint drept corporativ, nu perimetru CNPF/BNM, deci
merg in moldova-legal/, linga Codul civil, nu in cnpf/.
"""
from pathlib import Path
import subprocess, re, html as ihtml, hashlib, datetime
from lxml import html
try:
    import yaml
except Exception:
    yaml = None

ROOT = Path(r"C:\Users\harab\wiki")
RAW_DIR = ROOT / "raw" / "papers" / "moldova-legal"
META_DIR = ROOT / "_meta" / "imports" / "moldova-legal" / "legis-md-business"
META_DIR.mkdir(parents=True, exist_ok=True)
TODAY = datetime.date.today().isoformat()
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"

DOCS = {
    'L-135-2007': {'doc_id': '153674',
                   'title': 'Legea nr. 135/2007 privind societatile cu raspundere limitata'},
    'L-220-2007': {'doc_id': '155438',
                   'title': 'Legea nr. 220/2007 privind inregistrarea de stat a persoanelor '
                            'juridice si a intreprinzatorilor individuali'},
    # A treia sursa P1 din documentul 04, ultima care lipsea. doc_id gasit si verificat
    # 2026-09-04. Act din 1992, dar foloseste forma moderna "Articolul N", nu "Art.N. -",
    # deci extractorul il prinde. 28 de etichete <sup>, niciun span ridicat prin CSS.
    'L-845-1992': {'doc_id': '155963',
                   'title': 'Legea nr. 845/1992 cu privire la antreprenoriat si intreprinderi'},
    # Codurile. Codul fiscal poarta un CUPRINS de ~780 de linii care repeta fiecare titlu
    # de articol; vezi regula de suprimare a ancorarii din extract_doc. Numerotarea NU
    # reporneste pe titluri: in corp cele 353 de articole de baza sint unice.
    # Reimprospatat 2026-09-06 la 138613 (2026-07-01, LP318/2025), din 155071 (2026-06-25); vezi refresh_behind_2026-09-06.py.
    'COD-1163-1997': {'doc_id': '138613',
                      'title': 'Codul fiscal al Republicii Moldova nr. 1163/1997'},
    # Codul civil, 2026-09-06 seara: pina atunci textul venea din PDF (ingest 2026-07-13, ancorat
    # manual 2026-09-04, frontmatter doc_id 150561 = 2025-11-01). Trecut pe textul legis.md
    # 150498 @ 2026-04-01 (LP251/2025), prin refresh_behind_2026-09-06.py, lotul 2; inventarul de
    # articole identic (2657, aceleasi 14 lacune: 2047-2054 si cele sase abrogate prin LP251).
    # 5 <sup>, fara CUPRINS. Intrarea sta aici ca verify_business_law.py sa-l controleze.
    'CC-1107-2002': {'doc_id': '150498',
                     'title': 'Codul civil al Republicii Moldova nr. 1107/2002'},
    # Codul funciar nou, 2026-09-06 seara, la cererea lui Eugen, dupa ce HG-553-2024 (temei art. 58
    # alin. (10)) a aratat ca transmiterea si schimbul de terenuri nu mai au regulament al Guvernului.
    # Cautare in titlu 'codul funciar' (106 rezultate), rindul CF22/2024 marcat 'Modificat' trimite la
    # 154132, care este si capul istoricului (8 versiuni, 154132@2026-04-25, LP53/2026), fara versiune
    # viitoare, fara abrogare. In vigoare 07.03.2024. 25 <sup>, fara span CSS, fara CUPRINS,
    # 96 de ancore (79 de baza 1-79 fara lacune, 17 cu exponent), 13 capitole, fara titluri.
    'COD-22-2024': {'doc_id': '154132',
                    'title': 'Codul funciar al Republicii Moldova nr. 22/2024'},
    'COD-116-2018': {'doc_id': '150447',
                     'title': 'Codul administrativ al Republicii Moldova nr. 116/2018'},
    # Cele sapte coduri ramase din planul esuat de la 13 iulie 2026. Toate verificate
    # in prealabil: niciunul nu are cuprins, niciunul nu are ancore duplicate, toate
    # folosesc forma moderna "Articolul N". Cinci din sapte sint consolidari VIITOARE.
    # Reimprospatat 2026-09-06 la 155718 (2026-08-06, LP126/2026), din 152860 (2025-12-30).
    'COD-225-2003': {'doc_id': '155718', 'title': 'Codul de procedura civila al Republicii Moldova nr. 225/2003'},
    'COD-443-2004': {'doc_id': '156146', 'title': 'Codul de executare al Republicii Moldova nr. 443/2004'},
    'COD-95-2021':  {'doc_id': '154350', 'title': 'Codul vamal al Republicii Moldova nr. 95/2021'},
    'COD-154-2003': {'doc_id': '155882', 'title': 'Codul muncii al Republicii Moldova nr. 154/2003'},
    'COD-218-2008': {'doc_id': '155852', 'title': 'Codul contraventional al Republicii Moldova nr. 218/2008'},
    'COD-985-2002': {'doc_id': '156133', 'title': 'Codul penal al Republicii Moldova nr. 985/2002'},
    'COD-122-2003': {'doc_id': '156138', 'title': 'Codul de procedura penala al Republicii Moldova nr. 122/2003'},
    # Adaugata 2026-09-05. Nu este perimetru CNPF: este lege generala de publicitate si
    # protectie a consumatorului, deci merge in moldova-legal/, ca L-135-2007 si L-220-2007.
    # Motivul ingerarii: art. 4^1 alin. (9) din L-171-2012, introdus de L-177-2025, construieste
    # o prezumtie de publicitate inselatoare pe art. 3 din aceasta lege; fara ea prezumtia nu
    # poate fi ancorata. Verificat inainte de rulare pe HTML-ul descarcat: 13 etichete <sup>,
    # niciun span ridicat prin CSS, fara CUPRINS, 58 de ancore (53 de baza 1-53 fara lacune,
    # plus 11^1-11^4 si 32^1), fara ancore duplicate, consolidare 2026-08-14, deci trecuta.
    'L-62-2022': {'doc_id': '155339',
                  'title': 'Legea nr. 62/2022 cu privire la publicitate'},
    # Adaugata 2026-09-05, in aceeasi zi cu L-62-2022 si din acelasi motiv: art. 2 alin. (2)
    # din legea publicitatii isi ia criteriul de directionare teritoriala din art. 3 al acestui
    # act. ATENTIE LA DENUMIRE: legis.md da denumirea actuala "privind serviciile societatii
    # informationale" si denumirea precedenta "privind comertul electronic". Este acelasi act,
    # nr. 284 din 22.07.2004; celelalte legi din corpus il citeaza inca sub titlul vechi.
    # Verificat pe HTML inainte de rulare: 3 etichete <sup> si 4 span-uri ridicate prin CSS
    # (forma top:-Nem, prinsa de resolve_superscripts), fara CUPRINS, 29 de ancore
    # (28 de baza 1-28 fara lacune, plus 25^1), fara duplicate, consolidare 2026-02-14, trecuta.
    'L-284-2004': {'doc_id': '150486',
                   'title': 'Legea nr. 284/2004 privind serviciile societatii informationale '
                            '(fosta Legea comertului electronic)'},
    # Adaugata 2026-09-05. Metodologia AIR, a doua sursa a personei P4 din documentul 04,
    # singura care lipsea. Capcana: actul pe care il citeaza practica curenta, HG 23/2019
    # (doc_id 144735), a fost ABROGAT la 23.08.2024 chiar prin acest HG 574/2024, deci o AIR
    # intocmita dupa metodologia din 2019 se sprijina pe un act abrogat. Legatura cu L-100-2017
    # este dinamica: art. 2 (notiunea), art. 30 lit. d) si art. 31 alin. (3) trimit la
    # "metodologia aprobata de Guvern", fara sa o numeasca, deci trimiterea indica acum HG 574/2024.
    # Verificat pe HTML inainte de rulare: fara <sup>, fara span ridicat prin CSS, fara CUPRINS,
    # consolidare 2024-08-23 (trecuta), fara modificari, fara data de abrogare.
    # Structura in PUNCTE numerotate, nu articole: 7 puncte in hotarare, 9 in Metodologia
    # anexata, apoi lista de etape. Numerotarea REPORNESTE intre hotarare si anexa, deci o
    # ancorare la nivel de punct ar produce ancore duplicate. Ingerata cu zero ancore de
    # articol, ca HG-1170-2016 si HG-1171-2018. Consecinta de citare: o trimitere la
    # "pct. N din Metodologie" NU este ancorata. De ridicat cu Eugen.
    # Adaugata 2026-09-06 seara, la cererea lui Eugen, ca sa se verifice intinderea abrogarii
    # HG-1170-2016. Gasita prin cautare in titlu 'schimbarea destinatiei' (66 de rezultate), rindul
    # HG553/2024 marcat 'Modificat'; pagina actului are doua versiuni, 144532@2025-03-07 si
    # 150820@2025-10-18 (HG613/2025), cea din urma in vigoare azi, fara data de abrogare. Temei:
    # art. 58 alin. (10) din Codul funciar nr. 22/2024, NEINGERAT. Pct. 3 din hotarire abroga
    # HG 1170/2016 integral, 'cu modificarile ulterioare', fara dispozitii tranzitorii. Structura
    # in PUNCTE: 4 in hotarire, apoi 1-24 cu 1^1, 1^2 in Regulament, numerotarea REPORNESTE, deci
    # zero ancore de articol, ca HG-574-2024. 11 <sup>, fara span CSS, fara CUPRINS.
    'HG-553-2024': {'doc_id': '150820',
                    'title': 'Hotararea Guvernului nr. 553/2024 pentru aprobarea Regulamentului cu '
                             'privire la schimbarea destinatiei terenurilor cu destinatie agricola de '
                             'calitate superioara si a terenurilor destinate fondului forestier si '
                             'fondului apelor'},
    'HG-574-2024': {'doc_id': '144682',
                    'title': 'Hotararea Guvernului nr. 574/2024 cu privire la aprobarea '
                             'Metodologiei de analiza a impactului de reglementare'},
    # Adaugata 2026-09-05, lacuna descoperita la ingerarea HG-574-2024: este al doilea
    # temei al acelei hotarari si actul din care decurge mandatul Grupului de lucru al
    # Comisiei de stat, la care trimite pct. 7.3 din Metodologie. Fara ea, pasul de avizare
    # pentru proiectele care reglementeaza activitatea de intreprinzator nu poate fi ancorat.
    # Verificat pe HTML inainte de rulare: 3 etichete <sup>, toate la nivel de ALINEAT
    # (alin. (4^1) propriu, plus trimiteri la art. 11 alin. (2^1) si (2^2) din Legea 160/2011),
    # niciun span ridicat prin CSS, fara CUPRINS, 18 ancore distincte, fara duplicate,
    # consolidare 2024-07-05, deci trecuta.
    # Numerotare COMPLETA 1-21, fara lacune si fara niciun marcaj "abrogat".
    # Corectie de metoda, 2026-09-05. Verificarea prealabila raportase art. 3 si art. 8 ca
    # absente. Era fals. Cauza: verificarea inlocuise etichetele HTML cu un spatiu inainte de
    # a cauta "Articolul N.", iar acolo unde punctul sta intr-o eticheta separata rezulta
    # "Articolul 3 ." si tiparul nu se mai potriveste. Aceeasi clasa de eroare ca aplatizarea
    # exponentilor: marcajul se pierde la conversie, nu la sursa, doar ca aici produce o
    # LACUNA FALSA in loc de o citare falsa. Regula: o lacuna nu se consemneaza pe text
    # obtinut prin stergerea etichetelor, ci se confirma pe ancorele scrise de extractor.
    'L-235-2006': {'doc_id': '142654',
                   'title': 'Legea nr. 235/2006 cu privire la principiile de baza de '
                            'reglementare a activitatii de intreprinzator'},
    # Adaugata 2026-09-05, a patra veriga a aceluiasi lant: art. 26 alin. (1) din L-284-2004
    # trimite la organele de control in protectia consumatorilor "conform domeniilor de
    # competenta stabilite in Legea nr. 105/2003". Nu este doar o veriga procedurala: arts. 37
    # alin. (2) si 38 alin. (2) numesc EXPRES CNPF autoritate de supraveghere in protectia
    # consumatorilor pentru subiectii de la art. 4 alin. (2^1) din L-192-1998, deci actul intra
    # direct in harta de mandat a wiki-ului. Verificat inainte de rulare: 7 etichete <sup>,
    # niciun span ridicat prin CSS, fara CUPRINS, 75 de ancore (74 de baza 1-74 fara lacune,
    # plus 36^1), fara duplicate, toate titlurile au punct dupa numar, consolidare 2025-10-25.
    'L-105-2003': {'doc_id': '150997',
                   'title': 'Legea nr. 105/2003 privind protectia consumatorilor'},
    # Adaugata 2026-09-05. Inchide bucla deschisa de L-62-2022: art. 50 alin. (1) lit. a) al legii
    # publicitatii trimite la "atributiile prevazute de Legea concurentei nr. 183/2012", iar
    # art. 18 alin. (4) lit. a) califica publicitatea care este act de concurenta neloiala prin
    # raportare la aceeasi lege. Reciproca este in art. 32 lit. c) si art. 39 lit. f) de aici,
    # ambele cu ACEEASI LIMITA: publicitatea comerciala intra in competenta Consiliului
    # Concurentei doar "in cazul in care sunt afectate drepturile intreprinderilor".
    # Verificat pe HTML inainte de rulare: 41 de etichete <sup>, niciun span ridicat prin CSS,
    # fara CUPRINS, 110 ancore (95 de baza 1-95 fara lacune, plus 15 cu exponent), fara
    # duplicate, toate titlurile cu punct dupa numar, consolidare 2025-12-31, trecuta.
    'L-183-2012': {'doc_id': '152606',
                   'title': 'Legea concurentei nr. 183/2012'},
    # Adaugata 2026-09-05. A doua autoritate din art. 50 alin. (1) al legii publicitatii:
    # lit. b) trimite Consiliul Audiovizualului la "atributiile sale prevazute de Codul
    # serviciilor media audiovizuale pe domeniul publicitatii si al altor forme de comunicari
    # comerciale audiovizuale". Codul isi tine regimul propriu in cap. IX, arts. 62-72.
    # Prefix legis.md CSMA, nu LP, dar este COD, deci stem COD-174-2018, ca celelalte coduri.
    # Verificat pe HTML inainte de rulare: 66 de etichete <sup>, majoritatea la nivel de alineat
    # si litera (doar 4 articole cu exponent), niciun span ridicat prin CSS, fara CUPRINS,
    # 98 de ancore (94 de baza 1-94 fara lacune, plus 17^1, 25^1, 61^1, 61^2), fara duplicate,
    # toate titlurile cu punct dupa numar, consolidare 2026-06-24, trecuta, zero dispozitii
    # cu intrare in vigoare amanata.
    'COD-174-2018': {'doc_id': '150538',
                     'title': 'Codul serviciilor media audiovizuale al Republicii Moldova '
                              'nr. 174/2018'},
    # Adaugata 2026-09-05. Regulamentul privind continuturile audiovizuale, facut obligatoriu de
    # art. 62 alin. (1) si art. 75 alin. (3) lit. c) din COD-174-2018. NU este act al
    # Parlamentului: il emite Consiliul Audiovizualului, deci nu se cauta dupa numar de lege.
    # GASIT PRIN CAUTARE IN TITLU, cu o capcana proprie: endpointul de cautare in titlu este
    # getResults?search_string=<fraza>&search_type=1, iar fraza trebuie scrisa FARA DIACRITICE.
    # "continuturile audiovizuale" intoarce 13 randuri; "continuturile audiovizuale" cu diacritice
    # intoarce zero. Lista tipurilor de cautare vine de la https://www.legis.md/search_type/getlist
    # (1 = titlu, 2 = text).
    # DOUA GENERATII, verificate una cate una:
    #   RCA63/2021 (doc_id 125023) este textul aprobat prin Decizia 61/219 din 30.12.2019;
    #     acea decizie a fost ABROGATA la 30.05.2024, deci regulamentul acela este depasit.
    #   DCA61/2024 (doc_id 142648) aproba regulamentul CURENT, in vigoare din 05.05.2024,
    #     fara data de abrogare si fara modificari. Acesta se ingereaza.
    # Structura in PUNCTE numerotate, nu articole: 2 puncte in decizie, apoi 203 in Regulamentul
    # anexat, 8 capitole si 11 sectiuni. Numerotarea REPORNESTE intre decizie si anexa, deci o
    # ancorare la nivel de punct ar produce ancore duplicate. Ingerat cu zero ancore de articol,
    # ca HG-1170-2016, HG-1171-2018 si HG-574-2024. Consecinta de citare: o trimitere la
    # "pct. N din Regulament" NU este ancorata.
    'DCA-61-2024': {'doc_id': '142648',
                    'title': 'Decizia Consiliului Audiovizualului nr. 61/2024 cu privire la '
                             'aprobarea Regulamentului privind continuturile audiovizuale'},
    # Adaugata 2026-09-05. Trimisa de pct. 199 si 201 din DCA-61-2024: Consiliul Audiovizualului
    # asigura dreptul la replica "in conditiile CSMA si a prevederilor Legii nr. 64/2010".
    # Relevanta proprie, dincolo de veriga: arts. 24 si 25 asaza sarcina probatiunii si
    # prezumtiile in cauzele de defaimare, iar art. 4^1 alin. (7) din L-171-2012 declara alerta
    # CNPF, care numeste public persoane, necontestabila. Cele doua se ating direct.
    # Verificat pe HTML inainte de rulare: 2 etichete <sup>, niciun span ridicat prin CSS, fara
    # CUPRINS, 34 de ancore, numerotare 1-34 fara lacune, fara duplicate, fara exponenti de
    # articol, consolidare 2024-01-23, trecuta.
    # NOTA: art. 34 este scris `Articolul 34`, FARA punct. Este exact cazul pentru care a fost
    # reparat contorul din verify_business_law.py in aceeasi zi; inainte l-ar fi raportat drept
    # "33, range 1-33", adica o lacuna falsa la 34.
    'L-64-2010': {'doc_id': '141515',
                  'title': 'Legea nr. 64/2010 cu privire la libertatea de exprimare'},
    # ---- Perimetrul constructiilor, adaugat 2026-09-05. Lipsea complet din baza; o analiza
    # de contract de antrepriza din aceeasi zi a plecat cu trei pozitii neancorate.
    # PREFIX legis.md: CUC434/2023, nu LP. Este COD, deci stem COD-434-2023, ca celelalte coduri.
    # PREMISA VERIFICATA IN SURSA inainte de ingerare, art. 390:
    #   alin. (1) codul intra in vigoare "peste 12 luni de la data publicarii"; publicat
    #     30.01.2024, deci IN VIGOARE 30.01.2025. Nu 30.01.2026, cum circula in surse secundare.
    #   alin. (5) la acea data se abroga Legea 721/1996, Legea 835/1996 si Legea 163/2010.
    #   alin. (4) arts. 10, 11 si 14 din Legea 163/2010 erau deja abrogate de la PUBLICARE.
    #   CAPCANA DE FISA: legis.md scrie "Data intrarii in vigoare 30.01.2024", care este data
    #     exceptiilor din alin. (1) tezei a doua, nu a codului. Cine citeste fisa si nu art. 390
    #     dateaza gresit tot regimul cu un an.
    # Verificat pe HTML inainte de rulare: 59 etichete <sup>, TOATE la nivel de alineat sau
    # litera (niciun articol cu exponent), niciun span ridicat prin CSS, fara CUPRINS,
    # 390 de ancore, numerotare 1-390 COMPLETA, fara lacune, fara duplicate, fara forma N^X/Y,
    # consolidare 2026-08-06 (LP153/2026), trecuta, zero dispozitii cu intrare in vigoare amanata.
    # Structura: pe articole, nu pe puncte, deci ancorarea acopera tot actul.
    'COD-434-2023': {'doc_id': '155736',
                     'title': 'Codul urbanismului si constructiilor al Republicii Moldova '
                              'nr. 434/2023'},
    # Adaugata 2026-09-05, in aceeasi zi cu codul. Actul subordonat al codului, GASIT PRIN
    # TRIMITERILE DIN COD, nu din memorie: preambulul spune "In temeiul art. 129 alin. (6) si
    # art. 338 alin. (1) din Codul urbanismului si constructiilor nr. 434/2023".
    # Ce aproba: pct. 1.1 Regulamentul cu privire la atestarea specialistilor care desfasoara
    # activitati in constructii (anexa nr. 1) - acesta este regulamentul la care trimit art. 180
    # alin. (3) pentru dirigintele de santier si art. 187 alin. (4) pentru responsabilul tehnic;
    # pct. 1.2 Regulamentul privind verificarea documentatiei de proiect si expertiza tehnica
    # (anexa nr. 2); pct. 5 si anexa nr. 3 abroga lista de hotariri vechi.
    # CONSTATARE DE PERIMETRU: nu exista regulament de receptie a constructiilor sub cod.
    # HG 285/1996 (Regulamentul de receptie a constructiilor si instalatiilor aferente) a fost
    # ABROGATA prin HG726/2024, in vigoare 30.01.25, iar codul nu deleaga receptia catre niciun
    # regulament: o reglementeaza direct in arts. 192-215. Cautarea in text dupa "receptie" +
    # "regulament"/"Guvern" in COD-434-2023 nu intoarce nimic. De aceea se ingereaza un singur
    # act subordonat, nu doua.
    # Verificat pe HTML inainte de rulare: 29 etichete <sup>, niciun span ridicat prin CSS,
    # fara CUPRINS, ZERO ancore de articol, consolidare 2026-12-30, deci VIITOARE, cu 6
    # dispozitii care nu au intrat inca in vigoare (HG341/2026).
    # Structura in PUNCTE, nu articole: 211 puncte numerotate, iar numerotarea REPORNESTE intre
    # hotarire si cele trei anexe (punctele 1-25 si urmatoarele apar de mai multe ori), deci o
    # ancorare la nivel de punct ar produce ancore duplicate. Ingerata cu zero ancore, ca
    # HG-1170-2016, HG-1171-2018, HG-574-2024 si DCA-61-2024. Consecinta de citare, de spus in
    # orice raspuns: o trimitere la "pct. N din Regulamentul de atestare" NU este ancorata.
    'HG-743-2024': {'doc_id': '155190',
                    'title': 'Hotararea Guvernului nr. 743/2024 cu privire la asigurarea '
                             'calitatii in constructii (Regulamentul de atestare a '
                             'specialistilor, anexa nr. 1)'},
    # Adaugata 2026-09-05, seara. Regulamentul de demolare cerut de art. 322 alin. (4) din
    # COD-434-2023, ramas intrebare deschisa la prima trecere. GASIT, si nu unde il cauta codul.
    # CAPCANA CENTRALA: nu este emis in temeiul codului. Clauza proprie de adoptare spune
    # "In temeiul art. 439^6 alin. (5) din Codul contraventional nr. 218/2008". Este anterior
    # codului (2022 fata de 2023) si a fost adoptat pentru executarea masurii de siguranta a
    # demolarii dispuse de instanta - exact configuratia din art. 327 alin. (1) al codului.
    # Deci delegarea din art. 322 alin. (4) este implinita de un act care nu o invoca.
    # Consecinta de metoda: cautarea dupa temeiul legal NU l-ar fi gasit; l-a gasit cautarea
    # in titlu dupa "demolare a constructiilor neautorizate", fiindca titlul reia aproape
    # cuvant cu cuvant formula delegarii ("modul de demolare a constructiilor neautorizate").
    # Aliniat la cod prin HG27/2026: pct. 20 subpct. 1) trimite acum la art. 153 alin. (1)
    # lit. e) din cod, nu la art. 17 alin. (1) lit. f) din Legea 163/2010, abrogata.
    # Verificat pe HTML inainte de rulare: 7 etichete <sup>, niciun span ridicat prin CSS,
    # fara CUPRINS, ZERO ancore de articol, consolidare 2026-03-01, trecuta, fara dispozitii
    # amanate, fara data de abrogare.
    # Structura in PUNCTE: 34 de puncte, iar numerotarea REPORNESTE intre hotarire (pct. 1-2)
    # si Regulamentul anexat, deci punctele 1 si 2 apar de doua ori. Ingerata cu zero ancore,
    # ca HG-743-2024. "pct. N" NU este ancorat.
    'HG-582-2022': {'doc_id': '152829',
                    'title': 'Hotararea Guvernului nr. 582/2022 pentru aprobarea Regulamentului '
                             'cu privire la modul de demolare a constructiilor neautorizate si '
                             'de defrisare a arborilor si arbustilor'},
    # Adaugata 2026-09-05. Intrebarea deschisa nr. 2 de la ingerarea perimetrului constructiilor:
    # art. 387 alin. (3) din COD-434-2023 trimite la ea pentru inregistrarea caselor individuale,
    # iar legatura dintre procesul-verbal de receptie si inscrierea dreptului in Registrul
    # bunurilor imobile nu putea fi ancorata fara ea.
    # ATENTIE LA TITLU: legis.md da denumirea ca "LEGE Nr. 1543 din 25.02.1998 cadastrului
    # bunurilor imobile", fara cuvantul "Legea" si fara "privind" - cuvantul "Legea" sta in
    # campul TIPUL. O cautare dupa "Legea cadastrului bunurilor imobile" ca fraza exacta nu o
    # intoarce; cautarea dupa "cadastrul bunurilor imobile" da 65 de rezultate, iar actul de baza
    # este singurul rand cu prefixul LP1543.
    # REPUBLICATA: data publicarii din fisa este 02.04.2021 (MO 88-95 art. 79), nu 1998; data
    # intrarii in vigoare ramane 21.05.1998.
    # Verificat pe HTML inainte de rulare: 129 etichete <sup>, niciun span ridicat prin CSS,
    # fara CUPRINS, 99 de ancore (61 de baza, numerotate 1-61 fara lacune, plus 38 cu exponent),
    # fara duplicate, fara forma N^X/Y.
    # CONSOLIDARE VIITOARE: 2027-01-01 (LP176/2025), cu 6 dispozitii care nu sint inca in
    # vigoare. De verificat in registrul in-force inainte de a cita orice articol de aici.
    'L-1543-1998': {'doc_id': '150226',
                    'title': 'Legea cadastrului bunurilor imobile nr. 1543/1998'},
    # Adaugata 2026-09-09, la cererea lui Eugen, din lista de ingest a spetei mostenitorului unui
    # actionar de banca (8 septembrie): procedura succesorala, certificatul de mostenitor si
    # certificatul de calitate de mostenitor (art. 2548 alin. (3) Cod civil) se fac dupa aceasta
    # lege. Gasita prin cautare in titlu "procedura notariala" (6 rinduri; actul de baza LP246/2018
    # "Modificat", plus doua decizii de inadmisibilitate ale Curtii, DCC36/2022 si DCC92/2026, care
    # NU sint anulari si nu lasa marcaje). CAPCANA DE VERSIUNE: rindul de cautare trimite la
    # 150742 (01.11.2025, LP222/2025), dar istoricul are deasupra 137680 @ 23.06.2026 (LP126/2023,
    # intrare in vigoare aminata trei ani, de aceea doc_id-ul e mai mic desi versiunea e mai noua),
    # in vigoare azi: 97 de "Articolul" fata de 96, 15 <sup> fata de 3, 33 de marcaje "in vigoare
    # 23.06.26". Se ingereaza 137680. Fara CUPRINS, fara span CSS.
    'L-246-2018': {'doc_id': '137680',
                   'title': 'Legea nr. 246/2018 privind procedura notariala'},
    # Adaugata 2026-09-06, pasul 3 al planului de extindere a perimetrului de drept intern.
    # Nivelul 1 al ierarhiei surselor, absent din baza pana acum. PREFIX NOU: CONST-.
    # Prefix legis.md CRM1/1994, tipul actului CONSTITUŢIA, autoritatea PARLAMENTUL.
    # GASIT PRIN CAUTARE IN TITLU ("constitutia republicii moldova", fara diacritice): 234 de
    # rezultate, aproape toate acte de modificare, avize si decizii ale Curtii; actul de baza
    # este singurul rand cu prefixul CRM si sta pe ultima pagina, fiind cel mai vechi.
    # Verificat pe pagina actului, nu din lista: doc_id 145723 este cea mai noua din 19 versiuni
    # (145723@2024-11-13), REPUBLICATA 13.11.2024 (MO 466 art. 635), in vigoare din 19.08.1994,
    # fara data de abrogare; ultima modificare Legea nr. 244 din 20.10.24, in vigoare 05.11.24.
    # CAPCANA DE FISA: republicarea nu are randul MODIFICAT si nici "Versiune in vigoare din";
    # antetul spune "Modificată şi completată prin legile Republicii Moldova:" urmat de lista.
    # extract_doc cade pe rindul "Data modificarii" din fisa, deci consolidation_date iese
    # 2024-11-05 (intrarea in vigoare a LP244/2024), nu 2024-11-13 (data republicarii).
    # Verificat pe HTML inainte de rulare: 11 etichete <sup>, niciun span ridicat prin CSS,
    # fara CUPRINS. Structura pe articole: 143 numerotate, plus dispozitiile finale si
    # tranzitorii numerotate cu cifre romane (Articolul I - VIII), pe care regexul de ancorare
    # le prinde ca la L-177-2025 si L-178-2020. Titluri cu exponent ("Capitolul III1",
    # "Titlul V1") vin din <sup> si se rezolva in ^1.
    'CONST-1994': {'doc_id': '145723',
                   'title': 'Constitutia Republicii Moldova din 29.07.1994 (republicata 2024)'},
    # ---- Lotul A, corporativ, pasul 4 al planului din 2026-09-06. Toate gasite prin cautare in
    # titlu fara diacritice si verificate pe pagina actului (istoric de versiuni, fisa).
    # legis.md da denumirea "LEGE Nr. 149 din 29.06.2012 insolvabilităţii", fara "Legea" si fara
    # "privind" (aceeasi trunchiere ca la L-1543-1998). 187 de rezultate la "insolvabilitatii";
    # actul de baza este singurul rand LP149/2012. 152605 este cea mai noua din versiuni
    # (2025-12-31, LP330/2025). HTML de 1 MB, cel mai mare act de lege din corpus dupa coduri.
    # 55 etichete <sup>, fara span CSS, fara CUPRINS. In vigoare 13.03.2013, fara abrogare.
    'L-149-2012': {'doc_id': '152605', 'title': 'Legea insolvabilitatii nr. 149/2012'},
    # 15 rezultate; singurul rand LP160/2011. CONSOLIDARE VIITOARE 2029-01-01 (LP159 din 30.07.26,
    # in vigoare 01.01.29), cu alte versiuni viitoare la 2027-01-23 si 2027-05-21 intre azi si ea.
    # Ingerata ca L-1134-1997 (2028): cea mai noua consolidare, registrul in-force preia
    # dispozitiile amanate. 51 etichete <sup>, fara span CSS, fara CUPRINS. In vigoare 01.01.2012.
    # 2026-09-06 seara, decizia lui Eugen: reingerata la versiunea IN VIGOARE AZI, 151257 @
    # 2026-08-29 (LP199/2025), nu la 156152 (2029). Istoricul are cinci consolidari viitoare:
    # 149496@2026-12-28, 150231@2027-01-01, 154051@2027-01-23, 154478@2027-05-21, 156152@2029-01-01.
    'L-160-2011': {'doc_id': '151257',
                   'title': 'Legea nr. 160/2011 privind reglementarea prin autorizare a '
                            'activitatii de intreprinzator'},
    # CAPCANA DE LISTA, gasita aici: rindul din rezultatele cautarii trimite la doc_id 152529
    # (2025-12-31), dar pagina actului are doua consolidari mai noi, 149634@2026-07-31 si
    # 151146@2026-08-28 (LP201 din 10.07.25, in vigoare 28.08.26). Cea in vigoare azi este
    # 151146, cu doc_id MAI MIC decit cel vechi: numarul doc_id nu este cronologic. Deci doc_id-ul
    # din lista NU este garantat cel curent; se citeste istoricul de versiuni de pe pagina.
    # Denumirea in fisa: "LEGE Nr. 131 din 08.06.2012 privind controlul de stat" (trunchiata).
    # 47 etichete <sup>, fara span CSS, fara CUPRINS. In vigoare 31.01.2012 (asa spune fisa,
    # desi publicata 31.08.2012; de verificat pe text), fara abrogare.
    'L-131-2012': {'doc_id': '151146',
                   'title': 'Legea nr. 131/2012 privind controlul de stat asupra activitatii '
                            'de intreprinzator'},
    # ---- Lotul B, administrativ, pasul 4 al planului din 2026-09-06.
    # 281 de rezultate la "administratia publica locala"; singurul rand LP436/2006. 155118 este
    # cea mai noua din 76 de versiuni (2026-06-26, LP108/2026). 88 etichete <sup>, fara span CSS,
    # fara CUPRINS. In vigoare 09.03.2007 (fisa), fara abrogare.
    'L-436-2006': {'doc_id': '155118',
                   'title': 'Legea nr. 436/2006 privind administratia publica locala'},
    # 58 de rezultate; singurul rand LP158/2008, care trimite la 156075 (2026-08-28, in vigoare
    # azi). Istoricul are doua consolidari mai noi: 155439@2026-09-13 (LP154 din 30.07.26, aceeasi
    # lege si aceeasi data ca la COD-218-2008) si 155884@2028-07-01. Se ingereaza 155439, ca la
    # Codul contraventional: intra in vigoare peste o saptamina, iar registrul in-force preia cele
    # 29 de dispozitii amanate. Cea din 2028 ramine viitoare, consemnata in manifest. 71 etichete
    # <sup>, fara span CSS, fara CUPRINS. Fisierul 156075 descarcat inainte de a alege a ramas in
    # Downloads, nefolosit.
    'L-158-2008': {'doc_id': '155439',
                   'title': 'Legea nr. 158/2008 cu privire la functia publica si statutul '
                            'functionarului public'},
    # 6 rezultate; LP148/2023, o singura versiune, NEMODIFICATA, fara rindul MODIFICAT, deci
    # consolidation_date iese din "Data intrarii in vigoare": 08.01.2024. Zero <sup>, fara CUPRINS.
    # Abroga vechea Lege 982/2000 privind accesul la informatie (de verificat pe text la ingerare).
    'L-148-2023': {'doc_id': '137908',
                   'title': 'Legea nr. 148/2023 privind accesul la informatiile de interes public'},
    # ATENTIE: legis.md o marcheaza "Abrogat", cu Data abrogarii 01.01.2027. Succesoarea este
    # Legea nr. 325/2025 privind achizitiile publice (LP325/2025, doc_id 152974, publicata
    # 29.12.2025), insotita de LP20/2026 privind remediile si caile de atac (doc_id 153618).
    # Niciuna nu este in plan; decizia de a le ingera este a lui Eugen. 131/2015 este INCA in
    # vigoare azi si sta in planul aprobat, deci se ingereaza: 155117@2026-06-26 (LP101/2026) este
    # versiunea in vigoare; 153138@2027-01-01 este versiunea de dupa abrogare. 201 rezultate la
    # "achizitiile publice"; singurul rand LP131/2015. 7 etichete <sup>, fara span CSS, fara CUPRINS.
    # Succesoarele, ingerate 2026-09-06 seara la decizia lui Eugen. 325/2025: 91 de articole fara
    # lacune, 1 <sup>, fara CUPRINS, fara rind MODIFICAT; "Data intrarii in vigoare" 01.01.2027,
    # deci consolidare VIITOARE si tot actul e neintrat in vigoare azi. 20/2026: 29 de articole,
    # fara <sup>, in vigoare 01.04.2026 dupa fisa (de verificat pe dispozitiile finale).
    'L-325-2025': {'doc_id': '152974',
                   'title': 'Legea nr. 325/2025 privind achizitiile publice'},
    'L-20-2026': {'doc_id': '153618',
                  'title': 'Legea nr. 20/2026 privind remediile si caile de atac in materie de '
                           'atribuire a contractelor de achizitii publice'},
    'L-131-2015': {'doc_id': '155117',
                   'title': 'Legea nr. 131/2015 privind achizitiile publice (abrogata de la '
                            '01.01.2027 prin Legea 325/2025)'},
    # ---- Lotul C, profesia, pasul 4 al planului din 2026-09-06.
    # 53 de rezultate la "avocatura"; singurul rand LP1260/2002 trimite la 153429, a carui data
    # de versiune este 2030-01-01: este consolidarea LP10 din 12.02.26, "in vigoare la data
    # aderarii Republicii Moldova la Uniunea Europeana", pe care legis.md o codifica cu o data
    # fictiva. Se ingereaza versiunea IN VIGOARE AZI, 146148@2025-01-07 (LP284 din 05.12.24, forma
    # electronica a mandatului avocatului), nu cea conditionata de aderare. Republicata 04.09.2010
    # (MO 159 art. 582), in vigoare 13.12.2002. 38 etichete <sup>, fara span CSS, fara CUPRINS.
    'L-1260-2002': {'doc_id': '146148',
                    'title': 'Legea nr. 1260/2002 cu privire la avocatura'},
    # 42 de rezultate; singurul rand LP198/2007. 155726 este cea mai noua din 21 de versiuni
    # (2026-08-06, LP126/2026). 58 etichete <sup>, fara span CSS, fara CUPRINS. In vigoare 05.10.2007.
    'L-198-2007': {'doc_id': '155726',
                   'title': 'Legea nr. 198/2007 cu privire la asistenta juridica garantata de stat'},
    # 49 de rezultate; singurul rand LP514/1995. 156079 este cea mai noua din 56 de versiuni
    # (2026-08-28, LP197/2026). Titlul poarta asterisc: "privind organizarea judecatoreasca*".
    # 24 etichete <sup>, fara span CSS, fara CUPRINS. In vigoare 19.10.1995.
    'L-514-1995': {'doc_id': '156079',
                   'title': 'Legea nr. 514/1995 privind organizarea judecatoreasca'},
    # PREFIX NOU UA-, actele Uniunii Avocatilor (D5 din planul din 2026-09-06). Pe legis.md:
    # tipul STATUTUL, autoritatea UNIUNEA AVOCATILOR DIN REPUBLICA MOLDOVA, identificator
    # SUARM0/2011, publicat 08.04.2011 (MO 54-57 art. 302). doc_id-ul din plan, 86850, EXISTA dar
    # este consolidarea din 2012 (MUARM220 din 24.02.12), a doua din sapte; cea curenta este
    # 134919@2022-05-27 (HUA19-01 din 27.05.22, MO194-200/01.07.22). Structura PE ARTICOLE
    # (74 de linii "Articolul", zero puncte numerotate), deci se ancoreaza ca o lege. 19 etichete
    # <sup>, fara span CSS, fara CUPRINS. Codul deontologic si Regulamentul stagiului NU sint pe
    # legis.md (cautari in titlu: "codul deontologic" 12 rezultate, "avocatilor" 169, "avocat
    # stagiar" 4, "stagiului profesional" 3, "stagiului" 53; niciuna nu le contine): lacune D5.
    'UA-STATUT-2011': {'doc_id': '134919',
                       'title': 'Statutul profesiei de avocat (Uniunea Avocatilor, 29.01.2011)'},
}

DATE_RE = re.compile(r'(\d{1,2})[.\-/](\d{1,2})[.\-/](\d{2,4})')


def resolve_superscripts(html_text):
    """Rezolva <sup>...</sup> in HTML-ul brut, inainte de extractia textului.

    Contextul. legis.md marcheaza exponentii ca <sup>1</sup>. Daca ii lasam asa,
    lxml .text_content() lipeste cifrele: "Articolul 27<sup>1</sup>" devine
    "Articolul 271", iar "(1<sup>1</sup>)" devine "(11)". Ambele sint citari false.

    In cele doua acte exponentii apar in patru roluri, toate cu valoare juridica:
      - titluri de articol      Articolul 27<sup>1</sup>
      - numere de alineat       (1<sup>1</sup>)
      - litere de punct         f<sup>1</sup>)
      - trimiteri la capitole   cap. VI<sup>1</sup>

    Primeste HTML-ul brut ca string si intoarce acelasi HTML cu fiecare <sup>
    inlocuit de o forma textuala. Restul scriptului cere ca in rezultat sa nu mai
    existe niciun "<sup" (altfel se opreste cu eroare).

    Decizie 2026-09-04 (Eugen): forma ^N peste tot, in toate cele patru roluri.
    Motivul: se potriveste cu ancorele deja existente in corpus (## Articolul 146^1)
    si se cauta usor. Costul asumat: celelalte 15 fisiere raw au inca exponentii de
    alineat aplatizati, deci aceste doua fisiere sint corecte dar diferite de restul.

    Implementare: se prinde eticheta de deschidere cu eventuale atribute, continutul
    negreedy peste linii, se curata etichetele interne si entitatile, iar un <sup>
    gol dispare in loc sa lase un accent circumflex singur.
    """
    def repl(m):
        inner = re.sub(r'<[^>]*>', '', m.group(1))
        inner = ihtml.unescape(inner).replace(chr(160), ' ').strip()
        return f'^{inner}' if inner else ''

    # 1. Forma clasica: <sup>N</sup>.
    html_text = re.sub(r'<sup(?:\s[^>]*)?>(.*?)</sup>', repl, html_text, flags=re.S | re.I)

    # 2. Exponent prin CSS, gasit 2026-09-04 in consolidarea curenta a L-171-2012:
    #    Articolul 47<span style="... position: relative; vertical-align: baseline;
    #    top: -0.5em;">1</span>. Este ridicat vizual prin `top`, nu prin `vertical-align`,
    #    deci o cautare dupa `vertical-align: super` nu il gaseste. Semnul sigur este
    #    deplasarea negativa pe `top`.
    html_text = re.sub(r'<span[^>]*top:\s*-[0-9.]+em[^>]*>(.*?)</span>', repl, html_text,
                       flags=re.S | re.I)
    return html_text


def clean_line(s):
    s = ihtml.unescape(s or '').replace('\xa0', ' ')
    return re.sub(r'[ \t\r\f\v]+', ' ', s).strip()


def norm_year(y):
    y = int(y)
    return (2000 + y if y <= 40 else 1900 + y) if y < 100 else y


def all_dates(text):
    return [f"{norm_year(c):04d}-{int(b):02d}-{int(a):02d}"
            for a, b, c in DATE_RE.findall(text or '')]


def usable(data):
    """Un showdetails valid contine documentul si nu este pagina de verificare Cloudflare."""
    return bool(data) and 'id="contentdoc"' in data and 'Just a moment' not in data[:3000]


def fetch(doc_id):
    """Aduce showdetails-ul actului: intii prin curl, iar daca nu se poate, din cache-ul de pe disc.

    Din 2026-09-05 dupa-amiaza legis.md sta in spatele unei verificari Cloudflare care
    blocheaza curl (raspunsul este pagina "Just a moment", cu rc=0, deci un cod de retur
    curat NU inseamna ca avem documentul). Ruta de rezerva este cea folosita la P8 pentru
    legile bancare, vezi _meta/imports/bnm/ingest_bnm_ro.py: HTML-ul se ia din Chrome, dupa
    ce Eugen trece verificarea, si se pune in META_DIR ca showdetails-<doc_id>.html.
    Diferenta fata de P8: acolo s-a serializat DOM-ul (document.documentElement.outerHTML),
    aici se ia raspunsul serverului printr-un fetch same-origin din pagina, deci octetii sint
    cei originali, exact ce astepta extractorul scris pentru curl.

    Doua reguli de siguranta, ambele invatate aici:
      1. curl NU mai scrie direct peste fisierul din cache. Scria, si atunci o rulare blocata
         de Cloudflare inlocuia HTML-ul bun cu pagina de verificare, adica distrugea singura
         copie a sursei. Se descarca intr-un fisier temporar si se promoveaza doar la reusita.
      2. Cache-ul se foloseste doar daca trece usable(); altfel se opreste cu eroare, ca sa nu
         ingeram o pagina de verificare drept text de lege.
    """
    url = f"https://www.legis.md/cautare/showdetails/{doc_id}"
    out = META_DIR / f"showdetails-{doc_id}.html"
    tmp = META_DIR / f"showdetails-{doc_id}.html.part"
    res = subprocess.run(['curl', '-sL', '--max-time', '120', '-A', UA, url, '-o', str(tmp)],
                         capture_output=True, text=True)
    data = tmp.read_text(encoding='utf-8', errors='replace') if tmp.exists() else ''
    if res.returncode == 0 and usable(data):
        tmp.replace(out)
        return url, data, out
    tmp.unlink(missing_ok=True)

    cached = out.read_text(encoding='utf-8', errors='replace') if out.exists() else ''
    if usable(cached):
        print(f"  [cache] curl blocat (Cloudflare); folosesc {out.name} luat din Chrome")
        return url, cached, out
    raise RuntimeError(
        f"fetch failed for {doc_id}: rc={res.returncode} size={len(data)}; "
        f"nici cache utilizabil in {out}. Ia HTML-ul din Chrome (vezi docstring).")


def extract_doc(data):
    doc = html.fromstring(data)
    content = doc.xpath('//*[@id="contentdoc"]')[0]
    meta_nodes = doc.xpath('//*[@id="contentdoc_act"]')
    meta_pairs = []
    if meta_nodes:
        for tr in meta_nodes[0].xpath('.//tr'):
            cells = [c for c in (clean_line(x.text_content()) for x in tr.xpath('./th|./td')) if c]
            if len(cells) >= 2:
                meta_pairs.append((cells[0].rstrip(':'), cells[-1]))
    lines = [x for x in (clean_line(x) for x in content.text_content().splitlines()) if x]

    official_title = next((v for k, v in meta_pairs if 'Denumirea deplina actuala' in k
                           or 'Denumirea deplin' in k), '')
    if not official_title:
        for i, l in enumerate(lines[:10]):
            # "LEGE Nr. 135 din ..." pentru legi, "COD Nr. 1163 din ..." pentru coduri
            if l.lower().startswith(('lege nr', 'cod nr')) and i + 1 < len(lines):
                official_title = f"{l} {lines[i+1]}"
                break
    latest_line = ''
    for i, l in enumerate(lines[:60]):
        if l == 'MODIFICAT' and i + 1 < len(lines):
            latest_line = lines[i + 1]
            break
        if 'Versiune in vigoare din' in l or 'Versiune \u00een vigoare din' in l:
            latest_line = l
            break
    if not latest_line:
        latest_line = next((v.split('\n')[0].strip() for k, v in meta_pairs
                            if 'Data modific' in k), '')
    dates = all_dates(latest_line)
    consolidation_date = (dates[-1] if 'vigoare' in latest_line.lower()
                          else (dates[0] if dates else None))
    # Actele nemodificate niciodata nu au rindul "Data modificarii" in fisa, deci nu
    # exista nicio data de derivat. Fallback-ul anterior punea TODAY, adica data rularii.
    # Este gresit din doua motive: pretinde o actualitate care nu a fost verificata, si
    # scoate actul din controlul de vechime, fiindca va parea mereu proaspat. Corect este
    # data intrarii in vigoare: daca actul nu a fost modificat, textul de astazi este cel
    # de la adoptare. Defect prins la ingerarea HG-574-2024, 2026-09-05.
    never_amended = not consolidation_date
    if never_amended:
        eif = next((v for k, v in meta_pairs if 'Data intr' in k), '')
        eif_dates = all_dates(eif)
        consolidation_date = eif_dates[0] if eif_dates else TODAY

    # Codurile poarta un CUPRINS care repeta fiecare titlu de articol inainte de corp.
    # Daca il ancoram, fiecare articol capata doua ancore identice si citarea devine
    # ambigua. Solutia: NU stergem cuprinsul, textul ramine neatins, dar suprimam
    # ancorarea intre marcajul CUPRINS si formula de adoptare. Codul fiscal are 359 de
    # titluri in cuprins si 353 in corp; fara aceasta regula ar rezulta ~350 de ancore
    # duplicate. Suprimarea se aplica doar cind ambele repere exista, in aceasta ordine.
    toc_from = toc_to = -1
    # Egalitate stricta, nu startswith: Codul de procedura civila are un titlu de capitol
    # "UZUCAPIUNEA DREPTULUI CONTRAR / CUPRINSULUI REGISTRULUI DE PUBLICITATE", care ar
    # fi trecut drept marcaj de cuprins. Aici scapa fiindca apare dupa formula de adoptare,
    # dar intr-un act viitor ar putea aparea inainte si ar suprima ancorarea pe nedrept.
    cup = next((i for i, l in enumerate(lines)
                if l.replace(' ', '').upper() == 'CUPRINS'), -1)
    adopt = next((i for i, l in enumerate(lines)
                  if re.search(r'Parlamentul adopt', l, flags=re.I)), -1)
    if cup != -1 and adopt > cup:
        toc_from, toc_to = cup, adopt

    md_lines = []
    for i, l in enumerate(lines):
        in_toc = toc_from <= i <= toc_to
        if in_toc:
            md_lines.append(l)
        elif re.match(r'^(TITLUL|Titlul)\s+[IVXLCDM]+(\^\d+)?\b(?![,])', l):
            # \b inainte de lookahead este obligatoriu: fara el, "Titlul VII," trece, fiindca
            # [IVXLCDM]+ da inapoi la "VI" si urmatorul caracter este "I", nu virgula.
            # Corectie 2026-09-06, la ingerarea CONST-1994. Art. VIII din dispozitiile finale ale
            # Constitutiei are ca text intreg fraza "Titlul VII, Dispoziţii finale şi tranzitorii,
            # se consideră parte integrantă a prezentei Constituţii...". Regula veche, orice linie
            # care incepe cu "Titlul ", o lua drept titlu de structura: articolul aparea gol si
            # textul lui aparea ca ancora "## Titlul VII, ...". Textul nu era atins, structura era
            # falsa. Regula noua cere un numeral roman dupa "Titlul" si refuza virgula imediat dupa
            # el: un titlu de structura nu continua cu virgula, o trimitere in fraza da.
            md_lines += ['', f"## {l}"]
        elif re.match(r'^T i t l u l\s+[IVXLCDM]+(\^\d+)?\b(?![,])', l) \
                or re.match(r'^(Cartea|CARTEA)\s+(a\s+\S+|[iî]nt[aiîâ]i)\s*$', l):
            # Codul civil pe legis.md (150498, 2026-09-06): titlurile sint scrise cu litere
            # spatiate, "T i t l u l IV", iar cartile ca "Cartea intai", "Cartea a doua", fara
            # numeral. Ancorarea manuala din 4 septembrie le avea pe toate 27 (5 carti, 22 de
            # titluri); fara aceasta regula textul legis.md le pierdea. Textul liniei nu se
            # schimba, ancora reia linia asa cum este.
            md_lines += ['', f"## {l}"]
        elif re.match(r'^Capitolul\s+', l, flags=re.I):
            md_lines += ['', f"## {l}"]
        elif re.match(r'^Sec\u0163iunea|^Sec\u021biunea', l, flags=re.I):
            md_lines += ['', f"### {l}"]
        elif re.match(r'^Articolul\s+[0-9IVXLCDM]+(\^\d+)?[a-zA-Z]?\b', l, flags=re.I):
            md_lines += ['', f"## {l}"]
        else:
            md_lines.append(l)
    return {
        'official_title': official_title,
        'meta_pairs': meta_pairs,
        'lines': lines,
        'text_markdown': '\n'.join(md_lines).strip() + '\n',
        'latest_line': latest_line,
        'consolidation_date': consolidation_date,
        'never_amended': never_amended,
        # numara ancorele efectiv scrise, nu si repetarile din cuprins
        'article_count': len([l for l in md_lines
                              if re.match(r'^## Articolul\s+', l, flags=re.I)]),
        'char_count': len(content.text_content()),
    }


def future_pending(parsed):
    """Dispozitiile care poarta data de intrare in vigoare a unei consolidari VIITOARE.

    legis.md serveste uneori textul care va fi in vigoare la o data ulterioara, incorporand
    modificari inca neintrate in vigoare. Este o capcana mai rea decat vechimea, fiindca
    fisierul pare curent. Intoarce lista marcajelor afectate, goala daca data consolidarii
    nu este in viitor.
    """
    cdate = parsed['consolidation_date']
    if cdate <= TODAY:
        return []
    dmy = f"{cdate[8:10]}.{cdate[5:7]}.{cdate[2:4]}"
    return [re.sub(r'\s+', ' ', l).strip() for l in parsed['lines']
            if f"în vigoare {dmy}" in l and l.lstrip().startswith('[')]


def make_raw(stem, spec, parsed, show_url):
    sup_arts = sorted({m for l in parsed['lines']
                       for m in re.findall(r'^Articolul (\d+\^\d+)', l)},
                      key=lambda x: (int(x.split('^')[0]), int(x.split('^')[1])))
    pending = future_pending(parsed)
    body = [
        f"# raw/{stem} \u2014 text legis.md consolidat/curent", '',
        '> **TEXT LEGIS.MD RO \u2014 extras din `showdetails` \u0219i p\u0103strat pentru audit.** '
        'Nu corectez \u0219i nu armonizez t\u0103cut textul; pentru neconcordan\u021be cu amendamente '
        'ulterioare, p\u0103strez marcaje `[de verificat]` \u00een paginile wiki.', '',
        f"- **Surs\u0103 de referin\u021b\u0103:** https://www.legis.md/cautare/getResults?doc_id={spec['doc_id']}&lang=ro",
        f"- **Endpoint folosit:** {show_url}",
        f"- **doc_id legis.md:** {spec['doc_id']}",
        f"- **Titlu oficial detectat:** {parsed['official_title'] or spec['title']}",
        (f"- **consolidare legis.md:** {parsed['consolidation_date']} \u2014 actul nu a fost "
         f"modificat niciodat\u0103; fi\u0219a nu con\u021bine r\u00e2ndul \u201eData modific\u0103rii\u201d, "
         f"deci textul de ast\u0103zi este cel de la intrarea \u00een vigoare."
         if parsed.get('never_amended') else
         f"- **consolidare legis.md:** {parsed['consolidation_date']} \u2014 derivat\u0103 din prima "
         f"linie de modificare/versiune disponibil\u0103: {parsed['latest_line'] or 'n/a'}"),
        f"- **articole detectate:** {parsed['article_count']}",
        f"- **caractere text extras:** {parsed['char_count']}",
        f"- **exponen\u021bi de articol p\u0103stra\u021bi ca `^N`:** "
        f"{', '.join(sup_arts) if sup_arts else 'niciunul'}. Exponen\u021bii de alineat "
        f"\u0219i de liter\u0103 sînt p\u0103stra\u021bi \u00een corpul textului.", '',
        '## Fi\u0219a actului juridic \u2014 extras metadata', '',
    ]
    # 2026-09-06, la ingerarea L-325-2025: un act poate fi INTREG neintrat in vigoare, cu
    # consolidarea egala cu data intrarii in vigoare si fara niciun marcaj [Art.N ...]. Pina
    # aici avertismentul si flagul din frontmatter depindeau de existenta marcajelor, deci un
    # asemenea act trecea drept curent in blocul de acoperire, desi nu binde nicaieri.
    whole_act_future = (not pending) and parsed['consolidation_date'] > TODAY
    if whole_act_future:
        body[-2:-2] = ['', f"> **ATENȚIE, ACT NEINTRAT ÎN VIGOARE.** Consolidarea este datată "
                           f"**{parsed['consolidation_date']}**, ulterioară zilei de {TODAY}, "
                           f"și fișa nu conține niciun marcaj de dispoziție amânată: data este "
                           f"cea a intrării în vigoare a actului întreg. Nicio dispoziție de mai "
                           f"jos nu se aplică astăzi. Verificați articolul de dispoziții finale.", '']
    if pending:
        warn = ['', f"> **ATENȚIE, CONSOLIDARE VIITOARE.** Textul de mai jos este versiunea "
                    f"care va fi în vigoare la **{parsed['consolidation_date']}**, nu cea de "
                    f"astăzi, {TODAY}. Următoarele {len(pending)} dispoziții apar "
                    f"modificate, dar modificarea **nu a intrat încă în vigoare**:", '']
        warn += [f"> - `{p}`" for p in pending]
        warn += ['', '> Verificați data intrării în vigoare înainte de a cita '
                     'oricare dintre ele.', '']
        body[-2:-2] = warn
    if parsed['meta_pairs']:
        body += ['| C\u00e2mp | Valoare |', '|---|---|']
        body += [f"| {k.replace('|', '/')} | {v.replace('|', '/')} |" for k, v in parsed['meta_pairs']]
    else:
        body.append('_Fi\u0219a metadata nu a putut fi parsat\u0103 tabelar._')
    body += ['', '## Text integral extras din legis.md', '', parsed['text_markdown']]
    body_text = '\n'.join(body).strip() + '\n'
    fm = {
        'source_url': f"https://www.legis.md/cautare/getResults?doc_id={spec['doc_id']}&lang=ro",
        'showdetails_url': show_url,
        'ingested': TODAY,
        'sha256': hashlib.sha256(body_text.encode('utf-8')).hexdigest(),
        'source_type': 'legal-text',
        'publisher': 'legis.md / Ministerul Justi\u021biei al Republicii Moldova',
        'language': 'ro',
        'doc_id': str(spec['doc_id']),
        'instrument_id': stem,
        'official_title_detected': parsed['official_title'] or spec['title'],
        'consolidation_date': parsed['consolidation_date'],
        'latest_modification_line': parsed['latest_line'] or '',
        'full_text': True,
        'extract_method': 'curl showdetails + rezolvare exponenti (sup -> ^N) + lxml text extraction',
        'superscript_articles': sup_arts,
    }
    if parsed.get('never_amended'):
        fm['never_amended'] = True
    if pending:
        fm['consolidation_is_future'] = True
        fm['in_force_warning'] = (
            f"Consolidarea este datata {parsed['consolidation_date']}, ulterioara zilei "
            f"de {TODAY}. Fisierul contine modificari care NU sint inca in vigoare. "
            f"Dispozitii afectate: {len(pending)}.")
    elif whole_act_future:
        fm['consolidation_is_future'] = True
        fm['in_force_warning'] = (
            f"Consolidarea este datata {parsed['consolidation_date']}, ulterioara zilei "
            f"de {TODAY}, si nu exista marcaje de dispozitii amanate: este data intrarii in "
            f"vigoare a actului intreg. Nicio dispozitie nu se aplica astazi.")
    fm_text = (yaml.safe_dump(fm, allow_unicode=True, sort_keys=False).strip() if yaml
               else '\n'.join(f'{k}: {v}' for k, v in fm.items()))
    out = '---\n' + fm_text + '\n---\n\n' + body_text

    # Conventia corpusului (lib_anchor.sha_variants) calculeaza hash-ul peste octetii
    # corpului de DUPA fence-ul de frontmatter, deci inclusiv linia goala de la inceput.
    # Hash-ul calculat mai sus, pe body_text, nu corespunde acelei conventii. Defect prins
    # de fix_sha_drift.py al celuilalt fir la 2026-09-04. Se recalculeaza pe fisierul gata
    # asamblat, ca sa nu ramina drift la scriere.
    blob = out.encode('utf-8')
    fence = re.search(rb'^---\s*$', blob[3:], re.M)
    body_bytes = blob[3 + fence.end():]
    return re.sub(r'^sha256:\s*\w+',
                  'sha256: ' + hashlib.sha256(body_bytes).hexdigest(),
                  out, count=1, flags=re.M)


def main():
    # Fara argumente ingereaza tot. Cu argumente, doar actele numite, ca sa nu rescriem
    # fisiere existente fara motiv.
    import sys
    only = [a for a in sys.argv[1:] if not a.startswith('-')]
    targets = {k: v for k, v in DOCS.items() if not only or k in only}
    if only and not targets:
        raise SystemExit(f"nimic de ingerat; alege dintre: {', '.join(DOCS)}")
    for stem, spec in targets.items():
        show_url, data, path = fetch(spec['doc_id'])
        resolved = resolve_superscripts(data)
        if not resolved or '<sup' in resolved:
            raise RuntimeError('resolve_superscripts nu a rezolvat exponentii')
        parsed = extract_doc(resolved)
        (RAW_DIR / f"{stem}.md").write_text(make_raw(stem, spec, parsed, show_url),
                                            encoding='utf-8', newline='\n')
        print(f"{stem}: {parsed['article_count']} articole, "
              f"consolidat {parsed['consolidation_date']}, HTML {path.name}")


if __name__ == '__main__':
    main()
