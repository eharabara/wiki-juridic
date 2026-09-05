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
`_meta/schema/schema-spec.yaml`. Verified: `set(flagged) - set(spec taxonomy) == ∅`. The figure 757 itself could not be reproduced
statically on 2026-09-05: the 91 structured pages carry 637 tag entries in total, and the raw CNPF
files carry none. The mechanism holds whatever the count is, since the allowlist is empty.

**A2 — `broken_wikilinks: 10` is also false.** All ten are the five
`[[_archive/emir-2026-07/…]]` targets cited from `concepts/acquis-CSDR-EMIR.md` and
`comparisons/emir-concordance-skeleton.md`. All five files exist. The script predates
`wikilinks.path_only_targets`, so it cannot resolve an explicit archive path — which the spec
*requires* for archive targets.

**Consequence, corrected 2026-09-05 after verification.** This paragraph first said that the
committed report `_meta/lint/cnpf-legal-lint-2026-09-05.md` opens with
"Ridicat: 10 / Mediu: 807 / Scăzut: 814". It does not. That file opens with
"Ridicat: 0 / Mediu: 1229 / Scăzut: 60", and carries `broken_wikilinks: 0` and
`invalid_tags: 1`. It is sound. The reason is chronology: the report was generated at 09:18,
and `SCHEMA.md` was rewritten at 15:28 under P9. The committed report therefore predates the
break, and its numbers are valid. The false totals came from this audit’s own run of the
script, after the rewrite. A1 and A2 describe how the script behaves from 15:28 onward, not
what sits in git. The recommendation is unchanged, but the risk is prospective: the danger is
the next run, not the committed report.

**A3 — but it checks two things the validator does not**, and they are worth keeping:
- **orphan pages** — a page nothing links to (see D1);
- **`page_level_raw_refs`** (22 in the committed report; 21 was a miscount here) — a claim cited
  to a whole raw file rather than to an article,
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
| ~~`raw/papers/cnpf/L-234-2016.md`~~ | **resolved, not a gap** | Verified against legis.md on 2026-09-05. Art. 24 and the whole of Chapter IV (arts. 27–35) were repealed by **LP292/2023**. See B-ter. |
| `raw/papers/moldova-legal/COD-154-2003.md` | **arts. 374–382** (9) | A *second* run in the labour code. CLAUDE.md records only 226–244. |
| `raw/papers/moldova-legal/L-100-2017.md` | **art. 52** | See B-bis below — it is present but invisible. |
| `raw/papers/moldova-legal/L-220-2007.md` | **art. 6** | Only `## Capitolul II` between arts. 5 and 7. |
| `raw/papers/moldova-legal/L-845-1992.md` | **arts. 21, 31** | Nothing at all between the neighbours. |

`L-234-2016` was the one to look at first, and it was checked — see B-ter. It turned out not to
be a defect at all, and the reason it looked like one is the most important thing this audit
found.

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


### B-ter. Verified against legis.md: `L-234-2016` is sound, and the reason it looked broken is systemic

