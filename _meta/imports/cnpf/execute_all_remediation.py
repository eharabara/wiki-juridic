from pathlib import Path
import urllib.request, re, datetime, hashlib, json, shutil, html, xml.etree.ElementTree as ET

# This script does all of its work at module level: it re-fetches 14 EUR-Lex
# extracts, rewrites the concept and entity pages that cite them, and rewrites
# index.md and log.md. There is no main() guard, so *importing* it -- to reuse
# item_for_celex/parse_xhtml/raw_markdown, which is a reasonable thing to want --
# silently re-runs the whole 2026-07-09 remediation. That happened on
# 2026-09-04 and had to be reverted from a backup.
#
# Refuse to be imported rather than leave the hazard in place. To reuse the
# helpers, copy them or run this file directly.
if __name__ != "__main__":
    raise ImportError(
        "execute_all_remediation.py performs a full re-ingest at module level "
        "and must not be imported. Run it directly, or copy the helper you need."
    )

try:
    import yaml
except Exception:
    yaml = None

ROOT = Path(r"C:\Users\harab\wiki")
RAW_DIR = ROOT / "raw" / "papers" / "cnpf"
CONCEPTS = ROOT / "concepts"
ENTITIES = ROOT / "entities"
COMPARISONS = ROOT / "comparisons"
META = ROOT / "_meta" / "imports" / "cnpf" / "extended-acquis-remediation"
TODAY = datetime.date.today().isoformat()
STAMP = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
BACKUP = Path(r"C:\Users\harab\wiki-backups\wiki-before-execute-all-remediation-20260709-145828")
ARCHIVE = ROOT / "_archive" / "raw" / f"cnpf-extended-eurlex-before-{STAMP}"
META.mkdir(parents=True, exist_ok=True)
ARCHIVE.mkdir(parents=True, exist_ok=True)

EXT_INSTRUMENTS = [
    # AML
    {"id":"UE-2015-849", "base":"32015L0849", "kind":"directivă", "label":"Dir. (UE) 2015/849 (AMLD4/AMLD5 consolidată)", "page":"acquis-AML", "key":["1","2","3","11","13","18","30","45","48"]},
    {"id":"UE-2024-1624", "base":"32024R1624", "kind":"regulament", "label":"Reg. (UE) 2024/1624 (AMLR — cod unic AML/CFT)", "page":"acquis-AML", "key":["1","2","3","19","20","22","78"]},
    {"id":"UE-2024-1640", "base":"32024L1640", "kind":"directivă", "label":"Dir. (UE) 2024/1640 (AMLD6)", "page":"acquis-AML", "key":["1","2","4","8","34","37","52"]},
    {"id":"UE-2024-1620", "base":"32024R1620", "kind":"regulament", "label":"Reg. (UE) 2024/1620 (AMLA)", "page":"acquis-AML", "key":["1","2","5","6","12","13"]},
    # Company law
    {"id":"UE-2017-1132", "base":"32017L1132", "kind":"directivă", "label":"Dir. (UE) 2017/1132 (dreptul societăților, codificare)", "page":"acquis-CompanyLaw", "key":["1","2","13","14","44","46","86b"]},
    {"id":"UE-2007-36", "base":"32007L0036", "kind":"directivă", "label":"Dir. 2007/36/CE (drepturile acționarilor, consolidată)", "page":"acquis-CompanyLaw", "key":["1","2","3a","3b","9a","14a"]},
    {"id":"UE-2017-828", "base":"32017L0828", "kind":"directivă", "label":"Dir. (UE) 2017/828 (SRD II — modifică 2007/36/CE)", "page":"acquis-CompanyLaw", "key":["1","2","3"]},
    # Consumer credit
    {"id":"UE-2008-48", "base":"32008L0048", "kind":"directivă", "label":"Dir. 2008/48/CE (creditul de consum)", "page":"acquis-ConsumerCredit", "key":["1","2","3","5","8","10","16","22"]},
    {"id":"UE-2023-2225", "base":"32023L2225", "kind":"directivă", "label":"Dir. (UE) 2023/2225 (CCD2)", "page":"acquis-ConsumerCredit", "key":["1","2","3","10","18","20","30","48"]},
    # Insurance / MTPL
    {"id":"UE-2009-138", "base":"32009L0138", "kind":"directivă", "label":"Dir. 2009/138/CE (Solvency II)", "page":"acquis-Insurance", "key":["1","2","13","14","27","30","41","100"]},
    {"id":"UE-2016-97", "base":"32016L0097", "kind":"directivă", "label":"Dir. (UE) 2016/97 (IDD)", "page":"acquis-Insurance", "key":["1","2","3","10","17","20","25","29"]},
    {"id":"UE-2009-103", "base":"32009L0103", "kind":"directivă", "label":"Dir. 2009/103/CE (RCA auto / MTPL)", "page":"acquis-MTPL", "key":["1","2","3","10","18","30"]},
    {"id":"UE-2021-2118", "base":"32021L2118", "kind":"directivă", "label":"Dir. (UE) 2021/2118 (amendamente MTPL)", "page":"acquis-MTPL", "key":["1","2"]},
    # Pensions
    {"id":"UE-2016-2341", "base":"32016L2341", "kind":"directivă", "label":"Dir. (UE) 2016/2341 (IORP II)", "page":"acquis-IORP", "key":["1","2","6","9","19","21","34"]},
]
PAGE_MAP = {}
for instr in EXT_INSTRUMENTS:
    PAGE_MAP.setdefault(instr['page'], []).append(instr['id'])
