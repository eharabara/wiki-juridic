# Raport de execuție — planul de extindere a perimetrului de drept intern

Data: 6 septembrie 2026, seara
Plan executat: `_meta/plans/2026-09-06-plan-extindere-perimetru-domestic.md`
Stare: **pașii 1–4 executați integral, opt commit-uri locale, fără push.** Rescrie raportul parțial
din 20:30 (commit `bf57fd7`), scris când pașii 2–4 erau blocați de verificarea Cloudflare.

Condițiile prealabile (secțiunea 3) au trecut toate la început: arbore curat pe `main` la `d951aa6`,
validator 0 erori, acoperire la zi, documentele citite integral.

## 1. Sondajul de actualitate (pasul 2)

Raportul complet: `_meta/coverage/currency-sweep-2026-09-06.md` și `.json`. Metodă:
`/cautare/showdetails/<doc_id>` citit prin `fetch` same-origin din Chrome după ce Eugen a trecut
verificarea Cloudflare; istoricul versiunilor este lista `showDetails(null,'<id>')` cu data fiecărei
versiuni; pentru fiecare versiune mai nouă decât cea din wiki s-a citit rândul MODIFICAT. Nimic
reîmprospătat (D6).

| stare | acte |
|---|---:|
| curent | 37 |
| curent, consolidare viitoare | 11 |
| wiki în urmă | 3 |
| nerezolvat | 1 |
| abrogat pe legis.md | 1 |
| **total** | **53** |

Ce nu era știut: legis.md publică și consolidări cu dată viitoare, până în 2030 și una „la data
aderării la UE", deci „cea mai nouă versiune" nu este „versiunea în vigoare azi"; tabelul le dă pe
amândouă. Un act e „în urmă" numai dacă există o versiune mai nouă **cu dată deja trecută**.

Cele trei în urmă, fiecare o decizie separată:

| act | wiki | în vigoare azi | consolidări neaplicate |
|---|---|---|---|
| `COD-225-2003` | 152860 @ 2025-12-30 | 155718 @ 2026-08-06 | LP330/2025, LP187/2025, LP252/2025, LP126/2026 |
| `COD-1163-1997` | 155071 @ 2026-06-25 | 138613 @ 2026-07-01 | LP318/2025 (în vigoare 01.07.26); plus una viitoare 2027-01-01 |
| `L-202-2017` | 151445 @ 2025-09-20 | 151077 @ 2025-10-25 | LP189/2025 |

Două constatări care nu sunt reîmprospătări:

- `HG-1170-2016`: fișa legis.md dă **Data abrogării 07.03.2025**, data intrării în vigoare a
  HG553/2024. Wiki-ul îl ține ca act în vigoare. De verificat pe textul HG553/2024.
- `CC-1107-2002`: cazul „legis.md în urmă" s-a inversat; legis.md are LP251/2025 ca 150498 @
  2026-04-01 și o consolidare viitoare 149719 @ 2027-01-01 (LP76/2026). Frontmatter-ul nostru
  arată doc_id 150561, adică versiunea 2025-11-01; textul din PDF poartă LP251, dar identitatea
  cu 150498 nu e verificată.

Controlul „Publicat": cele două acte sărite de `build_coverage.py` (`L-177-2025`, `L-178-2020`) și
cele patru cu `never_amended: true` (`DCA-61-2024`, `HG-574-2024`, `L-160-2023`, `L-250-2017`) au
toate o singură versiune pe legis.md. Regula nu ascunde nicio modificare.

## 2. doc_id-urile găsite pentru cele 14 acte

Toate confirmate pe pagina actului (fișă și istoric de versiuni), nu din lista de rezultate.

