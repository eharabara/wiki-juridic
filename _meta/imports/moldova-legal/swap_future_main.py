#!/usr/bin/env python3
"""Inlocuieste fisierul principal al unui act, care tinea o consolidare cu data VIITOARE, cu versiunea in vigoare azi (2026-09-26).

Cauza: reimprospatarea din 2026-09-04 a luat cea mai noua versiune din lista de pe legis.md, fara sa intrebe daca e in vigoare.
Rezultat: pentru 12 acte textul in vigoare azi nu era in vault (registrul in-force il inlocuia cu o arhiva veche). Aici:
  1. fisierul principal vechi se arhiveaza in `_archive/raw/before-swap-2026-09-26/`;
  2. versiunea in vigoare devine fisierul principal, cu lantul de proveniența (doc_id si sha256 anterioare);
  3. fiecare versiune viitoare (cea tinuta pina acum si cele intermediare) se scrie in `viitor/<act>--<data>.md`.
Foloseste extractorul `ingest_business_law.py`; HTML-urile trebuie sa fie in `legis-md-business/` (sau in cache-ul CNPF/BNM).
"""
import hashlib, importlib.util, io, re, shutil, sys
from pathlib import Path

HERE = Path(__file__).parent
ROOT = HERE.parent.parent.parent
spec = importlib.util.spec_from_file_location("ibl", str(HERE / "ingest_business_law.py"))
ibl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ibl)

ML = ROOT / "raw" / "papers" / "moldova-legal"
FOLDERS = {"ml": ML, "cnpf": ROOT / "raw" / "papers" / "cnpf", "bnm": ROOT / "raw" / "papers" / "bnm" / "legal-ro"}
OTHER_CACHES = [ROOT / "_meta" / "imports" / "cnpf" / "legis-md-consolidated", ROOT / "_meta" / "imports" / "bnm" / "legis-md-ro"]
ARCHIVE = ROOT / "_archive" / "raw" / "before-swap-2026-09-26"
TODAY = "2026-09-26"

# stem: (pastrarea, versiunea in vigoare, [(doc_id, data) versiuni viitoare])
ACTS = {
    "L-1134-1997": ("cnpf", "154797", [("154811", "2028-01-01")]),
    "L-171-2012": ("cnpf", "145907", [("156016", "2027-06-01")]),
    "COD-154-2003": ("ml", "155185", [("155518", "2026-10-28"), ("156323", "2026-12-09"), ("155882", "2027-01-01")]),
    "HG-743-2024": ("ml", "155188", [("155190", "2026-12-30")]),
    "L-132-2016": ("ml", "147882", [("155890", "2027-01-01")]),
    "L-133-2016": ("ml", "152995", [("155891", "2027-01-01")]),
    "L-1543-1998": ("ml", "150224", [("150226", "2027-01-01")]),
    "COD-443-2004": ("ml", "155721", [("156146", "2026-12-02"), ("156325", "2026-12-09"), ("155964", "2027-01-01")]),
    "COD-985-2002": ("ml", "151140", [("156133", "2026-12-02"), ("156270", "2026-12-09")]),
    "L-181-2014": ("ml", "153027", [("153046", "2027-01-01")]),
    "L-845-1992": ("ml", "152587", [("155963", "2027-01-01")]),
    "L-114-2012": ("bnm", "155302", [("155331", "2027-01-01"), ("156446", "2027-03-17")]),
    "COD-122-2003": ("ml", "156018", [("156138", "2026-12-02"), ("156277", "2026-12-09")]),
    "L-72-2025": ("ml", "151457", []),
}


def ensure_cache(doc_id):
    dst = ibl.META_DIR / f"showdetails-{doc_id}.html"
    if dst.exists():
        return
    for c in OTHER_CACHES:
        src = c / f"showdetails-{doc_id}.html"
        if src.exists():
            shutil.copy2(src, dst)
            return
    dl = Path.home() / "Downloads" / f"showdetails-{doc_id}.html"
    if dl.exists():
        shutil.copy2(dl, dst)
        return
    raise SystemExit(f"lipseste HTML-ul {doc_id}")


def build(stem_out, spec_, doc_id):
    ensure_cache(doc_id)
    url, data, path = ibl.fetch(doc_id)
    resolved = ibl.resolve_superscripts(data)
    if not resolved or "<sup" in resolved:
        raise RuntimeError("exponenti nerezolvati " + doc_id)
    parsed = ibl.extract_doc(resolved, anchor_mode=spec_.get("anchor_mode"))
    return ibl.make_raw(stem_out, spec_, parsed, url), parsed


def sha_of_body(text):
    body = text.split("\n---\n", 2)[-1] if text.startswith("---") else text
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def main():
    only = [a for a in sys.argv[1:] if not a.startswith("-")]
    ARCHIVE.mkdir(parents=True, exist_ok=True)
    for stem, (where, cur, futs) in ACTS.items():
        if only and stem not in only:
            continue
        folder = FOLDERS[where]
        old_path = folder / f"{stem}.md"
        old = old_path.read_text(encoding="utf-8", newline="")
        (ARCHIVE / where).mkdir(exist_ok=True)
        shutil.copy2(old_path, ARCHIVE / where / f"{stem}.md")
        fm = lambda k: (re.search(rf"^{k}: '?([^'\n]+)'?", old.split("\n---\n", 1)[0], re.M) or [None, "?"])[1].strip()
        base = dict(ibl.DOCS.get(stem, {}))
        title = base.get("title") or f"act {stem}"
        spec_main = {k: v for k, v in base.items() if k in ("anchor_mode",)}
        spec_main.update(doc_id=cur, title=title)
        text, parsed = build(stem, spec_main, cur)
        chain = (f"refreshed: '{TODAY}'\n"
                 f"refreshed_reason: main file held a future-dated consolidation (see CLAUDE.md, Outstanding work 8); replaced by the version in force today\n"
                 f"doc_id_previous: '{fm('doc_id')}'\n"
                 f"consolidation_date_previous: '{fm('consolidation_date')}'\n"
                 f"sha256_previous: {fm('sha256')}\n"
                 f"ingested_previous: '{fm('ingested')}'\n"
                 f"archived_previous_at: _archive/raw/{ARCHIVE.name}/{where}/{stem}.md\n")
        text = text.replace("---\n", "---\n" + chain, 1)
        cdate = parsed["consolidation_date"]
        if cdate > TODAY:
            print(f"  ATENTIE {stem}: versiunea aleasa ({cur}) are data {cdate}, in viitor")
        old_path.write_text(text, encoding="utf-8", newline="\n")
        print(f"{stem}: principal {cur} @ {cdate}, {parsed['article_count']} articole")
        for fid, fdate in futs:
            vname = f"{stem}--{fdate}"
            vspec = {"doc_id": fid, "subdir": "viitor", "future_of": stem, "applies_from": fdate,
                     "title": f"Versiune viitoare, de la {fdate}, a actului {stem}"}
            if "anchor_mode" in spec_main:
                vspec["anchor_mode"] = spec_main["anchor_mode"]
            vtext, vparsed = build(vname, vspec, fid)
            (ML / "viitor").mkdir(exist_ok=True)
            (ML / "viitor" / f"{vname}.md").write_text(vtext, encoding="utf-8", newline="\n")
            note = "" if vparsed["consolidation_date"] == fdate else f"  ATENTIE: lista {fdate} vs corp {vparsed['consolidation_date']}"
            print(f"   viitor {vname}: {vparsed['article_count']} articole{note}")


if __name__ == "__main__":
    main()
