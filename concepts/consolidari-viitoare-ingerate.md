---
title: Consolidări viitoare ingerate — 46 de versiuni cu dată viitoare ale actelor deținute
created: '2026-09-25'
updated: '2026-09-25'
type: concept
perimeter: legal
tags:
- moldova
- concept
- legal-source
- methodology
sources:
- raw/papers/moldova-legal/viitor/L-160-2011--2027-01-23.md
- _meta/inforce/in-force-register.md
confidence: medium
---

# Consolidări viitoare ingerate

Politica veche a wiki-ului era să țină numai textul în vigoare azi și să nu ingereze versiunile viitoare, ca să nu se citeze ca lege ce încă nu se aplică. La cererea lui Eugen (2026-09-25) cele **46 de versiuni cu dată viitoare** ale actelor deținute au fost ingerate, dar **separat**: fiecare în `raw/papers/moldova-legal/viitor/<act>--<data>.md`, cu bannerul „VERSIUNE VIITOARE” și cu frontmatter `future_version_of`, `applies_from` și `in_force_warning`. Textul în vigoare azi rămîne neatins în fișierul actului. Ele vin din două liste: cele 23 din `_meta/inforce/pending-consolidations.json` (17 acte, citite de mînă la 2026-09-07 și 2026-09-24) și 23 ale celor 16 acte din [[perimetrul-actelor-permisive]].

## Reguli de citire

- **Un fișier `viitor/` nu se citează ca drept în vigoare.** Se citează numai cu data de la care se aplică și cu mențiunea că poate fi modificat pînă atunci; ex. `L-131-2007--2027-01-23` se aplică de la 23.01.2027.
- **Data versiunii** e cea din lista de versiuni de pe legis.md (`applies_from`, egală cu `consolidation_date`). Rîndul de modificare din act poate fi mai vechi: la `L-19-2016--2030-01-01`, `L-82-2024--2028-05-08` și `L-22-2025--2027-03-27` e mai vechi, și se păstrează în `consolidation_date_from_modification_line`.
- **Registrul in-force citește fișierele acestea** (`_meta/inforce/in-force-register.md`): 234 de dispoziții afectate în 51 de acte, față de 70 în 13 înainte. Graful de citare și registrul HCC **nu** le citesc (citesc doar folderul de sus), deci nu se dublează.
- **Versiunile succesive ale aceluiași act** (ex. 5 la `L-160-2011`) nu sînt comparate aici; diferențele, unde s-au citit, sînt în `pending-consolidations.json`.

## Cele 46 de fișiere

