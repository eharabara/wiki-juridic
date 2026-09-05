# Wiki Schema

Rewritten 2026-09-05 (plan `_meta/plans/2026-09-05-plan-restructurare-wiki.md`, decision D4). Two kinds
of text live in this file. The sections written by hand hold judgement: what the wiki is for, when a
page earns its place, how a contradiction is handled. The block between the `SCHEMA:BEGIN` and
`SCHEMA:END` markers is generated from `_meta/schema/schema-spec.yaml` and is checked by
`_meta/schema/validate_wiki.py`. Do not edit that block; edit the spec and rerun the generator.

## Domain

This wiki is a knowledge base of Moldovan law and of the policy documents that surround it, built to be
queried by a language model rather than read front to back. It holds two perimeters in one vault:

- **legal**: the CNPF and BNM perimeter laws, the codes, company law, the law on normative acts, the
  government decisions and the EU acquis extracts. A claim in this perimeter rests on an article read
  from `raw/`, and the answer says whether it was read.
- **policy**: Moldova's development strategies, the growth plan, EU accession programming, donor
  frameworks and the MDED policy corpus. A claim in this perimeter rests on the source document, with
  the document's own date and authority stated.

Real work crosses the line constantly: a transposition gap is legal by nature and political by
consequence. The perimeter field says which citation rule a page is held to, not what it may read.

The wiki preserves provenance, separates fact from interpretation, and makes method explicit. The
structured layer is a summary of the raw layer and is never cited as if it were the law.

## Conventions of judgement

- File names: lowercase, hyphenated, ASCII where practical. Legal acts keep their identifier form
  (`L-171-2012`, `COD-218-2008`, `HG-1171-2018`, `UE-648-2012`).
- Neutral, analytical language. Distinguish evidence, interpretation, open questions and
  recommendations.
- Preserve source meaning. Never rewrite, correct, harmonise or reflow legal text. Where structure is
  added to a raw file, prove the text survived unchanged, against a backup, not against a working copy.
- For facts, statistics, legal provisions and institutional claims, record provenance in `sources:`
  and, for multi-source syntheses, with inline markers of the form `[raw/papers/cnpf/L-171-2012.md art.4]`.
- Prefer tables for comparisons, mandates, indicator frameworks and programme architecture.
- When updating a page, bump `updated`. A scripted metadata-only change (such as adding a field to every
  page) may leave `updated` alone if the log records the operation and git holds the diff.

## Page thresholds

- Create a page when an act, institution, concept, programme, dataset, indicator or method is central
  to one source or appears across two or more.
- Add to an existing page when a source mentions something already covered.
- Do not create pages for passing mentions, incidental names or details outside the domain.
- Split a page when it exceeds roughly 200 lines or mixes topics that deserve separate treatment.
- Archive a page when it is superseded or when it is a working artefact rather than knowledge: move it
  to `_archive/<topic>-<yyyy-mm>/`, write a `_PROVENANCE.md` there saying where it came from and why it
  was withdrawn, remove it from `index.md`, and redirect inbound links to the explicit archive path.
  Raw files are never edited to redirect a link; their redirects are declared in the spec instead.

## Entity pages

Institutions, legal acts, programmes, data sources, major reports, named reform initiatives. Include:
what it is; mandate or role; key facts, dates, legal basis, consolidation date and whether the
consolidation is already in force; relations to other pages through wikilinks; source references; open
questions or verification needs.

## Concept pages

Policy concepts, reform areas, acquis instruments, methods, indicators, recurring analytical themes.
Include: definition; relevance to Moldova or to accession; current state of knowledge; measurement or
method where relevant; risks, debates, open questions; related concepts.

## Comparison pages

Side-by-side analysis: mandates, legal provisions, transposition status, policy options, programme
designs. Include: what is compared and why; dimensions, preferably as a table; similarities and
differences; verdict or implications; sources and a confidence note.

## Query pages

Substantial answered questions that would be costly to re-derive. Include: the question; the short
answer; evidence and synthesis; pages and sources consulted; follow-ups. Drafting artefacts (draft
laws, audit tables, method tests) are not query pages; they go to `_archive/` with a provenance note
once the work that produced them is closed.

## Update policy

When new information conflicts with existing content:

1. Check source date, authority and scope. An official or more recent source may supersede an older
   secondary one, but do not assume it.
2. If the claims genuinely conflict, record both, with dates and sources.
3. Mark the page `contested: true` and, where possible, `contradictions: [page-slug]`.
4. Record the conflict in `log.md` and in any answer that rests on the page.
5. Do not delete or overwrite a prior claim unless it is clearly obsolete and the source trail is kept.

## Quality rules

- Prefer primary sources for legal, institutional, budgetary, statistical and programme claims.
- A provision from an act whose consolidation is dated in the future may be correctly anchored and
  still not bind today; check `_meta/inforce/in-force-register.md` and say which version applies.
