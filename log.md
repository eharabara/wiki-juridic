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

## [2026-09-05] update | punctul deschis 3: legăturile EMIR din `raw/` rămân neatinse

- **Aflat:** Obsidian rezolvă wikilink-urile după numele fișierului, oriunde în vault, deci cele cinci legături din manifestul CNPF și din nota scheletului DOCX funcționează după mutare fără nicio editare. Alegerea era doar de principiu.
- **Decis:** Eugen a acceptat varianta strictă: `raw/` rămâne imuabil fără excepții, redirecționarea e declarată în `_PROVENANCE.md`, iar verificatorul primește excepția din tabelul de acolo.
- **Unde:** `_archive/emir-2026-07/_PROVENANCE.md`, secțiunea „Ce trimite încă la ele din raw/”.

## [2026-09-05] update | P4: câmpul `perimeter` pe cele 82 de pagini

- **Aflat:** clasificarea iese mecanic din surse: paginile ancorate în `raw/papers/cnpf`, `moldova-legal` sau `bnm` sunt juridice, cele din `moldova-policy` sau `mded-policy-2024` sunt de politici. Un singur caz mixt, `L-845-1992`, care citează și planul de reglementări 2025; e act primar, deci juridic. Rezultat: 64 `legal`, 18 `policy`. Cele cinci pagini EMIR arhivate nu primesc câmpul, sunt înghețate.
- **Decis:** câmpul se inserează imediat după `type:`. `updated` nu se ridică, pentru că nu s-a schimbat conținut, doar metadate, și git ține schimbarea. Dovada: pentru fiecare pagină, corpul de după frontmatter e identic byte cu byte, iar frontmatter-ul diferă exact printr-o linie.
- **Unde:** commit-ul P4; regula intră în `_meta/schema/schema-spec.yaml` la P5.

## [2026-09-05] create | P5: specificația mecanică, generatorul pentru `SCHEMA.md`, verificatorul

- **Aflat:** starea de bază era mai curată decât se bănuia: zero legături nerezolvate, zero surse lipsă, indexul complet, toate cele 396 de hash-uri din `raw/` reproduse (345 pe convenția LF, 51 pe octeți bruți). Două erori vechi, ambele mecanice: un al doilea folder parazit `C:\Users\harab\wiki` în `_meta/imports/moldova-legal/`, pe care planul nu l-a văzut, și eticheta `civil-code` pe `CC-1107-2002`, folosită fără să fie în taxonomie. Două lacune cunoscute rămân avertismente: 305 fișiere BNM cu `language: other` (ingestul din iulie n-a detectat limba) și 28 de traduceri BNM nedeclarate, identificate după liniile `Article N` din corp, pentru că limba nu ajută. Numele de bază ale actelor sunt ambigue în vault (entitate, sursă brută, copii arhivate), deci regula de rezolvare a wikilink-urilor a trebuit fixată: structurat, apoi brut, apoi rădăcină; arhiva și `_meta` doar prin cale explicită.
- **Decis:** Eugen: folderul parazit se șterge, eticheta `civil-code` se scoate (pagina rămâne pe `legal-act`), traducerile rămân avertisment până la P9. Specificația e în YAML citit de ambele scripturi, ca `SCHEMA.md` să nu poată spune altceva decât verifică verificatorul. `SCHEMA.md` rămâne în engleză, ca și `CLAUDE.md`; specificația, jurnalul și notele de proveniență sunt în română.
- **Unde:** `_meta/schema/schema-spec.yaml`, `build_schema.py`, `validate_wiki.py`; raport `_meta/lint/validate-2026-09-05.md`; `SCHEMA.md` secțiunea „Mechanical rules”, generată între marcaje.

## [2026-09-05] update | P6: jurnalul ca index și regulile noi în `CLAUDE.md`

- **Aflat:** forma D8 a fost aplicată deja de la P0, deci P6 a însemnat numai să o consemneze ca regulă și să lege `CLAUDE.md` de ea. Verificatorul o impune: antet cu dată și acțiune, cele trei rânduri în ordine.
- **Decis:** `CLAUDE.md` primește regula perimetrelor, regula jurnalului, rularea verificatorului, harta folderelor noi, întrebarea deschisă 5 marcată ca decisă prin D2, și un rând în lucrările deschise pentru P2, P7, P8, P9. `README.md` pentru GitHub se scrie la P2, când Eugen numește depozitul.
- **Unde:** `CLAUDE.md`, secțiunile „Where things are”, „Open questions” pct. 5, „Outstanding work” pct. 5, „Keeping this file true”, „Writing to the wiki”.