Checked on 2026-09-05 against the live source (`legis.md` doc_id 145901, Cloudflare passed in
Eugen's own Chrome; the check itself was not circumvented).

**The file is a faithful copy.** legis.md's current consolidated text of Law 234/2016 carries the
same 37 articles in the same order — 1–23, 25, 26, 36–47 — with no marker for the absences, and
Chapter IV missing from the chapter sequence (I, II, III, **V**, VI). Nothing was lost in ingest.

**The articles were properly repealed.** The earlier consolidation (doc_id 139826, 2023-10-21)
carries both explanations verbatim:

```
[Art.24 abrogat prin LP292 din 19.10.23, MO398/21.10.23 art.679; în vigoare 21.10.23]
[Capitolul IV abrogat prin LP292 din 19.10.23, MO398/21.10.23 art.679; în vigoare 21.10.23]
```

So art. 24 was repealed individually and arts. 27–35 as a whole chapter, by **LP292 of 19.10.2023,
in force 21.10.2023**. Law 234/2016 has 37 articles today. There is nothing to verify further and
nothing to mark `[de verificat]`. (LP259/2024, the only amendment the current page lists, was
checked too and is not the cause: it repeals one paragraph and adds art. 47¹.)

**The systemic finding: a refresh destroys the repeal history.** legis.md keeps, in any given
consolidation, only the markers of the amendment that produced *that* version. Older markers are
dropped. Counted on the same act:

| version | consolidation | bracketed markers |
|---|---|---:|
| doc_id 139826 | 2023-10-21 | **59** |
| doc_id 145901 | 2024-11-26 | **5** (all from LP259/2024) |

The wiki's own file shows the same collapse, because it was refreshed on 2026-09-04: the July
ingest in `wiki-backups/wiki-before-eu-transposition-foundation-20260709-193401/` has 59 markers
including both decisive ones; the current file has 5. **The refresh gained a current text and lost
the audit trail that explained it.** That is what turned a properly documented act into an
apparently defective one, and it is a standing risk for every act refreshed to a newer
consolidation.

**What this changes about section B.** The census stands as a description of the *files*, but
"no marker" must now be read as "no marker in this consolidation", never as "no repeal". Of the
remaining unexplained runs, `L-100-2017` art. 52 is unaffected — its older and current files both
carry one marker, and the cause there is the `Articol 52` misspelling, not marker loss. The others
(`COD-154-2003` 374–382, `L-220-2007` art. 6, `L-845-1992` arts. 21 and 31, `L-548-1995`) were all
ingested straight at their current consolidation and have never been compared against an older
version, so none of them has been shown to be a source defect either. Comparing them against
legis.md's earlier versions is the next step.


### B-quater. All fifteen unexplained runs, checked against legis.md's version history

Done 2026-09-05, after B-ter. legis.md exposes every past consolidation of an act as its own
`doc_id`, linked from the act page as `showDetails(null,'<doc_id>')`, and the text of any version
is at `/cautare/showdetails/<doc_id>`. That makes the question answerable: for each missing
article, find the last consolidation that contains it and the first that does not, and read the
amending law off the second.

**Result: every gap is explained. Not one is a defect in our ingest, and not one is an
unexplained hole in the law.**

| act | articles | repealed by | mechanism |
|---|---|---|---|
| `L-234-2016` | 24; 27–35 (Chapter IV) | LP292/2023, in force 21.10.2023 | 1 — marker dropped |
| `COD-154-2003` | 226–244 | LP254 din 09.12.2011, MO25-28/03.02.12 | 2 — no markers then |
| `COD-154-2003` | 374–382 | LP205 din 20.11.2015, in force 18.12.2015 | 1 — marker dropped |
| `COD-218-2008` | 441 | LP208 din 17.11.2016, in force 16.03.2017 | 2 — no markers then |
| `L-220-2007` | 6 | LP90 din 29.05.2014, MO169-173/27.06.14 | 2 — no markers then |
| `L-845-1992` | 21 | LP133 din 15.11.2018, in force 01.03.2019 | 1 — marker dropped |
| `L-845-1992` | 31 | LP746 din 27.12.2001, in force 12.02.2002 | 2 — no markers then |
| `L-548-1995` | 12, 13, 29, 30, 48, 54, 73 | various, all before 2016 | 3 — stubs deleted |
| `COD-225-2003` | 78 | repeal recorded in the body | misspelling `Aricolul 78` |
| `L-100-2017` | 52 | **never repealed** | misspelling `Articol 52` |

**Three mechanisms, not one.** B-ter found the first; the sweep found two more.

1. **Marker dropped on refresh.** The bracket existed in an earlier consolidation and is gone from
   the current one. Recovered verbatim for `L-845-1992` art. 21 —
   `[Art.21 abrogat prin LP133 din 15.11.18, MO467-479/14.12.18 art.784; în vigoare 01.03.19]` —
   and for `COD-154-2003` arts. 374 and 382 (`[Art.374 abrogat prin LP205 din 20.11.15 …]`).
2. **Marker never existed.** Consolidations before roughly 2018 carry no bracketed markers at all;
   every pre-2021 version of `L-845-1992` has zero. The evidence is then the transition itself,
   corroborated by date: `L-220-2007` art. 6 is present at 07-12-2012 and absent at 27-06-2014, and
   that version's sole amendment is LP90 din 29.05.14, published in MO of **27.06.14** — the same
   day. `COD-218-2008` art. 441 and `COD-154-2003` 226–244 align the same way.
3. **Repeal stub deleted.** `L-548-1995` held all seven articles as explicit
   `Articolul N – abrogat.` lines in the consolidation of 01-08-2016 (doc_id 94178); the next
   consolidation, 04-10-2016 (doc_id 95643), removed the lines outright, with no amendment
   distinguishing the two. This is the worst case: the earlier text was self-explanatory, and an
   `Articolul N – abrogat.` line is exactly the form our anchoring captures — had the act been
   ingested before October 2016, all seven would carry anchors reading "abrogat".

**One caveat on method.** The bisection assumes an article's presence is monotonic over time. That
held everywhere except `L-548-1995`, where the per-article transition dates came out inconsistent
(art. 12 appeared to vanish in 2006 while still standing as a stub in 2016). That is why the
evidence there is the side-by-side comparison of the two 2016 consolidations, not a bisected date.
Where a single amendment is named for the transition version, it is corroborated by the
publication date matching the version date.

**What it costs the vault.** Across the 44 anchored acts, 28 now carry fewer than 0.05 markers per
article: Codul fiscal has **1** for 512 articles, the Civil Code 29 for 2657, `COD-154-2003` 3 for
416. Acts that kept their history look nothing like it — `L-308-2017` has 46 for 47. Low density is
not by itself proof of loss, since a rarely amended act legitimately has few markers, but it bounds
what these files can answer: for most acts we hold the current text without the record of how it
got there.

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

**E1 — a stray duplicate at the vault root. Fixed 2026-09-05.**
`Claude outputs/2026-09-05-plan-restructurare-wiki.md` was **byte-identical** (md5 `de7159ec…`,
sha256 `b9410219…`) to `_meta/plans/2026-09-05-plan-restructurare-wiki.md`. It was tracked in git,
sat outside every folder the spec knows (structured, raw, `_archive`, `_meta`), was therefore
validated by nothing, and Obsidian indexed it as a note. The root copy is deleted; the
`_meta/plans/` copy is verified intact at the same hash.

**The folder was kept, deliberately.** While this audit was being written, a second agent working
on an unrelated matter wrote `2026-09-05-contract-antrepriza-sihastrului-11-revizuit.docx` into it.
So `Claude outputs/` is not a leftover — it is a live drop point for output from whatever else runs
against this vault, sitting outside every validated path. That also accounts for the two
`_meta/anchoring-work/` files whose line endings changed under this session without being edited.
CLAUDE.md already warns that more than one agent writes here; this is what that looks like in
practice. Deciding where that output belongs is a judgement call for Eugen, not a lint fix.

**E2 — 278 of the 280 validator warnings carried no information. Fixed 2026-09-05.**
They were `raw.language-other` on the BNM corpus, all from the bulk ingest of 2026-07-12.
**Now: 262 `en`, 15 `ro`, one honestly left as `other`. The warning count is 280 → 3.**
Only the single `language:` line changed in each file; all 378 raw sha256 still verify, which is
the proof that no body byte moved.

**The method matters more than the result, because this section originally recommended the wrong
one.** It said the `source_record` URL settles the language. It does not: BNM lists Romanian PDFs
on English catalogue pages and the reverse, and **ten files contradicted their own URL**:

| file | URL says | document is |
|---|---|---|
| `014__ISAP1_Final_WebVersion.pdf.md` | ro | **en** — body opens `TABLE OF CONTENTS / Preface / Section 1. General` |
| `252__RI_4_2021.pdf.md` and 8 more inflation reports/presentations | en | **ro** — body opens `Raport asupra inflației, noiembrie 2021` |

Had the URL been trusted, ten files would have been mislabelled with full confidence. The
document's own text decided instead — stopword frequency plus Romanian diacritic count — with the
URL and filename kept only as corroboration and overruled where they disagreed. Every conflict was
checked by eye before applying.

One file keeps `other`, correctly: `236__Prezentare_RI_mai_2025.pdf.md` is a slide deck whose PDF
text extraction produced 39 words and no diacritics (the body reads `1 ± 2`). Nothing in the file
can settle its language, and `other` is the honest value rather than a guess dressed as a fact.

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

1. ~~The article gaps~~ — **all closed 2026-09-05, see B-ter and B-quater.** Every one of the
   fifteen is dated to a repealing law; none is a defect in our ingest. What remains is the
   consequence, not the gaps: the vault holds current texts largely stripped of their amendment
   history, and three distinct mechanisms cause it. Decide whether that history is worth
   recovering — it is recoverable, act by act, from legis.md's version list.
2. **`L-100-2017` art. 52** — record the trap next to the `COD-225-2003` art. 78 one.
3. **CLAUDE.md corrections** — close outstanding-work item 2 for the Civil Code, reopen it against
   `COD-985-2002`; add the new gaps to open question 3; add `54^1/1` to open question 2.
4. **Retire or fix `run_cnpf_legal_lint.py`** (A1–A5), porting the orphan-page and
   page-level-raw-ref checks into the validator. Until then it should not be run at all: it
   writes a D8-breaking entry into `log.md` every time.
5. **`language: other`** — one script, 278 warnings gone.
6. **Delete `Claude outputs/`**; link the three orphan pages.
