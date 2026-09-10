# Graful de citare al actelor detinute

Generat 2026-09-10 13:08 de `_meta/graph/build_citation_graph.py`. Nu edita de mina; se reface rulind scriptul. Datele: `citation-graph.json` in acelasi folder.

**Ce este.** Trimiterile dintre actele detinute, extrase mecanic din textul brut: fiecare muchie poarta fisierul si liniile din care a fost citita, si nicio muchie nu este dedusa. Graful nu se citeaza. El spune unde sa deschizi fisierul, iar ancora se citeste.

**Regula de folosire.** Inainte de a cita un articol, cauta-l in tabelul „Dispozitii cu stare speciala si cine le citeaza”: daca apare, fie el, fie o dispozitie de care depinde nu se aplica astazi asa cum sta in text. Inainte de a ingera un act, citeste „Coada de ingerare”: acolo sint actele pe care textele detinute le citeaza si vault-ul nu le are.

## Numere

| | |
|---|---:|
| acte primare detinute (din care ancorate pe articole) | 86 (67) |
| dispozitii (noduri-articol) | 11758 |
| extrase UE detinute (noduri-tinta) | 29 |
| acte citate si nedetinute (noduri externe) | 479 |
| mentiuni de acte in text (din care ale actului insusi) | 3460 (281) |
| muchii act -> act (agregate pe segment-sursa) | 2439 |
| trimiteri la articole citite (in grupuri de enumerare) | 8427 (7360) |
|   rezolvate in actul curent | 6891 |
|   rezolvate in alt act detinut | 1019 |
|   nerezolvate: articolul nu are ancora in actul-tinta | 76 |
|   catre acte nedetinute (notate pe muchia act -> act) | 390 |
|   catre acte pe puncte (fara articole) | 33 |
|   autoreferinte (articolul se citeaza pe sine), ignorate | 18 |
| muchii articol -> articol (agregate) | 6489 |
| muchii articol -> act nerezolvate (agregate) | 68 |

Regula care a dat actul-tinta, pe trimiteri: din 1183, doua-puncte 46, intern 6693, modificare 57, paranteza 7. „intern” = niciun act in context, deci actul curent; „din” = `art. N ... din Legea X` sau `(art. N, M) Directiva X`; „paranteza” = `Legea X (art. N)`; „doua-puncte” = `din Codul X: art. N, M`; „modificare” = `Legea X se modifica dupa cum urmeaza: ... articolul N`. `din legea indicata` trimite la ultima lege numita in acelasi segment.

Coduri citate si pe nume si pe numar, unite dupa textul care le scrie impreuna: COD-audiovizualului = COD-260-2006; COD-educatiei = COD-152-2014; COD-electoral = COD-325-2022; COD-familiei = COD-1316-2000; COD-jurisdictiei-constitutionale = COD-502-1995; COD-transporturilor-rutiere = COD-150-2014.

## Coada de ingerare

Actele pe care textele detinute le citeaza si care nu sint in vault, in ordinea numarului de mentiuni. Un act citat de multe acte detinute inchide mai multe lanturi de trimitere decit unul citat des dintr-un singur loc; coloana a treia este cea care conteaza pentru ordinea de ingerare. Graful nu stie daca un act citat mai este in vigoare: o lege abrogata ramine citata de textele care n-au fost actualizate, si apare aici la fel ca una in vigoare.

### Acte moldovenesti citate pe numar

Legi, coduri si hotariri de Guvern identificate prin numar si an.

| act citat | mentiuni | acte care il citeaza | cel mai des din | articole citate |
|---|---:|---:|---|---|
| `COD-325-2022` Codul nr. 325/2022 | 38 | 9 | `L-436-2006` (14) | art. 178 (x2), art. 1, art. 89, art. 90 |
| `L-183-2016` Legea nr. 183/2016 | 25 | 7 | `DCU-REGULI-2026` (9) | art. 3 (x3), art. 6 (x2), art. 8 |
| `L-133-2016` Legea nr. 133/2016 | 22 | 11 | `COD-218-2008` (9) | art. 13, art. 18 |
| `L-213-2023` Legea nr. 213/2023 | 22 | 8 | `COD-225-2003` (11) | - |
| `L-1125-2002` Legea nr. 1125/2002 | 22 | 2 | `CC-1107-2002` (19) | art. 26, art. 27 |
| `COD-150-2014` Codul nr. 150/2014 | 22 | 1 | `COD-218-2008` (22) | art. 94 (x2), art. 23, art. 43, art. 45 |
| `L-86-2014` Legea nr. 86/2014 | 20 | 5 | `COD-434-2023` (11) | art. 7 |
| `L-325-2013` Legea nr. 325/2013 | 18 | 8 | `L-158-2008` (4) | art. 7 (x11), art. 6 (x3), art. 12 |
| `L-139-2010` Legea nr. 139/2010 | 16 | 9 | `DCU-PROC-RECONCILIERE` (2) | - |
| `L-245-2008` Legea nr. 245/2008 | 15 | 10 | `L-325-2025` (3) | - |
| `L-199-2010` Legea nr. 199/2010 | 15 | 7 | `L-436-2006` (4) | art. 21 (x6), art. 22, art. 23 |
| `L-74-2020` Legea nr. 74/2020 | 14 | 3 | `L-325-2025` (8) | art. 6, art. 14, art. 19, art. 43 |
| `L-440-2001` Legea nr. 440/2001 | 13 | 5 | `COD-1163-1997` (6) | art. 5, art. 6, art. 13 |
| `L-181-2014` Legea nr. 181/2014 | 12 | 12 | `L-514-1995` (1) | art. 43 |
| `L-124-2022` Legea nr. 124/2022 | 12 | 7 | `L-220-2007` (3) | art. 3 |
| `L-407-2006` Legea nr. 407/2006 | 12 | 6 | `HCNPF-14-5-2016` (5) | art. 29 (x2), art. 1 |
| `L-184-2016` Legea nr. 184/2016 | 12 | 5 | `CC-1107-2002` (6) | art. 8 (x3), art. 4, art. 14 |
| `L-11-2017` Legea nr. 11/2017 | 11 | 3 | `COD-434-2023` (9) | art. 10 |
| `L-419-2006` Legea nr. 419/2006 | 10 | 7 | `DCU-REGULI-2026` (3) | art. 16, art. 42 |
| `L-488-1999` Legea nr. 488/1999 | 10 | 6 | `COD-22-2024` (4) | - |
| `L-287-2017` Legea nr. 287/2017 | 9 | 7 | `L-234-2016` (2) | art. 4 (x5), art. 24 |
| `L-384-2023` Legea nr. 384/2023 | 9 | 6 | `L-325-2025` (3) | - |
| `L-202-2013` Legea nr. 202/2013 | 9 | 5 | `COD-218-2008` (3) | art. 2, art. 3, art. 5, art. 10 |
| `L-271-2017` Legea nr. 271/2017 | 9 | 5 | `L-181-2023` (3) | art. 44 (x3), art. 2, art. 21, art. 45 |
| `L-231-2010` Legea nr. 231/2010 | 9 | 4 | `L-105-2003` (3) | art. 14, art. 19^1, art. 21, art. 21^15 |
| `L-575-2003` Legea nr. 575/2003 | 9 | 4 | `L-160-2023` (6) | art. 16 |
| `COD-1316-2000` Codul nr. 1316/2000 | 9 | 3 | `L-246-2018` (3) | art. 35, art. 36, art. 37, art. 39 |
| `L-443-1995` Legea nr. 443/1995 | 9 | 1 | `L-158-2008` (9) | art. 6, art. 8 |
| `L-768-2000` Legea nr. 768/2000 | 9 | 1 | `L-436-2006` (9) | art. 5 (x5) |
| `L-121-2007` Legea nr. 121/2007 | 8 | 6 | `HCNPF-14-5-2016` (3) | art. 6, art. 14, art. 53 |
| … inca 295 in JSON | | | | |

