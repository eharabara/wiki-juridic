# Consolidarea și scalarea `wiki-juridic` — plan de implementare

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task.

**Goal:** Stabilizarea proiectului `wiki-juridic`, reducerea costului de întreținere și pregătirea unei căi controlate către căutare rapidă, colaborare sigură și, opțional, o interfață read-only, fără a pierde Markdown-ul și Git-ul ca sursă canonică.

**Architecture:** Se păstrează arhitectura existentă `raw → structured → generated controls → Git audit`. Se consolidează mai întâi corectitudinea și reproductibilitatea, apoi se introduc biblioteci comune și registre declarative, după care se adaugă regenerarea incrementală și un index SQLite strict derivat. O interfață/API se construiește numai peste indexul derivat și nu primește drept de scriere în corpus.

**Tech Stack:** Python 3.11–3.12, Markdown/YAML, Git/GitHub Actions, `unittest`, PyYAML, `lxml` și celelalte dependențe confirmate prin inventar; SQLite FTS5 pentru căutarea derivată; Obsidian rămâne interfața editorială.

---

## 1. Rezultatul urmărit

La sfârșitul programului:

1. toate testele și controalele proiectului trec pe Windows și Linux;
2. nicio regulă dependentă de timp nu folosește o dată hardcodată;
3. dependențele și versiunile Python sunt reproductibile;
4. frontmatter-ul, căile și hashurile sunt tratate prin utilitare comune;
5. actele ingerabile sunt descrise declarativ, nu numai într-un dicționar Python mare;
6. modificarea unui singur act poate declanșa o verificare incrementală locală;
7. colaboratorii lucrează în worktree-uri/ramuri separate, cu ownership explicit;
8. căutarea full-text este rapidă și poate filtra după act, articol, statut, perimetru și sursă;
9. orice UI/API este read-only și afișează proveniența, starea in-force și HCC;
10. Markdown-ul și Git-ul rămân singura sursă canonică; SQLite, grafurile și UI-ul se reconstruiesc din ele.

## 2. Constrângeri obligatorii

- Nu se modifică niciun text din `raw/` fără autoritatea expresă a lui Eugen și procedura de backup + strip-and-compare din `CLAUDE.md`.
- Nu se schimbă o analiză juridică înainte de reîmprospătarea `legal-career/06-matter-log.md` în ziua executării.
- Nu se începe implementarea în worktree-ul actual cât timp modificările existente nu au un proprietar și o stare clară.
- Nu se transformă Graphify în sursă juridică; rămâne instrument exploratoriu.
- Nu se mută sursa canonică în SQLite sau într-o aplicație web.
- Nu se adaugă autentificare, scriere prin API, vector database sau infrastructură cloud înainte de trecerea porților P0–P2.
- Orice commit sau push se face numai cu autorizarea explicită a lui Eugen și prin procedura `close_session.py`.

## 3. Starea de bază măsurată

- `close_session.py --check --no-hash`: curat, 0 erori și 2 avertismente.
- Validator: 285 pagini structurate, 686 surse raw, 686 hashuri reproduse.
- Teste: 17 rulate, o eroare — contractul `scan_file(..., today)` nu este reflectat în test.
- Control read-only fără hash: aproximativ 53 s; graful juridic consumă aproximativ 25 s, validatorul aproximativ 13 s.
- Graful juridic: 247 acte, 18.292 noduri-dispoziție, 10.746 muchii articol–articol.
- `citation-graph.json`: 8.776.509 octeți.
- Arborele Git are modificări și fișiere neversionate preexistente; implementarea trebuie izolată.

---

# Faza P0 — Stabilizare și bază reproductibilă

**Durată orientativă:** 1–2 zile de lucru.

**Poartă de ieșire:** toate testele și controalele trec; CI rulează ambele; nu există dată hardcodată în controlul temporal; mediul poate fi reconstruit din manifest.

## Task 0: Izolarea lucrului și capturarea baseline-ului

**Objective:** Evitarea amestecării programului de scalare cu lotul juridic aflat deja în lucru.

**Files:**
- Nu se modifică fișiere în acest task.
- Referință: `CLAUDE.md`, `AGENTS.md`, `log.md`.

**Steps:**

1. Rulați `git status --short` și grupați fiecare fișier modificat/neversionat după lotul care l-a produs.
2. Stabiliți cu Eugen dacă lotul curent:
   - se finalizează înaintea programului;
   - se lasă în worktree-ul actual, iar programul pornește într-un worktree nou;
   - se arhivează/abandonează explicit.
