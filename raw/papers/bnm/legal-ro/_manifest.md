# BNM — legile bancare în română (legal-ro) — manifest

Creat 2026-09-05, pasul P8 al planului de restructurare (decizia D3). Aceste fișiere sunt textul
românesc consolidat de pe legis.md al legilor bancare pe care corpusul BNM le avea doar ca traduceri
engleze neoficiale, neancorate. Regula D2: traducerea localizează, textul de aici se citează.

## Sursa și metoda

- Sursă: legis.md, endpoint `showdetails/<doc_id>`, extras în aceeași zi cu consultarea.
- Descărcare: legis.md a activat la 2026-09-05 după-amiază o verificare Cloudflare care blochează
  `curl`. HTML-ul a fost luat din Chrome-ul lui Eugen, după ce el a trecut verificarea, ca DOM
  serializat (`document.documentElement.outerHTML`), și păstrat în `_meta/imports/bnm/legis-md-ro/`.
  Consecință: fișierele HTML de probă sunt DOM-ul serializat de browser, nu octeții serverului;
  etichetele `<sup>` și structura `#contentdoc` sunt intacte, ceea ce este tot ce cere extractorul.
- Extracție: `_meta/imports/bnm/ingest_bnm_ro.py`, înveliș peste
  `_meta/imports/moldova-legal/ingest_business_law.py`, cu aceleași funcții de rezolvare a
  exponenților, extracție și asamblare. Verificare: `_meta/imports/bnm/verify_bnm_ro.py`, generat din
  `verify_business_law.py`, cu testul de fond identic: liniile de structură adăugate se scot și
  restul se compară linie cu linie cu extracția simplă din același HTML.
- doc_id-urile au fost găsite prin căutare în titlu, `search_type=1`, fără diacritice; rândul actului
  de bază apare cu marcajul „Modificat” și numărul `LP<nr>/<an>`.

## Actele

| Fișier | Act | doc_id | Consolidare | Ancore | Integritate | Note |
|---|---|---:|---|---:|---|---|
| `L-202-2017.md` | Legea nr. 202/2017 privind activitatea băncilor | **151077** (151445 până la 2026-09-06) | **2025-10-25** | 155 | PASS, 1560 linii | 149 de bază fără lacune, 6 cu exponent; reîmprospătat 2026-09-06 (LP189/2025, art. 97 alin. (5) lit. a^1), versiunea veche în `_archive/raw/bnm-legal-ro-legis-md-before-refresh-20260906-220712/` |
| `L-548-1995.md` | Legea nr. 548/1995 cu privire la BNM | 154046 | 2026-04-23 | 91 | PASS, 842 linii | **7 lacune fără marcaj în sursă**: 12, 13, 29, 30, 48, 54, 73; republicată 2015; `[de verificat]` |
| `L-114-2012.md` | Legea nr. 114/2012 servicii de plată și monedă electronică | 155331 | **2027-01-01, viitoare** | 131 | PASS, 1328 linii | o dispoziție cu intrare amânată, art. 103^1 alin. (4) lit. h) |
| `L-232-2016.md` | Legea nr. 232/2016 redresarea și rezoluția băncilor | 146912 | 2025-02-28 | 344 | PASS, 1443 linii | articole fără titlu, forma `Articolul N. –` |
| `L-62-2008.md` | Legea nr. 62/2008 reglementarea valutară | 152953 | 2025-12-31 | 73 | PASS, 1103 linii | titlul oficial poartă asterisc de republicare |
| `L-160-2023.md` | Legea nr. 160/2023 garantarea depozitelor în bănci | 137939 | 2023-10-01, nemodificată | 58 | PASS, 599 linii | **înlocuiește Legea 575/2003**, abrogată pe legis.md (doc_id 137950) |
| `L-550-1995.md` | Legea nr. 550/1995 cu privire la lichidarea băncilor (fosta Lege a instituțiilor financiare) | 146899 | 2025-02-28 | 20 | PASS, 348 linii | P8-bis; **denumire schimbată**; doar arts. 1–3 și 38^1–38^17 în vigoare, cap. I–VI abrogate |
| `L-250-2017.md` | Legea nr. 250/2017 supravegherea suplimentară a conglomeratelor financiare | 105629 | 2018-03-29, nemodificată | 23 | PASS, 251 linii | P8-bis; BNM și CNPF sub același regim |
| `L-239-2008.md` | Legea nr. 239/2008 transparența în procesul decizional | 142655 | 2024-07-05 | 20 | PASS, 148 linii | P8-bis; lege generală, aici doar pentru că BNM o ține în registrul său |
| `HBN-127-2013.md` | Hotărârea BNM nr. 127/2013, Regulamentul cu privire la deținerile în capitalul social al băncii | 126093 | 2021-05-09 | **0, structură pe puncte** | PASS, 390 linii | **primul act subordonat al BNM aici**, 2026-09-08; 75 de puncte în anexă, 10 capitole; anexele nr. 1–2^4 absente din text; pct. 8 definește circumstanțele obiective ale art. 46 din 202/2017 și numește succesiunea; denumire schimbată de HBN52/2021 |
| `HBN-130-2013.md` | Hotărârea BNM nr. 130/2013, Regulamentul cu privire la calculul drepturilor de vot şi înregistrarea transferului dreptului de proprietate asupra acţiunilor băncilor | 111967 | 2018-12-23 | **0, structură pe puncte** | PASS, 82 linii | al doilea act subordonat, 2026-09-08; 18 puncte, 3 capitole; anexele 1–2 absente din text, dar prezente în engleză în corpusul BNM (091–092); pct. 14: dobândirea în circumstanțe obiective se înscrie fără aprobare prealabilă, cu vot suspendat |

