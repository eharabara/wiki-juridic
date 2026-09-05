"""Shared helpers for the raw-layer anchoring work (2026-09-04).

Design rules that follow from the brief:
  * raw/ files are immutable apart from the headings we insert; body lines are
    never rewritten, reflowed or re-encoded.
  * files carry mixed line endings, so everything works on bytes and keeps the
    original terminator of every pre-existing line untouched.
  * two sha256 conventions exist in the corpus (raw bytes vs CRLF->LF
    normalised). Each file is re-hashed under the convention it already uses.
"""

import hashlib
import re

FM_END = re.compile(rb"\n---\r?\n")


def split_frontmatter(data: bytes):
    """Return (frontmatter_bytes, body_bytes). Frontmatter includes its fences."""
    if not data.startswith(b"---"):
        raise ValueError("no frontmatter")
    m = FM_END.search(data, 3)
    if not m:
        raise ValueError("unterminated frontmatter")
    return data[: m.end()], data[m.end():]


def sha_variants(body: bytes):
    return {
        "raw": hashlib.sha256(body).hexdigest(),
        "LF": hashlib.sha256(body.replace(b"\r\n", b"\n")).hexdigest(),
    }


def detect_sha_convention(data: bytes):
    """Which hashing rule reproduces the recorded sha256 for this file?"""
    fm, body = split_frontmatter(data)
    m = re.search(rb"^sha256:\s*(\w+)", fm, re.M)
    if not m:
        return None, None
    recorded = m.group(1).decode()
    for name, digest in sha_variants(body).items():
        if digest == recorded:
            return name, recorded
    return "UNKNOWN", recorded


def body_sha(body: bytes, convention: str) -> str:
    return sha_variants(body)[convention]


def split_lines_keep(body: bytes):
    """Split into (text_without_terminator, terminator) pairs, preserving both."""
    out = []
    start = 0
    n = len(body)
    while start < n:
        nl = body.find(b"\n", start)
        if nl == -1:
            out.append((body[start:], b""))
            break
        line = body[start:nl]
        if line.endswith(b"\r"):
            out.append((line[:-1], b"\r\n"))
        else:
            out.append((line, b"\n"))
        start = nl + 1
    return out


def join_lines(pairs) -> bytes:
    return b"".join(t + term for t, term in pairs)


def strip_added(body: bytes, marker_pred):
    """Remove every line for which marker_pred(text_bytes) is True."""
    return join_lines([(t, term) for t, term in split_lines_keep(body)
                       if not marker_pred(t)])
