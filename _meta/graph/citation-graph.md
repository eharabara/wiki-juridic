# Graful de citare al actelor detinute

Generat 2026-09-18 13:07 de `_meta/graph/build_citation_graph.py`. Nu edita de mina; se reface rulind scriptul. Datele: `citation-graph.json` in acelasi folder.

**Ce este.** Trimiterile dintre actele detinute, extrase mecanic din textul brut: fiecare muchie poarta fisierul si liniile din care a fost citita, si nicio muchie nu este dedusa. Graful nu se citeaza. El spune unde sa deschizi fisierul, iar ancora se citeste.

**Regula de folosire.** Inainte de a cita un articol, cauta-l in tabelul „Dispozitii cu stare speciala si cine le citeaza”: daca apare, fie el, fie o dispozitie de care depinde nu se aplica astazi asa cum sta in text. Inainte de a ingera un act, citeste „Coada de ingerare”: acolo sint actele pe care textele detinute le citeaza si vault-ul nu le are.

## Numere

| | |
|---|---:|
| acte primare detinute (din care ancorate pe articole) | 101 (82) |
| dispozitii (noduri-articol) | 12293 |
| extrase UE detinute (noduri-tinta) | 32 |
| acte citate si nedetinute (noduri externe) | 560 |
| mentiuni de acte in text (din care ale actului insusi) | 4154 (369) |
| muchii act -> act (agregate pe segment-sursa) | 2795 |
| trimiteri la articole citite (in grupuri de enumerare) | 8781 (7663) |
|   rezolvate in actul curent | 7178 |
|   rezolvate in alt act detinut | 1070 |
|   nerezolvate: articolul nu are ancora in actul-tinta | 100 |
|   catre acte nedetinute (notate pe muchia act -> act) | 380 |
|   catre acte pe puncte (fara articole) | 33 |
|   autoreferinte (articolul se citeaza pe sine), ignorate | 20 |
| muchii articol -> articol (agregate) | 6776 |
| muchii articol -> act nerezolvate (agregate) | 88 |

Regula care a dat actul-tinta, pe trimiteri: din 1262, doua-puncte 46, intern 6994, modificare 37, paranteza 9. „intern” = niciun act in context, deci actul curent; „din” = `art. N ... din Legea X` sau `(art. N, M) Directiva X`; „paranteza” = `Legea X (art. N)`; „doua-puncte” = `din Codul X: art. N, M`; „modificare” = `Legea X se modifica dupa cum urmeaza: ... articolul N`. `din legea indicata` trimite la ultima lege numita in acelasi segment.

Coduri citate si pe nume si pe numar, unite dupa textul care le scrie impreuna: COD-audiovizualului = COD-260-2006; COD-educatiei = COD-152-2014; COD-electoral = COD-325-2022; COD-familiei = COD-1316-2000; COD-jurisdictiei-constitutionale = COD-502-1995; COD-transporturilor-rutiere = COD-150-2014.

## Coada de ingerare

Actele pe care textele detinute le citeaza si care nu sint in vault, in ordinea numarului de mentiuni. Un act citat de multe acte detinute inchide mai multe lanturi de trimitere decit unul citat des dintr-un singur loc; coloana a treia este cea care conteaza pentru ordinea de ingerare. Graful nu stie daca un act citat mai este in vigoare: o lege abrogata ramine citata de textele care n-au fost actualizate, si apare aici la fel ca una in vigoare.

### Acte moldovenesti citate pe numar

Legi, coduri si hotariri de Guvern identificate prin numar si an.

| act citat | mentiuni | acte care il citeaza | cel mai des din | articole citate |
|---|---:|---:|---|---|
| `COD-325-2022` Codul nr. 325/2022 | 38 | 9 | `L-436-2006` (14) | art. 178 (x2), art. 1, art. 89, art. 90 |
| `COD-150-2014` Codul nr. 150/2014 | 22 | 1 | `COD-218-2008` (22) | art. 94 (x2), art. 23, art. 43, art. 45 |
| `L-139-2010` Legea nr. 139/2010 | 16 | 9 | `DCU-PROC-RECONCILIERE` (2) | - |
| `L-199-2010` Legea nr. 199/2010 | 16 | 8 | `L-436-2006` (4) | art. 21 (x6), art. 22, art. 23 |
| `L-184-2016` Legea nr. 184/2016 | 15 | 6 | `CC-1107-2002` (6) | art. 8 (x3), art. 4, art. 14 |
| `L-407-2006` Legea nr. 407/2006 | 14 | 7 | `HCNPF-14-5-2016` (5) | art. 29 |
| `L-74-2020` Legea nr. 74/2020 | 14 | 3 | `L-325-2025` (8) | art. 6, art. 14, art. 19, art. 43 |
| `L-137-2015` Legea nr. 137/2015 | 13 | 7 | `L-198-2007` (4) | art. 19, art. 32, art. 39 |
| `COD-1316-2000` Codul nr. 1316/2000 | 13 | 5 | `L-246-2018` (3) | art. 35, art. 36, art. 37, art. 39 |
| `L-440-2001` Legea nr. 440/2001 | 13 | 5 | `COD-1163-1997` (6) | art. 5, art. 6, art. 13 |
| `L-124-2022` Legea nr. 124/2022 | 12 | 7 | `L-220-2007` (3) | art. 3 |
| `L-287-2017` Legea nr. 287/2017 | 11 | 9 | `L-234-2016` (2) | art. 4 (x5), art. 24 |
| `L-11-2017` Legea nr. 11/2017 | 11 | 3 | `COD-434-2023` (9) | art. 10 |
| `L-419-2006` Legea nr. 419/2006 | 10 | 7 | `DCU-REGULI-2026` (3) | art. 16, art. 42 |
| `L-202-2013` Legea nr. 202/2013 | 10 | 6 | `COD-218-2008` (3) | art. 2, art. 3, art. 5, art. 10 |
| `L-488-1999` Legea nr. 488/1999 | 10 | 6 | `COD-22-2024` (4) | - |
| `L-121-2007` Legea nr. 121/2007 | 9 | 7 | `HCNPF-14-5-2016` (3) | art. 6, art. 14, art. 53, art. 54^1 |
| `L-989-2002` Legea nr. 989/2002 | 9 | 7 | `L-2-2020` (2) | art. 5 |
| `L-384-2023` Legea nr. 384/2023 | 9 | 6 | `L-325-2025` (3) | - |
| `L-271-2017` Legea nr. 271/2017 | 9 | 5 | `L-181-2023` (3) | art. 44 (x3), art. 2, art. 21, art. 45 |
| `L-231-2010` Legea nr. 231/2010 | 9 | 4 | `L-105-2003` (3) | art. 14, art. 19^1, art. 21, art. 21^15 |
| `L-575-2003` Legea nr. 575/2003 | 9 | 4 | `L-160-2023` (6) | art. 16 |
| `L-443-1995` Legea nr. 443/1995 | 9 | 1 | `L-158-2008` (9) | art. 6, art. 8 |
| `L-768-2000` Legea nr. 768/2000 | 9 | 1 | `L-436-2006` (9) | art. 5 (x5) |
| `L-199-1998` Legea nr. 199/1998 | 8 | 3 | `L-171-2012` (5) | - |
| `L-151-2022` Legea nr. 151/2022 | 8 | 1 | `COD-434-2023` (8) | art. 4 (x3), art. 8 (x2), art. 12, art. 19 |
| `L-100-2001` Legea nr. 100/2001 | 7 | 3 | `L-246-2018` (3) | art. 3, art. 5, art. 7, art. 11 |
| `L-174-2021` Legea nr. 174/2021 | 7 | 3 | `L-160-2011` (5) | art. 11 (x2), art. 4 |
| `L-186-2008` Legea nr. 186/2008 | 7 | 3 | `COD-154-2003` (5) | - |
| `L-291-2016` Legea nr. 291/2016 | 7 | 3 | `COD-174-2018` (4) | - |
| … inca 335 in JSON | | | | |

### Acte UE citate si neextrase

Directive si regulamente UE care nu au un extras `UE-*` in `raw/papers/cnpf/`.

