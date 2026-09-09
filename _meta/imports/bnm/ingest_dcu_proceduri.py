"""Ingerarea Procedurilor DCU (dcu.md, PDF-uri) in raw/papers/bnm/dcu/.

Sora scriptului ingest_dcu_rules.py, pentru un set de documente, nu unul. Procedurile sint acte ale
Comitetului executiv al DCU (art. 4 alin. (2) din Regulile DCU), publicate pe
https://www.dcu.md/ro/reglementari/procedurile-dcu, cite un PDF fiecare. Nu sint pe legis.md.

Ce face:
  1. citeste fiecare PDF din _meta/imports/bnm/dcu/proceduri/, il hashuieste (source_file_sha256);
  2. extrage textul cu PyMuPDF, pagina cu pagina, get_text(); liniile se curata de spatiile de
     capat si liniile goale se elimina; NIMIC altceva nu se schimba (nici antetul "PUBLIC" si
     numerele de pagina, nici cuprinsul, nici nota de copyright, nici diacriticele desprinse de
     cuvint pe care le produce fontul unor documente: "garan ț iilor");
  3. NU insereaza ancore: procedurile sint numerotate pe puncte in forme diferite (1., 1.1, a)),
     fara articole si fara capitole; o trimitere la "pct. N" NU este ancorata;
  4. refuza documentele fara strat de text: un PDF ale carui pagini sint imagini (glifele randate
     ca imagini, fara font) nu se ingereaza pina nu exista OCR; se raporteaza si se arhiveaza doar
     originalul, cu hash.

Rulare:  python _meta/imports/bnm/ingest_dcu_proceduri.py --precheck   (afiseaza fisa, nu scrie)
         python _meta/imports/bnm/ingest_dcu_proceduri.py              (scrie fisierele)
         python _meta/imports/bnm/ingest_dcu_proceduri.py --verify     (re-extrage si compara)
"""
import datetime, hashlib, re, sys
from pathlib import Path

import fitz
import yaml

ROOT = Path(__file__).resolve().parents[3]
SRC_DIR = ROOT / '_meta' / 'imports' / 'bnm' / 'dcu' / 'proceduri'
OUT_DIR = ROOT / 'raw' / 'papers' / 'bnm' / 'dcu'
SOURCE_PAGE = 'https://www.dcu.md/ro/reglementari/procedurile-dcu'
TODAY = datetime.date.today().isoformat()
TEXT_MARKER = '## Text integral extras din PDF (dcu.md)'
MIN_CHARS_PER_PAGE = 400   # sub acest prag paginile sint imagini, nu text

