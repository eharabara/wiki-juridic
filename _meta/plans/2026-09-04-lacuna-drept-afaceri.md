# Lacună de acoperire: dreptul afacerilor și codurile

Data: 2026-09-04. Sursă: `2026-09-04-plan-descarcare-esuat-drept-afaceri.json`,
recuperat din `Desktop\Justitiarul Path\Wiki\Dreptul afacerilor` înainte de ștergerea acelui folder.

## Ce s-a întâmplat

La 13 iulie 2026 a rulat o descărcare automată de pe legis.md pentru 11 acte. Toate cele 11 au
eșuat. Prima eroare este `net::ERR_ABORTED` la `https://www.legis.md/`, restul sunt
`Target page, context or browser has been closed`, adică sesiunea de browser a căzut după primul
refuz. Cauza este protecția anti-bot a legis.md, dar numai pe calea prin browser automatizat. Verificat
la 2026-09-04: `curl` cu un User-Agent obișnuit de desktop trece și acum, atât pe `showdetails`
cât și pe căutare. Deci metoda `showdetails` folosită la 9 iulie nu a fost o reacție la acest eșec,
ci îi este anterioară cu patru zile. Nota inițială inversa ordinea.

## Ce lipsește din wiki

### 01. Coduri și proceduri
- Codul de procedură civilă 225/2003
- Codul de executare 443/2004
- Codul administrativ 116/2018
- Codul fiscal 1163/1997
- Codul vamal 95/2021
- Codul muncii 154/2003
- Codul contravențional 218/2008
- Codul penal 985/2002
- Codul de procedură penală 122/2003

### 02. Societăți, antreprenoriat și insolvență
- Legea privind societățile cu răspundere limitată 135/2007
- Legea privind înregistrarea de stat a persoanelor juridice și a întreprinzătorilor individuali 220/2007
- Legea cu privire la antreprenoriat și întreprinderi 845/1992 — nu figura în planul de descărcare
  din 13 iulie, deci nu apare în JSON, dar documentul 04 o indică drept sursă de bază pentru P1.
  Adăugată aici la 2026-09-04. În wiki apare doar ca act modificat în interiorul L-181-2023 și în
  două documente de politici, niciodată ca sursă.

## De ce contează, în ordinea consecinței

Ultimele trei sunt cele mai urgente. Documentul 04 enumeră cinci surse care guvernează persona P1,
specialistul în drept corporativ. Două sunt prezente și ancorate, Codul civil și L-1134-1997. Trei
lipsesc: 135/2007, 220/2007 și 845/1992. În acest moment P1 nu are nicio sursă ancorată pentru întrebările
corporative curente: constituire de SRL, transmiterea părților sociale, competența adunării
generale, înregistrarea la ASP. Răspunsurile în această zonă pot fi doar `neancorate`.

Codul fiscal 1163/1997 este a doua prioritate. Regula analitică din documentul 03 cere ca fiecare
răspuns să ajungă la costul și la cine îl suportă. Fără Codul fiscal ancorat, partea fiscală a
oricărei structuri corporative sau contractuale rămâne raționament general, nu citare.

Codul administrativ 116/2018 este a treia. Este cadrul pentru contestarea actelor CNPF și BNM, deci
este direct legat de constatările privind depășirea mandatului, care sunt principalul rezultat
analitic al wiki-ului de până acum.

## Pasul următor

Reluarea descărcării nu se face cu același instrument. Metoda care a funcționat la 9 iulie este
`curl` pe endpointul `showdetails/<doc_id>` plus extracție cu lxml, documentată în
`_meta/imports/cnpf/legis_md_consolidated_ingest.py`. Ordinea propusă: 135/2007 și 220/2007, apoi
Codul fiscal, apoi Codul administrativ, apoi restul codurilor.

Condiția suspensivă din versiunea inițială a acestei note, anume așteptarea ancorării, s-a
îndeplinit. Ancorarea din `2026-09-04-anchoring-brief.md` este încheiată, inclusiv jobul 3.
Ingerarea este acum primul element de lucru deschis, nu al treilea.

## doc_id, găsite și verificate 2026-09-04

| Act | doc_id | Consolidat la | Articole |
| --- | --- | --- | --- |
| L-135-2007 privind societăţile cu răspundere limitată | `153674` | 27.03.2026, LP41 din 26.03.26 | 83 de bază, 9 cu exponent |
| L-220-2007 privind înregistrarea de stat a persoanelor juridice şi a întreprinzătorilor individuali | `155438` | 23.07.2026, LP76 din 02.07.26 | 39 de bază, 5 cu exponent |

Ambele au fost deschise, nu doar rezolvate. Trec poarta de acceptare aplicată de scriptul de
ingerare: `id="contentdoc"` prezent, fără interstitial Cloudflare. Titlurile din antet corespund
denumirilor din documentul 04. Ambele consolidări sunt curente, spre deosebire de L-308-2017 și
L-92-2022.

**Cum se găsesc restul.** Rezultatele căutării pe legis.md se încarcă prin AJAX, de aceea o
descărcare simplă a URL-ului de căutare întoarce o pagină goală. Sunt necesare două apeluri pe
aceeași sesiune cu cookie: întâi `GET /cautare/getResults?nr_doc=<N>&search_type=1&lang=ro`, care
depune criteriile pe server, apoi `GET /cautare/getAjaxContent?filter_title=&filtru=`, care
randează tabelul. Rândurile trimit la `getResults?doc_id=<id>&lang=ro`. Fără `search_type` apare o
notiță PHP și rezultatele nu sunt filtrate.

