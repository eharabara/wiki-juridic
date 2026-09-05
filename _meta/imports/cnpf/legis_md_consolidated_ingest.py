from pathlib import Path
import subprocess, re, html as ihtml, hashlib, json, datetime, shutil
from urllib.parse import urljoin
from lxml import html

try:
    import yaml
except Exception:
    yaml = None

ROOT = Path(r"C:\Users\harab\wiki")
RAW_DIR = ROOT / "raw" / "papers" / "cnpf"
ENTITIES = ROOT / "entities"
META_DIR = ROOT / "_meta" / "imports" / "cnpf" / "legis-md-consolidated"
META_DIR.mkdir(parents=True, exist_ok=True)
TODAY = datetime.date.today().isoformat()
STAMP = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
BACKUP = Path(r"C:\Users\harab\wiki-backups\wiki-before-legis-md-consolidated-ingest-20260709-151106")
ARCHIVE = ROOT / "_archive" / "raw" / f"cnpf-legis-md-before-{STAMP}"
ARCHIVE.mkdir(parents=True, exist_ok=True)
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"

# Current/best-known legis.md doc_id values discovered from CNPF/BNM pages and the existing source metadata.
# Some pages (notably L-171/2012) are only consolidated by legis.md up to 2020/2021 in this accessible doc_id;
# post-2025 amendments are preserved as separate raw amendments where available.
DOCS = {
    'L-1-2018': {'doc_id':'120941', 'title':'Legea nr. 1/2018 cu privire la organizațiile de creditare nebancară', 'page':'L-1-2018'},
    'L-106-2022': {'doc_id':'144476', 'title':'Legea nr. 106/2022 privind asigurarea obligatorie RCA auto', 'page':'L-106-2022'},
    'L-1134-1997': {'doc_id':'129078', 'title':'Legea nr. 1134/1997 privind societățile pe acțiuni', 'page':'L-1134-1997'},
    'L-122-2008': {'doc_id':'120927', 'title':'Legea nr. 122/2008 privind birourile istoriilor de credit', 'page':'L-122-2008'},
    'L-139-2007': {'doc_id':'121166', 'title':'Legea nr. 139/2007 privind asociațiile de economii și împrumut', 'page':'L-139-2007'},
    'L-171-2012': {'doc_id':'121985', 'title':'Legea nr. 171/2012 privind piața de capital', 'page':'L-171-2012'},
    'L-178-2020': {'doc_id':'123148', 'title':'Legea nr. 178/2020 privind modificarea unor acte normative', 'page':'L-178-2020'},
    'L-181-2023': {'doc_id':'138188', 'title':'Legea nr. 181/2023 privind serviciile de finanțare participativă', 'page':'L-181-2023'},
    'L-192-1998': {'doc_id':'128124', 'title':'Legea nr. 192/1998 privind Comisia Națională a Pieței Financiare', 'page':'L-192-1998'},
    'L-198-2020': {'doc_id':'124466', 'title':'Legea nr. 198/2020 privind fondurile de pensii facultative', 'page':'L-198-2020'},
    'L-2-2020': {'doc_id':'120967', 'title':'Legea nr. 2/2020 privind organismele de plasament colectiv alternative', 'page':'L-2-2020'},
    'L-234-2016': {'doc_id':'139826', 'title':'Legea nr. 234/2016 privind Depozitarul central unic al valorilor mobiliare', 'page':'L-234-2016'},
    'L-308-2017': {'doc_id':'110418', 'title':'Legea nr. 308/2017 privind AML/CFT', 'page':'L-308-2017'},
    'L-92-2022': {'doc_id':'134551', 'title':'Legea nr. 92/2022 privind activitatea de asigurare sau de reasigurare', 'page':'L-92-2022'},
    # Dreptul corporativ NU se ingereaza de aici. L-135/2007 (doc_id 153674) si
    # L-220/2007 (doc_id 155438) au fost ingerate la 2026-09-04 in
    # raw/papers/moldova-legal/, fiindca sint drept societar general, nu perimetru
    # CNPF/BNM. Scriptul lor este _meta/imports/moldova-legal/ingest_business_law.py,
    # care rezolva <sup> inainte de extractie. Nu le adauga in DOCS de aici: ar
    # rescrie fisierele in folderul gresit.
}
AMENDMENTS = {
    'L-177-2025': {'doc_id':'149610', 'title':'Legea nr. 177/2025 pentru modificarea unor acte normative (instrumente financiare derivate)', 'page':'L-171-2012'},
}

