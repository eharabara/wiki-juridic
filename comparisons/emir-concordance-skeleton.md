---
title: EMIR concordance skeleton — Regulamentul (UE) 648/2012 vs dreptul Moldovei
created: '2026-07-09'
updated: '2026-09-05'
type: comparison
tags:
- moldova
- comparison
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
- _archive/emir-2026-07/test-metoda-transpunere-emir-2026-07-09.md
- _archive/emir-2026-07/verificare-schelet-lege-emir-2026-07-03.md
- raw/papers/cnpf/UE-648-2012.md
- raw/papers/cnpf/UE-648-2012-priority-articles-2026-07-09.md
- raw/papers/cnpf/L-171-2012.md
- raw/papers/cnpf/L-192-1998.md
- raw/papers/cnpf/L-178-2020.md
- raw/papers/cnpf/L-234-2016.md
- raw/papers/moldova-legal/L-100-2017.md
- raw/papers/moldova-legal/HG-1171-2018.md
- _archive/emir-2026-07/emir-audit-conformitate-lege100-hg1171-2026-07-10.md
- _archive/emir-2026-07/emir-draft-complet-2026-07-10.md
- raw/papers/cnpf/md-2026-07-09-proiect-lege-emir-completat.md
confidence: medium
---

# EMIR concordance skeleton — Regulamentul (UE) 648/2012 vs dreptul Moldovei

## Scop și statut

Această pagină transformă recomandarea din [[_archive/emir-2026-07/test-metoda-transpunere-emir-2026-07-09|test-metoda-transpunere-emir-2026-07-09]] într-un prim **schelet de concordanță articol-cu-articol** pentru EMIR. Nu este încă tabelul oficial de concordanță cerut de [[HG-1171-2018]] și [[L-100-2017]]; este un instrument de lucru pentru a decide ce trebuie redactat, ce trebuie verificat și ce instituție este competentă.

Verdictul de lucru rămâne: **EMIR nu poate fi marcat ca transpus demonstrat**. Există sursă EUR-Lex, pagină de acquis, analiză de schelet național și ancore moldovenești parțiale, dar lipsește încă un tabel complet cu calificative de compatibilitate pentru fiecare obligație relevantă. Vezi [[acquis-CSDR-EMIR]], [[cnpf-transposition-matrix]] și [[_archive/emir-2026-07/verificare-schelet-lege-emir-2026-07-03|verificare-schelet-lege-emir-2026-07-03]].

## Surse și limite

- Act UE principal: `raw/papers/cnpf/UE-648-2012.md`, CELEX consolidat `02012R0648-20250117`.
- Pentru această pagină am salvat și un extract suplimentar: `raw/papers/cnpf/UE-648-2012-priority-articles-2026-07-09.md`, cu articolele prioritare art. 1, 2, 3, 4, 4a, 4b, 7a–7e, 9, 10, 11, 12, 14, 22–25, 39, 48, 55, 77, 81, 83, 84 și 89.
- Drept MD consultat: [[L-171-2012]], [[L-192-1998]], [[L-178-2020]], [[L-234-2016]]. Pentru [[L-171-2012]], **actualizat 2026-09-05:** fișierul raw a fost reîmprospătat la 2026-09-04 și poartă acum consolidarea 2027-06-01, nu 2021-01-01; [[L-177-2025]] este încorporat în textul de bază, inclusiv art. 4^1. Atenție însă că aceeași consolidare este **datată în viitor**: arts. 38 și 141^1 apar abrogate cu efect de la 01.06.2027 și sunt încă în vigoare astăzi.
- Calificativele de mai jos sunt **preliminare**: `parțial`, `lacună`, `decizie de politică`, `not applicable / adaptare`, `pending`. Ele nu înlocuiesc calificativele formale HG1171 din tabelul oficial.

## Ipoteze de arhitectură folosite în schelet

1. Instrumentul principal este o **lege separată EMIR / derivate OTC**, cu modificări conexe la legile sectoriale.
2. Nu se creează, în prima versiune, un regim complet de autorizare a unei CPC locale; proiectul trebuie să pornească de la folosirea **CPC autorizate în UE de autoritățile statelor membre** și/sau **CPC din țări terțe recunoscute de ESMA**, cu mecanism național de acceptare/registru.
3. Termenul pentru trade repositories este **registre centrale de tranzacții**, nu „registrele contractelor derivate”.
4. Competența este împărțită operațional între CNPF și BNM, nu atribuită generic doar CNPF.
5. Pentru EMIR 3, proiectul trebuie fie să includă elementele de cont activ, monitorizare și calitatea datelor, fie să justifice expres nepreluarea lor în nota de fundamentare.

