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
    'L-845-1992': {'doc_id': '152587',
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
    'COD-443-2004': {'doc_id': '155721', 'title': 'Codul de executare al Republicii Moldova nr. 443/2004'},
    'COD-95-2021':  {'doc_id': '154350', 'title': 'Codul vamal al Republicii Moldova nr. 95/2021'},
    'COD-154-2003': {'doc_id': '155185', 'title': 'Codul muncii al Republicii Moldova nr. 154/2003'},
    'COD-218-2008': {'doc_id': '155852', 'title': 'Codul contraventional al Republicii Moldova nr. 218/2008'},
    'COD-985-2002': {'doc_id': '151140', 'title': 'Codul penal al Republicii Moldova nr. 985/2002'},
    'COD-122-2003': {'doc_id': '156018', 'title': 'Codul de procedura penala al Republicii Moldova nr. 122/2003'},
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
    'HG-743-2024': {'doc_id': '155188',
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
    'L-1543-1998': {'doc_id': '150224',
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
    # ---------------------------------------------------------------------------------------
    # 2026-09-10. Protectia datelor cu caracter personal, trei acte deodata. Ceruta a fost numai
    # L-133-2011, primul rind al cozii de ingerare din graful de citare (34 de mentiuni in 18 acte
    # detinute). Verificarea prealabila a aratat de ce coada nu era de crezut pe cuvint: graful nu
    # stie daca un act citat mai este in vigoare, iar acesta NU MAI ESTE. Ingerarea numai a lui ar
    # fi pus text mort in vault ca raspuns la 18 trimiteri vii.
    #
    # Capcana doc_id, a doua oara dupa L-246-2018 (2026-09-09): rindul de cautare trimite la
    # 148996@2025-06-14, dar lista de versiuni de pe pagina actului tine 144823@2026-08-23,
    # doc_id MAI MIC si data MAI NOUA, creat in 2024 pentru o modificare cu intrare in vigoare
    # amanata doi ani. Se ia 144823.
    #
    # Capcana abrogarii, noua: corpul consolidarii 144823 poarta in antet, in locul rindului
    # MODIFICAT, "Abrogata prin LP195 din 25.07.24, MO367-369/23.08.24 art.574; in vigoare
    # 23.08.26", iar cimpul "Data abrogarii" din fisa este GOL. Sursa se contrazice pe sine.
    # De aici functia repeal_of() si avertismentul din corp.
    # Verificat pe HTML inainte de rulare: 12 <sup>, fara span CSS, fara CUPRINS, 36 de ancore
    # (34 de baza 1-34 fara lacune, plus 25^1 si 25^2), fara duplicate, art. 28 abrogat in corp.
    'L-133-2011': {'doc_id': '144823',
                   'title': 'Legea nr. 133/2011 privind protectia datelor cu caracter personal '
                            '(ABROGATA de la 23.08.2026 prin L-195-2024)'},
    # Succesorul general, in vigoare. Transpune Regulamentul (UE) 2016/679 (GDPR), acolo unde
    # L-133-2011 transpunea Directiva 95/46/CE, adica regimul dinaintea GDPR. Adoptata 25.07.2024,
    # publicata 23.08.2024, dar abrogarea legii vechi a fost amanata pina la 23.08.2026, deci
    # schimbarea de regim s-a produs acum 18 zile. Consolidarea curenta 155899@2026-08-23
    # incorporeaza LP160/2026. Verificat: 3 <sup>, fara span CSS, fara CUPRINS, 90 de ancore,
    # numerotare 1-90 fara nicio lacuna, fara duplicate, fara data de abrogare.
    'L-195-2024': {'doc_id': '155899',
                   'title': 'Legea nr. 195/2024 privind protectia datelor cu caracter personal'},
    # Al treilea act al aceleiasi reforme, gasit in aceeasi cautare: regimul datelor prelucrate
    # in scopul prevenirii si combaterii infractiunilor, adica echivalentul Directivei (UE)
    # 2016/680. Conteaza pentru corpus fiindca cele trei trimiteri ale Codului de procedura penala
    # catre L-133-2011 privesc exact prelucrarea in procesul penal. In vigoare 23.08.2026,
    # niciodata modificata, deci consolidarea este data intrarii in vigoare. Verificat: zero
    # <sup>, fara span CSS, fara CUPRINS, 46 de ancore, numerotare 1-46 fara lacune.
    'L-160-2026': {'doc_id': '155902',
                   'title': 'Legea nr. 160/2026 privind protectia datelor cu caracter personal '
                            'prelucrate in scopul prevenirii si combaterii infractiunilor'},
    # ---------------------------------------------------------------------------------------
    # 2026-09-16. Lotul D, litigii civile/comerciale si contracte, ales de Eugen dintre
    # citeva directii propuse pentru extinderea wiki-ului (inelul de stagiu din 6 septembrie
    # si reverificarea acquis din 15-16 septembrie fiind ambele incheiate). legis.md a fost
    # blocat de Cloudflare la inceputul sesiunii (curl si browserul intern, ambele "Just a
    # moment"); Eugen a trecut verificarea in propriul Chrome, apoi cautarea si descarcarea au
    # mers prin claude-in-chrome (fetch same-origin + download blob, ca la P8/BNM). Descarcarea
    # automata a Chrome-ului a blocat fisierele al doilea si al treilea dintr-un tab deja folosit
    # (Chrome opreste descarcarile succesive fara interactiune); rezolvat deschizind un tab nou
    # per descarcare.
    #
    # Prima verificare a rasturnat o ipoteza gresita: nu exista "Legea nr. 24/2023 cu privire la
    # arbitraj". Legea de arbitraj intern e nr. 23 din 22.02.2008, iar arbitrajul comercial
    # international e legea sora, nr. 24 din aceeasi data. Ambele gasite prin cautare in titlu
    # "arbitraj", paginate manual (46 rezultate, 5 pagini) pina la rindurile de baza LP23/2008 si,
    # separat, "arbitrajul comercial international" (11 rezultate) pentru LP24/2008.
    'L-23-2008': {'doc_id': '95607',
                  'title': 'Legea nr. 23/2008 cu privire la arbitraj'},
    # Verificat pe HTML: consolidare 30-09-2016 (LP211 din 29.07.16), 35 de articole, fara
    # CUPRINS. Art. 231 (Suspendarea procedurii arbitrale, introdus 2016) trimite la Legea
    # 137/2015 cu privire la mediere - vezi nota L-9-2026 mai jos, legea 137/2015 e acum
    # abrogata, trimiterea ramine corecta ca numar dar tinta si-a schimbat continutul.
    'L-24-2008': {'doc_id': '110184',
                  'title': 'Legea nr. 24/2008 cu privire la arbitrajul comercial international'},
    # Verificat pe HTML: consolidare 30-12-2018 (LP238 din 08.11.18), 41 de articole plus art.
    # 231 (acelasi mecanism de suspendare pentru mediere ca la L-23-2008). Doua versiuni cu
    # tabul de an listate; niciuna viitoare.
    #
    # A doua rasturnare de ipoteza, mai importanta: Legea nr. 137/2015 cu privire la mediere,
    # aflata deja in coada de ingerare a grafului de citare (9 mentiuni, L-198-2007 fiind citantul
    # principal), NU mai este legea in vigoare. Gasita la cautarea in titlu "mediere": LP9/2026
    # "privind medierea si statutul mediatorului", promulgata 03-03-2026, publicata 12-03-2026,
    # abroga expres Legea 137/2015 la data intrarii sale in vigoare (art. 62 alin. (2)). Verificat
    # in corp, nu presupus din titlu: cautarea textului intern a confirmat fraza "La data intrarii
    # in vigoare a prezentei legi, Legea nr. 137/2015 cu privire la mediere ... se abroga."
    # Transpune Directiva 2008/52/CE (CELEX 32008L0052) - e act de acquis, nu doar de drept intern.
    'L-9-2026': {'doc_id': '153389',
                 'title': 'Legea nr. 9/2026 privind medierea si statutul mediatorului '
                          '(abroga Legea nr. 137/2015 cu privire la mediere)'},
    # CAPCANA DE INTRARE IN VIGOARE, verificata pe art. 62: legea intra in vigoare la 6 luni de
    # la publicare (12-03-2026 + 6 luni = ~12-09-2026, deci in vigoare de cateva zile la data
    # acestei ingerari, 2026-09-16), CU DOUA EXCEPTII AMANATE scrise direct in art. 62 alin. (1),
    # nu ca marcaj [Art.N ... in vigoare] separat, fiindca legea e noua, nu amendata: art. 44
    # alin. (3) lit. b) si c) (prima sedinta de mediere in litigii de familie/munca) la 12 luni
    # (~12-03-2027), si art. 44 alin. (3) lit. a) (litigii civile, exceptind insolvabilitatea) la
    # 24 luni (~12-03-2028). Registrul in-force citeste marcaje de forma "[Art.N ... in vigoare
    # DD.MM.YY]"; aceasta forma de dispozitie amanata, scrisa in proza in ultimul articol al unei
    # legi noi, nu are acel tipar si NU va fi prinsa automat de build_inforce_register.py. De
    # verificat manual la orice citare a art. 44 alin. (3) din aceasta lege pina cind registrul
    # e extins sa acopere si acest tipar (a treia forma, dupa marcaj si dupa act-intreg-viitor).
    # HTML verificat: 62 de articole, fara CUPRINS, o singura versiune (2026), fara <sup> gasite
    # inca la verificare prealabila (de confirmat la rulare).
    #
    # Al patrulea act al lotului, fara surpriza de numar: Legea 1125/2002 pentru punerea in
    # aplicare a Codului civil, deja in coada de ingerare a grafului (22 mentiuni, 19 din chiar
    # CC-1107-2002 insusi - actul explica propriile dispozitii tranzitorii ale codului). Gasita
    # prin cautare in titlu "punerea in aplicare a Codului civil"; LP1125/2002 marcat "Modificat".
    'L-1125-2002': {'doc_id': '150208',
                    'title': 'Legea nr. 1125/2002 pentru punerea in aplicare a Codului civil '
                             'al Republicii Moldova'},
    # Verificat pe HTML: 50 de articole plus anexele 1-9 (formulare standard, netextualizate in
    # corp - doar titlurile "anexa nr.N" apar, ca linkuri separate pe pagina legis.md). Capitolul
    # III (art. 48-50), introdus de LP251 din 10.07.25, "in vigoare 01.04.26": desi pare o
    # consolidare viitoare fata de alte acte din corpus, 1 aprilie 2026 e deja trecut fata de
    # data acestei ingerari (2026-09-16), deci textul e curent, nu amanat. Capitolul reglementeaza
    # exact procedura succesorala pusa in aplicare de LP251/2025 pe cartea a patra a Codului
    # civil, deja documentata in alta parte a acestui manifest (speta mostenitorului, 8-9
    # septembrie).

    # 2026-09-17, al doilea act din coada de ingerare a grafului de citare (22 mentiuni, 11 acte
    # citatoare, cel mai des din COD-218-2008, care sanctioneaza contraventional nedeclararea/
    # nesolutionarea conflictului de interese sub aceasta lege). Legea-cadru a declararii averii
    # si intereselor personale (regimul ANI). Gasita prin cautare in titlu "privind declararea
    # averii si a intereselor personale", LP133/2016 marcat "Modificat", doc_id 155891. 21 <sup>,
    # fara CUPRINS. ATENTIE, doua straturi de neobisnuit gasite pe fisa inainte de ingerare:
    #   1. CONSOLIDARE VIITOARE: primele doua randuri MODIFICAT sint LP154 din 30.07.26 si LP327
    #      din 29.12.25, ambele "in vigoare 01.01.27" - deci textul de azi (17 septembrie 2026)
    #      contine deja amendamente care intra in vigoare abia peste trei luni si jumatate.
    #      Acelasi LP154 mai are un rind separat "in vigoare 13.09.26" (o alta dispozitie a
    #      aceleiasi legi modificatoare, deja trecuta) - actul e amendat pe straturi, nu dintr-o
    #      singura data.
    #   2. HCC29 din 21.09.21, MO256-260/22.10.21 art.184; in vigoare 21.09.21 apare direct in
    #      istoricul de modificari al fisei, nu doar in corpul textului - de verificat la
    #      regenerarea registrului HCC ce dispozitie a lovit.
    'L-133-2016': {'doc_id': '152995',
                   'title': 'Legea nr. 133/2016 privind declararea averii si a intereselor '
                            'personale'},

    # 2026-09-17, al treilea act din coada de ingerare. Candidatul initial, Legea nr. 133/2018
    # (renumerotarea Codului civil, ipoteza din CLAUDE.md pct. 8) confirmata ca fiind exact acel
    # act (art. 7 alin. (2) din L-1125-2002: "dind titlurilor... articolelor... o noua
    # numerotare"), dar NEPRACTICA de ingerat cu scriptul actual: showdetails are 4.8 MB, 1926 de
    # aparitii "Articolul N" (textul integral al Codului civil reprodus inline in blocurile de
    # modificare) si doar 18 articole proprii, numerotate roman (Art. I - Art. XVIII) - structura
    # complet diferita de ce asteapta extract_doc (ancore pe "Articolul N" la nivel de act, nu
    # aparitii ale unui Cod citat in text). Amina, semnalat lui Eugen, nu ingerat.
    # Ales in loc: Legea nr. 86/2014 privind evaluarea impactului asupra mediului, 20 de mentiuni,
    # citata de 5 acte, cel mai des din COD-434-2023 (Codul urbanismului, deja in corpus, 11
    # citari - doua definitii proprii ("acord de mediu", "constructie cu impact semnificativ")
    # trimit direct aici). Gasita prin cautare in titlu "evaluarea impactului asupra mediului",
    # doc_id 154125 (republicata in MO326-333/2022, versiunea curenta din 08.11.2023). 312 KB,
    # 42 de articole, 69 <sup>. Ultima modificare LP53 din 09.04.26, in vigoare 25.04.26 - trecuta,
    # deci consolidare curenta, nu viitoare.
    'L-86-2014': {'doc_id': '154125',
                  'title': 'Legea nr. 86/2014 privind evaluarea impactului asupra mediului'},

    # 2026-09-17, al patrulea act, ales pentru ca inchide o intrebare deschisa proprie: art. 22
    # alin. (2) din L-133-2016, ingerata mai devreme azi, trimite aici pentru organizarea ANI.
    # 12 mentiuni in coada de ingerare, 6 acte citatoare, cel mai des chiar din L-133-2016 (6 ori).
    # Gasita prin cautare in titlu "Autoritatea Nationala de Integritate", doc_id 155890 (adoptata
    # aceeasi zi ca L-133/2016, 17.06.2016, doc_id-uri consecutive). ATENTIE, acelasi tipar ca
    # L-133/2016: consolidare VIITOARE (LP154 din 30.07.26, in vigoare 01.01.27, primul rind
    # MODIFICAT). DOUA decizii HCC in istoricul fisei, nu una: HCC29 din 21.09.21 (aceeasi ca la
    # L-133/2016 - probabil aceeasi lovire a art. 23 al.(5^1), aici sub alt numar de articol) si
    # HCC6 din 10.04.18, MO157-166/18.05.18 art.76 - a doua, mai veche, negasita inca in registrul
    # HCC (20 de acte pina acum). 45 de articole, 33 <sup>.
    'L-132-2016': {'doc_id': '147882',
                   'title': 'Legea nr. 132/2016 cu privire la Autoritatea Nationala de '
                            'Integritate'},

    # 2026-09-17, al cincilea act din coada de ingerare a grafului de citare. Nu mai era
    # cel mai citat pe numar de mentiuni (COD-325-2022, 38 mentiuni, era mai sus), dar coloana
    # care conteaza pentru ordinea de ingerare e a treia: 11 acte citatoare, cel mai mult din
    # oricare candidat verificat (COD-325-2022 si L-325-2013 aveau cite 9). Cele 11: COD-122-2003
    # (procedura penala, art. 138^10, 57^2, 6), COD-985-2002 (penal, art. 121, divulgarea
    # secretului de stat), L-1260-2002 (avocatura, art. 39), L-131-2015 (achizitii publice,
    # abrogata, art. 30, 78), L-133-2016 (declararea averii, art. 5, 7, 7^1, 9 - ingerata azi mai
    # devreme, motivul principal de relevanta), L-160-2026 (protectia datelor, art. 2), L-192-1998
    # (protectia consumatorului, art. 20), L-195-2024 (protectia datelor, art. 2), L-20-2026
    # (achizitii, art. 7), L-325-2025 (achizitii publice, art. 50, 55, 81), UA-STATUT-2011
    # (avocatura, art. 43^1).
    # Gasita prin cautare in NR. DOCUMENTULUI = 245 (fara an: campul nu accepta "245/2008",
    # intoarce zero; cu numarul singur, 97 de rezultate paginate client-side, toate incarcate in
    # DOM din prima si doar ascunse de changePagination() - deci nu a fost nevoie de request-uri
    # suplimentare de pagina, un grep pe tabelele .table a gasit direct LP245/2008, 27-11-2008,
    # Modificat, "cu privire la secretul de stat"). legis.md era accesibil in browserul intern
    # din prima incercare, deci nu a fost nevoie de Chrome-ul lui Eugen ca la sesiunile anterioare.
    # doc_id 151410, confirmat cea mai noua din 17 versiuni pe fisa (rindul "an2025" activ, MODIFICAT
    # LP227 din 10.07.25, in vigoare 30.12.25 - trecuta). "Data abrogarii": "-". Fara <sup>
    # gasite in verificarea de dinaintea rularii (de confirmat la extractie), fara CUPRINS
    # (lege, nu cod), 40 din 41 aparitii "Articolul N" unice (o dubla, de verificat: ar putea fi
    # un exponent aplatizat sau un articol citat inline in corp, nu titlu de sectiune).
    'L-245-2008': {'doc_id': '151410',
                   'title': 'Legea nr. 245/2008 cu privire la secretul de stat'},

    # 2026-09-17, al saselea act din coada de ingerare, ales strict dupa coloana a treia
    # (acte citatoare): 14 acte detinute o citeaza, fiecare o singura data - cel mai mare numar
    # dintre toti candidatii vazuti pina acum in aceasta coada. Gasita prin NR. DOCUMENTULUI = 181
    # (fara an), rindul LP181/2014, 25-07-2014, Modificat, "finantelor publice si responsabilitatii
    # bugetar-fiscale" - legea-cadru a bugetului de stat. doc_id 153046.
    # CONSOLIDARE VIITOARE, 2027-01-01: singurul rind MODIFICAT vizibil in capul paginii este
    # LP327 din 29.12.25, in vigoare 01.01.27, dar fisa arata ACELASI LP327 cu DOUA date de
    # intrare in vigoare suplimentare, 31.12.25 (trecute fata de azi) - alte dispozitii ale
    # aceleiasi legi modificatoare, deja in vigoare, dar fara marcaj propriu in corpul acestei
    # consolidari (mecanismul 1 din CLAUDE.md, "marcajul se pierde la reimprospatare": doar
    # schimbarile CELEI MAI RECENTE date raman marcate). Corpul poarta 14 marcaje, toate cu
    # aceeasi data 01.01.27: art. 1 al.(2), art. 2, art. 3 (de trei ori), art. 20 al.(1) lit.
    # f)/k)/k^1, art. 21 al.(1) lit. a), art. 62 al.(9), art. 75 lit. a), art. 76 al.(1)-(5).
    # DOUA decizii HCC in istoricul fisei (HCC32 din 17.11.16, HCC10 din 16.03.17), NICIUNA
    # marcata in corpul textului - aceeasi categorie "fara articol" ca CONST-1994, L-213-2023
    # si L-132-2016.
    # Verificat pe HTML inainte de rulare: 89 de aparitii "Articolul N", toate unice (fara
    # duplicate), 34 <sup>, fara CUPRINS. LACUNA DE NUMEROTARE: art. 49 lipseste (48 -> 50),
    # fara niciun marcaj "abrogat" in aceasta consolidare - categoria "fara marcaj in aceasta
    # consolidare" din CLAUDE.md punctul 3, neinvestigata mai departe in istoricul legis.md la
    # aceasta ingerare.
    'L-181-2014': {'doc_id': '153027',
                   'title': 'Legea nr. 181/2014 privind finantele publice si responsabilitatea '
                            'bugetar-fiscala'},

    # 2026-09-17, al saptelea act din coada de ingerare. Trei candidati legati la coloana a treia
    # (9 acte citatoare): COD-325-2022 (Codul electoral, mare, generic), L-139-2010 (ABROGAT -
    # "privind dreptul de autor si drepturile conexe", verificat pe rindul de cautare inainte de a
    # alege, respins pentru ca necesita gasirea succesoarei) si aceasta lege, aleasa pentru
    # continuitatea tematica cu ciorchinele de integritate/anticoruptie deja in corpus
    # (L-132-2016, L-133-2016): legea de evaluare a integritatii institutionale (testarea
    # profesionala a agentilor publici, CNA). Gasita prin NR. DOCUMENTULUI = 325 (fara an), rindul
    # LP325/2013, 23-12-2013, Modificat, "privind evaluarea integritatii institutionale*". doc_id
    # 142068.
    # Verificat pe HTML inainte de rulare: 28 de aparitii "Articolul N", toate unice, fara
    # duplicate, fara lacuna, 10 <sup>, fara CUPRINS. Consolidare din "LP11 din 01.02.24, in
    # vigoare 29.03.24" - trecuta, deci nu viitoare.
    # DOUA decizii HCC in istoric: HCC37 din 07.12.21 (marcata DIRECT in corp, loveste art. 17
    # al.(2), (3) si (4) - testarea integritatii profesionale) si HCC7 din 16.04.15 (doar in
    # istoricul fisei, fara marcaj propriu in corp gasit la verificarea prealabila - categoria
    # "fara articol").
    'L-325-2013': {'doc_id': '142068',
                   'title': 'Legea nr. 325/2013 privind evaluarea integritatii institutionale'},

    # 2026-09-18, al optulea act din coada de ingerare, si primul ales NU dupa coloana a treia.
    # 21 de mentiuni, doar 2 acte citatoare (L-1125-2002 de 20 de ori, CC-1107-2002 o data),
    # deci mecanic ar fi stat la mijlocul cozii. Motivul real: este singurul candidat care
    # inchide o intrebare deschisa deja consemnata in CLAUDE.md, punctul 8 - ciorchinele de
    # 13 trimiteri nerezolvate catre CC-1107-2002 cu numerotarea de dinainte de 2019, unde
    # ipoteza scrisa era "probabil Legea 133/2018". Este ea.
    # CONFIRMAT INAINTE DE RULARE, pe textul sursei, nu pe presupunere: actul poarta ca titluri
    # de articol exact numerele vechi pe care le citeaza celelalte acte -
    #   Articolul 330^4  "Uzucapiunea dreptului contrar cuprinsului registrului" (citat de
    #     COD-225-2003 de 3 ori; art. 330 de azi este "Nulitatea relativa a actului juridic")
    #   Articolul 283^27 "Drepturile, actele sau faptele supuse notarii" (COD-225-2003)
    #   Articolul 1575^4 "Excluderea creantelor neinaintate", 1575^9 "Raspunderea mostenitorului
    #     pentru administrarea anterioara", 1572^117 "Cheltuielile de ingrijire si de
    #     inmormintare" (toate citate de L-149-2012 pentru masa succesorala)
    # LIMITA, verificata tot inainte de rulare si consemnata ca sa nu se supraliciteze: ciorchinele
    # art. 48^12/48^21/48^28/48^30/48^40 (ocrotirea judiciara, citat de COD-225-2003) NU vine de
    # aici. Actul nu are niciun articol 48^N; singurele trei titluri cu "ocrotire" sint 1051,
    # 1575^30 si 1591. Acele articole au fost introduse de o alta lege de modificare, negasita inca.
    # STRUCTURA, motivul pentru care acest act a cerut anchor_mode. Este o lege de MODIFICARE:
    # are 17 articole proprii, numerotate roman, scrise "Art. I. - ", "Art. II. - " etc., iar
    # intre ele reproduce textul nou al actelor modificate. Extractorul implicit ar fi scris
    # 1434 de ancore "## Articolul N" (text citat al Codului civil, al CPC, al legii
    # insolvabilitatii...), plus 42 de forma "Art.N. -", 101 sectiuni, 33 de capitole si 7
    # titluri - toate ancore pentru dispozitii care NU sint ale acestui act, si care ar fi
    # intrat in graful de citare si in registrele generate ca dispozitii proprii. De aceea
    # anchor_mode='roman-amending': se ancoreaza NUMAI cele 17 articole romane, iar ancora se
    # insereaza ca linie noua deasupra liniei sursa, in forma "## Articolul I." - conventia deja
    # folosita in corpus pentru L-177-2025 si L-178-2020, singura pe care ROMAN_RE din
    # build_coverage.py si ANCHOR_RE din build_citation_graph.py o recunosc. Linia originala
    # "Art. I. - ..." ramine neatinsa dedesubt.
    # Cele 17 articole, tinta fiecaruia (citita din prima linie): I Codul civil, II L-1125-2002,
    # III Codul familiei, IV L-1260-2002 (avocatura), V L-1453-2002 (notariat), VI L-105-2003,
    # VII COD-122-2003 art. 220, VIII COD-225-2003, IX COD-443-2004 art. 11, X L-407-2006
    # (asigurari), XI L-131-2007, XII L-135-2007, XIII L-220-2007, XIV COD-218-2008 art. 45,
    # XV L-98-2012, XVI L-149-2012 (insolvabilitate), XVII abrogarile de la 1 martie 2019.
    # Zece dintre aceste tinte sint deja in vault.
    # Restul verificarii prealabile: doc_id 34327, SINGURA versiune din istoric (act de modificare,
    # niciodata modificat el insusi); "Data abrogarii" in fisa: "-"; fara rind MODIFICAT, deci
    # never_amended, iar consolidarea va fi data intrarii in vigoare, 2019-03-01 - act vechi,
    # va aparea la "stale consolidations", ceea ce este corect si inofensiv pentru o lege de
    # modificare consumata. 1950 <sup>, niciun span ridicat prin CSS, fara CUPRINS.
    # HTML 4.859.144 octeti, luat prin browserul intern (curl primeste 403 de la Cloudflare).
    'L-133-2018': {'doc_id': '34327',
                   'anchor_mode': 'roman-amending',
                   'title': 'Legea nr. 133/2018 privind modernizarea Codului civil si '
                            'modificarea unor acte legislative'},

    # 2026-09-18, in aceeasi sesiune cu L-133-2018 si din cauza ei: este cealalta jumatate a
    # intrebarii 8 din CLAUDE.md. L-133-2018 a rezolvat toate trimiterile cu numerotare veche
    # ale wiki-ului IN AFARA de ciorchinele 48^N (ocrotirea judiciara, citat de COD-225-2003 de
    # sapte ori) - actul acela nu contine niciun articol 48^N, ci doar MODIFICA zece dintre ele
    # (48^5, 48^6, 48^25, 48^32, 48^55, 48^61, 48^63, 48^75, 48^82, 48^84), ceea ce dovedeste ca
    # existau deja. Legea care le-a introdus este aceasta.
    # CUM A FOST GASITA, fiindca metoda e generala: cautare pe TEXT (search_type=2) dupa o
    # sintagma proprie regimului, "ocrotitor provizoriu" - 24 de rezultate, din care LP66/2017
    # este cel mai vechi act de lege. Confirmata apoi in doua feluri independente: numarul apare
    # in blocul de istoric al Codului civil ("LP66 din 13.04.17, MO171-180/02.06.17 art.297"), iar
    # textul actului poarta 100 de titluri "Articolul 48^N", de la 48^1 "Temeiurile, formele si
    # principiile ocrotirii" pina la 48^100. Art. 48^12 este "Mandatul de ocrotire in viitor",
    # exact ce descrie fraza din COD-225-2003 care il citeaza.
    # doc_id 99281, SINGURA versiune din istoric, "Data abrogarii": "-", fara rind MODIFICAT,
    # deci never_amended si consolidare = data intrarii in vigoare, 02.06.2017 (act vechi, va
    # aparea la "stale consolidations", corect pentru o lege de modificare consumata).
    # Verificat pe HTML inainte de rulare, prin pipeline-ul real: 274 <sup>, toti rezolvati,
    # fara CUPRINS, 17 articole romane (aceeasi forma "Art. I. - "), 131 de titluri "Articolul N"
    # reproduse (toate distincte, fara duplicate) si 5 sectiuni - text al actelor modificate,
    # deci acelasi anchor_mode ca L-133-2018.
    # Cele 17 tinte: I L-269/1994, II L-1402/1997 (sanatatea mentala), III Codul vamal 1149/2000,
    # IV Codul familiei, V L-713/2001, VI Codul civil, VII COD-225-2003, VIII L-271/2003,
    # IX COD-443-2004 art. 52, X L-24/2008 (arbitraj comercial international, in vault),
    # XI L-42/2008, XII L-153/2008, XIII L-99/2010 (adoptia), XIV L-149-2012 art. 60,
    # XV L-140/2013, XVI L-91/2014, XVII dispozitii tranzitorii (termen de un an de la intrare).
    'L-66-2017': {'doc_id': '99281',
                  'anchor_mode': 'roman-amending',
                  'title': 'Legea nr. 66/2017 cu privire la modificarea si completarea unor '
                           'acte legislative (regimul masurilor de ocrotire judiciara)'},
    # Primul act din coada mecanica de ingestie la 2026-09-18: 38 de mentiuni din 9 acte
    # deja detinute. Identitatea a fost confirmata pe pagina oficiala legis.md: COD nr. 325
    # din 08.12.2022, publicat in MO 426-427/23.12.2022, art. 770; doc_id 148963. Pagina
    # curenta afiseaza versiunea din 26.08.2026, care este anterioara datei de lucru.
    #
    # 2026-09-19: doc_id-ul de mai sus era GRESIT si a fost inlocuit. Lista de versiuni citita
    # pe pagina actului da 22 de versiuni; 148963 este consolidarea 01-01-2026, adica TREI
    # versiuni in urma (au urmat 155595 @ 09-07-2026 si 153001 @ 26-08-2026). Nota despre
    # "versiunea din 26.08.2026" avea dreptate, antetul exportului PDF nu. Capcana din
    # ingerarea Legii 246/2018 se repeta: data cea mai noua NU are doc_id-ul cel mai mare
    # (153001 < 155595 < 156086), deci se citeste lista, nu se ghiceste.
    # Actul are si o consolidare VIITOARE, 156086 @ 01-01-2027, deci intra in registrul
    # "nu inca in vigoare". "Data abrogarii" = "-", si corpul nu contine "Abrogata prin".
    # Intra in registrul HCC cu DOUA hotariri: HCC16 din 03.10.23 (art. 16 al.(2) lit. e)) si
    # HCC9 din 26.03.24, care sterge tot blocul adaugat de LP280/2023 (art. 16 al.(2) lit. f)
    # si al.(2^1)-(2^4), art. 68 al.(1) lit. f), al.(1^1) si al.(5^1), art. 91 al.(3^1),
    # art. 98 al.(1) pct.2) lit. a) si a^1), art. 102 al.(5) lit. e)).
    # Exportul PDF al versiunii vechi ramine la
    #   raw/assets/moldova-legal/COD-325-2022-legis-148963-2026-09-18.pdf
    # ca proba a ce s-ar fi ingerat daca nu se citea lista de versiuni: 245 de articole in loc
    # de cele de azi, si 37 de exponenti in loc de 105. Vezi sectiunea AH din manifest.
    'COD-325-2022': {'doc_id': '153001',
                     'title': 'Codul electoral al Republicii Moldova nr. 325/2022'},
    # Adaugata 2026-09-19. Doua motive, ambele din CLAUDE.md: locul 12 in coada de ingerare
    # (9 mentiuni, 6 acte citatoare) si datarea abrogarii sectiunii secretelor comerciale din
    # Codul civil (arts. 2047-2054, vechile 1431^1-1431^8), intrebarea deschisa nr. 1.
    # doc_id 152656 = consolidarea 31-12-2025 (LP330 din 29.12.25); cealalta versiune, 140742,
    # este textul original in vigoare 22.02.2024. Fara versiune viitoare. "Data abrogarii" = "-".
    # 16 articole, ZERO etichete <sup>. Transpune Directiva (UE) 2016/943.
    'L-384-2023': {'doc_id': '152656',
                   'title': 'Legea nr. 384/2023 privind protectia secretelor comerciale'},
    # Adaugata 2026-09-19. Capul cozii de ingerare dupa Codul electoral: 19 mentiuni din 9 acte
    # (COD-150-2014 are mai multe mentiuni, dar dintr-un singur act). Art. 36 alin. (1) si (9)
    # din COD-325-2022 o cheama pe nume. Cautare in titlu fara diacritice: legis.md da denumirea
    # "LEGE Nr. 199 din 16.07.2010 cu privire la statutul persoanelor cu functii de demnitate
    # publica"; singurul rand LP199/2010. doc_id 155887 = consolidarea cu ultima modificare LP154
    # din 30.07.26, in vigoare 13.09.26 (deci trecuta la data ingerarii). Neabrogata: nici fisa,
    # nici antetul corpului nu poarta abrogare. 29 de articole.
    'L-199-2010': {'doc_id': '155887',
                   'title': 'Legea nr. 199/2010 cu privire la statutul persoanelor cu functii de demnitate publica'},
    # Legea comunicatiilor electronice, 2026-09-24. doc_id 152659 @ 2025-12-31 (LP330/2025), gasit
    # prin decretul de promulgare; nu e abrogata (Data abrogarii: -). CAPCANA doc_id vs data,
    # verificata in aceeasi zi: versiunea 151457 poarta data 01-01-2026, mai noua ca 152659, dar are
    # id mai mic, iar diferenta de text este exact zero linii proprii + 3 linii de marcaj
    # (MODIFICAT si cele doua [Art.27 al.(14)], [Art.31 al.(6)] prin LP330) prezente doar in 152659.
    # Se ia 152659, care pastreaza marcajele amendamentului. Inlocuieste Legea 241/2007.
    'L-72-2025': {'doc_id': '151457',
                  'title': 'Legea nr. 72/2025 comunicatiilor electronice'},
    # Inelul de drept administrativ, 2026-09-24, la cererea lui Eugen ("ingest everything related to
    # administrative law"). Doc_id-urile sint versiunile CURENTE (cea mai noua data care nu e in viitor),
    # nu capul listei: pentru 98/2012, 435/2006, 121/2007, 397/2003, 270/2018, 52/2014, 165/2023, 121/2018
    # si 22/2025 randul din cautare arata o consolidare viitoare, consemnata in
    # _meta/inforce/pending-consolidations.json, nu ingerata. Legea 793/2000 (contencios administrativ)
    # si 190/1994 (petitionare) sint ABROGATE, deci nu intra. Descarcate intr-un singur fisier
    # concatenat din Chrome-ul lui Eugen, cu hash pe parte verificat la despachetare.
    'L-136-2017': {'doc_id': '143456', 'title': 'Legea nr. 136/2017 cu privire la Guvern'},
    'L-98-2012': {'doc_id': '150065', 'title': 'Legea nr. 98/2012 privind administratia publica centrala de specialitate'},
    'L-764-2001': {'doc_id': '149266', 'title': 'Legea nr. 764/2001 privind organizarea administrativ-teritoriala a Republicii Moldova'},
    'L-435-2006': {'doc_id': '143037', 'title': 'Legea nr. 435/2006 privind descentralizarea administrativa'},
    'L-768-2000': {'doc_id': '147897', 'title': 'Legea nr. 768/2000 privind statutul alesului local'},
    'L-121-2007': {'doc_id': '152778', 'title': 'Legea nr. 121/2007 privind administrarea si deetatizarea proprietatii publice'},
    'L-397-2003': {'doc_id': '153023', 'title': 'Legea nr. 397/2003 privind finantele publice locale'},
    'L-52-2014': {'doc_id': '147958', 'title': 'Legea nr. 52/2014 cu privire la Avocatul Poporului (Ombudsmanul)'},
    'L-488-1999': {'doc_id': '147849', 'title': 'Legea nr. 488/1999 privind exproprierea pentru cauza de utilitate publica'},
    'L-124-2022': {'doc_id': '151294', 'title': 'Legea nr. 124/2022 privind identificarea electronica si serviciile de incredere'},
    'L-260-2017': {'doc_id': '154853', 'title': 'Legea nr. 260/2017 privind organizarea si functionarea Curtii de Conturi'},
    'L-270-2018': {'doc_id': '155894', 'title': 'Legea nr. 270/2018 privind sistemul unitar de salarizare in sectorul bugetar'},
    'L-523-1999': {'doc_id': '143274', 'title': 'Legea nr. 523/1999 cu privire la proprietatea publica a unitatilor administrativ-teritoriale'},
    'L-121-2018': {'doc_id': '150089', 'title': 'Legea nr. 121/2018 cu privire la concesiunile de lucrari si concesiunile de servicii'},
    'L-22-2025': {'doc_id': '153624', 'title': 'Legea nr. 22/2025 privind concesiunile de lucrari si concesiunile de servicii'},
    'L-179-2008': {'doc_id': '152602', 'title': 'Legea nr. 179/2008 cu privire la parteneriatul public-privat'},
    'L-25-2008': {'doc_id': '107130', 'title': 'Legea nr. 25/2008 privind Codul de conduita a functionarului public'},
    'L-165-2023': {'doc_id': '138148', 'title': 'Legea nr. 165/2023 privind avertizorii de integritate'},
    # Al doilea lot de drept administrativ, 2026-09-25 (starea persoanei, registre, cetatenie, straini).
    # Aceeasi metoda: versiunea curenta din lista de versiuni, nu randul de cautare; 274/2011 are
    # consolidare viitoare 156391 @ 2027-01-01 (LP200/2026) in pending-consolidations.json.
    # Legea 1024/2000 a cetateniei si Legea 200/2010 a regimului strainilor sint ABROGATE pe legis.md.
    'L-253-2025': {'doc_id': '154591', 'title': 'Legea nr. 253/2025 cetateniei Republicii Moldova'},
    'L-100-2001': {'doc_id': '151282', 'title': 'Legea nr. 100/2001 privind actele de stare civila'},
    'L-273-1994': {'doc_id': '154600', 'title': 'Legea nr. 273/1994 privind actele de identitate din sistemul national de pasapoarte'},
    'L-71-2007': {'doc_id': '140170', 'title': 'Legea nr. 71/2007 cu privire la registre'},
    'L-274-2011': {'doc_id': '151195', 'title': 'Legea nr. 274/2011 privind integrarea strainilor in Republica Moldova'},
    # Perimetrul "functionarea Guvernului", 2026-09-25 (sectiunea AR a manifestului). Un singur blob
    # din Chrome-ul lui Eugen, hash pe parte verificat la despachetare (27 din 27). doc_id-ul este
    # consolidarea cea mai noua care nu e in viitor; 149916, 155729, 154407 au id mai mic decit rindul
    # de cautare, alegerea s-a facut dupa data, nu dupa id.
    'HG-610-2018': {'doc_id': '144183', 'title': 'Hotararea Guvernului nr. 610/2018 pentru aprobarea Regulamentului Guvernului'},
    'HG-657-2009': {'doc_id': '153599', 'title': 'Hotararea Guvernului nr. 657/2009 pentru aprobarea Regulamentului privind organizarea si functionarea, structurii si efectivului-limita ale Cancelariei de Stat'},
    'HG-386-2020': {'doc_id': '147314', 'title': 'Hotararea Guvernului nr. 386/2020 cu privire la planificarea strategica (adoptata ca "cu privire la planificarea, elaborarea, aprobarea, implementarea, monitorizarea si evaluarea documentelor de politici publice")'},
    'HG-310-2025': {'doc_id': '148714', 'title': 'Hotararea Guvernului nr. 310/2025 pentru aprobarea Regulamentului privind informarea si consultarea publica in procesul elaborarii si aprobarii documentatiei de amenajare a teritoriului si de urbanism'},
    'HG-305-2026': {'doc_id': '154862', 'title': 'Hotararea Guvernului nr. 305/2026 cu privire la organizarea si functionarea Ministerului Mediului'},
    'HG-186-2026': {'doc_id': '154079', 'title': 'Hotararea Guvernului nr. 186/2026 cu privire la organizarea si functionarea Ministerului Afacerilor Externe'},
    'HG-9-2026': {'doc_id': '152608', 'title': 'Hotararea Guvernului nr. 9/2026 cu privire la organizarea si functionarea Ministerului Apararii'},
    'HG-118-2023': {'doc_id': '152432', 'title': 'Hotararea Guvernului nr. 118/2023 cu privire la organizarea si functionarea Ministerului Energiei'},
    'HG-143-2021': {'doc_id': '154567', 'title': 'Hotararea Guvernului nr. 143/2021 cu privire la organizarea si functionarea Ministerului Dezvoltarii Economice si Digitalizarii'},
    'HG-147-2021': {'doc_id': '154565', 'title': 'Hotararea Guvernului nr. 147/2021 cu privire la organizarea si functionarea Ministerului Culturii'},
    'HG-148-2021': {'doc_id': '152494', 'title': 'Hotararea Guvernului nr. 148/2021 cu privire la organizarea si functionarea Ministerului Sanatatii'},
    'HG-149-2021': {'doc_id': '154407', 'title': 'Hotararea Guvernului nr. 149/2021 cu privire la organizarea si functionarea Ministerului Muncii si Protectiei Sociale'},
    'HG-146-2021': {'doc_id': '155729', 'title': 'Hotararea Guvernului nr. 146/2021 cu privire la organizarea si functionarea Ministerului Educatiei si Cercetarii'},
    'HG-696-2017': {'doc_id': '152209', 'title': 'Hotararea Guvernului nr. 696/2017 cu privire la organizarea si functionarea Ministerului Finantelor'},
    'HG-690-2017': {'doc_id': '152469', 'title': 'Hotararea Guvernului nr. 690/2017 cu privire la organizarea si functionarea Ministerului Infrastructurii si Dezvoltarii Regionale'},
    'HG-693-2017': {'doc_id': '151933', 'title': 'Hotararea Guvernului nr. 693/2017 cu privire la organizarea si functionarea Ministerului Afacerilor Interne'},
    'HG-695-2017': {'doc_id': '154558', 'title': 'Hotararea Guvernului nr. 695/2017 cu privire la organizarea si functionarea Ministerului Agriculturii si Industriei Alimentare'},
    'HG-698-2017': {'doc_id': '152487', 'title': 'Hotararea Guvernului nr. 698/2017 cu privire la organizarea si functionarea Ministerului Justitiei'},
    'L-797-1996': {'doc_id': '136244', 'title': 'Legea nr. 797/1996 pentru adoptarea Regulamentului Parlamentului'},
    'L-595-1999': {'doc_id': '143454', 'title': 'Legea nr. 595/1999 privind tratatele internationale ale Republicii Moldova'},
    'L-155-2011': {'doc_id': '155888', 'title': 'Legea nr. 155/2011 pentru aprobarea Clasificatorului unic al functiilor publice'},
    'L-80-2010': {'doc_id': '155886', 'title': 'Legea nr. 80/2010 cu privire la statutul personalului din cabinetul persoanelor cu functii de demnitate publica'},
    'L-246-2017': {'doc_id': '136833', 'title': 'Legea nr. 246/2017 cu privire la intreprinderea de stat si intreprinderea municipala'},
    'L-82-2017': {'doc_id': '155892', 'title': 'Legea nr. 82/2017 privind integritatea'},
    'L-212-2004': {'doc_id': '150250', 'title': 'Legea nr. 212/2004 privind regimul starii de urgenta, de asediu si de razboi'},
    'L-229-2010': {'doc_id': '144429', 'title': 'Legea nr. 229/2010 privind controlul financiar public intern'},
    'L-123-2023': {'doc_id': '149916', 'title': 'Legea nr. 123/2023 cu privire la stagiile platite in serviciul public'},
    # Adaugate tot 2026-09-25, dupa ce ingerarea L-212-2004 a aratat ca starea de urgenta a iesit din
    # ea la 01.09.2025 (LP248/2025, art. 1 si capitolul III abrogate): legea succesoare este aceasta.
    'L-248-2025': {'doc_id': '155526', 'title': 'Legea nr. 248/2025 privind managementul situatiilor de criza'},
    'HG-967-2016': {'doc_id': '137925', 'title': 'Hotararea Guvernului nr. 967/2016 cu privire la mecanismul de consultare publica cu societatea civila in procesul decizional'},
    # 2026-09-25, la cererea lui Eugen. Lege de MODIFICARE (optimizarea proceselor de obtinere a actelor
    # permisive), 28 de articole romane. Doua versiuni in istoric: 150581 @ 31-12-2025 (LP317/2025,
    # cea curenta) si 152771 @ 30-12-2025, mai veche desi cu id mai mare. "abrogat" apare in fisa doar
    # ca text al unui articol interior, nu ca data de abrogare a actului. HTML 374.973 octeti,
    # SHA-256 d3fb87fba7a6..., luat din Chrome-ul lui Eugen prin fetch + blob.
    'L-227-2025': {'doc_id': '150581', 'anchor_mode': 'roman-amending',
                   'title': 'Legea nr. 227/2025 pentru modificarea unor acte normative (optimizarea proceselor de obtinere a actelor permisive)'},
    # 2026-09-25, la cererea lui Eugen, imediat dupa L-227-2025: LP317 este legea care i-a rescris art. XLII
    # alin. (1) (marcajul "Art.XLII al.(1) in redactia LP317"). doc_id gasit in linkul din fisa lui LP227
    # (getResults 150581, ancora "LP317 din 29.12.25"), nu prin cautare. O singura versiune in istoric,
    # 152374 @ 31-12-2025; niciun "abrogat" in corp. Lege de modificare cu articole romane pina la XVIII.
    # HTML 64.188 octeti, SHA-256 377814f301f84c13b163..., luat din Chrome-ul lui Eugen (a doua descarcare
    # de pe acelasi site a cerut tab nou, prima a ajuns tirziu ca "(1)").
    'L-317-2025': {'doc_id': '152374', 'anchor_mode': 'roman-amending',
                   'title': 'Legea nr. 317/2025 pentru modificarea unor acte normative (optimizarea procedurilor la eliberarea actelor permisive)'},
    # 2026-09-25, la cererea lui Eugen: art. XVII din LP317 amana in proza, la 30.11.2027, articole din aceasta lege, care nu era in vault.
    # Lege de MODIFICARE (migrarea autoritatilor administrative centrale), 24 de articole romane. Doua versiuni: 149260 @ 31-12-2025
    # (3 marcaje LP317) si 152770 @ 01-01-2026 (1 marcaj; textul art. XXIV alin. (1) identic, marcajul de sub el lipseste). Luata cea mai
    # noua care nu e in viitor, 152770; marcajele pierdute se recupereaza din 149260. HTML 59.554 octeti, SHA-256 b1f4eb70fa44d00de74d06a3...
    'L-140-2025': {'doc_id': '152770', 'anchor_mode': 'roman-amending',
                   'title': 'Legea nr. 140/2025 pentru modificarea unor acte normative (migrarea autoritatilor administrative centrale)'},
    # 2026-09-25, la cererea lui Eugen: cele 54 de acte tinta nedetinute ale LP227, LP317 si LP140 (cele trei legi de modificare din aceasta
    # sesiune). Lista, id-urile si versiunile: cea mai noua consolidare care nu e in viitor, citita din lista de versiuni a fiecarui act, nu din
    # rindul de cautare (la peste 20 din 54 rindul si versiunea buna difera). Patru blob-uri din Chrome-ul lui Eugen (16,5 MB), hash SHA-256 pe parte
    # verificat la despachetare, 54 din 54. Un singur act abrogat: COD-3-2009 (CS246/2024, de la 30.05.2026), pastrat pentru ca LP317 art. V l-a
    # modificat inainte de abrogare; succesorul este COD-246-2024.
    'L-1456-1993': {'doc_id': '155880', 'title': 'Legea nr. 1456/1993 cu privire la activitatea farmaceutica'},
    'L-411-1995': {'doc_id': '151099', 'title': 'Legea ocrotirii sanatatii nr. 411/1995'},
    'L-439-1995': {'doc_id': '154104', 'title': 'Legea regnului animal nr. 439/1995'},
    'L-93-1998': {'doc_id': '151182', 'title': 'Legea nr. 93/1998 cu privire la patenta de intreprinzator'},
    'L-1585-1998': {'doc_id': '155334', 'title': 'Legea nr. 1585/1998 cu privire la asigurarea obligatorie de asistenta medicala'},
    'L-599-1999': {'doc_id': '149495', 'title': 'Legea nr. 599/1999 pentru aprobarea Codului navigatiei maritime comerciale'},
    'L-1100-2000': {'doc_id': '151336', 'title': 'Legea nr. 1100/2000 cu privire la fabricarea si circulatia alcoolului etilic si a productiei alcoolice'},
    'L-382-2001': {'doc_id': '149501', 'title': 'Legea nr. 382/2001 cu privire la drepturile persoanelor apartinind minoritatilor nationale si la statutul juridic al organizatiilor lor'},
    'L-461-2001': {'doc_id': '155106', 'title': 'Legea nr. 461/2001 privind piata produselor petroliere'},
    'L-852-2002': {'doc_id': '151357', 'title': 'Legea nr. 852/2002 (regimul comercial al hidrocarburilor halogenate care distrug stratul de ozon)'},
    'L-283-2003': {'doc_id': '151359', 'title': 'Legea nr. 283/2003 privind activitatea particulara de detectiv si de paza'},
    'L-119-2004': {'doc_id': '151363', 'title': 'Legea nr. 119/2004 cu privire la produsele de uz fitosanitar si la fertilizanti'},
    'COD-259-2004': {'doc_id': '149538', 'title': 'Codul cu privire la stiinta si inovare al Republicii Moldova nr. 259/2004'},
    'L-282-2004': {'doc_id': '151364', 'title': 'Legea nr. 282/2004 privind regimul metalelor pretioase si pietrelor pretioase'},
    'L-149-2006': {'doc_id': '154111', 'title': 'Legea nr. 149/2006 privind fondul piscicol, pescuitul si piscicultura'},
    'L-131-2007': {'doc_id': '155464', 'title': 'Legea nr. 131/2007 privind siguranta traficului rutier'},
    'L-156-2007': {'doc_id': '150040', 'title': 'Legea nr. 156/2007 cu privire la organizarea serviciului civil (de alternativa)'},
    'L-221-2007': {'doc_id': '151369', 'title': 'Legea nr. 221/2007 privind activitatea sanitara veterinara'},
    'L-239-2007': {'doc_id': '154114', 'title': 'Legea regnului vegetal nr. 239/2007'},
    'L-278-2007': {'doc_id': '155539', 'title': 'Legea nr. 278/2007 privind controlul tutunului'},
    'COD-3-2009': {'doc_id': '154117', 'title': 'Codul subsolului nr. 3/2009 (abrogat de la 30.05.2026 prin Codul 246/2024)'},
    'L-10-2009': {'doc_id': '136063', 'title': 'Legea nr. 10/2009 privind supravegherea de stat a sanatatii publice'},
    'L-272-2011': {'doc_id': '154121', 'title': 'Legea apelor nr. 272/2011'},
    'L-130-2012': {'doc_id': '152951', 'title': 'Legea nr. 130/2012 privind regimul armelor si al munitiilor cu destinatie civila'},
    'L-132-2012': {'doc_id': '155525', 'title': 'Legea nr. 132/2012 privind desfasurarea in siguranta a activitatilor nucleare si radiologice'},
    'L-68-2013': {'doc_id': '154351', 'title': 'Legea nr. 68/2013 despre seminte'},
    'L-303-2013': {'doc_id': '151413', 'title': 'Legea nr. 303/2013 privind serviciul public de alimentare cu apa si de canalizare'},
    'L-92-2014': {'doc_id': '151415', 'title': 'Legea nr. 92/2014 cu privire la energia termica si promovarea cogenerarii'},
    'L-114-2014': {'doc_id': '152635', 'title': 'Legea nr. 114/2014 cu privire la Agentia de Stat pentru Proprietatea Intelectuala'},
    'L-116-2014': {'doc_id': '151416', 'title': 'Legea cinematografiei nr. 116/2014'},
    'L-143-2014': {'doc_id': '151417', 'title': 'Legea nr. 143/2014 privind regimul articolelor pirotehnice'},
    'COD-150-2014': {'doc_id': '152774', 'title': 'Codul transporturilor rutiere nr. 150/2014'},
    'L-10-2016': {'doc_id': '151418', 'title': 'Legea nr. 10/2016 privind promovarea utilizarii energiei din surse regenerabile'},
    'L-19-2016': {'doc_id': '154793', 'title': 'Legea metrologiei nr. 19/2016'},
    'L-108-2016': {'doc_id': '156017', 'title': 'Legea nr. 108/2016 cu privire la gazele naturale'},
    'L-179-2016': {'doc_id': '149777', 'title': 'Legea nr. 179/2016 cu privire la intreprinderile mici si mijlocii'},
    'L-209-2016': {'doc_id': '154126', 'title': 'Legea nr. 209/2016 privind deseurile'},
    'L-254-2016': {'doc_id': '150082', 'title': 'Legea nr. 254/2016 cu privire la infrastructura nationala de date spatiale'},
    'L-291-2016': {'doc_id': '149724', 'title': 'Legea nr. 291/2016 cu privire la organizarea si desfasurarea jocurilor de noroc'},
    'L-102-2017': {'doc_id': '155337', 'title': 'Legea nr. 102/2017 cu privire la dispozitivele medicale'},
    'L-296-2017': {'doc_id': '141242', 'title': 'Legea nr. 296/2017 privind cerintele generale de igiena a produselor alimentare'},
    'L-105-2018': {'doc_id': '151185', 'title': 'Legea nr. 105/2018 cu privire la promovarea ocuparii fortei de munca si asigurarea de somaj'},
    'L-119-2018': {'doc_id': '151314', 'title': 'Legea nr. 119/2018 cu privire la medicamentele de uz veterinar'},
    'L-306-2018': {'doc_id': '152512', 'title': 'Legea nr. 306/2018 privind siguranta alimentelor'},
    'L-227-2022': {'doc_id': '152513', 'title': 'Legea nr. 227/2022 privind emisiile industriale'},
    'L-43-2023': {'doc_id': '151296', 'title': 'Legea nr. 43/2023 privind gazele fluorurate cu efect de sera'},
    'L-394-2023': {'doc_id': '141885', 'title': 'Legea nr. 394/2023 privind produsele alimentare si furajele modificate genetic'},
    'L-403-2023': {'doc_id': '154348', 'title': 'Legea nr. 403/2023 privind introducerea pe piata a produselor fitosanitare si pentru modificarea unor acte normative'},
    'L-422-2023': {'doc_id': '142263', 'title': 'Legea nr. 422/2023 privind masurile de protectie impotriva organismelor daunatoare plantelor'},
    'L-28-2024': {'doc_id': '149711', 'title': 'Legea nr. 28/2024 cu privire la frontiera de stat a Republicii Moldova'},
    'L-67-2024': {'doc_id': '152851', 'title': 'Legea nr. 67/2024 privind regimul explozivilor de uz civil'},
    'L-82-2024': {'doc_id': '147967', 'title': 'Legea nr. 82/2024 privind controalele oficiale in domeniul agroalimentar'},
    'COD-246-2024': {'doc_id': '152769', 'title': 'Codul subsolului nr. 246/2024'},
    'L-164-2025': {'doc_id': '152515', 'title': 'Legea nr. 164/2025 cu privire la energia electrica'},
    # 2026-09-25, la cererea lui Eugen ("ingereaza consolidarile viitoare neingerate"): 46 de versiuni cu data in viitor ale actelor detinute,
    # cele 23 din pending-consolidations.json si 23 ale celor 16 acte din perimetrul actelor permisive. Fiecare intra ca fisier SEPARAT, in
    # raw/papers/moldova-legal/viitor/<act>--<data>.md (cheia 'subdir'), cu 'future_of' si 'applies_from'; textul in vigoare azi din <act>.md
    # ramine neatins. Subfolderul nu e citit de graful de citare si de registrul HCC (listeaza numai folderul de sus); registrul in-force citeste
    # recursiv. Patru blob-uri din Chrome-ul lui Eugen (14,8 MB), hash SHA-256 pe parte verificat, 46 din 46.
    'L-599-1999--2026-12-28': {'doc_id': '152435', 'subdir': 'viitor', 'future_of': 'L-599-1999', 'applies_from': '2026-12-28',
        'title': 'Versiune viitoare, de la 2026-12-28, a actului L-599-1999'},
    'L-282-2004--2027-01-01': {'doc_id': '152993', 'subdir': 'viitor', 'future_of': 'L-282-2004', 'applies_from': '2027-01-01',
        'title': 'Versiune viitoare, de la 2027-01-01, a actului L-282-2004'},
    'L-149-2006--2027-03-24': {'doc_id': '156549', 'subdir': 'viitor', 'future_of': 'L-149-2006', 'applies_from': '2027-03-24',
        'title': 'Versiune viitoare, de la 2027-03-24, a actului L-149-2006'},
    'L-131-2007--2027-01-23': {'doc_id': '155473', 'subdir': 'viitor', 'future_of': 'L-131-2007', 'applies_from': '2027-01-23',
        'title': 'Versiune viitoare, de la 2027-01-23, a actului L-131-2007'},
    'L-131-2007--2029-01-01': {'doc_id': '156143', 'subdir': 'viitor', 'future_of': 'L-131-2007', 'applies_from': '2029-01-01',
        'title': 'Versiune viitoare, de la 2029-01-01, a actului L-131-2007'},
    'L-221-2007--2026-11-13': {'doc_id': '150048', 'subdir': 'viitor', 'future_of': 'L-221-2007', 'applies_from': '2026-11-13',
        'title': 'Versiune viitoare, de la 2026-11-13, a actului L-221-2007'},
    'L-221-2007--2027-11-30': {'doc_id': '155875', 'subdir': 'viitor', 'future_of': 'L-221-2007', 'applies_from': '2027-11-30',
        'title': 'Versiune viitoare, de la 2027-11-30, a actului L-221-2007'},
    'L-278-2007--2027-03-01': {'doc_id': '152957', 'subdir': 'viitor', 'future_of': 'L-278-2007', 'applies_from': '2027-03-01',
        'title': 'Versiune viitoare, de la 2027-03-01, a actului L-278-2007'},
    'L-278-2007--2029-01-01': {'doc_id': '150512', 'subdir': 'viitor', 'future_of': 'L-278-2007', 'applies_from': '2029-01-01',
        'title': 'Versiune viitoare, de la 2029-01-01, a actului L-278-2007'},
    'L-278-2007--2029-03-21': {'doc_id': '149694', 'subdir': 'viitor', 'future_of': 'L-278-2007', 'applies_from': '2029-03-21',
        'title': 'Versiune viitoare, de la 2029-03-21, a actului L-278-2007'},
    'L-68-2013--2026-11-10': {'doc_id': '154352', 'subdir': 'viitor', 'future_of': 'L-68-2013', 'applies_from': '2026-11-10',
        'title': 'Versiune viitoare, de la 2026-11-10, a actului L-68-2013'},
    'L-68-2013--2027-11-30': {'doc_id': '150071', 'subdir': 'viitor', 'future_of': 'L-68-2013', 'applies_from': '2027-11-30',
        'title': 'Versiune viitoare, de la 2027-11-30, a actului L-68-2013'},
    'L-19-2016--2027-01-01': {'doc_id': '154798', 'subdir': 'viitor', 'future_of': 'L-19-2016', 'applies_from': '2027-01-01',
        'title': 'Versiune viitoare, de la 2027-01-01, a actului L-19-2016'},
    'L-19-2016--2030-01-01': {'doc_id': '154817', 'subdir': 'viitor', 'future_of': 'L-19-2016', 'applies_from': '2030-01-01',
        'title': 'Versiune viitoare, de la 2030-01-01, a actului L-19-2016'},
    'L-179-2016--2027-01-01': {'doc_id': '155447', 'subdir': 'viitor', 'future_of': 'L-179-2016', 'applies_from': '2027-01-01',
        'title': 'Versiune viitoare, de la 2027-01-01, a actului L-179-2016'},
    'L-296-2017--2027-11-30': {'doc_id': '150086', 'subdir': 'viitor', 'future_of': 'L-296-2017', 'applies_from': '2027-11-30',
        'title': 'Versiune viitoare, de la 2027-11-30, a actului L-296-2017'},
    'L-105-2018--2026-12-10': {'doc_id': '156343', 'subdir': 'viitor', 'future_of': 'L-105-2018', 'applies_from': '2026-12-10',
        'title': 'Versiune viitoare, de la 2026-12-10, a actului L-105-2018'},
    'L-119-2018--2027-11-30': {'doc_id': '150088', 'subdir': 'viitor', 'future_of': 'L-119-2018', 'applies_from': '2027-11-30',
        'title': 'Versiune viitoare, de la 2027-11-30, a actului L-119-2018'},
    'L-394-2023--2027-11-30': {'doc_id': '150093', 'subdir': 'viitor', 'future_of': 'L-394-2023', 'applies_from': '2027-11-30',
        'title': 'Versiune viitoare, de la 2027-11-30, a actului L-394-2023'},
    'L-403-2023--2027-11-30': {'doc_id': '150096', 'subdir': 'viitor', 'future_of': 'L-403-2023', 'applies_from': '2027-11-30',
        'title': 'Versiune viitoare, de la 2027-11-30, a actului L-403-2023'},
    'L-422-2023--2027-11-30': {'doc_id': '150097', 'subdir': 'viitor', 'future_of': 'L-422-2023', 'applies_from': '2027-11-30',
        'title': 'Versiune viitoare, de la 2027-11-30, a actului L-422-2023'},
    'L-82-2024--2027-11-30': {'doc_id': '152850', 'subdir': 'viitor', 'future_of': 'L-82-2024', 'applies_from': '2027-11-30',
        'title': 'Versiune viitoare, de la 2027-11-30, a actului L-82-2024'},
    'L-82-2024--2028-05-08': {'doc_id': '147969', 'subdir': 'viitor', 'future_of': 'L-82-2024', 'applies_from': '2028-05-08',
        'title': 'Versiune viitoare, de la 2028-05-08, a actului L-82-2024'},
    'COD-1163-1997--2027-01-01': {'doc_id': '152862', 'subdir': 'viitor', 'future_of': 'COD-1163-1997', 'applies_from': '2027-01-01',
        'title': 'Versiune viitoare, de la 2027-01-01, a actului COD-1163-1997'},
    'COD-325-2022--2027-01-01': {'doc_id': '156086', 'subdir': 'viitor', 'future_of': 'COD-325-2022', 'applies_from': '2027-01-01',
        'title': 'Versiune viitoare, de la 2027-01-01, a actului COD-325-2022'},
    'L-98-2012--2027-01-01': {'doc_id': '155442', 'subdir': 'viitor', 'future_of': 'L-98-2012', 'applies_from': '2027-01-01',
        'title': 'Versiune viitoare, de la 2027-01-01, a actului L-98-2012'},
    'L-160-2011--2026-12-28': {'doc_id': '149496', 'subdir': 'viitor', 'future_of': 'L-160-2011', 'applies_from': '2026-12-28',
        'title': 'Versiune viitoare, de la 2026-12-28, a actului L-160-2011'},
    'L-160-2011--2027-01-01': {'doc_id': '150231', 'subdir': 'viitor', 'future_of': 'L-160-2011', 'applies_from': '2027-01-01',
        'title': 'Versiune viitoare, de la 2027-01-01, a actului L-160-2011'},
    'L-160-2011--2027-01-23': {'doc_id': '154051', 'subdir': 'viitor', 'future_of': 'L-160-2011', 'applies_from': '2027-01-23',
        'title': 'Versiune viitoare, de la 2027-01-23, a actului L-160-2011'},
    'L-160-2011--2027-05-21': {'doc_id': '154478', 'subdir': 'viitor', 'future_of': 'L-160-2011', 'applies_from': '2027-05-21',
        'title': 'Versiune viitoare, de la 2027-05-21, a actului L-160-2011'},
    'L-160-2011--2029-01-01': {'doc_id': '156152', 'subdir': 'viitor', 'future_of': 'L-160-2011', 'applies_from': '2029-01-01',
        'title': 'Versiune viitoare, de la 2029-01-01, a actului L-160-2011'},
    'L-435-2006--2027-01-01': {'doc_id': '156387', 'subdir': 'viitor', 'future_of': 'L-435-2006', 'applies_from': '2027-01-01',
        'title': 'Versiune viitoare, de la 2027-01-01, a actului L-435-2006'},
    'L-121-2007--2027-01-01': {'doc_id': '156384', 'subdir': 'viitor', 'future_of': 'L-121-2007', 'applies_from': '2027-01-01',
        'title': 'Versiune viitoare, de la 2027-01-01, a actului L-121-2007'},
    'L-121-2007--2027-11-30': {'doc_id': '150035', 'subdir': 'viitor', 'future_of': 'L-121-2007', 'applies_from': '2027-11-30',
        'title': 'Versiune viitoare, de la 2027-11-30, a actului L-121-2007'},
    'L-397-2003--2027-01-01': {'doc_id': '153025', 'subdir': 'viitor', 'future_of': 'L-397-2003', 'applies_from': '2027-01-01',
        'title': 'Versiune viitoare, de la 2027-01-01, a actului L-397-2003'},
    'L-397-2003--2028-01-01': {'doc_id': '156390', 'subdir': 'viitor', 'future_of': 'L-397-2003', 'applies_from': '2028-01-01',
        'title': 'Versiune viitoare, de la 2028-01-01, a actului L-397-2003'},
    'L-270-2018--2027-01-01': {'doc_id': '156397', 'subdir': 'viitor', 'future_of': 'L-270-2018', 'applies_from': '2027-01-01',
        'title': 'Versiune viitoare, de la 2027-01-01, a actului L-270-2018'},
    'L-52-2014--2026-12-09': {'doc_id': '156266', 'subdir': 'viitor', 'future_of': 'L-52-2014', 'applies_from': '2026-12-09',
        'title': 'Versiune viitoare, de la 2026-12-09, a actului L-52-2014'},
    'L-165-2023--2026-12-09': {'doc_id': '156269', 'subdir': 'viitor', 'future_of': 'L-165-2023', 'applies_from': '2026-12-09',
        'title': 'Versiune viitoare, de la 2026-12-09, a actului L-165-2023'},
    'L-121-2018--2027-03-27': {'doc_id': '148335', 'subdir': 'viitor', 'future_of': 'L-121-2018', 'applies_from': '2027-03-27',
        'title': 'Versiune viitoare, de la 2027-03-27, a actului L-121-2018'},
    'L-22-2025--2027-03-27': {'doc_id': '153697', 'subdir': 'viitor', 'future_of': 'L-22-2025', 'applies_from': '2027-03-27',
        'title': 'Versiune viitoare, de la 2027-03-27, a actului L-22-2025'},
    'L-274-2011--2027-01-01': {'doc_id': '156391', 'subdir': 'viitor', 'future_of': 'L-274-2011', 'applies_from': '2027-01-01',
        'title': 'Versiune viitoare, de la 2027-01-01, a actului L-274-2011'},
    'L-82-2017--2026-12-09': {'doc_id': '156268', 'subdir': 'viitor', 'future_of': 'L-82-2017', 'applies_from': '2026-12-09',
        'title': 'Versiune viitoare, de la 2026-12-09, a actului L-82-2017'},
    'L-229-2010--2027-01-01': {'doc_id': '152994', 'subdir': 'viitor', 'future_of': 'L-229-2010', 'applies_from': '2027-01-01',
        'title': 'Versiune viitoare, de la 2027-01-01, a actului L-229-2010'},
    'HG-149-2021--2027-07-01': {'doc_id': '156116', 'subdir': 'viitor', 'future_of': 'HG-149-2021', 'applies_from': '2027-07-01',
        'title': 'Versiune viitoare, de la 2027-07-01, a actului HG-149-2021'},
    'HG-146-2021--2027-07-01': {'doc_id': '156115', 'subdir': 'viitor', 'future_of': 'HG-146-2021', 'applies_from': '2027-07-01',
        'title': 'Versiune viitoare, de la 2027-07-01, a actului HG-146-2021'},

    # 2026-09-26, auditul din aceeasi zi (A1): trei acte intrate la 2026-09-25 prin `web_extract` din exportul PDF, fara ancore
    # si fara data de consolidare. Versiunile bune, din lista de versiuni de pe legis.md (citita 2026-09-26 din Chrome):
    #   COD-1316-2000: 155707 @ 06-08-2026 (curenta; cea tinuta, 122974, era din 14-08-2020), 156321 @ 09-12-2026 (viitoare)
    #   L-69-2016:     137679 @ 23-06-2026 (curenta; cea tinuta, 125333, era din 25-12-2020)
    #   L-230-2022:    149374 @ 10-06-2025 (curenta; cea tinuta, 133204, era textul din 2022), 140343 @ 01-01-2030 (viitoare)
    # Fisa nu da data abrogarii la niciunul dintre ele; antetul corpului de verificat la ingerare (memoria check-repeal).
    # HTML-ul NU este inca in legis-md-business/: Cloudflare a cerut bifa "Verify you are human" si nu se bifeaza de catre
    # asistent. Pina atunci verify_business_law.py sare peste ele (SARIT), iar fisierele raw actuale raman neatinse.
    'COD-1316-2000': {'doc_id': '155707', 'title': 'Codul familiei nr. 1316/2000'},
    'L-69-2016': {'doc_id': '137679', 'title': 'Legea nr. 69/2016 privind organizarea activitatii notarilor'},
    'L-230-2022': {'doc_id': '149374', 'title': 'Legea nr. 230/2022 privind dreptul de autor si drepturile conexe'},
    'COD-1316-2000--2026-12-09': {'doc_id': '156321', 'subdir': 'viitor', 'future_of': 'COD-1316-2000', 'applies_from': '2026-12-09',
        'title': 'Versiune viitoare, de la 2026-12-09, a actului COD-1316-2000'},
    'L-230-2022--2030-01-01': {'doc_id': '140343', 'subdir': 'viitor', 'future_of': 'L-230-2022', 'applies_from': '2030-01-01',
        'title': 'Versiune viitoare, de la 2030-01-01, a actului L-230-2022'},
    # 2026-09-26, verificarea consolidarilor vechi (36 de acte, listele de versiuni citite din Chrome): 34 sint inca cele mai noi in vigoare.
    # Trei versiuni gasite si NEingerate inca (Cloudflare a cerut din nou bifa): HG-1171-2018 156468 @ 22-09-2026 (in vigoare de 4 zile;
    # fisierul tinut, 144185, e din 19-07-2024), si doua viitoare 2027-03-01, L-23-2008 156490 si L-24-2008 156492. HG-1171-2018 se scrie
    # peste fisierul vechi (intrat in iulie prin alt script); vechiul ramine in git si in backup.
    'HG-1171-2018': {'doc_id': '156468', 'title': 'Hotarirea Guvernului nr. 1171/2018 pentru aprobarea Regulamentului privind armonizarea legislatiei Republicii Moldova cu legislatia Uniunii Europene'},
    'L-23-2008--2027-03-01': {'doc_id': '156490', 'subdir': 'viitor', 'future_of': 'L-23-2008', 'applies_from': '2027-03-01',
        'title': 'Versiune viitoare, de la 2027-03-01, a actului L-23-2008'},
    'L-24-2008--2027-03-01': {'doc_id': '156492', 'subdir': 'viitor', 'future_of': 'L-24-2008', 'applies_from': '2027-03-01',
        'title': 'Versiune viitoare, de la 2027-03-01, a actului L-24-2008'},
    # 2026-09-27: HG-1171-2018 s-a dovedit ABROGATA de la 22.09.2026 prin HG497 din 02.09.26 (MO466-469/22.09.26 art.527), care aproba un nou
    # Regulament privind armonizarea legislatiei cu legislatia UE. doc_id 156454 (unica versiune), gasit prin linkul markerului de abrogare din
    # 156468. Regulamentul nou e in puncte, ca cel vechi. HTML 154.859 octeti, luat din Chrome-ul lui Eugen.
    'HG-497-2026': {'doc_id': '156454', 'title': 'Hotarirea Guvernului nr. 497/2026 pentru aprobarea Regulamentului privind armonizarea legislatiei Republicii Moldova cu legislatia Uniunii Europene'},
    # 2026-09-26: fisierul principal al acestor acte tinea o consolidare cu data viitoare; acum principal = versiunea in vigoare (doc_id de mai sus),
    # iar fiecare versiune viitoare este aici. Facut de swap_future_main.py (CLAUDE.md, Outstanding work 8). Actele L-1134-1997, L-171-2012 (cnpf/) si
    # L-114-2012 (bnm/legal-ro/) au principalul in alt folder si nu au intrare de principal aici; verify_business_law.py le cauta acolo.
    'L-1134-1997--2028-01-01': {'doc_id': '154811', 'subdir': 'viitor', 'future_of': 'L-1134-1997', 'applies_from': '2028-01-01',
        'title': 'Versiune viitoare, de la 2028-01-01, a actului L-1134-1997'},
    'L-171-2012--2027-06-01': {'doc_id': '156016', 'subdir': 'viitor', 'future_of': 'L-171-2012', 'applies_from': '2027-06-01',
        'title': 'Versiune viitoare, de la 2027-06-01, a actului L-171-2012'},
    'COD-154-2003--2026-10-28': {'doc_id': '155518', 'subdir': 'viitor', 'future_of': 'COD-154-2003', 'applies_from': '2026-10-28',
        'title': 'Versiune viitoare, de la 2026-10-28, a actului COD-154-2003'},
    'COD-154-2003--2026-12-09': {'doc_id': '156323', 'subdir': 'viitor', 'future_of': 'COD-154-2003', 'applies_from': '2026-12-09',
        'title': 'Versiune viitoare, de la 2026-12-09, a actului COD-154-2003'},
    'COD-154-2003--2027-01-01': {'doc_id': '155882', 'subdir': 'viitor', 'future_of': 'COD-154-2003', 'applies_from': '2027-01-01',
        'title': 'Versiune viitoare, de la 2027-01-01, a actului COD-154-2003'},
    'HG-743-2024--2026-12-30': {'doc_id': '155190', 'subdir': 'viitor', 'future_of': 'HG-743-2024', 'applies_from': '2026-12-30',
        'title': 'Versiune viitoare, de la 2026-12-30, a actului HG-743-2024'},
    'L-132-2016--2027-01-01': {'doc_id': '155890', 'subdir': 'viitor', 'future_of': 'L-132-2016', 'applies_from': '2027-01-01',
        'title': 'Versiune viitoare, de la 2027-01-01, a actului L-132-2016'},
    'L-133-2016--2027-01-01': {'doc_id': '155891', 'subdir': 'viitor', 'future_of': 'L-133-2016', 'applies_from': '2027-01-01',
        'title': 'Versiune viitoare, de la 2027-01-01, a actului L-133-2016'},
    'L-1543-1998--2027-01-01': {'doc_id': '150226', 'subdir': 'viitor', 'future_of': 'L-1543-1998', 'applies_from': '2027-01-01',
        'title': 'Versiune viitoare, de la 2027-01-01, a actului L-1543-1998'},
    'COD-443-2004--2026-12-02': {'doc_id': '156146', 'subdir': 'viitor', 'future_of': 'COD-443-2004', 'applies_from': '2026-12-02',
        'title': 'Versiune viitoare, de la 2026-12-02, a actului COD-443-2004'},
    'COD-443-2004--2026-12-09': {'doc_id': '156325', 'subdir': 'viitor', 'future_of': 'COD-443-2004', 'applies_from': '2026-12-09',
        'title': 'Versiune viitoare, de la 2026-12-09, a actului COD-443-2004'},
    'COD-443-2004--2027-01-01': {'doc_id': '155964', 'subdir': 'viitor', 'future_of': 'COD-443-2004', 'applies_from': '2027-01-01',
        'title': 'Versiune viitoare, de la 2027-01-01, a actului COD-443-2004'},
    'COD-985-2002--2026-12-02': {'doc_id': '156133', 'subdir': 'viitor', 'future_of': 'COD-985-2002', 'applies_from': '2026-12-02',
        'title': 'Versiune viitoare, de la 2026-12-02, a actului COD-985-2002'},
    'COD-985-2002--2026-12-09': {'doc_id': '156270', 'subdir': 'viitor', 'future_of': 'COD-985-2002', 'applies_from': '2026-12-09',
        'title': 'Versiune viitoare, de la 2026-12-09, a actului COD-985-2002'},
    'L-181-2014--2027-01-01': {'doc_id': '153046', 'subdir': 'viitor', 'future_of': 'L-181-2014', 'applies_from': '2027-01-01',
        'title': 'Versiune viitoare, de la 2027-01-01, a actului L-181-2014'},
    'L-845-1992--2027-01-01': {'doc_id': '155963', 'subdir': 'viitor', 'future_of': 'L-845-1992', 'applies_from': '2027-01-01',
        'title': 'Versiune viitoare, de la 2027-01-01, a actului L-845-1992'},
    'L-114-2012--2027-01-01': {'doc_id': '155331', 'subdir': 'viitor', 'future_of': 'L-114-2012', 'applies_from': '2027-01-01',
        'title': 'Versiune viitoare, de la 2027-01-01, a actului L-114-2012'},
    'L-114-2012--2027-03-17': {'doc_id': '156446', 'subdir': 'viitor', 'future_of': 'L-114-2012', 'applies_from': '2027-03-17',
        'title': 'Versiune viitoare, de la 2027-03-17, a actului L-114-2012'},
    'COD-122-2003--2026-12-02': {'doc_id': '156138', 'subdir': 'viitor', 'future_of': 'COD-122-2003', 'applies_from': '2026-12-02',
        'title': 'Versiune viitoare, de la 2026-12-02, a actului COD-122-2003'},
    'COD-122-2003--2026-12-09': {'doc_id': '156277', 'subdir': 'viitor', 'future_of': 'COD-122-2003', 'applies_from': '2026-12-09',
        'title': 'Versiune viitoare, de la 2026-12-09, a actului COD-122-2003'},
    'L-1134-1997': {'doc_id': '154797', 'external_folder': True, 'title': 'principal in alt folder (cnpf/ sau bnm/legal-ro/); nu se scrie de acest script'},
    'L-171-2012': {'doc_id': '145907', 'external_folder': True, 'title': 'principal in alt folder (cnpf/ sau bnm/legal-ro/); nu se scrie de acest script'},
    'L-114-2012': {'doc_id': '155302', 'external_folder': True, 'title': 'principal in alt folder (cnpf/ sau bnm/legal-ro/); nu se scrie de acest script'},
    # 2026-09-26, matura completa a listelor de versiuni: versiuni viitoare ale unor acte deja tinute la zi, care lipseau din viitor/ (nici 09-25 nu le prinsese).
    # HTML din Edge (mărimi 151.606 ... 5.452.383 octeti).
    'COD-218-2008--2026-12-09': {'doc_id': '156265', 'subdir': 'viitor', 'future_of': 'COD-218-2008', 'applies_from': '2026-12-09',
        'title': 'Versiune viitoare, de la 2026-12-09, a actului COD-218-2008'},
    'COD-218-2008--2027-01-23': {'doc_id': '154054', 'subdir': 'viitor', 'future_of': 'COD-218-2008', 'applies_from': '2027-01-23',
        'title': 'Versiune viitoare, de la 2027-01-23, a actului COD-218-2008'},
    'COD-218-2008--2027-03-24': {'doc_id': '156548', 'subdir': 'viitor', 'future_of': 'COD-218-2008', 'applies_from': '2027-03-24',
        'title': 'Versiune viitoare, de la 2027-03-24, a actului COD-218-2008'},
    'COD-218-2008--2027-05-13': {'doc_id': '153634', 'subdir': 'viitor', 'future_of': 'COD-218-2008', 'applies_from': '2027-05-13',
        'title': 'Versiune viitoare, de la 2027-05-13, a actului COD-218-2008'},
    'COD-218-2008--2028-01-01': {'doc_id': '154800', 'subdir': 'viitor', 'future_of': 'COD-218-2008', 'applies_from': '2028-01-01',
        'title': 'Versiune viitoare, de la 2028-01-01, a actului COD-218-2008'},
    'COD-218-2008--2030-01-01': {'doc_id': '154803', 'subdir': 'viitor', 'future_of': 'COD-218-2008', 'applies_from': '2030-01-01',
        'title': 'Versiune viitoare, de la 2030-01-01, a actului COD-218-2008'},
    'CC-1107-2002--2027-01-01': {'doc_id': '149719', 'subdir': 'viitor', 'future_of': 'CC-1107-2002', 'applies_from': '2027-01-01',
        'title': 'Versiune viitoare, de la 2027-01-01, a actului CC-1107-2002'},
    'COD-116-2018--2027-01-01': {'doc_id': '149723', 'subdir': 'viitor', 'future_of': 'COD-116-2018', 'applies_from': '2027-01-01',
        'title': 'Versiune viitoare, de la 2027-01-01, a actului COD-116-2018'},
    'COD-174-2018--2030-01-01': {'doc_id': '156376', 'subdir': 'viitor', 'future_of': 'COD-174-2018', 'applies_from': '2030-01-01',
        'title': 'Versiune viitoare, de la 2030-01-01, a actului COD-174-2018'},
    'COD-95-2021--2027-01-01': {'doc_id': '149774', 'subdir': 'viitor', 'future_of': 'COD-95-2021', 'applies_from': '2027-01-01',
        'title': 'Versiune viitoare, de la 2027-01-01, a actului COD-95-2021'},
    'COD-95-2021--2029-01-01': {'doc_id': '146678', 'subdir': 'viitor', 'future_of': 'COD-95-2021', 'applies_from': '2029-01-01',
        'title': 'Versiune viitoare, de la 2029-01-01, a actului COD-95-2021'},
    'L-192-1998--2027-03-17': {'doc_id': '156445', 'subdir': 'viitor', 'future_of': 'L-192-1998', 'applies_from': '2027-03-17',
        'title': 'Versiune viitoare, de la 2027-03-17, a actului L-192-1998'},
    # 2026-09-27, gasita la matura versiunilor de pe legis.md: L-202-2017 art. 14 si L-548-1995
    # art. 5/75^2 primesc, de la 17.03.2027, dispozitii noi "conform legislatiei privind piata
    # criptoactivelor" -- act pe care vaultul nu-l avea deloc. Cautare in titlu fara diacritice
    # "piata criptoactivelor" (2 rezultate: DP773/2026, decretul de promulgare, doc_id 156423, si
    # actul insusi, doc_id 156426). Verificat pe fisa: adoptata 24.08.2026, publicata 17.09.2026
    # (MO456-459 art.479), in vigoare 17.03.2027, NICIODATA modificata (fara rind "Data
    # modificarii"), fara data de abrogare -- singura versiune, ca la L-325-2025. Ca acolo,
    # intregul act e viitor: nu exista text "in vigoare azi" de pastrat separat, deci fisierul
    # principal poarta data viitoare (whole_act_future in extract_doc/main), fara subdir.
    # Verificat pe HTML inainte de rulare: 107 articole, 15 <sup>, 29 span-uri ridicate prin CSS,
    # fara CUPRINS. Este cadrul de tip MiCA al R. Moldova (Regulamentul (UE) 2023/1114, de
    # confirmat la citire). Prima lege gasita la matura de versiuni, nu prin coada grafului de
    # citare -- ceea ce inseamna ca acele 4941 de muchii act nu o cunosc inca.
    'L-180-2026': {'doc_id': '156426',
                   'title': 'Legea nr. 180/2026 privind piata criptoactivelor'},
    # 2026-09-27, primele trei din coada de ingerare a grafului de citare, prioritizate dupa
    # coloana care conteaza (nr. de acte detinute care le citeaza, nu mentiunile brute): toate
    # trei la 13 acte citatoare. Titlurile nu erau stiute dinainte; gasite prin cautare Google
    # ("Legea nr. N/AAAA" Moldova), apoi confirmate si localizate pe legis.md prin cautare in
    # titlu (fara diacritice). Ambele metode uzuale de cautare in titlu au esuat o data fiecare:
    # "schimbul de date si interoperabilitate" nu gaseste LP142/2018 fiindca titlul din
    # inregistrare e scris gresit, "interoperabiltate" (fara al doilea i) -- a patra sursa
    # gasita cu clasa asta de defect (v. CLAUDE.md, sectiunea 4); gasit abia prin cautarea mai
    # larga "schimbul de date" si citind randurile (metoda getAjaxContent, DOM, nu regex pe
    # HTML brut). Curl tot blocat de Cloudflare; HTML luat din Chrome-ul lui Eugen prin fetch
    # same-origin + POST la un receiver local pe 8765, ca la P8/BNM.
    #
    # CAPCANA DE LISTA la primele doua, a treia oara dupa L-133-2011 si L-131-2012: randul de
    # cautare (si getResults?doc_id= implicit) trimit direct la cea mai noua consolidare din
    # istoric, care aici e VIITOARE la ambele -- 154794@2027-01-01 (LP91/2026) pentru 235/2011,
    # 155459@2030-01-01 (LP62/2026) pentru 142/2018. Verificat pe lista de versiuni a fiecarei
    # pagini (showDetails), nu presupus: cea in vigoare azi (2026-09-27) e cea IMEDIAT sub, cu
    # data trecuta. L-231-2010 nu are aceasta capcana: randul de cautare trimite deja la
    # 154335@2026-08-10, trecuta.
    #
    # Verificat pe HTML inainte de rulare, cele trei consolidari CURENTE: fara CUPRINS la
    # niciuna, fara "Just a moment" (continut real), fara "ABROGAT" in antet. <sup>: 81 (235/2011),
    # 3 (142/2018), 84 (231/2010); niciun span ridicat prin CSS (top:-Nem) la niciuna.
    'L-235-2011': {'doc_id': '151201',
                   'title': 'Legea nr. 235/2011 privind activitatile de acreditare si de '
                            'evaluare a conformitatii'},
    'L-235-2011--2027-01-01': {'doc_id': '154794', 'subdir': 'viitor', 'future_of': 'L-235-2011',
        'applies_from': '2027-01-01',
        'title': 'Versiune viitoare, de la 2027-01-01, a actului L-235-2011'},
    'L-142-2018': {'doc_id': '142805',
                   'title': 'Legea nr. 142/2018 cu privire la schimbul de date si '
                            'interoperabilitate'},
    'L-142-2018--2030-01-01': {'doc_id': '155459', 'subdir': 'viitor', 'future_of': 'L-142-2018',
        'applies_from': '2030-01-01',
        'title': 'Versiune viitoare, de la 2030-01-01, a actului L-142-2018'},
    'L-231-2010': {'doc_id': '154335',
                   'title': 'Legea nr. 231/2010 cu privire la comertul interior'},
    # 2026-09-28, urmatoarele trei rinduri ale cozii de ingerare a grafului de citare (dupa
    # numarul de acte detinute care le citeaza, coloana care conteaza, nu mentiunile brute):
    # L-48-2023 (13 acte), L-287-2017 (12 acte), L-139-2010 (11 acte). Titlurile gasite prin
    # Google, doc_id-urile prin cautare in titlu pe legis.md (getAjaxContent + DOMParser, ca la
    # lotul de ieri). Curl tot blocat de Cloudflare; HTML luat prin Chrome-ul lui Eugen. Browserul
    # intern al sesiunii a ramas blocat la verificare chiar si dupa asteptari repetate, ca pe
    # 16 septembrie; tab-urile Chrome au nevoie de reincercare pe tab nou cind se blocheaza (tab-ul
    # de cautare initial a inghetat, tab nou a mers dupa opt secunde de asteptare).
    #
    # L-287-2017 repeta CAPCANA DE VERSIUNE de ieri: randul de cautare trimite la 154725@2027-01-01
    # (viitoare), textul de azi e 140124@2025-01-01, imediat sub ea in lista. Titlul din fisa e
    # trunchiat, "contabilitatii si raportarii financiare", ca la L-1543-1998 si L-149-2012.
    #
    # L-139-2010 e o CAPCANA NOUA, mai importanta decat cele de pina acum: randul de cautare
    # poarta chiar in tabelul de rezultate marcajul "Abrogat", nu "Modificat". Verificat pe pagina
    # actului: "Abrogata prin LP230 din 28.07.22, MO278-282/09.09.22 art.578; in vigoare 09.10.22".
    # Succesorul, Legea 230/2022 privind dreptul de autor si drepturile conexe, ESTE DEJA IN VAULT
    # (`L-230-2022`, ingerata 2026-09-25/26 din alt lot, 123 ancore). Deci graful de citare aici nu
    # gresete ca la L-133-2011 (unde succesorul lipsea): raspunsul viu la cele 11 trimiteri exista
    # deja. Se ingereaza totusi L-139-2010, ca L-133-2011/COD-3-2009/HG-1171-2018: textul guverneaza
    # faptele dinainte de 09.10.2022, iar cele 11 acte care il citeaza pot viza fapte de atunci.
    # Consolidarea 133300@09.10.2022 este chiar cea de la data abrogarii (ultima stare a textului
    # inainte de inlocuire), la fel cum s-a ales pentru L-133-2011. `repeal_of()` prinde marcajul
    # automat si scrie avertismentul in fisier; nu s-a scris nimic manual pentru asta.
    #
    # Verificat pe HTML inainte de rulare, toate patru: fara CUPRINS, fara "Just a moment", fara
    # span ridicat prin CSS. <sup>: 0 (48/2023), 2 (287/2017, ambele consolidari), 5 (139/2010).
    'L-48-2023': {'doc_id': '152655',
                  'title': 'Legea nr. 48/2023 privind securitatea cibernetica'},
    'L-287-2017': {'doc_id': '140124',
                   'title': 'Legea contabilitatii si raportarii financiare nr. 287/2017'},
    'L-287-2017--2027-01-01': {'doc_id': '154725', 'subdir': 'viitor', 'future_of': 'L-287-2017',
        'applies_from': '2027-01-01',
        'title': 'Versiune viitoare, de la 2027-01-01, a actului L-287-2017'},
    'L-139-2010': {'doc_id': '133300',
                   'title': 'Legea nr. 139/2010 privind dreptul de autor si drepturile conexe '
                            '(ABROGATA de la 09.10.2022 prin L-230-2022)'},
    'L-989-2002': {'doc_id': '155740',
                   'title': 'Legea nr. 989/2002 cu privire la activitatea de evaluare'},
    'L-989-2002--2027-01-01': {'doc_id': '150253', 'subdir': 'viitor', 'future_of': 'L-989-2002',
        'applies_from': '2027-01-01',
        'title': 'Versiune viitoare, de la 2027-01-01, a actului L-989-2002'},
    'L-139-2012': {'doc_id': '152604',
                   'title': 'Legea nr. 139/2012 cu privire la ajutorul de stat'},
    'L-139-2012--2027-03-17': {'doc_id': '156439', 'subdir': 'viitor', 'future_of': 'L-139-2012',
        'applies_from': '2027-03-17',
        'title': 'Versiune viitoare (abrogare programata prin LP182/2026), de la 2027-03-17, '
                 'a actului L-139-2012'},
    'L-172-2014': {'doc_id': '154286',
                   'title': 'Legea nr. 172/2014 privind aprobarea Nomenclaturii combinate a '
                            'marfurilor (fara anexa Nomenclaturii, tinuta separat pe legis.md)'},
    # 2026-09-28, al patrulea val al cozii de ingerare a grafului de citare: L-11-2017 (8 acte
    # citatoare), L-137-2015 (8 acte) si L-277-2018 (8 acte), toate trei egale, alese dupa numarul
    # de mentiuni ca departajare (17, 14, 14). Gasite prin Google, doc_id-uri prin cautare in titlu
    # pe legis.md, fara capcane de Cloudflare interactiv de data asta.
    #
    # L-137-2015 e A DOUA capcana de abrogare deja cunoscuta dinainte de ingerare: manifestul o
    # documenteaza la ingerarea L-9-2026 (2026-09-16) - "Legea nr. 137/2015 cu privire la mediere
    # ... NU mai este legea in vigoare", abrogata de LP9/2026 la data intrarii lui in vigoare.
    # Verificat aici din nou, nu doar presupus din nota veche: "Abrogata prin LP9 din 12.02.26,
    # ... in vigoare 12.09.26" - trecuta fata de azi (2026-09-28), deci abrogarea e deja efectiva,
    # spre deosebire de L-139-2012 de ieri. Succesorul L-9-2026 e deja detinut. Se ingereaza totusi
    # L-137-2015, ca L-139-2010/L-133-2011: 8 acte inca trimit la ea, textul guverneaza faptele
    # dinainte de 12.09.2026 (doar de doua saptamini in urma).
    #
    # L-11-2017 (evaluarea strategica de mediu, transpune Directiva 2001/42/CE) si L-277-2018
    # (substantele chimice) sint acte curente, fara capcane de versiune sau de abrogare - rindul
    # de cautare trimite direct la consolidarea trecuta cea mai noua la amindoua.
    #
    # Verificat pe HTML inainte de rulare, toate trei: fara CUPRINS, fara "Just a moment", fara
    # span ridicat prin CSS. <sup>: 35 (11/2017), 4 (137/2015), 4 (277/2018).
    'L-11-2017': {'doc_id': '154127',
                  'title': 'Legea nr. 11/2017 privind evaluarea strategica de mediu'},
    'L-137-2015': {'doc_id': '153426',
                   'title': 'Legea nr. 137/2015 cu privire la mediere '
                            '(ABROGATA de la 12.09.2026 prin L-9-2026)'},
    'L-277-2018': {'doc_id': '154128',
                   'title': 'Legea nr. 277/2018 privind substantele chimice'},
    # 2026-09-28, al cincilea val al cozii de ingerare a grafului de citare: L-419-2006 (8 acte
    # citatoare), L-184-2016 (7 acte) si L-187-2022 (7 acte), alese dupa mentiuni intre cele patru
    # egale la 7 (16, 14, 14, 9). Gasite prin Google, doc_id-uri prin cautare in titlu pe legis.md.
    #
    # L-419-2006 (datoria sectorului public, garantiile de stat si recreditarea de stat) nu are
    # nicio consolidare mai noua de 21.10.2023 - peste doi ani, deci va intra in flagul "stale
    # consolidations" al coverage, nu o capcana, doar o consolidare veche fara amendamente recente.
    #
    # L-184-2016 (contractele de garantie financiara) e relevanta direct pentru perimetrul CNPF/BNM
    # deja detinut - transpune acquis-ul Acordului de Asociere, cap. 9 "Servicii financiare" (gasit
    # in rezultatele Google). Fara capcane de versiune sau de titlu.
    #
    # L-187-2022 (condominiu) e A SASEA CAPCANA DE LISTA, de alt fel decit cele de pina acum:
    # randul de cautare trimite la 155742@2026-08-06, dar lista de versiuni are 154485@2026-08-21
    # DEASUPRA ei (data mai noua, ambele trecute fata de azi) - nu o consolidare viitoare, ci pur
    # si simplu randul de cautare nu e cea mai noua dintre versiunile TRECUTE. Se ia 154485.
    #
    # Verificat pe HTML inainte de rulare, toate trei: fara CUPRINS, fara "Just a moment", fara
    # span ridicat prin CSS. <sup>: 4 (419/2006), 0 (184/2016), 12 (187/2022).
    'L-419-2006': {'doc_id': '139640',
                   'title': 'Legea nr. 419/2006 cu privire la datoria sectorului public, '
                            'garantiile de stat si recreditarea de stat'},
    'L-184-2016': {'doc_id': '155573',
                   'title': 'Legea nr. 184/2016 cu privire la contractele de garantie '
                            'financiara'},
    'L-187-2022': {'doc_id': '154485',
                   'title': 'Legea nr. 187/2022 cu privire la condominiu'},
    # 2026-09-28, al saselea val al cozii de ingerare a grafului de citare: L-407-2006 (7 acte
    # citatoare), L-29-2018 (7 acte) si L-202-2013 (7 acte), departajate dupa mentiuni (14, 13, 11).
    # Ultimele doua sint direct relevante perimetrului CNPF/BNM deja detinut: L-202-2013 (creditul
    # de consum, transpune Directiva 2008/48/CE) e citata explicit de CNPF si BNM in surse gasite
    # prin Google.
    #
    # L-407-2006 (legea veche a asigurarilor) e A TREIA capcana de abrogare cu succesor deja
    # detinut, dar cu un twist nou: randul de cautare poarta "Abrogat", confirmat pe pagina -
    # "Abrogata prin LP92 din 07.04.22, ... in vigoare 01.01.23", succesorul fiind L-92-2022
    # (deja in vault, perimetrul cnpf/). DAR lista de versiuni are o consolidare CHIAR MAI NOUA
    # decit cea a abrogarii, 123206@2023-07-01, care poarta nu marcajul de abrogare ci
    # "MODIFICAT LP178 din 11.09.20 ... in vigoare 01.07.23" - adica cel putin o dispozitie a
    # actului "abrogat" a continuat sa fie amendata si sa intre in vigoare DUPA data generala a
    # abrogarii. Acelasi tipar ca legea gutuita L-550-1995 (doar cateva articole in vigoare), gasit
    # aici pentru prima data la un act altfel complet abrogat. Se ia 123206, nu 133979 (starea de
    # la data abrogarii), tocmai pentru ca 123206 e starea REALA mai completa/mai tirzie a textului.
    # doc_id-ul din randul de cautare, 133979, NU e folosit.
    #
    # Verificat pe HTML inainte de rulare, toate patru: fara CUPRINS, fara "Just a moment", fara
    # span ridicat prin CSS. <sup>: 86 (407/2006, cel mai mare din tot corpusul ingerat pina acum),
    # 12 (29/2018 curent), 10 (29/2018 viitor), 4 (202/2013).
    # RECONCILIAT 2026-09-30 (vezi log.md): valul 6 retinuse 123206@2023-07-01, o proiectie
    # pregatita in 2020 pentru LP178/2020 (in vigoare 01.07.23, DUPA abrogarea prin L-92-2022 de la
    # 01.01.23); diferenta fata de 133979 e doar antetul si redefinirea notiunii "autoritate de
    # supraveghere", niciodata aplicabila. Se foloseste 133979@2023-01-01, cea a abrogarii.
    'L-407-2006': {'doc_id': '133979',
                   'title': 'Legea nr. 407/2006 cu privire la asigurari '
                            '(ABROGATA de la 01.01.2023 prin L-92-2022)'},
    'L-29-2018': {'doc_id': '150232',
                  'title': 'Legea nr. 29/2018 privind delimitarea proprietatii publice'},
    'L-29-2018--2027-01-01': {'doc_id': '152997', 'subdir': 'viitor', 'future_of': 'L-29-2018',
        'applies_from': '2027-01-01',
        'title': 'Versiune viitoare, de la 2027-01-01, a actului L-29-2018'},
    'L-202-2013': {'doc_id': '151074',
                   'title': 'Legea nr. 202/2013 privind contractele de credit pentru '
                            'consumatori'},
    # 2026-09-30, al saptelea val al cozii de ingerare a grafului de citare, recalculata din
    # citation-graph.json (generat 2026-09-28, dupa valul 6): L-271-2017 (7 acte citatoare, 11
    # mentiuni), L-182-2008 (7 acte, 9 mentiuni) si L-74-2020 (6 acte, dar 28 de mentiuni - cea
    # mai citata dintre cele de 6). Titlurile si doc_id-urile prin cautare in titlu pe legis.md,
    # ruta Chrome (curl a fost din nou 403 Cloudflare azi); HTML-ul trimis prin POST no-cors la
    # un receptor local, verificat pe dimensiune si pe "Just a moment".
    #
    # L-271-2017 (auditul situatiilor financiare, transpune Directiva 2014/56/UE): cea mai noua
    # consolidare, 153011@2025-12-31, e trecuta; nu are versiuni viitoare in lista.
    #
    # L-182-2008 (aprobarea Regulamentului Centrului National pentru Protectia Datelor cu
    # Caracter Personal) e A PATRA capcana de abrogare cu succesor deja detinut: "Abrogata prin
    # LP195 din 25.07.24, MO367-369/23.08.24 art.574; in vigoare 23.08.26" (aceeasi operatiune
    # care a abrogat L-133-2011). Consolidarea 144822@2026-08-23 e cea a abrogarii, trecuta
    # fata de azi. Succesor: L-195-2024, deja detinut.
    #
    # L-74-2020 (achizitiile in sectoarele energeticii, apei, transporturilor si serviciilor
    # postale): lista de versiuni are doua consolidari VIITOARE deasupra celei in vigoare -
    # 156087@2027-01-02 si 155279@2027-01-01 - iar cea in vigoare azi e 153662@2026-04-01
    # (aceeasi capcana ca L-171-2012 si cele doisprezece din matura din 26.09). Cele doua
    # viitoare merg in viitor/.
    'L-271-2017': {'doc_id': '153011',
                   'title': 'Legea nr. 271/2017 privind auditul situatiilor financiare'},
    'L-182-2008': {'doc_id': '144822',
                   'title': 'Legea nr. 182/2008 cu privire la aprobarea Regulamentului '
                            'Centrului National pentru Protectia Datelor cu Caracter Personal '
                            '(ABROGATA de la 23.08.2026 prin L-195-2024)'},
    'L-74-2020': {'doc_id': '153662',
                  'title': 'Legea nr. 74/2020 privind achizitiile in sectoarele energeticii, '
                           'apei, transporturilor si serviciilor postale'},
    'L-74-2020--2027-01-01': {'doc_id': '155279', 'subdir': 'viitor', 'future_of': 'L-74-2020',
        'applies_from': '2027-01-01',
        'title': 'Versiune viitoare, de la 2027-01-01, a actului L-74-2020'},
    'L-74-2020--2027-01-02': {'doc_id': '156087', 'subdir': 'viitor', 'future_of': 'L-74-2020',
        'applies_from': '2027-01-02',
        'title': 'Versiune viitoare, de la 2027-01-02, a actului L-74-2020'},
    # 2026-09-30, al optulea val al cozii de ingerare a grafului de citare (graful regenerat dupa
    # valul 7): L-107-2016 (7 acte citatoare, 28 mentiuni), COD-152-2014 (6 acte, 12 mentiuni) si
    # L-162-2023 (6 acte, 12 mentiuni), primele trei dupa (acte, mentiuni, ordinea alfabetica).
    # HTML luat prin Chrome (curl 403), trimis printr-un receptor local; prima incercare a picat
    # pentru ca un receptor orfan din valul anterior asculta inca pe 8765 si inghitea cererile.
    #
    # L-107-2016 (energia electrica, vechea lege) e A CINCEA capcana de abrogare cu succesor deja
    # detinut: "Abrogata prin LP164 din 26.06.25, MO437-440/19.08.25 art.598; in vigoare
    # 19.08.25", succesorul L-164-2025 (deja detinut). Consolidarea 150245@2025-08-19 e prima din
    # lista de versiuni.
    #
    # COD-152-2014 (Codul educatiei) are doua versiuni VIITOARE (156379@2030-01-01,
    # 153379@2027-01-01) deasupra celei in vigoare, 156377@2026-09-14 - tot capcana de lista,
    # trecuta de o zi-doua in urma. Cele doua viitoare merg in viitor/.
    #
    # L-162-2023 (supravegherea pietei si conformitatea produselor): 148054@2025-09-27, cea mai
    # noua, trecuta; fara versiuni viitoare in lista.
    'L-107-2016': {'doc_id': '150245',
                   'title': 'Legea nr. 107/2016 cu privire la energia electrica '
                            '(ABROGATA de la 19.08.2025 prin L-164-2025)'},
    'COD-152-2014': {'doc_id': '156377',
                     'title': 'Codul educatiei al Republicii Moldova nr. 152/2014'},
    'COD-152-2014--2027-01-01': {'doc_id': '153379', 'subdir': 'viitor',
        'future_of': 'COD-152-2014', 'applies_from': '2027-01-01',
        'title': 'Versiune viitoare, de la 2027-01-01, a actului COD-152-2014'},
    'COD-152-2014--2030-01-01': {'doc_id': '156379', 'subdir': 'viitor',
        'future_of': 'COD-152-2014', 'applies_from': '2030-01-01',
        'title': 'Versiune viitoare, de la 2030-01-01, a actului COD-152-2014'},
    'L-162-2023': {'doc_id': '148054',
                   'title': 'Legea nr. 162/2023 privind supravegherea pietei si conformitatea '
                            'produselor'},
    # 2026-09-30, al noualea val al cozii de ingerare a grafului de citare (regenerat dupa valul 8):
    # L-982-2000 (7 acte citatoare), L-174-2017 (6 acte, 64 mentiuni) si L-279-2017 (6 acte, 12
    # mentiuni). HTML luat prin Chrome (curl 403), trimis printr-un receptor local pornit UN SINGUR
    # proces (verificat cu netstat inainte), apoi verificat pe disc.
    #
    # L-982-2000 (accesul la informatie) e A SASEA capcana de abrogare cu succesor deja detinut:
    # "Abrogata prin LP148 din 09.06.23, MO234/08.07.23 art.410; in vigoare 08.01.24", succesorul
    # L-148-2023 (deja detinut). Consolidarea 137924@2024-01-08 e prima din lista.
    #
    # L-279-2017 (informarea consumatorului cu privire la produsele alimentare) e A SAPTEA CAPCANA
    # DE LISTA, de un fel nou: lista de versiuni are deasupra 137017@2025-11-11, dar acela e o
    # versiune pregatita in 2023 pentru LP97/2023 (antet "MODIFICAT LP97 din 27.04.23 ... in vigoare
    # 11.11.25") care NU cuprinde LP27/2025 (in vigoare 19.03.25); randul de cautare arata 147674
    # (antet LP27/2025). Se ia 147674, cea cu ultima modificare reala; 137017 nu se foloseste.
    #
    # L-174-2017 (energetica) a fost republicata (MO 480-482/15.12.2023); 155923@2026-08-20 (LP164
    # din 30.07.26) e cea mai noua, trecuta.
    'L-982-2000': {'doc_id': '137924',
                   'title': 'Legea nr. 982/2000 privind accesul la informatie '
                            '(ABROGATA de la 08.01.2024 prin L-148-2023)'},
    'L-279-2017': {'doc_id': '147674',
                   'title': 'Legea nr. 279/2017 privind informarea consumatorului cu privire la '
                            'produsele alimentare'},
    'L-174-2017': {'doc_id': '155923',
                   'title': 'Legea nr. 174/2017 cu privire la energetica'},
    # 2026-09-30, al zecelea val al cozii de ingerare a grafului de citare (regenerat dupa valul 9):
    # L-151-2022 (6 acte citatoare, 15 mentiuni), L-36-2016 (6 acte, 11) si L-174-2021 (6 acte, 11).
    # HTML luat prin Chrome, un singur receptor (netstat inainte), verificat pe disc.
    #
    # L-36-2016 (comunicatiile postale) este citata de L-114-2012 art. 5 si 75 (prestatorii de
    # servicii postale care presteaza servicii de plata) si de COD-1163-1997 art. 226^11: relevanta
    # pentru perimetrul BNM. 142799@2025-01-01 e prima din lista si coincide cu randul de cautare;
    # antetul ei, insa, nu are nicio modificare mai noua decit LP58/2024.
    #
    # L-174-2021 (mecanismul de examinare a investitiilor de importanta pentru securitatea statului)
    # are in lista 147693@2030-01-01 DEASUPRA celei in vigoare, 155741@2026-08-06. Antetul lui
    # 147693 spune "LP33 din 27.02.25 ... in vigoare 01.01.30": 2030-01-01 e data-placeholder a
    # legis.md pentru o conditie (aderarea la UE), nu o data juridica, ca la L-1260-2002. Merge in
    # viitor/, nu se citeaza ca drept in vigoare.
    'L-151-2022': {'doc_id': '150494',
                   'title': 'Legea nr. 151/2022 privind functionarea in conditii de siguranta a '
                            'obiectivelor industriale si a instalatiilor tehnice potential '
                            'periculoase'},
    'L-36-2016': {'doc_id': '142799',
                  'title': 'Legea nr. 36/2016 a comunicatiilor postale'},
    'L-174-2021': {'doc_id': '155741',
                   'title': 'Legea nr. 174/2021 privind mecanismul de examinare a investitiilor '
                            'de importanta pentru securitatea statului'},
    'L-174-2021--2030-01-01': {'doc_id': '147693', 'subdir': 'viitor', 'future_of': 'L-174-2021',
        'applies_from': '2030-01-01',
        'title': 'Versiune viitoare, de la 2030-01-01 (data-placeholder legis.md), a actului '
                 'L-174-2021'},
    # 2026-09-30, al unsprezecelea val al cozii de ingerare a grafului de citare (regenerat dupa
    # valul 10): L-241-2007 (7 acte citatoare, 12 mentiuni), L-113-2007 (7 acte, 7) si L-156-1998
    # (6 acte, 7). HTML luat din legis.md in browserul integrat al aplicatiei, NU din Edge: ambele
    # browsere au inceput sa blocheze orice fetch catre 127.0.0.1 din paginile legis.md (inclusiv
    # cu no-cors si imagini), desi curl catre receptor mergea. Ruta care a functionat: textul
    # se pune in window.name, pagina navigheaza la nivel superior la http://127.0.0.1:8767/c.html
    # (navigarea nu e restrictionata) si pagina receptorului isi posteaza window.name catre propria
    # origine.
    #
    # L-241-2007 (comunicatiile electronice) NU e abrogata azi: 148404@2026-01-01 poarta antetul
    # "MODIFICAT LP72 din 10.04.25 ... in vigoare 01.01.26", iar 148407@2027-05-13 "Abrogata prin
    # LP72 din 10.04.25 ... in vigoare 13.05.27". Abrogarea prin L-72-2025 e deci programata, ca la
    # L-139-2012; 148407 merge in viitor/.
    #
    # L-156-1998 (sistemul public de pensii): 148342@2025-05-01 e in vigoare; 155512@2026-10-28
    # (LP138 din 09.07.26) e viitoare, in viitor/.
    #
    # L-113-2007 (Legea contabilitatii, cea veche): NU e abrogata - 137025@2023-06-11 (LP96/2023),
    # inca aplicata institutiilor bugetare (citata asa de COD-325-2022 si L-181-2014); peste doi
    # ani in urma, va intra in flagul "stale consolidations".
    'L-241-2007': {'doc_id': '148404',
                   'title': 'Legea nr. 241/2007 comunicatiilor electronice (abrogare programata '
                            'prin L-72-2025 la 13.05.2027)'},
    'L-241-2007--2027-05-13': {'doc_id': '148407', 'subdir': 'viitor', 'future_of': 'L-241-2007',
        'applies_from': '2027-05-13',
        'title': 'Versiune viitoare, de la 2027-05-13 (abrogata), a actului L-241-2007'},
    'L-113-2007': {'doc_id': '137025',
                   'title': 'Legea nr. 113/2007 contabilitatii'},
    'L-156-1998': {'doc_id': '148342',
                   'title': 'Legea nr. 156/1998 privind sistemul public de pensii'},
    'L-156-1998--2026-10-28': {'doc_id': '155512', 'subdir': 'viitor', 'future_of': 'L-156-1998',
        'applies_from': '2026-10-28',
        'title': 'Versiune viitoare, de la 2026-10-28, a actului L-156-1998'},
    # 2026-09-30, al doisprezecelea val al cozii de ingerare a grafului de citare (regenerat dupa
    # valul 11): L-152-2022 (5 acte citatoare, 27 mentiuni), L-440-2001 (5 acte, 13) si L-140-2013
    # (5 acte, 7). HTML luat din browserul integrat prin ruta window.name (vezi valul 11).
    #
    # L-152-2022 (organismele modificate genetic): 151256@2026-08-29 (LP199 din 10.07.25, in vigoare
    # 29.08.26) e prima din lista si in vigoare de ieri-alaltaieri; fara versiuni viitoare.
    # L-440-2001 (zonele economice libere): 154346@2026-05-11 (LP80/2026), prima din lista.
    # L-140-2013 (protectia speciala a copiilor aflati in situatie de risc): lista are 156331@2026-12-09
    # (LP167 din 30.07.26) DEASUPRA celei in vigoare, 146836@2025-01-16; cea viitoare in viitor/.
    'L-152-2022': {'doc_id': '151256',
                   'title': 'Legea nr. 152/2022 cu privire la reglementarea si controlul '
                            'organismelor modificate genetic'},
    'L-440-2001': {'doc_id': '154346',
                   'title': 'Legea nr. 440/2001 cu privire la zonele economice libere'},
    'L-140-2013': {'doc_id': '146836',
                   'title': 'Legea nr. 140/2013 privind protectia speciala a copiilor aflati in '
                            'situatie de risc si a copiilor separati de parinti'},
    'L-140-2013--2026-12-09': {'doc_id': '156331', 'subdir': 'viitor', 'future_of': 'L-140-2013',
        'applies_from': '2026-12-09',
        'title': 'Versiune viitoare, de la 2026-12-09, a actului L-140-2013'},
    # 2026-09-30, al treisprezecelea val al cozii de ingerare a
    # grafului de citare (graful regenerat dupa valul 12): L-509-1995 (5 acte citatoare, 7 mentiuni),
    # L-50-2013 (5 acte, 7) si L-344-1994 (5 acte, 6), primele trei dupa (acte, mentiuni). HTML luat
    # din browserul integrat prin ruta window.name + receptor local (vezi valul 11).
    #
    # L-509-1995 (Legea drumurilor, republicata): 155845@2026-08-13 (LP161 din 30.07.26), prima din
    # lista si randul de cautare; fara versiuni viitoare.
    #
    # L-50-2013 (controalele oficiale privind hrana pentru animale si alimentele): in vigoare 152645
    # @2025-12-31 (LP330/2025). Lista are DEASUPRA 143175@2028-05-08, al carei antet spune "Abrogata
    # prin LP82 din 12.04.24 ... in vigoare 08.05.28" - abrogarea programata de L-82-2024 (detinuta),
    # dar versiunea a fost pregatita in 2024, deci nu cuprinde LP330/2025. Merge in viitor/.
    #
    # L-344-1994 (statutul juridic special al Gagauziei): 155592@2026-07-09, antetul spune "MODIFICAT
    # HCC8 din 09.07.26, MO351-354/31.07.26" - o hotarire a Curtii Constitutionale de acum doua luni.
    'L-509-1995': {'doc_id': '155845',
                   'title': 'Legea nr. 509/1995 a drumurilor'},
    'L-50-2013': {'doc_id': '152645',
                  'title': 'Legea nr. 50/2013 cu privire la controalele oficiale pentru '
                           'verificarea conformitatii cu legislatia privind hrana pentru animale '
                           'si alimentele (abrogare programata prin L-82-2024 la 08.05.2028)'},
    'L-50-2013--2028-05-08': {'doc_id': '143175', 'subdir': 'viitor', 'future_of': 'L-50-2013',
        'applies_from': '2028-05-08',
        'title': 'Versiune viitoare, de la 2028-05-08 (abrogata prin L-82-2024), a actului L-50-2013'},
    'L-344-1994': {'doc_id': '155592',
                   'title': 'Legea nr. 344/1994 privind statutul juridic special al Gagauziei '
                            '(Gagauz-Yeri)'},
    # 2026-09-30, valurile 14 si 15 ale cozii de ingerare a grafului de citare (regenerat dupa
    # valul 13). Valul 14: L-1538-1998 (5 acte citatoare), L-25-2016 (5), L-108-2020 (4, 14
    # mentiuni). Valul 15: L-414-2006 (4, 11), L-575-2003 (4, 9), L-86-2020 (4, 8). HTML luat din
    # browserul integrat prin ruta window.name + receptor local (vezi valul 11).
    #
    # L-1538-1998 (fondul ariilor naturale protejate de stat): in vigoare 154107@2026-04-25 (LP53);
    # lista are deasupra 154487@2027-05-21 (LP71 din 30.04.26, "in vigoare 21.05.27"), viitoare,
    # merge in viitor/.
    # L-25-2016 (masurile restrictive internationale, republicata): 149779@2025-07-23 (LP244/2025).
    # L-108-2020 (pericolele de accidente majore, transpune Directiva 2012/18/UE): 150493@2025-09-12.
    # L-86-2020 (organizatiile necomerciale): 129338@2021-12-31, peste 2 ani in urma.
    #
    # L-414-2006 (RCA auto, legea veche) si L-575-2003 (garantarea depozitelor, legea veche) sint
    # ABROGATE cu succesor deja detinut: L-414-2006 prin LP106 din 21.04.22, in vigoare 01.04.23
    # (succesorul L-106-2022, art. 58? alin. (4) il abroga; citit), L-575-2003 prin LP160 din 22.06.23,
    # in vigoare 01.10.23 (succesorul L-160-2023, detinut). Pentru L-414-2006 lista de versiuni are
    # 123208@2023-07-01 DEASUPRA celei a abrogarii, 132393@2023-04-01; antetul lui 123208 e "MODIFICAT
    # LP178 din 11.09.20 ... in vigoare 01.07.23" (proiectie pregatita in 2020 pentru transferul de
    # supraveghere, anterioara abrogarii). S-a retinut 132393, cea a abrogarii si randul de cautare;
    # 123208 NU e ingerata. RECONCILIAT 2026-09-30: 123208 a fost descarcata si comparata pe cuvinte cu 132393 -
    # text identic, doar antetul si un marcaj LP178; la L-407-2006 (valul 6) alegerea cu data mai noua a fost
    # corectata la fel (vezi intrarea L-407-2006).
    'L-1538-1998': {'doc_id': '154107',
                    'title': 'Legea nr. 1538/1998 privind fondul ariilor naturale protejate de stat'},
    'L-1538-1998--2027-05-21': {'doc_id': '154487', 'subdir': 'viitor', 'future_of': 'L-1538-1998',
        'applies_from': '2027-05-21',
        'title': 'Versiune viitoare, de la 2027-05-21, a actului L-1538-1998'},
    'L-25-2016': {'doc_id': '149779',
                  'title': 'Legea nr. 25/2016 privind aplicarea masurilor restrictive '
                           'internationale'},
    'L-108-2020': {'doc_id': '150493',
                   'title': 'Legea nr. 108/2020 privind controlul pericolelor de accidente majore '
                            'care implica substante periculoase'},
    'L-414-2006': {'doc_id': '132393',
                   'title': 'Legea nr. 414/2006 cu privire la asigurarea obligatorie de '
                            'raspundere civila pentru pagube produse de autovehicule (ABROGATA '
                            'de la 01.04.2023 prin L-106-2022)'},
    'L-575-2003': {'doc_id': '137950',
                   'title': 'Legea nr. 575/2003 privind garantarea depozitelor in sistemul '
                            'bancar (ABROGATA de la 01.10.2023 prin L-160-2023)'},
    'L-86-2020': {'doc_id': '129338',
                  'title': 'Legea nr. 86/2020 cu privire la organizatiile necomerciale'},
    # 2026-09-30, valurile 16-19 ale cozii de ingerare (acte cu 4 acte citatoare; ultimele doua
    # cu 3). HTML prin ruta window.name. Versiuni alese (data de azi 2026-09-30):
    # L-354-2004 150483@2025-09-12; L-91-2014 131707@2022-12-10 (ABROGATA, succesor L-124-2022);
    # COD-1149-2000 136393@2024-01-01 (ABROGAT prin COD-95-2021; 140250@2023-11-22 e versiunea
    # dinaintea abrogarii, neingerata); L-59-2012 147975@2025-06-19 (156609@2027-03-29 in viitor/);
    # L-57-2006 155840@2026-08-13; L-60-2012 151196@2026-03-18 (randul de cautare era 151443,
    # mai veche); L-182-2010 152855@2026-02-02; L-880-1992 152590@2025-12-31; L-420-2006
    # 136384@2023-03-24; L-422-2006 150672@2026-03-11 (ABROGATA prin LP196/2025; randul de cautare
    # 152600 e textul dinaintea abrogarii); L-282-2023 150495@2025-09-12; L-139-2018
    # 148767@2025-06-03 (155448@2027-01-01 in viitor/).
    'L-354-2004': {'doc_id': '150483',
                   'title': 'Legea nr. 354/2004 cu privire la formarea bunurilor imobile'},
    'L-91-2014': {'doc_id': '131707',
                  'title': 'Legea nr. 91/2014 privind semnatura electronica si documentul '
                           'electronic (ABROGATA prin L-124-2022)'},
    'COD-1149-2000': {'doc_id': '136393',
                      'title': 'Codul vamal nr. 1149/2000 (ABROGAT de la 01.01.2024 prin '
                               'COD-95-2021)'},
    'L-59-2012': {'doc_id': '147975',
                  'title': 'Legea nr. 59/2012 privind activitatea speciala de investigatii'},
    'L-59-2012--2027-03-29': {'doc_id': '156609', 'subdir': 'viitor', 'future_of': 'L-59-2012',
        'applies_from': '2027-03-29',
        'title': 'Versiune viitoare, de la 2027-03-29 (LP209/2026), a actului L-59-2012'},
    'L-57-2006': {'doc_id': '155840',
                  'title': 'Legea nr. 57/2006 viei si vinului'},
    'L-60-2012': {'doc_id': '151196',
                  'title': 'Legea nr. 60/2012 privind incluziunea sociala a persoanelor cu '
                           'dizabilitati'},
    'L-182-2010': {'doc_id': '152855',
                   'title': 'Legea nr. 182/2010 cu privire la parcurile industriale'},
    'L-880-1992': {'doc_id': '152590',
                   'title': 'Legea nr. 880/1992 privind Fondul Arhivistic al Republicii Moldova'},
    'L-420-2006': {'doc_id': '136384',
                   'title': 'Legea nr. 420/2006 privind activitatea de reglementare tehnica'},
    'L-422-2006': {'doc_id': '150672',
                   'title': 'Legea nr. 422/2006 privind securitatea generala a produselor '
                            '(ABROGATA de la 11.03.2026 prin LP196/2025)'},
    'L-282-2023': {'doc_id': '150495',
                   'title': 'Legea nr. 282/2023 privind performanta energetica a cladirilor'},
    'L-139-2018': {'doc_id': '148767',
                   'title': 'Legea nr. 139/2018 cu privire la eficienta energetica'},
    'L-139-2018--2027-01-01': {'doc_id': '155448', 'subdir': 'viitor', 'future_of': 'L-139-2018',
        'applies_from': '2027-01-01',
        'title': 'Versiune viitoare, de la 2027-01-01 (LP76/2026), a actului L-139-2018'},
    # 2026-10-01, valurile 20-23 ale cozii de ingerare. Versiuni alese (azi 2026-10-01):
    # L-75-2015 154329@2026-05-09 (154330@2026-11-10, LP58/2026, in viitor/); L-7-2016 139008@2024-07-27
    # (ABROGATA prin LP162/2023, succesor L-162-2023); L-1308-1997 148859@2025-05-16; L-1380-1997
    # 138614@2024-01-01 (ABROGATA prin COD-95-2021; randul de cautare 139314 era 2023-01-01, mai veche);
    # L-241-2022 145809@2024-11-20; L-1453-2002 112687@2019-03-01 (succesor L-246-2018, text redus);
    # L-94-2007 154113@2026-04-25; L-199-1998 126102@2015-03-14 (ABROGATA prin LP171/2012 = L-171-2012);
    # L-129-2019 148053@2025-09-27 (155876@2026-11-13, LP168/2026, in viitor/); L-196-2025 150669@2026-03-11;
    # L-186-2008 151092@2026-01-01; L-271-2008 155885@2026-09-13.
    'L-75-2015': {'doc_id': '154329', 'title': 'Legea nr. 75/2015 cu privire la locuinte'},
    'L-75-2015--2026-11-10': {'doc_id': '154330', 'subdir': 'viitor', 'future_of': 'L-75-2015',
        'applies_from': '2026-11-10',
        'title': 'Versiune viitoare, de la 2026-11-10 (LP58/2026), a actului L-75-2015'},
    'L-7-2016': {'doc_id': '139008',
                 'title': 'Legea nr. 7/2016 privind supravegherea pietei in ceea ce priveste '
                          'comercializarea produselor nealimentare (ABROGATA de la 27.07.2024 prin '
                          'L-162-2023)'},
    'L-1308-1997': {'doc_id': '148859',
                    'title': 'Legea nr. 1308/1997 privind pretul normativ si modul de vinzare-'
                             'cumparare a pamintului'},
    'L-1380-1997': {'doc_id': '138614',
                    'title': 'Legea nr. 1380/1997 cu privire la tariful vamal (ABROGATA de la '
                             '01.01.2024 prin COD-95-2021)'},
    'L-241-2022': {'doc_id': '145809',
                   'title': 'Legea nr. 241/2022 privind Fondul de reducere a vulnerabilitatii '
                            'energetice'},
    'L-1453-2002': {'doc_id': '112687', 'title': 'Legea nr. 1453/2002 cu privire la notariat'},
    'L-94-2007': {'doc_id': '154113', 'title': 'Legea nr. 94/2007 cu privire la reteaua ecologica'},
    'L-199-1998': {'doc_id': '126102',
                   'title': 'Legea nr. 199/1998 cu privire la piata valorilor mobiliare (ABROGATA '
                            'de la 14.03.2015 prin L-171-2012)'},
    'L-129-2019': {'doc_id': '148053',
                   'title': 'Legea nr. 129/2019 privind subprodusele de origine animala si '
                            'produsele derivate care nu sunt destinate consumului uman'},
    'L-129-2019--2026-11-13': {'doc_id': '155876', 'subdir': 'viitor', 'future_of': 'L-129-2019',
        'applies_from': '2026-11-13',
        'title': 'Versiune viitoare, de la 2026-11-13 (LP168/2026), a actului L-129-2019'},
    'L-196-2025': {'doc_id': '150669', 'title': 'Legea nr. 196/2025 privind siguranta generala a produselor'},
    'L-186-2008': {'doc_id': '151092', 'title': 'Legea nr. 186/2008 securitatii si sanatatii in munca'},
    'L-271-2008': {'doc_id': '155885',
                   'title': 'Legea nr. 271/2008 privind verificarea titularilor si a candidatilor '
                            'la functii publice'},
    # 2026-10-01, valurile 24-27 ale cozii de ingerare. Versiuni alese (azi 2026-10-01):
    # L-107-2025 154135@2026-05-30; L-140-2001 151091@2025-12-31; L-1402-2002 148229@2025-04-22;
    # L-1409-1997 149996@2025-08-17 (ABROGATA prin LP153/2025, succesor nedetinut); L-161-2011
    # 106479@2017-10-27 (ultima din lista); L-142-2008 110170@2019-03-01 (ABROGATA prin L-133-2018);
    # L-163-2010 141610@2025-01-30 (ABROGATA prin COD-434-2023; randul de cautare 144639 era
    # 2024-09-01, text dinaintea abrogarii); HG-1123-2010 145413@2024-11-15 (ABROGATA prin HG678/2024,
    # nedetinuta); COD-828-1991 142259@2025-03-07 (Codul funciar vechi, golit de COD-22-2024);
    # L-160-2017 139802@2023-11-25; L-75-2020 155867@2026-08-13; L-77-2016 143443@2024-05-31.
    'L-107-2025': {'doc_id': '154135',
                   'title': 'Legea nr. 107/2025 privind raspunderea de mediu in legatura cu '
                            'prevenirea si repararea daunelor aduse mediului'},
    'L-140-2001': {'doc_id': '151091',
                   'title': 'Legea nr. 140/2001 privind Inspectoratul de Stat al Muncii'},
    'L-1402-2002': {'doc_id': '148229',
                    'title': 'Legea nr. 1402/2002 a serviciilor publice de gospodarie comunala'},
    'L-1409-1997': {'doc_id': '149996',
                    'title': 'Legea nr. 1409/1997 cu privire la medicamente (ABROGATA de la '
                             '17.08.2025 prin LP153/2025)'},
    'L-161-2011': {'doc_id': '106479',
                   'title': 'Legea nr. 161/2011 privind implementarea ghiseului unic in '
                            'desfasurarea activitatii de intreprinzator'},
    'L-142-2008': {'doc_id': '110170',
                   'title': 'Legea nr. 142/2008 cu privire la ipoteca (ABROGATA de la 01.03.2019 '
                            'prin L-133-2018)'},
    'L-163-2010': {'doc_id': '141610',
                   'title': 'Legea nr. 163/2010 privind autorizarea executarii lucrarilor de '
                            'constructie (ABROGATA de la 30.01.2025 prin COD-434-2023)'},
    'HG-1123-2010': {'doc_id': '145413',
                     'title': 'Hotarirea Guvernului nr. 1123/2010 privind aprobarea Cerintelor fata '
                              'de asigurarea securitatii datelor cu caracter personal la prelucrarea '
                              'lor in cadrul sistemelor informationale (ABROGATA de la 15.11.2024 '
                              'prin HG678/2024)'},
    'COD-828-1991': {'doc_id': '142259',
                     'title': 'Codul funciar nr. 828/1991 (golit; inlocuit prin COD-22-2024)'},
    'L-160-2017': {'doc_id': '139802', 'title': 'Legea nr. 160/2017 cu privire la biblioteci'},
    'L-75-2020': {'doc_id': '155867',
                  'title': 'Legea nr. 75/2020 privind procedura de constatare a incalcarilor in '
                           'domeniul prevenirii si combaterii spalarii banilor si finantarii '
                           'terorismului'},
    'L-77-2016': {'doc_id': '143443',
                  'title': 'Legea nr. 77/2016 cu privire la parcurile pentru tehnologia '
                           'informatiei'},
    # 2026-10-01, valurile 28-31 ale cozii de ingerare (azi 2026-10-01). Versiuni alese:
    # L-234-2021 151446@2025-09-20 (152999@2027-01-01, LP327/2025, in viitor/); L-320-2012
    # 155889@2026-09-13 (154180@2026-10-31 LP52/2026 si 156610@2027-03-29 LP209/2026 in viitor/);
    # L-66-2008 143289@2024-06-17 (155257@2027-04-02 = ABROGATA prin LP107/2026 din 02.04.2027, in
    # viitor/); HG-411-2022 133366@2023-09-16; L-1227-1997 130907@2023-01-08 (ABROGATA prin
    # L-62-2022); L-17-2007 26030@2012-04-14 (ABROGATA prin L-133-2011, ea insasi abrogata prin
    # L-195-2024); L-218-2010 150484@2025-09-12; L-467-2003 142789@2025-01-01; L-489-1999
    # 152954@2026-07-01 (152737@2027-01-01 LP327/2025 in viitor/; 155453@2030-01-01 e o consolidare
    # conditionata de aderarea la UE, neingerata); L-81-2004 137659@2023-09-23; L-153-2025
    # 155340@2026-08-14 (succesorul lui L-1409-1997); L-835-1996 141609@2025-01-30 (ABROGATA prin
    # COD-434-2023).
    'L-234-2021': {'doc_id': '151446', 'title': 'Legea nr. 234/2021 cu privire la serviciile publice'},
    'L-234-2021--2027-01-01': {'doc_id': '152999', 'subdir': 'viitor', 'future_of': 'L-234-2021',
        'applies_from': '2027-01-01',
        'title': 'Versiune viitoare, de la 2027-01-01 (LP327/2025), a actului L-234-2021'},
    'L-320-2012': {'doc_id': '155889',
                   'title': 'Legea nr. 320/2012 cu privire la activitatea Politiei si statutul '
                            'politistului'},
    'L-320-2012--2026-10-31': {'doc_id': '154180', 'subdir': 'viitor', 'future_of': 'L-320-2012',
        'applies_from': '2026-10-31',
        'title': 'Versiune viitoare, de la 2026-10-31 (LP52/2026), a actului L-320-2012'},
    'L-320-2012--2027-03-29': {'doc_id': '156610', 'subdir': 'viitor', 'future_of': 'L-320-2012',
        'applies_from': '2027-03-29',
        'title': 'Versiune viitoare, de la 2027-03-29 (LP209/2026), a actului L-320-2012'},
    'L-66-2008': {'doc_id': '143289',
                  'title': 'Legea nr. 66/2008 privind protectia indicatiilor geografice, denumirilor '
                           'de origine si specialitatilor traditionale garantate'},
    'L-66-2008--2027-04-02': {'doc_id': '155257', 'subdir': 'viitor', 'future_of': 'L-66-2008',
        'applies_from': '2027-04-02',
        'title': 'Versiune viitoare, de la 2027-04-02 (abrogata prin LP107/2026), a actului L-66-2008'},
    'HG-411-2022': {'doc_id': '133366',
                    'title': 'Hotarirea Guvernului nr. 411/2022 pentru aprobarea Regulamentului '
                             'privind transferurile de deseuri'},
    'L-1227-1997': {'doc_id': '130907',
                    'title': 'Legea nr. 1227/1997 cu privire la publicitate (ABROGATA de la '
                             '08.01.2023 prin L-62-2022)'},
    'L-17-2007': {'doc_id': '26030',
                  'title': 'Legea nr. 17/2007 cu privire la protectia datelor cu caracter personal '
                           '(ABROGATA de la 14.04.2012 prin L-133-2011)'},
    'L-218-2010': {'doc_id': '150484',
                   'title': 'Legea nr. 218/2010 privind protejarea patrimoniului arheologic'},
    'L-467-2003': {'doc_id': '142789',
                   'title': 'Legea nr. 467/2003 cu privire la informatizare si la resursele '
                            'informationale de stat'},
    'L-489-1999': {'doc_id': '152954',
                   'title': 'Legea nr. 489/1999 privind sistemul public de asigurari sociale'},
    'L-489-1999--2027-01-01': {'doc_id': '152737', 'subdir': 'viitor', 'future_of': 'L-489-1999',
        'applies_from': '2027-01-01',
        'title': 'Versiune viitoare, de la 2027-01-01 (LP327/2025), a actului L-489-1999'},
    'L-81-2004': {'doc_id': '137659',
                  'title': 'Legea nr. 81/2004 cu privire la investitiile in activitatea de '
                           'intreprinzator'},
    'L-153-2025': {'doc_id': '155340', 'title': 'Legea nr. 153/2025 cu privire la medicamente'},
    'L-835-1996': {'doc_id': '141609',
                   'title': 'Legea nr. 835/1996 privind principiile urbanismului si amenajarii '
                            'teritoriului (ABROGATA de la 30.01.2025 prin COD-434-2023)'},
    # 2026-10-01, valurile 32-35 ale cozii de ingerare (azi 2026-10-01). Versiuni alese:
    # L-107-2026 155256@2027-04-02 (lege noua, intra in vigoare la 02.04.2027, singura versiune: fisierul
    # principal ramine o versiune viitoare, ca L-325-2025; succesorul lui L-66-2008); L-1530-1993
    # 137389@2023-06-08; L-200-2010 154717@2026-06-04 (156316@2026-12-09 LP166/2026 si 154738@2027-06-01,
    # ABROGATA prin LP66/2026, in viitor/); HG-589-2017 151912@2026-02-05; HG-99-2018 144984@2024-09-06;
    # HG-483-2019 140056@2023-12-21; L-847-2002 155181@2026-06-30; L-294-2007 148792@2026-01-01 (randul
    # de cautare era 148968@2025-06-14, mai veche); L-20-2016 151254@2026-02-28; L-1353-2000
    # 146019@2024-11-29; L-299-2022 143912@2024-08-02; L-161-2014 152636@2025-12-31.
    'L-107-2026': {'doc_id': '155256',
                   'title': 'Legea nr. 107/2026 privind indicatiile geografice, specialitatile '
                            'traditionale garantate si mentiunile facultative de calitate'},
    'L-1530-1993': {'doc_id': '137389',
                    'title': 'Legea nr. 1530/1993 privind ocrotirea monumentelor'},
    'L-200-2010': {'doc_id': '154717',
                   'title': 'Legea nr. 200/2010 privind regimul strainilor in Republica Moldova'},
    'L-200-2010--2026-12-09': {'doc_id': '156316', 'subdir': 'viitor', 'future_of': 'L-200-2010',
        'applies_from': '2026-12-09',
        'title': 'Versiune viitoare, de la 2026-12-09 (LP166/2026), a actului L-200-2010'},
    'L-200-2010--2027-06-01': {'doc_id': '154738', 'subdir': 'viitor', 'future_of': 'L-200-2010',
        'applies_from': '2027-06-01',
        'title': 'Versiune viitoare, de la 2027-06-01 (abrogata prin LP66/2026), a actului L-200-2010'},
    'HG-589-2017': {'doc_id': '151912',
                    'title': 'Hotarirea Guvernului nr. 589/2017 privind aprobarea Regulamentului '
                             'transporturilor rutiere de marfuri periculoase'},
    'HG-99-2018': {'doc_id': '144984',
                   'title': 'Hotarirea Guvernului nr. 99/2018 pentru aprobarea Listei deseurilor'},
    'HG-483-2019': {'doc_id': '140056',
                    'title': 'Hotarirea Guvernului nr. 483/2019 pentru aprobarea Regulamentului cu '
                             'privire la formarea si atestarea specialistilor (gaze fluorurate)'},
    'L-847-2002': {'doc_id': '155181', 'title': 'Legea nr. 847/2002 privind sistemul de salarizare'},
    'L-294-2007': {'doc_id': '148792', 'title': 'Legea nr. 294/2007 privind partidele politice'},
    'L-20-2016': {'doc_id': '151254', 'title': 'Legea nr. 20/2016 cu privire la standardizarea nationala'},
    'L-1353-2000': {'doc_id': '146019',
                    'title': 'Legea nr. 1353/2000 privind gospodariile taranesti (de fermier)'},
    'L-299-2022': {'doc_id': '143912',
                   'title': 'Legea nr. 299/2022 privind prevenirea pierderii si risipei de alimente'},
    'L-161-2014': {'doc_id': '152636',
                   'title': 'Legea nr. 161/2014 cu privire la administratorii autorizati'},
    # Valul 36 (2026-10-01). L-66-2026 are o singura versiune pe legis.md, 154713 @ 2027-06-01
    # (legea intra in vigoare la 01.06.2027 si abroga L-200-2010 atunci): fisierul principal ramine
    # o versiune viitoare, ca L-325-2025. L-392-1999: ultima consolidare de pe legis.md e din 2002
    # (64772 @ 2002-05-09), fisa fara data abrogarii.
    'L-66-2026': {'doc_id': '154713',
                  'title': 'Legea nr. 66/2026 privind admisia, sederea si supravegherea strainilor '
                           'in Republica Moldova'},
    'L-392-1999': {'doc_id': '64772',
                   'title': 'Legea nr. 392/1999 privind restructurarea intreprinderilor agricole '
                            'in procesul de privatizare'},
    'L-163-2007': {'doc_id': '24012', 'anchor_mode': 'roman-amending',
                   'title': 'Legea nr. 163/2007 pentru modificarea si completarea Legii nr. 1134-XIII '
                            'din 2 aprilie 1997 privind societatile pe actiuni'},
    'L-237-2023': {'doc_id': '143874',
                   'title': 'Legea nr. 237/2023 privind productia ecologica si etichetarea '
                            'produselor ecologice'},
    'L-263-2005': {'doc_id': '140341',
                   'title': 'Legea nr. 263/2005 cu privire la drepturile si responsabilitatile pacientului'},
    'L-270-2008': {'doc_id': '146838',
                   'title': 'Legea nr. 270/2008 privind azilul in Republica Moldova'},
    # Valurile 36-39 (2026-10-01), a doua parte. COD-navigatiei-maritime-comerciale nu e act lipsa: este
    # L-599-1999, deja detinut (graful nu rezolva aliasul). Versiuni alese (toate in vigoare azi):
    # HG-1076-2010 144084@2024-07-11; L-755-2001 132359@2024-07-15 (abrogata prin LP152/2022);
    # L-289-2004 151180@2026-01-01; L-125-2007 136326@2023-03-24; L-1384-2002 150106@2025-08-23;
    # L-128-2014 139644@2024-04-27 (abrogata); L-851-1996 133763@2023-10-21 (abrogata); L-173-1994
    # 152531@2026-01-31; L-61-2007 107388@2019-01-01; L-209-2018 132669@2022-07-01; L-1216-1992
    # 138541@2024-01-01 (abrogata).
    'HG-1076-2010': {'doc_id': '144084',
                     'title': 'Hotarirea Guvernului nr. 1076/2010 cu privire la clasificarea situatiilor '
                              'exceptionale si la modul de acumulare si prezentare a informatiei'},
    'L-755-2001': {'doc_id': '132359', 'title': 'Legea nr. 755/2001 privind securitatea biologica'},
    'L-289-2004': {'doc_id': '151180',
                   'title': 'Legea nr. 289/2004 privind indemnizatiile pentru incapacitate temporara de '
                            'munca si alte prestatii de asigurari sociale'},
    'L-125-2007': {'doc_id': '136326',
                   'title': 'Legea nr. 125/2007 privind libertatea de constiinta, de gindire si de religie'},
    'L-1384-2002': {'doc_id': '150106',
                    'title': 'Legea nr. 1384/2002 cu privire la rechizitiile de bunuri si prestarile de '
                             'servicii in interes public'},
    'L-128-2014': {'doc_id': '139644', 'title': 'Legea nr. 128/2014 privind performanta energetica a cladirilor'},
    'L-851-1996': {'doc_id': '133763', 'title': 'Legea nr. 851/1996 privind expertiza ecologica'},
    'L-173-1994': {'doc_id': '152531',
                   'title': 'Legea nr. 173/1994 privind modul de publicare si intrare in vigoare a actelor oficiale'},
    'L-61-2007': {'doc_id': '107388', 'title': 'Legea nr. 61/2007 privind activitatea de audit'},
    'L-209-2018': {'doc_id': '132669',
                   'title': 'Legea nr. 209/2018 cu privire la Comitetul National de Stabilitate Financiara'},
    'L-1216-1992': {'doc_id': '138541', 'title': 'Legea nr. 1216/1992 privind taxa de stat'},
    # Valurile 36-39, restul cozii (2026-10-01): LP226/2022 (lege modificatoare cu articole romane, abroga
    # L-851-1996 si a republicat L-86-2014) 133703@2023-10-21; HG 678/2024 145409@2024-11-15 (a abrogat
    # HG-1123-2010; omnibus "facilitarea activitatii mediului de afaceri VI").
    'L-226-2022': {'doc_id': '133703', 'anchor_mode': 'roman-amending',
                   'title': 'Legea nr. 226/2022 privind modificarea unor acte normative'},
    'HG-678-2024': {'doc_id': '145409',
                    'title': 'Hotarirea Guvernului nr. 678/2024 cu privire la modificarea si abrogarea unor '
                             'hotarari ale Guvernului (facilitarea activitatii mediului de afaceri VI)'},
}

# (?<!\d) evita o capcana gasita 2026-09-16 la L-23-2008: fara ea, textul
# "MO338-341/30.09.16" produce un al doilea "candidat de data" fals, "41/30.09" (citit din
# coada lui "341"), care norm_year() il transforma in anul 2009. Cind linia contine "vigoare"
# si data buna sta la INCEPUTUL ei ("Versiune in vigoare din data 30.09.16 in baza ... MO338-
# 341/30.09.16 art.698"), all_dates() ia ultimul element din lista, iar candidatul fals ajunge
# ultimul: consolidation_date iesea "2009-30-41", o data invalida care ar fi trecut drept
# "consolidare viitoare" (2009 < TODAY, deci de fapt ar fi trecut drept veche, nu viitoare -
# tot gresit). Lookbehind-ul respinge orice inceput de potrivire precedat direct de o cifra,
# ceea ce exclude exact acest tipar fara sa afecteze nicio data reala din corpus.
DATE_RE = re.compile(r'(?<!\d)(\d{1,2})[.\-/](\d{1,2})[.\-/](\d{2,4})')


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


# Articolele proprii ale unei legi de modificare din vechea scoala de redactare: numeral roman,
# punct, linie de dialog. Nu se confunda cu ART_ABBR_NUM_RE (cifre) folosit pentru L-1125-2002.
ART_ROMAN_RE = re.compile(r'^Art\.\s*([IVXLCDM]+)\.\s*[-–—]')


def extract_doc(data, anchor_mode=None):
    """anchor_mode='roman-amending': ancoreaza NUMAI articolele romane proprii ale actului.

    Adaugat 2026-09-18, la ingerarea L-133-2018. O lege de modificare reproduce in corpul ei
    textul nou al actelor pe care le modifica, cu titlurile lor de articol, de capitol si de
    sectiune. Regulile implicite de ancorare le-ar lua pe toate drept structura proprie: la
    L-133-2018 asta inseamna 1434 de ancore "## Articolul N" care apartin Codului civil, CPC-ului
    si legii insolvabilitatii, nu acestei legi. O ancora spune "aici incepe dispozitia X a actului
    Y"; pusa pe text citat, minte de doua ori - despre autor si despre ce se poate cita de acolo.
    De aceea in acest mod se suprima TOATE celelalte ramuri de ancorare, nu doar cea de articol.

    Ancora nu rescrie linia sursa, ci se insereaza ca linie noua deasupra ei, in forma
    "## Articolul <ROMAN>." - conventia deja prezenta in corpus la L-177-2025 si L-178-2020,
    si singura forma pe care o recunosc ROMAN_RE din build_coverage.py si ANCHOR_RE din
    build_citation_graph.py. Linia originala "Art. I. - ..." ramine intacta dedesubt, deci
    proba prin stergerea liniilor "## " reface corpul octet cu octet.
    """
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
        if anchor_mode == 'roman-amending':
            m = ART_ROMAN_RE.match(l)
            if m:
                md_lines += ['', f"## Articolul {m.group(1)}.", l]
            else:
                md_lines.append(l)
            continue
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
        elif re.match(r'^Art\.\s*\d+(\^\d+)?\.\s*[-–—]', l):
            # Forma veche "Art.N. - text" / "Art. N. – text", gasita 2026-09-16 la
            # L-1125-2002: legea a fost republicata in 2019, dar spre deosebire de codurile
            # ingerate pina acum, legis.md nu i-a normalizat titlurile de articol la forma
            # moderna "Articolul N.". Fara aceasta ramura, cele 50 de articole raman text simplu,
            # fara nicio ancora: article_count iese 0 desi actul e complet si fara lacune. Cerinta
            # dublei puncte-liniuta ("N." urmat de un dash) exclude o trimitere de forma "art. 22"
            # aparuta in mijlocul unei fraze, care nu ar avea acel tipar exact la inceput de linie.
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
                              if re.match(r'^## (Articolul\s+|Art\.\s*\d)', l, flags=re.I)]),
        'char_count': len(content.text_content()),
    }