### Acte UE citate si neextrase

Directive si regulamente UE care nu au un extras `UE-*` in `raw/papers/cnpf/`.

| act citat | mentiuni | acte care il citeaza | cel mai des din | articole citate |
|---|---:|---:|---|---|
| `EU-L-2018-843` Directiva 2018/843 | 3 | 3 | `L-92-2022` (1) | - |
| `EU-TFUE` Tratatul privind functionarea Uniunii Europene | 3 | 3 | `L-183-2012` (1) | art. 101 |
| `EU-L-2014-23` Directiva 2014/23 | 3 | 2 | `L-20-2026` (2) | - |
| `EU-L-2014-24` Directiva 2014/24 | 3 | 2 | `L-131-2015` (2) | art. 1, art. 2, art. 22, art. 23 |
| `EU-R-2009-1060` Regulamentul (UE) nr. 1060/2009 | 3 | 2 | `L-171-2012` (2) | art. 2, art. 3, art. 4, art. 6 |
| `EU-R-2004-2006` Regulamentul (UE) nr. 2006/2004 | 3 | 1 | `L-105-2003` (3) | - |
| `EU-R-2013-952` Regulamentul (UE) nr. 952/2013 | 3 | 1 | `COD-95-2021` (3) | - |
| `EU-R-2017-2394` Regulamentul (UE) 2017/2394 | 3 | 1 | `L-105-2003` (3) | - |
| `EU-L-1989-665` Directiva 1989/665 | 2 | 2 | `L-20-2026` (1) | art. 1, art. 2 |
| `EU-L-1992-13` Directiva 1992/13 | 2 | 2 | `L-20-2026` (1) | art. 2 (x2), art. 1, art. 3 |
| `EU-L-1995-46` Directiva 1995/46 | 2 | 2 | `L-195-2024` (1) | - |
| `EU-L-2002-87` Directiva 2002/87 | 2 | 2 | `L-250-2017` (1) | art. 9 |
| `EU-L-2004-18` Directiva 2004/18 | 2 | 2 | `L-325-2025` (1) | - |
| `EU-L-2005-60` Directiva 2005/60 | 2 | 2 | `L-308-2017` (1) | - |
| `EU-L-2006-112` Directiva 2006/112 | 2 | 2 | `COD-95-2021` (1) | art. 143 (x2), art. 38, art. 59, art. 183 |
| `EU-L-2009-102` Directiva 2009/102 | 2 | 2 | `L-135-2007` (1) | art. 4 (x2), art. 2, art. 5 |
| `EU-L-2010-13` Directiva 2010/13 | 2 | 2 | `L-62-2022` (1) | - |
| `EU-L-2001-34` Directiva 2001/34 | 2 | 1 | `L-171-2012` (2) | - |
| `EU-L-2009-22` Directiva 2009/22 | 2 | 1 | `L-105-2003` (2) | - |
| `EU-L-2019-771` Directiva 2019/771 | 2 | 1 | `L-105-2003` (2) | - |
| … inca 69 in JSON | | | | |

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
| `LEGE:protectia-martorilor-si-altor` Legea cu privire la protecţia martorilor şi | 4 | 2 | `COD-122-2003` (3) | - |
| `LEGE:descentralizarea-administrativa` Legea privind descentralizarea administrativă | 4 | 1 | `L-436-2006` (4) | art. 4 (x3) |
| `LEGE:din` Legea din | 3 | 1 | `CONST-1994` (3) | - |
| `LEGE:locuinte` Legea cu privire la locuinţe | 3 | 1 | `L-436-2006` (3) | - |
| `LEGE:protectia-indicatiilor-geografice` Legea privind protecţia indicaţiilor geografice | 3 | 1 | `COD-218-2008` (3) | - |
| `LEGE:publicitate-si-cu` Legea cu privire la publicitate şi cu | 3 | 1 | `COD-174-2018` (3) | - |
| `LEGE:statutul-alesului-local` Legea privind statutul alesului local | 3 | 1 | `L-436-2006` (3) | - |
| `LEGE:gospodariile-taranesti` Legea privind gospodăriile ţărăneşti | 2 | 1 | `COD-154-2003` (2) | - |
| `LEGE:securitatii-si-sanatatii-in` Legea securităţii şi sănătăţii în muncă | 2 | 1 | `COD-154-2003` (2) | - |
| … inca 50 in JSON | | | | |

## Acquis: extrasele UE detinute si actele care le citeaza

Mentiunile actelor detinute catre cele 29 de extrase `UE-*`. Schita unei concordante: un act care citeaza o directiva o transpune, o aplica sau doar o numeste, si numai textul spune care.

| extras UE | mentiuni | citat din |
|---|---:|---|
| `UE-2004-109` | 0 | - |
| `UE-2004-25` | 0 | - |
| `UE-2007-36` | 1 | `L-1134-1997` (1) |
| `UE-2008-48` | 0 | - |
| `UE-2009-103` | 1 | `L-106-2022` (1) |
| `UE-2009-138` | 5 | `L-106-2022` (2), `L-92-2022` (2), `L-308-2017` (1) |
| `UE-2009-65` | 1 | `L-171-2012` (1) |
| `UE-2011-61` | 2 | `L-2-2020` (2) |
| `UE-2014-57` | 0 | - |
| `UE-2014-65` | 1 | `L-2-2020` (1) |
| `UE-2015-849` | 4 | `L-308-2017` (2), `L-106-2022` (1), `L-92-2022` (1) |
| `UE-2016-2341` | 1 | `L-198-2020` (1) |
| `UE-2016-97` | 0 | - |
| `UE-2017-1129` | 1 | `L-181-2023` (1) |
| `UE-2017-1132` | 2 | `L-1134-1997` (2) |
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
| `UE-97-9` | 0 | - |
| `UE-98-26` | 1 | `L-234-2016` (1) |

## Trimiteri catre acte abrogate

Acte detinute care nu mai sint in vigoare, si actele din corpus care trimit la ele. Fiecare trimitere de mai jos citeste astazi text mort. Nu inseamna ca actul care trimite e gresit: inseamna ca trimiterea trebuie citita prin dispozitiile tranzitorii ale actului abrogator, care de regula spune ca trimiterile la legea veche se considera facute la cea noua.

| act abrogat | de la | prin | mentiuni | acte care il citeaza | articole citate |
|---|---|---|---:|---:|---|
| `L-133-2011` | 2026-08-23 | LP195 din 25.07.24 | 44 | 19 | art. 2, art. 4, art. 5, art. 6, art. 12, art. 13, art. 20, art. 23 |

