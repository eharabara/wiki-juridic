"""Reimprospatarea celor trei acte gasite "in urma" de sondajul de actualitate din 2026-09-06.

Sondajul (_meta/coverage/currency-sweep-2026-09-06.md) a gasit trei acte cu o consolidare mai
noua CU DATA DEJA TRECUTA, deci textul detinut nu mai este cel in vigoare:

  COD-225-2003    152860 @ 2025-12-30  ->  155718 @ 2026-08-06   (LP330/2025, LP187/2025,
                                                                   LP252/2025, LP126/2026)
  COD-1163-1997   155071 @ 2026-06-25  ->  138613 @ 2026-07-01   (LP318/2025; consolidarea
                                                                   152862 @ 2027-01-01 ramine
                                                                   neingerata)
  L-202-2017      151445 @ 2025-09-20  ->  151077 @ 2025-10-25   (LP189/2025)

Refoloseste refresh_consolidations.py exact ca refresh_stale_batch.py din 4 septembrie: arhiva
versiunii inlocuite in _archive/raw/, lantul de provenienta in frontmatter, delta pe articole,
sha256 recalculat dupa asamblare. Diferenta: HTML-ul nu mai poate veni prin curl (Cloudflare),
deci fetch-ul cade pe cache-ul de pe disc, unde showdetails-<doc_id>.html trebuie pus dinainte,
luat din Chrome (vezi ingest_business_law.fetch). L-202-2017 sta in raw/papers/bnm/legal-ro/,
cu cache-ul in _meta/imports/bnm/legis-md-ro/, deci scriptul-mama e condus o data pe folder.

Usage: python refresh_behind_2026-09-06.py [--apply]
"""
import datetime, importlib.util, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
STAMP = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

BATCHES = {
    "moldova-legal": {
        "raw": ROOT / "raw" / "papers" / "moldova-legal",
        "html": ROOT / "_meta" / "imports" / "moldova-legal" / "legis-md-business",
        "acts": {"COD-225-2003": "155718", "COD-1163-1997": "138613"},
    },
    "bnm-legal-ro": {
        "raw": ROOT / "raw" / "papers" / "bnm" / "legal-ro",
        "html": ROOT / "_meta" / "imports" / "bnm" / "legis-md-ro",
        "acts": {"L-202-2017": "151077"},
    },
}


def load_module():
    spec = importlib.util.spec_from_file_location(
        "refresh_consolidations",
        str(ROOT / "_meta" / "imports" / "cnpf" / "refresh_consolidations.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def existing(path):
    block = path.read_text(encoding="utf-8", errors="replace").split("---", 2)[1]
    out = {}
    for key in ("doc_id", "consolidation_date", "official_title_detected"):
        m = re.search(r"^%s:\s*'?([^'\n]+)'?" % key, block, re.M)
        if m:
            out[key] = m.group(1).strip()
    return out


def main():
    apply_ = "--apply" in sys.argv
    mod = load_module()
    for folder, b in BATCHES.items():
        spec = {}
        for stem, new_id in b["acts"].items():
            cur = existing(b["raw"] / f"{stem}.md")
            spec[stem] = {"old": cur.get("doc_id", "?"), "new": new_id,
                          "title": re.sub(r"\s+", " ", cur.get("official_title_detected", stem))}
        print("=" * 78)
        print(f"folder {folder} -- {len(spec)} acte")
        for s, v in spec.items():
            cache = b["html"] / f"showdetails-{v['new']}.html"
            print(f"   {s:<14} {v['old']} -> {v['new']}   cache: "
                  f"{'prezent' if cache.exists() else 'LIPSA'} ({cache.relative_to(ROOT).as_posix()})")
        if not apply_:
            continue
        mod.TARGETS = spec
        mod.RAW = b["raw"]
        mod.HTML_DIR = b["html"]
        mod.ARCHIVE = ROOT / "_archive" / "raw" / f"{folder}-legis-md-before-refresh-{STAMP}"
        mod.main()
    if not apply_:
        print("\ndry run -- --apply scrie, dupa ce cache-ul e complet")


if __name__ == "__main__":
    main()
