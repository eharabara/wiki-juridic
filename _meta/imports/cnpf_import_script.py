from pathlib import Path
import shutil, hashlib, json, re, datetime, yaml

SRC = Path(r"C:\Users\harab\Desktop\cnpf-wiki-ro")
DST = Path(r"C:\Users\harab\wiki")
TODAY = datetime.date.today().isoformat()
STAMP = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
BACKUP_ROOT = Path(r"C:\Users\harab\wiki-backups")
BACKUP = BACKUP_ROOT / f"wiki-before-cnpf-import-{STAMP}"
IMPORT_META = DST / "_meta" / "imports" / "cnpf"
SOURCE_WIKI_META = IMPORT_META / "source-wiki"
RAW_DST = DST / "raw" / "papers" / "cnpf"

NEW_SCHEMA_TAGS_SECTION = """
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
""".strip()

REQUIRED = [SRC / "CLAUDE.md", SRC / "prompts.md", SRC / "raw", SRC / "wiki", DST / "SCHEMA.md", DST / "index.md", DST / "log.md"]
missing = [str(p) for p in REQUIRED if not p.exists()]
if missing:
    raise SystemExit("Missing required paths: " + json.dumps(missing, ensure_ascii=False))

# 1) Backup current wiki before any write.
BACKUP_ROOT.mkdir(parents=True, exist_ok=True)
if BACKUP.exists():
    raise SystemExit(f"Backup path already exists: {BACKUP}")
shutil.copytree(DST, BACKUP, ignore=shutil.ignore_patterns("__pycache__"))

# 2) Ensure target directories.
for d in [IMPORT_META, SOURCE_WIKI_META, RAW_DST, DST / "entities", DST / "concepts", DST / "comparisons"]:
    d.mkdir(parents=True, exist_ok=True)

# 3) Extend schema with needed tags if not already present.
schema_path = DST / "SCHEMA.md"
schema = schema_path.read_text(encoding="utf-8")
if "### Financial services, legal approximation, and CNPF" not in schema:
    marker = "### Evidence, indicators, and methods\n"
    if marker not in schema:
        raise SystemExit("Could not find schema insertion marker")
    schema = schema.replace(marker, NEW_SCHEMA_TAGS_SECTION + "\n\n" + marker)
    schema_path.write_text(schema, encoding="utf-8")

# Helpers.
def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def first_url(text: str) -> str:
    m = re.search(r"https?://\S+", text)
    return m.group(0).rstrip(").,;]") if m else ""

def yaml_list(items):
    return "[" + ", ".join(items) + "]"

