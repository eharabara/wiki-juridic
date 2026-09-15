"""Ingerarea partiala a Acordului de Asociere RM-UE (AA-2014) in raw/papers/cnpf/.

De ce partiala. Decizia D1 din planul pasului 6 (_meta/plans/2026-09-15-plan-pasul-6-acquis-aa.md):
documentul intreg (CELEX 22014A0830(01)) are 793 de articole si ~11 MB, iar perimetrul CNPF/BNM
al acestui vault se margineste la Capitolul 9 (Serviciile financiare) si la Anexa XXVIII-A pe care
acesta o invoca. Nu se ingereaza actul intreg.

Ce se ingereaza, patru bucati, fiecare delimitata de identificatori stabili ai documentului sursa
(atribute id ELI din HTML-ul EUR-Lex, nu numere de linie, care s-ar putea sa nu supravietuiasca
unei republicari):
  1. Capitolul 9 "Serviciile financiare" (art. 58-61), div id="tis_IV.cpt_9" pina la "tis_IV.cpt_10".
     Art. 61 este clauza de apropiere legislativa ce trimite la Anexa XXVIII-A.
  2. Art. 459-465, dispozitiile finale relevante (anexe si protocoale, durata, definirea partilor,
     aplicare teritoriala, depozitar, intrarea in vigoare si aplicarea cu titlu provizoriu, textele
     autentice), de la id="d1e13797-4-1" (art. 459) pina la semnatura "DREPT CARE...".
  3. Anexa XXVIII-A "Norme aplicabile serviciilor financiare", de la
     id="L_2014260RO.01040601" pina la "L_2014260RO.01041201" (inceputul Anexei XXVIII-B).
  4. Cele doua notificari oficiale ale datelor (aplicare provizorie, intrare in vigoare) si art. 3
     din Decizia 2014/492/UE a Consiliului (temeiul legal al datei corecte pentru Anexa XXVIII-A:
     vezi corectarea din log.md, 2026-09-15 -- calendarul curge de la aplicarea provizorie,
     1 septembrie 2014, nu de la intrarea in vigoare, 1 iulie 2016, pentru ca art. 464 alin. (5)
     converteste "data intrarii in vigoare" in "data aplicarii provizorii" pentru dispozitiile
     aplicate provizoriu, iar Capitolul 9 si Anexa XXVIII sint printre ele, art. 3 alin. (1) lit.
     (d) si (h) din decizie).

Surse, toate citite direct prin curl, fara nicio bariera de tip Cloudflare (spre deosebire de
legis.md): vezi memoria legis-md-search-via-curl -- aceasta nu se aplica aici, EUR-Lex e altfel.
  - Acordul insusi:            CELEX 22014A0830(01)
  - Notificare aplicare provizorie: CELEX 22014X0830(02)   (JO L 260, 30.8.2014, p. 1)
  - Notificare intrare in vigoare:  CELEX 22016X0618(03)   (JO L 161, 18.6.2016)
  - Decizia Consiliului 2014/492/UE (scopul aplicarii provizorii): CELEX 32014D0492

Rulare:
    python ingest_aa_2014.py --precheck   afiseaza extrasele, nu scrie nimic
    python ingest_aa_2014.py              scrie raw/papers/cnpf/AA-2014.md
    python ingest_aa_2014.py --verify     re-descarca, re-extrage, compara cu fisierul scris
"""
import datetime
import hashlib
import html as ihtml
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
RAW_OUT = ROOT / "raw" / "papers" / "cnpf" / "AA-2014.md"
CACHE_DIR = ROOT / "_meta" / "imports" / "cnpf" / "aa-2014"
CACHE_DIR.mkdir(parents=True, exist_ok=True)
TODAY = datetime.date.today().isoformat()
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120 Safari/537.36")

SOURCES = {
    "agreement": "22014A0830(01)",
    "notice_provisional": "22014X0830(02)",
    "notice_force": "22016X0618(03)",
    "council_decision": "32014D0492",
}


def fetch(celex: str) -> str:
    """curl direct; EUR-Lex nu are bariera Cloudflare-like, spre deosebire de legis.md."""
    url = f"https://eur-lex.europa.eu/legal-content/RO/TXT/?uri=CELEX:{celex}"
    r = subprocess.run(["curl", "-sL", "--max-time", "120", "-A", UA, url],
                        capture_output=True)
    if r.returncode != 0:
        raise RuntimeError(f"curl a esuat pentru {celex}, rc={r.returncode}")
    text = r.stdout.decode("utf-8", "replace")
    if len(text) < 5000:
        raise RuntimeError(f"raspuns suspect de mic pentru {celex}: {len(text)} octeti")
    return text


def cached(name: str, celex: str) -> str:
    p = CACHE_DIR / f"{name}.html"
    if p.exists():
        return p.read_text(encoding="utf-8")
    html_text = fetch(celex)
    p.write_text(html_text, encoding="utf-8", newline="\n")
    return html_text


