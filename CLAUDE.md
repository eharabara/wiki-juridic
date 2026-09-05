# Working instructions for this folder

This is the LLM Wiki: a structured knowledge base of Moldovan law, built to be queried by a
language model rather than read front to back. You are working for Eugen Harabara, a lawyer and
economist in Chișinău.

## Read this first, in this order

1. `legal-career/00-custom-instructions.md` for persona routing.
2. `legal-career/03-working-rules.md` for the source hierarchy, citation discipline, the
   confidence line, and the analytical standard. These bind every answer.
3. `legal-career/04-personas.md` to pick the role before you answer.
4. `legal-career/02-profile.md` for how to pitch and phrase the answer.
5. `SCHEMA.md` for the file conventions of this wiki. Follow it for anything you write here.

The `legal-career/` documents are copies. The master lives in the claude.ai project "Legal Wiki",
taken on 2026-09-04. If you find a contradiction between a copy and something Eugen says, the
project is authoritative, and the copy needs refreshing. Do not edit the copies here. Since
2026-09-05 each copy carries a provenance stamp in its frontmatter (`copy_of`, `taken`,
`sha256_body`, `refresh`); the validator fails if a copy's body no longer matches its stamp, so a
local edit cannot pass unnoticed. To refresh a copy, replace the body with the project's text and
re-stamp it (`python _meta/schema/stamp_copies.py`).

**The matter log is refreshed every session (decision D9).** `legal-career/06-matter-log.md` is
the one copy that changes with the work, not with the method. At the start of any session that
touches this wiki, ask Eugen for the current register from the project if the stamp's `taken`
date is not today, then re-stamp. The validator warns while it is stale. Positions in the
register are not re-argued here; they are used.

## The one rule that changes in this folder

In the claude.ai project, the confidence line at the end of every substantive answer is a
judgement about what the wiki probably holds. Here the text is physically present and you can
open it. So the confidence line is not a judgement, it is a check.

Before writing "anchored", open the file, find the article, and read it. If you did not open a
file, the answer is not anchored, whatever any summary says. This folder removes the excuse for
guessing, so guessing here is a worse error than it is in the project.

One thing the anchor alone does not tell you. Since the refresh of 4 September 2026, some files
hold consolidations dated in the future. A provision can be correctly anchored, with a valid
sha256, and still not bind today. The generated table below flags which acts, and
`_meta/inforce/in-force-register.md` lists the individual provisions. Check it before citing an
article from a future-dated act, and say in the answer which version applies today.

## Where things are

- `raw/papers/cnpf/` — the CNPF and BNM perimeter laws, full text from legis.md, plus the EU
  acquis extracts named `UE-*.md`. The EU files are structured extracts, not full text.
- `raw/papers/moldova-legal/` — Civil Code, Codul fiscal, Codul administrativ, company law,
  Law 100/2017 on normative acts, and the government decisions.
- `raw/papers/bnm/` — the BNM legal and reports corpus, converted documents plus originals.
  `raw/papers/bnm/legal-ro/` holds, since 2026-09-05, the Romanian legis.md text of the six
  banking laws (202/2017, 548/1995, 114/2012, 232/2016, 62/2008, 160/2023). Cite banks from
  there, never from the English translations.
- `raw/papers/cnpf/_manifest.md` — the source register. Read it before citing anything from the
  perimeter. It records mandate allocation between CNPF and BNM, acquis anchors, consolidation
  dates, and confidence per act.
- `entities/`, `concepts/`, `comparisons/`, `queries/` — the structured layer. These are
  summaries. They are not a substitute for the raw text and must not be cited as if they were
  the law. Every page carries `perimeter: legal | policy`; see the perimeter rule below.
- `_meta/schema/` — the mechanical specification (`schema-spec.yaml`), the generator of the
  mechanical block of `SCHEMA.md`, and the validator. Since 2026-09-05.
- `_meta/log/` — the old journal, 2026-07-08 to 2026-09-05, frozen. `log.md` in the root is the
  index that replaced it.
- `_archive/emir-2026-07/` — the five EMIR drafting pages withdrawn from `queries/` on 2026-09-05,
  with `_PROVENANCE.md`. Frozen. `queries/` is empty until a real query page is written.