def page_title(text: str, fallback: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback

def slug_summary(title: str) -> str:
    t = re.sub(r"^[A-Za-z0-9_-]+\s+—\s+", "", title).strip()
    return t[:180]

def clean_anchor_paths(text: str) -> str:
    # Convert Romanian legal anchors from old raw/ location to the imported raw path.
    def repl(m):
        ident = m.group(1)
        rest = m.group(2) or ""
        if ident.endswith(".md"):
            ident_file = ident
        else:
            ident_file = f"{ident}.md"
        return f"[raw/papers/cnpf/{ident_file}{rest}]"
    text = re.sub(r"\[raw/([A-Za-z0-9_-]+)([^\]]*)\]", repl, text)
    text = text.replace("[raw/ID]", "[raw/papers/cnpf/ID.md]")
    return text

def rewrite_wikilinks(text: str) -> str:
    return text.replace("[[_transposition-matrix]]", "[[cnpf-transposition-matrix]]")

def infer_tags_and_confidence(file_name: str, title: str, body: str, ptype: str):
    low = (title + "\n" + body).lower()
    tags = []
    def add(*xs):
        for x in xs:
            if x not in tags:
                tags.append(x)
    add("moldova")
    if ptype == "entity":
        add("entity")
        if file_name.startswith("L-") or file_name.startswith("REG-"):
            add("legal-act", "legal-source", "legal-approximation")
    elif ptype == "concept":
        add("concept", "eu", "eu-acquis", "transposition", "legal-approximation")
    elif ptype == "comparison":
        add("comparison", "eu", "eu-acquis", "transposition", "legal-approximation")

    if "cnpf" in low or "comisia națională a pieței financiare" in low:
        add("cnpf")
    if "bnm" in low or "banca națională" in low:
        add("bnm")
    if any(s in low for s in ["piața de capital", "piata de capital", "mifid", "mar ", "prospect", "ucits", "aifmd", "crowdfunding", "finanțare participativă", "finantare participativa"]):
        add("financial-services", "capital-market")
    if any(s in low for s in ["valori mobiliare", "instrumente financiare", "depozitarul central", "dcu", "emitenți", "emitenti"]):
        add("securities")
    if any(s in low for s in ["asigur", "mtpl", "rca", "solvency"]):
        add("insurance")
    if any(s in low for s in ["creditare nebancară", "creditare nebancara", "organizațiile de creditare", "ocn", "aeî", "asociațiile de economii", "asociatiile de economii"]):
        add("non-bank-credit")
    if any(s in low for s in ["birourile istoriilor de credit", "birou de credit", "credit bureau"]):
        add("credit-bureau")
    if any(s in low for s in ["pensii", "iorp"]):
        add("pensions")
    if any(s in low for s in ["societățile pe acțiuni", "societatile pe actiuni", "company law", "dreptul societăților", "dreptul societatilor", "srd ii"]):
        add("company-law")
    if any(s in low for s in ["consumator", "consumer credit", "protecție-consumatori", "protectie-consumatori"]):
        add("consumer-protection")
    if any(s in low for s in ["spălării banilor", "spalarii banilor", "aml", "finanțării terorismului", "finantarii terorismului"]):
        add("aml-cft")
    if any(s in low for s in ["supravegh", "mandat", "autoritate"]):
        add("financial-supervision")
    if ptype in {"concept", "comparison"}:
        add("financial-services")
    if "[de verificat]" in low or "de verificat" in low:
        confidence = "medium"
    else:
        confidence = "high" if ptype == "entity" and file_name.startswith("L-") else "medium"
    return tags, confidence

raw_files = sorted((SRC / "raw").glob("*.md"))
raw_name_set = {p.name for p in raw_files}

# 4) Copy raw sources with target raw frontmatter; preserve original body verbatim after frontmatter.
raw_copied = []
for p in raw_files:
    if p.name == "_manifest.md":
        continue
    body = p.read_text(encoding="utf-8", errors="replace")
    url = first_url(body) or str(p)
    publisher = "EUR-Lex" if p.name.startswith("UE-") else "legis.md / CNPF legal source note"
    frontmatter = "\n".join([
        "---",
        f"source_url: {url}",
        f"source_path: {str(p)}",
        f"ingested: {TODAY}",
        f"sha256: {sha256_text(body)}",
        "source_type: legal-text",
        f"publisher: {publisher}",
        "language: ro",
        "imported_from: cnpf-wiki-ro",
        "---",
        "",
    ])
    out = RAW_DST / p.name
    if out.exists():
        raise SystemExit(f"Collision before raw copy: {out}")
    out.write_text(frontmatter + body, encoding="utf-8")
    raw_copied.append(out)

# 5) Preserve source governance and source wiki files.
meta_copied = []
for src, name in [
    (SRC / "CLAUDE.md", "source-CLAUDE.md"),
    (SRC / "prompts.md", "source-prompts.md"),
    (SRC / "raw" / "_manifest.md", "source-raw-manifest.md"),
    (SRC / "wiki" / "_lint-report.md", "source-lint-report.md"),
]:
    if src.exists():
        out = IMPORT_META / name
        if out.exists():
            raise SystemExit(f"Collision before meta copy: {out}")
        shutil.copy2(src, out)
        meta_copied.append(out)

pdf_src = SRC / "_transposition-matrix.pdf"
if pdf_src.exists():
    out = IMPORT_META / "source-transposition-matrix.pdf"
    if out.exists():
        raise SystemExit(f"Collision before PDF copy: {out}")
    shutil.copy2(pdf_src, out)
    meta_copied.append(out)

for p in sorted((SRC / "wiki").glob("*.md")):
    out = SOURCE_WIKI_META / p.name
    if out.exists():
        raise SystemExit(f"Collision before source wiki preservation: {out}")
    shutil.copy2(p, out)
    meta_copied.append(out)

# 6) Convert active wiki pages into the main schema.
# Mapping from old page stem to new page stem for wikilink rewrite.
stem_map = {"_transposition-matrix": "cnpf-transposition-matrix"}
# Other stems stay the same to preserve concise legal references.
converted = []
index_entries = {"Entities": [], "Concepts": [], "Comparisons": [], "Queries": []}

# Raw source candidates for frontmatter.
raw_target_rel_by_name = {p.name: f"raw/papers/cnpf/{p.name}" for p in raw_copied}

def sources_for(file_name: str, title: str, text: str, ptype: str):
    sources = []
    stem = Path(file_name).stem
    same = f"{stem}.md"
    if same in raw_target_rel_by_name:
        sources.append(raw_target_rel_by_name[same])
    if file_name == "REG-ICF.md" and "L-171-2012.md" in raw_target_rel_by_name:
        sources.append(raw_target_rel_by_name["L-171-2012.md"])
    # Include law raw files linked in the page.
    for law in sorted(set(re.findall(r"\[\[(L-[0-9-]+)\]\]", text))):
        fname = f"{law}.md"
        if fname in raw_target_rel_by_name and raw_target_rel_by_name[fname] not in sources:
            sources.append(raw_target_rel_by_name[fname])
    # Include EU raw files whose act identifiers appear in the page.
    for rawname, rel in sorted(raw_target_rel_by_name.items()):
        if not rawname.startswith("UE-"):
            continue
        stem = rawname[:-3]
        parts = stem.split("-")[1:]
        forms = []
        if len(parts) == 2:
            a, b = parts
            if len(a) == 4:
                forms.extend([f"{a}/{b}", f"{a}-{b}"])
            else:
                forms.extend([f"{a}/{b}", f"{a}-{b}"])
        if any(f in text for f in forms):
            if rel not in sources:
                sources.append(rel)
    return sources[:8]

for p in sorted((SRC / "wiki").glob("*.md")):
    if p.name == "_lint-report.md":
        continue
    original = p.read_text(encoding="utf-8", errors="replace")
    title = page_title(original, p.stem)
    if p.name == "_transposition-matrix.md":
        ptype = "comparison"
        out = DST / "comparisons" / "cnpf-transposition-matrix.md"
        section = "Comparisons"
        link_stem = "cnpf-transposition-matrix"
    elif p.name.startswith("acquis-"):
        ptype = "concept"
        out = DST / "concepts" / p.name
        section = "Concepts"
        link_stem = p.stem
    else:
        ptype = "entity"
        out = DST / "entities" / p.name
        section = "Entities"
        link_stem = p.stem
    if out.exists():
        raise SystemExit(f"Collision before page conversion: {out}")
    body = original
    body = clean_anchor_paths(body)
    body = rewrite_wikilinks(body)
    tags, confidence = infer_tags_and_confidence(p.name, title, body, ptype)
    sources = sources_for(p.name, title, body, ptype)
    fm = {
        "title": title,
        "created": TODAY,
        "updated": TODAY,
        "type": ptype,
        "tags": tags,
        "sources": sources,
        "confidence": confidence,
        "imported_from": str(p),
    }
    front = "---\n" + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False).strip() + "\n---\n\n"
    out.write_text(front + body, encoding="utf-8")
    converted.append(out)
    index_entries[section].append((link_stem, slug_summary(title)))

