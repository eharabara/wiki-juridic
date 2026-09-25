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
  acquis extracts named `UE-*.md`. The EU files are structured extracts, not full text. Since
  2026-09-09 it also holds the first two CNPF subordinate acts, ingested with
  `_meta/imports/cnpf/ingest_cnpf_ro.py`, points, no anchors: `HCNPF-14-5-2016`, the Regulation
  on the circulation of securities (pct. 27: an inheritance is registered on the notary's
  certificat de moștenitor), and `HCNPF-38-5-2015`, the reporting instruction (F7 is a daily
  report form; its annex 1 with the forms is not on legis.md). Renamed acts are found on
  legis.md only under the title they were adopted with.
- `raw/papers/moldova-legal/` — Civil Code, Codul fiscal, Codul administrativ, company law,
  Law 100/2017 on normative acts, and the government decisions. Since 2026-09-25 it also holds the
  **Government-functioning perimeter** (29 acts: the Government's Regulation `HG-610-2018`, the State Chancellery
  `HG-657-2009`, 14 ministry regulations, the Rules of Parliament, the treaties law, crisis powers `L-248-2025`, the
  integrity law and others; map in `concepts/perimetrul-functionarea-guvernului.md`, method and findings in section AR of
  the moldova-legal manifest). Read `L-212-2004` with `L-248-2025`: the state of emergency left the old law on 01.09.2025.
  Since 2026-09-21 it also holds the
  **data-protection perimeter**: eight CNPDCP acts (`OCNPDCP-27-2022` consolidated with `OCNPDCP-39-2026`,
  `OCNPDCP-31-2026`, `OCNPDCP-40-2026`, `OCNPDCP-48-2026` — found 2026-09-24, it is the order Eugen's
  original question was actually about — and the two *decisions* `DCNPDCP-41-2026` and `DCNPDCP-581-2015`),
  in points, so "pct. N" is not anchored; `OCNPDCP-38-2026`, found the same day, is not on legis.md at
  all — a scanned PDF read from its rendered pages, unanchored, like `DCU-REGULI-2026`; `L-36-2026`, the ratification law of the Convention 108+
  protocol; and, since 2026-09-24, `CETS-223-2018`, the Protocol's own text (40 articles plus annex),
  likewise read from the rendered pages of the image-only official MFA translation, unanchored — art. 37
  gives the entry-into-force mechanism (unanimity, or a 38-Party threshold five years after 10.10.2018);
  the current ratification count on the Council of Europe's own treaty page for CETS 223 is still
  unverified. `UE-2016-679` (GDPR) and `UE-2016-680`, **full text** in Romanian from Cellar,
  articles under `###`, not `##`. Read `entities/CNPDCP-ORDINE.md` before citing any CNPDCP act: art. 90
  al. (5) of `L-195-2024` keeps alive only the acts issued under art. 32 al. (3) and (5) f), i) of
  `L-133-2011`, and `DCNPDCP-581-2015` has no clear legal basis (open, for Eugen). The comparison
  L-195/2024 against the GDPR is in `concepts/acquis-DataProtection.md`, structural plus four verified
  divergences, not alineat by alineat. EUR-Lex pages answer 202 with no body; Cellar
  (`publications.europa.eu/resource/celex/<CELEX>`, `Accept-Language: ron`) does not. Section AK of the
  moldova-legal manifest has the method and the findings.
- `raw/papers/bnm/` — the BNM legal and reports corpus, converted documents plus originals.
  `raw/papers/bnm/legal-ro/` holds, since 2026-09-05, the Romanian legis.md text of nine laws:
  the six banking laws (202/2017, 548/1995, 114/2012, 232/2016, 62/2008, 160/2023) and, from
  P8-bis the same day, 550/1995 (now "lichidarea băncilor", formerly the law on financial
  institutions, mostly repealed), 250/2017 (financial conglomerates) and 239/2008 (transparency
  in decision-making). Cite banks from there, never from the English translations. Since
  2026-09-08 the same folder holds the first two BNM subordinate acts in Romanian:
  `HBN-127-2013`, the Regulation on holdings in bank capital (pct. 8 names succession among the
  "objective circumstances" of art. 46 of Law 202/2017), and `HBN-130-2013`, the Regulation on
  the calculation of voting rights and the registration of share transfers (pct. 14: an
  acquisition in objective circumstances is registered without prior approval, with the vote
  marked suspended). Both are structured in points, so a citation to "pct. N" is not anchored;
  their English translations under `raw/papers/bnm/legal/` are translations, used only to
  locate, and for 130/2013 the English file holds the annexes that the Romanian text lacks.
  The same day the folder received its first non-legis.md source, `DCU-REGULI-2026`, the
  Rules of the Central Securities Depository (v3, in force 8 April 2026, final approval by
  BNM), taken as a PDF from dcu.md with its own script, `_meta/imports/bnm/ingest_dcu_rules.py`.
  Its 94 article anchors are synthetic, built from the source's "Art.N." line and the title on
  the next line; strip the `## ` lines to recover the extraction, whose hash is
  `sha256_extraction`. Art. 82^1 sits before art. 82 in the source.
  `raw/papers/bnm/dcu/` holds, since 2026-09-09, eight of the nine current DCU Procedures
  (acts of the DCU executive committee, PDFs from dcu.md, `_meta/imports/bnm/ingest_dcu_proceduri.py`,
  no anchors, points only). The ninth, the settlement procedure that describes the succession
  transfer, is image-only and is not ingested until OCR exists; what its pages say was read
  from the rendered images and is on `entities/DCU-PROCEDURI.md`, marked as such, not anchored.
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
- `_meta/hcc/` — since 2026-09-08, the register of provisions declared unconstitutional in the
  acts held, and its builder. Read `hcc-register.md` before citing an article from any act it
  lists: legis.md leaves the annulled text in place, and after a refresh only the `HCCnn din ...`
  row survives in the act's history block, with no article. The register's last table names the
  act–decision pairs whose article is still unknown; `recovered-provisions.json` is where a
  recovered one is written, by hand, with the doc_id of the version it was read from.
- `_meta/graph/` — since 2026-09-10, the citation graph of the acts held, and its builder
  `build_citation_graph.py`. Read `citation-graph.md` before citing an article and before ingesting
  an act. It is extracted mechanically from the raw text, with no inferred edge: every edge carries
  the file and the lines it was read from. Three things it holds that nothing else does. The
  **ingest queue**: the acts the held texts cite and the vault does not have, ranked by how many
  held acts cite them. The **dependency check**: for every provision flagged in the in-force
  register, the HCC register or as "abrogat", the articles that cite it, so a citation can be
  checked one step further than the article itself. The **unresolved references**: articles cited
  that have no anchor in the target act, which is where repealed articles still cited elsewhere,
  the Civil Code's pre-2019 numbering in the Civil Procedure Code, and source-side flattened
  superscripts (`art. 3142` for 314^2, with a mechanical hint) surface. Since 2026-09-10 it also
  carries **"Trimiteri catre acte abrogate"**: for every held act whose frontmatter says `repealed`,
  the acts that still cite it. That section exists because the first act taken off the ingest queue,
  `L-133-2011`, turned out to have been repealed eighteen days earlier, and nineteen held acts still
  point at it. It does not read acts structured in points below act level, does not read the EU
  extracts for edges, and still does not know whether a cited act that the vault does **not** hold is
  in force. Since 2026-09-18 it also does not read the articles of **amending laws whose own
  articles are all Roman numerals** (`L-133-2018`, `L-177-2025`, `L-178-2020`): the text between
  their own articles is the new text of the acts they amend, carrying *those* acts' numbering, and
  the `modificare` context rule cannot follow it across a single article of thousands of lines with
  sixteen targets — measured on `L-133-2018`, 514 of 837 references were attributed to
  `COD-225-2003` when art. I in fact amends the Civil Code, and 557 of the graph's 646 unresolved
  rows came from that one act. Act-level edges stay; 24 correct article edges from the two short
  amending laws were the measured cost. The graph is not citable; it says which anchor to open.
- `_meta/lint/` — the lint scripts and their outputs. `run_cnpf_legal_lint.py` (the July script
  that never survived the D4 rewrite of SCHEMA.md: it reported all 757 page tags invalid, called
  the ten explicit `_archive/` wikilinks broken, read only `raw/papers/cnpf/`, and appended a
  D8-breaking entry to `log.md` while rewriting the file to CRLF every run) was **retired on
  2026-09-16**: its two useful checks are ported into `validate_wiki.py` as `page.orphan` (inbound
  `[[wikilinks]]` from other structured pages, using the resolver instead of stem-matching) and
  `citation.raw-page-level` (a bracket citation naming a whole raw file with no `art./pct./anexa`
  locator), the latter generalised to every root under `raw/papers/`, not just `cnpf/`. The script
  itself is deleted; its committed reports from 9 July, 4 and 5 September stay as history, findings
  in `_meta/lint/audit-2026-09-05-full.md`, section A. `validate_wiki.py` is the only lint script
  now, and its two new checks currently surface 4 orphan pages and ~149 page-level citations
  (up from the 22 the July script found under its narrower `cnpf/`-only scope and a smaller
  corpus) — this is a wider net finding a pre-existing gap, not a new one; the pages themselves
  are unfixed.
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

Generated 2026-09-25 15:00 from the files themselves. Do not edit this section by hand; rerun `python3 _meta/coverage/build_coverage.py`. Judgement belongs in the hand-written sections above and below.

226 primary Moldovan acts, 51 EU acquis extracts, 1 Association Agreement extract(s), 294 BNM corpus documents.

