# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete
> When this file exceeds 500 entries, rotate it to `log-YYYY.md` and start a fresh `log.md`.

## [2026-07-08] create | Wiki initialized

- Domain: Moldova economic policy, EU accession, reform, development programming, composite indicators, dashboards, and evidence-backed policy analysis.
- Structure created: `SCHEMA.md`, `index.md`, `log.md`, `raw/`, `entities/`, `concepts/`, `comparisons/`, `queries/`, `_archive/`, `_meta/`.
- Initial page count: 0.

## [2026-07-08] create | WikiLLM guidebook generated

- Created comprehensive guidebook PDF: `_meta/wikillm-guidebook-for-moldova-policy-work.pdf`.
- Created editable Markdown source: `_meta/wikillm-guidebook-for-moldova-policy-work.md`.
- Created HTML version and audit file in `_meta/`.
- Verification: PDF generated as 59 A4 pages; required phrases present; no blank pages detected; cover and interior previews rendered for visual spot-checking.

## [2026-07-09] ingest | CNPF legal/acquis wiki imported

- Source folder: `C:\Users\harab\Desktop\cnpf-wiki-ro`.
- Backup created before import: `C:\Users\harab\wiki-backups\wiki-before-cnpf-import-20260709-141026`.
- Raw legal/acquis sources copied: 24 files → `raw/papers/cnpf/`.
- Active wiki pages converted: 30 files → `entities/`, `concepts/`, `comparisons/`.
- Original CNPF governance/source files preserved under `_meta/imports/cnpf/`.
- Schema extended with CNPF, financial-services, legal/acquis, and transposition tags.
- Legal import rule preserved: article-level anchors and `[de verificat]` markers remain visible; no legal contradiction was resolved silently.
- Post-import audit: 0 missing frontmatter, 0 missing required fields, 0 invalid tags, 0 broken wikilinks, 0 index gaps. Audit saved at `_meta/imports/cnpf/import-audit.json`.

## [2026-07-09] ingest | EUR-Lex RO acquis — nucleul pieței de capital

- Backup created before ingest: `C:\Users\harab\wiki-backups\wiki-before-eurlex-acquis-ingest-20260709-144036`.
- Fetched/refreshed structured Romanian EUR-Lex extracts for 14 instruments: 12 core instruments plus Takeover and SFD for fuller L-171/2012 coverage.
- Raw extracts written under `raw/papers/cnpf/UE-*.md`; previous UE raw files archived under `C:\Users\harab\wiki\_archive\raw\cnpf-eurlex-before-20260709-144036`.
- Raw acquis manifest updated: `raw/papers/cnpf/_manifest.md`, section `F. Acquis UE`.
- Existing acquis pages updated with EUR-Lex raw anchors; new pages created: `concepts/acquis-ICSD.md`, `concepts/acquis-Takeover.md`, `concepts/acquis-SFD.md`.
- Related link lines updated in `L-171-2012`, `L-2-2020`, `L-234-2016`, `L-181-2023`, `REG-ICF`, and `cnpf-transposition-matrix`.

## [2026-07-09] lint | CNPF legal/acquis complete lint

- Scope: 33 active pages and 28 raw CNPF files.
- Report: `_meta/lint/cnpf-legal-lint-2026-07-09.md`.
- JSON audit: `_meta/lint/cnpf-legal-lint-2026-07-09.json`.
- Severity counts: high=0, medium=340, low=29.
- Technical graph/frontmatter summary: broken wikilinks=0, invalid tags=0, missing index entries=0, raw SHA drift=0.

## [2026-07-09] update | Execute all CNPF remediation and extended EUR-Lex ingest

- Backup used: `C:\Users\harab\wiki-backups\wiki-before-execute-all-remediation-20260709-145828`.
- Legal anchor remediation applied to `entities/L-171-2012.md`, `entities/L-192-1998.md`, and `entities/L-1134-1997.md`; no unresolved `[de verificat]` was converted into a settled fact.
- Normalized transposition status wording in `concepts/acquis-AIFMD.md` and `concepts/acquis-CSDR-EMIR.md`.
- Fetched/wrote structured Romanian EUR-Lex extracts for 14 connected acquis instruments covering AML, Company Law, Consumer Credit, Insurance, IORP, and MTPL.
- Updated `raw/papers/cnpf/_manifest.md` section `G. Acquis UE — domenii conexe CNPF/BNM` and updated six connected acquis pages with raw anchors.

## [2026-07-09] lint | CNPF legal/acquis complete lint

- Scope: 33 active pages and 42 raw CNPF files.
- Report: `_meta/lint/cnpf-legal-lint-2026-07-09.md`.
- JSON audit: `_meta/lint/cnpf-legal-lint-2026-07-09.json`.
- Severity counts: high=0, medium=305, low=29.
- Technical graph/frontmatter summary: broken wikilinks=0, invalid tags=0, missing index entries=0, raw SHA drift=0.

## [2026-07-09] ingest | Legis.md RO consolidated/current Moldovan legal texts

- Backup created before ingest: `C:\Users\harab\wiki-backups\wiki-before-legis-md-consolidated-ingest-20260709-151106`.
- Previous Moldovan-law raw files archived under `C:\Users\harab\wiki\_archive\raw\cnpf-legis-md-before-20260709-152933`.
- Fetched `showdetails` HTML from legis.md and refreshed 15 raw Moldovan legal/amendment files under `raw/papers/cnpf/`.
- Core active pages updated conservatively: `entities/L-171-2012.md`, `entities/L-192-1998.md`, `entities/L-1134-1997.md`.
- Manifest updated: `raw/papers/cnpf/_manifest.md`, section `H. Legis.md — legi moldovenești CNPF/BNM refresh`.
- Note: uncertainty markers were preserved; post-2025 L-171 consolidation remains explicitly `[de verificat]` because accessible legis.md text and LP177/2025 amendment are separate sources.

## [2026-07-09] lint | CNPF legal/acquis complete lint

- Scope: 33 active pages and 43 raw CNPF files.
- Report: `_meta/lint/cnpf-legal-lint-2026-07-09.md`.
- JSON audit: `_meta/lint/cnpf-legal-lint-2026-07-09.json`.
- Severity counts: high=0, medium=303, low=29.
- Technical graph/frontmatter summary: broken wikilinks=0, invalid tags=0, missing index entries=0, raw SHA drift=0.
- Note: an intermediate lint exposed SHA drift on the freshly generated legis.md raw files; hashes were recalculated against the actual post-frontmatter body before this final lint.

## [2026-07-09] query | Verificare schelet lege EMIR DOCX

- Backup creat înainte de salvare: `C:\Users\harab\wiki-backups\wiki-before-save-emir-query-20260709-160607`.
- Raw DOCX extras salvat: `raw/papers/cnpf/md-2026-07-03-schelet-lege-emir.md` (comentarii extrase: 7; track changes detectate: 0; SHA-256 DOCX: `2649b83a3b3f8e1162f4c371c292d69500d1394e8f622bd7b37099947d63afdd`).
- Pagină query creată: `queries/verificare-schelet-lege-emir-2026-07-03.md`.
- Actualizate: `index.md`, `raw/papers/cnpf/_manifest.md`, `concepts/acquis-CSDR-EMIR.md`.
- Verificare finală: pagina query are frontmatter și 6 surse raw existente; raw `sha256` valid; 0 wikilink-uri rupte; 0 pagini active lipsă din index; total pagini active: 34.

## [2026-07-09] ingest | Legea 100/2017 și HG1170/2016 — surse legis.md

- Backup created before ingest: `C:\Users\harab\wiki-backups\wiki-before-add-L100-HG1170-20260709-184850`.
- Raw legis.md full-text sources written: `raw/papers/moldova-legal/L-100-2017.md` (`doc_id` 144467) and `raw/papers/moldova-legal/HG-1170-2016.md` (`doc_id` 118977).
- Entity pages created: `entities/L-100-2017.md`, `entities/HG-1170-2016.md`.
- Manifest created: `raw/papers/moldova-legal/_manifest.md`.
- Note: `HG1170` was treated literally as Hotărârea Guvernului nr. 1170/2016 privind transmiterea/schimbarea destinației/schimbul de terenuri; if the intended act was HG nr. 1171/2018 on EU-harmonisation, it remains to be ingested separately.
- Verification: raw SHA values recalculated against final post-frontmatter bodies; active index count updated to 36 pages.

## [2026-07-09] update | EU transposition workflow foundation — steps 1–3

- Backup created before changes: `C:\Users\harab\wiki-backups\wiki-before-eu-transposition-foundation-20260709-193401`.
- Plan saved: `_meta/plans/eu-transposition-foundation-20260709-193401.md`.
- Step 1 source pack: added raw legis.md text `raw/papers/moldova-legal/HG-1171-2018.md` (`doc_id` 144185) and entity `entities/HG-1171-2018.md`; updated `entities/L-100-2017.md`; kept `HG-1170-2016` as literal/non-core disambiguation.
- Step 2 method page created: `concepts/moldova-eu-transposition-method.md`.
- Step 3 rule matrix created: `concepts/moldova-eu-transposition-rule-matrix.md`.
- Manifest refreshed: `raw/papers/moldova-legal/_manifest.md`.
- Verification target: raw SHA valid, frontmatter/tags valid, no broken wikilinks, no active index gaps; active page count updated to 39.

## [2026-07-09] query | Test metodă transpunere pe EMIR

- Backup created before save: `C:\Users\harab\wiki-backups\wiki-before-emir-method-test-20260709-200214`.
- Query page created: `queries/test-metoda-transpunere-emir-2026-07-09.md`.
- Backlink added in `concepts/acquis-CSDR-EMIR.md`.
- Updated `index.md` with active page count 40.
- Finding: method/rule matrix works; EMIR remains partial/fail for demonstrated transposition until a complete article-by-article concordance table is produced.

## [2026-07-09] comparison | Schelet de concordanță EMIR

- Backup created before changes: `C:\Users\harab\wiki-backups\wiki-before-emir-concordance-skeleton-20260709-201713`.
- Supplemental Cellar extract created: `raw/papers/cnpf/UE-648-2012-priority-articles-2026-07-09.md` (priority EMIR articles for concordance work).
- Comparison page created: `comparisons/emir-concordance-skeleton.md`.
- Updated backlinks/status in `concepts/acquis-CSDR-EMIR.md`, `queries/test-metoda-transpunere-emir-2026-07-09.md`, and `comparisons/cnpf-transposition-matrix.md`.
- Manifest and index updated; active page count 41.
- Finding: EMIR remains transposition-undemonstrated until a formal HG1171 concordance table is completed; the new page provides the working skeleton and decision questions.
- Verification after correction: raw SHA valid, frontmatter/tags valid, no broken wikilinks, no active index gaps; active page count 41.

## [2026-07-09] query | Pachet soluții normative EMIR faza 1

- Backup created before changes: `C:\Users\harab\wiki-backups\wiki-before-emir-draft-normative-package-20260709-202713`.
- Query page created: `queries/emir-draft-normative-package-phase-1-2026-07-09.md`.
- Updated backlinks in `comparisons/emir-concordance-skeleton.md` and `concepts/acquis-CSDR-EMIR.md`.
- Index updated; active page count 42.
- Content: text normativ de lucru pentru dispoziții generale, definiții, tranzacții intragrup, CNPF/BNM, cooperare, clearing, reporting, risk mitigation, CPC eligibile, registre centrale de tranzacții și dispoziții tranzitorii.
- Open: capitolul de supraveghere/sancțiuni și modificările conexe la legi naționale rămân faza 2.

## [2026-07-10] query | Draft complet și audit Legea 100/HG1171 — EMIR

- Backup created before changes: `C:\Users\harab\wiki-backups\wiki-before-emir-complete-draft-audit-20260710-140634`.
- DOCX extracted from `C:\Users\harab\Downloads\2026.07.09_Proiect_lege_EMIR_completat.docx`; comments detected: 0; tracked changes detected: 0; SHA-256 `3b6c41b26961e435079ea4802c2a20ca4c181b8ccbc0696abd0ebe085fbb538b`.
- Raw source written: `raw/papers/cnpf/md-2026-07-09-proiect-lege-emir-completat.md`.
- Query pages created: `queries/emir-draft-complet-2026-07-10.md` and `queries/emir-audit-conformitate-lege100-hg1171-2026-07-10.md`.
- Download artifacts created: `Draft_complet_lege_EMIR_2026-07-10.md/.docx`, `Audit_conformitate_Legea100_HG1171_EMIR_2026-07-10.md/.docx`, `Tabel_concordanta_preliminar_EMIR_2026-07-10.md`.
- Updated: `index.md`, `raw/papers/cnpf/_manifest.md`, `concepts/acquis-CSDR-EMIR.md`, `comparisons/emir-concordance-skeleton.md`.
- Finding: draftul complet este utilizabil ca text normativ de lucru, dar dosarul Legea 100/HG1171 rămâne incomplet până la nota de fundamentare, tabelul oficial de concordanță și expertiza de compatibilitate.
- Verification: active pages 44 vs index 44; broken wikilinks 0; index gaps 0; frontmatter/tag issues 0; new raw source SHA valid; EMIR priority raw SHA valid. Exceptions: existing procedural raw files `raw/papers/moldova-legal/L-100-2017.md` and `raw/papers/moldova-legal/HG-1171-2018.md` show pre-existing SHA mismatch and were not modified.

## [2026-07-12] ingest | Moldova policy framework — official strategies, programmes and decisions from UNDP folder

- Backup created before changes: `C:\Users\harab\wiki-backups\wiki-before-undp-policy-ingest-20260712-115103`.
- Original source files preserved unchanged under `raw/papers/moldova-policy/original/`; readable raw extracts with provenance, body SHA-256 and original-file SHA-256 created under `raw/papers/moldova-policy/`.
- New source-backed entity pages: `L-315-2022`, `HG-393-2024`, `HG-361-2024`, `HG-829-2023`, `HG-841-2024`, `HG-650-2023`, and `HG-260-2025`.
- Scope intentionally excludes UNDP procurement/application materials, NEDS working files, internal M&E drafts, duplicate archives and personal documents.
- The 2023 digital-transformation implementation report was retained only as a dated supporting raw source for `HG-650-2023`; it is not treated as current performance evidence.
- Final validation: 51 active pages and index total 51; 0 frontmatter issues, 0 invalid tags, 0 broken wikilinks, 0 index gaps; all 8 raw body hashes and all 8 preserved-original hashes valid.
- Git note: `C:\Users\harab\wiki` is not a Git repository, so no Git diff/stat was available.

## [2026-07-12] lint | Full WikiLLM audit after policy-corpus reconciliation

- Fresh backup created before work: `C:\Users\harab\wiki-backups\wiki-before-policy-corpus-lint-20260712-120222`.
- Reconciliation confirmed that the official-policy corpus was already ingested; no duplicate pages or raw sources were created.
- Audit reports saved: `_meta/lint/wiki-lint-2026-07-12.md` and `_meta/lint/wiki-lint-2026-07-12.json`.
- Scope: 51 active pages and 59 raw Markdown sources.
- Findings: high=0, medium=2, low=44. Full path-level results are in the report; no automatic remediation was applied during this audit.
## [2026-07-12] ingest | MDED policy corpus — macroeconomic, sustainable finance, economic criteria and Growth Plan

- Backup created and verified: `C:\Users\harab\wiki-backups\wiki-before-mded-policy-ingest-20260712-122105`.
- Preserved 12 original source files under `raw/papers/mded-policy-2024/original/` and generated validated readable Markdown extractions under `raw/papers/mded-policy-2024/`.
- Created 11 active pages: World Bank CEM and CPF, ERP, sustainable-finance roadmap, EU Reform and Growth Facility, five linked concepts, and the Planul de creștere/SNDE/PND/ERP comparison.
- Updated `entities/HG-260-2025.md` with the EU-facility relationship and implementation-governance links.
- Source classification: EU, World Bank and Ministry of Finance documents are primary/official sources; the MDED screening slides and questionnaire are dated institutional preparation materials and are marked with appropriate confidence caveats.
- Post-ingest audit: 0 new-page frontmatter/tag errors, 0 broken wikilinks, 0 index gaps, and 0 raw-integrity errors after remediation; audit saved at `_meta/imports/mded-policy-2024/ingest-audit.json`.

## [2026-07-12] ingest | BNM official legal and formal-report corpus

- Backup created and verified: `C:\Users\harab\wiki-backups\wiki-before-bnm-corpus-ingest-20260712-205717`.
- Preserved 305 downloaded BNM-hosted originals unchanged under `raw/papers/bnm/original/` and created paired readable Markdown extracts under `raw/papers/bnm/documents/`.
- Added BNM corpus governance files: `raw/papers/bnm/_manifest.md`, `_manifest.csv`, `BNM_LEGISLATION_INVENTORY.md`, `BNM_REPORTS_INVENTORY.md`, and the original download manifests.
- Created entity pages: `entities/bnm.md` and `entities/bnm-official-document-corpus-2026.md`; `index.md` updated to 64 active pages.
- Corpus scope: 305 unique downloaded files mapped to 208 BNM catalogue records (115 legal-register and 93 formal-report-series records). PDF and DOC/DOCX variants are retained where published.
- Final audit: 305 raw records; 0 raw-integrity issues; 64 active pages; 0 frontmatter/tag issues; 0 broken wikilinks; 0 index gaps. Audit saved at `_meta/imports/bnm/ingest-audit.json` and `.md`.

## [2026-07-12] lint | Full WikiLLM audit after BNM corpus ingest

- Reports saved: `_meta/lint/wiki-lint-2026-07-12-post-bnm.md` and `.json`.
- Scope: 64 active pages, 374 raw Markdown sources with frontmatter, 20 log entries.
- Findings: high=12, medium=2, low=9.
- High findings are all raw-body SHA drift in 12 `raw/papers/mded-policy-2024/` files; no broken wikilinks, missing required active-page frontmatter, invalid tags, missing source paths, index gaps, or orphan pages were detected.
- Medium findings: two oversized EMIR query pages (991 and 487 lines). Low findings: nine single-source entity pages, all transparently marked by their `sources:` fields.
- No remediation was applied during this audit; the report preserves the exact paths and expected/actual hashes for review.

## [2026-07-12] repair | BNM Annual Report 2000 raw extraction

- Investigated `raw/papers/bnm/original/229__ra2000_en.pdf` (Annual Report 2000): the 585,032-byte PDF is unencrypted, has 68 pages, renders cleanly, and exactly matches a fresh download from `https://www.bnm.md/files/ra2000_en.pdf` (SHA-256 `0c3eddc199bed9199934cfd28aa915a7767d44daa03aeb06a5355956378f8da4`).
- The apparent wiki breakage was in the initial PyMuPDF text extraction: it emitted 71,753 non-printing control characters because of the PDF’s legacy font encoding, not a corrupt PDF.
- Replaced only the derived Markdown extraction at `raw/papers/bnm/documents/229__ra2000_en.pdf.md` with `pdftotext -layout` output; removed page-break control characters; preserved the original PDF unchanged.
- Updated the BNM CSV/Markdown manifests, extraction status and raw-body SHA-256. Validation: raw-body hash matches; manifest hash matches; extracted body has no non-printing control characters.

## [2026-07-12] update | BNM legal/report corpus separation

- Backup created and verified before the structural move: `C:\Users\harab\wiki-backups\bnm-before-legal-report-separation-20260712-232536` (619 files, matching the pre-move BNM corpus).
- Replaced the former flat `original/` and `documents/` folders with two explicit branches: `raw/papers/bnm/legal/{original,documents}/` and `raw/papers/bnm/reports/{original,documents}/`.
- Classification uses the source BNM catalogue record: legal branch = Laws/Regulations catalogue attachments; report branch = Annual/Inflation/Financial Stability report-catalogue attachments. It does not overstate the individual legal/report status of related page-level attachments.
- Counts: 204 preserved legal-branch files and 101 preserved report-branch files; master manifest retains all 305 rows. Branch-specific CSV/Markdown manifests and root `README.md`/master navigation added.
- Updated every raw provenance path, raw-body SHA-256 and report `source_type`; updated `entities/bnm-official-document-corpus-2026.md`.
- Verification: 305 master records; branch manifests 204/101; 0 path or original/raw-body hash issues; 0 invalid frontmatter/tags, broken wikilinks or index gaps. Annual Report 2000 now resides at `raw/papers/bnm/reports/original/229__ra2000_en.pdf`.

## [2026-07-13] ingest | Codul civil al Republicii Moldova — Cod nr. CC1107/2002

- Preserved the user-supplied 873-page consolidated PDF unchanged at `raw/assets/moldova-legal/CC-1107-2002-2026-07-12.pdf`; its SHA-256 is `ce9a2b286380eb8f8efcc218be78bc9f1ece7faefb4b9d51c20b924f0e323615`.
- Added the full text-layer extraction as `raw/papers/moldova-legal/CC-1107-2002.md` with raw-body SHA-256 `de211a1a0fb0a9482edca2c94a441145b40ae0487318dc613e428fde396c9bcc`.
- Created [[CC-1107-2002]], updated the transverse-legal-source manifest, and added the page to `index.md` (65 active pages).
- The source header identifies LP251/2025 as effective from 2026-04-01; the entity page retains a currentness and article-level verification caution for future legal work.

## [2026-09-04] lint | CNPF legal/acquis complete lint — baseline pre-ancorare

- Rulare de referință, înainte de orice scriere din jobs 1–3. Baseline-ul real pentru comparație, nu `cnpf-legal-lint-2026-07-09.json`, care derivase deja din lucrările 2026-07-09 → 07-13.
- Scope: 65 active pages and 46 raw CNPF files.
- Copie păstrată: `_meta/lint/cnpf-legal-lint-2026-09-04-pre-anchoring.{md,json}`.
- Severity counts: high=0, medium=1060, low=36.
- Technical graph/frontmatter summary: broken wikilinks=0, invalid tags=1, missing index entries=0, raw SHA drift=0.

## [2026-09-04] anchor | Job 1 — Codul civil CC-1107-2002 ancorat la nivel de articol

