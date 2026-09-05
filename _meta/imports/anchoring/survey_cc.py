"""Job 1 survey: verify the stated facts about CC-1107-2002 before anchoring."""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_anchor import split_frontmatter, split_lines_keep

SRC = "raw/papers/moldova-legal/CC-1107-2002.md"

ART = re.compile(r"^Articolul\s+(\d+)")
MARKERS = ["Cartea", "Titlul", "Capitolul", "Sec\u0163iunea", "Sec\u021biunea",
           "Subsec\u0163iunea", "Subsec\u021biunea"]


def main():
    data = open(SRC, "rb").read()
    fm, body = split_frontmatter(data)
    pairs = split_lines_keep(body)
    lines = [t.decode("utf-8") for t, _ in pairs]
    print("body lines: %d" % len(lines))

    arts = []           # (line_idx, number, full line)
    for i, l in enumerate(lines):
        m = ART.match(l)
        if m:
            arts.append((i, int(m.group(1)), l))
    print("lines starting 'Articolul N': %d" % len(arts))

    nums = [n for _, n, _ in arts]
    print("min %d  max %d  distinct %d" % (min(nums), max(nums), len(set(nums))))

    from collections import Counter
    dup = {n: c for n, c in Counter(nums).items() if c > 1}
    print("duplicate numbers: %s" % (dup if dup else "none"))

    missing = sorted(set(range(min(nums), max(nums) + 1)) - set(nums))
    print("absent numbers (%d): %s" % (len(missing), missing))

    # strict ascendancy -- a break is the signature of a flattened superscript
    breaks = [(arts[i - 1][1], arts[i][1], arts[i][0])
              for i in range(1, len(arts)) if arts[i][1] <= arts[i - 1][1]]
    print("non-ascending steps: %d %s" % (len(breaks), breaks[:20]))

    # structural markers at line start
    print("-- structural markers at line start --")
    for mk in MARKERS:
        c = sum(1 for l in lines if l.startswith(mk))
        if c:
            print("   %-16s %d" % (mk, c))

    # any heading already present?
    print("existing markdown headings: %d"
          % sum(1 for l in lines if l.startswith("#")))

    # 'Articolul' appearing NOT at line start, for awareness only
    inline = sum(l.count("Articolul") for l in lines) - len(
        [l for l in lines if l.startswith("Articolul")])
    print("inline (non-line-initial) 'Articolul' mentions: %d" % inline)

    # line-initial 'Art.' forms (job 2 pattern) inside CC
    artdot = [l for l in lines if re.match(r"^Art\.\s*\d+", l)]
    print("line-initial 'Art.N' forms: %d" % len(artdot))


if __name__ == "__main__":
    main()