| act citat | mentiuni | acte care il citeaza | cel mai des din | articole citate |
|---|---:|---:|---|---|
| `EU-TFUE` Tratatul privind functionarea Uniunii Europene | 5 | 4 | `AA-2014` (2) | art. 101 |
| `EU-L-2003-6` Directiva 2003/6 | 5 | 1 | `AA-2014` (5) | - |
| `EU-L-2005-60` Directiva 2005/60 | 4 | 3 | `AA-2014` (2) | - |
| `EU-R-2009-1060` Regulamentul (UE) nr. 1060/2009 | 4 | 3 | `L-171-2012` (2) | art. 2, art. 3, art. 4, art. 6 |
| `EU-L-2004-39` Directiva 2004/39 | 4 | 2 | `AA-2014` (3) | - |
| `EU-R-2004-2006` Regulamentul (UE) nr. 2006/2004 | 4 | 2 | `L-105-2003` (3) | - |
| `EU-L-2002-87` Directiva 2002/87 | 3 | 3 | `L-250-2017` (1) | art. 9 |
| `EU-L-2018-843` Directiva 2018/843 | 3 | 3 | `L-92-2022` (1) | - |
| `EU-L-1999-44` Directiva 1999/44 | 3 | 2 | `L-133-2018` (2) | - |
| `EU-L-2006-48` Directiva 2006/48 | 3 | 2 | `AA-2014` (2) | - |
| `EU-L-2006-70` Directiva 2006/70 | 3 | 2 | `AA-2014` (2) | - |
| `EU-L-2014-23` Directiva 2014/23 | 3 | 2 | `L-20-2026` (2) | - |
| `EU-L-2014-24` Directiva 2014/24 | 3 | 2 | `L-131-2015` (2) | art. 1, art. 2, art. 22, art. 23 |
| `EU-L-2009-31` Directiva 2009/31 | 3 | 1 | `L-86-2014` (3) | - |
| `EU-R-2013-952` Regulamentul (UE) nr. 952/2013 | 3 | 1 | `COD-95-2021` (3) | - |
| `EU-R-2017-2394` Regulamentul (UE) 2017/2394 | 3 | 1 | `L-105-2003` (3) | - |
| `EU-L-1985-611` Directiva 1985/611 | 2 | 2 | `L-171-2012` (1) | - |
| `EU-L-1989-665` Directiva 1989/665 | 2 | 2 | `L-20-2026` (1) | art. 1, art. 2 |
| `EU-L-1992-13` Directiva 1992/13 | 2 | 2 | `L-20-2026` (1) | art. 2 (x2), art. 1, art. 3 |
| `EU-L-1995-46` Directiva 1995/46 | 2 | 2 | `L-195-2024` (1) | - |
| … inca 109 in JSON | | | | |

### Legi citate doar pe nume, fara corespondent in vault

Fara numar in text si fara un titlu detinut care sa le contina, deci identificate numai prin primele cuvinte; acelasi act poate aparea sub doua forme flexionate. Orientativ.

| act citat | mentiuni | acte care il citeaza | cel mai des din | articole citate |
|---|---:|---:|---|---|
| `LEGE:contabilitatii` Legea contabilităţii | 6 | 3 | `L-139-2007` (2) | - |
| `LEGE:mediere` Legea cu privire la mediere | 6 | 3 | `COD-225-2003` (2) | - |
| `LEGE:avocatura` Legea cu privire la avocatură | 6 | 2 | `L-198-2007` (5) | - |
| `LEGE:serviciului-public` Legea serviciului public | 6 | 1 | `L-158-2008` (6) | art. 33 |
| `LEGE:statutul-municipiului` Legea privind statutul municipiului | 6 | 1 | `L-436-2006` (6) | - |
| `LEGE:privind` Legea privind | 5 | 2 | `L-1134-1997` (4) | - |
| `LEGE:finantele-publice-locale` Legea privind finanţele publice locale | 4 | 2 | `L-181-2014` (3) | - |
| `LEGE:protectia-martorilor-si-altor` Legea cu privire la protecţia martorilor şi | 4 | 2 | `COD-122-2003` (3) | - |
| `LEGE:descentralizarea-administrativa` Legea privind descentralizarea administrativă | 4 | 1 | `L-436-2006` (4) | art. 4 (x3) |
| `LEGE:din` Legea din | 3 | 1 | `CONST-1994` (3) | - |
| `LEGE:locuinte` Legea cu privire la locuinţe | 3 | 1 | `L-436-2006` (3) | - |
| `LEGE:protectia-indicatiilor-geografice` Legea privind protecţia indicaţiilor geografice | 3 | 1 | `COD-218-2008` (3) | - |
| `LEGE:publicitate-si-cu` Legea cu privire la publicitate şi cu | 3 | 1 | `COD-174-2018` (3) | - |
| `LEGE:statutul-alesului-local` Legea privind statutul alesului local | 3 | 1 | `L-436-2006` (3) | - |
| `LEGE:achizitiile-publice` Legea privind achiziţiile publice | 2 | 2 | `L-181-2014` (1) | - |
| … inca 51 in JSON | | | | |

## Acquis: extrasele UE detinute si actele care le citeaza

Mentiunile actelor detinute catre cele 29 de extrase `UE-*`. Schita unei concordante: un act care citeaza o directiva o transpune, o aplica sau doar o numeste, si numai textul spune care.

| extras UE | mentiuni | citat din |
|---|---:|---|
| `UE-1986-635` | 0 | - |
| `UE-1991-674` | 1 | `AA-2014` (1) |
| `UE-1994-19` | 1 | `AA-2014` (1) |
| `UE-2004-109` | 2 | `AA-2014` (2) |
| `UE-2004-25` | 0 | - |
| `UE-2007-36` | 1 | `L-1134-1997` (1) |
| `UE-2008-48` | 0 | - |
| `UE-2009-103` | 2 | `AA-2014` (1), `L-106-2022` (1) |
| `UE-2009-138` | 6 | `L-106-2022` (2), `L-92-2022` (2), `AA-2014` (1), `L-308-2017` (1) |
| `UE-2009-65` | 2 | `AA-2014` (1), `L-171-2012` (1) |
| `UE-2011-61` | 2 | `L-2-2020` (2) |
| `UE-2014-57` | 0 | - |
| `UE-2014-65` | 1 | `L-2-2020` (1) |
| `UE-2015-849` | 4 | `L-308-2017` (2), `L-106-2022` (1), `L-92-2022` (1) |
| `UE-2016-2341` | 1 | `L-198-2020` (1) |
| `UE-2016-97` | 0 | - |
| `UE-2017-1129` | 1 | `L-181-2023` (1) |
| `UE-2017-1132` | 3 | `L-1134-1997` (2), `L-133-2018` (1) |
| `UE-2017-828` | 0 | - |
| `UE-2020-1503` | 1 | `L-181-2023` (1) |
| `UE-2021-2118` | 0 | - |
| `UE-2023-2225` | 0 | - |
| `UE-2024-1620` | 0 | - |
| `UE-2024-1624` | 0 | - |
| `UE-2024-1640` | 0 | - |
| `UE-596-2014` | 0 | - |
| `UE-600-2014` | 0 | - |
| `UE-648-2012` | 2 | `L-202-2017` (1), `L-308-2017` (1) |
| `UE-648-2012-priority-articles-2026-07-09` | 0 | - |
| `UE-909-2014` | 1 | `L-234-2016` (1) |
| `UE-97-9` | 1 | `AA-2014` (1) |
| `UE-98-26` | 3 | `AA-2014` (1), `L-183-2016` (1), `L-234-2016` (1) |

## Trimiteri catre acte abrogate

Acte detinute care nu mai sint in vigoare, si actele din corpus care trimit la ele. Fiecare trimitere de mai jos citeste astazi text mort. Nu inseamna ca actul care trimite e gresit: inseamna ca trimiterea trebuie citita prin dispozitiile tranzitorii ale actului abrogator, care de regula spune ca trimiterile la legea veche se considera facute la cea noua.

| act abrogat | de la | prin | mentiuni | acte care il citeaza | articole citate |
|---|---|---|---:|---:|---|
| `L-133-2011` | 2026-08-23 | LP195 din 25.07.24 | 48 | 21 | art. 2, art. 4, art. 5, art. 6, art. 12, art. 13, art. 20, art. 23 |

