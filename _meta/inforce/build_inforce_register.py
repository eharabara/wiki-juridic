"""Registrul dispozitiilor care nu sint inca in vigoare (sau nu mai sint).

De ce exista. Textul consolidat de pe legis.md incorporeaza si modificarile cu
intrare in vigoare amanata. Un fisier poate fi deci curat ancorat, cu sha256
verificat, si totusi sa arate ca abrogata o dispozitie care astazi se aplica.
L-171-2012 este cazul: consolidarea este datata 2027-06-01, iar art. 38 si
art. 141^1 apar abrogate desi abrogarea produce efecte abia la 01.06.2027.

Ce face. Scaneaza raw/ dupa marcajele "in vigoare DD.MM.YY", pastreaza doar pe
cele cu data in viitor, le leaga de articolul pe care il privesc si scrie un
registru. Nu modifica niciun fisier de drept: singurele scrieri sint in
_meta/inforce/.

Ce NU face. Nu reconstruieste versiunea in vigoare a unui text rescris. Cind o
consolidare viitoare inlocuieste redactarea unui articol, textul de astazi pur
si simplu nu se afla in fisier, iar un marcaj nu poate suplini un text absent.
Registrul semnaleaza situatia si indica arhiva consolidarii anterioare, cu
avertismentul ca aceea este o consolidare mai veche, nu neaparat versiunea in
vigoare astazi.

Consolidari viitoare neingerate (2026-09-07). Cind legis.md publica deja o
consolidare cu data in viitor, iar wiki-ul tine, dinadins, textul in vigoare
astazi, nimic din raw/ nu poarta marcajele acelei consolidari. Lista lor se
tine de mina in _meta/inforce/pending-consolidations.json, cu articolele citite
versiune contra versiune pe legis.md, si este redata ca sectiune separata.
Scriptul nu o verifica pe legis.md; data verificarii sta in fisier.

Utilizare:
    python build_inforce_register.py --dry-run     # nu scrie nimic, doar raporteaza
    python build_inforce_register.py               # scrie registrul
    python build_inforce_register.py --check       # iese 1 daca registrul de pe disc difera
    python build_inforce_register.py --as-of 2027-06-02   # simuleaza o alta zi
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import re
import sys
import unicodedata
from pathlib import Path

# --------------------------------------------------------------------------
# Cai. Derivate din locul scriptului, cu suprascriere prin --root.
# --------------------------------------------------------------------------

DEFAULT_ROOT = Path(__file__).resolve().parents[2]
OUT_SUBDIR = Path("_meta") / "inforce"
REGISTER_MD = "in-force-register.md"
REGISTER_JSON = "in-force-register.json"
PENDING_JSON = "pending-consolidations.json"  # intrare scrisa de mina, vezi docstring

# --------------------------------------------------------------------------
# Tipare. Corpusul foloseste doua codificari de diacritice si ambele forme
# "in"/"in", deci textul este normalizat NFC inainte de potrivire, iar clasa
# de caractere le acopera pe amindoua.
# --------------------------------------------------------------------------

IN_FORCE = re.compile(
    r"[îÎiI]n\s+vigoare\s*(?:din|la|de\s+la)?\s*"
    r"(\d{1,2})\.(\d{1,2})\.(\d{2,4})",
    re.IGNORECASE,
)

# Referinta la articol din interiorul unei note de modificare: [Art.38 abrogat ...]
ART_IN_NOTE = re.compile(
    r"Art\.\s*(\d+(?:\^\d+)?)"
    r"((?:\s*(?:alin\.\s*\(\s*\d+(?:\^\d+)?\s*\)|pct\.\s*\d+(?:\^\d+)?"
    r"|lit\.\s*[a-zA-Z\u0219\u015f\u0163\u021b](?:\^\d+)?\))\,?)*)",
    re.IGNORECASE,
)

# Ancora de articol inserata la ancorare: "## Articolul 38." sau "## Articolul 141^1"
ART_ANCHOR = re.compile(r"^##\s+Articolul\s+(\d+(?:\^\d+)?)", re.MULTILINE)

# Actul modificator: LP162 din 30.07.26
AMENDING_ACT = re.compile(r"\b(LP\d+|HG\d+|LC\d+)\s+din\s+(\d{1,2}\.\d{1,2}\.\d{2,4})")

# Monitorul Oficial: MO390-393/25.08.26 art.416
MO_REF = re.compile(r"\bMO[\d\-]+/\d{1,2}\.\d{1,2}\.\d{2,4}(?:\s+art\.\d+)?")

OPERATIONS = [
    ("abrogat", "abrogare"),
    ("modificat", "modificare"),
    ("completat", "completare"),
    ("introdus", "introducere"),
    ("redactia", "reformulare"),
    ("republicat", "republicare"),
]

# Fisiere care sint comentariu propriu, nu text de lege.
SKIP_NAMES = {"_manifest.md"}


def parse_date(day: str, month: str, year: str) -> _dt.date | None:
    y = int(year)
    if y < 100:
        y += 2000
    try:
        return _dt.date(y, int(month), int(day))
    except ValueError:
        return None


def read_frontmatter(text: str) -> dict:
    """Citire minimala a frontmatterului. Doar chei plate, ceea ce ne ajunge."""
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    block = text[3:end]
    out: dict[str, str] = {}
    for line in block.splitlines():
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line)
        if m:
            out[m.group(1)] = m.group(2).strip().strip("'\"")
    return out


def frontmatter_span(text: str) -> int:
    """Indexul la care se termina frontmatterul, ca sa nu atribuim articole in el."""
    if not text.startswith("---"):
        return 0
    end = text.find("\n---", 3)
    return end + 4 if end != -1 else 0


def enclosing_note(text: str, pos: int, window: int = 400) -> str:
    """Nota [ ... ] care contine pozitia data. Nu trece peste linie goala."""
    lo = max(0, pos - window)
    open_at = text.rfind("[", lo, pos)
    if open_at == -1:
        return ""
    close_at = text.find("]", pos, pos + window)
    if close_at == -1:
        return ""
    note = text[open_at : close_at + 1]
    if "\n\n" in note:
        return ""
    return note


def detect_operation(note: str) -> str:
    low = unicodedata.normalize("NFKD", note.lower())
    low = "".join(c for c in low if not unicodedata.combining(c))
    for needle, label in OPERATIONS:
        if needle in low:
            return label
    return "nespecificat"


def preceding_article(text: str, pos: int, body_start: int) -> str | None:
    """Ultima ancora '## Articolul N.' inaintea pozitiei, in corp."""
    last = None
    for m in ART_ANCHOR.finditer(text, body_start, pos):
        last = m.group(1)
    return last


def scan_file(path: Path, rel: str, as_of: _dt.date) -> tuple[list[dict], dict]:
    raw = path.read_text(encoding="utf-8", errors="replace")
    text = unicodedata.normalize("NFC", raw)
    fm = read_frontmatter(text)
    body_start = frontmatter_span(text)

    entries: list[dict] = []
    for m in IN_FORCE.finditer(text):
        eff = parse_date(*m.groups())
        if eff is None or eff <= as_of:
            continue
        note = enclosing_note(text, m.start())
        art = None
        am = ART_IN_NOTE.search(note) if note else None
        subunit = ""
        if am:
            art = am.group(1)
            subunit = " ".join((am.group(2) or "").split()).strip(" ,")
        elif m.start() >= body_start:
            art = preceding_article(text, m.start(), body_start)
        context = note if note else text[max(0, m.start() - 160) : m.end() + 40]
        context = " ".join(context.split())
        act_m = AMENDING_ACT.search(context)
        mo_m = MO_REF.search(context)
        entries.append(
            {
                "file": rel,
                "instrument": fm.get("instrument_id") or path.stem,
                "article": art,
                "subunit": subunit,
                "scope": "articol" if art else "act",
                "effective_from": eff.isoformat(),
                "operation": detect_operation(note),
                "amending_act": f"{act_m.group(1)} din {act_m.group(2)}" if act_m else None,
                "official_gazette": mo_m.group(0) if mo_m else None,
                "line": text.count("\n", 0, m.start()) + 1,
                "context": context[:300],
            }
        )
    return entries, fm


def dedupe(entries: list[dict]) -> list[dict]:
    """O dispozitie apare de mai multe ori: frontmatter, antet, corp, manifest.
    Cheia este dispozitia, nu aparitia. Liniile se pastreaza toate."""
    merged: dict[tuple, dict] = {}
    for e in entries:
        key = (e["instrument"], e["article"], e.get("subunit", ""),
               e["amending_act"], e["effective_from"])
        if key in merged:
            cur = merged[key]
            cur["lines"].append(e["line"])
            cur["occurrences"] += 1
            if cur["operation"] == "nespecificat" and e["operation"] != "nespecificat":
                cur["operation"] = e["operation"]
                cur["context"] = e["context"]
            if not cur["official_gazette"]:
                cur["official_gazette"] = e["official_gazette"]
        else:
            item = dict(e)
            item["lines"] = [e.pop("line")]
            item["occurrences"] = 1
            item.pop("line", None)
            merged[key] = item
    out = list(merged.values())
    out.sort(key=lambda x: (x["effective_from"], x["instrument"], str(x["article"])))
    return out


def article_sort_key(a: str | None):
    if not a:
        return (0, 0)
    base, _, sup = a.partition("^")
    try:
        return (int(base), int(sup) if sup else 0)
    except ValueError:
        # anexe si alte unitati fara numar de articol (lista scrisa de mina), la sfirsit
        return (10**6, 0)


def load_pending(path: Path, as_of: _dt.date) -> list[dict]:
    """Consolidarile viitoare neingerate, din fisierul scris de mina. O consolidare a
    carei data a trecut nu mai este "pending": ea trebuie reimprospatata, deci este
    lasata deoparte aici si semnalata la iesire."""
    if not path.exists():
        return []
    data = json.loads(path.read_text(encoding="utf-8"))
    out: list[dict] = []
    for c in data.get("consolidations", []):
        cd = _dt.date.fromisoformat(c["consolidation_date"])
        if cd <= as_of:
            print(f"ATENTIE: {c['instrument']} {c['doc_id']}@{c['consolidation_date']} a intrat "
                  f"in vigoare; nu mai este viitoare, trebuie reimprospatata", file=sys.stderr)
            continue
        provs = [p for p in c.get("provisions", [])
                 if _dt.date.fromisoformat(p["effective_from"]) > as_of]
        provs.sort(key=lambda x: article_sort_key(x["article"]))
        item = dict(c)
        item["provisions"] = provs
        out.append(item)
    out.sort(key=lambda x: (x["consolidation_date"], x["instrument"]))
    return out


STATE_TODAY = {
    "abrogare": "inca in vigoare",
    "modificare": "se aplica textul anterior",
    "completare": "completarea nu se aplica",
    "introducere": "dispozitia nu se aplica",
    "reformulare": "se aplica textul anterior",
}


def build(root: Path, as_of: _dt.date) -> dict:
    rawdir = root / "raw"
    if not rawdir.is_dir():
        raise SystemExit(f"nu gasesc {rawdir}")

    all_entries: list[dict] = []
    future_acts: list[dict] = []
    scanned = 0

    for path in sorted(rawdir.rglob("*.md")):
        if path.name in SKIP_NAMES:
            continue
        scanned += 1
        rel = path.relative_to(root).as_posix()
        entries, fm = scan_file(path, rel, as_of)
        all_entries.extend(entries)

        cons = fm.get("consolidation_date")
        if cons:
            try:
                cd = _dt.date.fromisoformat(cons)
            except ValueError:
                cd = None
            if cd and cd > as_of:
                future_acts.append(
                    {
                        "instrument": fm.get("instrument_id") or path.stem,
                        "file": rel,
                        "consolidation_date": cons,
                        "doc_id": fm.get("doc_id"),
                        "previous_consolidation_date": fm.get("consolidation_date_previous"),
                        "previous_archive": fm.get("archived_previous_at"),
                        "flagged_in_frontmatter": fm.get("consolidation_is_future") == "true",
                    }
                )

    # Rindurile fara articol provin din frontmatter si din tabelul de antet: ele
    # descriu actul, nu o dispozitie, si sint deja acoperite de a doua sectiune.
    provisions = [p for p in dedupe(all_entries) if p["article"]]
    provisions.sort(key=lambda x: (x["effective_from"], x["instrument"], article_sort_key(x["article"])))
    future_acts.sort(key=lambda x: x["instrument"])

    pending = load_pending(root / OUT_SUBDIR / PENDING_JSON, as_of)

    return {
        "generated": _dt.datetime.now().isoformat(timespec="seconds"),
        "as_of": as_of.isoformat(),
        "files_scanned": scanned,
        "provisions_not_yet_in_force": provisions,
        "acts_with_future_consolidation": future_acts,
        "pending_consolidations": pending,
        "counts": {
            "provisions": len(provisions),
            "acts": len({p["instrument"] for p in provisions}),
            "future_consolidations": len(future_acts),
            "pending_consolidations": len(pending),
            "pending_provisions": sum(len(c["provisions"]) for c in pending),
        },
    }


def render_md(data: dict) -> str:
    L: list[str] = []
    A = L.append
    A("---")
    A("title: Registrul dispozitiilor care nu sint inca in vigoare")
    A(f"generated: '{data['generated']}'")
    A(f"as_of: '{data['as_of']}'")
    A("type: summary")
    A("tags: [moldova, legal-source, methodology, summary]")
    A("confidence: high")
    A("generated_by: _meta/inforce/build_inforce_register.py")
    A("---")
    A("")
    A("# Ce nu este in vigoare astazi, desi apare in text")
    A("")
    A("**Fisier generat. Nu se editeaza manual.** Se reface rulind scriptul din frontmatter.")
    A("")
    A(
        f"Stare la {data['as_of']}. {data['files_scanned']} fisiere scanate. "
        f"{data['counts']['provisions']} dispozitii afectate in "
        f"{data['counts']['acts']} act(e). "
        f"{data['counts']['future_consolidations']} consolidare/consolidari cu data in viitor. "
        f"{data['counts']['pending_consolidations']} consolidare/consolidari viitoare neingerate, "
        f"{data['counts']['pending_provisions']} dispozitii."
    )
    A("")
    A("## Regula de citare")
    A("")
    A(
        "Inainte de a cita un articol, verifica daca apare in tabelul de mai jos. "
        "Daca apare, spune in raspuns care versiune se aplica astazi si de cind se aplica cealalta. "
        "Un articol listat aici este ancorat corect si are un sha256 valid, deci nimic altceva "
        "din wiki nu semnaleaza problema."
    )
    A("")
    A("## Dispozitii afectate")
    A("")
    if not data["provisions_not_yet_in_force"]:
        A("Niciuna la data de mai sus.")
    else:
        A("| Act | Articol | Operatiune | Produce efecte de la | Act modificator | Stare astazi |")
        A("|---|---|---|---|---|---|")
        for p in data["provisions_not_yet_in_force"]:
            art = p["article"] + (" " + p["subunit"] if p.get("subunit") else "")
            state = {
                "abrogare": "inca in vigoare",
                "modificare": "se aplica textul anterior",
                "completare": "completarea nu se aplica",
                "introducere": "dispozitia nu se aplica",
                "reformulare": "se aplica textul anterior",
            }.get(p["operation"], "de verificat")
            A(
                f"| {p['instrument']} | {art} | {p['operation']} | {p['effective_from']} "
                f"| {p['amending_act'] or '-'} | {state} |"
            )
    A("")
    A("## Acte cu consolidare datata in viitor")
    A("")
    if not data["acts_with_future_consolidation"]:
        A("Niciunul.")
    else:
        A(
            "Fisierul incorporeaza modificari care nu au intrat in vigoare. Arhiva indicata este "
            "consolidarea anterioara, **nu neaparat versiunea in vigoare astazi**: ea poate fi ea "
            "insasi depasita. Pentru abrogari amanate, textul curent ramine cel bun, cu exceptia "
            "articolelor din tabelul de mai sus. Pentru reformulari amanate, textul de astazi poate "
            "lipsi cu totul din wiki."
        )
        A("")
        A("| Act | Consolidare | Semnalat in frontmatter | Consolidare anterioara | Arhiva |")
        A("|---|---|---|---|---|")
        for a in data["acts_with_future_consolidation"]:
            A(
                f"| {a['instrument']} | {a['consolidation_date']} "
                f"| {'da' if a['flagged_in_frontmatter'] else 'nu'} "
                f"| {a['previous_consolidation_date'] or '-'} "
                f"| `{a['previous_archive'] or '-'}` |"
            )
    A("")
    A("## Consolidari viitoare neingerate")
    A("")
    if not data.get("pending_consolidations"):
        A("Niciuna consemnata. Lista se tine in `_meta/inforce/pending-consolidations.json`.")
    else:
        A(
            "Cazul invers al sectiunii precedente: wiki-ul tine textul in vigoare astazi, iar "
            "legis.md a publicat deja consolidarea viitoare. Marcajele ei nu exista in raw/, deci "
            "scanarea nu le poate vedea. Articolele de mai jos au fost citite versiune contra "
            "versiune pe legis.md, fara descarcare, la data din coloana \"Verificat\". Textul din "
            "wiki este cel care se aplica astazi; de la data indicata se aplica textul consolidarii "
            "neingerate, care trebuie citit pe legis.md sau ingerat sub identificator distinct. "
            "Cind data trece, actul se reimprospateaza si rindul se sterge din fisierul de intrare."
        )
        A("")
        A("| Act | Consolidare neingerata | Text detinut | Act modificator | Verificat | Metoda |")
        A("|---|---|---|---|---|---|")
        for c in data["pending_consolidations"]:
            A(
                f"| {c['instrument']} | {c['doc_id']} @ {c['consolidation_date']} "
                f"| {c['held_doc_id']} @ {c['held_consolidation_date']} "
                f"| {c['amending_act']}, {c.get('official_gazette', '-')} "
                f"| {c['verified']} | {c['method']} |"
            )
        A("")
        A("| Act | Articol | Operatiune | Produce efecte de la | Act modificator | Stare astazi | Ce se schimba |")
        A("|---|---|---|---|---|---|---|")
        for c in data["pending_consolidations"]:
            for p in c["provisions"]:
                art = p["article"] + (" " + p["subunit"] if p.get("subunit") else "")
                A(
                    f"| {c['instrument']} | {art} | {p['operation']} | {p['effective_from']} "
                    f"| {c['amending_act']} | {STATE_TODAY.get(p['operation'], 'de verificat')} "
                    f"| {p.get('summary', '')} |"
                )
    A("")
    A("## Unde a fost gasit fiecare marcaj")
    A("")
    for p in data["provisions_not_yet_in_force"]:
        art = p["article"] + (" " + p["subunit"] if p.get("subunit") else "")
        A(f"- **{p['instrument']} art. {art}**, `{p['file']}`, liniile {p['lines']}")
        A(f"  - {p['context']}")
    A("")
    return "\n".join(L)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    ap.add_argument("--as-of", type=str, default=None, help="YYYY-MM-DD, implicit astazi")
    ap.add_argument("--dry-run", action="store_true", help="nu scrie nimic")
    ap.add_argument("--check", action="store_true", help="iese 1 daca registrul de pe disc difera")
    args = ap.parse_args()

    root = args.root.resolve()
    as_of = _dt.date.fromisoformat(args.as_of) if args.as_of else _dt.date.today()

    data = build(root, as_of)
    md = render_md(data)

    outdir = (root / OUT_SUBDIR).resolve()
    # Garda: scriem exclusiv sub _meta/inforce/. Nimic din raw/ nu este atins.
    if not str(outdir).startswith(str(root)) or outdir.name != "inforce":
        raise SystemExit(f"refuz sa scriu in {outdir}")

    c = data["counts"]
    print(
        f"as-of {data['as_of']}: {data['files_scanned']} fisiere, "
        f"{c['provisions']} dispozitii in {c['acts']} act(e), "
        f"{c['future_consolidations']} consolidare/consolidari viitoare"
    )
    for p in data["provisions_not_yet_in_force"]:
        print(f"  {p['instrument']} art. {p['article']}  {p['operation']}  de la {p['effective_from']}")
    for c in data.get("pending_consolidations", []):
        for p in c["provisions"]:
            print(f"  [neingerat {c['doc_id']}] {c['instrument']} art. {p['article']} "
                  f"{p.get('subunit','')}  {p['operation']}  de la {p['effective_from']}")

    if args.check:
        cur_md = (outdir / REGISTER_MD)
        if not cur_md.exists():
            print("CHECK: registrul lipseste")
            return 1
        old = cur_md.read_text(encoding="utf-8")
        # Datele nu conteaza la comparatie (2026-09-06): daca o dispozitie a intrat intre timp
        # in vigoare, continutul tabelului se schimba si controlul pica oricum.
        strip = lambda s: re.sub(r"^(generated|as_of):.*$|Stare la \d{4}-\d\d-\d\d\.", "", s, flags=re.M)
        if strip(old) != strip(md):
            print("CHECK: registrul de pe disc este invechit")
            return 1
        print("CHECK: registrul este la zi")
        return 0

    if args.dry_run:
        print("\n--- dry-run, nimic scris. Registrul ar arata asa: ---\n")
        print(md)
        return 0

    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / REGISTER_MD).write_text(md, encoding="utf-8")
    (outdir / REGISTER_JSON).write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"\nscris: {outdir / REGISTER_MD}")
    print(f"scris: {outdir / REGISTER_JSON}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