`L-133-2011` este citat din: `COD-122-2003`, `COD-218-2008`, `COD-95-2021`, `DCU-REGULI-2026`, `HCNPF-14-5-2016`, `L-105-2003`, `L-114-2012`, `L-122-2008`, `L-1543-1998`, `L-171-2012`, `L-181-2023`, `L-195-2024`, `L-202-2017`, `L-246-2018`, `L-284-2004`, `L-308-2017`, `L-325-2025`, `L-436-2006`, `L-548-1995`.

Limita care ramine: pentru actele **nedetinute** din coada de ingerare graful tot nu stie daca mai sint in vigoare. Se afla numai deschizind fisa lor pe legis.md, si nici acolo cimpul „Data abrogarii” nu este de incredere: pentru `L-133-2011` el era gol, desi corpul consolidarii declara abrogarea.

## Dispozitii cu stare speciala si cine le citeaza

Dispozitiile care apar in registrul in-force (textul din fisier nu se aplica inca), in registrul HCC (declarate neconstitutionale, in tot sau in parte) sau al caror titlu spune „abrogat”, si muchiile articol -> articol care intra in ele. Un articol din coloana „citat din” depinde de o dispozitie care nu sta in picioare asa cum e scrisa. Numai dispozitiile cu cel putin o citare intra aici, intii cele citate din alte acte; toate starile sint in JSON.

