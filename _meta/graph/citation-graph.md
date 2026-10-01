# Graful de citare al actelor detinute

Generat 2026-10-01 08:13 de `_meta/graph/build_citation_graph.py`. Nu edita de mina; se reface rulind scriptul. Datele: `citation-graph.json` in acelasi folder.

**Ce este.** Trimiterile dintre actele detinute, extrase mecanic din textul brut: fiecare muchie poarta fisierul si liniile din care a fost citita, si nicio muchie nu este dedusa. Graful nu se citeaza. El spune unde sa deschizi fisierul, iar ancora se citeste.

**Regula de folosire.** Inainte de a cita un articol, cauta-l in tabelul „Dispozitii cu stare speciala si cine le citeaza”: daca apare, fie el, fie o dispozitie de care depinde nu se aplica astazi asa cum sta in text. Inainte de a ingera un act, citeste „Coada de ingerare”: acolo sint actele pe care textele detinute le citeaza si vault-ul nu le are.

## Numere

| | |
|---|---:|
| acte primare detinute (din care ancorate pe articole) | 343 (281) |
| dispozitii (noduri-articol) | 22654 |
| extrase UE detinute (noduri-tinta) | 51 |
| acte citate si nedetinute (noduri externe) | 1096 |
| mentiuni de acte in text (din care ale actului insusi) | 10044 (1103) |
| muchii act -> act (agregate pe segment-sursa) | 6646 |
| trimiteri la articole citite (in grupuri de enumerare) | 17196 (15324) |
|   rezolvate in actul curent | 13988 |
|   rezolvate in alt act detinut | 2348 |
|   nerezolvate: articolul nu are ancora in actul-tinta | 202 |
|   catre acte nedetinute (notate pe muchia act -> act) | 512 |
|   catre acte pe puncte (fara articole) | 97 |
|   autoreferinte (articolul se citeaza pe sine), ignorate | 49 |
| muchii articol -> articol (agregate) | 13033 |
| muchii articol -> act nerezolvate (agregate) | 188 |

Regula care a dat actul-tinta, pe trimiteri: din 2736, doua-puncte 46, intern 13578, modificare 123, paranteza 55. „intern” = niciun act in context, deci actul curent; „din” = `art. N ... din Legea X` sau `(art. N, M) Directiva X`; „paranteza” = `Legea X (art. N)`; „doua-puncte” = `din Codul X: art. N, M`; „modificare” = `Legea X se modifica dupa cum urmeaza: ... articolul N`. `din legea indicata` trimite la ultima lege numita in acelasi segment.

Coduri citate si pe nume si pe numar, unite dupa textul care le scrie impreuna: COD-apelor = COD-1532-1993; COD-audiovizualului = COD-260-2006; COD-educatiei = COD-152-2014; COD-electoral = COD-325-2022; COD-familiei = COD-1316-2000; COD-jurisdictiei-constitutionale = COD-502-1995; COD-subsolului = COD-3-2009; COD-transporturilor-rutiere = COD-150-2014.

## Coada de ingerare

Actele pe care textele detinute le citeaza si care nu sint in vault, in ordinea numarului de mentiuni. Un act citat de multe acte detinute inchide mai multe lanturi de trimitere decit unul citat des dintr-un singur loc; coloana a treia este cea care conteaza pentru ordinea de ingerare. Graful nu stie daca un act citat mai este in vigoare: o lege abrogata ramine citata de textele care n-au fost actualizate, si apare aici la fel ca una in vigoare.

### Acte moldovenesti citate pe numar

Legi, coduri si hotariri de Guvern identificate prin numar si an.

| act citat | mentiuni | acte care il citeaza | cel mai des din | articole citate |
|---|---:|---:|---|---|
| `L-443-1995` Legea nr. 443/1995 | 9 | 1 | `L-158-2008` (9) | art. 6, art. 8 |
| `L-270-2008` Legea nr. 270/2008 | 8 | 3 | `L-200-2010` (4) | - |
| `COD-navigatiei-maritime-comerciale` Codului navigației maritime comerciale | 7 | 4 | `L-599-1999` (4) | - |
| `HG-1467-2016` Hotarirea Guvernului nr. 1467/2016 | 7 | 1 | `L-108-2020` (7) | - |
| `HG-561-2020` Hotarirea Guvernului nr. 561/2020 | 7 | 1 | `L-209-2016` (7) | art. 54^1 |
| `L-116-2012` Legea nr. 116/2012 | 7 | 1 | `L-151-2022` (7) | art. 14 |
| `L-151-2014` Legea nr. 151/2014 | 6 | 1 | `L-139-2018` (6) | - |
| `L-306-2023` Legea nr. 306/2023 | 6 | 1 | `L-139-2018` (6) | - |
| `L-81-2025` Legea nr. 81/2025 | 6 | 1 | `L-72-2025` (6) | - |
| `L-392-1999` Legea nr. 392/1999 | 5 | 2 | `HCNPF-14-5-2016` (4) | - |
| `L-231-2006` Legea nr. 231/2006 | 5 | 1 | `L-221-2007` (5) | art. 9 |
| `L-28-2016` Legea nr. 28/2016 | 5 | 1 | `L-72-2025` (5) | - |
| `L-1432-2000` Legea nr. 1432/2000 | 4 | 2 | `L-847-2002` (2) | - |
| `L-163-2007` Legea nr. 163/2007 | 4 | 2 | `L-199-1998` (3) | - |
| `L-237-2023` Legea nr. 237/2023 | 4 | 2 | `L-82-2024` (2) | - |
| `L-263-2005` Legea nr. 263/2005 | 4 | 2 | `OCNPDCP-SANATATE` (3) | art. 12 |
| `HG-1315-2004` Hotarirea Guvernului nr. 1315/2004 | 4 | 1 | `HG-657-2009` (4) | - |
| `L-123-2025` Legea nr. 123/2025 | 4 | 1 | `L-19-2016` (4) | art. 4, art. 5 |
| `L-371-2006` Legea nr. 371/2006 | 4 | 1 | `COD-122-2003` (4) | art. 113^1 |
| `L-48-2017` Legea nr. 48/2017 | 4 | 1 | `COD-122-2003` (4) | art. 9^1 |
| `HG-1076-2010` Hotarirea Guvernului nr. 1076/2010 | 3 | 3 | `L-108-2020` (1) | - |
| `HG-296-2012` Hotarirea Guvernului nr. 296/2012 | 3 | 3 | `OCNPDCP-SANATATE` (1) | - |
| `L-1216-1992` Legea nr. 1216/1992 | 3 | 3 | `L-213-2023` (1) | - |
| `L-125-2007` Legea nr. 125/2007 | 3 | 3 | `L-299-2022` (1) | - |
| `L-128-2014` Legea nr. 128/2014 | 3 | 3 | `L-282-2023` (1) | - |
| `L-1384-2002` Legea nr. 1384/2002 | 3 | 3 | `COD-3-2009` (1) | - |
| `L-173-1994` Legea nr. 173/1994 | 3 | 3 | `L-108-2016` (1) | - |
| `L-209-2018` Legea nr. 209/2018 | 3 | 3 | `L-548-1995` (1) | - |
| `L-289-2004` Legea nr. 289/2004 | 3 | 3 | `L-308-2017` (1) | art. 4, art. 5 |
| `L-61-2007` Legea nr. 61/2007 | 3 | 3 | `L-271-2017` (1) | - |
| … inca 551 in JSON | | | | |

### Acte UE citate si neextrase

Directive si regulamente UE care nu au un extras `UE-*` in `raw/papers/cnpf/`.

| act citat | mentiuni | acte care il citeaza | cel mai des din | articole citate |
|---|---:|---:|---|---|
| `EU-TFUE` Tratatul privind functionarea Uniunii Europene | 22 | 7 | `HG-497-2026` (13) | art. 101, art. 107, art. 108, art. 191 |
| `EU-L-1995-46` Directiva 1995/46 | 7 | 5 | `DCNPDCP-41-2026` (3) | - |
| `EU-L-2012-27` Directiva 2012/27 | 6 | 4 | `L-139-2018` (3) | - |
| `EU-L-2014-23` Directiva 2014/23 | 6 | 4 | `L-22-2025` (2) | art. 1, art. 2, art. 6, art. 7 |
| `EU-L-2013-36` Directiva 2013/36 | 6 | 2 | `L-180-2026` (5) | - |
| `EU-R-2010-1093` Regulamentul (UE) nr. 1093/2010 | 6 | 2 | `L-180-2026` (5) | - |
| `EU-R-2001-539` Regulamentul (UE) nr. 539/2001 | 6 | 1 | `L-200-2010` (6) | - |
| `EU-L-2005-60` Directiva 2005/60 | 5 | 4 | `AA-2014` (2) | - |
| `EU-R-2019-1243` Regulamentul (UE) 2019/1243 | 5 | 4 | `L-153-2025` (2) | - |
| `EU-R-2004-2006` Regulamentul (UE) nr. 2006/2004 | 5 | 3 | `L-105-2003` (3) | - |
| `EU-L-2003-6` Directiva 2003/6 | 5 | 1 | `AA-2014` (5) | - |
| `EU-R-2004-852` Regulamentul (UE) nr. 852/2004 | 5 | 1 | `L-296-2017` (5) | - |
| `EU-L-2004-48` Directiva 2004/48 | 4 | 4 | `L-66-2008` (1) | - |
| `EU-L-2018-843` Directiva 2018/843 | 4 | 4 | `L-92-2022` (1) | - |
| `EU-R-2008-765` Regulamentul (UE) nr. 765/2008 | 4 | 4 | `L-7-2016` (1) | art. 2 |
| `EU-L-1978-660` Directiva 1978/660 | 4 | 3 | `AA-2014` (2) | - |
| `EU-L-1979-117` Directiva 1979/117 | 4 | 3 | `L-403-2023` (2) | art. 1, art. 2, art. 3, art. 4 |
| `EU-L-1994-22` Directiva 1994/22 | 4 | 3 | `COD-246-2024` (2) | - |
| `EU-L-2006-70` Directiva 2006/70 | 4 | 3 | `AA-2014` (2) | - |
| `EU-R-2009-1060` Regulamentul (UE) nr. 1060/2009 | 4 | 3 | `L-171-2012` (2) | art. 2, art. 3, art. 4, art. 6 |
| … inca 380 in JSON | | | | |

