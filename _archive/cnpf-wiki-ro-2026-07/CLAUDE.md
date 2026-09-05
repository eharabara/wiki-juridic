# Wiki Legislație CNPF — Schemă și reguli de operare

O bază de cunoștințe întreținută de un LLM (tiparul „LLM Wiki" al lui Karpathy),
delimitată la legislația aflată sub mandatul **Comisiei Naționale a Pieței
Financiare (CNPF)** a Republicii Moldova, adaptată pentru validitatea sursei juridice.

## Arhitectură (trei straturi)

- `raw/`   Surse primare imuabile. Nu se editează niciodată de către agent. Texte de
           lege consolidate (de pe legis.md), texte de acquis UE (EUR-Lex), acte
           normative CNPF. Numele fișierului = ID scurt (ex. `L-171-2012.md`).
           `_manifest.md` le listează pe toate și indică autoritatea de mandat.
- `wiki/`  Pagini de entitate/concept generate de agent, interconectate. Câte o pagină
           pentru fiecare lege, fiecare directivă/regulament UE și fiecare concept transversal.
- `CLAUDE.md`  Acest fișier. Schema, șabloanele de pagină și cele trei operațiuni.

## Cele trei operațiuni

- **ingest** (ingestie) — Adaugă o sursă în `raw/`, adaugă un rând în manifest, apoi
  creează/actualizează pagina/paginile `wiki/` și fiecare pagină care o referențiază.
- **query** (interogare) — Răspunde întâi din `wiki/`; coboară la `raw/` doar pentru a verifica o ancoră.
- **lint** (verificare) — Rulează verificările de mai jos și scrie constatările în
  `wiki/_lint-report.md`. Nu se corectează niciodată în tăcere o contradicție juridică — se semnalează.

## Reguli juridice nenegociabile (au prioritate față de concizie sau fluență)

1. **Ancorare la sursa primară.** Fiecare afirmație juridică de pe o pagină wiki trebuie
   să poarte o ancoră la nivel de articol către un fișier `raw/`, ex. `[L-171-2012 art.6]`.
   O afirmație fără ancoră se șterge sau se mută într-un bloc `## Întrebări deschise`.
2. **Fără concluzii juridice sintetizate.** Wiki-ul consemnează ce spun sursele, cu citare.
   Nu opinează asupra modului în care ar decide o instanță.
3. **Urmărirea abrogărilor/succesiunii.** Când o sursă e modificată sau abrogată, marchează
   versiunea veche `ÎNLOCUITĂ de [X] de la data [dată]` — nu șterge niciodată consemnarea.
4. **Marcarea autorității de mandat.** Fiecare pagină de lege poartă câmpul `mandat:`
   (`CNPF` | `BNM` | `CNPF-rezidual` | `partajat` | `de verificat`). Preluarea de către BNM
   la 1 iulie 2023 a supravegherii asigurărilor/OCN/AEÎ/birourilor de credit înseamnă că
   multe surse sunt `BNM` din perspectivă prudențială, dar `CNPF-rezidual` pentru protecția consumatorilor.
5. **Legătura cu acquis-ul.** Când un act moldovenesc transpune legislație UE, leagă la pagina
   directivei/regulamentului și consemnează statutul transpunerii
   (`complet` | `parțial` | `planificat` | `necunoscut`).
6. **Marcaje de încredere.** Orice citare neverificată față de legis.md sau EUR-Lex se
   marchează `[de verificat]`. Nu transforma niciodată un `[de verificat]` într-un fapt stabilit.

## Șablon de pagină — o lege

```
# [ID] — [Titlu oficial]

- **mandat:** CNPF | BNM | CNPF-rezidual | partajat | de verificat
- **statut:** în vigoare | modificată | abrogată  (data versiunii consolidate)
- **referință MO:** Monitorul Oficial nr./an
- **domeniu:** piața de capital | asigurări | creditare nebancară | AEÎ | birou de credit | AML | transversal
- **acquis transpus:** [[pagini directive]] — statut
- **surse:** [raw/ID] (+ ancore de articol folosite mai jos)

## Scop (1–2 fraze, ancorate)
## Registre-cheie / entități supravegheate
## Acte normative subordonate (decizii CNPF/BNM emise în temeiul legii)
## Referințe încrucișate  [[alte pagini de lege]]
## Contradicții / întrebări deschise   ← aici scrie lint
## Jurnal de modificări (amendamente, abrogări)
```

## Verificări lint (specifice juridic)

- **Afirmații orfane** — orice frază fără o ancoră `raw/`.
- **Conflicte de mandat** — o pagină marcată `CNPF` a cărei sursă a trecut la BNM în 2023.
- **Consolidare învechită** — data versiunii `raw/` mai veche decât ultimul amendament
  consemnat pe pagina wiki.
- **Lacune de transpunere** — o pagină de acquis UE fără o măsură moldovenească legată,
  sau statut `planificat` depășind termenul din Acordul de Asociere.
- **Referințe încrucișate rupte** — legături `[[...]]` fără pagină-țintă.

## Instrumente recomandate

- **Obsidian** pentru stratul de fișiere/graf; **Claude Code** ca agent.
- **QMD** (Lütke) ca strat de căutare/regăsire — CLI + server MCP, astfel încât agentul
  să poată naviga un wiki mare fără a încărca totul în context.