## Hartă minimă de competențe

| Actor | Rol preliminar în proiectul EMIR | Ancoră / risc |
|---|---|---|
| CNPF | piața de capital, societăți de investiții, OPC/administratori, participanți la piața de capital, eventual emitenți/contrapărți din perimetrul său | [[L-171-2012]] și [[L-192-1998]] oferă baza de piață de capital, dar nu acoperă toate contrapărțile EMIR. |
| BNM | bănci, asigurări/reasigurări, DCU și alte entități transferate la BNM sau supravegheate prudențial de BNM | [[L-178-2020]] și [[L-234-2016]] fac imposibilă o lege EMIR pur CNPF-only. |
| CNPF + BNM | schimb de date, raportări, risc sistemic, cooperare cu ESMA/autorități străine, decizii privind CPC/TR eligibile | Art. 22–25, 81, 83–84 EMIR impun cooperare și acces la informații. |
| Parlament / Guvern | lege primară, modificări conexe, norme de punere în aplicare și dosarul de armonizare | [[L-100-2017]] și [[HG-1171-2018]] cer clauză, tabel, notă și expertiză de compatibilitate. |

## Schelet de concordanță EMIR → Moldova

| EMIR | Funcție / obligație UE | Corespondent MD actual | Grad preliminar | Autoritate | Acțiune recomandată pentru proiect | Evidență |
|---|---|---|---|---|---|---|
| Art. 1 | Obiect și domeniu: clearing, gestionare bilaterală a riscurilor, reporting pentru contracte derivate, cerințe uniforme pentru CPC și registre centrale de tranzacții. | [[L-171-2012]] acoperă piața de capital și derivate doar în limitele sale; [[L-234-2016]] acoperă DCU/CSDR, nu regimul EMIR. | parțial / lacună | CNPF + BNM | Definește domeniul legii EMIR separat de L-171 și include contrapărți financiare, nefinanciare, CPC, registre centrale de tranzacții și locuri de tranzacționare unde este cazul. | `[raw/papers/cnpf/UE-648-2012-priority-articles-2026-07-09.md art.1]` |
| Art. 2 | Definiții: CPC, registru central de tranzacții, compensare, instrument financiar derivat, OTC derivative, contrapărți, clase de instrumente. | [[L-171-2012]] are categorii de instrumente financiare derivate, dar nu setul EMIR complet. | parțial | CNPF + BNM | Creează articol de definiții EMIR; păstrează termenii „CPC” și „registru central de tranzacții”; verifică armonizarea cu noțiunile din L-171 și L-234. | `[raw/papers/cnpf/UE-648-2012-priority-articles-2026-07-09.md art.2]` |
| Art. 3 | Tranzacții intragrup. | Nu este demonstrat un regim MD echivalent pentru derogări/condiții intragrup EMIR. | lacună / decizie | CNPF + BNM | Adaugă articol privind tranzacții intragrup, notificări, condiții de exceptare și rolul autorității competente. | `[raw/papers/cnpf/UE-648-2012-priority-articles-2026-07-09.md art.3]` |
| Art. 4 | Obligația de compensare pentru anumite contracte derivate extrabursiere. | Nu există în wiki o normă MD care să instituie obligația EMIR de clearing pentru OTC derivatives. | lacună | CNPF + BNM | Reglementează obligația de compensare, clasele eligibile, data aplicării, relația cu contrapărți din țări terțe și prevenirea eludării. | `[raw/papers/cnpf/UE-648-2012-priority-articles-2026-07-09.md art.4]` |
| Art. 4a | Contrapărți financiare supuse obligației de compensare și calculul pozițiilor. | Perimetru MD împărțit între CNPF și BNM; nu există mapping FC pe categorii EMIR. | lacună | CNPF + BNM | Definește contrapărțile financiare moldovenești pe categorii sectoriale și stabilește cine calculează/verifică pragurile. | `[raw/papers/cnpf/UE-648-2012-priority-articles-2026-07-09.md art.4a]` |
| Art. 4b | Servicii de reducere a riscurilor post-tranzacționare / PTRR. | Nu este identificată ancoră MD. | decizie de politică | CNPF + BNM | Include excepția/condițiile PTRR dacă se preia EMIR 3; dacă se omite, justifică în nota de fundamentare. | `[raw/papers/cnpf/UE-648-2012-priority-articles-2026-07-09.md art.4b]` |
| Art. 7a | Cont activ la o CPC autorizată în UE pentru anumite categorii de contracte. | Nu este identificată ancoră MD; proiectul anterior doar semnalează EMIR 3 ca decizie. | decizie de politică / lacună | CNPF + BNM | Decide includerea cerinței de cont activ sau justifică amânarea; dacă se include, corelează cu accesul la CPC eligibile. | `[raw/papers/cnpf/UE-648-2012-priority-articles-2026-07-09.md art.7a]` |
| Art. 7b | Monitorizarea obligației privind contul activ. | Nu este identificată ancoră MD. | decizie de politică / lacună | CNPF + BNM | Stabilește raportări periodice, indicatori de monitorizare și schimb CNPF-BNM. | `[raw/papers/cnpf/UE-648-2012-priority-articles-2026-07-09.md art.7b]` |
| Art. 7c | Informații privind prestarea serviciilor de compensare. | Nu este identificată ancoră MD. | lacună | CNPF + BNM | Creează obligații de informare pentru furnizori/contrapărți și competențe de colectare date. | `[raw/papers/cnpf/UE-648-2012-priority-articles-2026-07-09.md art.7c]` |
| Art. 7d | Informații privind compensarea prin CPC recunoscute conform art. 25. | Nu este identificată ancoră MD. | lacună | CNPF + BNM | Leagă raportarea națională de folosirea CPC din țări terțe recunoscute de ESMA. | `[raw/papers/cnpf/UE-648-2012-priority-articles-2026-07-09.md art.7d]` |
| Art. 7e | Informații privind CPC-urile din Uniune. | Relevant mai ales pentru modelul de eligibilitate CPC UE. | adaptare / decizie | CNPF + BNM | Decide ce informații se preiau prin registre/ESMA și cum se reflectă în registrul național de CPC eligibile. | `[raw/papers/cnpf/UE-648-2012-priority-articles-2026-07-09.md art.7e]` |
| Art. 9 | Obligația de raportare către registru central de tranzacții înregistrat sau recunoscut. | Scheletul național are capitol de raportare, dar terminologia și modelul operațional nu sunt finale. | parțial | CNPF + BNM | Definește obligația de raportare, responsabilitatea/delegarea, termenele, calitatea datelor, corectarea erorilor și accesul autorităților. | `[raw/papers/cnpf/UE-648-2012-priority-articles-2026-07-09.md art.9]` |
| Art. 10 | Contrapărți nefinanciare și praguri. | Nu există mapping MD pentru contrapărți nefinanciare EMIR. | lacună | CNPF + BNM / posibil alte autorități | Definește NFC, calculul pozițiilor, notificări și tratamentul grupurilor; decide dacă autoritatea principală este CNPF, BNM sau mecanism comun. | `[raw/papers/cnpf/UE-648-2012-priority-articles-2026-07-09.md art.10]` |
| Art. 11 | Tehnici de atenuare a riscului pentru OTC derivatives necompensate: confirmare, reconciliere, dispute, evaluare, garanții. | Scheletul anterior are capitol dedicat; nu există încă text normativ final sau norme secundare. | parțial | CNPF + BNM | Redactează obligații primare și mandate pentru norme secundare privind confirmare, reconciliere, comprimare, dispute, mark-to-market/model, garanții și derogări intragrup. | `[raw/papers/cnpf/UE-648-2012-priority-articles-2026-07-09.md art.11]` |
| Art. 12 | Sancțiuni. | [[L-192-1998]] oferă drepturi/sancțiuni generale CNPF, dar nu familii EMIR complete; BNM trebuie inclusă unde are mandat. | parțial / fail | CNPF + BNM | Construiește capitol operațional de supraveghere/sancțiuni: clearing, neraportare, calitatea datelor, risk mitigation, evidențe, necooperare, prestare neautorizată CPC/TR. | `[raw/papers/cnpf/UE-648-2012-priority-articles-2026-07-09.md art.12]` |
| Art. 14 | Autorizarea CPC stabilite în Uniune de autoritatea competentă a statului membru. | Moldova nu este stat membru; proiectul trebuie să evite formula greșită „CPC autorizate de ESMA”. | adaptare / decizie | CNPF + BNM | Nu copia un regim UE de autorizare dacă nu se creează CPC locală; folosește formularea „CPC autorizate în UE” plus mecanism național de acceptare. | `[raw/papers/cnpf/UE-648-2012-priority-articles-2026-07-09.md art.14]` |
| Art. 22 | Desemnarea autorității competente. | [[L-192-1998]] și [[L-171-2012]] dau CNPF piața de capital; [[L-178-2020]] și [[L-234-2016]] indică BNM pentru sectoare/infra. | parțial | Parlament / CNPF + BNM | Articol explicit de desemnare: CNPF și BNM în limitele competenței, plus mecanism de coordonare și schimb obligatoriu de date. | `[raw/papers/cnpf/UE-648-2012-priority-articles-2026-07-09.md art.22]` |
| Art. 23 | Cooperarea dintre autorități. | CNPF are bază generală de colaborare; BNM/DCU are colaborare în L-234, dar EMIR cere cooperare specifică. | parțial | CNPF + BNM | Detaliază cooperarea CNPF-BNM și cooperarea externă cu ESMA/autorități UE/SEE/de origine, inclusiv schimb de informații și notificări. | `[raw/papers/cnpf/UE-648-2012-priority-articles-2026-07-09.md art.23]` |
| Art. 24 | Situații de urgență. | Nu este identificat un regim EMIR dedicat de urgență. | lacună | CNPF + BNM | Adaugă competențe pentru măsuri urgente, schimb rapid de informații, suspendări/limitări și coordonare cu autorități străine. | `[raw/papers/cnpf/UE-648-2012-priority-articles-2026-07-09.md art.24]` |
| Art. 25 | Recunoașterea CPC stabilite în țări terțe. | Nu există regim MD demonstrat; scheletul are capitol de recunoaștere. | parțial | CNPF + BNM | Distinge CPC UE autorizate de CPC terțe recunoscute de ESMA; stabilește registru național, notificare/decizie, suspendare/retragere și efecte. | `[raw/papers/cnpf/UE-648-2012-priority-articles-2026-07-09.md art.25]` |
| Art. 39 | Segregare și portabilitate. | L-234/SFD/DCU pot fi conexe, dar nu acoperă direct CPC EMIR și portabilitatea pozițiilor clientului. | parțial / lacună | CNPF + BNM | Corelează conturi individuale/omnibus, protecția activelor, portabilitate, garanții financiare, insolvabilitate și SFD. | `[raw/papers/cnpf/UE-648-2012-priority-articles-2026-07-09.md art.39]` |
| Art. 48 | Proceduri în situații de default ale membrilor compensatori. | Nu este identificată ancoră MD pentru default CPC/clearing member în sens EMIR. | lacună | CNPF + BNM | Leagă procedurile CPC de insolvabilitate, finalitate, garanții și portabilitate; evită doar transpunerea izolată a art. 39(11). | `[raw/papers/cnpf/UE-648-2012-priority-articles-2026-07-09.md art.48]` |
| Art. 55 | Înregistrarea registrelor centrale de tranzacții la ESMA. | Moldova nu are regim TR echivalent; scheletul trebuie să decidă dacă acceptă TR UE/ESMA-recunoscute. | adaptare / lacună | CNPF + BNM | Nu crea „registru al contractelor derivate” ca substitut terminologic; stabilește TR eligibile și condițiile de folosire de entitățile MD. | `[raw/papers/cnpf/UE-648-2012-priority-articles-2026-07-09.md art.55]` |
| Art. 77 | Recunoașterea registrelor centrale de tranzacții din țări terțe. | Nu este identificată ancoră MD. | lacună / decizie | CNPF + BNM | Decide dacă se acceptă doar TR înregistrate UE și/sau TR terțe recunoscute de ESMA; prevede efectul retragerii recunoașterii. | `[raw/papers/cnpf/UE-648-2012-priority-articles-2026-07-09.md art.77]` |
| Art. 81 | Transparență și disponibilitatea datelor TR pentru autorități. | Nu există model demonstrat de acces CNPF/BNM la date TR EMIR. | lacună | CNPF + BNM | Prevede accesul CNPF/BNM la date, schimb intern obligatoriu, confidențialitate, calitatea datelor și eventual acces pentru stabilitate financiară. | `[raw/papers/cnpf/UE-648-2012-priority-articles-2026-07-09.md art.81]` |
| Art. 83 | Secret profesional. | Scheletul național are articol dedicat; CNPF/BNM au regimuri generale, dar textul trebuie acoperit EMIR-specific. | parțial | CNPF + BNM | Acoperă personal actual/fost, auditori, experți, CNPF, BNM, ESMA/autorități externe și excepții procedural-penale/civile/fiscale. | `[raw/papers/cnpf/UE-648-2012-priority-articles-2026-07-09.md art.83]` |
| Art. 84 | Schimbul de informații. | Scheletul are articol dedicat, dar trebuie corelat cu art. 81 și cooperarea externă. | parțial | CNPF + BNM | Introduce bază legală de schimb de informații, condiții de utilizare, confidențialitate, reciprocitate și schimb CNPF-BNM. | `[raw/papers/cnpf/UE-648-2012-priority-articles-2026-07-09.md art.84]` |
| Art. 89 | Dispoziții tranzitorii. | Proiectul MD are nevoie de tranziții proprii, dar HG1171 impune atenție specială pentru regulamente. | pending / decizie | Parlament / Guvern | Stabilește intrare în vigoare etapizată, termene IT/raportare/clearing, norme secundare și mecanism de abrogare/adaptare la aderare. | `[raw/papers/cnpf/UE-648-2012-priority-articles-2026-07-09.md art.89]` |

