#!/usr/bin/env python3
"""Verificatorul wiki-ului. Aplică regulile din _meta/schema/schema-spec.yaml fișierelor.

De ce există. SCHEMA.md descria reguli pe care nimeni nu le verifica, iar CLAUDE.md a fost
scris de mână greșit de trei ori într-o oră. Acest script nu judecă nimic: citește
specificația și spune unde fișierele o contrazic. Ce găsește se arată, nu se repară în
tăcere (secțiunea 6 a planului din 2026-09-05).

Rulare:
    python _meta/schema/validate_wiki.py               raport pe ecran, exit 1 dacă sunt erori
    python _meta/schema/validate_wiki.py --report      scrie și _meta/lint/validate-YYYY-MM-DD.md
    python _meta/schema/validate_wiki.py --all         toate exemplele, nu doar primele 8 pe regulă
    python _meta/schema/validate_wiki.py --no-hash     sare peste verificarea sha256 (mai rapid)

Severități. `error` = contrazice o regulă și blochează (exit 1). `warn` = merită văzut, nu
blochează: lacune cunoscute, decizii încă neluate (D2 până la P9), praguri de calitate.
"""

import datetime as dt
import hashlib
import os
import re
import subprocess
import sys
from collections import defaultdict

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SPEC_PATH = os.path.join(ROOT, "_meta", "schema", "schema-spec.yaml")
WIKILINK = re.compile(r"\[\[([^\]\|#]+)(?:#[^\]\|]*)?(?:\|[^\]]*)?\]\]")
FM_END = re.compile(rb"\n---\r?\n")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def rel(path):
    return os.path.relpath(path, ROOT).replace("\\", "/")


def read_bytes(path):
    with open(path, "rb") as fh:
        return fh.read()


def split_frontmatter(data):
    """(frontmatter_text or None, body_bytes). Frontmatter is returned decoded, without fences."""
    if not data.startswith(b"---"):
        return None, data
    m = FM_END.search(data, 3)
    if not m:
        return None, data
    fm = data[3:m.start()].decode("utf-8", errors="replace").lstrip("\r\n")
    return fm, data[m.end():]


def parse_fm(fm_text):
    try:
        d = yaml.safe_load(fm_text)
    except yaml.YAMLError as e:
        return None, str(e).splitlines()[0]
    if not isinstance(d, dict):
        return None, "frontmatter is not a mapping"
    return d, None


def as_date_str(v):
    if isinstance(v, (dt.date, dt.datetime)):
        return v.strftime("%Y-%m-%d")
    return str(v).strip().strip("'\"") if v is not None else ""


def as_list(v):
    if v is None:
        return []
    if isinstance(v, list):
        return [str(x).strip() for x in v]
    return [x.strip() for x in str(v).strip("[]").split(",") if x.strip()]


class Report:
    def __init__(self):
        self.items = defaultdict(list)   # (severity, rule) -> [message]
        self.counts = {"error": 0, "warn": 0}

    def add(self, severity, rule, msg):
        self.items[(severity, rule)].append(msg)
        self.counts[severity] += 1

    def error(self, rule, msg):
        self.add("error", rule, msg)

    def warn(self, rule, msg):
        self.add("warn", rule, msg)


def walk_md(folder):
    out = []
    for dp, dn, fn in os.walk(os.path.join(ROOT, folder)):
        for f in fn:
            if f.endswith(".md"):
                out.append(os.path.join(dp, f))
    return sorted(out)


