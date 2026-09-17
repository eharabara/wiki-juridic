# wiki-juridic

Bază de cunoștințe despre dreptul Republicii Moldova, construită ca să fie interogată de un model
de limbaj, nu citită de la un capăt la altul. Perimetrul principal: legile CNPF și BNM, codurile,
dreptul societăților, actele normative și extrasele din acquis-ul UE. Un al doilea perimetru ține
documentele de politici din jurul lor. Proprietar: Eugen Harabara, Chișinău.

## Cum e construit

| Strat | Unde | Ce este |
|---|---|---|
| Text brut | `raw/papers/` | textul actelor de pe legis.md și EUR-Lex, imuabil, cu hash și ancore de articol; corpusul BNM |
| Structurat | `entities/`, `concepts/`, `comparisons/`, `queries/` | rezumate și analize; fiecare pagină poartă `perimeter: legal` sau `policy` |
| Control | `_meta/schema/`, `_meta/coverage/`, `_meta/inforce/` | specificația mecanică, verificatorul, generatorul de acoperire, registrul dispozițiilor neintrate în vigoare |
| Arhivă | `_archive/` | conținut înghețat, cu note de proveniență |

Regulile de lucru sunt în `CLAUDE.md`. Schema, cu partea mecanică generată din
`_meta/schema/schema-spec.yaml`, e în `SCHEMA.md`. Jurnalul deciziilor e `log.md`.

## Ce nu e aici

Folderele `original/` (PDF și DOCX descărcate, circa 576 MB) rămân doar pe disc; sunt
redescărcabile de la sursă. Dosarele de client nu au fost niciodată parte din depozit.

## Verificare

```bash
python _meta/schema/validate_wiki.py --report
python _meta/coverage/build_coverage.py --check
```

Prima comandă iese cu cod 1 dacă o regulă din specificație e încălcată. A doua spune dacă
secțiunea de acoperire din `CLAUDE.md` mai corespunde fișierelor.

## Stare

Starea live a corpusului, lacunele confirmate și controalele generate sunt în
`CLAUDE.md`. Acest README păstrează numai orientarea de intrare, pentru a nu
duplica un statut care se poate învechi.