- Backup verificat înainte de orice scriere: `C:\Users\harab\wiki-backups\wiki-2026-09-04-pre-anchoring` (859 fișiere, 39 directoare, 664.108.199 octeți, identice cu sursa).
- `raw/papers/moldova-legal/CC-1107-2002.md` avea zero titluri Markdown pe 2.057.333 de caractere de text integral; nu trecuse prin scriptul de ingest legis.md care creează ancorele.
- Inserate **3.038 de ancore**: 2.657 articole (`## Articolul N. <titlu>`), 5 Cartea, 22 Titlul, 109 Capitolul, 172 Secțiunea, 17 Subsecțiunea, 56 §. Titlurile rupte de extracția PDF au fost reunite doar în ancoră.
- Metodă: titlurile sînt **inserate deasupra** liniilor originale; nicio linie-sursă nu a fost modificată, reordonată sau reunită. Corpul rămîne identic octet cu octet.
- Frontmatter: `sha256` mutat în `sha256_pre_anchoring` (`de211a1a…396c9bcc`); `sha256` nou `66a1ec69…7b0cfb91`; adăugate `articole detectate: 2657`, `anchoring_date`, `anchor_convention`, `sha256_convention: raw`. `source_file_sha256` (hash-ul PDF-ului) păstrat neschimbat.
- Verificări, toate trecute față de copia din backup, nu față de copia de lucru: strip-and-compare identic octet cu octet; 2.657 ancore = 2.657 marcaje-sursă, număr cu număr; numerotare strict crescătoare; frontmatter valid, `sha256` reproduce corpul ancorat.
- Constatări de abrogare pentru cele 14 numere absente: 2171, 2172, 2185, 2188, 2404, 2485 au marcaj individual `[Art.NNNN abrogat prin LP251 din 10.07.25]`; blocul 2047–2054 este acoperit de `Secțiunea a 3-a- abrogată`, **fără citare LP în text** — marcat `[de verificat]` în manifest.
- Corecții față de datele din brief: `Titlul` există (22, scrise `T i t l u l` cu spațiere între litere); Secțiunea este 172 nu 111 și Subsecțiunea 17 nu 10 (fișierul folosește două codificări de diacritice); există 56 de subdiviziuni `§`, nemenționate.
- `Articolul 723`: extracția a unit titlul cu dispoziția pe aceeași linie fizică; ancora a fost corectată manual, linia-sursă rămîne nemodificată. Singurul caz din act, confirmat prin scanarea tuturor celor 2.657 de titluri.
- Lint: `_meta/lint/cnpf-legal-lint-2026-09-04-pre-anchoring.json` păstrat ca referință reală. Lintul acoperă doar `raw/papers/cnpf/`, deci este neschimbat după job 1 (high=0, medium=1060, low=36; `raw_sha_drift`=0).
- Scripturi repetabile: `_meta/imports/anchoring/{lib_anchor,anchor_cc,verify_anchoring,sample_diff,survey_cc,survey_sha_conventions}.py`.
- Rămîne nefăcut în această trecere: reunirea liniilor corpului (60,2% din liniile ne-goale continuă la mijloc de frază) — operațiune separată, cu backup și diff proprii.

## [2026-09-04] lint | CNPF legal/acquis complete lint — după job 1

- Scope: 65 active pages and 46 raw CNPF files.
- Report: `_meta/lint/cnpf-legal-lint-2026-09-04.md`.
- JSON audit: `_meta/lint/cnpf-legal-lint-2026-09-04.json`.
- Severity counts: high=0, medium=1061, low=37.
- Diferența față de baseline (+1 medium, +1 low) provine integral din textul adăugat de mine în `entities/CC-1107-2002.md`: un paragraf nou de status și un marcaj `[de verificat]` intenționat. Nicio regresie.
- Technical graph/frontmatter summary: broken wikilinks=0, invalid tags=1, missing index entries=0, raw SHA drift=0.

## [2026-09-04] anchor | Job 2 — forma `Art.N. –` ancorată (L-192-1998, L-178-2020, L-177-2025)

- `raw/papers/cnpf/L-192-1998.md` raporta `articole detectate: 0` pe 44.402 de caractere de text integral. Cauza: redactarea pre-2000 `Art.1. – ` în loc de `Articolul 1.`, pe care regexul de ingest nu o prindea. Legea care constituie CNPF și îi definește mandatul nu era citabilă la nivel de articol.
- Inserate **31 de ancore** în L-192-1998, **8** în L-178-2020 (Art. I–VIII) și **4** în L-177-2025 (Art. I–IV) — total 43. Tokenul `Art.N. –` și liniile-sursă rămîn nemodificate; ancora doar precede dispoziția.
- Aceste acte nu au titluri de articol: dispoziția continuă direct după linia de pauză, deci ancora este `## Articolul N.` — numărul singur, conform brief-ului.
- Marcajul de verificare este `^## Articolul `, mai îngust decît `^#`, fiindcă fișierele CNPF au deja titluri de preambul wiki (`# raw/…`, `## Capitolul I`).
- Verificări, toate trecute față de copiile din backup: strip-and-compare identic octet cu octet la toate trei; 31/31, 8/8 și 4/4 ancore, etichetă cu etichetă; ordine strict crescătoare (cifrele romane convertite pentru comparație); `sha256` recalculat reproduce corpul ancorat.
- `sha256` mutat în `sha256_pre_anchoring` la toate trei; convenția acestor fișiere este CRLF→LF, consemnată ca `sha256_convention: LF`. Lintul confirmă independent: `raw_sha_drift`=0.
- **art. 13^1 (L-192-1998).** Extracția a aplatizat exponentul în `Art. 131.`. Ancoră normalizată la `## Articolul 13^1.`, cu `superscript_articles:` în frontmatter. Dovada este exclusiv pozițională — urmează art. 13, numerotarea reia la art. 14, 131 este în afara intervalului 1–31. Nu există în text nici `Art.13^1`, nici notă de amendament care să confirme; consemnat ca atare, nu prezentat drept confirmat.
- **art. 21 (L-192-1998) lipsă, fără temei în sursă.** Numerotarea sare 20 → 22, dar fișierul nu conține niciun marcaj `abrogat`, nicio notă în paranteze drepte și nicio trimitere la art. 21. Regula de verificare „fiecare lacună explicată printr-o abrogare consemnată" nu poate fi satisfăcută din sursă. `[de verificat]` față de legis.md.
- **Reclasificare.** `L-178-2020` și `L-177-2025` erau descrise ca acte „fără articole proprii". Au articole proprii, numerotate roman, containere pentru modificări aduse altor acte. `L-178-2020` este pivotul instituțional care a mutat supravegherea prudențială la BNM, iar art. I–VIII sînt citate în practică.
- **Sweep pe toate cele 378 de fișiere din `raw/papers/`.** Defectul exact `Art.N. –` există într-un **singur** fișier — L-192-1998. Constatări conexe, raportate și nefixate: (a) 89 de fișiere din corpusul BNM în engleză conțin 3.597 de marcaje `Article N` la început de linie și zero ancore — traducerile legilor 202/2017, 232/2016, 548/1995, 92/2022, 139/2007, 114/2012, 62/2008; formă diferită, aceeași clasă de defect, în afara perimetrului brief-ului; (b) notele `[Art.15 al.(11)…]` și `[Art.15 al.(12)…]` din L-192-1998 sînt probabil alin. (1^1) și (1^2) aplatizate — defectul de exponent apare și la nivel de alineat.
- Restul rezultatelor sweep-ului nu necesită acțiune: cele ~40 de forme `Art.N` la început de linie din documentele BNM în engleză sînt trimiteri încrucișate rupte de rând (`Art.116 par. (1)-(4), Art.117…`), nu titluri.
- Scripturi: `_meta/imports/anchoring/{anchor_artdash,lib_superscript,sweep_art_forms}.py`; raport sweep în `_meta/anchoring-work/sweep-art-forms.txt`.

## [2026-09-04] lint | CNPF legal/acquis complete lint

- Scope: 65 active pages and 46 raw CNPF files.
- Report: `_meta/lint/cnpf-legal-lint-2026-09-04.md`.
- JSON audit: `_meta/lint/cnpf-legal-lint-2026-09-04.json`.
- Severity counts: high=0, medium=1064, low=40.
- Technical graph/frontmatter summary: broken wikilinks=0, invalid tags=1, missing index entries=0, raw SHA drift=0.

## [2026-09-04] consolidare | Metoda adusă în folder, folderul-strămoș arhivat și șters

- Adăugat `CLAUDE.md` la rădăcină și `legal-career/00` … `06`, copii ale documentelor din proiectul claude.ai „Legal Wiki", luate la 2026-09-04. Fiecare copie poartă în antet data și sursa. Proiectul rămâne originalul; copiile nu se editează aici.
- `CLAUDE.md` nu este o copie. Conține harta folderului, starea reală a stratului raw după auditul din 2026-09-04 și o singură regulă schimbată față de proiect: linia de încredere se stabilește deschizând fișierul și citind articolul, nu prin apreciere. Dacă nu s-a deschis niciun fișier, răspunsul nu este `ancorat`.
- Avertisment adăugat în antetul copiei locale a documentului 05: secțiunea de acoperire este contrazisă de audit în trei puncte. Corpul documentului nu a fost modificat.
- Examinat `C:\Users\harab\Desktop\Justitiarul Path\Wiki`, folderul-strămoș. Trei părți: `cnpf-wiki-ro` (8–9 iulie, originea acestui wiki), `BNM_site_inventory` (12 iulie, 305 fișiere sursă, 546 MB) și `Dreptul afacerilor` (13 iulie).
- Verificat că `BNM_site_inventory` este duplicat integral al fișierelor din `raw/papers/bnm/*/original`: 571.837.380 octeți acolo față de 571.841.476 aici, iar cele patru diferențe aparente sînt nume de fișier trunchiate, nu documente lipsă.
- Arhivat integral `cnpf-wiki-ro` în `_archive/cnpf-wiki-ro-2026-07/` (64 de fișiere, 570.281 octeți, verificat identic), cu `_PROVENANCE.md`. Se păstrează pentru trei lucruri care nu au trecut mai departe ca atare: `CLAUDE.md` cu regulile de operare originale în română, `prompts.md` și `wiki/_lint-report.md` din 9 iulie, care conține secțiunea „Rezolvat și menținut".
- Recuperat planul de descărcare eșuat din 13 iulie în `_meta/plans/2026-09-04-plan-descarcare-esuat-drept-afaceri.json`, cu nota `2026-09-04-lacuna-drept-afaceri.md`. Unsprezece acte, toate eșuate, probabil protecția anti-bot a legis.md. Consecința: persona P1 nu are sursă ancorată pentru dreptul corporativ, fiindcă lipsesc Legea 135/2007 și Legea 220/2007, ambele indicate ca surse de bază în documentul 04. Lipsesc și Codul fiscal 1163/1997 și Codul administrativ 116/2018.
- Șters `Desktop\Justitiarul Path\Wiki` (574 MB, 631 de fișiere) după arhivare și verificare. `balta marin` și `sabina` din același folder nu au fost atinse.
- `CLAUDE.md` actualizat la starea de după ancorare: Codul civil și L-192-1998 ancorate, reclasificarea L-178-2020 și L-177-2025, jobul 3 încă nefăcut, plus o secțiune nouă „Open findings that need Eugen's judgement" cu cinci puncte: art. 21 din L-192-1998 fără temei în sursă, cele 3.597 de marcaje neancorate din corpusul BNM în engleză, blocul 2047–2054 din Codul civil, aplatizarea exponentului la nivel de alineat și lacuna de drept al afacerilor. Versiunea anterioară a fișierului, scrisă în aceeași zi înainte de ancorare, a fost înlocuită.

## [2026-09-04] anchor | Job 3 — articole cu exponent aplatizat, numerotare normalizată