# Ordinea si titlurile sint cele de pe pagina dcu.md la 2026-09-09. `url` este calea de pe server,
# cu %20 acolo unde numele are spatii; `file` este numele local, fara spatii.
DOCS = {
    'DCU-PROC-DECONTARE': {
        'file': 'Proceduri_operatiuni_decontare.pdf',
        'url': 'https://www.dcu.md/doc/Proceduri%20operatiuni%20decontare.pdf',
        'title': 'Proceduri privind operațiunile de decontare',
        'scope': 'decontarea operațiunilor cu VMC (vânzarea, donația, succesiunea); decontarea '
                 'operațiunilor cu VMS și CBN, operațiuni reversibile (REPO, overnight); decontarea '
                 'operațiunilor încheiate la BVM și BAS; conturi de valori mobiliare (tipuri, mod de '
                 'creare); eliberarea extrasului din cont și rapoartelor privind decontarea VM'},
    'DCU-PROC-INREGISTRARE-VM': {
        'file': 'Proceduri_Inregistrare_VM.pdf',
        'url': 'https://www.dcu.md/doc/Proceduri%20Inregistrare%20VM.pdf',
        'title': 'Proceduri privind înregistrarea emitentului și valorilor mobiliare',
        'scope': 'înregistrarea valorilor mobiliare corporative și emitenților de VMC; înregistrarea '
                 'VMS și CBN; înregistrarea în custodie și retragerea VM înregistrate în custodie; '
                 'servicii adiționale pentru emitenți (eliberarea listei acționarilor)'},
    'DCU-PROC-PARTICIPANT': {
        'file': 'Proceduri_inregistrare_participant.pdf',
        'url': 'https://www.dcu.md/doc/Proceduri%20inregistrare%20participant.pdf',
        'title': 'Proceduri privind înregistrarea participantului DCU',
        'scope': 'entitățile care pot deveni participant la DCU; solicitarea și documente prezentate '
                 'la DCU; cerințe tehnice față de solicitant; utilizatorii participantului'},
    'DCU-PROC-RECONCILIERE': {
        'file': 'Proceduri_reconciliere_2023.pdf',
        'url': 'https://www.dcu.md/doc/Proceduri_reconciliere_2023.pdf',
        'title': 'Proceduri de reconciliere',
        'scope': 'etapele procedurii de reconciliere; tipul și structura rapoartelor expediate de DCU '
                 'în scop de reconciliere; modul de remediere a divergențelor'},
    'DCU-PROC-INSOLVABILITATE': {
        'file': 'Proceduri_insolvabilitate.pdf',
        'url': 'https://www.dcu.md/doc/Proceduri%20insolvabilitate.pdf',
        'title': 'Proceduri aplicate în cazul insolvabilității participantului',
        'scope': 'cazuri de insolvabilitate a participantului (procedura de insolvabilitate vs. '
                 'insolvabilitatea operațională); etapele gestionării cazului; cerințe de informare'},
    'DCU-PROC-DETINATOR': {
        'file': 'Proceduri_inregistrare_detinator.pdf',
        'url': 'https://www.dcu.md/doc/Proceduri%20inregistrare%20detinator.pdf',
        'title': 'Proceduri privind înregistrarea deținătorului de VM',
        'scope': 'înregistrarea profilului investitorului de către participant; rapoarte privind '
                 'deținerile și operațiunile investitorului'},
    'DCU-PROC-RECLAMATII': {
        'file': 'Proceduri_reclamatii_DCU.pdf',
        'url': 'https://www.dcu.md/doc/Proceduri%20reclamatii%20DCU.pdf',
        'title': 'Proceduri reclamații DCU',
        'scope': 'modul de adresare și examinare a reclamațiilor de către DCU'},
    'DCU-PROC-GARANTII': {
        'file': 'Proceduri_constituirea_garantiilor_apeluri_marja.pdf',
        'url': 'https://www.dcu.md/doc/Proceduri%20privind%20constituirea%20garantiilor%20si%20apelurile%20in%20marja.pdf',
        'title': 'Proceduri privind constituirea garanțiilor și apelurile în marjă',
        'scope': 'operațiuni în baza contractelor de garanție financiară; eligibilitatea valorilor '
                 'mobiliare ca garanții; înregistrarea, reevaluarea, apelul în marjă, înlocuirea, '
                 'eliberarea și executarea garanției'},
    'DCU-PROC-COMISIOANE': {
        'file': 'Proceduri_modul_de_calcul_si_percepere_a_plati_DCU.pdf',
        'url': 'https://www.dcu.md/doc/Proceduri_modul_de_calcul_si_percepere_a_plati_DCU.pdf',
        'title': 'Proceduri privind modul de calcul și percepere a plăților și comisioanelor de către DCU',
        'scope': 'mărimea plăților și comisioanelor; calculul sumelor spre plată; perceperea de la '
                 'participanți, emitenți, deținători de VMC și alte persoane'},
}


def extract(pdf_path):
    doc = fitz.open(str(pdf_path))
    lines, per_page = [], []
    for page in doc:
        t = page.get_text()
        per_page.append(len(t))
        for raw in t.split('\n'):
            line = raw.strip()
            if line:
                lines.append(line)
    return doc, lines, per_page


def has_text_layer(doc, per_page):
    """Un document este text daca paginile de corp (fara prima, coperta) au text; paginile
    randate ca imagini dau doar antetul si numarul de pagina."""
    body = per_page[1:] or per_page
    return sum(1 for c in body if c >= MIN_CHARS_PER_PAGE) >= max(1, len(body) // 2)


def body_hash(text):
    blob = text.encode('utf-8')
    fence = re.search(rb'^---\s*$', blob[3:], re.M)
    return hashlib.sha256(blob[3 + fence.end():]).hexdigest()


def cover(lines, n=28):
    """Primele linii ale paginii de titlu, pentru fisa; sint text de sursa, se reproduc ca atare."""
    return lines[:n]


def build(stem, spec, doc, lines, pdf_sha, plain_sha):
    src = SRC_DIR / spec['file']
    head = [
        f"# raw/{stem} — {spec['title']} (Procedurile DCU, dcu.md)", '',
        '> **TEXT DCU.MD RO — extras din PDF-ul publicat de Depozitarul central unic și păstrat '
        'pentru audit.** Nu corectez și nu armonizez tăcut textul. Fără ancore de articol: '
        'procedurile sînt numerotate pe puncte, în forme diferite; o trimitere la „pct. N" nu este '
        'ancorată. Extracția este identică cu corpul de sub marcajul de text (`sha256_extraction`).', '',
        f"- **Sursă de referință:** {SOURCE_PAGE}",
        f"- **Fișier-sursă:** {spec['url']} ({src.stat().st_size} octeți, sha256 `{pdf_sha}`), "
        f"arhivat la `{src.relative_to(ROOT).as_posix()}`",
        f"- **Obiect, după pagina dcu.md:** {spec['scope']}",
        '- **Natura actului:** procedură a Comitetului executiv al DCU, adoptată în temeiul art. 4 '
        'alin. (2) din Regulile DCU (`raw/papers/bnm/legal-ro/DCU-REGULI-2026.md`), obligatorie '
        'pentru participanți, emitenți și deținători conform art. 4 alin. (3) din Reguli; nu este '
        'act al BNM și nu se publică pe legis.md.',
        '- **articole detectate:** 0',
        f"- **pagini PDF:** {doc.page_count}; **linii nevide extrase:** {len(lines)}",
        '- **Aprobarea și intrarea în vigoare:** în pagina de titlu a documentului, reprodusă mai jos '
        'în text; nu sînt reluate aici ca să nu fie transcrise de mînă.',
        '', '## Pagina de titlu, primele linii extrase', '',
    ]
    head += [f"    {l}" for l in cover(lines)]
    head += ['', TEXT_MARKER, '']
    body_text = '\n'.join(head + lines).strip() + '\n'
    fm = {
        'source_url': spec['url'],
        'source_page': SOURCE_PAGE,
        'ingested': TODAY,
        'sha256': 'x',
        'sha256_extraction': plain_sha,
        'source_file': src.relative_to(ROOT).as_posix(),
        'source_file_sha256': pdf_sha,
        'source_type': 'legal-text',
        'publisher': 'Depozitarul Central Unic al Valorilor Mobiliare (dcu.md), Comitetul executiv',
        'language': 'ro',
        'instrument_id': stem,
        'official_title_detected': spec['title'],
        'full_text': True,
        'extract_method': 'PyMuPDF get_text() pagina cu pagina; spatii de capat si linii goale '
                          'eliminate; fara ancore',
        'pages': doc.page_count,
    }
    fm_text = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False).strip()
    out = '---\n' + fm_text + '\n---\n\n' + body_text
    return re.sub(r'^sha256:\s*\S+', 'sha256: ' + body_hash(out), out, count=1, flags=re.M)


