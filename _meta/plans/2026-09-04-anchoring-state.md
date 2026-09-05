---
title: Starea ancorării stratului raw după 2026-09-04
created: 2026-09-04
updated: 2026-09-04
type: summary
tags: [moldova, legal-source, import, methodology, summary]
sources:
  - _meta/plans/2026-09-04-anchoring-brief.md
  - raw/papers/cnpf/_manifest.md
  - raw/papers/moldova-legal/_manifest.md
confidence: high
---

# Ce este ancorat și ce nu, după 2026-09-04

Notă de închidere pentru cele trei joburi din [[2026-09-04-anchoring-brief]], plus cele trei
treceri suplimentare asupra Codului civil cerute după aceea (reunirea liniilor, eliminarea
titlurilor de articol duplicate, eliminarea duplicatelor structurale). Scrisă ca să poată
fi lipită în harta de cunoștințe. Perimetrul auditat este `raw/papers/cnpf/` și
`raw/papers/moldova-legal/`.

## Ce s-a făcut

| Job | Fișiere | Ancore | Rezultat |
|---|---|---:|---|
| 1 — Codul civil | `CC-1107-2002` | 3 038 inserate | 2 657 articole + 381 niveluri structurale |
| 2 — forma `Art.N. –` | `L-192-1998`, `L-178-2020`, `L-177-2025` | 43 inserate | 31 + 8 + 4 |
| 3 — exponenți aplatizați | `L-171-2012`, `L-100-2017`, `L-139-2007` | 11 normalizate | 8 + 2 + 1 |
| 4 — reunirea liniilor | `CC-1107-2002` | — | 17 062 întreruperi de linie eliminate |
| 5 — titluri duplicate | `CC-1107-2002` | — | 2 656 de linii duplicate eliminate |
| 6 — duplicate structurale | `CC-1107-2002` | — | 170 de linii eliminate; 5 ancore `§` completate |
| 7 — ultimul duplicat | `CC-1107-2002` | — | 1 linie eliminată (`Secțiunea a 3-a- abrogată`) |

Metoda pentru joburile 1–3: ancorele se **inserează deasupra** liniilor originale (1–2) sau schimbă
**un singur token** pe linia de titlu (3). Acolo, niciun caracter din corp nu s-a schimbat, iar
dovada este strip-and-compare față de copia din backup, nu față de copia de lucru.

Jobul 4 atinge textul doar prin **spații albe**. Jobul 5 este singurul care **șterge** linii, și
doar copii exacte, recuperabile din ancora de deasupra. Nicio literă, cifră sau semn de punctuație
nu a fost rescris, corectat sau armonizat în niciuna dintre cele șapte treceri.

**Verificarea care contează**, rulabilă oricând:
`_meta/imports/anchoring/verify_chain.py`. Desface cele cinci treceri asupra Codului civil în
ordine inversă și compară cu extracția originală din 2026-07-13: **1 859 072 de octeți ne-spațiu,
sha256 `124bd2b606868231835c0a85b614f72196c717467df9ba40d78c50c9ece3504d`, identic.**

Backup: `C:\Users\harab\wiki-backups\wiki-2026-09-04-pre-anchoring` (859 fișiere, 664 108 199 octeți,
verificat identic înainte de orice scriere).

## A patra trecere — reunirea liniilor Codului civil

Singura operațiune care atinge textul propriu-zis. Garanția este la nivel de caracter: **se
schimbă doar spații albe**, fiecare reunire înlocuind o întrerupere de linie cu un singur spațiu.
Dovada elimină tot spațiul alb din rezultat și din corpul **anterior ancorării** și compară octet
cu octet — 1 859 072 de octeți ne-spațiu identici, verificare care acoperă ambele treceri deodată.

Fraze rupte la mijloc: **16 878 → 213** (−98,7%). Linii ne-goale: 30 041 → 12 979. Cele 213 rămase
sunt corecte — enumerări încheiate cu `; sau` înaintea unui punct `b)`, marcaje structurale urmate
de titlul lor, și preambulul lăsat intenționat neatins.

