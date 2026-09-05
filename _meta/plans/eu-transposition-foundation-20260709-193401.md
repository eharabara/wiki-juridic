# EU Transposition Foundation Plan — Steps 1–3

**Date:** 2026-07-09  
**Scope:** transform Legea 100/2017 + the correct EU-harmonisation HG into an operational wiki foundation for future directive/regulation transposition tasks.

## Step 1 — Source pack correction and preservation

**Objective:** make the source base unambiguous: Legea 100/2017 is the general normative-procedure law; HG1171/2018 is the EU-harmonisation regulation; HG1170/2016 is a separate land-transfer act and should remain only as a literal-source correction.

**Actions:**
- Fetch `HG1171/2018` from legis.md (`doc_id=144185`) through `showdetails`.
- Preserve full raw text under `raw/papers/moldova-legal/HG-1171-2018.md` with source metadata and SHA.
- Create `entities/HG-1171-2018.md` and update `entities/L-100-2017.md` to point to the corrected harmonisation source.
- Keep `entities/HG-1170-2016.md` as non-core / disambiguation evidence.

## Step 2 — Method page

**Objective:** create one reusable synthesis page that says how future Moldova/EU transposition tasks should proceed.

**Output:** `concepts/moldova-eu-transposition-method.md`.

## Step 3 — Operational rule matrix

**Objective:** turn imperative legal requirements into checkable controls.

**Output:** `concepts/moldova-eu-transposition-rule-matrix.md`, with rule IDs, source basis, trigger, check, required output, and severity.

## Verification

- Raw SHA validates for all `raw/papers/moldova-legal/*.md` files.
- New pages have required frontmatter and schema-approved tags.
- No broken wikilinks.
- New active pages are in `index.md`.
- `log.md` records the action and backup path.