| Act | Articles | Anchors | Consolidation | Note |
|---|---:|---:|---|---|
| `CC-1107-2002` | 2657 | 2657 | 2026-04-01 | clean |
| `CETS-223-2018` | - | 40 | 2018-10-10 | **more than 2 years old** |
| `COD-116-2018` | 260 | 260 | 2025-08-31 | 2 superscript articles normalised; 2 provision(s) declared unconstitutional (HCC register) |
| `COD-1163-1997` | 511 | 511 | 2026-07-01 | 158 superscript articles normalised; 10 provision(s) declared unconstitutional (HCC register) |
| `COD-122-2003` | 658 | 658 | 2026-12-02 | **consolidation dated in the future**; 105 superscript articles normalised; 17 provision(s) declared unconstitutional (HCC register) |
| `COD-1316-2000` | - | 0 | - | no article structure |
| `COD-150-2014` | 201 | 201 | 2026-01-01 | 52 superscript articles normalised |
| `COD-154-2003` | 416 | 416 | 2027-01-01 | **consolidation dated in the future**; 52 superscript articles normalised; 3 provision(s) declared unconstitutional (HCC register) |
| `COD-174-2018` | 98 | 98 | 2026-06-24 | 4 superscript articles normalised; 2 provision(s) declared unconstitutional (HCC register) |
| `COD-218-2008` | 737 | 737 | 2026-09-13 | 254 superscript articles normalised; 6 provision(s) declared unconstitutional (HCC register) |
| `COD-22-2024` | 96 | 96 | 2026-04-25 | 17 superscript articles normalised |
| `COD-225-2003` | 540 | 540 | 2026-08-06 | 77 superscript articles normalised; 9 provision(s) declared unconstitutional (HCC register) |
| `COD-246-2024` | 98 | 98 | 2026-05-29 | clean |
| `COD-259-2004` | 119 | 119 | 2026-01-01 | 3 superscript articles normalised |
| `COD-3-2009` | 85 | 85 | 2026-05-30 | **ABROGAT de la 2026-05-30**; 3 superscript articles normalised |
| `COD-325-2022` | 252 | 252 | 2026-08-26 | 7 superscript articles normalised; 4 provision(s) declared unconstitutional (HCC register) |
| `COD-434-2023` | 390 | 390 | 2026-08-06 | clean |
| `COD-443-2004` | 361 | 361 | 2026-12-02 | **consolidation dated in the future**; 36 superscript articles normalised; 6 provision(s) declared unconstitutional (HCC register) |
| `COD-95-2021` | 472 | 472 | 2026-09-01 | 51 superscript articles normalised |
| `COD-985-2002` | 566 | 566 | 2026-12-02 | **consolidation dated in the future**; 178 superscript articles normalised; 8 provision(s) declared unconstitutional (HCC register) |
| `CONST-1994` | 157 | 157 | 2024-11-05 | 8 articles numbered in Roman figures; 6 superscript articles normalised; 2 provision(s) declared unconstitutional (HCC register) |
| `DCA-61-2024` | 0 | 0 | 2024-05-05 | no article structure; **more than 2 years old** |
| `DCNPDCP-08-2023` | - | 0 | 2023-03-01 | no article structure; **more than 2 years old** |
| `DCNPDCP-41-2026` | 0 | 0 | 2026-08-25 | no article structure |
| `DCNPDCP-581-2015` | 0 | 0 | 2023-03-01 | no article structure; **more than 2 years old** |
| `DCNPDCP-PARTIDE-2014` | - | 0 | 2014-12-17 | no article structure; **more than 2 years old** |
| `DCU-REGULI-2026` | 94 | 94 | 2026-04-08 | 1 superscript article normalised |
| `HBN-127-2013` | 0 | 0 | 2021-05-09 | no article structure; **more than 2 years old** |
| `HBN-130-2013` | 0 | 0 | 2018-12-23 | no article structure; **more than 2 years old** |
| `HCNPF-14-5-2016` | 0 | 0 | 2022-05-06 | no article structure; **more than 2 years old** |
| `HCNPF-38-5-2015` | 0 | 0 | 2025-10-01 | no article structure |
| `HG-1170-2016` | 0 | 0 | 2025-03-07 | no article structure |
| `HG-1171-2018` | - | 0 | 2024-07-05 | numbered points (65), not articles; **more than 2 years old** |
| `HG-118-2023` | 0 | 0 | 2025-12-30 | no article structure |
| `HG-143-2021` | 0 | 0 | 2026-05-22 | no article structure |
| `HG-146-2021` | 0 | 0 | 2026-09-06 | no article structure |
| `HG-147-2021` | 0 | 0 | 2026-05-22 | no article structure |
| `HG-148-2021` | 0 | 0 | 2026-01-01 | no article structure |
| `HG-149-2021` | 0 | 0 | 2026-05-14 | no article structure |
| `HG-186-2026` | 0 | 0 | 2026-05-24 | no article structure |
| `HG-305-2026` | 0 | 0 | 2026-06-16 | no article structure |
| `HG-310-2025` | 0 | 0 | 2025-06-02 | no article structure |
| `HG-386-2020` | 0 | 0 | 2024-11-04 | no article structure |
| `HG-553-2024` | 0 | 0 | 2025-10-18 | no article structure |
| `HG-574-2024` | 0 | 0 | 2024-08-23 | no article structure; **more than 2 years old** |
| `HG-582-2022` | 0 | 0 | 2026-03-01 | no article structure |
| `HG-610-2018` | 0 | 0 | 2024-07-05 | no article structure; **more than 2 years old** |
| `HG-657-2009` | 0 | 0 | 2026-03-21 | no article structure |
| `HG-690-2017` | 0 | 0 | 2025-12-30 | no article structure |
| `HG-693-2017` | 0 | 0 | 2025-12-09 | no article structure |
| `HG-695-2017` | 0 | 0 | 2026-05-22 | no article structure |
| `HG-696-2017` | 0 | 0 | 2025-12-24 | no article structure |
| `HG-698-2017` | 0 | 0 | 2026-01-01 | no article structure |
| `HG-743-2024` | 0 | 0 | 2026-12-30 | no article structure; **consolidation dated in the future** |
| `HG-9-2026` | 0 | 0 | 2026-01-16 | no article structure |
| `HG-967-2016` | 0 | 0 | 2023-08-08 | no article structure; **more than 2 years old** |
| `L-1-2018` | 28 | 28 | 2025-12-31 | clean |
| `L-10-2009` | 75 | 75 | 2026-03-21 | 4 superscript articles normalised |
| `L-10-2016` | 63 | 63 | 2025-12-30 | 18 superscript articles normalised |
| `L-100-2001` | 78 | 78 | 2025-10-21 | 7 superscript articles normalised; 1 provision(s) declared unconstitutional (HCC register) |
| `L-100-2017` | 79 | 79 | 2025-12-31 | 2 superscript articles normalised |
| `L-102-2017` | 26 | 26 | 2026-08-14 | 4 superscript articles normalised |
| `L-105-2003` | 75 | 75 | 2025-10-25 | 1 superscript article normalised |
| `L-105-2018` | 74 | 74 | 2026-03-18 | 9 superscript articles normalised |
| `L-106-2022` | 45 | 45 | 2025-10-25 | clean |
| `L-108-2016` | 144 | 144 | 2026-08-25 | 30 superscript articles normalised |
| `L-1100-2000` | 49 | 49 | 2025-12-30 | 13 superscript articles normalised |
| `L-1125-2002` | 50 | 50 | 2026-04-01 | clean |
| `L-1134-1997` | 110 | 110 | 2028-01-01 | **consolidation dated in the future**; 7 superscript articles normalised |
| `L-114-2012` | 131 | 131 | 2027-01-01 | **consolidation dated in the future**; 23 superscript articles normalised |
| `L-114-2014` | 28 | 28 | 2026-01-01 | clean |
| `L-116-2014` | 18 | 18 | 2025-12-31 | 2 superscript articles normalised |
| `L-119-2004` | 29 | 29 | 2025-12-30 | 2 superscript articles normalised |
| `L-119-2018` | 32 | 32 | 2025-12-30 | 1 superscript article normalised |
| `L-121-2007` | 73 | 73 | 2026-01-23 | 4 superscript articles normalised; 1 provision(s) declared unconstitutional (HCC register) |
| `L-121-2018` | 46 | 46 | 2026-01-01 | 2 superscript articles normalised |
| `L-122-2008` | 23 | 23 | 2025-12-31 | clean |
| `L-123-2023` | 16 | 16 | 2026-01-01 | 2 superscript articles normalised |
| `L-124-2022` | 58 | 58 | 2025-12-30 | 1 superscript article normalised |
| `L-1260-2002` | 73 | 73 | 2025-01-07 | 4 superscript articles normalised; 1 provision(s) declared unconstitutional (HCC register) |
| `L-130-2012` | 77 | 77 | 2026-07-01 | 4 superscript articles normalised |
| `L-131-2007` | 55 | 55 | 2026-08-23 | 6 superscript articles normalised |
| `L-131-2012` | 41 | 41 | 2026-08-28 | 8 superscript articles normalised |
| `L-131-2015` | 91 | 91 | 2026-06-26 | clean |
| `L-132-2012` | 52 | 52 | 2026-08-28 | 1 superscript article normalised |
| `L-132-2016` | 45 | 45 | 2027-01-01 | **consolidation dated in the future**; 1 superscript article normalised; 2 provision(s) declared unconstitutional (HCC register) |
| `L-133-2011` | 36 | 36 | 2026-08-23 | **ABROGAT de la 2026-08-23**; 2 superscript articles normalised |
| `L-133-2016` | 27 | 27 | 2027-01-01 | **consolidation dated in the future**; 2 superscript articles normalised; 1 provision(s) declared unconstitutional (HCC register) |
| `L-133-2018` | 17 | 17 | 2019-03-01 | 17 articles numbered in Roman figures; **more than 2 years old** |
| `L-135-2007` | 93 | 93 | 2026-03-27 | 10 superscript articles normalised; 1 provision(s) declared unconstitutional (HCC register) |
| `L-136-2017` | 48 | 48 | 2024-06-06 | **more than 2 years old**; 1 superscript article normalised; 1 provision(s) declared unconstitutional (HCC register) |
| `L-139-2007` | 59 | 59 | 2026-01-01 | 1 superscript article normalised |
| `L-140-2025` | 24 | 24 | 2025-12-31 | 24 articles numbered in Roman figures |
| `L-143-2014` | 54 | 54 | 2025-12-30 | 19 superscript articles normalised |
| `L-1456-1993` | 46 | 46 | 2026-09-13 | 19 superscript articles normalised |
| `L-148-2023` | 35 | 35 | 2024-01-08 | **more than 2 years old** |
| `L-149-2006` | 44 | 44 | 2026-04-25 | clean |
| `L-149-2012` | 271 | 271 | 2025-12-31 | 17 superscript articles normalised; 2 provision(s) declared unconstitutional (HCC register) |
| `L-1543-1998` | 99 | 99 | 2027-01-01 | **consolidation dated in the future**; 38 superscript articles normalised |
| `L-155-2011` | 6 | 6 | 2026-09-13 | 1 superscript article normalised |
| `L-156-2007` | 24 | 24 | 2025-09-01 | 1 superscript article normalised |
| `L-158-2008` | 88 | 88 | 2026-09-13 | 11 superscript articles normalised; 1 provision(s) declared unconstitutional (HCC register) |
| `L-1585-1998` | 25 | 25 | 2026-08-14 | 4 superscript articles normalised |
| `L-160-2011` | 32 | 32 | 2026-08-29 | 18 superscript articles normalised |
| `L-160-2023` | 58 | 58 | 2023-10-01 | **more than 2 years old** |
| `L-160-2026` | 46 | 46 | 2026-08-23 | clean |
| `L-164-2025` | 151 | 151 | 2026-06-26 | clean |
| `L-165-2023` | 31 | 31 | 2023-10-26 | **more than 2 years old** |
| `L-171-2012` | 156 | 156 | 2027-06-01 | **consolidation dated in the future**; 18 superscript articles normalised |
| `L-177-2025` | 4 | 4 | 2025-07-21 | 4 articles numbered in Roman figures |
| `L-178-2020` | 8 | 8 | 2020-09-18 | 8 articles numbered in Roman figures |
| `L-179-2008` | 56 | 56 | 2025-12-31 | 22 superscript articles normalised |
| `L-179-2016` | 23 | 23 | 2026-01-01 | 2 superscript articles normalised |
| `L-181-2014` | 89 | 89 | 2027-01-01 | **consolidation dated in the future**; 5 superscript articles normalised; 2 provision(s) declared unconstitutional (HCC register) |
| `L-181-2023` | 50 | 50 | 2026-06-26 | 1 superscript article normalised |
| `L-183-2012` | 110 | 110 | 2025-12-31 | 15 superscript articles normalised |
| `L-183-2016` | 17 | 17 | 2023-10-21 | **more than 2 years old** |
| `L-19-2016` | 26 | 26 | 2026-06-24 | clean |
| `L-192-1998` | 34 | 34 | 2026-01-01 | 3 superscript articles normalised |
| `L-195-2024` | 90 | 90 | 2026-08-23 | clean |
| `L-198-2007` | 54 | 54 | 2026-08-06 | 17 superscript articles normalised |
| `L-198-2020` | 64 | 64 | 2025-10-25 | clean |
| `L-199-2010` | 29 | 29 | 2026-09-13 | 3 superscript articles normalised |
| `L-2-2020` | 46 | 46 | 2025-10-25 | clean |
| `L-20-2026` | 29 | 29 | 2026-04-01 | clean |
| `L-202-2017` | 155 | 155 | 2025-10-25 | 6 superscript articles normalised |
| `L-209-2016` | 91 | 91 | 2026-04-25 | 23 superscript articles normalised |
| `L-212-2004` | 56 | 56 | 2025-09-01 | clean |
| `L-213-2023` | 10 | 10 | 2026-01-23 | 1 provision(s) declared unconstitutional (HCC register) |
| `L-22-2025` | 55 | 55 | 2026-04-01 | clean |
| `L-220-2007` | 44 | 44 | 2026-07-23 | 6 superscript articles normalised |
| `L-221-2007` | 59 | 59 | 2025-12-30 | 16 superscript articles normalised |
| `L-227-2022` | 60 | 60 | 2025-12-31 | clean |
| `L-227-2025` | 42 | 42 | 2025-12-31 | 42 articles numbered in Roman figures |
| `L-229-2010` | 35 | 35 | 2024-08-02 | **more than 2 years old**; 1 superscript article normalised |
| `L-23-2008` | 36 | 36 | 2016-09-30 | **more than 2 years old**; 1 superscript article normalised |
| `L-230-2022` | - | 66 | - | clean |
| `L-232-2016` | 344 | 344 | 2025-02-28 | 21 superscript articles normalised |
| `L-234-2016` | 37 | 37 | 2024-11-26 | clean |
| `L-235-2006` | 21 | 21 | 2024-07-05 | **more than 2 years old** |
| `L-239-2007` | 43 | 43 | 2026-04-25 | 2 superscript articles normalised |
| `L-239-2008` | 20 | 20 | 2024-07-05 | **more than 2 years old**; 2 superscript articles normalised |
| `L-24-2008` | 42 | 42 | 2018-11-08 | **more than 2 years old**; 1 superscript article normalised; 1 provision(s) declared unconstitutional (HCC register) |
| `L-245-2008` | 41 | 41 | 2025-12-30 | 1 superscript article normalised |
| `L-246-2017` | 20 | 20 | 2023-06-02 | **more than 2 years old**; 1 superscript article normalised |
| `L-246-2018` | 97 | 97 | 2026-06-23 | 1 superscript article normalised |
| `L-248-2025` | 56 | 56 | 2026-07-28 | 5 superscript articles normalised |
| `L-25-2008` | 17 | 17 | 2018-01-12 | **more than 2 years old**; 3 superscript articles normalised |
| `L-250-2017` | 23 | 23 | 2018-03-29 | **more than 2 years old** |
| `L-253-2025` | 44 | 44 | 2026-05-27 | clean |
| `L-254-2016` | 23 | 23 | 2026-01-01 | 1 superscript article normalised |
| `L-260-2017` | 40 | 40 | 2026-06-16 | 1 superscript article normalised |
| `L-270-2018` | 38 | 38 | 2026-09-13 | 8 superscript articles normalised; 3 provision(s) declared unconstitutional (HCC register) |
| `L-272-2011` | 84 | 84 | 2026-04-25 | 22 superscript articles normalised |
| `L-273-1994` | 12 | 12 | 2026-05-27 | 3 superscript articles normalised |
| `L-274-2011` | 35 | 35 | 2026-03-18 | clean |
| `L-278-2007` | 44 | 44 | 2025-05-29 | clean |
| `L-28-2024` | 63 | 63 | 2026-01-01 | clean |
| `L-282-2004` | 22 | 22 | 2025-12-30 | 1 superscript article normalised |
| `L-283-2003` | 48 | 46 | 2025-12-30 | **declared 48, found 46**; 11 superscript articles normalised; stale count line in body says 48; 1 provision(s) declared unconstitutional (HCC register) |
| `L-284-2004` | 29 | 29 | 2026-02-14 | 1 superscript article normalised |
| `L-291-2016` | 57 | 57 | 2026-01-01 | 2 superscript articles normalised |
| `L-296-2017` | 24 | 24 | 2024-02-22 | **more than 2 years old** |
| `L-303-2013` | 46 | 46 | 2025-12-30 | 7 superscript articles normalised; 2 provision(s) declared unconstitutional (HCC register) |
| `L-306-2018` | 38 | 38 | 2025-12-31 | 4 superscript articles normalised |
| `L-308-2017` | 47 | 47 | 2026-08-13 | 10 superscript articles normalised |
| `L-317-2025` | 20 | 20 | 2025-12-31 | 20 articles numbered in Roman figures |
| `L-325-2013` | 28 | 28 | 2024-03-29 | **more than 2 years old**; 2 provision(s) declared unconstitutional (HCC register) |
| `L-325-2025` | 91 | 91 | 2027-01-01 | **consolidation dated in the future** |
| `L-36-2026` | 4 | 4 | 2026-08-23 | clean |
| `L-382-2001` | 29 | 29 | 2026-01-01 | 1 provision(s) declared unconstitutional (HCC register) |
| `L-384-2023` | 16 | 16 | 2025-12-31 | clean |
| `L-394-2023` | 29 | 29 | 2024-07-15 | **more than 2 years old** |
| `L-397-2003` | 37 | 37 | 2025-12-31 | clean |
| `L-403-2023` | 59 | 59 | 2026-05-09 | clean |
| `L-411-1995` | 72 | 72 | 2026-08-28 | 8 superscript articles normalised |
| `L-422-2023` | 107 | 107 | 2024-09-14 | **more than 2 years old** |
| `L-43-2023` | 38 | 38 | 2025-12-30 | clean |
| `L-435-2006` | 17 | 17 | 2024-05-02 | **more than 2 years old**; 1 superscript article normalised |
| `L-436-2006` | 98 | 98 | 2026-06-26 | 6 superscript articles normalised |
| `L-439-1995` | 50 | 50 | 2026-04-25 | 2 superscript articles normalised |
| `L-461-2001` | 30 | 30 | 2026-06-26 | clean |
| `L-488-1999` | 24 | 24 | 2025-04-01 | 3 superscript articles normalised |
| `L-514-1995` | 60 | 60 | 2026-08-28 | 5 articles numbered in Roman figures; 10 superscript articles normalised; 4 provision(s) declared unconstitutional (HCC register) |
| `L-52-2014` | 41 | 41 | 2025-03-27 | 1 provision(s) declared unconstitutional (HCC register) |
| `L-523-1999` | 18 | 18 | 2024-05-16 | **more than 2 years old**; 1 superscript article normalised |
| `L-548-1995` | 91 | 91 | 2026-04-23 | 21 superscript articles normalised; 2 provision(s) declared unconstitutional (HCC register) |
| `L-550-1995` | 20 | 20 | 2025-02-28 | 17 superscript articles normalised |
| `L-595-1999` | 32 | 32 | 2024-06-06 | **more than 2 years old**; 1 superscript article normalised |
| `L-599-1999` | 399 | 399 | 2025-12-31 | 5 superscript articles normalised |
| `L-62-2008` | 73 | 73 | 2025-12-31 | 3 superscript articles normalised |
| `L-62-2022` | 58 | 58 | 2026-08-14 | 5 superscript articles normalised |
| `L-64-2010` | 34 | 34 | 2024-01-23 | **more than 2 years old**; 1 provision(s) declared unconstitutional (HCC register) |
| `L-66-2017` | 17 | 17 | 2017-06-02 | 17 articles numbered in Roman figures; **more than 2 years old** |
| `L-67-2024` | 35 | 35 | 2026-04-02 | clean |
| `L-68-2013` | 23 | 23 | 2026-05-09 | 1 superscript article normalised |
| `L-69-2016` | - | 0 | - | no article structure |
| `L-71-2007` | 33 | 33 | 2023-12-22 | **more than 2 years old** |
| `L-72-2025` | 127 | 127 | 2025-12-31 | clean |
| `L-764-2001` | 26 | 26 | 2025-06-28 | 3 superscript articles normalised |
| `L-768-2000` | 28 | 28 | 2025-03-27 | clean |
| `L-797-1996` | 160 | 160 | 2023-03-24 | **more than 2 years old**; 7 superscript articles normalised; 4 provision(s) declared unconstitutional (HCC register) |
| `L-80-2010` | 30 | 30 | 2026-09-13 | 1 superscript article normalised |
| `L-82-2017` | 51 | 51 | 2026-09-13 | 1 superscript article normalised |
| `L-82-2024` | 98 | 98 | 2026-05-08 | clean |
| `L-845-1992` | 46 | 46 | 2027-01-01 | **consolidation dated in the future**; 11 superscript articles normalised; 3 provision(s) declared unconstitutional (HCC register) |
| `L-852-2002` | 2 | 2 | 2025-12-30 | clean |
| `L-86-2014` | 42 | 42 | 2026-04-25 | 17 superscript articles normalised |
| `L-9-2026` | 63 | 63 | 2026-09-12 | clean |
| `L-92-2014` | 61 | 61 | 2025-12-30 | 15 superscript articles normalised |
| `L-92-2022` | 125 | 125 | 2026-06-25 | 1 superscript article normalised |
| `L-93-1998` | 19 | 19 | 2026-03-18 | 1 provision(s) declared unconstitutional (HCC register) |
| `L-98-2012` | 38 | 38 | 2026-01-01 | 2 superscript articles normalised |
| `OCNPDCP-03-1-2013` | - | 0 | 2013-02-28 | no article structure; **more than 2 years old** |
| `OCNPDCP-03-2015` | - | 0 | 2015-01-01 | no article structure; **more than 2 years old** |
| `OCNPDCP-27-2022` | 0 | 0 | 2026-08-23 | no article structure |
| `OCNPDCP-31-2026` | 0 | 0 | 2026-08-23 | no article structure |
| `OCNPDCP-31-2026-PROIECT` | - | 0 | - | no article structure |
| `OCNPDCP-38-2026` | - | 0 | 2026-08-23 | no article structure |
| `OCNPDCP-39-2026` | 0 | 0 | 2026-08-23 | no article structure |
| `OCNPDCP-40-2026` | 0 | 0 | 2026-08-25 | no article structure |
| `OCNPDCP-48-2026` | 0 | 0 | 2026-09-16 | no article structure |
| `OCNPDCP-POLITIE-2013` | - | 0 | 2013-05-01 | no article structure; **more than 2 years old** |
| `OCNPDCP-SANATATE` | - | 0 | n/a — data și numărul ordinului lipsesc din PDF | no article structure |
| `UA-COD-DEONTOLOGIC-2016` | 0 | 0 | - | no article structure |
| `UA-STATUT-2011` | 74 | 74 | 2022-05-27 | **more than 2 years old**; 6 superscript articles normalised |