## [2026-09-05] create | P2: depozit privat pe GitHub, `wiki-juridic`

- **Aflat:** `gh` era deja autentificat pe contul `eharabara`, cu drepturi `repo`. Niciun fișier urmărit nu trece de 5 MB, deci nu e nevoie de Git LFS.
- **Decis:** Eugen a numit depozitul `wiki-juridic` și a confirmat că e privat. Originalele (576 MB) nu se urcă; rămân doar pe disc, singura parte fără copie în afara mașinii, redescărcabile de la sursă. `README.md` scris pentru GitHub, în română, fără wikilink-uri.
- **Unde:** `README.md`; telecomanda `origin`; commit-urile de la `12e819d` încolo.

## [2026-09-05] update | P7: ștampile de proveniență pe copiile din `legal-career/`

- **Aflat:** copiile aveau deja o notă de copiere în proză, dar nimic nu putea spune dacă fuseseră editate local după copiere; 03 și 05 au fost modificate după ora copierii, cu note locale declarate în antet, și nimic nu le distingea de o editare tăcută. Registrul de spețe local, 06, nu are nicio speță, deși planul (secțiunea 8) vorbește de M-001 în proiect: copia e deja în urma masterului. Documentul 05 poartă la rândul 69 constatări depășite (art. 21 din L-192-1998 e prezent, numărul de fișiere BNM englezești e 87, nu 89); e treabă de reîmprospătare din proiect, nu de editare aici.
- **Decis:** ștampila e frontmatter verificabil: `copy_of`, `master`, `taken`, `stamped`, `sha256_body` (LF), `local_notes`, `refresh`. Corpul fiecărei copii a rămas byte cu byte cel dinainte, dovedit la ștampilare. Verificatorul dă eroare la orice editare locală și avertisment cât timp registrul de spețe (`refresh: every-session`) nu e luat azi din proiect. Reîmprospătarea registrului nu se poate face de aici: proiectul claude.ai nu e accesibil din acest folder, deci Eugen aduce textul.
- **Unde:** `legal-career/*.md` frontmatter; `_meta/schema/schema-spec.yaml` secțiunea `copies`; `_meta/schema/stamp_copies.py`; `CLAUDE.md` „Read this first”; `SCHEMA.md` „Copies in legal-career/”.

## [2026-09-05] decision | M-001: punctul deschis privind Codul contravențional s-a închis; copia registrului rămâne

- **Aflat:** copia locală a registrului de spețe (`legal-career/06-matter-log.md`, luată 2026-09-04) nu conține nicio speță, în timp ce masterul din proiectul claude.ai are M-001. Punctul deschis din M-001, care depindea de Codul contravențional, s-a închis între timp: `COD-218-2008` este ingerat și ancorat de la 2026-09-04 (737 de ancore, consolidare 2026-09-13, deci text cu dată viitoare, de verificat în `_meta/inforce/in-force-register.md` înainte de citare). Ce spune exact M-001 nu se vede de aici; poziția rămâne cea din proiect și nu se re-argumentează în acest folder.
- **Decis:** Eugen: închiderea se notează aici, în jurnal; copia registrului nu se reîmprospătează acum și rămâne la starea din 2026-09-04. Actualizarea lui M-001 se face în proiect, unde e masterul (planul, secțiunea 8). Consecința mecanică: verificatorul continuă să dea avertismentul `copy.stale` pe registru până la prima sesiune în care textul din proiect e adus și re-ștampilat.
- **Unde:** `legal-career/06-matter-log.md`, neschimbat; `entities/COD-218-2008.md`; `raw/papers/moldova-legal/COD-218-2008.md`.

## [2026-09-05] ingest | P8: cele șase legi bancare în română, `raw/papers/bnm/legal-ro/`