## Actualizare MD-TRANS după crearea scheletului

| Regulă | Status după această pagină | Observație |
|---|---|---|
| MD-TRANS-002 | improved / partial | CELEX, consolidarea și articolele prioritare sunt acum extrase explicit într-un raw suplimentar. |
| MD-TRANS-003 | partial | Există mapping preliminar UE→MD, dar nu încă pentru toate articolele EMIR și nu cu text de proiect. |
| MD-TRANS-004 | partial | Harta CNPF/BNM este explicită, însă responsabilitățile trebuie decise per articol în proiect. |
| MD-TRANS-006 | partial | Terminologia CPC/TR este fixată ca regulă; lipsește încă terminological map complet. |
| MD-TRANS-007 | pending/high risk | Dispozițiile tranzitorii pentru regulament UE trebuie redactate separat. |
| MD-TRANS-011 | improved / not complete | Scheletul de concordanță există; tabelul oficial complet încă lipsește. |
| MD-TRANS-013 | partial | Sunt folosite calificative preliminare, nu încă calificativele finale HG1171. |

## Întrebări de decizie înainte de text normativ

1. Moldova păstrează opțiunea unei CPC locale în viitor sau prima lege permite doar folosirea CPC UE/ESMA-recunoscute?
2. Raportarea se face exclusiv către registre centrale de tranzacții UE/ESMA-recunoscute sau se creează și un canal național CNPF/BNM?
3. Se preia EMIR 3 complet, inclusiv cont activ, monitorizare și calitatea datelor, sau se etapizează?
4. Cine este autoritatea principală pentru contrapărțile nefinanciare care nu intră clar în perimetrul CNPF/BNM?
5. Ce model național se folosește pentru sancțiuni: cod contravențional, lege sectorială EMIR, lege CNPF/BNM sau formulă mixtă?