- `_meta/coverage/` — the script that generates the coverage section of this file.
- `_meta/inforce/` — the register of provisions not yet in force, and the script that builds it.
- `_meta/lint/` — the lint scripts and their outputs.
- `_meta/imports/` — the ingestion and anchoring scripts.
- `_meta/plans/` — working plans and recorded gaps.
- `_archive/cnpf-wiki-ro-2026-07/` — the July ancestor of this wiki, kept for its original
  Romanian operating rules and its 9 July lint report. Its raw texts are stubs. Do not work in it.

Raw text under `raw/` is treated as immutable, per SCHEMA.md. Adding structural anchors is the
one permitted exception, and only with the audit trail used on 2026-09-04: headings inserted
above the original lines, no source line altered, `sha256` moved to `sha256_pre_anchoring`, and a
strip-and-compare check against a backup proving the body is byte-identical.

<!-- COVERAGE:BEGIN - generated by _meta/coverage/build_coverage.py, do not edit by hand -->

## State of the raw layer

Generated 2026-09-05 15:26 from the files themselves. Do not edit this section by hand; rerun `python3 _meta/coverage/build_coverage.py`. Judgement belongs in the hand-written sections above and below.

46 primary Moldovan acts, 29 EU acquis extracts, 289 BNM corpus documents.

| Act | Articles | Anchors | Consolidation | Note |
|---|---:|---:|---|---|
| `CC-1107-2002` | 2657 | 2657 | 2026-04-01 | clean |
| `COD-116-2018` | 260 | 260 | 2025-08-31 | 2 superscript articles normalised |
| `COD-1163-1997` | 512 | 512 | 2026-06-25 | 159 superscript articles normalised |
| `COD-122-2003` | 658 | 658 | 2026-12-02 | **consolidation dated in the future**; 105 superscript articles normalised |
| `COD-154-2003` | 416 | 416 | 2027-01-01 | **consolidation dated in the future**; 52 superscript articles normalised |
| `COD-174-2018` | 98 | 98 | 2026-06-24 | 4 superscript articles normalised |
| `COD-218-2008` | 737 | 737 | 2026-09-13 | **consolidation dated in the future**; 254 superscript articles normalised |
| `COD-225-2003` | 537 | 537 | 2025-12-30 | 77 superscript articles normalised |
| `COD-443-2004` | 361 | 361 | 2026-12-02 | **consolidation dated in the future**; 36 superscript articles normalised |
| `COD-95-2021` | 472 | 472 | 2026-09-01 | 51 superscript articles normalised |
| `COD-985-2002` | 566 | 566 | 2026-12-02 | **consolidation dated in the future**; 178 superscript articles normalised |
| `DCA-61-2024` | 0 | 0 | 2024-05-05 | no article structure; **2.3 years old** |
| `HG-1170-2016` | 0 | 0 | 2025-03-07 | no article structure |
| `HG-1171-2018` | - | 0 | 2024-07-05 | numbered points (65), not articles; **2.2 years old** |
| `HG-574-2024` | 0 | 0 | 2024-08-23 | no article structure; **2.0 years old** |
| `L-1-2018` | 28 | 28 | 2025-12-31 | clean |
| `L-100-2017` | 79 | 79 | 2025-12-31 | 2 superscript articles normalised |
| `L-105-2003` | 75 | 75 | 2025-10-25 | 1 superscript article normalised |
| `L-106-2022` | 45 | 45 | 2025-10-25 | clean |
| `L-1134-1997` | 110 | 110 | 2028-01-01 | **consolidation dated in the future**; 7 superscript articles normalised |
| `L-114-2012` | 131 | 131 | 2027-01-01 | **consolidation dated in the future**; 23 superscript articles normalised |
| `L-122-2008` | 23 | 23 | 2025-12-31 | clean |
| `L-135-2007` | 93 | 93 | 2026-03-27 | 10 superscript articles normalised |
| `L-139-2007` | 59 | 59 | 2026-01-01 | 1 superscript article normalised |
| `L-160-2023` | 58 | 58 | 2023-10-01 | **2.9 years old** |
| `L-171-2012` | 156 | 156 | 2027-06-01 | **consolidation dated in the future**; 18 superscript articles normalised |
| `L-177-2025` | 4 | 4 | 2025-07-21 | 4 articles numbered in Roman figures; stale count line in body says 0 |
| `L-178-2020` | 8 | 8 | 2020-09-18 | 8 articles numbered in Roman figures; stale count line in body says 0 |
| `L-181-2023` | 50 | 50 | 2026-06-26 | 1 superscript article normalised |
| `L-183-2012` | 110 | 110 | 2025-12-31 | 15 superscript articles normalised |
| `L-192-1998` | 34 | 34 | 2026-01-01 | 3 superscript articles normalised; stale count line in body says 0 |
| `L-198-2020` | 64 | 64 | 2025-10-25 | clean |
| `L-2-2020` | 46 | 46 | 2025-10-25 | clean |
| `L-202-2017` | 155 | 155 | 2025-09-20 | 6 superscript articles normalised |
| `L-220-2007` | 44 | 44 | 2026-07-23 | 6 superscript articles normalised |
| `L-232-2016` | 344 | 344 | 2025-02-28 | 21 superscript articles normalised |
| `L-234-2016` | 37 | 37 | 2024-11-26 | clean |
| `L-235-2006` | 21 | 21 | 2024-07-05 | **2.2 years old** |
| `L-284-2004` | 29 | 29 | 2026-02-14 | 1 superscript article normalised |
| `L-308-2017` | 47 | 47 | 2026-08-13 | 10 superscript articles normalised |
| `L-548-1995` | 91 | 91 | 2026-04-23 | 21 superscript articles normalised |
| `L-62-2008` | 73 | 73 | 2025-12-31 | 3 superscript articles normalised |
| `L-62-2022` | 58 | 58 | 2026-08-14 | 5 superscript articles normalised |
| `L-64-2010` | 34 | 34 | 2024-01-23 | **2.6 years old** |
| `L-845-1992` | 46 | 46 | 2027-01-01 | **consolidation dated in the future**; 11 superscript articles normalised |
| `L-92-2022` | 125 | 125 | 2026-06-25 | 1 superscript article normalised |

