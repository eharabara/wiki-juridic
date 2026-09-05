"""Find the current legis.md doc_id for an act we already hold at an older one.

legis.md gives every consolidation of an act its own doc_id, so a stored doc_id
pins the file to the version that was current when it was ingested and never
moves. The site's own search page is a JavaScript shell and `getResults` only
wraps `showdetails`, so neither reveals a newer version.

The version list is, however, already inside the `showdetails` page itself --
`showversions()` in the site's JS only shows and hides it client-side. Each
entry looks like:

    <li class="tab ultima versions classyear2026">
      <a href="#" onClick="showDetails(null, '155856')">13-08-2026</a></li>

so one fetch per act is enough: read the list, take the entry marked `ultima`,
and that is the current consolidation. No searching and no probing of id ranges.

Reads only. Writes nothing except the report it prints.

Usage: python discover_current_doc_ids.py [--json out.json]
"""

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(r"C:\Users\harab\wiki")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120 Safari/537.36")
VERSION = re.compile(
    r'<li class="tab\s+(?P<flag>\S*)\s*versions\s+classyear(?P<year>\d{4})">'
    r'\s*<a[^>]*onClick="showDetails\(null,\s*\'(?P<id>\d+)\'\)"[^>]*>\s*'
    r'(?P<date>\d{2}-\d{2}-\d{4})', re.S)


def fetch(doc_id):
    url = "https://www.legis.md/cautare/showdetails/%s" % doc_id
    r = subprocess.run(["curl", "-sL", "--max-time", "120", "-A", UA, url],
                       capture_output=True)
    if r.returncode != 0:
        return None, "curl failed rc=%d" % r.returncode
    html = r.stdout.decode("utf-8", "replace")
    if "Just a moment" in html[:2000]:
        return None, "blocked by bot protection"
    if 'id="contentdoc"' not in html:
        return None, "no contentdoc in response (%d bytes)" % len(html)
    return html, None


def versions(html):
    out = []
    for m in VERSION.finditer(html):
        d = m.group("date")
        iso = "%s-%s-%s" % (d[6:], d[3:5], d[0:2])
        out.append({"doc_id": m.group("id"), "date": iso,
                    "latest": "ultima" in m.group("flag")})
    return out


def main():
    targets = json.loads((ROOT / "_meta" / "imports" / "cnpf" /
                          "stale-targets.json").read_text(encoding="utf-8"))
    results = []
    for t in targets:
        html, err = fetch(t["doc_id"])
        if err:
            print("%-14s FETCH FAILED: %s" % (t["stem"], err))
            results.append(dict(t, error=err))
            continue
        vs = versions(html)
        latest = next((v for v in vs if v["latest"]), None)
        if latest is None and vs:
            latest = max(vs, key=lambda v: v["date"])
        cur = latest["doc_id"] if latest else t["doc_id"]
        newer = cur != t["doc_id"]
        print("%-14s held %s (%s)  ->  current %s (%s)  %s   [%d versions]"
              % (t["stem"], t["doc_id"], t["held"], cur,
                 latest["date"] if latest else "?",
                 "NEWER" if newer else "already current", len(vs)))
        results.append(dict(t, current_doc_id=cur,
                            current_date=latest["date"] if latest else None,
                            newer=newer, versions=len(vs)))
    if "--json" in sys.argv:
        p = sys.argv[sys.argv.index("--json") + 1]
        Path(p).write_text(json.dumps(results, indent=2, ensure_ascii=False),
                           encoding="utf-8")
        print("\nwrote %s" % p)


if __name__ == "__main__":
    main()