3. Dacă se creează worktree, folosiți o ramură dedicată, de exemplu `engineering/wiki-scalability`.
4. Rulați baseline-ul read-only:

```bash
python _meta/close_session.py --check --no-hash
python -m unittest discover -s tests -v
```

5. Salvați rezultatele în nota de lucru a sesiunii, nu într-un raport canonic nou.

**Expected:** controalele proiectului trec; testele reproduc eroarea `scan_file() missing ... today`; nicio stare existentă nu este modificată.

**Acceptance:** worktree-ul și ownership-ul sunt clare înainte de prima editare.

---

## Task 1: Repararea contractului testului `scan_file`

**Objective:** Readucerea suitei de teste la verde fără schimbarea comportamentului de producție.

**Files:**
- Modify: `tests/test_build_coverage.py:40-59`
- Read only: `_meta/coverage/build_coverage.py:102-153`

**Step 1: Actualizați testul existent**

În apelul din test, transmiteți o dată explicită și stabilă:

```python
record = coverage.scan_file(
    path,
    "raw/papers/moldova-legal/L-TEST-2026.md",
    dt.date(2026, 9, 28),
)
```

**Step 2: Rulați testul țintă**

```bash
python -m unittest tests.test_build_coverage.BuildCoverageTests.test_scan_file_recognises_abbreviated_article_anchors -v
```

**Expected:** PASS.

**Step 3: Rulați întreaga suită**

```bash
python -m unittest discover -s tests -v
```

**Expected:** toate cele 17 teste trec.

**Step 4: Rulați controlul proiectului**

```bash
python _meta/close_session.py --check --no-hash
```

**Expected:** 0 erori; numai avertismentele juridice preexistente.

---

## Task 2: Introducerea testelor unitare în CI

**Objective:** Prevenirea situației în care validatorul trece, dar testele unitare sunt defecte.

**Files:**
- Modify: `.github/workflows/validate.yml:36-60`

**Step 1: Adăugați un pas de teste înaintea controalelor generate**

```yaml
      - name: Teste unitare
        shell: bash
        run: python -X utf8 -m unittest discover -s tests -v
```

**Step 2: Păstrați separat controlul wiki**

Nu înlocuiți pasul existent `close_session.py --check`; testele și validarea corpusului au roluri diferite.

**Step 3: Verificați local comenzile CI**

```bash
python -X utf8 -m unittest discover -s tests -v
python -X utf8 _meta/close_session.py --check
```

**Expected:** ambele ies cu cod 0.

**Acceptance:** un test defect blochează PR-ul chiar dacă validatorul trece.

---

## Task 3: Eliminarea datei hardcodate din detectorul amânărilor în proză

**Objective:** Evaluarea candidaților în raport cu data reală sau cu o dată `--as-of` explicită și testabilă.

**Files:**
- Modify: `_meta/inforce/build_prose_deferral_candidates.py:14-110`
- Create: `tests/test_build_prose_deferral_candidates.py`

**Design:**

- introduceți `datetime.date`;
- `has_future_date(para, today)` primește data explicit;
- `build(today)` primește data explicit;
- CLI acceptă `--as-of YYYY-MM-DD`;
- implicit se folosește `date.today()`;
- raportul nu va conține o dată care se schimbă zilnic dacă setul de rezultate este identic; formularea fixă „după 2026-09-26” devine „după data de referință a rulării”; astfel `--check` devine stale numai când rezultatul semantic se schimbă.

**Step 1: Scrieți teste care eșuează**

Testați cel puțin:

```python
def test_future_date_depends_on_as_of_date():
    para = "Prevederea intră în vigoare la 1 ianuarie 2027."
    assert module.has_future_date(para, dt.date(2026, 9, 28)) is True
    assert module.has_future_date(para, dt.date(2027, 1, 2)) is False
```

```python
def test_cli_as_of_rejects_invalid_date():
    # extrageți parsing-ul într-o funcție testabilă
    with self.assertRaises(ValueError):
        module.parse_as_of("2026-13-40")
```

**Step 2: Verificați eșecul**

```bash
python -m unittest tests.test_build_prose_deferral_candidates -v
```

**Expected:** FAIL înaintea implementării.

**Step 3: Implementați minimul necesar**

