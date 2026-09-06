#!/usr/bin/env python3
"""Inchiderea unei sesiuni de lucru in wiki, intr-o singura comanda (2026-09-06).

Ruleaza controalele generate in ordinea corecta, se opreste la prima eroare si, la cerere,
face commit si push. Ordinea conteaza: blocul de acoperire din CLAUDE.md citeste registrul
in-force, deci registrul se reface primul.

    python _meta/close_session.py                     regenereaza registrul, acoperirea si SCHEMA,
                                                      apoi ruleaza validatorul cu raport
    python _meta/close_session.py --check             nu scrie nimic; iese 1 daca ceva e invechit
                                                      sau validatorul gaseste erori (pentru hook si CI)
    python _meta/close_session.py --commit "mesaj"    dupa o rulare curata: git add -A, commit, push
    python _meta/close_session.py --commit "mesaj" --no-push
    python _meta/close_session.py --commit "mesaj" --no-log-entry
                                                      sare peste controlul intrarii de azi din log.md

Ce NU face, dinadins:
  - nu re-stampileaza copiile din legal-career/. Stampila exista ca sa prinda o editare locala;
    un script care o reface automat ar ascunde exact ce trebuie sa prinda. Reimprospatarea unei
    copii ramane manuala: inlocuiesti corpul cu textul din proiect, apoi
    `python _meta/schema/stamp_copies.py --taken YYYY-MM-DD legal-career/NN-....md`.
  - nu scrie in log.md. Decizia D8 cere o intrare cu Aflat / Decis / Unde, adica judecata.
    Scriptul doar refuza sa comita daca lipseste intrarea de azi (se poate sari cu --no-log-entry).
  - nu repara nimic. Ce gaseste validatorul si cere judecata merge la Eugen.

Iesire: 0 = curat, 1 = ceva invechit sau erori, 2 = eroare de rulare (script lipsa, git lipsa).
"""

import datetime as dt
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PY = sys.executable

STEPS = [
    # (nume, script, argumente la regenerare, argumente la --check)
    ("registrul in-force", "_meta/inforce/build_inforce_register.py", [], ["--check"]),
    ("blocul de acoperire din CLAUDE.md", "_meta/coverage/build_coverage.py", [], ["--check"]),
    ("blocul mecanic din SCHEMA.md", "_meta/schema/build_schema.py", [], ["--check"]),
]
VALIDATOR = "_meta/schema/validate_wiki.py"


def run(args, cwd=ROOT):
    """Ruleaza o comanda si intoarce (cod, text). Iesirea e UTF-8 pe orice masina."""
    env = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONUTF8="1")
    p = subprocess.run(args, cwd=cwd, capture_output=True, env=env)
    out = (p.stdout + p.stderr).decode("utf-8", errors="replace")
    return p.returncode, out


def say(line=""):
    print(line, flush=True)


def step(name, script, extra, check):
    path = os.path.join(ROOT, script)
    if not os.path.exists(path):
        say(f"  [!] lipseste {script}")
        return 2
    code, out = run([PY, "-X", "utf8", path] + extra)
    last = [l for l in out.strip().splitlines() if l.strip()]
    tail = last[-1] if last else "(fara iesire)"
    if check:
        mark = "ok" if code == 0 else "INVECHIT"
        say(f"  {name}: {mark}  ({tail})")
        return 0 if code == 0 else 1
    if code != 0:
        say(f"  {name}: EROARE la regenerare")
        say("    " + "\n    ".join(last[-8:]))
        return 2
    say(f"  {name}: regenerat  ({tail})")
    return 0


