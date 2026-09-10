# Manifest de surse — Acte normative transversale Moldova

> Surse legis.md păstrate în afara subfolderului CNPF, pentru acte de cadru general sau acte sectoriale care pot deveni relevante în analize de politici publice, administrare publică, reglementare, reformă și transpunerea acquis-ului UE.

## A. Source pack minim pentru transpunere UE

| ID raw | doc_id | Titlu detectat | Pagină wiki | Consolidare / versiune locală | Rol operațional |
|---|---:|---|---|---|---|
| `L-100-2017` | **153007** | LEGE Nr. 100 din 22.12.2017 cu privire la actele normative | [[L-100-2017]] | **2025-12-31** | cadrul procedural general: nota de fundamentare, proiecte cu relevanță UE, tabel concordanță, expertiză compatibilitate |
| `HG-1171-2018` | 144185 | HOTĂRÂRE Nr. 1171 din 28.11.2018 pentru aprobarea Regulamentului privind armonizarea legislației Republicii Moldova cu legislația Uniunii Europene | [[HG-1171-2018]] | 2024-07-05 | regulamentul metodologic corect pentru armonizarea legislației Republicii Moldova cu legislația UE |

## B. Surse adăugate literal / delimitare

| ID raw | doc_id | Titlu detectat | Pagină wiki | Consolidare / versiune locală | Observație |
|---|---:|---|---|---|---|
| `HG-1170-2016` | **144537** | HOTĂRÂRE Nr. 1170 din 25.10.2016 pentru aprobarea Regulamentului cu privire la modul de transmitere, schimbare a destinaţiei şi schimb de terenuri | [[HG-1170-2016]] | **2025-03-07** | tratată literal din solicitarea inițială; nu este regulamentul de armonizare UE; **abrogată integral de la 07.03.2025 prin pct. 3 din HG553/2024**, verificat pe text (U.6); succesoarea `HG-553-2024` acoperă doar schimbarea destinației |

## C. Codul civil — sursă transversală de drept privat

| ID raw | doc_id | Titlu detectat | Pagină wiki | Consolidare / versiune locală | Rol operațional |
|---|---:|---|---|---|---|
| `CC-1107-2002` | — | COD Nr. CC1107/2002 din 06.06.2002 — Codul civil al Republicii Moldova | [[CC-1107-2002]] | copie PDF consolidată furnizată la 2026-07-13; antetul indică LP251/2025 în vigoare din 01.04.2026 | cadru transversal pentru raporturi civile, consumatori/profesioniști, persoane, bunuri, obligații, succesiuni și drept internațional privat |

**Articole detectate: 2 657** (numerotare 1–2671, 14 numere abrogate). Ancorat la nivel
de articol la **2026-09-04** — detalii în C.1, constatările de abrogare în C.2.

### C.1. Ancorare la nivel de articol — CC-1107-2002 (2026-09-04)

Fișierul a fost ancorat la nivel de articol la **2026-09-04**. Textul extras nu a fost
modificat: titlurile Markdown sînt **inserate deasupra** liniilor originale, iar corpul
rămîne identic octet cu octet față de `sha256_pre_anchoring`.

> **Atenție:** verificarea „șterge toate liniile care încep cu `#` și compară" a fost valabilă
> doar imediat după această primă trecere. Fișierul a trecut ulterior prin reunirea liniilor (C.4),
> eliminarea titlurilor de articol duplicate (C.5) și eliminarea duplicatelor structurale (C.6).
> Verificarea curentă, care le desface pe toate patru, este
> `_meta/imports/anchoring/verify_chain.py`.

| Nivel structural | Ancore inserate | Formă |
|---|---:|---|
| Cartea | 5 | `## Cartea a doua` |
| Titlul | 22 | `## Titlul I` |
| Capitolul | 109 | `## Capitolul I` |
| Secțiunea | 172 | `### Secțiunea a 2-a. <titlu>` |
| Subsecțiunea | 17 | `#### Subsecțiunea 1. <titlu>` |
| § | 56 | `##### § 1. <titlu>` |
| **Articolul** | **2 657** | `## Articolul 512. <titlu>` |
| **Total** | **3 038** | — |

Observații de extracție, relevante pentru citare:

- Numerotarea articolelor este **1–2671, strict crescătoare, fără duplicate**; cele 14
  numere absente sînt abrogări reale (vezi C.2). Nu există articole cu exponent
  (`146¹`) în acest act, deci defectul de tip „superscript aplatizat" nu apare aici.
- Marcajele `Titlul` apar în PDF cu spațiere între litere (`T i t l u l I`). Ancora
  inserată normalizează forma; linia-sursă rămîne neatinsă.
- Fișierul folosește **două codificări de diacritice** (cedilă `ţ` U+0163 și virgulă
  jos `ț` U+021B). Ambele sînt recunoscute la ancorare; o căutare cu o singură formă
  pierde 68 de titluri structurale.
- `Articolul 723`: extracția PDF a unit sfîrșitul titlului cu începutul dispoziției pe
  aceeași linie fizică. Ancora a fost corectată manual la
  „…drepturile și obligațiile părților la contractul de gaj"; linia-sursă rămîne
  nemodificată. Este singurul caz de acest tip din act.
- Corpul a fost **reunit** printr-o a doua trecere, în aceeași zi — vezi C.4.
- `sha256` pentru acest fișier se calculează pe **octeții bruți** de după `---`
  (CRLF păstrat), spre deosebire de restul corpusului, care normalizează CRLF→LF.
  Convenția este consemnată explicit în frontmatter ca `sha256_convention: raw`.

### C.2. Articole absente din CC-1107-2002 — constatări de abrogare

Toate cele 14 numere absente sînt explicate. Niciun articol nu a fost inventat și
nicio numerotare nu a fost modificată.

| Articole absente | Temei constatat în text | Sursa marcajului |
|---|---|---|
| 2171, 2172, 2185, 2188, 2404, 2485 | `[Art.NNNN abrogat prin LP251 din 10.07.25, MO417-419/06.08.25 art.569; în vigoare 01.04.26]` | marcaj individual, prezent în text |
| 2047–2054 (8 articole) | `Secțiunea a 3-a- abrogată` — abrogare la nivel de secțiune, fără marcaje individuale | marcaj de secțiune; **fără citare LP în text** `[de verificat]` |

> Atenție la citare: pentru blocul 2047–2054, actul de abrogare nu este identificat în
> textul consolidat furnizat. Temeiul trebuie confirmat din legis.md înainte de a fi
> invocat într-o analiză.

### C.4. Reunirea liniilor din Codul civil (2026-09-04, a doua trecere)

Extracția PyMuPDF rupsese textul la ~92 de coloane, indiferent de frază. A doua trecere reunește
liniile. Este singura operațiune din întreaga lucrare care atinge textul propriu-zis, așa că
garanția este formulată la nivel de caracter:

> **Se schimbă doar spații albe.** Fiecare reunire înlocuiește o întrerupere de linie cu un
> singur spațiu. Niciun alt caracter nu a fost adăugat, șters sau reordonat.

Dovada: se elimină toate caracterele de spațiu alb din corpul rezultat (fără titlurile inserate)
și din corpul **anterior ancorării**, iar cele două se compară octet cu octet. Verificarea trece
peste **ambele** treceri deodată — inserarea titlurilor și reunirea liniilor — și confirmă
1 859 072 de octeți ne-spațiu identici cu extracția originală.

| Măsură | Înainte | După |
|---|---:|---:|
| Linii ne-goale în corp | 30 041 | 12 979 |
| Întreruperi de linie eliminate | — | 17 062 |
| Fraze rupte la mijloc | 16 878 | **213** (−98,7%) |
| Lungime mediană a liniei | 82 | 127 |

Regula. Nu se folosește lungimea liniei: lățimea de rupere nu are prag curat — lungimile formează
o pantă continuă între 80 și 98 de caractere, iar 727 de linii de peste 88 de caractere încheie un
paragraf, în timp ce 13 068 mai scurte continuă. În loc de asta, o linie se reunește cu următoarea
doar dacă este **neterminată gramatical** — fără punctuație de final, sau terminată într-o
abreviere juridică precum `art.`, `alin.`, `lit.` (98 de cazuri) — **și** următoarea linie nu
începe o unitate nouă (`(1)`, `a)`, `[`, `Articolul`, marcaj structural).

Consecință deliberată: acolo unde o frază s-a terminat exact la punctul de rupere, linia rămâne
separată. Fiecare linie rezultată este deci cel puțin o frază întreagă, iar **două paragrafe nu
sunt niciodată contopite**.

Titlurile de articol se reunesc **exact cât spune ancora**, nu mai mult: 2 656 din 2 657 de titluri
se închid la limita înregistrată în `## Articolul N.`, ceea ce ține dispoziția în afara titlului
(art. 23 este cazul-tip). Singura excepție este **art. 723**, unde extracția a pus sfârșitul
titlului și începutul dispoziției pe aceeași linie fizică — vezi C.1.

Cele 213 rupturi rămase sunt corecte: enumerări care se încheie cu `; sau` / `; și` înaintea unui
punct `b)`, marcaje structurale urmate de titlul lor, și preambulul (datele de publicare și lista
legilor modificatoare), lăsat neatins intenționat — sunt coloane de linii scurte care nu trebuie
alipite.

### C.5. Eliminarea titlurilor duplicate (2026-09-04, a treia trecere)

După reunire, titlul fiecărui articol exista de două ori: o dată ca ancoră inserată, o dată ca
linie de corp imediat dedesubt, identice octet cu octet. Copia din corp a fost ștearsă:
**2 656 de linii eliminate**, corpul scăzând de la 17 009 la 14 353 de linii.

Este singura trecere care **șterge** text, deci regula este îngustă și reversibilitatea este
demonstrată, nu afirmată:

- o linie se șterge **doar** dacă este identică octet cu octet cu ancora imediat de deasupra și
  doar dacă este linia imediat următoare;
- reinserarea textului fiecărei ancore ca linie de corp reproduce corpul anterior ștergerii,
  octet cu octet — verificat;
- **art. 723 nu a fost deduplicat**: extracția i-a pus sfârșitul titlului și începutul dispoziției
  pe aceeași linie fizică, deci linia de corp conține text pe care ancora nu îl are.

**Lanțul complet de proveniență.** Scriptul `verify_chain.py` desface toate cele trei treceri în
ordine inversă — reinserează titlurile, elimină ancorele, normalizează spațiul alb — și compară cu
extracția originală: **1 859 072 de octeți ne-spațiu, sha256
`124bd2b606868231835c0a85b614f72196c717467df9ba40d78c50c9ece3504d`, identic**. Niciun caracter de
text juridic nu s-a schimbat de la extracția din 2026-07-13.

Frontmatterul păstrează lanțul: `source_file_sha256` → `sha256_pre_anchoring` →
`sha256_pre_unwrap` → `sha256_pre_dedup` → `sha256`.

### C.6. Eliminarea duplicatelor structurale (2026-09-04, a patra trecere)

Aceeași regulă de potrivire exactă, aplicată celor trei niveluri structurale a căror linie-sursă
era o copie a ancorei: **170 de linii eliminate** — `Cartea` (5), `Capitolul` (109), `§` (56).
Corpul a scăzut de la 14 353 la 14 183 de linii.

**Reparație colaterală: 5 ancore `§` erau trunchiate.** Prima trecere de ancorare a luat linia `§`
ca atare, dar PDF-ul rupsese titlul paragrafului pe două linii, deci ancora păstra doar prima
parte, în timp ce corpul (după reunire) avea titlul întreg. Ancorele au fost **completate din linia
de corp** înainte ca aceasta să fie ștearsă, deci nu s-a pierdut text, iar ancora nu mai
sub-raportează titlul. Exemplu: `§ 3. Ocrotirea intereselor personale` →
`§ 3. Ocrotirea intereselor personale nepatrimoniale`.

Trei niveluri **nu** au fost atinse, fiindcă ancora lor nu este o copie a liniei de dedesubt:

- **`Titlul` (22)** — ancora normalizează `T i t l u l I` la `Titlul I`; ștergerea liniei-sursă ar
  pierde forma cu spațiere din PDF.
- **`Secțiunea` (172)** și **`Subsecțiunea` (17)** — ancora unește marcajul cu titlul
  (`### Secțiunea a 2-a. <titlu>`), pe când corpul le ține pe linii separate.

Într-o trecere finală a fost eliminat și ultimul duplicat exact: `### Secțiunea a 3-a- abrogată`,
singura secțiune fără titlu propriu, deci singura al cărei ancoră coincidea cu linia-sursă.

**Nu mai există niciun duplicat exact în fișier.** Total, după cele cinci treceri: 3 038 de ancore
intacte, corpul de la 31 785 la 14 182 de linii.

> **Notă tehnică, pentru cine repetă operațiunea.** Fiecare rulare trebuie să consemneze hash-ul
> anterior sub o cheie **distinctă**. La a doua rulare a `dedup_structural.py` cheia
> `sha256_pre_dedup_structural` s-ar fi repetat, iar YAML păstrează doar ultima valoare — veriga
> intermediară ar fi dispărut tăcut din lanț. Scriptul are acum o aserțiune care refuză o etapă
> deja folosită și cere `--stage`.

### C.7. Trecerea pe textul legis.md — doc_id 150498 (2026-09-06, seara)

La decizia lui Eugen, fișierul brut nu mai este transcrierea PDF-ului, ci extracția legis.md a
consolidării **150498 @ 2026-04-01** (LP251 din 10.07.25), adusă prin
`_meta/imports/moldova-legal/refresh_behind_2026-09-06.py`, lotul `moldova-legal-cc`, cu lanțul de
proveniență în frontmatter (`doc_id_previous: 150561`, `sha256_previous`, `archived_previous_at`).
Versiunea din PDF, cu toate trecerile C.1–C.6, este arhivată la
`_archive/raw/moldova-legal-cc-legis-md-before-refresh-20260906-221637/CC-1107-2002.md`; PDF-ul
original rămâne la `raw/assets/moldova-legal/CC-1107-2002-2026-07-12.pdf`. Rândul din tabelul C
de mai sus („copie PDF consolidată") descrie de acum versiunea arhivată.

Ce s-a verificat: inventarul de articole este **identic** (2.657 de articole, aceleași 14 numere
absente: 2047–2054 și cele șase abrogate prin LP251), integritatea textului față de HTML este PASS
pe 14.148 de linii, cele 29 de marcaje `[Art.NNNN abrogat prin LP...]` sunt aceleași. Structura:
5 ancore de carte, 22 de titlu, 109 de capitol, 172 de secțiune, 2.968 de titluri Markdown în
total (față de 3.038 în versiunea ancorată manual, care avea și subsecțiuni și paragrafe `§`).

Două lucruri de metodă. Prima trecere pierduse cele 27 de ancore de carte și de titlu: legis.md
scrie cărțile „Cartea întâi", „Cartea a doua", fără numeral, și titlurile cu litere spațiate,
„T i t l u l IV", forme pe care regula `TITLUL|Titlul + numeral roman` nu le prindea. Regula a
fost adăugată în `extract_doc`, regresia a fost verificată pe toate celelalte acte din `DOCS`
(un singur act ar câștiga ancore: `COD-218-2008`, „Cartea întâi" și „Cartea a doua", neaplicat,
fiindcă acel fișier nu a fost reingerat), versiunea din PDF a fost pusă la loc din arhivă și
trecerea repetată. Al doilea: blocul art. 2047–2054 stă și în textul legis.md sub aceeași linie
`Secțiunea a 3-a- abrogată`, fără citare LP, deci întrebarea deschisă 1 din `CLAUDE.md` nu era
un defect al PDF-ului.

## C.3. Articole cu exponent — L-100-2017 (2026-09-04)

Extracția a aplatizat exponentul la două articole din `L-100-2017`. Ancorele au fost
normalizate; se schimbă un singur token pe linia de titlu, restul fișierului rămâne
identic octet cu octet.

| Stocat ca | Normalizat | Poziție | Art. de bază |
|---|---|---|---|
| 271 | **27^1** | între art. 27 și 28 | prezent |
| 701 | **70^1** | între art. 70 și 71 | prezent |

- **Corectat 2026-09-04.** Dovada a fost consemnată aici drept „exclusiv pozițională",
  pe motiv că fișierul nu conține forma `Art.70^1`, niciun exponent Unicode și nicio notă
  de amendament. Afirmația este corectă despre fișierul `.md` și greșită despre sursă:
  HTML-ul legis.md pentru doc_id 144467 marchează `Articolul 27<sup>1</sup>` și
  `Articolul 70<sup>1</sup>`. Aplatizarea se produce la extracție, fiindcă
  `text_content()` lipește cifrele. Ambele normalizări sînt deci **confirmate din marcaj**,
  nu doar deduse, și coincid cu ce stabilise raționamentul pozițional. Constatarea
  `[de verificat]` pe acest punct se închide.
- **Reîmprospătat 2026-09-04** la consolidarea curentă, doc_id **153007**, **2025-12-31**
  (anterior 144467, 2024-08-02). Textul nou rezolvă exponenții la sursă (`<sup>` → `^N`),
  deci `27^1` și `70^1` vin direct din marcaj. Articole: 77 de bază + 2 cu exponent.
- **Lacune de numerotare:** art. **33 există** în consolidarea curentă — absența lui din
  versiunea 2024 era vechime, nu gol inexplicabil. Rămân absente art. **25, 26 și 52**,
  fără marcaj de abrogare în text. `[de verificat]`
- **Lacune de numerotare neexplicate:** art. **25, 26**, **33** și **52** lipsesc. Fișierul
  nu conține niciun marcaj de abrogare pentru ele — mențiunile „abrogat" din text sunt
  dispoziții de fond despre procedura de abrogare, nu marcaje. `[de verificat]` față de
  legis.md.

## E. Drept corporativ — L-135/2007, L-220/2007 și L-845/1992 (ingerate 2026-09-04)

Cele trei legi indicate în documentul 04 ca surse de bază pentru persona P1 și care lipseau din
wiki. Primele două lipseau de la eșecul descărcării din 13 iulie 2026; a treia, 845/1992, nu
figurase niciodată în acel plan. Vezi `_meta/plans/2026-09-04-lacuna-drept-afaceri.md`. Plasate
aici, nu în `cnpf/`, fiindcă sînt drept societar general, nu perimetru CNPF/BNM. **Cu 845/1992,
acoperirea personei P1 este completă: cinci din cinci surse.**

| ID raw | doc_id | Titlu detectat | Pagină wiki | Consolidare | Articole |
|---|---:|---|---|---|---|
| `L-135-2007` | 153674 | LEGE Nr. 135 din 14-06-2007 privind societăţile cu răspundere limitată | [[L-135-2007]] | 2026-03-27 (LP41 din 26.03.26) | 83 de bază + 10 cu exponent |
| `L-220-2007` | 155438 | LEGE Nr. 220 din 19-10-2007 privind înregistrarea de stat a persoanelor juridice şi a întreprinzătorilor individuali | [[L-220-2007]] | 2026-07-23 (LP76 din 02.07.26) | 38 de bază + 6 cu exponent |
| `L-845-1992` | 155963 | LEGE Nr. 845 din 03-01-1992 cu privire la antreprenoriat şi întreprinderi | [[L-845-1992]] | **2027-01-01** ⚠ viitoare | 35 de bază + 11 cu exponent |

### E.1. Metoda de ingerare și diferența față de corpusul CNPF

Script: `_meta/imports/moldova-legal/ingest_business_law.py`. Verificare:
`verify_business_law.py`, în același folder. HTML-ul sursă este păstrat în
`_meta/imports/moldova-legal/legis-md-business/`.

Convențiile de format sînt cele din scriptul CNPF. **O singură diferență de fond:** exponenții
din HTML sînt rezolvați *înainte* de extracția textului, prin `resolve_superscripts()`. legis.md
îi marchează `<sup>1</sup>`; dacă se lasă așa, `text_content()` lipește cifrele și
„Articolul 27¹" devine „Articolul 271", iar „alin. (1¹)" devine „alin. (11)". Ambele sînt citări
false. Aici `<sup>N</sup>` devine `^N` **peste tot**, în toate cele patru roluri: titluri de
articol, numere de alineat, litere de punct, trimiteri la capitole.

> **Costul asumat al deciziei.** Celelalte fișiere raw au exponenții de articol normalizați, dar
> pe cei de alineat și de literă încă aplatizați. Aceste două fișiere sînt deci corecte și
> diferite de restul corpusului: o căutare după `alin. (11)` găsește fișierele vechi, nu și pe
> acestea. Decizia a fost luată explicit la 2026-09-04, preferând fidelitatea consecvenței.

Exponenți păstrați în corp, în afara titlurilor de articol: **17** în L-135-2007 și **60** în
L-220-2007.

### E.2. Dovada că textul nu a fost atins

Verificarea desface structura adăugată și compară restul cu extracția simplă din același HTML:
se scot prefixele `##` și `###` de pe liniile de titlu, se elimină liniile goale, iar rezultatul
se compară linie cu linie.

| Fișier | Linii scrise | Linii de referință | Rezultat |
|---|---:|---:|---|
| `L-135-2007` | 667 | 667 | identice |
| `L-220-2007` | 532 | 532 | identice |
| `L-845-1992` | 447 | 447 | identice |

Ancorele de exponent coincid cu marcajul `<sup>` din sursă: 10 din 10 pentru L-135-2007,
6 din 6 pentru L-220-2007. Numerotarea articolelor de bază nu are duplicate în niciunul.

### E.3. Constatări `[de verificat]` — L-220-2007

Două anomalii sînt **în sursa legis.md**, nu introduse la ingerare. Verificat la 2026-09-04 direct
în HTML. Textul a fost reprodus fidel, fără corectură tăcută.

| Constatare | Ce arată sursa |
|---|---|
| **Art. 6 lipsește** | Numerotarea trece de la art. 5 la art. 7. Niciun marcaj `abrogat` pentru art. 6 și nicio trimitere la el, deși actul conține 25 de alte mențiuni „abrogat". Aceeași clasă de defect ca art. 21 din L-192-1998. |
| **Art. 5 începe la alin. (2)** | Sub titlul „Termenele înregistrării de stat", prima unitate este `(2)`. Alineatul (1) nu apare în sursă. |

L-135-2007 nu are lacune de numerotare: 1–83, complet.

### E.4. L-845/1992 — constatări proprii

**Consolidare viitoare.** `consolidation_date: 2027-01-01`, ulterioară zilei de azi. O singură
dispoziție este afectată: art. 36^1 pct. 4 lit. l), introdusă prin LP171 din 30.07.26,
MO386-389/21.08.26 art.412, în vigoare 01.01.2027. Restul textului este în vigoare astăzi.
Detectarea este automată de la 2026-09-04: `future_pending()` din scriptul de ingerare marchează
situația în antet și în frontmatter (`consolidation_is_future: true`), deci se va repeta corect la
orice act viitor.