- **Aflat:** legis.md a pus după-amiază o verificare Cloudflare pe toate endpoint-urile, care blochează `curl` și ține browserul aplicației în buclă; a trecut doar în Chrome-ul lui Eugen, după bifa lui, iar Chrome a mai cerut o dată permisiunea de descărcări multiple. HTML-ul de probă e DOM serializat de browser, nu octeții serverului, cu `<sup>` și `#contentdoc` intacte. Legea 575/2003 e abrogată pe legis.md; actul curent e Legea 160/2023, care transpune parțial DGSD. `L-548-1995` are șapte articole lipsă fără niciun marcaj în sursă (12, 13, 29, 30, 48, 54, 73), aceeași clasă ca lacunele din Codul muncii; legea a fost republicată în 2015, ceea ce poate explica, dar textul nu o spune. `L-114-2012` vine cu consolidare viitoare, 2027-01-01, o singură dispoziție afectată. Art. 11 din 548/1995 derogă expres de la art. 44 din Codul administrativ și fixează cererea prealabilă exclusiv la Comitetul executiv al BNM: se citește înaintea codului, nu după. Art. 36 alin. (2) din 202/2017 e lista limitativă a excepțiilor de la Legea SA. Generatorul de acoperire nu știa de folderul nou și ar fi numărat cele șase legi drept corpus englezesc.
- **Decis:** Eugen: se ingerează 160/2023 în locul lui 575/2003; descărcarea din Chrome confirmată. Folder nou `bnm/legal-ro/`, conform D3, cu înveliș peste scriptul de la moldova-legal, nu o copie a lui; verificatorul de ingerare generat din cel existent cu trei înlocuiri, ca să nu diveargă. Titlul din fișă adus pe un rând ca metadată, textul legal neatins, integritate PASS pe toate șase. Lacunele din 548/1995 nu se corectează: întrebarea deschisă 6 în CLAUDE.md. Generatorul de acoperire învățat că `legal-ro` sunt acte primare. Ordinea generatoarelor contează: registrul de intrare în vigoare înaintea acoperirii, altfel acoperirea rămâne în urmă.
- **Unde:** `raw/papers/bnm/legal-ro/` cu `_manifest.md`; `_meta/imports/bnm/ingest_bnm_ro.py`, `verify_bnm_ro.py`, `legis-md-ro/`; `entities/L-202-2017.md`, `L-548-1995.md`, `L-114-2012.md`, `L-232-2016.md`, `L-62-2008.md`, `L-160-2023.md`; `entities/bnm.md`; `index.md` (88 de pagini); `CLAUDE.md` întrebarea deschisă 6 și lucrările deschise pct. 5; `_meta/coverage/build_coverage.py`.

## [2026-09-05] archive | P9: traducerile engleze BNM retrase; ancorele scoase de pe cele rămase

- **Aflat:** cele 26 de traduceri engleze de legi din corpusul BNM **erau ancorate** de ieri, cu `## Article N.`, de `anchor_bnm_en.py`; generatorul de acoperire și verificatorul căutau doar `## Articolul` și le raportau „neancorate”, fals în ambele sensuri, și contrar deciziei D2. 22 dintre ele au text românesc în vault, zece încă din iulie, în `cnpf/`. Cinci nu au: 250/2017, 550/1995, 239/2008. Fișierele BNM au terminatori CRLF, iar prima mea reconstrucție a antetului a dublat `\r`; corpul nu a fost atins, dovada față de `sha256_pre_anchoring` a trecut la fiecare pas, iar antetul a fost refăcut de la zero cu punctul de tăiere ales prin hash.
- **Decis:** Eugen: grupa A se mută, cu originalele, în `_archive/bnm-en-2026-09/`; grupa B rămâne, de-ancorată și declarată `translation`, iar ingerarea celor trei acte în română e lucrare deschisă, P8-bis. Manifestele BNM nu se editează; redirecționarea e declarată în `_PROVENANCE.md`. Regula: `## Article` e ancoră pe traducere, interzisă de D2, în specificație, `SCHEMA.md`, verificator și generatorul de acoperire.
- **Unde:** `_archive/bnm-en-2026-09/_PROVENANCE.md`; `raw/papers/bnm/legal/documents/` (182 de fișiere, 5 cu `source_type: translation`); `_meta/schema/schema-spec.yaml` `translation.anchor_pattern`; `_meta/coverage/build_coverage.py`; `entities/bnm-official-document-corpus-2026.md`; `entities/bnm.md`; `CLAUDE.md` întrebarea 5 și lucrările deschise pct. 5.