DATE_RE = re.compile(r'(\d{1,2})[.\-/](\d{1,2})[.\-/](\d{2,4})')

def norm_year(y):
    y = int(y)
    if y < 100:
        return 2000 + y if y <= 40 else 1900 + y
    return y

def norm_date(d, m, y):
    return f"{norm_year(y):04d}-{int(m):02d}-{int(d):02d}"

def first_date(text):
    m = DATE_RE.search(text or '')
    if not m:
        return None
    return norm_date(m.group(1), m.group(2), m.group(3))

def all_dates(text):
    return [norm_date(a,b,c) for a,b,c in DATE_RE.findall(text or '')]

def curl_showdetails(doc_id):
    url = f"https://www.legis.md/cautare/showdetails/{doc_id}"
    out = META_DIR / f"showdetails-{doc_id}.html"
    cmd = ['curl','-L','--max-time','120','-A',UA,url,'-o',str(out)]
    res = subprocess.run(cmd, capture_output=True, text=True)
    data = out.read_text(encoding='utf-8', errors='replace') if out.exists() else ''
    if res.returncode != 0 or 'id="contentdoc"' not in data or 'Just a moment' in data[:2000]:
        raise RuntimeError(f"fetch failed for {doc_id}: return={res.returncode}, size={len(data)}, stderr={res.stderr[:300]}")
    return url, data, out

def clean_line(s):
    s = ihtml.unescape(s or '').replace('\xa0',' ')
    s = re.sub(r'[ \t\r\f\v]+', ' ', s)
    return s.strip()

def extract_doc(data):
    doc = html.fromstring(data)
    content_nodes = doc.xpath('//*[@id="contentdoc"]')
    if not content_nodes:
        raise RuntimeError('contentdoc missing')
    content = content_nodes[0]
    meta_nodes = doc.xpath('//*[@id="contentdoc_act"]')
    meta_node = meta_nodes[0] if meta_nodes else None
    # Metadata table/pairs.
    meta_pairs = []
    if meta_node is not None:
        for tr in meta_node.xpath('.//tr'):
            cells = [clean_line(c.text_content()) for c in tr.xpath('./th|./td')]
            cells = [c for c in cells if c]
            if len(cells) >= 2:
                meta_pairs.append((cells[0].rstrip(':'), cells[-1]))
        if not meta_pairs:
            lines = [clean_line(x) for x in meta_node.text_content().splitlines()]
            lines = [x for x in lines if x]
            # Best-effort: alternating labels/values after title.
            for i in range(len(lines)-1):
                if lines[i].endswith(':'):
                    meta_pairs.append((lines[i].rstrip(':'), lines[i+1]))
    raw_lines = [clean_line(x) for x in content.text_content().splitlines()]
    lines = [x for x in raw_lines if x]
    # Extract visible title block from first lines.
    official_title = ''
    for k,v in meta_pairs:
        if 'Denumirea deplină actuală' in k:
            official_title = v; break
    if not official_title:
        # Usually first lines are: Republica Moldova, PARLAMENTUL, LEGE Nr..., title.
        for i,l in enumerate(lines[:10]):
            if l.lower().startswith('lege nr') and i+1 < len(lines):
                official_title = f"{l} {lines[i+1]}"; break
    # Modification/consolidation line.
    latest_line = ''
    for i,l in enumerate(lines[:60]):
        if l == 'MODIFICAT' and i+1 < len(lines):
            latest_line = lines[i+1]
            break
        if 'Versiune în vigoare din' in l or 'Versiune in vigoare din' in l:
            latest_line = l
            break
    if not latest_line:
        for k,v in meta_pairs:
            if 'Data modificării' in k or 'datele modificării' in k:
                latest_line = v.split('\n')[0].strip(); break
    if not latest_line:
        for l in lines[:30]:
            if 'Publicat :' in l:
                latest_line = l; break
    dates = all_dates(latest_line)
    consolidation_date = None
    if 'în vigoare' in latest_line.lower() or 'in vigoare' in latest_line.lower():
        # Prefer the last date if the line contains both adoption and entry-into-force dates.
        consolidation_date = dates[-1] if dates else None
    else:
        consolidation_date = dates[0] if dates else None
    if not consolidation_date:
        consolidation_date = TODAY
    # Structured markdown body.
    md_lines = []
    for l in lines:
        if re.match(r'^Capitolul\s+', l, flags=re.I):
            md_lines += ['', f"## {l}"]
        elif re.match(r'^Secţiunea|^Secțiunea', l, flags=re.I):
            md_lines += ['', f"### {l}"]
        elif re.match(r'^Articolul\s+[0-9IVXLCDM]+[a-zA-Z]?\b', l, flags=re.I):
            md_lines += ['', f"## {l}"]
        else:
            md_lines.append(l)
    return {
        'official_title': official_title,
        'meta_pairs': meta_pairs,
        'lines': lines,
        'text_markdown': '\n'.join(md_lines).strip() + '\n',
        'latest_line': latest_line,
        'consolidation_date': consolidation_date,
        'article_count': len([l for l in lines if re.match(r'^Articolul\s+', l, flags=re.I)]),
        'char_count': len(content.text_content()),
    }