**Arts. 21 și 31 lipsesc fără temei în sursă.** `[de verificat]` Numerotarea trece de la 20 la 22
și de la 30 la 32. Verificat direct în HTML: nu apar nicăieri, iar textul art. 20 curge în art. 22.
Actul distinge cele două situații, fiindcă pentru arts. 35 și 36 păstrează marcajul `- abrogat.`.
Aceeași clasă cu art. 21 din L-192-1998 și art. 6 din L-220-2007.

**Structură neobișnuită.** Două capitole cu exponent, VI^1 și VI^2, și un bloc de opt articole cu
exponent, 36^1–36^8, care sînt de fapt două regimuri întregi adăugate ulterior: antreprenoriatul
social (36^1–36^5) și monopolul fiscal (36^6–36^8). Aplatizate, ar fi apărut ca „art. 368" într-un
act cu 37 de articole.

## F. Coduri — Codul fiscal și Codul administrativ (ingerate 2026-09-04)

Ultimele două lipsuri semnalate în `_meta/plans/2026-09-04-lacuna-drept-afaceri.md`.

| ID raw | doc_id | Titlu detectat | Pagină wiki | Consolidare | Ancore de articol |
|---|---:|---|---|---|---:|
| `COD-1163-1997` | 155071 | COD Nr. 1163 din 24-04-1997 — Codul fiscal | [[COD-1163-1997]] | 2026-06-25 | 512 (353 de bază + 159 cu exponent) |
| `COD-116-2018` | 150447 | COD Nr. 116 din 19-07-2018 — Codul administrativ | [[COD-116-2018]] | 2025-08-31 | 260 (258 + 2) |

Integritate dovedită prin aceeași metodă: 6.916 și 1.447 de linii, identice cu extracția simplă
din același HTML. Niciuna dintre cele două consolidări nu este viitoare.

### F.1. Cuprinsul Codului fiscal nu este ancorat

Codul fiscal poartă un `C U P R I N S` de circa 780 de linii care repetă fiecare titlu de articol
înaintea corpului. Ancorat, ar fi produs **circa 350 de ancore duplicate**, iar o citare `art. N`
ar fi devenit ambiguă între cuprins și corp.

Regula adoptată: **cuprinsul nu se șterge**, textul rămâne neatins, dar ancorarea este suprimată
între marcajul `CUPRINS` și formula de adoptare `Parlamentul adoptă prezentul cod.`. Suprimarea se
aplică numai când ambele repere există, în această ordine, deci nu afectează actele fără cuprins.
Codul administrativ nu are cuprins și nu este atins de regulă.

Rezultatul: **fiecare ancoră din fișier este unică**, verificat. Numerotarea articolelor este
continuă între titluri, nu repornește, deci `art. N` identifică un singur articol.

### F.2. `art. 54^1/1`, o formă unică în corpus

Sursa scrie `Articolul 54<sup>1</sup>/1`, adică un articol distinct de `54^1`. Este singurul caz
din corpus cu bară după exponent. Prima verificare l-a raportat drept duplicat al lui `54^1`,
fiindcă regexul de control se oprea la exponent; controlul a fost corectat, nu ancora.

### F.3. Constatare `[de verificat]` — Codul fiscal

**26 de articole absente, explicate doar la nivel de capitol, fără citare LP.**

| Articole absente | Marcaj în text |
|---|---|
| 208–213 | `Capitolul 10 - abrogat.` |
| 315–334 | `Capitolul 5 - abrogat.` … `Capitolul 8 - abrogat.` |

Abrogarea este consemnată, deci lacunele nu sînt inexplicabile, dar actul de abrogare nu este
identificat în text. Aceeași clasă cu blocul 2047–2054 din Codul civil. Codul administrativ nu are
lacune: 1–258 complet.

## G. Celelalte șapte coduri (ingerate 2026-09-04)

Ultimele acte din planul eșuat de la 13 iulie 2026. **Toate cele 11 sînt acum în wiki.**

| ID raw | doc_id | Act | Pagină | Consolidare | Ancore |
|---|---:|---|---|---|---:|
| `COD-225-2003` | 152860 | Codul de procedură civilă | [[COD-225-2003]] | 2025-12-30 | 536 (459 + 77) |
| `COD-443-2004` | 156146 | Codul de executare | [[COD-443-2004]] | **2026-12-02** ⚠ viitoare | 361 (325 + 36) |
| `COD-95-2021` | 154350 | Codul vamal | [[COD-95-2021]] | 2026-09-01 | 472 (421 + 51) |
| `COD-154-2003` | 155882 | Codul muncii | [[COD-154-2003]] | **2027-01-01** ⚠ viitoare | 416 (364 + 52) |
| `COD-218-2008` | 155852 | Codul contravențional | [[COD-218-2008]] | **2026-09-13** ⚠ viitoare | 737 (483 + 254) |
| `COD-985-2002` | 156133 | Codul penal | [[COD-985-2002]] | **2026-12-02** ⚠ viitoare | 566 (388 + 178) |
| `COD-122-2003` | 156138 | Codul de procedură penală | [[COD-122-2003]] | **2026-12-02** ⚠ viitoare | 658 (553 + 105) |

Integritatea textului dovedită pentru toate șapte, linie cu linie: 3.308, 2.762, 3.913, 3.019,
6.172, 4.629 și 5.787 de linii, identice cu extracția simplă din același HTML. Niciun act nu are
ancore duplicate. Niciunul nu are cuprins, deci regula din F.1 nu se activează.

### G.1. ⚠ Cinci din șapte sînt consolidări viitoare

Două pachete de reformă adoptate în aceeași zi, **30 iulie 2026**, ating cinci coduri deodată, cu
intrare în vigoare eșalonată. legis.md servește deja textul de după, deci fișierele arată dispoziții
care **nu sînt încă în vigoare**.

| Act | Cod atins | În vigoare | Dispoziții |
|---|---|---|---:|
| LP154 din 30.07.26 | Codul contravențional | 13.09.2026 | 7 |
| LP154 din 30.07.26 | Codul muncii | 01.01.2027 | 1 |
| LP172 din 30.07.26 | Codul de executare | 02.12.2026 | 12 |
| LP172 din 30.07.26 | Codul penal | 02.12.2026 | 8 |
| LP172 din 30.07.26 | Codul de procedură penală | 02.12.2026 | 26 |

Fiecare fișier poartă avertismentul în antet, lista dispozițiilor afectate și
`consolidation_is_future: true` în frontmatter. Codul de procedură penală este cel mai atins, cu
26 de dispoziții, între care măsurile preventive, arts. 177–180 și 191.

### G.2. Titluri scrise cu litere distanțate

Codul muncii (13 titluri) și Codul de executare (3) poartă forma `T i t l u l X`, moștenită din
procesarea sursei, aceeași ca la Codul civil. Regula de ancorare a fost extinsă să o recunoască,
**cerând cifră romană după cuvânt**, altfel o frază care începe cu „Titlul executoriu" din Codul
de executare ar fi primit ancoră de titlu. Linia-sursă nu este normalizată, deci o căutare după
„Titlul X" nu găsește aceste titluri; se caută forma distanțată.

### G.3. Lacune de numerotare — ce este explicat și ce nu

Marcajele de abrogare apar în trei forme: individuală, de interval (`Articolul 397- 422 –
abrogate.`) și la nivel de capitol sau secțiune.

| Cod | Absente | Temei | Stare |
|---|---|---|---|
| Codul de procedură civilă | 28–31 | `Capitolul III – abrogat.` | explicat |
| Codul de procedură civilă | 78 | `Aricolul 78. – abrogat.` | explicat, dar vezi G.4 |
| Codul de procedură civilă | 397–422 | marcaj de interval | explicat |
| Codul vamal | 305–310 | `Secțiunea a 3-a - abrogată.` | explicat, fără citare LP |
| Codul muncii | 374–382 | marcaj de interval | explicat |
| Codul de procedură penală | 452–457 | `Secțiunea 1 - abrogată.` | explicat |
| Codul de procedură penală | 463–465 | marcaj de interval | explicat |
| **Codul muncii** | **226–244** | niciunul | **`[de verificat]`**, 19 articole |
| **Codul contravențional** | **441** | niciunul | **`[de verificat]`**, numerotarea merge 440, 440^1, 442 |

Codul de executare și Codul penal nu au nicio lacună.

### G.4. Greșeală de tipar în sursă — Codul de procedură civilă art. 78

Marcajul de abrogare este scris `Aricolul 78. – abrogat.`, fără „t". Abrogarea este deci
consemnată, dar linia **nu primește ancoră de articol**, fiindcă nu se potrivește formei
`Articolul N`. Nu am corectat-o: regula folderului interzice rescrierea textului legal. Consecința
practică: o căutare după `## Articolul 78` în acest fișier nu întoarce nimic, iar art. 78 apare ca
lacună de numerotare deși are temei.

## H. Legea publicității — L-62/2022 (ingerată 2026-09-05)

Ingerată pentru o singură trimitere, dar una care blochează o prezumție legală. Art. 4^1
alin. (9) din `L-171-2012`, introdus de `L-177-2025`, prezumă publicitatea derivatelor interzise
drept înșelătoare „astfel cum este definită aceasta la art. 3 din Legea nr. 62/2022". Fără actul
țintă, prezumția nu putea fi ancorată.

| Act | doc_id | Consolidare | Ancore |
|---|---|---|---|
| Legea nr. 62/2022 cu privire la publicitate | 155339 | 2026-08-14 | 58 (53 de bază + 5 cu exponent), 11 capitole |

**Perimetru.** A mers în `moldova-legal/`, nu în `cnpf/`: este lege generală de publicitate și
protecție a consumatorului, ca `L-135-2007` și `L-220-2007`. Nu adaug în `DOCS`-ul scriptului CNPF.

**Verificare.** `verify_business_law.py`: integritate de text **PASS, 675 de linii scrise față de
675 de referință**, deci s-au adăugat numai ancore. Fără `<sup>` rămas, fără ancore duplicate,
numerotare 1–53 completă, cei cinci exponenți de articol (11^1–11^4, 32^1) coincid cu sursa.
Consolidarea 2026-08-14 este **trecută**, deci fișierul conține textul aplicabil astăzi; niciun
avertisment de consolidare viitoare.

### H.1. Ce a deblocat, verigă cu verigă

| Verigă | Unde | Stare înainte |
|---|---|---|
| prezumția | `L-171-2012` art. 4^1 alin. (9) | ancorată |
| definiția publicității înșelătoare | `L-62-2022` art. 3 | **lipsă** |
| interdicția | `L-62-2022` art. 7 alin. (3) lit. b) | **lipsă** |
| conținutul | `L-62-2022` art. 20 | **lipsă** |
| sarcina probei | `L-62-2022` art. 52 alin. (2) | **lipsă** |
| definiția difuzorului de publicitate | `L-62-2022` art. 3 | **lipsă** |

### H.2. Constatări proprii

1. **Perimetrul financiar are deja regim propriu aici.** Art. 48 interzice publicitatea pentru
   servicii financiare, de asigurare, de investiții și pentru valori mobiliare, pe patru criterii
   de conținut, plus interdicția de publicitate pentru valori mobiliare înainte de înregistrarea
   ofertei publice și în perioada suspendării emisiunii. Este anterior și independent de art. 4^1.
2. **CNPF nu este autoritate de control sub această lege.** Art. 50 alin. (1) enumeră limitativ
   Consiliul Concurenței, Consiliul Audiovizualului, Poliția și Agenția Achiziții Publice.
   Competența pe care `L-177-2025` a dat-o CNPF stă în legea pieței de capital, nu aici.
   Suprapunerea cu Consiliul Concurenței nu este tranșată în niciunul dintre texte. `[de verificat]`
3. **Legea definește deja configurația offshore.** „Publicitate penetrantă" înseamnă publicitate
   accesibilă consumatorilor din Republica Moldova pentru a cărei difuzare nu s-a plătit unui
   difuzor din Republica Moldova. Este exact cazul pe care art. 4^1 îl vizează.
4. **O trimitere externă nouă, neacoperită.** Art. 2 alin. (2) își ia criteriul de direcționare
   teritorială din art. 3 al Legii comerțului electronic nr. 284/2004, care nu este ingerată.
   Aceeași formă de lacună pe care ingerarea de față tocmai a închis-o. `[de verificat]`

## I. Legea serviciilor societății informaționale — L-284/2004 (ingerată 2026-09-05)

A treia verigă a aceluiași lanț, ingerată în aceeași zi. Art. 2 alin. (2) din `L-62-2022` își ia
criteriul de direcționare teritorială din art. 3 al acestui act. Fără el, întinderea teritorială a
legii publicității — și deci capacitatea interdicțiilor din `L-177-2025` de a atinge platformele
fără prezență în Moldova — nu putea fi ancorată.

| Act | doc_id | Consolidare | Ancore |
|---|---|---|---|
| Legea nr. 284/2004 privind serviciile societății informaționale | 150486 | 2026-02-14 | 29 (28 de bază + 25^1), 7 capitole |

### I.1. ⚠ Actul a fost redenumit și corpusul îl citeăză sub titlul vechi

Fișa legis.md dă **denumirea actuală** „privind serviciile societății informaționale" și **denumirea
precedentă** „privind comerțul electronic". Este același act: nr. 284 din 22.07.2004. `L-62-2022`
art. 2 alin. (2) trimite la „Legea comerțului electronic nr. 284/2004", titlu care nu mai există.
Trimiterea rămâne validă — număr și dată corecte, act neabrogat — dar **o căutare după titlu nu
îl găsește**. Redenumirea are temei: actul poartă clauză expresă de transpunere a Directivei
2000/31/CE, care vorbește despre „servicii ale societății informaționale".

### I.2. Verificare

`verify_business_law.py`: integritate de text **PASS, 290 de linii scrise față de 290 de
referință**. Sursa avea 3 etichete `<sup>` și **4 exponenți ridicați prin CSS** (`top:-0.5em`),
a doua formă fiind cea găsită în septembrie pe `L-171-2012`; ambele rezolvate înainte de
extracție. Fără `<sup>` rămas, fără ancore duplicate. Consolidarea 2026-02-14 este trecută.

**Un defect al verificatorului, găsit pe acest act și reparat în aceeași zi.** Raportul spunea
„plain articles 27, range 1-27", ceea ce s-ar citi ca lacună la art. 28. Nu era. Contorul folosea
`^## Articolul (\d+)\.`, cu punct obligatoriu, iar în sursă ultimul articol este scris
`Articolul 28`, fără punct, fiindcă nu are titlu — este articolul de dispoziții finale. Ancora
exista și era corectă; numerotarea este completă **1–28**. Aritmetica: 29 de ancore = 27 cu punct
+ art. 28 fără punct + 25^1.

