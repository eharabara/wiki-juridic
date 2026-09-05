from pathlib import Path
import re, json, hashlib, datetime

try:
    import yaml
except Exception:
    yaml = None

ROOT = Path(r"C:\Users\harab\wiki")
TODAY = datetime.date.today().isoformat()
STAMP = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
OUT_DIR = ROOT / '_meta' / 'lint'
OUT_DIR.mkdir(parents=True, exist_ok=True)
REPORT = OUT_DIR / f'cnpf-legal-lint-{TODAY}.md'
JSON_OUT = OUT_DIR / f'cnpf-legal-lint-{TODAY}.json'
RAW_DIR = ROOT / 'raw' / 'papers' / 'cnpf'

LEGAL_EXPECTED_MANDATE = {
    'L-1-2018': ['BNM', 'CNPF-rezidual'],
    'L-92-2022': ['BNM', 'CNPF-rezidual'],
    'L-106-2022': ['BNM', 'CNPF-rezidual'],
    'L-139-2007': ['BNM', 'CNPF-rezidual'],
    'L-122-2008': ['BNM'],
    'L-234-2016': ['BNM'],
    'L-178-2020': ['BNM'],
    'L-171-2012': ['CNPF'],
    'L-192-1998': ['CNPF'],
    'L-2-2020': ['CNPF'],
    'L-181-2023': ['CNPF'],
    'L-198-2020': ['CNPF'],
    'L-308-2017': ['CNPF'],
    'REG-ICF': ['CNPF'],
    'L-1134-1997': ['partajat'],
}

CLAIM_KEYWORDS = re.compile(
    r'(lege|directiv|regulament|cnpf|bnm|mandat|statut|transpun|acquis|autoriza|supravegh|pia[țt]a|emitent|investitor|prospect|decont|asigur|credit|fond|contraven|capital|minim|acoper|obliga|cerin[țt]|abrog|modific|aplic|institu|sistem|protec|competent|lacun|alini|cluster|capitol|valo[ri]|instrument|pruden[țt]ial)',
    re.I
)
SKIP_SECTIONS = {
    'Referințe încrucișate', 'Întrebări deschise', 'Surse EUR-Lex RO ingerate',
    'Limite ale extractului', 'Jurnal de modificări', 'Contradicții / întrebări deschise'
}
ALLOWED_STATUS_TERMS = ['complet', 'parțial', 'partial', 'planificat', 'necunoscut', 'învechit', 'invechit', 'de verificat']

def parse_frontmatter(text):
    if not text.startswith('---\n'):
        return {}, text
    end = text.find('\n---\n', 4)
    if end < 0:
        return {}, text
    fm_text = text[4:end]
    body = text[end+5:]
    if yaml:
        try:
            return yaml.safe_load(fm_text) or {}, body
        except Exception:
            return {'_parse_error': True}, body
    return {}, body

def dump_frontmatter(fm):
    if yaml:
        return '---\n' + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False).strip() + '\n---\n\n'
    return ''

def read_text(path):
    return path.read_text(encoding='utf-8', errors='replace')

def rel(path):
    return str(path.relative_to(ROOT)).replace('\\', '/')

def active_pages():
    pages = []
    for sub in ['entities', 'concepts', 'comparisons', 'queries']:
        pages.extend(sorted((ROOT/sub).glob('*.md')))
    return pages

def allowed_tags():
    schema = read_text(ROOT/'SCHEMA.md')
    return set(re.findall(r'^- ([a-z0-9-]+)\s*$', schema, flags=re.M))

def title_for(path, fm, body):
    if fm.get('title'):
        return str(fm['title'])
    for line in body.splitlines():
        if line.startswith('# '): return line[2:].strip()
    return path.stem

def strip_code_spans(line):
    return re.sub(r'`[^`]*`', '', line)

def line_section(body_lines, i):
    for j in range(i, -1, -1):
        line = body_lines[j]
        m = re.match(r'^##\s+(.+?)\s*$', line)
        if m:
            return m.group(1).strip()
    return ''

def extract_raw_refs(line):
    refs=[]
    for m in re.finditer(r'\[raw/papers/cnpf/([^\]\s]+\.md)(?:\s+([^\]]+))?\]', line):
        refs.append({'file': m.group(1), 'detail': (m.group(2) or '').strip(), 'raw': m.group(0)})
    return refs

