# Graful de citare al actelor detinute

Generat 2026-09-26 22:27 de `_meta/graph/build_citation_graph.py`. Nu edita de mina; se reface rulind scriptul. Datele: `citation-graph.json` in acelasi folder.

**Ce este.** Trimiterile dintre actele detinute, extrase mecanic din textul brut: fiecare muchie poarta fisierul si liniile din care a fost citita, si nicio muchie nu este dedusa. Graful nu se citeaza. El spune unde sa deschizi fisierul, iar ancora se citeste.

**Regula de folosire.** Inainte de a cita un articol, cauta-l in tabelul „Dispozitii cu stare speciala si cine le citeaza”: daca apare, fie el, fie o dispozitie de care depinde nu se aplica astazi asa cum sta in text. Inainte de a ingera un act, citeste „Coada de ingerare”: acolo sint actele pe care textele detinute le citeaza si vault-ul nu le are.

## Numere

| | |
|---|---:|
| acte primare detinute (din care ancorate pe articole) | 237 (181) |
| dispozitii (noduri-articol) | 17886 |
| extrase UE detinute (noduri-tinta) | 50 |
| acte citate si nedetinute (noduri externe) | 903 |
| mentiuni de acte in text (din care ale actului insusi) | 7440 (781) |
| muchii act -> act (agregate pe segment-sursa) | 4941 |
| trimiteri la articole citite (in grupuri de enumerare) | 13583 (12010) |
|   rezolvate in actul curent | 11197 |
|   rezolvate in alt act detinut | 1559 |
|   nerezolvate: articolul nu are ancora in actul-tinta | 138 |
|   catre acte nedetinute (notate pe muchia act -> act) | 560 |
|   catre acte pe puncte (fara articole) | 94 |
|   autoreferinte (articolul se citeaza pe sine), ignorate | 35 |
| muchii articol -> articol (agregate) | 10324 |
| muchii articol -> act nerezolvate (agregate) | 125 |

Regula care a dat actul-tinta, pe trimiteri: din 1890, doua-puncte 46, intern 10857, modificare 56, paranteza 45. „intern” = niciun act in context, deci actul curent; „din” = `art. N ... din Legea X` sau `(art. N, M) Directiva X`; „paranteza” = `Legea X (art. N)`; „doua-puncte” = `din Codul X: art. N, M`; „modificare” = `Legea X se modifica dupa cum urmeaza: ... articolul N`. `din legea indicata` trimite la ultima lege numita in acelasi segment.

Coduri citate si pe nume si pe numar, unite dupa textul care le scrie impreuna: COD-apelor = COD-1532-1993; COD-audiovizualului = COD-260-2006; COD-educatiei = COD-152-2014; COD-electoral = COD-325-2022; COD-familiei = COD-1316-2000; COD-jurisdictiei-constitutionale = COD-502-1995; COD-subsolului = COD-3-2009; COD-transporturilor-rutiere = COD-150-2014.

## Coada de ingerare

Actele pe care textele detinute le citeaza si care nu sint in vault, in ordinea numarului de mentiuni. Un act citat de multe acte detinute inchide mai multe lanturi de trimitere decit unul citat des dintr-un singur loc; coloana a treia este cea care conteaza pentru ordinea de ingerare. Graful nu stie daca un act citat mai este in vigoare: o lege abrogata ramine citata de textele care n-au fost actualizate, si apare aici la fel ca una in vigoare.

### Acte moldovenesti citate pe numar

Legi, coduri si hotariri de Guvern identificate prin numar si an.

| act citat | mentiuni | acte care il citeaza | cel mai des din | articole citate |
|---|---:|---:|---|---|
| `L-174-2017` Legea nr. 174/2017 | 57 | 5 | `L-164-2025` (28) | art. 7^2 (x3), art. 20 (x2), art. 7^3, art. 11 |
| `L-235-2011` Legea nr. 235/2011 | 36 | 13 | `L-72-2025` (6) | art. 2, art. 14^3, art. 23^1, art. 31 |
| `L-142-2018` Legea nr. 142/2018 | 30 | 13 | `L-227-2025` (11) | art. 3 |
| `L-74-2020` Legea nr. 74/2020 | 28 | 6 | `L-22-2025` (9) | art. 6, art. 14, art. 19, art. 23^1 |
| `L-139-2012` Legea nr. 139/2012 | 27 | 8 | `L-10-2016` (10) | art. 3 |
| `L-107-2016` Legea nr. 107/2016 | 27 | 6 | `L-10-2016` (21) | art. 11, art. 47, art. 55, art. 69 |
| `L-152-2022` Legea nr. 152/2022 | 27 | 5 | `L-394-2023` (14) | art. 20 (x3), art. 4 (x2), art. 5, art. 9 |
| `L-48-2023` Legea nr. 48/2023 | 26 | 11 | `L-171-2012` (4) | - |
| `L-231-2010` Legea nr. 231/2010 | 23 | 13 | `L-1100-2000` (4) | art. 14, art. 16, art. 19^1, art. 20^1 |
| `L-139-2010` Legea nr. 139/2010 | 22 | 11 | `L-230-2022` (5) | art. 30 |
| `L-172-2014` Legea nr. 172/2014 | 18 | 9 | `L-82-2024` (6) | - |
| `L-11-2017` Legea nr. 11/2017 | 17 | 8 | `COD-434-2023` (9) | art. 10 (x2), art. 7 |
| `L-989-2002` Legea nr. 989/2002 | 16 | 9 | `L-121-2007` (5) | art. 5 |
| `L-184-2016` Legea nr. 184/2016 | 15 | 6 | `CC-1107-2002` (6) | art. 8 (x3), art. 4, art. 14 |
| `L-277-2018` Legea nr. 277/2018 | 14 | 8 | `L-403-2023` (5) | art. 31 (x2) |
| `L-187-2022` Legea nr. 187/2022 | 14 | 7 | `L-92-2014` (6) | art. 5, art. 59, art. 70, art. 86 |
| `L-407-2006` Legea nr. 407/2006 | 14 | 7 | `HCNPF-14-5-2016` (5) | art. 29 |
| `L-419-2006` Legea nr. 419/2006 | 13 | 8 | `L-397-2003` (3) | art. 16, art. 42, art. 45, art. 49 |
| `L-137-2015` Legea nr. 137/2015 | 13 | 7 | `L-198-2007` (4) | art. 19, art. 32, art. 39 |
| `L-151-2022` Legea nr. 151/2022 | 13 | 5 | `COD-434-2023` (8) | art. 4 (x3), art. 8 (x2), art. 12, art. 19 |
| `L-440-2001` Legea nr. 440/2001 | 13 | 5 | `COD-1163-1997` (6) | art. 5, art. 6, art. 13 |
| `L-287-2017` Legea nr. 287/2017 | 12 | 10 | `L-234-2016` (2) | art. 4 (x5), art. 24 |
| `L-162-2023` Legea nr. 162/2023 | 12 | 6 | `L-143-2014` (6) | - |
| `L-29-2018` Legea nr. 29/2018 | 12 | 6 | `L-121-2007` (6) | art. 9 (x2) |
| `L-282-2023` Legea nr. 282/2023 | 12 | 3 | `L-10-2016` (7) | art. 3 (x3), art. 8 |
| `L-174-2021` Legea nr. 174/2021 | 11 | 6 | `L-160-2011` (5) | art. 6 (x2), art. 11 (x2), art. 4, art. 9 |
| `COD-152-2014` Codul nr. 152/2014 | 11 | 5 | `COD-1163-1997` (6) | art. 12, art. 13, art. 15 |
| `L-279-2017` Legea nr. 279/2017 | 11 | 5 | `L-394-2023` (3) | art. 2, art. 8, art. 11 |
| `HG-411-2022` Hotarirea Guvernului nr. 411/2022 | 11 | 2 | `L-209-2016` (10) | - |
| `L-202-2013` Legea nr. 202/2013 | 10 | 6 | `COD-218-2008` (3) | art. 2, art. 3, art. 5, art. 10 |
| … inca 520 in JSON | | | | |

### Acte UE citate si neextrase

Directive si regulamente UE care nu au un extras `UE-*` in `raw/papers/cnpf/`.

