#!/usr/bin/env python3
"""Graful de citare al actelor detinute: un control generat (2026-09-10).

De ce exista. Lanturile de trimitere (L-177-2025 -> L-62-2022 -> L-284-2004 -> L-105-2003) au fost
descoperite de mina, o ingestie pe zi, iar registrele in-force si HCC stau in trei locuri pe care
cititorul trebuie sa-si aminteasca sa le deschida. Textul brut contine deja toate muchiile. Scriptul
le extrage mecanic, fara nicio muchie dedusa, si le scrie intr-un graf pe care un control sau o
persoana il poate parcurge: ce citeaza un articol, cine il citeaza, si daca vreuna dintre dispozitiile
de care depinde nu se aplica astazi.

Ce face. Citeste actele primare din raw/ (cnpf, moldova-legal, bnm/legal-ro, bnm/dcu), le imparte pe
ancorele `## Articolul N`, gaseste in fiecare segment trimiterile la alte acte (Legea nr. N/AAAA, legile pe
nume, codurile pe nume sau pe numar, Constitutia, Hotaririle Guvernului, directivele si regulamentele UE)
si trimiterile la articole (`art. N`, `articolul N`), grupeaza enumerarile (`art. 5, 6 si art. 7 alin. (2)`),
rezolva grupul la actul pe care il indica contextul (`din Legea nr. X`; `Directiva X (art. N ...)`;
`Legea nr. X se modifica dupa cum urmeaza: ... articolul N`; altfel actul curent) si verifica daca ancora
exista. Apoi ataseaza dispozitiilor starea din registrul in-force si din registrul HCC, si titlurilor
"abrogat". Scrie un JSON (graful) si un raport Markdown (coada de ingerare, dispozitiile cu stare speciala
si cine le citeaza, gradul fiecarui act, trimiterile nerezolvate).

Ce NU face, dinadins. Nu deduce nimic: fiecare muchie poarta fisierul si liniile din care a fost citita.
Nu citeste articolele actelor structurate pe puncte (HG, regulamente BNM/CNPF, proceduri DCU): pentru ele
exista doar muchii la nivel de act. Nu citeste extrasele UE pentru muchii, doar le foloseste ca tinte. Nu
citeste corpusul englez BNM (traduceri, neancorate). Nu coboara sub articol. Nu stie daca un act citat si
nedetinut mai este in vigoare. Graful nu se citeaza: el trimite la ancora, si ancora se deschide.

Utilizare:
    python _meta/graph/build_citation_graph.py            scrie citation-graph.json si citation-graph.md
    python _meta/graph/build_citation_graph.py --check    nu scrie; iese 1 daca fisierele de pe disc difera
    python _meta/graph/build_citation_graph.py --dry-run  construieste si raporteaza numerele, nu scrie
"""

from __future__ import annotations

import bisect
import datetime as dt
import json
import os
import re
import sys
import unicodedata
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT_DIR = os.path.join(ROOT, "_meta", "graph")
OUT_JSON = os.path.join(OUT_DIR, "citation-graph.json")
OUT_MD = os.path.join(OUT_DIR, "citation-graph.md")
SELF_PATH = "_meta/graph/build_citation_graph.py"
INFORCE_JSON = os.path.join(ROOT, "_meta", "inforce", "in-force-register.json")
HCC_JSON = os.path.join(ROOT, "_meta", "hcc", "hcc-register.json")

# Radacinile citite pentru muchii. Extrasele UE (UE-*) sint noduri-tinta, nu surse.
ROOTS = ["raw/papers/cnpf", "raw/papers/moldova-legal", "raw/papers/bnm/legal-ro", "raw/papers/bnm/dcu"]
SKIP_PREFIX = ("_", "md-", "README")
EU_PREFIX = "UE-"

MONTHS = ("ianuarie", "februarie", "martie", "aprilie", "mai", "iunie", "iulie", "august",
          "septembrie", "octombrie", "noiembrie", "decembrie")
MONTH_ALT = "|".join(MONTHS)

# Clase de litere, scrise cu coduri ca fisierul sa ramina ASCII.
RO_LOWER = "a-z\u0103\u00e2\u00ee\u0219\u015f\u021b\u0163"
RO_UPPER = "A-Z\u0102\u00c2\u00ce\u0218\u015e\u021a\u0162"
LETTERS = "A-Za-z\u00c0-\u024f"

# Numarul unui articol, asa cum apare in ancore si in trimiteri: 54, 54^1, 54^1/1 (unicul caz N^X/Y
# din vault, Codul fiscal linia 2309; tiparul fara `/` il trunchia la 54^1 si il suprapunea pe art. 54^1).
ARTNUM = r"\d+(?:\^\d+)?(?:/\d+)?"
ANCHOR_RE = re.compile(r"^## Articolul\s+(" + ARTNUM + r"|[IVXLC]+)\.?\s*(.*)$")

# Data unui act: /AAAA, din ZZ luna AAAA, din ZZ.LL.AAAA. Grupurile: (an1, zi2, luna2, an2, zi3, luna3, an3).
DATE_TAIL = (r"\s*(?:/\s*(\d{4})"
             r"|din\s+(\d{1,2})\s+(" + MONTH_ALT + r")\s+(\d{4})"
             r"|din\s+(\d{1,2})\.(\d{1,2})\.(\d{4}))")

LAW_RE = re.compile(r"\bLeg(?:ea|ii|e)\s+(?:Republicii\s+Moldova\s+)?nr\.\s*(\d+)(?:-[IVXLC]+)?" + DATE_TAIL, re.I)
# Legea pe nume, cu sau fara numar dupa nume: "Legea contabilitatii nr. 287/2017", "Legii cu privire la publicitate".
LAWNAME_RE = re.compile(
    r"\bLeg(?:ea|ii)\s+(?!nr\.)(?!Republicii)((?:(?!nr\.)[" + RO_LOWER + r"-]+\s+){0,6}(?!nr\.)[" + RO_LOWER + r"-]+)"
    r"(?:\s+nr\.\s*(\d+)(?:-[IVXLC]+)?" + DATE_TAIL + r")?")
CODE_NUM_RE = re.compile(r"\bCod(?:ul|ului)\b(?:(?!\bLeg|\bHot|\bCod|\bRegul|\bDirect)[^\n;]){0,70}?\bnr\.\s*(\d+)(?:-[IVXLC]+)?" + DATE_TAIL, re.I)
CONST_RE = re.compile(r"\bConstitu[\u021b\u0163t]i(?:a|ei|e)\b")
HG_RE = re.compile(r"\bHot[\u0103a]r[\u00e2\u00eea]r(?:ea|ii|e)\s+Guvernului\s+nr\.\s*(\d+)" + DATE_TAIL, re.I)
EU_DIR_RE = re.compile(r"\bDirectiv(?:a|ei|e|ele|elor)?\s+(?:\((?:UE|CE|CEE)\)\s+)?(\d{2,4})/(\d{1,4})(?:/(UE|CE|CEE))?\b")
EU_REG_RE = re.compile(r"\bRegulament(?:ul|ului|e|ele|elor)?(?:\s+(?:delegat|de\s+punere\s+[\u00een]n\s+aplicare))?"
                       r"\s+\((?:UE|CE|CEE)\)\s+(nr\.\s*)?(\d{1,4})/(\d{2,4})\b")
SELF_RE = re.compile(r"\bprezent(?:a|ei)\s+leg[ie]\b|\bprezent(?:ul|ului)\s+cod\b|\bprezent(?:ul|ului)\s+regulament\b"
                     r"|\bprezent(?:a|ei)\s+hot[\u0103a]r[\u00e2\u00ee]r[ie]\b|\bprezent(?:ul|ului)\s+statut\b"
                     r"|\bprezent(?:a|ei)\s+instruc[\u021b\u0163]iuni?\b|\bprezent(?:ele|elor)\s+reguli\b"
                     r"|\bprezent(?:ele|elor)\s+proceduri\b", re.I)
