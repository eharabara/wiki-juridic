# Lacună de acoperire: practica generală de avocatură

Data: 2026-09-17. Sursă: întrebare directă a lui Eugen în sesiune ("ce segmente de corpus
relevante pentru un avocat lipsesc?"), verificată mecanic împotriva `_meta/graph/citation-graph.md`
(coada de ingerare) și `raw/papers/moldova-legal/_manifest.md`, nu ghicită.

## Context

Corpusul de azi (99 acte moldovenești, coverage generat 2026-09-17) e construit dens în jurul
perimetrului CNPF/BNM și dreptul afacerilor, pentru că așa a fost definit perimetrul de la
început (`CLAUDE.md`, secțiunea "Read this first") și pentru că graful de citare trage fiecare
act nou ingerat spre acolo prin citări reale, nu prin alegere. Consecința: mai multe domenii pe
care o practică generală de avocatură le atinge des nu au nicio sursă primară în vault.

## Ce lipsește

### 01. Confirmat direct, gol cunoscut

- **Codul familiei (COD-1316-2000)** — absent complet. Apare doar ca țintă externă de citare în
  graf (citat de `L-246-2018`, `CC-1107-2002`). Divorț, încredințare minori, regim matrimonial,
  adopție: fără sursă ancorată.
- **Dreptul de autor** — singurul act de proprietate intelectuală întâlnit, `L-139-2010`
  ("privind dreptul de autor și drepturile conexe"), e **abrogat**; succesoarea a fost explicit
  lăsată deoparte la ingerarea lui `L-325-2013` din 2026-09-17 ("ar fi cerut găsirea
  succesoarei" — `raw/papers/moldova-legal/_manifest.md:2224`). Mărci, brevete, desene
  industriale (AGEPI): nimic în corpus.
- **Notariatul** — nicio lege-cadru a notariatului ingerată. Actele subordonate CNPF/BNM
  (`HCNPF-14-5-2016`, `HBN-127-2013`) doar *menționează* certificatul de moștenitor al
  notarului.
- **Mediere și avocatură** — `Legea cu privire la mediere` și `Legea cu privire la avocatură`
  sînt citate de acte deja ținute (6 mențiuni fiecare) dar apar în graf doar ca placeholder pe
  nume (`LEGE:mediere`, `LEGE:avocatura`), fără corp de text în vault.

### 02. În coada de ingerare, cu prioritate mecanică

Din `_meta/graph/citation-graph.md`, coloana "acte care îl citează" (cea care contează pentru
ordine):

| act citat | mențiuni | acte care îl citează |
|---|---:|---:|
| `COD-325-2022` Codul electoral | 38 | 9 |
| `COD-150-2014` Codul transporturilor rutiere | 22 | 1 |
| `COD-1316-2000` Codul familiei | — | citat de `L-246-2018`, `CC-1107-2002` |
| `COD-152-2014` Codul educației | — | citat, neingerat |
| `COD-502-1995` Codul jurisdicției constituționale | — | citat, neingerat |

### 03. Nu absent, dar cu rezervă de citat

`COD-154-2003` (Codul muncii) **este** ținut, dar cu consolidare datată în viitor
(2027-01-01) — orice citare azi trebuie verificată în `_meta/inforce/in-force-register.md`
înainte de a spune că textul leagă acum.

### 04. Neverificat, de urmărit

Succesoarea legii protecției datelor cu caracter personal, după abrogarea `L-133-2011`
(23-08-2026). Nu s-a confirmat dacă e sau nu în corpus — verificare de făcut înainte de a cita
orice pe acest subiect.

## De ce contează

Perimetrul actual servește bine persoanele P legate de CNPF/BNM/drept corporativ-financiar. Un
avocat cu practică generală (familie, imobiliar cu notar, IP, mediere, muncă) nu are azi nicio
sursă ancorată în aceste zone — răspunsurile ar fi `neancorate` prin construcție, nu prin
eroare.

## Pas următor

Nu e o decizie de ingerare imediată — Eugen decide ordinea. Dacă un dosar concret atinge unul
din domeniile de mai sus, verifică punctual înainte de a te baza pe vault, și ia în calcul
ingerarea țintită a actului relevant cu metoda deja folosită
(`_meta/imports/moldova-legal/ingest_business_law.py`), nu cu scriptul CNPF.

## Stare actualizată — 2026-09-25

Cele trei goluri primare au fost închise prin ingerare țintită din surse oficiale:

- `COD-1316-2000` — Codul familiei;
- `L-69-2016` — Legea privind organizarea activității notarilor;
- `L-230-2022` — Legea privind dreptul de autor și drepturile conexe.

Medierea și avocatura erau deja acoperite prin `L-9-2026` și `L-1260-2002`, deci nu au fost duplicate.
Rămîn deschise numai subperimetrele IP privind mărcile, brevetele și desenele industriale, precum și
verificarea actelor secundare notariale/AGEPI. Textele noi sînt extras web/legis.md și nu sînt PDF-uri
locale byte-verificate; pentru opinii externe se verifică versiunea consolidată, registrul in-force și
registrul HCC.

## Rezolvat 2026-09-19

Verificat mecanic, nu din memorie, în timp ce documentul 05 (`legal-career/05-knowledge-map.md`)
era analizat linie cu linie. Trei dintre cele patru puncte de mai sus se schimbă.

### Mediere și avocatură: nota era deja învechită în ziua în care a fost scrisă

Secțiunea „01. Confirmat direct, gol cunoscut" de mai sus le listează pe amândouă ca absente.
Fals la data notei (17 septembrie): `L-1260-2002` (Legea cu privire la avocatură, 73 de articole)
era deja ținută dinainte de 10 septembrie, iar `L-9-2026` (Legea privind medierea și statutul
mediatorului, 63 de articole, care abrogă expres `L-137/2015` la art. 62 alin. (2)) fusese
ingerată chiar cu o zi înainte, pe 16 septembrie. Ambele domenii au deci sursă primară ancorată.
Ce a indus în eroare: în `_meta/graph/citation-graph.md` cele două acte apar doar ca marcaje pe
nume, `LEGE:mediere` și `LEGE:avocatura`, pentru că actele care le citează le numesc fără număr
(„Legea cu privire la mediere"), iar rezolvatorul de graf potrivește actele deținute după număr,
nu după nume. **Concluzie generală, utilă dincolo de acest caz: un rând din coada de ingerare
identificat doar pe nume nu e dovadă de absență — verifică întâi dacă actul e deja ținut sub alt
număr, înainte de a-l trata ca lipsă.** Verificat la fel celelalte rânduri pe nume din aceeași
coadă: `LEGE:publicitate-si-cu` = `L-62-2022` (ținută), `LEGE:achizitiile-publice` =
`L-131-2015` și succesoarea `L-325-2025` (ambele ținute); rămân neidentificate
`LEGE:contabilitatii`, `LEGE:serviciului-public` (ambiguu, posibil deja acoperit de `L-158-2008`,
neverificat), `LEGE:statutul-municipiului`, `LEGE:protectia-martorilor-si-altor`,
`LEGE:descentralizarea-administrativa`, `LEGE:locuinte`, `LEGE:protectia-indicatiilor-geografice`,
`LEGE:statutul-alesului-local`.

### Protecția datelor cu caracter personal: succesoarea e în corpus

Întrebarea 04 de mai sus („neconfirmat dacă succesoarea lui `L-133-2011` e în corpus") are
răspuns simplu: da. `L-195-2024` și `L-160-2026`, ambele „privind protecția datelor cu caracter
personal", sunt ținute — `L-133-2011` însuși rămâne în vault doar ca text abrogat (de la
23.08.2026), păstrat pentru că alte acte din corpus încă îl citează și pentru faptele dinainte de
abrogare.

### Proprietatea intelectuală: `L-139-2010` nu e „deținut", e doar zgomot de subsol

Corectare de precizie, nu de fond: nota de mai sus scrie corect „**întâlnit**", nu „deținut" —
`L-139-2010` (dreptul de autor) nu are niciun fișier în vault, e doar o țintă externă de citare.
Dar rangul lui în coada de ingerare e fals: stă pe locul 1-2 la „acte care îl citează" (9 acte),
și toate cele nouă sunt fișierele DCU (`DCU-PROC-*`, `DCU-REGULI-2026`), iar fiecare „citare" e
nota de subsol de copyright tipărită pe fiecare pagină a PDF-ului sursă („Prezentul document și
conținutul acestuia este protejat de Legea nr.139/2010..."), nu un renvoi juridic. Concluzia
notei (IP neacoperit) rămâne corectă; premisa „e primul candidat după rang" nu ar trebui folosită
fără verificare — coada de ingerare nu distinge o citare juridică reală de o formulă de copyright
repetată mecanic pe fiecare pagină a unui PDF.

**Nefăcut, pentru că nu a fost cerut acum:** filtrarea notelor de subsol din
`build_citation_graph.py`. Ar cere o regulă specifică pentru DCU, cu riscul deja cunoscut din
`CLAUDE.md` (secțiunea „Coverage") pentru orice regulă îngustă aplicată graful validat — decizia
rămâne a lui Eugen.