### Mechanical flags

- **Repealed acts.** no longer in force: `COD-3-2009` (repealed 2026-05-30 by CS246 din 08.11.24), `L-133-2011` (repealed 2026-08-23 by LP195 din 25.07.24). These files are kept because other acts in the corpus still cite them and because the text governs facts before the repeal date. They are anchored, their sha256 verifies and their consolidation is recent, so nothing else here would reveal that they stopped binding. Do not cite them as law in force; cite the successor and say from when it applies.
- **Not yet in force.** 14 act(s) carry a consolidation dated after today, so the file holds text that will bind later, not text that binds now: `L-1134-1997` (2028-01-01), `L-171-2012` (2027-06-01), `COD-122-2003` (2026-12-02), `COD-154-2003` (2027-01-01), `COD-443-2004` (2026-12-02), `COD-985-2002` (2026-12-02), `HG-743-2024` (2026-12-30), `L-132-2016` (2027-01-01), `L-133-2016` (2027-01-01), `L-1543-1998` (2027-01-01), `L-181-2014` (2027-01-01), `L-325-2025` (2027-01-01), `L-845-1992` (2027-01-01), `L-114-2012` (2027-01-01). 73 affected provision(s) are listed in `_meta/inforce/in-force-register.md`. Check that register before citing an article from these acts. The citation will look correct in every other respect: the article exists, the anchor is valid, the sha256 matches.
- **Declared unconstitutional.** 35 act(s) carry at least one Constitutional Court decision in their history block, 98 decisions in total: 37 still marked at article level in the text itself, 126 more recovered by reading the legis.md version history (`_meta/hcc/recovered-provisions.json`), and 0 not yet attributed to any article. A struck provision looks like ordinary law: the article exists, the anchor is valid, the sha256 matches. Check `_meta/hcc/hcc-register.md` before citing an article from `COD-116-2018`, `COD-1163-1997`, `COD-122-2003`, `COD-154-2003`, `COD-174-2018`, `COD-218-2008`, `COD-225-2003`, `COD-325-2022`, `COD-443-2004`, `COD-985-2002`, `CONST-1994`, `L-100-2001`, `L-121-2007`, `L-1260-2002`, `L-132-2016`, `L-133-2016`, `L-135-2007`, `L-136-2017`, `L-149-2012`, `L-158-2008`, `L-181-2014`, `L-213-2023`, `L-24-2008`, `L-270-2018`, `L-283-2003`, `L-303-2013`, `L-325-2013`, `L-382-2001`, `L-514-1995`, `L-52-2014`, `L-548-1995`, `L-64-2010`, `L-797-1996`, `L-845-1992`, `L-93-1998` and say which decision struck it and what today's text actually holds.
- **Stale consolidations.** `OCNPDCP-03-1-2013` (2013-02-28), `OCNPDCP-POLITIE-2013` (2013-05-01), `DCNPDCP-PARTIDE-2014` (2014-12-17), `OCNPDCP-03-2015` (2015-01-01), `L-23-2008` (2016-09-30), `L-66-2017` (2017-06-02), `L-25-2008` (2018-01-12), `L-250-2017` (2018-03-29), `CETS-223-2018` (2018-10-10), `L-24-2008` (2018-11-08), `HBN-130-2013` (2018-12-23), `L-133-2018` (2019-03-01), `HBN-127-2013` (2021-05-09), `HCNPF-14-5-2016` (2022-05-06), `UA-STATUT-2011` (2022-05-27), `DCNPDCP-08-2023` (2023-03-01), `DCNPDCP-581-2015` (2023-03-01), `L-797-1996` (2023-03-24), `L-246-2017` (2023-06-02), `HG-967-2016` (2023-08-08), `L-160-2023` (2023-10-01), `L-183-2016` (2023-10-21), `L-165-2023` (2023-10-26), `L-71-2007` (2023-12-22), `L-148-2023` (2024-01-08), `L-64-2010` (2024-01-23), `L-296-2017` (2024-02-22), `L-325-2013` (2024-03-29), `L-435-2006` (2024-05-02), `DCA-61-2024` (2024-05-05), `L-523-1999` (2024-05-16), `L-136-2017` (2024-06-06), `L-595-1999` (2024-06-06), `HG-1171-2018` (2024-07-05), `HG-610-2018` (2024-07-05), `L-235-2006` (2024-07-05), `L-239-2008` (2024-07-05), `L-394-2023` (2024-07-15), `L-229-2010` (2024-08-02), `HG-574-2024` (2024-08-23), `L-422-2023` (2024-09-14). Anchoring is clean, so these look reliable. Say in the answer that the text may be superseded.
- **Stale count line inside the file.** `L-283-2003` (body says 48, anchors 46). The frontmatter is right and the anchors are right; the human-readable line in the body was written by the original ingest and never updated. Cosmetic, but it is the line a reader sees first.
- **Declared count does not match anchors.** `L-283-2003` (48 vs 46)
- **BNM English corpus.** 60 file(s) carry 149 line-initial `Article N` markers and no anchors. Any answer resting on the English BNM translations is not anchored.