- Defectul: redactarea moldovenească inserează articole ca 146¹, 50¹, 88¹, iar extracția a aplatizat exponentul. Art. 146¹ din L-171-2012 era stocat ca `## Articolul 1461`. Nu arată ca o lipsă — o citare la art. 146¹ este negăsibilă, iar vecinul art. 146 se citește drept „articolul o mie patru sute șaizeci și unu".
- **11 articole normalizate în 3 fișiere**, față de cele 3 numite în brief: `L-171-2012` — 40^1, 88^1, 88^2, 88^3, 88^4, 131^1, 141^1, 146^1 (8); `L-100-2017` — 27^1, 70^1 (2); `L-139-2007` — 50^1 (1).
- Spre deosebire de jobs 1–2, aici se **modifică** linii de titlu existente, nu se inserează linii noi. Se schimbă un singur token pe linia afectată; toate liniile care nu sunt titluri și toate celelalte titluri rămân identice octet cu octet. Verificare separată: `verify_superscripts.py`.
- Verificări, toate trecute față de copiile din backup: linii ne-titlu identice octet cu octet; număr de titluri neschimbat (182→182, 74→74, 99→99), cu 8/1/2 modificate; cifrele păstrate la fiecare normalizare (`1461` → `146^1`); ordine strict crescătoare sub cheia (bază, exponent); `sha256` recalculat reproduce corpul. Lintul confirmă independent: `raw_sha_drift`=0.
- **Blocul 88^1–88^4 din L-171-2012 — descoperire nouă, neinclusă în brief.** Cele patru articole despre agențiile de rating de credit formează Secțiunea a 7-a, inserată după art. 79. Detectorul naiv din brief („articol care urmează imediat unui articol al cărui număr este prefixul său") **ratează un șir**: după primul element, predecesorul este el însuși aplatizat. Detectorul a fost rescris ca să lucreze pe șiruri, cerând prefix comun și sufixe 1,2,3,… încadrate între articolul dinaintea și cel de după șir.
- **Articolul de bază 88 nu există**, iar **art. 80–87 lipsesc** din L-171-2012, fără niciun marcaj de abrogare în fișier. `[de verificat]` față de legis.md.
- **Nicio normalizare nu are confirmare textuală.** Ruta sugerată în brief — forma `Art.146^1` sau o notă `[Art.1461 introdus prin LP…]` — **nu există în niciunul dintre cele trei fișiere**: zero accente circumflexe, zero exponenți Unicode, zero note de amendament pentru aceste numere. Dovada este exclusiv pozițională și este consemnată ca atare în frontmatter, sub `superscript_articles:`, nu prezentată drept confirmată. Argumentul rămâne concludent: un act cu 78 de articole nu poate avea articolul 701.
- **Lacune de numerotare neexplicate**, raportate nu reparate: `L-171-2012` art. 80–87; `L-100-2017` art. 25, 26, 33, 52. Niciunul dintre fișiere nu conține marcaje de abrogare. Regula de verificare „fiecare lacună explicată printr-o abrogare consemnată" nu poate fi satisfăcută din sursă pentru aceste acte. `[de verificat]`
- Scanare pe tot corpusul cu detectorul rescris: în afara celor 11, singurele anomalii rămase sunt extractele UE rare (`UE-2009-138` art. 41→100, `UE-2024-1624` art. 20→78), care sunt prin construcție parțiale. Sub-articolele UE cu literă (`4a`, `7a`–`7e`) și `13^1` deja normalizat în job 2 sunt excluse explicit din detecție.
- Nicio pagină wiki nu cita numerele aplatizate, deci nicio trimitere nu a rămas suspendată. `article_anchor_missing_target`=0.
- Scripturi: `_meta/imports/anchoring/{detect_superscripts,fix_superscripts,verify_superscripts,lib_superscript}.py`.

## [2026-09-04] lint | CNPF legal/acquis complete lint

- Scope: 65 active pages and 46 raw CNPF files.
- Report: `_meta/lint/cnpf-legal-lint-2026-09-04.md`.
- JSON audit: `_meta/lint/cnpf-legal-lint-2026-09-04.json`.
- Severity counts: high=0, medium=1069, low=45.
- Technical graph/frontmatter summary: broken wikilinks=0, invalid tags=1, missing index entries=0, raw SHA drift=0.

## [2026-09-04] unwrap | Codul civil — reunirea liniilor rupte de extracția PDF

- Backup separat înainte de scriere: `C:\Users\harab\wiki-backups\wiki-2026-09-04-pre-unwrap` (977 fișiere, 668.921.628 octeți, verificat identic).
- Singura operațiune din întreaga lucrare care atinge textul propriu-zis. Garanția este formulată la nivel de caracter: **se schimbă doar spații albe** — fiecare reunire înlocuiește o întrerupere de linie cu un singur spațiu; niciun alt caracter nu a fost adăugat, șters sau reordonat.
- Dovada elimină tot spațiul alb din corpul rezultat (fără titlurile inserate) și din corpul **anterior ancorării**, apoi compară octet cu octet: **1.859.072 de octeți ne-spațiu identici**. Verificarea acoperă ambele treceri deodată — inserarea ancorelor și reunirea liniilor — și leagă starea curentă direct de extracția originală.
- Rezultate: 17.062 de întreruperi de linie eliminate; linii ne-goale în corp 30.041 → 12.979; **fraze rupte la mijloc 16.878 → 213 (−98,7%)**; lungime mediană a liniei 82 → 127; nicio linie peste 4.000 de caractere.
- Regula nu folosește lungimea liniei. Lățimea de rupere nu are prag curat: lungimile formează o pantă continuă între 80 și 98 de caractere, iar 727 de linii de peste 88 de caractere încheie un paragraf în timp ce 13.068 mai scurte continuă. Se reunește doar o linie **neterminată gramatical** — fără punctuație de final, sau terminată într-o abreviere juridică (`art.`, `alin.`, `lit.`; 98 de cazuri) — și doar dacă următoarea nu începe o unitate nouă.
- Consecință deliberată: acolo unde o frază s-a terminat exact la punctul de rupere, linia rămâne separată. Fiecare linie rezultată este cel puțin o frază întreagă, iar **două paragrafe nu sunt niciodată contopite** — verificat separat, 0 linii suspecte.
- Titlurile de articol se reunesc exact cât spune ancora: **2.656 din 2.657** se închid la limita înregistrată în `## Articolul N.`, ceea ce ține dispoziția în afara titlului (art. 23 este cazul-tip). Singura excepție rămâne art. 723, unde extracția a pus sfârșitul titlului și începutul dispoziției pe aceeași linie fizică.
- Cele 213 rupturi rămase sunt corecte: enumerări încheiate cu `; sau` / `; și` înaintea unui punct `b)`, marcaje structurale urmate de titlul lor, și preambulul (date de publicare, lista legilor modificatoare) lăsat neatins intenționat.
- Frontmatter: `sha256` mutat în `sha256_pre_unwrap` (`66a1ec69…`), `sha256` nou `edaf71fa…`, plus `unwrap_date` și `unwrap_convention`. `sha256_pre_anchoring` și `source_file_sha256` rămân neatinse, deci lanțul de proveniență este complet.
- Lint neschimbat pe invarianți: `raw_sha_drift`=0, `article_anchor_missing_target`=0, `broken_wikilinks`=0, high=0.
- Scripturi: `_meta/imports/anchoring/{unwrap_cc,verify_unwrap}.py`.

## [2026-09-04] corectare | Exponenții AU confirmare textuală în HTML-ul legis.md păstrat

- În raportul jobului 3 am scris că niciunul dintre cei 12 exponenți normalizați nu are confirmare textuală. Afirmația este corectă despre fișierele `.md` extrase și **greșită despre surse**.
- HTML-ul legis.md păstrat în acest depozit, la `_meta/imports/cnpf/legis-md-consolidated/`, conține marcajul explicit. Verificat direct: `showdetails-121985.html` (L-171-2012) conține `Articolul 40<sup>1</sup>`, `Articolul 131<sup>1</sup>`, `Articolul 141<sup>1</sup>`, `Articolul 146<sup>1</sup>`; `showdetails-121166.html` (L-139-2007) conține `Articolul 50<sup>1</sup>`.
- Cauza pierderii: extracția folosește `text_content()`, care concatenează conținutul lui `<sup>`, deci 146¹ devine `1461`. Ruta de confirmare pe care o aștepta brief-ul **există**; eu am căutat-o doar în textul extras, nu și în HTML-ul păstrat aici. Omisiune de verificare, nu de raționament.
- Toate normalizările coincid cu ce arată marcajul, deci **nicio ancoră nu se schimbă**. Concluziile poziționale erau corecte.
- **L-192-1998 art. 13^1 rămâne excepția:** HTML-ul acelui act (`showdetails-128124.html`) nu conține niciun `<sup>` pentru articole, deci acesta se sprijină în continuare exclusiv pe argument pozițional.
- **Confirmat totodată defectul la nivel de alineat și de literă**, semnalat ca „probabil" în jobul 2 și acum dovedit: același HTML conține `[Art.15 al.(1<sup>1</sup>)…]`, `[Art.15 al.(1<sup>2</sup>)…]` și un punct `c<sup>1</sup>)`. Deci alin. (1¹), (1²) și lit. c¹) apar în text ca `(11)`, `(12)` și `c1)`. Netratat.
- **Consecință operațională pentru ingestiile viitoare:** scriptul de ingest trebuie să mapeze `<sup>N</sup>` la `^N` înainte de extragerea textului, nu să deducă exponenții din poziție după aceea.

## [2026-09-04] surse | doc_id pentru dreptul afacerilor și pentru cele trei consolidări expirate

- Verificat nota `_meta/plans/2026-09-04-lacuna-drept-afaceri.md` și JSON-ul aferent față de starea
  reală a folderului. Confirmat: cele 11 acte lipsesc într-adevăr din `raw/`; documentul 04 indică
  135/2007 și 220/2007 ca surse P1; citările din documentele 03 și 05 sunt fidele. O nuanță de
  lectură a JSON-ului: doar primul act a fost efectiv testat, restul de zece erori fiind
  `Target page, context or browser has been closed`, adică sesiunea era deja căzută.
- Trei corecții în notă. Cronologia era inversată, `showdetails` din 9 iulie precedă eșecul din
  13 iulie, nu îi urmează. Lista lipsurilor era incompletă pe propriul ei criteriu, adăugată Legea
  845/1992, a treia sursă P1 absentă, care nu figurase niciodată în planul de descărcare. Condiția
  de așteptare a ancorării a căzut, ancorarea fiind încheiată.
- Găsit și verificat `doc_id` pentru cele două legi corporative: **L-135-2007 = 153674**,
  consolidat la 27.03.2026, și **L-220-2007 = 155438**, consolidat la 23.07.2026. Ambele deschise,
  nu doar rezolvate: trec poarta de acceptare a scriptului de ingerare, iar titlurile din antet
  corespund denumirilor din documentul 04. Adăugate în `DOCS` din
  `_meta/imports/cnpf/legis_md_consolidated_ingest.py`, marcate ca neingerate.
- Documentată metoda de căutare, care nu era consemnată nicăieri. Rezultatele legis.md se încarcă
  prin AJAX: `getResults?nr_doc=<N>&search_type=1` pe o sesiune cu cookie, apoi `getAjaxContent`.
  `curl` cu User-Agent de desktop trece și acum protecția; numai calea prin browser automatizat a
  fost blocată la 13 iulie.
- Corectată o afirmație din `CLAUDE.md` scrisă mai devreme în aceeași zi, potrivit căreia niciunul
  dintre cei 12 exponenți normalizați nu are confirmare textuală. **11 din 12 au.** legis.md îi
  marchează `Articolul 146<sup>1</sup>`; aplatizarea se produce la extracție, fiindcă
  `text_content()` lipește cifrele. Cinci se confirmă din HTML-ul deja păstrat în wiki sub
  `_meta/imports/cnpf/legis-md-consolidated/`, alte șase prin descărcarea sursei curente. Toate 11
  coincid cu ce stabilise raționamentul pozițional, deci nicio ancoră nu se schimbă. Excepția
  rămâne `L-192-1998` art. 13^1, a cărui sursă nu conține niciun `<sup>`.
- Adăugată a treia consolidare expirată. `L-171-2012` nu era pe listă și este cea mai înșelătoare,
  fiindcă nimic din frontmatter nu avertizează cititorul: `L-177-2025` îi inserează art. 4^1, iar
  fișierul de bază nu conține nici articolul, nici trimiterea la legea de modificare. `doc_id`
  curente, toate verificate: L-308-2017 → 155856 (în vigoare 13.08.26, 47 de linii de modificare),
  L-92-2022 → 151081 (25.06.26), L-171-2012 → 156016 (01.06.27).
- Rezolvată parțial constatarea 5. Intervalul lipsă din `L-171-2012` este 80–88, nu 80–87, iar
  art. 80 **există** în consolidarea curentă, deci absența lui de aici este vechime, nu gol
  inexplicabil. Art. 81–88 lipsesc și din sursa curentă și rămân nelămurite.
- Backup înainte de scriere: `wiki-backups\wiki-2026-09-04-doc-ids-lacuna`, 977 de fișiere,
  668.921.628 octeți, confirmat identic la momentul copierii. Atenție: nu mai reflectă folderul,
  fiindcă rejoin-ul Codului civil a aterizat la 15:45, după copiere.

## [2026-09-04] backup | Copie nouă după aterizarea ambelor fire de lucru

- `wiki-backups\wiki-2026-09-04-post-rejoin-doc-ids`, 983 de fișiere, 671.309.551 octeți,
  confirmat identic prin numărare, dimensiune și `diff -rq`, fără nicio diferență.
- Motivul: copia anterioară din aceeași zi, `wiki-2026-09-04-doc-ids-lacuna`, a fost luată la 15:37
  și nu conține rejoin-ul Codului civil, aterizat la 15:45. O restaurare din ea ar fi pierdut acea
  operațiune. Copia nouă cuprinde ambele fire: rejoin-ul plus `doc_id`-urile și corecțiile.
- Folderul era liniștit de zece minute la momentul copierii, ultima scriere străină fiind
  reluarea lintului la 15:49. Verificat înainte de copiere că modificările din acest fir sînt
  intacte în `CLAUDE.md`, în scriptul de ingerare și în nota de lacună.
- Copia precedă cu o intrare această linie de jurnal, ceea ce este normal.
- Ștearsă copia intermediară `wiki-2026-09-04-doc-ids-lacuna`, 977 de fișiere, 668.921.628 octeți.
  Verificat înainte de ștergere că nu conținea nimic unic: niciun fișier absent din copia nouă, iar
  stările mai vechi ale fișierelor din `raw/` și `entities/`, inclusiv Codul civil dinaintea
  rejoin-ului și versiunea de la 15:31 a `CLAUDE.md`, sînt identice octet cu octet cu cele din
  `wiki-2026-09-04-pre-unwrap`. Rămân trei copii ale zilei: `pre-anchoring`, `pre-unwrap` și
  `post-rejoin-doc-ids`.

## [2026-09-04] dedup | Codul civil — eliminarea liniei de titlu duplicate sub fiecare ancoră

- Backup separat înainte de scriere: `C:\Users\harab\wiki-backups\wiki-2026-09-04-pre-dedup` (983 fișiere, 671.310.979 octeți, verificat identic).
- După reunirea liniilor, titlul fiecărui articol exista de două ori, identic octet cu octet: o dată ca ancoră inserată, o dată ca linie de corp imediat dedesubt. Copia din corp a fost ștearsă: **2.656 de linii**; corpul a scăzut de la 17.009 la 14.353 de linii, fișierul de la 2.358.208 la 2.197.134 de octeți.
- Este singura trecere din întreaga lucrare care **șterge** text, deci regula este îngustă: se șterge o linie **doar** dacă este identică octet cu octet cu ancora imediat de deasupra și **doar** dacă este linia imediat următoare. Verificat înainte de rulare: 2.656 din 2.657 de ancore aveau duplicatul exact pe linia următoare, 0 după linii goale.
- Reversibilitatea este demonstrată, nu afirmată: verificatorul **reconstruiește** corpul anterior ștergerii, reinserând textul fiecărei ancore ca linie de corp, și cere identitate octet cu octet. Trece.
- **Art. 723 nu a fost deduplicat.** Extracția i-a pus sfârșitul titlului și începutul dispoziției pe aceeași linie fizică, deci linia de corp conține text pe care ancora nu îl are; ștergerea ar fi pierdut primele cuvinte ale dispoziției. Prima versiune a verificatorului a tratat greșit acest caz — presupunea că orice linie care nu este duplicat exact a fost ștearsă — și a picat verificarea; testul de reținere a fost corectat la „linia următoare începe cu textul ancorei".
- **Lanț complet de proveniență, verificat end-to-end.** `verify_chain.py` desface toate cele trei treceri asupra Codului civil în ordine inversă — reinserează titlurile, elimină ancorele, normalizează spațiul alb — și compară cu extracția originală din 2026-07-13: **1.859.072 de octeți ne-spațiu, sha256 `124bd2b606868231835c0a85b614f72196c717467df9ba40d78c50c9ece3504d`, identic**. Niciun caracter de text juridic nu s-a schimbat de la extracție.
- Frontmatter: `sha256` mutat în `sha256_pre_dedup` (`edaf71fa…`), `sha256` nou `fa97b7ce…`, plus `dedup_date` și `dedup_convention`. Lanțul complet: `source_file_sha256` → `sha256_pre_anchoring` → `sha256_pre_unwrap` → `sha256_pre_dedup` → `sha256`.
- **Rămân 166 de duplicate structurale**, neatinse fiindcă cererea a vizat titlurile de articol: `Cartea` (5), `Capitolul` (109) și subdiviziunile `§` (51). `Titlul` (22) **nu** este duplicat exact — ancora normalizează `T i t l u l I` la `Titlul I`, deci ștergerea liniei-sursă ar pierde forma din PDF. `Secțiunea` și `Subsecțiunea` își țin titlul pe linie separată.
- Verificarea „șterge liniile care încep cu `#` și compară", valabilă după jobul 1, **nu mai este aplicabilă**; a fost înlocuită de `verify_chain.py`. Notat în manifest (C.1) și în `CLAUDE.md`.
- Scripturi: `_meta/imports/anchoring/{dedup_titles,verify_dedup,verify_chain}.py`.

## [2026-09-04] dedup | Codul civil — eliminarea duplicatelor structurale (Cartea, Capitolul, §)

- Backup separat înainte de scriere: `C:\Users\harab\wiki-backups\wiki-2026-09-04-pre-dedup-structural` (995 fișiere, 674.070.440 octeți, verificat identic).
- Aceeași regulă de potrivire exactă folosită pentru titlurile de articol, aplicată celor trei niveluri structurale a căror linie-sursă era o copie a ancorei: **170 de linii eliminate** — `Cartea` (5), `Capitolul` (109), `§` (56). Corpul a scăzut de la 14.353 la 14.183 de linii; fișierul de la 2.197.134 la 2.194.047 de octeți.
- **Reparație descoperită în timpul lucrului: 5 ancore `§` erau trunchiate.** Prima trecere de ancorare a luat linia `§` ca atare, dar PDF-ul rupsese titlul paragrafului pe două linii, deci ancora păstra doar prima parte, în timp ce corpul, după reunire, avea titlul întreg. Ancorele au fost **completate din linia de corp** înainte ca aceasta să fie ștearsă — nu s-a pierdut text, iar ancorele nu mai sub-raportează titlul. Exemplu: `§ 3. Ocrotirea intereselor personale` → `§ 3. Ocrotirea intereselor personale nepatrimoniale`. Este un defect al jobului 1, pe care reunirea liniilor l-a scos la iveală.
- **Trei niveluri nu au fost atinse**, fiindcă ancora lor nu este o copie a liniei de dedesubt și ștergerea ar fi pierdut text: `Titlul` (22) — ancora normalizează `T i t l u l I` la `Titlul I`, deci forma cu spațiere din PDF există doar în corp; `Secțiunea` (172) și `Subsecțiunea` (17) — ancora unește marcajul cu titlul, corpul le ține pe linii separate.
- Rămâne **un singur duplicat exact**: `### Secțiunea a 3-a- abrogată`, care nu are titlu, deci ancora coincide cu linia-sursă. Nefiind în cererea formulată, nu a fost atins.
- Verificări: reconstrucția față de starea imediat anterioară diferă exact în cele 5 ancore completate și în nimic altceva — toate liniile de corp se recuperează. `verify_chain.py`, extins să desfacă și această trecere, trece în continuare față de extracția originală: **1.859.072 de octeți ne-spațiu, sha256 `124bd2b606868231835c0a85b614f72196c717467df9ba40d78c50c9ece3504d`, identic**.
- `verify_chain.py` reinserează textul ancorei doar pentru cele patru tipuri deduplicate (`Articolul`, `Cartea`, `Capitolul`, `§`). `Titlul`, `Secțiunea` și `Subsecțiunea` sunt excluse explicit: ancora lor diferă de linia-sursă, iar reinserarea ar fabrica o linie care nu a existat niciodată.
- Frontmatter: `sha256` mutat în `sha256_pre_dedup_structural` (`fa97b7ce…`), `sha256` nou `2aca75a9…`. Lanțul complet: `source_file_sha256` → `sha256_pre_anchoring` → `sha256_pre_unwrap` → `sha256_pre_dedup` → `sha256_pre_dedup_structural` → `sha256`.
- Bilanț după cele patru treceri asupra Codului civil: **3.038 de ancore intacte**, corpul de la 31.785 la 14.183 de linii, fișierul de la 2,19 MB la 2,19 MB (a crescut cu ancorele, apoi a scăzut la loc cu deduplicarea).
- Scripturi: `_meta/imports/anchoring/dedup_structural.py`; `verify_chain.py` actualizat.

## [2026-09-04] lint | CNPF legal/acquis complete lint

- Scope: 67 active pages and 46 raw CNPF files.
- Report: `_meta/lint/cnpf-legal-lint-2026-09-04.md`.
- JSON audit: `_meta/lint/cnpf-legal-lint-2026-09-04.json`.
- Severity counts: high=0, medium=1090, low=47.
- Technical graph/frontmatter summary: broken wikilinks=0, invalid tags=1, missing index entries=0, raw SHA drift=0.

## [2026-09-04] ingerare | L-135/2007 și L-220/2007, cu exponenții rezolvați la sursă

- Ingerate `L-135-2007` (doc_id 153674, consolidare 2026-03-27) și `L-220-2007` (doc_id 155438,
  consolidare 2026-07-23) în `raw/papers/moldova-legal/`. Plasare deliberată în afara folderului
  `cnpf/`: sînt drept societar general, nu perimetru CNPF/BNM.
- Script nou `_meta/imports/moldova-legal/ingest_business_law.py`, cu verificare separată
  `verify_business_law.py`. Convențiile de format sînt cele din scriptul CNPF. Diferența de fond:
  `resolve_superscripts()` rezolvă `<sup>N</sup>` în `^N` **înainte** de extracție, fiindcă
  `text_content()` lipește cifrele și transformă „Articolul 27¹" în „Articolul 271".
- Decizia lui Eugen: forma `^N` peste tot, în toate cele patru roluri (titluri de articol, numere
  de alineat, litere de punct, trimiteri la capitole). Costul asumat: celelalte fișiere raw au
  încă exponenții de alineat aplatizați, deci aceste două fișiere sînt corecte dar diferite de
  restul corpusului. Exponenți păstrați în corp: 17 în L-135-2007, 60 în L-220-2007.
- Dovada că textul nu a fost atins: se scot prefixele `##`/`###` adăugate și se compară restul,
  linie cu linie, cu extracția simplă din același HTML. 667 din 667 și 532 din 532, identice.
  Ancorele de exponent coincid cu marcajul din sursă, 10 din 10 și 6 din 6. Fără duplicate.
- Două constatări `[de verificat]` la L-220-2007, ambele **în sursa legis.md**, verificate direct
  în HTML, nu introduse de extracție: art. 6 lipsește, deși actul are 25 de alte mențiuni
  „abrogat" și niciuna pentru el; art. 5 începe la alin. (2), alineatul (1) nu apare. Aceeași
  clasă cu art. 21 din L-192-1998. L-135-2007 nu are lacune: 1–83 complet.
- Corectată secțiunea C.3 din manifestul moldova-legal, care afirma că exponenții din L-100-2017
  se sprijină „exclusiv pozițional". HTML-ul doc_id 144467 îi marchează `<sup>`, deci sînt
  confirmați din marcaj. Aceeași corecție ca în `CLAUDE.md`.
- Curățat un defect latent introdus mai devreme azi: cele două legi fuseseră adăugate în `DOCS`
  din scriptul CNPF, care scrie în `raw/papers/cnpf/`. O rulare completă le-ar fi scris în
  folderul greșit. Intrările au fost scoase și înlocuite cu o notă care trimite la scriptul nou.
  `DOCS` revine la cele 14 acte ale perimetrului.
- Pagini noi: `entities/L-135-2007.md` și `entities/L-220-2007.md`, cu intrări în `index.md`
  (total 67). Manifest: secțiunea E, cu metoda, dovada de integritate și constatările.
- Acoperirea personei P1 trece de la două din cinci surse la **patru din cinci**. Rămîne Legea
  845/1992. Pasul fiscal al metodei P1 rămîne neancorat, Codul fiscal lipsind în continuare.

## [2026-09-04] dedup | Codul civil — ultimul duplicat exact (`Secțiunea a 3-a- abrogată`)

- Backup separat: `C:\Users\harab\wiki-backups\wiki-2026-09-04-pre-dedup-sectiune` (1.001 fișiere, 676.307.620 octeți, verificat identic).
- O singură linie eliminată: `Secțiunea a 3-a- abrogată`. Este singura secțiune fără titlu propriu, deci singura al cărei ancoră coincidea exact cu linia-sursă; toate celelalte ancore `Secțiunea`/`Subsecțiunea` unesc marcajul cu titlul și nu sunt copii ale liniei de dedesubt. Corpul: 14.183 → 14.182 de linii. **Nu mai există niciun duplicat exact în fișier.**
- `dedup_structural.py` a fost extins cu tipurile `Secțiunea` și `Subsecțiunea`. Testul de potrivire exactă nu se declanșează pentru cele cu titlu, deci rularea a atins exact o linie, cu 358 de ancore lăsate corect neatinse.
- **Două defecte de metodă găsite și reparate în această trecere:**
  - `verify_chain.py` excludea `Secțiunea` din reinserare, deci după ștergere lanțul ar fi picat. Regula a fost generalizată: prezența copiei se testează pe **marcaj** (partea ancorei până la primul `. `), nu pe textul întreg al ancorei — fiindcă o ancoră poate purta un titlu pe care linia-sursă nu îl are. `Titlul` rămâne singura excludere explicită, ancora lui fiind o normalizare, nu o copie. Regresie verificată pe fișierul nemodificat înainte de ștergere: trece.
  - A doua rulare a `dedup_structural.py` ar fi scris din nou cheia `sha256_pre_dedup_structural`, producând **chei YAML duplicate**; loaderul păstrează doar ultima valoare, deci veriga `fa97b7ce…` ar fi dispărut tăcut din lanțul de proveniență. Scriptul are acum o aserțiune care refuză o etapă deja folosită și cere `--stage`; rularea a folosit `--stage dedup_sectiune`. Verificat: zero chei duplicate în frontmatter.
- Lanț de proveniență complet, șase verigi: `source_file_sha256` → `sha256_pre_anchoring` → `sha256_pre_unwrap` → `sha256_pre_dedup` → `sha256_pre_dedup_structural` → `sha256_pre_dedup_sectiune` → `sha256` (`283119f8…`).
- `verify_chain.py` trece în continuare față de extracția originală: **1.859.072 de octeți ne-spațiu, sha256 `124bd2b606868231835c0a85b614f72196c717467df9ba40d78c50c9ece3504d`, identic**.
- Stare finală a Codului civil: **3.038 de ancore intacte** (2.657 articole + 381 structurale), corpul de la 31.785 la 14.182 de linii, zero duplicate.

## [2026-09-04] lint | CNPF legal/acquis complete lint

- Scope: 67 active pages and 46 raw CNPF files.
- Report: `_meta/lint/cnpf-legal-lint-2026-09-04.md`.
- JSON audit: `_meta/lint/cnpf-legal-lint-2026-09-04.json`.
- Severity counts: high=3, medium=1088, low=47.
- Technical graph/frontmatter summary: broken wikilinks=0, invalid tags=1, missing index entries=0, raw SHA drift=3.

## [2026-09-04] reîmprospătare | Cele trei consolidări expirate, cu o capcană nouă descoperită

- Reîmprospătate `L-308-2017` (110418 → 155856, 2018-12-01 → **2026-08-13**), `L-92-2022`
  (134551 → 151081, 2023-01-01 → **2026-06-25**) și `L-171-2012` (121985 → 156016, 2021-01-01 →
  **2027-06-01**). Script: `_meta/imports/cnpf/refresh_consolidations.py`.
- Versiunile anterioare arhivate integral în
  `_archive/raw/cnpf-legis-md-before-refresh-20260904-162713/`, verificate identice cu copia de
  siguranță dinaintea operațiunii. Frontmatterul fiecărui fișier poartă lanțul: `doc_id_previous`,
  `consolidation_date_previous`, `sha256_previous`, `ingested_previous`, `archived_previous_at`.
- Integritatea textului dovedită pentru toate trei prin aceeași metodă ca la ingerarea din
  moldova-legal: 923, 1914 și 2306 de linii, identice cu extracția simplă din același HTML.
- **Capcană nouă, mai rea decât vechimea pe care a înlocuit-o.** `L-171-2012` este acum o
  consolidare **viitoare**: data 2027-06-01 este ulterioară zilei de azi. Art. 38 (adecvarea
  capitalului societăților de investiții) și art. 141^1 (supravegherea prudențială a acestora)
  apar abrogate prin LP162 din 30.07.26, dar abrogarea produce efecte abia la 01.06.2027, deci
  **astăzi ambele sînt încă în vigoare**. Fișierul poartă avertisment în antet și
  `consolidation_is_future: true` în frontmatter; scriptul detectează singur situația, deci se va
  repeta corect la viitoarele acte.
- **Constatare de metodă: legis.md marchează exponenții în două feluri.** Pe lângă `<sup>N</sup>`,
  consolidarea curentă a L-171-2012 folosește un span ridicat prin CSS
  (`position: relative; top: -0.5em`, cu `vertical-align: baseline`). Prima rulare a produs
  `Articolul 471` în loc de `47^1`, adică o citare falsă. `resolve_superscripts()` tratează acum
  ambele forme. Fișierele au fost restaurate din copia de siguranță și operațiunea reluată de la
  zero, ca arhiva să conțină originalele, nu versiunea intermediară greșită. Verificat că sursele
  L-135-2007 și L-220-2007 nu folosesc forma CSS, deci ingerarea lor nu este afectată.
- Delta la nivel de articol: L-308-2017 capătă 10 articole cu exponent care lipseau complet
  (5^1, 5^2, 8^1, 8^2, 13^1, 23^1–23^4, 30^1); L-92-2022 capătă 89^1; L-171-2012 trece de la 8 la
  18 exponenți, capătă art. 80 cu marcaj de abrogare și pierde art. 38 și 141^1, ambele cu marcaj.
  Toate dispariițiile sînt abrogări consemnate în text, niciuna nu este pierdere de extracție.
- Rezolvată parțial constatarea 5 din `CLAUDE.md`: art. 80 exista în sursa curentă, deci absența
  lui era vechime, nu gol inexplicabil. Art. 81–88 rămân neexplicate.
- Actualizate paginile `entities/L-308-2017.md`, `entities/L-92-2022.md` și
  `entities/L-171-2012.md`. Pentru ultima, blocajul „LP177/2025 ținut ca raw separat, neintegrat"
  s-a rezolvat: art. 4^1 este acum în textul de bază. Manifest CNPF: secțiunile H.3 și H.4.
- Copie de siguranță dinaintea operațiunii:
  `wiki-backups\wiki-2026-09-04-pre-refresh-consolidations`, 1001 de fișiere, confirmată.

## [2026-09-04] repair | Deriva sha256 la L-171-2012, L-308-2017 și L-92-2022

- Constatare: lintul a semnalat `raw_sha_drift`=3, `high`=3 — primele constatări high din ziua respectivă. Cele trei fișiere fuseseră reîmprospătate din legis.md în paralel, cu doc_id-uri noi (156016, 155856, 151081), dar `sha256` din frontmatter nu corespundea corpului sub nicio convenție.
- **Corpul a fost validat înainte de a recalcula hash-ul.** Recalcularea unui hash certifică un corp, deci întâi am verificat că textul este fidel sursei păstrate: ancorele din `.md` s-au comparat cu titlurile de articol din HTML-ul stocat la `_meta/imports/cnpf/legis-md-consolidated/showdetails-<doc_id>.html`. L-308-2017 (47/47) și L-92-2022 (125/125) coincid exact. La L-171-2012, 155 din 156 coincid; singura diferență, `47^1`, este în HTML sub forma unui exponent stilizat CSS (`top: -0.5em`), nu `<sup>` — deci lipsa era în regexul meu de validare, nu în extracție. Zero articole prezente în HTML și neancorate, la toate trei.
- Corectate doar valorile `sha256`; corpurile nu au fost atinse — verificat: 423.534 / 188.065 / 384.787 de octeți, neschimbate. Valorile înlocuite, pentru audit: L-171-2012 `e4050169…`, L-308-2017 `9d49b831…`, L-92-2022 `6500f04f…`. Cele noi: `d2fe290c…`, `c656b191…`, `149b528b…`, calculate pe corpul de după `---` cu CRLF→LF (fișierele au zero CRLF, deci ambele convenții coincid).
- **Scriere protejată împotriva coliziunii.** Fișierele erau rescrise de o sesiune paralelă chiar în acel interval — de două ori în patru minute, iar hash-ul consemnat la L-171-2012 s-a schimbat între două verificări ale mele. Am confirmat întâi că scrierile s-au oprit (hash și mtime identice peste un interval), apoi am folosit `--expect <hash-ul întregului fișier>`, care refuză scrierea dacă fișierul s-a schimbat față de starea inspectată. Prima încercare a fost **refuzată** din cauza unui `\r` rămas la citirea din shell — garda a eșuat închis, corect; după corectarea comparației, cele trei scrieri au trecut și s-au auto-verificat.
- Lint după reparație: `high`=0, `raw_sha_drift`=0.
- Script: `_meta/imports/anchoring/fix_sha_drift.py` — recalculează doar, refuză să ruleze fără `--apply`, și nu presupune niciodată că un corp este corect: validarea corpului rămâne în sarcina celui care rulează.

## [2026-09-04] repair | Deriva sha256 la L-135-2007 și L-220-2007

- Aceleași două fișiere ingerate în paralel pentru dreptul afacerilor prezentau aceeași derivă: `sha256` din frontmatter nu corespundea corpului sub nicio convenție. Nu apar în lintul CNPF, care acoperă doar `raw/papers/cnpf/`.
- **Corpurile validate întâi**, față de HTML-ul păstrat la `_meta/imports/moldova-legal/legis-md-business/`. Verificarea a fost extinsă să recunoască **ambele** forme de exponent din markup-ul legis.md — `<sup>N</sup>` și varianta stilizată CSS (`vertical-align` / `top: -0.5em`) — după ce prima formă singură produsese un fals pozitiv la L-171-2012 art. 47^1.
  - `L-135-2007` (doc_id 153674): 93 de ancore, 10 cu exponent — coincid exact cu HTML-ul, 0 în plus, 0 lipsă, numerotare strict crescătoare.
  - `L-220-2007` (doc_id 155438): 44 de ancore, 6 cu exponent — la fel, coincidență exactă.
  - Ambele au `extract_method: curl showdetails + rezolvare exponenti (sup -> ^N) + lxml text extraction`, deci exponenții sînt rezolvați la sursă, nu deduși ulterior.
- Corectate doar valorile `sha256`; corpurile neatinse (102.231 și 89.211 de octeți, neschimbate). Înlocuite: `f1fd8917…` → `8035489e…` și `29085c5d…` → `b315fe17…`. Scriere protejată cu `--expect`, auto-verificată după scriere.
- **Stare corpus după reparație: 365 de fișiere consistente, 12 cu derivă, 8 fără hash.** Cele 12 rămase sînt toate în `raw/papers/mded-policy-2024/` și sînt constatările high cunoscute din auditul de la 2026-07-12, pentru care s-a decis atunci explicit să nu se aplice remediere. Nu au fost atinse. Pentru ele nu există o sursă independentă de validare comparabilă cu HTML-ul legis.md; validarea ar trebui făcută față de fișierele originale păstrate în `raw/papers/mded-policy-2024/original/`.
- Copie nouă `wiki-backups\wiki-2026-09-04-post-refresh`, 1011 de fișiere, 681.633.433 octeți,
  confirmată prin `diff -rq` recursiv: identică octet cu octet, fără nicio diferență.
  Prima încercare a prins două fișiere în timpul scrierii, `L-135-2007` și `L-220-2007`, fiindcă
  celălalt fir le corecta `sha256` chiar atunci; lungimea fiind aceeași, totalurile coincideau și
  numai comparația pe conținut a arătat problema. Copia a fost resincronizată și reverificată.
- Defect propriu, găsit prin corecția celuilalt fir: ambele scripturi de ingerare calculau
  `sha256` pe `body_text`, înainte de asamblarea finală, în timp ce convenția corpusului
  (`lib_anchor.sha_variants`) îl calculează pe octeții corpului de după fence-ul de frontmatter,
  inclusiv linia goală. La `refresh_consolidations.py` diferența era agravată de inserarea
  lanțului de proveniență și a avertismentului după calcul. Corectate ambele scripturi; verificat
  că regenerarea din HTML-ul arhivat reproduce exact valorile corectate, fără a atinge fișierele.
- Șterse șase copii intermediare ale zilei: `post-rejoin-doc-ids`, `pre-unwrap`, `pre-dedup`,
  `pre-dedup-structural`, `pre-dedup-sectiune`, `pre-refresh-consolidations`. Eliberat 3,76 GB.
  Verificat înainte de ștergere că niciuna nu conținea ceva nerecuperabil: niciun fișier absent
  din `post-refresh`, iar starea Codului civil din fiecare este identică octet cu octet cu o copie
  de lucru păstrată în `_meta/anchoring-work/` (`CC-1107-2002.md`, `-unwrapped`, `-dedup`,
  `-dedup-struct`). Versiunile dinaintea reîmprospătării pentru L-308-2017, L-92-2022 și
  L-171-2012 sînt păstrate în `_archive/raw/cnpf-legis-md-before-refresh-20260904-162713/`.
- Rămân `wiki-2026-09-04-pre-anchoring`, starea de dinaintea lucrului de azi, și
  `wiki-2026-09-04-post-refresh`. Nu a fost atinsă `wiki-2026-09-04-pre-mded-sha-fix`, creată de
  celălalt fir în timpul operațiunii.

## [2026-09-04] repair | Deriva sha256 la cele 12 fișiere mded-policy-2024, validate din originale

- Backup: `C:\Users\harab\wiki-backups\wiki-2026-09-04-pre-mded-sha-fix` (1.012 fișiere, 681.639.771 octeți, verificat identic).
- Aceste 12 fișiere sînt constatările high din auditul de la 2026-07-12, pentru care s-a decis atunci să nu se aplice remediere. Lintul CNPF nu le acoperă, deci deriva a rămas invizibilă în rapoartele curente.
- **Diagnostic, înainte de orice scriere. Nu a fost derivă, ci un hash greșit de la bun început.** Corpurile sînt identice octet cu octet cu copiile din backupul `wiki-before-bnm-corpus-ingest-20260712-205717`, luat la ~8 ore după ingestie, iar `sha256` era deja greșit acolo. Deci nimic nu a modificat textul după ingestie; scriptul de ingest a calculat valoarea eronat. Aceasta este o constatare diferită de „derivă" și schimbă profilul de risc: recalcularea certifică un corp deja dovedit neatins.
- **Validare față de originale**, cum s-a cerut, în trei trepte:
  1. **Originalele sînt intacte.** Toate cele 12 fișiere păstrate în `raw/papers/mded-policy-2024/original/` se potrivesc cu `source_file_sha256` din frontmatter. Ancora reală de proveniență ține.
  2. **Corpurile nu au fost atinse de la ingestie** (comparație octet cu octet cu backupul din 12 iulie).
  3. **Cuvintele corpurilor sînt cele ale originalelor.** Textul a fost re-extras aici și comparat ca multiset de tokenuri, nu linie cu linie, fiindcă o altă versiune de bibliotecă diferă legitim la spații, despărțire în silabe și ordine de citire. Acoperire: **11 fișiere la 100,0%**, unul la **99,9%**.
- Metode de re-extragere: PDF prin PyMuPDF (8 fișiere), DOCX prin python-docx (1), PPTX prin citirea directă a rulărilor de text din arhiva OOXML (3) — `python-pptx` nu este instalat aici.
- Prima rulare a validării a dat 84,4% și 92,2% la două prezentări. Cauza era în validatorul meu, nu în corpuri: citeam și `notesSlides`. Restrâns la `ppt/slides/slideN.xml`, ambele urcă la **100,0%**. Consemnat în script, ca să nu se repete diagnosticul.
- Restul de 0,1% la `bilateral-screening-economic-criteria-2024.md`: 19 tokenuri din 16.753 („expenditures", „npb", „dynamics", „the2024", „9th"), etichete de grafic pe care python-docx le citește altfel. Corpul are 31.709 tokenuri față de 16.753 în re-extragerea mea, deci este mai bogat, nu mai sărac. Diferență între unelte, nu pierdere de conținut.
- Corectate doar valorile `sha256`; corpurile neatinse — verificat: toate 12 identice cu backupul de dinaintea reparației. Scrieri protejate cu `--expect`, fiecare auto-verificată.
- **Stare finală a stratului raw: 377 de fișiere cu `sha256` consistent, 0 cu derivă.** Cele 8 fără hash sînt manifeste, inventare și README-uri, care nu au frontmatter fiindcă nu sînt surse.
- **De raportat, neatins:** extragerile PPTX **nu conțin notele vorbitorului**. Este o alegere de ingestie defensabilă pentru un set de slide-uri, dar notele pot purta conținut de fond. Cele trei prezentări afectate: `economic-criteria-deregulation-2024`, `economic-criteria-soe-privatisation-2024`, `economic-criteria-state-aid-2024`.
- Scripturi: `_meta/imports/anchoring/{validate_mded_extractions,fix_sha_drift}.py`.

## [2026-09-04] enrich | Note ale vorbitorului adăugate la extragerile PPTX

- Backup: `C:\Users\harab\wiki-backups\wiki-2026-09-04-pre-speaker-notes` (1.012 fișiere, 681.644.200 octeți, verificat identic).
- Ingestia din 2026-07-12 a citit doar textul de pe slide-uri, deci ce a spus prezentatorul alături nu a intrat niciodată în wiki. Constatare ridicată la validarea extragerilor mded și acum rezolvată.
- **Doar două din cele trei prezentări au note reale.** PowerPoint scrie o parte `notesSlide` pentru fiecare slide, indiferent dacă s-a tastat ceva în ea, deci prezența părții nu înseamnă nimic în sine. `economic-criteria-soe-privatisation-2024` are zece panouri de note, toate goale — nemodificat.
- Adăugate:
  - `economic-criteria-deregulation-2024` — notele la slide-ul 2, 1.281 de caractere: misiunea Consiliului Economic și a Grupului de lucru pentru reglementarea activității de întreprinzător, cu trimiteri la Legile 235/2006, 160/2011, 161/2011 și 131/2012.
  - `economic-criteria-state-aid-2024` — notele la slide-ul 3, 567 de caractere. **Conținut de fond, nu decorativ:** nota spune că sumele ajutorului de stat pentru 2020–2022 **nu includ** ajutorul pentru SIEG, ajutorul pentru daune din calamități și măsurile aflate în examinare la Consiliul Concurenței, în timp ce cifra pentru 2019 **le include**. Slide-ul prezintă seria 2019–2022 ca pondere în PIB, între 0,38% și 0,57%. Fără notă, seria pare comparabilă și nu este.
- Notele sînt adăugate sub un titlu propriu, `## Speaker notes`, și **nu** sînt contopite cu textul slide-urilor: cititorul trebuie să poată distinge ce s-a arătat de ce s-a spus. Textul din notă este preluat verbatim, inclusiv repetiția „under under" din sursă — nu corectez textul sursei.
- Verificări: textul slide-urilor este **prefix exact, octet cu octet**, al noului corp la ambele fișiere (6.657 și 6.241 de octeți, neschimbate); textul notelor coincide exact cu cel din `ppt/notesSlides/notesSlideN.xml` din originalul arhivat; `sha256` recalculat și auto-verificat după scriere.
- Frontmatter: `sha256` mutat în `sha256_pre_speaker_notes`, plus `speaker_notes_added` și `speaker_notes_convention`. `source_file_sha256` neatins — originalele nu s-au schimbat și rămân ancora de proveniență.
- `validate_mded_extractions.py` va raporta de acum `CHANGED` la aceste două fișiere, ceea ce este **așteptat**; consemnat în script, ca să nu fie citit drept alarmă. `CHANGED` la oricare alt fișier rămâne o constatare reală.
- Stare corpus: 378 de fișiere cu `sha256` consistent, 0 cu derivă.
- Script: `_meta/imports/anchoring/add_pptx_speaker_notes.py` — sare peste panourile goale, refuză să adauge de două ori, nu atinge textul slide-urilor.

## [2026-09-04] ingerare | L-845/1992, ultima sursă P1 care lipsea

- Găsit `doc_id` **155963** prin căutarea documentată în nota de lacună, apoi ingerat
  `L-845-1992` în `raw/papers/moldova-legal/`: 35 de articole de bază, 11 cu exponent, 9 capitole.
  Integritatea textului dovedită pe 447 de linii, identice cu extracția simplă din același HTML.
  Rulat cu filtru pe nume de act, ca să nu rescrie fișierele existente fără motiv.
- Verificat înainte de ingerare că actul, deși din 1992, folosește forma modernă „Articolul N",
  nu forma veche „Art.N. –" care blocase ancorarea la L-192-1998. 28 de etichete `<sup>`, niciun
  exponent prin CSS.
- **Acoperirea personei P1 este completă: cinci din cinci surse.** Rămân absente Codul fiscal
  1163/1997, Codul administrativ 116/2018 și celelalte opt coduri, deci pasul fiscal al metodei P1
  rămâne neancorat.
- **A doua consolidare viitoare din corpus.** Data este 2027-01-01, ulterioară zilei de azi. O
  singură dispoziție afectată: art. 36^1 pct. 4 lit. l), introdusă prin LP171 din 30.07.26, în
  vigoare 01.01.2027. Detectarea a fost mutată din scriptul de reîmprospătare în calea comună de
  ingerare, ca funcție `future_pending()`, fiindcă prima rulare a produs fișierul fără avertisment.
  Acum orice ingerare viitoare marchează singură situația, în antet și în frontmatter.
- **Constatare `[de verificat]`:** arts. 21 și 31 lipsesc fără niciun temei în sursă. Verificat
  direct în HTML: nu apar nicăieri, iar textul art. 20 curge în art. 22. Actul distinge cele două
  situații, fiindcă pentru arts. 35 și 36 păstrează marcajul `- abrogat.`. Aceeași clasă cu art. 21
  din L-192-1998 și art. 6 din L-220-2007.
- Structură neobișnuită, de reținut la citare: două capitole cu exponent, VI^1 și VI^2, și un bloc
  de opt articole, 36^1–36^8, care sînt două regimuri întregi adăugate ulterior, antreprenoriatul
  social și monopolul fiscal. Aplatizate, ar fi apărut ca „art. 368" într-un act cu 37 de articole.
- Consemnat, cu temei, că [[HG-841-2024]] pct. 63 prevede rescrierea integrală a legii „în redacție
  nouă", deci această consolidare poate deveni rapid depășită.
- Pagină nouă `entities/L-845-1992.md`, intrare în `index.md` (total 68), manifest secțiunile E și
  E.4. Copie de siguranță dinaintea operațiunii: `wiki-backups\wiki-2026-09-04-pre-ingest-845`,
  1012 fișiere, confirmată identică.

## [2026-09-04] lint | CNPF legal/acquis complete lint

- Scope: 68 active pages and 46 raw CNPF files.
- Report: `_meta/lint/cnpf-legal-lint-2026-09-04.md`.
- JSON audit: `_meta/lint/cnpf-legal-lint-2026-09-04.json`.
- Severity counts: high=0, medium=1095, low=48.
- Technical graph/frontmatter summary: broken wikilinks=0, invalid tags=1, missing index entries=0, raw SHA drift=0.

## [2026-09-04] refresh | Reîmprospătarea celor 12 consolidări expirate rămase

- Backup: `C:\Users\harab\wiki-backups\wiki-2026-09-04-pre-stale-refresh` (1.019 fișiere, 681.972.999 octeți, verificat identic). Versiunile înlocuite sînt arhivate integral la `_archive/raw/{cnpf,moldova-legal}-legis-md-before-refresh-20260904-183240/`.
- **Descoperirea `doc_id`-urilor curente, automatizată.** Căutarea legis.md este un shell JS, iar `getResults` doar învelește `showdetails`, deci niciunul nu arată o versiune mai nouă. Însă **lista completă de versiuni este deja în pagina `showdetails`** — `showversions()` din JS-ul sitului doar o arată și o ascunde client-side — iar intrarea marcată `ultima` este consolidarea curentă. O cerere per act, fără căutare și fără sondarea intervalelor de id. Script: `_meta/imports/cnpf/discover_current_doc_ids.py`.
- Reîmprospătate 12 acte, refolosind `refresh_consolidations.py` al celuilalt fir (arhivează, păstrează lanțul de proveniență, rezolvă exponenții la sursă, calculează delta la nivel de articol, avertizează la consolidări viitoare, recalculează `sha256` după asamblare). Driver: `_meta/imports/cnpf/refresh_stale_batch.py`.
- Delte la nivel de articol: `L-1134-1997` +23^1, 71^1, 72^1, 73^1–73^4; `L-192-1998` +8^1, 8^2, 21; `L-181-2023` +28^1; `L-100-2017` +33. Restul: text actualizat, set de articole neschimbat.
- **`L-1134-1997` este datată 2028-01-01, în viitor față de astăzi.** Fișierul conține modificări care **nu sînt încă în vigoare**; poartă `consolidation_is_future: true` și un bloc de avertisment în text, cu cele 2 dispoziții afectate. Aceeași situație ca `L-171-2012` (2027-06-01), deci convenția casei este respectată.
- **Două acte nu au fost reîmprospătate, motivat:** `L-178-2020` — legis.md nu listează altă versiune; `HG-1171-2018` — cea mai recentă versiune este datată 2024-07-05, exact data ținută, deci deținem alt `doc_id` al aceleiași consolidări.
- **Constatări închise:** `L-192-1998` art. 21 apare explicit ca `Art.21. – abrogat.` — absența din versiunea 2021 era vechime, nu lacună inexplicabilă (constatarea 2 din nota de stare). `L-100-2017` art. 33 există; rămân absente 25, 26, 52.
- **Regresie prinsă în cursul operațiunii.** Reîmprospătarea a rescris `L-192-1998` cu text nou dar **fără ancore**, fiindcă pipeline-ul legis.md ancorează doar forma `Articolul N.`, iar acest act folosește forma pre-2000 `Art.N. – `. Fișierul a ajuns momentan la `articole detectate: 0` — exact defectul reparat la jobul 2. Re-ancorat cu `anchor_artdash.py`. **Regulă: reîmprospătarea oricărui act în formă pre-2000 trebuie urmată de re-ancorare.**
- **Defect în scriptul propriu, prins și reparat.** La re-ancorare, `anchor_artdash.py` a inserat 31 de ancore în loc de 34: expresia se oprea la cifre și rata liniile `Art. 8^1. – `, `Art. 8^2. – ` și `Art. 13^1. – `, unde exponentul este deja rezolvat la sursă. Trei articole ar fi rămas necitabile — exact clasa de defect pe care o repară jobul 3. Corectat, comentat în script, re-verificat: 34/34 ancore, strip-and-compare identic octet cu octet, ordine strict crescătoare.
- Verificări finale: toate cele 12 fișiere au `sha256` consistent; `raw_sha_drift`=0; `article_anchor_missing_target`=0, deci nicio citare din wiki nu a rămas suspendată în urma schimbării seturilor de articole; `broken_wikilinks`=0; `high`=0.
- `stale_consolidation` în lint: 14 → 8. Cele 8 rămase nu mai sînt semnalări de vechime, ci de neconcordanță pagină-sursă (pagina menționează un an ulterior datei consolidării).

## [2026-09-04] lint | CNPF legal/acquis complete lint

- Scope: 70 active pages and 46 raw CNPF files.
- Report: `_meta/lint/cnpf-legal-lint-2026-09-04.md`.
- JSON audit: `_meta/lint/cnpf-legal-lint-2026-09-04.json`.
- Severity counts: high=0, medium=1109, low=50.
- Technical graph/frontmatter summary: broken wikilinks=0, invalid tags=1, missing index entries=2, raw SHA drift=0.

## [2026-09-04] ingerare | Codul fiscal și Codul administrativ

- Ingerate `COD-1163-1997` (doc_id 155071, consolidare 2026-06-25, **512 ancore de articol**:
  353 de bază plus 159 cu exponent, 11 titluri) și `COD-116-2018` (doc_id 150447, consolidare
  2025-08-31, 260 de ancore, numerotare 1–258 completă). Integritate dovedită pe 6.916 și 1.447
  de linii, identice cu extracția simplă din același HTML. Niciuna nu este consolidare viitoare.
- **Problema de fond a Codului fiscal: cuprinsul.** Actul poartă un `C U P R I N S` de circa 780
  de linii care repetă fiecare titlu de articol înaintea corpului. Ancorat, ar fi produs circa 350
  de ancore duplicate, iar o citare `art. N` ar fi devenit ambiguă. Regula adoptată: cuprinsul
  **nu se șterge**, textul rămâne neatins, dar ancorarea este suprimată între marcajul `CUPRINS` și
  formula `Parlamentul adoptă prezentul cod.`. Se aplică doar când ambele repere există, în această
  ordine, deci nu atinge actele fără cuprins. Verificat că fiecare ancoră din fișier este unică.
- Verificat înainte de ingerare că numerotarea **nu repornește pe titluri**: în corp cele 353 de
  articole de bază sînt unice, iar titlurile încep la art. 1, 12, 93, 119, 129, 276, 288, 299, 335
  și 367. O citare `art. N` identifică deci un singur articol. Aparența inițială de 502 duplicate
  venea integral din cuprins și din exponenții încă nerezolvați.
- Adăugată ancorarea `TITLUL`, absentă până acum din scriptul de ingerare, și detectarea titlului
  oficial pentru acte care încep cu „COD Nr." nu „LEGE Nr.".
- **`art. 54^1/1` este un articol distinct de `art. 54^1`**, sursa scriindu-l
  `Articolul 54<sup>1</sup>/1`. Singurul caz din corpus cu bară după exponent. Prima verificare l-a
  raportat drept duplicat, fiindcă regexul de control se oprea la exponent; a fost corectat
  controlul, nu ancora.
- **Constatare `[de verificat]` la Codul fiscal:** 26 de articole absente, 208–213 și 315–334.
  Sînt explicate prin marcaje `Capitolul 10 - abrogat.` și `Capitolul 5` … `Capitolul 8 - abrogat.`,
  dar **fără citare LP**, deci actul de abrogare nu este identificat. Aceeași clasă cu blocul
  2047–2054 din Codul civil. Codul administrativ nu ridică nicio constatare.
- Consecință analitică: **pasul fiscal al metodei P1 este acum ancorat**, iar cadrul pentru
  contestarea actelor CNPF și BNM este prezent, deci constatările privind depășirea mandatului pot
  fi duse până la calea de atac.
- Pagini noi `entities/COD-1163-1997.md` și `entities/COD-116-2018.md`, intrări în `index.md`
  (total 70), manifest secțiunea F cu F.1–F.3. Copie de siguranță dinaintea operațiunii:
  `wiki-backups\wiki-2026-09-04-pre-ingest-coduri`, 1048 de fișiere, confirmată identică.
- Din cele 11 acte ale planului eșuat din 13 iulie 2026, patru sînt acum în wiki. Rămân șapte
  coduri.

## [2026-09-04] registru | Dispozitiile care nu sint inca in vigoare

- Motivul: consolidarea legis.md incorporeaza si modificarile cu intrare in vigoare amanata, deci un fisier curat ancorat, cu sha256 valid, poate arata ca abrogata o dispozitie care astazi se aplica. `L-171-2012` art. 38 si art. 141^1 sint cazul.
- Solutie aleasa: **registru generat** in `_meta/inforce/`, nu adnotare in `raw/`. Textul juridic nu este atins, deci nu este nevoie de lant de hash-uri sau de `verify_`. Optiunea de a insera marcaje in fisierele ancorate a fost evaluata si aminata: la 5 dispozitii, mecanismul ar costa mai mult decat rezultatul. Pragul de reevaluare: circa 20 de dispozitii in registru.
- Scris: `_meta/inforce/build_inforce_register.py`, `in-force-register.md`, `in-force-register.json`. Zero fisiere de drept modificate.
- Stare la 2026-09-04: **5 dispozitii in 3 acte**. `L-845-1992` art. 36^1 pct.4, lit.l) (introducere, 01.01.2027); `L-171-2012` art. 38 si art. 141^1 (abrogare, 01.06.2027); `L-1134-1997` art. 73^3 si art. 73^4 (introducere, 01.01.2028).
- Metoda: scanare dupa marcajul `in vigoare DD.MM.YY` in tot `raw/`, pastrand doar datele viitoare. Atribuirea la articol se face din referinta `Art.N` din interiorul notei, cu subdiviziune (`alin.`, `pct.`, `lit.`) acolo unde nota o poarta; altfel din ancora precedenta. Deduplicare pe dispozitie, nu pe aparitie, fiindca acelasi marcaj apare in frontmatter, in antet si in corp.
- Limita asumata: registrul semnaleaza, nu reconstruieste. Cind o consolidare viitoare **rescrie** un articol, textul in vigoare astazi lipseste cu totul din fisier si niciun marcaj nu il poate suplini. Pentru acest caz registrul indica arhiva consolidarii anterioare, cu avertismentul ca aceea poate fi ea insasi depasita: la `L-171-2012` arhiva este consolidarea 2021-01-01, mai slaba decat fisierul curent.
- Rulare: `python _meta/inforce/build_inforce_register.py`. `--check` iese 1 daca registrul este invechit, deci poate intra in lint. `--as-of YYYY-MM-DD` permite alta zi de referinta; verificat pe 2028-06-01 (registrul se goleste corect) si pe 2026-12-31 (cele 5 raman).
- Regula de citare adaugata in `CLAUDE.md`, sectiunea noua "The second check: is the article in force today". Fara ea registrul nu este consultat niciodata.
- De reluat dupa fiecare ingerare sau reimprospatare: `L-845-1992` si `L-1134-1997` au intrat azi purtand modificari amanate pe care nimic altceva nu le semnala.
- Copie de siguranta dinaintea operatiunii: `wiki-backups\wiki-2026-09-04-pre-inforce-rule`, 1057 de fisiere, 691.570.455 de octeti, confirmata identica.

