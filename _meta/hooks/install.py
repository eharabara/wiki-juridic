#!/usr/bin/env python3
"""Porneste sau opreste bariera la commit (2026-09-06).

    python _meta/hooks/install.py              git foloseste hook-urile din _meta/hooks
    python _meta/hooks/install.py --uninstall  inapoi la .git/hooks (fara bariera)
    python _meta/hooks/install.py --status     arata ce e setat acum

De ce un instalator: git nu trimite hook-urile pe GitHub (.git/hooks nu e versionat), dar
`core.hooksPath` poate arata spre un folder din depozit, care este versionat. Setarea e locala
clonei, deci se face o data pe fiecare masina. Testul din instalator ruleaza hook-ul o data,
ca sa se vada pe loc daca merge.
"""

import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HOOKS = "_meta/hooks"


def git(*args):
    p = subprocess.run(["git"] + list(args), cwd=ROOT, capture_output=True)
    return p.returncode, (p.stdout + p.stderr).decode("utf-8", errors="replace").strip()


def find_sh():
    """sh de pe PATH sau, pe Windows, cel livrat cu Git (usr/bin/sh.exe), pe care git il foloseste
    la hook-uri chiar daca nu e in PATH."""
    import shutil
    found = shutil.which("sh")
    if found:
        return found
    code, exec_path = git("--exec-path")
    if code == 0 and exec_path:
        # <Git>/mingw64/libexec/git-core -> <Git>/usr/bin/sh.exe
        base = os.path.dirname(os.path.dirname(os.path.dirname(exec_path)))
        cand = os.path.join(base, "usr", "bin", "sh.exe")
        if os.path.exists(cand):
            return cand
    return None


def status():
    code, cur = git("config", "--get", "core.hooksPath")
    if code != 0 or not cur:
        print("bariera: OPRITA (core.hooksPath nesetat; git foloseste .git/hooks)")
        return False
    print(f"bariera: {'PORNITA' if cur.replace(os.sep, '/') == HOOKS else 'ALT FOLDER: ' + cur}")
    return cur.replace(os.sep, "/") == HOOKS


def main():
    args = sys.argv[1:]
    if "--status" in args:
        return 0 if status() else 1
    if "--uninstall" in args:
        git("config", "--unset", "core.hooksPath")
        status()
        return 0
    hook = os.path.join(ROOT, "_meta", "hooks", "pre-commit")
    if not os.path.exists(hook):
        print(f"lipseste {hook}")
        return 2
    with open(hook, "rb") as fh:
        if b"\r\n" in fh.read():
            print("pre-commit are terminatii CRLF; sh nu il poate rula. Vezi .gitattributes.")
            return 2
    code, out = git("config", "core.hooksPath", HOOKS)
    if code != 0:
        print(out)
        return 2
    status()
    print("test: rulez hook-ul o data (nimic scris, fara commit)...")
    sh = find_sh()
    if not sh:
        print("test: nu gasesc sh (pe Windows vine cu Git, in usr/bin). Git il va gasi singur la commit;")
        print("      testul se poate face cu un commit oarecare.")
        return 0
    p = subprocess.run([sh, hook], cwd=ROOT)
    print("test: " + ("hook-ul merge, commit-ul ar fi permis" if p.returncode == 0
                      else f"hook-ul a refuzat (cod {p.returncode}); asa ar refuza si commit-ul"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