Nu modificați euristicile juridice `TRIGGER`, `CONDITION` și `EXCEPTION` în același task.

**Step 4: Regenerați raportul cu data zilei**

```bash
python _meta/inforce/build_prose_deferral_candidates.py
python _meta/inforce/build_prose_deferral_candidates.py --check
```

**Expected:** raport regenerat o dată, apoi `--check` trece.

**Step 5: Rulați toate testele și controalele**

```bash
python -m unittest discover -s tests -v
python _meta/close_session.py --check --no-hash
```

---

## Task 4: Rezolvarea celor două avertismente curente

**Objective:** Obținerea unui baseline cu zero avertismente acționabile înaintea refactorizărilor.

**Files:**
- Refresh, numai din masterul proiectului: `legal-career/06-matter-log.md`
- Modify după citirea sursei: `entities/L-180-2026.md`
- Read: `raw/papers/moldova-legal/UE-2023-1114.md`

**Prerequisite:** Eugen furnizează registrul curent din proiectul „Legal Wiki”. Nu se reconstruiește local.

**Steps:**

1. Înlocuiți corpul matter log-ului numai cu textul furnizat de Eugen.
2. Reștampilați copia:

```bash
python _meta/schema/stamp_copies.py --taken YYYY-MM-DD legal-career/06-matter-log.md
```

3. Deschideți și citiți articolul/anexa exactă din `UE-2023-1114.md` care susține afirmația fără localizator.
4. Înlocuiți citarea la nivel de pagină cu un localizator exact; nu adăugați un articol presupus.
5. Rulați:

```bash
python _meta/schema/validate_wiki.py --all
```

**Expected:** 0 erori, 0 avertismente sau numai avertismente noi explicate explicit.

**Acceptance:** nicio concluzie juridică nu este schimbată fără sursa deschisă și citită.

---

## Task 5: Manifest reproductibil de dependențe

**Objective:** Instalarea identică a mediului de validare și, separat, a mediului complet de ingerare.

**Files:**
- Create: `pyproject.toml`
- Optional create: `requirements-lock.txt` sau `uv.lock`, după alegerea instrumentului
- Modify: `README.md:25-35`
- Modify: `.github/workflows/validate.yml:36-43`

**Step 1: Inventariați importurile externe**

Folosiți AST, nu o listă presupusă. Clasificați dependențele în:

- `core`: controale și validator;
- `ingest`: lxml, PDF/DOCX și alte biblioteci confirmate;
- `dev`: testare și instrumente de dezvoltare.

**Step 2: Creați `pyproject.toml` minimal**

Structură propusă:

```toml
[project]
name = "wiki-juridic-tools"
version = "0.1.0"
requires-python = ">=3.11,<3.13"
dependencies = [
  "PyYAML>=6,<7",
]

[project.optional-dependencies]
ingest = [
  # numai pachetele confirmate din importurile reale
]
dev = []
```

Nu introduceți pachete care nu sunt importate sau necesare.

**Step 3: Instalați într-un mediu curat**

```bash
python -m venv .venv-test
. .venv-test/Scripts/activate
python -m pip install -e ".[dev]"
python -m unittest discover -s tests -v
python _meta/close_session.py --check
```

**Step 4: Actualizați CI**

Înlocuiți instalarea izolată `pip install pyyaml` cu instalarea proiectului.

**Acceptance:** un clone curat poate valida proiectul fără cunoaștere externă asupra dependențelor.

---

# Faza P1 — Consolidarea internă a instrumentelor

**Durată orientativă:** 3–5 zile.

**Poartă de ieșire:** parsarea comună este testată; registrele pot fi alimentate declarativ; principalele cazuri juridice dificile au teste sintetice.

## Task 6: Bibliotecă comună pentru frontmatter, căi și hashuri

**Objective:** Eliminarea interpretărilor divergente ale aceleiași metadate de către scripturi diferite.

**Files:**
- Create: `_meta/lib/__init__.py`
- Create: `_meta/lib/frontmatter.py`
- Create: `_meta/lib/paths.py`
- Create: `_meta/lib/hashes.py`
- Create: `tests/test_meta_frontmatter.py`
- Create: `tests/test_meta_hashes.py`
- Modify gradual: `_meta/coverage/build_coverage.py`
- Modify gradual: `_meta/inforce/build_inforce_register.py`
- Modify gradual: `_meta/hcc/build_hcc_register.py`
- Modify gradual: `_meta/graph/build_citation_graph.py`