- A translation locates a provision; the citation comes from the Romanian text.
- For acquis content, note chapter and cluster where known.
- For programme architecture, distinguish objectives, implementing partners, beneficiaries, funding,
  period, indicators and governance.
- When source language matters, keep the exact quoted term and note the language.

## Mechanical rules

<!-- SCHEMA:BEGIN - generated by _meta/schema/build_schema.py from _meta/schema/schema-spec.yaml, do not edit by hand -->

Generated from `_meta/schema/schema-spec.yaml` (version 2026-09-05). Every rule below is checked by `python _meta/schema/validate_wiki.py`. To change a rule, edit the spec, rerun `python _meta/schema/build_schema.py`, then run the validator.

### Layers

| Folder | Role | Page types allowed |
|---|---|---|
| `entities/` | structured layer: summaries and analysis, cited as analysis, never as law | `entity` |
| `concepts/` | structured layer: summaries and analysis, cited as analysis, never as law | `concept` |
| `comparisons/` | structured layer: summaries and analysis, cited as analysis, never as law | `comparison` |
| `queries/` | structured layer: summaries and analysis, cited as analysis, never as law | `query`, `summary` |
| `raw/papers/cnpf/` | raw source text, immutable, perimeter `legal` | — |
| `raw/papers/moldova-legal/` | raw source text, immutable, perimeter `legal` | — |
| `raw/papers/bnm/` | raw source text, immutable, perimeter `legal` | — |
| `raw/papers/moldova-policy/` | raw source text, immutable, perimeter `policy` | — |
| `raw/papers/mded-policy-2024/` | raw source text, immutable, perimeter `policy` | — |
| `_archive/` | frozen content; not validated; link target only by explicit path | — |
| `_meta/` | scripts, plans, old logs, working files; not validated; never a wikilink target | — |

Files under a raw root whose name starts with `_`, `README` or is one of `BNM_LEGISLATION_INVENTORY.md`, `BNM_REPORTS_INVENTORY.md` are metadata, not sources, and carry no source frontmatter. Names starting with `md-` are working papers extracted from DOCX: they need source frontmatter but are not normative text: a page may cite them as a working document, never as law.

### Perimeters

Every structured page carries `perimeter:` with one of `legal`, `policy`. A page may cite sources from both perimeters; the field says which citation rule applies to the page, not where it may read from.
A page must have at least one source under a raw root of its own perimeter.

### Frontmatter of structured pages

```yaml
---
title: Page title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary
perimeter: legal | policy
tags: [from the taxonomy below; must include the type tag]
sources: [raw/papers/<root>/<file>.md, ...]
# optional
confidence: high | medium | low
contested: true
contradictions: [other-page-slug]
imported_from: <original path, for pages carried over from an earlier wiki>
authority: <free text>
---
```

- Required: `title`, `created`, `updated`, `type`, `perimeter`, `tags`, `sources`. Optional: `confidence`, `contested`, `contradictions`, `imported_from`, `authority`. Any other key is reported.
- `type` must be allowed in the page's folder (table above).
- Dates are `YYYY-MM-DD`; `updated` is not before `created`; `updated` is not in the future.
- At least 1 tag, all from the taxonomy, including the page's own type tag.
- At least 1 source; every source path must exist.
- At least 2 distinct outbound wikilinks in the body, or the tag `needs-links`.

### Frontmatter of raw sources

```yaml
---
source_url: https://...
ingested: YYYY-MM-DD
sha256: <hex digest of the body after the closing --->
source_type: legal-text | translation | report | note | dataset | article | paper | transcript | webpage
publisher: <institution>
language: ro | en | ru | other
# optional, written by the anchoring scripts
sha256_convention: raw | LF
sha256_pre_anchoring: <hash before structural anchors were added>
---
```

- Required: `source_url`, `ingested`, `sha256`, `source_type`, `publisher`, `language`. Ingest scripts add their own keys (doc_id, consolidation_date, instrument_id, …); those are not restricted.
- `sha256` is computed over the body, under one of two conventions: `raw`, `LF` (raw bytes, or CRLF normalised to LF). The validator accepts either; if neither reproduces the recorded digest, the text changed after it was last hashed, which is an error. A declared `sha256_convention` must match the convention that reproduces the digest.
- `sha256_pre_anchoring` records the digest before anchors were inserted. It is provenance, not a check: proving the body survived anchoring is the job of the anchoring verify scripts.
- **Translations (D2).** `source_type: translation` marks a text that is not authoritative. It must carry no `## Articolul` anchors: an anchor on a translation would assert that the text can be cited, and it cannot. A `legal-text` file with 20 or more body lines matching `^Article\s+\d` is reported as an undeclared translation (warning until the English BNM corpus is retired, P9).

### Tag taxonomy

Closed list. A new tag is added to the spec before it is used; the validator reports any other tag.

