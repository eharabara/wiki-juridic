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
