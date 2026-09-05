"""Report which sha256 convention each raw legal file uses."""
import glob, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_anchor import detect_sha_convention

if __name__ == "__main__":
    roots = sys.argv[1:] or ["raw/papers/cnpf", "raw/papers/moldova-legal"]
    buckets = {}
    for root in roots:
        for f in sorted(glob.glob(os.path.join(root, "*.md"))):
            data = open(f, "rb").read()
            try:
                conv, rec = detect_sha_convention(data)
            except ValueError as e:
                conv, rec = "no-frontmatter(%s)" % e, None
            buckets.setdefault(conv, []).append(os.path.basename(f))
    for conv, files in sorted(buckets.items(), key=lambda kv: -len(kv[1])):
        print("%-22s %3d" % (conv, len(files)))
        if conv != "LF":
            for f in files:
                print("      ", f)