BY_ID = {i['id']: i for i in EXT_INSTRUMENTS}

# ---------------- helpers ----------------
def fetch(url, accept='application/rdf+xml,text/xml,text/html,*/*', max_bytes=None):
    req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0 (Hermes Wiki EUR-Lex ingest)', 'Accept': accept})
    with urllib.request.urlopen(req, timeout=120) as r:
        data = r.read(max_bytes or 40_000_000)
        return r.geturl(), r.headers.get('content-type'), data

def fetch_text(url, accept='application/rdf+xml'):
    return fetch(url, accept)[2].decode('utf-8', 'replace')

def clean_text(s):
    s = html.unescape(s or '').replace('\xa0',' ')
    return re.sub(r'\s+', ' ', s).strip()

def rdf_for_celex(celex):
    return fetch_text(f'https://publications.europa.eu/resource/celex/{celex}')

def get_title_from_rdf(rdf):
    pats = [r'<[^>]*:?title[^>]*xml:lang="ro"[^>]*>(.*?)</[^>]+>', r'<[^>]*:?expression_title[^>]*>(.*?)</[^>]+>', r'<[^>]*:?title[^>]*>(.*?)</[^>]+>']
    for pat in pats:
        m = re.search(pat, rdf, flags=re.S)
        if m:
            t = clean_text(m.group(1))
            if t and t != 'PROPCELEX':
                return t
    return ''

def find_consolidation_candidates(base):
    rdf = rdf_for_celex(base)
    cons_prefix = '0' + base[1:]
    today_num = int(TODAY.replace('-', ''))
    cands = sorted(set(re.findall(rf'{re.escape(cons_prefix)}-\d{{8}}', rdf)))
    cands = [c for c in cands if int(c.split('-')[-1]) <= today_num]
    return sorted(cands, key=lambda c: c.split('-')[-1], reverse=True)

def item_for_celex(celex):
    rdf = rdf_for_celex(celex)
    exprs = re.findall(r'rdf:resource="([^"]+\.RON)"', rdf)
    exprs = [e for e in exprs if '/resource/' in e]
    exprs.append(f'http://publications.europa.eu/resource/celex/{celex}.RON')
    last_err = None
    for expr in list(dict.fromkeys(exprs)):
        try:
            erdf = fetch_text(expr)
            title = get_title_from_rdf(erdf)
            mans = re.findall(r'rdf:resource="([^"]+)"', erdf)
            mans = [m for m in mans if m.endswith('.xhtml')] + [m for m in mans if m.endswith('.fmx4')]
            for man in list(dict.fromkeys(mans)):
                mrdf = fetch_text(man)
                items = re.findall(r'manifestation_has_item rdf:resource="([^"]+/DOC_\d+)"', mrdf)
                def doc_key(u):
                    m = re.search(r'DOC_(\d+)$', u)
                    return int(m.group(1)) if m else 0
                for item in sorted(list(dict.fromkeys(items)), key=doc_key, reverse=True):
                    final, ctype, data = fetch(item, 'application/xhtml+xml,text/html,application/xml,*/*')
                    sample = data[:3000].lower()
                    if b'<html' in sample or b'<!doctype html' in sample:
                        return {'celex': celex, 'expr': expr, 'manifestation': man, 'item': final, 'ctype': ctype, 'title': title, 'data': data}
        except Exception as e:
            last_err = f'{type(e).__name__}: {e}'
    raise RuntimeError(f'No XHTML item for {celex}: {last_err}')

def select_and_fetch(base):
    tried = find_consolidation_candidates(base) + [base]
    last = None
    for c in tried:
        try:
            res = item_for_celex(c)
            res['base_celex'] = base
            res['tried'] = tried
            return res
        except Exception as e:
            last = f'{type(e).__name__}: {e}'
    raise RuntimeError(f'No usable RO XHTML for {base}: {last}')

