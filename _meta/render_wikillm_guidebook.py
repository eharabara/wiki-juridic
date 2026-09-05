from pathlib import Path
import json
import re
import sys

import markdown
from weasyprint import HTML, CSS

BASE = Path(r"C:\Users\harab\wiki\_meta")
MD_PATH = BASE / "wikillm-guidebook-for-moldova-policy-work.md"
HTML_PATH = BASE / "wikillm-guidebook-for-moldova-policy-work.html"
PDF_PATH = BASE / "wikillm-guidebook-for-moldova-policy-work.pdf"
AUDIT_PATH = BASE / "wikillm-guidebook-for-moldova-policy-work-audit.json"

md_text = MD_PATH.read_text(encoding="utf-8")

# Extract title and metadata for a designed cover.
lines = md_text.splitlines()
title = lines[0].lstrip("# ").strip() if lines and lines[0].startswith("# ") else "WikiLLM Guidebook"
subtitle = "A practical operating manual for your Moldova policy, EU accession, economic intelligence, and dashboard knowledge base"
prepared_for = "Eugeniu Harabara"
date = "2026-07-08"
wiki_location = r"C:\Users\harab\wiki"

# Remove first title block up to first horizontal rule, because cover recreates it.
body_md = md_text
if "---" in md_text:
    parts = md_text.split("---", 1)
    body_md = parts[1].lstrip()

html_body = markdown.markdown(
    body_md,
    extensions=["extra", "toc", "sane_lists", "smarty", "nl2br"],
    output_format="html5",
)

# Post-process simple code blocks for nicer labels where possible.
html_body = re.sub(r"<table>", '<table class="data-table">', html_body)

