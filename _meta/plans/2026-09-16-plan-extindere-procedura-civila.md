# Plan pentru extinderea ingestiei: tot ce e relevant pentru dreptul procesual civil

Data: 16 septembrie 2026
Folder vizat pentru execuție: `C:\Users\harab\wiki` (nu această sesiune — vezi secțiunea 0)
Stare: **propunere, cu partea mecanică executată** (interogarea grafului, secțiunea 2). Ingestia
propriu-zisă (secțiunea 3) nu a fost făcută. Continuă firul D3 (procedura civilă), al cărui ultim
pas a fost `L-213-2023` (secțiunea W a manifestului moldova-legal, 16 septembrie).

---

## 0. De ce planul se oprește aici, în această sesiune

Cerința a fost „extindem ingestia, tot ce e relevant pentru drept procesual civil”. Sesiunea
curentă rulează într-un mediu izolat (agent remote pe `eharabara/wiki-juridic`), nu pe
`C:\Users\harab\wiki`, și verificarea directă arată că **`www.legis.md` nu este accesibil de
aici**: `curl` către `cautare/getResults` întoarce `connect_rejected` prin proxy-ul de ieșire, iar
jurnalul proxy-ului confirmă explicit `403` la `CONNECT www.legis.md:443` — refuz de politică a
organizației, nu o fluctuație Cloudflare de genul celor documentate deja în manifest. Nu există
nicio pagină legis.md pre-descărcată în repo pentru actele țintă de mai jos.

Asta înseamnă că nimic nu poate fi **ingerat** propriu-zis aici: nu există sursă de citit, deci nu
există ce ancora, ce hash-ui sau ce verifica. Scrierea de text de lege „din memorie” ar încălca
direct regula de bază a acestui folder (`raw/` este imuabil și orice ancorare trebuie dovedită
împotriva sursei), așa că nu s-a încercat.

Ce s-a făcut în loc: partea care nu cere legis.md — folosirea grafului de citare deja construit
pentru a găsi, mecanic, exact ce lipsește și cît de central e fiecare lipsă, exact metoda care a
dat `L-213-2023` cu o zi în urmă. Rezultatul e lista de mai jos, gata de executat cu
`ingest_business_law.py` de pe mașina cu acces la legis.md.

## 1. Metodă

Interogare directă a `_meta/graph/citation-graph.json`, filtrată pe muchiile `cites_act` al căror
`source` e unul din cele patru acte deținute care formează nucleul procedurii civile —
`COD-225-2003` (Codul de procedură civilă), `COD-443-2004` (Codul de executare),
`L-514-1995` (organizarea judecătorească), `L-198-2007` (asistența juridică garantată de stat) —
și al căror `target` e un nod extern (`EXT:...`, act nedeținut). Agregat pe act țintă, cu numărul
de mențiuni și actele-sursă. Fiecare rând de mai jos a fost apoi verificat citind linia sursă din
fișierul deținut (coloana „dovadă”), nu doar citit din agregat.

## 2. Ce a dat interogarea, pe niveluri de relevanță

### Nivelul 1 — conținut procesual direct (de ingerat primele)

| act | ce e | citat din | dovadă |
|---|---|---|---|
| `L-137-2015` — Legea cu privire la mediere | mediere civilă/penală/contravențională | `COD-225-2003` art. 60, 89, 260, 489; `L-198-2007` art. 2, 10^1, 36^9, 36^13; și, sub alias fără număr, `COD-122-2003`, `COD-218-2008` | CPC art. 260: „iniţierii medierii în condiţiile Legii cu privire la mediere”; art. 489: tranzacție anulabilă „cu încălcarea prevederilor Legii cu privire la mediere” |
| `L-325-2013` — Legea privind evaluarea integrității instituționale | susține un capitol întreg al CPC | `COD-225-2003` art. 343^6, 343^7, 343^8 (acțiunea civilă de control al averii) | art. 343^6: „autoritățile indicate la art. 12 din Legea nr. 325/2013” |
| `L-100-2001` — Legea privind actele de stare civilă | proceduri speciale civile | `COD-225-2003` art. 300, 301, 334 | art. 301: „anularea, în condițiile Legii nr. 100/2001 ..., a actului de deces” |
| `L-99-2010` — Legea privind regimul juridic al adopției | procedură specială civilă | `COD-225-2003` art. 290 | „consimțămintele părinților ... prevăzute la art. 26 alin. (2) din Legea nr. 99/2010” |
| `L-488-1999` — Legea exproprierii pentru cauză de utilitate publică | stabilirea despăgubirii pe cale civilă | `COD-225-2003` art. 175 (+ alte 8 acte deținute) | art. 175: „cu respectarea Legii exproprierii ... nr. 488/1999” |
| `L-142-2008` (ipotecă) + `L-449-2001` (gaj) | executarea silită a garanțiilor reale | `COD-443-2004` art. 24^1, 151^1 | art. 24^1: „Legea nr. 449-XV ... cu privire la gaj şi Legea nr. 142-XVI ... cu privire la ipotecă” |
| `L-289-2004` — indemnizații pentru incapacitate temporară de muncă | venituri exceptate de la urmărire silită | `COD-443-2004` art. 110; `CC-1107-2002` art. 36 | art. 110: trimitere la art. 5 alin. (1) lit. a)–c), g) din Legea 289/2004 |

