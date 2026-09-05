#!/usr/bin/env python3
"""Generate the mechanical part of SCHEMA.md from _meta/schema/schema-spec.yaml.

Same pattern as _meta/coverage/build_coverage.py: whatever a script can state is generated,
never typed. SCHEMA.md keeps its hand-written judgement sections; the block between the
markers named in the spec (`generated_into`) is replaced wholesale. The validator reads the
same spec, so the rules a reader sees are the rules that are enforced.

Run:  python _meta/schema/build_schema.py            (writes SCHEMA.md)
      python _meta/schema/build_schema.py --check    (exit 1 if out of date)
      python _meta/schema/build_schema.py --stdout   (print, write nothing)
"""

import os
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SPEC_PATH = os.path.join(ROOT, "_meta", "schema", "schema-spec.yaml")


def code(s):
    return f"`{s}`"


def lst(xs):
    return ", ".join(code(x) for x in xs)


def render(spec):
    L = []
    a = L.append
    a(f"Generated from `_meta/schema/schema-spec.yaml` (version {spec['version']}). "
      "Every rule below is checked by `python _meta/schema/validate_wiki.py`. "
      "To change a rule, edit the spec, rerun `python _meta/schema/build_schema.py`, then run the validator.")
    a("")

    # layers
    a("### Layers")
    a("")
    a("| Folder | Role | Page types allowed |")
    a("|---|---|---|")
    for folder, types in spec["layers"]["structured"]["folders"].items():
        a(f"| `{folder}/` | structured layer: summaries and analysis, cited as analysis, never as law | {lst(types)} |")
    for r in spec["layers"]["raw"]["roots"]:
        a(f"| `{r['path']}/` | raw source text, immutable, perimeter `{r['perimeter']}` | — |")
    a(f"| `{spec['layers']['archive']}/` | frozen content; not validated; link target only by explicit path | — |")
    a(f"| `{spec['layers']['meta']}/` | scripts, plans, old logs, working files; not validated; never a wikilink target | — |")
    a("")
    raw = spec["layers"]["raw"]
    a(f"Files under a raw root whose name starts with {lst(raw['metadata_prefixes'])} or is one of "
      f"{lst(raw['metadata_names'])} are metadata, not sources, and carry no source frontmatter. "
      f"Names starting with {lst(raw['working_paper_prefixes'])} are working papers extracted from DOCX: "
      "they need source frontmatter but are not normative text: a page may cite them as a working document, never as law.")
    a("")

    # perimeters
    a("### Perimeters")
    a("")
    a(f"Every structured page carries `perimeter:` with one of {lst(spec['perimeters']['values'])}. "
      "A page may cite sources from both perimeters; the field says which citation rule applies to the page, "
      "not where it may read from.")
    if spec["perimeters"]["source_root_required"]:
        a("A page must have at least one source under a raw root of its own perimeter.")
    a("")

    # structured frontmatter
    fs = spec["frontmatter"]["structured"]
    a("### Frontmatter of structured pages")
    a("")
    a("```yaml")
    a("---")
    a("title: Page title")
    a(f"created: {fs['dates']['format']}")
    a(f"updated: {fs['dates']['format']}")
    a(f"type: {' | '.join(fs['enums']['type'])}")
    a(f"perimeter: {' | '.join(fs['enums']['perimeter'])}")
    a("tags: [from the taxonomy below; must include the type tag]")
    a("sources: [raw/papers/<root>/<file>.md, ...]")
    a("# optional")
    a(f"confidence: {' | '.join(fs['enums']['confidence'])}")
    a("contested: true")
    a("contradictions: [other-page-slug]")
    a("imported_from: <original path, for pages carried over from an earlier wiki>")
    a("authority: <free text>")
    a("---")
    a("```")
    a("")
    a(f"- Required: {lst(fs['required'])}. Optional: {lst(fs['optional'])}. Any other key is reported.")
    a(f"- `type` must be allowed in the page's folder (table above).")
    rules = []
    if fs["dates"]["updated_not_before_created"]:
        rules.append("`updated` is not before `created`")
    if fs["dates"]["not_in_future"]:
        rules.append("`updated` is not in the future")
    a(f"- Dates are `{fs['dates']['format']}`; " + "; ".join(rules) + ".")
    a(f"- At least {fs['tags']['min']} tag, all from the taxonomy" +
      (", including the page's own type tag" if fs["tags"]["must_include_type_tag"] else "") + ".")
    a(f"- At least {fs['sources']['min']} source" + ("; every source path must exist" if fs["sources"]["must_exist"] else "") + ".")
    a(f"- At least {fs['min_outbound_wikilinks']} distinct outbound wikilinks in the body, or the tag `needs-links`.")
    a("")

    # raw frontmatter
    fr = spec["frontmatter"]["raw"]
    a("### Frontmatter of raw sources")
    a("")
    a("```yaml")
    a("---")
    a("source_url: https://...")
    a("ingested: YYYY-MM-DD")
    a("sha256: <hex digest of the body after the closing --->")
    a(f"source_type: {' | '.join(fr['enums']['source_type'])}")
    a("publisher: <institution>")
    a(f"language: {' | '.join(fr['enums']['language'])}")
    a(f"# optional, written by the anchoring scripts")
    a(f"{fr['sha256']['declared_field']}: {' | '.join(fr['sha256']['conventions'])}")
    a(f"{fr['sha256']['pre_anchoring_field']}: <hash before structural anchors were added>")
    a("---")
    a("```")
    a("")
    a(f"- Required: {lst(fr['required'])}. Ingest scripts add their own keys (doc_id, consolidation_date, "
      "instrument_id, …); those are not restricted.")
    a(f"- `sha256` is computed over the body, under one of two conventions: {lst(fr['sha256']['conventions'])} "
      "(raw bytes, or CRLF normalised to LF). The validator accepts either; if neither reproduces the recorded "
      "digest, the text changed after it was last hashed, which is an error. A declared "
      f"`{fr['sha256']['declared_field']}` must match the convention that reproduces the digest.")
    a(f"- `{fr['sha256']['pre_anchoring_field']}` records the digest before anchors were inserted. It is provenance, "
      "not a check: proving the body survived anchoring is the job of the anchoring verify scripts.")
    tr = fr["translation"]
    a(f"- **Translations (D2).** `source_type: translation` marks a text that is not authoritative. "
      + ("It must carry no `## Articolul` anchors: an anchor on a translation would assert that the text can be cited, "
         "and it cannot. " if tr["anchors_forbidden"] else "")
      + f"A `legal-text` file with {tr['english_marker_min']} or more body lines matching `{tr['english_marker']}` "
      "is reported as an undeclared translation (warning until the English BNM corpus is retired, P9).")
    a("")

    # tags
    a("### Tag taxonomy")
    a("")
    a("Closed list. A new tag is added to the spec before it is used; the validator reports any other tag.")
    a("")
    for group, tags in spec["tags"].items():
        a(f"- **{group.replace('_', ' ')}:** {lst(tags)}")
    a("")

    # wikilinks
    w = spec["wikilinks"]
    a("### Wikilinks")
    a("")
    a("Base names are ambiguous in this vault: `entities/L-171-2012.md`, `raw/papers/cnpf/L-171-2012.md` and "
      "several archived copies share a name. So resolution is fixed, not left to the editor:")
    a("")
    a(f"- A bare `[[name]]` resolves in this order: {lst(w['resolution_order'])}. The first layer that has the name wins. "
      "So `[[L-171-2012]]` is the entity page; the raw text is `[[raw/papers/cnpf/L-171-2012]]`.")
    a(f"- Pages under {lst(w['path_only_targets'])} can only be linked by explicit path, e.g. `[[_archive/emir-2026-07/name|name]]`.")
    a("- Every wikilink in the structured layer, in raw sources and in the root files must resolve.")
    a("- Raw files are immutable, so a raw file may keep a bare link to a page that has since been archived only "
      "if the redirect is declared in the spec and in the archive's `_PROVENANCE.md`:")
    for ex in w["raw_to_archive_exceptions"]:
        a(f"  - `{ex['file']}` → {lst(ex['targets'])} (declared in `{ex['declared_in']}`)")
    a("")

    # index
    ix = spec["index"]
    a(f"### `{ix['file']}`")
    a("")
    sections = ", ".join(f"`{h}` ({p})" for p, h in ix["perimeter_sections"].items())
    a(f"- Two perimeter sections: {sections}; inside each, type sections "
      + ", ".join(f"`{h}`" for h in dict.fromkeys(ix["type_sections"].values())) + ".")
    a("- Every structured page is listed exactly once, under its perimeter and type, as `- [[name]] — one-line summary`. "
      "Nothing is listed without a file.")
    a(f"- The header line `{ix['total_line']}N` must equal the number of structured pages.")
    a("")

    # log
    lg = spec["log"]
    a(f"### `{lg['file']}`")
    a("")
    a("Git records what changed; the log records what was learned and what was decided (D8). "
      "One entry per action:")
    a("")
    a("```markdown")
    a("## [YYYY-MM-DD] action | subject")
    a("")
    for f in lg["entry_fields"]:
        a(f"- {f} …")
    a("```")
    a("")
    a("- `action` is one of `create`, `update`, `ingest`, `archive`, `delete`, `lint`, `query`, `decision`.")
    a(f"- The three fields appear in this order in every entry. Older logs live in `{lg['archive_dir']}/` and are not written to.")
    a("")

    # hygiene
    hy = spec["hygiene"]
    a("### Hygiene")
    a("")
    chars = ", ".join(f"U+{ord(c):04X}" for c in hy["forbidden_name_chars"])
    a(f"- No file or folder name may contain {chars}: these are the MSYS substitutes for `:` and `\\`, and a name "
      "carrying them is a Windows path that a script wrote as a name under a POSIX shell.")
    a(f"- Empty folders under {lst(hy['no_empty_dirs_under'])} are reported as leftovers.")
    a(f"- `python {hy['coverage_check'][0]} {hy['coverage_check'][1]}` must report the CLAUDE.md coverage block as up to date.")
    a("")
    a("### Running the validator")
    a("")
    a("```bash")
    a("python _meta/schema/validate_wiki.py --report")
    a("```")
    a("")
    a("Exit code 1 on any error. Warnings do not block. Findings are shown, not repaired: anything that needs "
      "judgement goes to Eugen. Run it at the end of every session that touched the vault, after "
      "`build_coverage.py`.")
    return "\n".join(L).rstrip() + "\n"


def main():
    with open(SPEC_PATH, encoding="utf-8") as fh:
        spec = yaml.safe_load(fh)
    block = render(spec)
    target = os.path.join(ROOT, spec["generated_into"]["file"])
    begin, end = spec["generated_into"]["begin"], spec["generated_into"]["end"]
    if "--stdout" in sys.argv:
        sys.stdout.reconfigure(encoding="utf-8")
        print(block)
        return
    with open(target, encoding="utf-8") as fh:
        text = fh.read()
    if begin not in text or end not in text:
        sys.stderr.write(f"markers not found in {target}; add {begin} and {end}\n")
        sys.exit(2)
    pre, rest = text.split(begin, 1)
    _, post = rest.split(end, 1)
    new = pre + begin + "\n\n" + block + "\n" + end + post
    if "--check" in sys.argv:
        if new != text:
            print("out of date")
            sys.exit(1)
        print("up to date")
        return
    if new != text:
        with open(target, "w", encoding="utf-8", newline="") as fh:
            fh.write(new)
        print(f"wrote {os.path.relpath(target, ROOT)}")
    else:
        print("unchanged")


if __name__ == "__main__":
    main()