<!-- COVERAGE:END -->

## Open questions that need Eugen's judgement

Do not resolve these on your own. Raise them if a matter touches them.

1. **Codul civil arts. 2047 to 2054. Answered 2026-09-19: they were the trade-secrets section, and
   the marker sits on the section, not on the articles.** The gap was never an unexplained hole.
   `L-133-2018` pct. 652 adds to Capitolul XXXIV of Titlul III a whole **Secțiunea a 3-a**,
   "Răspunderea pentru dobîndirea, utilizarea sau divulgarea ilegală a secretelor comerciale",
   as arts. `1431^1`–`1431^8`; the block maps to today's numbering by the constant shift
   `1431^N → 2046 + N` (107 of 115 titles confirmed at the predicted position, second-best shift
   one vote against 87), sealed on both sides — old art. 1431 is today's art. 2046, old `1431^9`
   ("Noțiunea", fiducia) is today's art. 2055. So 2047–2054 is exactly that section, repealed as a
   whole, which is why the file carries `### Secțiunea a 3-a- abrogată` and no per-article marker.
   **That is a fourth mechanism hiding a repeal, on top of the three in item 3: a section-level
   repeal annotates the section heading.** **Proved and dated the same day by ingesting
   `L-384-2023`**, whose art. 16 alin. (3) pct. 2 reads, verbatim: "În cartea a treia titlul III
   capitolul XXXIII, secţiunea a 3-a «Răspunderea pentru dobândirea, utilizarea sau divulgarea
   legală a secretelor comerciale» se abrogă." Pct. 1 of the same paragraph names the article
   number outright — it replaces, in art. 1026 alin. (2), the words "în sensul dispoziţiilor
   **art. 2047** alin. (3)" with "în sensul legislaţiei privind protecţia secretelor comerciale",
   and today's art. 1026 alin. (2) carries the new wording. **In force 22.02.2024** (art. 16
   alin. (1): two months from publication on 22.12.2023).
   Three defects in that one repealing provision, worth knowing because they defeat a search:
   it calls the code "nr. 1107/**2022**" (it is 1107/2002); it writes the section title with
   "divulgarea **legală**" where the section was enacted as "divulgarea **ilegală**"; and it says
   **capitolul XXXIII** where `L-133-2018` pct. 652 had said Capitolul XXXIV — the republication
   renumbered chapters too. The intent is unambiguous all the same.
   The same pass also corrected what this item used to assert about the rest of the code. There are
   **six gaps, 14 articles**, and only **two** carry a marker (2171–2172, LP251/2025) — not "each".
   The other four are named by subject in section AG.5 of the moldova-legal manifest: 2185 = old
   art. 1455 (drepturile succesorale ale soțului supraviețuitor), 2188 = old art. 1458, 2404 = old
   `1572^102`, 2485 = old `1575^61`. None carries a marker; LP251/2025 is the likely repealer for
   all four, unproved.

2. **Superscript flattening below article level.** The legis.md refresh now resolves superscripts
   during extraction, so the acts pulled on 4 September are clean at article level. The Civil Code
   was extracted from a PDF and never went through that path. Amendment notes of the form
   `[Art.15 al.(11)...]` are probably alin. (1¹). Nobody has checked the paragraph layer. A
   paragraph citation can therefore be as corrupted as an article citation used to be.

   Related, found 2026-09-05, and a trap for any script that reads article numbers: `COD-1163-1997`
   line 2300 carries `## Articolul 54^1/1. Perioada fiscală`. It is the **only** `N^X/Y` article
   number in the vault. The pattern used everywhere else, `Articolul (\d+(?:\^\d+)?)`, truncates it
   to `54^1` and so collides with the real art. 54^1 at line 2285: a search for art. 54^1 returns
   two different articles. Check the ingest and any citation helper before relying on that pattern.

   **The inverse defect exists too, and it was the answer to three of the four citations this wiki
   could not explain (found 2026-09-19).** The source sometimes *raises* a digit that belongs on
   the line, and our extractor faithfully keeps it as `^N`, so a citation to `art. 291` arrives as
   `art. 29^1` and reads like a real superscript article. The mechanical test is cheap — the cited
   `N^M` has no anchor in the target act but the concatenation `NM` does — and over the 39
   superscript rows of the graph's unresolved table it yields five candidates, three of which
   confirm on the merits: `COD-1163-1997` art. 29^1 = art. 291, `L-202-2017` art. 13^9 / 14^1 =
   art. 139 / 141, `COD-116-2018` art. 17^1 = art. 171. **The concatenation alone proves nothing**
   — the other two candidates land on an electoral-lists article and a beekeeping one, with no
   relation to the citing text. Open both ends and compare titles, same bar as for flattening.
   Evidence in section AG.2 of `raw/papers/moldova-legal/_manifest.md`.

3. **Numbering gaps. Closed on 2026-09-05: every one is now dated to a repealing law.** The audit
   counted 31 gap runs across the anchored acts, 15 of them with no marker in our files
   (`_meta/lint/audit-2026-09-05-full.md`, sections B and B-quater). All 15 were then checked
   against legis.md's own version history, act by act. **Not one is a defect in our ingest, and
   not one is an unexplained hole in the law.** In every case the article was repealed, and only
   the *record* of the repeal is missing from the consolidation we hold. Nothing here is
   `[de verificat]` any more.

   | act | articles | repealed by | why our file cannot show it |
   |---|---|---|---|
   | `L-234-2016` | 24; 27-35 (Chapter IV) | **LP292/2023**, in force 21.10.2023 | marker dropped on refresh |
   | `COD-154-2003` | 226-244 | **LP254 din 09.12.2011**, MO25-28/03.02.12 | no markers in that era |
   | `COD-154-2003` | 374-382 | **LP205 din 20.11.2015**, in force 18.12.2015 | marker dropped on refresh |
   | `COD-218-2008` | 441 | **LP208 din 17.11.2016**, in force 16.03.2017 | no markers in that era |
   | `L-220-2007` | 6 | **LP90 din 29.05.2014**, MO169-173/27.06.14 | no markers in that era |
   | `L-845-1992` | 21 | **LP133 din 15.11.2018**, in force 01.03.2019 | marker dropped on refresh |
   | `L-845-1992` | 31 | **LP746 din 27.12.2001**, in force 12.02.2002 | no markers in that era |
   | `L-548-1995` | 12, 13, 29, 30, 48, 54, 73 | various, all before 2016 | **repeal stubs deleted** — see item 6 |
   | `COD-225-2003` | 78 | repeal is in the body | `Aricolul 78` misspelling — item 4; **fixed at source in consolidation 155718 (2026-09-06)** |
   | `L-100-2017` | 52 | **not repealed at all** | `Articol 52` misspelling — item 4 |


   **Four different mechanisms hide a repeal, and only the first was known before.** Method and
   evidence in section B-quater of the audit; legis.md exposes every past consolidation through
   `showDetails(null,'<doc_id>')`, and the text of one is at `/cautare/showdetails/<doc_id>`, which
   is how each date below was established.

   1. **The marker is dropped on refresh.** legis.md keeps, in a given consolidation, only the
      `[Art.N ... prin LP...]` markers of the amendment that produced *that* version; older ones
      are gone. `L-234-2016` carried **59** markers at doc_id 139826 (2023-10-21) and **5** at
      doc_id 145901 (2024-11-26) — and the two that vanished were exactly the ones that explained
      its numbering. Our own refresh of 2026-09-04 reproduced that collapse.
   2. **The marker never existed.** Consolidations from before roughly 2018 carry no bracketed
      markers at all, so the repeal was never annotated in the first place. Here the only evidence
      is the version history: the article is present in one consolidation and absent from the next,
      and that next version names the amending law.
   3. **The repeal stub is deleted.** The consolidation used to carry an explicit, anchorable
      `Articolul N – abrogat.` line, and a later consolidation removed the line itself. This is the
      worst of the three, because the earlier text was self-explanatory and the later one shows
      nothing at all. `L-548-1995` is the case — item 6.
   4. **The repeal is at section level, so the marker is on the heading.** Added 2026-09-19. When a
      whole `Secțiunea`/`Capitolul` is repealed, the consolidation keeps the heading and writes
      `abrogată` on it, and no article inside carries a marker — the articles simply are not there.
      `CC-1107-2002` arts. 2047-2054 is the case (item 1). Read one level up before calling an
      article-range gap unexplained: the heading immediately above it may already say why.

   **What this means for citation.** A gap with no marker means "no marker in this consolidation",
   never "no repeal". Before recording anything as a source defect, check legis.md's earlier
   versions and our own older ingests in `wiki-backups/`. And note what the vault has lost: 28 of
   the 44 anchored acts now carry fewer than 0.05 markers per article — Codul fiscal has **1** for
   512 articles, the Civil Code 29 for 2657 — so for most acts we hold the current text without the
   record of how it got there. Low density is not by itself proof of loss, since a rarely amended
   act legitimately has few markers, but it bounds what these files can answer.