### Mechanical flags

- **Not yet in force.** 9 act(s) carry a consolidation dated after today, so the file holds text that will bind later, not text that binds now: `L-1134-1997` (2028-01-01), `L-171-2012` (2027-06-01), `COD-122-2003` (2026-12-02), `COD-154-2003` (2027-01-01), `COD-218-2008` (2026-09-13), `COD-443-2004` (2026-12-02), `COD-985-2002` (2026-12-02), `L-845-1992` (2027-01-01), `L-114-2012` (2027-01-01). 47 affected provision(s) are listed in `_meta/inforce/in-force-register.md`. Check that register before citing an article from these acts. The citation will look correct in every other respect: the article exists, the anchor is valid, the sha256 matches.
- **Stale consolidations.** `L-160-2023` (2023-10-01), `L-64-2010` (2024-01-23), `DCA-61-2024` (2024-05-05), `HG-1171-2018` (2024-07-05), `L-235-2006` (2024-07-05), `HG-574-2024` (2024-08-23). Anchoring is clean, so these look reliable. Say in the answer that the text may be superseded.
- **Stale count line inside the file.** `L-177-2025` (body says 0, anchors 4), `L-178-2020` (body says 0, anchors 8), `L-192-1998` (body says 0, anchors 34). The frontmatter is right and the anchors are right; the human-readable line in the body was written by the original ingest and never updated. Cosmetic, but it is the line a reader sees first.
- **BNM English corpus.** 65 file(s) carry 432 line-initial `Article N` markers and no anchors. Any answer resting on the English BNM translations is not anchored.

<!-- COVERAGE:END -->

## Open questions that need Eugen's judgement

Do not resolve these on your own. Raise them if a matter touches them.

1. **Codul civil arts. 2047 to 2054.** Absent, covered by a heading `Secțiunea a 3-a- abrogată`
   at line 11283, with no LP citation in the text. The other eight absences in the code each
   carry an individual `[Art.NNNN abrogat prin LP...]`. Marked `[de verificat]` against legis.md.