**Approach:** Migrați câte un consumator, cu teste și comparație byte-for-byte a artefactului înainte/după. Nu migrați toate scripturile într-un singur diff.

**API minim propus:**

```python
def split_frontmatter(text: str) -> tuple[dict, str]: ...
def load_markdown(path: Path) -> tuple[dict, str]: ...
def canonical_relpath(path: Path, root: Path) -> str: ...
def body_hash(body: bytes, convention: str) -> str: ...
def detect_hash_convention(body: bytes, expected: str) -> str | None: ...
```

**Subtasks per consumer:**

1. scrieți fixture/test;
2. capturați artefactul generat înainte;
3. migrați un singur script;
4. regenerați într-un director temporar;
5. comparați ieșirea exactă;
6. rulați toate testele și controalele.

**Acceptance:** zero diferențe în artefactele generate, cu excepția celor aprobate și documentate.

---

## Task 7: Corpus sintetic de regresie pentru parserele juridice

**Objective:** Transformarea capcanelor documentate în teste care previn reapariția lor.

**Files:**
- Create: `tests/fixtures/legal/`
- Create: `tests/test_inforce_register.py`
- Create: `tests/test_hcc_register.py`
- Create: `tests/test_citation_graph.py`
- Create: `tests/test_ingest_business_law.py`

**Fixtures minime:**

1. articol simplu `Articolul 12`;
2. `Art. 31^49.`;
3. articolul special `54^1/1`;
4. titlu rupt pe două linii;
5. articol scris greșit `Articol 52`;
6. act structurat în puncte;
7. lege modificatoare cu articole romane;
8. abrogare la nivel de capitol/secțiune;
9. marcaj HCC rămas în text;
10. HCC recuperată din registrul manual;
11. versiune viitoare;
12. amânare scrisă în proză;
13. țintă „din legea indicată”;
14. exponent turtit și exponent ridicat eronat;
15. traducere engleză care nu poate fi ancorată.

**Rules:**

- fixture-urile sunt sintetice și scurte;
- nu copiați acte complete;
- fiecare test trebuie să declare exact defectul prevenit;
- nu modificați euristicile doar pentru a face fixture-ul să treacă dacă aceasta contrazice corpusul real.

**Verification:**

```bash
python -m unittest tests.test_inforce_register -v
python -m unittest tests.test_hcc_register -v
python -m unittest tests.test_citation_graph -v
python -m unittest tests.test_ingest_business_law -v
python -m unittest discover -s tests -v
```

---

## Task 8: Registru declarativ pentru actele de ingerat

**Objective:** Separarea datelor actelor de logica `ingest_business_law.py`.

**Files:**
- Create: `_meta/imports/moldova-legal/acts.yaml`
- Create: `_meta/imports/moldova-legal/load_registry.py`
- Create: `tests/test_ingest_registry.py`
- Modify: `_meta/imports/moldova-legal/ingest_business_law.py`
- Modify: `_meta/imports/moldova-legal/verify_business_law.py`

**Schema minimă propusă:**

```yaml
acts:
  L-180-2026:
    doc_id: "156426"
    output: raw/papers/moldova-legal/L-180-2026.md
    version: current
    source_cache: legis-md-business/showdetails-156426.html
    expected:
      articles: 106
  L-287-2017--2027-01-01:
    doc_id: "154725"
    output: raw/papers/moldova-legal/viitor/L-287-2017--2027-01-01.md
    version: future
    applies_from: "2027-01-01"
```

**Migration strategy:**

1. definiți schema și validarea;
2. migrați 3 acte reprezentative: curent, viitor, abrogat;
3. comparați outputul exact cu pipeline-ul vechi;
4. migrați registrul complet prin script;
5. păstrați temporar verificarea de paritate între YAML și vechiul `DOCS`;
6. eliminați `DOCS` numai după paritate totală.

**Acceptance:** același set de acte, aceleași căi, aceleași versiuni și aceleași verificări ca înainte.

---

## Task 9: Eliminarea căilor absolute și portabilitatea

**Objective:** Nicio operațiune curentă să nu depindă de `C:\Users\harab\...`.

**Files:**
- Modify numai fișierele active identificate de căutare
- Exclude din refactor scripturile istorice înghețate, dacă nu sunt rulate
- Create: `tests/test_portable_paths.py`

**Steps:**