**De reținut la ingerare.** În HTML-ul sursă numerele de articol cu exponent sunt marcate
`Articolul 27<sup>1</sup>`. Extracția prin `text_content()` le lipește în `271`. Aplatizarea este
un defect al extracției, nu o limită a sursei, deci `<sup>` trebuie mapat la forma `^N` înainte de
scrierea ancorelor. Articolele afectate: L-135-2007 are 27¹, 31¹, 33¹, 40¹, 43¹, 47¹, 56¹, 56²,
77¹; L-220-2007 are 25¹, 26¹, 31¹, 31², 34¹.

## Rezolvat 2026-09-04: cele două legi corporative sînt ingerate

`L-135-2007` și `L-220-2007` au fost ingerate în `raw/papers/moldova-legal/`, nu în `cnpf/`,
fiindcă sînt drept societar general, nu perimetru CNPF/BNM. Script:
`_meta/imports/moldova-legal/ingest_business_law.py`, verificare `verify_business_law.py`,
detalii în secțiunea E din `raw/papers/moldova-legal/_manifest.md`.

| Act | Articole | Consolidare | Pagină |
|---|---|---|---|
| L-135-2007 | 83 de bază + 10 cu exponent, numerotare 1–83 completă | 2026-03-27 | [[L-135-2007]] |
| L-220-2007 | 38 de bază + 6 cu exponent | 2026-07-23 | [[L-220-2007]] |

Exponenții sînt păstrați ca `^N` peste tot, inclusiv la alineate și litere. Integritatea textului
a fost dovedită linie cu linie față de o extracție simplă din același HTML: 667 și 532 de linii
identice. Două constatări `[de verificat]` la L-220-2007, ambele prezente în sursă, nu introduse
de noi: art. 6 lipsește fără marcaj de abrogare, iar art. 5 începe la alin. (2).

**Închis pentru persona P1 la 2026-09-04.** Legea 845/1992 a fost ingerată în aceeași zi, doc_id
155963, 35 de articole de bază plus 11 cu exponent, integritate dovedită pe 447 de linii.
**Acoperirea P1 este completă: cinci din cinci surse.** Două constatări `[de verificat]`: arts. 21
și 31 lipsesc fără temei în sursă, iar consolidarea este datată 2027-01-01, deci viitoare, cu o
singură dispoziție afectată.

## Rezolvat 2026-09-04: Codul fiscal și Codul administrativ

| Act | doc_id | Consolidare | Ancore |
|---|---|---|---|
| Codul fiscal 1163/1997 | 155071 | 2026-06-25 | 512 (353 de bază + 159 cu exponent), 11 titluri |
| Codul administrativ 116/2018 | 150447 | 2025-08-31 | 260 (258 + 2), fără lacune |

**Pasul fiscal al metodei P1 este acum ancorat**, iar cadrul pentru contestarea actelor CNPF și BNM
este prezent, deci constatările privind depășirea mandatului pot fi duse până la calea de atac.
Detalii în secțiunea F din `raw/papers/moldova-legal/_manifest.md`, inclusiv de ce cuprinsul
Codului fiscal este lăsat intenționat fără ancore.

O constatare `[de verificat]` la Codul fiscal: 26 de articole absente, 208–213 și 315–334,
explicate prin marcaje de abrogare la nivel de capitol, dar fără citare LP.

## Închis 2026-09-04: toate cele 11 acte sînt în wiki

Ultimele șapte coduri au fost ingerate în aceeași zi. **Lacuna semnalată de această notă nu mai
există.** Detalii în secțiunea G din `raw/papers/moldova-legal/_manifest.md`.

| Act | doc_id | Consolidare | Ancore |
|---|---|---|---|
| Codul de procedură civilă 225/2003 | 152860 | 2025-12-30 | 537 |
| Codul de executare 443/2004 | 156146 | **2026-12-02** ⚠ | 361 |
| Codul vamal 95/2021 | 154350 | 2026-09-01 | 472 |
| Codul muncii 154/2003 | 155882 | **2027-01-01** ⚠ | 416 |
| Codul contravențional 218/2008 | 155852 | **2026-09-13** ⚠ | 737 |
| Codul penal 985/2002 | 156133 | **2026-12-02** ⚠ | 566 |
| Codul de procedură penală 122/2003 | 156138 | **2026-12-02** ⚠ | 658 |

Cinci din șapte sînt consolidări viitoare, toate din două pachete de reformă adoptate la 30 iulie
2026, LP154 și LP172. Dispozițiile afectate sînt în `_meta/inforce/in-force-register.md`.

Două constatări `[de verificat]` rămân deschise: Codul muncii arts. 226–244 și Codul
contravențional art. 441, absente fără niciun temei în sursă.

**Această notă se poate arhiva.** Lacuna pe care o descrie este închisă; ce rămâne de urmărit stă
în `CLAUDE.md` și în registrul de intrare în vigoare.

## Actualizare 2026-09-04

Verificat integral față de starea reală a folderului. Ce s-a schimbat față de prima redactare:

1. Cronologia era inversată. `showdetails` precedă eșecul, nu îi urmează. Corectat mai sus.
2. Lista lipsurilor era incompletă pe propriul ei criteriu. Adăugată Legea 845/1992.
3. Condiția de așteptare a ancorării a căzut, ancorarea fiind încheiată.
4. Adăugate cele două `doc_id`, metoda de căutare și avertismentul privind exponenții.

Nemodificat și confirmat: cele 11 acte lipsesc într-adevăr din `raw/`; documentul 04 chiar indică
135/2007 și 220/2007 ca surse P1; citările din documentele 03 și 05 sunt fidele. O singură nuanță
de lectură a JSON-ului: doar primul act a fost efectiv testat, fiindcă cele zece erori următoare
sunt `Target page, context or browser has been closed`, adică sesiunea era deja căzută.
