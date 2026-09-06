# Raport de execuție — planul de extindere a perimetrului de drept intern

Data: 6 septembrie 2026, seara
Plan executat: `_meta/plans/2026-09-06-plan-extindere-perimetru-domestic.md`
Stare: **pasul 1 executat și comis. Pașii 2, 3 și 4 nu au putut începe: legis.md nu a fost accesibil.**
Acest raport se rescrie când execuția se reia.

## 0. Condițiile prealabile (secțiunea 3 a planului)

| condiție | rezultat |
|---|---|
| `git status` curat pe `main` | da, la `d951aa6` |
| validator la zero erori înainte de a începe | 0 erori, 2 avertismente (cele cunoscute: `236__Prezentare_RI_mai_2025`, COM(2024) 469) |
| `build_coverage.py --check` | la zi |
| citite: `SCHEMA.md`, `CLAUDE.md`, manifestul moldova-legal, `ingest_business_law.py`, `verify_business_law.py` | da, integral |

## 1. Tabelul sondajului de actualitate

**Nu s-a produs.** Sondajul cere, pentru fiecare din cele 53 de acte cu `doc_id`, istoricul de versiuni de pe legis.md. Site-ul stă în spatele verificării Cloudflare („Just a moment… Performing security verification"), care a rămas nerezolvată după 20 de secunde de așteptare în browserul integrat și după 15 secunde în Chrome-ul lui Eugen (fila 256310526, lăsată deschisă pe `getResults?doc_id=152650`). Regula consemnată la 5 septembrie este că bifa Turnstile o trece Eugen, nu agentul, deci nu s-a apăsat nimic.

Ce este pregătit pentru când accesul revine, în `_meta/plans/` nu, ci în scratchpad-ul sesiunii (`inventory.json`): lista celor **53 de acte** în perimetru, cu `doc_id`, data consolidării și linia ultimei modificări din frontmatter. Fișierele `UE-*` și cele cu `source_type: translation` sunt excluse, cum cere planul.

Controlul suplimentar cerut de documentul 05, actele pe care `build_coverage.py` le sare fiindcă `latest_modification_line` începe cu „Publicat": **2 acte**, `L-177-2025` (149610) și `L-178-2020` (123148). Alte **4 acte** poartă `never_amended: true` cu linia de modificare goală, deci intră în aceeași clasă de verificat: `DCA-61-2024` (142648), `HG-574-2024` (144682), `L-160-2023` (137939), `L-250-2017` (105629). Toate șase se verifică prin aceeași interogare când accesul revine.

Numărul de acte pe fiecare stare: **nerezolvat 53** (interogarea nu a răspuns), curent 0, wiki în urmă 0, legis.md în urmă 0.

## 2. doc_id-urile celor 14 acte noi

**Niciunul găsit**: căutarea pe legis.md nu a fost posibilă. Singurul cunoscut din plan, 86850 pentru Statutul profesiei de avocat, **nu a fost confirmat pe pagina actului** și rămâne, conform regulii lui Eugen, nerezolvat.

## 3. Lacune D5

Nu s-a putut stabili dacă Codul deontologic și Regulamentul stagiului sunt pe legis.md. Nimic consemnat în manifest, fiindcă o lacună se consemnează după căutare, nu înaintea ei.

## 4. Validatorul și tabelul de acoperire

Validator după pasul 1: **0 erori, 2 avertismente**, aceleași ca înainte. Spec versiunea 2026-09-06.

Tabelul de acoperire: **neschimbat** (53 de acte primare, 29 extrase UE, 284 documente BNM). Pasul 1 nu atinge `raw/`.

Ce a făcut pasul 1, verificabil în `git show 0056fea`:
- eticheta `unverified` adăugată în spec la `document_and_knowledge_types`; `SCHEMA.md` regenerat;
- cele 17 pagini `concepts/acquis-*.md` și `comparisons/cnpf-transposition-matrix.md`: `confidence: medium` → `low`, eticheta `unverified`, `updated: 2026-09-06`, paragraful unic sub H1; nimic altceva modificat în corp;
- editare la nivel de octet, cu terminatorii de linie ai fiecărui fișier păstrați. Observație de metodă: `schema-spec.yaml` este CRLF în depozit, iar prima scriere l-a convertit la LF (diferență pe 468 de linii); restaurat înainte de commit, diferența finală este de 2 linii.

## 5. Anomalii

Nimic nou: nicio numerotare, consolidare viitoare sau articol absent nu a fost examinat, fiindcă nu s-a ingerat nimic.

## 6. Commit-uri

| commit | pas |
|---|---|
| `0056fea` | Pasul 1: înghețarea stratului de constatări acquis |

Fără push, conform regulii.

## Ce trebuie de la Eugen ca execuția să continue

Trecerea verificării Cloudflare o singură dată în Chrome, pe fila legis.md lăsată deschisă. După aceea sesiunea reia de la pasul 2 și se oprește din nou, cum cere D6, cu tabelul sondajului înainte de pasul 3.