1. căutați `Users\\harab`, `Users/harab`, `wiki-backups` și căi de drive;
2. clasificați fiecare apariție: activă, istorică, documentară;
3. în codul activ folosiți `Path(__file__).resolve()` și argumente CLI;
4. pentru backup folosiți o opțiune `--backup-root` sau variabilă de mediu documentată;
5. testul importă modulele într-un director temporar și confirmă că rădăcina este derivată, nu fixată.

**Acceptance:** clone-ul poate fi mutat într-o altă cale fără editarea codului.

---

# Faza P2 — Performanță incrementală și colaborare

**Durată orientativă:** 4–7 zile.

**Poartă de ieșire:** un singur act modificat nu declanșează obligatoriu toate scanările locale; build-ul complet rămâne disponibil în CI; colaborarea are reguli verificabile.

## Task 10: Instrumentarea duratei controalelor

**Objective:** Stabilirea unui baseline repetabil înainte de optimizare.

**Files:**
- Create: `_meta/performance/benchmark_controls.py`
- Create: `_meta/performance/README.md`
- Optional generated/ignored: `.cache/wiki-benchmarks/latest.json`
- Modify: `.gitignore`

**Output minim:**

```json
{
  "inforce": {"seconds": 0.0, "returncode": 0},
  "hcc": {"seconds": 0.0, "returncode": 0},
  "citation_graph": {"seconds": 0.0, "returncode": 0},
  "validator_no_hash": {"seconds": 0.0, "returncode": 0}
}
```

**Command:**

```bash
python _meta/performance/benchmark_controls.py --runs 3
```

**Acceptance:** raportul arată mediană/minim/maxim; nu modifică artefactele canonice.

---

## Task 11: Cache incremental pe hash pentru controalele locale

**Objective:** Sărirea controalelor neafectate când intrările lor nu s-au schimbat.

**Files:**
- Create: `_meta/build/dependencies.yaml`
- Create: `_meta/build/cache.py`
- Create: `tests/test_build_cache.py`
- Modify: `_meta/close_session.py`
- Modify: `.gitignore`
- Generated local: `.cache/wiki-build/state.json`

**Dependency map propus:**

- `inforce`: raw legal roots + `pending-consolidations.json`;
- `hcc`: raw legal roots + `recovered-provisions.json`;
- `citation_graph`: raw legal roots + in-force/HCC JSON;
- `coverage`: raw legal roots + registrele generate;
- `schema`: `schema-spec.yaml`;
- `validator`: structured pages + raw metadata + schema + index/log.

**CLI:**

```bash
python _meta/close_session.py --incremental --check --no-hash
python _meta/close_session.py --full --check --no-hash
```

**Safety:**

- CI continuă să ruleze `--full` pe clone curate;
- cache miss înseamnă rulare, nu skip;
- cache corupt înseamnă rulare completă;
- modificările la generator invalidează propriul cache;
- nu se cache-uiește o execuție eșuată.

**Acceptance targets:**

- schimbarea unei singure pagini structurate: sub 15 s local, fără rebuild al grafului;
- schimbarea unui singur act raw: se refac numai controalele dependente;
- build-ul complet produce output byte-identic cu cel incremental.

---

## Task 12: Model de colaborare și ownership al artefactelor

**Objective:** Reducerea conflictelor între agenți și colaboratori.

**Files:**
- Create: `CONTRIBUTING.md`
- Create: `_meta/workflows/ingestion-batch.md`
- Modify: `CLAUDE.md` numai cu un link scurt către regula stabilă, fără duplicarea stării volatile
- Optional create: `.github/pull_request_template.md`

**Reguli obligatorii:**

1. un worktree/branch per lot;
2. un act are un singur proprietar în același interval;
3. `raw/` nu se rezolvă prin merge manual de text;
4. `index.md`, `log.md`, `CLAUDE.md` și artefactele generate se refac pe ramura de integrare;
5. PR-ul declară actele și paginile deținute;
6. înainte de integrare se rulează build complet;
7. conflictele juridice merg la Eugen, nu se „alege” automat una dintre versiuni.

**PR checklist minim:**

```markdown
- [ ] Sursele raw au proveniență și hash
- [ ] Textul raw nu a fost rescris
- [ ] Entitățile/paginile sunt în index
- [ ] Registrul in-force și HCC au fost verificate
- [ ] Testele trec
- [ ] `close_session.py --full --check` trece
- [ ] Avertismentele sunt explicate
```

---

