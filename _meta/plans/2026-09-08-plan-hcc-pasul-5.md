# Plan pentru pasul 5: hotărârile Curții Constituționale, restrânse la actele din bază

Data: 8 septembrie 2026
Folder vizat: `C:\Users\harab\wiki`
Stare: **propunere, cu partea mecanică executată** (recensământul, secțiunea 2). Deciziile din
secțiunea 3 sunt ale lui Eugen; nimic din `raw/` nu a fost atins.
Urmează: `_meta/plans/2026-09-06-plan-extindere-perimetru-domestic.md`, ai cărui pași 1–4 sunt
executați și raportați (`2026-09-06-raport-executie.md`, secțiunile 1–7). D3 din acel plan dă
pasul 5 ca următorul și cere pentru el plan separat.

---

## 1. Ce s-a verificat la 8 septembrie înainte de a porni

- Arbore curat pe `main` la `8c26928`; `close_session.py --check` curat: registrul in-force,
  blocul de acoperire și `SCHEMA.md` la zi, validator 0 erori, 3 avertismente (una este stampila
  registrului dosarelor, `taken 2026-09-07`, de reîmprospătat din proiect, D9).
- Planul din 6 septembrie: executat integral. Cele cinci decizii din secțiunea 5 a raportului
  și cele două lacune cu metodă (Codul fiscal 2027, Legea 160/2011) sunt închise pe 7 septembrie.
- Secțiunea „Planned extension" din copia `legal-career/05-knowledge-map.md` este încă versiunea
  din 5 septembrie. Planul din 6 septembrie o înlocuiește, iar raportul spune că documentul 05 se
  actualizează în proiect după raport. Nu s-a făcut; copia de aici nu se editează local.
- Ce rămâne din D3 după pasul 5: pasul 6 (Acordul de Asociere, textele UE integrale,
  reverificarea constatărilor acquis). Nu e acoperit aici.

## 2. Recensământul: ce spun textele deținute despre HCC

Generat de `_meta/plans/hcc_census.py`, ieșirea în `hcc-census-2026-09-08.md` și `.json`. Cifrele
de mai jos sunt cele din acea rulare; nu le retranscrie, rulează scriptul.

**Ce s-a aflat, și de ce contează mai mult decât s-a crezut la 5 septembrie.**

1. **19 acte din bază poartă cel puțin o hotărâre a Curții Constituționale în fișă**, în total 76
   de hotărâri distincte, din 1999 până la HCC9 din 22.07.2025. Toate codurile de procedură, Codul
   penal, Codul contravențional, Codul fiscal, Constituția, legea avocaturii, legea insolvabilității,
   organizarea judecătorească, Legea 548/1995 a BNM.
2. **Numai 16 dintre ele mai au marcaj la articol.** Pentru celelalte ~60, textul spune doar în
   fișă „HCCnn din dd.mm.yy", fără să spună ce articol a fost lovit. Este exact mecanismul 1 din
   întrebarea deschisă 3 (marcajul cade la reîmprospătare), aplicat hotărârilor Curții. Consecința
   este cea din documentul 05: „o dispoziție anulată se citește în continuare ca lege în textul
   brut". Un cititor al Codului fiscal vede 10 HCC în fișă și niciun articol marcat.
3. **Marcajul, unde există, are două forme**, și prima versiune a scriptului o pierdea pe a doua:
   `[Art.N ... declarat neconstituțional prin HCCnn ...]` între paranteze drepte, și
   `*Art.N ...` sau `*Notă: Articolul N ...` cu asterisc, forma Codului contravențional (7 din cele
   16). Orice cititor mecanic al marcajelor trebuie să știe ambele.
4. **O hotărâre poate lovi trei acte deodată**: HCC3 din 09.02.2012 (Legea 163/2011) apare în
   Codul de procedură penală, Codul contravențional și Legea 514/1995. Deci unitatea de lucru este
   hotărârea, nu actul.
5. **Verificat azi: nicio pagină din `entities/`, `concepts/`, `comparisons/` nu citează vreunul
   dintre cele 16 articole cu marcaj vizibil.** Pentru cele ~60 fără marcaj nu se poate verifica
   nimic până nu se știe articolul. Acesta este golul.

## 3. Decizii cerute lui Eugen