4. **A misspelling in the source makes an article invisible.** Several instances, all left
   uncorrected because rewriting legal text is forbidden here. In each case searching
   `## Articolul N` returns nothing, which is the trap, and the article reads as an unexplained
   gap in item 3.

   - `COD-225-2003` art. 78 carried `Aricolul 78. – abrogat.`, missing the `t`, in consolidation
     152860. **Resolved by the refresh of 2026-09-06**: consolidation 155718 spells it correctly
     and the line is anchored. Kept here because the trap is generic, not because it is open.
   - `CC-1107-2002` arts. 843 and 845 carry `Substituirea complete` and `Substituirea incomplete`
     — the adjective in the wrong form, where the article text itself says `substituie complet` /
     `substituie incomplet`. Found 2026-09-18 while measuring the L-133-2018 concordance: that act
     introduced them as `Substituirea completă` / `Substituirea incompletă`, so a title search on
     the correct form fails. **Verified against the archived source HTML (doc_id 150498): legis.md
     itself writes it that way**, and the same file spells `Substituirea incompletă` correctly once
     elsewhere, so the defect is the publisher's, not our extraction's. Milder than the other two —
     the anchor exists and the article is findable by number — but it breaks a title search, which
     is now a working method for concordances.
   - `L-100-2017` art. 52, file line 531, carries `Articol 52. Punctul` — `Articol`, without the
     `-ul`. Found by the audit of 2026-09-05. This one matters more than the average article:
     art. 52 of the law on normative acts is the provision governing **puncte**, which is how
     every HG in this vault is cited, and section M of the moldova-legal manifest already warns
     that a citation to "pct. N" is not anchored. The article is present in full; only the
     anchor is missing.
   - `CC-1107-2002` arts. 2447, 2448 and 2522, found 2026-09-19 by the same method as the 843/845
     pair — the title as `L-133-2018` enacted it, read against the title as legis.md prints it
     today. Today's file has `Supra îndatorarea` with a space inside the word (for
     `Supraîndatorarea`), `Dreptul de a întocmi un inventor` (for `inventar`) and `bunurile primate`
     (for `primite`). Anchors are fine and the articles are findable by number; what fails is a
     title search, and "inventor"/"primate" are real words, so a search will not even look wrong.
     This is now four separate acts with the same class of defect, so treat a failed title search
     as a source-spelling hypothesis before treating it as a missing provision.
     **A fifth kind, found 2026-09-25: a Cyrillic letter in a Latin position.** `L-121-2018` art. 5 alin. (3), line 159, opens with `с)` where the
     `с` is U+0441 (Cyrillic), not `c`; a search for `c) elaborarea` finds nothing. It is the provision `L-140-2025` art. XVIII will abrogate.

5. **The English BNM corpus is unanchored.** The generated flags give the current count. Decided
   on 2026-09-05 (decision D2 of the restructuring plan): a translation never carries an anchor.
   It is used only to locate a provision, which is then cited from the Romanian text. The
   P8 and P9 are done (2026-09-05): the six banking laws are in Romanian under
   `raw/papers/bnm/legal-ro/`, 22 English translations with a Romanian text in the vault are in
   `_archive/bnm-en-2026-09/`, and the five English law files left (250/2017, 550/1995, 239/2008)
   are `source_type: translation` with their anchors removed and the body proved unchanged. Any
   `## Article` anchor left in `raw/` is now a validator error. P8-bis, the same day: those three
   acts are ingested in Romanian too. The remaining `language: other` warnings are the BNM
   regulations and reports, not laws.

6. **`L-548-1995`: resolved 2026-09-05. The seven articles were repealed, and legis.md deleted the
   repeal stubs.** Arts. 12, 13, 29, 30, 48, 54 and 73 were repealed at various dates before 2016.
   The consolidation of **01-08-2016** (doc_id 94178) still carried each of them as an explicit
   line — `Articolul 12 – abrogat.`, `Articolul 29. – abrogat.`, `Articolul 73. - abrogat.`, and so
   on for all seven. The very next consolidation, **04-10-2016** (doc_id 95643), removed those
   lines entirely, and no amendment distinguishes the two versions' modification blocks. So the
   numbering gap in the file we hold is the residue of a deletion by the publisher, not a defect in
   our ingest and not a hole in the law.

   This is mechanism 3 of item 3, and it is the one worth remembering: the 2016 text was
   *self-explanatory*, and an `Articolul N – abrogat.` line is exactly the form our anchoring would
   have captured. Had the act been ingested before October 2016, all seven would carry anchors
   reading "abrogat" and no question would ever have arisen. The republication of 2015 (MO
   297-300/2015, under art. V of Law 147/2015) is therefore **not** the explanation, which is what
   was suspected here before; the stubs survived it and were removed a year later.

7. **Done 2026-09-16. The in-force register now reads acts structured in points.** Found
   2026-09-05, after `HG-743-2024` entered the corpus: the register collapsed the act's six
   deferred provisions (pct. 33 subpct. 33.3, pct. 50, pct. 61 subpct. 61.6, pct. 82, pct. 115,
   anexa nr. 9) into one entry labelled `HG-743-2024 art. 355` — 355 being the Official Monitor
   article number of the amending act (`MO284-287/30.06.26 art.355`), not an article of
   `HG-743-2024`. Root cause: `ART_IN_NOTE` in `build_inforce_register.py` searched for `Art\.N`
   **anywhere** in the bracketed note, and every note ends with that same MO reference, so its
   `art.355` was the only thing a points-only act ever matched. Fix: the locator patterns
   (`ART_IN_NOTE`, and two new ones, `PCT_IN_NOTE` and `ANEXA_IN_NOTE`) are now anchored with `^`
   to the very start of the note, tried in that order, so the MO reference at the tail is never
   reachable — this also closes the same latent hole for article-structured acts, not just
   `HG-743-2024`. The register now carries all six provisions as separate, searchable rows
   (`pct. 82` finds one; it didn't before) — 54 provisions across 10 acts, up from 49 (the one
   fake row minus, six real ones plus). `HBN-127-2013`, `HCNPF-14-5-2016`, `HCNPF-38-5-2015` have
   the same bracket shape but only past `în vigoare` dates today, so they didn't yet exercise the
   bug; the fix is general, not a patch scoped to one act. For any hotărâre de Guvern, the
   register is now the right place to check a point, same as an article.

