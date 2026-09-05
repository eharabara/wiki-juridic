# Proveniența arhivei EMIR

Arhivat: 2026-09-05, pasul P3 din `_meta/plans/2026-09-05-plan-restructurare-wiki.md`, decizia D7.

## Ce este aici

Cinci pagini de lucru din iulie 2026, mutate neschimbate din `queries/`:

| Fișier | Ce este | Creat |
|---|---|---|
| `verificare-schelet-lege-emir-2026-07-03.md` | sinteză asupra scheletului DOCX de lege EMIR și a comentariilor lui | 2026-07-03 |
| `test-metoda-transpunere-emir-2026-07-09.md` | test al metodei și matricei de reguli de transpunere pe cazul EMIR | 2026-07-09 |
| `emir-draft-normative-package-phase-1-2026-07-09.md` | pachet de soluții normative EMIR, faza 1 | 2026-07-09 |
| `emir-draft-complet-2026-07-10.md` | draft complet de lucru pentru legea EMIR | 2026-07-10 |
| `emir-audit-conformitate-lege100-hg1171-2026-07-10.md` | audit procedural Legea 100/2017 și HG 1171/2018 asupra draftului | 2026-07-10 |

Mutarea s-a făcut cu `git mv`, deci istoricul lor începe la prima înregistrare din 2026-09-05.

## De ce au fost retrase din `queries/`

Sunt artefacte de redactare pentru un proiect de lege, nu răspunsuri la întrebări de cercetare. Rămân în vault, nu se șterg, pentru că două pagini analitice active își sprijină afirmațiile pe ele: [[emir-concordance-skeleton]] și [[acquis-CSDR-EMIR]]. Legăturile din acele pagini au fost redirecționate aici la aceeași dată.

## Ce trimite încă la ele din `raw/`

Două fișiere din `raw/papers/cnpf/` le citează prin wikilink: `_manifest.md` (rândurile pentru `md-2026-07-03-schelet-lege-emir`, `UE-648-2012-priority-articles-2026-07-09` și `md-2026-07-09-proiect-lege-emir-completat`) și `md-2026-07-03-schelet-lege-emir.md` (două locuri). Decizie (Eugen, 2026-09-05, punctul deschis 3 din plan): **cele două fișiere nu se editează.** Regula „`raw/` este imuabil” rămâne fără excepții. Legăturile lor sunt **redirecționate declarat** aici:

| Din | Legătura | Ținta reală |
|---|---|---|
| `raw/papers/cnpf/_manifest.md` | `[[verificare-schelet-lege-emir-2026-07-03]]` | `_archive/emir-2026-07/verificare-schelet-lege-emir-2026-07-03.md` |
| `raw/papers/cnpf/_manifest.md` | `[[emir-concordance-skeleton]]` | `comparisons/emir-concordance-skeleton.md` (nemutat) |
| `raw/papers/cnpf/_manifest.md` | `[[emir-draft-complet-2026-07-10]]` | `_archive/emir-2026-07/emir-draft-complet-2026-07-10.md` |
| `raw/papers/cnpf/_manifest.md` | `[[emir-audit-conformitate-lege100-hg1171-2026-07-10]]` | `_archive/emir-2026-07/emir-audit-conformitate-lege100-hg1171-2026-07-10.md` |
| `raw/papers/cnpf/md-2026-07-03-schelet-lege-emir.md` (două locuri) | `[[verificare-schelet-lege-emir-2026-07-03]]` | `_archive/emir-2026-07/verificare-schelet-lege-emir-2026-07-03.md` |

Obsidian rezolvă wikilink-urile după numele fișierului, deci ele funcționează și fără editare. Verificatorul (`_meta/schema/validate_wiki.py`) tratează wikilink-urile din `raw/` către pagini din `_archive/` ca excepție declarată, pe baza acestui tabel.

## Statut

Conținut înghețat. Nu se actualizează. O reluare a lucrării EMIR pornește o pagină nouă, care poate cita de aici.