# Faza P3 — Căutare derivată și acces programatic read-only

**Durată orientativă:** 4–7 zile.

**Poartă de intrare:** P0–P2 finalizate; baseline complet verde; schema frontmatter comună.

**Poartă de ieșire:** indexul se reconstruiește integral; rezultatele sunt trasabile; API-ul nu poate modifica wiki-ul.

## Task 13: Specificarea contractului de căutare

**Objective:** Definirea rezultatului înainte de alegerea interfeței.

**Files:**
- Create: `_meta/search/SEARCH-SPEC.md`

**Câmpuri obligatorii pentru fiecare rezultat:**

- `page_path`;
- `title`;
- `page_type`;
- `perimeter`;
- `instrument_id`, unde există;
- `article_locator`, unde există;
- `source_path`;
- `consolidation_date`;
- `in_force_state`;
- `hcc_state`;
- `confidence`;
- fragment de text;
- indicator `canonical_source: raw | structured`.

**Queries obligatorii:**

1. căutare textuală exactă;
2. căutare fără diacritice;
3. act + articol;
4. toate paginile despre o instituție;
5. dispoziții care nu se aplică azi;
6. dispoziții afectate de HCC;
7. acte care citează un act dat;
8. acte citate, dar nedisponibile;
9. filtre `legal/policy`, limbă, tip de pagină.

**Acceptance:** specificația interzice prezentarea unei sinteze drept text legal.

---

## Task 14: Index SQLite FTS5 derivat

**Objective:** Căutare rapidă fără schimbarea sursei canonice.

**Files:**
- Create: `_meta/search/build_search_index.py`
- Create: `_meta/search/schema.sql`
- Create: `_meta/search/query.py`
- Create: `tests/test_search_index.py`
- Modify: `.gitignore`
- Generated local: `.cache/wiki-search/wiki.db`

**Tables propuse:**

- `documents` — o intrare per fișier;
- `sections` — heading/anchor + corp;
- `sources` — metadate raw;
- `page_sources` — relația structured→raw;
- `provision_status` — proiecție din registrul in-force;
- `hcc_status` — proiecție din registrul HCC;
- `citations` — subset util din graful canonic;
- `sections_fts` — FTS5 peste titlu, heading și corp.

**Rules:**

- DB-ul nu se comite inițial;
- build-ul pornește de la zero într-un fișier temporar și îl înlocuiește atomic;
- niciun tabel nu este editat manual;
- fiecare rând păstrează calea sursă și locatorul;
- rezultatele raw au prioritate distinctă față de structured, nu scor comun nediferențiat.

**Verification:**

```bash
python _meta/search/build_search_index.py --output .cache/wiki-search/wiki.db
python _meta/search/query.py "piața criptoactivelor" --limit 10
python -m unittest tests.test_search_index -v
```

**Acceptance:** o reconstrucție repetată produce aceleași rânduri și aceleași legături pentru același commit.

---

## Task 15: CLI unificat de interogare

**Objective:** O interfață sigură pentru utilizator și agenți înaintea unui API web.

**Files:**
- Create: `_meta/search/wiki_query.py`
- Create: `tests/test_wiki_query.py`

**CLI propus:**

```bash
python _meta/search/wiki_query.py search "termen de conformare"
python _meta/search/wiki_query.py provision L-180-2026 85
python _meta/search/wiki_query.py citations L-548-1995
python _meta/search/wiki_query.py status L-325-2025
```

**Output:** JSON implicit pentru agenți, `--format table` pentru utilizatori.

**Safety:** răspunsul pentru o dispoziție include întotdeauna:

- calea raw;
- ancora/localizatorul;
- data consolidării;
- starea in-force;
- starea HCC;
- avertisment dacă sursa este traducere sau neancorată.

---

## Task 16: API read-only opțional

**Objective:** Expunerea contractului CLI către o interfață locală, fără acces de scriere.

**Prerequisite:** decizie explicită a lui Eugen după validarea CLI-ului.

**Files posibile:**
- Create: `app/api.py`
- Create: `app/models.py`
- Create: `tests/test_api.py`
- Modify: `pyproject.toml` cu extra `app`

**Endpoints minime:**

```text
GET /health
GET /search?q=&limit=&perimeter=
GET /pages/{slug}
GET /acts/{instrument_id}
GET /acts/{instrument_id}/articles/{article}
GET /acts/{instrument_id}/citations
GET /status/{instrument_id}/{locator}
```