## Următorul pas


Artefacte de execuție create pe baza acestei pagini: [[_archive/emir-2026-07/emir-draft-normative-package-phase-1-2026-07-09|emir-draft-normative-package-phase-1-2026-07-09]], [[_archive/emir-2026-07/emir-draft-complet-2026-07-10|emir-draft-complet-2026-07-10]] și [[_archive/emir-2026-07/emir-audit-conformitate-lege100-hg1171-2026-07-10|emir-audit-conformitate-lege100-hg1171-2026-07-10]]. Draftul din 2026-07-10 transformă rândurile prioritare în text normativ complet și audit procedural Legea 100/HG1171.

Transformarea acestei pagini în tabel oficial cere două lucruri: (1) text de proiect pe articole, inclusiv modificări conexe; (2) completarea calificativelor de compatibilitate HG1171 pentru fiecare rând. Până atunci, această pagină este instrumentul de lucru pentru redactarea și verificarea proiectului EMIR.

## Linkuri interne

- [[_archive/emir-2026-07/test-metoda-transpunere-emir-2026-07-09|test-metoda-transpunere-emir-2026-07-09]]
- [[_archive/emir-2026-07/verificare-schelet-lege-emir-2026-07-03|verificare-schelet-lege-emir-2026-07-03]]
- [[acquis-CSDR-EMIR]]
- [[cnpf-transposition-matrix]]
- [[moldova-eu-transposition-method]]
- [[moldova-eu-transposition-rule-matrix]]
- [[L-171-2012]] · [[L-192-1998]] · [[L-178-2020]] · [[L-234-2016]]