def parse_xhtml(data):
    try:
        root = ET.fromstring(data)
    except Exception:
        txt = data.decode('utf-8', 'replace') if isinstance(data, (bytes, bytearray)) else str(data)
        txt = re.sub(r'<!DOCTYPE[^>]*>', '', txt, flags=re.I)
        root = ET.fromstring(txt.encode('utf-8'))
    articles=[]; amap={}
    for el in root.iter():
        tag = el.tag.split('}',1)[-1]
        elid = el.attrib.get('id','')
        if tag == 'div' and re.match(r'^art_[A-Za-z0-9]+$', elid):
            title=''; subtitle=''
            for child in el.iter():
                cls = child.attrib.get('class','')
                t = clean_text(' '.join(child.itertext()))
                if 'title-article' in cls and not title and t:
                    title = t
                elif 'stitle-article' in cls and not subtitle and t:
                    subtitle = t
            if not title:
                for child in el.iter():
                    t = clean_text(' '.join(child.itertext()))
                    if re.match(r'^Articolul\s+', t, flags=re.I):
                        title=t; break
            if title:
                m = re.search(r'Articolul\s+([0-9]+[a-zA-Z]?)', title, flags=re.I)
                num = m.group(1) if m else elid.replace('art_','')
                text = clean_text(' '.join(el.itertext()))
                item={'num':num, 'heading':title, 'subtitle':subtitle, 'text':text}
                articles.append(item); amap[num.lower()] = item
    if articles:
        return articles, amap
    blocks=[]
    for el in root.iter():
        tag=el.tag.split('}',1)[-1]
        if tag in {'p','div'}:
            t=clean_text(' '.join(el.itertext()))
            if t and (not blocks or blocks[-1]!=t): blocks.append(t)
    starts=[]
    for idx,line in enumerate(blocks):
        m=re.match(r'^Articolul\s+([0-9]+[a-zA-Z]?)$', line, flags=re.I)
        if m: starts.append((idx,m.group(1),line))
    for n,(idx,num,heading) in enumerate(starts):
        next_idx=starts[n+1][0] if n+1<len(starts) else len(blocks)
        segment=blocks[idx:next_idx]
        subtitle=''
        if len(segment)>1 and not segment[1].startswith('(') and not re.match(r'^Articolul\s+',segment[1]): subtitle=segment[1]
        item={'num':num,'heading':heading,'subtitle':subtitle,'text':'\n'.join(segment)}
        articles.append(item); amap[num.lower()] = item
    return articles, amap

def raw_markdown(instr, fetched):
    articles, amap = parse_xhtml(fetched['data'])
    selected = fetched['celex']
    dm = re.search(r'-(\d{8})$', selected)
    cdate = f'{dm.group(1)[:4]}-{dm.group(1)[4:6]}-{dm.group(1)[6:]}' if dm else 'n/a — act de bază / fără consolidare identificată în Cellar'
    title = fetched.get('title') or instr['label']
    eurlex = f'https://eur-lex.europa.eu/legal-content/RO/TXT/?uri=CELEX:{selected}'
    toc=[]
    for a in articles:
        line=f"- Articolul {a['num']}"
        if a.get('subtitle'): line += f" — {a['subtitle']}"
        toc.append(line)
    sections=[]; missing=[]
    for k in instr['key']:
        a = amap.get(k.lower())
        if not a:
            missing.append(k); continue
        heading=f"### Articolul {a['num']}"
        if a.get('subtitle'): heading += f" — {a['subtitle']}"
        sections.append(f"{heading}\n\n`[{instr['id']} art.{a['num']}]`\n\n{a['text']}\n")
    body = f"""# {instr['id']} — {instr['label']}

> **EXTRAS STRUCTURAT RO — nu textul integral.** Sursa primară este EUR-Lex / Publications Office. Fișierul păstrează metadatele, cuprinsul complet al articolelor detectate și textul integral al articolelor-cheie folosite pentru paginile wiki. Articolele neincluse integral aici trebuie verificate direct în EUR-Lex.

- **CELEX de bază:** {instr['base']}
- **CELEX folosit:** {selected}
- **tip:** {instr['kind']}
- **titlu oficial RO:** {title}
- **data consolidării:** {cdate}
- **link EUR-Lex:** {eurlex}
- **link Cellar XHTML:** {fetched['item']}
- **pagină wiki:** [[{instr['page']}]]
- **articole-cheie extrase:** {', '.join('art.'+x for x in instr['key'])}

## Cuprins complet detectat

""" + ('\n'.join(toc) if toc else '_Cuprinsul articolelor nu a putut fi detectat automat._') + "\n\n## Articole-cheie extrase integral\n\n" + ('\n'.join(sections) if sections else '_Niciun articol-cheie nu a putut fi extras automat._')
    if missing:
        body += "\n## Articole-cheie nedetectate automat\n\n" + "\n".join(f"- art.{m}" for m in missing) + "\n"
    body += f"\n## Limite ale extractului\n\n- Extras generat la {TODAY}; nu substituie verificarea textului integral EUR-Lex.\n- Dacă EUR-Lex publică o consolidare ulterioară, reingestia trebuie să compare `sha256` și data CELEX.\n"
    sha = hashlib.sha256(body.encode('utf-8')).hexdigest()
    fm = "\n".join([
        '---', f'source_url: {eurlex}', f'cellar_xhtml: {fetched["item"]}', f'ingested: {TODAY}', f'sha256: {sha}',
        'source_type: legal-text', 'publisher: EUR-Lex / Publications Office of the European Union', 'language: ro',
        f'celex: {selected}', f'base_celex: {instr["base"]}', f'instrument_id: {instr["id"]}', f'document_type: {instr["kind"]}',
        f'consolidation_date: {cdate}', 'extract: true', '---', ''
    ])
    meta={'id':instr['id'],'base_celex':instr['base'],'selected_celex':selected,'consolidation_date':cdate,'title':title,'eurlex_url':eurlex,'cellar_xhtml':fetched['item'],'articles_detected':len(articles),'key_articles_requested':instr['key'],'key_articles_missing':missing,'raw_path':f'raw/papers/cnpf/{instr["id"]}.md'}
    return fm+body, meta