css = r'''
@page {
  size: A4;
  margin: 17mm 16mm 19mm 16mm;
  @bottom-left {
    content: "WikiLLM Guidebook — Moldova Policy & Economic Intelligence";
    font-family: "Segoe UI", Arial, sans-serif;
    font-size: 8.5pt;
    color: #64748b;
  }
  @bottom-right {
    content: counter(page);
    font-family: "Segoe UI", Arial, sans-serif;
    font-size: 9pt;
    color: #0f172a;
  }
}

@page cover {
  margin: 0;
  @bottom-left { content: none; }
  @bottom-right { content: none; }
}

@page chapter {
  margin: 18mm 16mm 20mm 16mm;
}

:root {
  --navy: #0f2742;
  --navy-2: #17395c;
  --teal: #0f9f9a;
  --cyan: #2cb7c9;
  --gold: #c9972b;
  --ink: #172033;
  --muted: #5c6b82;
  --light: #f4f7fb;
  --paper: #fffdfa;
  --line: #d9e2ec;
  --soft-teal: #e8f7f6;
  --soft-gold: #fff5da;
}

html, body {
  font-family: "Segoe UI", Arial, sans-serif;
  color: var(--ink);
  line-height: 1.45;
  font-size: 10.4pt;
  background: white;
}

.cover {
  page: cover;
  height: 297mm;
  position: relative;
  overflow: hidden;
  color: white;
  background:
    radial-gradient(circle at 82% 12%, rgba(44,183,201,0.65) 0, rgba(44,183,201,0.1) 26%, transparent 44%),
    linear-gradient(140deg, #071827 0%, #0f2742 44%, #15456c 72%, #0f9f9a 124%);
}

.cover::before {
  content: "";
  position: absolute;
  inset: 17mm;
  border: 1px solid rgba(255,255,255,0.26);
}

.cover::after {
  content: "";
  position: absolute;
  right: -32mm;
  bottom: -38mm;
  width: 132mm;
  height: 132mm;
  border-radius: 50%;
  border: 22mm solid rgba(255,255,255,0.07);
}

.cover-inner {
  position: absolute;
  left: 23mm;
  right: 23mm;
  top: 32mm;
  bottom: 25mm;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.kicker {
  text-transform: uppercase;
  letter-spacing: 0.18em;
  font-size: 9pt;
  color: #a9f4ef;
  font-weight: 700;
}

.cover h1 {
  font-size: 34pt;
  line-height: 1.05;
  max-width: 165mm;
  margin: 16mm 0 5mm 0;
  font-weight: 800;
  letter-spacing: -0.03em;
}

.cover .subtitle {
  font-size: 14pt;
  line-height: 1.35;
  color: #d9f5f3;
  max-width: 160mm;
  margin-top: 6mm;
}

.cover-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 5mm;
  margin-top: 18mm;
}

.cover-card {
  background: rgba(255,255,255,0.09);
  border: 1px solid rgba(255,255,255,0.24);
  padding: 5mm;
  border-radius: 5mm;
}

.cover-card strong {
  display: block;
  color: #a9f4ef;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-size: 8pt;
  margin-bottom: 1.5mm;
}

.cover-meta {
  display: grid;
  grid-template-columns: 1.2fr 1fr;
  gap: 7mm;
  align-items: end;
  color: #d9f5f3;
  font-size: 10pt;
}

body > h1, .content h1 {
  break-before: page;
  color: var(--navy);
  font-size: 22pt;
  line-height: 1.12;
  margin: 0 0 7mm 0;
  padding-bottom: 3mm;
  border-bottom: 2px solid var(--teal);
  letter-spacing: -0.02em;
}

.content h2 {
  color: var(--navy-2);
  font-size: 15pt;
  margin: 8mm 0 3mm 0;
  break-after: avoid;
}

.content h3 {
  color: var(--navy-2);
  font-size: 12pt;
  margin: 6mm 0 2mm 0;
  break-after: avoid;
}

.content p {
  margin: 0 0 3.2mm 0;
}

.content a {
  color: var(--teal);
  text-decoration: none;
}

.content strong {
  color: #0f2742;
}

.content blockquote {
  margin: 5mm 0;
  padding: 4.5mm 5mm;
  border-left: 4px solid var(--teal);
  background: var(--soft-teal);
  border-radius: 0 4mm 4mm 0;
  color: #17395c;
  font-weight: 600;
}

.content ul, .content ol {
  margin-top: 1.5mm;
  margin-bottom: 4mm;
  padding-left: 6mm;
}

.content li {
  margin-bottom: 1.4mm;
}

pre {
  background: #0b1624;
  color: #e5f4ff;
  padding: 4mm;
  border-radius: 4mm;
  overflow-wrap: anywhere;
  white-space: pre-wrap;
  font-size: 8.1pt;
  line-height: 1.35;
  break-inside: avoid;
}

code {
  font-family: "Cascadia Mono", Consolas, monospace;
  font-size: 8.5pt;
  background: #eef5f7;
  color: #0f4f68;
  padding: 0.4mm 1mm;
  border-radius: 1.5mm;
}

pre code {
  background: transparent;
  color: inherit;
  padding: 0;
  border-radius: 0;
}

table.data-table, table {
  width: 100%;
  border-collapse: collapse;
  margin: 5mm 0 6mm 0;
  font-size: 8.7pt;
  break-inside: avoid;
}

th {
  background: var(--navy);
  color: white;
  padding: 2.7mm 2.5mm;
  text-align: left;
  font-weight: 700;
  border: 1px solid var(--navy);
}

td {
  padding: 2.5mm;
  border: 1px solid var(--line);
  vertical-align: top;
}

tr:nth-child(even) td {
  background: #f8fbfd;
}

hr {
  border: 0;
  height: 1px;
  background: var(--line);
  margin: 8mm 0;
}

.toc-card {
  break-before: page;
  background: var(--light);
  border: 1px solid var(--line);
  border-radius: 6mm;
  padding: 7mm;
  margin: 5mm 0 8mm 0;
}

.toc-card h2 {
  margin-top: 0;
}

.strategy-strip {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 4mm;
  margin: 5mm 0 7mm 0;
}

.strategy-box {
  background: var(--paper);
  border: 1px solid var(--line);
  border-top: 3px solid var(--teal);
  padding: 4mm;
  border-radius: 4mm;
  min-height: 28mm;
}

.strategy-box strong {
  display: block;
  margin-bottom: 1.5mm;
}

.footer-note {
  margin-top: 8mm;
  padding: 4mm;
  background: var(--soft-gold);
  border-left: 4px solid var(--gold);
  border-radius: 0 4mm 4mm 0;
  color: #5f4610;
}

.badge-row {
  display: flex;
  gap: 3mm;
  flex-wrap: wrap;
  margin-top: 5mm;
}

.badge {
  padding: 1.8mm 3mm;
  border-radius: 999px;
  background: rgba(255,255,255,0.12);
  border: 1px solid rgba(255,255,255,0.24);
  color: #e6fffb;
  font-size: 8.5pt;
}

.content {
  counter-reset: h1count;
}

.content h1::before {
  counter-increment: h1count;
}
'''

