"""Positional detector for flattened superscript article numbers.

Moldovan drafting inserts articles as 146^1, 50^1, 70^1. Extraction flattened the
superscript, so art. 146^1 is stored as "1461". That is worse than a missing
anchor because it does not look missing: a citation to art. 146^1 is unfindable,
and the neighbour of art. 146 reads as article one thousand four hundred sixty-one.

Detection is by POSITION, never by number alone.

The naive test -- "a number that immediately follows an article whose number is
its prefix" -- fails on a RUN of inserted articles, because after the first one
the predecessor is itself a flattened superscript. L-171-2012 contains exactly
that: 881, 882, 883, 884 sitting between art. 79 and art. 89, i.e. arts. 88^1 to
88^4, where the base article 88 does not even appear.

So the detector instead works on runs:

  1. walk the sequence keeping the last number that looks like genuine
     numbering (ascending, and not further ahead than MAX_GAP, which allows for
     repealed articles);
  2. group the consecutive anomalies into a run;
  3. a run is a superscript block if every member is one common prefix P
     followed by suffixes 1, 2, 3, ... in order, and P sits between the last
     genuine number before the run and the first genuine number after it.

Anything anomalous that does not fit that shape is returned as "unresolved" so
it gets reported rather than guessed at.
"""

MAX_GAP = 50


def _prefix_split(n, p):
    s, sp = str(n), str(p)
    if len(s) > len(sp) and s.startswith(sp):
        suf = s[len(sp):]
        if suf.isdigit() and not suf.startswith("0"):
            return suf
    return None


def detect(numbers, max_gap=MAX_GAP):
    """numbers: ordered article numbers as they appear in the act.

    Returns candidates:
      {index, number, prefix, suffix, normalised, run_len, before, after,
       confidence}
    """
    n = len(numbers)
    if n < 3:
        return []

    # 1. classify positions as genuine-looking or anomalous
    #
    # A large jump is the obvious signal (60 -> 601), but it is not enough: a
    # flattened superscript on a low number stays small, so 2^4 arrives as 24
    # and sits well inside any sensible gap threshold. What gives it away is
    # that it overshoots the article that FOLLOWS it -- 2, 24, 3 -- so a number
    # that is not less than its successor is anomalous too.
    # A run of flattened superscripts ascends among itself -- 2, 21, 22, 23, 24,
    # 3 -- so each member looks like ordinary numbering and only the RETURN to
    # art. 3 looks wrong. Marking that return would be exactly backwards, so on
    # hitting a descent the walk backtracks over the block that overshot it and
    # marks the block instead.
    anomalous = [False] * n
    spine = []                      # indices accepted as genuine numbering
    last = None
    for i, v in enumerate(numbers):
        nxt = numbers[i + 1] if i + 1 < n else None
        if last is not None and v <= last:
            while spine and numbers[spine[-1]] >= v:
                anomalous[spine.pop()] = True
            last = numbers[spine[-1]] if spine else None
        ascending = last is None or (v > last and v - last <= max_gap)
        overshoots = (nxt is not None and last is not None
                      and v >= nxt and nxt > last)
        if ascending and not overshoots:
            spine.append(i)
            last = v
        else:
            anomalous[i] = True

    # 2. group consecutive anomalies into runs
    runs = []
    i = 0
    while i < n:
        if anomalous[i]:
            j = i
            while j + 1 < n and anomalous[j + 1]:
                j += 1
            runs.append((i, j))
            i = j + 1
        else:
            i += 1

    out = []
    for lo, hi in runs:
        before = numbers[lo - 1] if lo > 0 else None
        after = numbers[hi + 1] if hi + 1 < n else None
        members = numbers[lo:hi + 1]

        # 3. find the common prefix P that makes the run a 1,2,3,... sequence
        chosen = None
        cands = {before} if before is not None else set()
        # the prefix may be a number that never appears (base article repealed),
        # so also try every prefix of the first member
        s0 = str(members[0])
        for k in range(1, len(s0)):
            cands.add(int(s0[:k]))
        # Longest prefix first. 131 after 13 splits as both 13^1 and 1^31; the
        # first is right, and only ordering decides it. Once the suffix was
        # allowed not to start at 1, the short prefix started winning and
        # 13^1 silently became 1^31.
        for p in sorted((c for c in cands if c is not None), reverse=True):
            sufs = [_prefix_split(v, p) for v in members]
            if any(s is None for s in sufs):
                continue
            # Suffixes must ascend by one, but need NOT start at 1: where the
            # earlier insertions were repealed, an act can carry 11^3 alone, and
            # requiring a run to begin at ^1 silently dropped those.
            ints = [int(s) for s in sufs]
            if ints != list(range(ints[0], ints[0] + len(ints))):
                continue
            # Article numbering ascends, so an inserted article's base cannot
            # come BEFORE the article that precedes it: 88^1 may follow art. 79
            # (base repealed), but nothing following art. 20 is 7^8. Without
            # this, a deliberately sparse extract -- the EU files list only key
            # articles -- reads its own gaps as flattened superscripts.
            if before is not None and p < before:
                continue
            if after is not None and p >= after:
                continue
            chosen = (p, sufs)
            break

        if chosen is None:
            for k, v in enumerate(members):
                out.append({"index": lo + k, "number": v, "prefix": None,
                            "suffix": None, "normalised": None,
                            "run_len": len(members), "before": before,
                            "after": after, "confidence": "unresolved"})
            continue

        p, sufs = chosen
        ceiling = max([v for idx, v in enumerate(numbers) if not anomalous[idx]]
                      or [max(numbers)])
        for k, v in enumerate(members):
            resumes = (after == p + 1) if after is not None else False
            conf = "high" if (v > ceiling and (resumes or len(members) > 1)) \
                else "medium"
            out.append({
                "index": lo + k,
                "number": v,
                "prefix": p,
                "suffix": sufs[k],
                "normalised": "%d^%s" % (p, sufs[k]),
                "run_len": len(members),
                "before": before,
                "after": after,
                "ceiling": ceiling,
                "base_present": p in numbers,
                "confidence": conf,
            })
    return out


def describe(cands):
    if not cands:
        return "   none"
    rows = []
    for c in cands:
        if c["confidence"] == "unresolved":
            rows.append("   art. %-6s -> UNRESOLVED (between %s and %s)"
                        % (c["number"], c["before"], c["after"]))
        else:
            rows.append(
                "   art. %-6s -> %-8s (run of %d, between art. %s and art. %s;"
                " base art. %d %s) => %s"
                % (c["number"], c["normalised"], c["run_len"], c["before"],
                   c["after"], c["prefix"],
                   "present" if c["base_present"] else "ABSENT",
                   c["confidence"]))
    return "\n".join(rows)