def parse_fm(text):
    if not text.startswith('---\n'):
        return {}, text
    end=text.find('\n---\n',4)
    if end<0: return {}, text
    fms=text[4:end]; body=text[end+5:]
    if yaml:
        try: return yaml.safe_load(fms) or {}, body
        except Exception: return {}, body
    return {}, body

def dump_fm(fm):
    return '---\n' + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False).strip() + '\n---\n\n'

def replace_section(body, heading, content):
    block = f"\n## {heading}\n\n{content.strip()}\n"
    pat = re.compile(rf'\n## {re.escape(heading)}\n.*?(?=\n## |\Z)', flags=re.S)
    if pat.search(body): return pat.sub(block, body)
    return body.rstrip() + block

def write_page(path, fm, body):
    path.write_text(dump_fm(fm)+body.lstrip(), encoding='utf-8')
    changed.add(str(path.relative_to(ROOT)).replace('\\','/'))

def replace_line(body, prefix, new_line):
    lines=body.splitlines()
    for i,l in enumerate(lines):
        if l.startswith(prefix):
            lines[i]=new_line
            return '\n'.join(lines)+('\n' if body.endswith('\n') else '')
    return body

changed=set(); fetched_meta=[]; errors=[]

# --------- legal anchor remediation ----------
def update_legal_pages():
    # L-171
    p=ENTITIES/'L-171-2012.md'; txt=p.read_text(encoding='utf-8'); fm, body=parse_fm(txt); fm['updated']=TODAY
    body=replace_line(body,'- **mandat:**','- **mandat:** CNPF — autoritate competentă de punere în aplicare pe piața de capital. `[raw/papers/cnpf/L-171-2012.md art.1]`')
    body=replace_line(body,'- **statut:**','- **statut:** în vigoare — raw legis.md folosit indică o consolidare la 30.11.2018; pagina consemnează amendamente ulterioare, inclusiv Legea 177/2025, deci această stare rămâne **de verificat pe text consolidat integral**. `[raw/papers/cnpf/L-171-2012.md art.1]`')
    body=replace_line(body,'- **domeniu:**','- **domeniu:** piața de capital — activitatea societăților de investiții, OPC, Fondul de compensare, oferte publice/de preluare, infrastructură, abuz de piață și dezvăluire. `[raw/papers/cnpf/L-171-2012.md art.1]`')
    body=replace_line(body,'- **acquis transpus:**','- **acquis transpus:** [[acquis-MiFID]] (prin 2006/73), [[acquis-MAR]] (prin 2003/6), [[acquis-Prospectus]], [[acquis-Transparency]], [[acquis-UCITS]], [[acquis-ICSD]], [[acquis-SFD]], [[acquis-Takeover]] și alte instrumente enumerate în anexa de transpunere; statutul este parțial / învechit — vezi [[cnpf-transposition-matrix]]. `[raw/papers/cnpf/L-171-2012.md anexa de transpunere]`')
    body=body.replace('## Registre-cheie / entități supravegheate  `[raw/papers/cnpf/L-171-2012.md art.1, art.2]`\n- Societăți de investiții, categoriile A / B / C\n- Organisme de plasament colectiv; depozitari\n- Operatori de piață reglementată / MTF (Bursa de Valori a Moldovei; **BIMx** — lansare\n  așteptată toamna 2026, sub rezerva licențierii) `[știri 2026; de verificat]`\n- Fondul de compensare a investitorilor, administrat de CNPF\n- Registrele acționarilor ținute de societăți de registru',
'''## Registre-cheie / entități supravegheate
- Societăți de investiții și persoane care prestează servicii sau desfășoară activități pe piața de capital. `[raw/papers/cnpf/L-171-2012.md art.1, art.2]`
- Organisme de plasament colectiv și depozitari. `[raw/papers/cnpf/L-171-2012.md art.1]`
- Fondul de compensare a investitorilor. `[raw/papers/cnpf/L-171-2012.md art.1]`
- Piețe reglementate / infrastructura pieței de capital. `[raw/papers/cnpf/L-171-2012.md art.1]`
- Bursa de Valori a Moldovei / BIMx rămân exemple operaționale de verificat din surse CNPF/BVM, nu afirmații stabilite din raw-ul L-171. `[de verificat]`''')
    body=body.replace('## Acte normative subordonate\n- [[REG-ICF]] — Regulamentul Fondului de compensare a investitorilor\n- Regulamentul privind ținerea registrului acționarilor de către societățile de registru\n- Regulamentul privind activitatea de control pe piața financiară nebancară\n  (adaugă ancore pe măsura ingestiei fiecăruia)',
'''## Acte normative subordonate
- [[REG-ICF]] — act subordonat privind Fondul de compensare a investitorilor, conectat la domeniul art.1. `[raw/papers/cnpf/L-171-2012.md art.1]`
- Regulamentul privind ținerea registrului acționarilor și regulamentul privind controlul pe piața financiară nebancară sunt menționate ca ținte de ingestie; nu sunt încă ancorate prin raw dedicat. `[de verificat]`''')
    body=body.replace('- De confirmat dacă Ofertele de preluare 2004/25 și MiFID I 2004/39 apar expres în anexa legis.md. `[de verificat]`','- Ofertele de preluare 2004/25 sunt acoperite substanțial prin domeniul art.1, dar apariția expresă în anexa legis.md rămâne de confirmat. `[raw/papers/cnpf/L-171-2012.md art.1]` `[de verificat]`')
    body=body.replace('- **Proprietatea DCU: rezolvat** — DCU aparține BNM sub [[L-234-2016]]; Registrul de stat al\n  valorilor mobiliare și înregistrarea emisiunilor au trecut de la CNPF la DCU. Această lege\n  păstrează interfața emitenți/registre, nu proprietatea infrastructurii.', '- **Proprietatea DCU: rezolvat** — DCU aparține BNM sub [[L-234-2016]]; pentru L-171 se păstrează doar interfața cu emitenți/registre și piața de capital. `[raw/papers/cnpf/L-234-2016.md art.23]` `[raw/papers/cnpf/L-171-2012.md art.1]`')
    body=body.replace('- 2012 — adoptată (MO 193–197/2012).\n- 2020 — fondurile alternative separate în Legea 2/2020 (OPCA).\n- 2025 — Legea 177/2025: art.1(1) modificat; restricții de marketing/distribuție a instrumentelor\n  derivate cu efect de levier (CFD) pentru clienți neprofesioniști; competențe de alertă ale CNPF;\n  sancțiuni din Codul penal.', '- 2012 — adoptată (MO 193–197/2012). `[raw/papers/cnpf/L-171-2012.md art.1]`\n- 2020 — fondurile alternative separate în [[L-2-2020]]; verifică articolul exact în textul de modificare. `[de verificat]`\n- 2025 — Legea 177/2025 modifică art.1(1) privind restricțiile CFD; raw-ul L-171 disponibil local nu include textul consolidat post-2018, deci detaliile rămân de verificat pe amendament/text consolidat. `[raw/papers/cnpf/L-171-2012.md art.1]` `[de verificat]`')
    write_page(p,fm,body)
    # L-192
    p=ENTITIES/'L-192-1998.md'; txt=p.read_text(encoding='utf-8'); fm, body=parse_fm(txt); fm['updated']=TODAY
    body=replace_line(body,'- **mandat:**','- **mandat:** CNPF (lege-cadru / instituțională) — autoritate publică autonomă responsabilă față de Parlament. `[raw/papers/cnpf/L-192-1998.md art.1]`')
    body=replace_line(body,'- **statut:**','- **statut:** în vigoare — raw-ul legis.md local indică versiune consolidată 31.07.2015; transferul de mandat din 2023 trebuie citit împreună cu [[L-178-2020]]. `[raw/papers/cnpf/L-192-1998.md art.1]` `[raw/papers/cnpf/L-178-2020.md art. I, art. VIII]`')
    body=replace_line(body,'- **domeniu:**','- **domeniu:** transversal — statut, independență, obiective, finanțare, conlucrare și atribuții ale CNPF. `[raw/papers/cnpf/L-192-1998.md art.1, art.2, art.3, art.6, art.7, art.8]`')
    body=body.replace('Legea 192/1998 încadrează CNPF asupra „pieței financiare nebancare" ca întreg. Acel perimetru a\nfost **scindat prin Legea 178/2020**: de la **1 iulie 2023** BNM a devenit autoritate de\nsupraveghere pentru creditarea nebancară, asigurări, AEÎ și birourile de credit. Astfel, 192/1998\nîncă guvernează CNPF instituțional, dar în practică perimetrul său prudențial activ este **piața\nde capital** (plus funcțiile reziduale de protecție a consumatorilor/educație). Orice pagină care\ncitează 192/1998 pentru o competență în asigurări/OCN/AEÎ/birouri de credit trebuie să verifice\ndacă acea competență a trecut la BNM în 2023. `[de verificat per prevedere]`',
'''Legea 192/1998 încadrează CNPF asupra „pieței financiare nebancare" ca întreg în consolidarea locală 31.07.2015. `[raw/papers/cnpf/L-192-1998.md art.1, art.8]` Acel perimetru a fost scindat prin [[L-178-2020]]: de la **1 iulie 2023** BNM a devenit autoritate de supraveghere pentru creditarea nebancară, asigurări, AEÎ și birourile de credit. `[raw/papers/cnpf/L-178-2020.md art. I, art. VIII]` Astfel, 192/1998 încă guvernează CNPF instituțional, dar în practică perimetrul său prudențial activ este piața de capital; competențele reziduale de protecție/educație trebuie verificate per prevedere. `[de verificat per prevedere]`''')
    write_page(p,fm,body)
    # L-1134
    p=ENTITIES/'L-1134-1997.md'; txt=p.read_text(encoding='utf-8'); fm, body=parse_fm(txt); fm['updated']=TODAY
    # add company law EU sources if fetched later after update_page_sources call
    body=replace_line(body,'- **mandat:**','- **mandat:** partajat — drept societar general; CNPF intervine pentru emitenți/înregistrarea acțiunilor în cazurile prevăzute. `[raw/papers/cnpf/L-1134-1997.md art.1, art.38]`')
    body=replace_line(body,'- **statut:**','- **statut:** în vigoare — raw-ul local notează republicarea 31.12.2020 și modificări ulterioare, dar consolidarea legis.md folosită este 29.12.2017; modificările post-2017 rămân de verificat pe text consolidat. `[raw/papers/cnpf/L-1134-1997.md art.1]` `[de verificat]`')
    body=replace_line(body,'- **domeniu:**','- **domeniu:** drept societar pentru societăți pe acțiuni și interfață cu emitenții de valori mobiliare. `[raw/papers/cnpf/L-1134-1997.md art.1, art.38]`')
    body=replace_line(body,'- **acquis:**','- **acquis:** dreptul societar UE — [[acquis-CompanyLaw]]; statutul transpunerii față de 2017/1132 și SRD/SRD II rămâne de verificat articol-cu-articol. `[de verificat]`')
    body=body.replace('Statutul general de drept societar pentru societățile pe acțiuni. CNPF se bazează pe el, împreună\ncu Legea 192/1998, pentru a supraveghea SA în calitatea lor de emitenți de valori mobiliare.\n`[raw/papers/cnpf/L-1134-1997.md art.38]`', 'Statutul general de drept societar pentru societățile pe acțiuni este definit de art.1. `[raw/papers/cnpf/L-1134-1997.md art.1]` CNPF are rol punctual în înregistrarea acțiunilor plasate la înființare, conform art.38; aplicarea față de emitenți trebuie citită împreună cu [[L-171-2012]]. `[raw/papers/cnpf/L-1134-1997.md art.38]` `[raw/papers/cnpf/L-171-2012.md art.1]`')
    body=body.replace('- Noțiunea de „entitate de interes public" extinsă la entități mari din domenii de importanță pentru\n  securitatea statului (prin Legea 174/2021).', '- Noțiunea de „entitate de interes public" extinsă prin Legea 174/2021 rămâne de reconfirmat pe text post-2020; raw-ul local semnalează această nevoie, dar nu conține articolul consolidat. `[raw/papers/cnpf/L-1134-1997.md art.1]` `[de verificat]`')
    write_page(p,fm,body)

