# Full lint audit — 2026-09-05

Read-only audit. Nothing in `raw/`, `entities/`, `concepts/`, `comparisons/`, `queries/`,
`index.md` or `log.md` was modified. Every claim below was checked against the files themselves,
not against a summary.

## What the existing tooling says

| tool | result |
|---|---|
| `_meta/schema/validate_wiki.py --all` | **0 errors**, 280 warnings; 91 structured pages, 378 raw sources, 378 sha256 verified |
| `_meta/coverage/build_coverage.py --check` | up to date |
| `_meta/schema/build_schema.py --check` | up to date |
| `_meta/inforce/build_inforce_register.py --check` | up to date, 47 provisions |
| `_meta/lint/run_cnpf_legal_lint.py` | 10 "broken wikilinks", 757 "invalid tags", 4 orphans — see A1/A2, most of this is false |

The form of the vault is sound. The findings below are the ones no script currently reports.

---

## A. The July legal lint is broken against the September schema

**A1 — `invalid_tags: 757` is entirely false.** `allowed_tags()` (line 78) builds its allowlist by
scraping `SCHEMA.md` for `^- ([a-z0-9-]+)$`. The D4 rewrite of 2026-09-05 moved the taxonomy into
the generated block, where tags are written as comma-separated code spans. The regex now matches
**nothing**: `allowed_tags()` returns an empty set, so every tag on every page is reported invalid.
All 46 distinct flagged tags (`moldova`, `entity`, `cnpf`, `legal-act`, …) are in
`_meta/schema/schema-spec.yaml`. Verified: `set(flagged) - set(spec taxonomy) == ∅`.

**A2 — `broken_wikilinks: 10` is also false.** All ten are the five
`[[_archive/emir-2026-07/…]]` targets cited from `concepts/acquis-CSDR-EMIR.md` and
`comparisons/emir-concordance-skeleton.md`. All five files exist. The script predates
`wikilinks.path_only_targets`, so it cannot resolve an explicit archive path — which the spec
*requires* for archive targets.

**Consequence.** `_meta/lint/cnpf-legal-lint-2026-09-05.md` is committed to git and opens with
"Ridicat: 10 / Mediu: 807 / Scăzut: 814". Those totals are noise. It is the file a reader would
open first.

**A3 — but it checks two things the validator does not**, and they are worth keeping:
- **orphan pages** — a page nothing links to (see D1);
- **`page_level_raw_refs`** (21) — a claim cited to a whole raw file rather than to an article,
  which is a citation-discipline check that belongs in this vault.

**A4 — its scope is stale.** It reads only `raw/papers/cnpf/` (46 files). It has never seen
`raw/papers/moldova-legal/` or `raw/papers/bnm/legal-ro/`, i.e. most of the corpus.

**A5 — running it writes to `log.md`, and breaks it.** This was found by running the script and
watching the vault change under it. It does two things nobody asked for:

1. It **appends a journal entry that violates D8** — no `**Aflat:**` / `**Decis:**` / `**Unde:**`
   lines, just a scope-and-counts dump. `validate_wiki.py` goes from 0 errors to 1
   (`log.fields`) the moment it runs. And the entry publishes the false numbers from A1 and A2
   into the journal: *"broken wikilinks=10, invalid tags=757"*.
2. It **rewrites the whole file from LF to CRLF**, so `git diff` shows 101 lines changed when one
   entry was added, and the real change is unreadable.

During this audit the script was run with its output redirected to a scratch directory, but the
`log.md` write is hardcoded and happened anyway. `log.md` was restored with
`git checkout -- log.md`; the validator is back to **0 errors** and the file is back to LF.
Anyone who has run this script since the D4 rewrite should check whether a stray entry is sitting
in their journal.

**Recommendation.** Retire the script or port A3's two checks into `validate_wiki.py` against the
spec. Do not leave it running as it is: its report reads as authoritative, is 97% false, and it
mutates the journal on every run.

---

## B. Article-number gaps not recorded anywhere

Census across all 49 anchored acts. A gap counts as *explained* only where an article-level or
higher marker sits between the surrounding anchors (`Articolul N … abrogat`, a range marker, or
`Capitolul/Secțiunea … abrogat`). A paragraph-level `(3) - abrogat.` explains nothing about a
missing article, and a bare `## Capitolul V` heading with no repeal word explains nothing either.