`L-133-2011` este citat din: `COD-122-2003`, `COD-218-2008`, `COD-95-2021`, `DCU-REGULI-2026`, `HCNPF-14-5-2016`, `L-105-2003`, `L-114-2012`, `L-122-2008`, `L-132-2016`, `L-1543-1998`, `L-171-2012`, `L-181-2023`, `L-195-2024`, `L-202-2017`, `L-246-2018`, `L-284-2004`, `L-308-2017`, `L-325-2013`, `L-325-2025`, `L-436-2006`, `L-548-1995`.

Limita care ramine: pentru actele **nedetinute** din coada de ingerare graful tot nu stie daca mai sint in vigoare. Se afla numai deschizind fisa lor pe legis.md, si nici acolo cimpul „Data abrogarii” nu este de incredere: pentru `L-133-2011` el era gol, desi corpul consolidarii declara abrogarea.

## Dispozitii cu stare speciala si cine le citeaza

Dispozitiile care apar in registrul in-force (textul din fisier nu se aplica inca), in registrul HCC (declarate neconstitutionale, in tot sau in parte) sau al caror titlu spune „abrogat”, si muchiile articol -> articol care intra in ele. Un articol din coloana „citat din” depinde de o dispozitie care nu sta in picioare asa cum e scrisa. Numai dispozitiile cu cel putin o citare intra aici, intii cele citate din alte acte; toate starile sint in JSON.