def extract_art_numbers(detail):
    nums=[]
    for m in re.finditer(r'art\.?\s*([0-9]+[a-zA-Z]?|[IVXLCDM]+)', detail, flags=re.I):
        nums.append(m.group(1))
    return nums

def article_exists(raw_text, art):
    a = re.escape(str(art))
    patterns = [
        rf'\bArt\.?\s*{a}\b',
        rf'\bArticolul\s+{a}\b',
        rf'\[.*?art\.?\s*{a}.*?\]',
        rf'##\s+Art\.?\s*{a}\b',
        rf'###\s+Articolul\s+{a}\b',
    ]
    return any(re.search(p, raw_text, flags=re.I) for p in patterns)

def body_without_frontmatter(path):
    fm, body = parse_frontmatter(read_text(path))
    return fm, body

pages = active_pages()
stems = {p.stem for p in pages}
allowed = allowed_tags()
index_text = read_text(ROOT/'index.md')
manifest_text = read_text(RAW_DIR/'_manifest.md') if (RAW_DIR/'_manifest.md').exists() else ''

issues = {
    'missing_frontmatter': [],
    'missing_required_fields': [],
    'invalid_tags': [],
    'missing_or_invalid_sources': [],
    'broken_wikilinks': [],
    'orphan_pages': [],
    'index_missing': [],
    'raw_missing_frontmatter': [],
    'raw_sha_drift': [],
    'raw_manifest_missing': [],
    'article_anchor_missing_target': [],
    'page_level_raw_refs': [],
    'potential_unanchored_claims': [],
    'mandate_conflicts': [],
    'missing_mandate_line': [],
    'stale_consolidation': [],
    'missing_consolidation_date': [],
    'acquis_without_moldovan_anchor': [],
    'acquis_without_eurlex_raw': [],
    'acquis_status_missing_or_unclear': [],
    'verification_markers': [],
    'large_pages': [],
    'contested_or_contradiction_markers': [],
}

# Graph and frontmatter checks.
inbound = {p.stem: 0 for p in pages}
page_meta = {}
for p in pages:
    txt = read_text(p)
    fm, body = parse_frontmatter(txt)
    page_meta[p.stem] = {'path': rel(p), 'fm': fm, 'body': body, 'title': title_for(p, fm, body)}
    r = rel(p)
    if not fm:
        issues['missing_frontmatter'].append(r)
    else:
        for field in ['title','created','updated','type','tags','sources']:
            if field not in fm:
                issues['missing_required_fields'].append({'file': r, 'field': field})
        for tag in fm.get('tags') or []:
            if tag not in allowed:
                issues['invalid_tags'].append({'file': r, 'tag': tag})
        for source in fm.get('sources') or []:
            if isinstance(source, str) and source.startswith('raw/'):
                if not (ROOT/source).exists():
                    issues['missing_or_invalid_sources'].append({'file': r, 'source': source, 'problem': 'path does not exist'})
    if f'[[{p.stem}]]' not in index_text:
        issues['index_missing'].append(r)
    for link in re.findall(r'\[\[([^\]]+)\]\]', txt):
        target = link.split('|')[0].split('#')[0].strip()
        if not target:
            continue
        if target not in stems:
            issues['broken_wikilinks'].append({'file': r, 'target': target})
        else:
            inbound[target] += 1
    line_count = txt.count('\n') + 1
    if line_count > 200:
        issues['large_pages'].append({'file': r, 'lines': line_count})
    if re.search(r'contested:\s*true|contradictions:|Contradicții|contradic', txt, flags=re.I):
        issues['contested_or_contradiction_markers'].append(r)

# Orphan pages: exempt the main matrix only if it is deliberately a hub? Keep it reported if no inbound.
for stem, count in inbound.items():
    if count == 0:
        issues['orphan_pages'].append(page_meta[stem]['path'])