## [2026-09-04] generator | Secțiunea de acoperire din CLAUDE.md, generată în loc de scrisă

- Motiv cauzal: secțiunea a fost scrisă de mână de trei ori în aceeași zi și a fost falsă în mai puțin de o oră de fiecare dată. Cauza nu este neatenția, ci structura: în folder scriu doi agenți, iar descrierea o actualizează doar unul. Aceeași derivă stricase și harta de cunoștințe (documentul 05) timp de două luni. Regula adoptată: tot ce este verificabil mecanic se generează, nu se tastează.
- Adăugat `_meta/coverage/build_coverage.py`. Citește fișierele din `raw/papers/`, nu metadatele scrise de om, și rescrie blocul dintre `<!-- COVERAGE:BEGIN -->` și `<!-- COVERAGE:END -->` din `CLAUDE.md`. Moduri: implicit scrie, `--stdout` afișează, `--check` iese cu 1 dacă fișierul este depășit.
- Ce raportează per act: articole declarate în frontmatter, ancore găsite efectiv, data consolidării, articole cu exponent normalizate, articole numerotate cu cifre romane, puncte numerotate pentru hotărâri.
- Semnalări mecanice: consolidare datată în viitor cu trimitere la registrul `_meta/inforce/`, consolidare mai veche de 2 ani (fără actele nemodificate niciodată, unde vechimea nu înseamnă nimic), nepotrivire între numărul declarat și ancore, text integral prezent dar neancorat, exponent aplatizat detectat pozițional (un număr care prelungește cifrele predecesorului, regula care a prins `1461` după `146`), și corpusul BNM în engleză neancorat.
- Verificat: rulare de două ori la rând produce fișier identic în afara marcajului de timp; `--check` confirmă „up to date"; secțiunile scrise de om au rămas neatinse.
- Starea la generare: 24 de acte moldovenești primare, 29 de extrase de acquis UE, 311 documente în corpusul BNM. Semnalări deschise: 3 acte cu consolidare în viitor (L-1134-1997, L-171-2012, L-845-1992) cu 5 dispoziții afectate; HG-1171-2018 la 2,2 ani vechime; trei linii de numărare depășite în corpul fișierelor (L-177-2025, L-178-2020, L-192-1998), cosmetice; 87 de fișiere BNM în engleză cu 3.556 de marcaje `Article N` neancorate.
- `CLAUDE.md` restructurat în jurul blocului generat. Secțiunea „Open questions that need Eugen's judgement" păstrează doar ce nu se poate decide mecanic: blocul 2047–2054 din Codul civil fără citare LP, aplatizarea exponentului sub nivel de articol în Codul civil (extras din PDF, deci în afara noii căi de extracție), și întrebarea de principiu dacă o traducere ar trebui vreodată să poarte ancoră.
- Închis ca rezolvat: art. 21 din L-192-1998 lipsea fără temei în sursă; consolidarea reîmprospătată îl conține. Consemnat în CLAUDE.md ca să nu fie reridicat.

