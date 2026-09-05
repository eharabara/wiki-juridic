# Task: complete the raw-layer article anchoring in the LLM Wiki

You are working on a legal knowledge base at `C:\Users\harab\wiki`. It is a Moldovan law wiki
built to be queried by a language model. Read `SCHEMA.md` at the root before you touch anything.
It sets the file conventions, the frontmatter contract, and the rule that sources under `raw/`
are treated as immutable. Also read `raw/papers/cnpf/_manifest.md`, which is the source register.

The wiki is NOT under version control. Before any write, copy the whole `wiki` folder to
`C:\Users\harab\wiki-backups\wiki-YYYY-MM-DD-pre-anchoring\`. Confirm the copy exists and has
the same file count before proceeding.

## Why this work matters

Every substantive answer built on this wiki must carry a confidence line: anchored, partially
anchored, or not anchored. That line is only trustworthy if the raw layer can actually be cited
to article level. A partially anchored knowledge base does not fail loudly. It returns something
plausible for almost any query, and the missing provision simply never appears. Completing the
anchoring inside the existing perimeter comes before extending the wiki to new areas.

## What the audit already established. Do not redo it.

A mechanical audit on 2026-09-04 compared the declared article count against the actual heading
anchors in every file under `raw/papers/`. Results:

**Clean, leave alone.** L-1-2018, L-106-2022, L-1134-1997, L-122-2008, L-181-2023, L-198-2020,
L-2-2020, L-92-2022, L-308-2017. Declared count equals anchor count, numbering dense.

**Not defects, do not "fix".**
- `L-234-2016` is missing art. 24 and arts. 27 to 35. These are real repeals by LP292 of
  19.10.2023, correctly preserved in the text as `[Art.24 abrogat prin ...]`.
- `HG-1170-2016` and `HG-1171-2018` have zero article anchors because government decisions are
  structured in numbered points, not articles. HG-1171 already declares "puncte numerotate
  detectate: 65".
- `L-178-2020` and `L-177-2025` are pure amending laws with no articles of their own.
- The EU files under `raw/papers/cnpf/UE-*.md` are declared structured extracts, not full text.
  Their sparse article numbering is by design.

**Three real defects, listed below as jobs 1 to 3.**

---

## Job 1. Anchor the Civil Code

File: `raw/papers/moldova-legal/CC-1107-2002.md`, 2,057,333 characters, extracted with PyMuPDF
from an 873-page consolidated PDF. The full text is present. It has zero markdown headings,
because it never passed through the legis.md ingest script that creates them.

Established facts, verify them yourself before relying on them:
- 2,657 lines begin with `Articolul N`. Numbers run 1 to 2671, with no duplicates.
- The 14 absent numbers are 2047 to 2054, 2171, 2172, 2185, 2188, 2404, 2485. Check each one
  against the surrounding text for an `abrogat` marker. Record what you find. Do not invent an
  article, and do not renumber anything.
- Structural markers at line start: `Cartea` (5), `Capitolul` (109), `Secțiunea` (111),
  `Subsecțiunea` (10). There are no `Titlul` lines.

Heading convention. Match the existing corpus exactly, so one retrieval rule works everywhere.
Look at `raw/papers/cnpf/L-198-2020.md` for the pattern. Articles sit at `##`:

```
## Cartea a doua
## Capitolul IV
### Secțiunea a 2-a. ...
#### Subsecțiunea 1. ...
## Articolul 512. Noțiunea de obligație
```

Article titles are hard-wrapped by the PDF extraction. Article 2's title runs across two lines
(`Articolul 2. Raporturile reglementate de legislaţia` / `civilă`). Join the continuation into
the heading. Rule: after `Articolul N.`, keep appending following lines while the next line does
not begin a new paragraph marker — `(1)`, `(2)`, a lettered point such as `a)`, an opening `[`,
or any of `Articolul`, `Cartea`, `Capitolul`, `Secțiunea`, `Subsecțiunea`. Cap the title at 200
characters and report every heading over 150 characters so it can be checked by hand.

Do not change the body text in this pass. The body is hard-wrapped throughout, which is a
separate question. Count how many body lines are wrapped mid-sentence, report the number, and
propose whether to unwrap in a second pass. Do not unwrap now.

