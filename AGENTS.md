# Working instructions for this folder

`CLAUDE.md` is the single canonical operating document for this LLM Wiki. Read
it in full before undertaking work in this repository. In particular, it
defines the source hierarchy, citation discipline, current corpus state, open
questions requiring Eugen's judgement, generated controls, and the session
closure procedure.

Do not duplicate volatile project state here. The coverage inventory and its
mechanical flags exist only in the generated block in `CLAUDE.md`; regenerate
that block with `python _meta/coverage/build_coverage.py` rather than copying
its contents into another document. `SCHEMA.md` remains the mechanical
specification and is authoritative for file conventions.

The following guardrails are repeated here because they apply before any other
repository action:

1. Treat text under `raw/` as immutable. Do not refresh, download, overwrite,
   correct, harmonise, or reflow it without Eugen's explicit authority and the
   evidence procedure in `CLAUDE.md`.
2. Before a legal conclusion, open and read the cited raw provision. Check both
   `_meta/inforce/in-force-register.md` and `_meta/hcc/hcc-register.md` where
   applicable. An anchor alone does not establish that the text binds today.
3. If `legal-career/06-matter-log.md` was not taken today, obtain the current
   register from Eugen's project and re-stamp it before altering legal analysis
   or position pages. Do not locally reconstruct or re-argue its positions.
4. Preserve unrelated working-tree changes. Run the relevant generated controls
   and `python _meta/schema/validate_wiki.py --all` before asserting that a
   change is valid. Warnings are findings, not permission to relax a rule.