cover = f'''
<section class="cover">
  <div class="cover-inner">
    <div>
      <div class="kicker">WikiLLM Operating Manual</div>
      <h1>{title}</h1>
      <div class="subtitle">{subtitle}</div>
      <div class="badge-row">
        <span class="badge">Moldova economic policy</span>
        <span class="badge">EU accession</span>
        <span class="badge">Composite indicators</span>
        <span class="badge">Donor architecture</span>
        <span class="badge">Policy evidence</span>
      </div>
      <div class="cover-grid">
        <div class="cover-card"><strong>Core idea</strong>Raw sources are preserved as evidence; wiki pages become reusable synthesis.</div>
        <div class="cover-card"><strong>Primary use</strong>Support reports, briefs, dashboards, programme design, and policy advice.</div>
        <div class="cover-card"><strong>Knowledge base</strong>{wiki_location}</div>
        <div class="cover-card"><strong>Operating rhythm</strong>Ingest → update → cross-link → query → audit → reuse.</div>
      </div>
    </div>
    <div class="cover-meta">
      <div>
        <strong>Prepared for</strong><br>{prepared_for}<br><br>
        <strong>Date</strong><br>{date}
      </div>
      <div>
        A practical guidebook for building a durable, source-backed policy intelligence system.
      </div>
    </div>
  </div>
</section>
'''

intro_boxes = '''
<div class="toc-card">
  <h2>Practical operating model</h2>
  <div class="strategy-strip">
    <div class="strategy-box"><strong>1. Preserve evidence</strong>Keep raw sources immutable and traceable in <code>raw/</code>.</div>
    <div class="strategy-box"><strong>2. Compile knowledge</strong>Update entity, concept, comparison, and query pages.</div>
    <div class="strategy-box"><strong>3. Reuse synthesis</strong>Generate briefs, dashboards, reports, and programme tables from wiki-backed knowledge.</div>
  </div>
  <div class="footer-note">Best habit: before drafting any serious output, ask the agent to read <code>SCHEMA.md</code>, <code>index.md</code>, recent <code>log.md</code>, and the relevant pages.</div>
</div>
'''

html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<style>{css}</style>
</head>
<body>
{cover}
<main class="content">
{intro_boxes}
{html_body}
</main>
</body>
</html>
'''

HTML_PATH.write_text(html, encoding="utf-8")

HTML(filename=str(HTML_PATH)).write_pdf(str(PDF_PATH), stylesheets=[CSS(string=css)])

# Verify with PyMuPDF.
import fitz
pdf = fitz.open(str(PDF_PATH))
text = "\n".join(page.get_text("text") for page in pdf)
audit = {
    "markdown_path": str(MD_PATH),
    "html_path": str(HTML_PATH),
    "pdf_path": str(PDF_PATH),
    "markdown_bytes": MD_PATH.stat().st_size,
    "html_bytes": HTML_PATH.stat().st_size,
    "pdf_bytes": PDF_PATH.stat().st_size,
    "pdf_pages": pdf.page_count,
    "first_page_size_points": [round(pdf[0].rect.width, 2), round(pdf[0].rect.height, 2)] if pdf.page_count else None,
    "text_chars_extracted_from_pdf": len(text),
    "required_phrases_present": {
        "Moldova economic policy": "Moldova economic policy" in text,
        "EU accession": "EU accession" in text,
        "composite indicators": "composite indicators" in text.lower(),
        "donor coordination": "donor coordination" in text.lower(),
        "C:\\Users\\harab\\wiki": r"C:\Users\harab\wiki" in text,
    },
}
AUDIT_PATH.write_text(json.dumps(audit, indent=2), encoding="utf-8")

# Render cover and one interior page for visual spot checks.
for page_index, name in [(0, "cover"), (min(4, pdf.page_count-1), "interior")]:
    if page_index >= 0:
        page = pdf[page_index]
        pix = page.get_pixmap(matrix=fitz.Matrix(1.5, 1.5), alpha=False)
        pix.save(str(BASE / f"wikillm-guidebook-{name}-preview.png"))

print(json.dumps(audit, indent=2))