## [2026-09-04] documente | Recopiate 03 si 05 din proiect, dupa rescrierea hartii de cunostinte

- `legal-career/05-knowledge-map.md` rescris in proiect si recopiat aici. Schimbarea de fond: un singur mod de esec (acoperire incompleta) devine trei, ordonate dupa cit de tacut esueaza. Unu, dispozitia lipseste din baza. Doi, este in baza dar textul e vechi: 21 din 23 de acte legis.md au consolidare sub doi ani, raman `L-178-2020` si `HG-1171-2018`. Trei, este in baza, curenta, ancorata si cu sha256 valid, si totusi nu este legea de astazi.
- Adaugat al patrulea strat in structura: **stratul de control** (`_meta/`) — lint, lantul de verificare a ancorarii, registrul in-force. Motivul: primele trei straturi pot fi gresite in tacere.
- Consemnat ca **cea mai mare necunoscuta a constructiei**: Codul civil nu are identitate de versiune. Fara `source_url`, fara `doc_id`, fara `consolidation_date`. Verificarea vechimii compara doc_id, verificarea in-force scaneaza marcajele legis.md; Codul civil este invizibil pentru amindoua. Nu a aparut in niciunul dintre cele doua audituri de azi nu fiindca e curat, ci fiindca nu poate fi masurat.
- Prioritatea de lucru schimbata: „termina ancorarea inainte de a extinde" este indeplinita si retrasa. Inlocuita cu: constringerea nu mai este extinderea, ci verificarea. Nicio ingerare fara controlul care o acopera, in aceeasi trecere.
- `legal-career/03-working-rules.md` recopiat cu sectiunea noua 4, „Is the provision in force today". Sectiunile 4-7 renumerotate 5-8; niciun document nu citeaza numere de sectiune, deci nimic nu s-a rupt. Nota locala despre diferenta fata de proiect pastrata neschimbata.
- Din copia lui 05 s-a scos avertismentul „auditul contrazice acest document in trei locuri". Toate trei sint rezolvate: Codul civil si `L-192-1998` sint ancorate, consolidarile expirate au fost reimprospatate. Inlocuit cu o nota care spune ca a fost scos si de ce. `CLAUDE.md` ramine sursa operationala si cistiga la orice divergenta de fapt.
- Copie de siguranta dinaintea operatiunii: `wiki-backups\wiki-2026-09-04-pre-doc-recopy`, 1058 de fisiere, 691.578.913 de octeti, confirmata identica.

## [2026-09-04] versiune | Codul civil primeste identitate de versiune, si rezultatul este invers decat se astepta

- Problema: `CC-1107-2002` nu avea `source_url`, `doc_id` sau `consolidation_date`. Provine dintr-un PDF consolidat furnizat, nu din legis.md, deci era invizibil atit pentru verificarea vechimii (care compara doc_id), cit si pentru registrul in-force (care scaneaza marcajele legis.md). Nu aparuse in niciunul dintre cele doua audituri de azi nu fiindca ar fi curat, ci fiindca nu putea fi masurat.
- `doc_id` gasit: **150561**, prin cautarea dupa numarul actului, aceeasi metoda folosita de scripturile de ingerare. HTML-ul a fost arhivat pentru audit la `_meta/imports/moldova-legal/legis-md-consolidated/showdetails-150561.html` (4.933.906 octeti, sha256 `4efc4153a803ea…`).
- **Constatarea centrala: legis.md este in urma, nu fisierul nostru.** Consolidarea de la doc_id 150561 este la 01.11.2025, ultima modificare aplicata fiind LP222 din 10.07.25. LP251 din 10.07.25, MO417-419/06.08.25 art.569, **in vigoare 01.04.26**, nu apare deloc acolo. Fisierul nostru o aplica. Data de azi fiind 04.09.2026, LP251 este in vigoare, deci textul din wiki este cel corect, iar consolidarea publicata de legis.md este cu cinci luni in urma pe acest punct.
- Dovada, pe inventarul de articole, comparatie pe text decodat cu `<sup>N</sup>` rezolvat in `^N` de ambele parti: legis.md 2663 de articole, fisierul nostru 2657. Prezente la legis.md si absente aici: exact sase, **2171, 2172, 2185, 2188, 2404, 2485**, adica exact cele abrogate prin LP251, fiecare cu marcaj propriu in fisierul nostru. Prezente aici si absente la legis.md: **niciunul**. Extractia nu a inventat si nu a pierdut articole.
- Limita dovezii: acopera inventarul de articole, nu redactarea fiecarui articol. LP251 a si reformulat texte (art. 509 al.(2), 2163, 2170, 2174), deci o comparatie la nivel de text ar arata diferente care sint corecte, nu erori. Separat, am confirmat o singura inregistrare a Codului civil prin cautarea dupa numar; nu am enumerat exhaustiv toate versiunile pe care le tine legis.md.
- **Pericol operational nou, invers celui asteptat.** O rulare a `refresh_consolidations.py` pe Codul civil cu doc_id 150561 ar da textul inapoi la 01.11.2025 si ar reintroduce cele sase articole abrogate. Mecanismul de reimprospatare presupune ca legis.md este intotdeauna sursa mai proaspata; pentru acest act nu este. Blocat in frontmatter prin `do_not_refresh_from_doc_id: true` si `legis_md_is_behind: true`.
- Scris **numai in frontmatter**. Corpul nu a fost atins: 2.190.956 de octeti, sha256 `283119f82209…`, identic inainte si dupa, iar valoarea `sha256` deja consemnata in frontmatter ramine valabila fara recalculare. Cele 3.038 de ancore sint intacte (2.657 de articole). Frontmatterul creste de la 3.636 la 4.855 de octeti, YAML valid, 38 de chei, fara duplicate.
- Registrul in-force regenerat dupa modificare. Codul civil nu intra in el: marcajele LP251 sint cu data trecuta, deci nu sint dispozitii amanate.
- Copie de siguranta dinaintea operatiunii: `wiki-backups\wiki-2026-09-04-pre-cc-version-identity`, 1058 de fisiere, confirmata identica.
- **De corectat in consecinta:** documentul 05 din proiect consemneaza Codul civil drept „cea mai mare necunoscuta a constructiei". Afirmatia nu mai este adevarata si trebuie rescrisa.

## [2026-09-04] documente | Documentul 05 corectat dupa rezolvarea identitatii de versiune a Codului civil

- Sectiunea „The one file no control reaches" inlocuita cu „The file that was unmeasurable, and now is not". Motivul: documentul consemna Codul civil drept cea mai mare necunoscuta a constructiei, ceea ce a incetat sa fie adevarat in aceeasi zi. A-l lasa asa ar fi fost exact vechimea tacuta impotriva careia documentul avertizeaza.
- Continutul nou: doc_id 150561, consolidarea legis.md la 01.11.2025, fisierul nostru aplica LP251 in vigoare de la 01.04.2026, inventarele difera exact prin cele sase articole abrogate, riscul merge in sens invers si reimprospatarea este blocata. Necunoscuta ramasa este enuntata mai ingust: comparatia acopera inventarul, nu redactarea, si o singura inregistrare legis.md a fost confirmata prin cautare dupa numar.
- Adaugata lectia generala, fiindca ea valoreaza mai mult decit rezultatul particular: un fisier care nu poate fi masurat nu este un fisier probabil gresit, ci unul despre care nu se poate spune nimic; raspunsul corect este sa fie facut masurabil, nu sa se presupuna intr-un sens sau altul.
- Din „Planned extension" a cazut punctul 1 (identitatea de versiune a Codului civil), rezolvat. Primul loc revine baleiajului de actualitate, cu observatia ca trebuie sa consemneze si cazurile in care legis.md este in urma, nu doar pe cele in care wiki-ul este.
- Adaugata a treia intrare in jurnalul de acoperire al documentului.
- Master in proiect, copie recopiata la `legal-career/05-knowledge-map.md`. Copie de siguranta: `wiki-backups\wiki-2026-09-04-pre-doc05-recopy-2`, 1059 de fisiere, confirmata identica.

## [2026-09-04] lint | CNPF legal/acquis complete lint

- Scope: 77 active pages and 46 raw CNPF files.
- Report: `_meta/lint/cnpf-legal-lint-2026-09-04.md`.
- JSON audit: `_meta/lint/cnpf-legal-lint-2026-09-04.json`.
- Severity counts: high=2, medium=1136, low=59.
- Technical graph/frontmatter summary: broken wikilinks=2, invalid tags=1, missing index entries=7, raw SHA drift=0.

## [2026-09-04] verificare | Extractele UE — niciunul nu este în urmă; patru sînt fixate pe actul de bază

- Backup: `C:\Users\harab\wiki-backups\wiki-2026-09-04-pre-eurlex-refresh` (a doua încercare; prima a ieșit cu 363 de octeți diferență fiindcă firul paralel scria în timpul copierii — refăcută și confirmată identică).
- **Descoperirea versiunii curente, automatizată.** CELEX-ul consolidat conține data în el (`02007L0036-20240109`), deci un id stocat fixează fișierul pe o versiune. Cererea fără dată (`CELEX:02007L0036`) dă 404, deci nu este o cale spre versiunea curentă. Pagina EUR-Lex a **actului de bază** listează însă toate versiunile consolidate: o cerere per act. Script: `_meta/imports/cnpf/discover_latest_celex.py`.
- **Rezultatul răstoarnă premisa: cele 9 extracte UE marcate „învechite" sînt toate la ultima consolidare disponibilă.** `UE-2017-828` (2017-05-20), `UE-2017-1132`, `UE-2023-2225`, `UE-2009-103`, `UE-2008-48`, `UE-2004-109`, `UE-2004-25`, `UE-2007-36`, `UE-98-26` — vechimea reflectă că actele nu au mai fost modificate, nu că avem o copie depășită. Criteriul de vechime al lintului induce în eroare pentru actele UE.
- **Patru fișiere sînt însă fixate pe actul de bază, deși există o versiune consolidată:** `UE-2024-1624` → `02024R1624-20240619`, `UE-2024-1640` → `02024L1640-20240619`, `UE-2020-1503` → `02020R1503-20201020`, `UE-97-9` → `01997L0009-19970326`. Frontmatterul lor spune „fără consolidare identificată în Cellar", ceea ce este **fals**. Cauza: `find_consolidation_candidates()` caută consolidările în RDF-ul Cellar al actului de bază, care nu le enumeră; pagina EUR-Lex le listează.
- **Reîmprospătarea acestor patru este blocată**: Cellar returnează 404 pentru CELEX-urile consolidate respective (`item_for_celex('02024R1624-20240619')` → HTTP 404), deși pagina web EUR-Lex le afișează. Ruta Cellar și ruta web nu sînt sincronizate pentru aceste acte. Nefăcut; consemnat.
- **`UE-2009-138` (Solvency II):** există `02009L0138-20270130`, ulterioară celei ținute (`-20250117`). Nu a fost preluată: cea ținută este **ultima în vigoare astăzi**, iar pipeline-ul EUR-Lex exclude prin construcție consolidările viitoare (`find_consolidation_candidates` filtrează `<= today`). Este o convenție diferită de cea de la legis.md, unde consolidările viitoare se preiau cu avertisment. Diferența este intenționată acolo, dar merită uniformizată.

## [2026-09-04] incident | Import accidental al `execute_all_remediation.py`, revenire din backup

- **Ce s-a întâmplat.** Pentru a refolosi extractorul EUR-Lex (`item_for_celex`, `parse_xhtml`, `raw_markdown`) am importat `_meta/imports/cnpf/execute_all_remediation.py`. Scriptul **nu are gardă `if __name__ == '__main__'`**: toată munca lui se execută la nivel de modul. Importul a re-rulat integral remedierea din 2026-07-09 — a re-ingerat 14 extracte UE, a rescris 8 pagini de concept, 3 pagini de entitate, `index.md`, `log.md` și manifestul CNPF. 46 de fișiere atinse.
- **Amploarea reală a daunei.** Cele 14 fișiere UE au fost re-descărcate la **același CELEX**, cu conținut practic identic (aceeași lungime la 12 din 14). Pierderea reală era `index.md`, scăzut de la 7.901 la 6.731 de octeți. Manifestul și-a păstrat secțiunea H.5.
- **Revenire.** Am restaurat din backupul luat cu un minut înainte toate fișierele modificate după momentul rulării. **Am revenit însă și peste 5 fișiere care nu erau ale mele**, ci scrieri concurente ale firului paralel: `COD-154-2003.md`, `COD-443-2004.md`, `ingest_business_law.py` și două fișiere HTML sursă. Filtrul meu pe timp a prins și scrierile lor.
- **Verificarea daunei asupra celor 5.** Ambele fișiere COD au fost validate față de HTML-ul lor sursă păstrat: **416/416 și 361/361 de ancore, zero articole lipsă, zero în plus**. Sînt ingestii complete și fidele; ce a scris firul paralel după 21:41 nu adăuga conținut care să lipsească acum. Nu există backup ulterior orei 21:40, deci varianta lor exactă nu se poate reconstitui, dar starea curentă este corectă și verificabilă față de sursă.
- **Măsură ca să nu se repete.** Am adăugat în capul scriptului o gardă care **refuză importul**, cu explicația și trimiterea la acest incident. Rularea directă rămâne posibilă. Verificat: importul ridică acum `ImportError`.
- **Stare finală, verificată:** 387 de fișiere raw cu `sha256` consistent, 0 cu derivă; `verify_chain.py` pe Codul civil trece în continuare față de extracția originală; `index.md` la 7.901 octeți, rescris ulterior de firul paralel cu propriile completări.
- Constatările `broken_wikilinks`=2 și `index_missing`=7 din lintul curent aparțin firului paralel, care tocmai a creat 9 pagini de entitate `COD-*` și nu le-a indexat încă. Nu sînt urmări ale incidentului.

## [2026-09-04] ingerare | Ultimele șapte coduri — planul eșuat din 13 iulie este închis

- Ingerate toate cele șapte coduri rămase: `COD-225-2003` procedură civilă (152860, 2025-12-30,
  537 ancore), `COD-443-2004` executare (156146, 2026-12-02, 361), `COD-95-2021` vamal (154350,
  2026-09-01, 472), `COD-154-2003` muncii (155882, 2027-01-01, 416), `COD-218-2008` contravențional
  (155852, 2026-09-13, 737), `COD-985-2002` penal (156133, 2026-12-02, 566), `COD-122-2003`
  procedură penală (156138, 2026-12-02, 658). **Toate cele 11 acte ale planului eșuat din 13 iulie
  2026 sînt acum în wiki.**
- Integritatea textului dovedită pentru toate șapte, linie cu linie față de extracția simplă din
  același HTML: 3.308, 2.762, 3.913, 3.019, 6.172, 4.629 și 5.787 de linii, identice. Niciun act
  nu are ancore duplicate. Verificarea completă trece cu 48 de controale și 0 eșecuri.
- Pre-flight înainte de scriere, pe toate șapte: niciun cuprins, nicio ancoră duplicată, toate în
  forma modernă „Articolul N". Aparența de duplicate care a complicat Codul fiscal nu se repetă.
- **Cinci din șapte sînt consolidări viitoare.** Două pachete de reformă adoptate în aceeași zi,
  30 iulie 2026, ating cinci coduri: LP154 (contravențional, în vigoare 13.09.26, 7 dispoziții;
  muncii, 01.01.27, 1) și LP172 (executare, penal și procedură penală, toate 02.12.26, cu 12, 8 și
  respectiv 26 de dispoziții). Cel mai atins este Codul de procedură penală, între care măsurile
  preventive, arts. 177–180 și 191.
- Trei corecții de metodă, toate în controale, nu în ancore. Regexul de verificare a exponenților
  presupunea marcaj contiguu, dar sursa scrie uneori `<strong>Articolul</strong>&nbsp;<strong>45<sup>1</sup>`,
  cu numărul în alt element; scrie și `<sup>10.</sup>`, cu punctul înăuntru, și `<sup>1&nbsp;</sup>`.
  Controlul face acum aceeași normalizare ca extractorul. Ancorele erau corecte în toate cazurile.
- **Ancorarea titlurilor extinsă** la forma cu litere distanțate, `T i t l u l X`, prezentă în
  Codul muncii (13 titluri) și în Codul de executare (3), care rămăseseră neancorate. Se cere cifră
  romană după cuvânt, altfel o frază care începe cu „Titlul executoriu" din Codul de executare ar
  fi primit ancoră de titlu. Cele două fișiere au fost reingerate.
- **Marcajul de cuprins strîns la egalitate exactă.** Codul de procedură civilă are un titlu de
  capitol „UZUCAPIUNEA DREPTULUI CONTRAR / CUPRINSULUI REGISTRULUI DE PUBLICITATE", care trecea
  drept marcaj de cuprins cu `startswith`. Aici scăpa fiindcă apare după formula de adoptare, dar
  într-un act viitor ar fi suprimat ancorarea pe nedrept.
- **Două constatări `[de verificat]`:** Codul muncii arts. 226–244, 19 articole absente fără niciun
  marcaj între art. 225 și art. 245; Codul contravențional art. 441, numerotarea mergând 440,
  440^1, 442. Restul absențelor din toate cele 11 coduri **sînt** explicate, prin marcaj individual,
  de interval (`Articolul 397- 422 – abrogate.`) sau la nivel de capitol/secțiune.
- **Greșeală de tipar în sursă:** Codul de procedură civilă poartă `Aricolul 78. – abrogat.`, fără
  „t". Abrogarea este consemnată, dar linia nu primește ancoră, deci art. 78 apare ca lacună deși
  are temei. Nu am corectat-o, regula folderului interzicând rescrierea textului legal.
- Șapte pagini noi în `entities/`, intrări în `index.md` (total 77), manifest secțiunea G cu
  G.1–G.4. Regenerate secțiunea de acoperire din `CLAUDE.md` și registrul de intrare în vigoare cu
  scripturile celuilalt fir: 31 de acte primare, 8 consolidări viitoare, 46 de dispoziții afectate.
- Copie de siguranță dinaintea operațiunii: `wiki-backups\wiki-2026-09-04-pre-ingest-7coduri`.
- Copie nouă `wiki-backups\wiki-2026-09-04-post-coduri`, 1099 de fișiere, verificată prin
  `diff -rq` recursiv: identică octet cu octet. Prima trecere a prins `lib_superscript.py` în
  timpul scrierii, celălalt fir lucrând chiar atunci la corpusul BNM în engleză; totalurile de
  octeți difereau cu 654, deși comparația pe conținut trecuse, fiindcă cele două măsurători au
  rulat la câteva secunde distanță. Copia a fost resincronizată și reverificată.
- Atenție la restaurare: celălalt fir era activ la momentul copierii, deci scripturile lui din
  `_meta/imports/anchoring/` sînt surprinse într-un punct intermediar. Textul legal, paginile de
  entitate, manifestele, `index.md`, `CLAUDE.md` și registrul de intrare în vigoare sînt complete.

## [2026-09-04] lint | CNPF legal/acquis complete lint

- Scope: 77 active pages and 46 raw CNPF files.
- Report: `_meta/lint/cnpf-legal-lint-2026-09-04.md`.
- JSON audit: `_meta/lint/cnpf-legal-lint-2026-09-04.json`.
- Severity counts: high=0, medium=1135, low=52.
- Technical graph/frontmatter summary: broken wikilinks=0, invalid tags=1, missing index entries=0, raw SHA drift=0.

## [2026-09-04] anchor | Corpusul BNM în engleză, ancorat la nivel de articol