2. **Superscript flattening below article level.** The legis.md refresh now resolves superscripts
   during extraction, so the acts pulled on 4 September are clean at article level. The Civil Code
   was extracted from a PDF and never went through that path. Amendment notes of the form
   `[Art.15 al.(11)...]` are probably alin. (1¹). Nobody has checked the paragraph layer. A
   paragraph citation can therefore be as corrupted as an article citation used to be.

3. **Two numbering gaps in the codes have no basis at all in the source.** `COD-154-2003`
   (muncii) is missing **arts. 226 to 244**, 19 in a row, with no marker of any kind between
   art. 225 and art. 245. `COD-218-2008` (contravențional) is missing **art. 441**, the numbering
   running 440, 440^1, 442. Every other absence across the eleven codes *is* explained, by an
   individual marker, a range marker (`Articolul 397- 422 – abrogate.`) or a chapter/section
   marker. Marked `[de verificat]` against legis.md.

4. **A typo in the source hides a repeal.** `COD-225-2003` art. 78 carries
   `Aricolul 78. – abrogat.`, missing the `t`. The repeal is recorded, but the line does not match
   the `Articolul N` form, so it takes no anchor and art. 78 reads as an unexplained gap. Not
   corrected, because rewriting legal text is forbidden here. Searching `## Articolul 78` in that
   file returns nothing, which is the trap.

5. **The English BNM corpus is unanchored.** The generated flags give the current count. Decided
   on 2026-09-05 (decision D2 of the restructuring plan): a translation never carries an anchor.
   It is used only to locate a provision, which is then cited from the Romanian text. The
   P8 and P9 are done (2026-09-05): the six banking laws are in Romanian under
   `raw/papers/bnm/legal-ro/`, 22 English translations with a Romanian text in the vault are in
   `_archive/bnm-en-2026-09/`, and the five English law files left (250/2017, 550/1995, 239/2008)
   are `source_type: translation` with their anchors removed and the body proved unchanged. Any
   `## Article` anchor left in `raw/` is now a validator error. Still open, "P8-bis": ingest
   those three acts in Romanian. The remaining `language: other` warnings are the BNM regulations
   and reports, not laws.

6. **`L-548-1995` is missing arts. 12, 13, 29, 30, 48, 54 and 73 with no marker of any kind.**
   The numbering runs 11^n to 14, 28 to 31, 47 to 49, 53 to 55, 72 to 74. The law was republished
   in 2015 (MO 297-300/2015, under art. V of Law 147/2015), which may explain a renumbering, but
   the legis.md text does not say so. Same class as item 3. Marked `[de verificat]`.

Resolved on 2026-09-04 and kept here so it is not re-raised: art. 21 of `L-192-1998` was absent
with no basis in the source. The refreshed consolidation contains it. No action needed.

## Outstanding work

1. Done 2026-09-04. All seven remaining codes are ingested, so **nothing from the failed
   13 July plan is outstanding**. Method kept for the next act:
   `_meta/imports/moldova-legal/ingest_business_law.py`, which takes act names as arguments,
   resolves `<sup>` and CSS-raised superscripts before extraction, suppresses anchoring inside a
   `CUPRINS` table of contents, anchors `TITLUL` including the letter-spaced form, flags future
   consolidations, and hashes the assembled file. Verify with `verify_business_law.py` in the same
   folder. Do not add general law or codes to the CNPF script's `DOCS`: it writes into
   `raw/papers/cnpf/`, the wrong perimeter.
2. Decide whether to unwrap the Civil Code body. 60.2 percent of its non-empty lines continue
   mid-sentence, so a quoted passage needs rejoining by hand. Separate operation, own backup and
   own diff.