# Raw frontmatter and SHA checks.
raw_files = sorted(RAW_DIR.glob('*.md'))
for p in raw_files:
    if p.name == '_manifest.md':
        continue
    txt = read_text(p)
    fm, body = parse_frontmatter(txt)
    if not fm:
        issues['raw_missing_frontmatter'].append(rel(p))
    else:
        for field in ['source_url','ingested','sha256','source_type','publisher','language']:
            if field not in fm:
                issues['raw_missing_frontmatter'].append({'file': rel(p), 'missing_field': field})
        sha = hashlib.sha256(body.encode('utf-8')).hexdigest()
        if fm.get('sha256') and str(fm.get('sha256')).lower() != sha.lower():
            issues['raw_sha_drift'].append({'file': rel(p), 'stored': fm.get('sha256'), 'computed': sha})
    if p.stem not in manifest_text:
        issues['raw_manifest_missing'].append(rel(p))

# Anchors, legal claims, mandate and consolidation checks.
raw_cache = {p.name: read_text(p) for p in raw_files if p.name != '_manifest.md'}
for p in pages:
    fm, body = body_without_frontmatter(p)
    r = rel(p)
    lines = body.splitlines()
    in_code = False
    for i, line in enumerate(lines):
        if line.strip().startswith('```'):
            in_code = not in_code
            continue
        if in_code:
            continue
        refs = extract_raw_refs(line)
        for ref in refs:
            target = RAW_DIR/ref['file']
            if not target.exists():
                issues['article_anchor_missing_target'].append({'file': r, 'line': i+1, 'ref': ref['raw'], 'problem': 'raw file missing'})
                continue
            arts = extract_art_numbers(ref['detail'])
            if not arts:
                issues['page_level_raw_refs'].append({'file': r, 'line': i+1, 'ref': ref['raw'], 'section': line_section(lines, i), 'text': line.strip()[:220]})
                continue
            rawtxt = raw_cache.get(ref['file'], '')
            for art in arts:
                if not article_exists(rawtxt, art):
                    issues['article_anchor_missing_target'].append({'file': r, 'line': i+1, 'ref': ref['raw'], 'article': art, 'problem': 'article marker not found in raw'})
        # Potential unanchored legal claim heuristic.
        stripped = line.strip()
        if not stripped or stripped.startswith('#') or stripped.startswith('|---') or stripped.startswith('---'):
            continue
        section = line_section(lines, i)
        if section in SKIP_SECTIONS:
            continue
        # Exempt source lines with only page-level source references.
        lowered = stripped.lower()
        has_art_anchor = bool(re.search(r'\[raw/papers/cnpf/[^\]]+\s+art\.?', stripped, flags=re.I))
        if has_art_anchor:
            continue
        if '[de verificat]' in lowered:
            # A marked uncertainty is not clean, but it is not silently asserted.
            issues['verification_markers'].append({'file': r, 'line': i+1, 'text': stripped[:240]})
            continue
        # Skip pure link/source list lines.
        if lowered.startswith('- **surse:**') or lowered.startswith('- **source'):
            continue
        if CLAIM_KEYWORDS.search(stripped) and len(strip_code_spans(stripped)) > 35:
            issues['potential_unanchored_claims'].append({'file': r, 'line': i+1, 'section': section, 'text': stripped[:260]})

# Mandate checks on legal entity pages.
for stem, expected_terms in LEGAL_EXPECTED_MANDATE.items():
    meta = page_meta.get(stem)
    if not meta:
        continue
    body = meta['body']
    m = re.search(r'^- \*\*mandat:\*\*\s*(.+)$', body, flags=re.M|re.I)
    if not m:
        issues['missing_mandate_line'].append(meta['path'])
        continue
    mandate = m.group(1)
    for term in expected_terms:
        if term.lower() not in mandate.lower():
            issues['mandate_conflicts'].append({'file': meta['path'], 'expected_contains': term, 'mandate_line': mandate})

# Consolidation staleness checks for L-* raw/legal pages.
def parse_date_any(s):
    # Return YYYY-MM-DD or None
    m = re.search(r'(\d{2})\.(\d{2})\.(\d{4})', s)
    if m:
        return f'{m.group(3)}-{m.group(2)}-{m.group(1)}'
    m = re.search(r'(\d{4})-(\d{2})-(\d{2})', s)
    if m:
        return m.group(0)
    return None

def date_tuple(d):
    return tuple(map(int, d.split('-'))) if d else None