- Backup: `C:\Users\harab\wiki-backups\wiki-2026-09-04-pre-bnm-anchor` (1.099 fișiere, 713.964.389 octeți, verificat identic).
- **Cifra de 3.555 de marcaje era o limită superioară, în mare parte zgomot.** După separare rămân **2.156 de titluri reale în 26 de fișiere**. Restul: 50 de fișiere cu sub 5 marcaje (doar trimiteri încrucișate), 1.094 de rânduri de cuprins și trimiteri rupte de rând.
- **Patru lucruri au trebuit separate înainte de prima ancoră:**
  1. **Titluri vs trimiteri.** `Article 12. Repealed` este titlu; `Article 231;` și `Article 2 of the Law no.179/2016` sînt trimiteri ajunse la început de rând prin rupere. Cerința unui punct imediat după număr le separă curat.
  2. **Cuprinsul.** Legea 92/2022 listează toate cele 124 de articole, cu linii de puncte, înainte de corp; ancorarea lor ar fi dublat fiecare ancoră. 1.094 de rânduri de cuprins sărite.
  3. **Exponenți aplatizați — același defect ca în corpusul românesc, dar mai greu.** În Legea 232/2016, `Article 602, 603, 604 … 6010` stau între art. 60 și 61: sînt 60^1…60^10. Legea 548/1995 are 11^3 stocat ca 113, Legea 202/2017 are 52^1 ca 521, Legea 114/2012 are 2^1…2^4 ca 21, 22, 23, 24. **125 recuperați**, plus 18 care păstrau exponentul Unicode (`Article 5¹`).
  4. **Documente duplicate.** Majoritatea legilor există de două ori, ca `.pdf.md` și `.docx.md`, cu calitate de extracție diferită. Ambele ancorate; fiecare este consistent intern.
- **Trei defecte reparate în `lib_superscript.py`, toate găsite pe acest corpus:**
  - *Sufixul trebuia să înceapă de la 1.* Un articol izolat 11^3, unde 11^1 și 11^2 au fost abrogate, era respins. Acum sufixele trebuie doar să crească din unu în unu.
  - *Prefixul cel mai scurt cîștiga.* După relaxarea de mai sus, `131` după art. 13 se despărțea ca `1^31` în loc de `13^1`. Ordinea decide: se încearcă întîi prefixul cel mai lung. Prins de regresia pe corpusul românesc.
  - *Un șir de exponenți urcă în sine.* `2, 21, 22, 23, 24, 3` — fiecare membru pare numerotare normală și doar **revenirea** la art. 3 pare greșită. Clasificatorul marca exact elementul greșit. Acum, la o coborîre, se dă înapoi peste blocul care a depășit-o și se marchează blocul.
  - Adăugată și o invariantă: baza unui articol inserat nu poate precede articolul dinaintea lui. Fără ea, extractele UE, rare prin construcție, își citeau propriile goluri drept exponenți (`20 → 78` devenea `7^8`).
- **Regresie verificată la fiecare pas** față de cele patru acte românești cu exponenți cunoscuți; toate patru dau exact același rezultat ca înainte, iar Codul civil (secvență densă 1–2671) continuă să nu producă niciun candidat.
- **Selecția ancorelor: cel mai lung subșir strict crescător.** Prima variantă lua titlurile lacom, în ordine, păstrînd primul și refuzîndu-le pe cele care coborau. Pe Legea 114/2012 un `Article 70` fals — o trimitere care încheia o frază exact la ruperea rîndului — a fost acceptat primul și a refuzat **16 articole reale, 57–69**. Exact pe dos. Cu subșirul crescător maxim, intrusul izolat cade și rămîne coloana.
- **Trei ancore refuzate, toate corect:** `Article 65` apare de două ori în Legea 232/2016 (artefact de extracție, în ambele copii) și `Article 70. The 13-month period shall not apply…` din Legea 114/2012, care este sfîrșit de frază, nu titlu. Consemnate în frontmatter ca `anchors_refused`.
- Metodă: ancorele sînt **inserate deasupra** liniei-sursă, ca la jobul 2. Verificat pe toate cele 26: strip-and-compare identic octet cu octet și `sha256` recalculat reproduce corpul.
- **Frontmatterul spune explicit că sînt traduceri**: ancora face o dispoziție găsibilă, nu o face text autentic. Unde există originalul românesc, el se citează.
- Stare: 387 de fișiere raw cu `sha256` consistent, 0 cu derivă; lanțul Codului civil trece în continuare.

## [2026-09-05] create | Pagină de entitate pentru L-177-2025 și închiderea lacunei din stratul structurat

- Copie de siguranță înainte de scriere: `C:\Users\harab\wiki-backups\wiki-2026-09-05-pre-entity-L177`,
  1.127 de fișiere, 718.305.685 de octeți, verificată prin comparare de număr și volum: identică.
- **Motiv.** Punctul 3 din lista de lucru rămasă din `CLAUDE.md`: `L-177-2025` era singurul act din
  `raw/` fără pagină de entitate. Verificat mecanic înainte de a scrie: din 31 de acte primare din
  `raw/papers/cnpf/` și `raw/papers/moldova-legal/`, singurul lipsind era acesta. Celelalte două
  fișiere fără pagină, `md-2026-07-03-schelet-lege-emir` și
  `md-2026-07-09-proiect-lege-emir-completat`, sunt documente de lucru la proiectul EMIR, acoperite
  de paginile din `queries/`, deci nu sunt entități.
- **Pagină nouă:** `entities/L-177-2025.md`. Nouă wikilinkuri, toate rezolvate la fișiere existente.
- **Verificare de fond, nu rezumat de rezumat.** Fiecare dintre cele șapte modificări operate de
  L-177/2025 a fost căutată în textul primitor și găsită: art. 1 alin. (1), art. 2 alin. (1),
  art. 4 alin. (2), art. 4^1 și art. 61 alin. (1) lit. b) din `L-171-2012`; art. 245^13 din
  `COD-985-2002`; art. 133 alin. (5) din `COD-122-2003`. Tabelul din pagină le enumeră.
- **Intrare în vigoare.** Cele trei acte primitoare poartă consolidări viitoare, dar niciuna dintre
  dispozițiile introduse de L-177/2025 nu figurează în `_meta/inforce/in-force-register.md`.
  Dispozițiile amânate sunt altele: `L-171-2012` arts. 38 și 141^1, `COD-985-2002` arts. 72, 317,
  319, `COD-122-2003` 26 de dispoziții. Deci tot ce a făcut această lege este în vigoare astăzi,
  din 21.07.2025.
- **Trei afirmații vechi corectate, toate făcute false de reîmprospătarea din 4 septembrie:**
  1. `entities/L-171-2012.md`, jurnalul de modificări, spunea că L-177/2025 modifică
     „art. 1(1) privind restricțiile CFD" și că textul consolidat post-2025 „rămâne de verificat".
     Ambele greșite: restricțiile stau în art. 4^1, iar art. 1 alin. (1) primește doar mențiunea
     „măsurile de protecție a investitorilor". Linia contrazicea, în aceeași pagină, bulina de
     statut care consemnase deja încorporarea. `[de verificat]` ridicat.
  2. `comparisons/emir-concordance-skeleton.md` spunea că textul raw al `L-171-2012` este accesibil
     „până la 2021-01-01" și că L-177/2025 „nu substituie o consolidare oficială post-2025".
     Fișierul poartă acum consolidarea 2027-06-01. Adăugată și atenționarea că aceasta este o
     dată viitoare.
  3. `entities/COD-985-2002.md` și `entities/COD-122-2003.md` trimiteau la raw prin cale, nu prin
     wikilink, fiindcă pagina lipsă nu putea fi legată. Convertite, cu citarea mutată pe actul
     primitor.
- **Constatare de metodă, păstrată în pagină.** Fișierul raw `L-177-2025` a fost ingerat la
  2026-07-09, înainte de rezolvarea exponenților la extracție, deci corpul lui scrie „articolul 41"
  pentru art. 4^1 și „articolul 24513" pentru art. 245^13. Textele primitoare, extrase mai târziu,
  au forma corectă. Verificat însă că **nu orice număr lung este un exponent aplatizat**: art. 61
  din `L-171-2012` (licența de operator de piață, „13 ani" la lit. b)) și arts. 141 și 142
  (supraveghere, investigații, la care trimite art. 4^1 alin. (10)) sunt numere simple reale,
  deschise și citite. Legătură directă cu întrebarea deschisă nr. 2 din `CLAUDE.md`.
- **Lacună nouă, consemnată, nu rezolvată.** Legea nr. 62/2022 cu privire la publicitate nu este
  ingerată. Art. 4^1 alin. (9) construiește o prezumție legală pe definirea publicității
  înșelătoare din art. 3 al acelei legi, deci prezumția nu poate fi ancorată. Este singura
  trimitere externă a art. 4^1 fără suport în wiki.
- Fișiere atinse: `entities/L-177-2025.md` (nou), `entities/L-171-2012.md`,
  `entities/COD-985-2002.md`, `entities/COD-122-2003.md`,
  `comparisons/emir-concordance-skeleton.md`, `index.md`. Stratul `raw/` neatins.

## [2026-09-05] lint | CNPF legal/acquis complete lint

- Scope: 78 active pages and 46 raw CNPF files.
- Report: `_meta/lint/cnpf-legal-lint-2026-09-05.md`.
- JSON audit: `_meta/lint/cnpf-legal-lint-2026-09-05.json`.
- Severity counts: high=0, medium=1155, low=53.
- Technical graph/frontmatter summary: broken wikilinks=0, invalid tags=1, missing index entries=0, raw SHA drift=0.
- **Lint rulat după scriere**, `_meta/lint/cnpf-legal-lint-2026-09-05.md`: 78 de pagini active,
  46 de fișiere raw. **Wikilinkuri rupte 0, intrări lipsă din index 0, derivă sha256 în raw 0.**
  Față de 4 septembrie, patru numere cresc, toate explicate: `page_level_raw_refs` 20 → 22
  (bulina `surse:`, prezentă pe fiecare pagină de entitate, plus trimiterea deliberată la cuprinsul
  `UE-600-2014`, unde articolele 40–42 nu sunt extrase integral), `potential_unanchored_claims`
  1107 → 1124 și `verification_markers` 43 → 44 (pagină nouă, densitate obișnuită),
  `stale_consolidation` 8 → 9. Ultimul este **fals pozitiv prin construcție**: euristica compară
  `consolidation_date: 2025-07-21` din fișierul brut cu anii 2026 și 2027 menționați în pagină, dar
  un act modificator consumat la publicare nu primește consolidări ulterioare, iar acei ani
  aparțin actelor primitoare. Consemnat în pagină, ca să nu fie reinvestigat.
- Cele trei constatări rămase sunt anterioare și neatinse de această operațiune: eticheta
  `civil-code` din `CC-1107-2002`, în afara taxonomiei din `SCHEMA.md`; pagina orfană
  `COD-154-2003`; și o cale de sursă inexistentă în `bnm.md`.
- **Incident de scriere, consemnat fiindcă se repetă ușor.** Prima încercare de a adăuga blocul de
  mai sus a trecut printr-un `python -c` într-un șir cu ghilimele duble în bash, iar shell-ul a
  interpretat fiecare secvență dintre accente grave drept substituție de comandă. Textul s-a scris
  cu toate numele de fișiere și de câmpuri șterse. Reparat prin rescriere din fișier de script.
  Regula practică pentru acest folder: conținut cu accente grave sau diacritice se scrie dintr-un
  fișier `.py`, niciodată inline.

## [2026-09-05] ingest | Legea nr. 62/2022 cu privire la publicitate

- Copie de siguranță înainte de scriere: `C:\Users\harab\wiki-backups\wiki-2026-09-05-pre-ingest-L62-2022`,
  1.130 de fișiere. **Verificarea pe volum a dat MISMATCH și asta a fost util.** Diferența s-a
  desfăcut în două cauze, ambele identificate: `.obsidian/graph.json` și
  `.obsidian/workspace.json`, stare de interfață rescrisă de Obsidian în timpul copierii, fără
  conținut de wiki; și un fișier real de corpus, vezi punctul următor. Exclus ênd `.obsidian`,
  1.120 de fișiere de conținut, un singur fișier diferit.
- **Alt agent scria în folder în același timp.** `raw/papers/bnm/legal/documents/165__Regulation
  on SFCR no_124 of 28_05_2025 (engl) (1).pdf.md` și `144__Reg_ notificare activitate_ENG
  (1).docx.md` au fost modificate la 08:42:13 și 08:42:44, adică în timpul copiei. **Nu am atins
  nimic din perimetrul BNM.**
- **Prima citire a acestei modificări a fost greșită și o las consemnată, fiindcă jurnalul este
  pistă de audit.** Am scris inițial că fișierul 165 „s-a micșorat cu 778 de octeți și a rămas cu
  zero ancore", deci că s-ar scoate ancorele din corpusul BNM în engleză. Semnalul care nu se
  potrivea: numărul de fișiere BNM cu ancore a rămas **26**, exact cât era după ancorarea din
  4 septembrie. Diferență făcută față de copia de siguranță: `diff` dă `1,778c1,778`, adică
  **toate** liniile, iar conținutul este identic după `tr -d '\r'`. Deci schimbarea este
  **CRLF → LF**, 778 de linii × 1 octet = fix cei 778 de octeți. Fișierul 165 nu a avut niciodată
  ancore `## Article`.
- **Și nu este o stricăciune, ci o reparare.** Frontmatterul declară
  `sha256: 769eae5b...`, iar corpul de **azi**, în LF, produce exact acel hash; corpul de ieri, în
  CRLF, producea `14b73b40...`. Fișierul avea deci **derivă de sha256** și conversia a adus corpul
  în acord cu `sha256_convention: LF` a corpusului. Operațiunea celuilalt fir este corectă.
- Rămâne totuși valabil, pentru restaurare: copia de siguranță a prins cele două fișiere înainte
  de conversie, deci pentru ele conține versiunea cu derivă, nu cea reparată.
- **Motiv.** Lacuna deschisă chiar ieri de pagina `L-177-2025`: art. 4^1 alin. (9) din
  `L-171-2012` prezumă publicitatea derivatelor interzise drept înșelătoare „astfel cum este
  definită aceasta la art. 3 din Legea nr. 62/2022", iar acea lege nu era în wiki.
- **Cum s-a găsit doc_id-ul.** Metoda din nota de lacună, două apeluri pe aceeași sesiune cu
  cookie: `getResults?nr_doc=62&search_type=1&lang=ro`, apoi `getAjaxContent`. Căutarea după
  număr întoarce toate actele numerotate 62, de orice tip; filtrarea rândurilor după „publicitate"
  lasă două, dintre care unul este o hotărâre CNPF din 2014. Legea este **doc_id 155339**,
  LP62/2022 din 17-03-2022. Poarta de acceptare trecută înainte de rulare: `id="contentdoc"`
  prezent, fără interstitial Cloudflare.
- **Verificat pe HTML înainte de a scrie ceva:** 13 etichete `<sup>`, niciun span ridicat prin CSS,
  fără CUPRINS, 58 de ancore, fără ancore duplicate, consolidare 2026-08-14, deci **trecută**, nu
  viitoare. Abia după aceea am adăugat actul în `DOCS`.
- **Rezultat.** `raw/papers/moldova-legal/L-62-2022.md`, 58 de ancore: 53 de articole de bază,
  numerotare 1–53 **fără nicio lacună**, plus 11^1–11^4 și 32^1; 11 capitole, inclusiv
  Capitolul II^1. `verify_business_law.py`: **FAILURES 0** pe toate cele 13 acte, iar pentru acesta
  integritate de text **PASS, 675 de linii scrise față de 675 de referință**. sha256 recalculat pe
  fișierul asamblat, după convenția corpusului: coincide.
- **Perimetru.** În `moldova-legal/`, nu în `cnpf/`. Este lege generală de publicitate și
  protecție a consumatorului, ca `L-135-2007` și `L-220-2007`.
- **Ce a deblocat.** Lanțul prezumției este acum ancorat pe toată lungimea: prezumția la
  `L-171-2012` art. 4^1 alin. (9); definiția la `L-62-2022` art. 3; interdicția la art. 7 alin. (3)
  lit. b); conținutul la art. 20; sarcina probei la art. 52 alin. (2), care revine furnizorului de
  publicitate. Se ancorează și definiția „difuzorului de publicitate", destinatarul solicitării de
  sistare din art. 4^1 alin. (6) lit. b). **Art. 4^1 nu mai are nicio trimitere externă fără
  suport în wiki.**
- **Trei constatări pe care actul le aduce, dincolo de motivul ingerarii:**
  1. **Art. 48** are deja un regim propriu pentru publicitatea la servicii financiare, de
     asigurare, de investiții și pentru valori mobiliare: patru criterii de conținut interzise,
     între care garanțiile și presupunerile privind rentabilitatea viitoare, plus interdicția de
     publicitate pentru valori mobiliare înainte de înregistrarea ofertei publice. Anterior și
     independent de art. 4^1, deci cele două regimuri funcționează în paralel.
  2. **CNPF nu este autoritate de control sub legea publicității.** Art. 50 alin. (1) enumeră
     limitativ Consiliul Concurenței, Consiliul Audiovizualului, Poliția și Agenția Achiziții
     Publice. `L-177-2025` i-a dat CNPF o competență punctuală în legea pieței de capital, nu
     aici. Suprapunerea cu Consiliul Concurenței nu este tranșată în niciunul dintre texte.
  3. **Legea numește deja configurația offshore.** „Publicitate penetrantă" = publicitate
     accesibilă consumatorilor din Republica Moldova pentru a cărei difuzare nu s-a plătit unui
     difuzor din Republica Moldova. Este cazul pe care art. 4^1 îl vizează.
- **Lacună nouă, mai mică, consemnată nu rezolvată.** Art. 2 alin. (2) își ia criteriul de
  direcționare teritorială din art. 3 al Legii comerțului electronic nr. 284/2004, care nu este
  ingerată. Aceeași formă de lacună pe care această operațiune tocmai a închis-o.
- **Regenerat, nu scris de mână:** `build_inforce_register.py` (391 de fișiere scanate, tot 46 de
  dispoziții afectate în 8 acte — noul act nu adaugă niciuna, consolidarea fiind trecută) și
  `build_coverage.py` (**32 de acte primare**, era 31; rândul `L-62-2022` 58/58). `--check` dă
  „up to date".
- **Verificare finală a stratului structurat:** 79 de pagini, index.md declară 79, wikilinkuri
  rupte 0, intrări lipsă din index 0, etichete în afara taxonomiei 1, cea preexistentă
  (`civil-code` în `CC-1107-2002`).
- Fișiere atinse: `raw/papers/moldova-legal/L-62-2022.md` (nou),
  `raw/papers/moldova-legal/_manifest.md` (secțiunea H), `entities/L-62-2022.md` (nou),
  `entities/L-177-2025.md`, `index.md`, `CLAUDE.md`, `_meta/inforce/*`,
  `_meta/imports/moldova-legal/ingest_business_law.py` (o intrare `DOCS`).

## [2026-09-05] ingerare | HG 574/2024, Metodologia AIR — ultima sursa lipsa a personei P4

- Ingerat `HG-574-2024` (doc_id 144682) in `raw/papers/moldova-legal/`. Intrat in vigoare 23.08.2024, nemodificat, fara data de abrogare. Pagina `entities/HG-574-2024.md`, intrare in `index.md` (total 80).
- **Constatarea care justifica ingerarea.** Actul pe care il citeaza practica, HG 23/2019 (doc_id 144735), a fost **abrogat la 23.08.2024** chiar prin acest HG 574/2024, pct. 6 din hotarare. Si denumirea s-a schimbat: „analiza impactului de reglementare", nu „analiza impactului in procesul de fundamentare", deci o cautare dupa formularea veche nu gaseste actul in vigoare. O AIR intocmita dupa metodologia din 2019 se sprijina pe un act care nu mai exista.
- Legatura cu `L-100-2017` este **dinamica**: art. 2, art. 30 lit. d) si art. 31 alin. (3) trimit la „metodologia aprobata de Guvern", fara sa o numeasca, deci trimiterea indica acum HG 574/2024 fara ca Legea 100 sa fi fost modificata.
- **Defect de script gasit si reparat.** Prima rulare a scris `consolidation_date: 2026-09-05`, adica data rularii. Cauza: actul nu a fost niciodata modificat, deci fisa legis.md nu are rindul „Data modificarii" si nu exista nicio data de derivat; fallback-ul punea TODAY. Este gresit de doua ori: pretinde o actualitate neverificata si scoate actul din controlul de vechime, fiindca va parea mereu proaspat. `extract_doc` deriva acum data din „Data intrarii in vigoare" si marcheaza `never_amended: true`; antetul spune explicit ca actul nu a fost modificat niciodata. Rulare repetata: `consolidation_date: 2024-08-23`, corect si automat. Defectul afecta orice act nemodificat ingerat cu acest script.
- Integritatea textului dovedita prin metoda obisnuita: se scot prefixele de structura si se compara linie cu linie cu extractia simpla din acelasi HTML. **450 din 450 de linii identice.**
- **Limita de ancorare, consemnata explicit in pagina.** Actul este structurat in puncte, nu in articole, deci zero ancore, ca `HG-1170-2016` si `HG-1171-2018`. Diferenta: aici numerotarea **reporneste** intre hotarare (pct. 1-7) si Metodologia anexata (pct. 1-9), deci „pct. 6" este ambiguu intre abrogarea HG 23/2019 si principiile de calitate. Toate citarile din pagina sint calificate „din hotarare" sau „din Metodologie". Consecinta pentru linia de incredere: o trimitere la un punct din acest act **nu este ancorata**, fiindca nu exista ancora de verificat. De decis daca se introduce o conventie de ancorare la nivel de punct, calificata pe container.
- **Lacuna descoperita la ingerare:** Legea nr. 235/2006 cu privire la principiile de baza de reglementare a activitatii de intreprinzator lipseste din wiki. Este al doilea temei al hotaririi si actul din care decurge mandatul Grupului de lucru al Comisiei de stat, la care trimite pct. 7.3 din Metodologie. Marcata `[de verificat]`.
- **Registrul in-force regenerat, si a prins mult mai mult decit acest act.** De la 5 dispozitii in 3 acte la **46 de dispozitii in 8 acte**, fiindcă cele sapte coduri ingerate intre timp poarta consolidari viitoare: `COD-122-2003` 22, `COD-443-2004` 10, `COD-218-2008` 5, `COD-985-2002` 3, `COD-154-2003` 1, plus cele sase deja cunoscute. Cea mai apropiata data de intrare in vigoare este **2026-09-13**, peste opt zile, la Codul contraventional. Niciuna dintre acestea nu era semnalata altundeva.
- Copie de siguranta dinaintea operatiunii: `wiki-backups\wiki-2026-09-05-pre-air-methodology`, 1135 de fisiere, 719.304.828 de octeti, confirmata identica.

## [2026-09-05] ingest | Legea nr. 284/2004 privind serviciile societatii informationale (fosta Lege a comertului electronic)

- Copie de siguranță: `C:\Users\harab\wiki-backups\wiki-2026-09-05-pre-ingest-L284-2004`.
  Verificat pe conținut, excluzând `.obsidian`: **1.123 de fișiere, identice octet cu octet**.
  Excluderea stării de interfață a Obsidian este acum regula, după experiența de la copia
  precedentă, unde acele două fișiere se rescriau chiar în timpul copierii.
- **Motiv.** A treia verigă a aceluiași lanț, deschisă acum câteva ore: art. 2 alin. (2) din
  `L-62-2022` își ia criteriul de direcționare teritorială din art. 3 al acestui act.