## Ce s-a schimbat față de lista D3

Lista D3 numea Legea 575/2003. legis.md o arată abrogată; actul curent este Legea 160/2023, în vigoare
din 01.10.2023, care transpune parțial Directiva 2014/49/UE. Decis de Eugen la 2026-09-05: se
ingerează înlocuitorul. Textul abrogat nu este ingerat; pentru spețe anterioare lui 01.10.2023 se
caută separat.

## P8-bis, 2026-09-05

După P9 au rămas în `raw/papers/bnm/legal/documents/` cinci traduceri engleze fără text românesc în
vault: 250/2017 (două variante), 550/1995 și 239/2008 (două variante). Cele trei acte au fost ingerate
în aceeași zi, pe aceeași metodă. Cloudflare a cerut din nou bifa lui Eugen la prima navigare:
verificarea expiră între sesiuni.

## HBN-127-2013, 2026-09-08 — primul act subordonat al BNM

Cerut de Eugen pentru speța moștenitorului unui acționar de bancă: art. 46 alin. (1) din 202/2017
lasă „circumstanțele obiective" în seama actelor normative ale BNM, iar registrul dosarelor (M-001,
punctul deschis (b)) nu putea spune dacă succesiunea este una dintre ele. Pct. 8 al regulamentului o
numește expres: „prin succesiune; moştenire; donaţie sau alt mod de transmitere cu titlu gratuit".
Detalii și capcane pe pagina de entitate `entities/HBN-127-2013.md`.

Ce diferă față de metoda legilor:

- **Structură pe puncte, zero ancore de articol.** Numerotarea repornește între hotărâre (pct. 1–4)
  și regulamentul anexat (pct. 1–75, plus 20 de puncte cu exponent). O trimitere la „pct. N" nu
  este ancorată; se citează prin capitol și punct. Aceeași consecință ca la `DCA-61-2024` și la
  hotărârile de Guvern din `moldova-legal/`.
- **Anexele nu sunt în text.** legis.md redă anexele nr. 1, 1^1, 2, 2^1–2^4 doar ca rânduri de
  titlu cu marcaj de modificare. Chestionarele și declarațiile nu se pot cita din vault.
- **Două denumiri de căutat.** HBN52/2021 a înlocuit „cotele de participare" cu „dețineri" în tot
  textul, deci actele de modificare de dinainte de 2021 apar sub titlul vechi, iar cel din 2021
  numai sub cel nou. Căutările în titlu, fără diacritice: „cotelor de participare in capitalul
  bancii" (3 rânduri) și „detinerile in capitalul social al bancii" (4 rânduri).