def yaml_quote(s):
    return str(s).replace('\\','\\\\')

def make_raw(stem, spec, parsed, show_url, is_amendment=False):
    body = []
    body.append(f"# raw/{stem} — text legis.md {'amendament' if is_amendment else 'consolidat/curent'}")
    body.append('')
    body.append('> **TEXT LEGIS.MD RO — extras din `showdetails` și păstrat pentru audit.** Nu corectez și nu armonizez tăcut textul; pentru neconcordanțe cu amendamente ulterioare, păstrez marcaje `[de verificat]` în paginile wiki.')
    body.append('')
    body.append(f"- **Sursă de referință:** https://www.legis.md/cautare/getResults?doc_id={spec['doc_id']}&lang=ro")
    body.append(f"- **Endpoint folosit:** {show_url}")
    body.append(f"- **doc_id legis.md:** {spec['doc_id']}")
    body.append(f"- **Titlu oficial detectat:** {parsed['official_title'] or spec['title']}")
    body.append(f"- **consolidare legis.md:** {parsed['consolidation_date']} — derivată din prima linie de modificare/versiune disponibilă: {parsed['latest_line'] or 'n/a'}")
    body.append(f"- **articole detectate:** {parsed['article_count']}")
    body.append(f"- **caractere text extras:** {parsed['char_count']}")
    body.append('')
    body.append('## Fișa actului juridic — extras metadata')
    body.append('')
    if parsed['meta_pairs']:
        body.append('| Câmp | Valoare |')
        body.append('|---|---|')
        for k,v in parsed['meta_pairs']:
            body.append(f"| {k.replace('|','/')} | {v.replace('|','/')} |")
    else:
        body.append('_Fișa metadata nu a putut fi parsată tabelar; vezi HTML arhivat în `_meta/imports/cnpf/legis-md-consolidated/`._')
    body.append('')
    body.append('## Text integral extras din legis.md')
    body.append('')
    body.append(parsed['text_markdown'])
    body_text = '\n'.join(body).strip() + '\n'
    sha = hashlib.sha256(body_text.encode('utf-8')).hexdigest()
    fm = {
        'source_url': f"https://www.legis.md/cautare/getResults?doc_id={spec['doc_id']}&lang=ro",
        'showdetails_url': show_url,
        'ingested': TODAY,
        'sha256': sha,
        'source_type': 'legal-text',
        'publisher': 'legis.md / Ministerul Justiției al Republicii Moldova',
        'language': 'ro',
        'doc_id': str(spec['doc_id']),
        'instrument_id': stem,
        'official_title_detected': parsed['official_title'] or spec['title'],
        'consolidation_date': parsed['consolidation_date'],
        'latest_modification_line': parsed['latest_line'] or '',
        'full_text': True,
        'extract_method': 'curl showdetails + lxml text extraction',
    }
    if yaml:
        fm_text = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False).strip()
    else:
        fm_text = '\n'.join(f'{k}: {v}' for k,v in fm.items())
    return '---\n' + fm_text + '\n---\n\n' + body_text, fm

def parse_page_fm(text):
    if not text.startswith('---\n'):
        return {}, text
    end = text.find('\n---\n',4)
    if end < 0:
        return {}, text
    fm_text=text[4:end]; body=text[end+5:]
    if yaml:
        try: return yaml.safe_load(fm_text) or {}, body
        except Exception: return {}, body
    return {}, body

def dump_page(fm, body):
    if yaml:
        return '---\n' + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False).strip() + '\n---\n\n' + body.lstrip()
    return body