Regula nu folosește lungimea liniei, fiindcă lățimea de rupere nu are prag curat: lungimile
formează o pantă continuă între 80 și 98 de caractere. Se reunește doar o linie **neterminată
gramatical** — fără punctuație de final, sau terminată într-o abreviere ca `art.`, `alin.` — și
doar dacă următoarea nu începe o unitate nouă. Două paragrafe nu sunt niciodată contopite.

## A cincea trecere — eliminarea titlurilor duplicate

După reunire, titlul fiecărui articol exista de două ori, identic: o dată în ancoră, o dată în
corp. Copia din corp a fost ștearsă — **2 656 de linii**, corpul scăzând de la 17 009 la 14 353 de
linii.

Singura trecere care **șterge** text, deci regula este îngustă și reversibilitatea este
demonstrată, nu afirmată: se șterge doar o linie identică octet cu octet cu ancora imediat de
deasupra, iar reinserarea textului fiecărei ancore reproduce corpul anterior, octet cu octet.
**Art. 723 este păstrat** — linia lui de corp conține și începutul dispoziției, fiindcă extracția
le-a pus pe aceeași linie fizică.

## A șasea trecere — duplicatele structurale

Aceeași regulă de potrivire exactă, aplicată nivelurilor structurale: **170 de linii eliminate** —
`Cartea` (5), `Capitolul` (109), `§` (56). Corpul a scăzut de la 14 353 la 14 183 de linii.

**Reparație colaterală.** Cinci ancore `§` erau **trunchiate**: prima trecere luase linia `§` ca
atare, dar PDF-ul rupsese titlul paragrafului pe două linii, deci ancora păstra doar prima parte.
Au fost completate din linia de corp înainte ca aceasta să fie ștearsă. Un defect al jobului 1, pe
care reunirea liniilor l-a scos la iveală.

Trei niveluri **nu** au fost atinse, fiindcă ancora lor nu este o copie a liniei de dedesubt și
ștergerea ar fi pierdut text: `Titlul` (22), unde ancora normalizează `T i t l u l I` la
`Titlul I`; `Secțiunea` (172) și `Subsecțiunea` (17), unde ancora unește marcajul cu titlul iar
corpul le ține separate.

O trecere finală a eliminat și ultimul duplicat exact — `### Secțiunea a 3-a- abrogată`, singura
secțiune fără titlu propriu. **Nu mai există niciun duplicat exact în fișier.**

**Bilanț final asupra Codului civil:** 3 038 de ancore intacte, corpul de la 31 785 la 14 182 de
linii, textul juridic neschimbat față de extracție.

## Ce este acum citabil la nivel de articol

Tot perimetrul. Cele 15 legi CNPF/BNM, Codul civil și L-100-2017. `article_anchor_missing_target`
și `raw_sha_drift` sunt 0 în lint după ancorare.

Convenția de retrieval este uniformă: `## Articolul N.` pentru articole, `## Capitolul`,
`### Secțiunea`, `#### Subsecțiunea`. Codul civil adaugă `## Cartea`, `## Titlul` și `##### §`,
niveluri care nu existau anterior în corpus.

## Ce NU este ancorat

- **Corpusul BNM în engleză.** 89 de fișiere, 3 597 de marcaje `Article N` la început de linie,
  zero ancore — traducerile legilor 202/2017, 232/2016, 548/1995, 92/2022, 139/2007, 114/2012,
  62/2008. Aceeași clasă de defect, formă diferită, în afara perimetrului brief-ului. **Orice
  răspuns care se sprijină pe corpusul BNM în engleză nu este ancorat.**
- **Extractele UE** (`UE-*.md`) sunt structurate, nu text integral, prin construcție. Numerotarea
  rară nu este un defect. Sub-articolele cu literă (`4a`, `7a`–`7e`) sunt corecte ca atare.
