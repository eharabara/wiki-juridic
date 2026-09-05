# WikiLLM Guidebook for Moldova Policy & Economic Intelligence

**A practical operating manual for using your `C:\Users\harab\wiki` knowledge base as a durable research, policy, dashboard, and EU-accession memory system**

Prepared for: **Eugeniu Harabara**  
Date: **2026-07-08**  
Wiki location: **`C:\Users\harab\wiki`**

---

## How to use this guidebook

This guidebook is meant to be a working manual, not a theoretical essay. It tells you how to use your WikiLLM-style knowledge base as a long-term knowledge system for Moldova-focused policy work, EU accession, economic reform, donor/programme architecture, composite indicators, and analytical dashboards.

You can use it in three ways:

1. **As a daily operating manual** — when you have a PDF, legal text, report, dataset, meeting note, or web article and want to ingest it into the wiki.
2. **As a research design manual** — when you want to build a structured evidence base for a policy report, programme concept note, dashboard, methodology note, or EU Careers writing sample.
3. **As a quality-control manual** — when you want to prevent weak evidence, duplicate pages, vague methodology, or AI-generated synthesis from contaminating your knowledge base.

The core idea is simple:

> Raw sources are preserved as evidence. Wiki pages are structured synthesis. Reports, briefs, dashboards, and presentations are outputs generated from that synthesis.

---

## Contents

1. Executive summary
2. The operating philosophy
3. Your current wiki architecture
4. Roles: what you do and what the agent does
5. The knowledge lifecycle
6. What to ingest first
7. Source-ingestion playbooks
8. Page types and when to use them
9. Templates for reusable pages
10. Moldova-specific examples
11. Using the wiki for composite indicators and dashboards
12. Using the wiki for EU accession and legal approximation
13. Using the wiki for donor and programme architecture
14. Querying the wiki effectively
15. Prompt cookbook
16. Obsidian and browsing tactics
17. Quality assurance and linting
18. Governance routines
19. A 30-day implementation plan
20. Appendices: checklists and templates

---

# 1. Executive summary

Your wiki should become a **policy intelligence system** for Moldova. It should not be a passive note archive and it should not merely store AI summaries. Its purpose is to make knowledge **durable, inspectable, reusable, and source-backed**.

The best use of your wiki is to repeatedly turn sources into four reusable knowledge assets:

| Asset | Folder | Purpose |
|---|---|---|
| Raw sources | `raw/` | Immutable evidence archive |
| Entity pages | `entities/` | Institutions, programmes, legal acts, datasets, reports, organisations |
| Concept pages | `concepts/` | Policy themes, methods, indicators, reform areas, analytical frameworks |
| Comparison/query pages | `comparisons/`, `queries/` | Reusable synthesis, tables, policy answers, decision support |

The strategic principle is:

> Do not ask the agent to remember everything in chat. Ask the agent to maintain a wiki that remembers for you.

The tactical principle is:

> Every useful source should either update an existing page, create a justified new page, or expose a gap/contradiction.

The wiki becomes more valuable over time when the same pages are improved by multiple sources. For example:

- `concepts/sme-competitiveness.md` should mature as you ingest OECD, World Bank, EU, government, and donor sources.
- `concepts/composite-indicators.md` should become your methodological backbone for dashboard design.
- `entities/european-commission.md`, `entities/eu-delegation-to-moldova.md`, and `entities/government-of-moldova.md` should become stable reference points.
- `comparisons/composite-indicator-weighting-options.md` should help you explain methodology choices transparently.
- `queries/what-indicators-best-capture-moldova-economic-resilience.md` should preserve a valuable answer you may reuse in reports.

The wiki should help you answer questions like:

- What are the recurring constraints to Moldova's SME competitiveness?
- Which reforms are linked to EU accession economic governance?
- What sources support each component of a composite economic indicator?
- Which donors work on digital transformation, regional development, SMEs, public administration, or procurement?
- Where do official claims and outcome indicators diverge?
- What are the strongest source-backed claims for a policy memo?
- Which methodology choices need to be documented before publishing a dashboard?

---

# 2. The operating philosophy

## 2.1 WikiLLM is not just RAG

A normal retrieval-augmented system often works like this:

```text
Question → retrieve chunks → answer → forget
```

A WikiLLM-style system works like this:

```text
Source → preserve raw evidence → compile into pages → cross-link → update over time → answer from the maintained wiki
```

The difference matters. In policy work, you need more than a clever answer. You need:

- provenance;
- stable terminology;
- traceable sources;
- institutional memory;
- clear methodology;
- explicit uncertainty;
- cumulative synthesis;
- reusable outputs.

The wiki should therefore behave like a **research department memory**, not a chat transcript.

## 2.2 The three-layer model

Your wiki has three layers:

### Layer 1: raw sources

Stored in:

```text
raw/articles/
raw/papers/
raw/transcripts/
raw/assets/
```

These are the evidence. They should be treated as immutable. If a source changes, save a new version or flag source drift. Do not casually edit raw sources.

### Layer 2: structured wiki pages

Stored in:

```text
entities/
concepts/
comparisons/
queries/
```

These are the agent-maintained synthesis layer. Pages should be concise, structured, source-backed, and linked.

### Layer 3: navigation and governance

Stored in:

```text
SCHEMA.md
index.md
log.md
_meta/
```

These files tell the agent how to behave, what pages exist, and what has changed.

## 2.3 The most important rule

> The wiki is valuable only if it improves with every source.

A single-source wiki is mostly a summary archive. A multi-source wiki becomes a compounding knowledge system.

For example, after five sources on SME competitiveness, the page should not be five pasted summaries. It should become a structured synthesis:

- recurring constraints;
- where sources agree;
- where they differ;
- policy instruments mentioned;
- implementation bottlenecks;
- evidence gaps;
- links to indicators, institutions, donors, and EU accession themes.

---

# 3. Your current wiki architecture

Your wiki is located at:

```text
C:\Users\harab\wiki
```

Current structure:

```text
wiki/
├── SCHEMA.md
├── index.md
├── log.md
├── raw/
│   ├── articles/
│   ├── papers/
│   ├── transcripts/
│   └── assets/
├── entities/
├── concepts/
├── comparisons/
├── queries/
├── _archive/
└── _meta/
```

The schema domain is Moldova-focused policy and evidence work, especially:

- economic policy;
- macroeconomic and sectoral development;
- competitiveness;
- SMEs;
- investment climate;
- infrastructure;
- regional development;
- digital transformation;
- innovation;
- private-sector reform;
- EU accession and acquis approximation;
- donor coordination and development architecture;
- composite indicators and dashboards;
- policy briefs and analytical reports.

This domain is broad enough to support your work, but narrow enough to maintain discipline.

---

# 4. Roles: what you do and what the agent does

## 4.1 Your role

You are the curator and policy owner. You should decide:

- which sources are worth ingesting;
- which topics matter strategically;
- when a source is authoritative;
- what outputs you need;
- whether a synthesis is useful or misleading;
- when political/legal nuance requires caution;
- when a claim needs primary-source verification.

You do not need to manually maintain every link and page. That is the agent's job.

## 4.2 The agent's role

The agent should:

- orient itself by reading `SCHEMA.md`, `index.md`, and recent `log.md`;
- save raw source material;
- identify entities, concepts, programmes, indicators, and claims;
- search for existing pages before creating new ones;
- update pages and cross-links;
- add frontmatter and tags;
- update `index.md` and `log.md`;
- flag contradictions, weak claims, missing evidence, and methodological gaps;
- answer questions using the wiki first;
- file reusable answers into `queries/` or `comparisons/`.

## 4.3 A good division of labour

| Human | Agent |
|---|---|
| Selects source and policy purpose | Extracts structure and claims |
| Judges relevance and sensitivity | Drafts/update pages |
| Decides final interpretation | Links pages and maintains index |
| Reviews methodology choices | Flags uncertainty and contradictions |
| Uses outputs in professional work | Produces source-backed drafts and tables |

The agent can generate useful synthesis, but it should not be the final authority on legal, political, or methodological claims.

---

# 5. The knowledge lifecycle

Every source should move through a structured lifecycle:

```text
1. Capture
2. Classify
3. Extract
4. Compare with existing wiki
5. Update/create pages
6. Cross-link
7. Record provenance
8. Update index and log
9. Query and reuse
10. Audit periodically
```

## 5.1 Capture

Save the source in the correct raw folder.

Examples:

| Source | Folder |
|---|---|
| European Commission Moldova Report PDF | `raw/papers/` |
| World Bank economic update webpage | `raw/articles/` |
| Meeting notes with donors | `raw/transcripts/` |
| Screenshot, chart, logo, diagram | `raw/assets/` |
| Dataset description or metadata note | `raw/articles/` or `raw/papers/` |

## 5.2 Classify

Ask:

- Is this a primary source, secondary analysis, dataset, legal text, programme document, or transcript?
- What institutions does it mention?
- What policy areas does it affect?
- Does it contain indicators or methodology?
- Does it support, refine, or contradict existing wiki pages?

## 5.3 Extract

Extract only what is reusable:

- definitions;
- institutional mandates;
- reform priorities;
- indicators;
- funding/programme details;
- legal approximation references;
- constraints and bottlenecks;
- methodological choices;
- source-backed claims;
- direct quotes where wording matters.

Avoid clutter. Not every paragraph deserves a wiki entry.

## 5.4 Compare

Before creating pages, search existing pages. The wiki should become denser, not just larger.

Good instruction:

```text
Before creating new pages, search the existing wiki for related entities and concepts. Prefer updating existing pages unless a new page is clearly justified.
```

## 5.5 Update or create

Create a page when the subject is central to the source or appears across multiple sources.

Update a page when the source adds evidence to an existing topic.

Do not create pages for passing mentions.

## 5.6 Cross-link

Every useful page should connect to other pages.

Example links from `concepts/sme-competitiveness.md`:

```markdown
Related: [[eu-accession]], [[investment-climate]], [[regulatory-reform]], [[digital-transformation]], [[oecd]], [[world-bank]]
```

## 5.7 Record provenance

Every page must say where evidence came from.

Use `sources:` in frontmatter, and when pages synthesize multiple sources, use inline provenance markers.

Example:

```markdown
Moldova's SME competitiveness constraints are recurrently linked to access to finance, regulatory burden, skills gaps, and limited export capacity.^[raw/papers/oecd-sme-policy-index-2026.md]
```

## 5.8 Update index and log

After every meaningful operation:

- add new pages to `index.md`;
- update page count;
- append an entry to `log.md`;
- list created/updated files.

---

# 6. What to ingest first

Your wiki is currently empty except for its schema and this guidebook. The first sources matter because they establish anchor pages.

## 6.1 Recommended first 10 sources

| Priority | Source type | Why it matters |
|---|---|---|
| 1 | European Commission Moldova Report | EU accession baseline and reform priorities |
| 2 | Moldova Economic Reform Programme | Government reform commitments and macroeconomic policy |
| 3 | National Development Strategy “European Moldova 2030” | National strategic framework |
| 4 | National Bureau of Statistics metadata/source notes | Statistical backbone for dashboards |
| 5 | World Bank Moldova economic update | External economic analysis |
| 6 | OECD SME Policy Index / SME competitiveness material | SME and competitiveness framework |
| 7 | EU enlargement package / accession methodology materials | EU process and conditionality context |
| 8 | A donor strategy or programme document | Development architecture and implementation actors |
| 9 | Your composite economic indicator methodology notes | Dashboard methodological backbone |
| 10 | Any existing Moldova dashboard data dictionary | Data governance and indicator design |

## 6.2 First anchor pages to build

After the first sources, the wiki should probably contain pages such as:

```text
concepts/eu-accession.md
concepts/economic-policy.md
concepts/sme-competitiveness.md
concepts/composite-indicators.md
concepts/dashboard-methodology.md
concepts/indicator-weighting.md
concepts/indicator-normalization.md
concepts/digital-transformation.md
concepts/regulatory-reform.md
concepts/investment-climate.md
concepts/donor-coordination.md
entities/european-commission.md
entities/eu-delegation-to-moldova.md
entities/government-of-moldova.md
entities/national-bureau-of-statistics.md
entities/world-bank.md
entities/oecd.md
comparisons/composite-indicator-weighting-options.md
queries/what-indicators-best-capture-moldova-economic-resilience.md
```