def replace_line_start(body, prefix, new_line):
    lines=body.splitlines()
    for i,l in enumerate(lines):
        if l.startswith(prefix):
            lines[i]=new_line
            return '\n'.join(lines)+('\n' if body.endswith('\n') else '')
    return body

changed=[]; fetched=[]; errors=[]

# Archive existing target raw files.
for stem in list(DOCS) + list(AMENDMENTS):
    p = RAW_DIR / f'{stem}.md'
    if p.exists():
        shutil.copy2(p, ARCHIVE / p.name)

# Fetch + write raw files.
for stem, spec in {**DOCS, **AMENDMENTS}.items():
    try:
        show_url, data, html_path = curl_showdetails(spec['doc_id'])
        parsed = extract_doc(data)
        content, fm = make_raw(stem, spec, parsed, show_url, is_amendment=stem in AMENDMENTS)
        out = RAW_DIR / f'{stem}.md'
        out.write_text(content, encoding='utf-8')
        changed.append(str(out.relative_to(ROOT)).replace('\\','/'))
        fetched.append({
            'id': stem, 'doc_id': spec['doc_id'], 'source_url': fm['source_url'], 'showdetails_url': show_url,
            'title': fm['official_title_detected'], 'consolidation_date': fm['consolidation_date'],
            'latest_modification_line': fm['latest_modification_line'], 'article_count': parsed['article_count'],
            'char_count': parsed['char_count'], 'html_archive': str(html_path.relative_to(ROOT)).replace('\\','/') if html_path.is_relative_to(ROOT) else str(html_path)
        })
    except Exception as e:
        errors.append({'id':stem,'doc_id':spec['doc_id'],'error':f'{type(e).__name__}: {e}'})

if errors:
    (META_DIR / 'legis-md-fetch-errors.json').write_text(json.dumps(errors, ensure_ascii=False, indent=2), encoding='utf-8')

# Update key entity pages conservatively.
def update_entity(stem, mutator):
    p = ENTITIES / f'{stem}.md'
    if not p.exists(): return
    txt = p.read_text(encoding='utf-8')
    fm, body = parse_page_fm(txt)
    fm['updated'] = TODAY
    sources = list(fm.get('sources') or [])
    rel = f'raw/papers/cnpf/{stem}.md'
    if rel not in sources: sources.append(rel)
    if stem == 'L-171-2012' and 'raw/papers/cnpf/L-177-2025.md' not in sources:
        sources.append('raw/papers/cnpf/L-177-2025.md')
    fm['sources'] = sources
    body = mutator(body)
    p.write_text(dump_page(fm, body), encoding='utf-8')
    changed.append(str(p.relative_to(ROOT)).replace('\\','/'))

def mut_l171(body):
    body = replace_line_start(body, '- **statut:**', '- **statut:** în vigoare — textul legis.md accesibil pentru Legea 171/2012 este consolidat până la LP97/2020 (în vigoare 01.01.2021); amendamentul LP177/2025 este păstrat ca raw separat și trebuie integrat numai după verificarea textului consolidat post-2025. `[raw/papers/cnpf/L-171-2012.md art.1]` `[raw/papers/cnpf/L-177-2025.md art.I]` `[de verificat text consolidat post-2025]`')
    body = replace_line_start(body, '- **acquis transpus:**', '- **acquis transpus:** [[acquis-MiFID]] (prin 2004/39 și 2006/73), [[acquis-MAR]] (prin 2003/6), [[acquis-Prospectus]], [[acquis-Transparency]], [[acquis-UCITS]], [[acquis-ICSD]], [[acquis-SFD]], [[acquis-Takeover]] și alte instrumente enumerate în clauza de armonizare; statutul rămâne parțial / învechit — vezi [[cnpf-transposition-matrix]]. `[raw/papers/cnpf/L-171-2012.md art.1]`')
    body = body.replace('- 2025 — Legea 177/2025 modifică art.1(1) privind restricțiile CFD; raw-ul L-171 disponibil local nu include textul consolidat post-2018, deci detaliile rămân de verificat pe amendament/text consolidat. `[raw/papers/cnpf/L-171-2012.md art.1]` `[de verificat]`', '- 2025 — Legea 177/2025 modifică art.1(1) privind restricțiile CFD; amendamentul este ingerat separat, dar textul consolidat L-171 post-2025 rămâne de verificat. `[raw/papers/cnpf/L-177-2025.md art.I]` `[de verificat]`')
    return body