3. Done 2026-09-05. `entities/L-177-2025.md` exists, and the raw-path references in the two code
   pages and in `emir-concordance-skeleton` are now wikilinks. Checked mechanically at the same
   time, not assumed: every primary act under `raw/papers/cnpf/` and `raw/papers/moldova-legal/`
   now has an entity page. The only two raw files still without one are the EMIR drafting
   documents, which are working papers covered from `queries/`, not entities.
   The gap that page opened is now closed too: **Legea nr. 62/2022 cu privire la publicitate was
   ingested on 2026-09-05**, doc_id 155339, consolidation 2026-08-14, 58 anchors, text integrity
   proved line by line. The presumption in art. 4^1 alin. (9) of `L-171-2012` anchors end to end,
   and art. 4^1 no longer has any external reference without support here. Details in section H
   of `raw/papers/moldova-legal/_manifest.md`.
   **What that ingest opened in turn, smaller but real:** art. 50 of the advertising law lists the
   control authorities and CNPF is not among them, although art. 4^1 gives CNPF a direct power
   against broadcasters. The second half of that gap is closed too: **Legea nr. 284/2004 was
   ingested the same day**, doc_id 150486, consolidation 2026-02-14, 29 anchors. Note the rename
   before searching for it: legis.md gives its current name as "privind serviciile societatii
   informationale" and "privind comertul electronic" as the previous one, and `L-62-2022` still
   cites the old title. Details in section I of `raw/papers/moldova-legal/_manifest.md`.
   **The chain is now complete.** `L-105-2003` privind protectia consumatorilor was ingested the
   same day, doc_id 150997, consolidation 2025-10-25, 75 anchors. So the whole chain
   `L-177-2025` -> `L-62-2022` -> `L-284-2004` -> `L-105-2003` is anchored, for control
   authorities as well as territorial reach. Details in section J of the moldova-legal manifest.
   **And it changed a mandate answer, so read J.2 before saying CNPF has no consumer-protection
   role:** arts. 37(2) and 38(2) of 105/2003 name CNPF expressly as the supervisor for unfair
   contract terms and distance contracts within its own perimeter, which art. 4(2^1) of
   `L-192-1998` defines - and that perimeter includes banks, whose prudential supervisor is BNM.
   What is still open one step further down: art. 44(2) of 105/2003 leaves the list of
   cross-border cooperation authorities to a government decision that is not ingested.
   **`L-183-2012`, the competition law, was ingested the same day** (doc_id 152606,
   consolidation 2025-12-31, 110 anchors) and it closes the loop back to `L-62-2022`, whose
   art. 50(1)(a) sends the Competition Council to "its powers under Law 183/2012". Read section K
   of the moldova-legal manifest before treating that Council as the general advertising
   regulator: arts. 32(c) and 39(f) of 183/2012 both limit it to commercial advertising "where
   the rights of undertakings are affected", and art. 14(2) makes the procedure complaint-driven
   by the injured undertaking. It is the B2B side only. Section K.3 also records four
   source-side flattened superscripts in that act (art. 572 twice, 571, 541 = 57^2, 57^1, 54^1),
   proved against the correctly tagged form elsewhere in the same file.
   **`COD-174-2018`, the audiovisual media services code, closes art. 50's second reference**
   (doc_id 150538, consolidation 2026-06-24, 98 anchors; section L of the manifest). Its relation
   to the advertising law is cumulative, not divided: art. 62(1) says commercial communications
   follow the code *and* the advertising law. Section L.2 records a negative finding worth
   keeping: the code has no rule at all for financial, investment or derivatives advertising, so
   the radio/TV ban in art. 4^1(2)(g) of `L-171-2012` binds the promoter, not the broadcaster's
   own code. **That last point was refined the same day by ingesting `DCA-61-2024`**, the
   Regulation on audiovisual content that arts. 62(1) and 75(3)(c) of the code make binding
   (doc_id 142648, in force 05.05.2024; section M of the manifest). Its **pct. 90** forbids
   presenting in audiovisual commercial communications any product, service or activity
   "interzise prin lege", which pulls the art. 4^1 ban in by general renvoi - so enforcement has
   two arms, CNPF's stop-broadcast request and the Audiovisual Council's own sanction.
   Two things to carry forward from section M: the act is structured in **puncte**, not articles,
   so a citation to "pct. N" is NOT anchored; and the superseded 2021 Regulation
   (`REGULAMENT 63/2021`, doc_id 125023) still carries **no repeal date** on legis.md even though
   the 2019 decision approving it was repealed on 30.05.2024 - a citation trap for anyone
   searching by title. Section M.1 also documents the title-search method used to find it:
   `getResults?search_string=<phrase>&search_type=1`, with the phrase written **without
   diacritics**, which is the only route to secondary acts of regulatory authorities.
   **`L-64-2010` cu privire la libertatea de exprimare closes that branch** (doc_id 141515,
   consolidation 2024-01-23, 34 anchors; section N), because pct. 199 and 201 of the Regulation
   send the right of reply there. Two things from section N are worth carrying: its arts. 24-25
   put the burden on the **claimant** and stack **six presumptions in favour of expression**,
   including a default moral-damages award of 1 leu - the fifth and most permissive of the
   burden-of-proof regimes mapped across this perimeter; and it is the natural counterweight to
   the non-contestable CNPF alert in art. 4^1(7) of `L-171-2012`, which forecloses challenge to
   the administrative act but says nothing about a separate defamation claim.