### Nivelul 2 — coloana vertebrală instituțională a justiției civile

| act | ce e | citat din |
|---|---|---|
| `L-544-1995` — statutul judecătorului | numire, suspendare, disciplină | `L-514-1995` art. 16, 21 |
| `L-947-1996` — Consiliul Superior al Magistraturii | organul de autoadministrare | `L-514-1995` art. 23^2 |
| `L-64-2023` — Curtea Supremă de Justiție | instanța de recurs/casație în procesul civil | `L-514-1995` art. 43 |

### Nivelul 3 — execuțional, relevanță mai îngustă sau mixtă civil/penal

`L-300-2017` (administrația penitenciară), `L-187-2022` (condominiu, context de executare
imobiliară), `L-140-2013` (protecția specială a copiilor, context de executare a pensiei de
întreținere), `L-235-2008` (control civil asupra armelor, capitol penitenciar din Codul de
executare), `L-186-2008` (securitate și sănătate în muncă, context Codul muncii/Codul de
executare). Toate citate o singură dată sau de două ori, din contexte care ating mai degrabă latura
penală/administrativă a Codului de executare decît procedura civilă propriu-zisă.

### Ce NU e o lacună reală (verificat, nu presupus)

- **`LEGE:avocatura`, `LEGE:avocatura-si-ale-prezentei`** — aliasuri ale grafului pentru „Legea cu
  privire la avocatură” citată fără număr. Actul e deja deținut: `L-1260-2002`. Nicio ingestie
  necesară; e limita de rezoluție a grafului pe citări fără număr, documentată deja pentru alte
  cazuri în `_meta/graph/citation-graph.md`.
- **`LEGE:mediere`** — același act ca `L-137-2015`, de mai sus, citat fără număr din
  `COD-122-2003` și `COD-218-2008`. Nu e un al doilea act.
- **`LEGE:insolvabilitatii`** — `L-149-2012`, deja deținut.
- **`LEGE:procedurala-civila-care-impune`** — fals pozitiv mecanic: CPC art. 3 conține fraza
  „Legea procedurală civilă care impune obligaţii noi anulează sau reduce drepturile...”, o
  normă tranzitorie **despre sine însuși**, pe care regula „din legea indicată” a extractorului a
  citit-o ca pe un act extern. Nu există un asemenea act de ingerat.
- **`L-17-2018`, `L-143-2010`, `L-153-2012`** — apar doar în preambulul actelor deținute, ca
  temei al republicării („Republicat în temeiul art. ... al Legii nr. ...”), nu ca normă de trimis
  la conținut. Nesubstanțiale pentru procedura civilă.
- **`COD-1524-1993`, `L-1226-1997`** — menționate o singură dată, în lista de acte abrogate/
  predecesoare din chiar articolul tranzitoriu al Codului de executare (art. 324). Text istoric,
  nu drept în vigoare de ingerat.

## 3. Comanda de execuție, cînd există acces la legis.md

Pentru fiecare act din nivelul 1 și 2: căutare pe legis.md după titlu (fără diacritice, ruta
`getResults?search_string=...&search_type=1` descrisă în manifest, secțiunea M.1), verificarea
listei de versiuni a actului pentru consolidarea curentă reală (nu rîndul de căutare, nu doc_id-ul
cel mai mare — capcana documentată de două ori în manifest, secțiunile U.14 și V.2), apoi adăugare
în `DOCS` din `_meta/imports/moldova-legal/ingest_business_law.py` cu `doc_id` și titlu, rulare,
și verificare cu `verify_business_law.py`. Pagină de entitate nouă pentru fiecare, rînd nou în
manifestul moldova-legal și în `index.md`, apoi `python _meta/close_session.py --commit`.

Ordinea recomandată: `L-137-2015` întîi (cel mai citat, singurul cu prezență și în Codul penal și
în cel contravențional, deci închide trei lanțuri deodată), apoi `L-325-2013` (susține un capitol
întreg al CPC care altfel rămîne fără temei ancorabil), apoi `L-100-2001` și `L-99-2010` (proceduri
speciale mici, ieftin de ingerat), apoi perechea `L-142-2008`/`L-449-2001`, apoi `L-488-1999`,
apoi `L-289-2004`. Nivelul 2 (statut judecător, CSM, CSJ) poate veni oricînd după, fiind
independent de conținutul de mai sus.

## 4. Ce rămîne deschis

- Nivelul 3 nu e recomandat pentru ingestie imediată; e listat ca să nu fie regăsit și confundat
  cu o lacună nouă la o rulare viitoare a grafului.
- După fiecare ingestie, coada de ingerare trebuie recalculată (`build_citation_graph.py`): actele
  noi vor cita, la rîndul lor, alte acte nedeținute (de exemplu `L-137-2015` va cita probabil
  Legea nr. 26/2022 sau alte acte despre profesia de mediator — neverificat aici, fără sursă).