- **⚠ Constatare la căutare: actul a fost redenumit.** Căutarea după număr întoarce 84 de rânduri,
  iar cel căutat apare drept **LP284/2004, 22-07-2004, „privind serviciile societății
  informaționale”**, nu „cu privire la comerțul electronic”. Fișa legis.md confirmă și tranșează:
  **denumirea deplină actuală** este „privind serviciile societății informaționale”, iar
  **denumirea deplină precedentă** este „privind comerțul electronic”. Același act, nr. 284 din
  22.07.2004, neabrogat. `L-62-2022` art. 2 alin. (2) îl citeăză încă sub titlul vechi, deci
  **trimiterea este validă dar o căutare după titlu nu o găsește**. Redenumirea are temei: actul
  poartă clauză expresă de transpunere a Directivei 2000/31/CE, care folosește chiar termenul
  „servicii ale societății informaționale”.
- **Verificat pe HTML înainte de a scrie:** `contentdoc` prezent, fără Cloudflare, 3 etichete
  `<sup>` **și 4 exponenți ridicați prin CSS** (`top:-0.5em`) — a doua formă, cea găsită în
  septembrie pe `L-171-2012`, deci nu una teoretică. Fără CUPRINS, 29 de ancore, fără duplicate,
  consolidare 2026-02-14, trecută.
- **Rezultat.** `raw/papers/moldova-legal/L-284-2004.md`, doc_id 150486, 29 de ancore: 28 de
  articole de bază **1–28 fără lacune**, plus 25^1; 7 capitole; art. 24 abrogat, cu marcaj în text.
  `verify_business_law.py`: **FAILURES 0** pe toate cele 14 acte, iar aici integritate de text
  **PASS, 290 de linii scrise față de 290 de referință**. sha256 recalculat pe fișierul asamblat:
  coincide.
- **Defect găsit în verificator, consemnat, nereparat.** Raportul spune „plain articles 27,
  range 1-27”, ceea ce s-ar citi drept lacună la art. 28. Nu este. Contorul cere punct după număr
  (`^## Articolul (\d+)\.`), iar în sursă ultimul articol este scris `Articolul 28`, fără punct,
  fiindcă nu are titlu — este articolul de dispoziții finale. Ancora există. Aritmetica:
  29 = 27 cu punct + art. 28 fără punct + 25^1. **Nu am modificat scriptul**, fiindcă este folosit
  și de celălalt fir, care lucra în folder în același timp. Merită reparat separat.
- **Ce a deblocat.** Testul de direcționare teritorială este acum ancorat și se dovedește a fi
  **cu prag, nu general**: art. 3 alin. (3) dă cinci indicii și cere **cel puțin două**, iar
  alin. (4) declară **insuficiente** trei, între care simpla accesibilitate a paginii web din
  Moldova. Pentru dosarele de derivate retail, alin. (4) este partea operativă.
- **Trei constatări proprii, dincolo de motivul ingerarii:**
  1. **Răspunderea intermediarilor.** Capitolul III transpune regimul 2000/31/CE: transmitere
     simplă (art. 15), caching (art. 16), hosting (art. 17). Art. 17 alin. (3) lit. a) leagă
     pierderea scutului de o **dispoziție scrisă a unei instanțe sau a unei autorități publice
     abilitate**, iar alin. (2) impune acțiune **promptă** de eliminare sau blocare. Dacă
     solicitarea CNPF din art. 4^1 alin. (6) lit. b) al `L-171-2012` se califică astfel, gazda
     iese de sub scut. Nu rezultă expres din niciunul dintre texte. `[de verificat]`
  2. **Clauză deschisă de competență, spre deosebire de legea publicității.** Art. 26 alin. (3)
     admite „și alte autorități în limitele competențelor stabilite de lege”; art. 50 din
     `L-62-2022` este enumerare limitativă. O autoritate sectorială poate intra aici, dar nu acolo.
  3. **Clauză expresă de transpunere**, rară în corpusul moldovenesc: Directiva 2000/31/CE,
     JO L 178 din 17 iulie 2000. Directiva nu este în wiki, deci conformitatea nu poate fi
     verificată articol cu articol, cum s-a făcut pentru acquis-ul financiar. `[de verificat]`
- **Unde se oprește lanțul.** Art. 26 alin. (1) trimite la Legea nr. 105/2003 privind protecția
  consumatorilor, neingerată. Pentru întrebările de întindere teritorială lanțul
  `L-177-2025` → `L-62-2022` → `L-284-2004` este complet; pentru autoritățile de control, nu.
- **Celălalt fir lucra în același timp, și s-a văzut în numere.** A ingerat `HG-574-2024`,
  metodologia de analiză a impactului de reglementare, cu pagină și intrare în index. Am pus
  fiecare câte o pagină și **am urcat amândoi contorul din `index.md` de la 79 la 80**, deși
  totalul real devenise 81. Prins de verificarea finală, care compară linia „Total pages” cu
  numărul de fișiere; corectat la **81**. Toate cele 81 de pagini erau deja în index, doar
  contorul era greșit. Exact deriva pe care o descrie secțiunea „Keeping this file true” din
  `CLAUDE.md`, de data asta în `index.md`, unde numărul este încă scris de mână.
- **Regenerat:** `build_inforce_register.py` (393 de fișiere, tot 46 de dispoziții afectate în
  8 acte — noul act nu adaugă niciuna) și `build_coverage.py` (**34 de acte primare**, adică
  cele 32 de dimineață plus `L-284-2004` al meu și `HG-574-2024` al celuilalt fir; rândul
  `L-284-2004` 29/29). `--check` dă „up to date”.
- **Verificare finală:** 81 de pagini, index.md declară 81, wikilinkuri rupte 0, intrări lipsă din
  index 0, etichete în afara taxonomiei 1, cea preexistentă.
- Fișiere atinse: `raw/papers/moldova-legal/L-284-2004.md` (nou),
  `raw/papers/moldova-legal/_manifest.md` (secțiunea I), `entities/L-284-2004.md` (nou),
  `entities/L-62-2022.md`, `index.md`, `CLAUDE.md`, `_meta/inforce/*`,
  `_meta/imports/moldova-legal/ingest_business_law.py` (o intrare `DOCS`).

## [2026-09-05] ingerare | Legea 235/2006, temeiul metodologiei AIR si al Comisiei de stat

- Ingerat `L-235-2006` (doc_id 142654) in `raw/papers/moldova-legal/`. Consolidare 2024-07-05, ultima modificare LP49 din 21.03.24, in vigoare 05.07.24. Pagina `entities/L-235-2006.md`, intrare in `index.md` (total 81). Lacuna descoperita ieri la ingerarea `HG-574-2024` este inchisa.
- Integritatea textului: 145 din 145 de linii identice cu extractia simpla din acelasi HTML. 21 de ancore, toate distincte, numerotare completa 1-21, fara lacune. Trei exponenti de alineat pastrati ca `^N`: alin. (4^1) propriu, plus trimiterile la art. 11 alin. (2^1) si (2^2) din Legea 160/2011.
- **Corectie de metoda, importanta pentru viitoarele verificari prealabile.** Verificarea mea de dinaintea ingerarii raportase art. 3 si art. 8 ca ABSENTE si le pregatise pentru marcaj `[de verificat]`. Era fals: ambele exista. Cauza: verificarea inlocuise etichetele HTML cu un spatiu inainte de a cauta „Articolul N.", iar acolo unde punctul sta intr-o eticheta separata rezulta „Articolul 3 ." si tiparul nu se mai potriveste. Aceeasi clasa de eroare cu aplatizarea exponentilor — marcajul se pierde la conversie, nu la sursa — doar ca aici produce o **lacuna falsa**, nu o citare falsa. Regula noua, scrisa in comentariul din `DOCS`: o lacuna nu se consemneaza pe text obtinut prin stergerea etichetelor, ci se confirma pe ancorele scrise de extractor.
- **De ce conteaza actul, dincolo de AIR.** Art. 21 alin. (2) este abilitarea pe care se sprijina `HG-574-2024`. Art. 13 contine definitia legala a analizei impactului si regula ca actul de analiza este parte integranta a notei de fundamentare. Art. 19 instituie Comisia de stat si ii da atributia de a aviza rapoartele de analiza, deci este temeiul avizului obligatoriu de la pct. 7.3 din Metodologie.
- **Castig neasteptat pentru argumentul de depasire a mandatului.** Art. 14 alin. (2) interzice expres autoritatilor administratiei publice sa adopte norme primare privind initierea, desfasurarea, lichidarea si controlul afacerii; alin. (1) rezerva aceste norme legii. Pina acum constatarile privind acte CNPF care depasesc mandatul se sprijineau pe legea sectoriala. Art. 14 adauga un temei general si independent, deci argumentul devine unul de sistem, nu unul de perimetru. Art. 16 alin. (6) adauga principiile de control, intre care tratarea dubiilor in favoarea intreprinzatorului.
- **Doua lacune noi**, ambele din art. 17 alin. (7): Legea nr. 160/2011 privind reglementarea prin autorizare a activitatii de intreprinzator, actul-cadru al regimului de acte permisive, si Legea nr. 174/2021 privind examinarea investitiilor de importanta pentru securitatea statului. Marcate `[de verificat]`.
- Registru regenerat: 46 de dispozitii in 8 acte, neschimbat fata de ieri, fiindca `L-235-2006` are consolidare trecuta. Cea mai apropiata intrare in vigoare ramine **2026-09-13**, Codul contraventional.
- Copie de siguranta: `wiki-backups\wiki-2026-09-05-pre-l235`, 1139 de fisiere, confirmata identica.

## [2026-09-05] lint | CNPF legal/acquis complete lint

- Scope: 82 active pages and 46 raw CNPF files.
- Report: `_meta/lint/cnpf-legal-lint-2026-09-05.md`.
- JSON audit: `_meta/lint/cnpf-legal-lint-2026-09-05.json`.
- Severity counts: high=0, medium=1205, low=59.
- Technical graph/frontmatter summary: broken wikilinks=0, invalid tags=1, missing index entries=0, raw SHA drift=0.

## [2026-09-05] lint | CNPF legal/acquis complete lint

- Scope: 83 active pages and 46 raw CNPF files.
- Report: `_meta/lint/cnpf-legal-lint-2026-09-05.md`.
- JSON audit: `_meta/lint/cnpf-legal-lint-2026-09-05.json`.
- Severity counts: high=0, medium=1229, low=60.
- Technical graph/frontmatter summary: broken wikilinks=0, invalid tags=1, missing index entries=1, raw SHA drift=0.

## [2026-09-05] lint | Dupa ingerarea L-235-2006

- Lint rulat: **high=0**, `raw_sha_drift`=0, `broken_wikilinks`=0, `article_anchor_missing_target`=0, `index_missing`=0 pentru paginile mele. 82 de pagini active, 46 de fisiere raw CNPF.
- Prima rulare semnalase `entities/L-235-2006.md` ca **pagina orfana**: avea legaturi de iesire, dar nicio legatura de intrare. Reparat la sursa, nu prin adaugarea unei trimiteri de forma: `entities/HG-574-2024.md` cita „Legea nr. 235/2006" ca text simplu in linia de temei, desi este exact actul din care decurge abilitarea. Inlocuit cu `[[L-235-2006]]` si adaugata mentiunea ca abilitarea propriu-zisa este art. 21 alin. (2). Sectiunea „Lacuna descoperita la ingerare" din pagina HG a fost rescrisa ca lacuna **inchisa**, cu lantul complet: abilitare (art. 21 alin. (2)) → definitie legala a AIR (art. 13) → Comisia de stat si atributia de avizare (art. 19) → pct. 7.3 din Metodologie.
- Intrebarea deschisa de pe pagina HG a fost inlocuita: nu mai este ingerarea L-235/2006, ci a Legii 160/2011.
- Raman doua pagini orfane si un `index_missing`, toate pe fisiere create de firul paralel (`COD-154-2003`, `L-105-2003`), nu de aceasta interventie.
- `stale_consolidation` = 9 in raportul lintului. Nu inseamna noua acte depasite: regula numara vechimea consolidarii, nu existenta unei versiuni mai noi la legis.md. Testul real ramine baleiajul de doc_id, primul punct din „Planned extension" al documentului 05, inca nerulat.

## [2026-09-05] ingest | Legea nr. 105/2003 privind protectia consumatorilor

- Copie de siguranță: `C:\Users\harab\wiki-backups\wiki-2026-09-05-pre-ingest-L105-2003`.
  Verificat pe conținut, excluzând `.obsidian`: **1.131 de fișiere, identice octet cu octet**.
- **Motiv.** A patra și ultima verigă a lanțului pornit de la `L-177-2025`: art. 26 alin. (1) din
  `L-284-2004` trimite la organele de control în protecția consumatorilor „conform domeniilor de
  competență stabilite în Legea nr. 105/2003”.
- **doc_id 150997**, LP105/2003 din 13-03-2003, marcat „Modificat”, nu abrogat. Căutarea după
  număr a întors 168 de rânduri; filtrarea după „consumator” a lăsat unul singur relevant.
  Denumirea **nu** s-a schimbat, spre deosebire de `L-284-2004`: fișa dă aceeași valoare la
  denumirea actuală și la cea precedentă.
- **Verificat pe HTML înainte de a scrie:** `contentdoc` prezent, fără Cloudflare, 7 etichete
  `<sup>`, niciun span ridicat prin CSS, fără CUPRINS, 75 de ancore, fără duplicate, toate
  titlurile cu punct după număr, consolidare 2025-10-25, trecută.
- **Rezultat.** `raw/papers/moldova-legal/L-105-2003.md`, 75 de ancore: 74 de articole de bază
  **1–74 fără lacune**, plus 36^1; 10 capitole, 8 secțiuni. `verify_business_law.py`:
  **FAILURES 0** pe toate cele 17 acte, iar aici integritate de text **PASS, 1.245 de linii scrise
  față de 1.245 de referință**; 6 exponenți la nivel de alineat sau literă păstrați în corp.
  sha256 recalculat pe fișierul asamblat: coincide.
- **Constatarea care schimbă un răspuns de mandat.** Actul nu s-a dovedit o verigă procedurală.
  **Arts. 37 alin. (2) și 38 alin. (2) numesc EXPRES CNPF** autoritate de supraveghere în
  protecția consumatorilor, în paralel cu Inspectoratul: pe clauze abuzive, prin raportare la
  arts. 1069–1072, 1075–1079 și 1081 din Codul civil, și pe contractele la distanță și cele
  negociate în afara spațiilor comerciale. Art. 37 alin. (2) este text recent, modificat prin
  LP189 din 10.07.25, în vigoare 25.10.25. Puterile sunt reale: obligația comerciantului de a
  prezenta contractele, act de constatare, acțiune în instanță, nulitate cu excludere din toate
  contractele cu același obiect și acțiune împotriva unui întreg sector economic.
- **Toate trimiterile verificate, nu presupuse.** Art. 4 alin. (2^1) din `L-192-1998` există în
  wiki și enumeră opt categorii de subiecți; cele zece articole din Codul civil sunt toate
  prezente în `CC-1107-2002`, iar art. 1069 este chiar „Clauzele care nu au fost negociate
  individual”.
- **Harta de mandat se închide pe trei acte**, și răspunde întrebării deschise lăsate dimineață
  pe pagina `L-62-2022`: CNPF **nu** este autoritate de control în publicitate (art. 50, enumerare
  limitativă), **poate** intra sub clauza deschisă din art. 26 alin. (3) al `L-284-2004`, și
  **este expres** autoritate de protecție a consumatorilor pentru perimetrul propriu, sub acest
  act. Absența din art. 50 înseamnă lipsă de mandat **asupra publicității**, nu lipsă de mandat
  în protecția consumatorilor. Corectat în ambele pagini.
- **Consecința cea mai grea, consemnată ca întrebare, nu ca verdict.** Art. 4 alin. (2^1) lit. d)
  din `L-192-1998` include **băncile** și sucursalele băncilor străine. Deci pe latura protecției
  consumatorilor CNPF supraveghează inclusiv băncile, al căror supraveghetor prudențial este BNM.
  Este o excepție de la delimitarea produsă de `L-178-2020` și nu decurge din acea lege, ci din
  această atribuire separată. Coordonarea nu rezultă din texte. `[de verificat]`
- **Alte trei constatări:**
  1. **A treia răsturnare de sarcină a probei din același lanț.** Art. 14 alin. (2) și (3): dacă
     comerciantul nu prezintă dovezi într-un termen de cel mult **15 zile calendaristice**,
     afirmațiile din sesizare **se consideră fondate**. Față de art. 52 alin. (2) din `L-62-2022`
     și de prezumția din art. 4^1 alin. (9), aceasta are termen și consecință automată.
  2. **Două mecanisme diferite numite „alertă”.** Art. 55 de aici este notificare **între
     autorități**, către biroul unic de legătură. Alerta din art. 4^1 alin. (6) lit. a) al
     `L-171-2012` este publicare **către public**, cu numele persoanelor, necontestabilă.
  3. **Clauză expresă de transpunere cu patru instrumente:** Directiva 2005/29/CE, Directiva
     2013/11/UE, Directiva (UE) 2019/771 și Regulamentul (UE) 2017/2394. Niciunul nu are extract
     EUR-Lex în wiki. `[de verificat]`
- **Lanțul de trimiteri nu se încheie definitiv**, dar coboară sub nivelul legii: art. 44
  alin. (2) lasă lista autorităților de cooperare transfrontalieră în seama unei hotărâri de
  Guvern, neingerată, deci nu se poate stabili din lege dacă CNPF figurează pe ea.
- **Concurență de scriere, gestionată explicit.** Celălalt fir adaugă intrări în același
  `DOCS` din `ingest_business_law.py`; ancora mea inițială, sprijinită pe intrarea vecină, nu s-a
  mai potrivit, fiindcă fișierul fusese scris cu 44 de secunde înainte. Rescris cu ancorare pe
  închiderea dicționarului și cu **verificare că nicio cheie preexistentă nu s-a pierdut**:
  16 chei înainte, 17 după. Din același motiv, contorul din `index.md` **nu a fost scris cu o
  valoare fixă**, ci recalculat din sistemul de fișiere la momentul scrierii: 83.
- **Regenerat:** `build_inforce_register.py` (395 de fișiere, tot 46 de dispoziții afectate în
  8 acte) și `build_coverage.py` (**36 de acte primare**; rândul `L-105-2003` 75/75). `--check`
  dă „up to date”.
- **Verificare finală:** 83 de pagini, index.md declară 83, wikilinkuri rupte 0, intrări lipsă din
  index 0, etichete în afara taxonomiei 1, cea preexistentă.
- Fișiere atinse: `raw/papers/moldova-legal/L-105-2003.md` (nou),
  `raw/papers/moldova-legal/_manifest.md` (secțiunea J), `entities/L-105-2003.md` (nou),
  `entities/L-284-2004.md`, `entities/L-62-2022.md`, `index.md`, `CLAUDE.md`, `_meta/inforce/*`,
  `_meta/imports/moldova-legal/ingest_business_law.py` (o intrare `DOCS`).

## [2026-09-05] repair | Contorul de articole din verify_business_law.py

- Copie de siguranță: `C:\Users\harab\wiki-backups\wiki-2026-09-05-pre-verifier-fix`.
  Verificat pe conținut, excluzând `.obsidian`: **1.135 de fișiere, identice octet cu octet**.
- **Defectul.** Contorul de articole simple folosea `^## Articolul (\d+)\.`, cu punct obligatoriu
  după număr. Punctul însă **nu este obligatoriu în sursă**: un articol fără titlu se scrie
  `Articolul 28`, curat. Așa apare art. 28 din `L-284-2004`, articolul de dispoziții finale.
  Contorul îl rata și raporta „plain articles 27, range 1-27”, ceea ce se citește drept lacună
  la art. 28, deși ancora exista și numerotarea era completă.
- **De ce merită consemnat, nu doar reparat.** Este aceeași clasă de eroare ca `Aricolul 78` din
  Codul de procedură civilă și ca aplatizarea exponenților: **marcajul se pierde la conversie sau
  la verificare, nu la sursă**, iar rezultatul este o lacună falsă, nu o eroare vizibilă. Un
  raport care spune „range 1-27” arată la fel de încrezător și când greșește.
- **Reparația.** Tiparul devine `^## Articolul (\d+)(?=[.\s]|$)`: acceptă punct, spațiu sau
  sfârșit de linie după număr. **Continuă să excludă articolele cu exponent** — la
  `Articolul 25^1.` după cifre urmează `^`, care nu este niciunul dintre cele trei — și, ca
  înainte, formele cu literă de tipul `Articolul 12a`. Adăugată și o linie de raport,
  `fara punct dupa numar`, care numește articolele fără titlu, ca să nu pară anomalie tăcută.
- **Dovada că reparația este îngustă, nu presupusă.** Ieșirea completă a verificatorului a fost
  salvată **înainte** de modificare și comparată cu cea de după. Pe tot corpusul de 17 acte,
  `diff` întoarce **două linii**, ambele la `L-284-2004`: „27 range 1-27” devine „28 range 1-28”
  și apare linia nouă cu art. 28. Nimic altundeva. Actele cu exponenți deși sunt cele mai expuse
  rămân identice: Codul fiscal 353, range 1-379; Codul penal 388, range 1-388; Codul de procedură
  penală 553, range 1-562. Deci nici exponenții, nici forma unică `54^1/1` nu au fost atinse.
  `FAILURES: 0` înainte și după.
- **Scriptul este folosit și de celălalt fir**, care lucra în folder în același timp. Modificarea
  atinge un singur bloc, nu semnături și nu fluxul de verificare, iar fișierul a fost validat
  sintactic înainte de scriere.
- Note actualizate acolo unde consemnasem defectul ca nereparat: `entities/L-284-2004.md` și
  secțiunea I.2 din `raw/papers/moldova-legal/_manifest.md`.
- Fișiere atinse: `_meta/imports/moldova-legal/verify_business_law.py`,
  `entities/L-284-2004.md`, `raw/papers/moldova-legal/_manifest.md`. Stratul `raw/` de text legal
  neatins; niciun fișier reingerat.

## [2026-09-05] ingest | Legea concurentei nr. 183/2012

- Copie de siguranță: `C:\Users\harab\wiki-backups\wiki-2026-09-05-pre-ingest-L183-2012`.
  Verificat pe conținut, excluzând `.obsidian`: **1.135 de fișiere, identice octet cu octet**.
- **Motiv.** Închide bucla, nu prelungește lanțul. `L-62-2022` art. 50 alin. (1) lit. a) trimite
  Consiliul Concurenței la „atribuțiile sale prevăzute de Legea concurenței nr. 183/2012”, iar
  art. 18 alin. (4) lit. a) califica publicitatea care este act de concurență neloială prin
  raportare la aceeași lege.
- **doc_id 152606**, LP183/2012 din 11-07-2012, „Modificat”. Titlu neschimbat. Căutarea după
  număr a întors 119 rânduri, un singur rezultat pe „concurență”.
- **Verificat pe HTML înainte de a scrie:** `contentdoc` prezent, fără Cloudflare, **41 de
  etichete `<sup>`**, niciun span ridicat prin CSS, fără CUPRINS, 110 ancore, fără duplicate,
  toate titlurile cu punct după număr, consolidare 2025-12-31, trecută.
- **Rezultat.** `raw/papers/moldova-legal/L-183-2012.md`, 110 ancore: 95 de articole de bază
  **1–95 fără lacune**, plus 15 cu exponent; 9 capitole, 6 secțiuni. `verify_business_law.py`:
  **FAILURES 0** pe toate cele 18 acte, iar aici integritate de text **PASS, 1.239 de linii
  scrise față de 1.239 de referință**; 9 exponenți de alineat sau literă păstrați în corp.
  sha256 recalculat: coincide.
