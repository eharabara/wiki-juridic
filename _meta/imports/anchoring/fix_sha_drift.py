"""Repair a stale `sha256` in a raw file's frontmatter.

Drift means the recorded hash no longer matches the body. That is either a bad
body or a stale hash, and the two need opposite responses, so this script
refuses to guess: it recomputes only, and it will not run unless the caller has
already satisfied themselves that the BODY is correct.

Safety:
  * the body is never touched -- only the `sha256:` value changes;
  * `--expect <sha256-of-whole-file>` makes the write conditional on the file
    being exactly what the caller inspected, so a concurrent writer cannot have
    its work silently overwritten;
  * the old value is printed for the audit trail before being replaced.

Usage:
  python fix_sha_drift.py <file.md> [--expect <sha256 of whole file>] [--apply]

Without --apply it reports what it would do and changes nothing.
"""

import hashlib
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_anchor import split_frontmatter, sha_variants


def main():
    path = sys.argv[1]
    expect = None
    if "--expect" in sys.argv:
        # strip: a value piped through a shell loop can pick up a stray CR
        expect = sys.argv[sys.argv.index("--expect") + 1].strip().lower()
    apply_ = "--apply" in sys.argv

    data = open(path, "rb").read()
    whole = hashlib.sha256(data).hexdigest()
    if expect and whole != expect:
        print("REFUSED %s" % path)
        print("   the file changed since it was inspected")
        print("   expected %s" % expect)
        print("   found    %s" % whole)
        return 2

    fm, body = split_frontmatter(data)
    m = re.search(rb"^sha256:\s*(\w+)", fm, re.M)
    if not m:
        print("SKIP %s -- no sha256 field" % path)
        return 1
    recorded = m.group(1).decode()
    variants = sha_variants(body)

    matching = [k for k, v in variants.items() if v == recorded]
    if matching:
        print("OK %s -- already consistent (%s)" % (path, matching[0]))
        return 0

    # both conventions coincide when the body has no CRLF, which is the case
    # for the legis.md ingests; otherwise keep the corpus default
    convention = "LF" if body.count(b"\r\n") == 0 else "LF"
    correct = variants[convention]

    print("%s %s" % ("FIX" if apply_ else "WOULD FIX", path))
    print("   body bytes   : %d (CRLF %d)" % (len(body), body.count(b"\r\n")))
    print("   recorded     : %s   <- stale, matches no convention" % recorded)
    print("   recomputed   : %s   (%s)" % (correct, convention))

    if not apply_:
        return 0

    new_fm = re.sub(rb"^sha256:\s*\w+", b"sha256: " + correct.encode(), fm,
                    count=1, flags=re.M)
    open(path, "wb").write(new_fm + body)

    # re-read and confirm
    d2 = open(path, "rb").read()
    fm2, body2 = split_frontmatter(d2)
    assert body2 == body, "body changed -- aborting"
    rec2 = re.search(rb"^sha256:\s*(\w+)", fm2, re.M).group(1).decode()
    ok = rec2 == sha_variants(body2)[convention]
    print("   verified     : %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
