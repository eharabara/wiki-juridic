# Plan de extindere: perimetrul de drept intern pentru munca de avocat stagiar

Data: 6 septembrie 2026
Folder vizat: `C:\Users\harab\wiki`
Stare: compoziția aprobată de Eugen la 6 septembrie. Execuția nu a început. Nimic din vault nu a fost modificat de acest plan.
Înlocuiește: secțiunea „Planned extension" din `legal-career/05-knowledge-map.md`, versiunea din 5 septembrie.

---

## 1. Ce s-a decis la 6 septembrie

**D1. Utilizarea wiki-ului pe termen scurt este dreptul intern.** Întrebările vin din munca zilnică de avocat stagiar: drept corporativ și drept administrativ în primul rând, litigii civile și comerciale și contracte în al doilea rând. Apărarea penală este exclusă. Pregătirea pentru examenul de calificare a fost discutată și lăsată deoparte; nu este un scop al wiki-ului.

**D2. Textele integrale ale actelor UE se amână.** Punctul 2 din lista veche coboară la sfârșit. Consecință directă: reverificarea stratului de constatări (punctul 1 vechi) nu mai poate fi făcută complet, pentru că partea UE a comparației rămâne un extras. Deci punctul 1 se restrânge la un control: paginile acquis se marchează ca neverificate, ca să nu mai poată fi citate ca lucru terminat. Nu se reverifică acum.

**D3. Ordinea nouă, după consecință.** (1) înghețarea și marcarea stratului de constatări; (2) sondajul de actualitate pe tot corpusul; (3) Constituția; (4) inelul de legi pentru munca de stagiar, listat mai jos; (5) hotărârile Curții Constituționale, restrânse la actele din bază; (6) după acestea, Acordul de Asociere, textele UE integrale și reverificarea constatărilor acquis.

**D4. Conținutul punctului 4, verificat la 6 septembrie contra tabelului de acoperire generat în aceeași dimineață.** Zece legi din legis.md și trei acte ale Uniunii Avocaților. Lista este în secțiunea 5.

**D5. Actele Uniunii Avocaților se ingerează numai dacă sunt pe legis.md.** Statutul profesiei este acolo (doc_id 86850, identificator SUARM0/2011). Codul deontologic și Regulamentul stagiului se caută. Dacă unul lipsește, se consemnează ca lacună și nu se ingerează de pe uam.md, pentru că nu există control pentru sursa aceea. Regula din CLAUDE.md rămâne: nicio ingerare fără controlul care o acoperă.

**D6. Sondajul de actualitate doar raportează.** Nu reîmprospătează niciun act. Reîmprospătarea distruge marcajele de abrogare ale amendamentelor anterioare (constatarea din 5 septembrie pe `L-234-2016`), deci fiecare reîmprospătare este o decizie separată a lui Eugen, luată pe baza raportului.

---

## 2. Ce acoperă acest plan și ce nu

Acoperă pașii 1 la 4 din D3. Pașii 5 și 6 primesc planuri separate, după ce acesta este executat și raportat.

Nu acoperă: reîmprospătarea vreunui act existent; modificarea textului brut; pagini noi de constatări; copiile din `legal-career/` (se reîmprospătează la închiderea sesiunii, cu `stamp_copies.py`).

---

## 3. Condiții înainte de orice pas

1. `git status` curat pe `main`. Fiecare pas se încheie cu un commit propriu. Push doar când spune Eugen.
2. `python _meta/schema/validate_wiki.py` la zero erori înainte de a începe. Dacă nu este la zero, oprire și raport.
3. `python _meta/coverage/build_coverage.py` rulat, ca tabelul din CLAUDE.md să fie cel de la începutul lucrării.
4. Citite: `SCHEMA.md`, `CLAUDE.md` integral, `raw/papers/moldova-legal/_manifest.md`, `_meta/imports/moldova-legal/ingest_business_law.py` (modelul de ingerare) și `verify_business_law.py`.

---

## 4. Pașii

### Pasul 1. Înghețarea stratului de constatări

Fișiere: cele 17 pagini `concepts/acquis-*.md` și `comparisons/cnpf-transposition-matrix.md`. Total 18.