- **HG-1170-2016 și HG-1171-2018** sunt structurate în puncte numerotate, nu articole. Corect zero.
- **Dreptul afacerilor și codurile lipsesc complet** — vezi
  [[2026-09-04-lacuna-drept-afaceri]]. Legea 135/2007, Legea 220/2007, Codul fiscal 1163/1997 și
  Codul administrativ 116/2018 nu sunt aici.

## Ce rămâne nedovedit — a se ridica înainte de citare

Șase constatări. Niciuna nu poate fi rezolvată din sursă; toate cer verificare la legis.md.

1. **Codul civil, art. 2047–2054.** Abrogate printr-un marcaj de secțiune
   (`Secțiunea a 3-a- abrogată`) care **nu identifică actul de abrogare**. Celelalte șase absențe
   poartă fiecare `[Art.NNNN abrogat prin LP251 din 10.07.25]`.
2. **L-192-1998, art. 21.** Absent, fără niciun temei în fișier: fără marcaj `abrogat`, fără notă,
   fără trimitere.
3. **L-171-2012, art. 80–87** absente și art. 88 prezent doar ca prefix al blocului 88^1–88^4.
   Fișierul nu conține niciun marcaj de abrogare.
4. **L-100-2017, art. 25, 26, 33, 52** absente, fără marcaj de abrogare.
5. **Corectare (aceeași zi).** Am scris inițial că niciunul dintre cei 12 exponenți normalizați
   nu are confirmare textuală. Este adevărat despre fișierele `.md` extrase și **fals despre
   surse**. HTML-ul legis.md păstrat în `_meta/imports/cnpf/legis-md-consolidated/` conține
   marcajul explicit: `Articolul 146<sup>1</sup>`, `Articolul 40<sup>1</sup>`,
   `Articolul 131<sup>1</sup>`, `Articolul 141<sup>1</sup>` (L-171-2012) și
   `Articolul 50<sup>1</sup>` (L-139-2007). Pierderea se produce la extracție, fiindcă
   `text_content()` concatenează cifrele și 146¹ devine `1461`. Verificarea am făcut-o doar pe
   textul extras, nu și pe HTML-ul păstrat în acest depozit — o omisiune. Toate normalizările
   coincid cu ce arată marcajul, deci nicio ancoră nu se schimbă. **Consecință operațională:
   ingestiile viitoare trebuie să mapeze `<sup>N</sup>` la `^N`, nu să deducă.**
   Singura excepție rămâne **L-192-1998 art. 13^1**: HTML-ul acelui act nu conține `<sup>` pentru
   articole, deci acesta se sprijină în continuare exclusiv pe argument pozițional.
6. **Aplatizarea exponentului apare și la nivel de alineat — acum dovedit, nu presupus.** HTML-ul
   L-192-1998 conține `[Art.15 al.(1<sup>1</sup>)…]` și `[Art.15 al.(1<sup>2</sup>)…]`, plus un
   punct `c<sup>1</sup>)`. Deci alin. (1¹), (1²) și lit. c¹) sunt aplatizate în text ca `(11)`,
   `(12)` și `c1)`. O citare la un alineat sau la o literă poate fi la fel de coruptă ca una la un
   articol. Netratat.

## Consolidări învechite — cele mai periculoase fișiere

Ancorarea lor este curată, deci arată de încredere. **26 de fișiere** au `consolidation_date` mai
veche de doi ani (înainte de 2024-09-04). Lintul raportează doar 14, fiindcă acoperă numai paginile
CNPF cu pagină wiki; cifra reală include extractele UE și `moldova-legal`.

Cele mai grave, cu vechimea la 2026-09-04:

| Fișier | Consolidare | Vechime |
|---|---|---:|
| `UE-2017-828` | 2017-05-20 | 9,3 ani |
| `L-308-2017` | 2018-12-01 | 7,8 ani |
| `HG-1170-2016` | 2019-11-22 | 6,8 ani |
| `L-2-2020` | 2020-03-27 | 6,4 ani |
| `L-1-2018` | 2020-04-20 | 6,4 ani |
| `L-122-2008`, `L-139-2007` | 2020-05-02 | 6,3 ani |
| `L-178-2020` | 2020-09-18 | 6,0 ani |
| `L-198-2020` | 2020-12-18 | 5,7 ani |
| `L-171-2012` | 2021-01-01 | 5,7 ani |
| `L-192-1998` | 2021-10-08 | 4,9 ani |
| `L-1134-1997` | 2022-01-10 | 4,6 ani |

`L-171-2012` este coloana vertebrală a pieței de capital și este ținut la versiunea 2021-01-01,
deși `L-177-2025` îl modifică. Înainte de a cita oricare dintre aceste acte, verifică
`consolidation_date` din frontmatter și spune în răspuns că textul poate fi depășit.

## Ce a fost corectat față de datele din brief

- Codul civil **are** 22 de marcaje `Titlul`, scrise `T i t l u l` cu spațiere între litere.
- Secțiunea este **172**, nu 111, și Subsecțiunea **17**, nu 10 — fișierul folosește două
  codificări de diacritice; o căutare cu o singură formă pierde 68 de titluri structurale.
- Codul civil are **56** de subdiviziuni `§`, nemenționate în brief.
- `L-178-2020` și `L-177-2025` **au** articole proprii, numerotate roman.
- Exponenții aplatizați sunt **12**, nu 3. Detectorul din brief ratează un **șir** de inserări
  (88^1–88^4), fiindcă după primul element predecesorul este el însuși aplatizat.
- Regula de reunire a titlurilor din brief ar fi înghițit text de dispoziție în **482** de titluri
  din Codul civil; discriminatorul corect este majuscula de la începutul liniei următoare.

## Scripturi

Toate repetabile, în `_meta/imports/anchoring/`:

| Script | Rol |
|---|---|
| `lib_anchor.py` | primitive comune: frontmatter, linii cu terminator păstrat, sha256 |
| `lib_superscript.py` | detector pozițional de exponenți aplatizați, conștient de șiruri |
| `anchor_cc.py` | jobul 1 — ancorarea Codului civil |
| `anchor_artdash.py` | jobul 2 — forma `Art.N. –` și cifrele romane |
| `fix_superscripts.py` | jobul 3 — normalizarea exponenților |
| `unwrap_cc.py` | reunirea liniilor |
| `dedup_titles.py` | eliminarea titlurilor de articol duplicate |
| `dedup_structural.py` | eliminarea duplicatelor `Cartea` / `Capitolul` / `§` |
| `detect_superscripts.py` | scanare pe corpus a exponenților, cu gradarea dovezilor |
| `sweep_art_forms.py` | scanare pe corpus a formelor `Art.` neancorate |
| `verify_anchoring.py` | verificare pentru joburile 1–2 (ancore inserate) |
| `verify_superscripts.py` | verificare pentru jobul 3 (titluri modificate) |
| `verify_unwrap.py` | verificare „doar spații albe" |
| `verify_dedup.py` | verificare prin reconstrucție a ștergerii |
| **`verify_chain.py`** | **verificarea care contează: desface toate trecerile și compară cu extracția originală** |
| `survey_cc.py`, `survey_sha_conventions.py`, `sample_diff.py` | analize pregătitoare |

## Notă tehnică — două convenții sha256 în corpus

`CC-1107-2002` este singurul fișier al cărui `sha256` se calculează pe **octeții bruți** de după
`---`, cu CRLF păstrat. Celelalte 47 normalizează CRLF→LF. Fiecare fișier a fost re-hash-uit sub
convenția pe care o folosea deja, ca `sha256_pre_anchoring` să rămână verificabil, iar convenția
este acum consemnată explicit în frontmatter ca `sha256_convention`. Neconcordanța în sine nu a
fost rezolvată.