| act citat | mentiuni | acte care il citeaza | cel mai des din | articole citate |
|---|---:|---:|---|---|
| `EU-TFUE` Tratatul privind functionarea Uniunii Europene | 18 | 5 | `HG-497-2026` (13) | art. 101, art. 288 |
| `EU-L-1995-46` Directiva 1995/46 | 7 | 5 | `DCNPDCP-41-2026` (3) | - |
| `EU-L-2014-23` Directiva 2014/23 | 6 | 4 | `L-22-2025` (2) | art. 1, art. 2, art. 6, art. 7 |
| `EU-L-2003-6` Directiva 2003/6 | 5 | 1 | `AA-2014` (5) | - |
| `EU-R-2004-852` Regulamentul (UE) nr. 852/2004 | 5 | 1 | `L-296-2017` (5) | - |
| `EU-L-2005-60` Directiva 2005/60 | 4 | 3 | `AA-2014` (2) | - |
| `EU-R-2009-1060` Regulamentul (UE) nr. 1060/2009 | 4 | 3 | `L-171-2012` (2) | art. 2, art. 3, art. 4, art. 6 |
| `EU-L-2004-39` Directiva 2004/39 | 4 | 2 | `AA-2014` (3) | - |
| `EU-R-2004-2006` Regulamentul (UE) nr. 2006/2004 | 4 | 2 | `L-105-2003` (3) | - |
| `EU-R-2004-853` Regulamentul (UE) nr. 853/2004 | 4 | 1 | `L-296-2017` (4) | art. 6 (x2), art. 3 |
| `EU-L-2002-87` Directiva 2002/87 | 3 | 3 | `L-250-2017` (1) | art. 9 |
| `EU-L-2018-843` Directiva 2018/843 | 3 | 3 | `L-92-2022` (1) | - |
| `EU-L-1979-117` Directiva 1979/117 | 3 | 2 | `L-403-2023` (2) | art. 1, art. 2, art. 3, art. 4 |
| `EU-L-1999-44` Directiva 1999/44 | 3 | 2 | `L-133-2018` (2) | - |
| `EU-L-2006-48` Directiva 2006/48 | 3 | 2 | `AA-2014` (2) | - |
| `EU-L-2006-70` Directiva 2006/70 | 3 | 2 | `AA-2014` (2) | - |
| `EU-L-2014-24` Directiva 2014/24 | 3 | 2 | `L-131-2015` (2) | art. 1, art. 2, art. 22, art. 23 |
| `EU-L-2019-1937` Directiva 2019/1937 | 3 | 2 | `L-165-2023` (2) | - |
| `EU-R-2009-1107` Regulamentul (UE) nr. 1107/2009 | 3 | 2 | `L-403-2023` (2) | art. 1, art. 3 |
| `EU-L-2009-31` Directiva 2009/31 | 3 | 1 | `L-86-2014` (3) | - |
| … inca 239 in JSON | | | | |

### Legi citate doar pe nume, fara corespondent in vault

Fara numar in text si fara un titlu detinut care sa le contina, deci identificate numai prin primele cuvinte; acelasi act poate aparea sub doua forme flexionate. Orientativ.

| act citat | mentiuni | acte care il citeaza | cel mai des din | articole citate |
|---|---:|---:|---|---|
| `LEGE:protectia-datelor-cu-caracter` Legea privind protecția datelor cu caracter personal | 65 | 7 | `OCNPDCP-SANATATE` (27) | art. 3 (x5), art. 4 (x5), art. 29 (x4), art. 5 (x3) |
| `LEGE:protectia-datelor-eu-caracter` Legea privind protecția datelor eu caracter personal | 10 | 1 | `OCNPDCP-SANATATE` (10) | art. 4, art. 5, art. 12, art. 29 |
| `LEGE:energetica` Legea cu privire la energetică | 8 | 1 | `L-108-2016` (8) | - |
| `LEGE:contabilitatii` Legea contabilităţii | 7 | 4 | `L-139-2007` (2) | - |
| `LEGE:mediere` Legea cu privire la mediere | 6 | 3 | `COD-225-2003` (2) | - |
| `LEGE:avocatura` Legea cu privire la avocatură | 6 | 2 | `L-198-2007` (5) | - |
| `LEGE:serviciului-public` Legea serviciului public | 6 | 1 | `L-158-2008` (6) | art. 33 |
| `LEGE:statutul-municipiului` Legea privind statutul municipiului | 6 | 1 | `L-436-2006` (6) | - |
| `LEGE:privind` Legea privind | 5 | 2 | `L-1134-1997` (4) | - |
| `LEGE:protectia-martorilor-si-altor` Legea cu privire la protecţia martorilor şi | 4 | 2 | `COD-122-2003` (3) | - |
| `LEGE:cetateniei` Legea cetățeniei | 3 | 3 | `L-273-1994` (1) | art. 18 |
| `LEGE:din` Legea din | 3 | 1 | `CONST-1994` (3) | - |
| `LEGE:locuinte` Legea cu privire la locuinţe | 3 | 1 | `L-436-2006` (3) | - |
| `LEGE:protectia-indicatiilor-geografice` Legea privind protecţia indicaţiilor geografice | 3 | 1 | `COD-218-2008` (3) | - |
| `LEGE:publicitate-si-cu` Legea cu privire la publicitate şi cu | 3 | 1 | `COD-174-2018` (3) | - |
| … inca 79 in JSON | | | | |

## Acquis: extrasele UE detinute si actele care le citeaza

Mentiunile actelor detinute catre cele 29 de extrase `UE-*`. Schita unei concordante: un act care citeaza o directiva o transpune, o aplica sau doar o numeste, si numai textul spune care.

| extras UE | mentiuni | citat din |
|---|---:|---|
| `UE-1986-635` | 0 | - |
| `UE-1991-674` | 1 | `AA-2014` (1) |
| `UE-1994-19` | 1 | `AA-2014` (1) |
| `UE-2000-518` | 0 | - |
| `UE-2002-2` | 0 | - |
| `UE-2003-490` | 0 | - |
| `UE-2003-821` | 0 | - |
| `UE-2004-109` | 2 | `AA-2014` (2) |
| `UE-2004-25` | 0 | - |
| `UE-2004-411` | 0 | - |
| `UE-2007-36` | 1 | `L-1134-1997` (1) |
| `UE-2008-393` | 0 | - |
| `UE-2008-48` | 0 | - |
| `UE-2009-103` | 2 | `AA-2014` (1), `L-106-2022` (1) |
| `UE-2009-138` | 6 | `L-106-2022` (2), `L-92-2022` (2), `AA-2014` (1), `L-308-2017` (1) |
| `UE-2009-65` | 2 | `AA-2014` (1), `L-171-2012` (1) |
| `UE-2010-146` | 0 | - |
| `UE-2010-625` | 0 | - |
| `UE-2011-61` | 0 | - |
| `UE-2012-484` | 0 | - |
| `UE-2013-65` | 0 | - |
| `UE-2014-57` | 0 | - |
| `UE-2014-65` | 1 | `L-2-2020` (1) |
| `UE-2015-849` | 4 | `L-308-2017` (2), `L-106-2022` (1), `L-92-2022` (1) |
| `UE-2016-2341` | 1 | `L-198-2020` (1) |
| `UE-2016-679` | 6 | `DCNPDCP-41-2026` (3), `L-195-2024` (1), `OCNPDCP-27-2022` (1), `OCNPDCP-31-2026` (1) |
| `UE-2016-680` | 1 | `L-160-2026` (1) |
| `UE-2016-97` | 0 | - |
| `UE-2017-1129` | 2 | `L-165-2023` (1), `L-181-2023` (1) |
| `UE-2017-1132` | 3 | `L-1134-1997` (2), `L-133-2018` (1) |
| `UE-2017-828` | 0 | - |
| `UE-2019-419` | 0 | - |
| `UE-2020-1503` | 2 | `L-165-2023` (1), `L-181-2023` (1) |
| `UE-2021-1772` | 0 | - |
| `UE-2021-2118` | 0 | - |
| `UE-2021-914` | 0 | - |
| `UE-2022-254` | 0 | - |
| `UE-2023-2225` | 0 | - |
| `UE-2024-1620` | 0 | - |
| `UE-2024-1624` | 0 | - |
| `UE-2024-1640` | 0 | - |
| `UE-2025-1382` | 0 | - |
| `UE-2026-179` | 0 | - |
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
| `COD-3-2009` | 2026-05-30 | CS246 din 08.11.24 | 6 | 4 | art. 9, art. 14, art. 15, art. 16, art. 19, art. 28, art. 30, art. 32 |
| `HG-1171-2018` | 2026-09-22 | HG497 din 02.09.26 | 2 | 2 | - |
| `L-133-2011` | 2026-08-23 | LP195 din 25.07.24 | 92 | 38 | art. 1, art. 2, art. 4, art. 5, art. 6, art. 12, art. 13, art. 20 |

`COD-3-2009` este citat din: `COD-246-2024`, `COD-434-2023`, `L-209-2016`, `L-317-2025`.

`HG-1171-2018` este citat din: `HG-497-2026`, `HG-610-2018`.

`L-133-2011` este citat din: `COD-122-2003`, `COD-150-2014`, `COD-218-2008`, `COD-95-2021`, `DCNPDCP-08-2023`, `DCNPDCP-581-2015`, `DCNPDCP-PARTIDE-2014`, `DCU-REGULI-2026`, `HCNPF-14-5-2016`, `HG-310-2025`, `L-102-2017`, `L-105-2003`, `L-105-2018`, `L-114-2012`, `L-122-2008`, `L-132-2016`, `L-1543-1998`, `L-165-2023`, `L-171-2012`, `L-181-2023`, `L-195-2024`, `L-202-2017`, `L-246-2018`, `L-28-2024`, `L-284-2004`, `L-308-2017`, `L-325-2013`, `L-325-2025`, `L-384-2023`, `L-436-2006`, `L-548-1995`, `L-71-2007`, `L-72-2025`, `OCNPDCP-03-1-2013`, `OCNPDCP-03-2015`, `OCNPDCP-39-2026`, `OCNPDCP-POLITIE-2013`, `OCNPDCP-SANATATE`.

Limita care ramine: pentru actele **nedetinute** din coada de ingerare graful tot nu stie daca mai sint in vigoare. Se afla numai deschizind fisa lor pe legis.md, si nici acolo cimpul „Data abrogarii” nu este de incredere: pentru `L-133-2011` el era gol, desi corpul consolidarii declara abrogarea.