Do not create all of these artificially. Let sources justify them. But these are likely anchor pages for your domain.

---

# 7. Source-ingestion playbooks

## 7.1 Ingesting a European Commission country report

Use this when adding an annual Moldova Report or enlargement-related document.

### Prompt

```text
Ingest this European Commission Moldova report into the wiki. Preserve the raw source, identify EU accession themes, institutions, legal approximation issues, economic governance points, public administration issues, procurement issues, SME/competitiveness implications, and indicators. Update existing pages before creating new ones. Create comparison or query pages only for reusable synthesis. Update index.md and log.md.
```

### Expected pages

Potential updates:

```text
concepts/eu-accession.md
concepts/legal-approximation.md
concepts/public-administration-reform.md
concepts/economic-governance.md
concepts/procurement.md
concepts/sme-competitiveness.md
entities/european-commission.md
entities/government-of-moldova.md
```

Potential comparison:

```text
comparisons/eu-accession-economic-governance-vs-competitiveness.md
```

### What to extract

- reform priorities;
- progress assessments;
- chapter/cluster relevance;
- implementation gaps;
- references to economic governance;
- public administration capacity issues;
- procurement/public finance issues;
- rule-of-law or anti-corruption constraints where relevant to business environment;
- indicators or metrics mentioned.

### Caution

Do not turn the report into a political summary. Preserve the Commission's language where wording matters. Mark interpretation separately.

---

## 7.2 Ingesting a legal act or acquis-approximation document

### Prompt

```text
Ingest this legal/acquis document into the wiki. Preserve exact legal terminology, identify the legal act, institutions responsible, policy area, EU acquis/chapter relevance if known, implementation obligations, deadlines, and open verification questions. Avoid over-interpreting legal meaning. Update index.md and log.md.
```

### Expected page type

Legal acts are usually `entities/`, because they are named objects.

Example:

```text
entities/law-on-state-aid.md
entities/government-decision-on-digital-transformation-strategy.md
```

Related concepts:

```text
concepts/legal-approximation.md
concepts/regulatory-reform.md
concepts/public-administration.md
```

### Legal-page template

```markdown
---
title: Law / Decision / Regulation Name
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity
tags: [moldova, eu, legal-approximation, regulatory-reform, entity]
sources: [raw/papers/source.md]
confidence: medium
---

# Overview

# Legal basis and status

# Responsible institutions

# EU/acquis relevance

# Key provisions

# Implementation requirements

# Related pages

# Open questions
```

### Caution

For legal texts, use low or medium confidence unless the legal source is primary and the interpretation is direct.

---

## 7.3 Ingesting a donor programme document

### Prompt

```text
Ingest this donor programme document into the wiki. Extract objectives, budget, period, implementing partners, beneficiaries, governance arrangements, indicators, reform area, geographic coverage, and links to Moldova EU accession or national strategies. Update donor/programme pages and create a donor comparison page if useful.
```

### Expected pages

```text
entities/eu-delegation-to-moldova.md
entities/undp-moldova.md
entities/world-bank.md
entities/programme-name.md
concepts/donor-coordination.md
concepts/programme-design.md
concepts/monitoring.md
comparisons/donor-programmes-digital-transformation.md
```

### Programme extraction table

| Field | What to capture |
|---|---|
| Programme name | Exact title |
| Donor/funder | EU, World Bank, UNDP, etc. |
| Implementing partner | Institution/agency/contractor |
| Period | Start/end date |
| Budget | Amount and currency |
| Objectives | Official objectives |
| Beneficiaries | Institutions, firms, citizens, municipalities |
| Indicators | Output/outcome indicators |
| Governance | Steering committee, reporting, coordination |
| Links | Strategies, EU accession, reforms |
| Risks | Implementation gaps, data issues, overlap |

---

## 7.4 Ingesting an economic update or analytical report

### Prompt

```text
Ingest this economic analytical report into the wiki. Extract macroeconomic assumptions, sectoral trends, competitiveness findings, risks, indicators, data sources, policy recommendations, and implications for Moldova's reform agenda. Separate facts, interpretation, and recommendations. Flag weak or single-source claims.
```

### Likely pages

```text
concepts/macroeconomics.md
concepts/economic-policy.md
concepts/investment-climate.md
concepts/trade.md
concepts/labour-market.md
concepts/public-finance.md
entities/world-bank.md
entities/imf.md
```

### Caution

Economic reports often include forecasts. Capture forecast date and assumptions. Do not treat old forecasts as current facts.

---

## 7.5 Ingesting a dataset or statistical source

### Prompt

```text
Ingest this dataset/data-source note into the wiki. Create or update a data-source entity page. Capture publisher, update frequency, coverage, variables, methodology, limitations, access URL/path, and relevance for dashboards or composite indicators. Link it to relevant indicator and methodology pages.
```

### Data-source template

```markdown
---
title: Data Source Name
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity
tags: [data-source, statistics, dashboard, indicator, moldova, entity]
sources: [raw/articles/source.md]
confidence: medium
---

# Overview

# Publisher and access

# Coverage

# Variables

# Update frequency

# Methodology

# Known limitations

# Relevance for dashboards

# Related indicators

# Open verification questions
```

### What matters most

For dashboard work, capture:

- frequency;
- breaks in series;
- geographic coverage;
- missing values;
- revisions;
- comparability;
- units;
- whether higher values are good or bad;
- whether normalization is required.

---

## 7.6 Ingesting meeting notes or transcripts

### Prompt

```text
Ingest these meeting notes into the wiki as a transcript/note source. Extract decisions, claims, institutional positions, action items, open questions, and topics requiring source verification. Do not treat informal statements as high-confidence facts. Link to relevant institution, programme, and concept pages.
```

### Caution

Meeting notes are useful, but they are not the same as official documents. Use:

```yaml
confidence: low
```

unless the content is corroborated.

---

# 8. Page types and when to use them

## 8.1 Entity pages

Use entity pages for named objects:

- institutions;
- ministries;
- EU bodies;
- donors;
- programmes;
- legal acts;
- datasets;
- official strategies;
- reports;
- dashboards.

### Example entity page: `entities/national-bureau-of-statistics.md`

```markdown
---
title: National Bureau of Statistics of Moldova
created: 2026-07-08
updated: 2026-07-08
type: entity
tags: [moldova, institution, statistics, data-source, entity]
sources: [raw/articles/nbs-source-note.md]
confidence: medium
---

# Overview

The National Bureau of Statistics is Moldova's central statistical authority and a core source for official economic, social, and demographic data.

# Relevance to the wiki

NBS data may support pages on [[macroeconomics]], [[labour-market]], [[regional-development]], [[dashboard-methodology]], and [[composite-indicators]].

# Data considerations

- Frequency varies by indicator.
- Some series may require seasonal adjustment or revision tracking.
- Regional indicators may have different coverage and reliability.

# Open questions

- Which indicators are available at monthly, quarterly, and annual frequency?
- Which series are suitable for a composite economic indicator?
```

## 8.2 Concept pages

Use concept pages for durable ideas:

- SME competitiveness;
- regulatory reform;
- digital transformation;
- EU accession;
- composite indicators;
- investment climate;
- programme design;
- monitoring and evaluation.

### Example concept page: `concepts/composite-indicators.md`

```markdown
---
title: Composite Indicators
created: 2026-07-08
updated: 2026-07-08
type: concept
tags: [composite-index, indicator, methodology, dashboard, concept]
sources: []
confidence: low
---

# Definition

A composite indicator combines multiple individual indicators into a single index or score to summarize a complex phenomenon.

# Relevance for Moldova

Composite indicators may help communicate economic resilience, competitiveness, reform progress, regional development, or institutional capacity, but they require transparent methodological choices.

# Methodological decisions

- Component selection
- Data quality screening
- Directionality
- Normalization
- Weighting
- Aggregation
- Missing-data handling
- Sensitivity analysis
- Interpretation limits

# Related pages

[[indicator-normalization]], [[indicator-weighting]], [[dashboard-methodology]], [[data-source-quality]]
```

## 8.3 Comparison pages

Use comparison pages when analytical judgement matters.

Examples:

```text
comparisons/composite-indicator-weighting-options.md
comparisons/donor-programmes-digital-transformation.md
comparisons/moldova-vs-georgia-economic-governance.md
comparisons/eu-accession-reform-clusters.md
```

### Example comparison table

| Weighting method | Strength | Risk | Best use |
|---|---|---|---|
| Equal weighting | Transparent and easy to explain | May imply equal policy importance | Public-facing dashboards |
| Expert weighting | Reflects policy judgment | Can be subjective | Strategic reform dashboards |
| PCA/statistical weighting | Data-driven | Hard to explain to nontechnical audiences | Exploratory analysis |
| Outcome-linked weighting | Tied to policy relevance | Requires strong causal theory | Programme monitoring |

## 8.4 Query pages

Use query pages when an answer is valuable enough to preserve.

Examples:

```text
queries/what-indicators-best-capture-moldova-economic-resilience.md
queries/how-should-sme-dashboard-components-be-weighted.md
queries/which-reforms-link-economic-governance-to-eu-accession.md
```

Query pages are especially useful for:

- report outlines;
- briefing notes;
- strategic memos;
- methodology decisions;
- donor mapping;
- evidence gap analysis.

---

# 9. Templates for reusable pages

## 9.1 Concept page template

```markdown
---
title: Concept Name
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: concept
tags: [moldova, concept]
sources: []
confidence: low
---

# Definition

# Relevance to Moldova

# Relevance to EU accession

# Evidence summary

# Measurement / methodology

# Policy implications

# Risks and debates

# Related pages

# Open questions
```

## 9.2 Entity page template

```markdown
---
title: Entity Name
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity
tags: [moldova, entity]
sources: []
confidence: low
---

# Overview

# Mandate / role

# Key facts and dates

# Relevance to policy work

# Relationships to other pages

# Evidence and sources

# Open questions
```

## 9.3 Programme page template

```markdown
---
title: Programme Name
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity
tags: [donor, programme-design, monitoring, entity]
sources: []
confidence: low
---

# Overview

# Donor / funder

# Implementing partners

# Time period and budget

# Objectives

# Beneficiaries

# Activities

# Indicators and monitoring

# Governance arrangements

# Links to national strategies / EU accession

# Risks and open questions
```

## 9.4 Indicator page template

```markdown
---
title: Indicator Name
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: concept
tags: [indicator, data-source, methodology, dashboard, concept]
sources: []
confidence: low
---

# Definition

# Policy relevance

# Data source

# Unit and frequency

# Directionality

Higher is better / lower is better / context-specific.

# Transformations

# Missing-data treatment

# Limitations

# Use in composite indicators

# Related pages
```

## 9.5 Query page template

```markdown
---
title: Research Question
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: query
tags: [query, moldova]
sources: []
confidence: medium
---

# Question

# Short answer

# Evidence consulted

# Synthesis

# Implications

# Confidence and limitations

# Follow-up questions
```

---

# 10. Moldova-specific examples

## 10.1 Example: SME competitiveness page

Suggested file:

```text
concepts/sme-competitiveness.md
```

Possible structure:

```markdown
# Definition

SME competitiveness refers to the ability of small and medium-sized enterprises to survive, grow, innovate, access markets, finance investment, comply with regulation, and compete domestically and internationally.

# Moldova relevance

For Moldova, SME competitiveness is linked to private-sector development, export diversification, employment, regional development, productivity growth, and EU market integration.

# Recurring constraints

- Access to finance
- Regulatory burden
- Skills gaps
- Limited innovation capacity
- Digitalization gaps
- Export-readiness constraints
- Infrastructure and logistics barriers
- Public procurement access

# EU accession relevance

SME competitiveness is relevant to economic governance, internal market alignment, industrial policy, enterprise policy, digital transformation, procurement, and state-aid frameworks.

# Related pages

[[eu-accession]], [[investment-climate]], [[regulatory-reform]], [[digital-transformation]], [[public-procurement]], [[composite-indicators]]
```