| fișier | act de bază | se aplică de la | act modificator (rîndul din text) | articole | HTML (octeți) |
|---|---|---|---|---:|---:|
| [[L-599-1999--2026-12-28]] | [[L-599-1999]] | 2026-12-28 | LP136 din 13.06.25 | 398 | 754933 |
| [[L-282-2004--2027-01-01]] | [[L-282-2004]] | 2027-01-01 | LP327 din 29.12.25 | 22 | 91524 |
| [[L-149-2006--2027-03-24]] | [[L-149-2006]] | 2027-03-24 | LP185 din 24.08.26 | 44 | 327624 |
| [[L-131-2007--2027-01-23]] | [[L-131-2007]] | 2027-01-23 | LP136 din 09.07.26 | 55 | 294186 |
| [[L-131-2007--2029-01-01]] | [[L-131-2007]] | 2029-01-01 | LP159 din 30.07.26 | 55 | 292133 |
| [[L-221-2007--2026-11-13]] | [[L-221-2007]] | 2026-11-13 | LP168 din 30.07.26 | 59 | 251222 |
| [[L-221-2007--2027-11-30]] | [[L-221-2007]] | 2027-11-30 | LP140 din 13.06.25 | 59 | 252007 |
| [[L-278-2007--2027-03-01]] | [[L-278-2007]] | 2027-03-01 | LP25 din 03.03.23 | 43 | 278535 |
| [[L-278-2007--2029-01-01]] | [[L-278-2007]] | 2029-01-01 | LP125 din 29.05.25 | 43 | 281164 |
| [[L-278-2007--2029-03-21]] | [[L-278-2007]] | 2029-03-21 | LP25 din 03.03.23 | 43 | 281814 |
| [[L-68-2013--2026-11-10]] | [[L-68-2013]] | 2026-11-10 | LP78 din 07.05.26 | 28 | 174934 |
| [[L-68-2013--2027-11-30]] | [[L-68-2013]] | 2027-11-30 | LP140 din 13.06.25 | 28 | 165627 |
| [[L-19-2016--2027-01-01]] | [[L-19-2016]] | 2027-01-01 | LP91 din 28.05.26 | 26 | 227414 |
| [[L-19-2016--2030-01-01]] | [[L-19-2016]] | 2030-01-01 | LP91 din 28.05.26 (mai vechi decît versiunea) | 26 | 215431 |
| [[L-179-2016--2027-01-01]] | [[L-179-2016]] | 2027-01-01 | LP76 din 02.07.26 | 23 | 125521 |
| [[L-296-2017--2027-11-30]] | [[L-296-2017]] | 2027-11-30 | LP140 din 13.06.25 | 25 | 132503 |
| [[L-105-2018--2026-12-10]] | [[L-105-2018]] | 2026-12-10 | LP169 din 24.08.26 | 81 | 420506 |
| [[L-119-2018--2027-11-30]] | [[L-119-2018]] | 2027-11-30 | LP140 din 13.06.25 | 32 | 204317 |
| [[L-394-2023--2027-11-30]] | [[L-394-2023]] | 2027-11-30 | LP140 din 13.06.25 | 29 | 170482 |
| [[L-403-2023--2027-11-30]] | [[L-403-2023]] | 2027-11-30 | LP140 din 13.06.25 | 59 | 274370 |
| [[L-422-2023--2027-11-30]] | [[L-422-2023]] | 2027-11-30 | LP140 din 13.06.25 | 107 | 541495 |
| [[L-82-2024--2027-11-30]] | [[L-82-2024]] | 2027-11-30 | LP140 din 13.06.25 | 98 | 521030 |
| [[L-82-2024--2028-05-08]] | [[L-82-2024]] | 2028-05-08 | LP140 din 13.06.25 (mai vechi decît versiunea) | 98 | 519681 |
| [[COD-1163-1997--2027-01-01]] | [[COD-1163-1997]] | 2027-01-01 | LP187 din 10.07.25 | 512 | 2905248 |
| [[COD-325-2022--2027-01-01]] | [[COD-325-2022]] | 2027-01-01 | LP327 din 29.12.25 | 252 | 991276 |
| [[L-98-2012--2027-01-01]] | [[L-98-2012]] | 2027-01-01 | LP76 din 02.07.26 | 38 | 184203 |
| [[L-160-2011--2026-12-28]] | [[L-160-2011]] | 2026-12-28 | LP136 din 13.06.25 | 32 | 195955 |
| [[L-160-2011--2027-01-01]] | [[L-160-2011]] | 2027-01-01 | LP176 din 03.07.25 | 32 | 196013 |
| [[L-160-2011--2027-01-23]] | [[L-160-2011]] | 2027-01-23 | LP40 din 26.03.26 | 32 | 196582 |
| [[L-160-2011--2027-05-21]] | [[L-160-2011]] | 2027-05-21 | LP71 din 30.04.26 | 32 | 196489 |
| [[L-160-2011--2029-01-01]] | [[L-160-2011]] | 2029-01-01 | LP159 din 30.07.26 | 32 | 196492 |
| [[L-435-2006--2027-01-01]] | [[L-435-2006]] | 2027-01-01 | LP200 din 03.09.26 | 17 | 76359 |
| [[L-121-2007--2027-01-01]] | [[L-121-2007]] | 2027-01-01 | LP200 din 03.09.26 | 77 | 393860 |
| [[L-121-2007--2027-11-30]] | [[L-121-2007]] | 2027-11-30 | LP140 din 13.06.25 | 77 | 365353 |
| [[L-397-2003--2027-01-01]] | [[L-397-2003]] | 2027-01-01 | LP327 din 29.12.25 | 37 | 168943 |
| [[L-397-2003--2028-01-01]] | [[L-397-2003]] | 2028-01-01 | LP200 din 03.09.26 | 37 | 169373 |
| [[L-270-2018--2027-01-01]] | [[L-270-2018]] | 2027-01-01 | LP200 din 03.09.26 | 38 | 148052 |
| [[L-52-2014--2026-12-09]] | [[L-52-2014]] | 2026-12-09 | LP165 din 30.07.26 | 41 | 129381 |
| [[L-165-2023--2026-12-09]] | [[L-165-2023]] | 2026-12-09 | LP165 din 30.07.26 | 36 | 182821 |
| [[L-121-2018--2027-03-27]] | [[L-121-2018]] | 2027-03-27 | LP22 din 20.02.25 | 46 | 217760 |
| [[L-22-2025--2027-03-27]] | [[L-22-2025]] | 2027-03-27 | LP20 din 26.02.26 (mai vechi decît versiunea) | 55 | 404202 |
| [[L-274-2011--2027-01-01]] | [[L-274-2011]] | 2027-01-01 | LP200 din 03.09.26 | 35 | 117114 |
| [[L-82-2017--2026-12-09]] | [[L-82-2017]] | 2026-12-09 | LP165 din 30.07.26 | 51 | 263770 |
| [[L-229-2010--2027-01-01]] | [[L-229-2010]] | 2027-01-01 | LP327 din 29.12.25 | 35 | 92745 |
| [[HG-149-2021--2027-07-01]] | [[HG-149-2021]] | 2027-07-01 | HG470 din 26.08.26 | 0 | 93944 |
| [[HG-146-2021--2027-07-01]] | [[HG-146-2021]] | 2027-07-01 | HG470 din 26.08.26 | 0 | 118808 |

Acte de bază fără pagină de entitate: vezi lista din manifest, secțiunea AX.