# "Legea nr. X ... se modifica dupa cum urmeaza:" / "se completeaza cu articolul N" - articolele care urmeaza sint ale legii X.
AMEND_RE = re.compile(r"\bse\s+(?:modific[\u0103a]|completeaz[\u0103a])(?:\s+[\u0219\u015fs]i\s+se\s+completeaz[\u0103a])?"
                      r"\s+dup[\u0103a]\s+cum\s+urmeaz[\u0103a]"
                      r"|\bse\s+completeaz[\u0103a]\s+cu(?=\s+articol)", re.I)
# "din legea indicata", "al aceleiasi legi": trimitere inapoi la ultima lege numita in acelasi segment.
ANAPHORA_RE = re.compile(r"\b(?:din|al|ale|a)\s+(?:(?:legea|legii|codul|codului)\s+(?:indicat[\u0103a]|men[\u021b\u0163t]ionat[\u0103a]"
                         r"|respectiv[\u0103a]|sus-men[\u021b\u0163t]ionat[\u0103a]|enun[\u021b\u0163t]at[\u0103a]|nominalizat[\u0103a]|citat[\u0103a])"
                         r"|aceleia[\u0219\u015fs]i\s+legi|acela[\u0219\u015fs]i\s+cod|aceluia[\u0219\u015fs]i\s+cod)\b", re.I)
TFUE_RE = re.compile(r"\bTratatul(?:ui)?\s+privind\s+func[\u021b\u0163t]ionarea\s+Uniunii\s+Europene\b|\bTFUE\b")
COLON_GAP_RE = re.compile(r"\s*,?\s*(?:respectiv|[\u0219\u015fs]i\s+anume|anume|adic[\u0103a])?\s*:\s*")

ART_RE = re.compile(r"\bart\.\s*(" + ARTNUM + r")")
ARTLONG_RE = re.compile(r"\b[Aa]rticol(?:ul|ului|ele|elor)\s+(" + ARTNUM + r")")
WORD_RE = re.compile(r"[" + LETTERS + r"]+")
SENTENCE_BOUNDARY_RE = re.compile(r"\.\s+[" + RO_UPPER + r"]")
# Cuvintele care pot sta intr-o enumerare de articole fara sa o rupa (fara diacritice, minuscule).
CONNECTOR_WORDS = {"alin", "alineatul", "alineatele", "lit", "litera", "literele", "pct", "punctul", "punctele",
                   "teza", "tezele", "si", "sau", "ori", "precum", "respectiv", "inclusiv", "coroborat", "coroborate",
                   "raportat", "raportate", "cu", "nr", "din", "al", "ale", "a", "la", "prima", "doua",
                   "anexa", "anexele", "anexei", "anexelor", "exceptia", "exceptiile", "exceptand"}
ROMAN_RE = re.compile(r"^[ivxlc]+$")
LINK_WORDS = {"din", "al", "ale", "a"}
GAP_BETWEEN = 300   # intre doua articole ale aceleiasi enumerari
GAP_LINK = 450      # intre ultimul articol al grupului si actul-tinta (listele din Codul de procedura penala)

# Ce se mascheaza inainte de citire: notele de modificare intre paranteze drepte, rindurile blocului de
# istoric (`LP162 din 30.07.26, MO390-393/25.08.26 art.416; in vigoare 01.06.27`) si orice referinta la
# Monitorul Oficial, al carei `art.` este articolul Monitorului, nu al legii. MO apare si cu litere
# chirilice, cu virgula inaintea lui art., cu spatii in jurul barei si cu `din` in loc de bara.
BRACKET_RE = re.compile(r"\[[^\[\]]{0,700}\]", re.S)
HIST_LINE_RE = re.compile(r"^[ \t]*[A-Z\u0410-\u042f]{2,6}\d+(?:/\d+)?\s+din\s+\d{1,2}\.\d{1,2}\.\d{2,4}.*$", re.M)
MO_RE = re.compile(r"\b[M\u041c][O\u041e]F?\s*\d+(?:\s*-\s*\d+)*\s*(?:/|din)\s*\d{1,2}\.\d{1,2}\.\d{2,4}\s*,?\s*art\.\s*\d+", re.I)
MO_LONG_RE = re.compile(r"Monitorul\s+Oficial[^\n;]{0,80}?\bart\.\s*\d+", re.I)
# "Republicata conform LP153/2012, art.620": articolul Monitorului, in fisa actului
LP_ART_RE = re.compile(r"\b(?:LP|HG|HP|LC|HCC)\d+(?:/\d{4}|\s+din\s+\d{1,2}\.\d{1,2}\.\d{2,4}),?\s*art\.\s*\d+")
# Titlurile inserate la ancorare (## Capitolul, ### Sectiunea) si notele structurale "(art. 28-31) - abrogat" nu sint
# trimiteri; in preambul, rindurile "Articolul N. ..." sint cuprinsul, nu textul.
HEADING_LINE_RE = re.compile(r"^#{2,6}\s.*$", re.M)
RANGE_ABROGAT_RE = re.compile(r"\((?:art\.|articolele)\s*" + ARTNUM + r"\s*[-\u2013]\s*" + ARTNUM + r"\)\s*[-\u2013.]?\s*abrogat", re.I)
TOC_LINE_RE = re.compile(r"^[ \t]*Articolul\s+\S.*$", re.M)
ABROGAT_RE = re.compile(r"\b(abrogat|exclus)\b", re.I)

# Codurile pe nume. Cele detinute primesc id-ul fisierului; cele nedetinute devin noduri externe pe nume,
# unite cu forma pe numar atunci cind textul le scrie impreuna ("Codul electoral nr. 325/2022").
CODE_NAMES = [
    (r"Cod(?:ul|ului)\s+civil\b", "CC-1107-2002"),
    (r"Cod(?:ul|ului)\s+fiscal\b", "COD-1163-1997"),
    (r"Cod(?:ul|ului)\s+penal\b", "COD-985-2002"),
    (r"Cod(?:ul|ului)\s+de\s+procedur[\u0103a]\s+penal[\u0103a]\b", "COD-122-2003"),
    (r"Cod(?:ul|ului)\s+de\s+procedur[\u0103a]\s+civil[\u0103a]\b", "COD-225-2003"),
    (r"Cod(?:ul|ului)\s+contraven[\u021b\u0163t]ional\b", "COD-218-2008"),
    (r"Cod(?:ul|ului)\s+administrativ\b", "COD-116-2018"),
    (r"Cod(?:ul|ului)\s+muncii\b", "COD-154-2003"),
    (r"Cod(?:ul|ului)\s+de\s+executare\b", "COD-443-2004"),
    (r"Cod(?:ul|ului)\s+vamal\b", "COD-95-2021"),
    (r"Cod(?:ul|ului)\s+funciar\b", "COD-22-2024"),
    (r"Cod(?:ul|ului)\s+serviciilor\s+media\s+audiovizuale\b", "COD-174-2018"),
    (r"Cod(?:ul|ului)\s+urbanismului(?:\s+[\u0219\u015fs]i\s+construc[\u021b\u0163t]iilor)?\b", "COD-434-2023"),
    (r"Cod(?:ul|ului)\s+electoral\b", "EXT:COD-electoral"),
    (r"Cod(?:ul|ului)\s+educa[\u021b\u0163t]iei\b", "EXT:COD-educatiei"),
    (r"Cod(?:ul|ului)\s+transporturilor\s+rutiere\b", "EXT:COD-transporturilor-rutiere"),
    (r"Cod(?:ul|ului)\s+naviga[\u021b\u0163t]iei\s+maritime\s+comerciale\b", "EXT:COD-navigatiei-maritime-comerciale"),
    (r"Cod(?:ul|ului)\s+familiei\b", "EXT:COD-familiei"),
    (r"Cod(?:ul|ului)\s+jurisdic[\u021b\u0163t]iei\s+constitu[\u021b\u0163t]ionale\b", "EXT:COD-jurisdictiei-constitutionale"),
    (r"Cod(?:ul|ului)\s+silvic\b", "EXT:COD-silvic"),
    (r"Cod(?:ul|ului)\s+subsolului\b", "EXT:COD-subsolului"),
    (r"Cod(?:ul|ului)\s+apelor\b", "EXT:COD-apelor"),
    (r"Cod(?:ul|ului)\s+audiovizualului\b", "EXT:COD-audiovizualului"),
]
CODE_NAME_RES = [(re.compile(p), t) for p, t in CODE_NAMES]
CODE_NUM_ALIAS = {"COD-1107-2002": "CC-1107-2002"}
# Cuvinte cu care nu poate incepe titlul unei legi citate pe nume (dupa "cu privire la"/"privind"/"pentru").
NAME_STOP = {"sau", "si", "ori", "care", "este", "nu", "se", "va", "in", "la", "de", "pe", "a", "al", "ale",
             "aplicabila", "aplicabile", "aplicabil", "speciala", "noua", "veche", "organica", "ordinara",
             "respectiva", "mentionata", "sus-mentionata", "prezenta", "anterioara", "ulterioara"}