**31 gap runs found: 16 explained, 15 unexplained, 51 articles absent with no marker.**

Already in CLAUDE.md (open questions 3, 4, 6): `COD-154-2003` 226–244, `COD-218-2008` 441,
`COD-225-2003` 78, `L-548-1995` 12–13, 29–30, 48, 54, 73. All confirmed present, exactly as
described.

**New — 5 acts, 23 articles, not recorded in CLAUDE.md:**

| act | absent | note |
|---|---|---|
| `raw/papers/cnpf/L-234-2016.md` | **art. 24, arts. 27–35** (10) | Depozitarul central unic. Anchors run 1–23, 25, 26, 36–47. Between art. 26 and art. 36 sits only `## Capitolul V ACTIVITATEA DEPOZITARULUI CENTRAL UNIC` — a chapter heading, not a repeal. CNPF perimeter, CSDR-relevant. |
| `raw/papers/moldova-legal/COD-154-2003.md` | **arts. 374–382** (9) | A *second* run in the labour code. CLAUDE.md records only 226–244. |
| `raw/papers/moldova-legal/L-100-2017.md` | **art. 52** | See B-bis below — it is present but invisible. |
| `raw/papers/moldova-legal/L-220-2007.md` | **art. 6** | Only `## Capitolul II` between arts. 5 and 7. |
| `raw/papers/moldova-legal/L-845-1992.md` | **arts. 21, 31** | Nothing at all between the neighbours. |

`L-234-2016` is the one to look at first: ten absent articles in a CNPF-perimeter law, and the
coverage table calls it "37 articles, 37 anchors, clean" — true mechanically, while the numbering
runs to 47 with two holes in it.

### B-bis. A second instance of the `Aricolul 78` trap

`raw/papers/moldova-legal/L-100-2017.md` line **531** reads:

```
Articol 52. Punctul
```

`Articol`, not `Articolul`. The line takes no anchor, so `## Articolul 52` returns nothing and
art. 52 reads as an unexplained gap — exactly the trap recorded for `COD-225-2003` art. 78.
It matters more than the average article: art. 52 of the law on normative acts is the provision
governing **puncte**, which is how every HG in this vault is cited, and section M of the
moldova-legal manifest already notes that a citation to "pct. N" is not anchored.

Not corrected — rewriting legal text is forbidden here. Recorded for `[de verificat]`.

---

## C. Two claims in CLAUDE.md that the files no longer support

**C1 — Outstanding work item 2 is obsolete, and it points at the wrong file.**
It reads: *"Decide whether to unwrap the Civil Code body. 60.2 percent of its non-empty lines
continue mid-sentence."* Measured today on `CC-1107-2002.md`: 13,190 non-empty lines,
**22 true mid-sentence continuations — 0.2%**, and **0 anchors with a title cut by a line break**.
The code was evidently re-ingested cleanly on 2026-09-04 and the item was never updated.

The concern is real, but it belongs to the other acts. Excluding enumerations (`a)`, `(1)`, …):

| act | non-empty lines | true continuations | |
|---|---:|---:|---:|
| `COD-985-2002` (penal) | 4,827 | 1,338 | **27.7%** |
| `L-62-2022` (publicitate) | 705 | 82 | 11.6% |
| `L-171-2012` (piața de capital) | 2,364 | 162 | 6.9% |
| `CC-1107-2002` (civil) | 13,190 | 22 | 0.2% |

Corpus-wide, **3,097 anchors carry a title cut in half by a line break** — every one of the 42
anchored acts is affected, worst in `COD-218-2008` (466), `COD-122-2003` (301), `COD-985-2002`
(276), `COD-95-2021` (205), `COD-1163-1997` (203). Practical harm: a title search fails, and a
quoted heading is incomplete. `## Articolul 7. Stabilirea, modificarea şi anularea` in Codul
fiscal loses `impozitelor şi taxelor de stat şi locale` to the next line.

**C2 — One article in the corpus is numbered `54^1/1`.**
`COD-1163-1997.md` line 2300: `## Articolul 54^1/1. Perioada fiscală`. It is the only occurrence
of the `N^X/Y` form in the whole vault. The standard pattern `Articolul (\d+(?:\^\d+)?)` — used by
this audit, and worth checking in the ingest and citation helpers — truncates it to `54^1`, which
collides with the real art. 54^1 at line 2285. A search for art. 54^1 returns two articles.