| ID raw | act | doc_id ingerat | consolidare | observație |
|---|---|---:|---|---|
| `CONST-1994` | Constituția, republicată 13.11.2024 | **145723** | 2024-11-05 | 19 versiuni; consolidarea derivată din LP244/2024, versiunea legis.md e datată 13.11.2024 |
| `L-149-2012` | insolvabilității | **152605** | 2025-12-31 | HTML de 1 MB |
| `L-160-2011` | actele permisive | **156152** | **2029-01-01, viitoare** | două trepte în 2027 fără marcaje |
| `L-131-2012` | controlul de stat | **151146** | 2026-08-28 | lista de căutare trimitea la 152529 (2025-12-31), o versiune veche |
| `L-436-2006` | administrația publică locală | **155118** | 2026-06-26 | 76 de versiuni |
| `L-158-2008` | funcția publică | **155439** | **2026-09-13, viitoare** | 29 de dispoziții amânate (LP154/2026); încă una în 2028, neingerată |
| `L-148-2023` | accesul la informații | **137908** | 2024-01-08 | nemodificată |
| `L-131-2015` | achizițiile publice | **155117** | 2026-06-26 | **abrogată de la 01.01.2027**; succesoare Legea 325/2025 (152974) și Legea 20/2026 (153618), neingerate |
| `L-1260-2002` | avocatura | **146148** | 2025-01-07 | versiunea în vigoare azi; 153429 e consolidarea „la aderarea la UE", datată fictiv 2030-01-01 |
| `L-198-2007` | asistența juridică garantată | **155726** | 2026-08-06 | |
| `L-514-1995` | organizarea judecătorească | **156079** | 2026-08-28 | 56 de versiuni |
| `UA-STATUT-2011` | Statutul profesiei de avocat | **134919** | 2022-05-27 | 86850 din plan e consolidarea din 2012; pe articole, nu pe puncte |
| `UA-DEONTOLOGIC-AAAA` | Codul deontologic al avocaților | — | — | lacună D5 |
| `UA-STAGIU-AAAA` | Regulamentul stagiului | — | — | lacună D5 |

Prefixe noi consemnate în manifest: `CONST-` (secțiunea Q) și `UA-` (secțiunea T).

## 3. Ce nu s-a găsit pe legis.md (D5)

Codul deontologic al avocaților și Regulamentul privind efectuarea stagiului profesional. Șase
căutări în titlu, fără diacritice: „codul deontologic" (12), „avocatilor" (169), „avocat stagiar"
(4), „stagiului profesional" (3), „stagiului" (53), „statutul profesiei de avocat" (5). Niciun
rezultat al Uniunii Avocaților în afara Statutului și a celor patru acte de modificare ale lui.
Consemnate ca lacune în manifest T.3; nimic ingerat de pe uam.md; identificatorii rezervați nu
sunt folosiți. Statutul însuși poate conține regulile stagiului; nu a fost citit în acest scop.

## 4. Validatorul și tabelul de acoperire

Validator după ultimul commit: **0 erori, 2 avertismente** (aceleași două de la început,
`236__Prezentare_RI_mai_2025` și COM(2024) 469). Spec versiunea 2026-09-06, cu eticheta nouă
`unverified`. 107 pagini structurate, 394 de surse brute cu sha256 verificat.

| | înainte (09:49) | după (21:28) |
|---|---:|---:|
| acte primare moldovenești | 53 | **65** |
| extrase UE | 29 | 29 |
| documente BNM | 284 | 284 |
| acte cu consolidare viitoare | 11 | **13** (+ `L-158-2008`, `L-160-2011`) |
| acte cu consolidare veche | 8 | **10** (+ `UA-STATUT-2011`, `L-148-2023`) |
| pagini structurate | 95 | **107** |

Rânduri noi în tabel, toate cu numărul de ancore egal cu cel declarat: `CONST-1994` 157,
`L-149-2012` 271, `L-160-2011` 32, `L-131-2012` 41, `L-436-2006` 98, `L-158-2008` 88, `L-148-2023` 35,
`L-131-2015` 91, `L-1260-2002` 73, `L-198-2007` 54, `L-514-1995` 60, `UA-STATUT-2011` 74. Total
**1.174 de ancore noi**, integritate de text PASS la fiecare (`verify_business_law.py`, linii
scrise = linii de referință).

Pasul 1: 18 pagini (`concepts/acquis-*.md`, `comparisons/cnpf-transposition-matrix.md`) cu
`confidence: low`, eticheta `unverified`, `updated` la zi și paragraful unic sub H1; corpul neatins.

## 5. Anomalii