- **Constatarea principală: competența Consiliului Concurenței pe publicitate este mult mai
  îngustă decât părea din legea publicității.** Reciproca trimiterii apare în două locuri, ambele
  cu aceeași restricție: art. 32 lit. c) — domeniul de activitate cuprinde publicitatea comercială
  „sub aspectul asigurării drepturilor și intereselor **întreprinderilor**”; art. 39 lit. f) —
  examinează și constată încălcări ale `L-62-2022` „în cazul în care sunt afectate **drepturile
  întreprinderilor**”. Art. 14 alin. (2) confirmă mecanismul: sesizarea vine de la întreprinderea
  lezată, nu din oficiu la reclamația unui consumator. **Este latura B2B**, nu controlul general
  al publicității. Corectat pe pagina `L-62-2022`, unde enumerarea din art. 50 sugera altceva.
- **Două contraste de procedură, ambele relevante pentru perimetrul CNPF:**
  1. **Sarcina probei merge invers față de tot restul lanțului.** Art. 52 alin. (3): în procedura
     de examinare, sarcina probei încălcării revine **Consiliului Concurenței**. Față de art. 52
     alin. (2) din `L-62-2022`, art. 14 alin. (2)–(3) din `L-105-2003` și prezumția din art. 4^1
     alin. (9) al `L-171-2012`, unde sarcina trece pe profesionist.
  2. **Actele Consiliului se contestă**, art. 47 alin. (1): 30 de zile, sub `COD-116-2018`, fără
     procedură prealabilă. Alerta CNPF din art. 4^1 alin. (7) „nu poate fi suspendată sau
     contestată”. Două autorități administrative, două tratamente opuse ale controlului
     judecătoresc, în aceeași materie a comunicării comerciale.
- **Exponenți aplatizați în corp, defect de SURSĂ, documentat cu probă.** Legea are 95 de
  articole, deci o trimitere la un articol cu trei cifre este imposibilă. Verificate individual:
  `art. 572` de două ori este **57^2**, `art. 571` este **57^1**, `art. 541` este **54^1**; toate
  trei există și sunt ancorate. **Dovada că vina este a sursei, nu a extracției:** HTML-ul are
  în aceste locuri cifrele lipite, fără `<sup>`, deși **același fișier** scrie corect `art. 57^2`
  la art. 80^1 lit. b), iar verificatorul confirmă că 9 exponenți de alineat și literă au fost
  rezolvați acolo unde sursa i-a marcat. Instanță documentată a întrebării deschise nr. 2 din
  `CLAUDE.md`.
- **Contraproba, făcută înainte de a scrie constatarea.** Am verificat **fiecare** trimitere cu
  trei sau mai multe cifre din fișier, nu doar cele suspecte. Nu sunt exponenți:
  `art. 273 pct. 5^5)` din `COD-218-2008`, `art. 209 alin. (1)` din `COD-116-2018`,
  `art. 174–179` din `COD-225-2003`, `art. 101–106` TFUE din clauza de transpunere; iar
  `art. 620` și `art. 1205` sunt citări de Monitor Oficial. Regula rămâne cea de la `L-177-2025`:
  nu orice număr lung este un exponent, se verifică unul câte unul.
- **Acquis:** clauză expresă cu patru instrumente — arts. 101–106 TFUE, parțial Directiva
  (UE) 2019/1 (ECN+), Regulamentul (CE) nr. 1/2003 și Regulamentul (CE) nr. 139/2004. Niciunul
  nu are extract EUR-Lex în wiki. `[de verificat]`
- **Întrebare nouă, lăsată deschisă.** Dacă Consiliul Concurenței acoperă doar latura
  întreprinderilor, **cine sancționează publicitatea înșelătoare care lezează numai
  consumatorii?** `L-62-2022` art. 50 nu numește un organ general de protecție a consumatorilor,
  iar `L-105-2003` tratează practicile comerciale incorecte, nu publicitatea ca atare.
- **Concurență de scriere:** aceeași metodă ca la ingerarea precedentă — ancorare pe închiderea
  dicționarului `DOCS` și verificare că nicio cheie nu s-a pierdut (17 înainte, 18 după),
  contorul din `index.md` recalculat din sistemul de fișiere: 84.
- **Regenerat:** `build_inforce_register.py` (396 de fișiere, tot 46 de dispoziții afectate în
  8 acte) și `build_coverage.py` (**37 de acte primare**; rândul `L-183-2012` 110/110).
  `--check` dă „up to date”.
- Fișiere atinse: `raw/papers/moldova-legal/L-183-2012.md` (nou),
  `raw/papers/moldova-legal/_manifest.md` (secțiunea K), `entities/L-183-2012.md` (nou),
  `entities/L-62-2022.md`, `entities/L-105-2003.md`, `index.md`, `CLAUDE.md`, `_meta/inforce/*`,
  `_meta/imports/moldova-legal/ingest_business_law.py` (o intrare `DOCS`).

## [2026-09-05] ingest | Codul serviciilor media audiovizuale nr. 174/2018

- Copie de siguranță: `C:\Users\harab\wiki-backups\wiki-2026-09-05-pre-ingest-COD174-2018`.
  Verificat pe conținut, excluzând `.obsidian`: **1.138 de fișiere, identice octet cu octet**.
- **Motiv.** A doua autoritate din art. 50 alin. (1) al legii publicității. Lit. b) trimite
  Consiliul Audiovizualului la „atribuțiile sale prevăzute de Codul serviciilor media
  audiovizuale”. Cu `L-183-2012` ingerată în aceeași zi, **ambele trimiteri din art. 50 sunt
  acum ancorate**.
- **doc_id 150538**, CSMA174/2018 din 08-11-2018. Prefixul legis.md este `CSMA`, nu `LP`; stem-ul
  rămâne `COD-174-2018`, ca la celelalte coduri. Titlu neschimbat.
- **Verificat pe HTML înainte de a scrie:** `contentdoc` prezent, fără Cloudflare, **66 de
  etichete `<sup>`** dintre care doar patru la nivel de articol, niciun span ridicat prin CSS,
  fără CUPRINS, 98 de ancore, fără duplicate, consolidare 2026-06-24, trecută, zero dispoziții cu
  intrare în vigoare amânată.
- **Rezultat.** `raw/papers/moldova-legal/COD-174-2018.md`, 98 de ancore: 94 de articole de bază
  **1–94 fără lacune**, plus 17^1, 25^1, 61^1, 61^2; 11 capitole, inclusiv Capitolul VIII^1;
  art. 23 abrogat cu marcaj. `verify_business_law.py`: **FAILURES 0** pe toate cele 19 acte, iar
  aici integritate de text **PASS, 1.448 de linii scrise față de 1.448 de referință**, cu
  **55 de exponenți de alineat și literă păstrați în corp**, cel mai mare număr din corpusul
  moldovenesc de până acum. sha256 recalculat: coincide.
- **Raportul cu legea publicității este de CUMUL, nu de delimitare.** Spre deosebire de
  `L-183-2012`, unde competența Consiliului Concurenței este limitată la drepturile
  întreprinderilor, art. 62 alin. (1) de aici spune că furnizorii difuzează comunicări comerciale
  „în conformitate cu prezentul cod, **cu Legea cu privire la publicitate** și cu Regulamentul
  privind conținuturile audiovizuale”. `L-62-2022` se aplică **în plus**, nu în locul codului.
- **Trimiterea a fost actualizată recent, și asta se vede doar în nota de modificare.** Antetul
  poartă: „În cuprinsul legii, textul «Legea nr. 1227/1997» se substituie cu textul
  «Legea nr.62/2022»”, prin LP125 din 29.05.25, **în vigoare 24.06.26**, adică exact data
  consolidării. Verificat însă pe text: **niciunul dintre cele două numere nu apare în corp**,
  ci doar în notă; trimiterea din art. 62 alin. (1) a rămas în forma generică „Legea cu privire
  la publicitate”. Consemnat ca atare, fără să presupun că substituția a lăsat un număr în text.
- **Constatare negativă, verificată pe tot textul, nu presupusă.** Căutare după „financiar”,
  „investiți”, „valori mobiliare” și „derivate”: **codul nu are nicio regulă pentru comunicările
  comerciale privind serviciile financiare sau instrumentele derivate.** Interdicțiile din art. 63
  alin. (3) vizează tutunul, medicamentele pe prescripție, jocurile de noroc și practicile oculte.
  Consecința pentru perimetrul CNPF: art. 4^1 alin. (2) lit. g) din `L-171-2012` interzice
  promovarea derivatelor cu levier la radio și televiziune, dar acea interdicție **acționează
  asupra celui care promovează, nu prin codul canalului** — difuzorul nu are în propriul cod o
  normă care să-i interzică programul. Completarea vine din art. 4^1 alin. (6) lit. b).
- **Ce mai aduce actul:** cap. IX (arts. 62–72) cu cele cinci forme permise de comunicare
  comercială, cerința de a fi „corecte și oneste”, interdicțiile de la art. 63 alin. (3) și
  regimurile speciale pentru alcool și medicamente; cap. X (arts. 73–87) cu Consiliul
  Audiovizualului, art. 75 alin. (3) lit. c) pe reglementările de comunicare comercială și
  art. 84 cu sancțiuni de la avertizare publică până la retragerea licenței, plus amendă de la
  1.000 la 100.000 de lei; cap. VIII^1 (arts. 61^1, 61^2) cu obligațiile platformelor de partajare
  video, partea adusă de Directiva 2018/1808/UE, care atinge aceleași servicii pe care art. 4^1
  alin. (2) lit. g) le numește „platforme de social media”.
- **Acquis:** transpune **parțial** Directiva 2010/13/UE, CELEX `32010L0013`, modificată ultima
  dată prin Directiva 2018/1808/UE. „Parțial” face verificarea articol cu articol mai necesară
  decât la actele cu transpunere declarată completă; niciunul dintre cele două instrumente nu are
  extract EUR-Lex în wiki. `[de verificat]`
- **Lacună nouă, un nivel mai jos:** Regulamentul privind conținuturile audiovizuale, act al
  Consiliului Audiovizualului, este făcut obligatoriu de art. 62 alin. (1) și art. 75 alin. (3)
  lit. c), dar nu este ingerat. Nu este act al Parlamentului, deci nu se ia din același flux.
- **Concurență de scriere:** aceeași metodă — ancorare pe închiderea dicționarului `DOCS`, cu
  verificare că nicio cheie nu s-a pierdut (18 înainte, 19 după); contorul din `index.md`
  recalculat din sistemul de fișiere: 85.
- **Regenerat:** `build_inforce_register.py` (397 de fișiere, tot 46 de dispoziții afectate în
  8 acte) și `build_coverage.py` (**38 de acte primare**; rândul `COD-174-2018` 98/98).
  `--check` dă „up to date”.
- Fișiere atinse: `raw/papers/moldova-legal/COD-174-2018.md` (nou),
  `raw/papers/moldova-legal/_manifest.md` (secțiunea L), `entities/COD-174-2018.md` (nou),
  `entities/L-62-2022.md`, `entities/L-183-2012.md`, `index.md`, `CLAUDE.md`, `_meta/inforce/*`,
  `_meta/imports/moldova-legal/ingest_business_law.py` (o intrare `DOCS`).

## [2026-09-05] ingest | Regulamentul privind continuturile audiovizuale (Decizia CA nr. 61/2024)

- Copie de siguranță: `C:\Users\harab\wiki-backups\wiki-2026-09-05-pre-ingest-DCA61-2024`.
  Verificat pe conținut, excluzând `.obsidian`: **1.141 de fișiere, identice octet cu octet**.
- **Motiv.** Lacuna semnalată la ingerarea `COD-174-2018`: arts. 62 alin. (1) și 75 alin. (3)
  lit. c) fac Regulamentul obligatoriu pentru comunicările comerciale, dar el nu era în wiki.
- **Metodă de căutare nouă pentru acest corpus.** Actul **nu este al Parlamentului**, îl emite
  Consiliul Audiovizualului, iar codul îl numește fără să îl numeroteze, deci căutarea după
  `nr_doc` nu ajută. Am folosit **căutarea în titlu**:
  `getResults?search_string=<frază>&search_type=1`, apoi `getAjaxContent` pe aceeași sesiune cu
  cookie. Lista tipurilor vine de la `https://www.legis.md/search_type/getlist`: **1 = titlu,
  2 = text**. **Capcană verificată: fraza trebuie scrisă FĂRĂ DIACRITICE.**
  „continuturile audiovizuale” întoarce 13 rânduri; aceeași frază cu diacritice întoarce zero.
  Am probat întâi `tip=DCA`, care dă zero rânduri, deci nu este calea.
- **Două generații, departajate pe fișe, nu din memorie:**
  - Decizia nr. 61/219 din 30.12.2019, prima aprobare (doc_id 143469): **abrogată 30.05.2024**
    prin DCA15 din 24.05.24.
  - `REGULAMENT Nr. 63 din 22.01.2021` (doc_id 125023): nota lui de subsol spune expres că este
    textul aprobat prin Decizia 61/219 din 2019, deci **generația veche**.
  - **Decizia nr. 61 din 01.03.2024** (doc_id 142648): aprobă Regulamentul curent, **în vigoare
    05.05.2024**, fără dată de abrogare și fără modificări. Aceasta a fost ingerată.
  - **Capcană consemnată:** `REGULAMENT 63/2021` **nu poartă dată de abrogare** în fișa legis.md,
    deși decizia care îl aprobase a fost abrogată. Cine îl deschide după titlu îl poate lua drept
    text curent.
- **Rezultat.** `raw/papers/moldova-legal/DCA-61-2024.md`. Decizia are 2 puncte; Regulamentul
  anexat are **203 puncte**, 8 capitole, 11 secțiuni. `verify_business_law.py`: **FAILURES 0** pe
  toate cele 20 de acte, iar aici integritate de text **PASS, 528 de linii scrise față de 528 de
  referință**. sha256 recalculat: coincide.
- **Ingerat cu zero ancore de articol, deliberat.** Numerotarea **repornește** între decizie
  (pct. 1–2) și anexă (pct. 1–203), deci ancorarea la nivel de punct ar produce duplicate.
  Aceeași decizie ca la `HG-1170-2016`, `HG-1171-2018` și `HG-574-2024`. **Consecință de citare:
  o trimitere la „pct. N din Regulament” NU este ancorată.** Ancorele structurale există, dar
  **secțiunile nu sunt unice**: „Secțiunea 1” apare de trei ori, „Secțiunea a 2-a” de trei ori,
  deci o trimitere la secțiune trebuie să numească și capitolul.
- **Constatarea care corectează ce am scris azi-dimineață.** Pe pagina `COD-174-2018` am
  consemnat că acel cod **nu are nicio regulă** pentru publicitatea la servicii financiare sau
  instrumente derivate. Rămâne adevărat pentru cod. **Regulamentul rezolvă altfel, printr-o
  trimitere generală:** pct. 90 — „În comunicările comerciale audiovizuale nu pot fi prezentate
  produse, servicii sau activități **interzise prin lege**”. Interdicția din art. 4^1 al
  `L-171-2012` fiind legală, difuzorul care transmite o comunicare comercială pentru opțiuni
  binare sau derivate cu levier **încalcă Regulamentul**, deși nici codul, nici Regulamentul nu
  numesc produsele financiare. **Executarea are deci două brațe, nu unul:** CNPF poate cere
  sistarea sub art. 4^1 alin. (6) lit. b), iar Consiliul Audiovizualului poate sancționa
  difuzorul pe temei propriu, sub Capitolul VIII al Regulamentului și art. 84 al codului.
  Coordonarea nu rezultă din texte. Corectat pe pagina codului și în secțiunea M.3 a manifestului.
- **Conținut, pe scurt:** 8 capitole — dispoziții generale și definiții (pct. 4); informarea
  corectă a publicului; protecția minorilor; programe interzise; **Capitolul V, difuzarea
  comunicărilor comerciale audiovizuale**, cu șapte secțiuni; accesul persoanelor cu dizabilități;
  dreptul la replică; sancțiuni. Din secțiunea 1 a cap. V: pct. 91 cere semnalarea telepromovării
  cu mențiunea „Publicitate” sau simbolul „P”, minimum 30 de puncte în format SD; pct. 92
  interzice practicile oculte; pct. 93 interzice serviciile matrimoniale și intime, produsele
  erotice, pornografia și limbajul obscen.
- **Semnalare așteptată, nu defect.** Generatorul de acoperire marchează `DCA-61-2024` drept
  consolidare învechită, 2,3 ani. Este corect mecanic: actul este din 2024 și nemodificat.
  Avertismentul „textul poate fi depășit” este însă real aici, fiindcă un Consiliu își poate
  înlocui propriul regulament fără intervenția Parlamentului — exact ce s-a întâmplat în 2024.
- **Concurență de scriere:** aceeași metodă — ancorare pe închiderea dicționarului `DOCS`, cu
  verificare că nicio cheie nu s-a pierdut (19 înainte, 20 după); contorul din `index.md`
  recalculat din sistemul de fișiere: 86.
- **Regenerat:** `build_inforce_register.py` (398 de fișiere, tot 46 de dispoziții afectate în
  8 acte) și `build_coverage.py` (**39 de acte primare**). `--check` dă „up to date”.
- **Lacune noi, consemnate:** metodologiile conexe ale aceluiași Consiliu nu sunt ingerate —
  Metodologia privind constatarea cazurilor de dezinformare (DCA285/2023) și Metodologia de
  monitorizare a discursului care incită la ură (DCA160/2023). Ambele au apărut în aceeași
  căutare. Nu sunt cerute de lanțul publicității.
- Fișiere atinse: `raw/papers/moldova-legal/DCA-61-2024.md` (nou),
  `raw/papers/moldova-legal/_manifest.md` (secțiunea M), `entities/DCA-61-2024.md` (nou),
  `entities/COD-174-2018.md`, `index.md`, `CLAUDE.md`, `_meta/inforce/*`,
  `_meta/imports/moldova-legal/ingest_business_law.py` (o intrare `DOCS`).

## [2026-09-05] ingest | Legea nr. 64/2010 cu privire la libertatea de exprimare

- Copie de siguranță: `C:\Users\harab\wiki-backups\wiki-2026-09-05-pre-ingest-L64-2010`.
  Verificat pe conținut, excluzând `.obsidian`: **1.144 de fișiere, identice octet cu octet**.
- **Motiv.** Trimisă de `DCA-61-2024`: pct. 199 și 201 spun că dreptul la replică se asigură
  „în condițiile CSMA și a prevederilor Legii nr. 64/2010”, iar acordarea replicii nu împiedică
  adresarea în instanță tot în condițiile acelei legi.
- **doc_id 141515**, LP64/2010 din 23-04-2010, „Modificat”, fără dată de abrogare. Titlu
  neschimbat. Consolidare 2024-01-23, trecută.
- **Verificat pe HTML înainte de a scrie:** `contentdoc` prezent, fără Cloudflare, 2 etichete
  `<sup>` ambele la nivel de alineat, niciun span ridicat prin CSS, fără CUPRINS, 34 de ancore,
  fără duplicate, fără exponenți de articol.
- **Rezultat.** `raw/papers/moldova-legal/L-64-2010.md`, 34 de ancore, numerotare **1–34 fără
  lacune**; 3 capitole, 2 secțiuni. `verify_business_law.py`: **FAILURES 0** pe toate cele 21 de
  acte, iar aici integritate de text **PASS, 269 de linii scrise față de 269 de referință**.
  sha256 recalculat: coincide.
- **Primul test real al contorului reparat azi.** Art. 34 este scris în sursă `Articolul 34`,
  **fără punct**, fiindcă nu are titlu. Contorul de dinainte l-ar fi raportat drept
  „33, range 1-33”, adică o **lacună falsă** la art. 34. Cel reparat dă **34, range 1-34** și îl
  numește pe linia `fara punct dupa numar`. Reparația fusese făcută pe `L-284-2004`; acesta este
  actul care arată că nu era un caz izolat.
- **A cincea configurație a sarcinii probei din același perimetru, și cea mai permisivă.**
  Art. 24: sarcina revine **reclamantului**, cu cinci elemente cumulative, inclusiv că informația
  este în esență falsă și că există prejudiciu. Art. 25 adaugă **șase prezumții, toate în
  favoarea exprimării**: dubiul asupra statutului persoanei se rezolvă spre „persoană publică”,
  asupra interesului spre „interes public”, asupra naturii afirmației spre „judecată de valoare”,
  asupra cuantumului prejudiciului moral spre **1 leu**, asupra bunei-credințe jurnalistice spre
  buna-credință, iar orice alt dubiu **împotriva restricționării** libertății de exprimare.
  Față de `L-171-2012` art. 4^1 alin. (9), `L-62-2022` art. 52 alin. (2) și `L-105-2003` art. 14,
  unde sarcina trece pe profesionist, aceasta merge în direcția dreptului concurenței.
- **Contragreutatea alertei necontestabile, consemnată ca întrebare, nu ca verdict.** Art. 4^1
  alin. (7) din `L-171-2012` publică numele persoanelor fără act permisiv și declară alerta
  „nu poate fi suspendată sau contestată”. Citită lângă legea de față: **pe fond direcțiile
  coincid**, fiindcă art. 25 alin. (2) rezolvă dubiul tot în favoarea interesului public, iar cine
  prestează servicii de investiții fără act permisiv intră ușor în definiția de persoană publică
  de la art. 2; **pe remediu diferă radical**, fiindcă această lege nu suprimă calea de atac, ci
  lasă acțiunea în defăimare cu dezmințire (art. 26), replică (art. 27) și compensație (art. 29).
  **Dacă persoana numită într-o alertă retrasă poate acționa în defăimare nu rezultă din niciunul
  dintre texte** — legea nu limitează expres cine poate fi pârât, iar „defăimare” este definită
  prin răspândirea informației false, fără a distinge după calitatea celui care o răspândește.
  `[de verificat]`
- **Distincția operativă pentru cererile la Consiliul Audiovizualului:** art. 27 alin. (1) leagă
  **replica** de judecățile de valoare fără substrat factologic suficient, nu de relatările false
  de fapte, pentru care remediul este **dezmințirea** (art. 26).
- **Semnalare așteptată:** generatorul de acoperire marchează actul drept consolidare învechită,
  2,6 ani. Corect mecanic — ultima modificare este LP452 din 28.12.23.
- **Concurență de scriere:** ancorare pe închiderea dicționarului `DOCS`, cu verificare că nicio
  cheie nu s-a pierdut (20 înainte, 21 după); contorul din `index.md` recalculat din sistemul de
  fișiere: 87.
- **Regenerat:** `build_inforce_register.py` (399 de fișiere, tot 46 de dispoziții afectate în
  8 acte) și `build_coverage.py` (**40 de acte primare**; rândul `L-64-2010` 34/34). `--check` dă
  „up to date”.
- Fișiere atinse: `raw/papers/moldova-legal/L-64-2010.md` (nou),
  `raw/papers/moldova-legal/_manifest.md` (secțiunea N), `entities/L-64-2010.md` (nou),
  `entities/DCA-61-2024.md`, `entities/COD-174-2018.md`, `index.md`, `CLAUDE.md`,
  `_meta/inforce/*`, `_meta/imports/moldova-legal/ingest_business_law.py` (o intrare `DOCS`).