Ce se face, pentru fiecare:
- `confidence: medium` devine `confidence: low`.
- Se adaugă eticheta `unverified`. Taxonomia este închisă (D4 din 5 septembrie), deci mai întâi se adaugă `unverified` în `_meta/schema/schema-spec.yaml`, la `document_and_knowledge_types`, apoi se regenerează blocul mecanic cu `python _meta/schema/build_schema.py`, apoi se folosește eticheta.
- Sub titlul H1 se inserează un singur paragraf, același în toate: „Neverificat după reconstrucția stratului brut din septembrie 2026. Partea UE a comparației este un extras, nu textul integral. Nu se citează ca o constatare finală." Corpul paginii nu se modifică altfel.
- `updated` devine data zilei.

Ce nu se face: nu se reverifică nicio constatare, nu se rescrie nicio pagină, nu se șterge nimic.

Control: validatorul la zero erori. Intrare în `log.md` de tip `decision`.

### Pasul 2. Sondajul de actualitate pe tot corpusul

Scop: să se afle, pentru fiecare act ingerat, dacă textul din wiki este consolidarea curentă de pe legis.md. Testul sistematic nu a fost rulat niciodată; până acum s-a verificat act cu act, la nevoie.

Perimetru: toate fișierele cu `doc_id` din `raw/papers/cnpf/`, `raw/papers/moldova-legal/`, `raw/papers/bnm/legal-ro/`. Fișierele `UE-*` și cele cu `source_type: translation` se sar.

Metodă, pentru fiecare act:
1. Se citește `doc_id` și data consolidării din frontmatter.
2. Se interoghează istoricul de versiuni al actului pe legis.md, prin mecanismul consemnat în CLAUDE.md la „Open questions", punctul 3 (`showDetails(null,'<doc_id>')`, textul unei versiuni la `/cautare/showdetails/<doc_id>`). Se ia cel mai recent doc_id și data lui.
3. Se compară. Patru stări posibile: **curent** (wiki = legis.md); **wiki în urmă** (legis.md are o consolidare mai nouă); **legis.md în urmă** (wiki aplică un amendament pe care consolidarea legis.md nu îl poartă încă, cazul Codului civil cu LP251/2025); **nerezolvat** (interogarea nu a răspuns sau răspunsul nu se poate citi).
4. Pentru starea „wiki în urmă" se notează și legea de modificare care a produs consolidarea nouă, ca Eugen să poată judeca dacă reîmprospătarea merită pierderea marcajelor.

Un control suplimentar, cerut în documentul 05: `build_coverage.py` sare actele al căror `latest_modification_line` începe cu „Publicat", tratându-le ca nemodificate. Se listează separat actele sărite astfel și se verifică pentru fiecare, prin aceeași interogare, dacă într-adevăr nu au fost modificate.

Rezultat: `_meta/coverage/currency-sweep-2026-09-DD.md` (tabel: act, doc_id wiki, consolidare wiki, doc_id curent legis.md, consolidare curentă, stare, lege de modificare) și `currency-sweep-2026-09-DD.json` cu aceleași date. Nimic altceva nu se modifică. Interdicția din D6 se respectă strict.

Control: raportul se trimite lui Eugen înainte de pasul 3. Reîmprospătările, dacă vor fi, se decid una câte una și se execută cu arhivarea versiunii anterioare în `_archive/`, cu marcajele ei, înainte de suprascriere.

### Pasul 3. Constituția

Nivelul 1 al ierarhiei surselor din documentul 03, absent din bază.

- Se caută pe legis.md doc_id-ul consolidării curente a Constituției Republicii Moldova din 29 iulie 1994 (republicată). Se verifică titlul și data pe pagină, nu din lista de rezultate.
- Identificator brut: `CONST-1994`. Prefix nou; se consemnează în `raw/papers/moldova-legal/_manifest.md` la momentul ingerării. Destinație: `raw/papers/moldova-legal/CONST-1994.md`.
- Ingerare pe modelul `ingest_business_law.py` (intrare în dicționar, aceleași câmpuri de frontmatter, sha256 pe corp, `source_type: legal-text`, `language: ro`). Ancore `## Articolul N` la nivel de articol; Constituția are 143 de articole și dispoziții finale și tranzitorii numerotate separat, care se ancorează la fel. Verificare cu `verify_business_law.py` sau echivalentul lui pentru un act.
- Rând în manifest, pagină `entities/CONST-1994.md` cu `perimeter: legal`, intrare în `index.md`, `build_coverage.py`, `build_inforce_register.py`, validator la zero.