def plain_text(lines):
    return '\n'.join(lines) + '\n'


def verify():
    fails = 0
    for stem, spec in DOCS.items():
        out = OUT_DIR / f"{stem}.md"
        src = SRC_DIR / spec['file']
        print(f"\n{stem}")
        if not out.exists():
            print("  (fara fisier brut; document fara strat de text, neingerat)")
            continue
        md = out.read_text(encoding='utf-8')
        doc, lines, per_page = extract(src)
        fm = yaml.safe_load(md.split('---', 2)[1])
        pdf_sha = hashlib.sha256(src.read_bytes()).hexdigest()
        ok = fm['source_file_sha256'] == pdf_sha
        print(f"  pdf sha256              : {'PASS' if ok else 'FAIL'}"); fails += not ok
        written = [l for l in md.split(TEXT_MARKER, 1)[1].split('\n') if l]
        same = written == lines
        print(f"  text integrity          : {'PASS' if same else 'FAIL'} ({len(written)} lines written vs {len(lines)} reference)")
        if not same:
            fails += 1
            for i, (a, b) in enumerate(zip(written, lines)):
                if a != b:
                    print(f"    first divergence at {i}: {a[:90]!r} vs {b[:90]!r}")
                    break
        ex = hashlib.sha256(plain_text(lines).encode('utf-8')).hexdigest()
        ok = fm['sha256_extraction'] == ex
        print(f"  sha256_extraction       : {'PASS' if ok else 'FAIL'}"); fails += not ok
        ok = fm['sha256'] == body_hash(md)
        print(f"  sha256 (body)           : {'PASS' if ok else 'FAIL'}"); fails += not ok
        anchors = len(re.findall(r'^## Articolul ', md, re.M))
        print(f"  article anchors         : {anchors} (asteptat 0) {'PASS' if anchors == 0 else 'FAIL'}"); fails += anchors != 0
    print(f"\nFAILURES: {fails}")
    return fails


def main():
    args = sys.argv[1:]
    if '--verify' in args:
        sys.exit(1 if verify() else 0)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for stem, spec in DOCS.items():
        src = SRC_DIR / spec['file']
        doc, lines, per_page = extract(src)
        pdf_sha = hashlib.sha256(src.read_bytes()).hexdigest()
        textual = has_text_layer(doc, per_page)
        print(f"{stem}: pagini={doc.page_count} linii={len(lines)} caractere/pagina="
              f"{[c for c in per_page][:6]}... text={'DA' if textual else 'NU, pagini-imagine'} "
              f"sha256={pdf_sha[:12]}")
        if '--precheck' in args:
            print('  coperta: ' + ' | '.join(cover(lines, 14))[:400])
            continue
        if not textual:
            print(f"  -> NEINGERAT: {spec['file']} nu are strat de text; original arhivat, OCR necesar")
            continue
        plain_sha = hashlib.sha256(plain_text(lines).encode('utf-8')).hexdigest()
        out = build(stem, spec, doc, lines, pdf_sha, plain_sha)
        (OUT_DIR / f"{stem}.md").write_bytes(out.encode('utf-8'))
        print(f"  -> {(OUT_DIR / (stem + '.md')).relative_to(ROOT).as_posix()}")


if __name__ == '__main__':
    main()