| dispozitie | stare | citari (din alte acte) | citat din |
|---|---|---:|---|
| `COD-985-2002#art.72` l.878 | in-force: modificare de la 2026-12-02 | 3 (3) | `COD-122-2003#art.469` l.5720, `COD-443-2004#art.197` l.2066, `COD-443-2004#art.255` l.2708 |
| `L-158-2008#art.27` l.481 | in-force: reformulare de la 2026-09-13 | 13 (2) | `L-158-2008#art.42`, `L-158-2008#art.45`, `L-158-2008#art.27^1`, `L-158-2008#art.29`, `L-158-2008#art.48`, `L-158-2008#art.62`, … (+5) |
| `COD-122-2003#art.191` l.3065 | in-force: modificare de la 2026-12-02; HCC: HCC17/2016-05-19, omisiune legislativa (+1) | 5 (2) | `COD-443-2004#art.301`, `COD-122-2003#art.192`, `COD-122-2003#art.309`, `COD-122-2003#art.310` |
| `COD-218-2008#art.34` l.1016 | HCC: HCC7/2018-04-26, alin. (3), text din articol | 3 (2) | `COD-443-2004#art.315` l.3262, `COD-218-2008#art.293^2` l.4868 |
| `COD-225-2003#art.449` l.3629 | HCC: HCC16/2013-06-25, lit. f), in parte | 12 (1) | `COD-225-2003#art.450`, `COD-116-2018#art.170`, `COD-225-2003#art.447`, `COD-225-2003#art.451`, `COD-225-2003#art.451^1`, `COD-225-2003#art.453` |
| `COD-225-2003#art.267` l.2164 | HCC: HCC33/2016-11-17, lit. b), in parte | 7 (1) | `COD-225-2003#art.268`, `COD-225-2003#art.185`, `COD-225-2003#art.49`, `COD-225-2003#art.89`, `COD-225-2003#art.98`, `COD-443-2004#art.163` |
| `COD-122-2003#art.179` l.2914 | in-force: modificare de la 2026-12-02 | 3 (1) | `COD-122-2003#art.181` l.2931, `COD-443-2004#art.297` l.3114 |
| `COD-122-2003#art.273` l.4004 | HCC: HCC29/2021-09-21, alin. (1) lit. d^2), in parte | 3 (1) | `COD-122-2003#art.166` l.2776, `COD-122-2003#art.215^2` l.3402, `COD-443-2004#art.245` l.2578 |
| `COD-122-2003#art.471` l.5746 | in-force: introducere de la 2026-12-02 | 3 (1) | `COD-122-2003#art.473` l.5810, `COD-122-2003#art.473^1` l.5816, `COD-443-2004#art.275` l.2914 |
| `COD-122-2003#art.186` l.2997 | HCC: HCC3/2016-02-23, alin. (3), (5), (8), (9), text din articol | 2 (1) | `COD-122-2003#art.195` l.3126, `COD-443-2004#art.198` l.2074 |
| `COD-122-2003#art.6` l.473 | in-force: introducere de la 2026-12-02 (pct.8^1); HCC: HCC2/2020-01-23, pct. 11^1), text din articol | 1 (1) | `COD-443-2004#art.98^1` l.1162 |
| `COD-218-2008#art.423^4` l.6654 | abrogat | 1 (1) | `L-195-2024#art.90` l.1164 |
| `COD-218-2008#art.427` l.6731 | HCC: HCC26/2024-12-12, alin.(2), text din articol | 1 (1) | `COD-95-2021#art.408` l.4420 |
| `COD-218-2008#art.74^1` l.1696 | abrogat | 1 (1) | `L-195-2024#art.90` l.1164 |
| `COD-985-2002#art.189` l.2580 | HCC: HCC24/2019-10-17, alin. (3) lit. f), text din articol | 1 (1) | `COD-122-2003#art.229^2` l.3545 |
| `L-131-2015#art.80` l.1484 | abrogat | 1 (1) | `L-20-2026#art.29` l.415 |
| `L-131-2015#art.86` l.1497 | abrogat | 1 (1) | `L-20-2026#art.29` l.419 |
| `L-158-2008#art.25` l.445 | in-force: reformulare de la 2026-09-13 | 1 (1) | `COD-1163-1997#art.148` l.4774 |
| `L-845-1992#art.36` l.565 | abrogat | 1 (1) | `COD-1163-1997#art.227^1` l.5963 |
| `L-158-2008#art.8` l.239 | in-force: modificare de la 2026-09-13 | 14 (0) | `L-158-2008#art.29`, `L-158-2008#art.35`, `L-158-2008#art.50`, `L-158-2008#art.59`, `L-158-2008#art.10`, `L-158-2008#art.14`, … (+2) |
| `COD-1163-1997#art.88` l.2970 | HCC: HCC7/2014-02-13, alin. (7), subunitate | 9 (0) | `COD-1163-1997#art.92`, `COD-1163-1997#art.372`, `COD-1163-1997#art.69^7`, `COD-1163-1997#art.73`, `COD-1163-1997#art.76`, `COD-1163-1997#art.79`, … (+2) |
| `COD-1163-1997#art.291` l.6906 | HCC: HCC2/2014-01-28, in parte | 8 (0) | `COD-1163-1997#art.293` l.6941, `COD-1163-1997#art.292` l.6935 |
| `COD-1163-1997#art.289` l.6857 | HCC: HCC2/2014-01-28, in parte | 6 (0) | `COD-1163-1997#art.297` l.7010, `COD-1163-1997#art.298` l.7019, `COD-1163-1997#art.294` l.6953 |
| `COD-122-2003#art.401` l.5218 | HCC: HCC9/2008-05-20, alin. (1) pct. 3), text din articol | 6 (0) | `COD-122-2003#art.402`, `COD-122-2003#art.420`, `COD-122-2003#art.421`, `COD-122-2003#art.438`, `COD-122-2003#art.445`, `COD-122-2003#art.447` |
| `COD-443-2004#art.174^1` l.1855 | in-force: introducere de la 2026-12-02 | 6 (0) | `COD-443-2004#art.196`, `COD-443-2004#art.204`, `COD-443-2004#art.263`, `COD-443-2004#art.269`, `COD-443-2004#art.271`, `COD-443-2004#art.290` |
| `L-158-2008#art.42` l.753 | in-force: modificare de la 2026-09-13 | 5 (0) | `L-158-2008#art.48`, `L-158-2008#art.49`, `L-158-2008#art.62`, `L-158-2008#art.69`, `L-158-2008#art.69^1` |
| `COD-122-2003#art.308` l.4399 | in-force: modificare de la 2026-12-02 | 4 (0) | `COD-122-2003#art.312` l.4458, `COD-122-2003#art.166` l.2780, `COD-122-2003#art.523` l.6326 |
| `COD-122-2003#art.385` l.5042 | in-force: introducere de la 2026-12-02 | 4 (0) | `COD-122-2003#art.382`, `COD-122-2003#art.392`, `COD-122-2003#art.485`, `COD-122-2003#art.498` |
| `COD-122-2003#art.42` l.831 | HCC: HCC3/2012-02-09, alin. (7), in parte | 4 (0) | `COD-122-2003#art.256`, `COD-122-2003#art.279^1`, `COD-122-2003#art.43`, `COD-122-2003#art.561` |
| `COD-122-2003#art.421` l.5369 | HCC: HCC16/2005-07-19, text din articol | 4 (0) | `COD-122-2003#art.423`, `COD-122-2003#art.429`, `COD-122-2003#art.432`, `COD-122-2003#art.433` |
| `COD-225-2003#art.170` l.1494 | HCC: HCC33/2016-11-17, alin. (1) lit. c), in parte | 4 (0) | `COD-225-2003#art.478`, `COD-225-2003#art.483`, `COD-225-2003#art.49`, `COD-225-2003#art.89` |
| `COD-225-2003#art.437` l.3537 | HCC: HCC20/2022-11-03, alin. (1), text din articol | 4 (0) | `COD-225-2003#art.426^1`, `COD-225-2003#art.436`, `COD-225-2003#art.438`, `COD-225-2003#art.439` |
| `COD-1163-1997#art.264` l.6317 | HCC: HCC10/2024-04-04, alin. (1) si (2), text din articol | 3 (0) | `COD-1163-1997#art.214` l.5478, `COD-1163-1997#art.226^2` l.5632, `COD-1163-1997#art.265` l.6328 |
| `COD-1163-1997#art.6` l.1545 | HCC: HCC5/2024-03-05, alin. (11), subunitate | 3 (0) | `COD-1163-1997#art.226^1` l.5620, `COD-1163-1997#art.5` l.1517, `COD-1163-1997#art.7` l.1612 |
| `COD-122-2003#art.321` l.4544 | in-force: modificare de la 2026-12-02; HCC: HCC3/2023-01-24, alin. (2) pct. 3), text din articol | 3 (0) | `COD-122-2003#art.199` l.3170, `COD-122-2003#art.412` l.5286, `COD-122-2003#art.559` l.6834 |
| `COD-174-2018#art.28` l.605 | HCC: HCC6/2022-03-10, al.(1), text din articol | 3 (0) | `COD-174-2018#art.25` l.555, `COD-174-2018#art.84` l.1536, `COD-174-2018#art.88` l.1600 |
| `COD-1163-1997#art.260` l.6249 | HCC: HCC20/2018-07-04, alin. (4), text din articol | 2 (0) | `COD-1163-1997#art.229` l.5987, `COD-1163-1997#art.234` l.6035 |
| `COD-122-2003#art.177` l.2881 | in-force: introducere de la 2026-12-02 | 2 (0) | `COD-122-2003#art.241^1` l.3658, `COD-122-2003#art.471` l.5761 |
| `COD-122-2003#art.287^1` l.4172 | in-force: modificare de la 2026-12-02 | 2 (0) | `COD-122-2003#art.287^2` l.4187 |
| `L-158-2008#art.38` l.708 | in-force: reformulare de la 2026-09-13 | 2 (0) | `L-158-2008#art.38^1` l.720, `L-158-2008#art.41` l.747 |
| `L-845-1992#art.36^1` l.571 | in-force: introducere de la 2027-01-01 (pct.4, lit.l)) | 2 (0) | `L-845-1992#art.36^3` l.599 |
| `COD-1163-1997#art.123` l.3742 | HCC: HCC17/2014-05-29, alin. (7), subunitate | 1 (0) | `COD-1163-1997#art.262` l.6292 |
| `COD-1163-1997#art.290` l.6884 | HCC: HCC2/2014-01-28, in parte | 1 (0) | `COD-1163-1997#art.297` l.7010 |
| `COD-122-2003#art.138^1` l.2374 | in-force: modificare de la 2026-12-02 | 1 (0) | `COD-122-2003#art.138^5` l.2421 |
| `COD-122-2003#art.178` l.2904 | in-force: modificare de la 2026-12-02; HCC: HCC19/2018-07-03, omisiune legislativa | 1 (0) | `COD-122-2003#art.547` l.6692 |
| `COD-122-2003#art.180` l.2921 | in-force: modificare de la 2026-12-02 | 1 (0) | `COD-122-2003#art.181` l.2931 |
| `COD-122-2003#art.185` l.2985 | HCC: HCC27/2018-10-30, al.(1), subunitate | 1 (0) | `COD-122-2003#art.188` l.3041 |
| `COD-122-2003#art.192` l.3086 | HCC: HCC15/2020-05-28, alin. (2), subunitate | 1 (0) | `COD-122-2003#art.192^1` l.3100 |
| `COD-122-2003#art.287` l.4164 | HCC: HCC12/2015-05-14, alin. (1), subunitate | 1 (0) | `COD-122-2003#art.326` l.4592 |
| `COD-122-2003#art.400` l.5213 | HCC: HCC3/2012-02-09, alin. (3), in parte | 1 (0) | `COD-122-2003#art.465^8` l.5668 |
| `COD-122-2003#art.74` l.1499 | in-force: modificare de la 2026-12-02 | 1 (0) | `COD-122-2003#art.223` l.3475 |
| `COD-154-2003#art.46` l.790 | in-force: introducere de la 2027-01-01 | 1 (0) | `COD-154-2003#art.391` l.3685 |
| `COD-154-2003#art.90` l.1293 | HCC: HCC9/2025-07-22, al.(2), lit. a), text din articol | 1 (0) | `COD-154-2003#art.330` l.3252 |
| `COD-218-2008#art.197^1` l.3385 | abrogat | 1 (0) | `COD-218-2008#art.431` l.6777 |
| `COD-218-2008#art.20` l.909 | abrogat | 1 (0) | `COD-218-2008#art.440^1` l.7016 |
| `COD-218-2008#art.233` l.3957 | HCC: HCC11/2018-05-08, alin. (3), text din articol | 1 (0) | `COD-218-2008#art.41` l.1100 |
| `COD-218-2008#art.313^2` l.5168 | in-force: reformulare de la 2026-09-13 | 1 (0) | `COD-218-2008#art.423^9` l.6685 |
| `COD-218-2008#art.313^4` l.5188 | in-force: reformulare de la 2026-09-13 | 1 (0) | `COD-218-2008#art.401` l.6463 |
| `COD-218-2008#art.445` l.7079 | HCC: HCC32/2018-11-29, articol intreg | 1 (0) | `COD-218-2008#art.451^3` l.7199 |
| `COD-218-2008#art.62` l.1486 | abrogat | 1 (0) | `COD-218-2008#art.293^2` l.4870 |
| `COD-225-2003#art.306` l.2668 | HCC: HCC33/2016-11-17, alin. (2), text din articol | 1 (0) | `COD-225-2003#art.77` l.826 |
| `COD-225-2003#art.39` l.518 | HCC: HCC3/2012-02-09, alin. (11^1), subunitate | 1 (0) | `COD-225-2003#art.41^1` l.560 |
| `COD-225-2003#art.58` l.687 | HCC: HCC33/2016-11-17, alin. (2), (2^1), (6), text din articol | 1 (0) | `COD-225-2003#art.79` l.832 |
| `COD-443-2004#art.174` l.1846 | HCC: HCC18/2013-07-04, alin. (3^1), subunitate | 1 (0) | `COD-443-2004#art.287` l.3000 |
| `COD-443-2004#art.263` l.2792 | in-force: modificare de la 2026-12-02 | 1 (0) | `COD-443-2004#art.194` l.2043 |
| `COD-95-2021#art.277^2` l.3004 | abrogat | 1 (0) | `COD-95-2021#art.277` l.2991 |
| `COD-985-2002#art.317` l.4791 | in-force: modificare de la 2026-12-02 | 1 (0) | `COD-985-2002#art.21` l.532 |
| `COD-985-2002#art.328` l.4968 | HCC: HCC22/2017-06-27, alin. (1), text din articol (+1) | 1 (0) | `COD-985-2002#art.55` l.732 |
| `COD-985-2002#art.329` l.4984 | HCC: HCC24/2019-10-17, alin. (1) si alin. (2) lit. b), text din articol | 1 (0) | `COD-985-2002#art.134^20` l.1573 |
| `COD-985-2002#art.335` l.5079 | HCC: HCC24/2019-10-17, alin. (1^1), text din articol (+1) | 1 (0) | `COD-985-2002#art.55` l.732 |
| `L-1543-1998#art.15^8` l.539 | in-force: introducere de la 2027-01-01 | 1 (0) | `L-1543-1998#art.15^4` l.498 |
| `L-158-2008#art.32` l.581 | in-force: modificare de la 2026-09-13 | 1 (0) | `L-158-2008#art.64` l.1097 |