**Non-goals:** fără `POST`, `PUT`, `PATCH`, `DELETE`; fără autentificare până când există un caz real de utilizare multiutilizator.

**Acceptance:** API-ul poate fi șters și reconstruit fără pierdere de cunoaștere; toate răspunsurile juridice au proveniență.

---

# Faza P4 — Interfață și operare extinsă, numai după validarea valorii

**Durată orientativă:** 5–10 zile, opțional.

## Task 17: Dashboard local read-only

**Objective:** Reducerea curbei de învățare pentru utilizatorii care nu lucrează direct în Obsidian.

**Views propuse:**

1. căutare unificată;
2. pagină de act cu versiune, statut, HCC și citări;
3. „Ce nu este încă în vigoare?”;
4. „Ce a fost declarat neconstituțional?”;
5. coada de ingerare;
6. acoperirea pe domenii și instituții;
7. avertismente și controale;
8. pagină de proveniență.

**UX rules:**

- culoarea nu este singurul indicator de statut;
- textul raw și sinteza au prezentări vizual diferite;
- orice citat are buton „deschide sursa și ancora”;
- consolidările viitoare poartă etichetă persistentă;
- Graphify este marcat „exploratoriu, posibil învechit”.

**Acceptance:** niciun ecran nu permite copierea unei concluzii fără a vedea sursa și statutul temporal.

---

## Task 18: Politica de prospețime pentru Graphify

**Objective:** Evitarea folosirii unui graf semantic vechi ca reprezentare a stării curente.

**Options to decide:**

- A. Graphify rămâne manual și UI-ul afișează commit/data corpusului;
- B. se rulează `graphify --update` după loturi majore, în afara `close_session.py`;
- C. se elimină din navigarea curentă și se generează numai la cerere.

**Recomandare:** A sau C. Nu introduceți Graphify în bariera juridică principală; are alt scop și alt model de adevăr decât graful canonic de citare.

**Acceptance:** utilizatorul poate vedea imediat dacă graful semantic corespunde commitului curent.

---

# Faza P5 — Pilot și închidere

## Task 19: Pilot end-to-end pe un lot mic

**Objective:** Validarea întregului lanț fără migrare masivă.

**Pilot recomandat:** 3 acte reprezentative:

- un act curent;
- un act cu versiune viitoare;
- un act abrogat sau cu dispoziție HCC.

**Flow:**

1. registru declarativ;
2. ingerare/verify într-un director temporar;
3. pagină structurată;
4. controale incrementale;
5. build complet;
6. index SQLite;
7. query CLI;
8. comparație cu rezultatul manual din Obsidian.

**Acceptance:** aceeași sursă, același locator, aceeași stare juridică și aceleași relații în toate interfețele.

---

## Task 20: Documentare, validare și închiderea sesiunii

**Objective:** Lăsarea proiectului într-o stare reluabilă și verificată.

**Files:**
- Update: `README.md`
- Update minimal: `CLAUDE.md`
- Update: `log.md` cu `Aflat / Decis / Unde`
- Update: documentele stabile create în fazele anterioare

**Steps:**

1. Rulați testele:

```bash
python -m unittest discover -s tests -v
```

2. Rulați build-ul complet, nu doar incremental:

```bash
python _meta/close_session.py --check
```

3. Construiți indexul din zero și rulați smoke tests.
4. Verificați `git diff --check` și `git status --short`.
5. Confirmați că nicio sursă raw nu a fost modificată accidental.
6. Scrieți intrarea în `log.md` numai pentru ce s-a aflat și decis, nu ca duplicat al diff-ului.
7. Numai cu autorizarea lui Eugen, folosiți:

```bash
python _meta/close_session.py --commit "Consolidarea instrumentelor și scalarea wiki-juridic"
```

**Acceptance:** teste verzi, controale verzi, zero diferențe raw neautorizate, documentație și ownership clare.

---

# 4. Ordinea de execuție și dependențe

```text
Task 0
  ├─ Task 1 ─ Task 2
  ├─ Task 3
  ├─ Task 4 (necesită text de la Eugen)
  └─ Task 5
       ↓
Task 6 ─ Task 7 ─ Task 8 ─ Task 9
       ↓
Task 10 ─ Task 11 ─ Task 12
       ↓
Task 13 ─ Task 14 ─ Task 15
       ↓
Task 16? ─ Task 17? ─ Task 18
       ↓
Task 19 ─ Task 20
```