8. **The citation graph's "Trimiteri nerezolvate" table, verified 2026-09-16 in full, all 65
   groups.** 38 are false positives (18 flattened exponents, 12 `AA-2014` self-citations, 8 more
   caught by a second, systematic resolver bug named below); 21 are real, explained gaps (the
   13-strong `CC-1107-2002` pre-2019-renumbering cluster, `L-171-2012` arts. 81/87/88 dated to a
   named repealing law and its art. 38 confirmed already correctly tracked, and `L-550-1995`'s
   four gutted-act citations); 2 are a resolver bug pointing at the wrong in-corpus act and a
   parser artifact reading our own editorial note; and the last 4 (`COD-116-2018` art. 17^1,
   `COD-1163-1997` art. 29^1, `L-105-2003` art. 201, `L-202-2017` art. 13^9) **were closed on
   2026-09-19 — see the end of this item.** The graph's own rule says a "poate fi" hint is a hypothesis, not an edge, to be
   checked in the source before use — this is that check, done exhaustively instead of article by
   article as citations come up.

   **18 groups (27 citations), all `suspect: exponent turtit` — confirmed, not gaps.** Every
   suggested base+exponent anchor exists in the target act, and every title matches the citing
   context on its face (`COD-218-2008` art. 441 → art. 44^1 "Aplicarea sancţiunii mai blânde";
   `COD-225-2003` art. 581 → art. 58^1 "Capacitatea de exerciţiu... a persoanei în privinţa căreia
   este instituită o măsură de ocrotire judiciară", read against a citing sentence about exactly
   that capacity — as clean a confirmation as this gets). Full list and titles in the session log.
   Method proven safe to trust going forward: when the script offers a `suspect`, opening both
   ends and comparing titles settles it in one read.

   **`AA-2014`'s entire cluster (12 groups, 18 citations) is a false positive, not a gap in the
   extract.** None of the cited numbers (art. 2–9, 12, 30, 278, 359) are citations to AA-2014's
   own anchored text. Two different reasons, both confirmed by reading the surrounding paragraph:
   some are `articolul N din respectiva directivă` — an anaphoric reference to whichever EU
   directive was last named in the same Annex XXVIII-A commitment (2006/48/CE, 2006/49/CE,
   94/19/CE...), none of which the vault holds as a full extract; others are inside the reproduced
   text of art. 3 of Decizia 2014/492/UE (the Council decision on provisional application, itself
   not held), naming titles and articles of the *full* Association Agreement outside what this
   structured extract covers. The resolver's `intern` rule defaults to the current act when no act
   name sits immediately next to `articolul N`, and neither anaphora ("respectiva directivă")
   nor a nested quoted decision resets that default — a real limitation of
   `build_citation_graph.py`, worth fixing if the AA-2014 extract grows, not fixed now given the
   size of the validated graph (2491 act-edges) and the low value of a working test harness for
   one act's twelve rows.

   **`CC-1107-2002`'s cluster (12 groups, 26 citations, the largest by volume) confirms and
   extends the pre-2019-renumbering note the graph's own description already carried — now with
   proof, across three unrelated chapters.** `COD-225-2003` cites art. 48^12, 48^21, 48^28, 48^30
   (x7) and 48^40 "din Codul civil" for the persons a court must hear when instituting a measure
   of judicial protection (`ocrotire judiciară`); the current `CC-1107-2002` has no `48^N` heading
   at all — that whole chapter (tutelă, curatelă, ocrotire) runs as plain sequential numbers,
   art. 50-119. The same code cites art. 330^4 (x3) and 283^27 for uzucapiune (adverse
   possession) tied to the land-registry procedure; today's art. 330 is "Nulitatea relativă a
   actului juridic" — unrelated — and the actual uzucapiune chapter sits at art. 524-534, plain
   numbers again, with art. 524 and 526 named for exactly the registry-based uzucapiune the citing
   text describes. `L-149-2012` (insolvency) cites art. 1575^4, 1575^5, 1575^9 (x3), 1575^10 and
   1572^117 for `masa succesorală` (the estate of a deceased debtor) provisions; today's art. 1575
   is "Constatarea cantităţii şi felului bunurilor" in the warehousing (`magazinaj`) chapter, and
   succession law now runs art. 2162-2360+. Three unrelated topics, two different citing acts,
   the same signature every time: the citing act's number, read literally against the current
   code, lands on real but unrelated content, never on nothing — which is what a whole-book
   renumbering looks like, not an extraction fault. No exact old-to-new mapping attempted; that
   needs legis.md's own concordance for the renumbering law (likely Legea 133/2018), and the route
   there is blocked the same way as everything else on legis.md today.

   **Closed 2026-09-18 for everything except the `48^N` cluster: the renumbering law was Legea
   133/2018, it is now ingested as `L-133-2018`, and the concordance is readable from it.** Its
   art. I carries 1,400 Civil Code article titles in the pre-republication numbering; matching
   those titles against today's `CC-1107-2002` anchors gives an exact hit for 1,176 of them (84%),
   a rewritten-title hit for 197, and nothing for 27. Every old number this wiki had a citation
   for resolves: **330^4 → 526**, **1572^117 → 2419**, **1575^4 → 2428**, **1575^5 → 2429**,
   **1575^9 → 2433**, **1575^10 → 2434** (the whole block moves as **1575^N → 2424 + N**, checked
   on four independent points, not extrapolated from one), **1144^9 → 1614**, and **283^27 → 435**.
   Method, counts and the full table: sections AE and AF of `raw/papers/moldova-legal/_manifest.md`,
   `entities/L-133-2018.md` and `entities/L-66-2017.md`.

   **The 16 titles left unopened on 2026-09-18 are closed on 2026-09-19, and not by opening them.**
   Title matching was the wrong tool for a block; the constant shift is the right one, and it was
   run over each of the three superscript blocks of art. I at once: `1431^N → 2046 + N` (107 of
   115 titles confirmed at the predicted position), `1572^N → 2302 + N` (116 of 119),
   `1575^N → 2424 + N` (147 of 151). At every block the runner-up shift has **one** vote against
   87, 64 and 98, so the shift is not a fit but a fact. **370 of 385 old numbers therefore resolve
   by position regardless of what happened to their titles**, and the 15 that do not are the
   findings, not the failures: 8 are the repealed trade-secrets section (item 1), 3 are source
   misspellings (item 4), 2 are real substantive retitlings by LP251/2025 (art. 2389, 2391 — the
   succession reform that turned renunciation into acceptance), and 2 are numbering gaps now named
   (arts. 2404 and 2485). Section AG.4-AG.5 of the moldova-legal manifest.

   **Closed the same day for the `48^N` cluster too, by ingesting the law that introduced it.**
   Legea 133/2018 contains no `48^N` article, but it *amends* ten of them (48^5, 48^6, 48^25,
   48^32, 48^55, 48^61, 48^63, 48^75, 48^82, 48^84), which proves they already existed. The act
   that introduced them is **Legea nr. 66/2017**, now held as `L-66-2017`: its art. VI adds 100
   articles `48^1`–`48^100` to the Civil Code (the măsuri de ocrotire judiciară regime). The shift
   to today's numbering is constant — **48^N → 64 + N**, verified across the whole block with no
   exception — so **48^12 → 76, 48^15 → 79, 48^21 → 85, 48^27 → 91, 48^28 → 92, 48^30 → 94,
   48^40 → 104**. Every `48^N` citation in the vault now resolves.

   **Two method points that came out of the second act and bind the first one too.** (a) *The
   constant shift is a second, stronger proof than the title.* A title can be rewritten or
   duplicated in the code; a shift checked against neighbours cannot match by accident five times
   running. It is what settled `283^27` (identical title at both art. 435 and art. 450; neighbours
   283^24 → 432 … 283^29 → 437 give a constant +408, so 435) and `48^15` (identical title at
   art. 1478 in the mandate chapter; the shift gives 79, in the protection chapter). Use it
   whenever the title alone is not decisive. (b) *Title normalisation must cover both spelling
   reforms, not just the circumflex.* Replacing î/â with "i" before NFKD handles
   `înmormîntare`/`înmormântare` but not `sînt`/`sunt`, which produced the only unmatched title of
   the 100 in `L-66-2017` (48^74 → art. 138). So the 27 unmatched titles reported for
   `L-133-2018` art. I are an upper bound, not a count of real gaps.

   **Real gap, dated and closed the same day: `L-171-2012` arts. 81-88 were repealed by LP23 din
   27.02.2020, in force 20.04.2020 — two CNPF regulations still cite them as live legal basis.**
   `HCNPF-14-5-2016#corp` (consolidation 2022-05-06) and `HCNPF-38-5-2015#corp` (consolidation
   2025-10-01) both open "În temeiul art... art. 81 alin. (2)... art. 87 alin. (4)... art.88
   alin.(5)... din Legea nr. 171" — a live legal-basis citation, not a stray cross-reference, and
   `raw/papers/cnpf/L-171-2012.md` (our held, 2027-06-01 future-dated consolidation) jumps art.
   80 → art. 88^1 with nothing between. Checked directly on legis.md once Cloudflare cleared
   later the same session (`LP171/2012`, doc_id `156016`): the original 2013 text (doc_id 22987)
   has arts. 81-88 in full; the 30-03-2020 consolidation (doc_id 106513) still has them; the very
   next one, 20-04-2020 (doc_id 120930), does not, and its own header carries exactly one
   amending act, "MODIFICAT: LP23 din 27.02.20, MO87-93/20.03.20 art.112; în vigoare 20.04.20" —
   with no bracket marker anywhere in the body pointing to it (mechanism 2 of item 3 above). So
   this is not a wiki gap, not the `CC-1107-2002` refresh regression, and not specific to holding
   a future-dated consolidation: the articles have been gone from the *actual current* law since
   April 2020, five years before `HCNPF-38-5-2015`'s own consolidation date. Both regulations
   simply carry a stale legal-basis preamble that was never refreshed after LP23/2020 — a fact
   about CNPF's own drafting practice, not about this wiki, but worth knowing before treating
   either regulation's opening "În temeiul..." clause as proof those articles still exist. (Art.
   80 itself reappears with new content by the 15-12-2022 consolidation, doc_id 134549 — a
   separate, later insertion, not investigated further.)

   **`L-550-1995` arts. 6, 15, 31, 37^9 need no further work: they are the gutted part of the
   act.** P8-bis already established that only arts. 1-3 and 38^1-38^17 of this act are in force
   (it used to be the law on financial institutions, now "lichidarea băncilor"). These four
   unresolved numbers are exactly the kind of pre-gutting provision the act's own remaining text,
   `COD-985-2002` and `HBN-130-2013`'s legal-basis line, and `L-202-2017` still cite — same
   deleted-stub mechanism as `L-548-1995` (item 6), just not yet worth a dedicated table entry
   since none of the four is a live legal-basis citation the way `L-171-2012` art. 81 is.

   **A genuine resolver bug, found by accident, worth recording exactly: `COD-434-2023#art.389`
   modifies two different acts in one numbered block, and the graph keeps the first act's name
   across the switch.** Points 6-7 of that block amend `COD-218-2008`; the next point, "(2)
   Articolul 13^1 din Legea nr. 1134/1992 cu privire la statutul misiunilor diplomatice... va avea
   următorul cuprins", switches target explicitly — but the graph still reports this as
   `COD-218-2008` art. 13^1, which does not exist and was never meant to. The real target, "Legea
   nr. 1134/1992" (Monitorul Parlamentului 1992, nr. 8), is a different, older law from the
   `L-1134-1997` this vault holds under the same bare number (which turned out on inspection to be
   the joint-stock companies law, art. 13 "Acţiunile" — no relation). So the citation is to an act
   genuinely outside the corpus, mislabelled as an in-corpus gap. Not fixed in the script for the
   same reason as the `AA-2014` case: a multi-target amending block is a real parsing case, but a
   narrow one, not worth risking the validated graph for a single instance found this way.

   **The dependency check's top row is clean — checked, not assumed.** `L-548-1995#art.11`,
   struck in part by HCC31/2013-10-01, is cited by six structured pages (`entities/bnm.md`,
   `L-202-2017.md`, `L-232-2016.md`, `L-239-2008.md`, `L-550-1995.md`, `L-62-2008.md`, plus its
   own entity page). All six describe *today's* rewritten al.(4) — contencios administrativ under
   Codul administrativ — which is the opposite of the struck text, not the struck text itself; the
   HCC recovery of 2026-09-15 (step 5.3) already got this right. No page needed a correction.

   **The remaining 12 groups, checked one by one the same session: 7 resolved to the same
   systematic bug as the `COD-434-2023`/`AA-2014` cases above, 1 confirmed a real gap by itself,
   4 stay open.** The pattern, now confirmed eight times total, is specific enough to name
   exactly: the citing sentence names the target act only once, either at the very end of a long
   enumeration of article numbers (`din legea indicată`, `din legea menţionată`, `din Codul penal
   nr. 985/2002`) or earlier in the same paragraph with several unrelated numbers appearing in
   between — and the resolver's `intern` rule takes the nearer, wrong default (the act doing the
   citing) instead of carrying the named act forward or back across the whole sentence. Every one
   of the seven below was settled by opening both ends and finding the real target's article
   title matches the citing context on its face, same bar as the flattened-exponent checks:
   - `COD-218-2008#art.293^2` cites art. 50, 52^1, 52^2, 53, 55, 56, 58, 59, 60^1, 61-70^1, 77 and
     104 "din legea indicată" — `Legea nr. 114/2012` (named earlier in the same paragraph), not
     `COD-218-2008` itself. **Verified end to end on 2026-09-19, and the doubt recorded here was
     simply wrong:** `L-114-2012` as held does have art. 52^1 (l. 993), 52^2 (l. 1007) and 60^1
     (l. 1153), and all **42** articles art. 293^2 cites across alin. (1)-(5) carry an anchor. The
     graph reports no unresolved row against `L-114-2012` either. Nothing to fix in any file.
   - `COD-218-2008#art.440` cites art. 4 and 5^1 "din legea menţionată" — `L-131-2012`, named
     earlier in the same paragraph. `L-131-2012` art. 5^1 exists and is the same one already
     confirmed above ("Limitele generale ale controlului"). Fully resolved.
   - `COD-225-2003#art.308^17` cites art. 48^15 "în sensul" a control-of-mandate provision, in the
     same sentence as art. 48^21 and 48^27 "din Codul civil" — the same `CC-1107-2002` pre-2019
     cluster documented above, just missed by the first pass because the act name sits earlier in
     the sentence than the number. A 13th member of that cluster, not a 12th separate gap.
   - `COD-122-2003#art.269` cites art. 181^1-181^3 "din Codul penal nr. 985/2002", named at the
     very end of the enumeration — `COD-985-2002` art. 181^1 is "Coruperea electorală", exactly
     the anti-corruption-prosecutor jurisdiction the citing sentence describes. Fully resolved.
   - `COD-122-2003#art.276` cites art. 185^2 and 185^3 "din Codul penal", same pattern —
     `COD-985-2002` art. 185^2 is "Încălcarea dreptului asupra obiectelor de proprietate
     industrială", matching the citing sentence's "protecţia indicaţiilor geografice". Resolved.
   - `L-160-2026#art.40` cites art. 72 and 73 "din Legea nr. 195/2024" — `L-195-2024` art. 72 is
     "Dreptul de a depune o plângere la Centru", the near-identical twin of `L-160-2026`'s own
     art. 40 title. Fully resolved.
   - `L-202-2017#art.142` cites art. 75^2 "din Legea nr. 548/1995" — the same `L-548-1995` art.
     75^2 already confirmed in the flattened-exponent batch above ("Aplicarea sancţiunilor").
     Fully resolved.

   Not part of the pattern, and a real gap confirmed by itself: `COD-116-2018` has no art. 17^1 —
   only plain art. 17 ("Dreptul vătămat") — and `L-192-1998#art.23` cites it as a live derogation
   ("Prin derogare de la art. 17^1 alin.(4) din Codul administrativ nr. 116/2018"). No renumbering
   evidence found on a first read; left open at the time, **closed 2026-09-19 — see below.**

   **The last 4 groups, closed 2026-09-19, and three of them by one mechanism nobody had named:
   the source raising a digit that belongs on the line** (the inverse of flattening; item 2 now
   carries it, evidence in section AG.2 of the moldova-legal manifest). In each case the target
   was found by concatenating and then reading both ends, never by concatenating alone:
   - `COD-1163-1997` art. 29^1 = **art. 291 alin. (1) lit. e)**, "taxa pentru unităţile comerciale
     şi/sau de prestări servicii". Proved three ways: the letter matches, the fee matches by name,
     and the citing sentence's own exception (`art. 295 lit. g^1)`) exempts physical persons with
     independent activity from *that same fee* by name. The fact that the paragraph above cites
     `art. 291 lit. n^1)` correctly is not evidence against — it is the same article, spelled
     correctly two lines earlier, which is what a rendering defect looks like.
   - `L-202-2017` art. 13^9 and 14^1 = **art. 139** ("Măsuri de supraveghere") and **art. 141**
     ("Sancțiunile şi măsurile sancționatoare aplicabile"). `HBN-127-2013` pct. 6 applies them to a
     qualified holding pledged without approval, and art. 141 alin. (1) lit. c) is the fine on
     direct and indirect holders of holdings in bank capital — the exact addressee. The
     `art. 13 alin. (9)` hypothesis recorded here before is wrong: art. 13 is the activity
     programme and governance framework, art. 14 the permitted activities, neither related.
   - `COD-116-2018` art. 17^1 = **art. 171 alin. (4)**, second sentence: "Dacă se depune o cerere
     de suspendare a executării actului administrativ individual, acesta poate fi executat doar
     după soluționarea cererii respective." The CNPF derogation negates it element by element. The
     Administrative Code has no automatic-suspension-on-filing rule anywhere else — art. 172 has
     three alineate, art. 214 says nothing of the sort, and a corpus-wide search for "suspendă de
     drept" finds nothing in that code.
   - `L-105-2003` art. 201 is the **flattened** kind, plus a renumbering: the law has 75 articles
     and never had 201, so the number is `20^1` in the pre-republication numbering. The act was
     **republished under LP342/2023** (published 28.03.2024; the body says so at file line 102),
     and the provision is today **art. 28, "Locurile de preschimbare a mărfii"** — matched not
     only by title but by three of the four limbs the contravention enumerates, which are art. 28
     alin. (4) word for word. What stays unproved is only that the old number was `20^1` rather
     than some other flattened form; LP342/2023's own text settles it.

   **`L-213-2023` art. 84 needs no action**: the "citation" is the graph reading `COD-225-2003`
   out of a hand-written HCC editorial note inside `L-213-2023.md` itself, not a citation in legal
   text. Parser artifact, not a defect.