**Reparat 2026-09-05.** Tiparul acceptă acum punct, spațiu sau sfârșit de linie după număr
(`^## Articolul (\d+)(?=[.\s]|$)`) și continuă să excludă articolele cu exponent, fiindcă după
cifre urmează `^`, care nu este niciunul dintre cele trei. S-a adăugat o linie de raport care
numește articolele fără titlu, ca să nu pară o anomalie tăcută. **Dovada că reparația este
îngustă:** ieșirea verificatorului a fost salvată înainte și după, iar diferența pe tot corpusul
de 17 acte este de două linii, ambele la acest act; Codul fiscal (353, range 1-379) și Codul penal
(388, range 1-388) rămân neschimbate, deci exponenții și forma `54^1/1` nu au fost afectate.

### I.3. Ce aduce actul, dincolo de motivul ingerarii

1. **Testul de direcționare este cu prag, nu general.** Art. 3 alin. (3) dă **cinci indicii și cere
   cel puțin două**; alin. (4) declară **trei indicii insuficiente**, între care simpla
   accesibilitate a paginii web din Moldova. Pentru cazurile de derivate retail, alin. (4) este
   partea operativă.
2. **Răspunderea intermediarilor.** Capitolul III transpune regimul 2000/31/CE: transmitere simplă
   (art. 15), caching (art. 16), hosting (art. 17). Art. 17 alin. (3) lit. a) leagă pierderea
   scutului de o **dispoziție scrisă a unei instanțe sau a unei autorități publice abilitate**.
   Dacă solicitarea CNPF din art. 4^1 alin. (6) lit. b) al `L-171-2012` se califică astfel, gazda
   trebuie să acționeze prompt. Nu rezultă expres din niciunul dintre texte. `[de verificat]`
3. **Autorități competente — clauză deschisă.** Art. 26 alin. (3) admite „și alte autorități în
   limitele competențelor stabilite de lege", spre deosebire de art. 50 din `L-62-2022`, care este
   o enumerare limitativă. O autoritate sectorială poate intra aici, dar nu acolo.
4. **Clauză expresă de transpunere**, rară în corpusul moldovenesc: Directiva 2000/31/CE,
   JO L 178 din 17 iulie 2000. Directiva nu este în wiki, deci conformitatea nu este verificată
   articol cu articol. `[de verificat]`
5. **Lanțul nu se închide complet.** Art. 26 alin. (1) trimite la Legea nr. 105/2003 privind
   protecția consumatorilor, neingerată. Pentru întrebările de direcționare teritorială lanțul
   este complet; pentru autoritățile de control, nu.

## J. Legea protecției consumatorilor — L-105/2003 (ingerată 2026-09-05)

A patra și ultima verigă a lanțului pornit de la `L-177-2025`. Art. 26 alin. (1) din `L-284-2004`
trimite la organele de control în protecția consumatorilor „conform domeniilor de competență
stabilite în Legea nr. 105/2003”.

| Act | doc_id | Consolidare | Ancore |
|---|---|---|---|
| Legea nr. 105/2003 privind protecția consumatorilor | 150997 | 2025-10-25 | 75 (74 de bază + 36^1), 10 capitole, 8 secțiuni |

**Verificare.** `verify_business_law.py`: integritate de text **PASS, 1.245 de linii scrise față de
1.245 de referință**. Fără `<sup>` rămas, fără ancore duplicate, numerotare **1–74 completă**,
6 exponenți la nivel de alineat sau literă păstrați în corp. Consolidarea 2025-10-25 este trecută.
Denumirea actului nu s-a schimbat, spre deosebire de `L-284-2004`.

### J.1. Actul nu este o verigă procedurală, ci o atribuire de mandat

**Arts. 37 alin. (2) și 38 alin. (2) numesc EXPRES CNPF** autoritate de supraveghere în protecția
consumatorilor, în paralel cu Inspectoratul de Stat pentru Supravegherea Produselor Nealimentare
și Protecția Consumatorilor:

| Domeniu | Regula generală | Perimetrul CNPF |
|---|---|---|
| clauze abuzive, prin raportare la arts. 1069–1072, 1075–1079 și 1081 din `CC-1107-2002` | Inspectoratul, art. 37 alin. (1) | **CNPF**, art. 37 alin. (2) |
| contracte la distanță și negociate în afara spațiilor comerciale | Inspectoratul, art. 38 alin. (1) | **CNPF**, art. 38 alin. (2) |

Art. 37 alin. (2) este text recent: modificat prin LP189 din 10.07.25, în vigoare 25.10.25.
Puterile atașate sunt reale — alin. (3) obligația comerciantului de a prezenta contractele,
alin. (4) act de constatare și acțiune în instanță, alin. (5) nulitate și excludere din toate
contractele cu același obiect, alin. (6) acțiune împotriva unui întreg sector economic.

**Toate trimiterile au fost verificate și se rezolvă în wiki:** art. 4 alin. (2^1) din `L-192-1998`
există și enumeră opt categorii, iar cele zece articole din Codul civil sunt toate prezente în
`CC-1107-2002`.

### J.2. Harta de mandat, închisă pe trei acte

| Act | Este CNPF autoritate acolo? |
|---|---|
| `L-62-2022` art. 50 — publicitate | **nu**, enumerare limitativă |
| `L-284-2004` art. 26 alin. (3) — servicii ale societății informaționale | **poate**, clauză deschisă |
| `L-105-2003` arts. 37 alin. (2), 38 alin. (2) | **da, expres**, pentru perimetrul propriu |

Răspunde întrebării deschise consemnate la secțiunea H: CNPF **este** autoritate de protecție a
consumatorilor pentru sectorul său, dar **nu** autoritate de control asupra publicității.
Competența punctuală față de difuzori dată de `L-177-2025` rămâne o excepție creată în legea
pieței de capital.

### J.3. Constatări proprii

1. **CNPF supraveghează băncile pe latura protecției consumatorilor.** Art. 4 alin. (2^1) lit. d)
   din `L-192-1998` include băncile și sucursalele băncilor străine sub Legea nr. 202/2017.
   Este o excepție de la delimitarea produsă de `L-178-2020` și nu decurge din acea lege, ci din
   această atribuire separată. Coordonarea cu supravegherea prudențială a BNM asupra acelorași
   bănci nu rezultă din texte. `[de verificat]`
2. **A treia răsturnare de sarcină a probei din același lanț.** Art. 14 alin. (2) și (3): dacă
   comerciantul nu prezintă dovezi într-un termen rezonabil, dar **nu mai mare de 15 zile
   calendaristice**, afirmațiile din sesizare **se consideră fondate**. Alături de art. 52
   alin. (2) din `L-62-2022` și de prezumția din art. 4^1 alin. (9) al `L-171-2012`. Diferența:
   aici există termen și consecință automată.
3. **Două mecanisme diferite poartă același nume, „alertă”.** Art. 55 de aici este o
   **notificare între autorități**, către biroul unic de legătură, cu șase categorii de
   informații. Alerta din art. 4^1 alin. (6) lit. a) al `L-171-2012` este o **publicare către
   public**, cu numele persoanelor, declarată necontestabilă de alin. (7).
4. **Clauză expresă de transpunere cu patru instrumente:** Directiva 2005/29/CE (practici
   comerciale neloiale), Directiva 2013/11/UE (SAL), Directiva (UE) 2019/771 (vânzarea de bunuri)
   și Regulamentul (UE) 2017/2394 (cooperarea CPC). Niciunul nu are extract EUR-Lex în wiki, deci
   conformitatea nu se poate verifica articol cu articol. `[de verificat]`
5. **Lanțul de trimiteri nu se încheie definitiv.** Art. 44 alin. (2) lasă lista autorităților
   competente pentru cooperarea transfrontalieră în seama unei hotărâri de Guvern, neingerată,
   deci nu se poate stabili din lege dacă CNPF figurează pe ea. `[de verificat]`

## K. Legea concurenței — L-183/2012 (ingerată 2026-09-05)

Închide bucla deschisă de `L-62-2022`: art. 50 alin. (1) lit. a) al legii publicității trimite
Consiliul Concurenței la „atribuțiile sale prevăzute de Legea concurenței nr. 183/2012”, iar
art. 18 alin. (4) lit. a) interzice publicitatea comercială care este act de concurență neloială
„conform Legii concurenței nr. 183/2012”.

| Act | doc_id | Consolidare | Ancore |
|---|---|---|---|
| Legea concurenței nr. 183/2012 | 152606 | 2025-12-31 | 110 (95 de bază + 15 cu exponent), 9 capitole, 6 secțiuni |

**Verificare.** `verify_business_law.py`: integritate de text **PASS, 1.239 de linii scrise față
de 1.239 de referință**. 41 de etichete `<sup>` în sursă, niciun span ridicat prin CSS. Fără
`<sup>` rămas, fără ancore duplicate, numerotare **1–95 completă**, 15 exponenți de articol
coincid cu sursa, 9 exponenți de alineat sau literă păstrați în corp.

### K.1. Limita care schimbă harta de mandat pe publicitate

Reciproca trimiterii există în două locuri, **amândouă cu aceeași restricție**: art. 32 lit. c)
(domeniul de activitate cuprinde publicitatea comercială „sub aspectul asigurării drepturilor și
intereselor întreprinderilor”) și art. 39 lit. f) (examinează și constată încălcări ale
`L-62-2022` „în cazul în care sunt afectate drepturile întreprinderilor”).

**Consiliul Concurenței nu este deci autoritatea generală de control asupra publicității**, ci
autoritate pentru latura **B2B**. Art. 14 alin. (2) confirmă mecanismul: faptele de concurență
neloială se examinează **la plângerea întreprinderii lezate**, nu din oficiu la sesizarea unui
consumator. Enumerarea din art. 50 al legii publicității părea să dea competență generală; fiecare
autoritate acționează însă „în limita atribuțiilor sale”, iar limita se citește în legea proprie.

### K.2. Două contraste de procedură

1. **Sarcina probei merge invers față de restul lanțului.** Art. 52 alin. (3): în procedura de
   examinare, sarcina probei încălcării revine **Consiliului Concurenței**. Față de art. 52
   alin. (2) din `L-62-2022`, art. 14 alin. (2)–(3) din `L-105-2003` și prezumția din art. 4^1
   alin. (9) al `L-171-2012`, unde sarcina trece pe profesionist. Dreptul concurenței o ține la
   autoritate; dreptul consumatorului și al publicității o mută.
2. **Actele sunt contestabile.** Art. 47 alin. (1): 30 de zile, sub `COD-116-2018`, fără
   procedură prealabilă. Față de art. 4^1 alin. (7) din `L-171-2012`, unde alerta CNPF „nu poate
   fi suspendată sau contestată”. Două autorități administrative, două tratamente opuse ale
   controlului judecătoresc, în aceeași materie a comunicării comerciale.

### K.3. Exponenți aplatizați în corp — defect de SURSĂ, nu de extracție

Legea are 95 de articole, deci orice trimitere la un articol cu trei cifre este imposibilă.
Verificate individual: `art. 572` de două ori este **57^2**, `art. 571` este **57^1**, `art. 541`
este **54^1**. Toate trei articolele există și sunt ancorate corect.

**Dovada că defectul este în sursă:** HTML-ul de la legis.md are în aceste locuri cifrele lipite,
fără etichetă `<sup>`, deși **același fișier** scrie corect `art. 57^2` la art. 80^1 lit. b), iar
verificatorul confirmă că 9 exponenți de alineat și literă au fost rezolvați acolo unde sursa i-a
marcat. Este o instanță documentată a întrebării deschise nr. 2 din `CLAUDE.md`.

**Contraproba, la fel de importantă:** nu orice număr lung este exponent. Confirmate ca trimiteri
reale la alte acte: `art. 273 pct. 5^5)` din `COD-218-2008`, `art. 209 alin. (1)` din
`COD-116-2018`, `art. 174–179` din `COD-225-2003`, `art. 101–106` TFUE; iar `art. 620` și
`art. 1205` sunt citări de Monitor Oficial, nu articole.

### K.4. Acquis

Clauză expresă, patru instrumente: **arts. 101–106 TFUE**, parțial **Directiva (UE) 2019/1**
(ECN+), **Regulamentul (CE) nr. 1/2003** și **Regulamentul (CE) nr. 139/2004**. Niciunul nu are
extract EUR-Lex în wiki. `[de verificat]`

## L. Codul serviciilor media audiovizuale — COD-174/2018 (ingerat 2026-09-05)

A doua autoritate din art. 50 alin. (1) al legii publicității. Lit. b) trimite Consiliul
Audiovizualului la „atribuțiile sale prevăzute de Codul serviciilor media audiovizuale pe
domeniul publicității și al altor forme de comunicări comerciale audiovizuale”. Cu `L-183-2012`
ingerată în aceeași zi, ambele trimiteri din art. 50 sunt ancorate.

| Act | doc_id | Consolidare | Ancore |
|---|---|---|---|
| Codul serviciilor media audiovizuale nr. 174/2018 | 150538 | 2026-06-24 | 98 (94 de bază + 4 cu exponent), 11 capitole |

Prefixul legis.md este `CSMA`, nu `LP`; stem-ul rămâne `COD-174-2018`, ca la celelalte coduri.

**Verificare.** `verify_business_law.py`: integritate de text **PASS, 1.448 de linii scrise față
de 1.448 de referință**. 66 de etichete `<sup>` în sursă, dintre care doar patru la nivel de
articol; **55 de exponenți de alineat și literă păstrați în corp**, cel mai mare număr din
corpusul moldovenesc de până acum. Fără `<sup>` rămas, fără ancore duplicate, numerotare
**1–94 completă**, art. 23 abrogat cu marcaj. Consolidarea 2026-06-24 este trecută, zero
dispoziții cu intrare în vigoare amânată.

### L.1. Raportul cu legea publicității este de CUMUL, nu de delimitare

Spre deosebire de `L-183-2012`, unde competența este limitată la drepturile întreprinderilor, aici
art. 62 alin. (1) spune că furnizorii difuzează comunicări comerciale „în conformitate cu prezentul
cod, **cu Legea cu privire la publicitate** și cu Regulamentul privind conținuturile audiovizuale”.
`L-62-2022` se aplică deci **în plus**, nu în locul codului.

**Trimiterea a fost actualizată recent.** Antetul poartă nota că „în cuprinsul legii” textul
„Legea nr. 1227/1997” se substituie cu „Legea nr.62/2022”, prin LP125 din 29.05.25, **în vigoare
24.06.26** — aceeași dată cu consolidarea. În textul de astăzi trimiterea a rămas în forma
generică „Legea cu privire la publicitate”, fără număr: niciunul dintre cele două numere nu mai
apare în corp, ci doar în nota de modificare.

### L.2. Constatare negativă, verificată pe tot textul

**Codul nu are nicio regulă specifică pentru comunicările comerciale privind serviciile
financiare, investițiile, valorile mobiliare sau instrumentele derivate.** Interdicțiile de la
art. 63 alin. (3) vizează tutunul, medicamentele pe prescripție, jocurile de noroc și practicile
oculte.

Consecința este precisă pentru perimetrul CNPF: art. 4^1 alin. (2) lit. g) din `L-171-2012`
interzice folosirea radioului și a televiziunii pentru promovarea derivatelor cu levier către
clienți neprofesioniști, dar acea interdicție **acționează asupra celui care promovează, nu prin
codul canalului**. Difuzorul nu are, în propriul cod, o normă care să-i interzică programul.
Completarea vine din art. 4^1 alin. (6) lit. b), care dă CNPF dreptul de a-i cere sistarea.

### L.3. Ce mai aduce actul

1. **Cap. IX, arts. 62–72:** cinci forme permise de comunicare comercială; cerința de a fi „corecte
   și oneste” și clar separate de conținutul editorial; interdicțiile de la art. 63 alin. (3);
   regimuri speciale pentru băuturi alcoolice (art. 70) și medicamente (art. 71); publicitate
   politică și electorală (art. 72).
2. **Cap. X, arts. 73–87:** Consiliul Audiovizualului. Art. 75 alin. (3) lit. c) îi dă competența
   asupra reglementărilor privind comunicările comerciale. Art. 84: sancțiuni de la avertizare
   publică până la retragerea licenței, plus amendă de la 1.000 la 100.000 de lei.
3. **Cap. VIII^1, arts. 61^1 și 61^2:** obligațiile furnizorilor de platformă de partajare a
   materialelor video, partea adusă de Directiva 2018/1808/UE. Atinge aceleași servicii pe care
   art. 4^1 alin. (2) lit. g) din `L-171-2012` le numește „platforme de social media”, din
   direcție diferită.
4. **Acquis:** transpune **parțial** Directiva 2010/13/UE, CELEX `32010L0013`, modificată ultima
   dată prin Directiva 2018/1808/UE. Cuvântul „parțial” face verificarea articol cu articol mai
   necesară decât la actele cu transpunere declarată completă; niciunul dintre cele două
   instrumente nu are extract EUR-Lex în wiki. `[de verificat]`
5. **Lacună de un nivel mai jos:** Regulamentul privind conținuturile audiovizuale, act al
   Consiliului Audiovizualului, este făcut obligatoriu de art. 62 alin. (1) și art. 75 alin. (3)
   lit. c), dar nu este ingerat. `[de verificat]`

## M. Regulamentul privind conținuturile audiovizuale — DCA-61/2024 (ingerat 2026-09-05)

Lacuna semnalată la secțiunea L: arts. 62 alin. (1) și 75 alin. (3) lit. c) din `COD-174-2018` fac
Regulamentul obligatoriu pentru comunicările comerciale, dar el nu era în wiki. **Nu este act al
Parlamentului**, îl emite Consiliul Audiovizualului.

| Act | doc_id | În vigoare | Ancore |
|---|---|---|---|
| Decizia CA nr. 61/2024, cu Regulamentul anexat | 142648 | 05.05.2024 | 0 de articol; 8 capitole, 11 secțiuni |

**Verificare.** `verify_business_law.py`: integritate de text **PASS, 528 de linii scrise față de
528 de referință**. Fără `<sup>` rămas. sha256 recalculat: coincide.

### M.1. Metodă de căutare nouă pentru acest corpus — căutarea în titlu

Actul nu se caută după număr de lege, iar codul îl numește fără să îl numeroteze. Se găsește prin
`getResults?search_string=<frază>&search_type=1`, urmat de `getAjaxContent` pe aceeași sesiune cu
cookie. Lista tipurilor: `https://www.legis.md/search_type/getlist` — **1 = căutare în titlu,
2 = căutare în text**.