## 10.2 Example: EU accession page

Suggested file:

```text
concepts/eu-accession.md
```

Possible sections:

- Overview of Moldova's accession process
- Enlargement methodology
- Clusters and chapters
- Economic governance relevance
- Institutional capacity
- Legal approximation
- Implementation and enforcement
- Monitoring sources
- Links to policy domains
- Open questions

Good links:

```markdown
[[legal-approximation]], [[public-administration-reform]], [[economic-governance]], [[procurement]], [[anti-corruption]], [[sme-competitiveness]]
```

## 10.3 Example: composite economic indicator methodology page

Suggested file:

```text
concepts/moldova-composite-economic-indicator-methodology.md
```

Possible structure:

```markdown
# Purpose

The Moldova composite economic indicator is intended to summarize multiple dimensions of economic performance, resilience, competitiveness, or reform progress in a transparent dashboard format.

# Candidate dimensions

| Dimension | Possible indicators | Notes |
|---|---|---|
| Macroeconomic stability | Inflation, fiscal balance, exchange rate, reserves | Requires careful interpretation |
| Labour market | Employment, unemployment, wages, vacancies | Frequency and comparability matter |
| Business environment | firm creation, insolvency, permits, regulatory burden | Data may be fragmented |
| Trade and investment | exports, FDI, trade balance | Volatile and externally influenced |
| Digital transformation | broadband, e-services, digital skills | Often mixed administrative/statistical data |
| Regional development | regional income, infrastructure, employment | Missing data likely |

# Methodological choices

- Normalization method
- Weighting system
- Aggregation formula
- Missing-data treatment
- Sensitivity analysis
- Update frequency
- Presentation rules
- Interpretation warnings

# Risks

- False precision
- Overweighting available data
- Mixing input, output, and outcome indicators
- Ignoring lag effects
- Political misuse of rankings
```

## 10.4 Example: donor coordination page

Suggested file:

```text
concepts/donor-coordination.md
```

Possible sections:

- What donor coordination means
- Why it matters in Moldova
- Main donors and instruments
- Coordination mechanisms
- Links to national strategies
- Links to EU accession
- Risks of fragmentation
- Programme overlap matrix
- Open questions

---

# 11. Using the wiki for composite indicators and dashboards

This is one of the highest-value applications for your wiki.

## 11.1 Why the wiki helps

Composite indicators are often criticized because their methodology is opaque. The wiki can solve this by documenting every design choice:

- why each component was selected;
- what data source supports it;
- what limitations exist;
- how directionality is defined;
- how normalization works;
- how weights are assigned;
- what happens when data is missing;
- how sensitive results are to alternative assumptions.

A good dashboard is not only a visual product. It is a documented evidence system.

## 11.2 Recommended wiki pages for dashboard work

```text
concepts/dashboard-methodology.md
concepts/composite-indicators.md
concepts/indicator-selection.md
concepts/indicator-normalization.md
concepts/indicator-weighting.md
concepts/missing-data-treatment.md
concepts/data-source-quality.md
concepts/sensitivity-analysis.md
entities/national-bureau-of-statistics.md
entities/world-bank-data.md
entities/eurostat.md
comparisons/composite-indicator-weighting-options.md
comparisons/normalization-methods.md
queries/which-indicators-best-capture-moldova-economic-resilience.md
```

## 11.3 Indicator documentation checklist

For each candidate indicator, capture:

| Field | Example |
|---|---|
| Name | Business density |
| Definition | Number of active enterprises per 1,000 population |
| Source | National Bureau of Statistics |
| Frequency | Annual |
| Geography | National / district / region |
| Unit | Enterprises per 1,000 population |
| Direction | Higher is generally better |
| Transformation | Per capita, normalized min-max |
| Missing data | Carry-forward not recommended unless justified |
| Limitation | Does not measure firm quality or productivity |
| Policy link | SME development, regional development |
| Dashboard role | Component in entrepreneurship dimension |

## 11.4 Component-selection strategy

Use the wiki to separate three things:

1. **Policy logic** — why the indicator matters.
2. **Data logic** — whether the indicator is available and reliable.
3. **Communication logic** — whether the indicator can be explained to decision-makers.

A technically sophisticated indicator is not always the best public dashboard indicator. A transparent indicator may be better if it supports trust.

## 11.5 Weighting strategy

Create a comparison page for weighting options.

Recommended table:

| Weighting approach | Advantages | Risks | Use case |
|---|---|---|---|
| Equal weights | Transparent, easy to defend | Implies all components equally important | Public dashboard baseline |
| Expert weights | Reflects policy priorities | Subjective, may be contested | Strategy-linked dashboard |
| Data-driven weights | Uses statistical structure | Hard to explain, unstable over time | Exploratory analysis |
| Hybrid weights | Balances transparency and policy relevance | Needs clear documentation | Most practical option |

For Moldova policy communication, a hybrid approach is often attractive:

- equal weights within dimensions;
- policy-reviewed weights across dimensions;
- sensitivity testing to show how rankings/scores change.

## 11.6 Prompt for dashboard methodology

```text
Using the wiki, draft a methodology note for the Moldova composite economic indicator. Include purpose, dimensions, component indicators, data sources, normalization, weighting, aggregation, missing-data treatment, sensitivity analysis, limitations, and interpretation rules. Use only wiki-backed claims and flag evidence gaps.
```

## 11.7 Prompt for indicator audit

```text
Audit all indicator-related pages in the wiki. Identify indicators with missing source metadata, unclear frequency, unclear directionality, weak policy rationale, missing-data risks, or unresolved methodology issues. Produce a table of fixes.
```

---

# 12. Using the wiki for EU accession and legal approximation

## 12.1 Why the wiki is useful for EU accession

EU accession work generates large amounts of recurring knowledge:

- chapters and clusters;
- screening findings;
- Commission assessments;
- reform commitments;
- legal approximation plans;
- implementation gaps;
- institutional responsibilities;
- donor support;
- monitoring indicators.

A wiki can keep this organized and reusable.

## 12.2 Recommended EU accession pages

```text
concepts/eu-accession.md
concepts/legal-approximation.md
concepts/economic-governance.md
concepts/public-administration-reform.md
concepts/procurement.md
concepts/state-aid.md
concepts/anti-corruption.md
concepts/institutional-capacity.md
comparisons/eu-accession-reform-clusters.md
comparisons/commission-assessments-by-year.md
entities/european-commission.md
entities/eu-delegation-to-moldova.md
entities/government-of-moldova.md
```

## 12.3 Legal approximation page structure

A strong legal approximation page should capture:

- EU act or acquis area;
- Moldovan corresponding law or draft law;
- responsible institution;
- status of transposition;
- implementation/enforcement requirements;
- capacity constraints;
- deadlines;
- donor support;
- Commission comments;
- open questions.

## 12.4 Prompt for EU accession synthesis

```text
Using the wiki, synthesize the main EU accession-related economic governance priorities for Moldova. Separate Commission assessments, government commitments, donor support, implementation gaps, and policy implications. Cite the wiki pages used and flag weak evidence.
```

## 12.5 Prompt for legal approximation mapping

```text
Create a comparison table from the wiki mapping Moldova legal approximation items to EU acquis areas, responsible institutions, current status, implementation risks, and source confidence. Do not infer legal status unless supported by a source.
```

---

# 13. Using the wiki for donor and programme architecture

## 13.1 Why this matters

Donor/programme architecture is complex because projects overlap across themes:

- digital transformation;
- SME support;
- public administration;
- regional development;
- procurement;
- anti-corruption;
- infrastructure;
- EU accession support;
- private-sector development.

The wiki can help you build a donor map that is source-backed and updated over time.

## 13.2 Recommended donor pages

```text
entities/eu-delegation-to-moldova.md
entities/world-bank.md
entities/undp-moldova.md
entities/oecd.md
entities/ebrd.md
entities/giz.md
entities/usaid.md
concepts/donor-coordination.md
concepts/programme-design.md
concepts/monitoring.md
comparisons/donor-programmes-sme-competitiveness.md
comparisons/donor-programmes-digital-transformation.md
comparisons/donor-programmes-regional-development.md
```

## 13.3 Donor map table

| Donor | Programme | Area | Period | Budget | Implementer | Beneficiaries | EU accession link | Indicators | Source confidence |
|---|---|---|---|---|---|---|---|---|---|
| EU | Example programme | SME competitiveness | 2024–2027 | EUR X | Implementer | SMEs, MDED | Economic criteria | Output/outcome indicators | Medium |

## 13.4 Prompt for donor mapping

```text
Using the wiki, create a donor/programme mapping table for Moldova economic reform, SME competitiveness, digital transformation, and EU accession support. Include donor, programme, period, budget if available, implementer, beneficiaries, policy area, indicators, and source confidence. Flag overlaps and gaps.
```

---

# 14. Querying the wiki effectively

## 14.1 Query types

Use the wiki for five main query types:

| Query type | Example |
|---|---|
| Evidence query | What sources support this claim? |
| Synthesis query | What are the main constraints to SME competitiveness? |
| Comparison query | How do weighting methods differ? |
| Gap query | What evidence is missing before publishing a dashboard? |
| Output query | Draft a report outline using wiki-backed evidence. |

## 14.2 Ask for pages consulted

A strong wiki answer should say which pages it used.

Prompt:

```text
Answer using the wiki first. Cite the wiki pages used, identify source confidence, and tell me what evidence is missing.
```

## 14.3 Ask for uncertainty

Prompt:

```text
Give me the strongest source-backed answer, but separate high-confidence facts, medium-confidence interpretation, and low-confidence assumptions.
```

## 14.4 Ask for reusable output

Prompt:

```text
If this answer is substantial, save it as a query page and update index.md and log.md.
```

---

# 15. Prompt cookbook

This section gives you ready-to-use prompts.

## 15.1 General ingest

```text
Ingest this into the wiki. Save the raw source, identify entities/concepts/programmes/indicators, update existing pages before creating new ones, use only schema-approved tags, cross-link pages, update index.md and log.md, and flag uncertainty or contradictions.
```

## 15.2 Focused Moldova policy ingest

```text
Ingest this into the wiki with special attention to Moldova economic policy, EU accession, SME competitiveness, digital transformation, regulatory reform, donor coordination, and dashboard indicators. Preserve source meaning and separate facts, interpretation, and recommendations.
```

## 15.3 Composite indicator ingest

```text
Ingest this source for the Moldova composite economic indicator. Extract candidate indicators, data sources, methodology notes, limitations, update frequency, directionality, missing-data issues, and dashboard relevance. Update indicator and methodology pages.
```

## 15.4 EU accession ingest

```text
Ingest this EU accession source. Extract reform priorities, Commission assessments, legal approximation issues, economic governance points, institutions responsible, implementation gaps, donor support, and chapter/cluster relevance if stated.
```

## 15.5 Donor programme ingest

```text
Ingest this donor programme document. Extract donor, programme title, objectives, budget, period, implementers, beneficiaries, governance, indicators, policy area, EU accession link, and implementation risks. Update donor and programme pages.
```

## 15.6 Query from wiki

```text
Answer this using the wiki first. Read index.md, relevant pages, and recent log.md. Cite the wiki pages used. Separate facts, interpretation, and assumptions. Flag weak evidence.
```

## 15.7 Create a comparison page

```text
Create a comparison page on [topic]. Use a table, cite sources, include implications for Moldova, explain confidence levels, update index.md and log.md.
```

## 15.8 Prepare a policy brief

```text
Using only wiki-backed evidence, prepare a policy brief outline on [topic]. Include problem statement, evidence, policy options, recommended approach, risks, implementation considerations, and source gaps.
```

## 15.9 Prepare a report structure

```text
Read the relevant wiki pages and propose a modern policy report structure for [topic]. Identify which claims are well-supported, which require verification, and which figures/tables could be generated.
```