NAME_LEAD_RE = re.compile(r"^(?:cu privire la |privind |pentru |a |al |ale )+")


# ---------------------------------------------------------------------------------------------
# Citire
# ---------------------------------------------------------------------------------------------

def read(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def frontmatter(text):
    """Acelasi cititor minimal ca in build_coverage.py: chei simple si liste cu `- `."""
    if not text.startswith("---"):
        return {}, (text, 1)
    end = text.find("\n---", 3)
    if end == -1:
        return {}, (text, 1)
    fm, key = {}, None
    for line in text[3:end].splitlines():
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line)
        if m:
            key = m.group(1)
            fm[key] = m.group(2).strip().strip("'\"")
        elif line.startswith("- ") and key:
            fm.setdefault(key + "__list", []).append(line[2:].strip().strip("'\""))
    body = text[end + 4:]
    if body.startswith("\n"):
        body = body[1:]
    first_body_line = text[:end + 4].count("\n") + 2
    return fm, (body, first_body_line)


def year_from(groups):
    """Din cele 7 grupuri ale DATE_TAIL intoarce anul, sau None."""
    an1, _zi2, _luna2, an2, _zi3, _luna3, an3 = groups
    return an1 or an2 or an3


def strip_diacritics(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


def norm(s):
    return re.sub(r"\s+", " ", strip_diacritics(s).lower()).strip()


def eu_year(y):
    y = int(y)
    return 1900 + y if y < 100 else y


def plausible_year(s):
    return len(s) == 4 and 1950 <= int(s) <= 2100


def words(s):
    return [strip_diacritics(w.lower()) for w in WORD_RE.findall(s)]


# ---------------------------------------------------------------------------------------------
# Actele
# ---------------------------------------------------------------------------------------------

class Act:
    def __init__(self, act_id, rel, fm, body, first_line):
        self.id = act_id
        self.rel = rel
        self.fm = fm
        self.lines = body.split("\n")
        self.first_line = first_line  # linia din fisier a self.lines[0]
        self.anchors = []  # (index in self.lines, article, title)
        for i, line in enumerate(self.lines):
            m = ANCHOR_RE.match(line)
            if m:
                self.anchors.append((i, m.group(1), m.group(2).strip()))
        self.anchor_set = {a for _, a, _ in self.anchors}
        self.title = (fm.get("official_title_detected") or fm.get("title") or act_id).strip().strip("'\"")
        # titlul fara antetul "LEGE Nr. N din ZZ.LL.AAAA", pentru rezolvarea legilor citate pe nume
        t = norm(self.title)
        t = re.sub(r"^(?:lege|cod|hotarare|hotarire|constitutia|decizie|statutul|regulile)\s+nr\.\s*[\d/]+\s+din\s+[\d.]+\s*", "", t)
        self.title_key = NAME_LEAD_RE.sub("", t).strip("* ")

    def file_line(self, idx):
        return self.first_line + idx

    def segments(self):
        """(segment_id, start_idx, end_idx, article|None, heading_title|None)."""
        if not self.anchors:
            yield (self.id + "#corp", 0, len(self.lines), None, None)
            return
        first = self.anchors[0][0]
        if first > 0:
            yield (self.id + "#preambul", 0, first, None, None)
        for k, (i, art, title) in enumerate(self.anchors):
            end = self.anchors[k + 1][0] if k + 1 < len(self.anchors) else len(self.lines)
            yield (self.id + "#art." + art, i, end, art, title)


def load_acts():
    acts, eu = {}, {}
    for root in ROOTS:
        d = os.path.join(ROOT, root)
        if not os.path.isdir(d):
            continue
        for name in sorted(os.listdir(d)):
            if not name.endswith(".md") or name.startswith(SKIP_PREFIX):
                continue
            path = os.path.join(d, name)
            rel = root + "/" + name
            text = read(path)
            fm, (body, first_line) = frontmatter(text)
            act_id = fm.get("instrument_id") or name[:-3]
            if name.startswith(EU_PREFIX):
                eu[name[:-3]] = {"id": name[:-3], "rel": rel, "celex": fm.get("celex", ""),
                                 "title": (fm.get("title") or name[:-3]).strip().strip("'\""),
                                 "consolidation": fm.get("consolidation_date", "")}
                continue
            acts[act_id] = Act(act_id, rel, fm, body, first_line)
    return acts, eu


def eu_index(eu):
    """(tip, an, numar) -> id detinut. Celex 02014R0596-20260605: sector, an, L/R, numar."""
    idx = {}
    for eid, e in sorted(eu.items(), key=lambda kv: (len(kv[0]), kv[0])):
        m = re.match(r"^\d(\d{4})([LR])(\d{4})", e["celex"] or "")
        if not m:
            continue
        idx.setdefault((m.group(2), int(m.group(1)), int(m.group(3))), eid)  # id-ul cel mai scurt cistiga
    return idx


def resolve_law_name(name, acts):
    """Legea citata pe nume -> actul detinut al carui titlu o contine, daca e exact unul. Altfel None."""
    key = NAME_LEAD_RE.sub("", norm(name))
    ws = key.split(" ")
    if not ws or ws[0] in NAME_STOP or len(ws[0]) < 3:
        return None, None
    for k in range(min(6, len(ws)), 1, -1):
        phrase = " ".join(ws[:k])
        hits = [aid for aid, a in acts.items() if phrase in a.title_key]
        if len(hits) == 1:
            return hits[0], phrase
        if len(hits) > 1:
            return None, None
    return None, None


# ---------------------------------------------------------------------------------------------
# Jetoane: trimiteri la acte si la articole
# ---------------------------------------------------------------------------------------------

def mask(text, preamble=False):
    def blank(m):
        return re.sub(r"[^\n]", " ", m.group())
    rxs = [BRACKET_RE, HIST_LINE_RE, MO_RE, MO_LONG_RE, LP_ART_RE, HEADING_LINE_RE, RANGE_ABROGAT_RE]
    if preamble:
        rxs.append(TOC_LINE_RE)
    for rx in rxs:
        text = rx.sub(blank, text)
    return text


def suspects(artnum, anchor_set):
    """Un numar citat fara ancora poate fi un exponent turtit in sursa: 3142 -> 314^2, daca ancora exista."""
    if "^" in artnum or "/" in artnum:
        return []
    out = []
    for i in range(1, len(artnum)):
        base, sup = artnum[:i], artnum[i:]
        if sup.startswith("0"):
            continue
        if f"{base}^{sup}" in anchor_set:
            out.append(f"{base}^{sup}")
    return out


def act_tokens(text, acts, eu_idx, aliases):
    """Lista de (start, end, target_id, label, kind), fara suprapuneri. Invata aliasurile nume->numar ale codurilor."""
    found = []
    for m in LAW_RE.finditer(text):
        y = year_from(m.groups()[1:8])
        tid = f"L-{m.group(1)}-{y}"
        found.append((m.start(), m.end(), tid, f"Legea nr. {m.group(1)}/{y}", "law"))
    for m in LAWNAME_RE.finditer(text):
        if m.group(2):
            y = year_from(m.groups()[2:9])
            tid = f"L-{m.group(2)}-{y}"
            found.append((m.start(), m.end(), tid, f"Legea nr. {m.group(2)}/{y}", "law"))
            continue
        name = re.sub(r"\s+", " ", m.group(1)).strip()
        held, _phrase = resolve_law_name(name, acts)
        if held:
            found.append((m.start(), m.end(), held, "Legea " + name, "law-named"))
            continue
        key = NAME_LEAD_RE.sub("", norm(name))
        ws = key.split(" ")
        if len(ws) < 1 or ws[0] in NAME_STOP or len(ws[0]) < 3:
            continue
        slug = "-".join(ws[:4])
        label = "Legea " + " ".join(name.split(" ")[:6])
        found.append((m.start(), m.end(), "EXT:LEGE:" + slug, label, "law-named"))
    for m in CODE_NUM_RE.finditer(text):
        y = year_from(m.groups()[1:8])
        tid = CODE_NUM_ALIAS.get(f"COD-{m.group(1)}-{y}", f"COD-{m.group(1)}-{y}")
        found.append((m.start(), m.end(), tid, f"Codul nr. {m.group(1)}/{y}", "code"))
    for rx, tid in CODE_NAME_RES:
        for m in rx.finditer(text):
            found.append((m.start(), m.end(), tid, re.sub(r"\s+", " ", m.group()), "code"))
    for m in CONST_RE.finditer(text):
        found.append((m.start(), m.end(), "CONST-1994", "Constitutia", "const"))
    for m in HG_RE.finditer(text):
        y = year_from(m.groups()[1:8])
        found.append((m.start(), m.end(), f"HG-{m.group(1)}-{y}", f"Hotarirea Guvernului nr. {m.group(1)}/{y}", "hg"))
    for m in EU_DIR_RE.finditer(text):
        if int(m.group(1)) < 50 or int(m.group(1)) > 2100:
            continue
        y, n = eu_year(m.group(1)), int(m.group(2))
        tid = eu_idx.get(("L", y, n), f"EXT:EU-L-{y}-{n}")
        found.append((m.start(), m.end(), tid, f"Directiva {y}/{n}", "eu"))
    for m in EU_REG_RE.finditer(text):
        a, b, has_nr = m.group(2), m.group(3), bool(m.group(1))
        if has_nr:  # forma veche: nr. 648/2012
            if plausible_year(b):
                n, y = int(a), int(b)
            elif plausible_year(a):
                y, n = int(a), int(b)
            else:
                continue
        else:  # forma noua: (UE) 2024/1624
            if plausible_year(a):
                y, n = int(a), int(b)
            elif plausible_year(b):
                n, y = int(a), int(b)
            else:
                continue
        tid = eu_idx.get(("R", y, n), f"EXT:EU-R-{y}-{n}")
        label = f"Regulamentul (UE) nr. {n}/{y}" if y < 2015 else f"Regulamentul (UE) {y}/{n}"
        found.append((m.start(), m.end(), tid, label, "eu"))
    for m in TFUE_RE.finditer(text):
        found.append((m.start(), m.end(), "EXT:EU-TFUE", "Tratatul privind functionarea Uniunii Europene", "eu"))
    for m in SELF_RE.finditer(text):
        found.append((m.start(), m.end(), None, m.group(), "self"))
    # fara suprapuneri: cel mai devreme, la egalitate cel mai lung. Un nume de cod inghitit de forma pe numar
    # ("Codul electoral nr. 325/2022") invata aliasul nume -> numar.
    found.sort(key=lambda t: (t[0], -t[1]))
    out, last = [], None
    for t in found:
        if last is not None and t[0] < last[1]:
            if last[4] == "code" and t[4] == "code" and t[2].startswith("EXT:") and not last[2].startswith("EXT:COD-") \
                    and re.match(r"^(?:EXT:)?COD-\d+-\d{4}$", last[2] or ""):
                aliases[t[2]][last[2]] += 1
            continue
        out.append(t)
        last = t
    res = []
    for s, e, tid, label, kind in out:
        if tid is not None and tid not in acts and not tid.startswith("EXT:") and not tid.startswith("UE-"):
            tid = "EXT:" + tid
        res.append((s, e, tid, label, kind))
    # anafora: "din legea indicata" -> ultima lege sau ultimul cod numit inainte, in acelasi segment
    extra = []
    for m in ANAPHORA_RE.finditer(text):
        prev = None
        for t in res:
            if t[1] <= m.start() and t[4] in ("law", "law-named", "code") and t[2] is not None:
                prev = t
            elif t[0] >= m.start():
                break
        if prev is not None and not any(t[0] < m.end() and m.start() < t[1] for t in res):
            extra.append((m.start(), m.end(), prev[2], prev[3] + " (anafora)", "anafora"))
    if extra:
        res = sorted(res + extra, key=lambda t: t[0])
    return res


def art_tokens(text):
    """(start, end, articol). `Articolul N` la inceput de rind este linia originala de sub ancora, nu o trimitere."""
    found = [(m.start(), m.end(), m.group(1)) for m in ART_RE.finditer(text)]
    for m in ARTLONG_RE.finditer(text):
        before = text[:m.start()].rsplit("\n", 1)[-1]
        if before.strip() == "" or before.endswith("## "):
            continue
        found.append((m.start(), m.end(), m.group(1)))
    found.sort()
    return found


def connector_ok(gap, limit=GAP_BETWEEN):
    """Textul dintre doua articole ale aceleiasi enumerari: fara `;`, fara granita de propozitie, numai
    cuvinte de legatura (alin., lit., si, sau, anexa...), litere izolate (lit. a), (h)) si numerale romane."""
    if ";" in gap or len(gap) > limit or SENTENCE_BOUNDARY_RE.search(gap):
        return False
    return all(w in CONNECTOR_WORDS or len(w) == 1 or ROMAN_RE.match(w) for w in words(gap))


def link_ok(gap):
    """Textul dintre ultimul articol al grupului si actul-tinta: conector care se termina in din/al/ale/a
    (`art. 5 din Legea X`) sau care inchide paranteza deschisa inaintea grupului (`(art. 5, 6) Directiva X`)."""
    if not connector_ok(gap, GAP_LINK):
        return False
    ws = words(gap)
    if ws and ws[-1] in LINK_WORDS:
        return True
    return gap.count(")") > gap.count("(")


def group_arts(text, arts):
    """Grupeaza trimiterile consecutive legate prin conectori: [(start, end, [articole...])]."""
    groups = []
    i = 0
    while i < len(arts):
        s, e, nums = arts[i][0], arts[i][1], [arts[i][2]]
        j = i + 1
        while j < len(arts) and connector_ok(text[e:arts[j][0]]):
            e = arts[j][1]
            nums.append(arts[j][2])
            j += 1
        groups.append((s, e, nums))
        i = j
    return groups


def resolve_group(text, g_start, g_end, tokens, amend_positions):
    """Actul la care trimite un grup de articole. Intoarce (index_jeton | None, regula)."""
    # 1. inainte: "art. 56 alin. (1) din Legea nr. 1134/1997"; "(art. 1, 2 si art. 10) Directiva 2008/104/CE"
    for i, t in enumerate(tokens):
        if t[0] < g_end:
            continue
        if t[0] - g_end > GAP_LINK:
            break
        if link_ok(text[g_end:t[0]]):
            return i, "din"
        break
    # 2. inapoi: "Directiva 2014/65/UE (art. 2 alin. (1), art. 3 ...)" - articolele in paranteza dupa act;
    #    "din Codul penal nr. 985/2002: art. 135-145, ..." - articolele dupa doua puncte
    prev = None
    for i, t in enumerate(tokens):
        if t[1] <= g_start and g_start - t[1] <= 400:
            prev = i
        elif t[0] >= g_start:
            break
    if prev is not None:
        gap = text[tokens[prev][1]:g_start]
        if gap.count("(") > gap.count(")") and ";" not in gap:
            return prev, "paranteza"
        if COLON_GAP_RE.fullmatch(gap):
            return prev, "doua-puncte"
    # 3. modificare: "Legea nr. X ... se modifica dupa cum urmeaza: 1. La articolul 3 alineatul (1) ..."
    last_amend = None
    for p in amend_positions:
        if p < g_start:
            last_amend = p
        else:
            break
    if last_amend is not None:
        cand = None
        for i, t in enumerate(tokens):
            if t[1] <= last_amend and t[4] != "self":
                cand = i
            elif t[0] > last_amend:
                break
        if cand is not None:
            return cand, "modificare"
    return None, "intern"


# ---------------------------------------------------------------------------------------------
# Registrele
# ---------------------------------------------------------------------------------------------

def load_json(path):
    if not os.path.exists(path):
        return None
    try:
        return json.loads(read(path))
    except Exception:
        return None


def inforce_flags(reg):
    flags, pending = defaultdict(list), {}
    if not reg:
        return flags, pending
    for p in reg.get("provisions_not_yet_in_force", []):
        flags[(p["instrument"], p["article"])].append({
            "effective_from": p.get("effective_from"), "operation": p.get("operation"),
            "subunit": p.get("subunit") or "", "amending_act": p.get("amending_act")})
    for p in reg.get("pending_consolidations", []):
        pending[p["instrument"]] = {"doc_id": p.get("doc_id"), "consolidation_date": p.get("consolidation_date"),
                                    "amending_act": p.get("amending_act")}
    return flags, pending


def hcc_flags(reg):
    flags, unattributed = defaultdict(list), {}
    if not reg:
        return flags, unattributed
    for a in reg.get("acts", []):
        inst = a["instrument"]
        for m in a.get("markers", []):
            hcc = m.get("hcc")
            hcc = ", ".join(hcc) if isinstance(hcc, list) else hcc
            flags[(inst, str(m.get("article")))].append({"hcc": hcc, "subunit": m.get("subunit") or "",
                                                           "scope": m.get("scope") or "", "source": "marcaj in text"})
        for r in a.get("recovered", []):
            flags[(inst, str(r.get("article")))].append({"hcc": r.get("hcc"), "subunit": r.get("subunit") or "",
                                                           "scope": r.get("scope") or "", "source": "recuperat"})
        if a.get("unattributed"):
            unattributed[inst] = [u.get("hcc") for u in a["unattributed"]]
    return flags, unattributed


# ---------------------------------------------------------------------------------------------
# Construirea grafului
# ---------------------------------------------------------------------------------------------

def build():
    acts, eu = load_acts()
    eu_idx = eu_index(eu)
    inforce = load_json(INFORCE_JSON)
    hcc = load_json(HCC_JSON)
    nif, pending = inforce_flags(inforce)
    hccf, hcc_unattr = hcc_flags(hcc)

    nodes, edges, ext_labels = {}, {}, {}
    aliases = defaultdict(Counter)
    stats = defaultdict(int)

    def edge(source, target, kind, line, evidence, rule=None):
        key = (source, target, kind)
        e = edges.get(key)
        if e is None:
            e = edges[key] = {"source": source, "target": target, "kind": kind, "count": 0,
                              "lines": set(), "evidence": evidence}
            if rule:
                e["rule"] = rule
        e["count"] += 1
        e["lines"].add(line)
        return e

    def snippet(text, s, e):
        a, b = max(0, s - 45), min(len(text), e + 70)
        return re.sub(r"\s+", " ", text[a:b]).strip()

    # nodurile actelor si dispozitiilor
    for aid in sorted(acts):
        act = acts[aid]
        fm = act.fm
        structure = "articole" if act.anchors else (
            "puncte" if re.search(r"\*\*puncte numerotate detectate:\*\*\s*[1-9]", "\n".join(act.lines)) else "fara")
        nodes[aid] = {
            "id": aid, "kind": "act", "title": act.title, "path": act.rel,
            "doc_id": fm.get("doc_id", ""), "consolidation_date": fm.get("consolidation_date", ""),
            "consolidation_is_future": fm.get("consolidation_is_future", "").lower() == "true",
            "structure": structure, "anchors": len(act.anchors),
            "entity_page": os.path.exists(os.path.join(ROOT, "entities", aid + ".md")),
            "pending_consolidation": pending.get(aid),
            "hcc_unattributed": hcc_unattr.get(aid, []),
        }
        for seg_id, s, e, art, title in act.segments():
            if art is None:
                nodes[seg_id] = {"id": seg_id, "kind": "segment", "act": aid,
                                 "line_from": act.file_line(s), "line_to": act.file_line(e - 1)}
                continue
            body_first = " ".join(l.strip() for l in act.lines[s + 1:s + 3])
            abrogat = bool(ABROGAT_RE.search(title)) or bool(re.match(
                r"^\s*(?:Articolul\s+\S+\.?\s*)?[\u2013\u2014-]?\s*(?:abrogat|exclus)", body_first, re.I))
            nodes[seg_id] = {
                "id": seg_id, "kind": "provision", "act": aid, "article": art, "title": title,
                "line": act.file_line(s), "abrogat": abrogat,
                "not_in_force": nif.get((aid, art), []), "hcc": hccf.get((aid, art), []),
            }
    for eid in sorted(eu):
        e = eu[eid]
        nodes[eid] = {"id": eid, "kind": "eu-act", "title": e["title"], "path": e["rel"], "celex": e["celex"],
                      "consolidation_date": e["consolidation"]}

    # muchiile
    for aid in sorted(acts):
        act = acts[aid]
        for seg_id, s, e, art, _title in act.segments():
            seg_lines = act.lines[s:e]
            if art is not None:
                seg_lines = [""] + seg_lines[1:]  # ancora insasi nu se citeste; linia originala de sub ea da
            text = mask("\n".join(seg_lines), preamble=(art is None))
            starts = [0]
            for line in seg_lines[:-1]:
                starts.append(starts[-1] + len(line) + 1)

            def line_of(off):
                return act.file_line(s + bisect.bisect_right(starts, off) - 1)

            toks = act_tokens(text, acts, eu_idx, aliases)
            arts = art_tokens(text)
            amend_positions = [m.start() for m in AMEND_RE.finditer(text)]
            tok_edge = {}
            for i, (ts, te, tid, label, kind) in enumerate(toks):
                if kind == "self" or tid is None:
                    continue
                stats["mentiuni_acte"] += 1
                if tid == aid:
                    stats["mentiuni_proprii"] += 1
                    continue
                if tid.startswith("EXT:"):
                    ext_labels.setdefault(tid, (label, "eu" if tid.startswith("EXT:EU-") else kind))
                ed = edge(seg_id, tid, "cites_act", line_of(ts), snippet(text, ts, te))
                ed.setdefault("articles", set())
                tok_edge[i] = ed
            for g_start, g_end, nums in group_arts(text, arts):
                ti, rule = resolve_group(text, g_start, g_end, toks, amend_positions)
                target_act = aid if ti is None or toks[ti][2] is None or toks[ti][2] == aid else toks[ti][2]
                line = line_of(g_start)
                ev = snippet(text, g_start, min(g_end, g_start + 60))
                stats["grupuri"] += 1
                for artnum in nums:
                    stats["trimiteri_articol"] += 1
                    if target_act in acts:
                        tgt = acts[target_act]
                        scope = "intern" if target_act == aid else "extern"
                        if not tgt.anchors:
                            if ti in tok_edge:
                                tok_edge[ti]["articles"].add(artnum)
                            stats["articol_in_act_pe_puncte"] += 1
                            continue
                        if artnum in tgt.anchor_set:
                            tprov = target_act + "#art." + artnum
                            if tprov == seg_id:
                                stats["autoreferinta"] += 1
                                continue
                            ed = edge(seg_id, tprov, "cites_article", line, ev, rule)
                            ed["resolved"] = True
                            ed["scope"] = scope
                            stats[f"articol_{scope}_rezolvat"] += 1
                        else:
                            ed = edge(seg_id, target_act, "cites_article:" + artnum, line, ev, rule)
                            ed["kind"] = "cites_article"
                            ed["resolved"] = False
                            ed["article"] = artnum
                            ed["scope"] = scope
                            ed["suspect"] = suspects(artnum, tgt.anchor_set)
                            ed["in_force_register"] = nif.get((target_act, artnum), [])
                            stats[f"articol_{scope}_nerezolvat"] += 1
                    else:
                        if ti in tok_edge:
                            tok_edge[ti]["articles"].add(artnum)
                        stats["articol_in_act_nedetinut"] += 1

    # aliasurile codurilor citate pe nume si pe numar: nodul pe nume se varsa in nodul pe numar
    alias_map = {}
    for name_id, cnt in aliases.items():
        num_id, _n = cnt.most_common(1)[0]
        alias_map[name_id] = num_id
        if num_id not in ext_labels and num_id.startswith("EXT:") and name_id in ext_labels:
            ext_labels[num_id] = (ext_labels[name_id][0] + f" ({num_id[4:]})", "code")
    if alias_map:
        merged = {}
        for (src, tgt, kind), e in edges.items():
            new_tgt = alias_map.get(tgt, tgt)
            key = (src, new_tgt, kind)
            if key in merged:
                m = merged[key]
                m["count"] += e["count"]
                m["lines"] |= e["lines"]
                if "articles" in e:
                    m.setdefault("articles", set()).update(e["articles"])
            else:
                e = dict(e)
                e["target"] = new_tgt
                merged[key] = e
        edges = merged
        for name_id in alias_map:
            ext_labels.pop(name_id, None)

    for tid, (label, kind) in ext_labels.items():
        nodes[tid] = {"id": tid, "kind": "external-act", "label": label, "class": kind}

    # serializare determinista
    edge_list = []
    for key in sorted(edges):
        e = dict(edges[key])
        e["lines"] = sorted(e["lines"])
        if "articles" in e:
            e["articles"] = sorted(e["articles"], key=art_sort_key)
        edge_list.append(e)
    node_list = [nodes[k] for k in sorted(nodes, key=node_sort_key)]

    counts = dict(stats)
    counts.update({
        "acte_detinute": len(acts),
        "acte_ancorate": sum(1 for a in acts.values() if a.anchors),
        "dispozitii": sum(1 for n in node_list if n["kind"] == "provision"),
        "acte_ue_detinute": len(eu),
        "acte_externe": len(ext_labels),
        "aliasuri_coduri": {k: v for k, v in sorted(alias_map.items())},
        "muchii_cites_act": sum(1 for e in edge_list if e["kind"] == "cites_act"),
        "muchii_cites_article": sum(1 for e in edge_list if e["kind"] == "cites_article" and e.get("resolved")),
        "muchii_cites_article_nerezolvate": sum(1 for e in edge_list if e["kind"] == "cites_article" and not e.get("resolved")),
    })
    graph = {
        "generated": dt.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        "generated_by": SELF_PATH,
        "inputs": {"inforce_generated": (inforce or {}).get("generated"), "hcc_generated": (hcc or {}).get("generated"),
                   "roots": ROOTS},
        "counts": counts,
        "nodes": node_list,
        "edges": edge_list,
    }
    return graph, acts


def art_sort_key(a):
    m = re.match(r"^(\d+)(?:\^(\d+))?(?:/(\d+))?$", a)
    if not m:
        return (10 ** 9, 0, 0, a)
    return (int(m.group(1)), int(m.group(2) or 0), int(m.group(3) or 0), "")


def node_sort_key(nid):
    if "#" in nid:
        act, seg = nid.split("#", 1)
        if seg.startswith("art."):
            return (1, act, 1) + art_sort_key(seg[4:])
        return (1, act, 0, 0, 0, 0, seg)
    return (0, nid, 0, 0, 0, 0, "")


# ---------------------------------------------------------------------------------------------
# Raportul
# ---------------------------------------------------------------------------------------------

def report(graph, acts):
    nodes = {n["id"]: n for n in graph["nodes"]}
    edges = graph["edges"]
    c = graph["counts"]
    L = []
    a = L.append

    def act_of(nid):
        return nid.split("#", 1)[0]

    a("# Graful de citare al actelor detinute")
    a("")
    a(f"Generat {graph['generated'][:16].replace('T', ' ')} de `{SELF_PATH}`. Nu edita de mina; se reface rulind scriptul. "
      f"Datele: `citation-graph.json` in acelasi folder.")
    a("")
    a("**Ce este.** Trimiterile dintre actele detinute, extrase mecanic din textul brut: fiecare muchie poarta fisierul "
      "si liniile din care a fost citita, si nicio muchie nu este dedusa. Graful nu se citeaza. El spune unde sa deschizi "
      "fisierul, iar ancora se citeste.")
    a("")
    a("**Regula de folosire.** Inainte de a cita un articol, cauta-l in tabelul „Dispozitii cu stare speciala si cine le "
      "citeaza”: daca apare, fie el, fie o dispozitie de care depinde nu se aplica astazi asa cum sta in text. Inainte de a "
      "ingera un act, citeste „Coada de ingerare”: acolo sint actele pe care textele detinute le citeaza si vault-ul nu le are.")
    a("")
    a("## Numere")
    a("")
    a("| | |")
    a("|---|---:|")
    rows = [
        ("acte primare detinute (din care ancorate pe articole)", f"{c['acte_detinute']} ({c['acte_ancorate']})"),
        ("dispozitii (noduri-articol)", c["dispozitii"]),
        ("extrase UE detinute (noduri-tinta)", c["acte_ue_detinute"]),
        ("acte citate si nedetinute (noduri externe)", c["acte_externe"]),
        ("mentiuni de acte in text (din care ale actului insusi)", f"{c.get('mentiuni_acte', 0)} ({c.get('mentiuni_proprii', 0)})"),
        ("muchii act -> act (agregate pe segment-sursa)", c["muchii_cites_act"]),
        ("trimiteri la articole citite (in grupuri de enumerare)", f"{c.get('trimiteri_articol', 0)} ({c.get('grupuri', 0)})"),
        ("  rezolvate in actul curent", c.get("articol_intern_rezolvat", 0)),
        ("  rezolvate in alt act detinut", c.get("articol_extern_rezolvat", 0)),
        ("  nerezolvate: articolul nu are ancora in actul-tinta", c.get("articol_intern_nerezolvat", 0) + c.get("articol_extern_nerezolvat", 0)),
        ("  catre acte nedetinute (notate pe muchia act -> act)", c.get("articol_in_act_nedetinut", 0)),
        ("  catre acte pe puncte (fara articole)", c.get("articol_in_act_pe_puncte", 0)),
        ("  autoreferinte (articolul se citeaza pe sine), ignorate", c.get("autoreferinta", 0)),
        ("muchii articol -> articol (agregate)", c["muchii_cites_article"]),
        ("muchii articol -> act nerezolvate (agregate)", c["muchii_cites_article_nerezolvate"]),
    ]
    for k, v in rows:
        a(f"| {k} | {v} |")
    a("")
    rules = Counter()
    for e in edges:
        if e["kind"] == "cites_article":
            rules[e.get("rule", "?")] += e["count"]
    a("Regula care a dat actul-tinta, pe trimiteri: " + ", ".join(f"{k} {v}" for k, v in sorted(rules.items())) + ". "
      "„intern” = niciun act in context, deci actul curent; „din” = `art. N ... din Legea X` sau `(art. N, M) Directiva X`; "
      "„paranteza” = `Legea X (art. N)`; „doua-puncte” = `din Codul X: art. N, M`; "
      "„modificare” = `Legea X se modifica dupa cum urmeaza: ... articolul N`. `din legea indicata` trimite la ultima lege "
      "numita in acelasi segment.")
    a("")
    if c.get("aliasuri_coduri"):
        a("Coduri citate si pe nume si pe numar, unite dupa textul care le scrie impreuna: "
          + "; ".join(f"{k[4:]} = {v[4:] if v.startswith('EXT:') else v}" for k, v in c["aliasuri_coduri"].items()) + ".")
        a("")

    # --- coada de ingerare -------------------------------------------------------------
    ext = defaultdict(lambda: {"count": 0, "acts": set(), "articles": defaultdict(int), "by_act": defaultdict(int)})
    for e in edges:
        if e["kind"] != "cites_act" or not e["target"].startswith("EXT:"):
            continue
        x = ext[e["target"]]
        x["count"] += e["count"]
        x["acts"].add(act_of(e["source"]))
        x["by_act"][act_of(e["source"])] += e["count"]
        for art in e.get("articles", []):
            x["articles"][art] += 1

    def ext_table(filter_fn, title, note, cap):
        items = [(tid, x) for tid, x in ext.items() if filter_fn(tid, nodes[tid])]
        items.sort(key=lambda kv: (-kv[1]["count"], -len(kv[1]["acts"]), kv[0]))
        a(f"### {title}")
        a("")
        a(note)
        a("")
        if not items:
            a("Nimic.")
            a("")
            return
        a("| act citat | mentiuni | acte care il citeaza | cel mai des din | articole citate |")
        a("|---|---:|---:|---|---|")
        for tid, x in items[:cap]:
            top = max(x["by_act"].items(), key=lambda kv: (kv[1], kv[0]))
            arts = sorted(x["articles"].items(), key=lambda kv: (-kv[1], art_sort_key(kv[0])))[:4]
            arts_s = ", ".join(f"art. {k}" + (f" (x{v})" if v > 1 else "") for k, v in arts) or "-"
            a(f"| `{tid[4:]}` {nodes[tid]['label']} | {x['count']} | {len(x['acts'])} | `{top[0]}` ({top[1]}) | {arts_s} |")
        if len(items) > cap:
            a(f"| … inca {len(items) - cap} in JSON | | | | |")
        a("")

    a("## Coada de ingerare")
    a("")
    a("Actele pe care textele detinute le citeaza si care nu sint in vault, in ordinea numarului de mentiuni. "
      "Un act citat de multe acte detinute inchide mai multe lanturi de trimitere decit unul citat des dintr-un singur loc; "
      "coloana a treia este cea care conteaza pentru ordinea de ingerare. Graful nu stie daca un act citat mai este in "
      "vigoare: o lege abrogata ramine citata de textele care n-au fost actualizate, si apare aici la fel ca una in vigoare.")
    a("")
    ext_table(lambda t, n: n["class"] in ("law", "code", "hg", "const") and not t.startswith("EXT:LEGE:"),
              "Acte moldovenesti citate pe numar", "Legi, coduri si hotariri de Guvern identificate prin numar si an.", 30)
    ext_table(lambda t, n: n["class"] == "eu",
              "Acte UE citate si neextrase", "Directive si regulamente UE care nu au un extras `UE-*` in `raw/papers/cnpf/`.", 20)
    ext_table(lambda t, n: t.startswith("EXT:LEGE:"),
              "Legi citate doar pe nume, fara corespondent in vault",
              "Fara numar in text si fara un titlu detinut care sa le contina, deci identificate numai prin primele cuvinte; "
              "acelasi act poate aparea sub doua forme flexionate. Orientativ.", 15)

    # --- acquis ----------------------------------------------------------------------------
    a("## Acquis: extrasele UE detinute si actele care le citeaza")
    a("")
    a("Mentiunile actelor detinute catre cele 29 de extrase `UE-*`. Schita unei concordante: un act care citeaza o "
      "directiva o transpune, o aplica sau doar o numeste, si numai textul spune care.")
    a("")
    eu_in = defaultdict(lambda: defaultdict(int))
    for e in edges:
        if e["kind"] == "cites_act" and e["target"].startswith("UE-"):
            eu_in[e["target"]][act_of(e["source"])] += e["count"]
    a("| extras UE | mentiuni | citat din |")
    a("|---|---:|---|")
    for eid in sorted(n["id"] for n in nodes.values() if n["kind"] == "eu-act"):
        by = eu_in.get(eid, {})
        total = sum(by.values())
        src = ", ".join(f"`{k}` ({v})" for k, v in sorted(by.items(), key=lambda kv: (-kv[1], kv[0]))[:8])
        if len(by) > 8:
            src += f", … (+{len(by) - 8})"
        a(f"| `{eid}` | {total} | {src or '-'} |")
    a("")

    # --- dispozitii cu stare speciala --------------------------------------------------
    a("## Dispozitii cu stare speciala si cine le citeaza")
    a("")
    a("Dispozitiile care apar in registrul in-force (textul din fisier nu se aplica inca), in registrul HCC (declarate "
      "neconstitutionale, in tot sau in parte) sau al caror titlu spune „abrogat”, si muchiile articol -> articol care intra "
      "in ele. Un articol din coloana „citat din” depinde de o dispozitie care nu sta in picioare asa cum e scrisa. Numai "
      "dispozitiile cu cel putin o citare intra aici, intii cele citate din alte acte; toate starile sint in JSON.")
    a("")
    inbound = defaultdict(list)
    for e in edges:
        if e["kind"] == "cites_article" and e.get("resolved"):
            inbound[e["target"]].append(e)
    rows = []
    for nid, n in nodes.items():
        if n["kind"] != "provision":
            continue
        flags = []
        if n["not_in_force"]:
            f = n["not_in_force"][0]
            flags.append(f"in-force: {f['operation']} de la {f['effective_from']}" + (f" ({f['subunit']})" if f["subunit"] else ""))
        if n["hcc"]:
            h = n["hcc"][0]
            flags.append(f"HCC: {h['hcc']}" + (f", {h['subunit']}" if h["subunit"] else "") + (f", {h['scope']}" if h["scope"] else ""))
            if len(n["hcc"]) > 1:
                flags[-1] += f" (+{len(n['hcc']) - 1})"
        if n["abrogat"]:
            flags.append("abrogat")
        if not flags or nid not in inbound:
            continue
        ins = inbound[nid]
        total = sum(e["count"] for e in ins)
        cross = sum(e["count"] for e in ins if act_of(e["source"]) != n["act"])
        srcs = sorted(ins, key=lambda e: (-e["count"], e["source"]))
        rows.append((total, cross, nid, n, flags, srcs))
    rows.sort(key=lambda r: (-r[1], -r[0], r[2]))
    if rows:
        a("| dispozitie | stare | citari (din alte acte) | citat din |")
        a("|---|---|---:|---|")
        cap = 80
        for total, cross, nid, n, flags, srcs in rows[:cap]:
            src_s = ", ".join(f"`{e['source']}`" + (f" l.{e['lines'][0]}" if len(srcs) <= 3 else "") for e in srcs[:6])
            if len(srcs) > 6:
                src_s += f", … (+{len(srcs) - 6})"
            a(f"| `{nid}` l.{n['line']} | {'; '.join(flags)} | {total} ({cross}) | {src_s} |")
        if len(rows) > cap:
            a(f"| … inca {len(rows) - cap} dispozitii, in JSON | | | |")
    else:
        a("Nicio dispozitie cu stare speciala nu este citata de alt articol.")
    a("")
    n_nif = sum(1 for n in nodes.values() if n["kind"] == "provision" and n["not_in_force"])
    n_hcc = sum(1 for n in nodes.values() if n["kind"] == "provision" and n["hcc"])
    n_abr = sum(1 for n in nodes.values() if n["kind"] == "provision" and n["abrogat"])
    a(f"Stari atasate dispozitiilor, in total: {n_nif} in-force, {n_hcc} HCC, {n_abr} abrogat. "
      f"{len(rows)} dintre ele au cel putin o citare intrata, {sum(1 for r in rows if r[1])} din alte acte.")
    a("")
    unattr = [(n["id"], n["hcc_unattributed"]) for n in nodes.values() if n["kind"] == "act" and n.get("hcc_unattributed")]
    if unattr:
        a("Acte care poarta hotariri HCC fara articol atribuit (orice citare din ele poate lovi textul anulat): "
          + ", ".join(f"`{i}` ({len(h)})" for i, h in sorted(unattr)) + ".")
        a("")

    # --- actele ---------------------------------------------------------------------------
    a("## Actele: ce citeaza si de cine sint citate")
    a("")
    a("Pe act: tintele distincte ale mentiunilor (detinute + externe), actele detinute distincte care il mentioneaza, "
      "trimiterile la articole rezolvate in propriul text, rezolvate in alt act detinut, si nerezolvate (articolul citat nu "
      "are ancora in actul-tinta: abrogat cu ciotul sters, renumerotat, exponent turtit in sursa, sau o greseala de citire).")
    a("")
    out_t, in_a, intra, cross, unres, ext_a = (defaultdict(set), defaultdict(set), defaultdict(int),
                                               defaultdict(int), defaultdict(int), defaultdict(int))
    for e in edges:
        sa = act_of(e["source"])
        if e["kind"] == "cites_act":
            out_t[sa].add(e["target"])
            if e["target"] in acts:
                in_a[e["target"]].add(sa)
            else:
                ext_a[sa] += e["count"]
        elif e["kind"] == "cites_article":
            if not e.get("resolved"):
                unres[sa] += e["count"]
            elif e["scope"] == "intern":
                intra[sa] += e["count"]
            else:
                cross[sa] += e["count"]
    a("| act | ancore | citeaza (acte) | citat de (acte) | art. interne | art. in alte acte | nerezolvate | mentiuni externe |")
    a("|---|---:|---:|---:|---:|---:|---:|---:|")
    for aid in sorted(acts):
        n = nodes[aid]
        a(f"| `{aid}` | {n['anchors']} | {len(out_t[aid])} | {len(in_a[aid])} | {intra[aid]} | {cross[aid]} | {unres[aid]} | {ext_a[aid]} |")
    a("")

    # --- nerezolvate ----------------------------------------------------------------------
    a("## Trimiteri nerezolvate")
    a("")
    a("Articole citate care nu au ancora in actul-tinta, grupate pe tinta. Cauze cunoscute: articolul a fost abrogat si "
      "consolidarea a sters ciotul (`L-548-1995` art. 12, 13, 29, 30, 48, 54, 73; CLAUDE.md, intrebarea 6); articolul a fost "
      "abrogat si textul care il citeaza n-a fost actualizat; actul-tinta a fost renumerotat (Codul civil in 2019); ancora "
      "lipseste din cauza unei greseli de tipar in sursa (`L-100-2017` art. 52; intrebarea 4); exponentul a fost turtit in "
      "sursa (`art. 3142` pentru 314^2; intrebarea 2); sau citirea a luat drept articol al acestui act unul al altui act, "
      "nenumit in context. Fiecare rind trimite la o linie: deschide-o inainte de a trage o concluzie.")
    a("")
    grp = defaultdict(lambda: {"count": 0, "sources": []})
    for e in edges:
        if e["kind"] == "cites_article" and not e.get("resolved"):
            g = grp[(e["target"], e["article"])]
            g["count"] += e["count"]
            g["sources"].append(e)
    items = sorted(grp.items(), key=lambda kv: (-kv[1]["count"], kv[0][0], art_sort_key(kv[0][1])))
    if items:
        a("| act-tinta | articol citat | citari | poate fi | regula | exemplu (sursa, linie) | fragment |")
        a("|---|---|---:|---|---|---|---|")
        for (tgt, art), g in items[:60]:
            s = sorted(g["sources"], key=lambda e: (-e["count"], e["source"]))[0]
            ev = s["evidence"].replace("|", "\\|")
            hint = []
            if s.get("suspect"):
                hint.append("exponent turtit: " + ", ".join(f"art. {x}" for x in s["suspect"]))
            if s.get("in_force_register"):
                f = s["in_force_register"][0]
                hint.append(f"in registrul in-force: {f['operation']} de la {f['effective_from']}, textul lipseste din fisier")
            a(f"| `{tgt}` | art. {art} | {g['count']} | {'; '.join(hint) or '-'} | {s.get('rule', '')} | `{s['source']}` l.{s['lines'][0]} | {ev} |")
        if len(items) > 60:
            a(f"| … inca {len(items) - 60} grupuri, in JSON | | | | | | |")
    else:
        a("Nimic.")
    a("")
    a("„Poate fi” este o ipoteza mecanica, nu o muchie: numarul citat, despartit in baza si exponent, da o ancora existenta. "
      "Se verifica in sursa inainte de a fi folosita.")
    a("")

    # --- limite -----------------------------------------------------------------------------
    a("## Ce nu face acest graf")
    a("")
    a("- Nu deduce. O muchie exista numai daca textul o contine, si poarta liniile din care vine.")
    a("- Nu coboara sub articol: `alin.`, `lit.`, `pct.` nu sint noduri.")
    a("- Nu citeste articolele actelor pe puncte (HG, regulamente BNM si CNPF, proceduri DCU), nici extrasele UE: pentru ele exista doar muchii la nivel de act.")
    a("- Citeste numai numerele scrise dupa `art.` sau `articolul`. Intr-un interval (`art. 5-7`) sau intr-o enumerare "
      "prescurtata (`art. 2-5, 7-21`) numerele care urmeaza fara `art.` nu sint citite.")
    a("- Un articol citat fara act in context este atribuit actului curent. Regulile de context sint cele de mai sus; "
      "o trimitere al carei act sta mai departe in fraza decit le vad ele, sau e numit prin `legea mentionata` fara o "
      "lege numita inainte, ramine atribuita actului curent.")
    a("- O lege citata pe nume este rezolvata la actul detinut al carui titlu contine numele, numai daca exact unul il contine.")
    a("- Notele de modificare intre paranteze drepte, rindurile blocului de istoric si referintele la Monitorul Oficial sint mascate inainte de citire.")
    a("- Nu citeste corpusul englez BNM (traduceri) si nici radacinile de politici.")
    a("- Nu stie daca un act citat si nedetinut mai este in vigoare.")
    a("")
    return "\n".join(L) + "\n"


# ---------------------------------------------------------------------------------------------
# Scriere si verificare
# ---------------------------------------------------------------------------------------------

def dump_json(graph):
    """Un nod sau o muchie pe rind, ca diff-ul din git sa fie citibil."""
    head = {k: graph[k] for k in ("generated", "generated_by", "inputs", "counts")}
    s = json.dumps(head, ensure_ascii=False, indent=1).rstrip().rstrip("}").rstrip()
    s += ",\n \"nodes\": [\n"
    s += ",\n".join("  " + json.dumps(n, ensure_ascii=False, separators=(",", ":")) for n in graph["nodes"])
    s += "\n ],\n \"edges\": [\n"
    s += ",\n".join("  " + json.dumps(e, ensure_ascii=False, separators=(",", ":")) for e in graph["edges"])
    s += "\n ]\n}\n"
    return s


def strip_generated(s):
    return re.sub(r"\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?::\d\d)?", "", s, count=1)


def main():
    argv = sys.argv[1:]
    graph, acts = build()
    md = report(graph, acts)
    js = dump_json(graph)
    c = graph["counts"]
    summary = (f"{c['acte_detinute']} acte, {c['dispozitii']} dispozitii, {c['acte_externe']} acte externe, "
               f"{c['muchii_cites_act']} muchii act, {c['muchii_cites_article']} muchii articol, "
               f"{c['muchii_cites_article_nerezolvate']} nerezolvate")
    if "--dry-run" in argv:
        print(summary)
        return 0
    if "--check" in argv:
        same = (os.path.exists(OUT_JSON) and os.path.exists(OUT_MD)
                and strip_generated(read(OUT_JSON)) == strip_generated(js)
                and strip_generated(read(OUT_MD)) == strip_generated(md))
        print("up to date" if same else "OUT OF DATE")
        return 0 if same else 1
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_JSON, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(js)
    with open(OUT_MD, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(md)
    print(f"graful de citare scris: {summary}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