- **geography and institutions:** `moldova`, `eu`, `accession`, `institution`, `donor`, `municipality`, `regional-development`
- **policy and reform areas:** `economic-policy`, `macroeconomics`, `competitiveness`, `sme`, `investment`, `trade`, `infrastructure`, `digital-transformation`, `innovation`, `public-administration`, `regulatory-reform`, `legal-approximation`, `governance`, `anti-corruption`, `procurement`, `public-finance`, `labour-market`, `education-skills`, `energy`, `agriculture`
- **financial services legal approximation cnpf:** `cnpf`, `bnm`, `financial-services`, `financial-supervision`, `capital-market`, `securities`, `insurance`, `non-bank-credit`, `credit-bureau`, `pensions`, `company-law`, `consumer-protection`, `aml-cft`, `eu-acquis`, `transposition`, `legal-act`, `legal-source`, `import`
- **evidence indicators methods:** `indicator`, `composite-index`, `methodology`, `data-source`, `statistics`, `dashboard`, `evaluation`, `monitoring`, `theory-of-change`, `programme-design`
- **document and knowledge types:** `entity`, `concept`, `comparison`, `query`, `summary`, `timeline`, `source-note`, `needs-links`, `contested`

### Wikilinks

Base names are ambiguous in this vault: `entities/L-171-2012.md`, `raw/papers/cnpf/L-171-2012.md` and several archived copies share a name. So resolution is fixed, not left to the editor:

- A bare `[[name]]` resolves in this order: `structured`, `raw`, `root`. The first layer that has the name wins. So `[[L-171-2012]]` is the entity page; the raw text is `[[raw/papers/cnpf/L-171-2012]]`.
- Pages under `_archive`, `_meta` can only be linked by explicit path, e.g. `[[_archive/emir-2026-07/name|name]]`.
- Every wikilink in the structured layer, in raw sources and in the root files must resolve.
- Raw files are immutable, so a raw file may keep a bare link to a page that has since been archived only if the redirect is declared in the spec and in the archive's `_PROVENANCE.md`:
  - `raw/papers/cnpf/_manifest.md` → `verificare-schelet-lege-emir-2026-07-03`, `emir-draft-complet-2026-07-10`, `emir-audit-conformitate-lege100-hg1171-2026-07-10` (declared in `_archive/emir-2026-07/_PROVENANCE.md`)
  - `raw/papers/cnpf/md-2026-07-03-schelet-lege-emir.md` → `verificare-schelet-lege-emir-2026-07-03` (declared in `_archive/emir-2026-07/_PROVENANCE.md`)

### `index.md`

- Two perimeter sections: `## Perimetrul juridic` (legal), `## Perimetrul de politici` (policy); inside each, type sections `### Entities`, `### Concepts`, `### Comparisons`, `### Queries`.
- Every structured page is listed exactly once, under its perimeter and type, as `- [[name]] — one-line summary`. Nothing is listed without a file.
- The header line `Total pages: N` must equal the number of structured pages.

### `log.md`

Git records what changed; the log records what was learned and what was decided (D8). One entry per action:

```markdown
## [YYYY-MM-DD] action | subject

- **Aflat:** …
- **Decis:** …
- **Unde:** …
```

- `action` is one of `create`, `update`, `ingest`, `archive`, `delete`, `lint`, `query`, `decision`.
- The three fields appear in this order in every entry. Older logs live in `_meta/log/` and are not written to.

### Copies in `legal-career/`

The method documents are copies; the master is the claude.ai project "Legal Wiki" (D9). Each copy carries a provenance stamp in its frontmatter:

```yaml
---
copy_of: legal-career/<file>.md
master: "claude.ai project \"Legal Wiki\""
taken: YYYY-MM-DD          # when the body was copied from the project
stamped: YYYY-MM-DD        # when this stamp was written
sha256_body: <hex digest of the body, LF convention>
local_notes: true | false  # whether the copy carries a note that exists only here
refresh: on-master-change | every-session
---
```

- Required: `copy_of`, `master`, `taken`, `stamped`, `sha256_body`, `local_notes`, `refresh`. `copy_of` must equal the file's own path.
- The body hash must reproduce: a mismatch means the copy was edited locally, which is an error. Refresh by replacing the body with the project's text and running `python _meta/schema/stamp_copies.py`.
- A copy with `refresh: every-session` (the matter log) is warned about whenever `taken` is before today: it is refreshed from the project at the start of any session that touches the wiki.

### Hygiene

- No file or folder name may contain U+F03A, U+F05C: these are the MSYS substitutes for `:` and `\`, and a name carrying them is a Windows path that a script wrote as a name under a POSIX shell.
- Empty folders under `entities`, `concepts`, `comparisons`, `raw`, `_archive` are reported as leftovers.
- `python _meta/coverage/build_coverage.py --check` must report the CLAUDE.md coverage block as up to date.

### Running the validator

```bash
python _meta/schema/validate_wiki.py --report
```

Exit code 1 on any error. Warnings do not block. Findings are shown, not repaired: anything that needs judgement goes to Eugen. Run it at the end of every session that touched the vault, after `build_coverage.py`.

<!-- SCHEMA:END -->