## Dispozitii cu stare speciala si cine le citeaza

Dispozitiile care apar in registrul in-force (textul din fisier nu se aplica inca), in registrul HCC (declarate neconstitutionale, in tot sau in parte) sau al caror titlu spune „abrogat”, si muchiile articol -> articol care intra in ele. Un articol din coloana „citat din” depinde de o dispozitie care nu sta in picioare asa cum e scrisa. Numai dispozitiile cu cel putin o citare intra aici, intii cele citate din alte acte; toate starile sint in JSON.

| dispozitie | stare | citari (din alte acte) | citat din |
|---|---|---:|---|
| `COD-1163-1997#art.123` l.3751 | HCC: HCC17/2014-05-29, alin. (7), subunitate | 5 (4) | `L-1100-2000#art.20`, `COD-1163-1997#art.262`, `L-1100-2000#art.4`, `L-1100-2000#art.5` |
| `L-548-1995#art.11` l.294 | HCC: HCC31/2013-10-01, al.(4), articol intreg | 7 (3) | `L-548-1995#art.75^1`, `L-114-2012#art.98`, `L-202-2017#art.144`, `L-232-2016#art.319`, `L-548-1995#art.6` |
| `COD-122-2003#art.191` l.3019 | HCC: HCC17/2016-05-19, omisiune legislativa (+1) | 5 (2) | `COD-443-2004#art.301`, `COD-122-2003#art.192`, `COD-122-2003#art.309`, `COD-122-2003#art.310` |
| `COD-218-2008#art.34` l.1025 | HCC: HCC7/2018-04-26, alin. (3), text din articol | 3 (2) | `COD-443-2004#art.315` l.3242, `COD-218-2008#art.293^2` l.4877 |
| `L-278-2007#art.26` l.498 | in-force: nespecificat de la 2027-03-01 | 2 (2) | `COD-218-2008#art.91^1` l.2002 |
| `COD-225-2003#art.449` l.3638 | HCC: HCC16/2013-06-25, lit. f), in parte | 12 (1) | `COD-225-2003#art.450`, `COD-116-2018#art.170`, `COD-225-2003#art.447`, `COD-225-2003#art.451`, `COD-225-2003#art.451^1`, `COD-225-2003#art.453` |
| `COD-225-2003#art.267` l.2173 | HCC: HCC33/2016-11-17, lit. b), in parte | 7 (1) | `COD-225-2003#art.268`, `COD-225-2003#art.185`, `COD-225-2003#art.49`, `COD-225-2003#art.89`, `COD-225-2003#art.98`, `COD-443-2004#art.163` |
| `COD-225-2003#art.170` l.1503 | HCC: HCC33/2016-11-17, alin. (1) lit. c), in parte | 5 (1) | `COD-225-2003#art.478`, `COD-225-2003#art.483`, `COD-225-2003#art.49`, `COD-225-2003#art.89`, `L-9-2026#art.47` |
| `COD-122-2003#art.273` l.3945 | HCC: HCC29/2021-09-21, alin. (1) lit. d^2), in parte | 3 (1) | `COD-122-2003#art.166` l.2749, `COD-122-2003#art.215^2` l.3350, `COD-443-2004#art.245` l.2569 |
| `COD-443-2004#art.15` l.376 | HCC: HCC39/2017-12-14, al.(2) lit.d), in parte | 3 (1) | `COD-443-2004#art.30` l.551, `COD-225-2003#art.470` l.3900 |
| `COD-122-2003#art.186` l.2951 | HCC: HCC3/2016-02-23, alin. (3), (5), (8), (9), text din articol | 2 (1) | `COD-122-2003#art.195` l.3076, `COD-443-2004#art.198` l.2066 |
| `L-135-2007#art.30` l.327 | HCC: HCC27/2016-09-27, al.(2) [numerotarea de la data hotaririi], subunitate | 2 (1) | `L-135-2007#art.25` l.279, `L-181-2023#art.49` l.737 |
| `L-303-2013#art.19` l.518 | HCC: HCC28/2016-10-11, alin. (5), text din articol (+1) | 2 (1) | `L-272-2011#art.25` l.585, `L-303-2013#art.8` l.258 |
| `COD-122-2003#art.6` l.452 | HCC: HCC2/2020-01-23, pct. 11^1), text din articol | 1 (1) | `COD-443-2004#art.98^1` l.1164 |
| `COD-218-2008#art.423^4` l.6663 | abrogat | 1 (1) | `L-195-2024#art.90` l.1173 |
| `COD-218-2008#art.427` l.6740 | HCC: HCC26/2024-12-12, alin.(2), text din articol | 1 (1) | `COD-95-2021#art.408` l.4429 |
| `COD-218-2008#art.74^1` l.1705 | abrogat | 1 (1) | `L-195-2024#art.90` l.1173 |
| `COD-225-2003#art.343^6` l.3015 | HCC: HCC37/2021-12-07, text din articol | 1 (1) | `L-325-2013#art.14` l.259 |
| `COD-325-2022#art.90` l.1605 | HCC: HCC16/2024-07-16, al.(2), textul „În serviciile media audiovizuale ... furnizorilor de servicii media.”, text din articol | 1 (1) | `COD-174-2018#art.84` l.1535 |
| `COD-443-2004#art.22` l.442 | HCC: HCC17/2017-05-10, al.(1) lit.v), text din articol | 1 (1) | `CC-1107-2002#art.757` l.5384 |
| `COD-985-2002#art.189` l.2579 | HCC: HCC24/2019-10-17, alin. (3) lit. f), text din articol | 1 (1) | `COD-122-2003#art.229^2` l.3493 |
| `L-100-2001#art.5` l.175 | HCC: HCC28/2002-05-30, al.(4), sintagma „și limba rusă”, text din articol | 1 (1) | `L-246-2018#art.42` l.501 |
| `L-131-2015#art.80` l.1493 | abrogat | 1 (1) | `L-20-2026#art.29` l.424 |
| `L-131-2015#art.86` l.1506 | abrogat | 1 (1) | `L-20-2026#art.29` l.428 |
| `L-158-2008#art.70` l.1154 | abrogat | 1 (1) | `L-80-2010#art.28` l.321 |
| `L-69-2016#art.12` l.201 | abrogat | 1 (1) | `L-246-2018#art.96` l.1018 |
| `L-845-1992#art.36` l.573 | abrogat | 1 (1) | `COD-1163-1997#art.227^1` l.5972 |
| `COD-325-2022#art.68` l.1216 | HCC: HCC9/2024-03-26, al.(1), lit.f), text din articol (+2) | 18 (0) | `COD-325-2022#art.91`, `COD-325-2022#art.102`, `COD-325-2022#art.111`, `COD-325-2022#art.112`, `COD-325-2022#art.113`, `COD-325-2022#art.115`, … (+9) |
| `COD-325-2022#art.16` l.253 | HCC: HCC16/2023-10-03, al.(2), lit.e), subunitate (+5) | 10 (0) | `COD-325-2022#art.68`, `COD-325-2022#art.102`, `COD-325-2022#art.72`, `COD-325-2022#art.245`, `COD-325-2022#art.89` |
| `COD-1163-1997#art.88` l.2979 | HCC: HCC7/2014-02-13, alin. (7), subunitate | 9 (0) | `COD-1163-1997#art.92`, `COD-1163-1997#art.372`, `COD-1163-1997#art.69^7`, `COD-1163-1997#art.73`, `COD-1163-1997#art.76`, `COD-1163-1997#art.79`, … (+2) |
| `COD-1163-1997#art.291` l.6915 | HCC: HCC2/2014-01-28, in parte | 8 (0) | `COD-1163-1997#art.293` l.6950, `COD-1163-1997#art.292` l.6944 |
| `L-24-2008#art.6` l.111 | HCC: HCC3/2012-02-09, al.(2), modificarea din art. XIII pct. 1 LP163/2011, revigorare | 7 (0) | `L-24-2008#art.11`, `L-24-2008#art.13`, `L-24-2008#art.14`, `L-24-2008#art.37` |
| `COD-1163-1997#art.289` l.6866 | HCC: HCC2/2014-01-28, in parte | 6 (0) | `COD-1163-1997#art.297` l.7019, `COD-1163-1997#art.298` l.7028, `COD-1163-1997#art.294` l.6962 |
| `COD-122-2003#art.401` l.5149 | HCC: HCC9/2008-05-20, alin. (1) pct. 3), text din articol | 6 (0) | `COD-122-2003#art.402`, `COD-122-2003#art.420`, `COD-122-2003#art.421`, `COD-122-2003#art.438`, `COD-122-2003#art.445`, `COD-122-2003#art.447` |
| `COD-325-2022#art.102` l.1795 | HCC: HCC9/2024-03-26, al.(5), lit.e), subunitate | 6 (0) | `COD-325-2022#art.101`, `COD-325-2022#art.42`, `COD-325-2022#art.43`, `COD-325-2022#art.54`, `COD-325-2022#art.72`, `COD-325-2022#art.94` |
| `COD-325-2022#art.91` l.1645 | HCC: HCC9/2024-03-26, al.(3^1), subunitate (+1) | 6 (0) | `COD-325-2022#art.95`, `COD-325-2022#art.92`, `COD-325-2022#art.93`, `COD-325-2022#art.94`, `COD-325-2022#art.99` |
| `L-278-2007#art.17` l.384 | in-force: nespecificat de la 2029-01-01 | 6 (0) | `L-278-2007#art.19` l.435, `L-278-2007#art.16` l.379, `L-278-2007#art.20` l.447 |
| `COD-1316-2000#art.108` l.893 | HCC: HCC23/2024-10-15, omisiune legislativa | 5 (0) | `COD-1316-2000#art.76`, `COD-1316-2000#art.78`, `COD-1316-2000#art.80`, `COD-1316-2000#art.84`, `COD-1316-2000#art.91` |
| `COD-122-2003#art.42` l.807 | HCC: HCC3/2012-02-09, alin. (7), in parte | 4 (0) | `COD-122-2003#art.256`, `COD-122-2003#art.279^1`, `COD-122-2003#art.43`, `COD-122-2003#art.561` |
| `COD-122-2003#art.421` l.5300 | HCC: HCC16/2005-07-19, text din articol | 4 (0) | `COD-122-2003#art.423`, `COD-122-2003#art.429`, `COD-122-2003#art.432`, `COD-122-2003#art.433` |
| `COD-225-2003#art.437` l.3546 | HCC: HCC20/2022-11-03, alin. (1), text din articol | 4 (0) | `COD-225-2003#art.426^1`, `COD-225-2003#art.436`, `COD-225-2003#art.438`, `COD-225-2003#art.439` |
| `L-132-2016#art.11` l.220 | HCC: HCC6/2018-04-10, al.(12), textul „și care a susținut proba detectorului comportamentului simulat (poligraf)”, text din articol | 4 (0) | `L-132-2016#art.10` l.218, `L-132-2016#art.13` l.303, `L-132-2016#art.15` l.366 |
| `L-230-2022#art.71` l.965 | HCC: HCC7/2025-06-10, al.(4), omisiune legislativa | 4 (0) | `L-230-2022#art.56`, `L-230-2022#art.70`, `L-230-2022#art.72`, `L-230-2022#art.99` |
| `L-797-1996#art.47` l.535 | HCC: HCC15/2012-12-04, al.(12), sintagma «și adoptat», text din articol | 4 (0) | `L-797-1996#art.48` l.555, `L-797-1996#art.147` l.1289, `L-797-1996#art.61` l.670 |
| `COD-1163-1997#art.264` l.6326 | HCC: HCC10/2024-04-04, alin. (1) si (2), text din articol | 3 (0) | `COD-1163-1997#art.214` l.5487, `COD-1163-1997#art.226^2` l.5641, `COD-1163-1997#art.265` l.6337 |
| `COD-1163-1997#art.6` l.1554 | HCC: HCC5/2024-03-05, alin. (11), subunitate | 3 (0) | `COD-1163-1997#art.226^1` l.5629, `COD-1163-1997#art.5` l.1526, `COD-1163-1997#art.7` l.1621 |
| `COD-122-2003#art.321` l.4480 | HCC: HCC3/2023-01-24, alin. (2) pct. 3), text din articol | 3 (0) | `COD-122-2003#art.199` l.3120, `COD-122-2003#art.412` l.5217, `COD-122-2003#art.559` l.6763 |
| `COD-174-2018#art.28` l.614 | HCC: HCC6/2022-03-10, al.(1), text din articol | 3 (0) | `COD-174-2018#art.25` l.564, `COD-174-2018#art.84` l.1545, `COD-174-2018#art.88` l.1609 |
| `COD-1163-1997#art.260` l.6258 | HCC: HCC20/2018-07-04, alin. (4), text din articol | 2 (0) | `COD-1163-1997#art.229` l.5996, `COD-1163-1997#art.234` l.6044 |
| `L-108-2016#art.24` l.703 | abrogat | 2 (0) | `L-108-2016#art.114` l.2500, `L-108-2016#art.37` l.886 |
| `L-213-2023#art.2` l.78 | HCC: HCC20/2024-09-26, al.(2), teza intai: textul „Taxa de timbru nu este susceptibilă de scutire, amânare sau eșalonare, cu excepțiile prevăzute de prezenta lege.”, text din articol | 2 (0) | `L-213-2023#preambul` l.55 |
| `L-283-2003#art.22^1` l.327 | HCC: HCC11/2023-07-20, alin. (1) lit. c), text din articol | 2 (0) | `L-283-2003#art.22^2` l.361, `L-283-2003#art.27` l.462 |
| `L-325-2013#art.17` l.292 | HCC: HCC37/2021-12-07, al.(2), subunitate (+2) | 2 (0) | `L-325-2013#art.10` l.214, `L-325-2013#art.21` l.381 |
| `COD-1163-1997#art.290` l.6893 | HCC: HCC2/2014-01-28, in parte | 1 (0) | `COD-1163-1997#art.297` l.7019 |
| `COD-122-2003#art.178` l.2861 | HCC: HCC19/2018-07-03, omisiune legislativa | 1 (0) | `COD-122-2003#art.547` l.6621 |
| `COD-122-2003#art.185` l.2939 | HCC: HCC27/2018-10-30, al.(1), subunitate | 1 (0) | `COD-122-2003#art.188` l.2995 |
| `COD-122-2003#art.192` l.3037 | HCC: HCC15/2020-05-28, alin. (2), subunitate | 1 (0) | `COD-122-2003#art.192^1` l.3050 |
| `COD-122-2003#art.287` l.4105 | HCC: HCC12/2015-05-14, alin. (1), subunitate | 1 (0) | `COD-122-2003#art.326` l.4527 |
| `COD-122-2003#art.400` l.5144 | HCC: HCC3/2012-02-09, alin. (3), in parte | 1 (0) | `COD-122-2003#art.465^8` l.5599 |
| `COD-154-2003#art.90` l.1301 | HCC: HCC9/2025-07-22, al.(2), lit. a), text din articol | 1 (0) | `COD-154-2003#art.330` l.3258 |
| `COD-174-2018#art.66` l.1278 | HCC: HCC36/2021-11-23, al.(7), text din articol | 1 (0) | `COD-174-2018#art.84` l.1542 |
| `COD-218-2008#art.197^1` l.3394 | abrogat | 1 (0) | `COD-218-2008#art.431` l.6786 |
| `COD-218-2008#art.20` l.918 | abrogat | 1 (0) | `COD-218-2008#art.440^1` l.7025 |
| `COD-218-2008#art.233` l.3966 | HCC: HCC11/2018-05-08, alin. (3), text din articol | 1 (0) | `COD-218-2008#art.41` l.1109 |
| `COD-218-2008#art.445` l.7088 | HCC: HCC32/2018-11-29, articol intreg | 1 (0) | `COD-218-2008#art.451^3` l.7208 |
| `COD-218-2008#art.62` l.1495 | abrogat | 1 (0) | `COD-218-2008#art.293^2` l.4879 |
| `COD-225-2003#art.306` l.2677 | HCC: HCC33/2016-11-17, alin. (2), text din articol | 1 (0) | `COD-225-2003#art.77` l.835 |
| `COD-225-2003#art.39` l.527 | HCC: HCC3/2012-02-09, alin. (11^1), subunitate | 1 (0) | `COD-225-2003#art.41^1` l.569 |
| `COD-225-2003#art.58` l.696 | HCC: HCC33/2016-11-17, alin. (2), (2^1), (6), text din articol | 1 (0) | `COD-225-2003#art.79` l.841 |
| `COD-325-2022#art.36` l.627 | HCC: HCC8/2026-07-09, al.(1), textul „Componența Consiliului Electoral Central al Găgăuziei se aprobă ... și cu actele normative locale”, text din articol | 1 (0) | `COD-325-2022#art.245` l.2737 |
| `COD-325-2022#art.98` l.1735 | HCC: HCC9/2024-03-26, al.(1), subunitate | 1 (0) | `COD-325-2022#art.93` l.1690 |
| `COD-443-2004#art.161` l.1732 | HCC: HCC8/2019-04-05, al.(1) teza a doua, text din articol | 1 (0) | `COD-443-2004#art.79` l.995 |
| `COD-443-2004#art.174` l.1851 | HCC: HCC18/2013-07-04, alin. (3^1), subunitate | 1 (0) | `COD-443-2004#art.287` l.2988 |
| `COD-443-2004#art.61` l.814 | HCC: HCC22/2019-10-08, al.(1), text din articol | 1 (0) | `COD-443-2004#art.60` l.812 |
| `COD-95-2021#art.277^2` l.3013 | abrogat | 1 (0) | `COD-95-2021#art.277` l.3000 |
| `COD-985-2002#art.328` l.4979 | HCC: HCC22/2017-06-27, alin. (1), text din articol (+1) | 1 (0) | `COD-985-2002#art.55` l.732 |
| `COD-985-2002#art.329` l.4995 | HCC: HCC24/2019-10-17, alin. (1) si alin. (2) lit. b), text din articol | 1 (0) | `COD-985-2002#art.134^20` l.1572 |
| `COD-985-2002#art.335` l.5090 | HCC: HCC24/2019-10-17, alin. (1^1), text din articol (+1) | 1 (0) | `COD-985-2002#art.55` l.732 |
| `L-136-2017#art.23` l.347 | HCC: HCC7/2021-03-04, al.(6), in parte | 1 (0) | `L-136-2017#art.24` l.357 |
| `L-158-2008#art.53` l.949 | HCC: HCC6/2016-03-03, lit.c), subunitate | 1 (0) | `L-158-2008#art.41` l.757 |
| … inca 4 dispozitii, in JSON | | | |