**Capcană verificată: fraza trebuie scrisă FĂRĂ DIACRITICE.** „continuturile audiovizuale”
întoarce 13 rânduri; aceeași frază cu diacritice întoarce **zero**. Această metodă completează
căutarea după `nr_doc` documentată în nota de lacună din iulie și este singura cale către actele
subordonate ale autorităților de reglementare.

### M.2. Două generații, și o capcană de citare

| Document | doc_id | Stare |
|---|---|---|
| Decizia nr. 61/219 din 30.12.2019, prima aprobare | 143469 | **abrogată 30.05.2024** prin DCA15 din 24.05.24 |
| `REGULAMENT Nr. 63 din 22.01.2021 privind conținuturile audiovizuale` | 125023 | textul aprobat prin decizia din 2019; **generația veche** |
| **Decizia nr. 61 din 01.03.2024**, cu Regulamentul anexat | **142648** | **în vigoare din 05.05.2024**, fără abrogare, fără modificări |

**Capcana:** `REGULAMENT 63/2021` **nu poartă dată de abrogare** în fișa legis.md, deși decizia care
îl aprobase a fost abrogată. Nota de subsol a acelui fișier spune expres că este textul aprobat
prin Decizia 61/219 din 2019. Cine îl deschide după titlu poate crede că este textul curent.

### M.3. Ce corectează față de secțiunea L.2

Secțiunea L.2 consemna că `COD-174-2018` **nu are nicio regulă** pentru publicitatea la servicii
financiare sau instrumente derivate. Rămâne adevărat pentru cod. **Regulamentul rezolvă altfel,
printr-o trimitere generală:**

> **pct. 90.** „În comunicările comerciale audiovizuale nu pot fi prezentate produse, servicii sau
> activități **interzise prin lege**.”

Interdicția din art. 4^1 alin. (1) și (2) al `L-171-2012` este o interdicție legală, deci prin
pct. 90 difuzorul care transmite o comunicare comercială pentru opțiuni binare sau derivate cu
levier către clienți neprofesioniști **încalcă Regulamentul**, deși nici codul, nici Regulamentul
nu numesc produsele financiare. Sancțiunea vine din Capitolul VIII al Regulamentului și din
art. 84 al codului.

**Executarea are deci două brațe, nu unul:** CNPF poate cere sistarea sub art. 4^1 alin. (6)
lit. b), **iar** Consiliul Audiovizualului poate sancționa difuzorul pe temei propriu. Coordonarea
nu rezultă din texte. `[de verificat]`

### M.4. Structură și consecință de citare

Decizia are 2 puncte; Regulamentul anexat are **203 puncte**, 8 capitole, 11 secțiuni.
**Numerotarea repornește** între decizie și anexă, deci ancorarea la nivel de punct ar produce
duplicate. Ingerat cu **zero ancore de articol**, ca `HG-1170-2016`, `HG-1171-2018` și
`HG-574-2024`. **O trimitere la „pct. N din Regulament” nu este ancorată.**

Ancorele structurale există, dar **secțiunile nu sunt unice**: „Secțiunea 1” apare de trei ori,
„Secțiunea a 2-a” de trei ori. O trimitere la secțiune trebuie să numească și capitolul.
Capitolul V, „Difuzarea comunicărilor comerciale audiovizuale”, are șapte secțiuni.

## N. Legea libertății de exprimare — L-64/2010 (ingerată 2026-09-05)

Trimisă de `DCA-61-2024`: pct. 199 și 201 din Regulamentul privind conținuturile audiovizuale spun
că dreptul la replică se asigură „în condițiile CSMA și a prevederilor Legii nr. 64/2010”.

| Act | doc_id | Consolidare | Ancore |
|---|---|---|---|
| Legea nr. 64/2010 cu privire la libertatea de exprimare | 141515 | 2024-01-23 | 34 (1–34, fără exponenți), 3 capitole, 2 secțiuni |

**Verificare.** `verify_business_law.py`: integritate de text **PASS, 269 de linii scrise față de
269 de referință**. Fără `<sup>` rămas, fără duplicate, numerotare **1–34 completă**, 2 exponenți
de alineat păstrați în corp. sha256 recalculat: coincide.

### N.1. Primul test real al contorului reparat

Art. 34 este scris în sursă `Articolul 34`, **fără punct**, fiindcă nu are titlu. Contorul de
dinaintea reparației din aceeași zi l-ar fi raportat drept „33, range 1-33”, adică **o lacună
falsă la art. 34**. Cel reparat raportează **34, range 1-34** și îl numește separat pe linia
`fara punct dupa numar`. Reparația a fost făcută pe `L-284-2004`, dar acesta este actul pe care
s-a văzut că nu era un caz izolat.

### N.2. A cincea configurație a sarcinii probei din același perimetru

Arts. 24–25 așază sarcina pe **reclamant** și adaugă **șase prezumții, toate în favoarea
exprimării**: dubiul asupra statutului de persoană se rezolvă spre „persoană publică”, asupra
interesului spre „interes public”, asupra naturii afirmației spre „judecată de valoare”, asupra
cuantumului prejudiciului moral spre **1 leu**, asupra bunei-credințe jurnalistice spre
buna-credință, iar orice alt dubiu **împotriva restricționării** libertății de exprimare.

| Act | Cine poartă sarcina |
|---|---|
| `L-171-2012` art. 4^1 alin. (9) | profesionistul |
| `L-62-2022` art. 52 alin. (2) | furnizorul de publicitate |
| `L-105-2003` art. 14 alin. (2)–(3) | comerciantul, în 15 zile |
| `L-183-2012` art. 52 alin. (3) | autoritatea |
| **`L-64-2010` arts. 24–25** | **reclamantul**, plus șase prezumții contra lui |

### N.3. Contragreutatea alertei necontestabile

Art. 4^1 alin. (7) din `L-171-2012` publică numele persoanelor fără act permisiv și declară alerta
„necontestabilă”, cu interesul public prezumat a prevala. Citită lângă această lege:

- **pe fond direcțiile coincid** — art. 25 alin. (2) rezolvă dubiul tot în favoarea interesului
  public, iar cine prestează servicii de investiții fără act permisiv intră ușor în definiția de
  persoană publică de la art. 2;
- **pe remediu diferă radical** — legea de față nu suprimă calea de atac, ci lasă acțiunea în
  defăimare, cu dezmințire (art. 26), replică (art. 27) și compensație (art. 29), pe când
  art. 4^1 alin. (7) suprimă contestarea actului administrativ.

**Dacă persoana numită într-o alertă retrasă poate acționa în defăimare nu rezultă din niciunul
dintre texte.** Legea nu limitează expres cine poate fi pârât, iar „defăimare” este definită prin
răspândirea informației false, fără a distinge după calitatea celui care o răspândește.
`[de verificat]`

### N.4. Distincția care contează pentru cererile la Consiliul Audiovizualului

Art. 27 alin. (1) leagă **replica** de judecățile de valoare fără substrat factologic suficient,
nu de relatările false de fapte, pentru care remediul este **dezmințirea** (art. 26). Cererile
adresate Consiliului sub `DCA-61-2024` cap. VII se califică după această distincție.

## O. Perimetrul construcțiilor — COD-434/2023 și HG-743/2024 (ingerate 2026-09-05)

Perimetrul lipsea complet. Motivul concret al ingerării: la 05.09.2026 o analiză de contract de
antrepriză pentru o casă individuală a trebuit livrată cu trei poziții neancorate — termenele de
garanție, dirigintele de șantier, autorizația de construire.

### O.1. Premisa verificată în sursă înainte de orice

Sursele secundare dădeau intrarea în vigoare a codului când 30.01.2025, când 30.01.2026.
**Textul rezolvă întrebarea: 30.01.2025.**

`COD-434-2023` **art. 390 alin. (1)**: codul intră în vigoare „peste 12 luni de la data publicării
în Monitorul Oficial", cu excepția unei liste de dispoziții — între care **art. 150**, pragul de
scutire de autorizație — care intră în vigoare la data publicării. Publicare 30.01.2024, deci
30.01.2025. Al treilea termen, alin. (1^1): arts. 129 alin. (1), (2), (4) și (6)–(8), 130, 324,
387 alin. (5^1) și 389 alin. (6) au intrat în vigoare la 1 septembrie 2024.

**Capcană de fișă.** Fișa legis.md a codului scrie „Data intrării în vigoare 30.01.2024", care
este data excepțiilor, nu a codului. Cine citește fișa și nu art. 390 datează greșit tot regimul.

Data se confirmă de patru ori independent: fișele celor trei legi abrogate și a HG 285/1996 dau
„Data abrogării 30.01.2025"; HG 329/2009 poartă „Abrogată prin HG743 […] în vigoare 30.01.25";
`HG-743-2024` pct. 6 spune „intră în vigoare la data de 30 ianuarie 2025".

### O.2. Cele trei acte abrogate — niciunul nu se ingerează

Art. 390 alin. (5) abrogă **integral**, la data intrării în vigoare a codului, Legea 721/1996
privind calitatea în construcții, Legea 835/1996 privind principiile urbanismului și amenajării
teritoriului și Legea 163/2010 privind autorizarea executării lucrărilor de construcție. Art. 390
alin. (4) abrogase deja arts. 10, 11 și 14 din Legea 163/2010 **de la publicare**, cu un an mai
devreme. Niciun regim tranzitoriu nu menține în vigoare vreo dispoziție din cele trei.

**Decizia:** nu se ingerează niciunul. Ținta 3 din plan era condiționată de constatarea că unul
dintre ele mai este aplicabil; constatarea este negativă.

**Anomalie de registru, de semnalat, nu de rezolvat.** Pentru Legea 721/1996 (doc_id 141608)
metadata legis.md contrazice propriul text al actului:

| act | corpul documentului | câmpul „Data abrogării" | marcaj în lista de căutare |
|---|---|---|---|
| L. 721/1996 | „Abrogată prin CUC434 […] în vigoare 30.01.25" | **„-", gol** | **„Modificat"** |
| L. 835/1996 | — | 30.01.2025 | „Abrogat" |
| L. 163/2010 | — | 30.01.2025 | „Abrogat" |
| HG 285/1996 | „Abrogată prin HG726 […] în vigoare 30.01.25" | 30.01.2025 | „Abrogat" |

Cine filtrează legis.md după marcaj sau după câmp conchide că legea calității în construcții este
încă în vigoare. `[de verificat]`

### O.3. Nu există regulament de recepție a construcțiilor

Ținta 2 cerea „regulamentul de recepție a construcțiilor și regulamentul de atestare
tehnico-profesională". Al doilea există; **primul nu mai există**, iar constatarea a fost făcută
prin trimiterile codului, nu din memorie:

1. Codul **nu deleagă** recepția. Căutarea în text după „recepție" alături de „regulament" sau
   „Guvern" nu întoarce nimic. Recepția este reglementată direct, în arts. 192–215.
2. Regulamentul anterior, HG 285/1996 (doc_id 145621), este abrogat de la 30.01.2025, prin
   HG 726/2024. Pct. 4 din `HG-743-2024` completează chiar HG 726/2024 cu norma care fixează data.

Materia tehnică a fost preluată de **NCM A.05.01:2025 „Executarea și recepția construcțiilor"**,
aprobat prin ordinul MIDR nr. 88/2025 (doc_id 148510) — normativ tehnic, nivelul 7 al ierarhiei
surselor, **neingerat**.

### O.4. Actul subordonat ingerat — HG-743/2024

Găsit prin preambulul propriu: „În temeiul **art. 129 alin. (6) și art. 338 alin. (1)** din Codul
urbanismului și construcțiilor nr. 434/2023". Aprobă Regulamentul cu privire la atestarea
specialiștilor care desfășoară activități în construcții (anexa nr. 1) — regulamentul la care
trimit art. 180 alin. (3) pentru dirigintele de șantier și art. 187 alin. (4) pentru responsabilul
tehnic — și Regulamentul privind verificarea documentației de proiect și expertiza tehnică
(anexa nr. 2). Abrogă HG 329/2009, cu menținerea certificatelor până la expirarea termenului lor
(pct. 2), coroborat cu art. 387 alin. (6) din cod.

Ruta de căutare care l-a găsit, de reținut fiindcă titlul nu conține niciun cuvânt-cheie evident
(„cu privire la asigurarea calității în construcții"): **căutare în TEXT**, `search_type=2`, cu
fraza din art. 338 alin. (1) al codului, „atestarea specialistilor care desfasoara activitati in
constructii", scrisă fără diacritice. Căutarea în titlu, `search_type=1`, nu îl întoarce.

### O.5. Ce nu este ancorat, în ambele acte

**Codul: cele 25 de anexe lipsesc din text.** `showdetails` le servește doar ca etichete de
legătură; extracția le-a păstrat ca listă de nume la finalul textului, „anexa nr.1" … „anexa
nr.25" (nr. 17 marcată „abrogată"). Conținutul stă în fișiere separate pe legis.md. **O trimitere
la „anexa nr. N din cod" NU este ancorată.** Afectate direct de normele deja folosite: anexa nr. 9
(Cartea tehnică, art. 229 alin. (1)), anexa nr. 10 (construcții de importanță redusă, art. 197
alin. (8)), anexa nr. 25 (modelul declarației de începere a lucrărilor, art. 176 alin. (2) lit. b)).
Este o limită mai insidioasă decât de obicei, fiindcă restul actului este ancorat perfect.

**Hotărârea: „pct. N" nu este ancorat**, ca la `HG-1170-2016`, `HG-1171-2018`, `HG-574-2024` și
`DCA-61-2024`. Aici motivul este demonstrabil, nu prezumat: numerotarea repornește între hotărâre
și cele trei anexe, iar în cele 211 puncte numerotate punctele 1–25 și următoarele apar de mai
multe ori. Exemplu real: **pct. 50** este, în anexa nr. 1 (linia 440), obligația de formare
continuă la 5 ani, iar în anexa nr. 2 (linia 647), înregistrarea avizelor de verificare. Spre
deosebire de cod, **anexele hotărârii sunt prezente integral în text**.

Consecință care atinge și registrul mecanic: marcajele de consolidare viitoare ale hotărârii
(`[Pct.50 …]`, `[Pct.82 …]`) **nu spun în care anexă**. Registrul nu poate dezambigua ce sursa nu
dezambiguează.

### O.6. Consolidări

| act | doc_id | consolidare | stare |
|---|---|---|---|
| `COD-434-2023` | 155736 | 2026-08-06 (LP153/2026) | trecută; **zero** dispoziții amânate |
| `HG-743-2024` | 155190 | 2026-12-30 (HG341/2026) | **viitoare**; 6 dispoziții amânate |

Cele șase: `Pct.33 subpct.33.3`, `Pct.50`, `Pct.61 subpct.61.6`, `Pct.82`, `Pct.115 introdus`,
`Anexa nr.9 introdusă`, toate „în vigoare 30.12.26". Niciuna nu privește caracterul obligatoriu al
dirigintelui de șantier sau al responsabilului tehnic, care rezultă din arts. 180 și 187 ale
codului, nu din regulament.

### O.7. Raportul cu actele deja ancorate

**Codul contravențional `COD-218-2008`.** Codul urbanismului **nu a modificat și nu a dublat
art. 179**. Art. 389 alin. (1) enumeră limitativ ce a modificat: arts. 46^1, 169 (lit. c^1) nouă),
**177** (alin. (6) abrogat, alineate (7) și (8) noi), 313^3 (alin. (1^1) nou), 401, 408^2 și
423^10. Art. 179 — construcții neautorizate, amendă 250–400 u.c. persoanei fizice — rămâne
neatins. Verificat în `_meta/inforce/in-force-register.md`: `COD-218-2008` are consolidare
viitoare, dar dispozițiile afectate sunt arts. 313^2, 313^4, 313^5, 313^6 și 330^2; **arts. 177 și
179 sunt citabile astăzi**.

Ce adaugă codul este consecința, nu sancțiunea: **art. 327 alin. (1)** trimite procesul-verbal de
contravenție instanței, care „va dispune, inclusiv ca măsură de siguranță, demolarea/demontarea".
Demolarea este judiciară, grefată pe procedura contravențională. **Art. 385 alin. (2)** închide
regularizarea retroactivă: obținerea autorizației în cursul sau după execuție nu înlătură
caracterul ilicit.

**Codul civil `CC-1107-2002`.** Termenul de garanție de 5 ani din art. 225 alin. (1) al codului
(curge de la recepția la terminarea lucrărilor) și termenul de 5 ani din art. 1126 alin. (1)
lit. b) CC (termen de descoperire și notificare a viciilor, curge de la intrarea în posesie) sunt
**paralele, nu cumulative**. Veriga: **art. 1374 alin. (1) CC** aplică arts. 1126 și 1127 „în mod
corespunzător în privința viciilor lucrării", deci și în antrepriză; alin. (2) mută punctul de
plecare la recepția lucrării în ansamblu când recepția se face pe părți. Concursul dintre norma
specială ulterioară și norma civilă nu este tranșat de texte. `[de verificat]`

### O.8. Metodă și integritate

Ambele acte ingerate cu `_meta/imports/moldova-legal/ingest_business_law.py`, verificate cu
`verify_business_law.py`: **integritate de text PASS**, 3.640/3.640 de linii pentru cod și 779/779
pentru hotărâre, deci s-au adăugat numai ancore. Codul: 59 `<sup>`, toate la nivel de alineat sau
literă, 390 de ancore, numerotare 1–390 completă, fără duplicate, fără lacune, fără articole cu
exponent — singurul act din corpus cu numerotare perfect continuă la această scară. Hotărârea:
29 `<sup>` devenite `^N` (19 apariții), zero ancore de articol.

**Două corecturi de unealtă făcute în aceeași sesiune, ambele documentate în scripturi:**

1. `fetch()` din scriptul de ingerare scria răspunsul `curl` **direct peste fișierul din cache**.
   Cum legis.md întoarce pagina de verificare Cloudflare cu `rc=0`, o rulare blocată ar fi
   înlocuit HTML-ul bun cu pagina de verificare, distrugând singura copie a sursei. Acum se
   descarcă într-un fișier temporar și se promovează doar la reușită, cu revenire pe cache.
2. Controlul „superscript articles" din `verify_business_law.py` căuta exponenții **în tot
   HTML-ul**, deci prindea și trimiterile la articolele altor acte. La cod raporta FAIL cerând
   ancore pentru „13^1" și „28^1", care sunt, toate trei potrivirile, în blocul de modificare a
   altor legi de la finalul actului: „Articolul 13^1 din Legea nr. 1134/1992", textul nou citat
   între ghilimele introdus în acea lege, și „Articolul 28^1 se abrogă" din Legea 163/2010.
   Niciunul nu este articol al codului. Controlul compară acum cu liniile de referință extrase din
   HTML **care încep** cu „Articolul N^M", deci rămâne independent de markdownul scris de noi, iar
   potrivirile din interiorul frazei se raportează separat, ca informație. Regresie verificată pe
   toate cele 21 de acte: **FAILURES: 0**, seturile de exponenți neschimbate, inclusiv cele 159 ale
   Codului fiscal cu forma `54^1/1` și cele 254 ale Codului contravențional.