- **Descărcarea:** octeții serverului, prin `fetch` same-origin în pagina legis.md din Chrome-ul lui
  Eugen și descărcare ca blob (156.741 de octeți), cu acordul lui explicit; nu DOM serializat ca la
  P8. Instrumentul JavaScript al extensiei maschează orice `href` cu șir de interogare, deci
  doc_id-urile s-au extras ca cifre simple. Verificarea Cloudflare a reapărut între două cereri și
  s-a rezolvat la reîncărcare, fără clic.
- **Consola:** `--precheck` cade pe consola Windows cp1252 la afișarea titlului cu „Ă"
  (`UnicodeEncodeError`); se rulează cu `PYTHONUTF8=1`. Scripturile nu se schimbă.
- **Trimitere învechită în sursă:** pct. 73 trimite la „articolul 54, alineatul (3) din Legea
  privind societăţile pe acţiuni"; în `L-1134-1997` de astăzi lista este art. 52, data de referință
  art. 56 alin. (1). Consemnat pe pagina de entitate, nu corectat.

Următorul din aceeași listă: Regulamentul BNM nr. 130/2013 privind calculul drepturilor de vot și
înregistrarea transferului, la care trimite pct. 11; corpusul englez are din el doar anexele.

## HBN-130-2013, 2026-09-08 — regulamentul-pereche, ingerat în aceeași zi

Actul la care trimit art. 45 alin. (6) și (7) din 202/2017 și pct. 11 din HBN-127-2013. Text scurt,
18 puncte în trei capitole, versiune în vigoare din 23.12.2018 prin HBN260/2018, care l-a rescris pe
Legea 202/2017. Pagina de entitate: `entities/HBN-130-2013.md`.

Ce aduce și ce diferă:

- **Pct. 14 tranșează înscrierea.** Dobândirea în circumstanțe obiective, deci și prin succesiune,
  se înscrie la registrator sau custode **fără** aprobarea prealabilă a BNM, cu declarația de la
  pct. 15, iar registratorul notează concomitent suspendarea dreptului de vot. Corectează lectura
  din răspunsul de dimineață, care lăsa art. 45 alin. (6) ca blocaj la înscriere.
- **Anexele sunt împărțite între două fișiere.** Textul românesc de pe legis.md are doar titlurile
  anexelor 1 și 2; traducerea engleză din `raw/papers/bnm/legal/documents/091–092` are doar
  anexele. Nu se retrag, spre deosebire de traducerile legilor de la P9.
- **Marcaje fără paranteze.** Modificările HBN260/2018 sunt însemnate „Substituit/în redacţie prin
  HBN260 ...", pe rând separat, fără număr de punct și fără dată de intrare în vigoare; data stă
  doar în rândul de versiune din capul textului, pe care extractorul îl citește corect
  (`consolidation_date: 2018-12-23`). Fișa nu are rândul „MODIFICAT".
- **Titlu-pereche citat greșit în sursă.** Pct. 14 numește „Regulamentul cu privire la deținerile
  de participare în capitalul social al băncii", formă care nu a existat niciodată. Consemnat, nu
  corectat.
- **Exponent turtit în preambul:** „articolelor 15-156 din Legea instituţiilor financiare" este
  15–15^6. Text de sursă, rămâne așa.
- Aceeași rută de descărcare ca la HBN-127-2013 (42.451 de octeți), Cloudflare reapărută o dată,
  rezolvată la reîncărcare.

## Ce rămâne deschis

- Lacunele din `L-548-1995`, mai sus. Nu se corectează aici; se verifică la sursă.
- Legile de interpretare (185/2023 și 22/2020 pentru 202/2017; 265/2016 pentru 232/2016) nu sunt
  ingerate. Articolele interpretate nu se citează fără ele.
- Retragerea traducerilor engleze corespunzătoare: făcută la P9 pentru primele șase legi
  (`_archive/bnm-en-2026-09/`); pentru cele trei de la P8-bis, cele cinci fișiere engleze au fost mutate
  în aceeași arhivă la 2026-09-05, după confirmarea lui Eugen.