## 15.10 Audit the wiki

```text
Lint the wiki for broken links, orphan pages, missing frontmatter, missing index entries, tags not in SCHEMA.md, low-confidence pages, stale pages, source drift, oversized pages, and contradictions. Provide a prioritized fix list.
```

## 15.11 Strengthen evidence

```text
Find weak or single-source claims in the wiki on [topic]. Suggest what primary sources, datasets, or official documents are needed to strengthen them.
```

## 15.12 Build a briefing pack

```text
Create a 2-page briefing pack from the wiki on [topic]. Use source-backed claims only, include key findings, evidence confidence, policy implications, and open questions.
```

---

# 16. Obsidian and browsing tactics

You can open the wiki folder in Obsidian:

```text
C:\Users\harab\wiki
```

## 16.1 Why Obsidian helps

Obsidian makes the wiki easier to browse because:

- `[[wikilinks]]` become clickable;
- backlinks show what refers to a topic;
- graph view shows relationships;
- tags can be browsed;
- Markdown remains plain and portable.

## 16.2 How to browse effectively

Start from:

```text
index.md
```

Then open anchor pages, such as:

```text
concepts/eu-accession.md
concepts/composite-indicators.md
concepts/sme-competitiveness.md
```

Use backlinks to discover related pages.

## 16.3 Suggested Obsidian habits

- Keep `index.md` pinned.
- Use graph view occasionally to spot orphan pages.
- Use search for recurring terms like “SME”, “acquis”, “indicator”, “weighting”, “procurement”.
- Do not manually edit raw sources except to correct ingestion errors.
- If you manually edit synthesis pages, keep frontmatter and links intact.

---

# 17. Quality assurance and linting

## 17.1 Why QA matters

A wiki can decay if it accumulates:

- duplicate pages;
- broken links;
- weak claims;
- missing sources;
- outdated pages;
- inconsistent tags;
- unstated methodology;
- hidden contradictions.

Quality assurance keeps the wiki trustworthy.

## 17.2 Lint checklist

Ask the agent to check:

| Check | Why it matters |
|---|---|
| Broken wikilinks | Prevents navigation failure |
| Orphan pages | Finds isolated knowledge |
| Missing index entries | Keeps the map complete |
| Missing frontmatter | Keeps metadata searchable |
| Invalid tags | Prevents tag sprawl |
| Low-confidence pages | Highlights weak evidence |
| Stale pages | Prevents outdated synthesis |
| Source drift | Detects changed raw sources |
| Oversized pages | Signals need to split |
| Contradictions | Preserves analytical honesty |

## 17.3 Confidence rules

Use this standard:

| Confidence | Meaning | Example |
|---|---|---|
| High | Strongly supported by primary or multiple credible sources | Official legal text, official statistics, repeated findings |
| Medium | Credible but limited or interpretive | One strong analytical report |
| Low | Uncertain, single-source, informal, politically sensitive, or inferred | Meeting note claim, unverified dataset assumption |

## 17.4 Contradiction handling

Do not hide contradictions. Record them.

Example:

```yaml
contested: true
contradictions: [investment-climate]
```

Then explain:

```markdown
# Contradiction

Source A presents regulatory reform progress as significant, while Source B emphasizes persistent implementation burdens for SMEs. The difference may reflect scope, date, or measurement method.
```

Contradictions often become valuable policy insights.

---

# 18. Governance routines

## 18.1 Daily or per-source routine

When you add a source:

1. Ingest raw source.
2. Update relevant pages.
3. Avoid duplicate pages.
4. Cross-link.
5. Update `index.md`.
6. Update `log.md`.
7. Flag gaps.

## 18.2 Weekly routine during active research

Ask:

```text
Review recent log.md entries and summarize what changed this week, unresolved questions, and recommended next sources to ingest.
```

## 18.3 Monthly routine

Ask:

```text
Run a full wiki lint and propose a maintenance plan grouped by high, medium, and low priority.
```

## 18.4 Before writing a major report

Ask:

```text
Before drafting, read the relevant wiki pages for [topic], identify the strongest source-backed claims, weak evidence, contradictions, and suggested figures/tables.
```

## 18.5 After finishing a major report

Ingest the final report back into the wiki. It becomes a source and synthesis artifact for future work.

Prompt:

```text
Ingest this final report back into the wiki. Treat it as a source produced from prior analysis. Update relevant concept/query/comparison pages, but preserve distinctions between original external evidence and this report's synthesis.
```

---

# 19. A 30-day implementation plan

## Week 1: establish the backbone

Goal: create anchor pages from 3–5 core sources.

Actions:

1. Ingest European Commission Moldova Report.
2. Ingest Moldova Economic Reform Programme.
3. Ingest National Development Strategy “European Moldova 2030”.
4. Ingest one World Bank or OECD Moldova economic source.
5. Create/update anchor pages for EU accession, economic policy, SME competitiveness, composite indicators, and dashboard methodology.

Deliverable:

```text
index.md has at least 10–20 meaningful pages.
```

## Week 2: build methodology depth

Goal: make the dashboard/composite indicator knowledge base robust.

Actions:

1. Ingest your composite indicator notes.
2. Create indicator templates.
3. Create pages for normalization, weighting, missing data, and sensitivity analysis.
4. Create comparison page on weighting methods.
5. Audit candidate indicators.

Deliverable:

```text
A source-backed dashboard methodology skeleton.
```

## Week 3: build EU accession and donor map

Goal: link reform priorities to programmes and institutions.

Actions:

1. Ingest EU accession or enlargement materials.
2. Ingest 2–3 donor programme documents.
3. Create donor/programme pages.
4. Create a comparison table of donor support by policy area.
5. Link donor support to EU accession themes.

Deliverable:

```text
A donor and reform architecture map.
```

## Week 4: produce outputs and audit

Goal: make the wiki useful for real products.

Actions:

1. Ask the wiki to prepare a policy brief outline.
2. Ask the wiki to draft a dashboard methodology note.
3. Ask the wiki to identify evidence gaps.
4. Run full lint.
5. Fix broken links, weak tags, and missing frontmatter.