### Legi citate doar pe nume, fara corespondent in vault

Fara numar in text si fara un titlu detinut care sa le contina, deci identificate numai prin primele cuvinte; acelasi act poate aparea sub doua forme flexionate. Orientativ.

| act citat | mentiuni | acte care il citeaza | cel mai des din | articole citate |
|---|---:|---:|---|---|
| `LEGE:protectia-datelor-cu-caracter` Legea privind protecția datelor cu caracter personal | 72 | 11 | `OCNPDCP-SANATATE` (27) | art. 3 (x5), art. 4 (x5), art. 29 (x4), art. 5 (x3) |
| `LEGE:energetica` Legea cu privire la energetică | 16 | 2 | `L-108-2016` (8) | - |
| `LEGE:privind` Legea privind | 11 | 7 | `L-1134-1997` (4) | - |
| `LEGE:protectia-datelor-eu-caracter` Legea privind protecția datelor eu caracter personal | 10 | 1 | `OCNPDCP-SANATATE` (10) | art. 4, art. 5, art. 12, art. 29 |
| `LEGE:contabilitatii` Legea contabilităţii | 8 | 5 | `L-139-2007` (2) | - |
| `LEGE:energia-electrica` Legea cu privire la energia electrică | 7 | 1 | `L-10-2016` (7) | art. 88 |
| `LEGE:mediere` Legea cu privire la mediere | 6 | 3 | `COD-225-2003` (2) | - |
| `LEGE:avocatura` Legea cu privire la avocatură | 6 | 2 | `L-198-2007` (5) | - |
| `LEGE:asigurarea-cu-pensii-de` Legea cu privire la asigurarea cu pensii | 6 | 1 | `L-156-1998` (6) | - |
| `LEGE:serviciului-public` Legea serviciului public | 6 | 1 | `L-158-2008` (6) | art. 33 |
| `LEGE:statutul-municipiului` Legea privind statutul municipiului | 6 | 1 | `L-436-2006` (6) | - |
| `LEGE:cetateniei` Legea cetățeniei | 4 | 4 | `L-273-1994` (1) | art. 18, art. 23 |
| `LEGE:energetica-si-in-actele` Legea cu privire la energetică şi în | 4 | 2 | `L-108-2016` (2) | - |
| `LEGE:protectia-martorilor-si-altor` Legea cu privire la protecţia martorilor şi | 4 | 2 | `COD-122-2003` (3) | - |
| `LEGE:achizitiile-publice` Legea privind achiziţiile publice | 3 | 3 | `L-74-2020` (1) | - |
| … inca 100 in JSON | | | | |

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
| `UE-2008-48` | 1 | `L-202-2013` (1) |
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
| `UE-2015-849` | 5 | `L-308-2017` (2), `L-106-2022` (1), `L-75-2020` (1), `L-92-2022` (1) |
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
| `UE-2023-1114` | 40 | `L-180-2026` (40) |
| `UE-2023-2225` | 0 | - |
| `UE-2024-1620` | 0 | - |
| `UE-2024-1624` | 0 | - |
| `UE-2024-1640` | 0 | - |
| `UE-2025-1382` | 0 | - |
| `UE-2026-179` | 0 | - |
| `UE-596-2014` | 0 | - |
| `UE-600-2014` | 0 | - |
| `UE-648-2012` | 3 | `L-202-2017` (1), `L-308-2017` (1), `L-75-2020` (1) |
| `UE-648-2012-priority-articles-2026-07-09` | 0 | - |
| `UE-909-2014` | 1 | `L-234-2016` (1) |
| `UE-97-9` | 1 | `AA-2014` (1) |
| `UE-98-26` | 3 | `AA-2014` (1), `L-183-2016` (1), `L-234-2016` (1) |

## Trimiteri catre acte abrogate

Acte detinute care nu mai sint in vigoare, si actele din corpus care trimit la ele. Fiecare trimitere de mai jos citeste astazi text mort. Nu inseamna ca actul care trimite e gresit: inseamna ca trimiterea trebuie citita prin dispozitiile tranzitorii ale actului abrogator, care de regula spune ca trimiterile la legea veche se considera facute la cea noua.

| act abrogat | de la | prin | mentiuni | acte care il citeaza | articole citate |
|---|---|---|---:|---:|---|
| `COD-1149-2000` | 2024-01-01 | CV95 din 24.08.21 | 12 | 5 | art. 1, art. 23, art. 43, art. 45, art. 49^1, art. 50, art. 53, art. 56 |
| `COD-3-2009` | 2026-05-30 | CS246 din 08.11.24 | 9 | 6 | art. 9, art. 14, art. 15, art. 16, art. 19, art. 28, art. 30, art. 32 |
| `HG-1123-2010` | 2024-11-15 | HG678 din 02.10.24 | 6 | 3 | - |
| `HG-1171-2018` | 2026-09-22 | HG497 din 02.09.26 | 2 | 2 | - |
| `L-107-2016` | 2025-08-19 | LP164 din 26.06.25 | 51 | 10 | art. 1, art. 4, art. 7, art. 8, art. 10, art. 11, art. 12, art. 13 |
| `L-1227-1997` | 2023-01-08 | LP62 din 17.03.22 | 4 | 3 | art. 19, art. 28 |
| `L-133-2011` | 2026-08-23 | LP195 din 25.07.24 | 102 | 44 | art. 1, art. 2, art. 4, art. 5, art. 6, art. 12, art. 13, art. 20 |
| `L-137-2015` | 2026-09-12 | LP9 din 12.02.26 | 17 | 8 | art. 5, art. 6, art. 9, art. 13, art. 15, art. 16, art. 19, art. 21 |
| `L-1380-1997` | 2024-01-01 | CV95 din 24.08.21 | 22 | 4 | art. 2, art. 4, art. 7, art. 11, art. 12, art. 15, art. 16, art. 20 |
| `L-139-2010` | 2022-10-09 | LP230 din 28.07.22 | 23 | 11 | art. 5, art. 10, art. 11, art. 12, art. 20, art. 23, art. 24, art. 26 |
| `L-139-2012` | 2027-03-17 (viitoare) | - | 31 | 9 | art. 3, art. 4, art. 10, art. 19 |
| `L-1409-1997` | 2025-08-17 | LP153 din 19.06.25 | 5 | 5 | - |
| `L-142-2008` | 2019-03-01 | LP133 din 15.11.18 | 6 | 3 | art. 10, art. 18, art. 30, art. 31, art. 32, art. 33, art. 33^1, art. 34 |
| `L-163-2010` | 2025-01-30 | CUC434 din 28.12.23 | 17 | 4 | art. 1, art. 4, art. 12, art. 17, art. 28, art. 28^1 |
| `L-17-2007` | 2012-04-14 | LP133 din 08.07.11 | 5 | 3 | art. 14 |
| `L-182-2008` | 2026-08-23 | LP195 din 25.07.24 | 9 | 7 | - |
| `L-199-1998` | 2015-03-14 | LP171 din 11.07.12 | 8 | 3 | art. 3, art. 9, art. 14, art. 21, art. 32, art. 44, art. 53, art. 54 |
| `L-200-2010` | 2027-06-01 (viitoare) | - | 6 | 4 | art. 6, art. 6^1, art. 8, art. 9, art. 10, art. 12, art. 19, art. 21 |
| `L-407-2006` | 2023-01-01 | LP92 din 07.04.22 | 17 | 7 | art. 8, art. 20, art. 21, art. 22, art. 24, art. 24^1, art. 24^6, art. 26 |
| `L-414-2006` | 2023-04-01 | LP106 din 21.04.22 | 14 | 4 | art. 4, art. 5, art. 8, art. 11, art. 14, art. 16, art. 18, art. 18^1 |
| `L-422-2006` | 2026-03-11 | LP196 din 10.07.25 | 16 | 6 | art. 2, art. 3, art. 4, art. 5, art. 6, art. 8 |
| `L-575-2003` | 2023-10-01 | LP160 din 22.06.23 | 10 | 4 | art. 6, art. 9, art. 16, art. 24, art. 25, art. 26, art. 27, art. 43 |
| `L-66-2008` | 2027-04-02 (viitoare) | - | 8 | 5 | art. 5, art. 6, art. 7, art. 8, art. 9, art. 11, art. 12, art. 13 |
| `L-7-2016` | 2024-07-27 | LP162 din 22.06.23 | 6 | 5 | art. 1, art. 5, art. 12, art. 14, art. 15, art. 16, art. 18, art. 19 |
| `L-835-1996` | 2025-01-30 | CUC434 din 28.12.23 | 5 | 3 | art. 13, art. 16, art. 24^1 |
| `L-91-2014` | 2022-12-10 | LP124 din 19.05.22 | 9 | 5 | art. 2, art. 5, art. 6, art. 8, art. 16, art. 26, art. 31, art. 36 |
| `L-982-2000` | 2024-01-08 | LP148 din 09.06.23 | 19 | 13 | art. 7, art. 8, art. 19 |

`COD-1149-2000` este citat din: `COD-95-2021`, `L-172-2014`, `L-440-2001`, `L-66-2017`, `L-7-2016`.

`COD-3-2009` este citat din: `COD-246-2024`, `COD-434-2023`, `L-107-2025`, `L-151-2022`, `L-209-2016`, `L-317-2025`.

`HG-1123-2010` este citat din: `OCNPDCP-03-1-2013`, `OCNPDCP-POLITIE-2013`, `OCNPDCP-SANATATE`.

`HG-1171-2018` este citat din: `HG-497-2026`, `HG-610-2018`.

`L-107-2016` este citat din: `COD-116-2018`, `COD-1163-1997`, `L-10-2016`, `L-108-2016`, `L-139-2018`, `L-164-2025`, `L-174-2017`, `L-174-2021`, `L-74-2020`, `L-92-2014`.

