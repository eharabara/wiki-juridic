---
title: Test metodă transpunere — EMIR 648/2012
created: '2026-07-09'
updated: '2026-07-09'
type: query
tags:
- moldova
- query
- eu
- eu-acquis
- transposition
- legal-approximation
- cnpf
- bnm
- financial-services
- capital-market
- securities
- financial-supervision
- methodology
sources:
- concepts/moldova-eu-transposition-method.md
- concepts/moldova-eu-transposition-rule-matrix.md
- concepts/acquis-CSDR-EMIR.md
- comparisons/cnpf-transposition-matrix.md
- queries/verificare-schelet-lege-emir-2026-07-03.md
- raw/papers/cnpf/UE-648-2012.md
- raw/papers/cnpf/L-171-2012.md
- raw/papers/cnpf/L-192-1998.md
- raw/papers/cnpf/L-178-2020.md
- raw/papers/cnpf/L-234-2016.md
- raw/papers/moldova-legal/L-100-2017.md
- raw/papers/moldova-legal/HG-1171-2018.md
confidence: medium
---

# Test metodă transpunere — EMIR 648/2012

## Întrebarea / scopul testului

Testarea paginilor [[moldova-eu-transposition-method]] și [[moldova-eu-transposition-rule-matrix]] pe cazul EMIR, folosind sursele deja existente în wiki: [[acquis-CSDR-EMIR]], [[cnpf-transposition-matrix]], [[verificare-schelet-lege-emir-2026-07-03]], raw-ul EUR-Lex `UE-648-2012`, precum și actele moldovenești relevante [[L-171-2012]], [[L-192-1998]], [[L-178-2020]] și [[L-234-2016]].

## Verdict scurt

Metoda funcționează: ea mută analiza EMIR de la „avem o lacună probabilă și un schelet bun” la o listă de artefacte obligatorii și reguli testabile. Testul arată că EMIR trebuie tratat ca **transpunere directă / aproximare pre-aderare a unui regulament UE**, nu doar ca implementare internă generică. Rezultatul minim acceptabil pentru următoarea etapă este o matrice articol-cu-articol EMIR → drept moldovenesc → autoritate competentă → grad de compatibilitate → acțiune.

Pe baza surselor citite, statutul actual rămâne: **partial / fail pentru transpunere demonstrată**, deoarece wiki-ul are raw EMIR, pagină de acquis și schelet de lege, dar nu are încă tabel de concordanță EMIR complet. `[raw/papers/cnpf/UE-648-2012.md art.1]` `[raw/papers/cnpf/UE-648-2012.md art.9]` `[[cnpf-transposition-matrix]]`

## Gate 0 — clasificarea intervenției

| Întrebare | Rezultat pentru EMIR | Consecință procedurală |
|---|---|---|
| Este transpunere directă a unui act UE? | Da, cazul vizează Regulamentul (UE) nr. 648/2012 / EMIR, CELEX consolidat `02012R0648-20250117`. | Se activează regimul complet din [[HG-1171-2018]]: clauză de armonizare, sigla UE, tabel de concordanță, nota de fundamentare și expertiza de compatibilitate. |
| Este directivă sau regulament? | Regulament UE, dar Moldova trebuie să-l aproximeze/transpună pre-aderare prin act național. | Conform [[moldova-eu-transposition-rule-matrix]], regimul tranzitoriu trebuie tratat cu atenție: pentru regulamente/decizii, HG1171 cere evitarea tranzițiilor condiționate de aderare și prevederi de abrogare la momentul aderării. |
| Este modificare a unui act deja armonizat? | Nu neapărat, dacă se păstrează lege EMIR separată; poate deveni „modificare” dacă se intervine în [[L-171-2012]], [[L-234-2016]] sau alte legi. | Dacă se modifică acte armonizate, se activează regula cu două tabele: UE→proiect și UE→versiune consolidată a actului național. |
| Este doar cadru de implementare? | Nu. Scheletul analizat urmărește obligații EMIR de fond: clearing, reporting, risk mitigation, CPC/TR, sancțiuni. | Tabelul de concordanță este obligatoriu ca disciplină de lucru, chiar dacă proiectul final va avea adaptări pre-aderare. |

## Source pack minim pentru EMIR