Stari atasate dispozitiilor, in total: 69 in-force, 72 HCC, 264 abrogat. 72 dintre ele au cel putin o citare intrata, 19 din alte acte.

Acte care poarta hotariri HCC fara articol atribuit (orice citare din ele poate lovi textul anulat): `COD-116-2018` (1), `COD-154-2003` (2), `COD-174-2018` (1), `COD-443-2004` (5), `CONST-1994` (2), `L-1260-2002` (1), `L-135-2007` (1), `L-149-2012` (2), `L-158-2008` (1), `L-514-1995` (3), `L-548-1995` (2), `L-64-2010` (1), `L-845-1992` (3).

## Actele: ce citeaza si de cine sint citate

Pe act: tintele distincte ale mentiunilor (detinute + externe), actele detinute distincte care il mentioneaza, trimiterile la articole rezolvate in propriul text, rezolvate in alt act detinut, si nerezolvate (articolul citat nu are ancora in actul-tinta: abrogat cu ciotul sters, renumerotat, exponent turtit in sursa, sau o greseala de citire).

| act | ancore | citeaza (acte) | citat de (acte) | art. interne | art. in alte acte | nerezolvate | mentiuni externe |
|---|---:|---:|---:|---:|---:|---:|---:|
| `CC-1107-2002` | 2657 | 27 | 29 | 1017 | 5 | 1 | 45 |
| `COD-116-2018` | 260 | 13 | 27 | 106 | 10 | 1 | 7 |
| `COD-1163-1997` | 511 | 66 | 20 | 447 | 17 | 1 | 81 |
| `COD-122-2003` | 658 | 27 | 11 | 471 | 219 | 2 | 30 |
| `COD-154-2003` | 416 | 26 | 11 | 198 | 0 | 0 | 30 |
| `COD-174-2018` | 98 | 18 | 4 | 71 | 4 | 0 | 21 |
| `COD-218-2008` | 737 | 57 | 30 | 508 | 49 | 10 | 93 |
| `COD-22-2024` | 96 | 26 | 4 | 18 | 5 | 0 | 28 |
| `COD-225-2003` | 540 | 23 | 14 | 213 | 29 | 17 | 30 |
| `COD-434-2023` | 390 | 44 | 7 | 137 | 17 | 1 | 75 |
| `COD-443-2004` | 361 | 30 | 17 | 129 | 75 | 0 | 24 |
| `COD-95-2021` | 472 | 37 | 3 | 430 | 8 | 0 | 31 |
| `COD-985-2002` | 566 | 22 | 21 | 166 | 3 | 1 | 14 |
| `CONST-1994` | 157 | 4 | 28 | 13 | 1 | 0 | 5 |
| `DCA-61-2024` | 0 | 5 | 0 | 0 | 5 | 0 | 4 |
| `DCU-PROC-COMISIOANE` | 0 | 2 | 0 | 0 | 1 | 0 | 2 |
| `DCU-PROC-DETINATOR` | 0 | 1 | 0 | 0 | 0 | 0 | 2 |
| `DCU-PROC-GARANTII` | 0 | 1 | 0 | 0 | 0 | 0 | 2 |
| `DCU-PROC-INREGISTRARE-VM` | 0 | 4 | 0 | 0 | 3 | 0 | 1 |
| `DCU-PROC-INSOLVABILITATE` | 0 | 4 | 0 | 0 | 1 | 0 | 4 |
| `DCU-PROC-PARTICIPANT` | 0 | 1 | 0 | 0 | 0 | 0 | 2 |
| `DCU-PROC-RECLAMATII` | 0 | 1 | 0 | 0 | 0 | 0 | 2 |
| `DCU-PROC-RECONCILIERE` | 0 | 2 | 0 | 0 | 0 | 0 | 2 |
| `DCU-REGULI-2026` | 94 | 11 | 0 | 0 | 17 | 0 | 16 |
| `HBN-127-2013` | 0 | 7 | 0 | 0 | 41 | 1 | 3 |
| `HBN-130-2013` | 0 | 3 | 0 | 0 | 6 | 1 | 0 |
| `HCNPF-14-5-2016` | 0 | 12 | 0 | 0 | 29 | 2 | 14 |
| `HCNPF-38-5-2015` | 0 | 9 | 0 | 0 | 16 | 1 | 4 |
| `HG-1170-2016` | 0 | 16 | 1 | 0 | 5 | 0 | 21 |
| `HG-1171-2018` | 0 | 3 | 0 | 0 | 2 | 0 | 2 |
| `HG-553-2024` | 0 | 3 | 0 | 0 | 13 | 0 | 0 |
| `HG-574-2024` | 0 | 5 | 1 | 0 | 2 | 0 | 3 |
| `HG-582-2022` | 0 | 5 | 0 | 0 | 16 | 2 | 0 |
| `HG-743-2024` | 0 | 11 | 0 | 0 | 19 | 0 | 11 |
| `L-1-2018` | 28 | 5 | 2 | 19 | 0 | 0 | 2 |
| `L-100-2017` | 79 | 18 | 6 | 12 | 7 | 0 | 17 |
| `L-105-2003` | 75 | 21 | 5 | 76 | 8 | 0 | 26 |
| `L-106-2022` | 45 | 10 | 2 | 32 | 1 | 0 | 7 |
| `L-1134-1997` | 110 | 30 | 16 | 134 | 14 | 0 | 28 |
| `L-114-2012` | 131 | 24 | 11 | 267 | 13 | 0 | 17 |
| `L-122-2008` | 23 | 7 | 5 | 11 | 0 | 0 | 2 |
| `L-1260-2002` | 73 | 9 | 3 | 21 | 1 | 0 | 5 |
| `L-131-2012` | 41 | 11 | 13 | 27 | 3 | 4 | 7 |
| `L-131-2015` | 91 | 14 | 8 | 120 | 1 | 0 | 13 |
| `L-133-2011` | 36 | 10 | 19 | 18 | 0 | 0 | 4 |
| `L-135-2007` | 93 | 11 | 3 | 17 | 12 | 0 | 6 |
| `L-139-2007` | 59 | 4 | 2 | 36 | 0 | 0 | 3 |
| `L-148-2023` | 35 | 6 | 7 | 25 | 2 | 0 | 4 |
| `L-149-2012` | 271 | 11 | 9 | 182 | 6 | 9 | 10 |
| `L-1543-1998` | 99 | 19 | 3 | 29 | 4 | 0 | 14 |
| `L-158-2008` | 88 | 51 | 12 | 74 | 2 | 0 | 69 |
| `L-160-2011` | 32 | 11 | 18 | 12 | 3 | 2 | 13 |
| `L-160-2023` | 58 | 13 | 3 | 47 | 5 | 0 | 11 |
| `L-160-2026` | 46 | 4 | 0 | 54 | 11 | 1 | 2 |
| `L-171-2012` | 156 | 31 | 21 | 153 | 17 | 0 | 24 |
| `L-177-2025` | 4 | 4 | 0 | 0 | 10 | 2 | 0 |
| `L-178-2020` | 8 | 7 | 0 | 0 | 14 | 0 | 2 |
| `L-181-2023` | 50 | 19 | 3 | 13 | 21 | 0 | 12 |
| `L-183-2012` | 110 | 28 | 6 | 183 | 5 | 4 | 23 |
| `L-192-1998` | 34 | 20 | 16 | 21 | 6 | 1 | 4 |
| `L-195-2024` | 90 | 20 | 1 | 200 | 6 | 0 | 10 |
| `L-198-2007` | 54 | 10 | 4 | 38 | 14 | 0 | 11 |
| `L-198-2020` | 64 | 10 | 2 | 23 | 8 | 0 | 3 |
| `L-2-2020` | 46 | 17 | 0 | 29 | 8 | 1 | 11 |
| `L-20-2026` | 29 | 18 | 1 | 16 | 13 | 0 | 19 |
| `L-202-2017` | 155 | 21 | 17 | 247 | 31 | 2 | 10 |
| `L-220-2007` | 44 | 10 | 9 | 14 | 15 | 0 | 9 |
| `L-232-2016` | 344 | 18 | 7 | 238 | 41 | 1 | 15 |
| `L-234-2016` | 37 | 14 | 9 | 30 | 6 | 0 | 9 |
| `L-235-2006` | 21 | 5 | 9 | 1 | 3 | 0 | 2 |
| `L-239-2008` | 20 | 5 | 5 | 0 | 0 | 0 | 5 |
| `L-246-2018` | 97 | 17 | 2 | 17 | 7 | 0 | 16 |
| `L-250-2017` | 23 | 6 | 1 | 14 | 0 | 0 | 4 |
| `L-284-2004` | 29 | 10 | 2 | 4 | 7 | 0 | 4 |
| `L-308-2017` | 47 | 21 | 7 | 65 | 12 | 0 | 19 |
| `L-325-2025` | 91 | 21 | 0 | 168 | 1 | 0 | 24 |
| `L-436-2006` | 98 | 35 | 4 | 16 | 2 | 0 | 65 |
| `L-514-1995` | 60 | 12 | 0 | 4 | 0 | 0 | 9 |
| `L-548-1995` | 91 | 34 | 15 | 40 | 19 | 4 | 17 |
| `L-550-1995` | 20 | 9 | 8 | 18 | 16 | 1 | 5 |
| `L-62-2008` | 73 | 11 | 13 | 71 | 10 | 1 | 4 |
| `L-62-2022` | 58 | 25 | 7 | 37 | 4 | 0 | 25 |
| `L-64-2010` | 34 | 2 | 3 | 5 | 1 | 0 | 1 |
| `L-845-1992` | 46 | 14 | 3 | 12 | 4 | 0 | 5 |
| `L-92-2022` | 125 | 17 | 5 | 61 | 6 | 0 | 7 |
| `UA-STATUT-2011` | 74 | 9 | 0 | 16 | 1 | 2 | 3 |