`L-1227-1997` este citat din: `COD-174-2018`, `L-171-2012`, `L-62-2022`.

`L-133-2011` este citat din: `COD-122-2003`, `COD-150-2014`, `COD-218-2008`, `COD-95-2021`, `DCNPDCP-08-2023`, `DCNPDCP-581-2015`, `DCNPDCP-PARTIDE-2014`, `DCU-REGULI-2026`, `HCNPF-14-5-2016`, `HG-310-2025`, `L-102-2017`, `L-105-2003`, `L-105-2018`, `L-107-2016`, `L-114-2012`, `L-122-2008`, `L-132-2016`, `L-139-2018`, `L-153-2025`, `L-1543-1998`, `L-165-2023`, `L-171-2012`, `L-181-2023`, `L-182-2008`, `L-195-2024`, `L-202-2017`, `L-246-2018`, `L-28-2024`, `L-284-2004`, `L-308-2017`, `L-325-2013`, `L-325-2025`, `L-36-2016`, `L-384-2023`, `L-436-2006`, `L-548-1995`, `L-59-2012`, `L-71-2007`, `L-72-2025`, `OCNPDCP-03-1-2013`, `OCNPDCP-03-2015`, `OCNPDCP-39-2026`, `OCNPDCP-POLITIE-2013`, `OCNPDCP-SANATATE`.

`L-137-2015` este citat din: `COD-225-2003`, `L-105-2003`, `L-198-2007`, `L-213-2023`, `L-23-2008`, `L-231-2010`, `L-24-2008`, `L-9-2026`.

`L-1380-1997` este citat din: `COD-1149-2000`, `COD-95-2021`, `L-172-2014`, `L-60-2012`.

`L-139-2010` este citat din: `DCU-PROC-COMISIOANE`, `DCU-PROC-DECONTARE`, `DCU-PROC-DETINATOR`, `DCU-PROC-GARANTII`, `DCU-PROC-INREGISTRARE-VM`, `DCU-PROC-INSOLVABILITATE`, `DCU-PROC-PARTICIPANT`, `DCU-PROC-RECLAMATII`, `DCU-PROC-RECONCILIERE`, `DCU-REGULI-2026`, `L-230-2022`.

`L-139-2012` este citat din: `COD-325-2022`, `HG-574-2024`, `L-10-2016`, `L-116-2014`, `L-139-2018`, `L-164-2025`, `L-183-2012`, `L-232-2016`, `L-92-2014`.

`L-1409-1997` este citat din: `DCA-61-2024`, `L-119-2018`, `L-153-2025`, `L-277-2018`, `L-394-2023`.

`L-142-2008` este citat din: `COD-443-2004`, `L-1125-2002`, `L-133-2018`.

`L-163-2010` este citat din: `COD-434-2023`, `L-107-2016`, `L-187-2022`, `L-835-1996`.

`L-17-2007` este citat din: `HG-1123-2010`, `L-133-2011`, `L-182-2008`.

`L-182-2008` este citat din: `DCNPDCP-08-2023`, `DCNPDCP-581-2015`, `DCNPDCP-PARTIDE-2014`, `L-195-2024`, `OCNPDCP-03-1-2013`, `OCNPDCP-03-2015`, `OCNPDCP-POLITIE-2013`.

`L-199-1998` este citat din: `L-1125-2002`, `L-133-2018`, `L-171-2012`.

`L-200-2010` este citat din: `COD-218-2008`, `L-105-2018`, `L-1585-1998`, `L-489-1999`.

`L-407-2006` este citat din: `HCNPF-14-5-2016`, `L-1134-1997`, `L-133-2018`, `L-178-2020`, `L-202-2017`, `L-250-2017`, `L-92-2022`.

`L-414-2006` este citat din: `COD-218-2008`, `L-106-2022`, `L-178-2020`, `L-407-2006`.

`L-422-2006` este citat din: `COD-434-2023`, `L-10-2009`, `L-143-2014`, `L-162-2023`, `L-196-2025`, `L-7-2016`.

`L-575-2003` este citat din: `L-160-2023`, `L-202-2017`, `L-548-1995`, `L-550-1995`.

`L-66-2008` este citat din: `COD-218-2008`, `L-107-2026`, `L-1100-2000`, `L-279-2017`, `L-57-2006`.

`L-7-2016` este citat din: `COD-434-2023`, `L-151-2022`, `L-162-2023`, `L-19-2016`, `L-420-2006`.

`L-835-1996` este citat din: `COD-434-2023`, `L-1543-1998`, `L-163-2010`.

`L-91-2014` este citat din: `HBN-127-2013`, `L-124-2022`, `L-151-2022`, `L-467-2003`, `L-66-2017`.

`L-982-2000` este citat din: `COD-443-2004`, `HG-411-2022`, `HG-967-2016`, `L-133-2011`, `L-148-2023`, `L-162-2023`, `L-239-2008`, `L-246-2018`, `L-306-2018`, `L-74-2020`, `L-82-2017`, `OCNPDCP-03-2015`, `OCNPDCP-POLITIE-2013`.

Limita care ramine: pentru actele **nedetinute** din coada de ingerare graful tot nu stie daca mai sint in vigoare. Se afla numai deschizind fisa lor pe legis.md, si nici acolo cimpul „Data abrogarii” nu este de incredere: pentru `L-133-2011` el era gol, desi corpul consolidarii declara abrogarea.

## Dispozitii cu stare speciala si cine le citeaza

Dispozitiile care apar in registrul in-force (textul din fisier nu se aplica inca), in registrul HCC (declarate neconstitutionale, in tot sau in parte) sau al caror titlu spune „abrogat”, si muchiile articol -> articol care intra in ele. Un articol din coloana „citat din” depinde de o dispozitie care nu sta in picioare asa cum e scrisa. Numai dispozitiile cu cel putin o citare intra aici, intii cele citate din alte acte; toate starile sint in JSON.

