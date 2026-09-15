# Plan pentru pasul 6: Acordul de Asociere, textele UE integrale, reverificarea constatărilor acquis

Data: 15 septembrie 2026
Folder vizat: `C:\Users\harab\wiki`
Stare: **executat integral, 2026-09-16.** Toți cei șase pași (6.1-6.6) sînt făcuți — vezi tabelul din
secțiunea 5. Cele 17 pagini `acquis-*` plus `cnpf-transposition-matrix` au ieșit din `unverified`;
`AA-2014` e ingerat; cele 5 verificări de consolidare UE (D5) sînt închise. Ce rămâne, consemnat ca
atare, nu ascuns: Reg. CRA 1060/2009, PRIIPs, vânzările în lipsă, indicii de referință și SFTR (fără
pagină `acquis-*` proprie), pragul minim MTPL (art. 9 din 2009/103 neextras integral), substanța
operațională AIFMD (nedistins dacă e delegată unor acte CNPF neingerate sau absentă), și RTS-urile
crowdfunding.

Precedent direct: `_meta/plans/2026-09-06-plan-extindere-perimetru-domestic.md`, D3: „(6) după
acestea, Acordul de Asociere, textele UE integrale și reverificarea constatărilor acquis" — ultimul
pas al planului din 6 septembrie, lăsat fără plan propriu până acum. Pasul 5 (HCC) e închis
(`_meta/plans/2026-09-08-plan-hcc-pasul-5.md`, executat 8-15 septembrie).

---

## 1. Ce s-a verificat la 15 septembrie înainte de a porni

- Arbore curat pe `main` la `1302e31`; `close_session.py --check` curat: toate cele patru registre
  generate la zi, validator 0 erori, 5 avertismente (stampila registrului dosarelor, cea mai veche).