# --------- fetch and raw write ----------
def fetch_all():
    for instr in EXT_INSTRUMENTS:
        old = RAW_DIR / f"{instr['id']}.md"
        if old.exists(): shutil.copy2(old, ARCHIVE / old.name)
        try:
            fetched = select_and_fetch(instr['base'])
            content, meta = raw_markdown(instr, fetched)
            (RAW_DIR / f"{instr['id']}.md").write_text(content, encoding='utf-8')
            fetched_meta.append(meta)
            changed.add(f"raw/papers/cnpf/{instr['id']}.md")
        except Exception as e:
            errors.append({'id':instr['id'], 'base':instr['base'], 'error':f'{type(e).__name__}: {e}'})
    if errors:
        (META/f'fetch-errors-{STAMP}.json').write_text(json.dumps(errors, ensure_ascii=False, indent=2), encoding='utf-8')
        raise SystemExit('Fetch errors: '+json.dumps(errors, ensure_ascii=False))

# --------- concept updates ----------
def update_concept_pages():
    status_updates = {
        'acquis-AIFMD': '- **statut transpunere:** parțial / învechit — baza AIFMD este acoperită prin [[L-2-2020]], dar AIFMD II (Dir. 2024/927) rămâne netranspusă/de verificat. `[raw/papers/cnpf/L-2-2020.md art.1, art.2]` `[raw/papers/cnpf/UE-2011-61.md art.1, art.2, art.6]`',
        'acquis-CSDR-EMIR': '- **statut transpunere:** necunoscut / parțial — SFD și unele elemente DCU au ancore în [[L-171-2012]] și [[L-234-2016]], dar CSDR/EMIR trebuie tratate ca lacune probabile până la mapare articol-cu-articol. `[raw/papers/cnpf/UE-909-2014.md art.1]` `[raw/papers/cnpf/UE-648-2012.md art.1]`',
        'acquis-AML': '- **statut transpunere:** parțial / învechit — L-308/2017 acoperă baza AMLD, dar alinierea la pachetul AML 2024 (AMLR/AMLD6/AMLA) rămâne netranspusă/de verificat. `[raw/papers/cnpf/L-308-2017.md art.4, art.15]` `[raw/papers/cnpf/UE-2015-849.md art.1, art.2]`',
        'acquis-CompanyLaw': '- **statut transpunere:** necunoscut / de verificat — maparea [[L-1134-1997]] la Dir. 2017/1132 și la SRD/SRD II nu este încă făcută articol-cu-articol. `[raw/papers/cnpf/L-1134-1997.md art.1, art.38, art.40]`',
        'acquis-ConsumerCredit': '- **statut transpunere:** parțial / învechit — baza 2008/48/CE este posibil reflectată în regimul OCN/credit de consum, dar CCD2 (2023/2225) rămâne netranspusă/de verificat. `[raw/papers/cnpf/L-1-2018.md art.1]` `[raw/papers/cnpf/UE-2008-48.md art.1, art.2]`',
        'acquis-Insurance': '- **statut transpunere:** parțial / de verificat — [[L-92-2022]] declară aliniere la Solvency II și IDD, dar gradul de transpunere trebuie mapat articol-cu-articol; competența prudențială este la BNM din 2023. `[raw/papers/cnpf/L-92-2022.md art.1]` `[raw/papers/cnpf/UE-2009-138.md art.1]` `[raw/papers/cnpf/UE-2016-97.md art.1]`',
        'acquis-IORP': '- **statut transpunere:** parțial / de verificat — [[L-198-2020]] acoperă pensiile facultative, dar compatibilitatea cu IORP II trebuie mapată pe guvernanță, funcții-cheie, informare și activitate transfrontalieră. `[raw/papers/cnpf/L-198-2020.md art.1, art.27]` `[raw/papers/cnpf/UE-2016-2341.md art.1, art.2]`',
        'acquis-MTPL': '- **statut transpunere:** parțial / de verificat — [[L-106-2022]] transpune baza 2009/103/CE, dar amendamentele 2021/2118 privind limitele, insolvența și istoricul daunelor trebuie verificate. `[raw/papers/cnpf/L-106-2022.md art.1, art.4]` `[raw/papers/cnpf/UE-2009-103.md art.1]`',
    }
    # Existing status normalizations even for non-extended core.
    for page in ['acquis-AIFMD','acquis-CSDR-EMIR','acquis-AML','acquis-CompanyLaw','acquis-ConsumerCredit','acquis-Insurance','acquis-IORP','acquis-MTPL']:
        p=CONCEPTS/f'{page}.md'
        txt=p.read_text(encoding='utf-8'); fm, body=parse_fm(txt); fm['updated']=TODAY
        # sources
        sources=list(fm.get('sources') or [])
        for sid in PAGE_MAP.get(page, []):
            rel=f'raw/papers/cnpf/{sid}.md'
            if rel not in sources: sources.append(rel)
        fm['sources']=sources
        # status line
        if page in status_updates:
            body = re.sub(r'^- \*\*statut transpunere:\*\*.*$', status_updates[page], body, flags=re.M)
        # Surse section for extended instruments
        if page in PAGE_MAP:
            bullets=[]
            for sid in PAGE_MAP[page]:
                instr=BY_ID[sid]
                meta=next((m for m in fetched_meta if m['id']==sid), None)
                if not meta: continue
                arts=', '.join(f'`[raw/papers/cnpf/{sid}.md art.{a}]`' for a in instr['key'][:5])
                if len(instr['key'])>5: arts += '…'
                miss = f" Articole nedetectate: {', '.join(meta['key_articles_missing'])}." if meta['key_articles_missing'] else ''
                bullets.append(f"- `{sid}` — {instr['label']}; CELEX folosit `{meta['selected_celex']}`; consolidare: {meta['consolidation_date']}; articole-cheie: {arts}.{miss}")
            body = replace_section(body, 'Surse EUR-Lex RO ingerate', '\n'.join(bullets))
        write_page(p,fm,body)

