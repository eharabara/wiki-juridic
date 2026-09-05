# Wiki Schema

## Domain

This wiki covers Moldova-focused policy and evidence work, especially:

- Moldova economic policy, macroeconomic and sectoral development, competitiveness, SMEs, investment climate, infrastructure, regional development, digital transformation, innovation, and private-sector reform.
- Moldova's EU accession, EU acquis approximation, institutional reform, programming, conditionality, donor coordination, and development architecture.
- Evidence and methodology behind composite indicators, dashboards, policy briefs, reports, and analytical products relevant to Moldova.

The wiki is intended to become a durable, source-backed research memory for future analysis, report drafting, programme design, and policy advice. It should preserve provenance, separate facts from interpretation, and make methodological choices explicit.

## Conventions

- File names: lowercase, hyphenated, no spaces, ASCII where practical; Romanian/Moldovan proper nouns may be transliterated when useful.
- Every wiki page starts with YAML frontmatter using the fields below.
- Use Obsidian-style `[[wikilinks]]` for links between wiki pages.
- Every new or substantially updated wiki page should include at least 2 outbound wikilinks where possible. If the wiki is still too small to support this, add `needs-links` in tags and revisit later.
- When updating a page, always bump the `updated` date.
- Every new page must be listed in `index.md` under the correct section with a one-line summary.
- Every action must be appended to `log.md`.
- Use neutral, policy-analytical language. Distinguish evidence, interpretation, open questions, and recommendations.
- Preserve source meaning. Do not silently rewrite or over-interpret legal/policy language.
- For facts, statistics, legal provisions, programme details, and institutional claims, record provenance clearly in `sources:` and, for multi-source syntheses, with inline provenance markers.
- Prefer tables for comparisons, indicator frameworks, institutional responsibilities, and programme architecture.

## Frontmatter

Every wiki page in `entities/`, `concepts/`, `comparisons/`, or `queries/` must begin with:

```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary
tags: [from taxonomy below]
sources: [raw/articles/source-name.md]
# Optional quality signals:
confidence: high | medium | low
contested: true
contradictions: [other-page-slug]
---
```

Use `confidence: low` for single-source, uncertain, politically sensitive, fast-moving, or interpretation-heavy material. Use `confidence: high` only when claims are well-supported across reliable sources or primary official documents.

## Raw Source Frontmatter

Raw sources in `raw/` are immutable and should begin with:

```yaml
---
source_url: https://example.com/source
ingested: YYYY-MM-DD
sha256: <hex digest of the raw content below this frontmatter>
source_type: article | paper | legal-text | report | dataset | transcript | note | webpage
publisher: Publisher or institution, if known
language: en | ro | ru | other
---
```

Compute `sha256` over the body after the closing `---`, not over the frontmatter. On re-ingest of the same URL or file, compare hashes and flag drift instead of silently replacing source material.

## Tag Taxonomy

Only use tags listed here. If a new tag is needed, add it to this section before using it.

### Geography and institutions
- moldova
- eu
- accession
- institution
- donor
- municipality
- regional-development

### Policy and reform areas
- economic-policy
- macroeconomics
- competitiveness
- sme
- investment
- trade
- infrastructure
- digital-transformation
- innovation
- public-administration
- regulatory-reform
- legal-approximation
- governance
- anti-corruption
- procurement
- public-finance
- labour-market
- education-skills
- energy
- agriculture

### Financial services, legal approximation, and CNPF
- cnpf
- bnm
- financial-services
- financial-supervision
- capital-market
- securities
- insurance
- non-bank-credit
- credit-bureau
- pensions
- company-law
- consumer-protection
- aml-cft
- eu-acquis
- transposition
- legal-act
- legal-source
- import

### Evidence, indicators, and methods
- indicator
- composite-index
- methodology
- data-source
- statistics
- dashboard
- evaluation
- monitoring
- theory-of-change
- programme-design

### Document and knowledge types
- entity
- concept
- comparison
- query
- summary
- timeline
- source-note
- needs-links
- contested

## Page Thresholds

- Create a page when an entity, concept, programme, institution, dataset, indicator, reform area, or methodology is central to one source or appears across 2+ sources.
- Add to an existing page when a source mentions something already covered.
- Do not create pages for passing mentions, incidental names, or details outside the domain.
- Split a page when it exceeds roughly 200 lines or mixes distinct topics that deserve separate treatment.
- Archive a page when it is fully superseded: move it to `_archive/`, remove it from `index.md`, and update inbound links.

## Entity Pages

Use for institutions, organisations, programmes, legal acts, data sources, dashboards, major reports, and named reform initiatives.

Include:

- Overview / what it is
- Mandate or role, where relevant
- Key facts, dates, legal basis, programme period, budget, or institutional responsibility
- Relationship to other entities and concepts via `[[wikilinks]]`
- Source references
- Open questions or verification needs

## Concept Pages

Use for policy concepts, reform areas, methodologies, indicators, and recurring analytical themes.

Include:

- Definition / explanation
- Relevance to Moldova and/or EU accession
- Current state of knowledge
- Measurement or methodological considerations, where relevant
- Risks, debates, or open questions
- Related concepts via `[[wikilinks]]`

## Comparison Pages

Use for side-by-side analysis: policy options, indicator methods, donor programmes, institutional mandates, legal provisions, or reform approaches.

Include:

- What is being compared and why
- Dimensions of comparison, preferably in table format
- Key similarities/differences
- Verdict, synthesis, or implications
- Sources and confidence notes

## Query Pages

Use for substantial answered questions that would be costly to re-derive.

Include:

- The user question or research question
- Short answer
- Evidence and synthesis
- Pages/sources consulted
- Follow-up questions

## Update Policy

When new information conflicts with existing content:

1. Check source date, authority, and scope. Official/legal/current sources may supersede older secondary sources, but do not assume this automatically.
2. If claims genuinely conflict, record both positions with dates and sources.
3. Mark the relevant page with `contested: true` and, where possible, `contradictions: [page-slug]`.
4. Flag the issue in `log.md` and in any user-facing report.
5. Do not silently delete or overwrite prior claims unless they are clearly obsolete and the source trail is preserved.

## Quality Rules

- Prefer primary sources for legal, institutional, budgetary, statistical, and programme claims.
- For composite indicators and dashboards, document: purpose, components, normalization, weighting, aggregation, missing-data handling, update frequency, and limitations.
- For policy recommendations, clearly separate diagnosis, evidence, assumptions, and proposed action.
- For EU accession/acquis content, note chapter/cluster relevance when known.
- For donor/programme architecture, distinguish objectives, implementing partners, beneficiaries, funding, time period, indicators, and governance arrangements.
- When source language matters, keep exact quoted terminology and note the language.