def main():
    show_all = "--all" in sys.argv
    do_hash = "--no-hash" not in sys.argv
    write_report = "--report" in sys.argv
    today = dt.date.today()

    with open(SPEC_PATH, encoding="utf-8") as fh:
        spec = yaml.safe_load(fh)
    rep = Report()
    stats = {}

    structured_folders = spec["layers"]["structured"]["folders"]
    raw_roots = spec["layers"]["raw"]["roots"]
    meta_prefixes = tuple(spec["layers"]["raw"]["metadata_prefixes"])
    meta_names = set(spec["layers"]["raw"]["metadata_names"])
    working_prefixes = tuple(spec["layers"]["raw"]["working_paper_prefixes"])
    taxonomy = set()
    for group in spec["tags"].values():
        taxonomy.update(group)

    # ------------------------------------------------------------------ name index for wikilinks
    names = {"structured": {}, "raw": {}, "root": {}}
    for folder in structured_folders:
        for p in walk_md(folder):
            names["structured"].setdefault(os.path.basename(p)[:-3], []).append(rel(p))
    for r in raw_roots:
        for p in walk_md(r["path"]):
            names["raw"].setdefault(os.path.basename(p)[:-3], []).append(rel(p))
    for f in os.listdir(ROOT):
        if f.endswith(".md"):
            names["root"].setdefault(f[:-3], []).append(f)
    all_md = {rel(p) for p in walk_md("")}

    def resolve(target):
        """Return the resolved relative path, or None. Explicit paths resolve as paths."""
        t = target.strip()
        if t.endswith(".md"):
            t = t[:-3]
        if "/" in t:
            cand = t + ".md"
            return cand if cand in all_md else None
        for layer in spec["wikilinks"]["resolution_order"]:
            if t in names[layer]:
                return names[layer][t][0]
        return None

    for base, paths in names["structured"].items():
        if len(paths) > 1:
            rep.error("structured.duplicate-name", f"`{base}` exists twice in the structured layer: {paths}")

    # ------------------------------------------------------------------ structured pages
    fm_rules = spec["frontmatter"]["structured"]
    pages = {}   # rel path -> dict(type, perimeter, ...)
    for folder, allowed_types in structured_folders.items():
        for p in walk_md(folder):
            rp = rel(p)
            if os.path.basename(p).startswith("."):
                continue
            data = read_bytes(p)
            fm_text, body = split_frontmatter(data)
            if fm_text is None:
                rep.error("page.frontmatter-missing", rp)
                continue
            fm, err = parse_fm(fm_text)
            if fm is None:
                rep.error("page.frontmatter-invalid", f"{rp}: {err}")
                continue
            for k in fm_rules["required"]:
                if k not in fm or fm[k] in (None, "", []):
                    rep.error("page.field-missing", f"{rp}: `{k}`")
            known = set(fm_rules["required"]) | set(fm_rules["optional"])
            for k in fm:
                if k not in known:
                    rep.warn("page.field-unknown", f"{rp}: `{k}` is not in the spec")
            for k, allowed in fm_rules["enums"].items():
                if k in fm and str(fm[k]) not in allowed:
                    rep.error("page.enum", f"{rp}: `{k}: {fm[k]}` not in {allowed}")
            ty = str(fm.get("type", ""))
            if ty and ty not in allowed_types:
                rep.error("page.type-folder", f"{rp}: type `{ty}` not allowed in `{folder}/` ({allowed_types})")
            created, updated = as_date_str(fm.get("created")), as_date_str(fm.get("updated"))
            for k, v in (("created", created), ("updated", updated)):
                if v and not DATE_RE.match(v):
                    rep.error("page.date-format", f"{rp}: `{k}: {v}`")
            if DATE_RE.match(created) and DATE_RE.match(updated):
                if fm_rules["dates"]["updated_not_before_created"] and updated < created:
                    rep.error("page.date-order", f"{rp}: updated {updated} before created {created}")
                if fm_rules["dates"]["not_in_future"] and updated > today.isoformat():
                    rep.error("page.date-future", f"{rp}: updated {updated}")
            tags = as_list(fm.get("tags"))
            if len(tags) < fm_rules["tags"]["min"]:
                rep.error("page.tags-min", rp)
            if fm_rules["tags"]["taxonomy_only"]:
                for tg in tags:
                    if tg not in taxonomy:
                        rep.error("page.tag-unknown", f"{rp}: `{tg}`")
            if fm_rules["tags"]["must_include_type_tag"] and ty and ty not in tags:
                rep.warn("page.type-tag", f"{rp}: tags lack `{ty}`")
            sources = as_list(fm.get("sources"))
            if len(sources) < fm_rules["sources"]["min"]:
                rep.error("page.sources-min", rp)
            perim = str(fm.get("perimeter", ""))
            in_root = False
            for s in sources:
                if fm_rules["sources"]["must_exist"] and not os.path.exists(os.path.join(ROOT, s)):
                    rep.error("page.source-missing", f"{rp}: `{s}`")
                for r in raw_roots:
                    if s.startswith(r["path"] + "/") and r["perimeter"] == perim:
                        in_root = True
            if spec["perimeters"]["source_root_required"] and perim and not in_root:
                rep.error("page.perimeter-source", f"{rp}: perimeter `{perim}` but no source under a `{perim}` root")
            body_text = body.decode("utf-8", errors="replace")
            links = [l.strip() for l in WIKILINK.findall(body_text)]
            if len(set(links)) < fm_rules["min_outbound_wikilinks"] and "needs-links" not in tags:
                rep.warn("page.links-min", f"{rp}: {len(set(links))} outbound wikilinks, no `needs-links` tag")
            for l in set(links):
                tgt = resolve(l)
                if tgt is None:
                    rep.error("link.unresolved", f"{rp} -> [[{l}]]")
                elif "/" not in l and tgt.split("/")[0] in spec["wikilinks"]["path_only_targets"]:
                    rep.error("link.path-only", f"{rp} -> [[{l}]] resolves into `{tgt}`; use the explicit path")
            pages[rp] = {"type": ty, "perimeter": perim, "base": os.path.basename(rp)[:-3]}
    stats["structured pages"] = len(pages)

    # ------------------------------------------------------------------ index.md
    idx_spec = spec["index"]
    idx_path = os.path.join(ROOT, idx_spec["file"])
    idx_text = read_bytes(idx_path).decode("utf-8", errors="replace")
    entry_re = re.compile(idx_spec["entry_pattern"], re.M)
    perim_of_heading = {v: k for k, v in idx_spec["perimeter_sections"].items()}
    type_of_heading = defaultdict(list)
    for k, v in idx_spec["type_sections"].items():
        type_of_heading[v].append(k)
    listed = {}
    cur_perim, cur_types = None, None
    for line in idx_text.splitlines():
        s = line.rstrip()
        if s in perim_of_heading:
            cur_perim, cur_types = perim_of_heading[s], None
            continue
        if s in type_of_heading:
            cur_types = type_of_heading[s]
            continue
        m = entry_re.match(s)
        if m:
            base = m.group(1).split("/")[-1]
            listed.setdefault(base, []).append((cur_perim, cur_types))
    for base, occ in listed.items():
        if len(occ) > 1:
            rep.error("index.duplicate", f"`{base}` listed {len(occ)} times")
    bases = {v["base"]: (rp, v) for rp, v in pages.items()}
    for base, (rp, v) in bases.items():
        if base not in listed:
            rep.error("index.missing", f"{rp} not listed in index.md")
            continue
        perim, types = listed[base][0]
        if perim != v["perimeter"]:
            rep.error("index.perimeter", f"`{base}` listed under `{perim}`, page says `{v['perimeter']}`")
        if not types or v["type"] not in types:
            rep.error("index.type-section", f"`{base}` listed under types {types}, page type `{v['type']}`")
    for base in listed:
        if base not in bases:
            rep.error("index.orphan", f"`{base}` listed but no structured page exists")
    m = re.search(re.escape(idx_spec["total_line"]) + r"(\d+)", idx_text)
    if not m:
        rep.error("index.total-line", "no `Total pages: N` line")
    elif int(m.group(1)) != len(pages):
        rep.error("index.total-line", f"says {m.group(1)}, structured layer has {len(pages)}")

    # ------------------------------------------------------------------ raw layer
    raw_rules = spec["frontmatter"]["raw"]
    conv_names = raw_rules["sha256"]["conventions"]
    tr = raw_rules["translation"]
    anchor_re = re.compile(tr["anchor_pattern"], re.M)
    en_re = re.compile(tr["english_marker"], re.M)
    exceptions = {}
    for ex in spec["wikilinks"]["raw_to_archive_exceptions"]:
        exceptions[ex["file"]] = set(ex["targets"])
        if not os.path.exists(os.path.join(ROOT, ex["declared_in"])):
            rep.error("raw.exception-undeclared", f"{ex['file']}: `{ex['declared_in']}` does not exist")
    n_raw, n_hash_ok, conv_count = 0, 0, defaultdict(int)
    for r in raw_roots:
        for p in walk_md(r["path"]):
            rp = rel(p)
            base = os.path.basename(p)
            data = read_bytes(p)
            fm_text, body = split_frontmatter(data)
            body_text = body.decode("utf-8", errors="replace")
            # wikilinks from raw: allowed to structured/raw/root; to archive only if declared
            for l in set(x.strip() for x in WIKILINK.findall(body_text)):
                tgt = resolve(l)
                if tgt is None:
                    # a bare name that lives only in _archive: undeclared or declared redirect?
                    if l in exceptions.get(rp, set()):
                        continue
                    rep.error("raw.link-unresolved", f"{rp} -> [[{l}]]")
                elif tgt.split("/")[0] == spec["layers"]["archive"] and l not in exceptions.get(rp, set()):
                    rep.error("raw.link-to-archive", f"{rp} -> [[{l}]] not declared in the spec")
            if base.startswith(meta_prefixes) or base in meta_names:
                continue
            n_raw += 1
            if fm_text is None:
                rep.error("raw.frontmatter-missing", rp)
                continue
            fm, err = parse_fm(fm_text)
            if fm is None:
                rep.error("raw.frontmatter-invalid", f"{rp}: {err}")
                continue
            for k in raw_rules["required"]:
                if k not in fm or fm[k] in (None, ""):
                    rep.error("raw.field-missing", f"{rp}: `{k}`")
            for k, allowed in raw_rules["enums"].items():
                if k in fm and str(fm[k]) not in allowed:
                    rep.error("raw.enum", f"{rp}: `{k}: {fm[k]}`")
            if str(fm.get("language")) == "other":
                rep.warn("raw.language-other", rp)
            if do_hash and fm.get("sha256"):
                recorded = str(fm["sha256"])
                variants = {"raw": hashlib.sha256(body).hexdigest(),
                            "LF": hashlib.sha256(body.replace(b"\r\n", b"\n")).hexdigest()}
                match = [c for c in conv_names if variants[c] == recorded]
                declared = fm.get(raw_rules["sha256"]["declared_field"])
                if not match:
                    rep.error("raw.sha256-mismatch", f"{rp}: body hash does not reproduce `sha256` under {conv_names}")
                else:
                    n_hash_ok += 1
                    conv_count[match[0]] += 1
                    if declared and str(declared) not in match:
                        rep.error("raw.sha256-convention", f"{rp}: declares `{declared}`, hash matches {match}")
            st = str(fm.get("source_type"))
            n_anchor = len(anchor_re.findall(body_text))
            n_en = len(en_re.findall(body_text))
            if st == "translation" and tr["anchors_forbidden"] and n_anchor:
                rep.error("raw.translation-anchored", f"{rp}: {n_anchor} `## Articolul` anchors on a translation (D2)")
            if st == "legal-text" and n_en >= tr["english_marker_min"] and not base.startswith(working_prefixes):
                rep.warn("raw.translation-undeclared", f"{rp}: {n_en} `Article N` lines, source_type still `legal-text` (D2, pending P9)")
    stats["raw sources checked"] = n_raw
    if do_hash:
        stats["raw sha256 verified"] = f"{n_hash_ok} ({', '.join(f'{k}: {v}' for k, v in sorted(conv_count.items()))})"

    # ------------------------------------------------------------------ root files' wikilinks
    for f in ("CLAUDE.md", "SCHEMA.md", "README.md"):
        fp = os.path.join(ROOT, f)
        if not os.path.exists(fp):
            continue
        text = read_bytes(fp).decode("utf-8", errors="replace")
        # skip fenced code, where [[...]] is quoted as syntax
        text = re.sub(r"```.*?```", "", text, flags=re.S)
        text = re.sub(r"`[^`\n]*`", "", text)
        for l in set(x.strip() for x in WIKILINK.findall(text)):
            if resolve(l) is None:
                rep.error("link.unresolved", f"{f} -> [[{l}]]")

    # ------------------------------------------------------------------ log.md
    log_spec = spec["log"]
    log_text = read_bytes(os.path.join(ROOT, log_spec["file"])).decode("utf-8", errors="replace")
    header_re = re.compile(log_spec["entry_header"], re.M)
    entries = list(header_re.finditer(log_text))
    bad_headers = [l for l in log_text.splitlines() if l.startswith("## ") and not header_re.match(l)]
    for l in bad_headers:
        rep.error("log.header", f"`{l[:80]}`")
    fields = log_spec["entry_fields"]
    for i, m in enumerate(entries):
        chunk = log_text[m.end(): entries[i + 1].start() if i + 1 < len(entries) else len(log_text)]
        pos = [chunk.find(f) for f in fields]
        if any(x < 0 for x in pos):
            rep.error("log.fields", f"entry `{m.group(0)[:70]}` lacks {[f for f, x in zip(fields, pos) if x < 0]}")
        elif pos != sorted(pos):
            rep.error("log.fields-order", f"entry `{m.group(0)[:70]}`")
    stats["log entries"] = len(entries)
    if not os.path.isdir(os.path.join(ROOT, log_spec["archive_dir"])):
        rep.error("log.archive-dir", f"`{log_spec['archive_dir']}` missing")

    # ------------------------------------------------------------------ hygiene
    hy = spec["hygiene"]
    bad_chars = set(hy["forbidden_name_chars"])
    for dp, dn, fn in os.walk(ROOT):
        if "/.git" in dp.replace("\\", "/") or dp.replace("\\", "/").endswith("/.git"):
            dn[:] = []
            continue
        for name in dn + fn:
            if any(c in name for c in bad_chars):
                rep.error("hygiene.stray-name", f"{rel(os.path.join(dp, name))} (Windows path written as a name under a POSIX shell)")
    for folder in hy["no_empty_dirs_under"]:
        top = os.path.join(ROOT, folder)
        if not os.path.isdir(top):
            continue
        for dp, dn, fn in os.walk(top):
            if not dn and not fn:
                rep.warn("hygiene.empty-dir", rel(dp))
    try:
        cmd = [sys.executable] + [os.path.join(ROOT, hy["coverage_check"][0])] + hy["coverage_check"][1:]
        res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, timeout=300)
        if res.returncode != 0:
            rep.error("hygiene.coverage-stale", "CLAUDE.md coverage block is out of date; run build_coverage.py")
    except Exception as e:  # noqa: BLE001
        rep.warn("hygiene.coverage-check", f"could not run coverage check: {e}")

    # ------------------------------------------------------------------ report
    lines = [f"# Validare wiki — {today.isoformat()}", "",
             f"Specificație: `{rel(SPEC_PATH)}` versiunea {spec['version']}. "
             f"Erori: **{rep.counts['error']}**. Avertismente: **{rep.counts['warn']}**.", ""]
    for k, v in stats.items():
        lines.append(f"- {k}: {v}")
    lines.append("")
    for severity in ("error", "warn"):
        keys = sorted(k for k in rep.items if k[0] == severity)
        if not keys:
            continue
        lines.append(f"## {'Erori' if severity == 'error' else 'Avertismente'}")
        lines.append("")
        for key in keys:
            msgs = rep.items[key]
            lines.append(f"### `{key[1]}` — {len(msgs)}")
            lines.append("")
            shown = msgs if show_all else msgs[:8]
            for m in shown:
                lines.append(f"- {m}")
            if len(msgs) > len(shown):
                lines.append(f"- … și încă {len(msgs) - len(shown)} (rulează cu `--all`)")
            lines.append("")
    out = "\n".join(lines)
    sys.stdout.reconfigure(encoding="utf-8")
    print(out)
    if write_report:
        lint_dir = os.path.join(ROOT, "_meta", "lint")
        os.makedirs(lint_dir, exist_ok=True)
        rpath = os.path.join(lint_dir, f"validate-{today.isoformat()}.md")
        with open(rpath, "w", encoding="utf-8") as fh:
            fh.write(out + "\n")
        print(f"\n(report written to {rel(rpath)})")
    sys.exit(1 if rep.counts["error"] else 0)


if __name__ == "__main__":
    main()