Numerotare:
- `L-514-1995`, lacune 29–34, 41–42, 51–53: abrogări la nivel de **capitol**, cu stub în text
  (`Capitolul 3 (art.29-34) - abrogat.` etc.), ancorate. Nu e defect, nu e `[de verificat]`.
- `CONST-1994`: 143 de bază fără lacune; arts. 82–83 ca stub `abrogat`; 8 articole romane I–VIII;
  **titlul articolului stă pe linia de după ancoră**, deci ancorele nu au titlu.
- O verificare prealabilă pe HTML cu etichetele scoase raportase lacune și duplicate în lotul A;
  erau exponenți neresolvați lipiți de număr (clasa `L-235-2006`). Ancorele scrise nu au lacune.

Consolidări viitoare:
- `L-158-2008` 2026-09-13, 29 de dispoziții amânate, toate în registrul in-force (39 de rânduri).
- `L-160-2011` 2029-01-01, **un singur marcaj** (anexa nr. 1) deși istoricul are trepte la
  2027-01-23 și 2027-05-21 ale căror marcaje s-au pierdut; registrul nu le vede. Și registrul
  etichetează acea dispoziție „art. 440", numărul din Monitorul Oficial al legii de modificare,
  nu „anexa nr. 1": defectul din întrebarea deschisă 7, acum și pe o lege, nu doar pe HG.
- Codificarea **2030-01-01 = „la data aderării la UE"** (`L-1260-2002`, `COD-218-2008`): registrul
  ar data greșit o asemenea dispoziție dacă ar fi ingerată.

Fișe contrazise de text: `CONST-1994` (fișa 19.08.1994, art. I: 27.08.1994); `L-131-2012` (fișa
31.01.2012, anterioară publicării din 31.08.2012, art. 33: 6 luni de la publicare); `L-160-2011`
(fișa 01.01.2012, art. 14: 6 luni de la publicare, cu excepții).

Absent fără marcaj: **nimic**. `CONST-1994` nu are niciun marcaj `[Art.N ...]` în text
(republicarea le-a eliminat; istoricul celor 17 modificări, inclusiv două HCC, e doar în fișă).

Metodă, corectată pe parcurs:
- `ingest_business_law.py`: un rând care începe cu „Titlul VII," (textul art. VIII din Constituție)
  nu mai e luat drept titlu de structură; regexul cere numeral roman, graniță de cuvânt, fără
  virgulă. Regresie verificată: nicio ancoră `## Titlul` existentă nu s-ar pierde.
- `build_coverage.py`: articolele romane fără punct (`## Articolul I`) sunt numărate; înainte
  raporta 149 în loc de 157 și o nepotrivire falsă.
- Ruta cu receptor HTTP local pentru HTML, pregătită ca să evit descărcările, a fost blocată de
  clasificatorul de permisiuni și abandonată; s-a folosit descărcarea blob din Chrome, cu acordul
  explicit al lui Eugen. Trei fișiere descărcate și nefolosite au rămas în `Downloads`:
  `showdetails-152529.html`, `-156075.html`, `-153429.html`.

Decizii rămase lui Eugen, în ordinea urgenței: statutul `HG-1170-2016`; reîmprospătarea celor trei
acte în urmă; ingerarea Legii 325/2025 și a Legii 20/2026 (achiziții); `CC-1107-2002` la 150498;
dacă `L-160-2011` se reingerează la versiunea în vigoare azi în loc de 2029.

## 6. Commit-uri

| commit | pas |
|---|---|
| `0056fea` | Pasul 1: înghețarea stratului de constatări acquis |
| `bf57fd7` | Raport parțial (blocaj Cloudflare), înlocuit de acesta |
| `8c0a31b` | Pasul 2: sondajul de actualitate |
| `036630b` | Pasul 3: Constituția, CONST-1994 |
| `0eef968` | Pasul 3, urmare: `build_coverage.py` numără articolele romane fără punct |
| `87514fb` | Pasul 4, lotul A |
| `f047adc` | Pasul 4, lotul B |
| `db3b453` | Pasul 4, lotul C |

Plus commit-ul acestui raport. Fără push. Copiile din `legal-career/` nu au fost atinse;
documentul 05 din proiect se actualizează după acest raport, cum spune secțiunea 5 a planului.
