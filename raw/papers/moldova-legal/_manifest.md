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
| `HG-1170-2016` | **144537** | HOTĂRÂRE Nr. 1170 din 25.10.2016 pentru aprobarea Regulamentului cu privire la modul de transmitere, schimbare a destinaţiei şi schimb de terenuri | [[HG-1170-2016]] | **2025-03-07** | tratată literal din solicitarea inițială; nu este regulamentul de armonizare UE |

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

## D. Artefacte metodologice create

| Artefact | Tip | Rol |
|---|---|---|
| [[moldova-eu-transposition-method]] | concept | flux de lucru pentru transpuneri UE |
| [[moldova-eu-transposition-rule-matrix]] | concept | reguli imperative transformate în controale operaționale |