Stari atasate dispozitiilor, in total: 4 in-force, 127 HCC, 382 abrogat. 84 dintre ele au cel putin o citare intrata, 27 din alte acte.

## Actele: ce citeaza si de cine sint citate

Pe act: tintele distincte ale mentiunilor (detinute + externe), actele detinute distincte care il mentioneaza, trimiterile la articole rezolvate in propriul text, rezolvate in alt act detinut, si nerezolvate (articolul citat nu are ancora in actul-tinta: abrogat cu ciotul sters, renumerotat, exponent turtit in sursa, sau o greseala de citire).

| act | ancore | citeaza (acte) | citat de (acte) | art. interne | art. in alte acte | nerezolvate | mentiuni externe |
|---|---:|---:|---:|---:|---:|---:|---:|
| `AA-2014` | 11 | 44 | 0 | 4 | 0 | 18 | 64 |
| `CC-1107-2002` | 2657 | 27 | 48 | 1017 | 5 | 1 | 20 |
| `CETS-223-2018` | 40 | 0 | 0 | 113 | 0 | 1 | 0 |
| `COD-116-2018` | 260 | 13 | 59 | 106 | 11 | 1 | 3 |
| `COD-1163-1997` | 511 | 66 | 41 | 447 | 23 | 1 | 64 |
| `COD-122-2003` | 657 | 25 | 18 | 465 | 217 | 2 | 23 |
| `COD-1316-2000` | 133 | 7 | 7 | 28 | 2 | 0 | 4 |
| `COD-150-2014` | 206 | 16 | 6 | 46 | 3 | 0 | 7 |
| `COD-154-2003` | 416 | 25 | 24 | 198 | 2 | 0 | 23 |
| `COD-174-2018` | 98 | 18 | 8 | 71 | 7 | 0 | 9 |
| `COD-218-2008` | 737 | 56 | 60 | 508 | 85 | 14 | 37 |
| `COD-22-2024` | 96 | 26 | 6 | 18 | 6 | 0 | 20 |
| `COD-225-2003` | 540 | 23 | 29 | 213 | 31 | 17 | 10 |
| `COD-246-2024` | 99 | 25 | 1 | 47 | 3 | 1 | 15 |
| `COD-259-2004` | 119 | 8 | 2 | 7 | 0 | 0 | 7 |
| `COD-3-2009` | 85 | 10 | 4 | 19 | 1 | 0 | 5 |
| `COD-325-2022` | 252 | 36 | 13 | 164 | 23 | 0 | 22 |
| `COD-434-2023` | 390 | 44 | 18 | 137 | 18 | 1 | 55 |
| `COD-443-2004` | 360 | 30 | 23 | 123 | 75 | 0 | 18 |
| `COD-95-2021` | 472 | 37 | 6 | 430 | 8 | 0 | 30 |
| `COD-985-2002` | 566 | 22 | 35 | 166 | 3 | 1 | 12 |
| `CONST-1994` | 157 | 4 | 84 | 13 | 1 | 0 | 5 |
| `DCA-61-2024` | 0 | 5 | 0 | 0 | 5 | 0 | 2 |
| `DCNPDCP-08-2023` | 0 | 2 | 0 | 0 | 1 | 0 | 1 |
| `DCNPDCP-41-2026` | 0 | 6 | 0 | 0 | 2 | 0 | 9 |
| `DCNPDCP-581-2015` | 0 | 3 | 0 | 0 | 1 | 0 | 2 |
| `DCNPDCP-PARTIDE-2014` | 0 | 5 | 0 | 0 | 0 | 0 | 8 |
| `DCU-PROC-COMISIOANE` | 0 | 2 | 2 | 0 | 1 | 0 | 2 |
| `DCU-PROC-DECONTARE` | 0 | 9 | 0 | 0 | 7 | 0 | 3 |
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
| `HCNPF-14-5-2016` | 0 | 12 | 0 | 0 | 29 | 2 | 11 |
| `HCNPF-38-5-2015` | 0 | 9 | 0 | 0 | 16 | 1 | 4 |
| `HG-1170-2016` | 0 | 16 | 1 | 0 | 6 | 0 | 17 |
| `HG-1171-2018` | 0 | 6 | 2 | 0 | 10 | 0 | 3 |
| `HG-118-2023` | 0 | 7 | 0 | 0 | 2 | 0 | 0 |
| `HG-143-2021` | 0 | 12 | 0 | 0 | 2 | 0 | 5 |
| `HG-146-2021` | 0 | 10 | 0 | 0 | 2 | 0 | 3 |
| `HG-147-2021` | 0 | 12 | 0 | 0 | 2 | 0 | 5 |
| `HG-148-2021` | 0 | 7 | 0 | 0 | 1 | 0 | 3 |
| `HG-149-2021` | 0 | 9 | 0 | 0 | 1 | 0 | 4 |
| `HG-186-2026` | 0 | 8 | 0 | 0 | 2 | 0 | 2 |
| `HG-305-2026` | 0 | 10 | 0 | 0 | 2 | 0 | 3 |
| `HG-310-2025` | 0 | 3 | 0 | 0 | 6 | 0 | 1 |
| `HG-386-2020` | 0 | 5 | 0 | 0 | 2 | 0 | 2 |
| `HG-497-2026` | 0 | 6 | 0 | 0 | 10 | 0 | 14 |
| `HG-553-2024` | 0 | 3 | 0 | 0 | 13 | 0 | 0 |
| `HG-574-2024` | 0 | 5 | 2 | 0 | 2 | 0 | 3 |
| `HG-582-2022` | 0 | 5 | 0 | 0 | 16 | 2 | 0 |
| `HG-610-2018` | 0 | 14 | 2 | 0 | 8 | 0 | 4 |
| `HG-657-2009` | 0 | 23 | 1 | 0 | 4 | 0 | 21 |
| `HG-690-2017` | 0 | 8 | 0 | 0 | 2 | 0 | 3 |
| `HG-693-2017` | 0 | 4 | 0 | 0 | 1 | 0 | 1 |
| `HG-695-2017` | 0 | 10 | 0 | 0 | 2 | 0 | 3 |
| `HG-696-2017` | 0 | 6 | 0 | 0 | 1 | 0 | 1 |
| `HG-698-2017` | 0 | 5 | 0 | 0 | 2 | 0 | 0 |
| `HG-743-2024` | 0 | 11 | 0 | 0 | 19 | 0 | 10 |
| `HG-9-2026` | 0 | 8 | 0 | 0 | 2 | 0 | 1 |
| `HG-967-2016` | 0 | 5 | 0 | 0 | 3 | 0 | 4 |
| `L-1-2018` | 28 | 5 | 2 | 19 | 0 | 0 | 2 |
| `L-10-2009` | 75 | 12 | 3 | 1 | 4 | 0 | 7 |
| `L-10-2016` | 63 | 28 | 3 | 95 | 3 | 0 | 58 |
| `L-100-2001` | 78 | 4 | 4 | 6 | 3 | 0 | 1 |
| `L-100-2017` | 80 | 18 | 15 | 12 | 7 | 0 | 7 |
| `L-102-2017` | 26 | 13 | 1 | 0 | 0 | 0 | 12 |
| `L-105-2003` | 75 | 21 | 11 | 76 | 8 | 0 | 26 |
| `L-105-2018` | 74 | 16 | 3 | 22 | 3 | 0 | 8 |
| `L-106-2022` | 45 | 10 | 2 | 32 | 1 | 0 | 7 |
| `L-108-2016` | 144 | 41 | 5 | 293 | 5 | 1 | 54 |
| `L-1100-2000` | 49 | 15 | 2 | 9 | 4 | 0 | 15 |
| `L-1125-2002` | 50 | 9 | 5 | 4 | 16 | 1 | 4 |
| `L-1134-1997` | 108 | 30 | 20 | 127 | 21 | 0 | 20 |
| `L-114-2012` | 131 | 24 | 13 | 267 | 13 | 0 | 15 |
| `L-114-2014` | 28 | 3 | 2 | 4 | 0 | 2 | 0 |
| `L-116-2014` | 18 | 6 | 2 | 2 | 0 | 0 | 7 |
| `L-119-2004` | 29 | 7 | 2 | 3 | 0 | 0 | 5 |
| `L-119-2018` | 32 | 11 | 6 | 56 | 6 | 1 | 7 |
| `L-121-2007` | 73 | 27 | 10 | 11 | 4 | 0 | 30 |
| `L-121-2018` | 46 | 7 | 4 | 29 | 1 | 0 | 3 |
| `L-122-2008` | 23 | 7 | 5 | 11 | 0 | 0 | 2 |
| `L-123-2023` | 16 | 3 | 1 | 6 | 1 | 0 | 0 |
| `L-124-2022` | 58 | 5 | 8 | 22 | 0 | 0 | 9 |
| `L-1260-2002` | 73 | 9 | 5 | 21 | 1 | 0 | 3 |
| `L-130-2012` | 77 | 10 | 1 | 164 | 1 | 0 | 7 |
| `L-131-2007` | 55 | 9 | 5 | 4 | 2 | 0 | 5 |
| `L-131-2012` | 41 | 11 | 46 | 27 | 3 | 4 | 5 |
| `L-131-2015` | 91 | 14 | 15 | 120 | 1 | 0 | 9 |
| `L-132-2012` | 52 | 7 | 1 | 6 | 0 | 1 | 2 |
| `L-132-2016` | 45 | 13 | 13 | 27 | 7 | 0 | 4 |
| `L-133-2011` | 36 | 10 | 38 | 18 | 1 | 0 | 2 |
| `L-133-2016` | 27 | 7 | 20 | 28 | 5 | 0 | 2 |
| `L-133-2018` | 17 | 58 | 2 | 0 | 0 | 0 | 42 |
| `L-135-2007` | 93 | 11 | 6 | 17 | 16 | 0 | 2 |
| `L-136-2017` | 48 | 2 | 18 | 13 | 3 | 0 | 1 |
| `L-139-2007` | 59 | 4 | 2 | 36 | 0 | 0 | 3 |
| `L-140-2025` | 24 | 26 | 1 | 0 | 0 | 0 | 1 |
| `L-143-2014` | 54 | 14 | 2 | 58 | 0 | 3 | 18 |
| `L-1456-1993` | 46 | 6 | 3 | 7 | 1 | 2 | 5 |
| `L-148-2023` | 35 | 6 | 16 | 25 | 2 | 0 | 1 |
| `L-149-2006` | 44 | 5 | 2 | 5 | 0 | 1 | 0 |
| `L-149-2012` | 271 | 11 | 13 | 182 | 7 | 9 | 9 |
| `L-1543-1998` | 93 | 17 | 4 | 25 | 6 | 0 | 10 |
| `L-155-2011` | 6 | 0 | 2 | 0 | 0 | 0 | 0 |
| `L-156-2007` | 24 | 2 | 1 | 1 | 1 | 0 | 1 |
| `L-158-2008` | 88 | 51 | 38 | 74 | 10 | 0 | 54 |
| `L-1585-1998` | 25 | 10 | 3 | 4 | 3 | 1 | 6 |
| `L-160-2011` | 32 | 11 | 58 | 12 | 3 | 2 | 9 |
| `L-160-2023` | 58 | 13 | 3 | 47 | 5 | 0 | 7 |
| `L-160-2026` | 46 | 4 | 2 | 54 | 11 | 1 | 1 |
| `L-164-2025` | 151 | 42 | 3 | 351 | 2 | 3 | 61 |
| `L-165-2023` | 31 | 10 | 1 | 4 | 0 | 0 | 5 |
| `L-171-2012` | 158 | 31 | 26 | 154 | 17 | 0 | 24 |
| `L-177-2025` | 4 | 4 | 0 | 0 | 0 | 0 | 0 |
| `L-178-2020` | 8 | 7 | 0 | 0 | 0 | 0 | 2 |
| `L-179-2008` | 56 | 11 | 2 | 16 | 4 | 0 | 5 |
| `L-179-2016` | 23 | 4 | 5 | 5 | 0 | 0 | 2 |
| `L-181-2014` | 86 | 28 | 41 | 30 | 3 | 1 | 25 |
| `L-181-2023` | 50 | 19 | 3 | 13 | 24 | 1 | 9 |
| `L-183-2012` | 110 | 28 | 11 | 183 | 8 | 4 | 14 |
| `L-183-2016` | 17 | 6 | 7 | 8 | 3 | 0 | 1 |
| `L-19-2016` | 26 | 18 | 7 | 21 | 0 | 0 | 24 |
| `L-192-1998` | 34 | 20 | 18 | 21 | 8 | 1 | 1 |
| `L-195-2024` | 90 | 20 | 11 | 200 | 8 | 0 | 5 |
| `L-198-2007` | 54 | 10 | 5 | 38 | 14 | 0 | 11 |
| `L-198-2020` | 64 | 10 | 2 | 23 | 8 | 0 | 3 |
| `L-199-2010` | 29 | 8 | 25 | 2 | 5 | 0 | 2 |
| `L-2-2020` | 46 | 17 | 0 | 29 | 9 | 0 | 10 |
| `L-20-2026` | 29 | 18 | 2 | 16 | 17 | 0 | 9 |
| `L-202-2017` | 155 | 21 | 20 | 247 | 31 | 2 | 10 |
| `L-209-2016` | 91 | 40 | 12 | 236 | 4 | 0 | 49 |
| `L-212-2004` | 56 | 3 | 8 | 6 | 2 | 2 | 2 |
| `L-213-2023` | 10 | 6 | 9 | 5 | 2 | 1 | 3 |
| `L-22-2025` | 55 | 17 | 2 | 54 | 2 | 0 | 18 |
| `L-220-2007` | 44 | 10 | 14 | 14 | 16 | 0 | 5 |
| `L-221-2007` | 59 | 12 | 8 | 7 | 4 | 0 | 9 |
| `L-227-2022` | 60 | 15 | 5 | 44 | 3 | 0 | 12 |
| `L-227-2025` | 42 | 52 | 1 | 0 | 0 | 0 | 19 |
| `L-229-2010` | 35 | 1 | 3 | 1 | 0 | 0 | 1 |
| `L-23-2008` | 36 | 4 | 0 | 6 | 0 | 0 | 3 |
| `L-230-2022` | 123 | 23 | 4 | 145 | 4 | 0 | 28 |
| `L-232-2016` | 344 | 18 | 8 | 238 | 43 | 1 | 8 |
| `L-234-2016` | 37 | 14 | 10 | 30 | 6 | 0 | 7 |
| `L-235-2006` | 21 | 5 | 23 | 1 | 3 | 0 | 1 |
| `L-239-2007` | 43 | 7 | 4 | 4 | 0 | 0 | 4 |
| `L-239-2008` | 20 | 5 | 17 | 0 | 0 | 0 | 1 |
| `L-24-2008` | 42 | 3 | 2 | 31 | 1 | 0 | 2 |
| `L-245-2008` | 41 | 5 | 17 | 9 | 0 | 0 | 2 |
| `L-246-2017` | 20 | 8 | 3 | 6 | 8 | 0 | 2 |
| `L-246-2018` | 97 | 17 | 2 | 17 | 23 | 0 | 6 |
| `L-248-2025` | 56 | 4 | 1 | 1 | 1 | 0 | 0 |
| `L-25-2008` | 17 | 6 | 0 | 4 | 1 | 0 | 0 |
| `L-250-2017` | 23 | 6 | 1 | 14 | 0 | 0 | 4 |
| `L-253-2025` | 44 | 3 | 0 | 18 | 1 | 0 | 1 |
| `L-254-2016` | 23 | 2 | 1 | 10 | 0 | 0 | 1 |
| `L-260-2017` | 40 | 11 | 1 | 5 | 8 | 0 | 1 |
| `L-270-2018` | 38 | 8 | 4 | 6 | 7 | 0 | 5 |
| `L-272-2011` | 84 | 32 | 9 | 49 | 1 | 0 | 26 |
| `L-273-1994` | 12 | 11 | 1 | 19 | 1 | 0 | 7 |
| `L-274-2011` | 35 | 5 | 3 | 12 | 1 | 0 | 5 |
| `L-278-2007` | 44 | 12 | 4 | 21 | 0 | 0 | 8 |
| `L-28-2024` | 63 | 16 | 1 | 8 | 0 | 0 | 13 |
| `L-282-2004` | 22 | 3 | 1 | 0 | 0 | 0 | 0 |
| `L-283-2003` | 46 | 9 | 3 | 13 | 0 | 0 | 5 |
| `L-284-2004` | 29 | 10 | 4 | 4 | 7 | 0 | 3 |
| `L-291-2016` | 57 | 11 | 5 | 13 | 0 | 0 | 8 |
| `L-296-2017` | 24 | 13 | 4 | 12 | 7 | 0 | 19 |
| `L-303-2013` | 46 | 15 | 3 | 12 | 1 | 1 | 11 |
| `L-306-2018` | 38 | 17 | 7 | 6 | 5 | 1 | 15 |
| `L-308-2017` | 47 | 21 | 10 | 65 | 12 | 0 | 14 |
| `L-317-2025` | 20 | 25 | 0 | 0 | 0 | 0 | 3 |
| `L-325-2013` | 28 | 11 | 17 | 41 | 2 | 0 | 7 |
| `L-325-2025` | 91 | 21 | 0 | 168 | 2 | 0 | 14 |
| `L-36-2026` | 4 | 0 | 0 | 0 | 0 | 0 | 0 |
| `L-382-2001` | 29 | 1 | 1 | 0 | 1 | 0 | 0 |
| `L-384-2023` | 16 | 6 | 9 | 15 | 1 | 0 | 2 |
| `L-394-2023` | 29 | 17 | 1 | 58 | 1 | 0 | 28 |
| `L-397-2003` | 37 | 7 | 6 | 14 | 0 | 0 | 5 |
| `L-403-2023` | 59 | 14 | 2 | 89 | 3 | 0 | 18 |
| `L-411-1995` | 72 | 9 | 5 | 5 | 1 | 5 | 6 |
| `L-422-2023` | 107 | 11 | 2 | 429 | 1 | 0 | 9 |
| `L-43-2023` | 38 | 15 | 2 | 53 | 1 | 0 | 20 |
| `L-435-2006` | 17 | 4 | 2 | 0 | 0 | 0 | 3 |
| `L-436-2006` | 98 | 29 | 9 | 16 | 14 | 0 | 19 |
| `L-439-1995` | 50 | 5 | 4 | 5 | 0 | 0 | 2 |
| `L-461-2001` | 30 | 11 | 3 | 6 | 0 | 0 | 6 |
| `L-488-1999` | 24 | 3 | 11 | 14 | 1 | 1 | 5 |
| `L-514-1995` | 60 | 12 | 0 | 4 | 0 | 0 | 7 |
| `L-52-2014` | 41 | 10 | 2 | 8 | 5 | 0 | 4 |
| `L-523-1999` | 18 | 4 | 0 | 1 | 0 | 0 | 2 |
| `L-548-1995` | 91 | 34 | 18 | 40 | 22 | 4 | 13 |
| `L-550-1995` | 20 | 9 | 8 | 18 | 16 | 1 | 2 |
| `L-595-1999` | 32 | 4 | 16 | 14 | 1 | 2 | 2 |
| `L-599-1999` | 399 | 11 | 1 | 97 | 1 | 0 | 10 |
| `L-62-2008` | 73 | 11 | 14 | 71 | 10 | 1 | 4 |
| `L-62-2022` | 58 | 25 | 10 | 37 | 4 | 0 | 10 |
| `L-64-2010` | 34 | 2 | 4 | 5 | 1 | 0 | 0 |
| `L-66-2017` | 17 | 17 | 0 | 0 | 0 | 0 | 11 |
| `L-67-2024` | 35 | 13 | 2 | 34 | 0 | 2 | 10 |
| `L-68-2013` | 23 | 19 | 1 | 5 | 1 | 0 | 18 |
| `L-69-2016` | 70 | 4 | 1 | 18 | 0 | 0 | 2 |
| `L-71-2007` | 33 | 3 | 8 | 0 | 0 | 0 | 3 |
| `L-72-2025` | 127 | 52 | 3 | 407 | 24 | 0 | 52 |
| `L-764-2001` | 26 | 3 | 5 | 0 | 1 | 0 | 3 |
| `L-768-2000` | 28 | 6 | 2 | 0 | 4 | 0 | 2 |
| `L-797-1996` | 160 | 10 | 1 | 37 | 8 | 0 | 8 |
| `L-80-2010` | 30 | 7 | 8 | 7 | 6 | 0 | 2 |
| `L-82-2017` | 51 | 16 | 8 | 14 | 4 | 0 | 6 |
| `L-82-2024` | 98 | 25 | 1 | 317 | 15 | 0 | 28 |
| `L-845-1992` | 46 | 14 | 5 | 12 | 4 | 0 | 3 |
| `L-852-2002` | 2 | 10 | 1 | 0 | 4 | 2 | 8 |
| `L-86-2014` | 42 | 17 | 17 | 67 | 0 | 5 | 16 |
| `L-9-2026` | 63 | 13 | 0 | 27 | 5 | 0 | 5 |
| `L-92-2014` | 61 | 19 | 4 | 31 | 1 | 0 | 23 |
| `L-92-2022` | 125 | 17 | 7 | 61 | 6 | 0 | 7 |
| `L-93-1998` | 19 | 4 | 3 | 4 | 1 | 0 | 3 |
| `L-98-2012` | 38 | 9 | 15 | 3 | 1 | 0 | 1 |
| `OCNPDCP-03-1-2013` | 0 | 7 | 0 | 0 | 5 | 0 | 12 |
| `OCNPDCP-03-2015` | 0 | 6 | 0 | 0 | 4 | 0 | 13 |
| `OCNPDCP-27-2022` | 0 | 3 | 0 | 0 | 4 | 0 | 2 |
| `OCNPDCP-31-2026` | 0 | 2 | 0 | 0 | 13 | 0 | 1 |
| `OCNPDCP-31-2026-PROIECT` | 0 | 1 | 0 | 0 | 14 | 1 | 0 |
| `OCNPDCP-38-2026` | 0 | 1 | 0 | 0 | 3 | 0 | 0 |
| `OCNPDCP-39-2026` | 0 | 2 | 0 | 0 | 10 | 0 | 0 |
| `OCNPDCP-40-2026` | 0 | 3 | 0 | 0 | 4 | 0 | 0 |
| `OCNPDCP-48-2026` | 0 | 4 | 0 | 0 | 13 | 0 | 0 |
| `OCNPDCP-POLITIE-2013` | 0 | 9 | 0 | 0 | 5 | 0 | 17 |
| `OCNPDCP-SANATATE` | 0 | 13 | 0 | 0 | 5 | 0 | 48 |
| `UA-COD-DEONTOLOGIC-2016` | 0 | 1 | 0 | 0 | 0 | 0 | 1 |
| `UA-STATUT-2011` | 74 | 9 | 0 | 16 | 1 | 2 | 2 |