REPEAL_RE = re.compile(r'^Abrogat[ăaǎ]?\s+prin\s+(.+)$', re.I)


def repeal_of(parsed):
    """Actul abrogat: ce spune corpul textului, si ce spune fisa.

    De ce exista, 2026-09-10, la ingerarea L-133-2011. Pina aici scriptul nu avea nicio notiune
    de act abrogat. Un act mort intra in raw/ cu o consolidare recenta si trecuta, deci blocul de
    acoperire il arata drept `clean` si nimic nu spune ca a incetat sa lege. Este exact clasa de
    eroare pe care wiki-ul o previne pentru consolidarile viitoare, cu semnul opus: acolo textul
    nu se aplica INCA, aici nu se mai aplica.

    Doua surse, si NU sint de acord intre ele. Corpul consolidarii poarta, in antet, in locul
    rindului `MODIFICAT`, forma `Abrogata prin LP195 din 25.07.24, MO367-369/23.08.24 art.574;
    in vigoare 23.08.26`. Fisa are un cimp propriu, `Data abrogarii`, si pentru L-133-2011 acel
    cimp este GOL, desi actul este abrogat de la 23.08.2026. Se citesc amindoua si se pastreaza
    amindoua, fiindca dezacordul lor este el insusi o constatare despre sursa.

    Data care conteaza este cea de intrare in vigoare a abrogarii (`in vigoare DD.MM.YY`), nu data
    actului abrogator: L-133-2011 a fost abrogata printr-o lege din 2024 cu efect din 2026.
    """
    line = next((l for l in parsed['lines'][:20] if REPEAL_RE.match(l.strip())), '')
    fisa = next((v for k, v in parsed['meta_pairs'] if 'abrog' in k.lower()), '').strip()
    if not line and fisa in ('', '-'):
        return None
    tail = REPEAL_RE.match(line.strip()).group(1) if line else ''
    dates = all_dates(tail)
    # `in vigoare DD.MM.YY` este ultima data din rind; daca lipseste, ramine data publicarii
    eff = dates[-1] if dates else (all_dates(fisa)[0] if all_dates(fisa) else None)
    by = re.split(r'\s*,\s*', tail)[0] if tail else ''
    return {'line': line.strip(), 'effective': eff, 'by': by,
            'fisa_field': fisa or '-', 'in_force_today': bool(eff and eff <= TODAY)}


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
    # In modul 'roman-amending' liniile "Articolul N^M" din corp sint titluri ale actului
    # MODIFICAT, reproduse aici. Cimpul `superscript_articles` declara exponentii articolelor
    # PROPRII ale fisierului; umplut cu ele ar spune, in frontmatter, ca L-133-2018 are un
    # articol 1575^4. Se lasa gol, iar numerele vechi ramin unde le este locul: in corpul
    # textului, care este tocmai ce face din acest fisier o concordanta.
    sup_arts = [] if spec.get('anchor_mode') == 'roman-amending' else sorted(
        {m for l in parsed['lines'] for m in re.findall(r'^Articolul (\d+\^\d+)', l)},
        key=lambda x: (int(x.split('^')[0]), int(x.split('^')[1])))
    pending = future_pending(parsed)
    repeal = repeal_of(parsed)
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
    # Abrogarea se scrie INAINTEA oricarui alt avertisment: un act abrogat nu se mai citeaza,
    # oricare ar fi starea consolidarii lui.
    if repeal:
        if repeal['in_force_today']:
            head = (f"> **ATENȚIE, ACT ABROGAT.** Textul de mai jos **nu mai este în vigoare**. "
                    f"Abrogarea produce efecte de la **{repeal['effective']}**, iar astăzi este "
                    f"{TODAY}. Fișierul se păstrează fiindcă alte acte din corpus încă trimit la "
                    f"el și fiindcă textul guvernează faptele anterioare acelei date. **Nu îl "
                    f"cita ca drept în vigoare.**")
        else:
            head = (f"> **ATENȚIE, ACT ABROGAT CU EFECT AMÂNAT.** Abrogarea produce efecte de la "
                    f"**{repeal['effective']}**, ulterioară zilei de {TODAY}, deci textul de mai "
                    f"jos se aplică încă, dar are termen. Verifică data înainte de a-l cita "
                    f"pentru fapte ulterioare.")
        warn = ['', head, '', f"> - **abrogat prin:** {repeal['by'] or 'n/a'}",
                f"> - **rândul din corpul actului:** `{repeal['line']}`",
                f"> - **câmpul „Data abrogării” din fișa legis.md:** `{repeal['fisa_field']}`"]
        if repeal['fisa_field'] == '-':
            warn.append("> - **cele două nu concordă:** corpul actului declară abrogarea, fișa "
                        "lasă câmpul gol. Un control care s-ar sprijini numai pe fișă ar rata "
                        "abrogarea. Constatare despre sursă, nu despre acest fișier.")
        warn.append('')
        body[-2:-2] = warn
    if spec.get('future_of'):
        body[-2:-2] = ['', f"> **ATENȚIE, VERSIUNE VIITOARE A ACTULUI {spec['future_of']}.** Textul de mai jos "
                           f"se aplică de la **{spec.get('applies_from') or parsed['consolidation_date']}**, nu "
                           f"astăzi ({TODAY}). Este ținut **separat** de textul în vigoare azi, care rămâne în "
                           f"`{spec['future_of']}.md`. Nu îl cita ca drept în vigoare; compară cu textul de azi "
                           f"înainte de a spune ce se schimbă.", '']
    whole_act_future = (not spec.get('future_of')) and (not pending) and parsed['consolidation_date'] > TODAY
    if whole_act_future:
        body[-2:-2] = ['', f"> **ATENȚIE, ACT NEINTRAT ÎN VIGOARE.** Consolidarea este datată "
                           f"**{parsed['consolidation_date']}**, ulterioară zilei de {TODAY}, "
                           f"și fișa nu conține niciun marcaj de dispoziție amânată: data este "
                           f"cea a intrării în vigoare a actului întreg. Nicio dispoziție de mai "
                           f"jos nu se aplică astăzi. Verificați articolul de dispoziții finale.", '']
    if pending and not spec.get('future_of'):
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
    if repeal:
        fm['repealed'] = True
        fm['repeal_effective'] = repeal['effective'] or ''
        fm['repealed_by'] = repeal['by']
        fm['repeal_line'] = repeal['line']
        fm['repeal_fisa_field'] = repeal['fisa_field']
        fm['repeal_in_force_today'] = repeal['in_force_today']
        fm['repeal_warning'] = (
            f"Act ABROGAT de la {repeal['effective']}; astazi este {TODAY}. Nu se citeaza ca "
            f"drept in vigoare." if repeal['in_force_today'] else
            f"Act abrogat cu efect de la {repeal['effective']}, inca in vigoare astazi, {TODAY}.")
    if spec.get('future_of'):
        fm['future_version_of'] = spec['future_of']
        fm['applies_from'] = spec.get('applies_from') or parsed['consolidation_date']
        # Data din lista de versiuni a legis.md are prioritate: cea dedusa din rindul de modificare
        # poate fi mai veche (L-19-2016 @ 2030, L-82-2024 @ 2028, L-22-2025 @ 2027 au iesit asa,
        # 2026-09-25), iar registrul in-force citeste `consolidation_date`.
        if fm['applies_from'] != fm['consolidation_date']:
            fm['consolidation_date_from_modification_line'] = fm['consolidation_date']
            fm['consolidation_date'] = fm['applies_from']
        fm['in_force_warning'] = (
            f"VERSIUNE VIITOARE a actului {spec['future_of']}, tinuta separat. Se aplica de la "
            f"{fm['applies_from']}, nu astazi ({TODAY}). Textul in vigoare azi este in "
            f"{spec['future_of']}.md; acest fisier nu se citeaza ca drept in vigoare.")
        fm['consolidation_is_future'] = True
    elif pending:
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
    targets = {k: v for k, v in DOCS.items() if (k in only) or (not only and not v.get('external_folder'))}
    if only and not targets:
        raise SystemExit(f"nimic de ingerat; alege dintre: {', '.join(DOCS)}")
    for stem, spec in targets.items():
        show_url, data, path = fetch(spec['doc_id'])
        resolved = resolve_superscripts(data)
        if not resolved or '<sup' in resolved:
            raise RuntimeError('resolve_superscripts nu a rezolvat exponentii')
        parsed = extract_doc(resolved, anchor_mode=spec.get('anchor_mode'))
        # Versiunile VIITOARE (2026-09-25) se scriu intr-un subfolder, ca sa nu intre in graful de
        # citare si in registrul HCC, care citesc doar folderul de sus, si ca textul in vigoare azi
        # din <act>.md sa ramina neatins. Registrul in-force citeste recursiv, deci le vede.
        out_dir = RAW_DIR / spec['subdir'] if spec.get('subdir') else RAW_DIR
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / f"{stem}.md").write_text(make_raw(stem, spec, parsed, show_url),
                                            encoding='utf-8', newline='\n')
        note = ''
        if spec.get('applies_from') and spec['applies_from'] != parsed['consolidation_date']:
            note = (f"  ATENTIE: data versiunii din lista legis.md ({spec['applies_from']}) difera de "
                    f"cea dedusa din rindul de modificare ({parsed['consolidation_date']})")
        print(f"{stem}: {parsed['article_count']} articole, "
              f"consolidat {parsed['consolidation_date']}, HTML {path.name}{note}")


if __name__ == '__main__':
    main()