Semnul `?` înseamnă poartă de decizie: nu se implementează automat.

# 5. Milestones și criterii de oprire

## M0 — Baseline verde

- toate testele trec;
- CI rulează testele;
- data hardcodată este eliminată;
- dependențele sunt declarate;
- avertismentele sunt rezolvate sau documentate ca blocaje externe.

**Stop dacă:** lotul juridic curent nu poate fi izolat sau matter log-ul necesar nu este furnizat.

## M1 — Tooling consolidat

- frontmatter și hashuri comune;
- fixture-uri pentru cazurile dificile;
- registru declarativ verificat prin paritate;
- zero schimbări semantice neintenționate în artefactele generate.

**Stop dacă:** paritatea cu pipeline-ul existent nu poate fi demonstrată act-cu-act.

## M2 — Scalare operațională

- benchmark repetabil;
- control incremental local;
- full build obligatoriu în CI;
- model de colaborare documentat.

**Stop dacă:** incremental și full build produc output diferit.

## M3 — Căutare

- SQLite reconstruit din zero;
- CLI returnează proveniență și statut;
- testele diferențiază raw de structured.

**Stop dacă:** un rezultat juridic poate apărea fără sursă, locator sau stare temporală.

## M4 — Produs opțional

- API/UI read-only;
- test de utilizare;
- nicio cale de scriere în corpus.

**Stop dacă:** cererea reală poate fi satisfăcută suficient prin Obsidian + CLI; evitați un frontend fără utilizatori.

# 6. Praguri recomandate pentru următoarea etapă de scalare

- Dacă full check depășește 2 minute local sau 5 minute în CI: prioritizați cache-ul incremental și profilarea grafului.
- Dacă `citation-graph.json` depășește 50 MB: evaluați sharding-ul derivat sau stocarea SQLite, păstrând un raport Markdown compact.
- Dacă există mai mult de 2 editori/agenți simultan: worktree și ownership devin obligatorii.
- Dacă corpusul depășește aproximativ 3.000 de surse raw: indexul SQLite devine componentă standard de lucru.
- Dacă se cere acces pentru utilizatori non-tehnici: implementați mai întâi CLI/API read-only, apoi UI.
- Dacă se cere scriere multiutilizator: tratați-o ca proiect separat de guvernanță și securitate, nu ca extensie minoră.

# 7. Riscuri și măsuri

| Risc | Măsură |
|---|---|
| Refactorul modifică artefacte juridice | comparație byte-for-byte înainte/după și build complet |
| Cache-ul ascunde o schimbare | CI fără cache, invalidare fail-closed |
| YAML-ul actelor diverge de pipeline | perioadă de paritate și test de acoperire 100% |
| SQLite devine sursă paralelă | DB ignorat, reconstrucție integrală, fără editare manuală |
| UI ascunde incertitudinea | sursă, locator, in-force și HCC obligatorii în contract |
| Cloudflare blochează actualizarea | cache verificat + intervenție umană documentată; fără bypass nesigur |
| Mai mulți agenți suprascriu fișiere | worktree, ownership și integrare serializată |
| Regulile temporale devin stale | `--as-of`, teste pe limite de dată, fără constante calendaristice |
| Extinderea devine prea mare | porți M0–M4; API/UI sunt opționale și pot fi oprite |

# 8. Întrebări care necesită decizia lui Eugen

1. Lotul juridic necomis existent se finalizează înaintea programului sau programul pornește într-un worktree separat?
2. Se dorește doar consolidarea internă P0–P2 sau și produsul de căutare P3–P4?
3. Graphify rămâne disponibil manual, se actualizează periodic sau se scoate din navigarea curentă?
4. Indexul SQLite va fi strict local sau trebuie distribuit ca artefact de release?
5. Există utilizatori non-tehnici concreți pentru dashboard sau interfața poate rămâne Obsidian + CLI?
6. Care este politica de commit: un commit per fază, per task sau un singur commit verificat la final? Recomandare: per fază, numai cu aprobare explicită.
7. Matter log-ul curent poate fi furnizat înaintea Task 4?

# 9. Recomandarea de start

Executați mai întâi numai **P0**. După ce testele, CI-ul, data temporală și mediul reproductibil sunt rezolvate, reevaluați costul și beneficiul P1. Nu începeți SQLite, API sau dashboard înainte ca M0 și M1 să fie închise.