Resolved on 2026-09-04 and kept here so it is not re-raised: art. 21 of `L-192-1998` was absent
with no basis in the source. The refreshed consolidation contains it. No action needed.

9. **A third form of hidden deferred provision, found 2026-09-16 at `L-9-2026`.** The in-force
   register (`_meta/inforce/build_inforce_register.py`) reads only the bracket marker
   `[Art.N ... în vigoare DD.MM.YY]`, which an *amendment* leaves in the text of an already-existing
   act. `L-9-2026` (Legea privind medierea și statutul mediatorului) is a brand-new law, never
   amended, whose own final article (art. 62 alin. (1)) writes two deferred entry-into-force dates
   directly in prose — art. 44 alin. (3) lit. b) and c) at 12 months from publication, lit. a) at
   24 months — with no bracket marker at all, because there is no amendment to attach one to. The
   register does not and cannot see this. Not fixed in the script, for the same reason as the
   `HG-743-2024` case before it was fixed (item 7 above) was initially left alone: a real but narrow
   pattern, and the risk of a regression on an already-validated register outweighs the gain of one
   act's two provisions. Anyone citing `L-9-2026` art. 44 alin. (3) must check the date by hand.

   **A second instance, found 2026-09-18 at `L-66-2017`, and it shows the pattern is not confined
   to brand-new laws.** Art. XVII alin. (7) of that amending law reads "Prevederile art. 48 şi
   48^32 din Codul civil intră în vigoare după crearea condiţiilor necesare, dar nu mai tîrziu de
   2 ani de la data publicării prezentei legi" — a deferred entry into force written in prose, in
   the *amending* act's transitional article, with no bracket marker anywhere in the amended code.
   The register cannot see it, for the same reason as `L-9-2026`. Here it is harmless because the
   deadline (02.06.2019) is long past, but the shape is the one to watch: **an amending law's final
   article can defer part of what it enacts, and the deferral lives in the amending law, not in the
   act being read.** Anyone dating a provision introduced by an amending law should open that law's
   transitional article, not only the bracket markers in the target act. (The two provisions are
   today's `CC-1107-2002` art. 64 and art. 96.)
   **A third instance, found 2026-09-24 at `L-72-2025`** (the electronic communications law): art. 127
   alin. (1) sets 1 January 2026, defers arts. 96, 99-104, 106-107 and 109-113 by 24 months from
   publication (13.05.2027) and arts. 61(4)(b), 97, 98, 105, 108 to a decision of the Association Council,
   all in prose, while the fișa gives 13.05.2025 as the entry into force. Art. 127 alin. (11) also switches
   off art. 126 on 1 April 2026. The register cannot see either. Detail in `entities/L-72-2025.md`.
   **A fourth instance, found 2026-09-24 at `L-22-2025`** (concessions law, in the administrative-law batch):
   art. 54 alin. (1) defers the **whole act** to 24 months from publication (27.03.2027) and alin. (3) repeals
   `L-121-2018` then; the fișa says 31.12.2025 and the held consolidation carries a past date, so neither the
   coverage table nor the marker scan flags it. This is the first case where the deferral covers the entire
   act, not some articles. `L-435-2006` art. 16 alin. (2) is a fifth, of another kind: application conditioned on
   an action plan being approved, no date at all. The register carries a row for the whole of `L-22-2025`
   (`pending-consolidations.json`), added by hand. Detail in section AO of the moldova-legal manifest.
   **Sixth to eighth, found 2026-09-25 in the Government-functioning perimeter (section AR):** `L-246-2017` art. 19 alin. (1)
   (art. 8 alin. (2) applies only "after the reorganisation procedure of state enterprises is concluded", art. 11 alin. (1)
   from Law 287/2017), `L-82-2017`'s final clause (art. 13 alin. (2) lit. b)-f) applies until electronic filing of
   declarations is implemented), and `L-248-2025` art. 51 alin. (2)-(3) (12-month implementation deadlines from 01.09.2025).
   Same blind spot: the register reads bracket markers only. Also worth knowing: an HG bracket marker can write
   `[... în vigoare 01.07.27 ]` with a space before the closing bracket (`HG-146-2021`, `HG-149-2021`), which a naive
   regex for future markers misses.
   **Ninth, found 2026-09-25 at `L-227-2025`** (optimization of permissive acts, an amending law with 42 Roman-numeral articles): art. XLII
   alin. (1) lit. a) defers art. XX pct. 6, the new art. 4^2 alin. (8) of `L-160-2011`, to one year from publication (05.09.2026, computed) for
   central authorities and two years (05.09.2027, computed) for local ones; alin. (4) opens a two-year tacit-approval derogation from art. 6^2
   alin. (3) of the same law. It is the first case where the deferral also shows in the *target* act, as a `NOTĂ:` line under art. 4^2 alin. (8)
   in `L-160-2011`, and even there the register misses it because it reads bracket markers, not `NOTĂ`. Detail in `entities/L-227-2025.md`.
   **Tenth, the same day, at `L-317-2025`** (the law that amended `L-227-2025`): art. XVII inserts into art. XXIV alin. (1) of Law 140/2025 (migration
   of central administrative authorities) an exception that puts its arts. VI, VIII, XII, XVI, XVII, XVIII in part, and XX-XXIII in force on 30.11.2027.
   The deferral sits in an amending law and points at a **third** act; that act, `L-140-2025`, was ingested the same day and art. XXIV alin. (1)
   reads exactly so, with its `[Art.XXIV al.(1) modificat prin LP317]` marker lost in the newer consolidation (152770, 01-01-2026; the marker
   survives only in 149260). Detail in `entities/L-317-2025.md` and `entities/L-140-2025.md`.
   Two other things learned ingesting the same batch, general enough to matter beyond this act:
   `ingest_business_law.py`'s `DATE_RE` could misread a Monitorul Oficial citation like
   `MO338-341/30.09.16` as a second, spurious date (the tail of "341" plus the real date, parsed as
   day/month 41/30) — fixed with a negative lookbehind rejecting any match preceded by a digit,
   verified against the whole corpus rather than just the triggering file. And a law's article
   headings are not guaranteed to be normalised to the modern "Articolul N." form even after a
   2019 republication: `L-1125-2002` used "Art.N. -" throughout and produced zero anchors until the
   extractor's heading regex was extended to recognise that literal form (requiring a dash after
   the number, so an inline "art. 22" reference cannot be mistaken for a heading).

## Outstanding work

1. Done 2026-09-04. All seven remaining codes are ingested, so **nothing from the failed
   13 July plan is outstanding**. Method kept for the next act:
   `_meta/imports/moldova-legal/ingest_business_law.py`, which takes act names as arguments,
   resolves `<sup>` and CSS-raised superscripts before extraction, suppresses anchoring inside a
   `CUPRINS` table of contents, anchors `TITLUL` including the letter-spaced form, flags future
   consolidations, and hashes the assembled file. Verify with `verify_business_law.py` in the same
   folder. Do not add general law or codes to the CNPF script's `DOCS`: it writes into
   `raw/papers/cnpf/`, the wrong perimeter.