| dispozitie | stare | citari (din alte acte) | citat din |
|---|---|---:|---|
| `L-440-2001#art.6` l.209 | HCC: HCC3/2012-02-09, alin. (2^1), text din articol | 5 (5) | `COD-1163-1997#art.49` l.2203, `L-57-2006#art.3` l.188 |
| `COD-1163-1997#art.123` l.3751 | HCC: HCC17/2014-05-29, alin. (7), subunitate | 5 (4) | `L-1100-2000#art.20`, `COD-1163-1997#art.262`, `L-1100-2000#art.4`, `L-1100-2000#art.5` |
| `L-60-2012#art.49` l.582 | HCC: HCC3/2022-02-24, al.(4), text din articol | 4 (4) | `COD-1149-2000#art.20`, `COD-1163-1997#art.124`, `COD-218-2008#art.232^1`, `L-1380-1997#art.28` |
| `L-548-1995#art.11` l.294 | HCC: HCC31/2013-10-01, al.(4), articol intreg | 7 (3) | `L-548-1995#art.75^1`, `L-114-2012#art.98`, `L-202-2017#art.144`, `L-232-2016#art.319`, `L-548-1995#art.6` |
| `L-278-2007#art.26` l.498 | in-force: nespecificat de la 2027-03-01 | 3 (3) | `COD-218-2008#art.91^1` l.2002, `L-320-2012#art.25` l.352 |
| `COD-122-2003#art.191` l.3019 | HCC: HCC17/2016-05-19, omisiune legislativa (+1) | 5 (2) | `COD-443-2004#art.301`, `COD-122-2003#art.192`, `COD-122-2003#art.309`, `COD-122-2003#art.310` |
| `COD-122-2003#art.273` l.3945 | HCC: HCC29/2021-09-21, alin. (1) lit. d^2), in parte | 4 (2) | `COD-1149-2000#art.189^3`, `COD-122-2003#art.166`, `COD-122-2003#art.215^2`, `COD-443-2004#art.245` |
| `COD-218-2008#art.34` l.1025 | HCC: HCC7/2018-04-26, alin. (3), text din articol | 3 (2) | `COD-443-2004#art.315` l.3242, `COD-218-2008#art.293^2` l.4877 |
| `L-163-2010#art.28^1` l.422 | abrogat | 2 (2) | `COD-434-2023#art.389` l.4152 |
| `COD-225-2003#art.449` l.3638 | HCC: HCC16/2013-06-25, lit. f), in parte | 12 (1) | `COD-225-2003#art.450`, `COD-116-2018#art.170`, `COD-225-2003#art.447`, `COD-225-2003#art.451`, `COD-225-2003#art.451^1`, `COD-225-2003#art.453` |
| `COD-225-2003#art.267` l.2173 | HCC: HCC33/2016-11-17, lit. b), in parte | 7 (1) | `COD-225-2003#art.268`, `COD-225-2003#art.185`, `COD-225-2003#art.49`, `COD-225-2003#art.89`, `COD-225-2003#art.98`, `COD-443-2004#art.163` |
| `COD-225-2003#art.170` l.1503 | HCC: HCC33/2016-11-17, alin. (1) lit. c), in parte | 5 (1) | `COD-225-2003#art.478`, `COD-225-2003#art.483`, `COD-225-2003#art.49`, `COD-225-2003#art.89`, `L-9-2026#art.47` |
| `COD-443-2004#art.15` l.376 | HCC: HCC39/2017-12-14, al.(2) lit.d), in parte | 3 (1) | `COD-443-2004#art.30` l.551, `COD-225-2003#art.470` l.3900 |
| `COD-122-2003#art.186` l.2951 | HCC: HCC3/2016-02-23, alin. (3), (5), (8), (9), text din articol | 2 (1) | `COD-122-2003#art.195` l.3076, `COD-443-2004#art.198` l.2066 |
| `L-135-2007#art.30` l.327 | HCC: HCC27/2016-09-27, al.(2) [numerotarea de la data hotaririi], subunitate | 2 (1) | `L-135-2007#art.25` l.279, `L-181-2023#art.49` l.737 |
| `L-232-2016#art.2` l.103 | in-force: introducere de la 2030-01-01 (pct.13^1) | 2 (1) | `L-180-2026#art.44` l.887, `L-232-2016#art.30` l.315 |
| `L-303-2013#art.19` l.518 | HCC: HCC28/2016-10-11, alin. (5), text din articol (+1) | 2 (1) | `L-272-2011#art.25` l.585, `L-303-2013#art.8` l.258 |
| `COD-122-2003#art.6` l.452 | HCC: HCC2/2020-01-23, pct. 11^1), text din articol | 1 (1) | `COD-443-2004#art.98^1` l.1164 |
| `COD-218-2008#art.291^2` l.4826 | abrogat | 1 (1) | `L-75-2020#art.64` l.779 |
| `COD-218-2008#art.423^4` l.6663 | abrogat | 1 (1) | `L-195-2024#art.90` l.1173 |
| `COD-218-2008#art.427` l.6740 | HCC: HCC26/2024-12-12, alin.(2), text din articol | 1 (1) | `COD-95-2021#art.408` l.4429 |
| `COD-218-2008#art.74^1` l.1705 | abrogat | 1 (1) | `L-195-2024#art.90` l.1173 |
| `COD-225-2003#art.343^6` l.3015 | HCC: HCC37/2021-12-07, text din articol | 1 (1) | `L-325-2013#art.14` l.259 |
| `COD-325-2022#art.90` l.1614 | HCC: HCC16/2024-07-16, al.(2), textul „În serviciile media audiovizuale ... furnizorilor de servicii media.”, text din articol | 1 (1) | `COD-174-2018#art.84` l.1535 |
| `COD-443-2004#art.22` l.442 | HCC: HCC17/2017-05-10, al.(1) lit.v), text din articol | 1 (1) | `CC-1107-2002#art.757` l.5384 |
| `COD-985-2002#art.189` l.2579 | HCC: HCC24/2019-10-17, alin. (3) lit. f), text din articol | 1 (1) | `COD-122-2003#art.229^2` l.3493 |
| `L-100-2001#art.5` l.175 | HCC: HCC28/2002-05-30, al.(4), sintagma „și limba rusă”, text din articol | 1 (1) | `L-246-2018#art.42` l.501 |
| `L-1308-1997#art.11` l.214 | abrogat | 1 (1) | `HG-1170-2016#corp` l.90 |
| `L-131-2015#art.80` l.1493 | abrogat | 1 (1) | `L-20-2026#art.29` l.424 |
| `L-131-2015#art.86` l.1506 | abrogat | 1 (1) | `L-20-2026#art.29` l.428 |
| `L-158-2008#art.70` l.1154 | abrogat | 1 (1) | `L-80-2010#art.28` l.321 |
| `L-69-2016#art.12` l.201 | abrogat | 1 (1) | `L-246-2018#art.96` l.1018 |
| `L-845-1992#art.36` l.573 | abrogat | 1 (1) | `COD-1163-1997#art.227^1` l.5972 |
| `COD-325-2022#art.68` l.1225 | HCC: HCC9/2024-03-26, al.(1), lit.f), text din articol (+2) | 18 (0) | `COD-325-2022#art.91`, `COD-325-2022#art.102`, `COD-325-2022#art.111`, `COD-325-2022#art.112`, `COD-325-2022#art.113`, `COD-325-2022#art.115`, … (+9) |
| `COD-325-2022#art.16` l.262 | HCC: HCC16/2023-10-03, al.(2), lit.e), subunitate (+5) | 10 (0) | `COD-325-2022#art.68`, `COD-325-2022#art.102`, `COD-325-2022#art.72`, `COD-325-2022#art.245`, `COD-325-2022#art.89` |
| `COD-1163-1997#art.88` l.2979 | HCC: HCC7/2014-02-13, alin. (7), subunitate | 9 (0) | `COD-1163-1997#art.92`, `COD-1163-1997#art.372`, `COD-1163-1997#art.69^7`, `COD-1163-1997#art.73`, `COD-1163-1997#art.76`, `COD-1163-1997#art.79`, … (+2) |
| `COD-1163-1997#art.291` l.6915 | HCC: HCC2/2014-01-28, in parte | 8 (0) | `COD-1163-1997#art.293` l.6950, `COD-1163-1997#art.292` l.6944 |
| `L-232-2016#art.164` l.977 | in-force: reformulare de la 2030-01-01 | 8 (0) | `L-232-2016#art.39`, `L-232-2016#art.165`, `L-232-2016#art.29`, `L-232-2016#art.2` |
| `L-24-2008#art.6` l.120 | HCC: HCC3/2012-02-09, al.(2), modificarea din art. XIII pct. 1 LP163/2011, revigorare | 7 (0) | `L-24-2008#art.11`, `L-24-2008#art.13`, `L-24-2008#art.14`, `L-24-2008#art.37` |
| `COD-1163-1997#art.289` l.6866 | HCC: HCC2/2014-01-28, in parte | 6 (0) | `COD-1163-1997#art.297` l.7019, `COD-1163-1997#art.298` l.7028, `COD-1163-1997#art.294` l.6962 |
| `COD-122-2003#art.401` l.5149 | HCC: HCC9/2008-05-20, alin. (1) pct. 3), text din articol | 6 (0) | `COD-122-2003#art.402`, `COD-122-2003#art.420`, `COD-122-2003#art.421`, `COD-122-2003#art.438`, `COD-122-2003#art.445`, `COD-122-2003#art.447` |
| `COD-325-2022#art.102` l.1804 | HCC: HCC9/2024-03-26, al.(5), lit.e), subunitate | 6 (0) | `COD-325-2022#art.101`, `COD-325-2022#art.42`, `COD-325-2022#art.43`, `COD-325-2022#art.54`, `COD-325-2022#art.72`, `COD-325-2022#art.94` |
| `COD-325-2022#art.91` l.1654 | HCC: HCC9/2024-03-26, al.(3^1), subunitate (+1) | 6 (0) | `COD-325-2022#art.95`, `COD-325-2022#art.92`, `COD-325-2022#art.93`, `COD-325-2022#art.94`, `COD-325-2022#art.99` |
| `L-278-2007#art.17` l.384 | in-force: nespecificat de la 2029-01-01 | 6 (0) | `L-278-2007#art.19` l.435, `L-278-2007#art.16` l.379, `L-278-2007#art.20` l.447 |
| `COD-1316-2000#art.108` l.893 | HCC: HCC23/2024-10-15, omisiune legislativa | 5 (0) | `COD-1316-2000#art.76`, `COD-1316-2000#art.78`, `COD-1316-2000#art.80`, `COD-1316-2000#art.84`, `COD-1316-2000#art.91` |
| `L-271-2008#art.5` l.107 | HCC: HCC32/2017-12-05, lit. a), in parte | 5 (0) | `L-271-2008#art.15`, `L-271-2008#art.21`, `L-271-2008#art.8`, `L-271-2008#art.9` |
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
| `L-156-1998#art.42` l.615 | HCC: HCC27/2011-12-20, alin. (11), subunitate | 3 (0) | `L-156-1998#art.15^2` l.290, `L-156-1998#art.16` l.298, `L-156-1998#art.1^1` l.173 |
| `COD-1163-1997#art.260` l.6258 | HCC: HCC20/2018-07-04, alin. (4), text din articol | 2 (0) | `COD-1163-1997#art.229` l.5996, `COD-1163-1997#art.234` l.6044 |
| `L-108-2016#art.24` l.703 | abrogat | 2 (0) | `L-108-2016#art.114` l.2500, `L-108-2016#art.37` l.886 |
| `L-142-2008#art.31` l.333 | HCC: HCC26/2016-09-27, alin. (7), subunitate | 2 (0) | `L-142-2008#art.34` l.388, `L-142-2008#art.36` l.397 |
| `L-156-1998#art.50` l.652 | HCC: HCC27/1999-05-18, alin. (4), subunitate | 2 (0) | `L-156-1998#art.5` l.206 |
| `L-213-2023#art.2` l.78 | HCC: HCC20/2024-09-26, al.(2), teza intai: textul „Taxa de timbru nu este susceptibilă de scutire, amânare sau eșalonare, cu excepțiile prevăzute de prezenta lege.”, text din articol | 2 (0) | `L-213-2023#preambul` l.55 |
| `L-232-2016#art.39` l.368 | in-force: introducere de la 2030-01-01 (lit.j)) | 2 (0) | `L-232-2016#art.155` l.938, `L-232-2016#art.315` l.1730 |
| `L-283-2003#art.22^1` l.327 | HCC: HCC11/2023-07-20, alin. (1) lit. c), text din articol | 2 (0) | `L-283-2003#art.22^2` l.361, `L-283-2003#art.27` l.462 |
| `L-294-2007#art.8` l.198 | HCC: HCC5/2020-02-25, alin. (1) lit. d), text din articol | 2 (0) | `L-294-2007#art.10` l.226, `L-294-2007#art.4` l.149 |
| `L-303-2013#art.8` l.241 | in-force: nespecificat de la 2027-01-13 | 2 (0) | `L-303-2013#art.35` l.791, `L-303-2013#art.36^2` l.850 |
| `L-325-2013#art.17` l.292 | HCC: HCC37/2021-12-07, al.(2), subunitate (+2) | 2 (0) | `L-325-2013#art.10` l.214, `L-325-2013#art.21` l.381 |
| `COD-1149-2000#art.1` l.314 | HCC: HCC23/2019-10-10, pct. 22), text din articol (+1) | 1 (0) | `COD-1149-2000#art.49^3` l.811 |
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
| … inca 25 dispozitii, in JSON | | | |

Stari atasate dispozitiilor, in total: 20 in-force, 159 HCC, 506 abrogat. 105 dintre ele au cel putin o citare intrata, 33 din alte acte.

Acte care poarta hotariri HCC fara articol atribuit (orice citare din ele poate lovi textul anulat): `COD-828-1991` (2).

## Actele: ce citeaza si de cine sint citate