## Trimiteri nerezolvate

Articole citate care nu au ancora in actul-tinta, grupate pe tinta. Cauze cunoscute: articolul a fost abrogat si consolidarea a sters ciotul (`L-548-1995` art. 12, 13, 29, 30, 48, 54, 73; CLAUDE.md, intrebarea 6); articolul a fost abrogat si textul care il citeaza n-a fost actualizat; actul-tinta a fost renumerotat (Codul civil in 2019); ancora lipseste din cauza unei greseli de tipar in sursa (`L-100-2017` art. 52; intrebarea 4); exponentul a fost turtit in sursa (`art. 3142` pentru 314^2; intrebarea 2); sau citirea a luat drept articol al acestui act unul al altui act, nenumit in context. Fiecare rind trimite la o linie: deschide-o inainte de a trage o concluzie.

| act-tinta | articol citat | citari | poate fi | regula | exemplu (sursa, linie) | fragment |
|---|---|---:|---|---|---|---|
| `CC-1107-2002` | art. 48^30 | 7 | - | din | `COD-225-2003#art.308^2` l.2698 | de judecată audiază persoanele enumerate la art. 48^30 alin. (1) din Codul civil. (2) Audierea persoanelor indicate la art. |
| `COD-218-2008` | art. 441 | 5 | exponent turtit: art. 44^1 | din | `HG-582-2022#corp` l.94 | rocesul contravențional a încetat în temeiul art. 441 alin. (1) lit. f) din Codul contravențional al Republicii Moldova nr. |
| `L-131-2012` | art. 51 | 4 | exponent turtit: art. 5^1 | intern | `L-131-2012#art.29` l.551 | or încălcări, conform limitelor stabilite la art. 51. (1^1) În cazul prevăzut la art.28 alin.(9), organul respectiv includ |
| `CC-1107-2002` | art. 330^4 | 3 | - | din | `COD-225-2003#art.327` l.2893 | rilor de constatare a uzucapiunii în temeiul art. 330^4 din Codul civil şi efectuării înregistrării corespunzătoare în regist |
| `CC-1107-2002` | art. 1575^9 | 3 | - | din | `L-149-2012#art.235^13` l.2428 | asei succesorale de către moștenitor conform art. 1575^9–1575^11 din Codul civil pot fi folosite pentru a satisface creanțele |
| `CC-1107-2002` | art. 48^40 | 2 | - | din | `COD-225-2003#art.308^9` l.2729 | oire a măsurii de ocrotire judiciare conform art. 48^40 din Codul civil, instanţa de judecată va pronunţa hotărârea judecător |
| `CC-1107-2002` | art. 1575^4 | 2 | - | din | `L-149-2012#art.235^12` l.2424 | ța ce aparține creditorului care, în temeiul art. 1575^4 din Codul civil, a fost exclus din cadrul procedurii de somare public |
| `CC-1107-2002` | art. 1575^5 | 2 | - | din | `L-149-2012#art.235^12` l.2424 | publică a creditorilor sau care, în temeiul art. 1575^5 din Codul civil, se asimilează creditorului exclus va fi satisfăcută |
| `COD-218-2008` | art. 562 | 2 | exponent turtit: art. 56^2 | intern | `COD-218-2008#art.415` l.6578 | (1) Contravenţiile prevăzute la art. 562 , 563, 242, 366–369, art. 370 alin. (1), art. 371–373^3 se constată de Ministerul Apărării. (2) Sunt în drept să consta |
| `COD-985-2002` | art. 24513 | 2 | exponent turtit: art. 245^13 | modificare | `L-177-2025#art.II` l.107 | u modificările ulterioare, se completează cu articolul 24513 cu următorul cuprins: „Articolul 24513. Marketingul, vânzarea sau dis |
| `L-183-2012` | art. 572 | 2 | exponent turtit: art. 57^2 | intern | `L-183-2012#art.47` l.786 | lui Consiliului Concurenței emisă în temeiul art. 572 alin. (1) pot fi contestate, în conformitate cu prevederile Codului a |
| `UA-STATUT-2011` | art. 35^1 | 2 | - | intern | `UA-STATUT-2011#art.53^1` l.790 | anele care întrunesc condițiile prevăzute la art. 34 alin. (1) și art. 35^1 din Lege cu respectarea limitei numărului de mandate consecutive. Ver |
| `CC-1107-2002` | art. 48^12 | 1 | - | din | `COD-225-2003#art.81` l.853 | l să le exercite, cu excepțiile stabilite la art. 48^12–48^27 din Codul civil și de mandatul de ocrotire în viitor. |
| `CC-1107-2002` | art. 48^21 | 1 | - | din | `COD-225-2003#art.308^17` l.2780 | că prin care se împuterniceşte, în aplicarea art. 48^21 şi 48^27 din Codul civil, mandatarul sau un mandatar special cu înche |
| `CC-1107-2002` | art. 48^28 | 1 | - | din | `COD-225-2003#art.307` l.2678 | ire; b) expunerea circumstanţelor, în sensul art. 48^28 din Codul civil, care impun instituirea măsurii de ocrotire judiciare |
| `CC-1107-2002` | art. 283^27 | 1 | - | din | `COD-225-2003#art.175^1` l.1552 | revăzut de lege (1) În cazurile prevăzute de art. 283^27 din Codul civil şi în alte cazuri prevăzute de lege, acţiunea este no |
| `CC-1107-2002` | art. 1572^117 | 1 | - | din | `L-149-2012#art.235^9` l.2405 | lile de îngrijire și de înmormântare conform art. 1572^117din Codul civil; c) cheltuielile din contul masei succesorale suportat |
| `CC-1107-2002` | art. 1575^10 | 1 | - | din | `L-149-2012#art.235^11` l.2418 | făcut din contul masei succesorale în sensul art. 1575^10 din Codului civil, moștenitorul poate înainta creanța care aparține c |
| `COD-116-2018` | art. 17^1 | 1 | - | din | `L-192-1998#art.23` l.376 | te. d) - abrogată; (1^2) Prin derogare de la art. 17^1 alin.(4) din Codul administrativ nr. 116/2018, depunerea unei cereri |
| `COD-116-2018` | art. 2451 | 1 | exponent turtit: art. 245^1 | intern | `COD-116-2018#art.247` l.1733 | epția recursului în care se invocă întemeiat art. 2451 alin. (1) lit. b) și d). Completul poate decide și în alte cazuri inv |
| `COD-1163-1997` | art. 29^1 | 1 | - | intern | `COD-1163-1997#art.292` l.6936 | art. 295 lit. g^1), achită taxa stipulată la art. 29^1 alin.(1) lit.e), anual, în termen de până la data de 25 martie a anul |
| `COD-122-2003` | art. 181^1 | 1 | - | intern | `COD-122-2003#art.269` l.3914 | în privința infracțiunilor prevăzute la: a) art. 181^1–181^3, 239–240, 243, art. 244 alin. (3)–(5) doar pentru faptele prevăzute la alin. (3) și (4), art. |
| `COD-122-2003` | art. 185^2 | 1 | - | intern | `COD-122-2003#art.276` l.4056 | tru săvârșirea unor infracţiuni prevăzute la art. 185^2, cu excepţia infracţiunilor prevăzute la alin. (2^3), şi la art. 185^ |
| `COD-218-2008` | art. 5^1 | 1 | - | intern | `COD-218-2008#art.440` l.7003 | zător se efectuează în limitele stabilite la art. 4 alin.(10) și art. 5^1din legea menționată. (5) Dacă la depistarea sau la examinarea cazului |
| `COD-218-2008` | art. 13^1 | 1 | - | modificare | `COD-434-2023#art.389` l.4129 | rile ulterioare, va avea următorul cuprins: „Articolul 13^1. Misiunile diplomatice pot procura sau obține prin schimb terenuri și |
| `COD-218-2008` | art. 52^2 | 1 | - | intern | `COD-218-2008#art.293^2` l.4870 | e plată și moneda electronică a prevederilor art. 50 alin. (1)–(5) și (7), art. 52^1 alin. (5), art. 52^2 alin. (1) și (2), art. 53 alin. (3), (4), (6) și (7), art. 55 alin. ( |
| `COD-218-2008` | art. 60^1 | 1 | - | intern | `COD-218-2008#art.293^2` l.4870 | e plată și moneda electronică a prevederilor art. 50 alin. (1)–(5) și (7), art. 52^1 alin. (5), art. 52^2 alin. (1) și (2), art. 53 alin. (3), (4), (6) și (7), art. 55 alin. ( |
| `COD-218-2008` | art. 641 | 1 | exponent turtit: art. 64^1 | intern | `COD-218-2008#art.409^2` l.6545 | (1) Contravențiile prevăzute la art.641, 642, 327^3 se constată de către Inspectoratul Social de Stat. (2) Su |
| `COD-225-2003` | art. 48^15 | 1 | - | intern | `COD-225-2003#art.308^17` l.2780 | u controlul executării mandatului, în sensul art. 48^15 alin. (3), şi de către persoanele ale căror drepturi sunt afectate pr |
| `COD-225-2003` | art. 581 | 1 | exponent turtit: art. 58^1 | din | `CC-1107-2002#art.113` l.943 | ori din oficiu. (3) În cazurile prevăzute la art. 581 din Codul de procedură civilă, curatorul special sau tutorele special |
| `L-105-2003` | art. 201 | 1 | - | din | `COD-218-2008#art.273` l.4531 | locului de preschimbare a mărfii prevăzut la art. 201 din Legea nr. 105/2003 privind protecția consumatorilor, lipsa inform |
| `L-131-2012` | art. 191 | 1 | exponent turtit: art. 19^1 | din | `L-160-2011#art.11^1` l.371 | permisiv în modul și termenele stabilite la art. 191 din Legea nr. 131/2012 privind controlul de stat asupra activităţii d |
| `L-160-2011` | art. 62 | 1 | exponent turtit: art. 6^2 | intern | `L-160-2011#art.8` l.320 | fel de taxă. Prin derogare de la prevederile art. 62 alin. (2), duplicatul actului permisiv se consideră eliberat prin apr |
| `L-160-2026` | art. 72 | 1 | - | intern | `L-160-2026#art.40` l.456 | o privesc încalcă prezenta lege. Prevederile art. 72 și 73, precum și ale cap. VIII secțiunea a 2-a din Legea nr. 195/2024 |
| `L-171-2012` | art. 38 | 1 | in registrul in-force: abrogare de la 2027-06-01, textul lipseste din fisier | din | `L-2-2020#art.17` l.400 | nirii de către SAI a cerințelor stabilite în art. 38, 41 și 49 din Legea nr. 171/2012 privind piața de capital. (8) SAI ar |
| `L-171-2012` | art. 81 | 1 | - | din | `HCNPF-14-5-2016#corp` l.73 | nistru_________ Vladimir CEBOTARI În temeiul art.1 alin.(2)-(4), art.5, art. 34, art. 59 alin. (3), art. 81 alin. (2), art. 87 alin. (4), art.147 alin.(8) din Legea nr. 171 di |
| `L-171-2012` | art. 87 | 1 | - | din | `HCNPF-14-5-2016#corp` l.73 | nistru_________ Vladimir CEBOTARI În temeiul art.1 alin.(2)-(4), art.5, art. 34, art. 59 alin. (3), art. 81 alin. (2), art. 87 alin. (4), art.147 alin.(8) din Legea nr. 171 di |
| `L-171-2012` | art. 88 | 1 | - | din | `HCNPF-38-5-2015#corp` l.72 | alin.(3), art.71 alin.(6), art.78, art.88 alin.(5) art.140 alin.(15) lit.c), art.143 alin.(2) din Legea nr.171 din 11.07.2012 „Privind piaţa |
| `L-183-2012` | art. 541 | 1 | exponent turtit: art. 54^1 | intern | `L-183-2012#art.68` l.1103 | or solicitate la interviul dispus în temeiul art. 541 ori se prezintă la interviu, dar refuză de a fi intervievate sau, în |
| `L-183-2012` | art. 571 | 1 | exponent turtit: art. 57^1 | intern | `L-183-2012#art.71` l.1151 | ine obligatoriu printr-o decizie, în temeiul art. 571; e) nu notifică o concentrare economică, definită la art. 22 alin. (1 |
| `L-202-2017` | art. 13^9 | 1 | - | din | `HBN-127-2013#corp` l.150 | nctul 2), Banca Naţională aplică prevederile art.13^9 şi/sau 14^1 din Legea nr.202 din 6 octombrie 2017 privind activitatea |
| `L-202-2017` | art. 75^2 | 1 | - | intern | `L-202-2017#art.142` l.1721 | plicabile, în mod corespunzător, prevederile art. 75^2 alin. (5) referitoare la încălcarea repetată, ale alin. (6) şi ale al |
| `L-202-2017` | art. 521 | 1 | exponent turtit: art. 52^1 | din | `L-232-2016#art.58` l.477 | cazul în care acțiunile emise în condițiile art. 521 din Legea nr. 202/2017 privind activitatea băncilor nu au fost vândut |
| `L-548-1995` | art. 112 | 1 | exponent turtit: art. 11^2 | intern | `L-548-1995#art.11` l.290 | emise de Banca Națională se notifică conform art. 112. (3^2) - abrogat. (3^3) În cadrul avizării și consultării publice a p |
| `L-548-1995` | art. 491 | 1 | exponent turtit: art. 49^1 | intern | `L-548-1995#art.75` l.973 | perceperea incontestabilă a amenzii conform art. 491 alin. (3) lit. f) în mărime de la 10 000 de lei la 600 000 de lei; d) |
| `L-548-1995` | art. 494 | 1 | exponent turtit: art. 49^4 | intern | `L-548-1995#art.49^1` l.738 | ea acestora în vederea punerii în aplicare a art. 494 alin. (8) și art. 495 alin. (8); c) să adopte acte normative care stabilesc cerințe față de |
| `L-548-1995` | art. 495 | 1 | exponent turtit: art. 49^5 | intern | `L-548-1995#art.49^1` l.738 | ea acestora în vederea punerii în aplicare a art. 494 alin. (8) și art. 495 alin. (8); c) să adopte acte normative care stabilesc cerințe față de |
| `L-548-1995` | art. 752 | 1 | exponent turtit: art. 75^2 | din | `L-62-2008#art.63` l.1155 | urilor se face ţinînd cont şi de prevederile art. 75 şi art. 752 din Legea nr. 548-XIII din 21 iulie 1995 cu privire la Banca Naţional |
| `L-550-1995` | art. 6 | 1 | - | intern | `L-550-1995#art.38^5` l.230 | or financiare și sînt aplicabile prevederile art. 6 alin. (3) din legea menționată; i) executarea obligaţiilor faţă de ba |
| `L-550-1995` | art. 15 | 1 | - | din | `HBN-130-2013#corp` l.72 | modificările şi completările ulterioare, şi articolelor 15-156 din Legea instituţiilor financiare nr.550-XIII din 21 iulie 1995 |
| `L-550-1995` | art. 31 | 1 | - | din | `COD-985-2002#art.239^1` l.3541 | ă afiliată va avea semnificația prevăzută în art. 31 din Legea instituțiilor financiare nr. 550-XIII din 21 iulie 1995. |
| `L-550-1995` | art. 37^9 | 1 | - | din | `L-202-2017#art.148` l.1811 | tolelor I, II, III, III^1, IV, V, VI, VII și art. 37^9 din Legea instituţiilor financiare nr. 550/1995 se abrogă. |

