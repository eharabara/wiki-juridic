# BNM official-source corpus — master manifest

## Clear separation

| Branch | Source-register basis | Preserved files | Local navigation |
|---|---|---:|---|
| Legal documents | BNM Laws and Regulations catalogues | 204 | [legal/_manifest.md](./legal/_manifest.md) |
| Formal reports | BNM Annual Report, Inflation Report and Financial Stability Report catalogues | 101 | [reports/_manifest.md](./reports/_manifest.md) |

The legal branch contains BNM catalogue-record attachments from the legal register; the report branch contains attachments from BNM’s three explicitly labelled formal-report series. This is a **catalogue-origin classification**. Some parent pages expose related or general attachments, so individual file relevance remains traceable to its parent BNM record in `_manifest.csv`.

## Romanian texts of the banking laws (added 2026-09-05)

`legal-ro/` holds the consolidated Romanian text from legis.md of six banking laws that this corpus
otherwise had only as unofficial English translations: 202/2017, 548/1995, 114/2012, 232/2016,
62/2008 and 160/2023 (which replaced 575/2003). These are the citable texts; the English files in
`legal/documents/` only locate a provision (decision D2). Branch manifest: [legal-ro/_manifest.md](./legal-ro/_manifest.md).

## Procedurile DCU (added 2026-09-09)

`dcu/` holds the Romanian text of eight of the nine current Procedures of the Central Securities
Depository, taken as PDFs from dcu.md (acts of the DCU executive committee under art. 4(2) of the
DCU Rules, not BNM acts, hence a folder of their own). The ninth, the settlement procedure that
covers succession, is image-only and awaits OCR; its original is archived with its hash. No
anchors: the procedures are numbered in points. Branch manifest: [dcu/_manifest.md](./dcu/_manifest.md).

## Paths

- Legal originals: `legal/original/`; legal Markdown extracts: `legal/documents/`.
- Report originals: `reports/original/`; report Markdown extracts: `reports/documents/`.
- Master machine-readable manifest: `_manifest.csv` (all 305 files, with `kind`, root-relative paths and hashes).
- Branch manifests: `legal/_manifest.csv` and `reports/_manifest.csv` (branch-relative paths).

## Official-register scope

The parent BNM catalogues identify 115 legal-register entries (16 laws; 99 regulations/decisions/norms/methodologies) and 93 formal-report-series records (25 Annual Reports; 61 Inflation Reports; 7 Financial Stability Reports). The preservation branches contain more files than source records because BNM sometimes supplies multiple formats or attachments.
