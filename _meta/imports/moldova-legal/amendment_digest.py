#!/usr/bin/env python3
"""Rezumat mecanic al modificarilor LP227/LP317/LP140 asupra actelor tinta (2026-09-26).

Pentru fiecare act tinta din perimetrul actelor permisive: articolul/articolele legilor modificatoare care il
vizeaza, punctele lor, si o proba de sincronizare: textele noi ghilimetate (intre ghilimele romanesti, cel putin 40 de caractere) ale
fiecarui punct se cauta, normalizate, in textul detinut al actului (a) in vigoare azi, (b) in versiunile din
`viitor/`. Un text nou care nu apare nicaieri fie a fost rescris de o modificare ulterioara, fie este amanat
si vizibil doar in alta versiune, fie nu s-a aplicat: verdictul il da un om, scriptul numai numara.

Nu citeste actele integral si nu interpreteaza. Scrie `_meta/coverage/amendment-digest.json` si, cu --write-pages,
un bloc marcat in paginile de entitate mecanice.
"""
import glob
import json
import os
import re
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
MD = os.path.join(ROOT, "raw", "papers", "moldova-legal")
AMENDERS = {"LP227": "L-227-2025", "LP317": "L-317-2025", "LP140": "L-140-2025"}
OUT = os.path.join(ROOT, "_meta", "coverage", "amendment-digest.json")
BEGIN, END = "<!-- amendment-digest:begin -->", "<!-- amendment-digest:end -->"