| dispozitie | stare | citari (din alte acte) | citat din |
|---|---|---:|---|
| `L-548-1995#art.11` l.294 | HCC: HCC31/2013-10-01, al.(4), articol intreg | 7 (3) | `L-548-1995#art.75^1`, `L-114-2012#art.98`, `L-202-2017#art.144`, `L-232-2016#art.319`, `L-548-1995#art.6` |
| `COD-985-2002#art.72` l.887 | in-force: modificare de la 2026-12-02 | 3 (3) | `COD-122-2003#art.469` l.5729, `COD-443-2004#art.197` l.2075, `COD-443-2004#art.255` l.2717 |
| `L-133-2016#art.3` l.138 | in-force: modificare de la 2027-01-01 (lit.e^2)) | 6 (2) | `L-132-2016#art.34`, `L-132-2016#art.39`, `L-133-2016#art.23`, `L-133-2016#art.24`, `L-133-2016#art.4`, `L-133-2016#art.7` |
| `COD-122-2003#art.191` l.3074 | in-force: modificare de la 2026-12-02; HCC: HCC17/2016-05-19, omisiune legislativa (+1) | 5 (2) | `COD-443-2004#art.301`, `COD-122-2003#art.192`, `COD-122-2003#art.309`, `COD-122-2003#art.310` |
| `COD-218-2008#art.34` l.1025 | HCC: HCC7/2018-04-26, alin. (3), text din articol | 3 (2) | `COD-443-2004#art.315` l.3271, `COD-218-2008#art.293^2` l.4877 |
| `L-181-2014#art.43` l.564 | in-force: reformulare de la 2027-01-01 | 3 (2) | `COD-225-2003#art.84` l.877, `L-181-2014#art.25` l.424, `L-213-2023#art.6` l.127 |
| `COD-225-2003#art.449` l.3638 | HCC: HCC16/2013-06-25, lit. f), in parte | 12 (1) | `COD-225-2003#art.450`, `COD-116-2018#art.170`, `COD-225-2003#art.447`, `COD-225-2003#art.451`, `COD-225-2003#art.451^1`, `COD-225-2003#art.453` |
| `COD-225-2003#art.267` l.2173 | HCC: HCC33/2016-11-17, lit. b), in parte | 7 (1) | `COD-225-2003#art.268`, `COD-225-2003#art.185`, `COD-225-2003#art.49`, `COD-225-2003#art.89`, `COD-225-2003#art.98`, `COD-443-2004#art.163` |
| `COD-225-2003#art.170` l.1503 | HCC: HCC33/2016-11-17, alin. (1) lit. c), in parte | 5 (1) | `COD-225-2003#art.478`, `COD-225-2003#art.483`, `COD-225-2003#art.49`, `COD-225-2003#art.89`, `L-9-2026#art.47` |
| `COD-122-2003#art.179` l.2923 | in-force: modificare de la 2026-12-02 | 3 (1) | `COD-122-2003#art.181` l.2940, `COD-443-2004#art.297` l.3123 |
| `COD-122-2003#art.273` l.4013 | HCC: HCC29/2021-09-21, alin. (1) lit. d^2), in parte | 3 (1) | `COD-122-2003#art.166` l.2785, `COD-122-2003#art.215^2` l.3411, `COD-443-2004#art.245` l.2587 |
| `COD-122-2003#art.471` l.5755 | in-force: introducere de la 2026-12-02 | 3 (1) | `COD-122-2003#art.473` l.5819, `COD-122-2003#art.473^1` l.5825, `COD-443-2004#art.275` l.2923 |
| `COD-443-2004#art.15` l.389 | HCC: HCC39/2017-12-14, al.(2) lit.d), in parte | 3 (1) | `COD-443-2004#art.30` l.564, `COD-225-2003#art.470` l.3900 |
| `COD-122-2003#art.186` l.3006 | HCC: HCC3/2016-02-23, alin. (3), (5), (8), (9), text din articol | 2 (1) | `COD-122-2003#art.195` l.3135, `COD-443-2004#art.198` l.2083 |
| `L-132-2016#art.7` l.154 | in-force: introducere de la 2027-01-01 | 2 (1) | `L-132-2016#art.33` l.579, `L-133-2016#art.7^1` l.229 |
| `L-133-2016#art.18` l.325 | in-force: introducere de la 2027-01-01 | 2 (1) | `COD-154-2003#art.46` l.804, `L-133-2016#art.17` l.323 |
| `L-135-2007#art.30` l.327 | HCC: HCC27/2016-09-27, al.(2) [numerotarea de la data hotaririi], subunitate | 2 (1) | `L-135-2007#art.25` l.279, `L-181-2023#art.49` l.737 |
| `COD-122-2003#art.6` l.482 | in-force: introducere de la 2026-12-02 (pct.8^1); HCC: HCC2/2020-01-23, pct. 11^1), text din articol | 1 (1) | `COD-443-2004#art.98^1` l.1171 |
| `COD-218-2008#art.423^4` l.6663 | abrogat | 1 (1) | `L-195-2024#art.90` l.1173 |
| `COD-218-2008#art.427` l.6740 | HCC: HCC26/2024-12-12, alin.(2), text din articol | 1 (1) | `COD-95-2021#art.408` l.4429 |
| `COD-218-2008#art.74^1` l.1705 | abrogat | 1 (1) | `L-195-2024#art.90` l.1173 |
| `COD-225-2003#art.343^6` l.3015 | HCC: HCC37/2021-12-07, text din articol | 1 (1) | `L-325-2013#art.14` l.259 |
| `COD-443-2004#art.22` l.455 | HCC: HCC17/2017-05-10, al.(1) lit.v), text din articol | 1 (1) | `CC-1107-2002#art.757` l.5384 |
| `COD-985-2002#art.189` l.2589 | HCC: HCC24/2019-10-17, alin. (3) lit. f), text din articol | 1 (1) | `COD-122-2003#art.229^2` l.3554 |
| `L-131-2015#art.80` l.1493 | abrogat | 1 (1) | `L-20-2026#art.29` l.424 |
| `L-131-2015#art.86` l.1506 | abrogat | 1 (1) | `L-20-2026#art.29` l.428 |
| `L-845-1992#art.36` l.574 | abrogat | 1 (1) | `COD-1163-1997#art.227^1` l.5972 |
| `COD-1163-1997#art.88` l.2979 | HCC: HCC7/2014-02-13, alin. (7), subunitate | 9 (0) | `COD-1163-1997#art.92`, `COD-1163-1997#art.372`, `COD-1163-1997#art.69^7`, `COD-1163-1997#art.73`, `COD-1163-1997#art.76`, `COD-1163-1997#art.79`, … (+2) |
| `COD-1163-1997#art.291` l.6915 | HCC: HCC2/2014-01-28, in parte | 8 (0) | `COD-1163-1997#art.293` l.6950, `COD-1163-1997#art.292` l.6944 |
| `COD-1163-1997#art.289` l.6866 | HCC: HCC2/2014-01-28, in parte | 6 (0) | `COD-1163-1997#art.297` l.7019, `COD-1163-1997#art.298` l.7028, `COD-1163-1997#art.294` l.6962 |
| `COD-122-2003#art.401` l.5227 | HCC: HCC9/2008-05-20, alin. (1) pct. 3), text din articol | 6 (0) | `COD-122-2003#art.402`, `COD-122-2003#art.420`, `COD-122-2003#art.421`, `COD-122-2003#art.438`, `COD-122-2003#art.445`, `COD-122-2003#art.447` |
| `COD-443-2004#art.174^1` l.1864 | in-force: introducere de la 2026-12-02 | 6 (0) | `COD-443-2004#art.196`, `COD-443-2004#art.204`, `COD-443-2004#art.263`, `COD-443-2004#art.269`, `COD-443-2004#art.271`, `COD-443-2004#art.290` |
| `COD-122-2003#art.308` l.4408 | in-force: modificare de la 2026-12-02 | 4 (0) | `COD-122-2003#art.312` l.4467, `COD-122-2003#art.166` l.2789, `COD-122-2003#art.523` l.6335 |
| `COD-122-2003#art.385` l.5051 | in-force: introducere de la 2026-12-02 | 4 (0) | `COD-122-2003#art.382`, `COD-122-2003#art.392`, `COD-122-2003#art.485`, `COD-122-2003#art.498` |
| `COD-122-2003#art.42` l.840 | HCC: HCC3/2012-02-09, alin. (7), in parte | 4 (0) | `COD-122-2003#art.256`, `COD-122-2003#art.279^1`, `COD-122-2003#art.43`, `COD-122-2003#art.561` |
| `COD-122-2003#art.421` l.5378 | HCC: HCC16/2005-07-19, text din articol | 4 (0) | `COD-122-2003#art.423`, `COD-122-2003#art.429`, `COD-122-2003#art.432`, `COD-122-2003#art.433` |
| `COD-225-2003#art.437` l.3546 | HCC: HCC20/2022-11-03, alin. (1), text din articol | 4 (0) | `COD-225-2003#art.426^1`, `COD-225-2003#art.436`, `COD-225-2003#art.438`, `COD-225-2003#art.439` |
| `COD-1163-1997#art.264` l.6326 | HCC: HCC10/2024-04-04, alin. (1) si (2), text din articol | 3 (0) | `COD-1163-1997#art.214` l.5487, `COD-1163-1997#art.226^2` l.5641, `COD-1163-1997#art.265` l.6337 |
| `COD-1163-1997#art.6` l.1554 | HCC: HCC5/2024-03-05, alin. (11), subunitate | 3 (0) | `COD-1163-1997#art.226^1` l.5629, `COD-1163-1997#art.5` l.1526, `COD-1163-1997#art.7` l.1621 |
| `COD-122-2003#art.321` l.4553 | in-force: modificare de la 2026-12-02; HCC: HCC3/2023-01-24, alin. (2) pct. 3), text din articol | 3 (0) | `COD-122-2003#art.199` l.3179, `COD-122-2003#art.412` l.5295, `COD-122-2003#art.559` l.6843 |
| `COD-174-2018#art.28` l.614 | HCC: HCC6/2022-03-10, al.(1), text din articol | 3 (0) | `COD-174-2018#art.25` l.564, `COD-174-2018#art.84` l.1545, `COD-174-2018#art.88` l.1609 |
| `COD-1163-1997#art.260` l.6258 | HCC: HCC20/2018-07-04, alin. (4), text din articol | 2 (0) | `COD-1163-1997#art.229` l.5996, `COD-1163-1997#art.234` l.6044 |
| `COD-122-2003#art.177` l.2890 | in-force: introducere de la 2026-12-02 | 2 (0) | `COD-122-2003#art.241^1` l.3667, `COD-122-2003#art.471` l.5770 |
| `COD-122-2003#art.287^1` l.4181 | in-force: modificare de la 2026-12-02 | 2 (0) | `COD-122-2003#art.287^2` l.4196 |
| `L-325-2013#art.17` l.292 | HCC: HCC37/2021-12-07, al.(2), subunitate (+2) | 2 (0) | `L-325-2013#art.10` l.214, `L-325-2013#art.21` l.381 |
| `L-845-1992#art.36^1` l.580 | in-force: introducere de la 2027-01-01 (pct.4, lit.l)) | 2 (0) | `L-845-1992#art.36^3` l.608 |
| `COD-1163-1997#art.123` l.3751 | HCC: HCC17/2014-05-29, alin. (7), subunitate | 1 (0) | `COD-1163-1997#art.262` l.6301 |
| `COD-1163-1997#art.290` l.6893 | HCC: HCC2/2014-01-28, in parte | 1 (0) | `COD-1163-1997#art.297` l.7019 |
| `COD-122-2003#art.138^1` l.2383 | in-force: modificare de la 2026-12-02 | 1 (0) | `COD-122-2003#art.138^5` l.2430 |
| `COD-122-2003#art.178` l.2913 | in-force: modificare de la 2026-12-02; HCC: HCC19/2018-07-03, omisiune legislativa | 1 (0) | `COD-122-2003#art.547` l.6701 |
| `COD-122-2003#art.180` l.2930 | in-force: modificare de la 2026-12-02 | 1 (0) | `COD-122-2003#art.181` l.2940 |
| `COD-122-2003#art.185` l.2994 | HCC: HCC27/2018-10-30, al.(1), subunitate | 1 (0) | `COD-122-2003#art.188` l.3050 |
| `COD-122-2003#art.192` l.3095 | HCC: HCC15/2020-05-28, alin. (2), subunitate | 1 (0) | `COD-122-2003#art.192^1` l.3109 |
| `COD-122-2003#art.287` l.4173 | HCC: HCC12/2015-05-14, alin. (1), subunitate | 1 (0) | `COD-122-2003#art.326` l.4601 |
| `COD-122-2003#art.400` l.5222 | HCC: HCC3/2012-02-09, alin. (3), in parte | 1 (0) | `COD-122-2003#art.465^8` l.5677 |
| `COD-122-2003#art.74` l.1508 | in-force: modificare de la 2026-12-02 | 1 (0) | `COD-122-2003#art.223` l.3484 |
| `COD-154-2003#art.46` l.799 | in-force: introducere de la 2027-01-01 | 1 (0) | `COD-154-2003#art.391` l.3694 |
| `COD-154-2003#art.90` l.1302 | HCC: HCC9/2025-07-22, al.(2), lit. a), text din articol | 1 (0) | `COD-154-2003#art.330` l.3261 |
| `COD-174-2018#art.66` l.1278 | HCC: HCC36/2021-11-23, al.(7), text din articol | 1 (0) | `COD-174-2018#art.84` l.1542 |
| `COD-218-2008#art.197^1` l.3394 | abrogat | 1 (0) | `COD-218-2008#art.431` l.6786 |
| `COD-218-2008#art.20` l.918 | abrogat | 1 (0) | `COD-218-2008#art.440^1` l.7025 |
| `COD-218-2008#art.233` l.3966 | HCC: HCC11/2018-05-08, alin. (3), text din articol | 1 (0) | `COD-218-2008#art.41` l.1109 |
| `COD-218-2008#art.445` l.7088 | HCC: HCC32/2018-11-29, articol intreg | 1 (0) | `COD-218-2008#art.451^3` l.7208 |
| `COD-218-2008#art.62` l.1495 | abrogat | 1 (0) | `COD-218-2008#art.293^2` l.4879 |
| `COD-225-2003#art.306` l.2677 | HCC: HCC33/2016-11-17, alin. (2), text din articol | 1 (0) | `COD-225-2003#art.77` l.835 |
| `COD-225-2003#art.39` l.527 | HCC: HCC3/2012-02-09, alin. (11^1), subunitate | 1 (0) | `COD-225-2003#art.41^1` l.569 |
| `COD-225-2003#art.58` l.696 | HCC: HCC33/2016-11-17, alin. (2), (2^1), (6), text din articol | 1 (0) | `COD-225-2003#art.79` l.841 |
| `COD-443-2004#art.161` l.1737 | HCC: HCC8/2019-04-05, al.(1) teza a doua, text din articol | 1 (0) | `COD-443-2004#art.79` l.1003 |
| `COD-443-2004#art.174` l.1855 | HCC: HCC18/2013-07-04, alin. (3^1), subunitate | 1 (0) | `COD-443-2004#art.287` l.3009 |
| `COD-443-2004#art.263` l.2801 | in-force: modificare de la 2026-12-02 | 1 (0) | `COD-443-2004#art.194` l.2052 |
| `COD-443-2004#art.61` l.826 | HCC: HCC22/2019-10-08, al.(1), text din articol | 1 (0) | `COD-443-2004#art.60` l.824 |
| `COD-95-2021#art.277^2` l.3013 | abrogat | 1 (0) | `COD-95-2021#art.277` l.3000 |
| `COD-985-2002#art.317` l.4800 | in-force: modificare de la 2026-12-02 | 1 (0) | `COD-985-2002#art.21` l.541 |
| `COD-985-2002#art.328` l.4977 | HCC: HCC22/2017-06-27, alin. (1), text din articol (+1) | 1 (0) | `COD-985-2002#art.55` l.741 |
| `COD-985-2002#art.329` l.4993 | HCC: HCC24/2019-10-17, alin. (1) si alin. (2) lit. b), text din articol | 1 (0) | `COD-985-2002#art.134^20` l.1582 |
| `COD-985-2002#art.335` l.5088 | HCC: HCC24/2019-10-17, alin. (1^1), text din articol (+1) | 1 (0) | `COD-985-2002#art.55` l.741 |
| `L-1543-1998#art.15^8` l.548 | in-force: introducere de la 2027-01-01 | 1 (0) | `L-1543-1998#art.15^4` l.507 |
| `L-158-2008#art.53` l.949 | HCC: HCC6/2016-03-03, lit.c), subunitate | 1 (0) | `L-158-2008#art.41` l.757 |
| `L-181-2014#art.20` l.316 | in-force: reformulare de la 2027-01-01 | 1 (0) | `L-181-2014#art.82` l.1009 |
| `L-181-2014#art.21` l.339 | in-force: reformulare de la 2027-01-01 | 1 (0) | `L-181-2014#art.82` l.1009 |
| … inca 3 dispozitii, in JSON | | | |