for p in sorted((ROOT/'entities').glob('L-*.md')):
    stem = p.stem
    rawp = RAW_DIR / f'{stem}.md'
    if not rawp.exists():
        continue
    rawtxt = read_text(rawp)
    con_lines = [ln for ln in rawtxt.splitlines() if 'consolidare' in ln.lower()]
    cons_date = None
    for ln in con_lines:
        cons_date = parse_date_any(ln)
        if cons_date:
            break
    if not cons_date:
        issues['missing_consolidation_date'].append({'file': rel(rawp), 'sample': con_lines[:3]})
        continue
    txt = read_text(p)
    # issue if page explicitly says modified later, or contains dates/years after consolidation in amendment/status context.
    after = []
    for y in re.findall(r'\b(20\d{2})\b', txt):
        if int(y) > int(cons_date[:4]):
            after.append(y)
    stale_trigger = False
    if re.search(r'modificat[ăa] ulterior|amendament|legea\s+\d+\/20\d{2}|post-20\d{2}|202[0-9]', txt, flags=re.I) and after:
        stale_trigger = True
    # Known: if raw says source itself does not include amendments, flag.
    if re.search(r'NU\s+include|învechit|invechit', rawtxt, flags=re.I):
        stale_trigger = True
    if stale_trigger:
        issues['stale_consolidation'].append({'file': rel(p), 'raw': rel(rawp), 'raw_consolidation_date': cons_date, 'later_years_in_page': sorted(set(after))})

# Acquis checks.
for p in sorted((ROOT/'concepts').glob('acquis-*.md')):
    txt = read_text(p)
    fm, body = parse_frontmatter(txt)
    r = rel(p)
    if not re.search(r'ancor[ăa]\s+moldoveneasc[ăa].*\[\[(L-|REG-)', body, flags=re.I|re.S):
        # Less strict fallback: any page-level Moldovan legal link.
        if not re.search(r'\[\[(L-[0-9-]+|REG-[^\]]+)\]\]', body):
            issues['acquis_without_moldovan_anchor'].append(r)
    sources = fm.get('sources') or []
    if not any(isinstance(s, str) and re.search(r'raw/papers/cnpf/UE-', s) for s in sources):
        issues['acquis_without_eurlex_raw'].append(r)
    stat_lines = re.findall(r'^- \*\*statut[^:]*:\*\*\s*(.+)$', body, flags=re.M|re.I)
    if not stat_lines:
        issues['acquis_status_missing_or_unclear'].append({'file': r, 'problem': 'missing statut line'})
    else:
        if not any(any(term in line.lower() for term in ALLOWED_STATUS_TERMS) for line in stat_lines):
            issues['acquis_status_missing_or_unclear'].append({'file': r, 'status_line': stat_lines[0]})
    for m in re.finditer(r'\[de verificat\]', body, flags=re.I):
        line_no = body[:m.start()].count('\n') + 1
        issues['verification_markers'].append({'file': r, 'line': line_no, 'text': body.splitlines()[line_no-1][:240]})

# Deduplicate verification markers and potential claim samples.
def dedupe_list_of_dicts(items):
    seen=set(); out=[]
    for it in items:
        key=json.dumps(it, ensure_ascii=False, sort_keys=True)
        if key not in seen:
            seen.add(key); out.append(it)
    return out
for k,v in list(issues.items()):
    if isinstance(v, list) and v and isinstance(v[0], dict):
        issues[k] = dedupe_list_of_dicts(v)

summary = {k: len(v) for k, v in issues.items()}
# Severity buckets.
high_keys = ['broken_wikilinks','article_anchor_missing_target','mandate_conflicts','acquis_without_moldovan_anchor','raw_sha_drift']
medium_keys = ['potential_unanchored_claims','page_level_raw_refs','stale_consolidation','missing_consolidation_date','acquis_without_eurlex_raw','acquis_status_missing_or_unclear','raw_manifest_missing']
low_keys = ['orphan_pages','index_missing','missing_frontmatter','missing_required_fields','invalid_tags','missing_or_invalid_sources','raw_missing_frontmatter','large_pages','verification_markers','contested_or_contradiction_markers','missing_mandate_line']
severity = {
    'high': sum(summary.get(k,0) for k in high_keys),
    'medium': sum(summary.get(k,0) for k in medium_keys),
    'low': sum(summary.get(k,0) for k in low_keys),
}

