# Plan de lucru — remedierea auditului din 2026-09-26

Sursa: `_meta/lint/audit-2026-09-26-full.md` (constatările A1–A7). Ordinea merge de la ce nu cere
nimic din afară la ce cere descărcări și judecata lui Eugen. Fiecare etapă se închide cu
`python _meta/close_session.py` (fără `--commit`); commit doar la cerere.

## Etapa 0 — Pornire (5 min)

- D9: Eugen aduce registrul curent din proiectul „Legal Wiki”; se înlocuiește corpul
  `legal-career/06-matter-log.md`, apoi `python _meta/schema/stamp_copies.py`. (A7)
- `git status` curat înainte de orice scriere.

## Etapa 1 — Pagini de entitate rămase la versiunea veche (A2), fără descărcări

Pentru fiecare pagină: deschid fișierul raw, citesc frontmatter-ul și antetul corpului, corectez
**doar** linia de statut și ce depinde de ea. Nu se atinge `raw/`.

| pagină | ce se corectează |
|---|---|
| `entities/L-1134-1997.md` | doc_id 154811, consolidarea 2028-01-01 numită ca viitoare; art. 73^3, 73^4 (LP92/2026) neintrate în vigoare, trimitere la registrul in-force; ce text se aplică azi |
| `entities/L-192-1998.md` | doc_id 150996, consolidarea 2026-01-01; se verifică dacă restul paginii mai ține pe textul nou |
| `entities/L-100-2017.md` | doc_id 153007, consolidarea 2025-12-31, ultima modificare din antetul corpului |

Verificare: rerulez scriptul de audit (doc_id anterior fără cel curent) — trebuie 0 rânduri.
Plus o trecere pe toate entitățile după același tipar (statut cu dată de extragere din iulie/august).

## Etapa 2 — Text scris de mână rămas în urmă (A6), fără descărcări

- `CLAUDE.md`, intrarea `_meta/lint/`: numerele „4 orphan / ~149” înlocuite cu starea reală (0 din
  2026-09-17, commit 26af056).
- `CLAUDE.md`, „Where things are”: un rând pentru perimetrul actelor permisive
  (`concepts/perimetrul-actelor-permisive.md`, manifest AV) și unul pentru `viitor/` (AX).
- Manifestul moldova-legal, secțiunea AV: nota „consolidările viitoare (23) neingerate” marcată ca
  închisă prin AX (adăugare datată, nu rescriere).

## Etapa 3 — Reingerarea celor trei acte din commit-ul 24c0918 (A1) — cere acordul lui Eugen

1. Pe legis.md, pentru `COD-1316-2000`, `L-69-2016`, `L-230-2022`: fișa, lista de versiuni, cea mai
   nouă consolidare care nu e în viitor, `Data abrogării` și antetul corpului (memoria
   „check repeal before ingesting”). Rezultatul poate schimba doc_id-ul (122974, 125333, 133204).
2. Descărcare: întreb Eugen per fișier (nume, sursă, mărime). Ruta: curl cu Referer/X-Requested-With;
   dacă nu merge, Chrome-ul lui Eugen.
3. Backup în `wiki-backups/wiki-2026-09-26-reingerare-3-acte/`.
4. `ingest_business_law.py` cu cele trei intrări noi, apoi `verify_business_law.py` — 0 eșecuri;
   `fix_wrapped_titles.py` dacă e cazul, cu dovada strip-and-compare.
5. Numărul de ancore egal cu numărul de articole declarat; `consolidation_date` prezentă.
6. Paginile de entitate și rândurile din manifest (247–249) aduse la noua versiune.
7. Regenerare graf: cele 16 grupuri nerezolvate ale `L-230-2022` trebuie să dispară.

## Etapa 4 — O regulă de validator pentru articole neancorate (lacuna de unelte din A1)

- Regula nouă `raw.unanchored-article-heading`: un rând care începe cu `Articolul N.` /
  `**Articolul N.**` / `Art.N.` fără ancoră `##` deasupra, în actele cu `source_type: legal-text`.
- Excepții cunoscute, măsurate înainte să fie scrise: legile modificatoare cu articole romane
  (`L-133-2018`, `L-66-2017`, `L-227-2025` — textul nou al altor acte), `DCU-REGULI-2026`
  (ancore sintetice deasupra rândului), `COD-1163-1997` și versiunea din `viitor/` (5 rânduri în plus
  de explicat), `COD-150-2014` (5 rânduri `Art. 31^N.`), `COD-95-2021` (5, text explicativ).
- Nivel: avertisment. Specificația în `schema-spec.yaml`, apoi `build_schema.py`.
- Proba: pe arborele de dinainte de etapa 3 regula trebuie să prindă exact cele trei acte.

## Etapa 5 — Grupurile nerezolvate noi din graf (A5)

Cele circa 19 grupuri rămase în afara clusterelor cunoscute (`CC-1107-2002`, `AA-2014`) și a
artefactelor `L-230-2022`: pentru fiecare, deschid ambele capete și compar titlurile (exponent
turtit, cifră ridicată, renumerotare, abrogare, act greșit atribuit). Rezultatul se scrie în
CLAUDE.md, întrebarea 8, cu aceeași rigoare ca pe 16–19 septembrie.

## Etapa 6 — Decizii pentru Eugen (A3, A4)

- **Manifestul:** rânduri per act pentru cele 54 + `viitor/`, generate mecanic din frontmatter
  (propunere: un tabel generat, nu scris de mână), sau rămâne descrierea pe lot.
- **Cele 54 de pagini mecanice:** care se citesc integral și în ce ordine (propunere: după coada
  de ingerare / numărul de citări din graf, sau după dosarele din registru).

## Închidere

Intrare în `log.md` (Aflat / Decis / Unde), `python _meta/close_session.py`, `git status` și
`git diff --stat` citite, apoi commit și push doar la cererea lui Eugen.

## Estimare

Etapele 0–2: o sesiune scurtă. Etapa 3: depinde de Cloudflare. Etapele 4–5: câte o sesiune.
Etapa 6: o discuție.

## Stare la 2026-09-26, seara

Etapele 0-5 făcute, etapa 3 după ce Eugen a trecut bifa Cloudflare. Etapa 6: registrul act cu act generat; rămîne citirea integrală a celor 54 de pagini mecanice (coada în `_meta/coverage/act-register.md`). Detalii: `_meta/lint/audit-2026-09-26-full.md`, secțiunea C, și `log.md`.