| Element | Sursă în wiki | Observație |
|---|---|---|
| Act UE principal | `raw/papers/cnpf/UE-648-2012.md` | Reg. (UE) 648/2012, CELEX `02012R0648-20250117`, extract RO structurat, consolidare 2025-01-17. |
| Pagina acquis | [[acquis-CSDR-EMIR]] | Marchează EMIR ca lacună probabilă și conectează cu CSDR/SFD/DCU. |
| Matrice sectorială | [[cnpf-transposition-matrix]] | EMIR apare ca „probabil lacună `[de verificat]`”. |
| Schelet național existent | [[verificare-schelet-lege-emir-2026-07-03]] | Confirmă că proiectul abordează clearing, reporting, risk mitigation, CPC/TR, sancțiuni, dar încă nu e matrice articol-cu-articol. |
| Procedură națională generală | [[L-100-2017]] | Art. 30, 31, 35: nota de fundamentare, tabel concordanță, clauză/siglă UE, expertiză compatibilitate. |
| Regulament armonizare UE | [[HG-1171-2018]] | Etape, tabel de concordanță, calificative, expertiză, distincție direct/implementation-only. |
| Acte MD relevante | [[L-171-2012]], [[L-192-1998]], [[L-178-2020]], [[L-234-2016]] | Mandat CNPF/BNM, piață de capital, derivate, DCU/CSDR, transfer prudențial către BNM. |

## EU obligation map — versiune de test

| Cluster EMIR | Articole / sursă | Obligație sau instituție UE | Implicație pentru Moldova |
|---|---|---|---|
| Obiect și domeniu | art. 1 | clearing/risk management pentru OTC derivatives, reporting pentru contracte derivate, cerințe uniforme pentru CPC și registre centrale de tranzacții. | Legea națională nu trebuie să acopere doar piața de capital; trebuie să acopere contrapărți financiare/nefinanciare și infrastructură. |
| Definiții | art. 2 | CPC, registru central de tranzacții, compensare, instrument financiar derivat etc. | Terminologia „registre centrale de tranzacții” este obligatorie; „registrele contractelor derivate” este insuficient/ambiguu. |
| Obligația de compensare | art. 4; art. 4a; art. 10 | clase de OTC derivatives supuse compensării; contrapărți financiare/nefinanciare și praguri. | Trebuie stabilit cine calculează pragurile, cine notifică, ce clase se aplică și ce autoritate supraveghează. |
| EMIR 3 / cont activ | cuprins art. 7a–7e; scheletul anterior | cerințe noi privind cont activ și monitorizare. | Dacă textul invocă consolidarea post-2024, omiterea cerințelor EMIR 3 trebuie decisă și explicată. |
| Raportare | art. 9; art. 55; art. 77; art. 81 | raportare către registru central înregistrat/recunoscut; calitatea datelor; acces la date. | Trebuie decis dacă raportarea se face către TR UE/ESMA-recunoscut, mecanism național sau model hibrid; CNPF/BNM au nevoie de acces la date. |
| Risk mitigation | art. 11 | confirmare, reconciliere, dispute, evaluare zilnică, garanții. | Necesită norme secundare și mandat clar pentru CNPF/BNM. |
| Sancțiuni | art. 12 și arhitectura EMIR 3 | sancțiuni eficace/proporționale/disuasive; reporting/data-quality devine critic. | Capitol sancțiuni nu poate fi decorativ; trebuie să acopere familii de încălcări. |
| CPC | art. 14, 22, 23, 25, 39 | autorizare CPC UE de autorități stat membru; recunoaștere CPC țări terțe de ESMA; segregare/portabilitate. | Formula „CPC autorizate de ESMA” trebuie evitată; trebuie distins între CPC UE autorizate și CPC terțe recunoscute de ESMA. |
| Secret / schimb informații | art. 83–84, verificat în pagina de schelet | secret profesional și schimb de informații între autorități. | Art. naționale privind CNPF/BNM/ESMA/autorități străine trebuie să fie operaționale, nu generice. |

## MD mapping — constatări preliminare