# --------- manifest / index / log ----------
def update_manifest_index_log():
    manifest = (RAW_DIR/'_manifest.md').read_text(encoding='utf-8') if (RAW_DIR/'_manifest.md').exists() else '# Manifest CNPF\n'
    heading='## G. Acquis UE — domenii conexe CNPF/BNM (EUR-Lex RO)'
    rows=[heading,'',f'Ingestie EUR-Lex RO extinsă efectuată la **{TODAY}** pentru paginile acquis conexe semnalate de lint. Toate fișierele sunt **extracte structurate**, nu text integral.','', '| ID raw | Instrument | Pagină wiki | CELEX folosit | Data consolidării | Observație |','|---|---|---|---|---|---|']
    for meta in fetched_meta:
        instr=BY_ID[meta['id']]
        rows.append(f"| `{instr['id']}` | {instr['label']} | [[{instr['page']}]] | `{meta['selected_celex']}` | {meta['consolidation_date']} | extract RO: cuprins + articole-cheie |")
    section='\n'.join(rows)+'\n'
    if heading in manifest:
        manifest=re.sub(rf'\n{re.escape(heading)}\n.*?(?=\n## |\Z)', '\n'+section, manifest, flags=re.S)
    else:
        manifest=manifest.rstrip()+'\n\n'+section
    (RAW_DIR/'_manifest.md').write_text(manifest, encoding='utf-8'); changed.add('raw/papers/cnpf/_manifest.md')
    # index
    def page_title(path):
        txt=path.read_text(encoding='utf-8'); fm, body=parse_fm(txt)
        if fm.get('title'): return str(fm['title'])
        for line in body.splitlines():
            if line.startswith('# '): return line[2:].strip()
        return path.stem
    def summary(title): return re.sub(r'^[A-Za-z0-9_-]+\s+—\s+','',title).strip()[:180]
    sections={'Entities':sorted((ROOT/'entities').glob('*.md')), 'Concepts':sorted((ROOT/'concepts').glob('*.md')), 'Comparisons':sorted((ROOT/'comparisons').glob('*.md')), 'Queries':sorted((ROOT/'queries').glob('*.md'))}
    total=sum(len(v) for v in sections.values())
    lines=['# Wiki Index','', '> Content catalog. Every wiki page is listed under its type with a one-line summary.', '> Read this first to find relevant pages for any query.', f'> Last updated: {TODAY} | Total pages: {total}', '']
    for sec, files in sections.items():
        lines += [f'## {sec}','']
        if files:
            for p in sorted(files, key=lambda x:x.stem.lower()): lines.append(f'- [[{p.stem}]] — {summary(page_title(p))}')
        elif sec=='Queries': lines.append('<!-- No query pages yet -->')
        lines.append('')
    (ROOT/'index.md').write_text('\n'.join(lines), encoding='utf-8'); changed.add('index.md')
    # log
    entry=f"""
## [{TODAY}] update | Execute all CNPF remediation and extended EUR-Lex ingest

- Backup used: `{BACKUP}`.
- Legal anchor remediation applied to `entities/L-171-2012.md`, `entities/L-192-1998.md`, and `entities/L-1134-1997.md`; no unresolved `[de verificat]` was converted into a settled fact.
- Normalized transposition status wording in `concepts/acquis-AIFMD.md` and `concepts/acquis-CSDR-EMIR.md`.
- Fetched/wrote structured Romanian EUR-Lex extracts for {len(fetched_meta)} connected acquis instruments covering AML, Company Law, Consumer Credit, Insurance, IORP, and MTPL.
- Updated `raw/papers/cnpf/_manifest.md` section `G. Acquis UE — domenii conexe CNPF/BNM` and updated six connected acquis pages with raw anchors.
""".strip()
    logp=ROOT/'log.md'; log=logp.read_text(encoding='utf-8')
    logp.write_text(log.rstrip()+'\n\n'+entry+'\n', encoding='utf-8'); changed.add('log.md')