**C3 — Codul fiscal's own table of contents disagrees with its body**, in both directions:
arts. 208–213 are listed in the CUPRINS as `- abrogat.` but carry no body anchor (the body has
`## Capitolul 10 - abrogat.`, so the absence *is* explained — but `## Articolul 208` returns
nothing); and art. 189^1 is anchored in the body while absent from the CUPRINS.

---

## D. Structured layer

**D1 — three orphan pages**, all created today by P8-bis. Nothing in the vault links to them
(`index.md` excluded, since it lists everything and so cannot show reachability by meaning):

- `entities/L-239-2008.md`
- `entities/L-250-2017.md`
- `entities/L-550-1995.md`

Each needs at least one inbound link from the page whose gap it fills — 550/1995 from the banking
pages, 250/2017 from the conglomerates material, 239/2008 from wherever transparency in
decision-making is argued.

**D2 — the in-force discipline holds. Clean pass.** Checked every structured page against the 47
provisions in `_meta/inforce/in-force-register.json` at provision level, not act level.
**No page cites a provision that is not yet in force.** (An act-level check is worthless here:
most of `L-171-2012` binds today; only arts. 38 and 141^1 do not.)

**D3 — 19 pages under 15 body lines**, mostly policy-perimeter stubs (`entities/HG-650-2023.md`
and `entities/HG-841-2024.md` at 9 lines are the thinnest). The spec sets a ceiling for splitting
a page but no floor. Informational.

---

## E. Hygiene

**E1 — a stray duplicate at the vault root.**
`Claude outputs/2026-09-05-plan-restructurare-wiki.md` is **byte-identical** (md5
`de7159ec…`) to `_meta/plans/2026-09-05-plan-restructurare-wiki.md`. It is tracked in git, sits
outside every folder the spec knows (structured, raw, `_archive`, `_meta`), is therefore validated
by nothing, and Obsidian will index it as a note. Delete the root copy; `_meta/plans/` is where
CLAUDE.md says plans live.

**E2 — 278 of the 280 validator warnings carry no information.** They are `raw.language-other` on
the BNM corpus, all from the bulk ingest of 2026-07-12. They are mechanically resolvable: the
`source_record` URL states the language (`bnm.md/en/content/…` vs `bnm.md/ro/content/…`), and the
filenames agree (`Annual_Report_2024.pdf` → en, `Recomandare OCDE_ro.pdf` → ro). Setting them
would take the warning count from 280 to about 2 and make the next warning that matters visible.

**E3 — the one `raw.translation-undeclared` warning is a false positive.**
`raw/papers/mded-policy-2024/eu-reform-growth-facility-moldova-2024.md` is COM(2024) 469 final,
publisher European Commission, `language: en` — an English **original**, not a translation of a
Moldovan act. The rule (`legal-text` + 20 or more `Article N` lines) should be narrowed to the
Moldovan and BNM roots rather than satisfied by relabelling a Commission document.

**E4 — `copy.stale`, live.** `legal-career/06-matter-log.md` was taken 2026-09-04. D9 requires a
refresh from the project at the start of any session that touches the wiki, then a re-stamp with
`python _meta/schema/stamp_copies.py`.

---

## Suggested order of work

1. **`L-234-2016` arts. 24 and 27–35** — verify against legis.md, mark `[de verificat]`, and say
   in CLAUDE.md whether the file is an incomplete extract. It is the only finding that can change
   an answer about the CNPF perimeter.
2. **`L-100-2017` art. 52** — record the trap next to the `COD-225-2003` art. 78 one.
3. **CLAUDE.md corrections** — close outstanding-work item 2 for the Civil Code, reopen it against
   `COD-985-2002`; add the new gaps to open question 3; add `54^1/1` to open question 2.
4. **Retire or fix `run_cnpf_legal_lint.py`** (A1–A5), porting the orphan-page and
   page-level-raw-ref checks into the validator. Until then it should not be run at all: it
   writes a D8-breaking entry into `log.md` every time.
5. **`language: other`** — one script, 278 warnings gone.
6. **Delete `Claude outputs/`**; link the three orphan pages.