def validate(check, no_hash):
    args = [PY, "-X", "utf8", os.path.join(ROOT, VALIDATOR)]
    if not check:
        args.append("--report")
    if no_hash:
        args.append("--no-hash")
    code, out = run(args)
    m = re.search(r"Erori: \*\*(\d+)\*\*\. Avertismente: \*\*(\d+)\*\*", out)
    errors, warns = (int(m.group(1)), int(m.group(2))) if m else (None, None)
    say(f"  validator: {'ok' if code == 0 else 'ERORI'}  (erori {errors}, avertismente {warns})")
    # Avertismentele care cer o actiune manuala se arata pe scurt, nu se ascund.
    for line in out.splitlines():
        if line.startswith("- ") and ("copy.stale" in out) and "legal-career/" in line:
            say(f"    {line.strip()}")
    if code != 0:
        say("    Erorile, cu exemple, sunt in raportul validatorului"
            + (" (_meta/lint/validate-YYYY-MM-DD.md)." if not check else " (ruleaza fara --check)."))
    return 0 if code == 0 else 1


def git(*args):
    code, out = run(["git"] + list(args))
    return code, out.strip()


def commit_and_push(message, push, need_log_entry):
    code, _ = git("--version")
    if code != 0:
        say("  [!] git nu este disponibil")
        return 2
    code, status = git("status", "--porcelain")
    if not status:
        say("  git: nimic de comis, arborele de lucru e curat")
        return 0
    today = dt.date.today().isoformat()
    if need_log_entry:
        with open(os.path.join(ROOT, "log.md"), encoding="utf-8") as fh:
            if f"## [{today}]" not in fh.read():
                say(f"  [!] log.md nu are o intrare pentru {today}. Decizia D8 cere una per actiune:")
                say("      Aflat / Decis / Unde. Scrie-o, sau treci --no-log-entry daca chiar nu e cazul.")
                return 1
    say(f"  git: {len(status.splitlines())} fisier(e) de comis")
    git("add", "-A")
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".txt", delete=False) as fh:
        fh.write(message.rstrip("\n") + "\n")
        tmp = fh.name
    try:
        code, out = git("-c", "i18n.commitEncoding=utf-8", "commit", "-q", "-F", tmp)
    finally:
        os.unlink(tmp)
    if code != 0:
        say("  git commit a esuat:\n    " + out.replace("\n", "\n    "))
        return 2
    _, head = git("log", "--oneline", "-1")
    say(f"  commit: {head}")
    if not push:
        say("  push: sarit (--no-push)")
        return 0
    code, out = git("push", "origin", "HEAD")
    if code != 0:
        say("  git push a esuat:\n    " + out.replace("\n", "\n    "))
        return 2
    _, local = git("rev-parse", "HEAD")
    _, remote = git("rev-parse", "@{upstream}")
    say(f"  push: {'ok, origin identic cu HEAD' if local == remote else 'facut, dar upstream difera: verifica'}")
    return 0


def main():
    argv = sys.argv[1:]
    check = "--check" in argv
    no_hash = "--no-hash" in argv
    push = "--no-push" not in argv
    need_log = "--no-log-entry" not in argv
    message = None
    if "--commit" in argv:
        i = argv.index("--commit")
        if i + 1 >= len(argv) or argv[i + 1].startswith("--"):
            say("--commit cere un mesaj: --commit \"ce s-a facut\"")
            return 2
        message = argv[i + 1]
    if check and message:
        say("--check nu scrie nimic, deci nu se combina cu --commit")
        return 2

    say(f"Inchiderea sesiunii, {dt.datetime.now():%Y-%m-%d %H:%M}, {'doar verificare' if check else 'regenerare'}")
    say("Controale generate:")
    worst = 0
    for name, script, extra, check_args in STEPS:
        rc = step(name, script, check_args if check else extra, check)
        worst = max(worst, rc)
        if rc == 2:
            say("Oprit: un control nu a putut rula.")
            return 2
    say("Validator:")
    worst = max(worst, validate(check, no_hash))

    if worst != 0:
        say("Rezultat: NU e curat." + (" Ruleaza fara --check ca sa regenerezi, apoi citeste raportul." if check else
                                     " Vezi raportul validatorului; ce cere judecata merge la Eugen."))
        return 1
    say("Rezultat: curat.")
    if message is None:
        return 0
    say("Commit:")
    return commit_and_push(message, push, need_log)


if __name__ == "__main__":
    sys.exit(main())