def mut_l192(body):
    body = replace_line_start(body, '- **statut:**', '- **statut:** în vigoare — text legis.md accesibil prin doc_id 128124; delimitarea post-2023 cu BNM trebuie citită împreună cu [[L-178-2020]], nu dedusă doar din L-192/1998. `[raw/papers/cnpf/L-192-1998.md art.1, art.8]` `[raw/papers/cnpf/L-178-2020.md art.I]`')
    body = body.replace('Legea 192/1998 încadrează CNPF asupra „pieței financiare nebancare" ca întreg în consolidarea locală 31.07.2015.', 'Legea 192/1998 încadrează CNPF asupra „pieței financiare nebancare" ca întreg în textul legis.md accesibil curent.')
    return body

def mut_l1134(body):
    body = replace_line_start(body, '- **statut:**', '- **statut:** în vigoare — text legis.md accesibil prin doc_id 129078; modificările post-publicare trebuie verificate pe fișa actului și pe articolele afectate. `[raw/papers/cnpf/L-1134-1997.md art.1]` `[de verificat]`')
    body = body.replace('raw-ul local semnalează această nevoie, dar nu conține articolul consolidat.', 'raw-ul legis.md refresh conține textul de bază accesibil, dar compatibilitatea post-2020 trebuie verificată articol-cu-articol.')
    return body

update_entity('L-171-2012', mut_l171)
update_entity('L-192-1998', mut_l192)
update_entity('L-1134-1997', mut_l1134)

# Update manifest section H.
manifest_path = RAW_DIR / '_manifest.md'
manifest = manifest_path.read_text(encoding='utf-8') if manifest_path.exists() else '# Manifest CNPF raw sources\n'
heading = '## H. Legis.md — legi moldovenești CNPF/BNM refresh'
rows = [heading, '', f'Refresh executat la **{TODAY}** prin endpointul `showdetails`, după ce pagina publică `getResults` a fost accesibilă doar ca shell JS / parțial blocată de protecție. Fișierele sunt text integral extras din legis.md unde `contentdoc` a fost disponibil.', '', '| ID raw | doc_id | Titlu detectat | Consolidare / versiune locală | Articole detectate |', '|---|---:|---|---|---:|']
for item in fetched:
    rows.append(f"| `{item['id']}` | {item['doc_id']} | {item['title'].replace('|','/')} | {item['consolidation_date']} | {item['article_count']} |")
section = '\n'.join(rows) + '\n'
if heading in manifest:
    manifest = re.sub(rf'\n{re.escape(heading)}\n.*?(?=\n## |\Z)', '\n' + section, manifest, flags=re.S)
else:
    manifest = manifest.rstrip() + '\n\n' + section
manifest_path.write_text(manifest, encoding='utf-8')
changed.append(str(manifest_path.relative_to(ROOT)).replace('\\','/'))

# Update log.
log_path = ROOT / 'log.md'
entry = f"""
## [{TODAY}] ingest | Legis.md RO consolidated/current Moldovan legal texts

- Backup created before ingest: `{BACKUP}`.
- Previous Moldovan-law raw files archived under `{ARCHIVE}`.
- Fetched `showdetails` HTML from legis.md and refreshed {len(fetched)} raw Moldovan legal/amendment files under `raw/papers/cnpf/`.
- Core active pages updated conservatively: `entities/L-171-2012.md`, `entities/L-192-1998.md`, `entities/L-1134-1997.md`.
- Manifest updated: `raw/papers/cnpf/_manifest.md`, section `H. Legis.md — legi moldovenești CNPF/BNM refresh`.
- Note: uncertainty markers were preserved; post-2025 L-171 consolidation remains explicitly `[de verificat]` because accessible legis.md text and LP177/2025 amendment are separate sources.
""".strip()
log = log_path.read_text(encoding='utf-8')
log_path.write_text(log.rstrip() + '\n\n' + entry + '\n', encoding='utf-8')
changed.append('log.md')

# Write audit.
audit = {
    'date': TODAY,
    'backup': str(BACKUP),
    'archive': str(ARCHIVE),
    'fetched_count': len(fetched),
    'fetched': fetched,
    'errors': errors,
    'changed_files': sorted(set(changed)),
}
(META_DIR / 'legis-md-consolidated-ingest-audit.json').write_text(json.dumps(audit, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(audit, ensure_ascii=False, indent=2))