Stari atasate dispozitiilor, in total: 60 in-force, 94 HCC, 268 abrogat. 83 dintre ele au cel putin o citare intrata, 27 din alte acte.

Acte care poarta hotariri HCC fara articol atribuit (orice citare din ele poate lovi textul anulat): `CONST-1994` (2), `L-132-2016` (2), `L-181-2014` (2), `L-213-2023` (1), `L-24-2008` (1), `L-325-2013` (1).

## Actele: ce citeaza si de cine sint citate

Pe act: tintele distincte ale mentiunilor (detinute + externe), actele detinute distincte care il mentioneaza, trimiterile la articole rezolvate in propriul text, rezolvate in alt act detinut, si nerezolvate (articolul citat nu are ancora in actul-tinta: abrogat cu ciotul sters, renumerotat, exponent turtit in sursa, sau o greseala de citire).

| act | ancore | citeaza (acte) | citat de (acte) | art. interne | art. in alte acte | nerezolvate | mentiuni externe |
|---|---:|---:|---:|---:|---:|---:|---:|
| `AA-2014` | 11 | 44 | 0 | 4 | 0 | 18 | 64 |
| `CC-1107-2002` | 2657 | 27 | 33 | 1017 | 5 | 1 | 24 |
| `COD-116-2018` | 260 | 13 | 33 | 106 | 10 | 1 | 6 |
| `COD-1163-1997` | 511 | 66 | 24 | 447 | 18 | 1 | 80 |
| `COD-122-2003` | 658 | 26 | 13 | 471 | 219 | 2 | 26 |
| `COD-154-2003` | 416 | 26 | 13 | 198 | 3 | 0 | 26 |
| `COD-174-2018` | 98 | 18 | 4 | 71 | 4 | 0 | 19 |
| `COD-218-2008` | 737 | 57 | 34 | 508 | 50 | 10 | 79 |
| `COD-22-2024` | 96 | 26 | 5 | 18 | 5 | 0 | 26 |
| `COD-225-2003` | 540 | 23 | 20 | 213 | 31 | 17 | 15 |
| `COD-434-2023` | 390 | 44 | 8 | 137 | 18 | 1 | 61 |
| `COD-443-2004` | 361 | 30 | 20 | 129 | 75 | 0 | 21 |
| `COD-95-2021` | 472 | 37 | 3 | 430 | 8 | 0 | 31 |
| `COD-985-2002` | 566 | 22 | 23 | 166 | 3 | 1 | 12 |
| `CONST-1994` | 157 | 4 | 34 | 13 | 1 | 0 | 5 |
| `DCA-61-2024` | 0 | 5 | 0 | 0 | 5 | 0 | 4 |
| `DCU-PROC-COMISIOANE` | 0 | 2 | 0 | 0 | 1 | 0 | 2 |
| `DCU-PROC-DETINATOR` | 0 | 1 | 0 | 0 | 0 | 0 | 2 |
| `DCU-PROC-GARANTII` | 0 | 1 | 0 | 0 | 0 | 0 | 2 |
| `DCU-PROC-INREGISTRARE-VM` | 0 | 4 | 0 | 0 | 3 | 0 | 1 |
| `DCU-PROC-INSOLVABILITATE` | 0 | 4 | 0 | 0 | 1 | 0 | 2 |
| `DCU-PROC-PARTICIPANT` | 0 | 1 | 0 | 0 | 0 | 0 | 2 |
| `DCU-PROC-RECLAMATII` | 0 | 1 | 0 | 0 | 0 | 0 | 2 |
| `DCU-PROC-RECONCILIERE` | 0 | 2 | 0 | 0 | 0 | 0 | 2 |
| `DCU-REGULI-2026` | 94 | 11 | 0 | 0 | 21 | 0 | 7 |
| `HBN-127-2013` | 0 | 7 | 0 | 0 | 41 | 1 | 3 |
| `HBN-130-2013` | 0 | 3 | 0 | 0 | 6 | 1 | 0 |
| `HCNPF-14-5-2016` | 0 | 12 | 0 | 0 | 29 | 2 | 14 |
| `HCNPF-38-5-2015` | 0 | 9 | 0 | 0 | 16 | 1 | 4 |
| `HG-1170-2016` | 0 | 16 | 1 | 0 | 5 | 0 | 20 |
| `HG-1171-2018` | 0 | 3 | 0 | 0 | 2 | 0 | 2 |
| `HG-553-2024` | 0 | 3 | 0 | 0 | 13 | 0 | 0 |
| `HG-574-2024` | 0 | 5 | 1 | 0 | 2 | 0 | 3 |
| `HG-582-2022` | 0 | 5 | 0 | 0 | 16 | 2 | 0 |
| `HG-743-2024` | 0 | 11 | 0 | 0 | 19 | 0 | 10 |
| `L-1-2018` | 28 | 5 | 2 | 19 | 0 | 0 | 2 |
| `L-100-2017` | 79 | 18 | 8 | 12 | 7 | 0 | 16 |
| `L-105-2003` | 75 | 21 | 6 | 76 | 8 | 0 | 26 |
| `L-106-2022` | 45 | 10 | 2 | 32 | 1 | 0 | 7 |
| `L-1125-2002` | 50 | 9 | 4 | 4 | 16 | 1 | 5 |
| `L-1134-1997` | 110 | 30 | 16 | 134 | 14 | 0 | 28 |
| `L-114-2012` | 131 | 24 | 12 | 267 | 13 | 0 | 15 |
| `L-122-2008` | 23 | 7 | 5 | 11 | 0 | 0 | 2 |
| `L-1260-2002` | 73 | 9 | 4 | 21 | 1 | 0 | 4 |
| `L-131-2012` | 41 | 11 | 13 | 27 | 3 | 4 | 6 |
| `L-131-2015` | 91 | 14 | 8 | 120 | 1 | 0 | 11 |
| `L-132-2016` | 45 | 13 | 6 | 27 | 7 | 0 | 5 |
| `L-133-2011` | 36 | 10 | 21 | 18 | 1 | 0 | 2 |
| `L-133-2016` | 27 | 8 | 12 | 28 | 5 | 0 | 3 |
| `L-133-2018` | 17 | 58 | 2 | 0 | 0 | 0 | 47 |
| `L-135-2007` | 93 | 11 | 4 | 17 | 12 | 0 | 6 |
| `L-139-2007` | 59 | 4 | 2 | 36 | 0 | 0 | 3 |
| `L-148-2023` | 35 | 6 | 7 | 25 | 2 | 0 | 4 |
| `L-149-2012` | 271 | 11 | 11 | 182 | 7 | 9 | 9 |
| `L-1543-1998` | 99 | 19 | 4 | 29 | 6 | 0 | 11 |
| `L-158-2008` | 88 | 51 | 13 | 74 | 7 | 0 | 62 |
| `L-160-2011` | 32 | 11 | 21 | 12 | 3 | 2 | 11 |
| `L-160-2023` | 58 | 13 | 3 | 47 | 5 | 0 | 8 |
| `L-160-2026` | 46 | 4 | 0 | 54 | 11 | 1 | 1 |
| `L-171-2012` | 156 | 31 | 23 | 153 | 17 | 0 | 24 |
| `L-177-2025` | 4 | 4 | 0 | 0 | 0 | 0 | 0 |
| `L-178-2020` | 8 | 7 | 0 | 0 | 0 | 0 | 2 |
| `L-181-2014` | 89 | 31 | 15 | 30 | 2 | 1 | 33 |
| `L-181-2023` | 50 | 19 | 3 | 13 | 21 | 0 | 12 |
| `L-183-2012` | 110 | 28 | 6 | 183 | 8 | 4 | 17 |
| `L-183-2016` | 17 | 6 | 7 | 8 | 3 | 0 | 1 |
| `L-192-1998` | 34 | 20 | 17 | 21 | 8 | 1 | 1 |
| `L-195-2024` | 90 | 20 | 1 | 200 | 8 | 0 | 6 |
| `L-198-2007` | 54 | 10 | 5 | 38 | 14 | 0 | 11 |
| `L-198-2020` | 64 | 10 | 2 | 23 | 8 | 0 | 3 |
| `L-2-2020` | 46 | 17 | 0 | 29 | 8 | 1 | 11 |
| `L-20-2026` | 29 | 18 | 1 | 16 | 14 | 0 | 15 |
| `L-202-2017` | 155 | 21 | 18 | 247 | 31 | 2 | 10 |
| `L-213-2023` | 10 | 6 | 9 | 5 | 2 | 1 | 3 |
| `L-220-2007` | 44 | 10 | 11 | 14 | 15 | 0 | 9 |
| `L-23-2008` | 36 | 4 | 0 | 6 | 0 | 0 | 3 |
| `L-232-2016` | 344 | 18 | 7 | 238 | 42 | 1 | 9 |
| `L-234-2016` | 37 | 14 | 10 | 30 | 6 | 0 | 7 |
| `L-235-2006` | 21 | 5 | 9 | 1 | 3 | 0 | 1 |
| `L-239-2008` | 20 | 5 | 5 | 0 | 0 | 0 | 1 |
| `L-24-2008` | 42 | 3 | 2 | 31 | 1 | 0 | 2 |
| `L-245-2008` | 41 | 5 | 12 | 9 | 0 | 0 | 2 |
| `L-246-2018` | 97 | 17 | 2 | 17 | 7 | 0 | 16 |
| `L-250-2017` | 23 | 6 | 1 | 14 | 0 | 0 | 4 |
| `L-284-2004` | 29 | 10 | 2 | 4 | 7 | 0 | 4 |
| `L-308-2017` | 47 | 21 | 8 | 65 | 12 | 0 | 18 |
| `L-325-2013` | 28 | 11 | 9 | 41 | 2 | 0 | 7 |
| `L-325-2025` | 91 | 21 | 0 | 168 | 1 | 0 | 20 |
| `L-436-2006` | 98 | 34 | 4 | 16 | 2 | 0 | 63 |
| `L-514-1995` | 60 | 12 | 0 | 4 | 0 | 0 | 8 |
| `L-548-1995` | 91 | 34 | 16 | 40 | 21 | 4 | 14 |
| `L-550-1995` | 20 | 9 | 8 | 18 | 16 | 1 | 2 |
| `L-62-2008` | 73 | 11 | 14 | 71 | 10 | 1 | 4 |
| `L-62-2022` | 58 | 25 | 7 | 37 | 4 | 0 | 25 |
| `L-64-2010` | 34 | 2 | 3 | 5 | 1 | 0 | 0 |
| `L-66-2017` | 17 | 17 | 1 | 0 | 0 | 0 | 12 |
| `L-845-1992` | 46 | 14 | 4 | 12 | 4 | 0 | 5 |
| `L-86-2014` | 42 | 17 | 5 | 67 | 0 | 5 | 21 |
| `L-9-2026` | 63 | 13 | 0 | 27 | 5 | 0 | 5 |
| `L-92-2022` | 125 | 17 | 5 | 61 | 6 | 0 | 7 |
| `UA-STATUT-2011` | 74 | 9 | 0 | 16 | 1 | 2 | 2 |