Deliverable:

```text
A maintained wiki capable of supporting reports, briefs, dashboards, and presentations.
```

---

# 20. Common failure modes and how to avoid them

## 20.1 Failure: dumping summaries into the wiki

Bad pattern:

```text
Every source becomes a long summary page.
```

Better pattern:

```text
Every source updates the relevant concept/entity pages and only creates new pages when justified.
```

## 20.2 Failure: creating too many small pages

Bad:

```text
A page for every minor project, person, or passing mention.
```

Better:

```text
Broader pages with sections until a topic becomes central or recurring.
```

## 20.3 Failure: weak provenance

Bad:

```text
Moldova has weak implementation capacity.
```

Better:

```text
The source identifies implementation capacity as a constraint in the context of public administration and reform delivery.^[raw/papers/source.md]
```

## 20.4 Failure: hidden methodology

Bad:

```text
The dashboard shows a competitiveness score.
```

Better:

```text
The dashboard score aggregates normalized indicators across four dimensions using equal within-dimension weights and policy-reviewed dimension weights. Missing values are excluded if less than X% of the dimension is missing; otherwise the dimension is flagged incomplete.
```

## 20.5 Failure: treating old sources as current

Always capture dates. Policy and economic claims age quickly.

---

# 21. Practical examples of complete workflows

## 21.1 Workflow: building a policy brief on SME competitiveness

### Step 1: query the wiki

```text
Using the wiki, identify the strongest source-backed claims about SME competitiveness constraints in Moldova. Separate high-confidence facts, medium-confidence interpretations, and evidence gaps.
```

### Step 2: create evidence table

```text
Create a table with constraint, supporting sources, policy implication, confidence, and open questions.
```

### Step 3: outline brief

```text
Using that evidence table, draft a policy brief outline with problem statement, evidence, policy options, recommended approach, implementation risks, and indicators.
```

### Step 4: preserve synthesis

```text
Save the evidence table and outline as a query page because I may reuse it later.
```

## 21.2 Workflow: creating a composite economic indicator methodology

### Step 1: audit candidate indicators

```text
Audit all candidate indicators in the wiki for data source, frequency, directionality, missing data, policy relevance, and limitations.
```

### Step 2: compare methodology options

```text
Create a comparison page for normalization and weighting options. Include advantages, risks, and recommended use for a Moldova public-facing dashboard.
```

### Step 3: draft methodology note

```text
Draft a methodology note for the Moldova composite economic indicator using only wiki-backed evidence. Include purpose, dimensions, normalization, weighting, aggregation, missing-data treatment, sensitivity analysis, limitations, and interpretation guidance.
```

### Step 4: flag missing data

```text
List all methodology assumptions that still need data or expert validation.
```

## 21.3 Workflow: preparing for EU Delegation / programme officer style work

### Step 1: create reform map

```text
Using the wiki, map economic reform priorities to EU accession themes, responsible institutions, donor programmes, indicators, and implementation risks.
```

### Step 2: create programme architecture table

```text
Create a programme architecture table with objective, activities, outputs, outcomes, beneficiaries, implementing partners, indicators, risks, and evidence sources.
```

### Step 3: generate interview/writing examples

```text
Using wiki-backed examples, prepare concise STAR-style examples showing experience with EU accession, programme management, economic reform, and donor coordination. Keep claims factual and source-supported where applicable.
```

---

# 22. Appendix A: master ingest checklist

Before finishing any ingest, check:

- [ ] Raw source saved in the correct folder.
- [ ] Raw frontmatter added.
- [ ] Existing pages searched before new pages created.
- [ ] New pages meet page-creation threshold.
- [ ] Frontmatter complete.
- [ ] Tags come from `SCHEMA.md`.
- [ ] Sources listed.
- [ ] Confidence level assigned where needed.
- [ ] At least two wikilinks added where practical.
- [ ] Index updated.
- [ ] Log updated.
- [ ] Contradictions flagged.
- [ ] Open questions recorded.

---

# 23. Appendix B: master query checklist

Before trusting an answer from the wiki, check:

- [ ] Which pages were read?
- [ ] Which sources support the answer?
- [ ] Are facts separated from interpretation?
- [ ] Is confidence stated?
- [ ] Are there contradictions?
- [ ] Are dates current enough?
- [ ] Is there a missing primary source?
- [ ] Should this answer be saved as a query page?

---

# 24. Appendix C: minimal commands and paths

Wiki root:

```text
C:\Users\harab\wiki
```

Important files:

```text
C:\Users\harab\wiki\SCHEMA.md
C:\Users\harab\wiki\index.md
C:\Users\harab\wiki\log.md
```

Main folders:

```text
C:\Users\harab\wiki\raw
C:\Users\harab\wiki\entities
C:\Users\harab\wiki\concepts
C:\Users\harab\wiki\comparisons
C:\Users\harab\wiki\queries
C:\Users\harab\wiki\_meta
```

Recommended first instruction in future sessions:

```text
Orient yourself in my wiki, then help me with [task].
```

---

# 25. Final principles

1. **Preserve evidence.** Raw sources should remain traceable.
2. **Prefer updating over duplicating.** Mature pages are more useful than many shallow pages.
3. **Make methodology explicit.** Especially for indicators and dashboards.
4. **Separate fact, interpretation, and recommendation.** This is essential for policy work.
5. **Use confidence levels.** Prevent weak claims from becoming hard assumptions.
6. **Capture contradictions.** They are often analytically valuable.
7. **Ask better questions.** Use the wiki for synthesis, comparison, gaps, and outputs.
8. **Maintain the index and log.** They are the nervous system of the wiki.
9. **Audit regularly.** A wiki decays without maintenance.
10. **Use the wiki before writing.** Briefs, reports, dashboards, and presentations should draw from the maintained knowledge base.

The ultimate goal is that, after months of use, you can ask:

```text
What do we know, from source-backed evidence, about Moldova's economic reform priorities and how they connect to EU accession, donor support, and dashboard indicators?
```

and the wiki will answer from a structured, traceable, carefully maintained body of knowledge rather than from scattered files or memory.