Frontmatter. Preserve `source_file_sha256`, which is the PDF hash and the real provenance
anchor. Move the existing `sha256` to `sha256_pre_anchoring`, compute the new `sha256` over the
body after the closing `---`, and add `articole detectate: <count>`, `anchoring_date`, and a
one-line `anchor_convention` note.

## Job 2. Anchor L-192-1998, and sweep for the same defect

File: `raw/papers/cnpf/L-192-1998.md`. This is the law that constitutes CNPF and defines its
mandate. It records "articole detectate: 0" while holding 44,808 characters of full text. The
cause is drafting style: it uses the pre-2000 form `Art.1. – ` rather than `Articolul 1.`, so
the ingest regex matched nothing. Every mandate-boundary finding in the wiki currently rests on
a source that cannot be cited to article level.

Convert `Art.N. – ` at line start into `## Articolul N. <title>` where a title exists, or
`## Articolul N.` where the text runs straight into the provision. Keep the original `Art.N. –`
token at the start of the body line so the extracted text is not altered, only preceded by an
anchor. Apply the same frontmatter treatment as job 1.

Then sweep every file under `raw/papers/` for the same pattern: files declaring zero articles
while containing line-initial `Art.` forms. Report what you find before fixing anything beyond
L-192-1998.

## Job 3. Fix superscript articles

Moldovan drafting inserts articles as 146¹, 50¹, 70¹. The extraction flattened the superscript,
so article 146¹ of L-171-2012 is stored as `## Articolul 1461`. Same defect in L-139-2007
(art. 50¹ stored as 501) and L-100-2017 (art. 70¹ stored as 701).

This is worse than a missing anchor, because it does not look missing. A citation to art. 146¹
is unfindable, and a query for art. 146 sits beside a neighbour that reads as article one
thousand four hundred sixty-one.

Detect candidates by position, not by number alone: a heading whose number is far outside the
act's article range and which immediately follows an article whose number is its prefix. Verify
each candidate against the body text, where the original often appears as `Art.146^1` or in an
amendment note such as `[Art.1461 introdus prin LP...]`. Normalise the heading to
`## Articolul 146^1. <title>` and add a `superscript_articles:` list to the frontmatter naming
every one you changed. Report any candidate you could not confirm rather than guessing.

---

## How to work

1. Back up first, as set out above.
2. Do each job on a copy under `_meta/anchoring-work/` first. Show me a unified diff, or for the
   Civil Code a representative sample plus the full statistics, and wait for my go-ahead before
   writing over the file in `raw/`.
3. Write the scripts to `_meta/imports/anchoring/` so the work is repeatable, not one-off
   commands lost to the shell.
4. Never rewrite, correct, harmonise or reflow legal text. You are adding structure around text
   that must stay byte-identical apart from the headings you insert. Prove this: for every file
   you touch, strip all lines you added and confirm the remainder is identical to the original.
   Report the check result explicitly.

## Verification, required before you call any job done

- Anchor count equals the count of line-initial article markers in the source.
- Article numbers are strictly ascending within each act, with every break explained by a
  recorded repeal.
- The strip-and-compare check above passes.
- Re-run `_meta/lint/run_cnpf_legal_lint.py` and compare the output against
  `_meta/lint/cnpf-legal-lint-2026-07-09.json`. Report what changed and why.

## What to update when the work is done

- `raw/papers/cnpf/_manifest.md` and `raw/papers/moldova-legal/_manifest.md`: corrected article
  counts, the anchoring date, and the repeal findings from job 1.
- `log.md`: one entry per job, per the SCHEMA convention.
- `index.md`: only if a page's status line changes.
- A short note at `_meta/plans/` recording what is now anchored and what is not, written so it
  can be pasted into the project knowledge map.

## One thing to report but not act on

Some raw texts are years behind their current consolidation. `L-308-2017` is held at the
2018-12-01 version, `L-92-2022` at 2023-01-01 although the manifest says the law was later
amended. The anchoring on these is clean, which makes them the most dangerous files in the wiki:
well-formed, confidently citable, and superseded. List every file whose `consolidation_date` is
more than two years old, with the date, and stop there. Refreshing them from legis.md is a
separate task.
