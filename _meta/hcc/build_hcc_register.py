"""Registrul dispozitiilor declarate neconstitutionale in actele detinute.

De ce exista. Cind Curtea Constitutionala declara neconstitutional un articol sau un text
dintr-un articol, legis.md nu scoate textul din consolidare: il lasa in loc si pune un marcaj
linga el. La urmatoarea reimprospatare marcajul cade (mecanismul 1 din intrebarea deschisa 3
a CLAUDE.md) si ramine numai rindul "HCCnn din dd.mm.yy" in fisa actului, fara articol. Textul
anulat se citeste atunci ca lege. La 8 septembrie 2026: 19 acte, 76 de hotariri in fise, 16
marcaje inca vizibile la articol (`_meta/plans/hcc-census-2026-09-08.md`).

Ce face. Scaneaza raw/ dupa marcajele HCC in ambele forme pe care le foloseste legis.md:
  [Art.N ... declarat neconstitutional prin HCCnn din dd.mm.yy, MO...]      (paranteze drepte)
  *Art.N ... declarat neconstitutional prin HCCnn ...  /  *Nota: Articolul N ...  (asterisc)
  Nota: Art.N ... declarata neconstitutionala prin HCCnn din dd.mm.yy, MO...      (fara asterisc)
si le leaga de articol. Citeste apoi `_meta/hcc/recovered-provisions.json`, scris de mina, cu
dispozitiile ale caror marcaje s-au pierdut si au fost recuperate citind pe legis.md versiunea
produsa de hotarire (metoda U.7, fetch fara descarcare); fiecare rind poarta doc_id-ul versiunii
citite. Redă apoi, pe act, hotaririle din fisa care nu au inca niciun articol atribuit, ca golul
sa fie vizibil, nu tacut. Nu modifica niciun fisier de drept; scrie doar in _meta/hcc/.

Ce NU face. Nu verifica nimic pe legis.md. Nu judeca daca o hotarire e de anulare sau de
interpretare: pentru cele recuperate, cimpul "operation" din JSON spune; pentru cele din fisa
fara articol nu se stie. Nu citeste hotaririle care nu apar in fisa niciunui act detinut.

Utilizare:
    python build_hcc_register.py             # scrie registrul
    python build_hcc_register.py --check     # iese 1 daca registrul de pe disc difera
    python build_hcc_register.py --dry-run   # doar raporteaza
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import re
import sys
import unicodedata
from pathlib import Path

DEFAULT_ROOT = Path(__file__).resolve().parents[2]
OUT_SUBDIR = Path("_meta") / "hcc"
REGISTER_MD = "hcc-register.md"
REGISTER_JSON = "hcc-register.json"
RECOVERED_JSON = "recovered-provisions.json"
SCAN_DIRS = ["raw/papers/cnpf", "raw/papers/moldova-legal", "raw/papers/bnm/legal-ro"]

HCC_ID = re.compile(r"HCC\s*(\d+)\s+din\s+(\d{1,2})\.(\d{1,2})\.(\d{2,4})")
BRACKET = re.compile(r"\[([^\[\]]*?HCC[^\[\]]*?)\]")
NECONST = re.compile(r"neconstitu", re.IGNORECASE)
ART_IN_MARK = re.compile(r"^\s*(?:Not[aă]:\s*)?Art(?:icolul|\.)\s*(\d+(?:\^\d+)?(?:/\d+)?)", re.IGNORECASE)
SUBUNIT = re.compile(
    r"((?:al(?:in)?\.\s*\(\s*\d+(?:\^\d+)?\s*\)|alin\.\s*\(\d+\)\s*-\s*\(\d+\)|lit\.\s*[a-zA-Zșşţț](?:\^\d+)?\)|pct\.\s*\d+)"
    r"(?:\s*(?:,|și|şi|si|-)\s*(?:al(?:in)?\.\s*\(\s*\d+(?:\^\d+)?\s*\)|lit\.\s*[a-zA-Zșşţț](?:\^\d+)?\)|\(\d+\)))*)",
    re.IGNORECASE,
)
QUOTED = re.compile(r"[„\"“]([^”\"“„]{3,200})[”\"“]")
# A treia forma, gasita 2026-09-19 la COD-325-2022: linia incepe cu "Nota:" fara asterisc si
# fara paranteze drepte. Cele 13 atribuiri ale acelui act sint toate asa, si pina la fixul de
# fata cadeau in ramura "rind de fisa", deci actul aparea cu 4 hotariri si ZERO articole
# atribuite, desi textul le numeste pe toate. Garda e aceeasi ca la forma cu asterisc
# (HCC_ID + NECONST), deci nu poate transforma o nota oarecare intr-o atribuire.
NOTA = re.compile(r"^Not[aă]\s*:", re.IGNORECASE)
MO = re.compile(r"(MO\s?[\d\-–]+/\s?\d{1,2}\.\d{1,2}\.\d{2,4}(?:\s*(?:art|cm)\.?\s*\d+)?)", re.IGNORECASE)


def nfc(s: str) -> str:
    return unicodedata.normalize("NFC", s)


def hcc_key(n: str, d: str, m: str, y: str) -> str:
    if len(y) == 2:
        y = ("19" if int(y) > 50 else "20") + y
    return f"HCC{int(n)}/{y}-{int(m):02d}-{int(d):02d}"


def read_frontmatter(text: str) -> dict:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    fm = {}
    for line in text[3:end].splitlines():
        m = re.match(r"^([A-Za-z_0-9]+):\s*(.*)$", line)
        if m:
            fm[m.group(1)] = m.group(2).strip().strip("'\"")
    return fm


def body_start(text: str) -> int:
    if not text.startswith("---"):
        return 0
    end = text.find("\n---", 3)
    return text.find("\n", end + 1) + 1


def scope_of(mark: str) -> str:
    """Intinderea: articolul intreg, un alineat, un text citat, o omisiune."""
    low = mark.lower()
    if "omisiun" in low:
        return "omisiune legislativa"
    if QUOTED.search(mark) and ("textul" in low or "sintagma" in low or "cuvintele" in low):
        return "text din articol"
    if "în partea" in low or "in partea" in low:
        return "in parte"
    if SUBUNIT.search(mark):
        return "subunitate"
    return "articol intreg"


def parse_mark(mark: str) -> dict | None:
    mark = nfc(mark).strip()
    ids = [hcc_key(*g) for g in HCC_ID.findall(mark)]
    if not ids:
        return None
    a = ART_IN_MARK.match(mark)
    sub = SUBUNIT.search(mark[a.end():a.end() + 80]) if a else None
    q = QUOTED.search(mark)
    mo = MO.search(mark)
    return {
        "article": a.group(1) if a else None,
        "subunit": sub.group(1).strip() if sub else None,
        "quoted_text": q.group(1) if q else None,
        "scope": scope_of(mark),
        "hcc": ids,
        "official_gazette": mo.group(1) if mo else None,
        "marker": mark[:400],
    }


def scan_file(path: Path, rel: str) -> tuple[list[dict], list[dict], dict]:
    text = path.read_text(encoding="utf-8")
    fm = read_frontmatter(text)
    if fm.get("source_type") == "translation":
        return [], [], fm
    start = body_start(text)
    marks, fisa = [], []
    # numerotarea este cea a fisierului (frontmatter inclus), ca sa fie clicabila
    for i, raw_line in enumerate(text[start:].splitlines(), text[:start].count("\n") + 1):
        line = nfc(raw_line)
        st = line.strip()
        found = [m.group(1) for m in BRACKET.finditer(line)]
        if not found and st.startswith("*") and HCC_ID.search(st) and NECONST.search(st):
            found = [st.lstrip("*").strip()]
        if not found and NOTA.match(st) and HCC_ID.search(st) and NECONST.search(st):
            found = [st]
        if found:
            for mk in found:
                p = parse_mark(mk)
                if p:
                    p["line"] = i
                    marks.append(p)
            continue
        for g in HCC_ID.findall(line):
            fisa.append({"hcc": hcc_key(*g), "line": i, "text": st[:200]})
    return marks, fisa, fm


def load_recovered(path: Path) -> list[dict]:
    if not path.exists():
        return []
    data = json.loads(path.read_text(encoding="utf-8"))
    return data.get("provisions", [])


def build(root: Path) -> dict:
    acts = []
    for d in SCAN_DIRS:
        for p in sorted((root / d).glob("*.md")):
            if p.name.startswith("_") or p.name.startswith("UE-"):
                continue
            rel = str(p.relative_to(root)).replace("\\", "/")
            marks, fisa, fm = scan_file(p, rel)
            if not marks and not fisa:
                continue
            acts.append({
                "instrument": p.stem, "file": rel, "doc_id": fm.get("doc_id"),
                "consolidation_date": fm.get("consolidation_date"),
                "markers": marks, "fisa": fisa,
            })

    recovered = load_recovered(root / OUT_SUBDIR / RECOVERED_JSON)
    rec_by_act: dict[str, list[dict]] = {}
    for r in recovered:
        rec_by_act.setdefault(r["instrument"], []).append(r)

    for a in acts:
        known = set()
        for m in a["markers"]:
            known.update(m["hcc"])
        for r in rec_by_act.get(a["instrument"], []):
            known.add(r["hcc"])
        seen = set()
        unattributed = []
        for f in a["fisa"]:
            if f["hcc"] not in known and f["hcc"] not in seen:
                unattributed.append(f)
                seen.add(f["hcc"])
        a["recovered"] = rec_by_act.get(a["instrument"], [])
        a["unattributed"] = unattributed
        a["distinct_hcc"] = sorted({f["hcc"] for f in a["fisa"]} | known)

    total_hcc = sorted({h for a in acts for h in a["distinct_hcc"]})
    return {
        "generated": _dt.date.today().isoformat(),
        "acts": acts,
        "counts": {
            "acts": len(acts),
            "distinct_hcc": len(total_hcc),
            "markers_in_text": sum(len(a["markers"]) for a in acts),
            "recovered": len(recovered),
            "unattributed": sum(len(a["unattributed"]) for a in acts),
        },
    }


def render_md(data: dict) -> str:
    c = data["counts"]
    L = []
    A = L.append
    A("# Registrul dispozitiilor declarate neconstitutionale")
    A("")
    A(f"Generat {data['generated']} de `_meta/hcc/build_hcc_register.py`. Nu edita de mina; "
      "dispozitiile recuperate se scriu in `recovered-provisions.json`.")
    A("")
    A(f"{c['acts']} acte cu cel putin o hotarire a Curtii Constitutionale in fisa, "
      f"{c['distinct_hcc']} hotariri distincte. Articolul atins este cunoscut pentru "
      f"{c['markers_in_text']} marcaje inca prezente in text si {c['recovered']} dispozitii "
      f"recuperate din istoricul versiunilor; **{c['unattributed']} hotariri nu au inca niciun "
      "articol atribuit**, deci textul pe care l-au anulat se citeste azi ca lege.")
    A("")
    A("Regula de citare: un articol din tabelele de mai jos se citeaza numai cu mentiunea "
      "hotaririi si a intinderii anularii. Un act din tabelul „fara articol atribuit” se citeaza "
      "cu avertismentul ca poarta hotariri ale Curtii neverificate la nivel de articol.")
    A("")
    A("## Sumar pe act")
    A("")
    A("| act | doc_id | consolidare | HCC in fisa | cu articol cunoscut | fara articol |")
    A("|---|---|---|---:|---:|---:|")
    for a in data["acts"]:
        known = len(a["distinct_hcc"]) - len(a["unattributed"])
        A(f"| `{a['instrument']}` | {a['doc_id']} | {a['consolidation_date']} | "
          f"{len(a['distinct_hcc'])} | {known} | {len(a['unattributed'])} |")
    A("")
    A("## Dispozitii cu articol cunoscut")
    A("")
    A("| act | articol | subunitate | intindere | hotarire | MO | sursa |")
    A("|---|---|---|---|---|---|---|")
    for a in data["acts"]:
        rows = []
        for m in a["markers"]:
            rows.append((m["article"], m["subunit"], m["scope"], ", ".join(m["hcc"]),
                         m["official_gazette"], f"marcaj in text, l.{m['line']}", m.get("quoted_text")))
        for r in a["recovered"]:
            rows.append((r.get("article"), r.get("subunit"), r.get("scope"), r["hcc"],
                         r.get("official_gazette"), f"versiunea {r.get('read_doc_id')} @ {r.get('read_consolidation')}, verificat {r.get('verified')}",
                         r.get("quoted_text")))
        for art, sub, sc, h, mo, src, q in rows:
            cell_sc = sc or ""
            if q:
                cell_sc += f" („{q[:90]}{'…' if len(q) > 90 else ''}”)"
            A(f"| `{a['instrument']}` | {art or '?'} | {sub or ''} | {cell_sc} | {h} | {mo or ''} | {src} |")
    A("")
    A("## Hotariri din fisa fara articol atribuit")
    A("")
    A("Marcajul s-a pierdut la o reimprospatare anterioara a consolidarii. Articolul se recupereaza "
      "citind pe legis.md versiunea produsa de hotarire (istoricul de versiuni, `showDetails`), "
      "prin `fetch` in pagina, fara descarcare, si se scrie in `recovered-provisions.json`.")
    A("")
    A("| act | hotarire | rindul din fisa |")
    A("|---|---|---|")
    for a in data["acts"]:
        for f in a["unattributed"]:
            A(f"| `{a['instrument']}` | {f['hcc']} | l.{f['line']}: {f['text'][:120]} |")
    A("")
    return "\n".join(L) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    root = args.root.resolve()
    data = build(root)
    md = render_md(data)
    js = json.dumps(data, ensure_ascii=False, indent=1) + "\n"
    out = root / OUT_SUBDIR
    c = data["counts"]
    summary = (f"{c['acts']} acte, {c['distinct_hcc']} hotariri, {c['markers_in_text']} marcaje in text, "
               f"{c['recovered']} recuperate, {c['unattributed']} fara articol")
    if args.check:
        old = (out / REGISTER_MD).read_text(encoding="utf-8") if (out / REGISTER_MD).exists() else ""
        # compara fara rindul cu data generarii
        strip = lambda s: "\n".join(l for l in s.splitlines() if not l.startswith("Generat "))
        if strip(old) != strip(md):
            print(f"CHECK: registrul HCC de pe disc este vechi ({summary})")
            return 1
        print(f"CHECK: registrul HCC este la zi ({summary})")
        return 0
    if args.dry_run:
        print(summary)
        return 0
    out.mkdir(parents=True, exist_ok=True)
    (out / REGISTER_MD).write_text(md, encoding="utf-8", newline="\n")
    (out / REGISTER_JSON).write_text(js, encoding="utf-8", newline="\n")
    print(f"scris {out / REGISTER_MD}: {summary}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