## Trimiteri nerezolvate

Articole citate care nu au ancora in actul-tinta, grupate pe tinta. Cauze cunoscute: articolul a fost abrogat si consolidarea a sters ciotul (`L-548-1995` art. 12, 13, 29, 30, 48, 54, 73; CLAUDE.md, intrebarea 6); articolul a fost abrogat si textul care il citeaza n-a fost actualizat; actul-tinta a fost renumerotat (Codul civil in 2019); ancora lipseste din cauza unei greseli de tipar in sursa (`L-100-2017` art. 52; intrebarea 4); exponentul a fost turtit in sursa (`art. 3142` pentru 314^2; intrebarea 2); sau citirea a luat drept articol al acestui act unul al altui act, nenumit in context. Fiecare rind trimite la o linie: deschide-o inainte de a trage o concluzie.

| act-tinta | articol citat | citari | poate fi | regula | exemplu (sursa, linie) | fragment |
|---|---|---:|---|---|---|---|
| `CC-1107-2002` | art. 48^30 | 7 | - | din | `COD-225-2003#art.308^2` l.2707 | de judecată audiază persoanele enumerate la art. 48^30 alin. (1) din Codul civil. (2) Audierea persoanelor indicate la art. |
| `COD-218-2008` | art. 441 | 5 | exponent turtit: art. 44^1 | din | `HG-582-2022#corp` l.94 | rocesul contravențional a încetat în temeiul art. 441 alin. (1) lit. f) din Codul contravențional al Republicii Moldova nr. |
| `AA-2014` | art. 3 | 4 | - | intern | `AA-2014#preambul` l.32 | ând cu data de 1 septembrie 2014, în temeiul articolului 3 alineatul (1) din Decizia Consiliului privind semnarea și aplicarea c |
| `L-131-2012` | art. 51 | 4 | exponent turtit: art. 5^1 | intern | `L-131-2012#art.29` l.560 | or încălcări, conform limitelor stabilite la art. 51. (1^1) În cazul prevăzut la art.28 alin.(9), organul respectiv includ |
| `AA-2014` | art. 7 | 3 | - | intern | `AA-2014#art.465` l.163 | italului inițial prevăzut în conformitate cu articolul 5 alineatele (1) și (3), articolul 6, articolul 7 literele (a), (b) și (c), articolul 8 literele (a), (b) și (c) și arti |
| `CC-1107-2002` | art. 330^4 | 3 | - | din | `COD-225-2003#art.327` l.2902 | rilor de constatare a uzucapiunii în temeiul art. 330^4 din Codul civil şi efectuării înregistrării corespunzătoare în regist |
| `CC-1107-2002` | art. 1575^9 | 3 | - | din | `L-149-2012#art.235^13` l.2437 | asei succesorale de către moștenitor conform art. 1575^9–1575^11 din Codul civil pot fi folosite pentru a satisface creanțele |
| `L-86-2014` | art. 105 | 3 | exponent turtit: art. 10^5 | intern | `L-86-2014#art.10^12` l.469 | entă a acordului de mediu în conformitate cu art. 105 alin. (5). (8) În cazul activităților planificate care nu cad sub inc |
| `AA-2014` | art. 4 | 2 | - | intern | `AA-2014#art.465` l.206 | sare pentru fiecare investitor, prevăzută la articolul 4 din respectiva directivă, sunt puse în aplicare în termen de cinci an |
| `CC-1107-2002` | art. 48^40 | 2 | - | din | `COD-225-2003#art.308^9` l.2738 | oire a măsurii de ocrotire judiciare conform art. 48^40 din Codul civil, instanţa de judecată va pronunţa hotărârea judecător |
| `CC-1107-2002` | art. 1575^4 | 2 | - | din | `L-149-2012#art.235^12` l.2433 | ța ce aparține creditorului care, în temeiul art. 1575^4 din Codul civil, a fost exclus din cadrul procedurii de somare public |
| `CC-1107-2002` | art. 1575^5 | 2 | - | din | `L-149-2012#art.235^12` l.2433 | publică a creditorilor sau care, în temeiul art. 1575^5 din Codul civil, se asimilează creditorului exclus va fi satisfăcută |
| `COD-218-2008` | art. 562 | 2 | exponent turtit: art. 56^2 | intern | `COD-218-2008#art.415` l.6587 | (1) Contravenţiile prevăzute la art. 562 , 563, 242, 366–369, art. 370 alin. (1), art. 371–373^3 se constată de Ministerul Apărării. (2) Sunt în drept să consta |
| `L-183-2012` | art. 572 | 2 | exponent turtit: art. 57^2 | intern | `L-183-2012#art.47` l.795 | lui Consiliului Concurenței emisă în temeiul art. 572 alin. (1) pot fi contestate, în conformitate cu prevederile Codului a |
| `UA-STATUT-2011` | art. 35^1 | 2 | - | intern | `UA-STATUT-2011#art.53^1` l.799 | anele care întrunesc condițiile prevăzute la art. 34 alin. (1) și art. 35^1 din Lege cu respectarea limitei numărului de mandate consecutive. Ver |
| `AA-2014` | art. 2 | 1 | - | intern | `AA-2014#art.465` l.157 | același mod ca și instituțiile enumerate la articolul 2 din respectiva directivă, și în consecință, vor fi exceptate de la do |
| `AA-2014` | art. 5 | 1 | - | intern | `AA-2014#art.465` l.163 | italului inițial prevăzut în conformitate cu articolul 5 alineatele (1) și (3), articolul 6, articolul 7 literele (a), (b) și (c), articolul 8 literele (a), (b) și (c) și arti |
| `AA-2014` | art. 6 | 1 | - | intern | `AA-2014#art.465` l.163 | italului inițial prevăzut în conformitate cu articolul 5 alineatele (1) și (3), articolul 6, articolul 7 literele (a), (b) și (c), articolul 8 literele (a), (b) și (c) și arti |
| `AA-2014` | art. 8 | 1 | - | intern | `AA-2014#art.465` l.163 | italului inițial prevăzut în conformitate cu articolul 5 alineatele (1) și (3), articolul 6, articolul 7 literele (a), (b) și (c), articolul 8 literele (a), (b) și (c) și arti |
| `AA-2014` | art. 9 | 1 | - | intern | `AA-2014#art.465` l.163 | italului inițial prevăzut în conformitate cu articolul 5 alineatele (1) și (3), articolul 6, articolul 7 literele (a), (b) și (c), articolul 8 literele (a), (b) și (c) și arti |
| `AA-2014` | art. 12 | 1 | - | intern | `AA-2014#preambul` l.57 | I: articolele 3,4, 7 și 8; (c) titlul III: articolele 12 și 15; (d) titlul IV: capitolele 5, 9 și 12 |
| `AA-2014` | art. 30 | 1 | - | intern | `AA-2014#preambul` l.61 | , capitolele 26 și 28, precum și articolele 30, 37, 46, 57, 97, 102 și 116; (e) titlul V (cu excepția articolului |
| `AA-2014` | art. 278 | 1 | - | intern | `AA-2014#preambul` l.65 | 97, 102 și 116; (e) titlul V (cu excepția articolului 278, în măsura în care se referă la aplicarea de sancțiuni penale în caz |
| `AA-2014` | art. 359 | 1 | - | intern | `AA-2014#preambul` l.65 | de proprietate intelectuală, și cu excepția articolelor 359 și 360, în măsura în care aceste dispoziții se aplică procedurilor ad |
| `CC-1107-2002` | art. 48^12 | 1 | - | din | `COD-225-2003#art.81` l.862 | l să le exercite, cu excepțiile stabilite la art. 48^12–48^27 din Codul civil și de mandatul de ocrotire în viitor. |
| `CC-1107-2002` | art. 48^21 | 1 | - | din | `COD-225-2003#art.308^17` l.2789 | că prin care se împuterniceşte, în aplicarea art. 48^21 şi 48^27 din Codul civil, mandatarul sau un mandatar special cu înche |
| `CC-1107-2002` | art. 48^28 | 1 | - | din | `COD-225-2003#art.307` l.2687 | ire; b) expunerea circumstanţelor, în sensul art. 48^28 din Codul civil, care impun instituirea măsurii de ocrotire judiciare |
| `CC-1107-2002` | art. 283^27 | 1 | - | din | `COD-225-2003#art.175^1` l.1561 | revăzut de lege (1) În cazurile prevăzute de art. 283^27 din Codul civil şi în alte cazuri prevăzute de lege, acţiunea este no |
| `CC-1107-2002` | art. 1572^117 | 1 | - | din | `L-149-2012#art.235^9` l.2414 | lile de îngrijire și de înmormântare conform art. 1572^117din Codul civil; c) cheltuielile din contul masei succesorale suportat |
| `CC-1107-2002` | art. 1575^10 | 1 | - | din | `L-149-2012#art.235^11` l.2427 | făcut din contul masei succesorale în sensul art. 1575^10 din Codului civil, moștenitorul poate înainta creanța care aparține c |
| `COD-116-2018` | art. 17^1 | 1 | - | din | `L-192-1998#art.23` l.376 | te. d) - abrogată; (1^2) Prin derogare de la art. 17^1 alin.(4) din Codul administrativ nr. 116/2018, depunerea unei cereri |
| `COD-116-2018` | art. 2451 | 1 | exponent turtit: art. 245^1 | intern | `COD-116-2018#art.247` l.1742 | epția recursului în care se invocă întemeiat art. 2451 alin. (1) lit. b) și d). Completul poate decide și în alte cazuri inv |
| `COD-1163-1997` | art. 29^1 | 1 | - | intern | `COD-1163-1997#art.292` l.6945 | art. 295 lit. g^1), achită taxa stipulată la art. 29^1 alin.(1) lit.e), anual, în termen de până la data de 25 martie a anul |
| `COD-122-2003` | art. 181^1 | 1 | - | intern | `COD-122-2003#art.269` l.3923 | în privința infracțiunilor prevăzute la: a) art. 181^1–181^3, 239–240, 243, art. 244 alin. (3)–(5) doar pentru faptele prevăzute la alin. (3) și (4), art. |
| `COD-122-2003` | art. 185^2 | 1 | - | intern | `COD-122-2003#art.276` l.4065 | tru săvârșirea unor infracţiuni prevăzute la art. 185^2, cu excepţia infracţiunilor prevăzute la alin. (2^3), şi la art. 185^ |
| `COD-218-2008` | art. 5^1 | 1 | - | intern | `COD-218-2008#art.440` l.7012 | zător se efectuează în limitele stabilite la art. 4 alin.(10) și art. 5^1din legea menționată. (5) Dacă la depistarea sau la examinarea cazului |
| `COD-218-2008` | art. 13^1 | 1 | - | modificare | `COD-434-2023#art.389` l.4138 | rile ulterioare, va avea următorul cuprins: „Articolul 13^1. Misiunile diplomatice pot procura sau obține prin schimb terenuri și |
| `COD-218-2008` | art. 52^2 | 1 | - | intern | `COD-218-2008#art.293^2` l.4879 | e plată și moneda electronică a prevederilor art. 50 alin. (1)–(5) și (7), art. 52^1 alin. (5), art. 52^2 alin. (1) și (2), art. 53 alin. (3), (4), (6) și (7), art. 55 alin. ( |
| `COD-218-2008` | art. 60^1 | 1 | - | intern | `COD-218-2008#art.293^2` l.4879 | e plată și moneda electronică a prevederilor art. 50 alin. (1)–(5) și (7), art. 52^1 alin. (5), art. 52^2 alin. (1) și (2), art. 53 alin. (3), (4), (6) și (7), art. 55 alin. ( |
| `COD-218-2008` | art. 641 | 1 | exponent turtit: art. 64^1 | intern | `COD-218-2008#art.409^2` l.6554 | (1) Contravențiile prevăzute la art.641, 642, 327^3 se constată de către Inspectoratul Social de Stat. (2) Su |
| `COD-225-2003` | art. 48^15 | 1 | - | intern | `COD-225-2003#art.308^17` l.2789 | u controlul executării mandatului, în sensul art. 48^15 alin. (3), şi de către persoanele ale căror drepturi sunt afectate pr |
| `COD-225-2003` | art. 581 | 1 | exponent turtit: art. 58^1 | din | `CC-1107-2002#art.113` l.952 | ori din oficiu. (3) În cazurile prevăzute la art. 581 din Codul de procedură civilă, curatorul special sau tutorele special |
| `L-105-2003` | art. 201 | 1 | - | din | `COD-218-2008#art.273` l.4540 | locului de preschimbare a mărfii prevăzut la art. 201 din Legea nr. 105/2003 privind protecția consumatorilor, lipsa inform |
| `L-1125-2002` | art. 1756 | 1 | - | intern | `L-1125-2002#art.45` l.268 | a) exceptarea prevăzută de art.1756 alin.(2) enunțul al doilea din Codul civil în redacția introdusă prin |
| `L-131-2012` | art. 191 | 1 | exponent turtit: art. 19^1 | din | `L-160-2011#art.11^1` l.380 | permisiv în modul și termenele stabilite la art. 191 din Legea nr. 131/2012 privind controlul de stat asupra activităţii d |
| `L-160-2011` | art. 62 | 1 | exponent turtit: art. 6^2 | intern | `L-160-2011#art.8` l.329 | fel de taxă. Prin derogare de la prevederile art. 62 alin. (2), duplicatul actului permisiv se consideră eliberat prin apr |
| `L-160-2026` | art. 72 | 1 | - | intern | `L-160-2026#art.40` l.465 | o privesc încalcă prezenta lege. Prevederile art. 72 și 73, precum și ale cap. VIII secțiunea a 2-a din Legea nr. 195/2024 |
| `L-171-2012` | art. 38 | 1 | in registrul in-force: abrogare de la 2027-06-01, textul lipseste din fisier | din | `L-2-2020#art.17` l.409 | nirii de către SAI a cerințelor stabilite în art. 38, 41 și 49 din Legea nr. 171/2012 privind piața de capital. (8) SAI ar |
| `L-171-2012` | art. 81 | 1 | - | din | `HCNPF-14-5-2016#corp` l.73 | nistru_________ Vladimir CEBOTARI În temeiul art.1 alin.(2)-(4), art.5, art. 34, art. 59 alin. (3), art. 81 alin. (2), art. 87 alin. (4), art.147 alin.(8) din Legea nr. 171 di |
| `L-171-2012` | art. 87 | 1 | - | din | `HCNPF-14-5-2016#corp` l.73 | nistru_________ Vladimir CEBOTARI În temeiul art.1 alin.(2)-(4), art.5, art. 34, art. 59 alin. (3), art. 81 alin. (2), art. 87 alin. (4), art.147 alin.(8) din Legea nr. 171 di |
| `L-171-2012` | art. 88 | 1 | - | din | `HCNPF-38-5-2015#corp` l.72 | alin.(3), art.71 alin.(6), art.78, art.88 alin.(5) art.140 alin.(15) lit.c), art.143 alin.(2) din Legea nr.171 din 11.07.2012 „Privind piaţa |
| `L-181-2014` | art. 49 | 1 | - | intern | `L-181-2014#art.82` l.1009 | ă în vigoare la 1 ianuarie 2015, cu excepţia art.10, art.15-17, art.18 lit.b) şi d), art.19 lit.d), f) şi g), art.20 alin.(1) lit.b), c) şi k), art.21 alin.(1) lit.j), art.24 |
| `L-183-2012` | art. 541 | 1 | exponent turtit: art. 54^1 | intern | `L-183-2012#art.68` l.1112 | or solicitate la interviul dispus în temeiul art. 541 ori se prezintă la interviu, dar refuză de a fi intervievate sau, în |
| `L-183-2012` | art. 571 | 1 | exponent turtit: art. 57^1 | intern | `L-183-2012#art.71` l.1160 | ine obligatoriu printr-o decizie, în temeiul art. 571; e) nu notifică o concentrare economică, definită la art. 22 alin. (1 |
| `L-202-2017` | art. 13^9 | 1 | - | din | `HBN-127-2013#corp` l.150 | nctul 2), Banca Naţională aplică prevederile art.13^9 şi/sau 14^1 din Legea nr.202 din 6 octombrie 2017 privind activitatea |
| `L-202-2017` | art. 75^2 | 1 | - | intern | `L-202-2017#art.142` l.1730 | plicabile, în mod corespunzător, prevederile art. 75^2 alin. (5) referitoare la încălcarea repetată, ale alin. (6) şi ale al |
| `L-202-2017` | art. 521 | 1 | exponent turtit: art. 52^1 | din | `L-232-2016#art.58` l.477 | cazul în care acțiunile emise în condițiile art. 521 din Legea nr. 202/2017 privind activitatea băncilor nu au fost vândut |
| `L-213-2023` | art. 84 | 1 | - | paranteza | `L-213-2023#preambul` l.56 | lovit art. 2 alin. (2) din prezenta lege (și art. 84 alin. (4) din `COD-225-2003`) — deja înregistrată în `_meta/hcc/hcc-r |
| `L-548-1995` | art. 112 | 1 | exponent turtit: art. 11^2 | intern | `L-548-1995#art.11` l.299 | emise de Banca Națională se notifică conform art. 112. (3^2) - abrogat. (3^3) În cadrul avizării și consultării publice a p |
| `L-548-1995` | art. 491 | 1 | exponent turtit: art. 49^1 | intern | `L-548-1995#art.75` l.982 | perceperea incontestabilă a amenzii conform art. 491 alin. (3) lit. f) în mărime de la 10 000 de lei la 600 000 de lei; d) |
| … inca 9 grupuri, in JSON | | | | | | |