„Poate fi” este o ipoteza mecanica, nu o muchie: numarul citat, despartit in baza si exponent, da o ancora existenta. Se verifica in sursa inainte de a fi folosita.

## Ce nu face acest graf

- Nu deduce. O muchie exista numai daca textul o contine, si poarta liniile din care vine.
- Nu coboara sub articol: `alin.`, `lit.`, `pct.` nu sint noduri.
- Nu citeste articolele actelor pe puncte (HG, regulamente BNM si CNPF, proceduri DCU), nici extrasele UE: pentru ele exista doar muchii la nivel de act.
- Citeste numai numerele scrise dupa `art.` sau `articolul`. Intr-un interval (`art. 5-7`) sau intr-o enumerare prescurtata (`art. 2-5, 7-21`) numerele care urmeaza fara `art.` nu sint citite.
- Un articol citat fara act in context este atribuit actului curent. Regulile de context sint cele de mai sus; o trimitere al carei act sta mai departe in fraza decit le vad ele, sau e numit prin `legea mentionata` fara o lege numita inainte, ramine atribuita actului curent.
- O lege citata pe nume este rezolvata la actul detinut al carui titlu contine numele, numai daca exact unul il contine.
- Notele de modificare intre paranteze drepte, rindurile blocului de istoric si referintele la Monitorul Oficial sint mascate inainte de citire.
- Nu citeste corpusul englez BNM (traduceri) si nici radacinile de politici.
- Nu stie daca un act citat si **nedetinut** mai este in vigoare. Pentru actele detinute stie, din 2026-09-10, fiindca ingestul scrie `repealed` in frontmatter.

