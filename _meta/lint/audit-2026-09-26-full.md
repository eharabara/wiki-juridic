# Full lint audit — 2026-09-26

Read-only audit after the expansion of 21–25 September. Nothing in `raw/`, `entities/`, `concepts/`,
`comparisons/`, `index.md`, `log.md` or `CLAUDE.md` was modified. Every finding below was checked
against the files, not against a summary. Scripts used are ad hoc and not committed.

## What the existing tooling says

| control | result |
|---|---|
| `close_session.py --check` | in-force register, HCC register, citation graph, coverage block, SCHEMA.md: all current |
| `validate_wiki.py --report` (with hashes) | **0 errors, 3 warnings**; 274 structured pages, 633 raw sources, 633 sha256 verified |
| git | working tree clean, `main` level with `origin/main` |

The three warnings: `legal-career/06-matter-log.md` stale (D9, taken 2026-09-25), and the BNM slide
deck `236__Prezentare_RI_mai_2025.pdf.md` twice (known since 2026-09-05).

Clean on checks no script runs: every structured page is in `index.md` and every index link
resolves; no structured page cites, by anchor, any of the 257 rows of the in-force register;
`L-133-2011` and `COD-3-2009` are cited only with their repeal stated; the 46 `viitor/` files are
linked only from `concepts/consolidari-viitoare-ingerate.md`.

## A. Findings