Pe act: tintele distincte ale mentiunilor (detinute + externe), actele detinute distincte care il mentioneaza, trimiterile la articole rezolvate in propriul text, rezolvate in alt act detinut, si nerezolvate (articolul citat nu are ancora in actul-tinta: abrogat cu ciotul sters, renumerotat, exponent turtit in sursa, sau o greseala de citire).

| act | ancore | citeaza (acte) | citat de (acte) | art. interne | art. in alte acte | nerezolvate | mentiuni externe |
|---|---:|---:|---:|---:|---:|---:|---:|
| `AA-2014` | 11 | 44 | 0 | 4 | 0 | 18 | 64 |
| `CC-1107-2002` | 2657 | 26 | 78 | 1017 | 8 | 1 | 8 |
| `CETS-223-2018` | 40 | 0 | 0 | 113 | 0 | 1 | 0 |
| `COD-1149-2000` | 407 | 22 | 5 | 95 | 16 | 2 | 6 |
| `COD-116-2018` | 260 | 13 | 85 | 106 | 12 | 1 | 2 |
| `COD-1163-1997` | 511 | 66 | 57 | 447 | 34 | 1 | 24 |
| `COD-122-2003` | 657 | 25 | 24 | 465 | 217 | 2 | 23 |
| `COD-1316-2000` | 133 | 7 | 8 | 28 | 3 | 0 | 1 |
| `COD-150-2014` | 206 | 16 | 8 | 46 | 3 | 0 | 6 |
| `COD-152-2014` | 171 | 7 | 9 | 17 | 0 | 0 | 3 |
| `COD-154-2003` | 416 | 24 | 35 | 198 | 2 | 0 | 12 |
| `COD-174-2018` | 98 | 18 | 8 | 71 | 7 | 0 | 8 |
| `COD-218-2008` | 737 | 55 | 83 | 508 | 96 | 14 | 15 |
| `COD-22-2024` | 96 | 26 | 12 | 18 | 7 | 0 | 7 |
| `COD-225-2003` | 540 | 23 | 40 | 213 | 33 | 17 | 8 |
| `COD-246-2024` | 99 | 25 | 1 | 47 | 3 | 1 | 10 |
| `COD-259-2004` | 119 | 8 | 3 | 7 | 0 | 0 | 6 |
| `COD-3-2009` | 85 | 10 | 6 | 19 | 1 | 0 | 4 |
| `COD-325-2022` | 252 | 36 | 15 | 164 | 24 | 0 | 5 |
| `COD-434-2023` | 390 | 44 | 26 | 137 | 35 | 1 | 12 |
| `COD-443-2004` | 360 | 30 | 31 | 123 | 76 | 0 | 11 |
| `COD-828-1991` | 4 | 0 | 3 | 0 | 0 | 11 | 0 |
| `COD-95-2021` | 472 | 37 | 15 | 430 | 10 | 0 | 20 |
| `COD-985-2002` | 566 | 22 | 47 | 166 | 3 | 1 | 11 |
| `CONST-1994` | 157 | 4 | 108 | 13 | 1 | 0 | 5 |
| `DCA-61-2024` | 0 | 5 | 0 | 0 | 5 | 0 | 1 |
| `DCNPDCP-08-2023` | 0 | 2 | 0 | 0 | 1 | 0 | 0 |
| `DCNPDCP-41-2026` | 0 | 6 | 0 | 0 | 2 | 0 | 9 |
| `DCNPDCP-581-2015` | 0 | 3 | 0 | 0 | 1 | 0 | 1 |
| `DCNPDCP-PARTIDE-2014` | 0 | 5 | 0 | 0 | 0 | 0 | 7 |
| `DCU-PROC-COMISIOANE` | 0 | 2 | 3 | 0 | 1 | 0 | 0 |
| `DCU-PROC-DECONTARE` | 0 | 9 | 0 | 0 | 7 | 0 | 2 |
| `DCU-PROC-DETINATOR` | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| `DCU-PROC-GARANTII` | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| `DCU-PROC-INREGISTRARE-VM` | 0 | 4 | 0 | 0 | 3 | 0 | 0 |
| `DCU-PROC-INSOLVABILITATE` | 0 | 4 | 0 | 0 | 1 | 0 | 0 |
| `DCU-PROC-PARTICIPANT` | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| `DCU-PROC-RECLAMATII` | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| `DCU-PROC-RECONCILIERE` | 0 | 2 | 0 | 0 | 0 | 0 | 0 |
| `DCU-REGULI-2026` | 94 | 11 | 0 | 0 | 24 | 0 | 0 |
| `HBN-127-2013` | 0 | 7 | 0 | 0 | 41 | 1 | 2 |
| `HBN-130-2013` | 0 | 3 | 0 | 0 | 6 | 1 | 0 |
| `HCNPF-14-5-2016` | 0 | 12 | 0 | 0 | 32 | 2 | 6 |
| `HCNPF-38-5-2015` | 0 | 9 | 0 | 0 | 17 | 1 | 2 |
| `HG-1123-2010` | 0 | 3 | 3 | 0 | 1 | 0 | 1 |
| `HG-1170-2016` | 0 | 16 | 1 | 0 | 7 | 1 | 9 |
| `HG-1171-2018` | 0 | 6 | 2 | 0 | 10 | 0 | 3 |
| `HG-118-2023` | 0 | 7 | 0 | 0 | 2 | 0 | 0 |
| `HG-143-2021` | 0 | 12 | 0 | 0 | 2 | 0 | 5 |
| `HG-146-2021` | 0 | 10 | 0 | 0 | 2 | 0 | 3 |
| `HG-147-2021` | 0 | 12 | 0 | 0 | 2 | 0 | 5 |
| `HG-148-2021` | 0 | 7 | 0 | 0 | 1 | 0 | 3 |
| `HG-149-2021` | 0 | 9 | 0 | 0 | 1 | 0 | 4 |
| `HG-186-2026` | 0 | 8 | 0 | 0 | 2 | 0 | 2 |
| `HG-305-2026` | 0 | 10 | 0 | 0 | 2 | 0 | 3 |
| `HG-310-2025` | 0 | 3 | 0 | 0 | 7 | 0 | 0 |
| `HG-386-2020` | 0 | 5 | 1 | 0 | 2 | 0 | 1 |
| `HG-411-2022` | 0 | 15 | 3 | 0 | 25 | 0 | 9 |
| `HG-483-2019` | 0 | 4 | 2 | 0 | 0 | 0 | 5 |
| `HG-497-2026` | 0 | 6 | 0 | 0 | 10 | 0 | 14 |
| `HG-553-2024` | 0 | 3 | 0 | 0 | 13 | 0 | 0 |
| `HG-574-2024` | 0 | 5 | 2 | 0 | 2 | 0 | 2 |
| `HG-582-2022` | 0 | 5 | 0 | 0 | 16 | 2 | 0 |
| `HG-589-2017` | 0 | 13 | 3 | 0 | 1 | 0 | 10 |
| `HG-610-2018` | 0 | 14 | 2 | 0 | 8 | 0 | 4 |
| `HG-657-2009` | 0 | 23 | 1 | 0 | 4 | 0 | 21 |
| `HG-690-2017` | 0 | 8 | 0 | 0 | 2 | 0 | 3 |
| `HG-693-2017` | 0 | 4 | 0 | 0 | 1 | 0 | 1 |
| `HG-695-2017` | 0 | 10 | 0 | 0 | 2 | 0 | 3 |
| `HG-696-2017` | 0 | 6 | 0 | 0 | 1 | 0 | 1 |
| `HG-698-2017` | 0 | 5 | 0 | 0 | 2 | 0 | 0 |
| `HG-743-2024` | 0 | 11 | 0 | 0 | 19 | 0 | 10 |
| `HG-9-2026` | 0 | 8 | 0 | 0 | 2 | 0 | 1 |
| `HG-967-2016` | 0 | 4 | 0 | 0 | 3 | 0 | 3 |
| `HG-99-2018` | 0 | 6 | 2 | 0 | 7 | 0 | 5 |
| `L-1-2018` | 28 | 5 | 2 | 19 | 0 | 0 | 1 |
| `L-10-2009` | 75 | 12 | 5 | 1 | 4 | 0 | 2 |
| `L-10-2016` | 63 | 27 | 8 | 95 | 13 | 0 | 13 |
| `L-100-2001` | 78 | 4 | 4 | 6 | 3 | 0 | 1 |
| `L-100-2017` | 80 | 18 | 17 | 12 | 7 | 0 | 6 |
| `L-102-2017` | 26 | 13 | 1 | 0 | 0 | 0 | 5 |
| `L-105-2003` | 75 | 21 | 16 | 76 | 10 | 0 | 18 |
| `L-105-2018` | 74 | 16 | 5 | 22 | 4 | 0 | 4 |
| `L-106-2022` | 45 | 10 | 2 | 32 | 1 | 0 | 5 |
| `L-107-2016` | 113 | 32 | 10 | 142 | 5 | 0 | 22 |
| `L-107-2025` | 27 | 24 | 4 | 22 | 1 | 0 | 10 |
| `L-107-2026` | 99 | 19 | 0 | 111 | 6 | 0 | 12 |
| `L-108-2016` | 144 | 41 | 11 | 293 | 7 | 1 | 28 |
| `L-108-2020` | 24 | 13 | 4 | 59 | 1 | 0 | 10 |
| `L-11-2017` | 29 | 6 | 11 | 53 | 0 | 1 | 1 |
| `L-1100-2000` | 49 | 15 | 5 | 9 | 7 | 0 | 6 |
| `L-1125-2002` | 50 | 9 | 7 | 4 | 16 | 1 | 1 |
| `L-113-2007` | 48 | 7 | 7 | 18 | 0 | 0 | 5 |
| `L-1134-1997` | 108 | 30 | 22 | 127 | 24 | 0 | 16 |
| `L-114-2012` | 131 | 24 | 17 | 267 | 16 | 2 | 7 |
| `L-114-2014` | 28 | 3 | 2 | 4 | 0 | 2 | 0 |
| `L-116-2014` | 18 | 6 | 2 | 2 | 0 | 0 | 5 |
| `L-119-2004` | 29 | 7 | 3 | 3 | 0 | 0 | 4 |
| `L-119-2018` | 32 | 11 | 6 | 56 | 6 | 1 | 5 |
| `L-121-2007` | 73 | 27 | 15 | 11 | 8 | 0 | 15 |
| `L-121-2018` | 46 | 7 | 6 | 29 | 1 | 0 | 3 |
| `L-122-2008` | 23 | 7 | 5 | 11 | 0 | 1 | 1 |
| `L-1227-1997` | 35 | 6 | 3 | 2 | 0 | 0 | 2 |
| `L-123-2023` | 16 | 3 | 1 | 6 | 1 | 0 | 0 |
| `L-124-2022` | 58 | 5 | 9 | 22 | 0 | 0 | 2 |
| `L-1260-2002` | 73 | 9 | 5 | 21 | 1 | 0 | 3 |
| `L-129-2019` | 43 | 7 | 5 | 67 | 5 | 2 | 3 |
| `L-130-2012` | 77 | 10 | 1 | 164 | 1 | 0 | 6 |
| `L-1308-1997` | 15 | 4 | 4 | 1 | 0 | 1 | 0 |
| `L-131-2007` | 55 | 9 | 6 | 4 | 2 | 0 | 4 |
| `L-131-2012` | 41 | 11 | 71 | 27 | 3 | 4 | 1 |
| `L-131-2015` | 91 | 14 | 21 | 120 | 1 | 0 | 8 |
| `L-132-2012` | 52 | 7 | 4 | 6 | 0 | 1 | 2 |
| `L-132-2016` | 45 | 13 | 15 | 27 | 7 | 0 | 1 |
| `L-133-2011` | 36 | 10 | 44 | 18 | 1 | 0 | 1 |
| `L-133-2016` | 27 | 7 | 22 | 28 | 5 | 0 | 2 |
| `L-133-2018` | 17 | 58 | 2 | 0 | 0 | 0 | 29 |
| `L-135-2007` | 93 | 11 | 6 | 17 | 17 | 0 | 1 |
| `L-1353-2000` | 37 | 17 | 4 | 10 | 1 | 0 | 8 |
| `L-136-2017` | 48 | 2 | 18 | 13 | 3 | 0 | 1 |
| `L-137-2015` | 42 | 11 | 8 | 14 | 2 | 0 | 4 |
| `L-1380-1997` | 42 | 3 | 4 | 14 | 6 | 1 | 0 |
| `L-139-2007` | 59 | 4 | 2 | 36 | 0 | 0 | 3 |
| `L-139-2010` | 72 | 11 | 11 | 58 | 0 | 0 | 10 |
| `L-139-2012` | 25 | 11 | 9 | 4 | 0 | 1 | 8 |
| `L-139-2018` | 42 | 27 | 4 | 63 | 13 | 0 | 20 |
| `L-140-2001` | 27 | 5 | 4 | 9 | 1 | 1 | 0 |
| `L-140-2013` | 34 | 4 | 5 | 12 | 3 | 2 | 1 |
| `L-140-2025` | 24 | 26 | 1 | 0 | 0 | 0 | 1 |
| `L-1402-2002` | 28 | 3 | 5 | 2 | 0 | 0 | 1 |
| `L-1409-1997` | 32 | 6 | 5 | 0 | 0 | 0 | 2 |
| `L-142-2008` | 51 | 6 | 3 | 11 | 0 | 0 | 1 |
| `L-142-2018` | 14 | 2 | 13 | 2 | 0 | 0 | 0 |
| `L-143-2014` | 54 | 14 | 2 | 58 | 4 | 3 | 2 |
| `L-1453-2002` | 1 | 1 | 5 | 0 | 0 | 0 | 1 |
| `L-1456-1993` | 46 | 6 | 4 | 7 | 1 | 2 | 1 |
| `L-148-2023` | 35 | 6 | 13 | 25 | 2 | 0 | 0 |
| `L-149-2006` | 44 | 5 | 2 | 5 | 0 | 1 | 0 |
| `L-149-2012` | 271 | 11 | 17 | 182 | 8 | 9 | 3 |
| `L-151-2022` | 31 | 17 | 7 | 25 | 8 | 1 | 7 |
| `L-152-2022` | 36 | 6 | 5 | 14 | 2 | 0 | 4 |
| `L-153-2025` | 161 | 22 | 3 | 169 | 16 | 0 | 15 |
| `L-1530-1993` | 66 | 3 | 5 | 1 | 0 | 0 | 1 |
| `L-1538-1998` | 102 | 3 | 7 | 11 | 0 | 0 | 0 |
| `L-1543-1998` | 93 | 17 | 8 | 25 | 8 | 0 | 3 |
| `L-155-2011` | 6 | 0 | 2 | 0 | 0 | 0 | 0 |
| `L-156-1998` | 55 | 12 | 7 | 37 | 1 | 0 | 14 |
| `L-156-2007` | 24 | 2 | 1 | 1 | 1 | 0 | 1 |
| `L-158-2008` | 88 | 51 | 42 | 74 | 10 | 0 | 52 |
| `L-1585-1998` | 25 | 10 | 3 | 4 | 4 | 1 | 1 |
| `L-160-2011` | 32 | 11 | 77 | 12 | 6 | 2 | 1 |
| `L-160-2017` | 43 | 8 | 3 | 1 | 2 | 0 | 3 |
| `L-160-2023` | 58 | 13 | 5 | 47 | 5 | 0 | 1 |
| `L-160-2026` | 46 | 4 | 2 | 54 | 11 | 1 | 1 |
| `L-161-2011` | 25 | 3 | 4 | 2 | 1 | 0 | 0 |
| `L-161-2014` | 56 | 4 | 2 | 31 | 0 | 0 | 0 |
| `L-162-2023` | 35 | 11 | 7 | 41 | 6 | 0 | 3 |
| `L-163-2010` | 30 | 5 | 4 | 3 | 2 | 0 | 0 |
| `L-164-2025` | 151 | 42 | 3 | 351 | 9 | 4 | 16 |
| `L-165-2023` | 31 | 10 | 2 | 4 | 0 | 0 | 5 |
| `L-17-2007` | 19 | 1 | 3 | 0 | 0 | 0 | 0 |
| `L-171-2012` | 158 | 31 | 31 | 154 | 19 | 0 | 11 |
| `L-172-2014` | 0 | 3 | 10 | 0 | 6 | 0 | 0 |
| `L-174-2017` | 46 | 42 | 9 | 84 | 43 | 1 | 17 |
| `L-174-2021` | 21 | 22 | 6 | 19 | 10 | 0 | 3 |
| `L-177-2025` | 4 | 4 | 0 | 0 | 0 | 0 | 0 |
| `L-178-2020` | 8 | 7 | 0 | 0 | 0 | 0 | 0 |
| `L-179-2008` | 56 | 11 | 7 | 16 | 6 | 0 | 2 |
| `L-179-2016` | 23 | 4 | 8 | 5 | 0 | 0 | 2 |
| `L-180-2026` | 106 | 24 | 0 | 318 | 34 | 0 | 52 |
| `L-181-2014` | 86 | 28 | 47 | 30 | 3 | 1 | 21 |
| `L-181-2023` | 50 | 19 | 3 | 13 | 26 | 1 | 4 |
| `L-182-2008` | 4 | 8 | 7 | 0 | 1 | 0 | 4 |
| `L-182-2010` | 28 | 7 | 5 | 22 | 1 | 0 | 2 |
| `L-183-2012` | 110 | 28 | 15 | 183 | 8 | 4 | 10 |
| `L-183-2016` | 17 | 6 | 8 | 8 | 3 | 0 | 1 |
| `L-184-2016` | 19 | 12 | 8 | 12 | 7 | 0 | 2 |
| `L-186-2008` | 29 | 11 | 5 | 18 | 3 | 1 | 6 |
| `L-187-2022` | 105 | 18 | 8 | 81 | 19 | 1 | 5 |
| `L-19-2016` | 26 | 17 | 10 | 21 | 0 | 0 | 15 |
| `L-192-1998` | 34 | 20 | 21 | 21 | 8 | 1 | 0 |
| `L-195-2024` | 90 | 20 | 12 | 200 | 8 | 0 | 2 |
| `L-196-2025` | 37 | 11 | 0 | 70 | 24 | 0 | 7 |
| `L-198-2007` | 54 | 10 | 7 | 38 | 15 | 0 | 7 |
| `L-198-2020` | 64 | 10 | 4 | 23 | 8 | 0 | 2 |
| `L-199-1998` | 70 | 16 | 3 | 17 | 4 | 0 | 14 |
| `L-199-2010` | 29 | 8 | 28 | 2 | 5 | 0 | 0 |
| `L-2-2020` | 46 | 17 | 1 | 29 | 9 | 0 | 8 |
| `L-20-2016` | 26 | 6 | 2 | 4 | 0 | 0 | 5 |
| `L-20-2026` | 29 | 18 | 3 | 16 | 26 | 0 | 4 |
| `L-200-2010` | 165 | 34 | 4 | 77 | 9 | 4 | 27 |
| `L-202-2013` | 33 | 6 | 7 | 43 | 2 | 0 | 3 |
| `L-202-2017` | 155 | 21 | 26 | 247 | 32 | 2 | 5 |
| `L-209-2016` | 91 | 40 | 19 | 236 | 6 | 0 | 23 |
| `L-212-2004` | 56 | 3 | 10 | 6 | 2 | 2 | 2 |
| `L-213-2023` | 10 | 6 | 12 | 5 | 2 | 1 | 2 |
| `L-218-2010` | 48 | 2 | 4 | 1 | 0 | 0 | 0 |
| `L-22-2025` | 55 | 17 | 2 | 54 | 6 | 0 | 3 |
| `L-220-2007` | 44 | 10 | 20 | 14 | 19 | 0 | 1 |
| `L-221-2007` | 59 | 12 | 11 | 7 | 5 | 1 | 7 |
| `L-227-2022` | 60 | 15 | 7 | 44 | 4 | 0 | 9 |
| `L-227-2025` | 42 | 52 | 1 | 0 | 0 | 0 | 1 |
| `L-229-2010` | 35 | 1 | 3 | 1 | 0 | 0 | 1 |
| `L-23-2008` | 36 | 4 | 2 | 6 | 0 | 0 | 2 |
| `L-230-2022` | 123 | 23 | 6 | 145 | 5 | 0 | 19 |
| `L-231-2010` | 55 | 20 | 15 | 50 | 11 | 2 | 4 |
| `L-232-2016` | 344 | 18 | 12 | 238 | 44 | 1 | 5 |
| `L-234-2016` | 37 | 14 | 10 | 30 | 8 | 0 | 3 |
| `L-234-2021` | 31 | 7 | 4 | 2 | 1 | 0 | 0 |
| `L-235-2006` | 21 | 5 | 30 | 1 | 3 | 0 | 0 |
| `L-235-2011` | 39 | 12 | 18 | 30 | 1 | 0 | 3 |
| `L-239-2007` | 43 | 7 | 5 | 4 | 0 | 0 | 3 |
| `L-239-2008` | 20 | 5 | 20 | 0 | 0 | 0 | 0 |
| `L-24-2008` | 42 | 3 | 3 | 31 | 1 | 0 | 1 |
| `L-241-2007` | 6 | 13 | 7 | 3 | 0 | 5 | 17 |
| `L-241-2022` | 15 | 5 | 4 | 4 | 2 | 0 | 1 |
| `L-245-2008` | 41 | 5 | 21 | 9 | 0 | 0 | 2 |
| `L-246-2017` | 20 | 8 | 3 | 6 | 8 | 0 | 1 |
| `L-246-2018` | 97 | 17 | 2 | 17 | 33 | 0 | 3 |
| `L-248-2025` | 56 | 4 | 1 | 1 | 1 | 0 | 0 |
| `L-25-2008` | 17 | 6 | 0 | 4 | 1 | 0 | 0 |
| `L-25-2016` | 33 | 8 | 5 | 64 | 11 | 5 | 5 |
| `L-250-2017` | 23 | 6 | 1 | 14 | 0 | 0 | 3 |
| `L-253-2025` | 44 | 3 | 0 | 18 | 1 | 0 | 1 |
| `L-254-2016` | 23 | 2 | 1 | 10 | 0 | 0 | 1 |
| `L-260-2017` | 40 | 11 | 1 | 5 | 8 | 0 | 0 |
| `L-270-2018` | 38 | 8 | 4 | 6 | 7 | 0 | 4 |
| `L-271-2008` | 22 | 4 | 3 | 9 | 0 | 0 | 2 |
| `L-271-2017` | 50 | 13 | 7 | 36 | 0 | 0 | 7 |
| `L-272-2011` | 84 | 32 | 10 | 49 | 1 | 0 | 15 |
| `L-273-1994` | 12 | 11 | 2 | 19 | 1 | 0 | 7 |
| `L-274-2011` | 35 | 5 | 5 | 12 | 1 | 0 | 5 |
| `L-277-2018` | 47 | 36 | 10 | 65 | 8 | 0 | 21 |
| `L-278-2007` | 44 | 12 | 5 | 21 | 0 | 0 | 4 |
| `L-279-2017` | 42 | 19 | 8 | 60 | 1 | 0 | 14 |
| `L-28-2024` | 63 | 16 | 1 | 8 | 0 | 0 | 13 |
| `L-282-2004` | 22 | 3 | 1 | 0 | 0 | 0 | 0 |
| `L-282-2023` | 38 | 17 | 4 | 46 | 1 | 0 | 10 |
| `L-283-2003` | 46 | 9 | 3 | 13 | 0 | 0 | 5 |
| `L-284-2004` | 29 | 10 | 5 | 4 | 7 | 0 | 2 |
| `L-287-2017` | 36 | 5 | 17 | 32 | 0 | 0 | 6 |
| `L-29-2018` | 24 | 12 | 9 | 6 | 4 | 2 | 3 |
| `L-291-2016` | 57 | 11 | 6 | 13 | 0 | 0 | 2 |
| `L-294-2007` | 40 | 12 | 2 | 21 | 7 | 0 | 3 |
| `L-296-2017` | 24 | 13 | 5 | 12 | 7 | 0 | 13 |
| `L-299-2022` | 15 | 12 | 2 | 8 | 4 | 0 | 3 |
| `L-303-2013` | 46 | 15 | 5 | 12 | 3 | 1 | 0 |
| `L-306-2018` | 38 | 17 | 11 | 6 | 6 | 1 | 8 |
| `L-308-2017` | 47 | 21 | 15 | 65 | 12 | 0 | 9 |
| `L-317-2025` | 20 | 25 | 0 | 0 | 0 | 0 | 1 |
| `L-320-2012` | 35 | 7 | 4 | 1 | 5 | 0 | 4 |
| `L-325-2013` | 28 | 11 | 19 | 41 | 2 | 0 | 6 |
| `L-325-2025` | 91 | 21 | 0 | 168 | 5 | 0 | 4 |
| `L-344-1994` | 27 | 2 | 7 | 0 | 0 | 0 | 1 |
| `L-354-2004` | 26 | 7 | 4 | 4 | 3 | 1 | 1 |
| `L-36-2016` | 41 | 12 | 6 | 4 | 0 | 0 | 7 |
| `L-36-2026` | 4 | 0 | 0 | 0 | 0 | 0 | 0 |
| `L-382-2001` | 29 | 1 | 1 | 0 | 1 | 0 | 0 |
| `L-384-2023` | 16 | 6 | 12 | 15 | 1 | 0 | 2 |
| `L-394-2023` | 29 | 17 | 1 | 58 | 17 | 0 | 10 |
| `L-397-2003` | 37 | 7 | 7 | 14 | 2 | 0 | 2 |
| `L-403-2023` | 59 | 14 | 3 | 89 | 5 | 0 | 8 |
| `L-407-2006` | 68 | 15 | 7 | 31 | 8 | 1 | 4 |
| `L-411-1995` | 72 | 9 | 7 | 5 | 1 | 5 | 2 |
| `L-414-2006` | 43 | 3 | 4 | 34 | 0 | 0 | 3 |
| `L-419-2006` | 52 | 7 | 10 | 5 | 1 | 0 | 3 |
| `L-420-2006` | 20 | 9 | 4 | 5 | 2 | 0 | 6 |
| `L-422-2006` | 13 | 4 | 6 | 14 | 0 | 0 | 1 |
| `L-422-2023` | 107 | 11 | 2 | 429 | 1 | 0 | 7 |
| `L-43-2023` | 38 | 15 | 3 | 53 | 2 | 0 | 10 |
| `L-435-2006` | 17 | 4 | 3 | 0 | 0 | 0 | 0 |
| `L-436-2006` | 98 | 29 | 10 | 16 | 15 | 0 | 13 |
| `L-439-1995` | 50 | 5 | 6 | 5 | 0 | 0 | 1 |
| `L-440-2001` | 15 | 10 | 9 | 1 | 8 | 0 | 2 |
| `L-461-2001` | 30 | 11 | 6 | 6 | 0 | 0 | 5 |
| `L-467-2003` | 38 | 3 | 3 | 1 | 2 | 0 | 0 |
| `L-48-2023` | 23 | 6 | 18 | 12 | 0 | 0 | 4 |
| `L-488-1999` | 24 | 3 | 16 | 14 | 1 | 1 | 3 |
| `L-489-1999` | 57 | 29 | 3 | 16 | 12 | 1 | 15 |
| `L-50-2013` | 31 | 6 | 6 | 5 | 2 | 0 | 2 |
| `L-509-1995` | 20 | 10 | 7 | 10 | 1 | 0 | 4 |
| `L-514-1995` | 60 | 12 | 0 | 4 | 0 | 0 | 7 |
| `L-52-2014` | 41 | 10 | 2 | 8 | 5 | 0 | 4 |
| `L-523-1999` | 18 | 4 | 1 | 1 | 0 | 0 | 2 |
| `L-548-1995` | 91 | 34 | 21 | 40 | 24 | 4 | 8 |
| `L-550-1995` | 20 | 9 | 9 | 18 | 17 | 1 | 0 |
| `L-57-2006` | 53 | 31 | 5 | 14 | 9 | 2 | 24 |
| `L-575-2003` | 46 | 3 | 4 | 11 | 3 | 1 | 0 |
| `L-59-2012` | 48 | 5 | 5 | 18 | 1 | 0 | 3 |
| `L-595-1999` | 32 | 4 | 18 | 14 | 1 | 2 | 2 |
| `L-599-1999` | 399 | 11 | 1 | 97 | 1 | 0 | 8 |
| `L-60-2012` | 62 | 11 | 6 | 4 | 3 | 0 | 3 |
| `L-62-2008` | 73 | 11 | 17 | 71 | 11 | 1 | 1 |
| `L-62-2022` | 58 | 25 | 10 | 37 | 4 | 0 | 3 |
| `L-64-2010` | 34 | 2 | 4 | 5 | 1 | 0 | 0 |
| `L-66-2008` | 64 | 9 | 5 | 84 | 0 | 0 | 5 |
| `L-66-2017` | 17 | 17 | 0 | 0 | 0 | 0 | 8 |
| `L-67-2024` | 35 | 13 | 2 | 34 | 0 | 2 | 2 |
| `L-68-2013` | 23 | 19 | 2 | 5 | 1 | 0 | 15 |
| `L-69-2016` | 70 | 4 | 1 | 18 | 0 | 0 | 0 |
| `L-7-2016` | 39 | 10 | 5 | 29 | 0 | 0 | 1 |
| `L-71-2007` | 33 | 3 | 17 | 0 | 0 | 0 | 3 |
| `L-72-2025` | 127 | 52 | 3 | 407 | 26 | 0 | 37 |
| `L-74-2020` | 96 | 17 | 7 | 69 | 7 | 0 | 5 |
| `L-75-2015` | 59 | 17 | 6 | 11 | 1 | 6 | 9 |
| `L-75-2020` | 64 | 15 | 2 | 40 | 176 | 0 | 5 |
| `L-764-2001` | 26 | 3 | 5 | 0 | 1 | 0 | 1 |
| `L-768-2000` | 28 | 6 | 3 | 0 | 4 | 0 | 1 |
| `L-77-2016` | 22 | 0 | 4 | 7 | 0 | 0 | 0 |
| `L-797-1996` | 160 | 10 | 1 | 37 | 8 | 0 | 8 |
| `L-80-2010` | 30 | 7 | 9 | 7 | 6 | 0 | 0 |
| `L-81-2004` | 26 | 5 | 4 | 1 | 1 | 0 | 2 |
| `L-82-2017` | 51 | 16 | 9 | 14 | 4 | 0 | 1 |
| `L-82-2024` | 98 | 26 | 1 | 317 | 20 | 0 | 12 |
| `L-835-1996` | 71 | 8 | 3 | 3 | 0 | 0 | 2 |
| `L-845-1992` | 46 | 14 | 5 | 12 | 4 | 0 | 2 |
| `L-847-2002` | 48 | 5 | 3 | 4 | 4 | 0 | 4 |
| `L-852-2002` | 2 | 10 | 2 | 0 | 5 | 2 | 5 |
| `L-86-2014` | 42 | 17 | 25 | 67 | 0 | 5 | 9 |
| `L-86-2020` | 28 | 5 | 5 | 11 | 0 | 0 | 2 |
| `L-880-1992` | 46 | 1 | 4 | 2 | 0 | 0 | 0 |
| `L-9-2026` | 63 | 13 | 0 | 27 | 5 | 0 | 2 |
| `L-91-2014` | 44 | 4 | 5 | 11 | 0 | 0 | 3 |
| `L-92-2014` | 61 | 19 | 11 | 31 | 2 | 0 | 1 |
| `L-92-2022` | 125 | 17 | 8 | 61 | 7 | 0 | 4 |
| `L-93-1998` | 19 | 4 | 3 | 4 | 1 | 0 | 1 |
| `L-94-2007` | 32 | 8 | 4 | 0 | 0 | 0 | 1 |
| `L-98-2012` | 38 | 9 | 17 | 3 | 1 | 0 | 0 |
| `L-982-2000` | 25 | 2 | 13 | 1 | 0 | 0 | 2 |
| `L-989-2002` | 36 | 7 | 10 | 5 | 3 | 2 | 1 |
| `OCNPDCP-03-1-2013` | 0 | 7 | 0 | 0 | 5 | 0 | 9 |
| `OCNPDCP-03-2015` | 0 | 6 | 0 | 0 | 4 | 0 | 11 |
| `OCNPDCP-27-2022` | 0 | 3 | 0 | 0 | 4 | 0 | 2 |
| `OCNPDCP-31-2026` | 0 | 2 | 0 | 0 | 13 | 0 | 1 |
| `OCNPDCP-31-2026-PROIECT` | 0 | 1 | 0 | 0 | 14 | 1 | 0 |
| `OCNPDCP-38-2026` | 0 | 1 | 0 | 0 | 3 | 0 | 0 |
| `OCNPDCP-39-2026` | 0 | 2 | 0 | 0 | 10 | 0 | 0 |
| `OCNPDCP-40-2026` | 0 | 3 | 0 | 0 | 4 | 0 | 0 |
| `OCNPDCP-48-2026` | 0 | 4 | 0 | 0 | 13 | 0 | 0 |
| `OCNPDCP-POLITIE-2013` | 0 | 9 | 0 | 0 | 5 | 0 | 13 |
| `OCNPDCP-SANATATE` | 0 | 13 | 0 | 0 | 5 | 0 | 45 |
| `UA-COD-DEONTOLOGIC-2016` | 0 | 1 | 0 | 0 | 0 | 0 | 1 |
| `UA-STATUT-2011` | 74 | 9 | 0 | 16 | 1 | 2 | 2 |

