#!/usr/bin/env python3
"""Stamp or re-stamp the copies in legal-career/ (decision D9).

A copy's body is everything after the frontmatter. The stamp records where it came from, when
it was taken, and the sha256 of the body (CRLF normalised to LF). The validator recomputes the
hash; a mismatch means the copy was edited locally instead of being re-copied from the project.

Run:  python _meta/schema/stamp_copies.py                 re-stamp every copy whose body changed,
                                                          keeping `taken` unless --taken is given
      python _meta/schema/stamp_copies.py --taken 2026-09-12 legal-career/06-matter-log.md
                                                          after replacing the body with the project's text
"""

import datetime as dt
import hashlib
import os
import re
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SPEC_PATH = os.path.join(ROOT, "_meta", "schema", "schema-spec.yaml")
FM_END = re.compile(rb"\n---\r?\n")


def split(data):
    if not data.startswith(b"---"):
        return None, data
    m = FM_END.search(data, 3)
    return (yaml.safe_load(data[3:m.start()].decode("utf-8")) or {}), data[m.end():]


def main():
    args = sys.argv[1:]
    taken = None
    if "--taken" in args:
        i = args.index("--taken")
        taken = args[i + 1]
        del args[i:i + 2]
    with open(SPEC_PATH, encoding="utf-8") as fh:
        spec = yaml.safe_load(fh)["copies"]
    folder = os.path.join(ROOT, spec["folder"])
    files = [os.path.join(ROOT, a) for a in args] or sorted(
        os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(".md"))
    today = dt.date.today().isoformat()
    for p in files:
        data = open(p, "rb").read()
        fm, body = split(data)
        if fm is None:
            sys.stderr.write(f"{p}: no stamp yet; add the frontmatter by hand once, then rerun\n")
            continue
        h = hashlib.sha256(body.replace(b"\r\n", b"\n")).hexdigest()
        changed = h != fm.get("sha256_body") or (taken and taken != str(fm.get("taken")))
        if not changed:
            print(f"{os.path.relpath(p, ROOT)}: unchanged")
            continue
        fm["sha256_body"] = h
        fm["stamped"] = today
        if taken:
            fm["taken"] = taken
        order = spec["required"]
        lines = ["---"]
        for k in order:
            v = fm.get(k)
            if k in ("taken", "stamped"):
                v = f"'{v}'"
            elif k == "master":
                v = f'"{v}"'
            elif isinstance(v, bool):
                v = "true" if v else "false"
            lines.append(f"{k}: {v}")
        lines.append("---")
        open(p, "wb").write(("\n".join(lines) + "\n").encode("utf-8") + body)
        print(f"{os.path.relpath(p, ROOT)}: re-stamped ({h[:12]}, taken {fm['taken']})")


if __name__ == "__main__":
    main()
