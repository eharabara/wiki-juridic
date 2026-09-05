"""Job 2 -- anchor pre-2000 drafting style: 'Art.N. - <provision>' at line start.

L-192-1998 (and any file the sweep turns up) uses the pre-2000 form
'Art.1. - ' instead of 'Articolul 1.', so the ingest regex matched nothing and
the file records "articole detectate: 0" while holding full text.

Method, per the brief: insert '## Articolul N.' ABOVE the provision line and
keep the original 'Art.N. -' token at the start of the body line, so the
extracted text is not altered, only preceded by an anchor.

Because these files already carry wiki-preamble headings ('# raw/...',
'## Capitolul I'), the strip-and-compare marker is the narrower
'^## Articolul ', which no pre-existing line uses.

Usage: python anchor_artdash.py <src.md> <dst.md> [--report r.txt] [--dry-run]
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_anchor import (split_frontmatter, split_lines_keep, join_lines,
                        detect_sha_convention, body_sha)
import lib_superscript

ANCHOR_DATE = "2026-09-04"

# 'Art.13. - ' and 'Art. 20. - ' both occur; the separator is an en dash.
# Amending laws number their own articles in Roman: 'Art. I. - ' ... 'Art. VIII. - '.
# A superscript article may already be resolved at source as 'Art. 8^1. - ': the
# legis.md ingest maps <sup> to ^N, so the caret arrives in the text. An earlier
# version of this pattern stopped at the digits and silently skipped those lines
# -- three articles of L-192-1998 (8^1, 8^2, 13^1) were dropped that way.
ARTDASH = re.compile(r"^Art\.\s*(\d+\^\d+|\d+|[IVXLC]+)\s*\.\s*[–—-]\s")
ADDED = re.compile(r"^## Articolul ")


def build(lines, superscripts):
    """superscripts: {flattened_number: 'P^S'}, applied to Arabic numbers only"""
    out = []
    inserted = 0
    for line in lines:
        m = ARTDASH.match(line)
        if m:
            tok = m.group(1)
            if tok.isdigit():
                label = superscripts.get(int(tok), tok)
            else:
                # Roman numeral, or a caret superscript already resolved at
                # source; either way it is kept exactly as drafted
                label = tok
            out.append(("## Articolul %s." % label, True))
            inserted += 1
        out.append((line, False))
    return out, inserted


def main():
    src, dst = sys.argv[1], sys.argv[2]
    report_path = None
    if "--report" in sys.argv:
        report_path = sys.argv[sys.argv.index("--report") + 1]

    data = open(src, "rb").read()
    fm, body = split_frontmatter(data)
    conv, recorded = detect_sha_convention(data)
    pairs = split_lines_keep(body)
    lines = [t.decode("utf-8") for t, _ in pairs]
    terms = [t for _, t in pairs]
    body_term = b"\r\n" if terms.count(b"\r\n") >= terms.count(b"\n") else b"\n"

    toks = [ARTDASH.match(l).group(1) for l in lines if ARTDASH.match(l)]
    nums = [int(t) for t in toks if t.isdigit()]
    # a caret token is a superscript already resolved at source: it needs no
    # positional detection and must not be mistaken for a Roman numeral
    caret = [t for t in toks if "^" in t]
    roman = [t for t in toks if not t.isdigit() and "^" not in t]
    cands = lib_superscript.detect(nums)
    superscripts = {c["number"]: c["normalised"] for c in cands}

    out, inserted = build(lines, superscripts)

    new_pairs = []
    oi = 0
    for text, ins in out:
        if ins:
            new_pairs.append((text.encode("utf-8"), body_term))
        else:
            new_pairs.append(pairs[oi])
            oi += 1
    assert oi == len(pairs), "line accounting mismatch"
    new_body = join_lines(new_pairs)

    fm_text = fm.decode("utf-8")
    new_sha = body_sha(new_body, conv)
    fm_text = re.sub(r"^sha256: .*$", "sha256_pre_anchoring: %s" % recorded,
                     fm_text, count=1, flags=re.M)
    add = [
        "sha256: %s" % new_sha,
        "sha256_convention: %s" % conv,
        "articole detectate: %d" % inserted,
        "anchoring_date: '%s'" % ANCHOR_DATE,
    ]
    if superscripts:
        add.append("superscript_articles:")
        for c in cands:
            add.append("  - normalised: '%s'" % c["normalised"])
            add.append("    flattened_as: %d" % c["number"])
            add.append("    evidence: positional -- follows art. %d, numbering "
                       "resumes at art. %d, number outside the act's range; "
                       "no 'Art.%s^%s' or amendment note in the body to confirm "
                       "against" % (c["prefix"], c["resumes_at"], c["prefix"],
                                    c["suffix"]))
    form = ("'Art. <Roman>. -' (an amending act numbering its own articles)"
            if roman and not nums else
            "'Art.N. -' (pre-2000 drafting) and 'Art. <Roman>. -'"
            if roman else "'Art.N. -' (pre-2000 drafting)")
    add += [
        "anchor_convention: >-",
        "  Source form %s anchored by" % form,
        "  INSERTING '## Articolul N.' above the provision line; the original",
        "  'Art.' token and the whole body line are unchanged. These acts carry",
        "  no article titles -- the provision runs straight on from the dash --",
        "  so the anchor is the number alone. Roman numerals are kept as drafted.",
        "  Strip every line matching '^## Articolul ' to recover the",
        "  pre-anchoring body byte-for-byte.",
    ]
    # the closing fence may be '---\n' or '---\r\n' depending on the file
    fm_nl = "\r\n" if fm_text.rstrip().endswith("---") and "\r\n" in fm_text \
        else "\n"
    fm_text = fm_text.rstrip("\r\n")
    assert fm_text.endswith("---"), repr(fm_text[-20:])
    fm_text = (fm_text[:-3].rstrip("\r\n") + fm_nl
               + fm_nl.join(add) + fm_nl + "---" + fm_nl)

    if "--dry-run" not in sys.argv:
        open(dst, "wb").write(fm_text.encode("utf-8") + new_body)

    o = []
    p = o.append
    p("source            : %s" % src)
    p("output            : %s" % dst)
    p("sha256 convention : %s" % conv)
    p("sha256 pre        : %s" % recorded)
    p("sha256 post       : %s" % new_sha)
    p("anchors inserted  : %d" % inserted)
    if nums:
        p("arabic numbers    : %s" % nums)
        gaps = [(nums[i - 1], nums[i]) for i in range(1, len(nums))
                if nums[i] > nums[i - 1] + 1 and nums[i] not in superscripts]
        p("numbering gaps    : %s" % gaps)
    if caret:
        p("source-resolved superscripts: %s" % ", ".join(caret))
    if roman:
        p("roman numbers     : %s" % ", ".join(roman))
    p("")
    p("flattened superscript candidates:")
    p(lib_superscript.describe(cands))
    txt = "\n".join(o)
    print(txt)
    if report_path:
        open(report_path, "w", encoding="utf-8").write(txt + "\n")


if __name__ == "__main__":
    main()