def norm(s):
    s = unicodedata.normalize("NFKD", s.lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.replace(" ", " ")
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def read_body(path):
    t = open(path, encoding="utf-8", errors="replace").read()
    m = re.match(r"---\r?\n.*?\r?\n---\r?\n", t, re.S)
    return t[m.end():] if m else t


def article_block(body, roman):
    m = re.search(r"^## Articolul " + re.escape(roman) + r"\.\s*\n(.*?)(?=^## Articolul |\Z)", body, re.M | re.S)
    return m.group(1) if m else ""


def points(block):
    """Punctele numerotate ale articolului: (numar, prima linie, text complet)."""
    out, cur = [], None
    for line in block.split("\n"):
        m = re.match(r"^(\d+)\.\s+(.*)", line)
        if m and (cur is None or int(m.group(1)) == cur[0] + 1):
            cur = [int(m.group(1)), m.group(2), [line]]
            out.append(cur)
        elif cur is not None:
            cur[2].append(line)
    return [(n, first, "\n".join(txt)) for n, first, txt in out]


OLD_AFTER = re.compile(r"^(?:(?!va\s+avea|se\s+introduce|se\s+introduc)[^.;]){0,120}?se\s+(?:exclud|elimin|abrog|substituie|înlocuie)", re.I | re.S)


def quotes(text):
    """[(text citat, este_text_vechi)]: un text urmat de `se exclude/elimina/abroga/substituie` este textul SCOS."""
    out = []
    for m in re.finditer(r"„([^“”„]{40,}?)”", text):
        out.append((m.group(1), bool(OLD_AFTER.match(text[m.end():m.end() + 110]))))
    return out


def hcc_by_act():
    """act -> {HCCnn/AAAA-LL-ZZ, ...}, din rindurile registrului HCC."""
    p = os.path.join(ROOT, "_meta", "hcc", "hcc-register.md")
    out = {}
    if os.path.exists(p):
        for line in open(p, encoding="utf-8"):
            m = re.match(r"^\| `([^`]+)` \|", line)
            if m:
                for h in re.findall(r"HCC\d+/\d{4}-\d\d-\d\d", line):
                    out.setdefault(m.group(1), set()).add(h)
    return out


HCC_BY_ACT = hcc_by_act()


def main():
    write_pages = "--write-pages" in sys.argv
    amender_body = {k: read_body(os.path.join(MD, v + ".md")) for k, v in AMENDERS.items()}
    result = {}
    for page in sorted(glob.glob(os.path.join(ROOT, "entities", "*.md"))):
        pt = open(page, encoding="utf-8", newline="").read()
        if "Pagină mecanică" not in pt:
            continue
        act = os.path.basename(page)[:-3]
        m = re.search(r"Articolele lor care îl vizează: ([^\n]+)", pt)
        if not m:
            continue
        refs = re.findall(r"(LP\d+) art\.([IVXLC]+)", m.group(1))
        cur_path = None
        for r in ("", "cnpf/"):
            pass
        cur = os.path.join(MD, act + ".md")
        if not os.path.exists(cur):
            cur = os.path.join(ROOT, "raw", "papers", "cnpf", act + ".md")
        cur_txt = norm(read_body(cur))
        fut_files = sorted(glob.glob(os.path.join(MD, "viitor", act + "--*.md")))
        fut_txt = {os.path.basename(f)[len(act) + 2:-3]: norm(read_body(f)) for f in fut_files}
        info = {"refs": [], "points": 0, "quotes": 0, "in_current": 0, "only_future": {}, "absent": 0, "old": 0, "old_gone": 0, "old_present": 0, "old_examples": [], "future_files": list(fut_txt)}
        for lp, roman in refs:
            block = article_block(amender_body[lp], roman)
            pts = points(block)
            ent = {"law": lp, "art": roman, "points": len(pts), "targets": [], "absent_examples": []}
            for n, first, txt in pts:
                ent["targets"].append(f"{n}. {first[:90]}")
                info["points"] += 1
                for q, is_old in quotes(txt):
                    nq = norm(q)
                    if is_old:
                        info["old"] += 1
                        if nq in cur_txt:
                            info["old_present"] += 1
                            if len(info["old_examples"]) < 3:
                                info["old_examples"].append(f"{lp} art. {roman} pct. {n}: {q[:100]}")
                        else:
                            info["old_gone"] += 1
                        continue
                    info["quotes"] += 1
                    w = nq.split()
                    ends = len(w) >= 12 and " ".join(w[:6]) in cur_txt and " ".join(w[-6:]) in cur_txt
                    if nq in cur_txt or ends:
                        info["in_current"] += 1
                    else:
                        hit = [d for d, t in fut_txt.items() if nq in t]
                        if hit:
                            info["only_future"][hit[0]] = info["only_future"].get(hit[0], 0) + 1
                        else:
                            info["absent"] += 1
                            if len(ent["absent_examples"]) < 3:
                                ent["absent_examples"].append(f"pct. {n}: {q[:110]}")
            info["refs"].append(ent)
        result[act] = info
        if write_pages:
            block = [BEGIN, "## Ce modifică legile din perimetru (rezumat mecanic, 2026-09-26)", ""]
            for e in info["refs"]:
                head = f"- **{e['law']} art. {e['art']}**: {e['points']} puncte."
                block.append(head)
                for t in e["targets"][:12]:
                    block.append(f"  - {t}")
                if len(e["targets"]) > 12:
                    block.append(f"  - … încă {len(e['targets']) - 12} puncte")
            block.append("")
            if info["quotes"] or info["old"]:
                fut = "; ".join(f"{n} în versiunea `{d}`" for d, n in info["only_future"].items())
                parts = []
                if info["quotes"]:
                    parts.append(f"din {info['quotes']} texte noi ghilimetate (cel puțin 40 de caractere), {info['in_current']} apar în textul "
                                 f"deținut în vigoare azi" + (f", {fut} numai într-o versiune viitoare" if fut else "")
                                 + f", {info['absent']} nu apar nicăieri")
                if info["old"]:
                    parts.append(f"din {info['old']} texte scoase (`se exclude`, `se abrogă`, `se substituie`), {info['old_gone']} nu mai apar "
                                 f"în textul deținut, {info['old_present']} mai apar (semnal orientativ: același text poate rămîne în alte alineate neatinse de modificare)")
                block.append("- **Proba de sincronizare:** " + "; ".join(parts) + ". Scriptul numără, nu judecă; un text absent poate fi "
                             "rescris de o modificare ulterioară.")
                for e in info["refs"]:
                    for ex in e["absent_examples"]:
                        block.append(f"  - text nou lipsă, {e['law']} art. {e['art']}, {ex}")
            else:
                block.append("- **Proba de sincronizare:** punctele nu conțin texte ghilimetate de cel puțin 40 de caractere "
                             "(abrogări, înlocuiri de cuvinte); nimic de căutat mecanic.")
            if act in HCC_BY_ACT:
                block.append("- **Curtea Constituțională:** hotărîri în registrul HCC pentru acest act: " + ", ".join(sorted(HCC_BY_ACT[act]))
                             + " (`_meta/hcc/hcc-register.md`). Un articol amintit mai sus poate fi unul dintre cele atinse; se verifică registrul "
                             "înainte de a-l cita.")
            block.append(END)
            new = "\n".join(block) + "\n"
            if BEGIN in pt:
                pt = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END) + r"\n?", lambda _m: new, pt, flags=re.S)
            else:
                pt = pt.replace("\n## Semnalări", "\n" + new + "\n## Semnalări", 1) if "\n## Semnalări" in pt else pt + "\n" + new
            open(page, "w", encoding="utf-8", newline="").write(pt)
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(result, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    tot = {k: sum(v[k] for v in result.values()) for k in ("points", "quotes", "in_current", "absent", "old", "old_gone", "old_present")}
    print(f"{len(result)} acte, {tot}")


if __name__ == "__main__":
    main()