| Zonă | Sursă MD | Status preliminar | Observație |
|---|---|---|---|
| Derivate în piața de capital | [[L-171-2012]] art. 4 | Parțial / insuficient | Legea 171 include instrumente derivate, dar le reglementează doar în contextul tranzacționării pe piețe reglementate/MTF; nu echivalează cu regimul OTC EMIR. `[raw/papers/cnpf/L-171-2012.md art.4]` |
| Mandat CNPF | [[L-192-1998]] | Parțial | CNPF are competențe pe piața financiară nebancară/piața de capital, schimb de informații și sancțiuni, dar atribuțiile nu trebuie suprapuse cu BNM. `[raw/papers/cnpf/L-192-1998.md art.4-5, art.8-9]` |
| Mandat BNM / perimetru prudențial | [[L-178-2020]] | Critic pentru arhitectură | BNM a preluat supravegherea prudențială pentru asigurări, OCN, AEÎ, birouri de credit; EMIR poate atinge entități BNM. |
| DCU / CSDR | [[L-234-2016]] | Parțial pentru CSDR, nu EMIR | Legea 234 transpune parțial CSDR și plasează DCU sub BNM; nu rezolvă clearing/reporting/risk mitigation EMIR. `[raw/papers/cnpf/L-234-2016.md]` |
| Regim EMIR dedicat | [[verificare-schelet-lege-emir-2026-07-03]] | În lucru | Scheletul este o bază bună, dar necesită tabel de concordanță, clarificare CNPF/BNM, CPC/TR și sancțiuni. |

## Arhitectură normativă recomandată de test

Pentru o primă etapă pre-aderare, cea mai curată opțiune rămâne **lege separată EMIR / derivate OTC**, cu modificări conexe la legile sectoriale. Motivul: EMIR traversează piața de capital, bănci, asigurări/reasigurări, DCU, contrapărți nefinanciare și infrastructură post-tranzacționare; încadrarea exclusivă în [[L-171-2012]] ar risca o lege CNPF-only.

Arhitectura ar trebui să aibă:

1. dispoziții generale, definiții și domeniu;
2. autorități competente și cooperare CNPF/BNM/ESMA/autorități străine;
3. capitol umbrelă pentru clearing, reporting și risk mitigation;
4. regim pentru CPC eligibile: CPC autorizate în UE sau CPC din țări terțe recunoscute de ESMA, plus mecanism național de acceptare/registru;
5. registre centrale de tranzacții și acces la date;
6. supraveghere, investigații, măsuri corective și sancțiuni;
7. dispoziții finale/tranzitorii compatibile cu faptul că EMIR este regulament UE.

## Rule matrix run — rezultate pe EMIR

| Rule ID | Status test | Motiv / următoare acțiune |
|---|---|---|
| MD-TRANS-001 | pass | Am clasificat cazul ca transpunere directă/aproximare pre-aderare a Regulamentului EMIR; nu implementation-only. |
| MD-TRANS-002 | partial | CELEX și sursa EMIR există, dar fișa de obligații UE este doar preliminară; trebuie extinsă pentru toate articolele relevante, inclusiv EMIR 3. |
| MD-TRANS-003 | fail/partial | Există mapping preliminar la L-171/L-192/L-178/L-234, dar nu există tabel complet UE→MD pentru fiecare obligație. |
| MD-TRANS-004 | partial | CNPF/BNM sunt identificate ca problemă critică, dar tabelul de responsabilități pe obligații EMIR încă lipsește. |
| MD-TRANS-005 | partial | Direcția de lege separată este formulată; trebuie verificată metoda de transpunere pentru regulament UE și textul de abrogare la aderare. |
| MD-TRANS-006 | partial | Terminologia CPC/TR este identificată; lipsește încă terminological map complet: FC/NFC, OTC derivative, clearing member, intragroup etc. |
| MD-TRANS-007 | fail/partial | Pentru că EMIR este regulament UE, dispozițiile tranzitorii și abrogarea la aderare trebuie proiectate explicit. |
| MD-TRANS-008 | fail/pending | Nu există încă nota de fundamentare sau compartimentul 5 complet privind compatibilitatea UE. |
| MD-TRANS-009 | fail/pending | Nu există clauza de armonizare completă pentru proiect. |
| MD-TRANS-010 | fail/pending | Nu există verificare a siglei UE pe proiect. |
| MD-TRANS-011 | fail | Nu există încă tabel de concordanță EMIR complet. Acesta este principalul output lipsă. |
| MD-TRANS-012 | not applicable / conditional | Devine aplicabil dacă proiectul modifică explicit L-171, L-234 sau alt act armonizat; pentru lege separată pură, nu este regula principală. |
| MD-TRANS-013 | fail | Nu există încă calificative de compatibilitate pe rânduri EMIR. |
| MD-TRANS-014 | pending | Se aplică după ce există proiect și tabel; trebuie urmărit pe parcursul redactării. |
| MD-TRANS-015 | fail/pending | Expertiza de compatibilitate nu poate fi pregătită fără tabel complet. |
| MD-TRANS-016 | not applicable | Nu tratăm cazul ca implementation-only. |
| MD-TRANS-017 | pending | Se aplică în etapa consultare/avizare; pentru moment trebuie pregătită sinteza viitoare. |
| MD-TRANS-018 | fail/pending | Dosarul final nu există; gate-ul este util ca ultim control. |