def tag_start_before(html_text: str, pos: int) -> int:
    """Pozitia lui '<' care deschide tag-ul ce contine `pos` (unde `pos` e in mijlocul unui
    atribut, ex. chiar dupa 'id='). Taind aici, nu la `pos`, fragmentul nu se opreste in
    mijlocul unui tag deschis -- altfel TAG_RE nu il mai recunoaste (nu are '>' de inchidere)
    si textul lui brut ('<div id=' etc.) ramine nesters in iesire."""
    lt = html_text.rfind("<", 0, pos)
    if lt == -1:
        raise ValueError("niciun '<' inaintea pozitiei date")
    return lt


def between_id(html_text: str, start_id: str, end_id: str) -> str:
    """Taie fragmentul HTML intre doua atribute id= ELI, ambele capete stabile in document.
    Capatul de sfirsit se taie la inceputul tag-ului care poarta end_id, nu la 'id=' insusi."""
    si = html_text.find(f'id="{start_id}"')
    if si == -1:
        raise ValueError(f"id de start negasit: {start_id}")
    ei = html_text.find(f'id="{end_id}"', si)
    if ei == -1:
        raise ValueError(f"id de sfirsit negasit: {end_id}")
    return html_text[si:tag_start_before(html_text, ei)]


def between_text(html_text: str, start_marker: str, end_marker: str) -> str:
    si = html_text.find(start_marker)
    if si == -1:
        raise ValueError(f"marcaj de start negasit: {start_marker!r}")
    ei = html_text.find(end_marker, si)
    if ei == -1:
        raise ValueError(f"marcaj de sfirsit negasit: {end_marker!r}")
    return html_text[si:ei]


def from_id_to_text(html_text: str, start_id: str, end_marker: str) -> str:
    """La fel ca between_id, dar capatul de sfirsit e text simplu (nu un id de tag), si
    capatul de start se taie inaintea tag-ului intreg, nu la 'id=' -- altfel primul marcaj
    oj-ti-art din fragment nu se mai potriveste cu ART_ID_RE (ii lipseste '<p ' din fata)."""
    si_raw = html_text.find(f'id="{start_id}"')
    if si_raw == -1:
        raise ValueError(f"id de start negasit: {start_id}")
    si = tag_start_before(html_text, si_raw)
    ei = html_text.find(end_marker, si_raw)
    if ei == -1:
        raise ValueError(f"marcaj de sfirsit negasit: {end_marker!r}")
    return html_text[si:ei]


TAG_RE = re.compile(r"<[^>]+>")
WS_RE = re.compile(r"[ \t]+")


def html_to_paragraphs(fragment: str) -> list[str]:
    """Strip la tag-uri, un rind per element de bloc (p, div.oj-box). NIMIC din text nu se
    rescrie -- doar spatiile de capat de linie provenite din indentarea sursei se normalizeaza,
    ca sa nu ramina zeci de spatii in fata fiecarui paragraf."""
    # separatori intre elemente de bloc, ca sa nu se lipeasca doua paragrafe intr-o singura linie
    fragment = re.sub(r"</(p|div|li)>", "\n", fragment)
    fragment = re.sub(r"<(p|div|li)[^>]*>", "\n", fragment)
    fragment = re.sub(r"<br\s*/?>", "\n", fragment)
    text = TAG_RE.sub("", fragment)
    text = ihtml.unescape(text)
    lines = [WS_RE.sub(" ", ln).strip() for ln in text.splitlines()]
    return [ln for ln in lines if ln]


ART_ID_RE = re.compile(r'<p id="([^"]+)" class="oj-ti-art">Articolul (\d+)</p>')
# Titlul unui articol, cind exista, sta separat in sursa: <div class="eli-title">...
#   <p class="oj-sti-art">Titlu</p></div>, imediat dupa marcajul oj-ti-art. Nu orice articol
# are asa ceva (art. 58, 59, 60 din capitolul 9 nu au); de-aici nu se ghiceste dupa forma
# textului, se citeste marcajul propriu al sursei.
ART_TITLE_RE = re.compile(r'^\s*<div class="eli-title"[^>]*>\s*<p class="oj-sti-art">([^<]*)</p>\s*</div>')


def extract_articles(fragment: str) -> list[tuple[int, str | None, list[str]]]:
    """Imparte un fragment in articole, folosind marcajele oj-ti-art proprii sursei ca ancore.
    Intoarce [(numar_articol, titlu_sau_None, [paragrafe...]), ...], in ordinea din sursa."""
    marks = list(ART_ID_RE.finditer(fragment))
    if not marks:
        raise ValueError("niciun marcaj oj-ti-art gasit in fragment")
    out = []
    for i, m in enumerate(marks):
        num = int(m.group(2))
        start = m.end()
        end = marks[i + 1].start() if i + 1 < len(marks) else len(fragment)
        chunk = fragment[start:end]
        title = None
        tm = ART_TITLE_RE.match(chunk)
        if tm:
            title = ihtml.unescape(tm.group(1)).strip()
            chunk = chunk[tm.end():]
        paras = html_to_paragraphs(chunk)
        out.append((num, title, paras))
    return out


