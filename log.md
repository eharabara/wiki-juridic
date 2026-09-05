# Jurnal

> Git înregistrează ce s-a schimbat. Jurnalul înregistrează ce s-a aflat și ce s-a decis.
> Decizia D8 din `_meta/plans/2026-09-05-plan-restructurare-wiki.md`.
>
> O intrare pe acțiune, cu trei rânduri fixe: **Aflat** (constatarea care nu se vede din diff),
> **Decis** (alegerea făcută și de cine) și **Unde** (commit, fișier, secțiune de manifest).
> Ce se vede din `git log` și `git diff` nu se repetă aici.
>
> Jurnalul de dinainte, 2026-07-08 până la 2026-09-05, 1471 de rânduri, este în
> `_meta/log/2026-07-08.md`. Nu se mai scrie în el.

## [2026-09-05] create | P0: copie de rezervă, git local, prima înregistrare

- **Aflat:** vault-ul are 1159 de fișiere, 689 MB, din care 576 MB în folderele `original/`. Git ține 120 MB în 826 de fișiere, nu 78,5 MB cum estima planul, pentru că `_meta/imports/` (instantanee HTML de pe legis.md) și `raw/assets/` (PDF) sunt probe de ingerare, nu originale, și au rămas înăuntru. Nimic peste 50 MB. `python3` nu există pe sistem, doar `python` 3.14.
- **Decis:** Eugen a confirmat trecerea la P1 după ce a văzut cele trei abateri. Copiile Obsidian de setări rămân în git, doar `workspace*.json` iese.
- **Unde:** commit `12e819d`; copie confirmată prin sha256 în `C:\Users\harab\wiki-backups\wiki-2026-09-05-restructurare\`.

## [2026-09-05] archive | P1: răspunsul pentru speța acționarului la bancă iese din vault

- **Aflat:** folderul de dosare `Desktop\Justitiarul Path` are două dosare, `balta marin` și `sabina`, niciunul al acestei spețe.
- **Decis:** fișierul merge în rădăcina folderului de dosare, sub același nume; Eugen îl mută în dosarul potrivit. Hash identic înainte și după mutare.
- **Unde:** `C:\Users\harab\Desktop\Justitiarul Path\2026-09-04-raspuns-scurt-drepturi-actionar-banca.md`.

## [2026-09-05] archive | P3: paginile EMIR, jurnalul vechi, folderele goale, calea ruptă

- **Aflat:** paginile EMIR erau citate în mai multe locuri decât spunea planul: 11 locuri în `emir-concordance-skeleton`, 7 în `acquis-CSDR-EMIR`, cinci intrări în `index.md`, trei rânduri în manifestul CNPF și două în nota scheletului DOCX. Rapoartele de lint din `_meta/lint/` le citează și ele, ca ieșiri istorice. Folderul parazit din rădăcină avea numele `C:\Users\harab\wiki` cu `:` și `\` înlocuite de MSYS prin U+F03A și U+F05C, deci arăta ca o cale reală în Explorer. Jurnalul vechi începe la 2026-07-08, nu la 2026-07-09 cum spunea planul, așa că arhiva poartă data reală.
- **Decis:** Eugen a confirmat lista exactă de mutări și ștergeri. Wikilink-urile din stratul structurat trimit explicit la `_archive/emir-2026-07/`, cu alias, ca textul să se citească la fel. Rapoartele de lint nu se editează. `queries/` rămâne ca folder gol, cu `.gitkeep`. Cele două fișiere din `raw/` cu legături EMIR: punct deschis 3, în așteptarea răspunsului.
- **Unde:** `_archive/emir-2026-07/_PROVENANCE.md`; `_meta/log/2026-07-08.md`; `entities/bnm.md` (trei căi corectate spre `raw/papers/bnm/legal/documents/`).