**A1 — Three acts of commit 24c0918 (2026-09-25) bypassed the ingest pipeline, and the coverage
table calls them sound.** `COD-1316-2000` (Codul familiei, ~130 `**Articolul N.**` lines, 0 anchors),
`L-69-2016` (notaries, ~70 lines, 0 anchors) and `L-230-2022` (copyright: 66 anchors, 61 article
lines left unanchored, e.g. art. 58 at line 1534, art. 99 at line 2907). All three carry
`extract_method: web_extract`, no `consolidation_date`, no fișă, and were never run through
`verify_business_law.py`. Consequences: no article of these acts can be cited as anchored; the
in-force, HCC and staleness checks cannot see them (no date to compare); 16 of the 60 unresolved
groups in the citation graph are artefacts of `L-230-2022` (art. 58 ×11, 99 ×9, 103 ×9 exist in
the text); the coverage table reports "no article structure" and "clean". No structured page yet
cites an article of the three. Fix: re-ingest from legis.md with `ingest_business_law.py`, which
needs a download (Eugen's yes per file). Tooling gap: nothing flags a line-initial article heading
that carries no anchor; a validator rule for that would have caught it the same day.

**A2 — Entity pages still describe the version held before the 4 September refresh.**
- `entities/L-1134-1997.md`: "în vigoare — doc_id 129078". Held: doc_id 154811, consolidation
  **2028-01-01**, with arts. 73^3 and 73^4 introduced by LP92/2026 and not in force. The page never
  mentions the future date or the register.
- `entities/L-192-1998.md`: doc_id 128124; held 150996, consolidation 2026-01-01.
- `entities/L-100-2017.md`: "extras la 2026-07-09", last amendment LP174/2024; held 153007,
  consolidation 2025-12-31.

**A3 — The moldova-legal manifest has no per-act row for 56 acts.** The 54 target acts of section AV
are recorded as a batch, not act by act (doc_id, consolidation, confidence); 43 of the 46 `viitor/`
files are not named (section AX is generic). The data lives in the raw frontmatter and entity pages.
A decision, not necessarily a defect: CLAUDE.md tells the reader to use the manifest before citing.

**A4 — 54 mechanical entity pages** (`confidence: medium`, "Pagină mecanică"), acts not read in full.
Known (manifest AV, "Neexecutat").

**A5 — The unresolved-references table has grown and is not re-verified.** 218 references in 60
groups. The exhaustive check of 16–19 September covered the smaller corpus. Of the 60 groups: 16 are
A1 artefacts, 13 `CC-1107-2002` and 12 `AA-2014` belong to the known clusters, and the rest
(`COD-150-2014` ×4, `L-212-2004`, `COD-218-2008`, `COD-122-2003`, `COD-116-2018` ×2 each, and single
rows) are unchecked.

**A6 — Hand-written text in CLAUDE.md out of date.**
- `_meta/lint/` entry: "currently surface 4 orphan pages and ~149 page-level citations". Both counts
  are 0 since the fixes of 2026-09-17 (commit 26af056).
- "Where things are" does not mention the 54-act permissive perimeter
  (`concepts/perimetrul-actelor-permisive.md`), nor the three acts of A1; `viitor/` appears only in
  Outstanding work 7.
- Manifest AV still ends "consolidările viitoare (23) neingerate", superseded by section AX.

**A7 — D9.** The matter log copy was taken on 2026-09-25; the current register is needed from the
project before this vault is used on a matter today.

## B. Still open, unchanged

`L-283-2003` stale count line (48 vs 46 anchors); the BNM slide deck with no extractable text; the
prose deferrals the in-force register cannot read (CLAUDE.md open question 9).

## C. Remediere (aceeași zi, la cererea lui Eugen)

| constatare | stare |
|---|---|
| A1 trei acte fără ancore | **făcut.** Reingerate cu ruta standard după ce Eugen a trecut bifa: `COD-1316-2000` 155707, `L-69-2016` 137679, `L-230-2022` 149374, plus două versiuni viitoare; HCC23/2024 recuperată; graful 187 → 126 nerezolvate |
| A1 unealta | **făcut.** `raw.unanchored-article` în validator și spec; 7 articole reale ancorate în `COD-150-2014` (5), `COD-246-2024`, `L-100-2017`; `verify_business_law.py` 0 eșecuri |
| A2 pagini vechi | **făcut.** `L-1134-1997`, `L-192-1998`, `L-100-2017`, `HG-1171-2018`; în plus corectate citări greșite (capitalul minim art. 38 alin. (2); art. 3 și art. 4 din `L-192-1998`) |
| A3 manifest | **făcut altfel:** registru generat `_meta/coverage/act-register.md`, în `close_session.py` |
| A4 pagini mecanice | **deschis:** coada de citire e în registru; cele 54 de acte nu s-au citit integral |
| A5 trimiteri nerezolvate | **făcut.** Toate rîndurile în afara clusterelor cunoscute citite; un singur fapt real: `L-108-2016` art. 105^1 și `L-212-2004` art. 42 citează art. 17-20 abrogate (CLAUDE.md, întrebarea 8) |
| A6 CLAUDE.md | **făcut** |
| A7 D9 | **făcut**, reștampilat la 2026-09-26 (Eugen: registrul nu s-a schimbat) |

Avertismentele validatorului rămase: 2, prezentarea BNM 236.

## D. Rămășițele, reluate la cererea lui Eugen

| item | stare |
|---|---|
| paginile mecanice (A4) | **făcut pe jumătate.** Afirmațiile vechi corectate, rezumat mecanic al modificărilor + probă de sincronizare pe toate cele 54; **nu** citite integral actele (nu se poate face onest mecanic) |
| consolidări vechi | 34 din 36 sînt încă cele mai noi; `HG-1171-2018` are 156468 @ 22.09.2026, `L-23-2008` și `L-24-2008` cîte o viitoare (156490, 156492): **deschis**, blocat de Cloudflare |
| amînări în proza (întrebarea 9) | script de candidați, 52 de linii; **COD-95-2021** art. 49, 140, 180, 336, 337 de la 01.01.2027 adăugat în registru |
| avertismente validator | 0: prezentarea BNM 236 declarată `image-only-slides`, `ro`; `L-283-2003` rîndul de număr corectat |
| `L-100-2017` art. 25-26 | **deschis**, cere istoricul de versiuni de pe legis.md |
| `HCC23/2024` decizia însăși | **deschis**, aceeași cauză |