def build_body() -> str:
    agreement = cached("agreement", SOURCES["agreement"])
    notice_prov = cached("notice_provisional", SOURCES["notice_provisional"])
    notice_force = cached("notice_force", SOURCES["notice_force"])
    decision = cached("council_decision", SOURCES["council_decision"])

    chapter9 = between_id(agreement, "tis_IV.cpt_9", "tis_IV.cpt_10")
    articles_459_465 = from_id_to_text(agreement, "d1e13797-4-1", "DREPT CARE")
    annex_28a = between_id(agreement, "L_2014260RO.01040601", "L_2014260RO.01041201")

    ch9_articles = extract_articles(chapter9)
    fin_articles = extract_articles(articles_459_465)
    # art. 465 nu are marcaj de sfirsit prin urmatorul articol (e ultimul); textul lui se
    # opreste la "DREPT CARE" prin taietura between_id de mai sus, deci extract_articles il
    # prinde corect ca ultimul element.

    annex_paras = html_to_paragraphs(annex_28a)
    # primele doua linii sint titlul ("ANEXA XXVIII-A", "NORME APLICABILE SERVICIILOR FINANCIARE");
    # restul alterneaza intre denumirea instrumentului si linia "Calendar: ...".

    def para_containing(html_text: str, needle: str) -> str | None:
        """Gaseste <p class="oj-normal">...</p> care contine needle, indiferent de tag-uri
        imbricate inauntru (note de subsol etc.); DOTALL, prima potrivire care are needle."""
        for m in re.finditer(r'<p class="oj-normal">(.*?)</p>', html_text, re.S):
            if needle in m.group(1):
                return WS_RE.sub(" ", ihtml.unescape(TAG_RE.sub("", m.group(1))).strip())
        return None

    notice_prov_para = para_containing(notice_prov, "titlu provizoriu")
    notice_force_para = para_containing(notice_force, "vigoare la data de")

    # art. 3 din decizia 2014/492/UE: fragment intre "Articolul 3" si "Articolul 4"; capetele
    # sint id-uri complete de tag (nu doar textul vizibil), ca taietura sa nu cada in mijlocul
    # unui tag deschis, ceea ce ar lasa text HTML nestripat in iesire.
    art3 = between_text(decision, '<p id="d1e146-1-1" class="oj-ti-art">Articolul 3</p>',
                         '<p id="d1e212-1-1" class="oj-ti-art">')
    art3_paras = html_to_paragraphs(art3)

    L = []
    a = L.append

    a("# AA-2014 — Acordul de Asociere Republica Moldova–Uniunea Europeană (extras)")
    a("")
    a("> **EXTRAS, NU TEXTUL INTEGRAL.** Documentul complet (CELEX `22014A0830(01)`) are 793 de "
      "articole și cca. 11 MB; perimetrul acestui vault se mărginește la Capitolul 9 (Serviciile "
      "financiare) și la Anexa XXVIII-A pe care acesta o invocă, plus dispozițiile finale ale "
      "acordului și cele două notificări oficiale ale datelor. Restul acordului (comerțul cu "
      "mărfuri, celelalte capitole și anexe, cooperarea politică) nu e ingerat — vezi decizia D1 "
      "din `_meta/plans/2026-09-15-plan-pasul-6-acquis-aa.md`.")
    a("")
    a("- **CELEX acord:** `22014A0830(01)`")
    a("- **titlu oficial:** Acordul de asociere dintre Uniunea Europeană și Comunitatea Europeană "
      "a Energiei Atomice și statele membre ale acestora, pe de o parte, și Republica Moldova, pe "
      "de altă parte")
    a("- **semnat:** 27 iunie 2014, Bruxelles")
    a("- **publicat:** JO L 260, 30.8.2014, p. 4")
    a("- **pagină wiki:** [[AA-2014]]")
    a("")
    a("## Datele — și temeiul lor legal exact")
    a("")
    a("Două date distincte, fiecare cu propria notificare oficială pe EUR-Lex, citite integral, nu "
      "doar din câmpul de metadate al documentului principal:")
    a("")
    if notice_prov_para:
        a(f"**Aplicare cu titlu provizoriu: 1 septembrie 2014.** `CELEX 22014X0830(02)`, "
          f"JO L 260, 30.8.2014, p. 1:")
        a("")
        a(f"> {notice_prov_para}")
        a("")
    if notice_force_para:
        a(f"**Intrare în vigoare: 1 iulie 2016.** `CELEX 22016X0618(03)`, JO L 161, 18.6.2016:")
        a("")
        a(f"> {notice_force_para}")
        a("")
    a("**Care dată guvernează Anexa XXVIII-A: 1 septembrie 2014, nu 1 iulie 2016.** Art. 464 "
      "alin. (5) din acord (mai jos) convertește orice trimitere la „data de intrare în vigoare a "
      "prezentului acord\", din dispozițiile aplicate cu titlu provizoriu, într-o trimitere la "
      "„data de la care prezentul acord se aplică cu titlu provizoriu\". Care dispoziții au fost "
      "aplicate provizoriu se stabilește prin art. 3 alin. (1) din Decizia 2014/492/UE a "
      "Consiliului (`CELEX 32014D0492`), reprodus integral mai jos: litera (d) include titlul IV "
      "capitolul 9 (Serviciile financiare, deci art. 58-61 de mai jos) și litera (h) include "
      "anexele XV-XXXV (interval ce cuprinde Anexa XXVIII întreagă). Prin urmare calendarul "
      "Anexei XXVIII-A curge de la **1 septembrie 2014**.")
    a("")
    a("### Art. 3 din Decizia 2014/492/UE a Consiliului (`CELEX 32014D0492`) — scopul aplicării provizorii")
    a("")
    for p in art3_paras:
        a(p)
        a("")
    a("## Capitolul 9 — Serviciile financiare (Titlul IV)")
    a("")
    a("Arts. 58-61. Art. 61 este clauza de apropiere legislativă ce trimite la Anexa XXVIII-A.")
    a("")
    for num, title, paras in ch9_articles:
        a(f"## Articolul {num}" + (f". {title}" if title else ""))
        for p in paras:
            a(p)
        a("")
    a("## Dispoziții finale relevante (art. 459-465)")
    a("")
    for num, title, paras in fin_articles:
        a(f"## Articolul {num}" + (f". {title}" if title else ""))
        for p in paras:
            a(p)
        a("")
    a("## Anexa XXVIII-A — Norme aplicabile serviciilor financiare")
    a("")
    a("41 de instrumente UE la care Republica Moldova s-a angajat să își apropie legislația, "
      "fiecare cu propriul calendar. Calendarul complet, calculat de la 1 septembrie 2014, e în "
      "`_meta/plans/2026-09-15-plan-pasul-6-acquis-aa.md`, secțiunea 2.2-ter.")
    a("")
    # sarim primele doua linii (titlul dublu, deja in H2 de mai sus)
    for p in annex_paras[2:]:
        a(p)
    a("")
    return "\n".join(L).rstrip() + "\n"