Ruta de descărcare: legis.md stă în spatele unei verificări Cloudflare care blochează `curl`.
HTML-ul a fost luat din Chrome, după ce Eugen a trecut verificarea, printr-un `fetch` same-origin
care întoarce **octeții serverului**, nu DOM-ul serializat ca la P8 — deci markupul `<sup>` este
exact cel servit, ceea ce extractorul scris pentru `curl` și aștepta.

### O.9. Ce rămâne deschis

1. **Rezolvat în aceeași zi — vezi O.10.** Este `HG-582-2022`, doc_id 152829, ingerată. Termenele
   de demolare sunt ancorate. Afirmația de mai sus, că actul „nu a fost identificat prin căutare
   în titlu", era **neverificată**: acea căutare nu fusese rulată. Se păstrează aici, tăiată, ca
   dovadă a erorii, nu ștearsă.
2. **Rezolvat în aceeași zi — vezi P.** `L-1543-1998` este ingerată, doc_id 150226. Răspunsul
   este da: art. 40^4 alin. (1) face din documentele de recepție o condiție cumulativă de
   înregistrare, alături de dreptul asupra terenului.
3. **Certificatele de urbanism emise sub Legea 163/2010** înainte de 30.01.2025: codul nu conține
   nicio normă tranzitorie despre ele. Art. 388 alin. (3) privește documentația de urbanism, care
   este alt lucru. `[de verificat]`
4. **Celelalte regulamente delegate de cod** (arts. 103, 107, 111, 150 alin. (8), 322 alin. (4))
   nu au fost căutate. Perimetrul actelor subordonate este mai larg decât cele două ingerate.
5. **Anexele codului**, vezi O.5.

6. **Registrul in-force etichetează greșit dispoziția amânată a hotărârii.**
   `_meta/inforce/in-force-register.md` listează „**HG-743-2024 art. 355**". Actul are **zero**
   ancore de articol; 355 este numărul de articol al **Monitorului Oficial** din citarea
   modificării, „MO284-287/30.06.26 art.355", pe care parserul l-a luat drept dispoziție a
   actului. Efectul nu ascunde nimic — actul e semnalat corect ca având consolidare viitoare, iar
   liniile indicate sunt corecte — dar numește o dispoziție inexistentă. Este primul act structurat
   în puncte cu consolidare viitoare din corpus, deci prima dată când defectul se poate vedea.
   Fișierul e generat, iar scriptul e comun tuturor actelor: **nu se corectează aici**, se ridică
   cu Eugen. `[de verificat]`


### O.10. Regulamentul de demolare — găsit în aceeași zi (HG-582/2022)

Întrebarea deschisă nr. 1 de la O.9 este închisă. Regulamentul la care trimit art. 322 alin. (4)
și art. 328 alin. (1) și (2) din `COD-434-2023` este **HG 582/2022 pentru aprobarea Regulamentului
cu privire la modul de demolare a construcțiilor neautorizate și de defrișare a arborilor și
arbuștilor**, doc_id 152829, MO 2022 nr. 274–277 art. 682, în vigoare de la publicare, **fără dată
de abrogare**, consolidare 2026-03-01 (trecută).

**Corectură de consemnare, făcută înainte de orice altceva.** O.9 punctul 1 spunea că actul „nu a
fost identificat pe legis.md prin căutare în titlu". Afirmația era neverificată: **căutarea în
titlu după „demolare" nu fusese rulată**. Când a fost rulată, `search_type=1`, fraza „demolare a
constructiilor neautorizate" fără diacritice, a întors **un singur rezultat**, chiar actul căutat.
Ipoteza scrisă atunci, că actul „poartă un titlu care nu conține cuvântul", era exact pe dos:
titlul reia aproape cuvânt cu cuvânt formula delegării. Regula care se desprinde: **o negație nu
se scrie decât după căutarea care o susține**, altfel închide un drum care era deschis.

**Capcana reală era alta: actul nu este emis în temeiul codului.** Clauza lui de adoptare spune
„În temeiul **art. 439^6 alin. (5) din Codul contravențional** nr. 218/2008". Este anterior codului
și a fost adoptat pentru executarea măsurii de siguranță a demolării dispuse de instanță — exact
configurația pe care codul o construiește în art. 327 alin. (1). Deci delegarea din art. 322
alin. (4) este împlinită de un act care nu o invocă, iar o căutare după temeiul legal presupus
**nu l-ar fi găsit niciodată**.

Lanțul este acum ancorat cap la cap, toate verigile în vault:

| verigă | unde | ce spune |
|---|---|---|
| fapta | `COD-218-2008` art. 179 | construcție fără autorizație, amendă 250–400 u.c. persoanei fizice |
| măsura | `COD-218-2008` art. 439^6 alin. (1) | demolarea se aplică inclusiv pentru art. 179 |
| cine o dispune | `COD-218-2008` art. 439^6 alin. (3) | instanța; **supraviețuiește** încetării procesului contravențional (art. 441 alin. (1) lit. f)) și înlăturării răspunderii (art. 26) |
| cine o execută | `COD-218-2008` art. 439^6 alin. (4) | contravenientul, ori APL din contul proprietarului |
| delegarea | `COD-218-2008` art. 439^6 alin. (5) | modul se stabilește de Guvern |
| oglinda în cod | `COD-434-2023` arts. 327 alin. (1), 328 | aceeași construcție, cu trimitere la „regulamentul aprobat de Guvern" |
| regulamentul | `HG-582-2022` | actul ingerat |

Verificat în registrul dispozițiilor neintrate în vigoare: **art. 439^6 nu figurează**, deci este
citabil astăzi, ca și arts. 177 și 179.

**Termenele cerute de art. 328 alin. (1),** acum ancorate: executarea lucrărilor **nu poate depăși
12 luni** la demolare și 6 luni la defrișare, prelungire numai din motive tehnologice prevăzute în
documentația de proiect (pct. 3, definiții); prescripția de conformare se comunică în **trei zile**
(pct. 4); răspunsul la prescripție are **trei zile**, iar **lipsa lui declanșează direct dispoziția
de executare silită** (pct. 5); dispoziția se comunică în trei zile lucrătoare (pct. 9).

**Acoperă și demontarea**, deși titlul spune doar „demolare": pct. 4 numește
„demolarea/demontarea/defrișarea", iar pct. 20 subpct. 3) „demontarea instalațiilor și utilajelor
tehnologice". Titlul e mai îngust decât conținutul.

**Aliniat la cod prin HG27/2026**, în vigoare 01.03.26: la pct. 20 subpct. 1) trimiterea la art. 17
alin. (1) lit. f) din Legea 163/2010 a fost înlocuită cu art. 153 alin. (1) lit. e) din cod.
Fișierul nu mai conține nicio trimitere la legea abrogată. Alinierea s-a făcut cu 13 luni după
intrarea în vigoare a codului.

**Citare:** act în puncte, 34 de puncte, **zero ancore**, numerotarea repornește între hotărâre
(pct. 1–2) și Regulament, deci punctele 1 și 2 apar de două ori. „pct. N" nu este ancorat. Cele
trei anexe — modelele de prescripție, dispoziție și proces-verbal — **sunt** în text, spre
deosebire de anexele codului.

**Integritate:** 125/125 de linii, PASS. Cele 7 `<sup>` au devenit `439^6` (4 apariții) și `134^1`
(3), cu **zero** apariții ale formei aplatizate „4396" — care ar fi transformat chiar temeiul legal
al actului într-o citare falsă.

**Ce rămâne deschis aici:** art. 328 alin. (1) și (2) trimit la regulament și pentru **remedierea**
construcțiilor afectate de intervenții neautorizate, iar regulamentul reglementează demolarea și
defrișarea, nu remedierea; dacă termenele de remediere sunt cele de demolare prin asimilare nu
rezultă din text. Și contestarea dispoziției de executare silită nu e reglementată, rămâne dreptul
comun al `COD-116-2018`. `[de verificat]`

## P. Legea cadastrului bunurilor imobile — L-1543/1998 (ingerată 2026-09-05)

Închide întrebarea deschisă nr. 2 de la O.9: `COD-434-2023` trimite la această lege în art. 387
alin. (3), iar legătura dintre procesul-verbal de recepție și înscrierea dreptului în Registrul
bunurilor imobile nu putea fi ancorată fără ea. doc_id 150226, în vigoare din 21.05.1998,
**republicată** 02.04.2021 (MO 88–95 art. 79), fără dată de abrogare.

### P.1. Capcană de titlu

legis.md dă denumirea ca „LEGE Nr. 1543 din 25.02.1998 **cadastrului bunurilor imobile**" — fără
„Legea", care stă în câmpul TIPUL, și fără „privind". **O căutare în titlu după fraza „Legea
cadastrului bunurilor imobile" nu o întoarce.** Căutarea după „cadastrul bunurilor imobile" dă 65
de rezultate, aproape toate acte de modificare pe șapte pagini; actul de bază este singurul rând cu
prefixul **LP1543**. Este a treia capcană de denumire din corpus, după `L-284-2004` (titlu schimbat)
și `L-550-1995` (titlu schimbat), dar de alt tip: aici titlul nu s-a schimbat, doar este **trunchiat
în fișă**, cu primul cuvânt mutat în câmpul de tip.

### P.2. Răspunsul: recepția ESTE condiție de înregistrare

`art. 40^4 alin. (1)`: „Construcția construită se înregistrează ca proprietate a beneficiarului
(investitorului) construcției dacă anterior sau concomitent se înregistrează dreptul de proprietate
sau superficie asupra terenului al beneficiarului (investitorului) construcției **și se prezintă
documentele ce confirmă recepția lucrărilor de construcție**."

Două condiții **cumulative**: dreptul asupra terenului, și documentele de recepție. Legea nu spune
„proces-verbal de recepție", ci folosește categoria generică; actul concret este cel din
`COD-434-2023` art. 193 alin. (1).

| situație | ce se cere | temei |
|---|---|---|
| construcție finalizată | drept asupra terenului **+** documentele de recepție | `L-1543-1998` art. 40^4 alin. (1) |
| construcție nefinalizată | drept asupra terenului **+** autorizația **+** avizul tehnic al expertului atestat; grad de executare **nu mai mic de planșeul la cota 0.000** | art. 40^4 alin. (2) |
| case vechi din registrele gospodăriilor, anterioare Legii 835/1996 | extrasul din acele registre | art. 40^4 alin. (3), la care trimite art. 387 alin. (3) din cod |
| construcții neautorizate funcționale la 30.01.2024 | declarație notarială + certificat APL, cu notare permanentă; **până la 30.01.2028** | `COD-434-2023` art. 387 alin. (4) |

Alin. (2) este perechea exactă a art. 351 alin. (3) din cod, care spune că avizul tehnic „este
întocmit **în scopul înregistrării construcției nefinalizate** în Registrul bunurilor imobile şi nu
poate fi utilizat în alte scopuri". Codul spune la ce servește avizul; legea cadastrului spune ce
prag trebuie să atingă. Cele două se confirmă reciproc.

Verificat în `_meta/inforce/in-force-register.md`: **art. 40^4 nu figurează** printre dispozițiile
amânate, deci este în vigoare astăzi, deși actul are consolidare viitoare.

### P.3. Consolidare viitoare

**2027-01-01** (LP176 din 03.07.25), cu **6 dispoziții** care nu sunt încă în vigoare: arts. **15^3,
15^4, 15^5, 15^6, 15^7, 15^8**, toate „introduse", toate „în vigoare 01.01.27". Sunt în materia
**inginerului cadastral certificat**, nu în materia înregistrării drepturilor, deci nu ating
răspunsul de la P.2. Registrul le listează individual, cu numărul de linie — spre deosebire de
`HG-743-2024`, unde marcajele în puncte nu se pot dezambigua (vezi O.5).

Notă de sursă, păstrată fiindcă textul brut este imuabil: marcajul art. 15^6 este scris
`[Art.15^6introdus prin LP176…]`, lipit, fără spațiu după exponent. Greșeală a sursei, nu a
extracției; ancora articolului este corectă.

### P.4. Structură și integritate

99 de ancore: **61 de articole de bază, numerotate 1–61 fără nicio lacună**, plus 38 cu exponent
(10^1, 12^1, 15^1–15^8, 30^1, 33^1, 37^1, 40^1–40^9, 41^1, 42^1, 46^1–46^10, 47^1, 55^1, 55^2,
56^1); opt capitole. Cele 129 de etichete `<sup>` s-au rezolvat în cele 38 de articole cu exponent,
care se potrivesc exact cu sursa, plus 78 de exponenți la nivel de alineat și literă păstrați în
corp. Fără span-uri ridicate prin CSS, fără CUPRINS, fără duplicate.

Verificată cu `verify_business_law.py`: **integritate de text PASS, 1.038 de linii scrise față de
1.038 de referință**, deci s-au adăugat numai ancore.

### P.5. Ce rămâne deschis

1. **Codul și legea cadastrului nu se citează reciproc** exact în punctul care contează. Art. 40^4
   alin. (1) cere „documentele ce confirmă recepția" fără trimitere la art. 193 din cod; codul
   descrie procesul-verbal fără trimitere la art. 40^4. Îmbinarea se face prin categorii. Consecința
   practică: la **recepția în două etape** (art. 192 alin. (9) din cod, obligatorie la finanțare
   publică), nu rezultă din text dacă procesul-verbal la terminarea lucrărilor este suficient pentru
   înregistrare, sau se cere și cel final. `[de verificat]`
2. **Autorizația de construire nu este cerută expres pentru construcția finalizată.** Art. 40^4
   alin. (2) o cere explicit pentru cea nefinalizată; alin. (1) nu o menționează. Ea intră indirect,
   fiindcă art. 193 alin. (2) din cod spune că actul de recepție certifică îndeplinirea obligațiilor
   „ale proiectului de execuție verificat şi ale autorizației de construire". Cine verifică
   autorizația la înregistrare — registratorul, ori comisia de recepție înaintea lui — nu este
   împărțit de niciun text. `[de verificat]`

## Q. Constituția Republicii Moldova — CONST-1994 (ingerată 2026-09-06)

Pasul 3 al planului `_meta/plans/2026-09-06-plan-extindere-perimetru-domestic.md`: nivelul 1 al
ierarhiei surselor, absent din bază până acum. **Prefix nou `CONST-`**, consemnat aici la momentul
ingerării. Pagina wiki: [[CONST-1994]].

| ID raw | doc_id | Titlu detectat | Pagină wiki | Consolidare / versiune locală | Rol operațional |
|---|---:|---|---|---|---|
| `CONST-1994` | **145723** | CONSTITUŢIA Nr. 1 din 29.07.1994 CONSTITUŢIA REPUBLICII MOLDOVA* (republicată) | [[CONST-1994]] | **2024-11-05** (LP244/2024); versiunea legis.md este datată 2024-11-13, data republicării | legea supremă; ierarhia actelor (art. 72, 76, 102), accesul la justiție (art. 20), instanțele (art. 114–116), Curtea Constituțională (art. 134–140), revizuirea (art. 141–143) |

### Q.1. Cum a fost găsită și verificată

Căutare în titlu, fără diacritice, `search_string=constitutia republicii moldova&search_type=1`:
**234 de rezultate pe 12 pagini**, sortate descrescător după dată, aproape toate legi de modificare,
avize și decizii ale Curții Constituționale, hotărâri de Guvern de aprobare a proiectelor. Actul de
bază este **singurul rând cu prefixul CRM** (`CRM1/1994`) și stă pe ultima pagină, fiind cel mai
vechi. Lista de rezultate este randată de client și ține toate cele 234 de rânduri în DOM, deci
filtrarea s-a făcut pe pagină, nu prin paginare.

Verificat pe pagina actului (`showdetails/145723`), nu din listă: tipul CONSTITUŢIA, autoritatea
PARLAMENTUL, adoptată 29.07.1994, **republicată 13.11.2024 în MO nr. 466 art. 635**, „Data
abrogării: -", istoric de **19 versiuni** din care 145723 este cea mai nouă (145723@2024-11-13;
anterioare 145630@2024-11-05, 142462@2024-03-11, 136130@2023-03-24, 128016@2022-04-01,
111918@2019-01-14, 99183@2017-05-19, 96446@2016-11-29, 91571@2016-03-29 ...).

HTML-ul a fost adus prin `fetch` same-origin din pagina deschisă în Chrome, după ce Eugen a trecut
verificarea Cloudflare, și descărcat ca blob cu acordul lui explicit (octeții serverului, nu DOM-ul
serializat). Pus în `_meta/imports/moldova-legal/legis-md-business/showdetails-145723.html`,
280.116 octeți; `ingest_business_law.py` l-a luat din cache.

### Q.2. Structură și integritate

**157 de ancore**: 143 de articole de bază, **numerotate 1–143 fără nicio lacună** — arts. 82 și
83 sunt prezente ca stub, `Articolul 82 - abrogat.` și `Articolul 83 - abrogat.` —, 6 cu exponent
(**59^1, 106^1, 106^2, 121^1, 125^1, 140^1**, care se potrivesc exact cu sursa) și **8 articole cu
cifre romane, I–VIII**, dispozițiile finale și tranzitorii, prinse de regexul de ancorare la fel
ca la `L-177-2025` și `L-178-2020`. 8 titluri (I–VII și V^1), capitole (inclusiv III^1, Avocatul
Poporului), secțiuni. 11 etichete `<sup>` rezolvate; fără span ridicat prin CSS; fără CUPRINS.

Verificată cu `verify_business_law.py`: **integritate de text PASS, 883 de linii scrise față de
883 de referință**, deci s-au adăugat numai ancore; fără duplicate, fără lacune, frontmatter complet.

### Q.3. Trei particularități de sursă, de știut înainte de a cita

1. **Titlul articolului stă pe linia următoare ancorei.** Sursa scrie `Articolul 76` și, pe rândul
   de sub el, `Intrarea în vigoare a legii`. Ancorele sunt deci `## Articolul N` fără titlu, la toate
   cele 143 de articole (verify raportează „fara punct dupa numar" pentru fiecare, ceea ce este
   corect, nu un defect). La art. 8 și art. 54 titlul se întinde pe două linii. O căutare după
   titlu trebuie să citească linia de după ancoră.
