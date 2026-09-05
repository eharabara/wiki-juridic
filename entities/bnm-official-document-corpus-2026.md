---
title: BNM official document corpus — July 2026
created: 2026-07-12
updated: 2026-07-12
type: entity
tags: [moldova, bnm, legal-source, statistics, monitoring, source-note, entity]
sources: [raw/papers/bnm/_manifest.md, raw/papers/bnm/legal/_manifest.md, raw/papers/bnm/reports/_manifest.md, raw/papers/bnm/BNM_LEGISLATION_INVENTORY.md, raw/papers/bnm/BNM_REPORTS_INVENTORY.md]
confidence: high
---

# Overview

This is the local, source-preserved BNM corpus created from the official BNM legal and formal-report catalogues on 12 July 2026. It supports research on the BNM’s mandate, subordinate regulation, bank/non-bank/insurance supervision, payments and financial-market infrastructure, and macro-financial reporting.

# Contents and preservation method

| Layer | Location | Content |
|---|---|---|
| Legal originals | `raw/papers/bnm/legal/original/` | 204 files linked from the BNM Laws and Regulations catalogues |
| Legal extracts | `raw/papers/bnm/legal/documents/` | Paired Markdown source extracts for the legal branch |
| Report originals | `raw/papers/bnm/reports/original/` | 101 files linked from BNM Annual, Inflation and Financial Stability report catalogues |
| Report extracts | `raw/papers/bnm/reports/documents/` | Paired Markdown source extracts for the report branch |
| Master manifest | `raw/papers/bnm/_manifest.md` and `_manifest.csv` | All 305 files, classification, root-relative paths and SHA-256 values |
| Branch manifests | `raw/papers/bnm/legal/_manifest.md` and `raw/papers/bnm/reports/_manifest.md` | Clear, branch-specific navigation and machine-readable records |
| Scope registers | `raw/papers/bnm/BNM_LEGISLATION_INVENTORY.md` and `raw/papers/bnm/BNM_REPORTS_INVENTORY.md` | The BNM-site catalogues used to determine the branches |

The batch contains 305 successfully downloaded unique files from 208 BNM catalogue records: 115 legal-register entries and 93 formal-report-series records. The source inventory found 311 attachment references; links pointing to the same file were deduplicated for preservation. PDF and DOC/DOCX variants are intentionally retained where BNM published both. ^[raw/papers/bnm/_manifest.md]

# Legal and report branches

The filesystem now separates the two source families before the file level. **`legal/`** is reserved for attachments obtained from BNM’s Laws and Regulations catalogues; **`reports/`** is reserved for attachments obtained from BNM’s Annual Report, Inflation Report and Financial Stability Report catalogues. This is a classification by the parent official catalogue record, rather than an assertion that every attached file is itself a legal act or a formal report. The parent BNM record remains visible in every raw extract and branch manifest. ^[raw/papers/bnm/legal/_manifest.md] ^[raw/papers/bnm/reports/_manifest.md]

# Catalogue coverage

The formal report-series register includes 25 Annual Reports, 61 Inflation Reports and 7 Financial Stability Reports. The legal register includes 16 laws and 99 BNM regulations, decisions, norms and methodologies, arranged using BNM’s five domain headings. ^[raw/papers/bnm/BNM_LEGISLATION_INVENTORY.md] ^[raw/papers/bnm/BNM_REPORTS_INVENTORY.md]

# Relationship to active knowledge pages

The corpus is the primary-source evidence layer for [[bnm]], particularly for the BNM-facing portions of [[L-1-2018]], [[L-92-2022]], [[L-106-2022]], [[L-122-2008]], [[L-139-2007]] and [[L-234-2016]]. It can also support future refreshes of [[acquis-Insurance]], [[acquis-ConsumerCredit]] and [[acquis-CSDR-EMIR]].

# Integrity and caveats

- Each paired Markdown raw source contains the exact BNM file URL, parent catalogue record, original-file SHA-256, and SHA-256 of the extracted Markdown body.
- Text was successfully extracted for all 305 preserved files after one legacy `.doc` extraction was repaired using a safe ASCII working copy; the original remains unchanged.
- The BNM website had one additional linked DOCX that returned HTTP 404 during download. The related PDF was downloaded; the missing DOCX is recorded in the original desktop `download_errors.csv`, copied into this raw corpus.
- Some BNM content pages expose general or related attachments alongside the named document. The corpus therefore preserves link-level evidence with the parent page recorded, rather than asserting every attachment is the legal instrument named by that page.
- The corpus is not a substitute for checking the Official Monitor, legis.md or BNM’s live register for current legal status and consolidation.

# Reuse priorities

1. Use the manifest to find the parent BNM record and the preserved original.
2. For a current-law question, verify consolidation and amendment status before extracting propositions.
3. For a BNM-mandate or EU-approximation question, update the relevant existing legal/entity page rather than creating a standalone summary for every subordinate act.
4. Keep report evidence dated: annual, inflation and financial-stability reports describe their respective reporting periods and should not be treated as current conditions without a newer source.