# 7) Rebuild index.md with imported pages.
def sorted_entries(entries):
    return sorted(entries, key=lambda x: x[0].lower())

total_pages = sum(len(v) for v in index_entries.values())
index_lines = [
    "# Wiki Index",
    "",
    "> Content catalog. Every wiki page is listed under its type with a one-line summary.",
    "> Read this first to find relevant pages for any query.",
    f"> Last updated: {TODAY} | Total pages: {total_pages}",
    "",
    "## Entities",
    "",
]
for stem, summary in sorted_entries(index_entries["Entities"]):
    index_lines.append(f"- [[{stem}]] — {summary}")
index_lines += ["", "## Concepts", ""]
for stem, summary in sorted_entries(index_entries["Concepts"]):
    index_lines.append(f"- [[{stem}]] — {summary}")
index_lines += ["", "## Comparisons", ""]
for stem, summary in sorted_entries(index_entries["Comparisons"]):
    index_lines.append(f"- [[{stem}]] — {summary}")
index_lines += ["", "## Queries", "", "<!-- No query pages yet -->", ""]
(DST / "index.md").write_text("\n".join(index_lines), encoding="utf-8")

# 8) Append log entry.
log_path = DST / "log.md"
log = log_path.read_text(encoding="utf-8")
entry = f"""
## [{TODAY}] ingest | CNPF legal/acquis wiki imported

- Source folder: `C:\\Users\\harab\\Desktop\\cnpf-wiki-ro`.
- Backup created before import: `{BACKUP}`.
- Raw legal/acquis sources copied: {len(raw_copied)} files → `raw/papers/cnpf/`.
- Active wiki pages converted: {len(converted)} files → `entities/`, `concepts/`, `comparisons/`.
- Original CNPF governance/source files preserved under `_meta/imports/cnpf/`.
- Schema extended with CNPF, financial-services, legal/acquis, and transposition tags.
- Legal import rule preserved: article-level anchors and `[de verificat]` markers remain visible; no legal contradiction was resolved silently.
""".strip()
if entry not in log:
    log_path.write_text(log.rstrip() + "\n\n" + entry + "\n", encoding="utf-8")