4. The stale count lines flagged below, if they bother you. They are cosmetic.
5. **Restructuring of 2026-09-05, steps P0 to P6 done** (plan in `_meta/plans/`, log in `log.md`,
   history in git from commit `12e819d`). Still open from that plan: P2 the private GitHub
   repository (local git only so far; Eugen names the repository), P7 provenance stamps on the
   `legal-career/` copies and the refresh of the case register, P8 the six banking laws in
   Romanian, P9 the retirement of the English BNM translations. **P2 and P7 were done the same
   day. P8 was done on 2026-09-05 too**: `raw/papers/bnm/legal-ro/`, six acts, all with text
   integrity proved and entity pages; Law 575/2003 turned out to be repealed and was replaced by
   Law 160/2023. Method: `_meta/imports/bnm/ingest_bnm_ro.py` and `verify_bnm_ro.py`. Note the
   download route: legis.md now sits behind a Cloudflare check that blocks `curl`; the HTML was
   taken from Chrome after Eugen passed the check. **P9 was done the same day** (see open
   question 5). The plan is complete; what it opened in turn is P8-bis, three acts to ingest in
   Romanian: 550/1995, 250/2017, 239/2008.

## Keeping this file true

The coverage section between the markers is generated, not written. It was written by hand three
times on 4 September and was wrong within the hour each time, because more than one agent writes
to this folder and only one of them updated the description. The same drift had spoiled the
knowledge map over two months.

So the rule is: anything mechanically checkable is generated. Run
`python _meta/coverage/build_coverage.py` at the end of any session that touched `raw/`, and
`--check` to see whether it is out of date without writing. The same holds for `SCHEMA.md`: its
mechanical block comes from `python _meta/schema/build_schema.py`, and the validator reads the
same spec, so the rules a reader sees are the rules enforced. Judgement stays in the hand-written
sections. If you find yourself typing an article count or a field list into a file, stop and
run the script. On this machine the interpreter is `python`, not `python3`.

## Safety

This folder is not under version control. Before any operation that writes to existing files,
copy the folder to `C:\Users\harab\wiki-backups\wiki-YYYY-MM-DD-<reason>\` and confirm the copy.

Never rewrite, correct, harmonise or reflow legal text. Where you add structure, prove the text
survived unchanged: strip the lines you added and compare the remainder to the backup copy, not
to your own working copy.

## Writing to the wiki

Follow `SCHEMA.md`: the hand-written sections for judgement, the generated block for the mechanical
rules. In short: frontmatter fields including `perimeter`, the fixed tag taxonomy, Obsidian
`[[wikilinks]]` resolved in the order structured, raw, root, at least two outbound links per page,
and an entry in `index.md` under the page's perimeter and type. Where a new claim conflicts with an
existing page, record both with dates and mark the page `contested: true` rather than overwriting.

**Perimeters.** A `legal` page is held to the citation rule of this file: an article is anchored
only if the raw file was opened and read, and a provision from a future-dated consolidation is
named as such. A `policy` page rests on the source document, with its date and authority stated.
A page may cite from both perimeters; the field says which rule the page answers to.

**The log is an index, not a diff (decision D8).** Git records what changed. `log.md` records what
was learned and what was decided, one entry per action, with three fixed lines: **Aflat** (the
finding that the diff does not show), **Decis** (the choice made and by whom), **Unde** (commit,
file, manifest section). Do not repeat in the log what `git diff` already shows. Do not write to
`_meta/log/2026-07-08.md`.

**Run the validator** at the end of any session that touched the vault, after the coverage script:

```
python _meta/schema/validate_wiki.py --report
```

It exits 1 on errors. It repairs nothing. Anything it finds that needs judgement goes to Eugen.
A rule that produces old errors is not relaxed to make them pass.