**D1. Ce se construiește: registru, nu text integral, în prima etapă.** Propunere: un registru
al dispozițiilor declarate neconstituționale, pe modelul registrului in-force, în `_meta/hcc/`,
generat dintr-un fișier scris de mână (hotărâre, act, articol, întinderea, MO, data) plus
marcajele citite mecanic din `raw/`. Textul integral al hotărârilor nu se ingerează în această
etapă: 76 de hotărâri sunt volum mare, cu numerotare pe puncte (fără ancore, clasa HG), iar
răspunsul de zi cu zi are nevoie de dispozitiv, nu de motivare. Textul integral rămâne pentru
hotărârile cu constatare vie, la cerere, sub prefix nou `HCC-`, consemnat în manifest la momentul
primei ingerări, cu aceeași regulă ca pentru actele Uniunii Avocaților: **numai de pe legis.md**,
niciodată de pe constcourt.md, fiindcă nu există control pentru sursa aceea.

**D2. Cum se recuperează articolul pentru cele ~60 de hotărâri fără marcaj.** Două căi, ambele
prin `fetch` în pagina legis.md fără descărcare (metoda U.7, care nu cere acord de descărcare):
(a) se citește versiunea actului produsă de hotărâre, din istoricul de versiuni, unde marcajul
încă există; (b) se citește fișa hotărârii însăși pe legis.md, unde dispozitivul dă articolul.
Calea (a) e mai sigură, pentru că marcajul e scris de publisher în forma pe care o citim deja;
calea (b) verifică. Amândouă cer trecerea verificării Cloudflare de către Eugen, deci pasul nu
poate fi executat într-o sesiune fără el.

**D3. Ordinea.** Codurile cu cele mai multe HCC pierdute și cele mai citate în munca de stagiar
primesc întâietate: Codul fiscal (10, zero marcaje), Codul contravențional (9 în fișă, 7 marcaje),
Codul de procedură penală (21 în fișă, 3 marcaje), Codul de procedură civilă (6, zero), Codul
penal (8, zero). Constituția (3, două HCC interpretative ale art. 13 și 78, de tratat separat:
interpretarea nu anulează).

**D4. Controlul.** Trei lucruri, în ordinea asta: (i) registrul e citit de blocul de acoperire
din `CLAUDE.md` ca flag nou, „articole declarate neconstituționale", alături de „Not yet in
force"; (ii) validatorul avertizează când o pagină structurată citează un articol din registru
fără cuvântul „neconstituțional" în același paragraf, așa cum verifică azi citarea provizioanelor
neintrate în vigoare; (iii) pagina de entitate a fiecărui act lovit primește o secțiune cu lista.
Nimic din acestea nu rescrie textul brut.

## 4. Pașii, după decizii

| pas | ce | control | poate rula fără Eugen |
|---|---|---|---:|
| 5.1 | recensământ mecanic | `hcc_census.py`, ieșirea în plan | **făcut 2026-09-08** |
| 5.2 | `_meta/hcc/build_hcc_register.py` + `recovered-provisions.json` (scris de mână, gol la început); cele 16 marcaje vizibile intră mecanic; al patrulea control din `close_session.py` | validator 0, `--check` curat | **făcut 2026-09-08**: 18 acte, 76 hotărâri, 16 cu articol, 67 fără |
| 5.3 | recuperarea articolului pentru cele ~60 fără marcaj, hotărâre cu hotărâre, prin `fetch` | fiecare rând poartă doc_id-ul versiunii citite | **nu, Cloudflare** |
| 5.4 | integrarea în blocul de acoperire și în validator (D4 i–ii) | regresie pe tot corpusul | da, după 5.2 |
| 5.5 | paginile de entitate ale celor 19 acte, manifestul (secțiune nouă), `index.md` | validator 0, commit | da, după 5.3 |
| 5.6 | text integral pentru hotărârile cu constatare vie, prefix `HCC-` | ingerare pe modelul `ingest_business_law.py`, integritate PASS | **nu, Cloudflare; și numai la cerere** |

Fiecare pas se încheie cu commit propriu și intrare în `log.md`. Pasul 5.3 este cel lung: ~60
de citiri de versiune. Se poate tăia pe acte, în ordinea D3, cu raport după fiecare cod.

## 5. Ce nu acoperă planul

Hotărârile Curții care nu apar în nicio fișă a unui act deținut (de exemplu cele asupra unor legi
neingerate, sau interpretările Constituției neconsemnate în fișa ei). Sesizările respinse. Avizele.
Deciziile de inadmisibilitate. Toate acestea rămân în afara „restrânse la actele din bază".

## 6. Raportul de la sfârșit

1. Tabelul recensământului, înainte și după recuperare: câte hotărâri au articol cunoscut.
2. Lista rândurilor din registru, pe act, cu doc_id-ul versiunii din care a fost citit fiecare.
3. Ce nu s-a putut recupera și de ce.
4. Ieșirea validatorului, cu noul avertisment, și paginile pe care le-a prins, dacă vreuna.
5. Commit-urile.