# 9) Post-import audit.
def read_active_pages():
    active = []
    for sub in ["entities", "concepts", "comparisons", "queries"]:
        d = DST / sub
        if d.exists():
            active.extend(sorted(d.glob("*.md")))
    return active

def parse_frontmatter(text):
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end < 0:
        return None
    try:
        return yaml.safe_load(text[4:end]) or {}
    except Exception:
        return None

schema_now = schema_path.read_text(encoding="utf-8")
allowed_tags = set(re.findall(r"^\- ([a-z0-9-]+)\s*$", schema_now, flags=re.M))
active_pages = read_active_pages()
stems = {p.stem for p in active_pages}
missing_fm=[]; missing_fields=[]; invalid_tags=[]; broken_links=[]; index_missing=[]
index_text=(DST/"index.md").read_text(encoding="utf-8")
for p in active_pages:
    txt=p.read_text(encoding="utf-8")
    fm=parse_frontmatter(txt)
    rel=str(p.relative_to(DST)).replace('\\','/')
    if not fm:
        missing_fm.append(rel); continue
    for field in ["title", "created", "updated", "type", "tags", "sources"]:
        if field not in fm:
            missing_fields.append({"file": rel, "field": field})
    for tag in fm.get("tags", []) or []:
        if tag not in allowed_tags:
            invalid_tags.append({"file": rel, "tag": tag})
    for link in re.findall(r"\[\[([^\]]+)\]\]", txt):
        target=link.split('|')[0].split('#')[0].strip()
        if target and target not in stems:
            broken_links.append({"file": rel, "target": target})
    if f"[[{p.stem}]]" not in index_text and p.parent.name != "queries":
        index_missing.append(rel)

audit = {
    "date": TODAY,
    "source_folder": str(SRC),
    "target_wiki": str(DST),
    "backup": str(BACKUP),
    "raw_sources_copied": len(raw_copied),
    "active_pages_converted": len(converted),
    "meta_files_preserved": len(meta_copied),
    "active_page_count_after_import": len(active_pages),
    "index_total_pages": total_pages,
    "missing_frontmatter": missing_fm,
    "missing_required_fields": missing_fields,
    "invalid_tags": invalid_tags,
    "broken_wikilinks": broken_links,
    "index_missing": index_missing,
    "new_schema_section_added": "### Financial services, legal approximation, and CNPF" in schema_path.read_text(encoding="utf-8"),
    "files_created": [str(p.relative_to(DST)).replace('\\','/') for p in raw_copied + converted + meta_copied],
}
(AUDIT_PATH := IMPORT_META / "import-audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(audit, ensure_ascii=False, indent=2))