# Write JSON.
audit = {
    'date': TODAY,
    'scope': {
        'active_pages_checked': len(pages),
        'raw_cnpf_files_checked': len([p for p in raw_files if p.name != '_manifest.md']),
        'rules_source': '_meta/imports/cnpf/source-CLAUDE.md + SCHEMA.md + llm-wiki lint checks',
    },
    'severity_counts': severity,
    'summary_counts': summary,
    'issues': issues,
}
JSON_OUT.write_text(json.dumps(audit, ensure_ascii=False, indent=2), encoding='utf-8')

# Markdown report.
def md_list(items, formatter=None, limit=None):
    if not items:
        return '_Nimic de raportat._\n'
    out=[]
    for idx, it in enumerate(items[:limit] if limit else items, 1):
        if formatter:
            out.append(f'{idx}. {formatter(it)}')
        else:
            out.append(f'{idx}. `{it}`')
    if limit and len(items)>limit:
        out.append(f'... încă {len(items)-limit} elemente în JSON.')
    return '\n'.join(out)+'\n'

report_lines = []
report_lines += [
    f'# Raport lint juridic CNPF — {TODAY}',
    '',
    '## Domeniu verificat',
    '',
    f'- Pagini active verificate: **{len(pages)}** (`entities/`, `concepts/`, `comparisons/`, `queries/`).',
    f'- Fișiere raw CNPF verificate: **{len([p for p in raw_files if p.name != "_manifest.md"])}** (`raw/papers/cnpf/`).',
    '- Reguli aplicate: ancorare la articol `raw/`, mandat CNPF/BNM, consolidare, lacune acquis/transpunere, wikilinks, frontmatter, index, raw SHA.',
    '',
    '## Rezumat severitate',
    '',
    f'- **Ridicat:** {severity["high"]}',
    f'- **Mediu:** {severity["medium"]}',
    f'- **Scăzut / informativ:** {severity["low"]}',
    '',
    '## Rezumat pe verificări',
    '',
    '| Verificare | Număr |',
    '|---|---:|',
]
for key in sorted(summary):
    report_lines.append(f'| `{key}` | {summary[key]} |')