## Trimiteri nerezolvate

Articole citate care nu au ancora in actul-tinta, grupate pe tinta. Cauze cunoscute: articolul a fost abrogat si consolidarea a sters ciotul (`L-548-1995` art. 12, 13, 29, 30, 48, 54, 73; CLAUDE.md, intrebarea 6); articolul a fost abrogat si textul care il citeaza n-a fost actualizat; actul-tinta a fost renumerotat (Codul civil in 2019); ancora lipseste din cauza unei greseli de tipar in sursa (`L-100-2017` art. 52; intrebarea 4); exponentul a fost turtit in sursa (`art. 3142` pentru 314^2; intrebarea 2); sau citirea a luat drept articol al acestui act unul al altui act, nenumit in context. Fiecare rind trimite la o linie: deschide-o inainte de a trage o concluzie.

| act-tinta | articol citat | citari | poate fi | regula | exemplu (sursa, linie) | fragment |
|---|---|---:|---|---|---|---|
| `CC-1107-2002` | art. 48^30 | 7 | - | din | `COD-225-2003#art.308^2` l.2707 | de judecată audiază persoanele enumerate la art. 48^30 alin. (1) din Codul civil. (2) Audierea persoanelor indicate la art. |
| `COD-218-2008` | art. 441 | 5 | exponent turtit: art. 44^1 | din | `HG-582-2022#corp` l.94 | rocesul contravențional a încetat în temeiul art. 441 alin. (1) lit. f) din Codul contravențional al Republicii Moldova nr. |
| `L-131-2012` | art. 51 | 5 | exponent turtit: art. 5^1 | intern | `L-131-2012#art.29` l.560 | or încălcări, conform limitelor stabilite la art. 51. (1^1) În cazul prevăzut la art.28 alin.(9), organul respectiv includ |
| `AA-2014` | art. 3 | 4 | - | intern | `AA-2014#preambul` l.32 | ând cu data de 1 septembrie 2014, în temeiul articolului 3 alineatul (1) din Decizia Consiliului privind semnarea și aplicarea c |
| `AA-2014` | art. 7 | 3 | - | intern | `AA-2014#art.465` l.163 | italului inițial prevăzut în conformitate cu articolul 5 alineatele (1) și (3), articolul 6, articolul 7 literele (a), (b) și (c), articolul 8 literele (a), (b) și (c) și arti |
| `CC-1107-2002` | art. 330^4 | 3 | - | din | `COD-225-2003#art.327` l.2902 | rilor de constatare a uzucapiunii în temeiul art. 330^4 din Codul civil şi efectuării înregistrării corespunzătoare în regist |
| `CC-1107-2002` | art. 1575^9 | 3 | - | din | `L-149-2012#art.235^13` l.2437 | asei succesorale de către moștenitor conform art. 1575^9–1575^11 din Codul civil pot fi folosite pentru a satisface creanțele |
| `L-86-2014` | art. 105 | 3 | exponent turtit: art. 10^5 | intern | `L-86-2014#art.10^12` l.469 | entă a acordului de mediu în conformitate cu art. 105 alin. (5). (8) În cazul activităților planificate care nu cad sub inc |
| `AA-2014` | art. 4 | 2 | - | intern | `AA-2014#art.465` l.206 | sare pentru fiecare investitor, prevăzută la articolul 4 din respectiva directivă, sunt puse în aplicare în termen de cinci an |
| `CC-1107-2002` | art. 48^40 | 2 | - | din | `COD-225-2003#art.308^9` l.2738 | oire a măsurii de ocrotire judiciare conform art. 48^40 din Codul civil, instanţa de judecată va pronunţa hotărârea judecător |
| `CC-1107-2002` | art. 1575^4 | 2 | - | din | `L-149-2012#art.235^12` l.2433 | ța ce aparține creditorului care, în temeiul art. 1575^4 din Codul civil, a fost exclus din cadrul procedurii de somare public |
| `CC-1107-2002` | art. 1575^5 | 2 | - | din | `L-149-2012#art.235^12` l.2433 | publică a creditorilor sau care, în temeiul art. 1575^5 din Codul civil, se asimilează creditorului exclus va fi satisfăcută |
| `COD-218-2008` | art. 562 | 2 | exponent turtit: art. 56^2 | intern | `COD-218-2008#art.415` l.6587 | (1) Contravenţiile prevăzute la art. 562 , 563, 242, 366–369, art. 370 alin. (1), art. 371–373^3 se constată de Ministerul Apărării. (2) Sunt în drept să consta |
| `L-1456-1993` | art. 200 | 2 | - | intern | `L-1456-1993#preambul` l.70 | 04.2005 în MONITORUL PARLAMENTULUI Nr. 59-61 art. 200 \| \| Data intrării în vigoare \| 25.05.1993 \| \| Data modificării/datele |
| `L-183-2012` | art. 572 | 2 | exponent turtit: art. 57^2 | intern | `L-183-2012#art.47` l.795 | lui Consiliului Concurenței emisă în temeiul art. 572 alin. (1) pot fi contestate, în conformitate cu prevederile Codului a |
| `L-212-2004` | art. 17 | 2 | - | din | `L-108-2016#art.105^1` l.2255 | larării stării de urgență în conformitate cu art. 17–19 din Legea nr. 212/2004 privind regimul stării de urgență, de asedi |
| `L-212-2004` | art. 20 | 2 | - | intern | `L-212-2004#art.42` l.267 | asediu, suplimentar la măsurile prevăzute la art.20, pot fi luate următoarele măsuri: a) închiderea frontierei de stat a |
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
| `CETS-223-2018` | art. 44 | 1 | - | intern | `CETS-223-2018#preambul` l.69 | deja făcută în [ ] cu art. 44-50 GDPR. Protocolul de amendare a Convenției pentru pro |
| `COD-116-2018` | art. 17^1 | 1 | - | din | `L-192-1998#art.23` l.376 | te. d) - abrogată; (1^2) Prin derogare de la art. 17^1 alin.(4) din Codul administrativ nr. 116/2018, depunerea unei cereri |
| `COD-116-2018` | art. 2451 | 1 | exponent turtit: art. 245^1 | intern | `COD-116-2018#art.247` l.1742 | epția recursului în care se invocă întemeiat art. 2451 alin. (1) lit. b) și d). Completul poate decide și în alte cazuri inv |
| `COD-1163-1997` | art. 29^1 | 1 | - | intern | `COD-1163-1997#art.292` l.6945 | art. 295 lit. g^1), achită taxa stipulată la art. 29^1 alin.(1) lit.e), anual, în termen de până la data de 25 martie a anul |
| `COD-122-2003` | art. 181^1 | 1 | - | intern | `COD-122-2003#art.269` l.3855 | în privința infracțiunilor prevăzute la: a) art. 181^1–181^3, 239–240, 243, art. 244 alin. (3)–(5) doar pentru faptele prevăzute la alin. (3) și (4), art. |
| `COD-122-2003` | art. 185^2 | 1 | - | intern | `COD-122-2003#art.276` l.3997 | tru săvârșirea unor infracţiuni prevăzute la art. 185^2, cu excepţia infracţiunilor prevăzute la alin. (2^3), şi la art. 185^ |
| `COD-150-2014` | art. 622 | 1 | exponent turtit: art. 62^2 | din | `COD-218-2008#art.197` l.3383 | ransport rutier, a obligațiilor prevăzute la art. 23 alin. (8), art. 48, 49, 79, art. 3126 alin. (4), art. 3136 alin. (5), art. 3142 alin. (3), art. 622 alin. (1) din Codul tr |
| `COD-150-2014` | art. 3126 | 1 | exponent turtit: art. 31^26 | din | `COD-218-2008#art.197` l.3383 | ransport rutier, a obligațiilor prevăzute la art. 23 alin. (8), art. 48, 49, 79, art. 3126 alin. (4), art. 3136 alin. (5), art. 3142 alin. (3), art. 622 alin. (1) din Codul tr |
| `COD-150-2014` | art. 3136 | 1 | exponent turtit: art. 31^36 | din | `COD-218-2008#art.197` l.3383 | ransport rutier, a obligațiilor prevăzute la art. 23 alin. (8), art. 48, 49, 79, art. 3126 alin. (4), art. 3136 alin. (5), art. 3142 alin. (3), art. 622 alin. (1) din Codul tr |
| `COD-150-2014` | art. 3142 | 1 | exponent turtit: art. 31^42 | din | `COD-218-2008#art.197` l.3383 | ransport rutier, a obligațiilor prevăzute la art. 23 alin. (8), art. 48, 49, 79, art. 3126 alin. (4), art. 3136 alin. (5), art. 3142 alin. (3), art. 622 alin. (1) din Codul tr |
| `COD-218-2008` | art. 5^1 | 1 | - | intern | `COD-218-2008#art.440` l.7012 | zător se efectuează în limitele stabilite la art. 4 alin.(10) și art. 5^1din legea menționată. (5) Dacă la depistarea sau la examinarea cazului |
| `COD-218-2008` | art. 13^1 | 1 | - | modificare | `COD-434-2023#art.389` l.4138 | rile ulterioare, va avea următorul cuprins: „Articolul 13^1. Misiunile diplomatice pot procura sau obține prin schimb terenuri și |
| `COD-218-2008` | art. 52^2 | 1 | - | intern | `COD-218-2008#art.293^2` l.4879 | e plată și moneda electronică a prevederilor art. 50 alin. (1)–(5) și (7), art. 52^1 alin. (5), art. 52^2 alin. (1) și (2), art. 53 alin. (3), (4), (6) și (7), art. 55 alin. ( |
| `COD-218-2008` | art. 60^1 | 1 | - | intern | `COD-218-2008#art.293^2` l.4879 | e plată și moneda electronică a prevederilor art. 50 alin. (1)–(5) și (7), art. 52^1 alin. (5), art. 52^2 alin. (1) și (2), art. 53 alin. (3), (4), (6) și (7), art. 55 alin. ( |
| `COD-218-2008` | art. 641 | 1 | exponent turtit: art. 64^1 | intern | `COD-218-2008#art.409^2` l.6554 | (1) Contravențiile prevăzute la art.641, 642, 327^3 se constată de către Inspectoratul Social de Stat. (2) Su |
| `COD-225-2003` | art. 48^15 | 1 | - | intern | `COD-225-2003#art.308^17` l.2789 | u controlul executării mandatului, în sensul art. 48^15 alin. (3), şi de către persoanele ale căror drepturi sunt afectate pr |
| `COD-225-2003` | art. 581 | 1 | exponent turtit: art. 58^1 | din | `CC-1107-2002#art.113` l.952 | ori din oficiu. (3) În cazurile prevăzute la art. 581 din Codul de procedură civilă, curatorul special sau tutorele special |
| `COD-246-2024` | art. 251 | 1 | - | intern | `COD-246-2024#preambul` l.82 | te care fac obiectul procedurii prevăzute la articolul 251 din tratat, în ceea ce privește procedura de reglementare cu control |
| `COD-259-2004` | art. 117 | 1 | - | din | `L-114-2014#art.37` l.431 | 2) lit. i), secţiunea 1 a capitolului VII şi art. 117 alin. (3) din Codul cu privire la ştiinţă şi inovare al Republicii Mo |
| `L-10-2016` | art. 395 | 1 | exponent turtit: art. 39^5 | din | `L-164-2025#art.125` l.2461 | energie din surse regenerabile prevăzute la art. 395 din Legea nr. 10/2016 privind promovarea utilizării energiei din surs |
| `L-105-2003` | art. 201 | 1 | - | din | `COD-218-2008#art.273` l.4540 | locului de preschimbare a mărfii prevăzut la art. 201 din Legea nr. 105/2003 privind protecția consumatorilor, lipsa inform |
| `L-1125-2002` | art. 1756 | 1 | - | intern | `L-1125-2002#art.45` l.268 | a) exceptarea prevăzută de art.1756 alin.(2) enunțul al doilea din Codul civil în redacția introdusă prin |
| `L-114-2014` | art. 82 | 1 | - | intern | `L-114-2014#art.37` l.431 | trării în vigoare a prezentei legi se abrogă art. 82 alin. (2) lit. i), secţiunea 1 a capitolului VII şi art. 117 alin. (3 |
| `L-131-2012` | art. 191 | 1 | exponent turtit: art. 19^1 | din | `L-160-2011#art.11^1` l.380 | permisiv în modul și termenele stabilite la art. 191 din Legea nr. 131/2012 privind controlul de stat asupra activităţii d |
| `L-143-2014` | art. 37 | 1 | - | paranteza | `L-143-2014#preambul` l.95 | alin. (2) paragraful întâi și alin. (3)–(5), art. 14–21, art. 23–29, art. 31, art. 32 alin. (2) și (4), art. 33–35, art. 37 paragraful al doilea, art. 38 alin. (1) și (3), art |
| `L-143-2014` | art. 38 | 1 | - | intern | `L-143-2014#preambul` l.95 | ), art. 33–35, art. 37 paragraful al doilea, art. 38 alin. (1) și (3), art. 39 alin. (1) paragrafele întâi și al doilea, alin. (2)–(5) și (8), art. |
| `L-143-2014` | art. 39 | 1 | - | intern | `L-143-2014#preambul` l.95 | ), art. 33–35, art. 37 paragraful al doilea, art. 38 alin. (1) și (3), art. 39 alin. (1) paragrafele întâi și al doilea, alin. (2)–(5) și (8), art. |
| … inca 43 grupuri, in JSON | | | | | | |

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