- 18 pagini poartă înghețarea din 6 septembrie: `tags: [unverified]`, `confidence: low`, paragraful
  fix sub H1 (`log.md`, intrarea „Înghețarea stratului de constatări acquis"). 17 sunt
  `concepts/acquis-*.md`, a 18-a e `comparisons/cnpf-transposition-matrix.md`.
- Niciun text integral al Acordului de Asociere nu există în vault, în nicio formă. Căutare
  exhaustivă (`grep -rl` pe `raw/`, `entities/`, `concepts/`) — zero rezultate.

## 2. Recensământul: ce ține azi stratul de acquis UE

### 2.1 Cele 29 de extrase EUR-Lex (`raw/papers/cnpf/UE-*.md`)

Toate sunt **extrase structurate**, ingerate 2026-07-09: cuprinsul complet detectat (numărul de
articole al actului, de la 4 la 567) plus textul integral doar al „articolelor-cheie" alese atunci
(6-9 pe act, cele citate în paginile `concepts/`). Suma articolelor din cuprins pe cele 29 de acte:
**~2427**. Suma articolelor-cheie deja cu text integral: sub 150. Diferența e mărimea reală a
golului „extras, nu text integral" — nu 2427, pentru că marea majoritate a articolelor unei
directive (definiții tehnice, proceduri de comitologie, dispoziții tranzitorii ale unor state
membre) nu vor fi citate niciodată de o pagină despre transpunerea moldovenească.

**Verificare de actualitate CELEX, rulată azi** (`_meta/imports/cnpf/discover_latest_celex.py`,
citire, nimic scris): **5 din 29 au o consolidare mai nouă pe EUR-Lex decât cea ținută.**

| act ținut | consolidare ținută | consolidare disponibilă | notă |
|---|---|---|---|
| `UE-2009-138` (Solvency II) | `-20250117` | `-20270130` | **nou găsit azi**; de verificat dacă e cu dată viitoare (simetricul „consolidation dated in the future" domestic) sau deja aplicabilă |
| `UE-2024-1624` (AMLR) | act de bază, fără consolidare | `-20240619` | deja semnalat fals în manifest (secțiunea F, nota de sub tabelul F) |
| `UE-2024-1640` (AMLD6) | act de bază, fără consolidare | `-20240619` | idem |
| `UE-2020-1503` (crowdfunding) | act de bază, fără consolidare | `-20201020` | idem |
| `UE-97-9` (ICSD) | act de bază, fără consolidare | `-19970326` | idem |

Ultimele patru sînt deja documentate ca „fals pozitiv" în manifest (act de bază fără versiune
consolidată distinctă listată pe propria pagină EUR-Lex, dar existentă la căutare directă) — de
verificat o singură dată, nu patru. Primul, Solvency II, e o constatare nouă a acestei sesiuni.

### 2.2 Acordul de Asociere — găsit, verificat accesibil, dimensionat

CELEX-ul corect e **`22014A0830(01)`** (nu `22014A0630(01)`, care dă 404 — data din CELEX e a
publicării în Jurnalul Oficial, 30 august 2014, nu a semnării). Textul RO se ia direct prin `curl`,
fără nicio barieră Cloudflare-like: `GET https://eur-lex.europa.eu/legal-content/RO/TXT/?uri=CELEX:22014A0830(01)`
răspunde 200, ~11 MB, HTML structurat pe articole (`class="oj-ti-art"`) exact ca `showdetails` de pe
legis.md, dar fără sesiune, fără cookie, fără `Referer`. Există și `22014A0830(02)`, ~9,8 MB — verificat
azi: **acesta e schedulele tarifare de mărfuri** (nu conține „ANEXA XXVIII"), deci în afara
perimetrului CNPF/BNM al acestui vault. Nu există `(03)`.

**Descoperirea care contează:** documentul `(01)` conține **Anexa XXVIII-A, „Norme aplicabile
serviciilor financiare"** (liniile 64964-65087 din HTML-ul brut, ~120 de linii) — o listă de
~20-25 directive/regulamente UE pe care Republica Moldova **s-a angajat expres** să le transpună,
fiecare cu **propriul calendar legal** („trei ani de la data intrării în vigoare a prezentului
acord", „zece ani" pentru anumite dispoziții ale 2006/49/CE, „cinci ani" pentru 2003/41/CE
pensiile ocupaționale, etc.). Anexele XXVIII-B, C, D de lângă ea (telecomunicații, poștă,
transport maritim) sînt confirmate în afara perimetrului. Mecanismul intrării în vigoare/aplicării
provizorii e la art. 462-464 din același document, dar **data calendaristică efectivă nu e în
corpul acordului însuși** — e într-o decizie separată a Consiliului UE/o notificare OJ, de găsit
separat înainte de a calcula orice termen.

Asta transformă „reverificarea constatărilor acquis" dintr-o presupunere generică
(„Moldova ar trebui să transpună MiFID") într-un fapt juridic verificabil, cu dată: dacă un
instrument e în Anexa XXVIII-A, are termen legal; dacă nu e, angajamentul (dacă există) vine din
altă parte (foaia de parcurs de aderare la UE, planuri naționale) și trebuie spus așa, nu confundat
cu obligația din Acord.

### 2.2-bis Datele — rezolvat 2026-09-15 (pasul 6.2), **corectat același 2026-09-15**

Găsite în panoul propriu „Dates" al metadatelor EUR-Lex pentru `22014A0830(01)`
(`https://eur-lex.europa.eu/legal-content/RO/ALL/?uri=CELEX:22014A0830(01)`), fiecare cu propria
notificare oficială, citită integral, nu doar câmpul de metadate:

- **Aplicare cu titlu provizoriu: 1 septembrie 2014.** `CELEX 22014X0830(02)`, JO L 260, 30.8.2014,
  p. 1, în temeiul art. 3 alin. (1) din Decizia 2014/492/UE a Consiliului din 16.06.2014: „va fi
  aplicat cu titlu provizoriu, începând cu data de 1 septembrie 2014".
- **Intrare în vigoare: 1 iulie 2016.** `CELEX 22016X0618(03)`, JO L 161, 18.6.2016, în temeiul
  art. 464 alin. (2) al acordului însuși, „având în vedere faptul că ultimul instrument de
  ratificare sau aprobare a fost depus la data de 23 mai 2016".

**Corectare, aceeași zi, la trecerea la ingestie (pasul 6.3): prima concluzie despre care dată
guvernează Anexa XXVIII-A era greșită.** Citind art. 464 alin. (5) din acord — nu doar alin. (2),
citat de notificarea de intrare în vigoare — textul spune: „orice trimitere la «data de intrare
în vigoare a prezentului acord» care figurează în [dispozițiile relevante, inclusiv anexele]
se înțelege ca trimitere la «data de la care prezentul acord se aplică cu titlu provizoriu»" —
**dar numai pentru dispozițiile care chiar au fost aplicate cu titlu provizoriu**, listate exhaustiv
la art. 3 alin. (1) din Decizia 2014/492/UE a Consiliului (CELEX `32014D0492`, citită integral).
Acel articol include expres **litera (d): titlul IV capitolul 9** (Serviciile financiare — exact
capitolul care conține art. 61, clauza de apropiere ce trimite la Anexa XXVIII-A) și **litera (h):
anexele II-XIII și XV-XXXV** (interval care include Anexa XXVIII întreagă, cu toate cele patru
părți A-D). Consecință directă: **calendarul Anexei XXVIII-A curge de la 1 septembrie 2014, nu de
la 1 iulie 2016.** Tabelul din 2.2-ter (versiunea inițială) era calculat pe baza greșită și e
înlocuit mai jos.

### 2.2-ter Calendarul integral al Anexei XXVIII-A, calculat de la 1 septembrie 2014

Textul complet al anexei (liniile 64964-65087 din HTML-ul `22014A0830(01)`, citit integral, nu
eșantionat) listează **41 de instrumente**, nu „~20-25" cum estimase recensământul inițial din
secțiunea 2.2 pe o privire parțială. Fiecare rând de mai jos e termenul din anexă, calculat de la
**1 septembrie 2014** — data corectă, per corectarea din 2.2-bis, nu 1 iulie 2016. **Toate cele 41
de termene au expirat deja** — cel mai îndepărtat, zece ani, a căzut la 1 septembrie 2024, acum doi
ani.

| nr. | instrument | subiect | termen din text | scadent | `UE-*.md` corespunzător |
|---:|---|---|---|---|---|
| 1 | Dir. 2007/44/CE | evaluarea prudențială a achizițiilor de participații | trei ani | 2017-09-01 | — |
| 2 | Dir. 2002/87/CE | supravegherea suplimentară a conglomeratelor financiare | trei ani | 2017-09-01 | — |
| 3 | Dir. 2006/48/CE | inițierea/exercitarea activității instituțiilor de credit (CRD I) | trei ani | 2017-09-01 | — |
| 4 | Dir. 2007/18/CE | modifică 2006/48/CE (bănci de dezvoltare multilaterală) | imediat | 2014-09-01 | — |
| 5 | Dir. 2006/49/CE | rata de adecvare a capitalului (CAD) | trei ani (regula generală) | 2017-09-01 | — |
| 5bis | — idem, capitalul inițial al instituțiilor, altele decât cele de credit (art. 5, 6, 7, 8, 9) | zece ani | 2024-09-01 | — |
| 6 | Dir. 2009/110/CE | monedă electronică | trei ani | 2017-09-01 | — |
| 7 | Dir. 94/19/CE | garantarea depozitelor | cinci ani (regula generală) | 2019-09-01 | — |
| 7bis | — idem, nivelul minim de compensare per deponent (art. 7) | zece ani | 2024-09-01 | — |
| 8 | Dir. 86/635/CEE | conturile anuale ale băncilor | trei ani | 2017-09-01 | — |
| 9 | Dir. 2001/65/CE | modifică 78/660, 83/349, 86/635 (evaluare) | trei ani | 2017-09-01 | — |
| 10 | Dir. 2003/51/CE | modifică 78/660, 83/349, 86/635, 91/674 | trei ani | 2017-09-01 | — |
| 11 | Dir. 2006/46/CE | modifică 78/660, 83/349, 86/635, 91/674 | trei ani | 2017-09-01 | — |
| 12 | Dir. 2001/24/CE | reorganizarea și lichidarea instituțiilor de credit | imediat | 2014-09-01 | — |
| 13 | **Dir. 2009/138/CE** | inițierea/exercitarea activității de asigurare (Solvabilitate II) | șapte ani | 2021-09-01 | **`UE-2009-138`** — potrivire directă |
| 14 | Dir. 91/674/CEE | conturile anuale ale întreprinderilor de asigurare | trei ani | 2017-09-01 | — |
| 15 | Recomandarea 92/48/CEE | intermediarii de asigurări | nu este aplicabil | — | — |
| 16 | Dir. 2002/92/CE | intermedierea de asigurări | trei ani | 2017-09-01 | — (succesoarea IDD, `UE-2016-97`, e generație nouă, neangajată prin acest text) |
| 17 | **Dir. 2009/103/CE** | asigurarea RCA auto (MTPL) | trei ani | 2017-09-01 | **`UE-2009-103`** — potrivire directă |
| 18 | Dir. 2003/41/CE | instituțiile pentru pensii ocupaționale (IORP I) | cinci ani | 2019-09-01 | `UE-2016-2341` ține **IORP II** (2016) — generație mai nouă decât cea angajată |
| 19 | Dir. 2004/39/CE | piețele instrumentelor financiare (MiFID I) | trei ani | 2017-09-01 | `UE-2014-65` ține **MiFID II** — generație mai nouă decât cea angajată |
| 20 | Dir. 2006/73/CE | implementarea MiFID I | trei ani | 2017-09-01 | — |
| 21 | Reg. (CE) 1287/2006 | implementarea MiFID I | trei ani | 2017-09-01 | — |
| 22 | Dir. 2003/71/CE | prospectul valorilor mobiliare (Prospectus I) | trei ani | 2017-09-01 | `UE-2017-1129` ține **Regulamentul Prospectus nou** (2017) — generație mai nouă |
| 23 | Reg. (CE) 809/2004 | implementarea Prospectus I | trei ani | 2017-09-01 | — |
| 24 | **Dir. 2004/109/CE** | obligații de transparență (emitenți) | patru ani | 2018-09-01 | **`UE-2004-109`** — potrivire directă |
| 25 | Dir. 2007/14/CE | implementarea Directivei transparență | patru ani | 2018-09-01 | — |
| 26 | **Dir. 97/9/CE** | sisteme de compensare pentru investitori (ICSD) | cinci ani (regula generală) | 2019-09-01 | **`UE-97-9`** — potrivire directă |
| 26bis | — idem, nivelul minim de compensare per investitor (art. 4) | zece ani | 2024-09-01 | |
| 27 | Dir. 2003/6/CE | abuzul de piață (MAD I) | trei ani | 2017-09-01 | `UE-596-2014`/`UE-2014-57` țin **MAR/CSMAD** (2014) — generație mai nouă |
| 28 | Dir. 2004/72/CE | implementarea MAD I | trei ani | 2017-09-01 | — |
| 29 | Dir. 2003/124/CE | implementarea MAD I | trei ani | 2017-09-01 | — |
| 30 | Dir. 2003/125/CE | implementarea MAD I | trei ani | 2017-09-01 | — |
| 31 | Reg. (CE) 2273/2003 | implementarea MAD I | trei ani | 2017-09-01 | — |
| 32 | Reg. (CE) 1060/2009 | agențiile de rating de credit | cinci ani | 2019-09-01 | — |
| 33 | **Dir. 2009/65/CE** | organisme de plasament colectiv (UCITS) | cinci ani | 2019-09-01 | **`UE-2009-65`** — potrivire directă |
| 34 | Dir. 2007/16/CE | implementarea UCITS (text vechi, 85/611/CEE) | trei ani | 2017-09-01 | — |
| 35 | Dir. 2002/47/CE | contractele de garanție financiară | trei ani | 2017-09-01 | — |
| 36 | **Dir. 98/26/CE** | caracterul definitiv al decontării (SFD) | trei ani | 2017-09-01 | **`UE-98-26`** — potrivire directă |
| 37 | Dir. 2009/44/CE | modifică SFD + garanție financiară | trei ani | 2017-09-01 | — |
| 38 | Dir. 2007/64/CE | serviciile de plată (PSD1) | trei ani | 2017-09-01 | — |
| 39 | Dir. 2005/60/CE | prevenirea spălării banilor (AMLD3) | **un an** | **2015-09-01** | `UE-2015-849` ține **AMLD4/5** (2015) — generație mult mai nouă |
| 40 | Dir. 2006/70/CE | implementarea AMLD3 | un an | 2015-09-01 | — |
| 41 | Reg. (CE) 1781/2006 | informații privind plătitorul la transferuri de fonduri | un an | 2015-09-01 | — |

**Ce arată tabelul, dincolo de faptul că toate termenele au expirat de mult.** Din cele 41 de
instrumente, doar **6** au o potrivire directă în cele 29 de extrase deja ținute (Solvency II, MTPL,
Transparență, ICSD, UCITS, SFD) — restul de **33 nu au niciun extras `UE-*.md`**, inclusiv domenii
întregi absente din corpus: garantarea depozitelor, serviciile de plată (PSD1), contractele de
garanție financiară, agențiile de rating, conturile anuale bancare/de asigurare, CRD I. Alte **5**
instrumente au un corespondent în vault, dar la **generația greșită**: tratatul angajează Moldova la
MiFID I, Prospectus I, MAD I, IORP I și AMLD3, în timp ce extrasele deja ingerate (iulie 2026) sînt
generațiile mai noi (MiFID II, Regulamentul Prospectus, MAR/CSMAD, IORP II, AMLD4/5) — exact tiparul
„parțial/învechit" pe care `acquis-MiFID.md` îl semnalase deja intuitiv, dar acum verificabil
instrument cu instrument. Cel mai scurt termen din toată anexa, **un an** (AMLD3 și normele ei de
aplicare), e și cel mai depășit la nivelul UE însuși — trei generații în urmă (AMLD3 → AMLD4/5 →
pachetul AMLR/AMLD6/AMLA din 2024, deja în vault ca `UE-2024-1624/1640/1620`) — și scadent la doar
un an de la aplicarea provizorie, **1 septembrie 2015**, nu 2017 cum spunea calculul greșit inițial.

**Ce nu e în Anexa XXVIII-A** — precizat, nu doar presupus, pentru cinci pagini `acquis-*` din
vault. Company Law/Takeover/SRD (`UE-2017-1132`, `UE-2004-25`, `UE-2007-36`, `UE-2017-828`) și
Consumer Credit (`UE-2008-48`, `UE-2023-2225`) au fost **verificate** ca stând în alte anexe ale
aceluiași Titlu IV: dreptul societăților în **Anexa II** (Capitolul 3), protecția consumatorilor
în **Anexa IV** (Capitolul 5) — găsite azi, la citirea capitolelor din jurul Capitolului 9, dar
**neingerate și necitite integral**, deci nu se poate încă spune care instrumente anume din
Anexa II/IV corespund paginilor din vault. AIFMD (`UE-2011-61`), EMIR/CSDR (`UE-648-2012`,
`UE-909-2014`) și Crowdfunding (`UE-2020-1503`, firesc — regulamentul e din 2020, posterior
Acordului) rămân **neverificate unde anume**, dacă undeva. Rămâne pentru pasul 6.5.

### 2.3 Ce spun azi cele 18 pagini înghețate

Structura e uniformă: `Ce acoperă` (rezumat tematic), `Lacuna de examinat pentru Moldova` (narativ,
adesea cu `[de verificat]`), `Întrebări deschise` (2-4 întrebări punctuale), apoi lista surselor
EUR-Lex cu articolele-cheie. Citările la nivel de articol sînt rare în corpul paginii (sub 30 de
mențiuni `art. N` distincte pe toate cele 18 pagini) — miezul verificabil e mai degrabă în
frontmatter (`sources:`) și în lista finală, nu în proză. Asta înseamnă că reverificarea nu constă
în a citi mii de articole de directivă, ci în a verifica un set mic de afirmații punctuale, act cu
act.

## 3. Ce s-a schimbat sub aceste pagini de la înghețare (6 septembrie) încoace

Relevant fiindcă unele „Întrebări deschise" de acum trei luni pot avea deja răspuns în corpus:

- Perimetrul CNPF/BNM a primit de atunci: Constituția, HCC (registru complet), primele acte
  subordonate CNPF (`HCNPF-14-5-2016`, `HCNPF-38-5-2015`) și BNM (`HBN-127-2013`, `HBN-130-2013`,
  Regulile DCU, opt Proceduri DCU), Legea 149/2012 (insolvabilitate), Legea 514/1995 (organizare
  judecătorească), grupele de legi corporative/profesionale din 6 septembrie. Niciuna dintre
  acestea nu a fost verificată contra vreunei pagini `acquis-*`, pentru că înghețarea din 6
  septembrie a venit înainte de ele.
- Graful de citare (`_meta/graph/citation-graph.md`) nu citește extrasele UE pentru muchii
  (declarat explicit ca limită), deci nu ajută aici direct — dar coada lui de ingerare poate
  suprapune cu instrumente din Anexa XXVIII-A, de verificat punct cu punct la momentul potrivit.

## 4. Decizii cerute lui Eugen

**D1. Perimetrul Acordului de Asociere: doar Anexa XXVIII-A și articolele-cadru, nu documentul
întreg.** Propunere: ingerarea se limitează la (a) Anexa XXVIII-A („Norme aplicabile serviciilor
financiare", ~25 de instrumente cu calendar), (b) articolele-cadru care guvernează mecanismul de
apropiere legislativă și intrarea în vigoare (art. 462-464 identificate azi; restul capitolului de
servicii/DCFTA relevant rămâne de localizat exact la execuție, nu e un blocaj de plan), și (c) orice
alt punct din acord la care o pagină `acquis-*` sau `entities/` trimite explicit. Restul acordului
(mărfuri, tarife, alte 28 de anexe, cooperare politică) rămâne **neingerat**, exact ca EU-urile
domeniilor conexe pe care coada de ingerare le arată fără să le tragă automat în vault. Prefix nou
propus: `AA-2014` pentru raw, secțiune nouă în manifestul CNPF (pe modelul F/G), pagină de entitate
`entities/AA-2014.md`.

**D2. Nu se digitalizează mecanic toate cele ~2427 de articole din cele 29 de extrase UE.**
Propunere, simetrică cu D1: pentru fiecare din cele 18 pagini, lista de „Întrebări deschise" și
„Lacuna de examinat" se verifică punct cu punct contra (i) Anexei XXVIII-A (există termen legal?
care?) și (ii) textului moldovenesc curent, deja reîmprospătat. Articolele-cheie deja extrase
(sub 150) plus orice articol nou pe care o întrebare concretă îl cere se extrag integral, pe
modelul `discover_latest_celex.py` + o rută de citire simplă (curl direct, fără antete speciale,
verificat azi). Restul actului rămâne „extras", nu se completează „ca să fie complet" — corpusul
existent are deja acest defect (stratul brut cu articole nefolosite, semnalat la punctul 2 din
lucrările deschise ale `CLAUDE.md`) și nu-l repetăm aici cu directive UE de sute de articole.

**D3. Dezghețarea e per-pagină, nu în bloc.** O pagină `acquis-*` iese din `unverified`/
`confidence: low` numai după ce (i) fiecare afirmație din „Lacuna de examinat" a fost verificată
contra textului moldovenesc curent și (ii) fiecare „Întrebare deschisă" a primit fie un răspuns
citat, fie o mutare explicită în lista deschisă a paginii. Data intrării în vigoare a Acordului
(pentru a calcula termenele Anexei XXVIII-A) se stabilește o singură dată, separat, înainte de a
verifica orice pagină individuală — nu se recalculează pe fiecare pagină.

**D4. Ordinea.** Pe numărul de acte legate și pe cât de aproape e perimetrul CNPF de bază:
1. Data intrării în vigoare/aplicării provizorii a Acordului (o căutare, nu o pagină).
2. Ingerarea Anexei XXVIII-A și a articolelor-cadru identificate (`AA-2014`).
3. `acquis-MiFID`, `acquis-MAR` — nucleul pieței de capital, cele mai citate din L-171-2012, deja
   cel mai documentat perimetru al vault-ului.
4. `acquis-AML`, `acquis-Insurance`, `acquis-CompanyLaw` — perimetre cu acte moldovenești deja
   ingerate integral și proaspete (mai puțin de o lună).
5. Restul (`acquis-Crowdfunding`, `acquis-IORP`, `acquis-MTPL`, `acquis-ConsumerCredit`,
   `acquis-Takeover`, `acquis-Transparency`, `acquis-UCITS`, `acquis-AIFMD`, `acquis-CSDR-EMIR`,
   `acquis-ICSD`, `acquis-SFD`) — fără prioritate specială între ele, cea mai simplă ordine e
   alfabetică sau cea a lucrărilor deschise curente ale lui Eugen.
6. `comparisons/cnpf-transposition-matrix.md` la final, fiindcă citează toate celelalte 17.

**D5. Cele 5 consolidări UE mai noi (secțiunea 2.1). Rezolvat 2026-09-15 (pasul 6.4).** Solvency II
(`UE-2009-138`): `-20270130` este cu dată viitoare (2027-01-30, după 2026-09-15) — se amână, nu se
trece la ea acum, pe modelul registrului in-force domestic; cea ținută (`-20250117`) rămâne cea în
vigoare astăzi. Celelalte patru (`UE-2024-1624`, `UE-2024-1640`, `UE-2020-1503`, `UE-97-9`) rămân
„act de bază fără consolidare distinctă listată în RDF-ul Cellar" — explicația din manifest
(corectarea de 2026-09-04) verificată din nou azi, neschimbată. Rulare integrală
`discover_latest_celex.py`: rezultat identic literă cu literă cu cel de acum 11 zile, pe toate cele
29 de extracte, nu doar pe cele 5. Vezi manifestul CNPF, secțiunea F, nota „Reverificat 2026-09-15".

## 5. Pașii, după decizii

| pas | ce | control | poate rula fără Eugen |
|---|---|---|---:|
| 6.1 | recensământ mecanic (acest document, secțiunile 2-3) | ieșirea de mai sus | **făcut 2026-09-15** |
| 6.2 | data intrării în vigoare/aplicării provizorii a Acordului, căutată separat | o singură constatare, citată | **făcut 2026-09-15**: 1 septembrie 2014 (provizorie) / 1 iulie 2016 (vigoare); vezi 2.2-bis |
| 6.3 | `AA-2014`: Anexa XXVIII-A + articolele-cadru, script nou (`ingest_aa.py`, pe modelul `ingest_dcu_rules.py`: sursă unică, PDF sau HTML, ancore proprii) | integritate text PASS, manifest, pagină de entitate | da, curl merge fără Eugen |
| 6.4 | cele 5 verificări de consolidare (D5) | manifest actualizat, `discover_latest_celex.py --check` | **făcut 2026-09-15**: rezultat identic cu 2026-09-04, cele 5 explicate, niciuna schimbată |
| 6.5 | reverificare pagină cu pagină, ordinea din D4, cu extragere țintită de articole noi unde o întrebare o cere | `unverified` scos per pagină, `confidence` ridicat, validator 0 | **făcut 2026-09-16**: toate cele 17 pagini `acquis-*` dezghețate, în patru niveluri, validator 0 pe fiecare |
| 6.6 | `cnpf-transposition-matrix` la final | validator 0, commit | **făcut 2026-09-16**: toate secțiunile A/B/D rescrise cu constatările verificate, validator 0 |

Fiecare pas se încheie cu commit propriu și intrare în `log.md`, pe modelul pasului HCC.

## 6. Ce nu acoperă planul

Restul Acordului de Asociere (Titlurile de comerț cu mărfuri, cooperare politică, justiție și
afaceri interne, capitolele DCFTA din afara serviciilor financiare, toate anexele în afara
XXVIII-A). Actele din Anexa XXVIII-A care nu au deja un extras `UE-*.md` corespunzător în vault
(de verificat la pasul 6.1 dacă listele se suprapun perfect sau dacă apar instrumente noi, cum ar
fi cele mai vechi — 86/635/CEE, 94/19/CE, 91/674/CEE — care s-ar putea să nu fie printre cele 29
deja ingerate). Foaia de parcurs de aderare la UE și planurile naționale de apropiere legislativă
care nu sînt parte a Acordului însuși.

## 7. Raportul de la sfârșit

1. Data intrării în vigoare/aplicării provizorii a Acordului, cu sursa.
2. Ce anume s-a ingerat din Acord (`AA-2014`), cu numărul de articole/puncte și verificarea de
   integritate.
3. Tabelul celor 18 pagini, înainte/după: câte întrebări deschise au primit răspuns, câte au
   rămas, câte pagini au ieșit din `unverified`.
4. Rezultatul celor 5 verificări de consolidare.
5. Ieșirea validatorului și commiturile.
