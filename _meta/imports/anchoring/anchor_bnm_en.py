"""Anchor the BNM English-language legal corpus to article level.

These are English translations of Moldovan banking, insurance and payments law.
They hold full text but carried no anchors, so nothing resting on them could be
cited to article level.

What had to be separated before a single anchor could be inserted:

  * genuine headings from cross-references. 'Article 12. Repealed' is a heading;
    'Article 231;' and 'Article 2 of the Law no.179/2016' are wrapped
    cross-references. A period straight after the number splits them.
  * a table of contents. Several documents list every article before the body
    starts; anchoring those rows would duplicate every anchor.
  * flattened superscripts, the same defect as the Romanian corpus but worse
    here, because a run like 2^1..2^4 arrives as 21, 22, 23, 24 and ascends
    among itself. lib_superscript handles that; the Unicode form ('Article 5¹')
    also occurs and is read directly.

Anchors are INSERTED above the source line, exactly as in job 2, so the body
stays byte-identical and stripping '^## Article ' recovers it.

These files are TRANSLATIONS. The anchor makes them findable; it does not make
them the authoritative text. The frontmatter note says so.

Usage: python anchor_bnm_en.py <file.md> <out.md> [--report r.txt]
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_anchor import (split_frontmatter, split_lines_keep, join_lines,
                        detect_sha_convention, body_sha)
import lib_superscript

ANCHOR_DATE = "2026-09-04"
HEAD = re.compile(r"^Article\s+(\d+)([¹²³⁴])?\s*\.\s+\S")
NUM = re.compile(r"^Article\s+(\d+)([¹²³⁴])?")
SUPMAP = {"¹": "1", "²": "2", "³": "3", "⁴": "4"}
DOTS = re.compile(r"\.{5,}")


def headings(lines):
    out = []
    for i, l in enumerate(lines):
        if HEAD.match(l):
            m = NUM.match(l)
            out.append({"line": i, "num": int(m.group(1)),
                        "usup": SUPMAP.get(m.group(2) or "", ""),
                        "dots": bool(DOTS.search(l)), "text": l})
    return out


def split_toc(hs):
    if not hs:
        return [], []
    if sum(1 for h in hs if h["dots"]) >= 5:
        last = max(k for k, h in enumerate(hs) if h["dots"])
        return hs[:last + 1], hs[last + 1:]
    for k in range(1, len(hs)):
        if hs[k]["num"] == 1 and hs[k - 1]["num"] > 5:
            return hs[:k], hs[k:]
    return [], hs


def main():
    src, dst = sys.argv[1], sys.argv[2]
    report = None
    if "--report" in sys.argv:
        report = sys.argv[sys.argv.index("--report") + 1]

    data = open(src, "rb").read()
    fm, body = split_frontmatter(data)
    conv, recorded = detect_sha_convention(data)
    pairs = split_lines_keep(body)
    lines = [t.decode("utf-8", "replace") for t, _ in pairs]
    terms = [t for _, t in pairs]
    nl = b"\r\n" if terms.count(b"\r\n") >= terms.count(b"\n") else b"\n"

    hs = headings(lines)
    toc, bodyh = split_toc(hs)
    nums = [h["num"] for h in bodyh]
    cands = [c for c in lib_superscript.detect(nums)
             if c["confidence"] != "unresolved"]
    supmap = {c["index"]: c["normalised"] for c in cands}

    key = lambda x: (int(x.split("^")[0]),
                     int(x.split("^")[1]) if "^" in x else 0)

    # Anything that would break ascending order is dropped rather than anchored.
    # Two things reach here: a cross-reference that ended a sentence exactly at a
    # line break ('... in Article 70. The 13-month period shall not apply ...'),
    # which is not a heading at all, and a heading the extraction emitted twice.
    # A wrong anchor is worse than a missing one -- it is citable and looks
    # right -- so these are refused and reported.
    #
    # The choice of WHICH to drop matters. Taking them greedily in order keeps
    # whichever came first, so one spurious 'Article 70' early in the run made
    # the watermark 70 and refused the sixteen genuine articles 57 to 69 that
    # followed -- precisely backwards. Keeping the longest strictly ascending
    # subsequence instead discards the isolated intruder and keeps the spine.
    cand = []
    for k, h in enumerate(bodyh):
        lab = ("%d^%s" % (h["num"], h["usup"])) if h["usup"] \
            else supmap.get(k, str(h["num"]))
        cand.append((k, h, lab))

    n = len(cand)
    best = [1] * n
    back = [-1] * n
    for i in range(n):
        for j in range(i):
            if key(cand[j][2]) < key(cand[i][2]) and best[j] + 1 > best[i]:
                best[i] = best[j] + 1
                back[i] = j
    keep = set()
    if n:
        i = max(range(n), key=lambda x: best[x])
        while i != -1:
            keep.add(i)
            i = back[i]

    labels, at, dropped = {}, {}, []
    for idx, (k, h, lab) in enumerate(cand):
        if idx not in keep:
            dropped.append((lab, h["line"], h["text"].strip()[:90]))
            continue
        labels[h["line"]] = lab
        at[k] = lab

    out, inserted = [], 0
    for i, line in enumerate(lines):
        if i in labels:
            out.append(("## Article %s." % labels[i], True))
            inserted += 1
        out.append((line, False))

    new_pairs, oi = [], 0
    for text, ins in out:
        if ins:
            new_pairs.append((text.encode("utf-8"), nl))
        else:
            new_pairs.append(pairs[oi])
            oi += 1
    assert oi == len(pairs)
    new_body = join_lines(new_pairs)

    seq = [at[k] for k in sorted(at)]
    desc = [(seq[k - 1], seq[k]) for k in range(1, len(seq))
            if key(seq[k]) <= key(seq[k - 1])]

    fmt = fm.decode("utf-8")
    new_sha = body_sha(new_body, conv)
    if re.search(r"^sha256:", fmt, re.M):
        fmt = re.sub(r"^sha256: .*$", "sha256_pre_anchoring: %s" % recorded,
                     fmt, count=1, flags=re.M)
    add = ["sha256: %s" % new_sha,
           "sha256_convention: %s" % conv,
           "articles_detected: %d" % inserted,
           "anchoring_date: '%s'" % ANCHOR_DATE]
    if toc:
        add.append("toc_rows_skipped: %d" % len(toc))
    if dropped:
        add.append("anchors_refused: %d  # would break ascending order; see log"
                   % len(dropped))
    if cands:
        add.append("superscript_articles:")
        for c in cands:
            add.append("  - normalised: '%s'" % c["normalised"])
            add.append("    flattened_as: %d" % c["number"])
    add += [
        "anchor_convention: >-",
        "  English translation, anchored 2026-09-04. '## Article N.' inserted",
        "  above the source line; no source line altered. Table-of-contents rows",
        "  and wrapped cross-references are not anchored. Flattened superscripts",
        "  are normalised to '^N'. THIS IS A TRANSLATION: the anchor makes a",
        "  provision findable, it does not make this the authoritative text.",
        "  Cite the Romanian original where one is held.",
    ]
    fnl = "\r\n" if "\r\n" in fmt else "\n"
    fmt = fmt.rstrip("\r\n")
    assert fmt.endswith("---")
    fmt = fmt[:-3].rstrip("\r\n") + fnl + fnl.join(add) + fnl + "---" + fnl
    open(dst, "wb").write(fmt.encode("utf-8") + new_body)

    o = []
    p = o.append
    p("source          : %s" % os.path.basename(src))
    p("anchors inserted: %d" % inserted)
    p("toc rows skipped: %d" % len(toc))
    p("superscripts    : %d flattened normalised, %d already Unicode"
      % (len(cands), sum(1 for h in bodyh if h["usup"])))
    p("sha256          : %s -> %s" % ((recorded or "-")[:16], new_sha[:16]))
    p("non-ascending   : %d %s" % (len(desc), desc[:4]))
    p("refused (would break order): %d" % len(dropped))
    for lab, ln, txt in dropped:
        p("   line %-6d Article %-8s %s" % (ln, lab, txt))
    txt = "\n".join(o)
    print(txt)
    if report:
        open(report, "w", encoding="utf-8").write(txt + "\n")


if __name__ == "__main__":
    main()