## Mini-schelet de tabel de concordanță EMIR pentru etapa următoare

| EMIR | Obligație | Corespondent MD actual | Status | Acțiune recomandată |
|---|---|---|---|---|
| Art. 1 | obiect: clearing, risk mitigation, reporting, CPC, TR | L-171 reglementează derivate doar limitat; L-234 acoperă DCU/CSDR | parțial/lacună | lege EMIR separată + modificări conexe |
| Art. 2 | definiții CPC, TR, clearing, derivative | L-171 are categorii de instrumente financiare derivate, dar nu toate definițiile EMIR | parțial | capitol definiții + termen „registre centrale de tranzacții” |
| Art. 4/4a/10 | clearing obligation și praguri FC/NFC | nu există mapping complet | lacună probabilă | articole privind obligația de compensare, praguri, notificări, autoritate competentă |
| Art. 7a–7e | cont activ / monitorizare EMIR 3 | nu apare demonstrat în schelet | lacună / decizie politică | include sau justifică nepreluarea în nota de fundamentare |
| Art. 9/55/77/81 | reporting către TR și acces la date | scheletul are capitol raportare, dar terminologie/operare nefinalizată | parțial | definește TR eligibile, acces CNPF/BNM, calitatea datelor |
| Art. 11 | risk mitigation | scheletul are capitol dedicat | parțial | detaliază norme secundare, termene, garanții, reconciliere, dispute |
| Art. 12 | sancțiuni | scheletul are capitol scurt | parțial/fail | extinde competențe și familii de încălcări |
| Art. 14/22/23/25 | CPC authorization/recognition/cooperation | scheletul are recunoaștere CPC, dar riscă formula greșită „autorizate de ESMA” | parțial | distinge CPC UE autorizate național vs CPC terțe recunoscute de ESMA |
| Art. 39/48 | segregation/portability/default | menționat în analiza scheletului | parțial | corelează cu SFD, insolvabilitate, garanții financiare și DCU |
| Art. 83–84 | secret profesional / schimb informații | scheletul are articole dedicate | parțial | text detaliat pentru CNPF, BNM, ESMA, autorități străine |

## Ce am învățat despre metodă

1. **Gate 0 este util:** separă transpunerea directă de implementation-only și forțează tratamentul special al regulamentelor UE.
2. **Rule matrix scoate la suprafață lipsa centrală:** nu lipsa de text narativ, ci lipsa tabelului de concordanță complet și a calificativelor de compatibilitate.
3. **Metoda previne eroarea CNPF-only:** EMIR nu poate fi atribuit exclusiv CNPF fără maparea contrapărților financiare și a BNM.
4. **Metoda cere decizii de politică înainte de draft complet:** CPC locală vs CPC UE/ESMA, TR eligibile, acces la date, EMIR 3, sancțiuni.
5. **Următorul artefact nu trebuie să fie un skill încă:** trebuie întâi creată matricea EMIR articol-cu-articol, apoi skill-ul poate impune automat acel format.

## Recomandare imediată

Următorul pas ar trebui să fie crearea unei pagini `comparisons/emir-concordance-skeleton.md` sau `queries/emir-concordance-skeleton-2026-07-09.md`, cu tabel complet pe articole EMIR prioritare. Pentru început, nu trebuie acoperit tot EMIR dintr-o dată; minimul util ar fi art. 1, 2, 4, 4a, 4b, 7a–7e, 9, 10, 11, 12, 14, 22–25, 39, 48, 55, 77, 81, 83, 84, 89.

Artefact creat pe baza acestei recomandări: [[emir-concordance-skeleton]].

## Linkuri interne

- [[moldova-eu-transposition-method]]
- [[moldova-eu-transposition-rule-matrix]]
- [[acquis-CSDR-EMIR]]
- [[cnpf-transposition-matrix]]
- [[verificare-schelet-lege-emir-2026-07-03]]
- [[L-171-2012]] · [[L-192-1998]] · [[L-178-2020]] · [[L-234-2016]]