2. **Niciun marcaj de modificare în text.** Zero linii `[Art.N ... prin LP...]`: republicarea le-a
   eliminat pe toate. Istoricul stă doar în fișă, 17 intrări: LP244/2024, HCC8/2024, LP52/2023,
   LP120/2021, LP255/2018, LP70/2017, LP256/2016, republicarea din 29.03.2016, HCC7/2016,
   LP185-XVI/2006, LP344-XV/2003, LP1471-XV, LP1470-XV, LP1469-XV/2002, LP351-XV/2001,
   LP1115-XIV/2000, LP957-XIII/1996. Două dintre ele sunt **hotărâri ale Curții Constituționale**.
   Este mecanismul 2 din întrebarea deschisă 3 a `CLAUDE.md`, pe tot actul.
3. **Data intrării în vigoare din fișă (19.08.1994) contrazice textul (27.08.1994).** Art. I
   alin. (2): „Constituţia Republicii Moldova intră în vigoare la 27 august 1994." Textul are
   prioritate. Aceeași clasă de capcană ca la `COD-434-2023` art. 390 (secțiunea O).

Consolidarea este derivată din rândul „Data modificării" al fișei, fiindcă republicarea nu are nici
rândul MODIFICAT, nici „Versiune în vigoare din"; antetul spune „Modificată şi completată prin
legile Republicii Moldova:" urmat de listă. Rezultă **2024-11-05** (intrarea în vigoare a LP244),
nu 2024-11-13 (data republicării). Ambele sunt trecute.

### Q.4. Corecție de metodă făcută cu această ocazie

Art. VIII din dispozițiile finale are ca text întreg fraza „Titlul VII, Dispoziţii finale şi
tranzitorii, se consideră parte integrantă a prezentei Constituţii şi reglementează problemele ce
ţin de intrarea ei în vigoare." Regula veche de ancorare a titlurilor, orice linie care începe cu
`Titlul `, a luat-o drept titlu de structură: **art. VIII apărea gol, iar textul lui apărea ca
`## Titlul VII, ...`**. Textul nu era atins (verify PASS), structura era falsă. Regula din
`ingest_business_law.py` cere acum un numeral roman după `Titlul` urmat de graniță de cuvânt și
refuză virgula imediat după el; prima variantă fără `\b` lăsa regexul să dea înapoi de la „VII" la
„VI" și tot trecea. Reingerat; 8 titluri reale, art. VIII cu textul lui. Regresie: nicio ancoră
`## Titlul`/`## TITLUL` existentă în `moldova-legal/` sau `cnpf/` nu ar fi pierdută de regula nouă
(verificat prin grep pe toate fișierele brute).

## R. Lotul A, corporativ — L-149/2012, L-160/2011, L-131/2012 (ingerate 2026-09-06)

Pasul 4, lotul A al planului `_meta/plans/2026-09-06-plan-extindere-perimetru-domestic.md`. Toate
trei găsite prin căutare în titlu fără diacritice, verificate pe pagina actului (istoric de versiuni,
fișă), aduse prin `fetch` same-origin din Chrome și descărcate ca blob cu acordul lui Eugen.

| ID raw | doc_id | Titlu detectat | Pagină wiki | Consolidare / versiune locală | Rol operațional |
|---|---:|---|---|---|---|
| `L-149-2012` | **152605** | LEGE Nr. 149 din 29.06.2012 insolvabilităţii | [[L-149-2012]] | **2025-12-31** (LP330/2025) | procedura colectivă: restructurare și faliment; instanța de insolvabilitate; administratorul |
| `L-160-2011` | **156152** | LEGE Nr. 160 din 22.07.2011 privind reglementarea prin autorizare a activităţii de întreprinzător | [[L-160-2011]] | **2029-01-01 — VIITOARE** (LP159/2026) | actele permisive, Nomenclatorul, ghișeul unic, SIA GEAP |
| `L-131-2012` | **151146** | LEGE Nr. 131 din 08.06.2012 privind controlul de stat | [[L-131-2012]] | **2026-08-28** (LP201/2025) | controlul de stat asupra întreprinzătorilor: principii, planificare pe riscuri, delegația de control |

### R.1. Capcană de listă, nouă: rândul din rezultate nu trimite la consolidarea curentă

La `L-131-2012`, rândul din lista de rezultate trimite la **doc_id 152529** (2025-12-31). Pagina
actului arată însă două consolidări mai noi: 149634@2026-07-31 și **151146@2026-08-28** (LP201 din
10.07.25, în vigoare 28.08.26), aceasta din urmă fiind cea în vigoare azi. Și **doc_id-ul curent
este mai mic decât cel vechi**: numărul doc_id nu este cronologic. Regula care rezultă: doc_id-ul
din lista de căutare se ia doar ca intrare în pagina actului; ce se ingerează este cel din capul
istoricului de versiuni. Fișierul 152529 descărcat înainte de a observa aceasta a rămas în
`Downloads` și nu a fost pus în cache.

### R.2. Fișele contrazic textul la intrarea în vigoare, de două ori

| act | fișa: „Data intrării în vigoare" | textul | publicat |
|---|---|---|---|
| `L-131-2012` | **31.01.2012** | art. 33 alin. (1): „la 6 luni de la data publicării" | 31.08.2012, deci în vigoare la sfârșitul lui februarie 2013 |
| `L-160-2011` | **01.01.2012** | art. 14: „la 6 luni de la data publicării", cu excepția art. 13 alin. (1) (la publicare) și art. 11 alin. (6) (1 februarie 2012) | 14.10.2011, deci regula generală dă aprilie 2012 |
| `L-149-2012` | 13.03.2013 | art. 254 alin. (1): „la expirarea a 180 de zile de la data publicării" | 14.09.2012; **concordă** |

Fișa `L-131-2012` dă o dată **anterioară publicării**. Textul are prioritate, ca la `CONST-1994`
(Q.3) și `COD-434-2023` (O). `[de verificat]` pe niciunul: textul e limpede, fișa e greșită.

### R.3. `L-160-2011`: consolidare viitoare cu marcaje pierdute

Consolidarea este **2029-01-01**, iar între azi și ea istoricul de versiuni mai are două trepte:
154051@2027-01-23 și 154478@2027-05-21. Fișierul poartă însă **un singur marcaj** de dispoziție
amânată: `[Anexa nr.1 modificată prin LP159 din 30.07.26 ...; în vigoare 01.01.29]`. Marcajele
amendamentelor care intră în vigoare în 2027 au fost eliminate de consolidarea din 2029 —
mecanismul 1 din întrebarea deschisă 3 a `CLAUDE.md`. **Registrul in-force listează deci numai
anexa nr. 1 și nu poate vedea dispozițiile din 2027.** Pentru orice citare din această lege între
azi și 2029, istoricul de versiuni de pe legis.md este singura sursă a datei de intrare în vigoare.
Anexele (Nomenclatorul actelor permisive, anexele 1–4) apar în text doar ca titluri, fără conținut
tabelar extras.

**Urmare, 6 septembrie seara (decizia lui Eugen):** actul a fost reingerat la **151257 @
2026-08-29** (LP199 din 10.07.25, anexa nr. 1), versiunea în vigoare azi; consolidarea din 2029
este arhivată la `_archive/raw/moldova-legal-lot2-legis-md-before-refresh-20260906-221015/`.
Istoricul citit integral are **cinci** consolidări viitoare, nu două: 149496@2026-12-28,
150231@2027-01-01, 154051@2027-01-23, 154478@2027-05-21, 156152@2029-01-01. Inventarul de
articole este același (14 + 18), integritatea PASS pe 349 de linii. Registrul in-force nu mai
listează actul, corect: textul deținut nu conține nicio dispoziție amânată. Paragraful de mai sus
rămâne valabil ca descriere a versiunii arhivate.

### R.4. Structură și integritate

| act | ancore | de bază | cu exponent | capitole | `<sup>` | linii verify |
|---|---:|---|---|---:|---:|---|
| `L-149-2012` | **271** | 254, numerotate 1–254 fără lacune | 17: 48^1, 235^1–235^16 | 16 | 55 | PASS, 2.183 / 2.183 |
| `L-160-2011` | **32** | 14, numerotate 1–14 fără lacune | 18: 4^1, 4^2, 6^1, 6^2, 11^1, 12^1–12^13 | 5 | 51 | PASS, 349 / 349 |
| `L-131-2012` | **41** | 33, numerotate 1–33 fără lacune | 8: 3^1, 3^2, 5^1, 19^1, 29^1, 31^1, 31^2, 32^1 | 4 | 47 | PASS, 506 / 506 |