### Pasul 4. Inelul de legi pentru munca de stagiar

Trei loturi. Fiecare lot se încheie cu manifest, pagini de entitate, index, coverage, registrul in-force, validator la zero și commit. Lotul următor nu începe până lotul curent nu trece validatorul.

Pentru fiecare act: doc_id-ul se găsește prin căutare pe legis.md și se verifică pe pagina actului că este consolidarea curentă (nu prima publicare). Dacă data consolidării este în viitor, registrul in-force o preia; se semnalează în raport. Se verifică modelul de numerotare a articolelor înainte de ancorare (capcana `54^1/1` din Codul fiscal, consemnată în CLAUDE.md).

**Lotul A, corporativ.** Destinație `raw/papers/moldova-legal/`.

| ID brut | Act | doc_id |
|---|---|---|
| `L-149-2012` | Legea insolvabilității nr. 149/2012 | de găsit |
| `L-160-2011` | Legea nr. 160/2011 privind reglementarea prin autorizare a activității de întreprinzător | de găsit |
| `L-131-2012` | Legea nr. 131/2012 privind controlul de stat asupra activității de întreprinzător | de găsit |

**Lotul B, administrativ.** Destinație `raw/papers/moldova-legal/`.

| ID brut | Act | doc_id |
|---|---|---|
| `L-436-2006` | Legea nr. 436/2006 privind administrația publică locală | de găsit |
| `L-158-2008` | Legea nr. 158/2008 cu privire la funcția publică și statutul funcționarului public | de găsit |
| `L-148-2023` | Legea nr. 148/2023 privind accesul la informațiile de interes public | de găsit |
| `L-131-2015` | Legea nr. 131/2015 privind achizițiile publice | de găsit |

**Lotul C, profesia.** Destinație `raw/papers/moldova-legal/`. Prefix nou `UA-` pentru actele Uniunii Avocaților; se consemnează în manifest.

| ID brut | Act | doc_id |
|---|---|---|
| `L-1260-2002` | Legea nr. 1260/2002 cu privire la avocatură | de găsit |
| `L-198-2007` | Legea nr. 198/2007 cu privire la asistența juridică garantată de stat | de găsit |
| `L-514-1995` | Legea nr. 514/1995 privind organizarea judecătorească | de găsit |
| `UA-STATUT-2011` | Statutul profesiei de avocat | 86850, de confirmat pe pagină |
| `UA-DEONTOLOGIC-AAAA` | Codul deontologic al avocaților | de căutat; dacă lipsește, lacună (D5) |
| `UA-STAGIU-AAAA` | Regulamentul privind efectuarea stagiului profesional | de căutat; dacă lipsește, lacună (D5) |

Actele Uniunii pot fi structurate pe articole sau pe puncte. Dacă sunt pe puncte, se tratează ca hotărârile de Guvern: fără ancore de articol, cu nota „numbered points, not articles" în coverage, și se consemnează că citarea se face pe punct. Registrul in-force nu citește acte pe puncte (limita din documentul 05), deci dispozițiile amânate, dacă există, se notează manual în manifest.

Deja în bază, nu se reingerează: 220/2007, 845/1992, 135/2007, 183/2012, 235/2006, 100/2017, 239/2008, 1134/1997, toate codurile.

---

## 5. Raportul de la sfârșit

Ce se trimite în Cowork după execuție, în ordinea aceasta:
1. Tabelul sondajului de actualitate, cu numărul de acte pe fiecare stare.
2. Lista doc_id-urilor găsite pentru cele 14 acte, cu data consolidării fiecăruia.
3. Ce nu s-a găsit pe legis.md (D5) și ce a fost consemnat ca lacună.
4. Ieșirea validatorului și diferența din tabelul de acoperire (înainte și după).
5. Orice anomalie de numerotare, orice consolidare în viitor, orice articol absent fără marcaj.
6. Lista commit-urilor.

După raport, documentul 05 din proiect se actualizează din nou, iar copiile din `legal-career/` se reîmprospătează la închiderea sesiunii.