# Run
update_legal_pages()
fetch_all()
update_concept_pages()
update_manifest_index_log()

# basic audit
# verify links/frontmatter/index/raw presence
pages=[]
for sub in ['entities','concepts','comparisons','queries']:
    pages += list((ROOT/sub).glob('*.md'))
stems={p.stem for p in pages}
index=(ROOT/'index.md').read_text(encoding='utf-8')
broken=[]; missing_index=[]; missing_fm=[]; raw_missing=[]
for p in pages:
    txt=p.read_text(encoding='utf-8')
    if not txt.startswith('---\n'): missing_fm.append(str(p.relative_to(ROOT)).replace('\\','/'))
    for link in re.findall(r'\[\[([^\]]+)\]\]', txt):
        target=link.split('|')[0].split('#')[0].strip()
        if target and target not in stems: broken.append({'file':str(p.relative_to(ROOT)).replace('\\','/'),'target':target})
    if f'[[{p.stem}]]' not in index: missing_index.append(str(p.relative_to(ROOT)).replace('\\','/'))
for instr in EXT_INSTRUMENTS:
    if not (RAW_DIR/f'{instr["id"]}.md').exists(): raw_missing.append(instr['id'])
audit={'date':TODAY,'backup':str(BACKUP),'archive':str(ARCHIVE),'fetched_count':len(fetched_meta),'fetched':fetched_meta,'errors':errors,'changed_files':sorted(changed),'broken_links':broken,'missing_frontmatter':missing_fm,'missing_index':missing_index,'raw_missing':raw_missing}
(META/'execute-all-remediation-audit.json').write_text(json.dumps(audit, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(audit, ensure_ascii=False, indent=2))