Fără span ridicat prin CSS, fără CUPRINS, fără duplicate, fără forma `N^X/Y`, toate titlurile cu
punct după număr. La `L-131-2012` titlul art. 1 se întinde pe două linii („Scopul, obiectul de
reglementare / şi domeniul de aplicare a prezentei legi"), deci ancora ține doar prima jumătate;
este cazul de titlu tăiat din „Outstanding work" 2 al `CLAUDE.md`, nu un defect nou. Legea
insolvabilității are HTML de 1 MB, cel mai mare act de lege din corpus după coduri.

O verificare prealabilă pe textul HTML cu etichetele scoase raportase lacune și duplicate în toate
trei (de exemplu „max 23516" la insolvabilitate). Erau exponenți neresolvați lipiți de număr, adică
exact clasa de eroare consemnată la `L-235-2006` (E): o lacună se confirmă pe ancorele scrise de
extractor, nu pe text cu etichetele șterse. Ancorele nu au nicio lacună.

## S. Lotul B, administrativ — L-436/2006, L-158/2008, L-148/2023, L-131/2015 (ingerate 2026-09-06)

Pasul 4, lotul B. Aceeași metodă ca la lotul A (R): căutare în titlu fără diacritice, verificare pe
pagina actului, `fetch` same-origin din Chrome, descărcare blob cu acordul lui Eugen.

| ID raw | doc_id | Titlu detectat | Pagină wiki | Consolidare / versiune locală | Rol operațional |
|---|---:|---|---|---|---|
| `L-436-2006` | **155118** | LEGE Nr. 436 din 28.12.2006 privind administraţia publică locală | [[L-436-2006]] | **2026-06-26** (LP108/2026) | autoritățile locale de nivelul întâi și al doilea, primarul, consiliile; temeiul art. 109 din [[CONST-1994]] |
| `L-158-2008` | **155439** | LEGE Nr. 158 din 04.07.2008 cu privire la funcţia publică şi statutul funcţionarului public | [[L-158-2008]] | **2026-09-13 — VIITOARE** (LP154/2026), 29 de dispoziții amânate | raporturile de serviciu, funcția publică |
| `L-148-2023` | **137908** | LEGE Nr. 148 din 09.06.2023 privind accesul la informațiile de interes public | [[L-148-2023]] | 2024-01-08, **nemodificată** | accesul la informații, obligațiile furnizorilor, contenciosul |
| `L-131-2015` | **155117** | LEGE Nr. 131 din 03.07.2015 privind achiziţiile publice | [[L-131-2015]] | **2026-06-26** (LP101/2026); **abrogată de la 01.01.2027** | achizițiile publice până la 31.12.2026 |

### S.1. `L-131-2015` este marcată „Abrogat" pe legis.md, cu Data abrogării 01.01.2027

Rândul din lista de rezultate poartă eticheta **Abrogat**, iar fișa dă **Data abrogării
01.01.2027**. Actul este încă în vigoare azi, versiunea 155117@2026-06-26 (LP101 din 04.06.26), și
istoricul mai are o versiune 153138@2027-01-01, cea de după abrogare. Succesoarea, găsită în
aceeași listă de rezultate: **Legea nr. 325 din 29.12.2025 privind achizițiile publice** (LP325/2025,
doc_id 152974), însoțită de **Legea nr. 20 din 26.02.2026 privind remediile și căile de atac în
materie de atribuire a contractelor de achiziții publice** (LP20/2026, doc_id 153618). Niciuna nu
este în planul aprobat, deci niciuna nu a fost ingerată; **decizia este a lui Eugen**. Până la ea,
orice răspuns pe achiziții publice spune că legea citată expiră la 31.12.2026 și că regimul de după
este în 325/2025. Textul poartă o linie de abrogare a vechii Legi 96-XVI/2007 („La data intrării
în vigoare a prezentei legi, Legea nr. 96-XVI din 13 aprilie 2007 ... se abrogă"), găsită prin
căutare în text; articolul care o conține nu a fost identificat pentru manifest, iar art. 91 este
„Organizarea executării", nu abrogarea.

**Urmare, 6 septembrie seara:** amândouă ingerate, la decizia lui Eugen; vezi secțiunea U. Două
lucruri schimbă citirea acestei legi. Legea 20/2026 este **în vigoare din 01.04.2026** și anexa ei
(pct. 2) a abrogat art. 80–84 și 86–88 și a rescris art. 32 și 85, deci contestațiile au ieșit
din 131/2015 cu nouă luni înaintea abrogării legii; textul nostru 155117 poartă stub-urile. Iar
art. 91 din 325/2025 lasă procedurile și contractele în curs la 01.01.2027 sub legea de la data
inițierii.

### S.2. `L-158-2008`: consolidare care intră în vigoare peste o săptămână, plus una în 2028

Rândul din listă trimite la 156075 (2026-08-28, LP197/2026, în vigoare azi). Istoricul are două
consolidări mai noi: **155439@2026-09-13** (LP154 din 30.07.26, MO375-378/13.08.26 art. 393) și
155884@2028-07-01. S-a ingerat 155439, cum s-a făcut la `COD-218-2008`, care are aceeași lege și
aceeași dată: intră în vigoare la 13.09.2026, iar registrul in-force preia cele **29 de
dispoziții amânate** (clauza de armonizare, arts. 4, 5, 8, 12, 20, 22, 24, 25, 27, 30, 32, 38, 42,
47, 49, 56, 57, 65^1), toate marcate individual în text. Versiunea din 2028 rămâne viitoare și
neingerată. Fișierul 156075 descărcat înainte de alegere a rămas în `Downloads`, nefolosit. **După
13.09.2026 avertismentul de consolidare viitoare din fișier devine caduc**; nu se rescrie fișierul,
se citește data.

### S.3. `L-148-2023`: nemodificată, fără rândul MODIFICAT

O singură versiune pe legis.md, zero etichete `<sup>`. Consolidarea iese din „Data intrării în
vigoare" a fișei, 08.01.2024, ca la `HG-574-2024` (regula din E). Este legea care a înlocuit Legea
982/2000 privind accesul la informație; abrogarea aceleia nu a fost citită pe text pentru manifest.
Art. 35 ține cererile și acțiunile anterioare pe legea veche.

### S.4. Structură și integritate

| act | ancore | de bază | cu exponent | capitole | `<sup>` | linii verify |
|---|---:|---|---|---:|---:|---|
| `L-436-2006` | **98** | 92, numerotate 1–92 fără lacune | 6: 10^1, 10^2, 59^1–59^3, 72^1 | 15 | 88 | PASS, 855 / 855 |
| `L-158-2008` | **88** | 77, numerotate 1–77 fără lacune | 11: 19^1, 19^2, 27^1, 38^1, 42^1, 49^1, 52^1, 54^1, 65^1, 69^1, 73^1 | 9 | 71 | PASS, 967 / 967 |
| `L-148-2023` | **35** | 35, numerotate 1–35 fără lacune | 0 | 7 | 0 | PASS, 301 / 301 |
| `L-131-2015` | **91** | 91, numerotate 1–91 fără lacune | 0 | 11 | 7 | PASS, 1.331 / 1.331 |

Fără span ridicat prin CSS, fără CUPRINS, fără duplicate. Titluri tăiate pe două linii, cazul
cunoscut: `L-436-2006` art. 3 („Principiile de bază ale administrării / publice locale"). `L-436-2006`
art. 92 și `L-158-2008` art. 77 sunt articole fără titlu (`Articolul 92`, `Articolul 77.`), prinse
de contorul reparat la 2026-09-05. Anexele 1 și 2 ale `L-131-2015` apar doar ca titluri.

## T. Lotul C, profesia — L-1260/2002, L-198/2007, L-514/1995, UA-STATUT-2011 (ingerate 2026-09-06)

Pasul 4, lotul C. Aceeași metodă ca la R și S. **Prefix nou `UA-`** pentru actele Uniunii
Avocaților, consemnat aici la momentul ingerării (D5 din plan).

| ID raw | doc_id | Titlu detectat | Pagină wiki | Consolidare / versiune locală | Rol operațional |
|---|---:|---|---|---|---|
| `L-1260-2002` | **146148** | LEGE Nr. 1260 din 19.07.2002 cu privire la avocatură | [[L-1260-2002]] | **2025-01-07** (LP284/2024), versiunea **în vigoare azi**; o consolidare condiționată de aderarea la UE (153429, LP10/2026) neingerată | profesia de avocat, admiterea, stagiul, formele de organizare |
| `L-198-2007` | **155726** | LEGE Nr. 198 din 26.07.2007 cu privire la asistenţa juridică garantată de stat | [[L-198-2007]] | **2026-08-06** (LP126/2026) | asistența juridică garantată de stat, avocatul public, para-juristul |
| `L-514-1995` | **156079** | LEGE Nr. 514 din 06.07.1995 privind organizarea judecătorească* | [[L-514-1995]] | **2026-08-28** (LP197/2026) | instanțele, președinții, CSJ, curțile de apel, judecătoriile |
| `UA-STATUT-2011` | **134919** | STATUTUL Nr. 0 din 29.01.2011 STATUTUL PROFESIEI DE AVOCAT | [[UA-STATUT-2011]] | **2022-05-27** (HUA19-01/2022) | statutul profesiei; act al Uniunii Avocaților, pe articole |

### T.1. Legea avocaturii: consolidarea „la data aderării la UE" este codificată 2030-01-01

Rândul din listă trimite la **153429**, a cărui dată de versiune pe legis.md este **2030-01-01**.
Nu este o dată reală: rândul MODIFICAT al acelei versiuni spune „LP10 din 12.02.26, MO112-115/12.03.26
art.91, **în vigoare la data aderării Republicii Moldova la Uniunea Europeană**", iar legis.md
codifică condiția cu o dată fictivă. Aceeași codificare apare în sondajul de actualitate la
`COD-218-2008` (154803@2030-01-01, LP82/2026). S-a ingerat **versiunea în vigoare azi, 146148**
(2025-01-07, LP284 din 05.12.24, forma electronică a mandatului avocatului), nu cea condiționată.
Consecință de metodă: **o dată de versiune 2030-01-01 pe legis.md înseamnă „la aderare", nu
„1 ianuarie 2030"**, iar registrul in-force ar data greșit o astfel de dispoziție dacă ar fi
ingerată. Republicată 04.09.2010 (MO 159 art. 582), în vigoare 13.12.2002.

### T.2. Statutul profesiei: doc_id-ul din plan era o versiune din 2012

Planul dădea 86850 „de confirmat pe pagină". **86850 există și este Statutul**, dar este a doua
din șapte versiuni, consolidarea MUARM220 din 24.02.2012. Cea curentă este **134919@2022-05-27**
(HUA19-01 din 27.05.22, MO194-200/01.07.22); între ele, 118228@2017-12-15, 121620@2019-12-13,
128405@2021-09-09. Fișa: tipul STATUTUL, autoritatea UNIUNEA AVOCAȚILOR DIN REPUBLICA MOLDOVA,
identificator SUARM0/2011, publicat 08.04.2011 în MO 54-57 art. 302, fără abrogare. Titlul de pe
legis.md e scris „STATUTUL Nr. 0 din 29.01.2011", cu numărul 0.

**Structura este pe articole**, nu pe puncte: 74 de linii `Articolul N`, zero puncte numerotate.
Se ancorează deci ca o lege, nu ca hotărârile de Guvern; ipoteza „pe puncte" din plan nu s-a
confirmat. Art. 1 alin. (1) își declară temeiul: Legea 1260/2002, republicată în MO 159/582 din
04.09.2010.

### T.3. Lacune D5: Codul deontologic și Regulamentul stagiului nu sunt pe legis.md

Căutări în titlu, fără diacritice, toate fără rezultat pentru actele Uniunii Avocaților:

| căutare | rezultate | ce conține |
|---|---:|---|
| `codul deontologic` | 12 | coduri deontologice ale CNA, expertului judiciar, lucrătorului medical, mediatorului, polițistului de frontieră, Curții de Conturi; decizii ale Curții Constituționale; **niciunul al avocaților** |
| `avocatilor` | 169 | Avocatul Poporului, decizii ale Curții, HG 158/2013 privind mandatul avocatului; **niciun act al Uniunii** |
| `avocat stagiar` | 4 | HG 158/2013 și modificarea ei, două ordine MJ din 2003 (lista stagiarilor, legitimația) |
| `stagiului profesional` | 3 | regulamente ale MJ pentru experți și concursuri, nu pentru avocați |
| `stagiului` | 53 | niciunul cu „avocat" sau „Uniune" în titlu; stagiul în biroul notarului da |
| `statutul profesiei de avocat` | 5 | Statutul și cele patru acte de modificare ale lui |

Conform D5, **niciunul nu se ingerează de pe uam.md**: nu există control pentru sursa aceea.
Rămân lacune consemnate. Identificatorii rezervați în plan, `UA-DEONTOLOGIC-AAAA` și
`UA-STAGIU-AAAA`, nu sunt folosiți. De reținut că Statutul însuși poate conține regulile stagiului
și trimiterile la codul deontologic; nu a fost citit în acest scop.

### T.4. `L-514-1995`: lacunele de numerotare sunt abrogări la nivel de capitol, cu stub în text

Verify raportează lacune la **29–34, 41–42, 51–53**. Toate sunt explicate în textul consolidării,
la nivel de capitol, cu linia păstrată: `Capitolul 3 (art.29-34) - abrogat.`, `Capitolul 5.
(art. 41-42) - abrogat.`, `Capitolul 8. (art.51-53) - abrogat.`, plus „Denumirea capitolului 4. -
abrogată." și „Denumirea capitolului 6. - abrogată.". Cele trei linii sunt ancorate ca `## Capitolul`,
deci citabile. Celelalte abrogări sunt la nivel de articol, cu stub `Articolul N. - abrogat.` (12,
18, 19, 23, 26, 27, 28, 36, 38, 39, 40, 44, 49), și la nivel de alineat. Este mecanismul „stub
păstrat", opusul celui de la `L-548-1995` (întrebarea deschisă 6): aici publicatorul a ținut
stub-urile, dar la nivel de capitol, pe care contorul de articole nu le vede. **Nu este defect de
ingest și nu este `[de verificat]`.** Titlul actului poartă asterisc în sursă („judecătorească*").

### T.5. Structură și integritate

| act | ancore | de bază | cu exponent | capitole | `<sup>` | linii verify |
|---|---:|---|---|---:|---:|---|
| `L-1260-2002` | **73** | 69, numerotate 1–69 fără lacune | 4: 35^1, 37^1, 43^1, 50^1 | 12 | 38 | PASS, 664 / 664 |
| `L-198-2007` | **54** | 37, numerotate 1–37 fără lacune | 17: 10^1, 13^1, 23^1, 31^1, 36^1–36^13 | 6 | 58 | PASS, 496 / 496 |
| `L-514-1995` | **60** | 45 prezente din 1–56 (vezi T.4) | 10: 6^1, 6^2, 15^1, 16^1, 23^1–23^3, 48^1, 56^1, 56^2 | 7 + 1 titlu | 24 | PASS, 347 / 347 |
| `UA-STATUT-2011` | **74** | 68, numerotate 1–68 fără lacune | 6: 28^1, 41^1, 43^1, 52^1, 52^2, 53^1 | 10 | 19 | PASS, 851 / 851 |

Fără span ridicat prin CSS, fără CUPRINS, fără duplicate. Titlu tăiat pe două linii: `L-514-1995`
art. 16 („Preşedinţii şi vicepreşedinţii instanţelor / judecătoreşti") și `L-198-2007` în antet.
Fișierele 153429 (avocatura, versiunea condiționată) și 86850 (Statut 2012, nedescărcat) nu sunt
în cache; 153429 a rămas în `Downloads`, nefolosit.

## U. Seara de 6 septembrie: trei reîmprospătări, L-160/2011 la zi, Codul civil pe legis.md, L-325/2025 și L-20/2026

Toate la decizia lui Eugen, după raportul de execuție al zilei. HTML-ul a venit pe ruta din
5 septembrie: după ce Eugen a trecut verificarea Cloudflare, `fetch` same-origin în pagina
legis.md și descărcare ca blob, cu acordul lui explicit pentru cele șapte fișiere; mutate în
cache-urile `_meta/imports/moldova-legal/legis-md-business/` și `_meta/imports/bnm/legis-md-ro/`.

### U.1. Cele trei acte „în urmă" din sondaj

Scriptul: `_meta/imports/moldova-legal/refresh_behind_2026-09-06.py`, care conduce
`refresh_consolidations.py` pe folder, ca lotul din 4 septembrie: arhivă în `_archive/raw/`, lanț
de proveniență în frontmatter, delta pe articole, sha256 recalculat după asamblare.
`refresh_consolidations.py` descarcă acum prin `ibl.fetch` (fișier `.part`, cădere pe cache); vechiul
`curl` direct ar fi suprascris cache-ul cu pagina Cloudflare.

| act | doc_id | consolidare | delta pe articole | marcaje |
|---|---|---|---|---|
| `COD-225-2003` | 152860 → **155718** | 2025-12-30 → **2026-08-06** | +3 de bază: **78** (scris corect acum, `Articolul 78. – abrogat.`, ancorat), **491, 492** (capitolul XLVI, nou) | numai LP126/2026 (6); marcajele LP330/2025, LP187/2025, LP252/2025 s-au pierdut, mecanismul 1 |
| `COD-1163-1997` | 155071 → **138613** | 2026-06-25 → **2026-07-01** | −1 cu exponent: **88^1 abrogat** prin LP318/2025 | 4, toate LP318: art. 14 al. (3), 35^1, 88^1, 92 al. (14) |
| `L-202-2017` | 151445 → **151077** | 2025-09-20 → **2025-10-25** | niciuna | 1, LP189/2025: art. 97 al. (5) lit. a^1) |

Integritate PASS pe toate trei (3.350, 6.906, 1.560 de linii). Arhive:
`_archive/raw/moldova-legal-legis-md-before-refresh-20260906-220712/` și
`_archive/raw/bnm-legal-ro-legis-md-before-refresh-20260906-220712/`. Consolidarea viitoare a
Codului fiscal, 152862@2027-01-01 (LP187/2025), rămâne neingerată.

**Capcană de sursă nouă, a patra formă a mecanismului 3.** La art. 88^1 din Codul fiscal legis.md a
lăsat stub-ul `Articolul 88^1. – abrogat.` **numai în cuprins** și a șters din corp linia de
articol, păstrând doar marcajul `[Art.88^1 abrogat prin LP318 ...]` după art. 88. Corpul nu mai
poate purta ancora, iar `verify_business_law.py`, care citea și cuprinsul, a raportat FAIL pe un
articol pe care extractorul nu avea cum să-l ancoreze. Verificatorul aplică acum aceeași regulă
ca extractorul: titlurile dintre marcajul CUPRINS și formula de adoptare nu contează.

### U.2. `L-160-2011` la versiunea în vigoare azi

Vezi R.3, urmarea. 156152 (2029) → **151257 @ 2026-08-29**; cinci consolidări viitoare în istoric,
niciuna ingerată.

### U.3. Codul civil pe textul legis.md

Vezi C.7. 150561 (PDF, 2025-11-01 după fișă, cu textul LP251) → **150498 @ 2026-04-01**; inventar
identic, 27 de ancore de carte și de titlu recuperate printr-o regulă nouă în extractor.

### U.4. `L-325-2025` și `L-20-2026`, succesoarele legii achizițiilor

| act | doc_id | consolidare | ancore | capitole | `<sup>` | integritate |
|---|---:|---|---:|---:|---:|---|
| `L-325-2025` | 152974 | **2027-01-01, viitoare: actul întreg** | 91, numerotate 1–91 fără lacune | 14 | 1 (nu de articol) | PASS, 1.367 / 1.367 |
| `L-20-2026` | 153618 | 2026-04-01 | 29, numerotate 1–29 fără lacune | 5 | 0 | PASS, 348 / 348 |

Amândouă cu o singură versiune pe legis.md, fără rândul MODIFICAT, fără CUPRINS, fără span ridicat
prin CSS. **Consolidarea 2027-01-01 a Legii 325/2025 este data ei de intrare în vigoare** (art. 90
alin. (1)), nu o modificare amânată: registrul in-force o listează ca act cu consolidare viitoare
și zero dispoziții marcate, ceea ce este exact situația, actul nu binde încă nicăieri. Blocul de
acoperire din `CLAUDE.md` nu o vedea însă ca viitoare: extractorul punea `consolidation_is_future`
numai când găsea marcaje amânate, deci un act întreg neintrat în vigoare trecea drept curent.
`make_raw` pune acum flagul și un avertisment „ACT NEINTRAT ÎN VIGOARE” ori de câte ori data
consolidării este în viitor fără marcaje; Legea 325/2025 a fost reingerată cu el. Art. 90
alin. (4) abrogă Legea 131/2015 la aceeași dată; art. 91 lasă procedurile și contractele în curs sub
legea de la inițiere. Legea 20/2026 este în vigoare din 01.04.2026 (art. 28 alin. (1)) și anexa ei
a modificat deja Legea 131/2015 (vezi S.1, urmarea). Titluri tăiate pe două linii, cazul cunoscut:
`L-325-2025` art. 1, 8, 11, 42, 44; `L-20-2026` art. 3, 6, 12, 13, 20. Anexele 1 și 2 ale
Legii 325/2025 nu au fost citite.

### U.6. `HG-553-2024`: întinderea abrogării HG 1170/2016, verificată pe text

La cererea lui Eugen, după consemnarea abrogării de dimineață. Găsită prin căutare în titlu
„schimbarea destinatiei" (66 de rezultate; „schimb de terenuri", 40 de rezultate, nu o conține,
fiindcă titlul ei nu are cuvântul „schimb"); rândul HG553/2024, marcat „Modificat", trimite la
150820, iar pagina actului are două versiuni, 144532@2025-03-07 și **150820@2025-10-18**
(HG613/2025), cea din urmă în vigoare azi, fără dată de abrogare. Titlul complet: „pentru
aprobarea Regulamentului cu privire la schimbarea destinației terenurilor cu destinație agricolă
de calitate superioară și a terenurilor destinate fondului forestier și fondului apelor". Temei:
art. 58 alin. (10) din **Codul funciar nr. 22/2024**, neingerat. 11 `<sup>`, fără span CSS, fără
CUPRINS, integritate PASS pe 110 linii. Structură în **puncte** (4 în hotărâre, 1–24 cu 1^1 și 1^2
în Regulament, numerotarea repornește), deci **zero ancore**, ca `HG-574-2024`; 15 marcaje, toate
HG613/2025.

Constatarea: **pct. 3 din hotărâre abrogă HG 1170/2016 integral**, „cu modificările ulterioare",
fără nicio dispoziție tranzitorie; pct. 4 dă intrarea în vigoare la 7 martie 2025, data din fișa
actului abrogat. Dar Regulamentul din 2024 acoperă numai schimbarea destinației, și numai pentru
terenurile agricole de calitate superioară și cele ale fondului forestier și apelor; transmiterea
și schimbul de terenuri, celelalte două obiecte ale regulamentului din 2016, nu apar în act. Deci
abrogarea e totală ca act și parțială ca regim, iar lacuna următoare este Codul funciar 22/2024.

### U.7. `COD-22-2024`, Codul funciar: lacuna deschisă de U.6, închisă la cererea lui Eugen

Căutare în titlu „codul funciar" (106 rezultate); rândul CF22/2024, marcat „Modificat", trimite la
**154132**, care este și capul istoricului (opt versiuni, de la 142192@2024-03-07; 154132@2026-04-25,
LP53/2026), fără versiune viitoare, fără abrogare. Titlul de pe legis.md este doar „CODUL FUNCIAR",
fără „al Republicii Moldova". 25 `<sup>`, fără span CSS, fără CUPRINS; **96 de ancore**, 79 de bază
numerotate 1–79 fără lacune, 17 cu exponent (27^1–27^3, 31^1–31^3, 53^1, 54^1–54^10), 13 capitole
(I–XII și VI^1), fără titluri; integritate PASS pe 747 de linii. Prefixul `COD-` este cel al
codurilor, ca `COD-434-2023`.

Trei constatări de sursă. **Fișa contrazice textul la intrarea în vigoare**, a treia oară în
corpus: fișa dă 07.03.2024, data publicării; art. 79 alin. (1) spune „1 aprilie 2025". Lămurit
pe istoricul versiunilor, citit prin `fetch` versiune cu versiune fără descărcare: textul inițial
(142192) dădea „12 luni de la data publicării", adică 07.03.2025, și LP30/2025, în vigoare
06.03.2025, a rescris alin. (1) la 1 aprilie 2025; marcajul `[Art.79 al.(1) în redacția LP30...]`
există în 147402 și lipsește din 154132. HG 553/2024, cu intrarea în vigoare la 7 martie 2025,
a rămas pe termenul inițial, deci a intrat în vigoare cu 25 de zile înaintea codului-temei. **Marcajele s-au pierdut aproape toate**: șapte legi de
modificare în fișă, trei marcaje în text, toate LP53/2026, toate în art. 58. **Art. 79 nu are
nicio dispoziție tranzitorie** pentru dosarele în curs; abrogă Codul funciar 828/1991 cu excepția
art. 12, 13, 40 până la 31.12.2028, Legea 1247/1992 cu excepția art. 18–20, Legea 1308/1997 cu
cinci excepții, și cere Guvernului o Metodologie de calcul al pierderilor, act al Parlamentului
(art. 60 alin. (3)), neidentificat.

Ce închide: transmiterea și schimbul terenurilor proprietate publică, rămase fără regulament după
abrogarea HG 1170/2016 (U.6), sunt direct în **art. 16** (transmiterea la alin. (1)–(5), schimbul
la alin. (6)–(8), cu echivalența valorii de piață la alin. (7)); schimbarea destinației este în
art. 58–60, cu delegarea din art. 58 alin. (10) împlinită de `HG-553-2024`.

### U.8. `COD-1163-1997`, consolidarea 152862 @ 2027-01-01, verificată fără ingerare (2026-09-07)

Executarea punctului din raportul de execuție, secțiunea 7, pe calea (b). Pe pagina actului, lista
`a[onclick*="showDetails"]` dă 152862 @ 01-01-2027 drept cap al istoricului, urmat direct de 138613 @
01-07-2026, textul deținut; nicio consolidare intermediară de la sondajul din 6 septembrie. 152862 și
138613 citite prin `fetch` în pagină, fără descărcare, metoda din U.7, cu articolele extrase din
`innerText` prin ultima apariție a antetului (prima apariție este în CUPRINS) și comparate alineat cu
alineat. **Cinci marcaje „în vigoare 01.01.27”, toate LP187 din 10.07.25**: art. 131 alin. (1^1) în
redacție nouă (portalul guvernamental al unităților de drept ca al doilea canal de comunicare al SFS,
recepție prezumată din ziua lucrătoare următoare), art. 342 alin. (1), (1^1) și (2) abrogate (darea de
seamă privind taxa pentru folosirea drumurilor), art. 342^1 alin. (3) modificat („raportarea” eliminată).
Marcajele scriu `al.(11)` pentru alin. (1^1). LP187/2025 apare în fișele a șase acte deținute doar cu
trepte în vigoare azi; treapta din 2027 este numai în Codul fiscal.

Consemnat în `_meta/inforce/pending-consolidations.json`, fișier scris de mână pe care
`build_inforce_register.py` îl redă de acum ca secțiune separată, „Consolidări viitoare neingerate”;
scriptul refuză intrarea și avertizează când data ei a trecut. Nimic din `raw/` nu s-a atins.

### U.9. `L-160-2011`, cele cinci consolidări viitoare, citite fără ingerare (2026-09-07)

Aceeași metodă ca U.8. Lista de versiuni confirmă cele cinci consolidări viitoare din U.2, fără una
nouă. Șase versiuni (151257 și 149496, 150231, 154051, 154478, 156152) citite prin `fetch` fără
descărcare și comparate în lanț, paragraf cu paragraf. **Rezultat negativ util: corpul legii este
identic în toate șase.** Fiecare consolidare adaugă doar rândul din fișă și, de la 154051 încolo, un
marcaj `[Anexa nr.1 modificată prin LP...]` care îl înlocuiește pe cel precedent; pentru LP136/2025
și LP176/2025 marcajul nu a existat niciodată. Toate cinci modifică Nomenclatorul actelor permisive,
anexa nr. 1, care nu este în textul de pe legis.md în nicio versiune. Consemnate ca cinci rânduri în
`_meta/inforce/pending-consolidations.json`, cu unitatea „anexa nr. 1”; `article_sort_key` din
generator acceptă de acum unități fără număr de articol. LP176/2025 atinge și `L-1543-1998`
(art. 15^3–15^8, consolidare ingerată).

### U.10. `COD-1163-1997`, cele zece hotărâri ale Curții Constituționale din fișă, recuperate la articol (2026-09-08)

Pasul 5.3 din `_meta/plans/2026-09-08-plan-hcc-pasul-5.md`, primul act în ordinea D3. Textul deținut
(138613) nu poartă niciun marcaj HCC la articol; fișa are zece rânduri. Pentru fiecare, istoricul de
versiuni al actului (286 de ancore `showDetails`, 256 datate) are o versiune la data exactă a hotărârii;
versiunile citite prin `fetch` în pagină, fără descărcare: 79116, 79268, 79269, 79270, 79271, 79275,
113173, 122989, 142465, 142855. Dispozitivele hotărârilor citite pe legis.md la doc_id 16986, 4996,
16103, 6309, 16104, 15622, 111134, 122834, 142698, 142823, găsite prin căutare în titlu („codului
fiscal”, „codul fiscal”, „legii nr. 324”, „taxelor locale”, „timbre”, toate fără diacritice).

Ce spun versiunile, pe epoci: consolidările din 1999 nu au marcaj deloc (HCC12 vine numai din hotărâre);
cele din 2014 au marcajul în paranteze rotunde la **sfârșitul** articolului sau al anexei, fără numărul
articolului („(se declară neconstituţional prin HCC7...)”), deci articolul se ia din poziție și se
confirmă în dispozitiv; din 2018 marcajul e în paranteze drepte cu articolul. Trei defecte ale
publisherului: marcajul HCC22 numește art. 226^11 în loc de 226^16 (dispozitivul e clar); marcajul
HCC20 e rupt, rămâne doar coada după semnătură; HCC11 e scris „neconstutuţional”. Toate cele zece
dispoziții au fost apoi corectate de Parlament în textul deținut (abrogare sau rescriere), deci Codul
fiscal nu ține azi text anulat; registrul le consemnează pentru istoric și pentru spețele anterioare.
Rânduri în `_meta/hcc/recovered-provisions.json` (17, HCC2/2014 pe nouă articole); tabelul pe
`entities/COD-1163-1997.md`. Nimic din `raw/` atins.

### U.11. `COD-218-2008` și `COD-225-2003`, hotărârile Curții din fișe, recuperate la articol (2026-09-08)

Pasul 5.3, continuare. Eugen a cerut Codul contravențional; procedura civilă a fost luată în aceeași
sesiune fiindcă pagina ei era deja deschisă. Codul contravențional: 4 recuperate din 6 (versiunile
6776, 93895, 108178, 108180; hotărârile 15895, 93737, 111024, 111030), acum 6/6. Procedura civilă:
5 recuperate din 9 (versiunile 81050, 81103, 97669, 134150, 145370; hotărârile 10267, 15921, 97527,
134115, 145340), acum 9/9; 13 rânduri noi în `recovered-provisions.json`.

Ce s-a învățat în plus față de U.10. (1) Al patrulea tip de marcaj: în Codul contravențional din
2013 și 2018 marcajul stă pe rând separat sau lipit de sancțiune, fără paranteze și fără articol
(„declarat neconstituțional prin HCC7 din 26.04.18”). (2) Data versiunii nu e mereu data hotărârii:
HCC10/2016 are versiunea la 12.07.16, data publicării în MO. (3) O hotărâre care lovește **legea de
modificare**, nu codul, nu lasă marcaj în nicio versiune a codului (HCC16/2013 pe LP29/2012), iar
titlul ei nu conține numele codului; singura cale de a o găsi a fost căutarea în titlu pe
„sesizarea”, care returnează practic toate HCC (2.742 de rânduri) și se filtrează pe număr și an.
(4) Fișa listează numai anulările: HCC4/2018 și HCC28/2018 (recunoașteri cu rezervă de interpretare
în Codul contravențional) și HCC4/2016 (procedura civilă) nu apar în fișe și nu sunt în registru.
(5) Toate cele nouă dispoziții recuperate azi au fost rescrise sau abrogate de Parlament; una are
formă înșelătoare: art. 449 lit. f) CPC se citește „abrogată” deși abrogarea a fost anulată, pentru că
temeiul a fost reintrodus ca lit. e^1). Nimic din `raw/` atins.

### U.12. `COD-122-2003`, cele 14 hotărâri ale Curții fără marcaj, recuperate la articol (2026-09-08)

Pasul 5.3, continuare, la cererea lui Eugen. 17 hotărâri în fișă, 3 cu marcaj în text, 14 recuperate:
versiunile 17232, 17273, 17299, 17311, 85426, 91217, 113967, 120451, 124153, 126068, 126190, 135679;
hotărârile 16022, 15961, 13647, 3340, 85436, 91184, 113703, 120315, 121723, 124113, 126050, 128296,
128377, 135403. Găsirea hotărârilor: „sesizarea” pentru cele din 2012 încoace, „procedura penala” pentru
cele din 2005–2010, ale căror titluri încep cu „asupra excepţiei” și nu conțin „sesizarea”. 23 de
rânduri noi; acum 17/17.

Ce s-a învățat în plus. (1) Două hotărâri nu au versiune proprie: HCC15/2020 (28.05.2020) nu apare
deloc în istoric și niciun marcaj al ei nu există în versiunile vecine, iar HCC29/2021 (21.09.2021) stă
în versiunea produsă de HCC31 două zile mai târziu; deci „versiunea de la data hotărârii” este regula,
nu legea. (2) Dispozitivul poate numi un articol pe care fișa nu îl are: HCC15/2020 lovește și art. 192
alin. (2), abrogat azi. (3) Consolidarea deținută fiind viitoare (02.12.2026), un articol lovit poate să
nu mai existe sub numărul lui: art. 132^9 (HCC31/2021) e renumerotat, capitolul măsurilor speciale de
investigații fiind acum 138^1–138^N; iar art. 452–457 au dispărut cu tot cu stub, secțiunea fiind
„abrogată” ca întreg. (4) Cloudflare a reapărut o dată în mijlocul lucrului (pagina „Just a moment”) și
s-a rezolvat singură la a doua încărcare, fără intervenție. Nimic din `raw/` atins.

### U.13. `COD-985-2002`, cele opt hotărâri ale Curții din fișă, recuperate la articol (2026-09-08)

Pasul 5.3, continuare, la cererea lui Eugen. Versiunile 17781, 93751, 94191, 109485, 109490, 118807,
127791, 129474, toate cu marcaj; hotărârile 15880, 100435, 30023, 111031, 111139, 118717, 127780,
129451, găsite prin „codul penal” în titlu. 16 rânduri noi, dintre care două pentru Codul de
executare (HCC18/2013, art. 174 alin. (3^1) și 291^1, luate din dispozitiv fără a citi versiunea
acelui cod). Acum 8/8 pentru Codul penal.

Ce s-a învățat în plus. (1) Cel mai curat act de până acum: toate cele opt versiuni au marcaj, șapte
în paranteze drepte cu articolul; numai 2013 e în forma veche, cu paranteze rotunde, lipită de rândul
următor și datată cu data MO. (2) Șase din opt sunt o singură linie: previzibilitatea „intereselor
publice” și „urmărilor grave” în infracțiunile de serviciu, patru hotărâri 2017–2021 pe art. 327, 328,
329, 335, 361, 189, 307; HCC24/2019 singură lovește șase texte. (3) Toate cele opt au fost rescrise de
Parlament; art. 104^1 a dispărut fără stub. (4) Defecte de fișă: „cт.4” chirilic (HCC33/2017),
„art.89” contra „art.88” din marcaj (HCC12/2018). Nimic din `raw/` atins.

### U.14. `L-246-2018`, Legea privind procedura notarială, ingerată la cerere (2026-09-09)

Din lista de ingest a speței moștenitorului unui acționar de bancă (8 septembrie 2026), după cele
două regulamente BNM și Regulile DCU: procedura prin care notarul ajunge la certificatul de
moștenitor, titlul de înregistrare la Depozitarul central.

| Act | doc_id | Consolidare | Ancore |
|---|---|---|---|
| Legea nr. 246/2018 privind procedura notarială | **137680** | **2026-06-23** (LP126/2023) | 97: 1–96 fără lacune, plus 5^1; 9 capitole |

**Verificare.** `verify_business_law.py`: integritate de text **PASS, 850 de linii scrise față de
850 de referință**, fără `<sup>` rămas din 15, fără duplicate, 12 exponenți de alineat și literă în
corp. sha256 recalculat: coincide.

**Capcană de versiune, nouă pentru acest corpus.** Rândul de căutare de pe legis.md trimite la
doc_id 150742, consolidarea din 01.11.2025 (LP222/2025). Istoricul actului are deasupra ei
**137680 @ 23.06.2026**, consolidarea produsă de LP126/2023, lege cu intrare în vigoare amânată
trei ani: doc_id-ul e mai mic fiindcă versiunea a fost creată în 2023, dar este cea în vigoare
astăzi, cu 97 de articole față de 96 și 33 de marcaje „în vigoare 23.06.26". Regula de lucru:
lista de versiuni a paginii actului decide, nu rândul de căutare și nu mărimea doc_id-ului. Până
acum consolidarea curentă fusese întotdeauna cea cu doc_id-ul cel mai mare.

**Ce dă pentru speță**, pe pagina de entitate: art. 82 alin. (3), certificatul de moștenitor nu
mai devreme de o lună de la ultima publicare; art. 73, suspendarea la contestare; art. 69
alin. (1^1), singura mențiune a certificatului de calitate de moștenitor; art. 79–80, custodele,
care poate fi unul dintre succesibili cu acordul tuturor.

Descărcarea: octeții serverului prin `fetch` din Chrome, 343.023 de octeți, cu acordul lui Eugen.
Renderer-ul paginii `showdetails` a înghețat de două ori la această mărime; `fetch` a reușit din
pagina actului (`getResults?doc_id=`), care e mai ușoară. Două decizii de inadmisibilitate ale
Curții (DCC36/2022, DCC92/2026) privesc legea; nu sunt anulări, nu intră în registrul HCC.

### U.5. Ce a rămas în afara acestei seri

- `COD-218-2008` ar câștiga două ancore de carte cu regula nouă din extractor; neaplicat.
- Consolidarea viitoare a Codului fiscal (152862@2027-01-01) și cele cinci ale Legii 160/2011.
- Cele trei fișiere descărcate dimineața și nefolosite (`showdetails-152529/-156075/-153429.html`)
  au rămas în `Downloads`.

## V. Protecția datelor cu caracter personal — L-133/2011, L-195/2024, L-160/2026 (ingerate 2026-09-10)

Ceruta a fost o singura lege: **L-133/2011**, primul rand al cozii de ingerare din graful de
citare construit in aceeasi zi (34 de mentiuni in 18 acte detinute, mai mult decat orice alt act
lipsa). Verificarea prealabila a schimbat continutul lucrarii, si merita citita ca atare, fiindca
este exact limita pe care graful si-o declara singur: **graful nu stie daca un act citat mai este
in vigoare.**

### V.1. Constatarea: legea ceruta era moarta de 18 zile

`L-133/2011` a fost **abrogata de la 23.08.2026** prin art. 90 alin. (3) lit. b) din
`L-195/2024`. Astazi este 10 septembrie 2026. Ingerarea numai a ei ar fi pus text mort in vault
ca raspuns la 19 trimiteri vii.

Aceeasi operatiune a abrogat si Legea nr. 182/2008 privind Regulamentul Centrului (neingerata) si
**arts. 74^1–74^3 si art. 423^4 din `COD-218-2008`**. Ultima parte este verificabila la noi si se
verifica: in consolidarea detinuta a Codului contraventional toate patru apar `– abrogat.`, la
liniile 1696, 1698, 1700 si 6654. Sanctionarea contraventionala a incalcarilor privind datele
personale a iesit din Codul contraventional si a trecut integral in regimul administrativ-pecuniar
al legii noi, arts. 86–88.

### V.2. Doua capcane de sursa, ambele tacute

**Prima, cunoscuta, a doua oara: randul de cautare arata o consolidare veche.** Cautarea trimite
la doc_id **148996** @ 14.06.2025. Lista de versiuni de pe pagina actului tine insa **144823** @
**23.08.2026** — doc_id **mai mic**, data **mai noua**, creat in 2024 pentru o modificare cu
intrare in vigoare amanata doi ani. Identic cu `L-246-2018` la 9 septembrie. Regula ramane: se
citeste lista de versiuni, se ia data cea mai noua care nu e in viitor; niciodata doc_id-ul cel
mai mare, niciodata randul de cautare.

**A doua, noua: fisa contrazice corpul actului.** Corpul consolidarii 144823 poarta in antet, in
locul randului `MODIFICAT`, textul `Abrogata prin LP195 din 25.07.24, MO367-369/23.08.24 art.574;
in vigoare 23.08.26`. Campul **„Data abrogarii" din fisa este GOL** (`-`). Un control care s-ar
sprijini pe campul structurat al fisei ar rata abrogarea in intregime.

Fara aceste doua verificari actul ar fi intrat cu o consolidare recenta si trecuta, deci ar fi
aparut `clean` in blocul de acoperire, cu ancorare curata si sha256 valid. Este simetricul
capcanei consolidarilor viitoare: acolo textul nu se aplica **inca**, aici nu se mai aplica.

### V.3. Ce s-a ingerat, si de ce trei acte in loc de unul

| stem | doc_id | consolidare | ancore | stare | acquis |
|---|---|---|---:|---|---|
| `L-133-2011` | 144823 | 2026-08-23 | 36 | **abrogat de la 23.08.2026** | Directiva 95/46/CE |
| `L-195-2024` | 155899 | 2026-08-23 | 90 | in vigoare din 23.08.2026 | Regulamentul (UE) 2016/679 (GDPR) |
| `L-160-2026` | 155902 | 2026-08-23 | 46 | in vigoare din 23.08.2026 | Directiva (UE) 2016/680 |

`L-195/2024` si `L-160/2026` au fost gasite in aceeasi cautare in titlu, `protectia datelor cu
caracter personal`. Impartirea materiei este curata: art. 2 alin. (2) lit. c) din `L-195/2024`
scoate din legea generala prelucrarea de catre autoritatile competente in scop penal, iar art. 1
alin. (1) din `L-160/2026` o preia. `L-160/2026` nu este autonoma — imprumuta notiunile din art. 4,
procedura amenzii din art. 87 si examinarea plangerii din cap. VIII sect. a 2-a ale legii generale.

Verificare de integritate, `verify_business_law.py`: **PASS pe toate trei**, 357 / 1009 / 381 de
linii scrise fata de tot atatea de referinta, deci s-au adaugat numai ancore. Fara `<sup>` ramas,
fara ancore duplicate, fara lacune de numerotare.

### V.4. Ce a intrat in scripturi

**`repeal_of()` in `ingest_business_law.py`.** Pana aici ingestul nu avea nicio notiune de act
abrogat. Citeste amandoua sursele — randul din corpul actului si campul din fisa — si le pastreaza
pe amandoua in frontmatter (`repealed`, `repeal_effective`, `repealed_by`, `repeal_line`,
`repeal_fisa_field`, `repeal_in_force_today`), fiindca dezacordul lor este el insusi o constatare
despre sursa. Data care conteaza este cea de intrare in vigoare a abrogarii, nu data actului
abrogator: legea a fost abrogata printr-o lege din 2024 cu efect din 2026. In corpul fisierului
brut se scrie un avertisment inaintea oricarui alt avertisment.

**Flagul din `build_coverage.py`.** Un act abrogat apare acum in tabel cu
`**ABROGAT de la ...**` si intr-o sectiune proprie de „Mechanical flags".

**Sectiunea „Trimiteri catre acte abrogate" din `build_citation_graph.py`.** Graful citeste
`repealed` din frontmatter, deci pentru actele **detinute** limita pe care si-o declara este
ridicata. Pentru cele externe ramane intreaga.

### V.5. Ruta de descarcare: legis.md este din nou accesibil prin `curl`

Notat pentru ca schimba metoda. La 10 septembrie `curl` trece de Cloudflare pentru
`showdetails/<doc_id>`, cu reaparitii intermitente pe care le rezolva o reincercare. **Si cautarea
este acum scriptabila fara Chrome**, ceea ce nu era: rezultatele se incarca prin AJAX din
`cautare/justicejs`, functia `showcontent()`, care apeleaza

```
GET https://www.legis.md/cautare/getAjaxContent?filter_title=<fraza>&filtru=
```

Endpointul depinde de starea de sesiune PHP fixata de apelul anterior la
`cautare/getResults?search_string=<fraza>&search_type=1`, deci se ruleaza in doi pasi **cu acelasi
borcan de cookie-uri** (`curl -c/-b`). Fraza se scrie in continuare **fara diacritice**. Randurile
intoarse contin `doc_id=` in `href`, deci se parseaza direct.

Ce **nu** s-a schimbat: `curl` intoarce pagina „Just a moment" cu **rc=0**, deci un cod de retur
curat nu inseamna ca avem documentul; `usable()` ramane obligatoriu. Si nu s-a verificat daca ruta
tine cand Cloudflare urca pragul; ruta prin Chrome din memoria `legis-md-fetch-route` ramane
rezerva.

### V.6. Ce a ramas deschis

- **Trimiterile la legea abrogata nu sunt convertite de nimeni.** Art. 90 din `L-195/2024` **nu**
  contine clauza „trimiterile la Legea nr. 133/2011 se considera facute la prezenta lege"; cautarea
  in textul integral nu o gaseste. Art. 55 din `L-100-2017`, singura norma generala despre trimiteri,
  reglementeaza cum se **fac** trimiterile, nu ce se intampla cand actul-tinta e abrogat. Nouasprezece
  acte din corpus trimit astazi la un text care nu mai e in vigoare, fara punte statutara expresa.
  **De ridicat cu Eugen.**
- **Actele normative ale Centrului**, cerute de art. 89 alin. (3) din `L-195/2024`, nu sunt ingerate.
  Cel putin unul exista: ordinul nr. 31 din 31.07.2026 privind Contractul standard pentru transferul
  de date catre state fara nivel adecvat de protectie (legis.md `OCNPDCP31/2026`, doc_id 155738).
  Fara el, cap. transferurilor, arts. 44–49, nu se ancoreaza pana la instrumentul aplicabil.
- **Legea nr. 245/2008 cu privire la secretul de stat** nu este ingerata; ambele legi noi isi
  definesc limita exterioara prin trimitere la ea.
- **Legea nr. 182/2008**, abrogata in aceeasi operatiune, nu e ingerata si nu e nevoie sa fie.
- CNPF si BNM **nu sunt numite** in `L-195/2024`. Nu exista regim sectorial financiar, nici
  exceptie pentru entitatile supravegheate prudential, nici mecanism de cooperare. `[de verificat]`
  daca o regula de cooperare exista in actele normative ale Centrului.

## D. Artefacte metodologice create

| Artefact | Tip | Rol |
|---|---|---|
| [[moldova-eu-transposition-method]] | concept | flux de lucru pentru transpuneri UE |
| [[moldova-eu-transposition-rule-matrix]] | concept | reguli imperative transformate în controale operaționale |