## [2026-09-05] ingest | P8-bis: 550/1995, 250/2017 și 239/2008 în română

- **Aflat:** verificarea Cloudflare expiră între sesiuni: la prima navigare a cerut din nou bifa lui Eugen, deci fiecare sesiune care atinge legis.md o va cere o dată. Legea 550/1995 e pe legis.md sub denumirea actuală „cu privire la lichidarea băncilor”, cu cea precedentă „instituțiilor financiare”, și a rămas cu **3 articole de bază și 17 cu exponent** (38^1–38^17), capitolele I–VI fiind abrogate și materia preluată de 202/2017; traducerea engleză din corpusul BNM, cu 115 articole, e versiunea de dinainte de golire, deci o citare din ea poate fi corectă istoric și goală azi. Nota din capul legii spune că „Legea 575/2003” se citește „Legea 160/2023”, confirmând înlocuirea de la P8. 250/2017 e singurul act din corpus care pune BNM și CNPF sub același regim, deci pentru harta de mandat e act de intersecție. Browserul numărase zero linii „Articolul” în 250/2017; extractorul a găsit 23: numărarea din `innerText` nu e un control, controlul e `--precheck`.
- **Decis:** cele trei intră în `bnm/legal-ro/` cu aceeași metodă; 239/2008 stă acolo doar pentru că BNM o ține în registrul său și traducerea ei era în corpusul BNM, iar pagina spune asta. Cele cinci traduceri engleze rămase în `bnm/legal/documents/` se mută în `_archive/bnm-en-2026-09/` după ce Eugen confirmă lista.
- **Unde:** `raw/papers/bnm/legal-ro/L-550-1995.md`, `L-250-2017.md`, `L-239-2008.md`; `_manifest.md` de acolo, secțiunea „P8-bis”; `entities/` cu aceleași nume; `index.md` (91 de pagini); `CLAUDE.md` „Where things are”, întrebarea 5, lucrările deschise pct. 5.

## [2026-09-05] archive | P8-bis, încheiere: ultimele cinci traduceri engleze de legi mutate în arhivă

- **Aflat:** după mutare, `raw/papers/bnm/legal/documents/` nu mai conține nicio lege în engleză, doar regulamente, hotărâri și documente ale BNM; avertismentul „BNM English corpus” din acoperire numără de acum doar acte secundare cu marcaje `Article N`, nu legi.
- **Decis:** Eugen a confirmat lista. Cele cinci merg în `_archive/bnm-en-2026-09/` fără ancore, cu hash-ul de dinainte de ancorare, spre deosebire de grupa A; nota de proveniență ține cele două grupe separat, cu data și starea fiecăreia.
- **Unde:** `_archive/bnm-en-2026-09/_PROVENANCE.md`, secțiunea „Grupa B, mutată aici la P8-bis”; `entities/bnm-official-document-corpus-2026.md`; `raw/papers/bnm/legal-ro/_manifest.md`.

## [2026-09-05] decision | Sesiunea de restructurare s-a încheiat

- **Aflat:** planul din 5 septembrie e executat integral, P0 până la P9, plus P8-bis pe care l-a deschis P9; ultimul commit `5683961`, `origin/main` identic, verificatorul cu zero erori pe 91 de pagini și 378 de surse. Următoarea lacună reală, în afara planului: regulamentele BNM sunt tot în engleză, 60 de fișiere cu marcaje `Article N`, deci o obligație concretă dintr-un regulament rămâne parțial ancorată.
- **Decis:** Eugen închide sesiunea. Rămân la judecata lui, nerezolvate aici: lacunele fără marcaj din 548/1995 (întrebarea deschisă 6), legile de interpretare neingerate pentru 202/2017 și 232/2016, regulamentul UE în engleză din perimetrul de politici pe care regula de traducere îl marchează greșit, reîmprospătarea registrului de spețe din proiect, cele trei actualizări din proiectul claude.ai (secțiunea 8 a planului).
- **Unde:** `CLAUDE.md`, „Open questions” și „Outstanding work”; `_meta/lint/validate-2026-09-05.md`; acest jurnal, de la prima intrare a zilei.