„Poate fi” este o ipoteza mecanica, nu o muchie: numarul citat, despartit in baza si exponent, da o ancora existenta. Se verifica in sursa inainte de a fi folosita.

## Ce nu face acest graf

- Nu deduce. O muchie exista numai daca textul o contine, si poarta liniile din care vine.
- Nu coboara sub articol: `alin.`, `lit.`, `pct.` nu sint noduri.
- Nu citeste articolele actelor pe puncte (HG, regulamente BNM si CNPF, proceduri DCU), nici extrasele UE: pentru ele exista doar muchii la nivel de act.
- Nu citeste articolele **legilor de modificare cu articole romane** (`L-133-2018`, `L-177-2025`, `L-178-2020`): textul dintre articolele lor proprii este textul nou al actelor modificate, cu numerotarea ACELOR acte, iar regula `modificare` nu tine pasul cind un singur articol are mii de linii si mai multe tinte. Masurat 2026-09-18 pe `L-133-2018`: 514 din 837 de trimiteri atribuite gresit lui `COD-225-2003`. Muchiile act -> act raman.
- Citeste numai numerele scrise dupa `art.` sau `articolul`. Intr-un interval (`art. 5-7`) sau intr-o enumerare prescurtata (`art. 2-5, 7-21`) numerele care urmeaza fara `art.` nu sint citite.
- Un articol citat fara act in context este atribuit actului curent. Regulile de context sint cele de mai sus; o trimitere al carei act sta mai departe in fraza decit le vad ele, sau e numit prin `legea mentionata` fara o lege numita inainte, ramine atribuita actului curent.
- O lege citata pe nume este rezolvata la actul detinut al carui titlu contine numele, numai daca exact unul il contine.
- Notele de modificare intre paranteze drepte, rindurile blocului de istoric si referintele la Monitorul Oficial sint mascate inainte de citire.
- Nu citeste corpusul englez BNM (traduceri) si nici radacinile de politici.
- Nu stie daca un act citat si **nedetinut** mai este in vigoare. Pentru actele detinute stie, din 2026-09-10, fiindca ingestul scrie `repealed` in frontmatter.