def frontmatter(sha256_hex: str) -> str:
    return f"""---
source_url: https://eur-lex.europa.eu/legal-content/RO/TXT/?uri=CELEX:22014A0830(01)
ingested: {TODAY}
sha256: {sha256_hex}
source_type: legal-text
publisher: EUR-Lex / Jurnalul Oficial al Uniunii Europene
language: ro
celex: 22014A0830(01)
instrument_id: AA-2014
document_type: acord de asociere (extras)
extract: true
signed: 2014-06-27
provisional_application: 2014-09-01
entry_into_force: 2016-07-01
---
"""


def write(precheck: bool) -> None:
    body = build_body()
    digest = hashlib.sha256(body.encode("utf-8")).hexdigest()
    if precheck:
        print(body[:6000])
        print("...")
        print(f"[precheck] {len(body)} octeți, sha256={digest}")
        return
    RAW_OUT.write_text(frontmatter(digest) + body, encoding="utf-8", newline="\n")
    print(f"scris {RAW_OUT}: {len(body)} octeți corp, sha256={digest}")


def verify() -> None:
    if not RAW_OUT.exists():
        print("AA-2014.md nu există încă"); sys.exit(1)
    written = RAW_OUT.read_text(encoding="utf-8")
    fm_end = written.find("\n---", 3)
    body_written = written[written.find("\n", fm_end + 1) + 1:]
    body_fresh = build_body()
    if body_written == body_fresh:
        print("VERIFY OK: corpul scris este identic cu o nouă extracție din sursele cache-uite.")
    else:
        print("VERIFY FAIL: diferență între corpul scris și o nouă extracție.")
        for i, (a_, b_) in enumerate(zip(body_written.splitlines(), body_fresh.splitlines())):
            if a_ != b_:
                print(f"prima diferență la linia {i}:\n  scris:  {a_!r}\n  fresh:  {b_!r}")
                break
        sys.exit(1)


if __name__ == "__main__":
    if "--precheck" in sys.argv:
        write(precheck=True)
    elif "--verify" in sys.argv:
        verify()
    else:
        write(precheck=False)