report_lines += ['', '## 1. Integritate tehnică', '']
report_lines += ['### 1.1 Wikilinks rupte', md_list(issues['broken_wikilinks'], lambda x: f"`{x['file']}` → `[[{x['target']}]]`")]
report_lines += ['### 1.2 Pagini orfane', md_list(issues['orphan_pages'])]
report_lines += ['### 1.3 Index incomplet', md_list(issues['index_missing'])]
report_lines += ['### 1.4 Frontmatter / taguri / surse', '']
report_lines += [f'- Missing frontmatter: **{len(issues["missing_frontmatter"])}**', f'- Missing required fields: **{len(issues["missing_required_fields"])}**', f'- Invalid tags: **{len(issues["invalid_tags"])}**', f'- Missing/invalid frontmatter sources: **{len(issues["missing_or_invalid_sources"])}**', '']
report_lines += ['## 2. Surse raw și drift SHA', '']
report_lines += ['### 2.1 Raw fără frontmatter complet', md_list(issues['raw_missing_frontmatter'], lambda x: json.dumps(x, ensure_ascii=False) if isinstance(x, dict) else f'`{x}`')]
report_lines += ['### 2.2 Drift SHA raw', md_list(issues['raw_sha_drift'], lambda x: f"`{x['file']}` stored `{x['stored']}` vs computed `{x['computed']}`")]
report_lines += ['### 2.3 Raw lipsă din manifest', md_list(issues['raw_manifest_missing'])]
report_lines += ['## 3. Ancore juridice la articol', '']
report_lines += ['### 3.1 Ancore la articole inexistente / raw lipsă', md_list(issues['article_anchor_missing_target'], lambda x: f"`{x['file']}` linia {x['line']} — {x['ref']} — {x['problem']}")]
report_lines += ['### 3.2 Referințe raw doar la nivel de pagină', md_list(issues['page_level_raw_refs'], lambda x: f"`{x['file']}` linia {x['line']} ({x['section']}) — {x['ref']} — {x['text']}", limit=80)]
report_lines += ['### 3.3 Afirmații juridice potențial neancorate', 'Acestea sunt detectate euristic. Nu le-am modificat automat; trebuie fie ancorate la articol, fie mutate la întrebări deschise / marcate `[de verificat]` dacă rămân incerte.\n', md_list(issues['potential_unanchored_claims'], lambda x: f"`{x['file']}` linia {x['line']} ({x['section']}) — {x['text']}", limit=120)]
report_lines += ['## 4. Mandat CNPF/BNM', '']
report_lines += ['### 4.1 Lipsă linie mandat', md_list(issues['missing_mandate_line'])]
report_lines += ['### 4.2 Conflicte de mandat', md_list(issues['mandate_conflicts'], lambda x: f"`{x['file']}` expected `{x['expected_contains']}` în: {x['mandate_line']}")]
report_lines += ['## 5. Consolidare legis.md / actualitate', '']
report_lines += ['### 5.1 Dată consolidare lipsă în raw', md_list(issues['missing_consolidation_date'], lambda x: f"`{x['file']}` — sample: {x.get('sample')}")]
report_lines += ['### 5.2 Consolidare probabil învechită', md_list(issues['stale_consolidation'], lambda x: f"`{x['file']}` raw `{x['raw']}` consolidare `{x['raw_consolidation_date']}`, ani ulteriori în pagină: {', '.join(x['later_years_in_page']) if x['later_years_in_page'] else 'n/a'}")]
report_lines += ['## 6. Acquis / transpunere', '']
report_lines += ['### 6.1 Pagini acquis fără ancoră moldovenească', md_list(issues['acquis_without_moldovan_anchor'])]
report_lines += ['### 6.2 Pagini acquis fără raw EUR-Lex în frontmatter', md_list(issues['acquis_without_eurlex_raw'])]
report_lines += ['### 6.3 Statut transpunere lipsă / neclar', md_list(issues['acquis_status_missing_or_unclear'], lambda x: f"`{x.get('file')}` — {x.get('problem') or x.get('status_line')}")]
report_lines += ['### 6.4 Marcaje `[de verificat]`', md_list(issues['verification_markers'], lambda x: f"`{x['file']}` linia {x['line']} — {x['text']}", limit=100)]
report_lines += ['## 7. Dimensiune pagini / contradicții', '']
report_lines += ['### 7.1 Pagini >200 linii', md_list(issues['large_pages'], lambda x: f"`{x['file']}` — {x['lines']} linii")]
report_lines += ['### 7.2 Marcaje contradicții / contestări', md_list(issues['contested_or_contradiction_markers'])]
report_lines += ['## 8. Recomandări de remediere', '', '1. Prioritate maximă: rezolvă `article_anchor_missing_target`, `mandate_conflicts` și `broken_wikilinks` dacă apar.', '2. Pentru `potential_unanchored_claims`, lucrează pagină cu pagină: păstrează doar afirmațiile ancorate la articol; restul se mută la `Întrebări deschise` sau se marchează `[de verificat]`.', '3. Pentru `stale_consolidation`, ingestia textelor consolidate integrale de pe legis.md rămâne pasul critic pentru legile mari.', '4. Pentru paginile acquis fără raw EUR-Lex, decide dacă extinzi ingestia EUR-Lex dincolo de nucleul pieței de capital.', '', f'JSON complet: `{rel(JSON_OUT)}`', '']
REPORT.write_text('\n'.join(report_lines), encoding='utf-8')

# Append log.
log_path = ROOT/'log.md'
log = read_text(log_path)
entry = f"""
## [{TODAY}] lint | CNPF legal/acquis complete lint

- Scope: {len(pages)} active pages and {len([p for p in raw_files if p.name != '_manifest.md'])} raw CNPF files.
- Report: `_meta/lint/{REPORT.name}`.
- JSON audit: `_meta/lint/{JSON_OUT.name}`.
- Severity counts: high={severity['high']}, medium={severity['medium']}, low={severity['low']}.
- Technical graph/frontmatter summary: broken wikilinks={summary['broken_wikilinks']}, invalid tags={summary['invalid_tags']}, missing index entries={summary['index_missing']}, raw SHA drift={summary['raw_sha_drift']}.
""".strip()
if entry not in log:
    log_path.write_text(log.rstrip() + '\n\n' + entry + '\n', encoding='utf-8')

print(json.dumps({
    'report': str(REPORT),
    'json': str(JSON_OUT),
    'severity_counts': severity,
    'summary_counts': summary,
    'active_pages_checked': len(pages),
    'raw_files_checked': len([p for p in raw_files if p.name != '_manifest.md']),
}, ensure_ascii=False, indent=2))
