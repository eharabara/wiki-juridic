"""Refresh the remaining stale Moldovan consolidations.

Reuses the machinery of refresh_consolidations.py rather than reimplementing it:
that script already archives the version it replaces, carries the provenance
chain forward, resolves superscripts at source, computes an article-level delta,
warns loudly when legis.md serves a consolidation dated in the future, and
recomputes sha256 after the file is fully assembled. All of that is exactly what
is needed here, so it is imported and driven with a different target list.

Targets come from discover_current_doc_ids.py, which reads the version list that
every showdetails page already carries. Two acts on the stale list are NOT here:

  L-178-2020    legis.md lists no other version; what we hold is the only one.
  HG-1171-2018  the latest version available is dated 2024-07-05, which is the
                date we already hold. We hold a different doc_id record of the
                same consolidation, so a refresh would change the id and nothing
                else.

The files live in two folders, and the imported script targets one, so it is
driven once per folder.

Usage: python refresh_stale_batch.py [--apply]
"""

import datetime
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(r"C:\Users\harab\wiki")
STAMP = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

BATCHES = {
    "cnpf": {
        "L-1-2018": "152650",
        "L-106-2022": "151082",
        "L-1134-1997": "154811",
        "L-122-2008": "138262",
        "L-139-2007": "151001",
        "L-181-2023": "155126",
        "L-192-1998": "150996",
        "L-198-2020": "151070",
        "L-2-2020": "151078",
        "L-234-2016": "145901",
    },
    "moldova-legal": {
        "HG-1170-2016": "144537",
        "L-100-2017": "153007",
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
    text = path.read_text(encoding="utf-8", errors="replace")
    block = text.split("---", 2)[1]
    out = {}
    for key in ("doc_id", "consolidation_date", "official_title_detected"):
        m = re.search(r"^%s:\s*'?([^'\n]+)'?" % key, block, re.M)
        if m:
            out[key] = m.group(1).strip()
    return out


def main():
    apply_ = "--apply" in sys.argv
    mod = load_module()
    for folder, targets in BATCHES.items():
        raw = ROOT / "raw" / "papers" / folder
        html = (ROOT / "_meta" / "imports" / "cnpf" / "legis-md-consolidated"
                if folder == "cnpf" else
                ROOT / "_meta" / "imports" / "moldova-legal" / "legis-md-business")
        spec = {}
        for stem, new_id in targets.items():
            cur = existing(raw / ("%s.md" % stem))
            spec[stem] = {"old": cur.get("doc_id", "?"), "new": new_id,
                          "title": cur.get("official_title_detected", stem)}
        print("=" * 78)
        print("folder %s -- %d acts" % (folder, len(spec)))
        for s, v in spec.items():
            print("   %-14s %s -> %s" % (s, v["old"], v["new"]))
        if not apply_:
            continue
        mod.TARGETS = spec
        mod.RAW = raw
        mod.HTML_DIR = html
        mod.ARCHIVE = (ROOT / "_archive" / "raw" /
                       ("%s-legis-md-before-refresh-%s" % (folder, STAMP)))
        mod.main()

    if not apply_:
        print("\ndry run -- pass --apply to fetch and write")


if __name__ == "__main__":
    main()