2. **Done 2026-09-16. Titles cut by a line break are unwrapped, corpus-wide, headings only.**
   Method: `_meta/imports/anchoring/fix_wrapped_titles.py`, reusing the DANGLING/STOP continuation
   heuristic already validated for the Civil Code (`anchor_cc.collect_article_title`). For every
   `## Articolul N. <fragment>` heading, it decides whether the line(s) immediately below are the
   missing tail of the title and, if so, rewrites **only that heading line's text** — the
   continuation line(s) stay in the body untouched, byte-for-byte, exactly the shape already
   accepted for the Civil Code's own pre-existing joins. Backed up first to
   `C:\Users\harab\wiki-backups\wiki-2026-09-16-line-unwrap\`; every one of the 61 changed files
   proved, by script, strip-and-compare byte-identical against that backup with every `#`-heading
   line removed from both sides — not just against its own pre-edit copy. **4,973 headings fixed**
   across 61 files (`raw/papers/moldova-legal/`, `raw/papers/cnpf/`, `raw/papers/bnm/`); reports in
   `_meta/lint/title-unwrap-2026-09-16-*.txt`.

   **This revises, not confirms, the "Civil Code is already clean" finding of 2026-09-05.** That
   finding was true when written — `CC-1107-2002` had gone through `anchor_cc.py`'s join logic on
   4 September and measured 22 continuations out of 13,190 lines. The refresh of **2026-09-06**
   (`refreshed: '2026-09-06'` in its frontmatter, pulling fresh doc_id 150498) replaced that
   anchored file with a new raw extraction that did **not** carry the join logic forward, silently
   reintroducing the same wrap defect as every other `ingest_business_law.py` file. This job found
   **1,097** wrapped titles in `CC-1107-2002` as it stood on 2026-09-16, not 22 — a regression that
   sat undetected for ten days because nothing re-measured the claim after the refresh. Fixed now,
   same file, same method. **Lesson for the next legis.md refresh of an already-anchored act:**
   confirm the refresh preserves prior title-joins, or re-run this script afterward — a refresh can
   silently undo point-in-time anchoring work.

   Two heuristic bugs were found and fixed while building the script, both against real corpus
   examples, before any file was written: (a) a heading with **no title at all** (`## Articolul N.`
   followed directly by body text — final/transitional articles genuinely have no title, e.g.
   `COD-218-2008` arts. 481-483) was wrongly absorbing the first body sentence, via the
   "two-sentence title" branch triggering on a title that ends in `.` with nothing before it — fixed
   by never attempting a join when the heading carries no text at all after `Articolul N.`. (b) a
   bare-numbered paragraph style (`1. Text`, no parentheses — `L-845-1992`, a 1992 act) wasn't
   recognised as a stop boundary, so `Articolul 22`'s already-complete title absorbed all of
   paragraph `1.` — fixed by adding `\d+\.` to the stop patterns alongside `(1)`. Both were caught
   by manually reading samples before writing, not by the script's own self-check (which only
   proves headings-stripped equality, not title correctness) — a reminder that the mechanical proof
   and the semantic proof are different checks, and this job needed both.

   **Audited end to end on 2026-09-18, and it was not quite clean.** The claim above — headings
   only, joins only — was checked for every one of the 68 raw files the commit touched, on the
   body (the commit also adds 9 frontmatter lines, so a whole-file comparison does not align):
   each changed heading had to be exactly the old heading joined, with a space, to the following
   source lines. **4,972 headings were clean joins; exactly one was not.** `L-105-2003` art. 36
   had a space inserted after the number, where legis.md writes `Articolul 36.Alte organe...`
   with none. Restored to the source form on 2026-09-18 (the join kept, only the space removed),
   `sha256` recomputed. The other seven flagged differences belong to other work in the same
   commit, not to the unwrap. With that one fixed, `verify_business_law.py` passes the whole
   corpus again: **58 acts, 0 failures** — it had been reporting 46 failures since this job ran,
   because its line-by-line check knew nothing about the join; it now knows that transformation
   and only that one, with the join depth measured rather than guessed.

   Original scope (measured 2026-09-05, before the CC-1107-2002 regression was known), kept for
   the record — the per-act split above is now superseded by the corpus-wide 4,973 figure:

   | act | non-empty lines | true continuations | |
   |---|---:|---:|---:|
   | `COD-985-2002` (penal) | 4,827 | 1,338 | **27.7%** |
   | `L-62-2022` (publicitate) | 705 | 82 | 11.6% |
   | `L-171-2012` (piața de capital) | 2,364 | 162 | 6.9% |
   | `CC-1107-2002` (civil) | 13,190 | 22 | 0.2% (stale — see above; refresh reintroduced it) |

   The count below (**3,097**, 42 acts) was the pre-2026-09-16 estimate, from `raw/papers/moldova-legal/`
   only and before the CC-1107-2002 regression was known; it is superseded by the **4,973** figure
   above, which covers all three raw roots and is the number actually fixed. New worst-hit list,
   by heading count: `CC-1107-2002` (1,097 — all from the 2026-09-06 regression, see above),
   `COD-218-2008` (468), `COD-122-2003` (302), `COD-985-2002` (276), `COD-154-2003` (253). The
   practical harm was that a title search failed and a quoted heading was incomplete —
   `## Articolul 7. Stabilirea, modificarea şi anularea` in Codul fiscal lost `impozitelor şi
   taxelor de stat şi locale` to the next line; searching that full phrase now finds it.
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
4. Done 2026-09-16. The three stale count lines are fixed: `L-177-2025` (0 → 4),
   `L-178-2020` (0 → 8), `L-192-1998` (0 → 34). `sha256` re-verified for all three; the
   generated coverage flag above clears on the next `build_coverage.py` run.
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
   question 5). The plan is complete. P8-bis, the three acts whose English translations had no
   Romanian text (550/1995, 250/2017, 239/2008), was done the same day; note that 550/1995 is the
   gutted former law on financial institutions, with only arts. 1-3 and 38^1-38^17 in force.
6. **From the full lint audit of 2026-09-05** (`_meta/lint/audit-2026-09-05-full.md`). The vault
   passed every generated check — validator 0 errors, coverage, SCHEMA and the in-force register
   all current, 378 raw sources with sha256 verified — and no structured page cites any of the 47
   provisions that are not yet in force, which is the check that matters most. What the audit left
   open, in the order it recommends:
   - `L-234-2016` was verified against legis.md on 2026-09-05 and is **not** a defect: art. 24 and
     Chapter IV (arts. 27-35) were repealed by LP292/2023. It exposed the marker-loss problem now
     recorded in open question 3, which is the real item: compare the remaining runs against
     legis.md's *earlier* versions before calling any of them a source defect. Then the art. 52
     anchor in open question 4.
   - Done 2026-09-16. `run_cnpf_legal_lint.py` is retired (deleted); its two checks are ported
     into `validate_wiki.py` as `page.orphan` and `citation.raw-page-level`, the latter
     generalised beyond `cnpf/`. See the `_meta/lint/` entry above for counts.
   - Done 2026-09-05. **The 278 `raw.language-other` warnings are resolved: 262 `en`, 15 `ro`, and
     the warning count is down from 280 to 3.** Only frontmatter changed; the declared `sha256`
     covers the body and all 378 raw files still verify, which is the proof no body byte moved.
     **Read this before trusting the same shortcut again.** The audit first proposed reading the
     language off the `source_record` URL. That is wrong: BNM lists Romanian PDFs on English
     catalogue pages and the reverse, and **ten files contradicted their own URL** — nine Romanian
     inflation reports and presentations filed under `/en/content/`, and `ISAP1_Final_WebVersion`,
     an English document under `/ro/content/`. The document's own text decided in every case,
     scored by stopword frequency and Romanian diacritics, with the URL and filename recorded as
     corroboration and overruled where they disagreed. One file keeps `language: other` honestly:
     `236__Prezentare_RI_mai_2025.pdf.md`, a slide deck whose PDF extraction yielded 39 words and
     no diacritics, so nothing in the file can settle it.
   - The one `raw.translation-undeclared` warning is a **false positive**:
     `raw/papers/mded-policy-2024/eu-reform-growth-facility-moldova-2024.md` is COM(2024) 469
     final, an English original of the European Commission, not a translation of a Moldovan act.
     Narrow the rule to the Moldovan and BNM roots rather than relabel a Commission document.
   - **Done 2026-09-05.** The three orphan pages created by P8-bis are linked now:
     `entities/L-550-1995.md` and `entities/L-250-2017.md` from `entities/bnm.md`, and
     `entities/L-239-2008.md` from `entities/bnm.md` and `entities/L-100-2017.md`. No page in
     `entities/`, `concepts/`, `comparisons/` or `queries/` is now without an inbound wikilink
     from outside `index.md`.
   - Done 2026-09-05. `Claude outputs/2026-09-05-plan-restructurare-wiki.md` was a byte-identical
     duplicate of the copy in `_meta/plans/`; the root copy is deleted and the `_meta/plans/` one
     verified intact at the same hash. **The folder itself stays, and it is worth watching.** It
     is outside every path the spec validates, and a second agent working on another matter wrote
     a `.docx` into it during this same session — so it is not a leftover, it collects live output
     from whatever else is running against this vault. Decide where that output belongs before it
     accumulates.
   - Done 2026-09-06. `Claude outputs/` is in `.gitignore`: it holds deliverables of other
     sessions (a contract, a memo), not wiki. It stays on disk and out of the repository.

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

Since 2026-09-06 the generated controls run in one command, in the right order (the in-force and
HCC registers first, then the citation graph that reads them, then the coverage block and
`SCHEMA.md`): `python _meta/close_session.py`. See "Closing a session" below.

## Safety

This folder is under git since 2026-09-05 (private repository `eharabara/wiki-juridic`), so a
committed file can always be compared and restored. Before any operation that writes to many
existing files, still copy the folder to `C:\Users\harab\wiki-backups\wiki-YYYY-MM-DD-<reason>\`
and confirm the copy: the strip-and-compare proof below runs against an untouched tree, not
against git's view of it.

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

## Closing a session

One command, after the log entry is written:

```
python _meta/close_session.py --commit "what was done"
```

It regenerates the in-force register, the coverage block and `SCHEMA.md` in that order, runs
the validator with a report, and only then commits and pushes. It stops at the first problem.
It refuses to commit when `log.md` has no entry dated today (decision D8; `--no-log-entry`
overrides, on purpose and visibly). It does not re-stamp the `legal-career/` copies, because the
stamp exists to catch a local edit; refreshing a copy stays manual, per D9. It does not write to
the log. Run it without `--commit` to regenerate and check only; `--check` writes nothing.

The validator alone is still `python _meta/schema/validate_wiki.py --report`. It exits 1 on
errors. It repairs nothing. Anything it finds that needs judgement goes to Eugen. A rule that
produces old errors is not relaxed to make them pass.

**The commit barrier.** `_meta/hooks/pre-commit` runs `close_session.py --check --no-hash`
before every commit and refuses the commit when a generated control is stale or the validator
finds errors (about ten seconds; hashes are left to the full run and to GitHub). Git does not
ship hooks with a clone, so once per machine: `python _meta/hooks/install.py`, which points
`core.hooksPath` at `_meta/hooks` and runs the hook once as a test. `git commit --no-verify`
skips the barrier when that is what you mean.
