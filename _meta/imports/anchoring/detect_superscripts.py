"""Job 3 -- find flattened superscript article numbers across the raw corpus.

Detection is positional (see lib_superscript). This script then tries to CONFIRM
each candidate against the body text, where the original usually survives as
'Art.146^1' or in an amendment note like '[Art.1461 introdus prin LP...]'.

Candidates that cannot be confirmed are reported as such, never silently fixed.

Usage: python detect_superscripts.py [root ...]
"""

import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_anchor import split_frontmatter, split_lines_keep
import lib_superscript

# An article anchor already present in the file. The label is captured whole so
# that forms which are NOT flattened superscripts can be excluded from the
# sequence rather than corrupting it:
#   * '4a', '7e'   -- lettered EU sub-articles, correct as drafted
#   * '13^1'       -- already normalised by an earlier pass
HEAD = re.compile(r"^(#{1,6})\s+Articolul\s+(\d+(?:\^\d+)?[a-z]?)\b(.*)$")
PLAIN = re.compile(r"^\d+$")


def confirm(body_text, prefix, suffix, flattened):
    """Look for corroboration of 'prefix^suffix' in the body.

    STRONG evidence preserves the superscript in some form, so it independently
    proves the reading. A plain cross-reference to the flattened number is only
    WEAK: the same extraction flattened it too, so it proves the number is used
    consistently, not that it is a superscript.
    """
    strong, weak = [], []
    strong_pats = [
        (r"Art\.\s*%s\s*\^\s*%s\b" % (prefix, suffix), "caret form Art.%s^%s"),
        (r"art\.\s*%s\s*\^\s*%s\b" % (prefix, suffix), "caret form art.%s^%s"),
        (r"Articolul\s+%s\s*\^\s*%s\b" % (prefix, suffix),
         "caret form Articolul %s^%s"),
        (r"%s[¹²³]" % prefix, "unicode superscript"),
        (r"\[\s*Art\.\s*%d\b[^\]]*\]" % flattened, "amendment note [Art.%d ...]"),
    ]
    weak_pats = [
        (r"\bart\.\s*%d\b" % flattened, "cross-reference to art.%d"),
    ]
    for pats, bucket in ((strong_pats, strong), (weak_pats, weak)):
        for pat, label in pats:
            m = re.search(pat, body_text)
            if m:
                s = max(0, m.start() - 70)
                bucket.append((label, re.sub(r"\s+", " ",
                                             body_text[s:m.end() + 70]).strip()))
    return strong, weak


def scan(path):
    data = open(path, "rb").read()
    try:
        fm, body = split_frontmatter(data)
    except ValueError:
        return None
    lines = [t.decode("utf-8", "replace") for t, _ in split_lines_keep(body)]
    heads = [(i, HEAD.match(l)) for i, l in enumerate(lines) if HEAD.match(l)]
    # keep only plain numeric labels; lettered and already-normalised anchors
    # are correct as they stand and would otherwise look like anomalies
    heads = [(i, m) for i, m in heads if PLAIN.match(m.group(2))]
    if len(heads) < 3:
        return None
    nums = [int(m.group(2)) for _, m in heads]
    cands = lib_superscript.detect(nums)
    if not cands:
        return None
    body_text = body.decode("utf-8", "replace")
    out = []
    for c in cands:
        li, m = heads[c["index"]]
        strong, weak = confirm(body_text, c["prefix"], c["suffix"], c["number"])
        out.append({
            "line": li,
            "heading": lines[li],
            "cand": c,
            "strong": strong,
            "weak": weak,
        })
    return {"path": path, "total_articles": len(nums),
            "range": (min(nums), max(nums)), "cands": out}


def main():
    roots = sys.argv[1:] or ["raw/papers"]
    found = []
    for root in roots:
        for p in sorted(glob.glob(os.path.join(root, "**", "*.md"),
                                  recursive=True)):
            r = scan(p)
            if r:
                found.append(r)

    if not found:
        print("no flattened-superscript candidates found")
        return
    for r in found:
        print("=" * 96)
        print("%s   (%d anchors, numbering %d-%d)"
              % (r["path"].replace(os.sep, "/"), r["total_articles"],
                 r["range"][0], r["range"][1]))
        print("=" * 96)
        for c in r["cands"]:
            k = c["cand"]
            print("  line %-6d %s" % (c["line"], c["heading"][:110]))
            if k["confidence"] == "unresolved":
                print("     UNRESOLVED anomaly between art. %s and art. %s"
                      % (k["before"], k["after"]))
                print()
                continue
            print("     positional: run of %d between art. %s and art. %s "
                  "-> %s  => %s"
                  % (k["run_len"], k["before"], k["after"], k["normalised"],
                     k["confidence"]))
            print("     act ceiling excluding candidates: art. %d  "
                  "(so art. %d cannot be a genuine article number); "
                  "base art. %d %s"
                  % (k["ceiling"], k["number"], k["prefix"],
                     "present" if k["base_present"] else "ABSENT"))
            for label, ctx in c["strong"]:
                lab = (label % (k["prefix"], k["suffix"]) if "%s" in label
                       else (label % k["number"] if "%d" in label else label))
                print("     STRONG evidence: %s" % lab)
                print("        ...%s..." % ctx[:150])
            for label, ctx in c["weak"]:
                lab = label % k["number"] if "%d" in label else label
                print("     weak evidence  : %s" % lab)
                print("        (the same extraction flattened this reference "
                      "too, so it shows consistent usage, not superscript-ness)")
                print("        ...%s..." % ctx[:130])
            if not c["strong"]:
                print("     NO STRONG EVIDENCE -- positional reasoning only")
            print()


if __name__ == "__main__":
    main()