## Trimiteri nerezolvate

Articole citate care nu au ancora in actul-tinta, grupate pe tinta. Cauze cunoscute: articolul a fost abrogat si consolidarea a sters ciotul (`L-548-1995` art. 12, 13, 29, 30, 48, 54, 73; CLAUDE.md, intrebarea 6); articolul a fost abrogat si textul care il citeaza n-a fost actualizat; actul-tinta a fost renumerotat (Codul civil in 2019); ancora lipseste din cauza unei greseli de tipar in sursa (`L-100-2017` art. 52; intrebarea 4); exponentul a fost turtit in sursa (`art. 3142` pentru 314^2; intrebarea 2); sau citirea a luat drept articol al acestui act unul al altui act, nenumit in context. Fiecare rind trimite la o linie: deschide-o inainte de a trage o concluzie.

| act-tinta | articol citat | citari | poate fi | regula | exemplu (sursa, linie) | fragment |
|---|---|---:|---|---|---|---|
| `CC-1107-2002` | art. 48^30 | 7 | - | din | `COD-225-2003#art.308^2` l.2707 | de judecată audiază persoanele enumerate la art. 48^30 alin. (1) din Codul civil. (2) Audierea persoanelor indicate la art. |
| `L-131-2012` | art. 51 | 6 | exponent turtit: art. 5^1 | intern | `L-131-2012#art.29` l.560 | or încălcări, conform limitelor stabilite la art. 51. (1^1) În cazul prevăzut la art.28 alin.(9), organul respectiv includ |
| `COD-218-2008` | art. 441 | 5 | exponent turtit: art. 44^1 | din | `HG-582-2022#corp` l.94 | rocesul contravențional a încetat în temeiul art. 441 alin. (1) lit. f) din Codul contravențional al Republicii Moldova nr. |
| `L-25-2016` | art. 41 | 5 | - | intern | `L-25-2016#art.1` l.93 | iunilor Unite, adoptate în baza prevederilor art. 41 al Cartei Naţiunilor Unite; b) prin actele Uniunii Europene la care R |
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
| `L-1380-1997` | art. 281 | 2 | exponent turtit: art. 28^1 | din | `COD-1149-2000#art.126` l.1254 | erea mărfurilor destinate exportului conform art. 281 din Legea cu privire la tariful vamal şi art. 4 alin. (20^3)–(20^6) d |
| `L-1456-1993` | art. 200 | 2 | - | intern | `L-1456-1993#preambul` l.70 | 04.2005 în MONITORUL PARLAMENTULUI Nr. 59-61 art. 200 \| \| Data intrării în vigoare \| 25.05.1993 \| \| Data modificării/datele |
| `L-183-2012` | art. 572 | 2 | exponent turtit: art. 57^2 | intern | `L-183-2012#art.47` l.795 | lui Consiliului Concurenței emisă în temeiul art. 572 alin. (1) pot fi contestate, în conformitate cu prevederile Codului a |
| `L-212-2004` | art. 17 | 2 | - | din | `L-108-2016#art.105^1` l.2255 | larării stării de urgență în conformitate cu art. 17–19 din Legea nr. 212/2004 privind regimul stării de urgență, de asedi |
| `L-212-2004` | art. 20 | 2 | - | intern | `L-212-2004#art.42` l.267 | asediu, suplimentar la măsurile prevăzute la art.20, pot fi luate următoarele măsuri: a) închiderea frontierei de stat a |
| `L-231-2010` | art. 215 | 2 | exponent turtit: art. 21^5 | intern | `L-231-2010#art.15` l.440 | e loc cu respectarea cerințelor stabilite la art. 215 alin. (2). (5) Notificările semnate olograf de către deponent, precum |
| `L-241-2007` | art. 2 | 2 | - | din | `L-114-2012#art.3` l.263 | ctronice – rețea astfel cum este definită la art. 2 din Legea comunicațiilor electronice nr. 241/2007; rezidenți – entită |
| `L-241-2007` | art. 20 | 2 | - | intern | `L-241-2007#art.64` l.125 | erviciile de acces la Internet, prevăzute la art. 20 alin. (1^1) și (1^2), la care se abonează utilizatorul final, ar pute |
| `L-241-2007` | art. 88 | 2 | - | intern | `L-241-2007#art.64` l.126 | c) atunci când există o obligație în temeiul art. 88, opțiunile abonatului privind înscrierea sau nu a datelor sale cu car |
| `L-488-1999` | art. 7 | 2 | - | din | `L-29-2018#art.21` l.358 | a obiectivelor de utilitate publică, conform art. 7 din Legea exproprierii pentru cauză de utilitate publică nr. 488/1999 |
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
| `COD-1163-1997` | art. 208 | 1 | - | din | `L-354-2004#art.22` l.308 | ferându-se beneficiarilor în conformitate cu art.208 din Codul fiscal nr.1163-XIII din 24 aprilie 1997. În celelalte cazur |
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
| `COD-22-2024` | art. 82 | 1 | - | din | `L-29-2018#art.21` l.349 | art. 11 din Codul funciar nr. 828/1991 şi cu art. 82 din Codul funciar al R.S.S.Moldova, astfel cum a fost modificat prin |
| `COD-225-2003` | art. 48^15 | 1 | - | intern | `COD-225-2003#art.308^17` l.2789 | u controlul executării mandatului, în sensul art. 48^15 alin. (3), şi de către persoanele ale căror drepturi sunt afectate pr |
| `COD-225-2003` | art. 581 | 1 | exponent turtit: art. 58^1 | din | `CC-1107-2002#art.113` l.952 | ori din oficiu. (3) În cazurile prevăzute la art. 581 din Codul de procedură civilă, curatorul special sau tutorele special |
| `COD-246-2024` | art. 251 | 1 | - | intern | `COD-246-2024#preambul` l.82 | te care fac obiectul procedurii prevăzute la articolul 251 din tratat, în ceea ce privește procedura de reglementare cu control |
| … inca 96 grupuri, in JSON | | | | | | |

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

