"""Find the latest consolidated CELEX for each EUR-Lex extract we hold.

A consolidated CELEX carries the consolidation date in the id itself
(02007L0036-20240109), so a stored id pins the file to one version and never
moves. Requesting the family without a date (CELEX:02007L0036) returns 404, so
that is not a way to reach the current one.

The base act's own EUR-Lex page, however, lists every consolidated version of
it. One request per act is enough: read the ids off that page and take the
latest by date.

Being older than two years does NOT by itself mean a file is behind: an act that
has not been amended since 2017 has no newer consolidation, and the version we
hold is the current one. This script reports the difference between the two.

Reads only.

Usage: python discover_latest_celex.py [--json out.json]
"""

import glob
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, str(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    "..", "anchoring")))
from lib_anchor import split_frontmatter

RAW = "raw/papers/cnpf"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120 Safari/537.36")
CONS = re.compile(r"CELEX[:%]3?A?(0\d{4}[LR]\d{4}-\d{8})")


def field(text, key):
    m = re.search(r"^%s:\s*'?([^'\n]+)'?" % key, text, re.M)
    return m.group(1).strip() if m else None


def latest_for(base_celex):
    url = ("https://eur-lex.europa.eu/legal-content/RO/TXT/?uri=CELEX:%s"
           % base_celex)
    r = subprocess.run(["curl", "-sL", "--max-time", "120", "-A", UA, url],
                       capture_output=True)
    if r.returncode != 0:
        return None, [], "curl failed rc=%d" % r.returncode
    html = r.stdout.decode("utf-8", "replace")
    if len(html) < 5000:
        return None, [], "short response (%d bytes)" % len(html)
    found = sorted(set(CONS.findall(html)))
    same = [c for c in found if c.startswith(base_celex[1:6] + base_celex[6:10])
            or c[1:] .startswith(base_celex[1:])]
    # keep only ids of this very act
    stem = base_celex[1:]
    same = [c for c in found if c.startswith("0" + stem)]
    if not same:
        return None, found, "no consolidated version listed"
    return max(same), same, None


def main():
    rows = []
    for p in sorted(glob.glob(os.path.join(RAW, "UE-*.md"))):
        fm, _ = split_frontmatter(open(p, "rb").read())
        t = fm.decode("utf-8", "replace")
        base = field(t, "base_celex")
        held = field(t, "celex")
        cdate = field(t, "consolidation_date")
        if not base:
            continue
        latest, allv, err = latest_for(base)
        newer = bool(latest and latest != held)
        name = os.path.basename(p)[:-3]
        if err:
            print("%-16s %-22s  ERROR: %s" % (name, held, err))
        else:
            print("%-16s held %-22s latest %-22s %s  [%d versions]"
                  % (name, held, latest,
                     "NEWER AVAILABLE" if newer else "already current",
                     len(allv)))
        rows.append({"stem": name, "path": p.replace(os.sep, "/"),
                     "base_celex": base, "held": held, "held_date": cdate,
                     "latest": latest, "versions": allv, "newer": newer,
                     "error": err})
    print()
    n = sum(1 for r in rows if r["newer"])
    print("%d of %d EU extracts have a newer consolidation available"
          % (n, len(rows)))
    if "--json" in sys.argv:
        out = sys.argv[sys.argv.index("--json") + 1]
        open(out, "w", encoding="utf-8").write(
            json.dumps(rows, indent=2, ensure_ascii=False))
        print("wrote %s" % out)


if __name__ == "__main__":
    main()
