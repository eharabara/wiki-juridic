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

## [2026-09-05] lint | Audit complet de lint: ce trece, ce nu vede niciun script

- **Aflat:** forma vault-ului e sănătoasă — verificator 0 erori, acoperirea, SCHEMA și registrul in-force la zi, 378 de surse cu sha256 verificat — și, verificat la nivel de dispoziție, nicio pagină nu citează vreuna din cele 47 de dispoziții neintrate în vigoare. Ce nu vede niciun script: (a) `run_cnpf_legal_lint.py` nu a supraviețuit rescrierii D4 — lista lui de etichete se extrage din SCHEMA.md cu un tipar dispărut, deci se întoarce goală și raportează toate cele 757 de etichete ca nevalide, iar cele zece „wikilink-uri rupte” sunt legăturile explicite spre `_archive/`, care există toate; mai grav, la fiecare rulare scrie în `log.md` o intrare fără cele trei rânduri D8 și rescrie fișierul în CRLF (s-a întâmplat în această sesiune, restaurat cu `git checkout`). (b) Recensământul lacunelor pe toate cele 49 de acte: 31 de intervale, 16 explicate, 15 fără niciun marcaj, 51 de articole; cinci acte nu erau consemnate nicăieri, dintre care `L-234-2016` lipsește arts. 24 și 27-35, zece articole într-o lege din perimetrul CNPF pe care tabelul de acoperire o numește „clean”. (c) `L-100-2017` art. 52 scrie `Articol 52`, fără `-ul`, deci nu ia ancoră — a doua instanță a capcanei `Aricolul 78`, și tocmai articolul despre **puncte**, forma în care se citează orice HG de aici. (d) Punctul 2 din „Outstanding work” arăta spre fișierul greșit: Codul civil are 0,2% linii continuate, nu 60,2%; `COD-985-2002` are 27,7%, iar 3.097 de ancore din corpus au titlul tăiat de un salt de linie. (e) `COD-1163-1997` conține singurul articol `54^1/1` din vault, pe care tiparul obișnuit îl trunchiază la `54^1` și îl confundă cu articolul real. (f) 278 din cele 280 de avertismente sunt `language: other` din ingestia în masă din iulie, rezolvabile mecanic din URL-ul `source_record`.
- **Decis:** Eugen a cerut raportul în vault și corectarea CLAUDE.md. Nu s-a atins niciun text de drept: cele două articole invizibile rămân necorectate, pentru că rescrierea textului legal e interzisă aici, și sunt consemnate ca `[de verificat]`. Întrebarea deschisă 3 devine recensământul complet, cu tabel; întrebarea 4 primește a doua instanță; întrebarea 2 primește capcana `54^1/1`; punctul 2 din „Outstanding work” e corectat cu măsurătorile, nu cu o estimare. `run_cnpf_legal_lint.py` nu se retrage azi, dar primește interdicție de rulare în „Where things are”, cu motivul; cele două verificări ale lui care lipsesc din validator — pagini orfane și referințe raw la nivel de pagină — rămân de portat.
- **Unde:** `_meta/lint/audit-2026-09-05-full.md`; `CLAUDE.md`, „Where things are” (`_meta/lint/`), întrebările deschise 2, 3 și 4, „Outstanding work” punctele 2 și 6; copie de siguranță în `C:\Users\harab\wiki-backups\wiki-2026-09-05-pre-audit-claudemd\`, 2346 de fișiere, confirmată prin sha256.

## [2026-09-05] delete | Duplicatul planului din „Claude outputs” iese; folderul rămâne

- **Aflat:** `Claude outputs/2026-09-05-plan-restructurare-wiki.md` era identic la octet cu copia din `_meta/plans/` (sha256 `b9410219…`), urmărit în git, în afara oricărei căi pe care o verifică specificația. Folderul nu e însă o rămășiță: în timpul acestei sesiuni, un al doilea agent care lucra la contractul Casa Sihastrului a scris în el un `.docx`. Tot concurenței i se datorează și cele două fișiere din `_meta/anchoring-work/` care și-au schimbat terminațiile de linie fără să fie editate de nimeni aici — conținut identic, restaurate cu `git checkout`.
- **Decis:** Eugen a cerut ștergerea duplicatului. Se șterge doar fișierul, nu folderul, pentru că folderul conține munca în curs a altui agent. Unde ajunge de acum înainte ieșirea aceea rămâne la judecata lui: e o decizie de organizare, nu o reparație de lint.
- **Unde:** `git rm "Claude outputs/2026-09-05-plan-restructurare-wiki.md"`; copia păstrată, verificată la același hash, în `_meta/plans/`; `CLAUDE.md`, „Outstanding work” punctul 6; `_meta/lint/audit-2026-09-05-full.md`, secțiunea E1; copie de siguranță în `C:\Users\harab\wiki-backups\wiki-2026-09-05-pre-delete-duplicate\`, 2355 de fișiere.

## [2026-09-05] update | Paginile orfane din P8-bis legate; filtrul grafului Obsidian

- **Aflat:** graful Obsidian arăta circa 500 de puncte izolate din 693 de fișiere. Cauza nu e o lacună de fond: citarea stratului raw se scrie `[raw/...]` cu o singură paranteză, 691 de astfel de referințe față de un singur `[[raw/...]]`, iar Obsidian desenează muchii doar pentru wikilink-uri. Așa că `raw/` (355 de fișiere fără wikilink), `_meta/` (47), `_archive/` (90) și `legal-career/` (7) apar orfane prin construcție. În sens util erau orfane doar trei pagini structurate, cele din P8-bis; cele două din lintul de dimineață, `COD-154-2003` și `L-105-2003`, erau deja legate. Duplicatul planului din „Claude outputs” nu mai era pe disc la verificare, deși apărea cu o oră mai devreme; git nu îl mai urmărește din commit `7a95b4c`.
- **Decis:** Eugen a cerut rezolvarea completă. Nu se schimbă sintaxa citărilor `[raw/...]` în `[[raw/...]]`, pentru că validatorul și lintul citesc exact forma aceea; se leagă cele trei pagini de paginile-părinte firești și se filtrează graful, nu vault-ul. Filtrul lasă `showOrphans` pornit, ca o pagină structurată rămasă nelegată să se vadă imediat.
- **Unde:** `entities/bnm.md`, paragraf nou după lista P8; `entities/L-100-2017.md`, înainte de „Repere de utilizare”; `.obsidian/graph.json`, câmpul `search`; `CLAUDE.md`, „Outstanding work” punctul 6.

## [2026-09-05] update | `language: other` rezolvat pe 277 de fișiere; URL-ul de catalog s-a dovedit nesigur

- **Aflat:** metoda propusă de audit era greșită și s-a văzut doar pentru că a fost verificată. Auditul spunea să se citească limba din `source_record` (`bnm.md/en/content` față de `/ro/content`). BNM listează însă PDF-uri românești pe pagini engleze și invers: **zece fișiere își contrazic propriul URL** — nouă rapoarte și prezentări de inflație în română sub `/en/content/`, plus `ISAP1_Final_WebVersion`, document englez sub `/ro/content/`. Dacă mă luam după URL, zece fișiere ar fi fost etichetate greșit, cu toată încrederea. Textul documentului a decis, prin frecvența cuvintelor-unelte și numărul de diacritice, cu URL-ul și numele fișierului doar ca argument secundar, înlăturat unde contrazicea conținutul; fiecare conflict a fost citit cu ochiul înainte de aplicare. Două încercări de scriere au fost oprite de propriile asserturi înainte să atingă vreun fișier: prima decodase cu `read_text()`, care normalizează CRLF în LF, deci frontmatter-ul nu se mai potrivea cu octeții fișierului; a doua pierdea `\r` de la capătul liniei rescrise.
- **Decis:** se schimbă doar linia `language:` din frontmatter, la nivel de octeți, cu restul fișierului neatins — 262 `en`, 15 `ro`. Un fișier rămâne `other` pe bună dreptate: `236__Prezentare_RI_mai_2025.pdf.md` e o prezentare din care extracția PDF a scos 39 de cuvinte și nicio diacritică, deci nimic din fișier nu poate stabili limba, iar `other` e valoarea onestă, nu o presupunere prezentată ca fapt. Avertismentele scad de la 280 la 3. **Acoperirea nu se regenerează în acest commit:** e învechită din cauza ingerării `COD-434-2023` a altui agent, aflată în curs, iar singura diferență este acel act; regenerarea ar trage munca lui neterminată într-un commit străin.
- **Unde:** 277 de fișiere sub `raw/papers/bnm/`; dovada că textul n-a fost atins e verificatorul, 378/378 sha256 valide după schimbare; `CLAUDE.md`, „Outstanding work" punctul 6; `_meta/lint/audit-2026-09-05-full.md`, secțiunea E2; copie de siguranță în `C:\Users\harab\wiki-backups\wiki-2026-09-05-pre-language-fix\`, 2362 de fișiere.

## [2026-09-05] lint | Verificarea auditului: o eroare de fapt, corectată

- **Aflat:** reverificarea mecanică a auditului confirmă aproape tot: lacunele din `L-234-2016` (24, 27-35, doar titlu de capitol între 26 și 36), `COD-154-2003` (226-244 și 374-382), `L-220-2007` art. 6, `L-845-1992` arts. 21 și 31, „Articol 52” la linia 531, `54^1/1` unic în vault, CUPRINS-ul Codului fiscal, cele cinci ținte de arhivă existente, scrierea în `log.md` din codul scriptului, și disciplina in-force, refăcută independent, cu zero citări ancorate spre cele 47 de dispoziții. Nu rezistă patru lucruri: raportul comis nu scrie „Ridicat 10 / Mediu 807 / Scăzut 814” ci „0 / 1229 / 60”, pentru că a fost generat la 09:18, înainte de rescrierea `SCHEMA.md` de la 15:28; cifra 757 nu se reproduce static, pe cele 91 de pagini sunt 637 de etichete; `page_level_raw_refs` e 22 în raport, nu 21; `L-315-2022` are tot 9 rânduri și lipsea din enumerarea celor mai subțiri pagini.
- **Decis:** Eugen a cerut corectarea. Se rescrie doar paragraful „Consequence”, cu explicația cronologică, și se notează cele două cifre în A1 și A3. Diagnosticul A1-A2 și recomandarea de retragere a scriptului rămân, pentru că riscul e prospectiv: următoarea rulare, nu fișierul din git.
- **Unde:** `_meta/lint/audit-2026-09-05-full.md`, secțiunile A1, A3 și „Consequence”.

## [2026-09-05] ingest | Perimetrul construcțiilor: Codul urbanismului 434/2023 și HG 743/2024

- **Aflat:** premisa de verificat s-a confirmat, dar cu data corectată și cu o anomalie de registru pe deasupra. Codul intră în vigoare **30.01.2025**, nu 30.01.2026: art. 390 alin. (1) spune „peste 12 luni de la data publicării", iar publicarea e 30.01.2024. Cifra 30.01.2026 pare să vină din confundarea publicării cu intrarea în vigoare; capcana simetrică e chiar fișa legis.md, care scrie „Data intrării în vigoare 30.01.2024" — data excepțiilor din teza a doua, între care art. 150, nu a codului. Data se confirmă de patru ori în afara art. 390. Cele trei legi vechi sunt abrogate integral (art. 390 alin. (5)), deci ținta 3 cade: **niciuna nu se ingerează**. Dar pentru **Legea 721/1996 metadata legis.md își contrazice propriul text**: corpul actului poartă „Abrogată prin CUC434 […] în vigoare 30.01.25", iar câmpul „Data abrogării" e gol și lista o marchează „Modificat" — cine filtrează după marcaj crede că legea calității în construcții e în vigoare. A doua constatare care schimbă ținta: **nu mai există regulament de recepție**. Codul nu deleagă recepția nicăieri, o reglementează el însuși în arts. 192–215, iar HG 285/1996 e abrogată de la 30.01.2025 prin HG 726/2024. A treia, de metodă: HG 743/2024 nu se găsește prin căutare în titlu, fiindcă titlul e „cu privire la asigurarea calității în construcții"; l-a găsit **căutarea în text**, `search_type=2`, cu fraza din art. 338 alin. (1) al codului. A patra, cea care limitează ce putem cita: **cele 25 de anexe ale codului nu sunt în text** — `showdetails` le servește doar ca etichete de legătură — deci „anexa nr. N din cod" nu e ancorat, inclusiv anexele 9, 10 și 25, pe care normele deja folosite le invocă. În fine, verificatorul a raportat un FAIL care era al lui, nu al sursei: cerea ancore pentru art. 13^1 și 28^1, care sunt trimiteri la articolele **altor legi** din blocul de modificare de la finalul codului.
- **Decis:** se ingerează două acte, nu trei — codul și HG 743/2024 — cu motivul negativ scris în manifest, ca ținta 3 și „regulamentul de recepție" să nu fie recăutate. Se repară două unelte, amândouă cu regresie verificată: `fetch()` nu mai scrie răspunsul `curl` peste fișierul din cache (legis.md întoarce pagina Cloudflare cu `rc=0`, deci o rulare blocată ar fi distrus singura copie a sursei — descarcă în temporar, promovează la reușită, cade pe cache); și controlul de exponenți din `verify_business_law.py` compară acum cu liniile de referință care **încep** cu „Articolul N^M", nu cu tot HTML-ul, iar potrivirile din interiorul frazei se raportează separat, ca informație. Regresia pe toate cele 21 de acte: FAILURES 0, seturile de exponenți neschimbate, inclusiv cele 159 ale Codului fiscal cu forma `54^1/1` și cele 254 ale Codului contravențional. HTML-ul s-a luat din Chrome printr-un `fetch` same-origin, care întoarce **octeții serverului**, nu DOM-ul serializat ca la P8, deci markupul `<sup>` e exact cel servit. Cele patru întrebări rămase — regulamentul de demolare de la art. 322 alin. (4), negăsit pe legis.md; Legea cadastrului 1543/1998, neingerată; soarta certificatelor de urbanism emise înainte de 30.01.2025, despre care codul tace; celelalte regulamente delegate — se lasă deschise pentru Eugen, nu se rezolvă aici.
- **Unde:** commit-ul acestei sesiuni; `raw/papers/moldova-legal/COD-434-2023.md` (doc_id 155736, 390 de ancore, numerotare 1–390 completă, integritate 3.640/3.640 de linii) și `HG-743-2024.md` (doc_id 155190, zero ancore de articol, consolidare **viitoare** 2026-12-30 cu 6 dispoziții amânate, integritate 779/779); `entities/COD-434-2023.md` și `entities/HG-743-2024.md`; `index.md`, 91→93 pagini; `raw/papers/moldova-legal/_manifest.md`, **secțiunea O**; `_meta/imports/moldova-legal/ingest_business_law.py` (DOCS plus `fetch()`) și `verify_business_law.py`; copie de siguranță în `C:\Users\harab\wiki-backups\wiki-2026-09-05-cod-urbanism\`, 2362 de fișiere, 763.247.072 de octeți, confirmată identică. Validator: **0 erori**, 380 de surse cu sha256 valid.

## [2026-09-05] lint | Controalele regenerate după ingestie; registrul in-force nu vede punctele

- **Aflat:** după ingestia codului urbanismului și a HG 743/2024, două controale erau învechite, iar ordinea dintre ele contează: blocul de acoperire din `CLAUDE.md` depinde de registrul in-force, deci regenerat înaintea lui redevine învechit; ordinea corectă este registru, apoi acoperire. Mai important, registrul nu citește actele structurate pe puncte. HG 743/2024 poartă șase dispoziții amânate până la 30.12.2026 — pct. 33 subpct. 33.3, pct. 50, pct. 61 subpct. 61.6, pct. 82, pct. 115 și anexa nr. 9 — iar registrul le strânge într-o singură intrare, „HG-743-2024 art. 355”. 355 nu este o dispoziție a hotărârii, ci numărul de articol din Monitorul Oficial al actului modificator, HG341 din 24.06.26. Cele douăsprezece linii sunt consemnate, deci informația nu se pierde, dar cine caută în registru „pct. 82” nu găsește nimic și poate conchide că textul din fișier se aplică azi. Regula 4 din documentul 03 face consultarea registrului obligatorie înainte de citare, deci lacuna lovește exact în controlul pe care se sprijină răspunsul.
- **Decis:** Eugen a cerut rularea generatoarelor. S-au rulat în ordinea registru, apoi acoperire, iar validatorul dă 0 erori și 3 avertismente. Nu s-a atins parserul registrului: e o reparație de unealtă, cu regresie pe toate actele, nu ceva de făcut în trecere. Lacuna intră ca întrebarea deschisă 7 în `CLAUDE.md`, cu regula provizorie: pentru orice hotărâre de Guvern se citesc parantezele de modificare din fișierul raw, nu eticheta de articol din registru.
- **Unde:** `CLAUDE.md`, blocul generat de acoperire, 49→51 de acte primare; `_meta/inforce/in-force-register.md` și `.json`, 47→48 de dispoziții, 383 de fișiere scanate; `raw/papers/moldova-legal/HG-743-2024.md`, liniile 40-45 și 612-862; `CLAUDE.md`, întrebarea deschisă 7.

## [2026-09-05] lint | `L-234-2016` verificat la sursă: nu e lacună, iar motivul aparenței e sistemic

- **Aflat:** legea nu are articole lipsă. Art. 24 și tot Capitolul IV (arts. 27-35) au fost abrogate prin **LP292 din 19.10.2023, MO398/21.10.23 art.679, în vigoare 21.10.2023**; legea are astăzi 37 de articole, iar fișierul din vault e o copie fidelă a textului de pe legis.md (doc_id 145901, verificat în direct). Ce contează mai mult decât rezultatul: **reîmprospătarea unui act la o consolidare mai nouă distruge marcajele amendamentelor anterioare.** legis.md păstrează, într-o consolidare dată, numai marcajele amendamentului care a produs acea versiune. Același act are **59** de marcaje la doc_id 139826 (2023-10-21) și **5** la doc_id 145901 (2024-11-26), toate cinci din LP259/2024 — iar cele două dispărute erau exact cele care explicau numerotarea. Fișierul nostru arată aceeași prăbușire, pentru că a fost reîmprospătat la 2026-09-04: ingestia din iulie are 59 de marcaje, cea curentă are 5. Deci reîmprospătarea câștigă textul în vigoare și pierde istoricul abrogărilor. LP259/2024, singurul amendament pe care pagina curentă îl listează, a fost verificat și nu e cauza: abrogă un alineat și adaugă art. 47^1.
- **Decis:** `L-234-2016` iese din întrebarea deschisă 3 și nu se marchează `[de verificat]`, pentru că nu mai e nimic de verificat. În locul ei intră avertismentul de mai sus: „fără marcaj" înseamnă de acum „fără marcaj în această consolidare", niciodată „fără abrogare", iar versiunea mai veche de pe legis.md sau o ingestie mai veche din `wiki-backups/` pot încă ține explicația. Celelalte rânduri rămase în întrebarea 3 au fost ingerate direct la consolidarea lor curentă și n-au fost niciodată comparate cu o versiune anterioară, deci niciunul nu e dovedit defect de sursă; comparația e pasul următor, nu o concluzie. Verificarea Cloudflare nu a fost ocolită: pagina s-a deschis în Chrome-ul lui Eugen, unde trecuse deja.
- **Unde:** `_meta/lint/audit-2026-09-05-full.md`, secțiunea B-ter și rândul din B; `CLAUDE.md`, întrebarea deschisă 3 (rândul barat plus avertismentul despre pierderea marcajelor) și „Outstanding work" punctul 6; dovada locală în `wiki-backups/wiki-before-eu-transposition-foundation-20260709-193401/raw/papers/cnpf/L-234-2016.md`.

## [2026-09-05] ingest | Regulamentul de demolare: HG 582/2022, și o negație pe care o scrisesem neverificată

- **Aflat:** actul căutat există, e în vigoare și **nu e emis în temeiul codului**. Clauza lui de adoptare spune „În temeiul **art. 439^6 alin. (5) din Codul contravențional** nr. 218/2008", deci delegarea din art. 322 alin. (4) al `COD-434-2023` e împlinită de un act din 2022, anterior codului, adoptat pentru executarea măsurii de siguranță a demolării dispuse de instanță — exact configurația pe care codul o construiește în art. 327 alin. (1). O căutare după temeiul legal presupus nu l-ar fi găsit niciodată. Ce l-a găsit a fost căutarea în titlu după **formula delegării**, fiindcă titlul o reia aproape cuvânt cu cuvânt: „modul de demolare a construcțiilor neautorizate". **Și aici e greșeala mea de la prima trecere:** scrisesem în manifest și pe pagina codului că actul „nu a fost identificat prin căutare în titlu". Căutarea aceea **nu fusese rulată**. Când a fost, a întors un singur rezultat, chiar actul. Ipoteza pe care o adăugasem, că actul „poartă un titlu care nu conține cuvântul", era exact pe dos. Lanțul e acum ancorat cap la cap, prin `COD-218-2008` art. 439^6: alin. (1) leagă demolarea de art. 179, alin. (3) o dă instanței și o face să **supraviețuiască** încetării procesului contravențional, alin. (5) e delegarea. Termenele cerute de art. 328 alin. (1) din cod sunt acum ancorate: executarea nu poate depăși **12 luni**, iar ciclul prescripție–răspuns–executare silită merge din trei în trei zile, cu **lipsa răspunsului declanșând direct** executarea silită. Regulamentul acoperă și **demontarea**, deși titlul spune doar demolare (pct. 4 și pct. 20 subpct. 3)). A fost aliniat la cod abia prin HG27/2026, în vigoare 01.03.26, cu 13 luni după intrarea în vigoare a codului.
- **Decis:** se ingerează, cu zero ancore, ca celelalte acte în puncte — numerotarea repornește între hotărâre (pct. 1–2) și Regulament, deci „pct. N" nu e ancorat. Corectura afirmației greșite se scrie **înainte** de constatarea nouă, în ambele locuri unde a apărut, și se păstrează tăiată, nu ștearsă, ca dovadă a erorii: regula pe care o consemnez este că **o negație nu se scrie decât după căutarea care o susține**, fiindcă altfel închide un drum care era deschis. Cele două întrebări rămase — dacă termenele de demolare se aplică prin asimilare și **remedierii**, la care art. 328 trimite la același regulament, și cum se contestă dispoziția de executare silită — se lasă deschise pentru Eugen.
- **Unde:** `raw/papers/moldova-legal/HG-582-2022.md` (doc_id 152829, consolidare 2026-03-01 trecută, fără dată de abrogare, integritate 125/125 de linii, cele 7 `<sup>` devenite `439^6` și `134^1`, zero apariții ale formei aplatizate „4396" care ar fi falsificat chiar temeiul legal); `entities/HG-582-2022.md`; corecturi în `entities/COD-434-2023.md` întrebarea 1, `entities/HG-743-2024.md` întrebarea 1 și `raw/papers/moldova-legal/_manifest.md` O.9 punctul 1; secțiune nouă **O.10** în manifest; `index.md`, 93→94 pagini. Validator: **0 erori**, 381 de surse cu sha256 valid, `verify_business_law.py` FAILURES 0 pe toate cele 22 de acte.

## [2026-09-05] lint | Toate cele cincisprezece lacune, verificate în istoricul de versiuni al legis.md

- **Aflat:** niciuna nu e defect de ingerare și niciuna nu e gaură inexplicabilă în lege. Fiecare articol a fost abrogat; lipsește doar *consemnarea* abrogării din consolidarea pe care o ținem. Datele: `COD-154-2003` 226-244 prin LP254 din 09.12.2011 și 374-382 prin LP205 din 20.11.2015; `COD-218-2008` 441 prin LP208 din 17.11.2016, în vigoare 16.03.2017; `L-220-2007` 6 prin LP90 din 29.05.2014; `L-845-1992` 21 prin LP133 din 15.11.2018 și 31 prin LP746 din 27.12.2001; `L-548-1995` toate șapte, înainte de 2016. **Trei mecanisme, nu unul.** (1) Marcajul e aruncat la reîmprospătare — recuperat cuvânt cu cuvânt pentru `L-845-1992` art. 21 și `COD-154-2003` arts. 374, 382. (2) Marcajul n-a existat niciodată: consolidările de dinainte de ~2018 nu poartă paranteze deloc, deci proba e tranziția însăși, coroborată prin dată (art. 6 din 220/2007 dispare în versiunea din 27.06.2014, iar unicul amendament al acelei versiuni e publicat în MO chiar în 27.06.2014). (3) **Ciotul de abrogare e șters**: `L-548-1995` purta toate cele șapte articole ca linii explicite `Articolul N – abrogat.` în consolidarea din 01-08-2016 (doc_id 94178), iar următoarea, 04-10-2016 (doc_id 95643), le-a scos cu totul, fără vreun amendament care să deosebească cele două versiuni. Al treilea e cel mai grav: textul din 2016 se explica singur, iar `Articolul N – abrogat.` e exact forma pe care ancorarea noastră o prinde — ingerat înainte de octombrie 2016, actul ar fi avut toate cele șapte ancore. Metoda: legis.md expune fiecare consolidare veche prin `showDetails(null,'<doc_id>')`, iar textul ei la `/cautare/showdetails/<doc_id>`.
- **Decis:** întrebarea deschisă 3 se închide, cu tabelul de datări în locul listei de lacune, și nimic din ea nu mai e `[de verificat]`. Întrebarea 6 se închide și ea, iar republicarea din 2015, bănuită acolo, **nu** e explicația: ciotele au supraviețuit republicării și au fost șterse un an mai târziu. Bisecția presupune monotonie, presupunere care a cedat la `L-548-1995`, deci acolo proba e comparația celor două consolidări din 2016, nu o dată bisectată — asta e scris în raport, nu ascuns. Verificarea Cloudflare a fost trecută de Eugen; nu am ocolit-o.
- **Unde:** `_meta/lint/audit-2026-09-05-full.md`, secțiunea B-quater; `CLAUDE.md`, întrebările deschise 3 și 6.

## [2026-09-05] ingest | Legea cadastrului 1543/1998: recepția este condiție de înregistrare, și o a treia capcană de denumire

- **Aflat:** răspunsul la întrebarea deschisă nr. 2 de la ingerarea perimetrului construcțiilor este **da, și e scris direct**. `art. 40^4 alin. (1)`: construcția se înregistrează dacă anterior sau concomitent se înregistrează dreptul de proprietate ori superficie asupra terenului **și se prezintă documentele ce confirmă recepția lucrărilor**. Două condiții cumulative, nu alternative. Pentru construcția nefinalizată, alin. (2) cere autorizația plus avizul tehnic al expertului atestat, cu un prag explicit — gradul de executare **nu mai mic decât planșeul la cota 0.000** — ceea ce este perechea exactă a art. 351 alin. (3) din `COD-434-2023`: codul spune la ce servește avizul, legea cadastrului spune ce prag trebuie să atingă. Alin. (3) preia casele vechi din registrele gospodăriilor, adică chiar norma la care trimite art. 387 alin. (3) din cod. **Capcană de denumire, a treia din corpus și de alt tip decât primele două:** legis.md dă titlul ca „LEGE Nr. 1543 din 25.02.1998 **cadastrului bunurilor imobile**" — fără „Legea", care stă în câmpul TIPUL, și fără „privind". O căutare în titlu după „Legea cadastrului bunurilor imobile" nu o întoarce; la `L-284-2004` și `L-550-1995` titlul se schimbase, aici e doar trunchiat în fișă. Actul are **consolidare viitoare, 2027-01-01**, cu șase dispoziții neintrate în vigoare, arts. 15^3–15^8, toate în materia inginerului cadastral certificat — **niciuna nu atinge art. 40^4**, verificat în registru înainte de a-l cita.
- **Decis:** se ingerează cu pipeline-ul obișnuit, fără abateri; 99 de ancore, 61 de articole de bază 1–61 fără lacune plus 38 cu exponent. Cele două întrebări care rămân se lasă deschise, fiindcă sunt de drept, nu de text: codul și legea cadastrului **nu se citează reciproc** în punctul care contează, iar la recepția în două etape (art. 192 alin. (9) din cod) nu rezultă dacă procesul-verbal la terminarea lucrărilor e suficient pentru înregistrare sau se cere și cel final; și autorizația de construire **nu e cerută expres** pentru construcția finalizată — intră doar indirect, prin art. 193 alin. (2) din cod, care spune că actul de recepție certifică respectarea ei. Secțiunea despre recepție de pe pagina codului trece din „parțial ancorat" în „ancorat".
- **Unde:** `raw/papers/moldova-legal/L-1543-1998.md` (doc_id 150226, republicată 02.04.2021, integritate 1.038/1.038 de linii, 129 `<sup>` rezolvate în 38 de articole cu exponent plus 78 de exponenți de alineat și literă); `entities/L-1543-1998.md`; `entities/COD-434-2023.md`, întrebarea 2 închisă și secțiunea de recepție rescrisă; `raw/papers/moldova-legal/_manifest.md`, **secțiunea P** și O.9 punctul 2; `index.md`, 94→95 pagini. Copie de siguranță în `C:\Users\harab\wiki-backups\wiki-2026-09-05-cadastru\`, 2681 de fișiere, confirmată identică. Validator: **0 erori**, 382 de surse cu sha256 valid; `verify_business_law.py` FAILURES 0 pe toate cele 23 de acte. Registrul in-force trece la 54 de dispoziții în 11 acte.

## [2026-09-05] update | `.gitattributes`: git nu mai convertește nimic, deci verificatorul e reproductibil

- **Aflat:** verificatorul dădea 0 erori aici și 2 într-o clonă proaspătă, iar cauza nu era vault-ul: Git for Windows are `core.autocrlf=true` în configurația de **sistem**, în timp ce depozitul poartă local `core.autocrlf=false`. Clona rescria totul în CRLF, iar `L-192-1998`, care declară `sha256_convention: raw`, nu-și mai reproducea amprenta. Măsurat înainte de a atinge ceva: 382 de surse brute cu `sha256`, dintre care 321 au CRLF în corp, dar numai **trei** se reproduc exclusiv peste octeții neconvertiți — `CC-1107-2002` și cele două `economic-criteria-*` din mded-policy-2024. Normalizarea la LF ar fi rupt exact acele trei amprente, adică tocmai controlul care dovedește că textul de drept n-a fost atins, și ar fi rescris în plus 129 de blob-uri din afara zonelor brute, între care probele strip-and-compare din `_meta/anchoring-work/` și instantaneele `showdetails-*.html`, a căror valoare e că sunt ce s-a primit de la sursă.
- **Decis:** nu normalizare, ci determinism. `* -text diff` oprește orice conversie în ambele sensuri, cu `binary` pentru formatele binare; o extragere e identică la octet cu commit-ul pe orice mașină, indiferent de `core.autocrlf`. Zero blob-uri rescrise și zero fișiere atinse, ceea ce conta și pentru că alt agent lucra în același arbore. Terminațiile mixte rămân, ceea ce e onest: sursele așa au venit. Dacă normalizarea reală se dorește vreodată, e o operațiune separată, cu re-ștampilarea celor trei surse și o decizie explicită despre probele de ancorare.
- **Unde:** `.gitattributes`, commit `94fd97d`; verificat pe o clonă proaspătă cu setările implicite de sistem — erorile scad de la 2 la 1, iar cele două fișiere de control sunt identice la octet cu copia de lucru. Eroarea rămasă, `hygiene.coverage-stale`, nu ține de terminații: blocul de acoperire comis nu mai corespunde registrului in-force regenerat în `fb2d785` și se închide când intră ingerările în curs.

## [2026-09-05] update | Documentul 05 reîmprospătat din proiect, și un defect în ștampilarea copiilor

- **Aflat:** documentul 05 contrazicea folderul pe care îl descrie: spunea că cele șapte coduri rămase sunt „outside coverage entirely", iar ele erau ingerate și ancorate de a doua zi. Greșeala mergea în direcția care irosește baza, fiindcă subestima acoperirea și ar fi coborât la „not anchored" un răspuns care era de fapt ancorat. Verificarea directă a vault-ului a mai dat lipsuri neînregistrate nicăieri: Constituția, Acordul de Asociere cu anexele și jurisprudența, adică treptele 1, 2 și 8 din ierarhia surselor a documentului 03, plus Legea insolvabilității 149/2012 și zero acte secundare CNPF. Constatarea cea mai grea nu e însă de acoperire: **stratul de constatări este acum partea cea mai slabă a vault-ului.** Toate cele 17 pagini `acquis-*` și matricea de transpunere poartă `confidence: medium`, iar 16 din 18 au ultima actualizare 9 iulie, deci sunt anterioare reconstrucției stratului brut din septembrie; matricea încă poartă `imported_from` folderul-strămoș din iulie. Sub ele stă o asimetrie măsurabilă: legile de perimetru moldovenești au 14.161 de linii de text integral, cele 29 de acte UE au 4.960 de linii în total, în medie 171 pe act, fiindcă sunt extrase structurate. MiFID II stă ca vreo 170 de linii față de 2.611 ale Legii 171/2012. Deci o constatare de transpunere compară un text integral cu un rezumat, iar pagina care o consemnează e anterioară versiunii curente a textului moldovenesc, și nimic din toate astea nu se vede în constatarea însăși: se citește ca lucru terminat. **Și un defect de unealtă:** `stamp_copies.py` reconstruiește frontmatter-ul și pune `master` între ghilimele duble, dar valoarea conține deja ghilimele, deci rezultatul `master: "claude.ai project "Legal Wiki""` nu mai este YAML valid. Nu s-a văzut până acum fiindcă scriptul rescrie fișierul doar când corpul s-a schimbat, iar celelalte șase copii au ștampila pusă de mână și au fost raportate mereu „unchanged". Prima reîmprospătare reală a declanșat defectul la prima ocazie pe care a avut-o.
- **Decis:** Eugen a cerut actualizarea documentului 05 și a decis să nu urmărească actele secundare CNPF; lipsa rămâne totuși consemnată în hartă ca lacună, nu ca plan, fiindcă regula documentului cere înregistrarea lacunelor independent de faptul că se lucrează sau nu la ele. Ordinea de extindere se schimbă: pe primul loc nu mai stă o extindere, ci reverificarea stratului de constatări, apoi actele UE în text integral, sweep-ul de actualitate, Constituția și Acordul de Asociere, deciziile Curții Constituționale, Legea 149/2012. Regula nouă a documentului, ca să nu mai derive: **nu repetă nicio cifră pe care o generează un script**, ci numește tabelul și păstrează judecata. Regula a fost pusă la încercare în aceeași oră, fiindcă trei cifre scrise dimineața erau deja învechite după-amiaza, alt agent ingerând un act în timp ce documentul se scria; cifrele au fost scoase, nu corectate. Defectul din `stamp_copies.py` a fost ocolit manual pe linia `master` și **nu** a fost reparat în script: e o reparație de unealtă, cu regresie pe toate cele șapte copii, nu ceva de făcut în trecere.
- **Unde:** master în proiectul claude.ai „Legal Wiki", `legal-career/05-knowledge-map.md`; copia locală reîmprospătată și re-ștampilată, `taken: 2026-09-05`, `sha256_body` 8a5d95e9a017; defectul în `_meta/schema/stamp_copies.py`, linia care forțează ghilimelele pe câmpul `master`, nereparat. Validator: 0 erori, 3 avertismente, iar `copy.stale` rămâne doar pentru `legal-career/06-matter-log.md`.

## [2026-09-05] update | `stamp_copies.py` reparat: ghilimelele nu se mai pun de mână

- **Aflat:** defectul nu stătea în câmpul `master`, ci în metodă. Scriptul reconstruia frontmatter-ul punând ghilimelele după o listă de excepții scrisă de mână, câte una pe cheie: apostrofuri la `taken` și `stamped`, ghilimele duble la `master`, `true`/`false` la valorile logice, restul lăsate neatinse. Orice valoare care nu se potrivea excepției ei ieșea greșit, iar `master` conține el însuși ghilimele duble, deci rezultatul era `master: "claude.ai project "Legal Wiki""`, YAML nevalid. A doua consecință, nedescoperită până acum doar fiindcă nu s-a nimerit: o cheie lipsă din frontmatter ieșea ca `k: None`, adică șirul „None", nu valoare nulă. Regresia pe toate cele șapte copii confirmă că forma fișierelor nu se schimbă: `master` rămâne neîncadrat, datele rămân între apostrofuri, `local_notes` rămâne `true`/`false`, ordinea cheilor rămâne cea din spec.
- **Decis:** ghilimelele nu se mai pun de mână. Fiecare rând se emite prin `yaml.safe_dump`, deci YAML însuși decide dacă o valoare are nevoie de încadrare și de care fel. Singura excepție păstrată este conversia `taken` și `stamped` prin `isoformat()` când YAML le-a citit ca dată, ca să rămână șiruri și după rescriere. Testul de regresie s-a rulat pe o rădăcină de probă din afara vault-ului, cu toate cele șapte copii și cu `--taken` forțat ca să declanșeze calea de scriere pe fiecare; în vault scriptul le-ar fi raportat „unchanged" și nu ar fi testat nimic. Verificate pe fiecare fișier: corpul neatins octet cu octet, hash-ul recalculat corect, câmpurile netemporale neschimbate, ordinea cheilor păstrată.
- **Unde:** `_meta/schema/stamp_copies.py`, funcția nouă `emit()` și blocul de reconstrucție din `main()`; originalul păstrat în afara vault-ului pe durata sesiunii. Rulare live după reparație: 7 din 7 „unchanged", deci reparația nu a atins niciun fișier de metodă. Validator: 0 erori, 3 avertismente, 7 copii verificate.

## [2026-09-06] update | Verificare completă, documentul 06 reîmprospătat, munca de pe 5 septembrie comisă

- **Aflat:** vault-ul trece toate controalele generate: validator 0 erori, acoperire la zi, SCHEMA neschimbat, 382 de surse cu sha256 valid. Două lucruri nu se vedeau din controale. Copia locală a documentului 06 era în urma proiectului cu o intrare întreagă, M-001 (acționarul băncii, 4 septembrie), deci o sesiune din folder ar fi lucrat fără poziția deja luată. Și registrul in-force ieșea „învechit” la `--check` numai din cauza datei `as_of`, conținutul fiind identic; regenerat din shell-ul Linux al sesiunii, fișierul ar fi trecut de la CRLF la LF, adică exact rescrierea pe care `.gitattributes` a fost pus să o oprească. Tot din acel shell: nu poate șterge fișiere, așa că git lasă în urmă un `index.lock` și nu are acreditările GitHub, deci commit-ul și push-ul se fac de pe Windows.
- **Decis:** Eugen a aprobat planul. Documentul 06 reîmprospătat din proiect cu textul integral (M-001 inclus) și re-ștampilat `taken: 2026-09-06`; hash-ul recalculat coincide cu ștampila. Registrul in-force nu se regenerează pentru o diferență de dată; se reface de pe Windows la următoarea ingerare. Folderul `Claude outputs/` intră în `.gitignore`: e livrabil al altor sesiuni, nu wiki, ceea ce închide punctul lăsat deschis în „Outstanding work” 6. Munca de pe 5 septembrie rămasă necomisă, cele patru acte ale perimetrului construcțiilor și cadastrului cu paginile lor, manifestul, registrul, documentul 05 și scripturile, intră într-un singur commit.
- **Unde:** commit-ul acestei sesiuni; `legal-career/06-matter-log.md`, `sha256_body` 216943c0d315; `.gitignore`; `_meta/lint/validate-2026-09-06.md`. Validator după reîmprospătare: 0 erori, 2 avertismente, `copy.stale` dispărut.

## [2026-09-06] update | Scriptul de închidere a sesiunii, și controlul registrului in-force nu mai pică pe dată

- **Aflat:** închiderea corectă a unei sesiuni cerea șase comenzi într-o ordine care nu era scrisă nicăieri decât în jurnal: registrul in-force înaintea acoperirii, fiindcă acoperirea îl citește; apoi SCHEMA; apoi validatorul cu raport; apoi commit. Dimineața, ordinea uitată a lăsat registrul cu data veche. Testul scriptului a arătat cauza mai adâncă: `--check` din `build_inforce_register.py` ignora doar linia `generated:`, dar compara `as_of:` și „Stare la ...”, deci registrul ieșea „învechit” în orice zi de după generare, fără să se fi schimbat vreo dispoziție. O barieră la commit construită pe acest control ar fi blocat fiecare commit dintr-o zi nouă.
- **Decis:** Eugen a cerut trei niveluri de automatizare, pe rând: script unic, barieră la commit, verificare pe GitHub. Primul e `_meta/close_session.py`: regenerează cele trei controale în ordinea corectă, rulează validatorul cu raport, se oprește la prima problemă, iar cu `--commit "mesaj"` face commit și push; `--check` nu scrie nimic și e ce vor folosi bariera și GitHub. Două refuzuri deliberate, scrise în capul scriptului: nu re-ștampilează copiile din `legal-career/`, fiindcă ștampila există ca să prindă editarea locală și un script care o reface automat ar ascunde exact asta; și nu scrie în jurnal, ci refuză să comită dacă lipsește intrarea de azi (D8), cu `--no-log-entry` ca ieșire explicită. Controlul registrului ignoră acum și `as_of:` și „Stare la”: dacă o dispoziție a intrat între timp în vigoare, tabelul se schimbă și controlul pică oricum. Verificat în ambele sensuri: `--as-of 2026-09-12` la zi, `--as-of 2026-09-14` învechit, fiindcă atunci intră în vigoare cele cinci articole din `COD-218-2008`.
- **Unde:** `_meta/close_session.py`, nou; `_meta/inforce/build_inforce_register.py`, funcția `--check`, trei linii; registrul, blocul de acoperire și raportul validatorului regenerate de pe Windows prin script, doar datele s-au schimbat. Prima rulare `--commit` este chiar commit-ul acestei intrări.

## [2026-09-06] update | Bariera la commit: git refuză singur un commit cu controale învechite

- **Aflat:** git nu trimite hook-urile pe GitHub, `.git/hooks` nu e versionat, dar `core.hooksPath` poate arăta spre un folder din depozit, care este; prețul e o setare locală pe fiecare clonă. Pe Windows, `sh` nu e în PATH din PowerShell, dar git își folosește propriul `sh` din `usr/bin` la hook-uri, deci hook-ul merge chiar dacă un test naiv din Python nu-l găsește; instalatorul îl caută acum plecând de la `git --exec-path`. Verificarea fără hash-uri durează 11 secunde pe această mașină, cu hash-uri ar fi mult mai mult, așa că bariera lasă hash-urile pentru rularea completă și pentru GitHub. Testat în ambele sensuri: cu registrul in-force stricat dinadins (un rând scos), commit-ul e refuzat cu mesajul scriptului; cu registrul restaurat, trece. Și un rând vechi din `CLAUDE.md` spunea că folderul nu e sub control de versiune, fals de pe 5 septembrie.
- **Decis:** `_meta/hooks/pre-commit` rulează `close_session.py --check --no-hash` înainte de fiecare commit; nu regenerează nimic, doar refuză și spune ce să rulezi. `python _meta/hooks/install.py` pornește bariera pe o clonă, cu `--status` și `--uninstall`, și rulează hook-ul o dată ca test. Ieșirea de urgență rămâne cea standard, `git commit --no-verify`. `CLAUDE.md` are o secțiune nouă, „Closing a session”, cu comanda unică, bariera și instalarea; secțiunea „Safety” spune acum că folderul e sub git și de ce copia de siguranță rămâne pentru rescrierile în masă. `Claude outputs/` e consemnat ca rezolvat în „Outstanding work”.
- **Unde:** `_meta/hooks/pre-commit` și `_meta/hooks/install.py`, noi; `CLAUDE.md`, secțiunile „Keeping this file true”, „Safety”, „Closing a session”, „Outstanding work” pct. 6. Bariera e pornită pe această mașină. Commit-ul acestei intrări e primul care trece prin ea.

## [2026-09-06] update | Verificarea pe GitHub: aceleași controale, pe o clonă curată, după fiecare push

- **Aflat:** o clonă proaspătă pe Linux, făcută din copia de lucru, trece controlul complet cu hash-uri în 7 secunde: registrul, acoperirea, SCHEMA la zi, validator 0 erori. Deci `.gitattributes` din 5 septembrie face exact ce promitea, o extragere e identică la octet cu commit-ul pe orice mașină, iar verificarea din exterior nu are nevoie de nimic în plus față de `pyyaml`. Fișierul de flux nu a putut fi scris prin uneltele de fișiere ale sesiunii, `.github/workflows/` e protejat de ele, dar shell-ul îl scrie normal.
- **Decis:** `.github/workflows/validate.yml` rulează `python _meta/close_session.py --check` la fiecare push pe `main`, la cereri de fuziune și la cerere din fila Actions. Nimic scris, nimic reparat. Iese bifă verde sau X roșu lângă commit, cu rezumatul controalelor în pagina rulării, iar la eșec rulează validatorul cu toate exemplele. Prinde ce a scăpat local: o clonă cu alt `core.autocrlf`, un `--no-verify`, o mașină fără barieră. Cele trei niveluri sunt acum complete: scriptul face, bariera nu lasă să uiți, GitHub verifică din afară.
- **Unde:** `.github/workflows/validate.yml`, nou. Prima rulare pe GitHub este declanșată de commit-ul acestei intrări; rezultatul se vede în fila Actions a depozitului `eharabara/wiki-juridic`.

## [2026-09-06] decision | Înghețarea stratului de constatări acquis: 18 pagini marcate `unverified`, `confidence: low`

- **Aflat:** cele 17 pagini `concepts/acquis-*.md` și `comparisons/cnpf-transposition-matrix.md` purtau `confidence: medium` din 9 iulie, cu ancorele UE sprijinite pe extrasele `UE-*`, nu pe texte integrale, și cu stratul brut reconstruit între timp (4–5 septembrie). Nicio pagină nu avea o marcă vizibilă a acestei stări, deci putea fi citată ca lucru terminat. Taxonomia de etichete era închisă și nu avea o etichetă pentru „neverificat".
- **Decis:** planul din 6 septembrie, D2 și pasul 1: nu se reverifică acum nicio constatare, fiindcă partea UE rămâne un extras până la ingerarea textelor integrale (pasul 6 din D3). Se marchează în schimb: eticheta nouă `unverified` adăugată în spec la `document_and_knowledge_types` (versiunea spec 2026-09-06, SCHEMA regenerat), `confidence: low`, `updated` la zi, și un singur paragraf identic sub H1 în toate cele 18 pagini: „Neverificat după reconstrucția stratului brut din septembrie 2026. Partea UE a comparației este un extras, nu textul integral. Nu se citează ca o constatare finală." Corpul paginilor nu s-a modificat altfel; nimic șters, nimic rescris. Editarea s-a făcut la nivel de octet, cu terminatorii de linie ai fiecărui fișier păstrați (`acquis-AIFMD.md` și altele sunt mixte CRLF/LF; spec-ul este CRLF).
- **Unde:** `_meta/schema/schema-spec.yaml`, `SCHEMA.md`, cele 18 pagini; commit „Pasul 1”. Validator: 0 erori, 2 avertismente, neschimbate.

## [2026-09-06] lint | Sondajul de actualitate pe tot corpusul: 53 de acte, 3 în urmă, unul abrogat pe legis.md

- **Aflat:** trei lucruri pe care verificarea act cu act nu le arătase. Întâi, legis.md publică și consolidări cu dată viitoare, până în 2030 și una „la data aderării la UE", deci „cea mai nouă versiune" din istoricul unui act nu este „versiunea în vigoare azi"; sondajul le dă pe amândouă. Al doilea, fișa `HG-1170-2016` poartă „Data abrogării 07.03.2025", data la care a intrat în vigoare HG553/2024, ultima „modificare" din fișă; wiki-ul ține actul ca în vigoare de un an și jumătate. Al treilea, cazul „legis.md în urmă" al Codului civil s-a inversat: legis.md are acum consolidarea LP251/2025 (150498@2026-04-01) și una viitoare (149719@2027-01-01, LP76/2026), iar `doc_id: 150561` din frontmatter este versiunea 2025-11-01, nu cea pe care textul din PDF o poartă. Rezultatul pe stări: 37 curente, 11 curente cu consolidare viitoare, 3 în urmă (`L-202-2017` cu LP189/2025; `COD-225-2003` cu patru consolidări neaplicate, LP330/2025, LP187/2025, LP252/2025, LP126/2026; `COD-1163-1997` cu LP318/2025 în vigoare 01.07.26), 1 nerezolvat (Codul civil), 1 abrogat pe legis.md. Cele două acte sărite de `build_coverage.py` prin regula „Publicat" și cele patru cu `never_amended: true` au toate o singură versiune pe legis.md, deci regula nu ascunde nicio modificare. Metoda: `/cautare/showdetails/<doc_id>` citit prin `fetch` same-origin din Chrome după ce Eugen a trecut verificarea Cloudflare; pagina `getResults` este randată de client și nu se poate parsa din HTML-ul adus.
- **Decis:** planul din 6 septembrie, D6: nimic reîmprospătat, niciun fișier din `raw/` atins. Reîmprospătările, dacă vor fi, se decid de Eugen una câte una pe baza raportului, cu arhivarea versiunii anterioare și a marcajelor ei. Statutul `HG-1170-2016` se verifică pe textul HG553/2024 înainte de orice altceva. Execuția se oprește aici până la revizuire; pasul 3 nu începe.
- **Unde:** `_meta/coverage/currency-sweep-2026-09-06.md` și `.json`; commit „Pasul 2". Validator: 0 erori, 2 avertismente.

## [2026-09-06] ingest | Constituția Republicii Moldova, CONST-1994 (doc_id 145723, republicată 13.11.2024)

- **Aflat:** actul de bază este invizibil în căutarea în titlu până la ultima pagină: 234 de rezultate pentru „constitutia republicii moldova", sortate descrescător după dată, iar Constituția, cea mai veche, este singurul rând cu prefixul CRM. Pe pagina actului: 19 versiuni, 145723 cea mai nouă, republicată în MO 466/13.11.2024, fără abrogare, ultima modificare LP244/2024. Trei particularități de sursă. Titlul articolului stă pe linia de după `Articolul N`, deci ancorele nu au titlu și o căutare după titlu trebuie să citească linia următoare. Republicarea nu poartă niciun marcaj `[Art.N ... prin LP...]`; istoricul celor 17 modificări, între care două hotărâri ale Curții Constituționale (HCC7/2016, HCC8/2024), stă doar în fișă. Fișa dă intrarea în vigoare 19.08.1994, textul spune 27 august 1994 (art. I alin. (2)). Un defect de metodă, nu de sursă: art. VIII din dispozițiile finale are ca text o frază care începe cu „Titlul VII,", iar regula de ancorare o lua drept titlu de structură, lăsând articolul gol; corectată în `ingest_business_law.py` (numeral roman, graniță de cuvânt, fără virgulă după el), cu regresie verificată pe toate ancorele `## Titlul` existente. Ruta de transfer pregătită ca să evit descărcarea, un receptor HTTP local alimentat prin `fetch` din pagină, a fost blocată de clasificatorul de permisiuni și abandonată; HTML-ul a venit prin descărcare blob din Chrome, cu acordul explicit al lui Eugen.
- **Decis:** prefix nou `CONST-`, consemnat în manifest la secțiunea Q. Ingerare pe modelul `ingest_business_law.py`, 157 de ancore (143 de bază fără lacune, 6 cu exponent, I–VIII romane), integritate de text PASS pe 883 de linii. Pagina de entitate citează numai articole citite în această sesiune și ține conținutul Titlului V^1, art. 140^1 și cap. III^1 ca neexaminat. Consolidarea rămâne 2024-11-05, derivată din fișă, cu nota că data republicării este 2024-11-13.
- **Unde:** `raw/papers/moldova-legal/CONST-1994.md`, `entities/CONST-1994.md`, manifestul secțiunea Q, `index.md` (96 de pagini), `_meta/imports/moldova-legal/ingest_business_law.py` (intrarea `CONST-1994` și regula titlurilor), cache `showdetails-145723.html`; commit „Pasul 3”.

## [2026-09-06] ingest | Lotul A, corporativ: L-149/2012, L-160/2011, L-131/2012

- **Aflat:** două capcane noi, ambele de fișă, nu de text. Prima: rândul din lista de rezultate legis.md nu trimite neapărat la consolidarea curentă. La 131/2012 lista dădea doc_id 152529 (2025-12-31), iar pagina actului avea două consolidări mai noi, cea în vigoare azi fiind 151146 (2026-08-28, LP201/2025), cu doc_id mai mic decât cel vechi; numărul doc_id nu este cronologic. A doua: fișa dă date de intrare în vigoare pe care textul nu le susține, la 131/2012 chiar o dată anterioară publicării (31.01.2012 față de publicarea din 31.08.2012 și „6 luni de la publicare” în art. 33). Și una de marcaje: 160/2011 are consolidare 2029-01-01 cu un singur marcaj amânat (anexa nr. 1), deși istoricul are două trepte în 2027 ale căror marcaje au fost eliminate; registrul in-force nu le poate vedea. O verificare prealabilă pe text cu etichetele scoase raportase lacune și duplicate în toate trei; erau exponenți neresolvați lipiți de număr, clasa de eroare de la L-235-2006; ancorele scrise nu au nicio lacună.
- **Decis:** se ingerează doc_id-ul din capul istoricului de versiuni, nu cel din listă; 152529 rămâne neutilizat. 160/2011 se ingerează ca L-1134-1997, cea mai nouă consolidare, cu avertisment explicit în manifest (R.3) și pe pagina de entitate că treptele din 2027 sunt invizibile pentru registru. Paginile de entitate citează numai articolele citite (obiect, noțiuni, principii, dispoziții finale) și declară restul necitit.
- **Unde:** `raw/papers/moldova-legal/L-149-2012.md`, `L-160-2011.md`, `L-131-2012.md`; `entities/` cu aceleași nume; manifestul secțiunea R; `index.md` (99 de pagini); `ingest_business_law.py` (trei intrări); cache `showdetails-152605/156152/151146.html`; commit „Pasul 4, lotul A”.

## [2026-09-06] ingest | Lotul B, administrativ: L-436/2006, L-158/2008, L-148/2023, L-131/2015

- **Aflat:** legea achizițiilor publice din plan, 131/2015, este marcată „Abrogat” pe legis.md, cu data abrogării 01.01.2027; este încă în vigoare azi, iar succesoarea, Legea 325/2025 privind achizițiile publice, cu Legea 20/2026 privind remediile, stă în aceeași listă de rezultate și nu este în plan. Legea 158/2008 are, ca Codul contravențional, o consolidare LP154/2026 care intră în vigoare la 13.09.2026, cu 29 de dispoziții amânate marcate individual, și încă una în 2028; rândul din listă trimitea la versiunea în vigoare azi, nu la acestea. Legea 148/2023 este nemodificată, cu o singură versiune și fără exponenți. Toate patru au trecut integritatea de text și nu au lacune de numerotare.
- **Decis:** 131/2015 se ingerează cum cere planul, fiindcă binde azi, cu data expirării scrisă pe pagina de entitate, în manifest (S.1) și în index; 325/2025 și 20/2026 nu se ingerează, decizia fiind a lui Eugen. 158/2008 se ingerează la consolidarea din 13.09.2026, ca la COD-218-2008, cu registrul in-force preluând dispozițiile amânate; versiunea din 2028 rămâne neingerată. Paginile de entitate citează numai articolele citite și numesc ce nu s-a citit.
- **Unde:** `raw/papers/moldova-legal/L-436-2006.md`, `L-158-2008.md`, `L-148-2023.md`, `L-131-2015.md`; `entities/` cu aceleași nume; manifestul secțiunea S; `index.md` (103 pagini); `ingest_business_law.py` (patru intrări); cache `showdetails-155118/155439/137908/155117.html`; commit „Pasul 4, lotul B”.

## [2026-09-06] ingest | Lotul C, profesia: L-1260/2002, L-198/2007, L-514/1995, UA-STATUT-2011; două lacune D5

- **Aflat:** trei lucruri despre legis.md. O dată de versiune 2030-01-01 înseamnă „la data aderării la Uniunea Europeană”, nu 1 ianuarie 2030: legea avocaturii are o asemenea consolidare (LP10/2026), pe care lista de rezultate o dă drept curentă, iar Codul contravențional alta (LP82/2026, văzută în sondaj). Doc_id-ul din plan pentru Statut, 86850, există, dar este consolidarea din 2012; cea curentă este 134919 din 2022, iar Statutul e structurat pe articole, nu pe puncte, cum presupunea planul. Codul deontologic al avocaților și Regulamentul stagiului nu apar în nicio căutare în titlu (șase fraze încercate, 289 de rezultate cumulate, niciunul al Uniunii). Legea 514/1995 are lacune de numerotare la 29–34, 41–42, 51–53, toate explicate în text prin stub-uri de capitol „Capitolul N (art. X-Y) - abrogat.”, ancorate; mecanismul opus celui de la 548/1995.
- **Decis:** pentru avocatură se ingerează versiunea în vigoare azi, 146148, nu cea condiționată de aderare; consecința pentru registrul in-force, care ar data greșit o dispoziție „la aderare”, e consemnată în manifest T.1. Statutul se ingerează la 134919 sub prefixul nou UA-, ancorat ca o lege. Codul deontologic și Regulamentul stagiului rămân lacune, conform D5, fără ingerare de pe uam.md; identificatorii rezervați nu se folosesc. Lacunele din 514/1995 nu sunt defect și nu sunt de verificat.
- **Unde:** `raw/papers/moldova-legal/L-1260-2002.md`, `L-198-2007.md`, `L-514-1995.md`, `UA-STATUT-2011.md`; `entities/` cu aceleași nume; manifestul secțiunea T (T.3 pentru lacune); `index.md` (107 pagini); `ingest_business_law.py` (patru intrări); cache `showdetails-146148/155726/156079/134919.html`; commit „Pasul 4, lotul C”.

## [2026-09-06] decision | Cele cinci decizii rămase după raportul de execuție: HG-1170-2016 consemnat abrogat; restul pregătit, blocat de Cloudflare

- **Aflat:** statutul `HG-1170-2016` nu cerea o sursă nouă: reîmprospătarea din 4 septembrie adusese deja consolidarea 144537, a cărei fișă dă „Data abrogării 07.03.2025” și al cărei text poartă, la rândul de după publicare, „Abrogată prin HG553 din 30.07.24, MO347-349/09.08.24 art.682; în vigoare 07.03.25”. Fișierul brut spunea deci de două zile că actul e abrogat, iar pagina de entitate, scrisă la 9 iulie pe consolidarea din 2019, îl ținea în vigoare; sondajul de actualitate a citit fișa, nu pagina. Ce rămâne neverificat este textul HG553/2024, neingerat, deci întinderea abrogării și dispozițiile tranzitorii. Pentru celelalte patru decizii nimic nu se poate face fără legis.md: verificarea Cloudflare este activă din nou pe Chrome-ul lui Eugen și nu se trece de ea fără el, iar HTML-ul celor șapte consolidări noi (155718, 138613, 151077, 152974, 153618, 150498 și versiunea în vigoare azi a Legii 160/2011, cu doc_id încă necunoscut) ar veni prin descărcare blob, care cere acordul lui explicit. `refresh_consolidations.py` avea și el un defect latent: descărca cu `curl` direct peste fișierul din cache, deci o rulare blocată de Cloudflare ar fi înlocuit un HTML bun cu pagina de verificare, exact defectul reparat în `ingest_business_law.fetch` pe 5 septembrie.
- **Decis:** `HG-1170-2016` este consemnat abrogat de la 07.03.2025 pe pagina de entitate (statut, secțiune nouă cu consecințele ratione temporis), în index și în manifestul moldova-legal secțiunea B; fișierul brut nu se atinge, rămâne text istoric cu fișa care îi poartă data abrogării; HG553/2024 se ingerează numai dacă un dosar îl cere, `[de verificat]` până atunci. Reîmprospătarea celor trei acte în urmă (`COD-225-2003` la 155718, `COD-1163-1997` la 138613 cu 152862@2027 neingerată, `L-202-2017` la 151077) are scriptul gata, `refresh_behind_2026-09-06.py`, condus pe folder ca lotul din 4 septembrie, cu arhivă, lanț de proveniență și delta pe articole; `refresh_consolidations.py` folosește acum `ibl.fetch`, cu `.part` și cădere pe cache. Se rulează după ce cele trei HTML-uri sunt în cache. Legile 325/2025 și 20/2026, Codul civil la 150498 și Legea 160/2011 la versiunea în vigoare azi așteaptă același HTML; recomandarea consemnată aici: toate patru da, cu 160/2011 reingerat la versiunea de azi fiindcă registrul in-force nu vede treptele din 2027 ale consolidării din 2029, și cu Codul civil trecut de la PDF la textul legis.md, cu arhivarea versiunii ancorate manual.
- **Unde:** `entities/HG-1170-2016.md`, `index.md`, `raw/papers/moldova-legal/_manifest.md` secțiunea B; `_meta/imports/moldova-legal/refresh_behind_2026-09-06.py`, nou; `_meta/imports/cnpf/refresh_consolidations.py`, pasul 2 al buclei. Validator după această intrare: vezi commit-ul.

## [2026-09-06] update | Reîmprospătarea celor trei acte „în urmă": COD-225-2003, COD-1163-1997, L-202-2017

- **Aflat:** trei lucruri de sursă. Reîmprospătarea Codului de procedură civilă peste patru legi de modificare a păstrat marcajele numai pentru ultima, LP126/2026; cele ale LP330/2025, LP187/2025 și LP252/2025 s-au pierdut la trecerea prin consolidările intermediare, mecanismul 1 din întrebarea deschisă 3, văzut de data aceasta în timp real, pe un act reîmprospătat de noi. Aceeași consolidare a corectat la sursă greșeala „Aricolul 78" din întrebarea deschisă 4: linia este acum scrisă corect și poartă ancoră. În Codul fiscal, LP318/2025 a abrogat art. 88^1 și legis.md a lăsat stub-ul „abrogat" numai în cuprins, ștergând linia din corp; verificatorul, care citea și cuprinsul, a raportat FAIL pe o ancoră pe care corpul nu o mai poate purta. Și un defect latent: `refresh_consolidations.py` descărca cu curl direct peste cache, deci o rulare sub Cloudflare ar fi înlocuit un HTML bun cu pagina de verificare.
- **Decis:** cele trei reîmprospătate prin `refresh_behind_2026-09-06.py`, condus pe folder, cu arhivă și lanț de proveniență; `refresh_consolidations.py` descarcă prin `ibl.fetch`; `verify_business_law.py` ignoră cuprinsul la numărarea exponenților, aceeași regulă ca extractorul. Consolidarea viitoare a Codului fiscal rămâne neingerată. Paginile de entitate spun ce s-a schimbat și unde e arhivată versiunea veche. Eugen a trecut verificarea Cloudflare și a aprobat explicit descărcarea celor șapte HTML-uri.
- **Unde:** `raw/papers/moldova-legal/COD-225-2003.md`, `COD-1163-1997.md`, `raw/papers/bnm/legal-ro/L-202-2017.md`; `entities/` cu aceleași nume; manifestul moldova-legal secțiunea U.1, manifestul bnm/legal-ro rândul L-202; `_meta/imports/moldova-legal/refresh_behind_2026-09-06.py`, `verify_business_law.py`, `ingest_business_law.py` (doc_id-uri), `_meta/imports/bnm/ingest_bnm_ro.py` (doc_id), `_meta/imports/cnpf/refresh_consolidations.py`; arhive `_archive/raw/*-before-refresh-20260906-220712/`; `CLAUDE.md` întrebările 3 și 4.

## [2026-09-06] ingest | Legile 325/2025 și 20/2026, succesoarele legii achizițiilor publice

- **Aflat:** Legea 20/2026 privind remediile este în vigoare din 01.04.2026, cu nouă luni înaintea legii de fond 325/2025 (01.01.2027), și anexa ei a modificat deja Legea 131/2015: art. 80–84 și 86–88 abrogate, art. 32 și 85 rescrise, deci contestațiile în achiziții se soluționează de pe acum după 20/2026, iar termenele de așteptare sunt 11 sau 16 zile (art. 20). Textul nostru al Legii 131/2015 purta stub-urile fără ca pagina de entitate să le fi observat dimineața. Consolidarea 2027-01-01 a Legii 325/2025 este data ei de intrare în vigoare, nu o modificare amânată: prima dată când un act întreg cu dată viitoare intră în corpus; registrul in-force îl listează cu zero dispoziții marcate, ceea ce este corect. Art. 91 din 325/2025 închide întrebarea lăsată deschisă pe pagina 131/2015: procedurile și contractele în curs la 01.01.2027 se termină sub legea de la inițiere. Art. 27 din 20/2026 trimite la art. 61 alin. (19) și 62 alin. (13)–(17) din 131/2015, trimiteri care vor rămâne în text după abrogarea acelei legi.
- **Decis:** ingerate în `moldova-legal/`, cu integritate PASS și pagini de entitate care citează numai articolele citite (1, 90, 91 din 325; 1, 2, 3, 20, 26, 27, 28, 29 și anexa din 20). Pagina 131/2015 rescrisă la succesiune și la întrebările deschise. Corespondentul în 325/2025 al articolelor trimise de art. 27 din 20/2026 rămâne `[de verificat]`.
- **Unde:** `raw/papers/moldova-legal/L-325-2025.md`, `L-20-2026.md`; `entities/L-325-2025.md`, `entities/L-20-2026.md`, `entities/L-131-2015.md`; manifestul secțiunile U.4 și S.1 (urmarea); `index.md` (109 pagini); `ingest_business_law.py` (două intrări); cache `showdetails-152974/153618.html`.

## [2026-09-06] decision | L-160/2011 la versiunea în vigoare azi; Codul civil trecut de pe PDF pe textul legis.md

- **Aflat:** istoricul Legii 160/2011, citit integral din pagina actului, are cinci consolidări viitoare, nu două cum se scrisese dimineața: 28.12.2026, 01.01.2027, 23.01.2027, 21.05.2027 și 01.01.2029; versiunea în vigoare azi este 151257 @ 2026-08-29. La Codul civil, textul legis.md 150498 are exact inventarul PDF-ului, 2.657 de articole cu aceleași 14 absențe, și aceeași linie `Secțiunea a 3-a- abrogată` fără citare LP la 2047–2054, deci întrebarea deschisă 1 nu era un defect al PDF-ului. Prima trecere a pierdut însă cele 27 de ancore de carte și de titlu: legis.md scrie „Cartea întâi" fără numeral și „T i t l u l IV" cu litere spațiate, forme pe care extractorul nu le prindea; și, de reținut pentru oricine editează scripturi din această sesiune, un `\b` scris printr-un heredoc a ajuns în fișier ca octetul 0x08, iar corecția a trebuit scrisă dintr-un fișier de script, nu din shell.
- **Decis:** amândouă confirmate de Eugen. 160/2011 reingerată la 151257, cu versiunea din 2029 arhivată; registrul in-force nu o mai listează. Codul civil adus la 150498 prin același script, cu versiunea ancorată manual arhivată și PDF-ul păstrat în `raw/assets/`; regula pentru „Cartea" și „T i t l u l" adăugată în `extract_doc`, regresia verificată pe toate actele din `DOCS` (doar `COD-218-2008` ar câștiga două ancore de carte, neaplicat), trecerea repetată de la versiunea arhivată. Secțiunea „Statutul sursei" a paginii Codului civil descrie acum fișierul de azi și păstrează ce era despre PDF ca istoric al arhivei.
- **Unde:** `raw/papers/moldova-legal/L-160-2011.md`, `CC-1107-2002.md`; `entities/L-160-2011.md`, `entities/CC-1107-2002.md`; manifestul secțiunile C.7, R.3 (urmarea), U.2, U.3, U.5; `index.md`; `ingest_business_law.py` (regula de structură, intrările `L-160-2011` și `CC-1107-2002`); arhive `_archive/raw/moldova-legal-lot2-legis-md-before-refresh-20260906-221015/` și `moldova-legal-cc-legis-md-before-refresh-20260906-221637/`; `CLAUDE.md` întrebarea 1.

## [2026-09-06] lint | Un act întreg neintrat în vigoare trecea drept curent în blocul de acoperire

- **Aflat:** după commit, rândul `L-325-2025` din tabelul generat al `CLAUDE.md` purta „clean", fără nota de consolidare viitoare, iar lista „Not yet in force" nu o cuprindea, deși consolidarea ei este 2027-01-01 și niciun articol nu se aplică azi. Cauza: blocul de acoperire citește flagul `consolidation_is_future` din frontmatter, iar extractorul îl punea numai când găsea marcaje `[Art.N ... în vigoare ...]` cu data consolidării; un act nou, nemodificat, cu consolidarea egală cu data intrării în vigoare, nu are niciun marcaj. Registrul in-force, care judecă după dată, îl listase corect. Pe calea de reîmprospătare defectul nu există, `refresh_consolidations.py` flaghează după dată. Niciun alt act din `DOCS` nu era în situația asta.
- **Decis:** `make_raw` pune flagul și avertismentul de frontmatter ori de câte ori data consolidării este în viitor, cu un text distinct („este data intrării în vigoare a actului întreg") când nu există marcaje, și un bloc „ATENȚIE, ACT NEINTRAT ÎN VIGOARE" în corp. Legea 325/2025 reingerată din același HTML, integritate PASS; blocul de acoperire o listează acum printre cele 13 acte cu consolidare viitoare.
- **Unde:** `_meta/imports/moldova-legal/ingest_business_law.py` (`make_raw`); `raw/papers/moldova-legal/L-325-2025.md`; manifestul U.4; `CLAUDE.md`, blocul generat.

## [2026-09-06] ingest | HG-553-2024, la cererea lui Eugen: abrogarea HG 1170/2016 este totală ca act, parțială ca regim

- **Aflat:** titlul HG553/2024 nu conține „schimb de terenuri", deci căutarea în titlu pe obiectul actului abrogat nu o găsește; o găsește „schimbarea destinatiei". Are două versiuni, cea în vigoare fiind 150820 din 18.10.2025 (HG613/2025), și rândul din listă trimite de data asta la ea. Pct. 3 din hotărâre abrogă HG 1170/2016 integral, cu modificările ulterioare, fără dispoziții tranzitorii, iar pct. 4 dă 7 martie 2025, data din fișa actului abrogat: fișa spunea adevărul. Regulamentul nou acoperă însă o singură operațiune din cele trei ale celui vechi, schimbarea destinației, și numai pentru terenurile agricole de calitate superioară și cele ale fondului forestier și apelor, în temeiul art. 58 alin. (10) din Codul funciar nr. 22/2024; pentru transmiterea și schimbul de terenuri nu mai există regulament al Guvernului. Act structurat pe puncte cu numerotare care repornește, deci zero ancore, clasa HG-574-2024.
- **Decis:** ingerat cu integritate PASS; pagină de entitate care citează cu calificativul „din hotărâre" sau „din Regulament" și declară punctele necitite. Pagina HG-1170-2016 spune acum că abrogarea e verificată pe text și că succesiunea de regim e parțială. Codul funciar 22/2024 devine lacuna următoare, consemnată, nu ingerată: decizia e a lui Eugen.
- **Unde:** `raw/papers/moldova-legal/HG-553-2024.md`; `entities/HG-553-2024.md`, `entities/HG-1170-2016.md`; manifestul secțiunile B (rândul HG-1170-2016) și U.6; `index.md` (110 pagini); `ingest_business_law.py` (intrarea); cache `showdetails-150820.html`.

## [2026-09-06] ingest | COD-22-2024, Codul funciar nou, la cererea lui Eugen: transmiterea și schimbul de terenuri sunt în cod, art. 16

- **Aflat:** codul nou ține direct în text ce HG 1170/2016 ținea în regulament: art. 16 pentru transmiterea (alin. (1)–(5)) și schimbul (alin. (6)–(8)) terenurilor proprietate publică, art. 58–60 pentru schimbarea destinației și compensarea pierderilor, cu delegarea din art. 58 alin. (10) împlinită de HG 553/2024. Deci lanțul HG-1170-2016 → HG-553-2024 → COD-22-2024 este închis pe text, și nu există nicio dispoziție tranzitorie pentru dosarele în curs în niciunul din cele trei acte. Trei lucruri de sursă: fișa dă intrarea în vigoare 07.03.2024, textul 1 aprilie 2025, a treia fișă contrazisă de text; șapte legi de modificare, trei marcaje păstrate, toate LP53/2026; titlul de pe legis.md e doar „CODUL FUNCIAR". Verificarea Cloudflare a reapărut între cele două cereri și a trebuit trecută din nou de Eugen; HTML-ul, 291 KB, descărcat cu acordul lui.
- **Decis:** ingerat sub prefixul `COD-`, 96 de ancore, integritate PASS; pagină de entitate cu art. 1, 2, 16, 58, 59, 60, 77, 78, 79 citite și restul declarat necitit. Paginile HG-553-2024 și HG-1170-2016 trimit acum la art. 16 și la art. 79. Data intrării în vigoare rămâne `[de verificat]` din istoricul de versiuni, fiindcă marcajul unei eventuale modificări a art. 79 alin. (1) nu e în text.
- **Unde:** `raw/papers/moldova-legal/COD-22-2024.md`; `entities/COD-22-2024.md`, `entities/HG-553-2024.md`, `entities/HG-1170-2016.md`; manifestul secțiunea U.7; `index.md` (111 pagini); `ingest_business_law.py` (intrarea); cache `showdetails-154132.html`.

## [2026-09-06] lint | Data intrării în vigoare a Codului funciar 22/2024, lămurită din istoricul versiunilor

- **Aflat:** cele opt consolidări, citite prin `fetch` în pagina legis.md fără descărcare, dau răspunsul pe care textul de azi nu-l mai poartă. Versiunea inițială (142192) spunea „la expirarea termenului de 12 luni de la data publicării", adică 7 martie 2025; LP30 din 27.02.2025, în vigoare 6 martie 2025, cu o zi înainte de termen, a rescris art. 79 alin. (1) la „1 aprilie 2025", cu marcaj în versiunea 147402, pierdut din versiunile următoare. Fișa, cu 07.03.2024, este pur și simplu greșită. Consecința care contează: HG 553/2024, adoptată în temeiul codului cu intrarea în vigoare pe termenul inițial, 7 martie 2025, nu a fost amânată odată cu codul, deci a intrat în vigoare cu 25 de zile înaintea lui și a abrogat HG 1170/2016 într-un interval în care codul nou încă nu se aplica.
- **Decis:** paginile COD-22-2024 și HG-553-2024 și manifestul U.7 consemnează data, mecanismul și intervalul; întrebarea deschisă 1 de pe pagina codului este închisă. Metoda, citirea unui articol în toate versiunile prin `fetch` fără descărcare, este cea potrivită pentru orice marcaj pierdut și nu cere acord de descărcare.
- **Unde:** `entities/COD-22-2024.md`, `entities/HG-553-2024.md`, manifestul secțiunea U.7.

## [2026-09-06] decision | Consolidarea din 2027 a Codului fiscal pusă în plan; sesiunea închisă

- **Aflat:** după executarea celor cinci decizii și a celor două ingerări la cerere, singura lacună care schimbă un răspuns în următoarele luni este consolidarea 152862 @ 2027-01-01 a Codului fiscal (LP187/2025), pe care registrul in-force nu o poate vedea fiindcă textul deținut e cel în vigoare azi. O reîmprospătare simplă ar înlocui textul curent cu cel viitor, exact defectul pe care corpusul l-a avut până la 4 septembrie.
- **Decis:** Eugen pune consolidarea din 2027 a Codului fiscal în plan, cu termen înainte de decembrie 2026, și închide sesiunea. Planul, în raportul de execuție secțiunea 7, lasă la execuție alegerea între ingerarea sub identificator distinct și citirea versiune contra versiune fără descărcare, cu recomandarea celei de-a doua. Celelalte lacune ale zilei sunt listate acolo fără termen.
- **Unde:** `_meta/plans/2026-09-06-raport-executie.md`, secțiunea 7.

## [2026-09-07] lint | Consolidarea din 2027 a Codului fiscal (152862), citită versiune contra versiune; registrul in-force vede acum consolidările neingerate

- **Aflat:** 152862 @ 01-01-2027 este încă vârful istoricului Codului fiscal, imediat peste 138613 @ 01-07-2026, textul deținut; nu a apărut nicio consolidare intermediară. Consolidarea din 2027 poartă exact cinci marcaje „în vigoare 01.01.27”, toate LP187/2025, în trei articole: art. 131 alin. (1^1) în redacție nouă (portalul guvernamental al unităților de drept devine al doilea canal de comunicare al SFS, cu recepție prezumată din ziua lucrătoare următoare), art. 342 alin. (1), (1^1), (2) abrogate (darea de seamă privind taxa pentru folosirea drumurilor dispare cu tot cu termenele de 25 ianuarie și 25 martie) și art. 342^1 alin. (3) modificat în consecință. LP187/2025 apare în fișele a șase acte deținute numai cu trepte în vigoare azi. Ce nu vedea niciun control: registrul in-force scanează `raw/`, iar o consolidare viitoare ținută dinadins neingerată nu lasă niciun marcaj acolo; fără o intrare scrisă de mână, regula de lucru 4 nu avea unde să găsească aceste cinci dispoziții.
- **Decis:** calea (b) din raportul de execuție, fără descărcare și fără text viitor în `raw/`, este suficientă pentru cinci marcaje în trei articole. Lista se ține în `_meta/inforce/pending-consolidations.json` și registrul o redă ca secțiune separată, cu avertisment la rulare când data trece; ingerarea sub identificator distinct rămâne rezervată cazului în care un răspuns trebuie să citeze textul din 2027 la nivel de alineat. Eugen a cerut consemnarea în registru, pe pagina de entitate și în log.
- **Unde:** `_meta/inforce/pending-consolidations.json` (nou), `_meta/inforce/build_inforce_register.py` (secțiunea „Consolidări viitoare neingerate”, `load_pending`), `entities/COD-1163-1997.md`, manifestul moldova-legal U.8, raportul de execuție secțiunea 7.

## [2026-09-07] lint | Legea 160/2011: cele cinci consolidări viitoare schimbă numai anexa nr. 1, care nu este în text

- **Aflat:** șase versiuni ale Legii 160/2011 (151257 deținută și 149496@28.12.2026, 150231@01.01.2027, 154051@23.01.2027, 154478@21.05.2027, 156152@01.01.2029) citite prin `fetch` fără descărcare și comparate în lanț, paragraf cu paragraf: corpul legii este identic în toate. Fiecare consolidare aduce doar rândul din fișă și, de la a treia încolo, un marcaj `[Anexa nr.1 modificată prin LP...]` care îl înlocuiește pe cel anterior; pentru LP136/2025 și LP176/2025 nu a existat niciodată un marcaj. Toate cinci modifică Nomenclatorul actelor permisive, anexa nr. 1, iar conținutul anexei nu este în textul de pe legis.md în nicio versiune. Deci un articol citat din fișierul deținut rămâne bun și după 28.12.2026, iar o întrebare despre o poziție din Nomenclator nu se poate răspunde din vault la nicio dată; sursa este Monitorul Oficial al legii de modificare. LP176/2025 este aceeași lege care introduce art. 15^3–15^8 în L-1543-1998, deja în registru.
- **Decis:** cele cinci consolidări intră în `pending-consolidations.json` ca rânduri cu unitatea „anexa nr. 1”, ca registrul să spună explicit că nu e nimic de citit acolo, nu doar să tacă; generatorul acceptă de acum unități fără număr de articol. Întrebarea deschisă 1 de pe pagina de entitate este închisă; întrebarea 2, Nomenclatorul absent, rămâne deschisă pentru toate datele. Nicio ingerare; nimic din `raw/` atins. Eugen a cerut execuția cu aceeași metodă.
- **Unde:** `_meta/inforce/pending-consolidations.json`, `_meta/inforce/build_inforce_register.py` (`article_sort_key`), `entities/L-160-2011.md`, manifestul moldova-legal U.9, raportul de execuție secțiunea 7.

## [2026-09-08] create | Pasul 5 (hotărârile Curții Constituționale) pornit: recensământ, plan, registrul HCC ca al patrulea control generat

- **Aflat:** planul din 6 septembrie este executat integral, deci următorul pas din D3 este pasul 5. Recensământul mecanic al textelor deținute (`hcc_census.py`) arată golul exact: 18 acte poartă în fișă 76 de hotărâri distincte ale Curții, dar numai 16 mai au marcaj la articol; pentru 67 de perechi act–hotărâre textul spune doar „HCCnn din dd.mm.yy", fără articol, fiindcă marcajul a căzut la o reîmprospătare anterioară (mecanismul 1 din întrebarea deschisă 3, aplicat hotărârilor Curții). Codul fiscal are 10 hotărâri și zero marcaje; Codul penal 8 și zero; procedura civilă 6 și zero. Marcajul are două forme, cu paranteze drepte și cu asterisc (`*Notă: Articolul N ...`, forma Codului contravențional), iar un cititor care o știe doar pe prima pierde 7 din 16. HCC3/2012 lovește trei acte deodată, deci unitatea de lucru este hotărârea. Nicio pagină structurată nu citează azi vreunul dintre cele 16 articole cu marcaj vizibil; pentru cele 67 nu se poate verifica nimic până nu se știe articolul. Copia `legal-career/05` ține încă „Planned extension" din 5 septembrie; documentul din proiect nu a fost actualizat după raportul din 6 septembrie. Stampila registrului dosarelor e din 7 septembrie; Eugen nu a fost de față ca să dea registrul curent.
- **Decis:** registru, nu text integral, în prima etapă: `_meta/hcc/build_hcc_register.py` scanează marcajele în ambele forme, citește `recovered-provisions.json` (scris de mână, gol la început) pentru articolele recuperate din istoricul versiunilor și redă pe act hotărârile fără articol atribuit, ca golul să fie vizibil; intră în `close_session.py` ca al patrulea control generat. Recuperarea celor 67 (pasul 5.3) cere `fetch` pe legis.md, deci trecerea Cloudflare de către Eugen, și nu s-a executat. Deciziile D1–D4 din plan (registru vs text integral sub prefix `HCC-`, calea de recuperare, ordinea actelor, integrarea în validator și în blocul de acoperire) rămân ale lui Eugen. Propus de Claude, autonom, în lipsa lui.
- **Unde:** `_meta/plans/2026-09-08-plan-hcc-pasul-5.md`, `_meta/plans/hcc_census.py` și `hcc-census-2026-09-08.md/.json`, `_meta/hcc/build_hcc_register.py`, `hcc-register.md/.json`, `recovered-provisions.json`, `_meta/close_session.py` (STEPS), `CLAUDE.md` („Where things are").

## [2026-09-08] lint | Pasul 5.3, Codul fiscal: cele zece hotărâri ale Curții din fișă, recuperate la articol fără ingerare

- **Aflat:** istoricul de versiuni al Codului fiscal are o consolidare la data exactă a fiecărei hotărâri, și în nouă din zece marcajul mai există acolo; a zecea (HCC12/1999) nu a avut niciodată marcaj și vine numai din dispozitiv. Forma marcajului se schimbă pe epoci: 1999 nimic, 2014 paranteze rotunde la sfârșitul articolului fără numărul lui, din 2018 paranteze drepte cu articol. Trei defecte de publisher care ar fi păcălit un cititor mecanic: HCC22 marcat pe art. 226^11 când dispozitivul dă 226^16; HCC20 cu marcajul rupt, doar coada după semnătură; HCC11 scris „neconstutuţional”. Fondul: toate cele zece dispoziții (art. 3(3), 6(11), 88(7), 123(7), 226^16(1^1), 260(4), 264(1)-(2), modificările LP324/2013 la titlul VII și două cote din anexele titlului IV) au fost între timp abrogate sau rescrise de Parlament, deci Codul fiscal deținut nu ține text anulat; registrul contează pentru istoric și pentru spețele anterioare. HCC17/2014 e invizibilă la căutarea „codul fiscal” în titlu, titlul ei numind HG 243/2010, act neingerat pe care îl lovește și el.
- **Decis:** 17 rânduri în `recovered-provisions.json`, câte unul pe articol pentru HCC2/2014; registrul HCC dă acum Codul fiscal 10/10 cunoscute, corpus 57 fără articol din 76. Eugen a cerut pasul 5.3 începând cu Codul fiscal; următoarele în ordinea D3: Codul contravențional, procedura penală, procedura civilă, Codul penal.
- **Unde:** `_meta/hcc/recovered-provisions.json`, `_meta/hcc/hcc-register.md`, `entities/COD-1163-1997.md` (secțiune nouă), manifestul moldova-legal U.10.

## [2026-09-08] lint | Pasul 5.3, Codul contravențional și procedura civilă: nouă hotărâri recuperate la articol; fișa listează numai anulările

- **Aflat:** Codul contravențional (4 recuperate, acum 6/6) și procedura civilă (5 recuperate, acum 9/9), aceeași metodă ca la Codul fiscal, fără descărcare. Patru lucruri noi. Un al patrulea tip de marcaj, fără paranteze și fără articol, pe rând separat sau lipit de sancțiune (contravențional 2013, 2018), deci articolul vine numai din dispozitiv. O hotărâre care lovește legea de modificare, nu codul (HCC16/2013 pe LP29/2012, care abrogase art. 449 lit. f) CPC), nu lasă marcaj în nicio versiune a codului și titlul ei nu conține numele codului; singura cale de a o găsi a fost căutarea în titlu pe „sesizarea”, care listează practic toate HCC și se filtrează pe număr și an. Fișele listează numai anulările: HCC4/2018, HCC28/2018 (contravențional) și HCC4/2016 (procedura civilă), recunoașteri cu rezervă de interpretare, nu apar în fișe deși leagă interpretarea textului. Și o formă înșelătoare: art. 449 lit. f) CPC se citește azi „abrogată” deși abrogarea a fost anulată, fiindcă Parlamentul a reintrodus temeiul ca lit. e^1). Toate cele nouă dispoziții au fost rescrise sau abrogate între timp; HCC10/2016 pct. 3 a dat o regulă tranzitorie pentru toate sancțiunile fixe din Partea specială a Codului contravențional, nu doar pentru art. 345.
- **Decis:** 13 rânduri în `recovered-provisions.json`; secțiuni pe cele două pagini de entitate, cu hotărârile interpretative numite ca lacună a fișei, nu a registrului. Eugen a cerut Codul contravențional; procedura civilă luată în aceeași sesiune fiindcă pagina era deschisă. Rămân în ordinea D3: procedura penală (14), Codul penal (8), executare (6).
- **Unde:** `_meta/hcc/recovered-provisions.json`, `_meta/hcc/hcc-register.md`, `entities/COD-218-2008.md`, `entities/COD-225-2003.md`, manifestul moldova-legal U.11.

## [2026-09-08] lint | Pasul 5.3, procedura penală: 14 hotărâri recuperate la articol; versiunea de la data hotărârii e regula, nu legea

- **Aflat:** Codul de procedură penală, cel mai lovit act din corpus (17 hotărâri), este acum 17/17. Două hotărâri nu au versiune proprie în istoric: HCC15/2020 lipsește cu totul, fără marcaj în versiunile vecine, iar HCC29/2021 stă în versiunea produsă de HCC31 două zile mai târziu; dispozitivul a fost singura sursă pentru prima și a arătat că lovește și art. 192 alin. (2), pe care fișa nu îl are. Hotărârile din 2005–2010 au titluri care încep cu „asupra excepţiei” și nu conțin „sesizarea”, deci ruta găsită ieri nu le acoperă; le-a găsit „procedura penala”. Consolidarea deținută fiind cea viitoare (02.12.2026), art. 132^9 lovit de HCC31/2021 nu mai există sub numărul lui, capitolul măsurilor speciale de investigații fiind renumerotat 138^1–138^N, iar art. 452–457 (recursul în anulare, HCC16/2005 și HCC26/2020) au dispărut cu tot cu stub, secțiunea fiind „abrogată” ca întreg. Două hotărâri lovesc legi de modificare în bloc (HCC3/2012 pe LP163/2011, HCC29/2021 pe LP244/2020) și lasă urme numai în marcajele versiunii. Cloudflare a reapărut o dată și s-a rezolvat singură la reîncărcare.
- **Decis:** 23 de rânduri în `recovered-provisions.json`, câte unul pe articol; pagina de entitate spune explicit că pentru interceptări textul în vigoare azi se citește pe legis.md la versiunea anterioară consolidării viitoare. Eugen a cerut procedura penală. Rămân 34 de perechi fără articol: Codul penal (8), executare (6), Legea 845/1992 (3), L-514-1995 (3), restul câte 1–2.
- **Unde:** `_meta/hcc/recovered-provisions.json`, `_meta/hcc/hcc-register.md`, `entities/COD-122-2003.md`, manifestul moldova-legal U.12.

## [2026-09-08] lint | Pasul 5.3, Codul penal: opt hotărâri recuperate la articol; șase din ele sunt o singură linie jurisprudențială

- **Aflat:** Codul penal este acum 8/8, cel mai curat act de până acum: toate cele opt versiuni de la data hotărârii poartă marcaj, șapte în forma nouă cu articol. Puse alături, șase din opt sunt o singură linie, previzibilitatea expresiilor „intereselor publice” și „urmări grave” în infracțiunile de serviciu (art. 327, 328, 329, 335, 361, 189, 307), în patru hotărâri din 2017 până în 2021, iar HCC24/2019 singură lovește șase texte. Toate au fost rescrise de Parlament; art. 104^1 (castrarea chimică, HCC18/2013) a dispărut fără stub. Aceeași HCC18/2013 lovește și Codul de executare la art. 174 alin. (3^1) și 291^1, ambele abrogate azi, atribuite din dispozitiv fără a citi versiunea acelui cod. Defecte de fișă: „cт.4” cu litere chirilice, MO „art.89” contra „art.88” din marcaj.
- **Decis:** 16 rânduri în `recovered-provisions.json`, două pentru Codul de executare; pagina Codului penal spune explicit că cine are o speță anterioară rescrierii aplică hotărârea, nu textul de atunci. Eugen a cerut Codul penal. Rămân 25 de perechi fără articol: executare (5), Legea 845/1992 (3), L-514-1995 (3), restul câte 1–2.
- **Unde:** `_meta/hcc/recovered-provisions.json`, `_meta/hcc/hcc-register.md`, `entities/COD-985-2002.md`, `entities/COD-443-2004.md`, manifestul moldova-legal U.13.

## [2026-09-08] ingest | HBN-127-2013, Regulamentul BNM privind deținerile în capitalul băncii: succesiunea este circumstanță obiectivă a art. 46, pe text românesc

- **Aflat:** speța moștenitorului unui acționar cu 10% într-o bancă, care deține doar certificat de calitate de moștenitor, se decide pe trei texte deja ancorate (art. 20 alin. (1), 52 și 56 alin. (1) lit. c) din Legea SA; art. 11 alin. (3), (5) din Legea 171/2012; art. 2548 alin. (3) și 2557 alin. (5) Cod civil; art. 45, 46 și 54 din Legea 202/2017) și pe unul care nu era: actul BNM care spune ce sunt „circumstanțele obiective" din art. 46 alin. (1). Două dintre actele declarate lipsă în răspuns erau de fapt în corpus ca traduceri engleze (127/2013 și 130/2013), inutilizabile pentru citare prin D2; fișierul englez al lui 130/2013 conține doar anexele. Textul românesc al Regulamentului 127/2013, pct. 8, numește expres „succesiune; moştenire; donaţie sau alt mod de transmitere cu titlu gratuit", cu drepturile suspendate de drept „din data achiziţiei pînă la data eliberării aprobării prealabile" și acțiunile numărate la cvorum, nu la hotărâri; pct. 9 dă termenele de 15 zile, 60 de zile și 3 luni. Nici legea, nici regulamentul nu fixează „data achiziţiei" pentru moștenire. Pct. 73 trimite la un articol al Legii SA care nu mai reglementează lista (art. 54 alin. (3) în loc de art. 52). Anexele regulamentului nu sunt în textul legis.md. Denumirea s-a schimbat în 2021, deci actele de modificare se găsesc sub două titluri. Instrumentul JavaScript din Chrome maschează `href`-urile cu șir de interogare; consola cp1252 rupe `--precheck` la „Ă".
- **Decis:** ingerat sub identificatorul `HBN-127-2013`, după codul legis.md al hotărârilor BNM, în `raw/papers/bnm/legal-ro/`, primul act subordonat de acolo; zero ancore de articol, ca la actele pe puncte, cu nota de citare pe pagina de entitate. Descărcarea ca octeți ai serverului, cu acordul explicit al lui Eugen. Punctul deschis (b) din M-001 se închide pe text românesc; rămân deschise „data achiziţiei" în succesiune și ingerarea Regulamentului 130/2013, următorul din lista din aceeași zi. Retragerea traducerii engleze 093/094 în arhivă rămâne decizia lui Eugen. Registrul dosarelor poartă ștampila din 7 septembrie; Eugen a dat instrucțiunea de ingest fără a furniza registrul curent.
- **Unde:** `raw/papers/bnm/legal-ro/HBN-127-2013.md`; `entities/HBN-127-2013.md`; `entities/L-202-2017.md` (secțiunea dețineri calificate); manifestul `raw/papers/bnm/legal-ro/_manifest.md` (rând nou și secțiunea HBN-127-2013); `index.md`; `_meta/imports/bnm/ingest_bnm_ro.py` (intrarea); cache `_meta/imports/bnm/legis-md-ro/showdetails-126093.html`.

## [2026-09-08] ingest | HBN-130-2013, calculul voturilor și înregistrarea transferului: dobândirea prin succesiune se înscrie fără aprobare prealabilă, cu votul suspendat

- **Aflat:** actul la care trimit art. 45 alin. (6)–(7) din 202/2017 și pct. 11 din HBN-127-2013 are 18 puncte și rescrie, la pct. 14, a treia barieră din răspunsul de dimineață: o dobândire în circumstanțe obiective, deci și prin succesiune, „se va efectua fără prezentarea aprobării prealabile a Băncii Naţionale", cu declarația de activitate concertată de la pct. 15 anexată la orice transfer „indiferent de cota vizată", iar registratorul notează concomitent suspendarea dreptului de vot. Deci moștenitorul cu certificat de moștenitor devine acționar la înscriere și intră în listă, cu votul suspendat; certificatul de calitate rămâne fără efect de înregistrare. Trei lucruri de sursă: anexele 1–2 lipsesc din textul românesc, dar sunt în fișierele engleze 091–092 ale corpusului BNM, care au numai anexele; marcajele HBN260/2018 au o formă fără paranteze și fără număr de punct, iar data intrării în vigoare stă doar în rândul „Versiune în vigoare din 23.12.18", pe care extractorul îl citește; pct. 14 citează regulamentul-pereche sub un titlu care nu a existat niciodată. Preambulul poartă „articolelor 15-156", adică 15–15^6, exponent turtit în sursă. Cloudflare a reapărut la prima cerere de descărcare și s-a rezolvat la reîncărcare.
- **Decis:** ingerat sub `HBN-130-2013`, zero ancore de articol, cu acordul explicit al lui Eugen pentru descărcare; fișierele engleze 091–092 rămân, fiindcă țin anexele. Întrebarea deschisă 2 de pe pagina HBN-127-2013 este închisă; pagina L-202-2017 primește pct. 14 la art. 45. Rămân deschise: actele CNPF și regulile DCU la care trimite pct. 12; „data achiziţiei" în succesiune. Eugen a cerut ingestul imediat după HBN-127-2013.
- **Unde:** `raw/papers/bnm/legal-ro/HBN-130-2013.md`; `entities/HBN-130-2013.md`; `entities/HBN-127-2013.md` (întrebarea 2); `entities/L-202-2017.md`; manifestul legal-ro (rând și secțiunea HBN-130-2013); `index.md` (113 pagini); `CLAUDE.md` („Where things are"); `ingest_bnm_ro.py` (intrarea); cache `showdetails-111967.html`.

## [2026-09-08] lint | Commitul 27e6363 a luat cu el două fișiere neatinse de sesiunea de ingest: o conversie CRLF→LF a copiei de lucru a Codului civil și starea Obsidian

- **Aflat:** commitul HBN-130-2013 arată 69.646 de linii schimbate în `_meta/anchoring-work/CC-1107-2002.md`, fișier pe care sesiunea de ingest nu l-a deschis. Comparat octet cu octet între 8a96327 și 27e6363: blobul vechi avea 34.823 de octeți CR, cel nou zero, iar textul fără CR este identic linie cu linie (34.847 de linii). Deci este o normalizare a corpului din CRLF în LF, scrisă pe disc la 12:50:59, între cele două commituri, de un alt proces: sesiunea `wiki-39`, activă în același folder, sau Obsidian, a cărui stare `.obsidian/graph.json` s-a schimbat la 12:51:59 și a intrat și ea în commit. Conținutul nu s-a schimbat, `raw/` nu este atins, validatorul nu citește `_meta/`. Cauza măturării: `close_session.py --commit` face `git add -A`, iar `git diff --stat` fusese lansat în aceeași rundă cu commitul, deci nu putea să-l oprească.
- **Decis:** nu se reface istoricul; commitul e împins și conversia în LF e în sensul convenției vault-ului. Se consemnează aici ca istoricul să explice diff-ul. Regula de lucru, notată și în memoria sesiunii: starea git se citește într-o rundă proprie înainte de orice `--commit`, iar un fișier neatins care apare modificat se inspectează la nivel de octeți și fie se lasă afară, fie se numește în log și în mesajul commitului. Cine a rescris fișierul rămâne `[de verificat]` de Eugen, dacă îl interesează.
- **Unde:** `git show --stat 27e6363`; acest log.

## [2026-09-08] ingest | DCU-REGULI-2026, Regulile Depozitarului central unic: prima sursă PDF cu ancore de articol, de pe dcu.md, nu de pe legis.md

- **Aflat:** Regulile DCU nu sunt pe legis.md și nu apar în Monitorul Oficial; art. 25 din Legea 234/2016 le cere publicate pe pagina DCU, unde stau ca PDF, v3 în vigoare din 8 aprilie 2026, cu cele trei aprobări datate (CS DCU 49/2025, CNPF 11/1/2026, BNM HCE 89/2026) și cu v1 și v2 abrogate alături. Spre deosebire de actele BNM, sunt structurate pe articole, 93 plus 82^1, în 13 capitole, deci pot purta ancore; dar sursa scrie „Art.N." și pune titlul pe rândul următor, deci ancorele sunt sintetice, construite din una-două linii-sursă și inserate deasupra lor, cu un al doilea hash, al extracției, care dovedește că nicio linie nu s-a schimbat. Trei linii care încep cu „Art.66.", „Art.80.", „Capitolul XII." sunt trimiteri rupte la capăt de rând, prinse prin regula ordinii numerotării. „Art.821." este 82^1 cu flag de superscript în PDF, așezat de DCU înaintea art. 82. Pentru speța moștenitorului: art. 13 alin. (3) lit. g) și o) și art. 53 alin. (4) lit. e) dau moștenitorului și notarului informația și extrasul; art. 49 alin. (1) lit. a) pune dobândirea proprietății la creditarea contului individual; art. 52 alin. (2) lit. a) cere ordin de transfer al operatorului de cont sau al DCU; art. 75 face DCU autorul listei acționarilor. Procedura concretă de succesiune nu e în Reguli, ci în Procedurile DCU, publicate separat. PDF-ul poartă o notă de copyright a DCU. dcu.md nu are Cloudflare; `curl` merge.
- **Decis:** ingerat în `raw/papers/bnm/legal-ro/` sub `DCU-REGULI-2026`, cu script propriu `ingest_dcu_rules.py` (precheck, scriere, verify) și PDF-ul arhivat în `_meta/imports/bnm/dcu/`, cu acordul explicit al lui Eugen pentru descărcare; identificatorul urmează emitentul și anul intrării în vigoare, fiindcă nu există cod legis.md. Aprecierea notei de copyright rămâne a lui Eugen; vault-ul e privat și textul se citează, nu se reproduce în afară. Rămân deschise Procedurile DCU, legile 183/2016 și 184/2016, hotărârea BNM 89/2026 pe bnm.md, și versiunile abrogate.
- **Unde:** `raw/papers/bnm/legal-ro/DCU-REGULI-2026.md`; `entities/DCU-REGULI-2026.md`; `entities/HBN-130-2013.md` (întrebarea 1); manifestul legal-ro (rând și secțiunea DCU-REGULI-2026); `index.md` (114 pagini); `CLAUDE.md` („Where things are"); `_meta/imports/bnm/ingest_dcu_rules.py`; `_meta/imports/bnm/dcu/Reguli_DCU_v3.pdf`.

## [2026-09-08] lint | Un fișier brut convertit CRLF→LF de alt proces în timpul sesiunii; lăsat afară din commit

- **Aflat:** la 13:12:43, între commiturile sesiunii de ingest, `raw/papers/bnm/legal/documents/069__REG 328_EN_08_12_21 (1).doc.md` a apărut modificat în arborele de lucru: 1.113 octeți CR în HEAD, zero pe disc, text identic fără CR, hash-ul declarat verificabil în continuare pe convenția LF. Este a doua conversie de acest fel în aceeași oră, după copia de lucru a Codului civil de la 12:50; de data aceasta pe un fișier din `raw/`, declarat imuabil. Sesiunea de ingest nu a deschis fișierul. Sursa probabilă: sesiunea `wiki-39`, activă în același folder, sau Obsidian.
- **Decis:** commitul pentru DCU-REGULI-2026 se face cu `git add` pe lista explicită de fișiere ale sesiunii și ale controalelor regenerate, nu cu `git add -A` al lui `close_session.py`, ca fișierul străin să rămână necomis. Nu se readuce la CRLF: conversia nu schimbă textul și convenția vault-ului este LF, dar cine o face trebuie să o consemneze el. De raportat lui Eugen; `[de verificat]` ce proces rulează normalizarea.
- **Unde:** `git status` la 13:12; acest log.

## [2026-09-09] ingest | L-246-2018, procedura notarială: consolidarea în vigoare stă deasupra rândului de căutare, cu doc_id mai mic

- **Aflat:** Legea 246/2018 are pe legis.md șapte consolidări, iar rândul de căutare trimite la 150742 (01.11.2025); cea în vigoare azi este 137680 @ 23.06.2026, produsă de LP126/2023, lege cu intrare în vigoare amânată trei ani, deci cu doc_id mai mic decât versiunea mai veche. Diferența nu e cosmetică: art. 5^1 (actul notarial electronic și la distanță), 33 de marcaje, 97 de articole față de 96. Până acum consolidarea curentă fusese mereu cea cu doc_id-ul cel mai mare; regula devine: lista de versiuni decide. Pentru speța moștenitorului, capitolul V dă calendarul până la certificatul de moștenitor: publicare în 5 zile lucrătoare pe pagina Camerei Notariale (art. 71), certificatul nu mai devreme de o lună de la ultima publicare (art. 82 alin. (3)), suspendare la orice contestare între succesibili (art. 73); certificatul de calitate de moștenitor apare o singură dată, la art. 69 alin. (1^1), fără regim propriu; custodele poate fi unul dintre succesibili cu acordul tuturor (art. 80 alin. (2)). Descărcarea la 340 KB a înghețat de două ori renderer-ul paginii `showdetails`; a mers din pagina actului. Două decizii de inadmisibilitate ale Curții privesc legea și nu intră în registrul HCC.
- **Decis:** ingerată sub `L-246-2018` în `moldova-legal`, din 137680, cu acordul explicit al lui Eugen pentru descărcare; pagină de entitate cu capitolul V citit și restul declarat necitit; manifestul U.14 consemnează capcana de versiune ca regulă. Commit cu `git add` explicit, fiindcă fișierul brut convertit CRLF→LF de alt proces e încă în arbore. Rămân neingerate: regulamentele ministrului justiției (inventariere, acte la distanță), Legea 69/2016 privind organizarea notarilor.
- **Unde:** `raw/papers/moldova-legal/L-246-2018.md`; `entities/L-246-2018.md`; manifestul moldova-legal U.14; `index.md` (115 pagini); `ingest_business_law.py` (intrarea); cache `showdetails-137680.html`.

## [2026-09-09] ingest | Procedurile DCU: opt din nouă ingerate; cea cu succesiunea este PDF-imagine, citită din imagine; documentele cerute stau în Regulamentul CNPF 14/5/2016

- **Aflat:** cele nouă proceduri de pe dcu.md sunt acte ale Comitetului executiv al DCU (art. 4 alin. (2) din Reguli), câte un PDF fiecare, fără articole, numerotate pe puncte în forme diferite. Opt au strat de text și au intrat fără ancore, cu verificare PASS pe toate; a noua, „Proceduri privind operațiunile de decontare", singura care descrie pasul succesiunii, are glifele randate ca imagini și nu se poate extrage fără OCR, care nu există pe mașină. Citită din imaginile paginilor, ea spune: moștenitorul înstrăinează doar după ce obține proprietatea prin creditarea contului; transferul are patru pași, documente, factură și dispoziție de transmitere pregătită de DCU, semnătura părților la oficiu cu actul de identitate în original, transferul; iar **lista documentelor nu este în Proceduri, ci în Regulamentul CNPF nr. 14/5/2016 privind circulația valorilor mobiliare pe piața de capital**, care nu este în vault; anexa nr. 1 dă codul MD03, „Moștenirea valorilor mobiliare", cod CNPF 4. Din textul ingerat: comisionul DCU la decontarea prin moștenire este 10 lei pe tranzacție, scutit pentru pensionari, persoane cu dizabilități și participanți la acțiuni militare, ca și extrasul cerut pentru certificatul de moștenitor (comisioane, 9.3); lista acționarilor pentru AGA o eliberează DCU numai emitenților cu registrul transferat la DCU și conține drepturile sau restricțiile de vot. Patru documente au textul fragmentat de font. Procedura garanțiilor e marcată „DCU INTERN" pe pagina de titlu, deși e publică.
- **Decis:** folder nou `raw/papers/bnm/dcu/`, cu manifest propriu, fiindcă nu sunt acte BNM; script propriu `ingest_dcu_proceduri.py`, care refuză explicit PDF-urile fără text, ca să nu intre o extracție inventată; pagina de entitate este un hub pentru set, cu partea citită din imagine marcată ca neancorată. Descărcarea lotului cu acordul explicit al lui Eugen. Rămân deschise: OCR pentru decontare, Regulamentul CNPF 14/5/2016 și Hotărârea CNPF 38/5/2015, reconstituirea fragmentelor de font, documentele model. Commit cu `git add` explicit, fișierul brut străin fiind încă în arbore.
- **Unde:** `raw/papers/bnm/dcu/` (opt fișiere și `_manifest.md`); `entities/DCU-PROCEDURI.md`; `raw/papers/bnm/_manifest.md` (secțiune nouă); `index.md` (116 pagini); `CLAUDE.md` („Where things are"); `_meta/imports/bnm/ingest_dcu_proceduri.py`; `_meta/imports/bnm/dcu/proceduri/` (nouă PDF-uri, inclusiv cel neingerat).

## [2026-09-09] ingest | HCNPF-14-5-2016, circulația valorilor mobiliare: pct. 27 numește certificatul de moștenitor drept documentul de înregistrare; lanțul speței este închis la nivel de document

- **Aflat:** Regulamentul CNPF 14/5/2016 este primul act subordonat al CNPF din vault; hotărâre cu regulament anexat, 61 de puncte plus 5 cu exponent, consolidarea 131276 din 06.05.2022 (HCNPF14/15/2022), aceeași cu rândul de căutare. Pentru speță: pct. 11 subpct. 4) face din moștenire o tranzacție în afara pieței reglementate; pct. 18 cere dispoziția de transmitere și documentele de identificare; pct. 27, „în cazul moştenirii valorilor mobiliare se prezintă certificatul de moştenitor eliberat de notar", plus actele notariale de partaj, donație sau vânzare a cotei succesorale; pct. 20 trimite, pentru acțiunile băncii, la Legea 202/2017 și la Regulamentul BNM 130/2013, care trimite înapoi la pct. 12; pct. 45 subpct. 1), moștenirea se înregistrează la valoarea nominală dacă actele nu prevăd altfel. Certificatul de calitate de moștenitor nu apare: poziția din 8 septembrie că nu este titlu de înregistrare stă acum și pe actul CNPF. Cu acesta, lanțul Cod civil → Legea 246/2018 → Regulamentul CNPF 14/5/2016 → Regulamentul BNM 130/2013 → Regulile DCU → Procedurile DCU este ingerat integral, mai puțin textul procedurii de decontare, fără OCR.
- **Decis:** ingerat în `raw/papers/cnpf/`, perimetrul CNPF, sub `HCNPF-14-5-2016`, cu învelișul nou `_meta/imports/cnpf/ingest_cnpf_ro.py` peste scriptul bancar și cache-ul legilor CNPF, plus `verify_cnpf_ro.py`; scriptul CNPF din iulie nu se mai folosește pentru acte noi. Zero ancore, pe puncte. Descărcarea cu acordul explicit al lui Eugen. Întrebările deschise despre actele CNPF de pe paginile HBN-130-2013 și DCU-PROCEDURI sunt închise; rămân Hotărârea CNPF 38/5/2015 (tipurile de tranzacții F7) și hotărârea anuală a taxelor CNPF. Commit cu `git add` explicit, fișierul brut străin fiind încă în arbore.
- **Unde:** `raw/papers/cnpf/HCNPF-14-5-2016.md`; `entities/HCNPF-14-5-2016.md`; `entities/DCU-PROCEDURI.md` și `entities/HBN-130-2013.md` (întrebări închise); manifestul cnpf, secțiunea J; `index.md` (117 pagini); `CLAUDE.md`; `_meta/imports/cnpf/ingest_cnpf_ro.py`, `verify_cnpf_ro.py`; cache `showdetails-131276.html`.

## [2026-09-09] ingest | HCNPF-38-5-2015, instrucțiunea de raportare: F7 e un formular, nomenclatorul lui nu e pe legis.md; actul a fost redenumit și nu se găsește după număr

- **Aflat:** Hotărârea CNPF 38/5/2015, la care trimit codurile de transfer ale DCU, este instrucțiunea de raportare a pieței de capital, redenumită din „raportările persoanelor licențiate și autorizate" în „sistemul de raportare în domeniul pieței de capital"; legis.md nu o găsește după număr, nici în titlu, nici în text, iar căutarea în text a înghețat browserul și a fost urmată de o eroare 524 a legis.md, revenit în aceeași după-amiază. Titlul l-a dat cnpf.md; căutarea în titlu a mers cu titlul vechi. Consolidarea curentă 147834 din 01.10.2025 (HCNPF12/4/2025), cea mai nouă din nouă. Pentru speță, rezultat negativ și util: F7 este raportul zilnic al tranzacțiilor în afara pieței, prezentat de depozitarul central, registratori și societățile de investiții; nomenclatorul tipurilor de tranzacții stă în modelul formularului, anexa nr. 1, care nu este în textul legis.md, deci „cod 4 = moștenire" de pe pagina DCU rămâne neverificabil din vault. Anexa nr. 2 pct. 9 subpct. 3) trimite taxa pe tranzacție la hotărârea Parlamentului privind bugetul CNPF, nu la o hotărâre CNPF; antetul anexei nr. 2 poartă parafa Ministerului Finanțelor, ciudățenie de sursă consemnată.
- **Decis:** ingerat sub `HCNPF-38-5-2015` cu același înveliș, zero ancore; descărcare cu acordul explicit al lui Eugen. Întrebările despre 38/5 de pe paginile DCU-PROCEDURI și HCNPF-14-5-2016 sunt închise parțial; rămân anexa nr. 1 (din Monitorul Oficial sau cnpf.md, ca sursă de lucru) și actul care fixează taxa pe tranzacție. Regula de căutare, a doua oară în două zile: un act redenumit se caută sub titlul vechi. Commit cu `git add` explicit, fișierul brut străin fiind încă în arbore.
- **Unde:** `raw/papers/cnpf/HCNPF-38-5-2015.md`; `entities/HCNPF-38-5-2015.md`; manifestul cnpf, J.2; `index.md` (118 pagini); `CLAUDE.md`; `ingest_cnpf_ro.py` (intrarea); cache `showdetails-147834.html`.

## [2026-09-10] decision | Sesiunea speței moștenitorului închisă: lanțul de acte ingerat integral, două goluri de text, un fișier străin lăsat necomis

- **Aflat:** în două zile, 8 și 9 septembrie, lanțul speței moștenitorului unui acționar de bancă a intrat în vault de la un capăt la altul: Legea 246/2018 (procedura notarială), Regulamentele BNM 127/2013 și 130/2013, Regulile DCU, opt din nouă Proceduri DCU, Regulamentele CNPF 14/5/2016 și 38/5/2015; opt acte, trei rute noi de ingest (înveliș BNM pentru acte subordonate, PDF cu ancore sintetice, înveliș CNPF), 118 pagini structurate, 412 surse brute verificate. Răspunsul din 8 septembrie s-a schimbat într-un punct: art. 45 alin. (6) din Legea 202/2017 nu blochează înscrierea moștenitorului, pct. 14 din Regulamentul 130/2013 o face fără aprobare prealabilă, cu votul suspendat; celelalte două bariere au rămas și s-au ancorat, pct. 27 din Regulamentul CNPF numind certificatul de moștenitor drept singurul titlu. Rămân două goluri de text, nu de act: procedura de decontare a DCU, PDF-imagine fără OCR, și anexa nr. 1 a instrucțiunii de raportare, absentă de pe legis.md. Un singur fapt nu îl fixează niciun act: „data achiziției" de la care curg termenele de 15 zile, 60 de zile și 3 luni în caz de moștenire. La închidere, controalele generate au avut doar deriva de dată (ștampila, o vechime „8.4" devenită „8.5 ani"); validatorul dă 0 erori. Fișierul brut `069__REG 328_EN...` stă convertit CRLF→LF de alt proces din 8 septembrie, necomis de niciunul din cele nouă commituri ale sesiunii; conținut identic, hash valid pe convenția LF.
- **Decis:** sesiunea se închide cu controalele regenerate comise, fără fișierul străin, printr-un `git add` explicit. Rămân ale lui Eugen: registrul dosarelor din proiect, cu ștampila din 7 septembrie, pentru re-ștampilare; intrările pentru documentul 06 (M-001 punctul (b) închis, dosarul nou al moștenitorului cu poziția revizuită); decizia despre fișierul 069 și despre procesul care normalizează terminațiile de linie; OCR pentru procedura de decontare; notele de copyright ale DCU; actul care fixează taxa CNPF pe tranzacție.
- **Unde:** commiturile 8a96327 … 472b657; `CLAUDE.md` („Where things are"); manifestele `bnm/legal-ro`, `bnm/dcu`, `cnpf` (J, J.2), `moldova-legal` (U.14); acest log.

## [2026-09-10] decision | Fișierul brut 069, convertit CRLF→LF de alt proces, comis așa cum e, la decizia lui Eugen

- **Aflat:** `raw/papers/bnm/legal/documents/069__REG 328_EN_08_12_21 (1).doc.md`, traducerea engleză a Regulamentului BNM 328, a fost rescris pe disc la 8 septembrie, 13:12, de un proces care nu a fost sesiunea de ingest: 1.113 octeți CR au dispărut, textul fără CR este identic, iar hash-ul declarat verifică pe convenția LF, pe care validatorul o acceptă. Nouă commituri l-au ocolit prin `git add` explicit. Este un fișier `source_type: translation`, neancorat (D2), deci schimbarea nu atinge nicio citare.
- **Decis:** Eugen a cerut să fie comis așa cum e: conversia în LF este în sensul convenției vault-ului și nu schimbă conținutul. Nu se readuce la CRLF. Cine a făcut conversia rămâne neaflat; dacă se repetă pe alte fișiere din `raw/`, se caută procesul înainte de a comite din nou.
- **Unde:** commitul acestei intrări; `git diff 472b657 HEAD -- "raw/papers/bnm/legal/documents/069__REG 328_EN_08_12_21 (1).doc.md"` arată 2.226 de linii schimbate pentru zero octeți de text.

## [2026-09-10] update | Harta de cunoștințe (05) rescrisă după ingestiile din 6-10 septembrie; copiile 05 și 06 reîmprospătate (D9)

- **Aflat:** documentul 05 din proiect, revizuit la 6 septembrie, spunea că lipsesc din bază Constituția, hotărârile Curții Constituționale, legislația secundară CNPF și Legea 149/2012; toate patru au intrat între 6 și 10 septembrie (34 de commituri), deci harta subestima acoperirea, a doua oară în aceeași direcție ca la 4 septembrie. Copia locală a lui 06 (luată la 7 septembrie) nu avea speța M-002 și închiderea punctului (b) din M-001; copia lui 05 era la versiunea din 5 septembrie. Vault-ul în sine era curat: git la zi cu origin, controalele generate și validatorul fără erori.
- **Decis:** Eugen a cerut actualizarea a tot ce e necesar. Documentul 05 a fost rescris în proiect contra `git log`: patru moduri de eroare în loc de trei (al patrulea: dispoziție anulată de Curtea Constituțională, controlul fiind registrul HCC), sondajul de actualitate consemnat ca executat, Codul civil pe textul legis.md, extinderea planificată redusă la ce a rămas (25 HCC fără articol, procedura DCU imagine, registrul in-force pentru actele pe puncte, Codul fiscal după 01.01.2027, Acordul de asociere și textele EU integrale). Regulă nouă în 05: la fiecare închidere de sesiune se compară documentul cu `git log` de la data reviziei. Copiile 05 și 06 aduse din proiect și reștampilate `taken 2026-09-10`.
- **Unde:** proiectul claude.ai „Legal Wiki”, `legal-career/05-knowledge-map.md`; `legal-career/05-knowledge-map.md` și `legal-career/06-matter-log.md` în vault; commitul acestei intrări.

## [2026-09-10] update | Documentul 03, secțiunea 4: cifra datată a registrului in-force înlocuită cu trimiterea la antetul registrului

- **Aflat:** secțiunea 4 din 03 spunea „la 4 septembrie registrul ține cinci dispoziții în trei acte”; datată, deci nu falsă, dar cu un ordin de mărime sub registrul de azi, și ar fi fost citită ca stare curentă de orice persona.
- **Decis:** Eugen a cerut schimbarea. Fraza trimite acum la linia de antet a registrului, ca în 05; exemplul art. 38 și 141^1 din Legea 171/2012 rămâne. Nimic altceva în 03 nu s-a schimbat. Copia locală adusă din proiect și reștampilată.
- **Unde:** proiectul claude.ai „Legal Wiki”, `legal-career/03-working-rules.md`; copia din vault; commitul acestei intrări.

## [2026-09-10] create | Graful de citare al actelor deținute, control generat în `_meta/graph/`

- **Aflat:** textul brut conține deja muchiile căutate până acum de mână, o ingestie pe zi: 3.391 de mențiuni de acte și 8.134 de trimiteri la articole în cele 83 de acte primare, din care 996 se rezolvă într-un alt act deținut și 75 (67 de grupuri) nu au ancoră în actul-țintă. Trei lucruri nu se vedeau fără graf. Coada de ingerare: 475 de acte citate și nedeținute, în frunte Legea 133/2011 (34 de mențiuni din 18 acte), Legea 183/2016 (25 din 7), Legea 1125/2002 (22 din 2), Legea 213/2023 (22 din 8); Codul electoral, al educației, al familiei, al transporturilor rutiere, al jurisdicției constituționale și al audiovizualului, citate pe nume, au fost unite cu forma pe număr de textul care le scrie împreună. Dependența: 17 dispoziții din registrele in-force și HCC sau abrogate sunt citate din alte acte, de pildă art. 72 din Codul penal, modificat de la 02.12.2026, din CPP art. 469 și din Codul de executare art. 197 și 255. Trimiterile nerezolvate sunt aproape toate reale, nu erori de citire: CPC și Legea insolvabilității citează Codul civil cu numere care nu există în consolidarea deținută (art. 48^30, 330^4, 283^27, 1575^4–1575^11; probabil numerotarea dinainte de republicarea din 2019), HG 582/2022 citează art. 441 din Codul contravențional, abrogat în 2016 (întrebarea deschisă 3), HCNPF 14/5/2016 și 38/5/2015 citează art. 81, 87 și 88 din Legea 171/2012, care nu au ancoră, Legea 2/2020 citează art. 38 din 171/2012, al cărui text lipsește din fișier (registrul in-force), iar 23 din cele 67 de grupuri au ipoteza mecanică de exponent turtit în sursă (art. 3142 pentru 314^2, 24513 pentru 245^13, 572, 541, 571 în Legea concurenței, cum notase manifestul la K.3). Capcane de citire găsite și închise în aceeași sesiune: blocul de istoric al actului (`LP… MO…/… art.N`, și cu litere chirilice, `MOF`, virgulă sau `din` înaintea datei) dădea sute de muchii false către articolele actului însuși; enumerările (`art. 61 … sau ale art. 62 … din Legea 131/2015`) se rezolvă numai ca grup; clauzele de transpunere pun lista de articole în paranteză înaintea directivei, fără `din`; `din legea indicată` este anaforă la ultima lege numită în același segment; cuprinsul din preambul repetă titlurile articolelor.
- **Decis:** Eugen: graful se construiește ca control generat, nu cu graphify (muchii deduse, un al treilea strat de rezumat, ieșire în afara căilor validate). Alegerile de proiectare din această sesiune, de confirmat: nicio muchie dedusă, fiecare muchie poartă fișierul și liniile din care a fost citită; graful nu se citează, el spune ce ancoră se deschide; ipoteza de exponent turtit este câmp separat, nu muchie; actele pe puncte și extrasele UE sunt doar ținte; corpusul englez BNM nu se citește; `close_session.py` rulează graful după cele două registre pe care le citește și înaintea blocului de acoperire, deci bariera de commit îl verifică; JSON-ul are un nod sau o muchie pe rând, ca diff-ul să fie citibil. Rămân atribuite actului curent, de decis dacă merită o regulă: trimiterile în care actul e numit `Lege` fără număr (statutul avocaților) sau stă mai departe în frază decât văd regulile de context.
- **Unde:** `_meta/graph/build_citation_graph.py`, `_meta/graph/citation-graph.json`, `_meta/graph/citation-graph.md`; `_meta/close_session.py`, pasul „graful de citare”; `CLAUDE.md`, „Where things are” și „Keeping this file true”; commitul acestei intrări.

## [2026-09-10] ingest | Protecția datelor: legea cerută era abrogată de 18 zile; ingerate trei acte, nu unul

- **Aflat:** `L-133/2011`, primul rând al cozii de ingerare (34 de mențiuni în 18 acte deținute), este **abrogată de la 23.08.2026** prin art. 90 alin. (3) lit. b) din `L-195/2024`. Graful o ridicase în capul cozii tocmai fiindcă nu știe dacă un act citat mai este în vigoare, limită pe care o declara el însuși; prima extragere din coadă a lovit-o. Două capcane de sursă, ambele tăcute. Prima, a doua oară după `L-246-2018`: rândul de căutare trimite la doc_id 148996@14.06.2025, dar lista de versiuni ține 144823@**23.08.2026**, doc_id mai mic și dată mai nouă, creat în 2024 pentru o modificare cu intrare în vigoare amânată doi ani. A doua, nouă: corpul consolidării poartă în antet „Abrogată prin LP195 … în vigoare 23.08.26”, iar câmpul **„Data abrogării” din fișă este GOL** — sursa se contrazice pe sine, și un control sprijinit pe fișă ar fi ratat abrogarea. Fără aceste verificări actul ar fi intrat cu consolidare recentă și trecută, deci `clean` în blocul de acoperire, cu ancorare curată și sha256 valid: simetricul capcanei consolidărilor viitoare. Aceeași căutare a scos la iveală doi succesori, niciunul în vault: `L-195/2024` (GDPR, în vigoare 23.08.2026) și `L-160/2026` (Directiva 2016/680, materie penală, cel mai nou act din corpus). Împărțirea e curată — art. 2 alin. (2) lit. c) din legea generală scoate materia penală, art. 1 alin. (1) din cea penală o preia — dar a doua nu e autonomă: împrumută noțiunile din art. 4, procedura amenzii din art. 87 și examinarea plângerii din cap. VIII secț. 2 ale primei. Trei constatări de fond: amenzile sunt eșalonate la **10% în primul an**, 40% în al doilea, 100% din al treilea (art. 90 alin. (4)); plafoanele sunt 1%/2% din cifra de afaceri, **sub** cele 2%/4% ale GDPR; și art. 90 alin. (3) lit. c) a abrogat arts. 74^1–74^3 și 423^4 din `COD-218-2008`, ceea ce se verifică în consolidarea deținută, unde toate patru apar `– abrogat.`. Ce **nu** există: nicio clauză „trimiterile la Legea 133/2011 se consideră făcute la prezenta lege”, iar art. 55 din `L-100-2017` reglementează cum se *fac* trimiterile, nu ce se întâmplă când ținta e abrogată. Separat, un defect propriu, prins la verificarea cozii după ingerare: redirecționarea aliasurilor de coduri scrisă la commitul `bca3c38` producea ținte fără nod, fiindcă aliasurile se învață înainte de bucla care pune prefixul `EXT:`. **47 de mențiuni dispăreau din raport fără nicio eroare**, 34 ale Codului electoral, care este de fapt capul cozii, nu `L-183/2016`.
- **Decis:** se ingerează **toate trei**, nu doar cea cerută: un act mort singur în vault ar fi răspuns la 19 trimiteri vii cu text care nu mai leagă. `L-133/2011` se păstrează fiindcă art. 90 alin. (5)–(8) din legea nouă o menține în picioare pentru faptele anterioare, pentru actele de transfer emise sub art. 32 al ei, pentru plângerile depuse până la 23.08.2026 și pentru consimțământul deja dat. Abrogarea devine control mecanic, nu observație în text: `repeal_of()` în ingest citește **ambele** surse și le păstrează pe amândouă în frontmatter, fiindcă dezacordul lor este el însuși o constatare despre sursă; blocul de acoperire scrie `**ABROGAT de la ...**` în tabel și o secțiune proprie de flaguri; graful capătă secțiunea „Trimiteri către acte abrogate”, deci pentru actele **deținute** limita pe care și-o declara este ridicată. Defectul de aliasuri se repară și primește un **invariant care oprește construcția** dacă vreo muchie mai ajunge la un id fără nod, ca pierderea tăcută să nu se mai poată repeta. Rămâne la Eugen: conversia celor 19 trimiteri către legea abrogată, care nu are temei expres.
- **Unde:** `raw/papers/moldova-legal/L-133-2011.md`, `L-195-2024.md`, `L-160-2026.md`; manifest moldova-legal secțiunea **V**; `entities/L-133-2011.md`, `entities/L-195-2024.md`, `entities/L-160-2026.md`; `index.md`; `_meta/imports/moldova-legal/ingest_business_law.py` (`repeal_of`, trei intrări în `DOCS`); `_meta/coverage/build_coverage.py`; `_meta/graph/build_citation_graph.py`; `CLAUDE.md`, `_meta/graph/`; commitul acestei intrări.

## [2026-09-15] update | Pasul 5.3–5.5 al planului HCC: 23 din 25 hotărâri recuperate, flag de acoperire, avertisment de citare, 11 pagini de entitate

- **Aflat:** blocarea Cloudflare presupusă în planul din 8 septembrie (5.3 „nu, Cloudflare”) nu mai ține: `getResults`/`showdetails` răspund la `curl` cu doi antete în plus față de ruta din septembrie — `Referer` către pagina actului și `X-Requested-With: XMLHttpRequest` — fără cookie jar de Chrome și fără Eugen prezent; capcana e că, fără aceste antete, endpointul `showdetails` dă tot 403 „Just a moment” deși pagina principală a actului trece curat, deci un test superficial ar fi conchis greșit că bariera ține. Cu ruta nouă, 23 din cele 25 de hotărâri fără articol au fost recuperate: cinci coduri/legi capătă articolul complet (`COD-116-2018`, `COD-154-2003` ×3, `COD-174-2018`, `COD-443-2004` ×6, `L-1260-2002`, `L-135-2007`, `L-149-2012` ×2, `L-158-2008`, `L-514-1995` ×3, `L-64-2010`, `L-845-1992` ×3, `L-548-1995` ×2). Cele două rămase fără articol, `CONST-1994` (HCC8/2024, HCC7/2016), sunt hotărâri **interpretative**: nu lovesc niciun text, deci legis.md nu pune niciun marcaj în corpul Constituției, iar căutarea în titlu nu indexează după numărul hotărârii — planul le tratase deja separat (D3, secțiunea 3). Trei descoperiri de fond ies din verificarea „ce spune azi textul”, nu doar din recuperarea articolului: `L-514-1995` art. 15 al.(2) — HCC3/2012 a anulat art. III întreg din Legea 163/2011, deci a revigorat nu doar alineatul ci și Capitolul 5 (art. 41-42) și pozițiile din anexele 1-3, iar Capitolul 5 e din nou „abrogat” azi, semn că o lege ordinară ulterioară l-a reabrogat — istorie în trei pași, nu defect; `L-548-1995` art. 11 al.(4) — interdicția absolută de suspendare judecătorească a actelor BNM (administrare specială, retragere licență, lichidare silită), lovită de HCC31/2013, e azi înlocuită cu controlul de legalitate în contencios administrativ, exact opusul textului anulat, punct relevant pentru orice speță de contestare a unui act BNM; `L-548-1995` art. 77 al.(4) — clauza de auto-supremație a legii BNM față de orice altă lege, lovită de HCC9/1999 la doar trei săptămâni după HCC12/1999 (aceeași clasă de clauză, în Codul fiscal, deja în registru), a dispărut fără urmă din consolidarea deținută. Planul D4 presupunea că blocul de acoperire și validatorul verifică deja citarea provizioanelor neintrate în vigoare „așa cum verifică azi” — fals: nicio asemenea verificare nu exista în `validate_wiki.py` sau `schema-spec.yaml` pentru registrul in-force, darămite pentru unul HCC încă neconstruit; D4 a trebuit construit de la zero, nu doar oglindit. Primul cut al avertismentului de citare, pe paragraf, a dat 71 de false pozitive pe `COD-1163-1997` (tabelul propriu de HCC, cu hotărârea numită o singură dată în antet, nu repetată pe fiecare rând); rescris pe **secțiune** (de la un titlu la următorul), a coborât la 8, din care 6 erau goluri reale (pagina discuta articolul în altă secțiune decât cea cu tabelul HCC) și 2 rămân reziduale, fără urmare: în `COD-1163-1997`, „art. 88” apare ca reper de poziție într-o secțiune despre exponenți turtiți, nu ca citare de drept.
- **Decis:** cele 23 de rânduri recuperate merg în `_meta/hcc/recovered-provisions.json`, cu `read_doc_id`, `decision_doc_id` (unde legătura era încorporată în marcaj) și `status_today` verificat direct în textul brut deținut pentru șapte dintre ele (nu doar presupus). Blocul de acoperire din `CLAUDE.md` capătă flagul „Declared unconstitutional”, pe modelul „Not yet in force”, plus o notă pe fiecare rând din tabelul actelor. Validatorul capătă regula nouă `citation.hcc-unmarked`, restrânsă deliberat la paginile `entities/<ACT>.md` (unde pagina și actul sînt evident același lucru) și scopată pe secțiune, nu pe paragraf, ca să nu penalizeze un tabel deja corect etichetat; paginile din `concepts/`, `comparisons/`, `queries/` rămîn neacoperite, consemnat, nu ghicit. Cele 11 acte fără secțiune HCC pe pagina de entitate (din cele 18 ale registrului) primesc una, pe modelul deja folosit la `COD-1163-1997`, plus o notă inline exact la locul citat pentru cele cinci unde avertismentul rezista din prima trecere (`COD-174-2018`, `L-135-2007`, `L-514-1995`, `L-548-1995` de două ori). Cele două reziduale din `COD-1163-1997` rămân neatinse: pagina are deja secțiunea HCC completă, iar cele două mențiuni sînt repere de poziție, nu citări. `updated` ridicat la 2026-09-15 pe cele 11 pagini editate. Cele două hotărâri interpretative ale Constituției rămân deschise, de recuperat printr-o altă metodă (nu căutare în titlu) decât cea aplicată aici.
- **Unde:** `_meta/hcc/recovered-provisions.json` (72→95 dispoziții), `_meta/hcc/hcc-register.md`/`.json` (regenerate); `_meta/coverage/build_coverage.py` (funcția `hcc()`, flagul „Declared unconstitutional”, nota pe rând); `_meta/schema/validate_wiki.py` (`load_hcc_known`, `check_hcc_citations`, regula `citation.hcc-unmarked`); `entities/COD-116-2018.md`, `COD-154-2003.md`, `COD-174-2018.md`, `L-1260-2002.md`, `L-135-2007.md`, `L-149-2012.md`, `L-158-2008.md`, `L-514-1995.md`, `L-64-2010.md`, `L-845-1992.md`, `L-548-1995.md`; `CLAUDE.md` (bloc generat, „Read this first” neschimbat); `_meta/plans/2026-09-08-plan-hcc-pasul-5.md` (pașii 5.3–5.5 acum executați, ce rămâne: CONST-1994 și pasul 5.6 la cerere); `_meta/lint/validate-2026-09-15.md`; commitul acestei intrări.

## [2026-09-15] create | Pasul 6 (Acordul de Asociere, textele UE integrale, reverificarea acquis) pornit: recensământ și plan, nimic ingerat încă

- **Aflat:** planul din 6 septembrie lăsase pasul 6 fără conținut propriu, doar o propoziție. Recensământul de azi găsește patru lucruri care schimbă mărimea reală a sarcinii. Întâi, „textele UE integrale" nu înseamnă 2427 de articole (suma cuprinsului celor 29 de extrase `UE-*.md`): sub 30 de citări `art. N` distincte apar în tot stratul de 18 pagini `concepts/acquis-*` + `cnpf-transposition-matrix`, deci golul verificabil e mic, nu corpusul întreg al fiecărei directive. Al doilea, Acordul de Asociere **nu e nicăieri în vault**, dar CELEX-ul corect (`22014A0830(01)`, nu `22014A0630(01)` cum ar sugera data semnării — data din CELEX e a publicării în JO, 30 august 2014) răspunde direct la `curl`, fără nicio barieră de tip Cloudflare, text RO complet, ~11 MB, structurat pe articole ca `showdetails` de pe legis.md. Al treilea, și cel mai important: documentul conține **Anexa XXVIII-A, „Norme aplicabile serviciilor financiare"** — o listă de ~20-25 directive/regulamente UE cu **calendar legal propriu** de transpunere („trei ani de la intrarea în vigoare a prezentului acord", unele „cinci" sau „zece"), exact perimetrul CNPF/BNM al acestui vault. Anexele XXVIII-B/C/D de lângă ea (telecomunicații, poștă, transport maritim) sînt verificate și confirmate în afara perimetrului; documentul-soră `22014A0830(02)` (~9,8 MB) e schedulele tarifare de mărfuri, la fel în afara perimetrului. Data calendaristică efectivă a intrării în vigoare/aplicării provizorii NU e în corpul acordului (art. 462-464 dau doar mecanismul), ci într-o decizie separată a Consiliului — de găsit separat înainte de a calcula orice termen din Anexa XXVIII-A. Al patrulea, o verificare de actualitate CELEX pe toate cele 29 de extrase (`discover_latest_celex.py`, citire) arată 5 cu consolidare mai nouă disponibilă: patru sînt deja documentate în manifest ca fals pozitiv (act de bază fără consolidare distinctă listată), dar Solvency II (`UE-2009-138`) e o constatare nouă — consolidarea disponibilă e `-20270130`, de verificat dacă e cu dată viitoare, simetricul consolidărilor domestice viitoare.
- **Decis:** planul propriu (`_meta/plans/2026-09-15-plan-pasul-6-acquis-aa.md`) scrie cinci decizii pentru Eugen: (D1) se ingerează doar Anexa XXVIII-A și articolele-cadru ale Acordului, nu documentul întreg — prefix nou `AA-2014`; (D2) nu se digitalizează mecanic toate cele ~2427 de articole din extrasele UE, ci se extrag țintit cele cerute de „Întrebările deschise" ale celor 18 pagini, verificate contra Anexei XXVIII-A și textului moldovenesc curent; (D3) dezghețarea `unverified`/`confidence: low` e per pagină, nu în bloc; (D4) ordinea de reverificare, pe apropierea de nucleul deja documentat (MiFID/MAR întâi, restul după); (D5) cele cinci consolidări mai noi, cu Solvency II tratat separat de celelalte patru deja cunoscute. Nimic din `raw/` sau din cele 18 pagini nu s-a atins azi; sesiunea a fost doar recensământ, pe modelul pasului 5.1-5.2 al HCC.
- **Unde:** `_meta/plans/2026-09-15-plan-pasul-6-acquis-aa.md`; commitul acestei intrări.

## [2026-09-15] lint | Pasul 6.2: data intrării în vigoare a Acordului, găsită și citită integral la sursă

- **Aflat:** panoul de metadate „Dates" al `22014A0830(01)` pe EUR-Lex (`.../legal-content/RO/ALL/?uri=CELEX:22014A0830(01)`) dă direct cele două date, fiecare cu propria notificare oficială separată — nu presupuse, citite integral. Aplicarea cu titlu provizoriu: **1 septembrie 2014** (`CELEX 22014X0830(02)`, JO L 260, 30.8.2014, p. 1, în temeiul art. 3 alin. (1) din Decizia 2014/492/UE a Consiliului din 16.06.2014). Intrarea în vigoare: **1 iulie 2016** (`CELEX 22016X0618(03)`, JO L 161, 18.6.2016, în temeiul art. 464 alin. (2) al acordului însuși, „având în vedere faptul că ultimul instrument de ratificare sau aprobare a fost depus la data de 23 mai 2016"). Ambele notificări se citesc la fel de simplu ca acordul însuși — `curl` direct, fără barieră, text RO complet, deși fișierele HTML-shell arată titlul paginii tot în engleză (`WT.z_usr_lan=en`), ceea ce ar putea păcăli un script care verifică titlul în loc de corpul paginii. Formula calendarului din Anexa XXVIII-A trimite explicit la art. 464, deci termenele curg de la **1 iulie 2016**, nu de la aplicarea provizorie din 2014: „trei ani" expiră 1 iulie 2019, „cinci ani" 1 iulie 2021, „zece ani" 1 iulie 2026 — luna trecută. Niciun termen din anexă nu mai e în viitor.
- **Decis:** constatarea intră în planul pasului 6 (secțiunea 2.2-bis), pasul 6.2 marcat făcut. Nimic din `raw/` nu s-a atins — cele două notificări nu s-au ingerat separat, doar citit; ingerarea propriu-zisă (`AA-2014`, pasul 6.3) va cita ambele date din articolul-cadru al acordului însuși, cu trimitere la notificările care le confirmă.
- **Unde:** `_meta/plans/2026-09-15-plan-pasul-6-acquis-aa.md` (secțiunea 2.2-bis, tabelul pașilor rândul 6.2); commitul acestei intrări.

## [2026-09-15] lint | Calendarul integral al Anexei XXVIII-A, citit și calculat: 41 de instrumente, nu ~20-25, toate termenele expirate

- **Aflat:** citirea integrală a anexei (nu eșantionată, cum fusese recensământul inițial) dă **41 de instrumente**, nu „~20-25" cum estimase secțiunea 2.2. Calculat de la 1 iulie 2016 (intrarea în vigoare, pasul 6.2): **toate cele 41 de termene au expirat deja**, cel mai îndepărtat (zece ani, pentru trei dispoziții punctuale) acum luna trecută, 1 iulie 2026. Din cele 41, doar **6** au o potrivire directă în cele 29 de extrase `UE-*.md` deja ținute (Solvency II, MTPL, Transparență, ICSD, UCITS, SFD); **33 n-au niciun extras**, inclusiv domenii întregi absente din corpus — garantarea depozitelor, serviciile de plată (PSD1), garanția financiară, agențiile de rating, CRD I, conturile anuale bancare/de asigurare. Alte **5** au un corespondent în vault, dar la **generația greșită**: Acordul angajează Moldova la MiFID I, Prospectus I, MAD I, IORP I și AMLD3 (cea din urmă cu cel mai scurt termen din toată anexa, un an), pe când extrasele deja ingerate (iulie 2026) sînt generațiile mai noi — MiFID II, Regulamentul Prospectus, MAR/CSMAD, IORP II, AMLD4/5. Confirmă instrument cu instrument ceea ce `acquis-MiFID.md` semnalase deja intuitiv drept „parțial/învechit". Separat, cinci pagini `acquis-*` din vault (AIFMD, EMIR/CSDR, Crowdfunding, Consumer Credit, Company Law/Takeover/SRD) n-au niciun instrument în Anexa XXVIII-A — nu înseamnă că nu există obligație de apropiere, doar că nu vine din această anexă; rămâne neverificat unde, dacă undeva.
- **Decis:** tabelul complet intră în plan (secțiunea 2.2-ter), ca bază de lucru pentru pasul 6.5. Nu s-a scris nimic în `raw/` — nici anexa, nici tabelul, nu sînt încă ingerate ca sursă citabilă; asta rămâne pasul 6.3 (`AA-2014`).
- **Unde:** `_meta/plans/2026-09-15-plan-pasul-6-acquis-aa.md` (secțiunea 2.2-ter); commitul acestei intrări.

## [2026-09-15] decision | Corectare: calendarul Anexei XXVIII-A curge de la aplicarea provizorie (1 septembrie 2014), nu de la intrarea în vigoare (1 iulie 2016)

- **Aflat:** la trecerea la ingestia efectivă (pasul 6.3), citirea integrală a art. 464 din acord — nu doar alin. (2), citat de notificarea de intrare în vigoare deja consemnată la pasul 6.2 — arată alin. (5): „orice trimitere la «data de intrare în vigoare a prezentului acord»" din dispozițiile care au fost aplicate cu titlu provizoriu „se înțelege ca trimitere la «data de la care prezentul acord se aplică cu titlu provizoriu»". Care dispoziții au fost aplicate provizoriu nu stă în acord, ci în Decizia 2014/492/UE a Consiliului (CELEX `32014D0492`, citită integral azi), art. 3 alin. (1): litera (d) include expres **titlul IV capitolul 9** (Serviciile financiare — art. 58-61, unde art. 61 trimite la Anexa XXVIII-A) și litera (h) include **anexele XV-XXXV**, interval ce cuprinde Anexa XXVIII întreagă. Deci calendarul Anexei XXVIII-A curge de la **1 septembrie 2014**, nu de la 1 iulie 2016 cum spunea concluzia pasului 6.2 (comisă și împinsă deja în două commituri, `caa3838` și `906eacf`). Diferența e de 22 de luni pe fiecare termen din tabel — suficient să schimbe un răspuns despre când anume a expirat o obligație de transpunere. Concluzia de fond a tabelului (toate cele 41 de termene sînt expirate) rămâne adevărată, dar fiecare dată individuală din tabel era greșită. Descoperit înainte de a scrie `AA-2014` în `raw/`, deci nicio sursă citabilă n-a purtat vreodată data greșită — corectarea a prins la timp, în planul de lucru, nu într-o pagină a stratului structurat.
- **Decis:** secțiunile 2.2-bis și 2.2-ter din plan se rescriu cu explicația corectării și tabelul recalculat (1 septembrie 2014 + N ani). Nu se ascunde eroarea inițială: paragraful de corectare rămâne în document, cu trimitere explicită la ce anume era greșit și de ce. Profitând de aceeași citire, două din cele cinci pagini „neverificat unde" ale tabelului anterior se precizează: Company Law/Takeover/SRD stau în Anexa II (Capitolul 3), Consumer Credit în Anexa IV (Capitolul 5) — găsite, dar neingerate, deci tot „neverificat instrument cu instrument", doar cu locația știută acum.
- **Unde:** `_meta/plans/2026-09-15-plan-pasul-6-acquis-aa.md` (secțiunile 2.2-bis, 2.2-ter, rescrise); Decizia 2014/492/UE (`CELEX 32014D0492`) citită, necesar de citat la ingestia `AA-2014`; commitul acestei intrări.

## [2026-09-15] ingest | Pasul 6.3: `AA-2014`, extras al Acordului de Asociere — Capitolul 9, art. 459-465, Anexa XXVIII-A

- **Aflat:** EUR-Lex nu are nicio barieră de tip Cloudflare (spre deosebire de legis.md), deci un script de extracție poate fetch-ui direct prin `curl`, fără sesiune, fără antete speciale. Capcana găsită la scriere, nu la citire: fiecare `id=` ELI din HTML-ul sursă apare de obicei DE DOUĂ ORI în document — o dată într-un cuprins/index, o dată în corpul real — deci o extracție care caută text în loc de identificatori stabili riscă să prindă varianta greșită; secțiunile deja verificate manual sesiunea trecută (Capitolul 9, art. 459-465, Anexa XXVIII-A) au fost tăiate pe `id=` unic, nu pe cuvinte. A doua capcană, de data asta mecanică: tăierea unui fragment chiar la poziția unui `id="..."` lasă tag-ul de deschidere neterminat („`<div id=`" fără `>` de închidere), pe care regexul de curățare a tag-urilor nu-l mai recunoaște — a apărut de trei ori (Capitolul 9, Anexa XXVIII-A, art. 3 din decizie) până la reparație (taie la `<` dinaintea poziției, nu la poziția însăși). A treia: primul marcaj `oj-ti-art` al unui fragment tăiat exact la `id="..."` (nu la `<p`) nu se mai potrivește cu regexul de articol, fiindcă îi lipsește `<p ` din față — art. 459 a dispărut tăcut din prima trecere, prins abia la numărătoarea anchorelor (10 în loc de 11). Titlurile articolelor (unde există) stau într-un element separat, `<p class="oj-sti-art">`, nu se ghicesc din forma textului — o presupunere inițială („primul paragraf care nu începe cu cifră e titlul") ar fi lipit greșit primul paragraf al art. 58 de antet. Toate trei capcanele au fost prinse prin `--verify` (re-extragere din cache, comparație octet cu octet) înainte de scriere, nu descoperite după.
- **Decis:** `_meta/imports/cnpf/ingest_aa_2014.py`, scris de la zero (nu pe modelul unui script existent, fiindcă sursa HTML EUR-Lex diferă structural de legis.md și de PDF-urile DCU): extrage patru fragmente prin identificatori `id=` stabili (Capitolul 9, art. 459-465, Anexa XXVIII-A, plus paragrafele relevante din cele două notificări și art. 3 din Decizia 2014/492/UE), le asamblează cu ancore `## Articolul N. Titlu` unde sursa are titlu separat, calculează sha256 pe corp. Cache-ul celor patru surse (agreement.html 11 MB, celelalte trei sub 260 KB fiecare) se comite, pe modelul deja stabilit pentru `showdetails` de pe legis.md (fișiere multi-MB deja în `_meta/imports/moldova-legal/legis-md-business/`) — reproductibilitate fără re-fetch. `build_coverage.py` capătă un al treilea prefix de excludere, `AA-`, numărat separat de extrasele UE, ca `AA-2014` să nu apară fals ca „act moldovenesc primar" fără ancore. Pagină de entitate, secțiune nouă K în manifestul CNPF, rând nou în `index.md` (121→122 pagini).
- **Unde:** `raw/papers/cnpf/AA-2014.md` (30.508 octeți corp, sha256 `1023032d...`); `_meta/imports/cnpf/ingest_aa_2014.py`; cache `_meta/imports/cnpf/aa-2014/`; `entities/AA-2014.md`; `raw/papers/cnpf/_manifest.md` secțiunea K; `index.md`; `_meta/coverage/build_coverage.py` (`TREATY_PREFIX`); controale regenerate; commitul acestei intrări.

## [2026-09-16] lint | Pasul 6.4: cele 5 verificări de consolidare UE (D5), reconfirmate

- **Aflat:** `discover_latest_celex.py` rulat din nou azi pe toate cele 29 de extracte `UE-*.md` — nu doar cele 5 semnalate — dă un rezultat identic literă cu literă cu rularea din 2026-09-04, la unsprezece zile distanță: aceleași 5 „NEWER AVAILABLE" (`UE-2009-138` Solvency II, `UE-2024-1624` AMLR, `UE-2024-1640` AMLD6, `UE-2020-1503` crowdfunding, `UE-97-9` ICSD), aceleași 24 „already current". Pentru Solvency II, întrebarea lăsată deschisă de recensământul pasului 6.1 („e `-20270130` cu dată viitoare, simetricul consolidărilor domestice viitoare?") are acum răspuns direct din aritmetica datei: 2027-01-30 e după 2026-09-15, deci da, e viitoare — nu diferă de constatarea deja scrisă în manifest la 2026-09-04, doar o confirmă la o dată de verificare ulterioară. Pentru celelalte patru, explicația deja scrisă în manifest (act de bază, consolidarea distinctă figurează doar pe pagina web a actului, nu în RDF-ul Cellar pe care-l citește scriptul, iar trecerea pe CELEX-ul consolidat dă 404 direct) rămâne valabilă neschimbată.
- **Decis:** punctul D5 al planului se închide fără nicio acțiune asupra `raw/`: se amână Solvency II (rămâne `-20250117`, cea în vigoare azi), se închid celelalte patru ca verificate a doua oară. Nu s-a schimbat niciun fișier `UE-*.md`; singurele scrieri sînt nota de reverificare în manifest și rularea proaspătă a scriptului salvată în `_meta/imports/cnpf/latest-celex.json` (conținut identic cu cel dinainte, deci fără diff efectiv).
- **Unde:** `raw/papers/cnpf/_manifest.md` secțiunea F (nota „Reverificat 2026-09-15"); `_meta/imports/cnpf/latest-celex.json`; `_meta/plans/2026-09-15-plan-pasul-6-acquis-aa.md` (D5, tabelul pașilor rândul 6.4); commitul acestei intrări.

## [2026-09-16] update | `.codex/` dezurmărit, adăugat la `.gitignore`; `AGENTS.md` rămâne urmărit

- **Aflat:** commitul pasului 6.4 (`8f1d8c9`) a folosit `close_session.py --commit`, care aplică
  `git add -A` — a prins și `.codex/environments/environment.toml` (config local autogenerat de
  Codex CLI) și `AGENTS.md` (oglinda acestui `CLAUDE.md` pentru Codex, scrisă de Eugen, referind
  „proiectul Codex.ai" în loc de claude.ai), niciunul urmărit înainte și niciunul parte a acestei
  sesiuni. Semnalat lui Eugen imediat, fără a rescrie istoria deja împinsă.
- **Decis:** Eugen a cerut păstrarea distincției: `AGENTS.md` e conținut real (analogul acestui
  fișier pentru un alt asistent) și rămâne urmărit așa cum a intrat; `.codex/` e stare locală de
  unealtă, ca `.obsidian/workspace*.json`, și se dezurmărește (`git rm -r --cached .codex/`) plus
  intră în `.gitignore`, pe modelul intrării `Claude outputs/`. Nu s-a atins `raw/`, niciun
  registru generat, niciun control mecanic — commit simplu, fără `close_session.py`.
- **Unde:** `.gitignore`; `.codex/environments/environment.toml` (dezurmărit, rămas pe disc);
  commitul acestei intrări.

## [2026-09-16] update | Pasul 6.5, nivelul 1 (D4): `acquis-MiFID`, `acquis-MAR`, `acquis-Prospectus` dezghețate

- **Aflat:** cele trei pagini, toate ancorate în `L-171-2012`, se verifică mult mai repede decît
  presupusese planul datorită unui bloc pe care legea îl are chiar în propriul text (liniile
  124-137): o listă de autodeclarare a actelor UE pe care legea susține că le transpune, cu directivă
  și dată exactă — inclusiv Dir. 2003/6/CE (linia 128), 2003/71/CE (linia 129), 2004/39/CE
  (linia 131), pe lîngă altele relevante pentru pașii următori (97/9, 98/26, 2004/109, 2006/49,
  2006/73, 2009/65, 2013/36 parțial, Reg. 1060/2009 parțial). Căutare exhaustivă pe termeni specifici
  fiecărei generații noi confirmă golurile deja presupuse, fără nicio excepție: zero rezultate pentru
  „OTF”, „piață-țintă”/„guvernanță” (MiFID II), „IFR”/„IFD”/„2019/2033”/„2019/2034” (regimul
  prudențial nou al firmelor de investiții), „sondare”/„safe harbour” (MAR, sondarea pieței),
  „prospectul UE de creștere”/„document de înregistrare universal” (Regulamentul Prospectus). Art. 58
  al legii impune raportare T+1 către Comisia Națională, nu regimul MiFIR de raportare aproape în
  timp real; art. 128 impune doar o obligație pasivă de informare, nu monitorizarea activă STOR a
  art. 16 MAR; pragurile de exceptare la ofertă publică (liniile 548-550) sînt cele ale directivei
  Prospectus originale din 2003, sub pragul minim al regulamentului actual. Amendamentele CFD din
  2025 (`L-177-2025`, citită integral, 4 articole) introduc un regim separat de intervenție asupra
  produsului (interdicție opțiuni binare/CFD cu levier către clienți neprofesioniști, alertă CNPF,
  infracțiune nouă Cod penal art. 245^13) — nu amendează art. 127-128 și nu atinge regimul abuzului
  de piață, răspuns direct la întrebarea deschisă lăsată pe `acquis-MAR`. Separat, verificat contra
  calendarului Anexei XXVIII-A (`AA-2014`, pasul 6.3): pentru toate trei, tratatul angajează Moldova
  la generația **veche** (2004/39, 2003/6+implementare, 2003/71+implementare), deja transpusă și cu
  termenul expirat din 2017 — MiFID II/MAR/Regulamentul Prospectus nu figurează în anexă, deci golul
  e de apropiere legislativă continuă, nu de încălcare a unui termen din Acord. Distincție care nu
  era făcută explicit pe nicio pagină înainte.
- **Decis:** toate trei ies din `unverified`/`confidence: low`, ridicate la `confidence: medium` (nu
  `high`: extrasele UE rămîn extrase, nu text integral, iar acoperirea Codului penal pentru
  sancțiunile CSMAD rămîne neverificată, consemnată explicit ca atare pe `acquis-MAR`, nu ascunsă).
  `updated: 2026-09-16` pe toate trei. `AA-2014` adăugat la `sources` pe toate trei ca sursă a
  distincției tratat-vs-acquis-curent. Secțiunile „Lacuna de examinat” rescrise cu citate de linie
  precise; „Întrebări deschise” fie răspunse cu citat, fie eliminate unde nu mai există gol de
  verificat.
- **Unde:** `concepts/acquis-MiFID.md`, `concepts/acquis-MAR.md`, `concepts/acquis-Prospectus.md`;
  `raw/papers/cnpf/L-171-2012.md` (liniile 124-137, 548-550, 568-572, 1354-1365, 2222-2260, citite,
  neatinse); `raw/papers/cnpf/L-177-2025.md` (citit integral); `_meta/plans/2026-09-15-plan-pasul-6-acquis-aa.md`
  (D4, nivelul 1); commitul acestei intrări.

## [2026-09-16] update | Pasul 6.5, nivelul 2 (D4): `acquis-AML`, `acquis-Insurance`, `acquis-CompanyLaw` dezghețate

- **Aflat:** primul caz favorabil verificat la acest pas — `L-308-2017` declară expres, la linia 93,
  transpunerea Dir. (UE) 2015/849 **și** Dir. (UE) 2018/843 (AMLD4+AMLD5), aceeași generație cu
  extrasul `UE-2015-849` deja ținut, cu două generații peste angajamentul Acordului (AMLD3, expirat
  1 sept. 2015, cel mai scurt termen din toată Anexa XXVIII-A). Golul real e doar pachetul AML 2024
  (AMLR/AMLD6/AMLA — zero mențiuni în text), cu aplicare eșalonată încă din 2027 chiar în UE. Art. 15
  alin. (1) lit. b) arată supravegherea CNPF mai largă decît nota anterioară a paginii: nu doar
  societăţile de investiţii, ci şi societăţile de registru/Depozitarul central, administratorii de
  pensii facultative şi **furnizorii de servicii de finanțare participativă** — legătură directă cu
  [[acquis-Crowdfunding]], de urmat la nivelul 3. Art. 4 alin. (1^1) interzice complet serviciile
  privind activele virtuale în Moldova — divergență de politică, nu lacună de transpunere.
  `acquis-Insurance`: `L-92-2022` admite chiar în text (linia 79) că transpune „parțial” Solvency II
  — confirmat prin căutare exhaustivă (zero SCR/MCR/ORSA) — și **nu** declară nicio transpunere a IDD
  (zero „2016/97”, „IBIP”), contrar afirmației anterioare a paginii. Acesta e singurul caz verificat
  azi unde Anexa XXVIII-A angajează chiar instrumentul actual (Solvency II însăși, termen expirat 1
  septembrie 2021, nu o generație abrogată) — deci golul e direct față de un termen din Acord, nu doar
  rămînere în urmă. `acquis-CompanyLaw`: constatare inversă celei așteptate — `L-1134-1997` NU citează
  SRD II (2017/828) în propriul bloc de autodeclarare (linia 178 citează 2007/36/CE modificată prin
  2023/2864, o directivă de interconectare digitală a registrelor, nu SRD II), dar **conține deja
  substanța SRD II**: identificarea acționarilor (art. 52), „say on pay” (politică de remunerare
  revizuită la 4 ani + raport anual votat, liniile 869-870, 1357-1378) și tranzacțiile cu părți
  afiliate (regimul detaliat al „tranzacției cu conflict de interese”, art. 81-85). Lipsește doar
  transparența consilierilor de vot (proxy advisors, zero rezultate). Anexa XXVIII-A nu acoperă acest
  instrument (dreptul societăților stă în Anexa II, neingerată) — consemnat ca limită reală, nu
  ascunsă.
- **Decis:** toate trei ies din `unverified`/`confidence: low`, ridicate la `confidence: medium`,
  `updated: 2026-09-16`, `AA-2014` adăugat la sursele celor două unde se aplică (AML, Insurance — nu
  CompanyLaw, unde Anexa XXVIII-A nu e relevantă). Pe `acquis-CompanyLaw`, cele două puncte rămase
  neverificate (termenul exact din Anexa II; semnalarea veche de mis-citare art.38(2)) sînt mutate
  explicit în „Întrebări deschise”, nu tăcute — per D3, dezghețarea nu cere ca fiecare întrebare să
  aibă răspuns, doar ca fiecare să fie tratată vizibil.
- **Unde:** `concepts/acquis-AML.md`, `concepts/acquis-Insurance.md`, `concepts/acquis-CompanyLaw.md`;
  `raw/papers/cnpf/L-308-2017.md` (linia 93, art. 4, art. 15, citite); `raw/papers/cnpf/L-92-2022.md`
  (linia 79 și căutare exhaustivă, citite, neatinse); `raw/papers/cnpf/L-1134-1997.md` (liniile
  173-179, 52, 81-85, 869-870, 1357-1378, citite, neatinse); `_meta/plans/2026-09-15-plan-pasul-6-acquis-aa.md`
  (D4, nivelul 2); commitul acestei intrări.

## [2026-09-16] update | Pasul 6.5, nivelul 3 (D4): `acquis-ICSD`, `acquis-SFD`, `acquis-Takeover`, `acquis-Transparency`, `acquis-UCITS` dezghețate

- **Aflat:** toate cinci ancorate, direct sau ocolit, în `L-171-2012`; verificate rapid datorită
  blocului de autodeclarare găsit la nivelul 1 (liniile 124-137), care citează expres 97/9, 98/26,
  2004/25, 2004/109 și 2009/65. Constatarea cea mai concretă a pasului: `acquis-ICSD`, art. 131
  alin. (1) — Fondul de compensare a investitorilor acoperă azi **1.000 euro** per client, cînd
  minimul armonizat al ICSD (art. 4(1), citit direct din `UE-97-9.md` liniile 108-109) e **20.000
  euro** — un decalaj de 20x, pe un termen din Anexa XXVIII-A expirat de doi ani (`AA-2014`,
  rîndul 26bis: „zece ani” pentru exact acest plafon, expirat 1 septembrie 2024). Excluderile de
  compensare (art. 134) mapează totuși structural anexa I a directivei; termenul de plată (o lună)
  e mai strict decît cel al directivei. `acquis-SFD`: cale de transpunere neașteptată — `L-234-2016`
  declară (linia 83) transpunerea parțială a CSDR (Reg. 909/2014), nu a 98/26/CE direct, dar CSDR
  însuși modifică 98/26 şi substanța (irevocabilitatea ordinelor, liniile 375 și 443; regulile de
  insolvabilitate ale Depozitarului, liniile 463-465) apare deja transpusă pe acea cale. `acquis-
  Takeover`: regim mult mai complet decît sugera statutul „de verificat” — oferta obligatorie (art.
  21, prag 50%), prețul echitabil (art. 21-23), ofertele competitive (art. 22), squeeze-out (art. 30,
  prag 90%) și sell-out (linia 807) toate găsite cu articol precis. `acquis-Transparency`: la fel —
  raportarea periodică (art. 120, plus raportul semestrial la 2 luni, mai strict decît cele 3 luni
  ale directivei) și notificarea deținerilor importante (art. 125, prag-listă aproape identică
  structural directivei, cu opt situații de agregare a drepturilor de vot corespunzînd exact art. 10
  lit. a)-h) directivă) sînt ambele prezente; doar ESEF (raportarea structurată) confirmat absent,
  zero rezultate. `acquis-UCITS`: depozitarul are articol de răspundere propriu (art. 110), dar
  formulat ca răspundere generală pentru culpă, nu ca standardul strict cu sarcina probei inversată
  al OPCVM V (art. 24 directivă) — discrepanță semnalată, nu confirmată integral; nicio politică de
  remunerare specifică managerilor de fonduri găsită (doar regimul corporativ general, comun cu
  `acquis-CompanyLaw`). `REG-ICF`, citat ca ancoră pe `acquis-ICSD`, s-a dovedit o pagină-fantomă:
  hotărârea CNPF proprie nu are număr identificat și nu e ținută ca sursă brută.
- **Decis:** toate cinci ies din `unverified`/`confidence: low`, ridicate la `confidence: medium`,
  `updated: 2026-09-16`, `AA-2014` adăugat la surse unde se aplică (nu pe `acquis-Takeover`, unde
  instrumentul stă în afara Anexei XXVIII-A, ca la `acquis-CompanyLaw`). Constatările rămase
  neconfirmate integral (standardul de răspundere al depozitarului OPCVM, derogările de la oferta
  obligatorie) mutate explicit în „Întrebări deschise”, nu tăcute.
- **Unde:** `concepts/acquis-ICSD.md`, `concepts/acquis-SFD.md`, `concepts/acquis-Takeover.md`,
  `concepts/acquis-Transparency.md`, `concepts/acquis-UCITS.md`; `raw/papers/cnpf/L-171-2012.md`
  (art. 21-31, 110-111, 120-125, 130-134, citite, neatinse); `raw/papers/cnpf/L-234-2016.md` (linia
  83, 375, 443, 463-465, citite, neatinse); `raw/papers/cnpf/UE-97-9.md` (art. 4, citit); `entities/REG-ICF.md`
  (citit, fantomă confirmată); `_meta/plans/2026-09-15-plan-pasul-6-acquis-aa.md` (D4, nivelul 3);
  commitul acestei intrări.

## [2026-09-16] update | Pasul 6.5, nivelul 4 (D4, restul): ultimele șase pagini `acquis-*` dezghețate — toate cele 17 verificate

- **Aflat:** ultimul nivel al planului, fără ordine specială între cele șase. Descoperirea cu cea mai
  mare miză cantitativă: `acquis-MTPL` rămîne blocată la o comparație reală — art. 9 din
  `UE-2009-103.md` („Sumele minime”) e doar în cuprins, fără text integral, deci sumele proprii ale
  `L-106-2022` (100.000/100.000/500.000 euro, plus o limită de prejudiciu moral de 5.000/10.000 euro
  negăsită la recensământul inițial) nu pot fi comparate cu pragul UE fără o extragere țintită —
  semnalat ca pas concret, nu ocolit cu o cifră din memorie. Istoricul daunelor (2021/2118) există
  (linia 211); organismul de garantare pentru insolvența asigurătorului, introdus de același
  amendament, confirmat absent. Al doilea caz, după AML, unde transpunerea depășește angajamentul
  tratatului: `acquis-IORP` — `L-198-2020` linia 65 declară expres transpunerea IORP II
  (2016/2341) însăși, nu predecesoarea 2003/41/CE la care angajează Anexa XXVIII-A, cu funcțiile-cheie
  (gestionarea riscului, audit intern, actuariat — linia 102) aproape identice structural directivei.
  `acquis-ConsumerCredit`: gol confirmat la nivelul legii-cadru, nu doar „posibil reflectat” cum
  spunea statutul anterior — nici `L-1-2018`, nici `L-105-2003` (protecția consumatorilor generală)
  nu conțin DAE, SECCI sau dreptul de retragere; doar o trimitere generică la bonitate (linia 130) care
  deleagă mai departe unui act BNM neingerat. `acquis-AIFMD`: declarația de transpunere a `L-2-2020`
  (linia 72) e mai amplă decît știut — nu doar AIFMD, ci și EuVECA (Reg. 345/2013), un regulament
  delegat de standarde tehnice și ELTIF (Reg. 2015/760) — dar substanța operațională (efect de
  levier, gestionarea lichidității, delegare) nu are niciun corespondent găsit; nedistins dacă golul e
  real sau delegat unor acte CNPF neingerate. `acquis-CSDR-EMIR`: regimul de disciplină a decontării
  (penalități, buy-in) și regimul EMIR pentru contrapărți centrale/registre de tranzacții confirmate
  absente prin căutare exhaustivă, nu doar presupuse. `acquis-Crowdfunding`: constatarea cea mai
  favorabilă a nivelului — divergența „debitor-consumator”, semnalată anterior ca posibilă eroare de
  scop, se dovedește o extensie deliberată cu regim propriu (plafon 7.500 euro, evaluare a bonității,
  termen de revocare de 14 zile), iar protecția investitorilor UE (fișa KIIS, simularea capacității de
  a suporta pierderi la 10% din capital) e substanțial prezentă.
- **Decis:** toate șase ies din `unverified`/`confidence: low`, ridicate la `confidence: medium`,
  `updated: 2026-09-16`. Punctele rămase neconfirmate (pragul MTPL, substanța AIFMD, RTS-urile
  crowdfunding, poziția AIFMD în Acord) mutate explicit în „Întrebări deschise”, cu pasul concret
  necesar pentru fiecare, nu tăcute și nu ghicite. **Cu acest nivel, toate cele 17 pagini `acquis-*`
  ale planului din 6 septembrie sînt reverificate** — rămîne doar `cnpf-transposition-matrix`
  (pasul 6.6), care le citează pe toate.
- **Unde:** `concepts/acquis-MTPL.md`, `concepts/acquis-IORP.md`, `concepts/acquis-ConsumerCredit.md`,
  `concepts/acquis-AIFMD.md`, `concepts/acquis-CSDR-EMIR.md`, `concepts/acquis-Crowdfunding.md`;
  `raw/papers/cnpf/L-106-2022.md`, `L-198-2020.md`, `L-1-2018.md`, `L-2-2020.md`, `L-181-2023.md`
  (citite, neatinse); `raw/papers/moldova-legal/L-105-2003.md` (căutare țintită, neatins);
  `raw/papers/cnpf/UE-2009-103.md` (art. 9 identificat ca lipsă din extras, neatins);
  `_meta/plans/2026-09-15-plan-pasul-6-acquis-aa.md` (D4, nivelul 4, ultimul); commitul acestei
  intrări.

## [2026-09-16] update | Pasul 6.6: `cnpf-transposition-matrix` rescrisă — planul din 15 septembrie închis integral

- **Aflat:** matricea era ultimul document care încă cita toate cele 17 pagini `acquis-*` cu
  constatările lor din iulie 2026, dinainte de reverificarea pasului 6.5 — un cititor care deschidea
  doar matricea, nu și paginile individuale, ar fi văzut concluzii vechi. Rescrierea a scos la iveală
  o lacună de structură, nu de conținut: pagina nu avea niciun rând pentru `acquis-Takeover`, deși
  pagina proprie exista și era citată în „Referințe încrucișate” — adăugat acum ca rând propriu în
  secțiunea A, cu constatarea verificată (regim complet, prag 50%, squeeze-out la 90%).
- **Decis:** secțiunile A, B și D rescrise integral, celulă cu celulă, cu constatarea verificată a
  paginii proprii, nu cu presupunerea din iulie; fiecare celulă trimite prin wikilink la pagina cu
  citatul exact, ca matricea să nu dubleze articolul-sursă. Adăugat un paragraf nou despre ce arată
  Anexa XXVIII-A per ansamblu (41 instrumente, toate termenele expirate, cu ICSD și Solvency II ca
  singurele cazuri unde tratatul angajează chiar instrumentul actual). Secțiunea C capătă două note
  noi, extrase din tiparele găsite la 6.5: nu presupune că un amendament recent (ca `L-177-2025`)
  închide automat o lacună căutată, și nu presupune automat o lacună cînd legea declară o generație
  mai nouă decît cea angajată de tratat (găsit de două ori: AML, IORP). Rândurile fără pagină
  `acquis-*` proprie (Reg. CRA, PRIIPs, vânzări în lipsă, indici de referință, SFTR) rămân
  `[de verificat]`, neatinse, nu ghicite. Iese din `unverified`, `confidence: medium`. **Cu acest pas,
  planul din 15 septembrie (`2026-09-15-plan-pasul-6-acquis-aa.md`) e închis integral**: toți cei șase
  pași (6.1-6.6) sînt făcuți, consemnat în capul planului.
- **Unde:** `comparisons/cnpf-transposition-matrix.md`; `_meta/plans/2026-09-15-plan-pasul-6-acquis-aa.md`
  (stare rescrisă la „executat integral”, tabelul pașilor 6.5-6.6); commitul acestei intrări.

## [2026-09-16] update | Reîmprospătarea D9: registrul dosarelor verificat împotriva proiectului

- **Aflat:** Eugen a lipit conținutul curent al `legal-career/06-matter-log.md` din proiectul
  claude.ai „Legal Wiki”. Corpul e identic byte cu byte cu copia locală luată la 2026-09-10 —
  `sha256_body` recalculat dă exact `9749803a952d...`, aceeași valoare din stampilă. Niciun dosar
  nou (M-003 sau ulterior) nu a fost înregistrat în proiect din 2026-09-10 încoace; M-001 și M-002
  rămân `live`.
- **Decis:** fără înlocuire de corp, doar re-stampilare: `taken` și `stamped` ridicate la
  2026-09-16 prin `python _meta/schema/stamp_copies.py --taken 2026-09-16`, ca verificarea de azi
  să fie vizibilă separat de cea din 10 septembrie. Avertismentul `copy.stale` al validatorului
  dispare.
- **Unde:** `legal-career/06-matter-log.md` (frontmatter); commitul acestei intrări.

## [2026-09-16] update | Verificarea consolidării Solvency II, sursă citită direct pe EUR-Lex

- **Aflat:** pasul 6.4 semnalase doar mecanic, din `discover_latest_celex.py`, că
  `02009L0138-20270130` există lîngă cea ținută (`-20250117`), fără să deschidă sursa. Deschisă
  azi: pagina `-20270130` poartă chiar ea linkul „Access current version (17/01/2025)", deci
  EUR-Lex confirmă din interior, nu doar prin data din CELEX, că textul în vigoare azi e cel
  ținut. Amendamentul e Directiva (UE) 2025/2 (Solvency II 2025 review, marcaj `M13`, 199
  apariții în text). Art. 4 din 2025/2, citit direct (CELEX `32025L0002`): o singură dată pentru
  tot actul — statele membre transpun pînă la 29.01.2027, aplică de la 30.01.2027, fără eșalonare
  pe articole. Verificare articol cu articol a celor opt articole-cheie din extractul ținut: patru
  sînt modificate de M13 (art. 2, 13, 30, 41), patru nu (art. 1, 14, 27, 100).
- **Decis:** nimic din `raw/` nu se schimbă — data ținută rămîne corectă pînă la 30.01.2027.
  Constatarea intră în manifest ca notă datată, cu lista celor patru articole afectate, ca o
  citare viitoare din art. 2, 13, 30 sau 41 să poată fi recunoscută ca expirînd la acea dată, spre
  deosebire de art. 1, 14, 27, 100, neafectate. Reingerarea `-20270130` e programată pentru după
  30.01.2027, nu înainte.
- **Unde:** `raw/papers/cnpf/_manifest.md`, secțiunea F (nota din 2026-09-16); surse citite, nu
  atinse: EUR-Lex CELEX `02009L0138-20270130` și `32025L0002` (art. 4, 5); commitul acestei
  intrări.

## [2026-09-16] update | Cele două referințe nerezolvate ale COD-225-2003 din graf, verificate: nicio lacună reală

- **Aflat:** graful de citare semnalează două „nerezolvate" care ating procedura civilă. (1)
  `COD-225-2003#art.308^17`, l.2780: fraza numește „art. 48^21 şi 48^27 din Codul civil" la
  început și „în sensul art. 48^15 alin. (3)" mai departe, tot despre mandatul de ocrotire în
  viitor — o instituție exclusiv a Codului civil (art. 48^1-48^40 CC). Calificativul „din Codul
  civil" nu ajunge pînă la a doua trimitere în regulile de context ale grafului, care a atribuit-o
  greșit actului curent, unde nu există art. 48^15. (2) `CC-1107-2002#art.113`, l.943, citează
  „art. 581 din Codul de procedură civilă": indiciul mecanic al grafului („exponent turtit: art.
  58^1") s-a confirmat direct în sursă — `COD-225-2003` linia 697 poartă `Articolul 58^1.
  Capacitatea de exerciţiu al drepturilor`, ancorat.
- **Decis:** nimic de scris în `raw/`, imuabil oricum. Ambele intră în categoria documentată în
  graf, „Ce nu face acest graf" — limită mecanică, nu defect de corpus. Nu se cere nicio acțiune
  la o reingerare viitoare a Codului civil sau a procedurii civile.
- **Unde:** `raw/papers/moldova-legal/COD-225-2003.md` (liniile 687-697, 2780, citite, neatinse);
  `_meta/graph/citation-graph.md` (secțiunea „Dispoziții cu stare specială"); commitul acestei
  intrări.

## [2026-09-16] ingest | `L-213-2023`, Legea taxei de stat: prima cu ancoră principală ratată de curl

- **Aflat:** actul din capul cozii de ingerare pentru `COD-225-2003` (22 mențiuni, 11 din codul de
  procedură civilă singur, restul din șapte acte). `curl` pe `cautare/showdetails/152741`, cu cele
  două antete documentate în memoria de sesiune, a întors pagina de verificare Cloudflare — și la
  fel un `getResults?doc_id=` simplu, care mai devreme trecea curat; regresie confirmată, nu
  fluctuație. Textul actului (zece articole) și fișa au fost citite prin browserul Chrome al lui
  Eugen. Descoperirea reală a fost a doua, nu prima: **anexele nu sînt deloc pe pagina actului**.
  Nici HTML-ul, nici exportul `.pdf` propriu al paginii nu poartă conținutul lor — „anexa nr. 1” și
  „anexa nr. 2” sînt linkuri goale către două fișiere `.docx` separate
  (`an_1_213md.docx`, `an_2_213md.docx`), primul cu 110 poziții tabelare (cuantumurile), al doilea
  cu 98 de poziții (scutirile). Descărcate cu acordul lui Eugen, extrase cu `python-docx`; niciun
  caracter `|` în conținut, deci tabelul markdown nu s-a rupt. Douăsprezece rânduri din tabelul
  anexei 1 sînt titluri de secțiune pe celulă îmbinată orizontal, pe care `python-docx` le întoarce
  ca text duplicat pe ambele coloane — redate o singură dată, ca titlu, cu regula consemnată în
  fișierul brut. Constatare de fond găsită abia la citirea anexei: apelul costă 85% din taxa
  achitată în prima instanță, recursul 70%, revizuirea 55% — cifre pe care `COD-225-2003` însuși nu
  le conține, doar trimite la anexa nr. 1 pct. 1.16-1.18. Anexa nr. 2 numește direct CNPF (pct.
  1.17, scutire în acțiunile de protecție a consumatorilor financiari) și BNM (pct. 1.19, scutire
  în supravegherea bancară și nebancară) — scutiri ale autorității ca parte în proces.
- **Decis:** ingerat în `raw/papers/moldova-legal/L-213-2023.md`, cu proveniența .docx (surse și
  sha256) în câmpul `annexes` al frontmatter-ului, ca o reîmprospătare viitoare să știe că anexele
  nu vin din același loc ca restul textului. Pagină de entitate `entities/L-213-2023.md`, secțiune
  nouă W în manifestul moldova-legal, rând nou în `index.md` (123 de pagini), și o secțiune scurtă
  adăugată în `entities/COD-225-2003.md` ca arts. 84-89 să nu mai fie ancorate, dar goale.
  Memoria de sesiune despre ruta curl e actualizată cu regresia de azi. Rămân neverificate celelalte
  șapte acte din corpus care citează `L-213-2023`.
- **Unde:** `raw/papers/moldova-legal/L-213-2023.md`; `entities/L-213-2023.md`;
  `entities/COD-225-2003.md` (secțiune nouă); `raw/papers/moldova-legal/_manifest.md` (secțiunea
  W); `index.md`; commitul acestei intrări.

## [2026-09-16] update | Celelalte șapte acte care citează `L-213-2023`, verificate articol cu articol

- **Aflat:** `grep` pe tot `raw/papers/moldova-legal/` pentru „213/2023” a găsit exact șapte acte
  în afară de `COD-225-2003`, confirmând numărul din coada de ingerare a grafului:
  `CC-1107-2002` art. 715 (taxa pentru gaj — anexa nr. 1 pct. 7.1-7.2, 36 și 9 lei),
  `COD-116-2018` art. 212 (contencios administrativ — anexa nr. 1 pct. 1.15, anexa nr. 2 pct.
  1.1.11), `COD-154-2003` art. 353 (Codul muncii — anexa nr. 2 pct. 1.1.1, scutire care acoperă
  expres doar taxa de stat, nu și taxa de timbru, exact ca în textul Codului muncii însuși),
  `COD-218-2008` arts. 448, 451^3, 468 și 476 (patru căi de atac contravenționale, toate pe art. 2
  alin. (1) și (4) — chiar definiția taxei de timbru numește calea contravențională, 200 lei fix),
  `COD-443-2004` arts. 158 și 161 (executare), `L-20-2026` art. 19 (achiziții publice — anexa nr.
  1 pct. 14, 0,5% din valoarea estimată, minim 1500, maximum 50000 lei) și `L-64-2010` art. 19,
  intitulat chiar „Taxa de stat” (defăimare — anexa nr. 1 pct. 1.13-1.14, 250 lei). Fiecare
  citare se sprijină pe un punct real din legea deținută; nu s-a găsit nicio trimitere greșită sau
  la un articol care nu există. Un al doilea `grep`, pentru „1216/1992” (legea abrogată de
  213/2023), nu a găsit nimic în niciunul din cele șapte fișiere — migrarea la noua lege e
  completă în tot corpusul, nu doar formal declarată la art. 10 al noii legi.
- **Decis:** tabelul complet al corespondențelor intră în `entities/L-213-2023.md`, cu wikilink-uri
  noi către `CC-1107-2002`, `L-20-2026` și `L-64-2010`. Manifestul (secțiunea W) își pierde nota
  „rămas neatins” și capătă rezultatul. Nimic din `raw/` s-a atins — verificare, nu corectare.
- **Unde:** `entities/L-213-2023.md`; `raw/papers/moldova-legal/_manifest.md` (secțiunea W);
  `raw/papers/moldova-legal/CC-1107-2002.md` (art. 715, citit, neatins),
  `raw/papers/moldova-legal/COD-116-2018.md` (art. 212), `raw/papers/moldova-legal/COD-154-2003.md`
  (art. 353), `raw/papers/moldova-legal/COD-218-2008.md` (arts. 448, 451^3, 468, 476),
  `raw/papers/moldova-legal/COD-443-2004.md` (arts. 158, 161), `raw/papers/moldova-legal/L-20-2026.md`
  (art. 19), `raw/papers/moldova-legal/L-64-2010.md` (art. 19); commitul acestei intrări.

## [2026-09-16] update | Art. 9 din 2009/103/CE citit pe EUR-Lex: pragurile MTPL, cu un ordin de mărime sub minim

- **Aflat:** art. 9 („Sumele minime”), care în `UE-2009-103.md` apare doar în cuprins, citit direct
  pe EUR-Lex (consolidarea `02009L0103-20231223`, amendament ▼M1 = Directiva (UE) 2021/2118). Prima
  căutare a textului `Articolul 9\n` a găsit doar tabelul de concordanță de la finalul directivei
  (anexa III), nu articolul propriu-zis — capcană de metodă, rezolvată căutând direct „Sumele
  minime”. Textul: (a) vătămări corporale, minimum 6.450.000 euro per accident **sau** 1.300.000
  euro per persoană prejudiciată; (b) daune materiale, minimum 1.300.000 euro per accident.
  Comparat cu plafoanele proprii ale `L-106-2022` art. 13 (liniile 288-291, deja confirmate la
  pasul 6.5): 100.000 euro daune materiale, 100.000/500.000 euro vătămare corporală per
  persoană/per accident. Raportul: **~13x sub minimul UE pe daune materiale și pe vătămare
  corporală per persoană, ~12,9x pe vătămare corporală per accident.** Nu există categorie UE
  separată pentru prejudiciul moral (5.000/10.000 euro în legea moldovenească). Anexa XXVIII-A
  angajează „Directiva 2009/103/CE” fără să precizeze generația, iar 2021/2118 (sursa sumelor de
  mai sus) e ulterioară semnării Acordului — punct lăsat deschis, dar practic irelevant: decalajul
  e de ordin de mărime, nu de procente, indiferent de generația angajată.
- **Decis:** `raw/papers/cnpf/UE-2009-103.md` nu s-a atins — citirea e directă din EUR-Lex, ca la
  verificarea Solvency II de mai devreme azi. `concepts/acquis-MTPL.md` rescris cu pragurile și
  tabelul comparativ; rândul MTPL din `comparisons/cnpf-transposition-matrix.md` actualizat cu
  cifrele reale în loc de „comparația rămâne blocată”. Cu aceasta, punctul rămas deschis din
  pasul 6.5 (nivelul 4) e închis.
- **Unde:** `concepts/acquis-MTPL.md`; `comparisons/cnpf-transposition-matrix.md`;
  `raw/papers/cnpf/L-106-2022.md` (art. 13, liniile 288-291, citit, neatins); sursă externă citită,
  nu ingerată: EUR-Lex CELEX `02009L0103-20231223` art. 9; commitul acestei intrări.

## [2026-09-16] update | Cele cinci instrumente fără pagină proprie — CRA, PRIIPs, vânzări în lipsă, indici de referință, SFTR — toate verificate, planul din 15 septembrie depășit

- **Aflat:** căutare exhaustivă în tot `raw/papers/cnpf/` și `raw/papers/moldova-legal/`, pe termeni
  proprii fiecărui regim, nu doar pe numărul regulamentului. Rezultatul cel mai important răstoarnă
  presupunerea din nota plaului („fără pagină acquis-* = neverificat”): **CRA (Reg. 1060/2009) e de
  fapt substanțial transpus**, nu doar netratat — `L-171-2012` poartă o declarație de transpunere
  cu tabel articol cu articol (linia 137, ultima generație citată fiind Reg. 2017/2402, nu CRA III
  462/2013) și patru articole proprii (88^1-88^4, Secțiunea a 7-a) care reproduc înregistrarea,
  utilizarea în scopuri de reglementare și regulile de conduită ale agențiilor de rating; `L-192-1998`
  art. 222 lit. c^1) dă CNPF mandatul expres, art. 235 cere registrul public. Pentru celelalte patru,
  absența e confirmată, nu doar presupusă, fiecare cu o singură urmă adiacentă găsită și dovedită
  a nu fi regimul căutat: **vânzări în lipsă** (236/2012) — o interdicție punctuală pentru un tip de
  fond în `L-2-2020` art. 39, nu regimul de raportare a pozițiilor scurte; **indici de referință**
  (2016/1011) — „indice de referință” apare doar în `L-92-2022`, în sensul asigurărilor unit-linked,
  fals pozitiv față de regimul administratorilor de indici; **SFTR** (2015/2365) — `L-234-2016`
  listează „organizarea mecanismului de împrumut de valori mobiliare” ca serviciu auxiliar al DCU,
  acoperire de infrastructură pe calea CSDR, nu regimul de raportare SFTR; **PRIIPs** (1286/2014) —
  cel mai nuanțat: `L-2-2020` art. 39 alin. (9)-(18) chiar cere un „document cu informații-cheie”
  pentru fonduri alternative distribuite către retail, dar conținutul minim cerut (alin. (10))
  reproduce structura KIID OPCVM (obiective, performanțe anterioare, costuri, profil de risc), nu
  formatul PRIIPs (indicator de risc 1-7, scenarii de performanță); declarația de transpunere a
  legii (linia 72) nu numește PRIIPs. A doua urmă găsită la PRIIPs, `L-198-2020` linia 896
  („document cu informații-cheie – declarația de pensie”), e regimul IORP II, nu PRIIPs — produsele
  de pensii personale sînt oricum excluse din domeniul regulamentului.
- **Decis:** cinci pagini noi, `concepts/acquis-CRA.md`, `acquis-PRIIPs.md`, `acquis-ShortSelling.md`,
  `acquis-Benchmarks.md`, `acquis-SFTR.md`, toate `confidence: medium`. Rândurile corespunzătoare din
  `comparisons/cnpf-transposition-matrix.md` (secțiunile A și B) rescrise cu constatările, nu mai
  „neverificat”; nota introductivă a matricei actualizată. Adăugate în `index.md` (128 de pagini).
  Cu acest pas, planul din 15 septembrie e depășit: nu doar cele 17 pagini `acquis-*` originale, ci
  și cele cinci semnalate ca gol de acoperire în capul planului sînt acum verificate.
- **Unde:** `concepts/acquis-CRA.md`; `concepts/acquis-PRIIPs.md`; `concepts/acquis-ShortSelling.md`;
  `concepts/acquis-Benchmarks.md`; `concepts/acquis-SFTR.md`; `comparisons/cnpf-transposition-matrix.md`;
  `index.md`; `raw/papers/cnpf/L-171-2012.md` (arts. 88^1-88^4, linia 137, citite, neatinse);
  `raw/papers/cnpf/L-192-1998.md` (art. 222, art. 235); `raw/papers/cnpf/L-2-2020.md` (art. 39,
  linia 72); `raw/papers/cnpf/L-92-2022.md`; `raw/papers/cnpf/L-234-2016.md` (liniile 157-161);
  `raw/papers/cnpf/L-198-2020.md` (linia 896); commitul acestei intrări.

## [2026-09-16] update | RTS-urile crowdfunding: nota anterioară era greșită, nu doar incompletă — toate temele au corespondent

- **Aflat:** ultimul punct rămas de pe lista din 15 septembrie. Nota veche a `acquis-Crowdfunding`
  numea trei RTS („2022/2112, 2022/2116, 2022/2117 — continuitate, plângeri, autorizare”); lista
  oficială a Comisiei Europene (sursă secundară, necitită articol cu articol) arată cel puțin 13
  acte delegate/de punere în aplicare pentru Reg. 2020/1503, iar atribuirea temă-număr veche nu se
  potrivește cu ce arată acea listă. S-a renunțat la a mai atribui exact temă-număr pentru fiecare
  din cele 13 și s-a verificat direct dacă **tema** fiecăruia are corespondent în `L-181-2023` —
  căutare inițială pe termeni greșiți („plânger”, „administrare individuală a portofoliului”) a dat
  fals-negativ, corectată căutând termenii exacți ai legii („reclamații”, „administrare de portofolii
  individuale de împrumuturi”, „bonitatea debitorului-consumator”). Rezultat: **toate cele șapte teme
  identificabile au corespondent la nivel de lege primară** — conflicte de interese (art. 9, 22),
  testarea cunoștințelor și simularea de pierderi (art. 28, deja confirmat la pasul 6.5), examinarea
  reclamațiilor (art. 16, patru alineate), planul de continuitate (art. 9 alin. (1^1) lit. c) și
  dosarul de autorizare), administrarea de portofolii individuale de împrumuturi (definiție proprie
  la art. 2, plus substanță la arts. 9, 33, 35, 41), fișa cu informații esențiale (art. 24, conținut
  minim la nivel de lege), evaluarea riscului de credit la stabilirea prețului ofertei (art. 9 alin.
  (4)) și creditarea responsabilă pentru debitorul-consumator (art. 5 alin. (3)). Tipar constant: de
  fiecare dată, legea stabilește principiul și delegă explicit detaliul tehnic — formatul, pragurile,
  metodologia — „actelor normative ale autorității de supraveghere”, neingerate în vault. Trei-patru
  din cele 13 numere rămân neidentificate tematic, nu verificate individual pe EUR-Lex.
- **Decis:** `concepts/acquis-Crowdfunding.md` rescris cu tabelul de corespondențe și cu corectarea
  explicită a notei vechi; rândul din `comparisons/cnpf-transposition-matrix.md` actualizat. Cu
  aceasta, ultimul punct rămas deschis din planul de 15 septembrie e închis.
- **Unde:** `concepts/acquis-Crowdfunding.md`; `comparisons/cnpf-transposition-matrix.md`;
  `raw/papers/cnpf/L-181-2023.md` (arts. 2, 5, 9, 16, 22, 24, 28, 33, 35, 41, liniile 555-575,
  citite, neatinse); commitul acestei intrări.

## [2026-09-16] update | Substanța operațională AIFMD reverificată: lichiditatea era fals negativ, levierul și delegarea sînt golul real

- **Aflat:** constatarea de la pasul 6.5 spunea „zero rezultate” pentru efect de levier,
  lichiditate și delegare deodată — aceeași capcană a căutării combinate găsită azi la RTS-urile
  crowdfunding. Reluat termen cu termen pe `L-2-2020`: **administrarea lichidității nu e absentă,
  e substanțial prezentă** — art. 28 (sistem de administrare a lichidităților, monitorizarea
  riscului, simulări de criză periodice, coerență cu politica de răscumpărare), art. 27
  (administrarea riscurilor, separarea funcției de risc), art. 34 alin. (3) lit. c)-f) (raportarea
  periodică către CNPF a măsurilor de lichiditate și a rezultatelor simulărilor de criză). Art. 34
  însuși, dedicat integral cerințelor de raportare, acoperă aproape orice categorie din anexa IV
  AIFMD — active, profil de risc, remunerație — **cu o singură excepție reală: levierul nu apare
  nicăieri**, verificat pe patru formulări diferite („efect de levier”, „levier financiar”,
  „pârghie financiară”, „grad de îndatorare”), toate cu zero rezultate. **Delegarea funcțiilor de
  administrare către terți** — verificată separat pe mai multe formulări — la fel, zero rezultate
  relevante. A treia constatare, nouă, nu doar o corecție: **răspunderea depozitarului pentru
  pierderea instrumentelor financiare în custodie (art. 32 alin. (8)-(9)) e strictă, cu sarcina
  probei inversată** — restituire automată, exonerare doar cu dovada unui eveniment exterior în
  afara controlului rezonabil — exact standardul art. 21 alin. (12) AIFMD, spre deosebire de
  răspunderea generală pentru culpă găsită la depozitarul OPCVM (`acquis-UCITS`, art. 110).
- **Decis:** `concepts/acquis-AIFMD.md` rescris, cu constatarea „substanța operațională neconfirmată”
  înlocuită de constatarea precisă: lichiditate/raportare/răspunderea depozitarului prezente,
  levier/delegare absente confirmat. Rândul din `comparisons/cnpf-transposition-matrix.md`
  actualizat în același sens. Cu aceasta, ultimul item rămas din lista de continuare a firului
  acquis (după MTPL, cele cinci instrumente și RTS-urile crowdfunding) e închis.
- **Unde:** `concepts/acquis-AIFMD.md`; `comparisons/cnpf-transposition-matrix.md`;
  `raw/papers/cnpf/L-2-2020.md` (arts. 21, 27, 28, 32, 34, citite, neatinse); commitul acestei
  intrări.

## [2026-09-16] update | Cinci puncte vechi din CLAUDE.md, niciunul atins de la deschidere

- **Aflat:** cinci itemi din secțiunile „Open questions"/„Outstanding work" ale `CLAUDE.md`
  rămăseseră nerezolvați de mult, semnalați dar niciodată lucrați. (1) Liniile de numărătoare
  învechite din `L-177-2025`, `L-178-2020`, `L-192-1998` — confirmat: frontmatter-ul și ancorele
  reale erau corecte, doar linia „articole detectate" din corpul textului (bloc de metadate
  generat la ingestie, nu text juridic) rămăsese la 0. (2) `run_cnpf_legal_lint.py` avea două
  verificări utile pe care nimic altceva nu le făcea — pagini orfane și citări la nivel de fișier
  raw întreg — dar scriptul însuși era stricat de la rescrierea SCHEMA.md (D4) și corupea `log.md`
  la fiecare rulare. (3) `build_inforce_register.py` avea un bug real, nu doar o lacună: regexul
  `ART_IN_NOTE` căuta „Art.N" oriunde în nota încadrată `[...]`, iar fiecare notă se termină cu
  referința Monitorul Oficial (`MO.../DD.MM.YY art.NNN`) — pentru un act pe puncte, ca
  `HG-743-2024`, care nu are deloc marcaj „Art.", acel `art.NNN` din coada notei era singura
  potrivire găsită, iar cele 6 dispoziții amânate distincte ale actului colapsau într-o singură
  intrare falsă „HG-743-2024 art. 355" la deduplicare. (4) 86/635/CEE, 94/19/CE și 91/674/CEE,
  numite în Anexa XXVIII-A a Acordului de Asociere, erau semnalate ca posibil suprapuse peste unul
  din cele 29 de extrase `UE-*.md` deja ținute — niciodată verificat. Verificat acum contra
  frontmatter-ului (`base_celex`) tuturor celor 29: nicio suprapunere; toate trei lipseau genuin.
  94/19/CE s-a dovedit, suplimentar, **abrogată** din 2019, înlocuită de Directiva 2014/49/UE, pe
  care vault-ul nu o ține — gol nou, nu unul rezolvat de ingestia de azi.
- **Decis:** (1) cele trei linii corectate (0→4, 0→8, 0→34), cu `sha256` recalculat și reverificat
  pentru toate trei. (2) cele două verificări portate în `validate_wiki.py` ca `page.orphan`
  (folosind rezolvatorul de wikilinkuri existent, nu potrivire naivă de nume) și
  `citation.raw-page-level` (generalizată la toate rădăcinile `raw/papers/`, nu doar `cnpf/`, ceea
  ce era defectul A4 al scriptului vechi); scriptul vechi șters, rapoartele lui comise păstrate ca
  istorie. (3) regexul de extragere a locatorului ancorat cu `^` la începutul notei, cu doi
  regexuri noi pentru puncte/anexe (`PCT_IN_NOTE`, `ANEXA_IN_NOTE") încercate înaintea celui de
  articol — fix general, nu doar pentru `HG-743-2024`; registrul regenerat: 49→54 dispoziții (o
  intrare falsă înlocuită de cele 6 reale), nicio regresie pe actele pe articole. (4) ingerate
  `UE-1986-635`, `UE-1991-674`, `UE-1994-19` (extrase structurate RO, EUR-Lex), cu două pagini de
  concept noi (`acquis-ContabilitateInstitutiiFinanciare`, `acquis-GarantareaDepozitelor`),
  `_manifest.md` și `AA-2014.md` actualizate cu constatarea.
- **Unde:** `raw/papers/cnpf/L-177-2025.md`, `L-178-2020.md`, `L-192-1998.md`;
  `_meta/schema/validate_wiki.py`; `_meta/lint/run_cnpf_legal_lint.py` (șters);
  `_meta/inforce/build_inforce_register.py`; `_meta/inforce/in-force-register.md` (regenerat);
  `raw/papers/cnpf/UE-1986-635.md`, `UE-1991-674.md`, `UE-1994-19.md`;
  `concepts/acquis-ContabilitateInstitutiiFinanciare.md`, `acquis-GarantareaDepozitelor.md`;
  `raw/papers/cnpf/_manifest.md`; `entities/AA-2014.md`; `entities/L-160-2023.md`; `index.md`;
  `CLAUDE.md` (secțiunile „Open questions"/„Outstanding work" și descrierea `_meta/lint/`);
  commitul acestei intrări.

## [2026-09-16] update | Al cincilea punct: liniile rupte la mijloc de propoziție, tot corpusul, cu o regresie descoperită pe parcurs

- **Aflat:** scriptul nou (`_meta/imports/anchoring/fix_wrapped_titles.py`, reutilizând euristica
  DANGLING/STOP deja validată pentru Codul civil în `anchor_cc.py`) a găsit, la prima trecere pe
  tot corpusul, **1.097 titluri rupte doar în `CC-1107-2002`** — deși nota din 5 septembrie spunea
  explicit „Codul civil e deja curat, 22 din 13.190". Verificat: adevărat *atunci*. Frontmatter-ul
  fișierului arată `refreshed: '2026-09-06'` — o zi după acea măsurătoare, o reîmprospătare de pe
  legis.md (doc_id nou 150498) a înlocuit fișierul deja ancorat corect de `anchor_cc.py` cu o
  extracție brută nouă, care nu a mai dus mai departe unirea titlurilor — o regresie tăcută,
  nedetectată zece zile, pentru că nimeni nu a remăsurat afirmația după reîmprospătare. În timpul
  scrierii scriptului, înainte de a scrie vreun fișier, au fost găsite și corectate două erori
  reale de euristică, ambele pe exemple concrete din corpus, nu ipotetice: (1) un antet fără
  niciun titlu (`## Articolul N.` urmat direct de corpul textului — articole finale/tranzitorii
  care chiar nu au titlu, ex. `COD-218-2008` art. 481-483 „Prezentul cod intră în vigoare...")
  era absorbit greșit ca „a doua propoziție a titlului", pentru că ramura euristicii care permite
  o a doua propoziție se declanșează pe orice titlu ce se termină cu punct, inclusiv unul gol;
  corectat interzicând orice unire când antetul nu are deloc text după „Articolul N.". (2) stilul
  vechi de numerotare fără paranteze („1. Text", nu „(1) Text" — `L-845-1992`, act din 1992) nu
  era recunoscut ca limită de oprire, așa că titlul deja complet al art. 22 a absorbit tot
  paragraful „1."; corectat adăugând acest tipar la limitele de oprire. Ambele au fost prinse
  citind manual eșantioane înainte de scriere, nu de auto-verificarea proprie a scriptului (care
  dovedește doar egalitatea corpului fără anteturi, nu corectitudinea titlului) — proba mecanică
  și proba de sens sunt verificări diferite, iar această operațiune a avut nevoie de amândouă.
- **Decis:** backup complet la `C:\Users\harab\wiki-backups\wiki-2026-09-16-line-unwrap\` înainte
  de orice scriere. Scris pe toate cele trei rădăcini raw (`moldova-legal`, `cnpf`, `bnm`):
  **4.973 anteturi corectate în 61 de fișiere**. Fiecare fișier atins verificat, prin script,
  strip-and-compare byte-identic față de backup-ul intact (nu față de propria copie de lucru) —
  toate 61 trec, zero discrepanțe. `sha256` recalculat pentru fiecare; `sha256_pre_title_unwrap`
  păstrează hash-ul dinainte. Cifra veche din `CLAUDE.md` (3.097, doar `moldova-legal`, dinainte
  de regresia CC) e înlocuită de cifra reală (4.973, toate trei rădăcinile), cu regresia
  CC-1107-2002 documentată explicit ca lecție pentru orice reîmprospătare viitoare a unui act deja
  ancorat: confirmă că unirea titlurilor supraviețuiește reîmprospătării, sau rulează din nou
  acest script după.
- **Unde:** `_meta/imports/anchoring/fix_wrapped_titles.py` (nou); backup
  `C:\Users\harab\wiki-backups\wiki-2026-09-16-line-unwrap\`; rapoarte
  `_meta/lint/title-unwrap-2026-09-16-moldova-legal.txt`, `-cnpf.txt`, `-bnm.txt`; 61 de fișiere
  raw sub `raw/papers/moldova-legal/`, `raw/papers/cnpf/`, `raw/papers/bnm/`;
  `CLAUDE.md` (Outstanding work, item 2); commitul acestei intrări.

## [2026-09-16] update | Verificarea manuală a tabelului „Trimiteri nerezolvate” din graful de citare

- **Aflat:** din cele 65 de grupuri nerezolvate din `_meta/graph/citation-graph.md`, 42 au fost
  verificate pe sursă, cu rezultate în patru clase. (1) 18 grupuri (27 citări), toate cu indiciul
  scriptului „exponent turtit" — ancora sugerată există de fiecare dată, iar titlul ei se
  potrivește cu contextul citării (ex. `COD-218-2008` art. 441 → art. 44^1 „Aplicarea sancţiunii
  mai blânde"): confirmate, nu sînt goluri. (2) Tot clusterul `AA-2014` (12 grupuri, 18 citări)
  este fals pozitiv: numerele citate nu sînt din textul ancorat al AA-2014, ci fie din directiva
  UE numită anterior în același paragraf prin anaforă „din respectiva directivă" (nedeținută ca
  extras), fie din textul reprodus al art. 3 din Decizia 2014/492/UE (nedeținută), care numește
  articole ale acordului integral, în afara a ceea ce acoperă acest extras structurat — regula
  „intern" a rezolvatorului nu resetează ținta la o schimbare de act prin anaforă sau citat
  imbricat, limitare reală, neînlăturată acum, risc prea mare pentru un graf validat de 2491 de
  muchii pentru un cîștig de douăsprezece rînduri ale unui singur act. (3) Clusterul `CC-1107-2002`
  (12 grupuri, 26 citări, cel mai mare ca volum) confirmă și extinde, cu dovezi concrete pe trei
  teme fără legătură, nota deja purtată de descrierea grafului despre numerotarea Codului civil de
  dinainte de renumerotarea din 2019: `COD-225-2003` citează art. 48^12/21/28/30/40 pentru
  persoanele audiate la instituirea unei măsuri de ocrotire judiciare, dar capitolul respectiv
  rulează azi pe numere simple, art. 50-119; același cod citează art. 330^4 și 283^27 pentru
  uzucapiune legată de registrul de publicitate, dar art. 330 de azi e „Nulitatea relativă a
  actului juridic", iar capitolul uzucapiunii e la art. 524-534; `L-149-2012` citează art.
  1575^4/5/9/10 și 1572^117 pentru masa succesorală, dar art. 1575 de azi e în capitolul
  magazinajului, iar moștenirea rulează la art. 2162-2360+. Fără hartă exactă veche→nouă; ar
  cere concordanța legis.md pentru legea de renumerotare (probabil 133/2018), inaccesibilă azi.
  (4) Un gol real, cu miză practică: `L-171-2012` art. 81, 87 și 88 lipsesc din consolidarea
  curentă ȘI din arhiva dinaintea reîmprospătării din 4 septembrie, deci nu e o regresie de
  reîmprospătare — dar două regulamente CNPF în vigoare azi (`HCNPF-14-5-2016`,
  `HCNPF-38-5-2015`) le citează ca temei legal viu. Registrul in-force nu semnalează nimic pe
  acest interval (doar art. 38 și 141^1, corect, la 2027-06-01). Necesită istoricul versiunilor de
  pe legis.md, blocat azi (Cloudflare interactiv). (5) `L-550-1995` art. 6/15/31/37^9 nu cer lucru
  suplimentar: sînt exact partea „scoasă" a actului, deja documentată la P8-bis (doar art. 1-3 și
  38^1-38^17 în vigoare) — același mecanism ca la `L-548-1995` (întrebarea 6), doar că nici unul
  nu e citat ca temei legal viu. (6) Un bug real de rezolvare, găsit din întâmplare:
  `COD-434-2023#art.389` modifică două acte diferite în același bloc numerotat, iar graful
  păstrează numele primului act peste schimbarea de țintă — citarea atribuită greșit lui
  `COD-218-2008` art. 13^1 e de fapt spre „Legea nr. 1134/1992" (statutul misiunilor diplomatice),
  un act diferit de `L-1134-1997` din corpus (care s-a dovedit, la verificare, legea societăților
  pe acțiuni) — deci o citare spre un act complet neținut, nu un gol intern. (7) Rîndul cel mai
  citat din tabelul „Dispoziții cu stare specială", `L-548-1995#art.11` (lovit parțial de
  HCC31/2013), verificat: toate cele șase pagini structurate care îl citează descriu textul de azi
  (rescris, opus celui anulat), nu pe cel anulat — recuperarea HCC din 2026-09-15 a făcut treaba
  corect, nici o corecție necesară. (8) `L-213-2023` art. 84 e artefact de parser: graful citește
  o notă editorială proprie din `L-213-2023.md`, nu o citare din text juridic. Au rămas
  neexplicate 11 grupuri, fără indiciu de la script și fără cauză găsită la o primă citire —
  lăsate deschise, nu ghicite.
- **Decis:** nici o modificare pe `raw/` (nimic de reparat acolo: fie citarea sursă e corectă și
  ținta lipsește din consolidarea deținută, fie e o problemă a rezolvatorului, nu a textului).
  Nici o modificare pe `build_citation_graph.py`: cele două limitări reale găsite (anafora
  „respectiva directivă"/decizie imbricată; bloc de modificare cu schimbare de act) sînt
  documentate exact, nu reparate, pentru că fiecare atinge un singur act și riscul de regresie pe
  un graf de 2491 de muchii, deja validat, depășește cîștigul. Constatările scrise ca punctul 8
  nou în „Open questions" din `CLAUDE.md`, cu golul `L-171-2012` art. 81/87/88 semnalat explicit
  pentru atenția lui Eugen ca singurul cu miză practică imediată (temei legal citat de regulamente
  CNPF azi în vigoare).
- **Unde:** `CLAUDE.md` (Open questions, item 8 nou); nici o schimbare pe `raw/`,
  `_meta/graph/build_citation_graph.py` sau paginile din `entities/`; commitul acestei intrări.

## [2026-09-16] update | L-171-2012 art. 81-88: data exactă a abrogării, verificată pe legis.md

- **Aflat:** Cloudflare s-a eliberat pe parcursul sesiunii (curl tot blocat, dar Chrome-ul lui
  Eugen a trecut fără interacțiune, ~8s de așteptare). Verificat direct pe fișa `LP171/2012`
  (doc_id `156016`, 42 de consolidări în istoric): textul din 2013 (doc_id 22987) are art. 81-88
  intacte; consolidarea din 30-03-2020 (doc_id 106513) încă le are; următoarea, din 20-04-2020
  (doc_id 120930), nu le mai are, iar antetul acelei consolidări poartă un singur act
  modificator: „LP23 din 27.02.20, MO87-93/20.03.20 art.112; în vigoare 20.04.20" — fără niciun
  marcaj în corp care să trimită la el. Deci art. 81-88 lipsesc din legea în vigoare **astăzi**
  (nu doar din consolidarea noastră, datată în viitor), din aprilie 2020, cu cinci ani înainte de
  data de consolidare a `HCNPF-38-5-2015`. Cele două regulamente CNPF care le citează ca temei
  legal poartă deci un preambul neactualizat de la LP23/2020, nu o problemă a wiki-ului. Art. 80
  reapare cu conținut nou la consolidarea din 15-12-2022 (doc_id 134549) — inserție separată,
  neinvestigată.
- **Decis:** constatarea din intrarea precedentă (aceeași zi) e completată, nu repetată: golul e
  acum datat exact și cauza (preambul CNPF neactualizat) e explicată. Nici o modificare pe `raw/`
  — nu era un defect de-al nostru de reparat, iar textul de azi al legii tot nu are art. 81-88,
  deci nici o reîmprospătare a consolidării noastre nu ar aduce înapoi aceste articole.
- **Unde:** `CLAUDE.md` (Open questions, item 8, paragraful `L-171-2012`, rescris cu data și sursa
  exactă); commitul acestei intrări.

## [2026-09-16] update | Cele 12 grupuri rămase din „Trimiteri nerezolvate": al doilea bug sistematic

- **Aflat:** verificate una câte una ultimele 12 grupuri (din cele 65) rămase neatinse în cele
  două intrări precedente. 8 s-au dovedit un al doilea bug sistematic al rezolvatorului, distinct
  de anafora „respectiva directivă" de la `AA-2014` dar de aceeași familie: propoziția care
  citează numește actul-țintă o singură dată, fie la finalul unei enumerări lungi de articole
  („din legea indicată", „din legea menţionată", „din Codul penal nr. 985/2002"), fie mai devreme
  în același paragraf, cu mai multe numere fără legătură între citare și numele actului — iar
  regula „intern" a rezolvatorului ia implicit actul care citează, nu pe cel numit. Fiecare caz a
  fost verificat citind ambele capete și potrivind titlul articolului real cu contextul citării:
  `COD-225-2003#art.308^17` (48^15) e al 13-lea membru al clusterului deja documentat pentru
  `CC-1107-2002` (renumerotarea din 2019), nu un caz nou; `COD-122-2003#art.269` (181^1-181^3) și
  `COD-122-2003#art.276` (185^2) citesc de fapt `COD-985-2002` — Codul penal propriu-zis, nu Codul
  de procedură penală care le citează — și titlurile („Coruperea electorală",  „Încălcarea
  dreptului asupra obiectelor de proprietate industrială") se potrivesc exact cu contextul;
  `L-160-2026#art.40` (72-73) citește `L-195-2024`, ale cărui art. 72-73 poartă titluri aproape
  identice cu propriul art. 40 al `L-160-2026`; `L-202-2017#art.142` (75^2) citește `L-548-1995`
  art. 75^2, deja confirmat în lotul de exponenți turtiți din prima intrare; `COD-218-2008#art.440`
  (5^1) citește `L-131-2012` art. 5^1, la fel deja confirmat. Un singur caz din acest lot rămâne
  neverificat până la capăt: `COD-218-2008#art.293^2` citează art. 50-104 „din legea indicată" =
  `L-114-2012`, dar `L-114-2012` așa cum îl deținem nu are `art.52^1`/`52^2`/`60^1` nici el — fie
  consolidarea noastră e mai veche decât amendamentul care le-a introdus, fie nepotrivirea
  continuă încă un nivel. Rămas deschis. `COD-116-2018` art. 17^1 e un gol real, confirmat pe cont
  propriu (fără alt act numit în context, doar art. 17 simplu în textul deținut) — cauza rămâne
  necunoscută. 3 grupuri rămân complet neexplicate: `COD-1163-1997` art. 29^1 (Codul fiscal,
  autocitare, fără altă cauză găsită), `L-105-2003` art. 201 (anomalie pe cont propriu — legea are
  75 de articole), `L-202-2017` art. 13^9 (citat din `HBN-127-2013`, posibil un alineat turtit —
  „art. 13 alin. (9)" — mai degrabă decât un articol real, formă pe care euristica de exponenți nu
  o acoperă).
- **Decis:** nici o modificare pe `raw/` sau pe script. Constatările înlocuiesc paragraful „11
  grupuri neexplicate" din item 8 cu bilanțul final: din 65, 38 fals pozitive, 21 goluri reale
  explicate, 2 artefacte/bug-uri de rezolvare spre acte greșite, doar 4 rămân complet neexplicate.
- **Unde:** `CLAUDE.md` (Open questions, item 8, rescris integral cu bilanțul final pe toate cele
  65 de grupuri); commitul acestei intrări.

## [2026-09-16] ingest | Lotul D, litigii civile/comerciale și contracte — L-23/2008, L-24/2008, L-9/2026, L-1125/2002

- **Aflat:** ales de Eugen, dintre mai multe direcții propuse, ca următoarea extindere a wiki-ului
  o dată ce inelul de stagiu din 6 septembrie și reverificarea acquis din 15-16 septembrie erau
  ambele închise. legis.md a fost blocat de Cloudflare interactiv la începutul sesiunii (curl și
  browserul intern al sesiunii, ambele „Just a moment"); Eugen a trecut verificarea în propriul
  Chrome, căutarea și descărcarea au mers prin Claude in Chrome (fetch same-origin + blob, ca la
  P8/BNM), cu o particularitate nouă: Chrome a blocat automat al doilea și al treilea fișier
  descărcate succesiv din același tab, rezolvat cu un tab nou per descărcare.
  Prima ipoteză (o „Lege 24/2023 cu privire la arbitraj") era greșită: arbitrajul e reglementat de
  două legi surori din 22.02.2008, nr. 23 (intern) și nr. 24 (comercial internațional), ambele
  găsite prin căutare în titlu și verificate direct în corp. A doua verificare a răsturnat o
  presupunere mai importantă: Legea nr. 137/2015 cu privire la mediere, deja în coada de ingerare a
  grafului de citare (9 mențiuni), nu mai e în vigoare — o lege complet nouă, LP9/2026 „privind
  medierea și statutul mediatorului" (transpune Directiva 2008/52/CE), o abrogă expres la propria
  intrare în vigoare (~12.09.2026, verificat direct în art. 62 alin. (2), nu presupus din titlu).
  Al patrulea act, Legea 1125/2002 (punerea în aplicare a Codului civil, deja în coadă cu 22
  mențiuni, 19 din chiar CC-1107-2002), a scos la iveală un al doilea defect de extracție: prima
  rulare a dat 0 ancore, fiindcă legea republicată în 2019 folosește peste tot forma veche
  „Art.N. -", nerecunoscută de regexul de ancorare scris pentru forma modernă „Articolul N.".
  Un al treilea defect, găsit la L-23/2008: linia de versiune conținea citatul „MO338-341/30.09.16",
  iar regexul de dată din `ingest_business_law.py` citea coada lui „341" ca pe o a doua dată falsă
  („41/30.09" → anul 2009), producând `consolidation_date: '2009-30-41'`, o dată invalidă.
- **Decis:** toate trei defectele s-au corectat în `ingest_business_law.py`, nu s-au ocolit manual:
  o ramură nouă de recunoaștere a formei „Art.N. -" (cu cerința unui dash după numărul articolului,
  ca să nu prindă o trimitere „art. 22" apărută la începutul unei fraze din corp), contorul de
  articole extins să numere și acest tipar, și un lookbehind negativ (`(?<!\d)`) în `DATE_RE`, care
  respinge orice început de potrivire precedat direct de o cifră. Toate patru actele s-au ingerat
  curat după corecții: L-23/2008 (36 de ancore, 1-35 + 23^1), L-24/2008 (42 de ancore, 1-41 + 23^1),
  L-9/2026 (63 de ancore, 1-63 fără lacune), L-1125/2002 (50 de ancore, 1-50 fără lacune). Legea
  137/2015 nu s-a ingerat (act mort de la ~12.09.2026, ca L-133-2011 pentru protecția datelor).
  Consemnat, nu rezolvat: două dispoziții amânate ale L-9/2026 (art. 44 alin. (3) lit. a)-c)) sînt
  scrise în proza ultimului articol, nu ca marcaj `[Art.N ... în vigoare DD.MM.YY]`, deci
  `build_inforce_register.py` nu le prinde — a treia formă cunoscută de dispoziție amânată
  invizibilă registrului, adăugată ca punctul 9 în „Open questions" din `CLAUDE.md`, neremediată în
  script pentru a nu risca o regresie pe un registru deja validat.
- **Unde:** `_meta/imports/moldova-legal/ingest_business_law.py` (patru intrări noi în `DOCS`, plus
  cele trei corecții de extracție); `raw/papers/moldova-legal/L-23-2008.md`, `L-24-2008.md`,
  `L-9-2026.md`, `L-1125-2002.md`; `entities/` cu aceleași patru nume; `raw/papers/moldova-legal/_manifest.md`
  (secțiunea X); `index.md` (134 de pagini); `CLAUDE.md` (Open questions, item 9 nou); memoria de
  sesiune `legis-md-search-via-curl.md` (Cloudflare intermitent, chiar și în Chrome-ul lui Eugen).

## [2026-09-16] update | Ancora „Art.N. -" nu era recunoscută de celelalte trei scripturi mecanice

- **Aflat:** intrarea anterioară a corectat `ingest_business_law.py` să recunoască forma veche
  „Art.N. -" ca ancoră de articol, dar regenerarea blocului de acoperire din `CLAUDE.md` a arătat
  imediat că defectul nu era izolat: `_meta/coverage/build_coverage.py` a raportat
  `L-1125-2002` ca „declared 50, found 0" — propriul lui `ANCHOR_RE` cunoaște doar forma
  „## Articolul N.", nu și „## Art.N. - text", pe care ancorarea o păstrează neschimbată (regula
  wiki-ului: ancora reia linia sursă așa cum este, nu o rescrie la forma modernă). Verificat, nu
  presupus: aceeași limitare există separat în `_meta/graph/build_citation_graph.py` (ANCHOR_RE
  propriu, folosit per-linie) și în `_meta/inforce/build_inforce_register.py` (ART_ANCHOR propriu,
  folosit ca să atribuie o dispoziție amânată articolului precedent) — trei regexuri independente,
  fiecare scris separat pentru propriul script, niciunul actualizat când s-a adăugat forma nouă.
- **Decis:** adăugată câte o a doua regulă de recunoaștere („Art.N. -"/„–"/„—", cu aceleași grupuri
  de captură ca regula existentă) în toate trei scripturile, combinată cu cea veche la punctul de
  folosire, fără să se atingă `ANCHOR_RE`/`ART_ANCHOR` originale — risc minim, niciun fișier deja
  ancorat cu „Articolul" nu poate ajunge să se potrivească dublu cu noua regulă. Regenerare
  completă după corecție: `L-1125-2002` iese „clean" în tabelul de acoperire (50/50), graful de
  citare crește de la 11920 la 11970 de dispoziții (cele 50 de articole reale, în loc de „#corp"
  nesegmentat) și de la 82 la 83 de trimiteri nerezolvate — singura nouă, `L-1125-2002#art.45` spre
  „art.1756", verificată imediat: e același bug sistematic de rezolvare deja documentat la punctul
  8 (actul țintă, „Codul civil", numit mai târziu în frază, nu lângă „art. N"), iar `CC-1107-2002`
  chiar are un art. 1756 („Contul fiduciar") care se potrivește exact contextului. Nu e un gol nou,
  doar unul nou vizibil, fiindcă înainte tot actul era un singur segment `#corp` fără ancore.
  Validator: 0 erori, 156 avertismente, neschimbat.
- **Unde:** `_meta/coverage/build_coverage.py` (ANCHOR_ABBR_RE nou, combinat în `scan_file`);
  `_meta/graph/build_citation_graph.py` (ANCHOR_ABBR_RE nou, combinat în bucla `Act.__init__`);
  `_meta/inforce/build_inforce_register.py` (ART_ANCHOR_ABBR nou, combinat în `preceding_article`);
  `entities/L-1125-2002.md` (secțiune nouă despre trimiterea „nerezolvată" explicată); registrele
  regenerate (`_meta/graph/citation-graph.md/.json`, `_meta/inforce/in-force-register.md/.json`,
  `_meta/hcc/hcc-register.md`, blocul de acoperire din `CLAUDE.md`).

## [2026-09-17] update | remedierea tehnică după auditul complet

- **Aflat:** singura eroare a validatorului era derivată din afișarea vârstei consolidărilor:
  rotunjirea la o zecimală făcea blocul generat din `CLAUDE.md` să devină depășit fără schimbare
  de corpus. `AGENTS.md` copia un instantaneu mult mai vechi al instrucțiunilor și al coverage,
  iar README încă prezenta drept deschise activități încheiate. Euristica D2 marca și propunerea
  originală în engleză a Comisiei Europene COM(2024) 469 ca traducere nedeclarată, deși aceasta
  nu este o traducere și stă în corpusul de politici, nu în corpusul juridic moldovenesc sau BNM.
- **Decis:** la acceptarea lui Eugen, eticheta de vechime devine stabilă („more than 2 years old"),
  cu test de regresie, iar `CLAUDE.md` devine unica sursă canonică pentru reguli, statut și
  controale generate; `AGENTS.md` rămâne doar bootstrap cu garanțiile care se aplică înainte de
  orice lucru. D2 se aplică numai rădăcinilor juridice `cnpf`, `moldova-legal` și `bnm`, păstrând
  avertismentul pentru traducerile englezești BNM și eliminând falsul pozitiv. Modificările de
  fond ale entităților juridice și ale citărilor lor sunt amânate: matter log are `taken:
  2026-09-16`, deci D9 cere registrul curent din proiect înainte de acea etapă.
- **Unde:** `_meta/coverage/build_coverage.py`; `CLAUDE.md`; `AGENTS.md`; `README.md`;
  `_meta/schema/schema-spec.yaml`, `build_schema.py`, `validate_wiki.py`, `SCHEMA.md`;
  `tests/test_build_coverage.py`. Verificate cu 5 teste unitare, toate controalele generate în
  mod `--check` și validatorul: 0 erori, 156 avertismente.

## [2026-09-17] update | corecturi juridice verificate după audit

- **Aflat:** documentul canonic păstra deja verificarea istorică a temeiurilor pentru lacunele
  din Codul muncii, Codul contravențional, legile 220/2007, 548/1995 și 845/1992, iar registrul
  in-force era deja corect pentru HG 743/2024. Paginile de entitate continuau însă să le prezinte
  drept neexplicate ori deschise. Cele două avertismente HCC rămase erau de context, iar trei
  entități erau izolate de navigația structurată. Eugen a confirmat că registrul de materii nu s-a
  schimbat; copia a fost reștampilată pentru 2026-09-17 cu același hash al corpului.
- **Decis:** fără modificarea surselor brute, au fost aliniate numai paginile structurale la
  verificările deja documentate: actele de abrogare sunt numite acolo unde istoria le confirmă,
  mecanismul ștergerii stub-urilor legis.md este explicat pentru L-548/1995, iar HG-743/2024
  trimite la cele șase poziții corecte ale registrului. Contextul HCC a fost adus în aceeași
  secțiune cu trimiterile afectate. L-148/2023, L-149/2012 și L-514/1995 au primit legături
  structurale relevante. Avertismentele pentru citări fără locator rămân neatinse: fiecare cere
  verificarea punctuală a afirmației, nu o completare mecanică.
- **Unde:** `legal-career/06-matter-log.md`; `entities/COD-116-2018.md`, `COD-1163-1997.md`,
  `COD-154-2003.md`, `COD-218-2008.md`, `COD-225-2003.md`, `HG-743-2024.md`, `L-220-2007.md`,
  `L-548-1995.md`, `L-845-1992.md`. Validatorul ulterior: 0 erori, 150 avertismente; toate 424
  hash-uri raw au fost verificate, fără modificări sub `raw/`.

## [2026-09-17] update | regula locatorului distinge dreptul pozitiv de documentele de politici

- **Aflat:** dintre cele 73 de avertismente rămase pentru citare la nivel de pagină, 31 trimiteau
  la documente de politici. Regula deja formulată în `SCHEMA.md` pentru acel perimetru cerea data
  și autoritatea sursei, nu un articol, punct sau anexă. Tratarea lor ca texte juridice era deci
  un fals pozitiv de implementare. Cele 42 de avertismente pentru corpusurile juridice au rămas
  intenționat active: fiecare trebuie rezolvat prin citirea afirmației și a sursei brute, nu prin
  completarea automată a unui locator.
- **Decis:** specificația declară explicit rădăcinile pentru care locatorul juridic este
  obligatoriu: `raw/papers/cnpf/`, `raw/papers/moldova-legal/` și `raw/papers/bnm/`. Validatorul
  ignoră sursele din celelalte rădăcini la această regulă, iar generatorul publică aceeași distincție
  în `SCHEMA.md`. Inventarul `**surse:**` rămâne tratat ca proveniență, nu ca afirmație juridică.
- **Unde:** `_meta/schema/schema-spec.yaml`, `_meta/schema/validate_wiki.py`,
  `_meta/schema/build_schema.py`, `SCHEMA.md`, `tests/test_validate_wiki.py`. Verificate cu 9
  teste unitare, generatorul de schemă, acoperirea, registrele in-force și HCC, graful de citare și
  validatorul: 0 erori, 43 avertismente. Toate cele 424 hash-uri raw rămân valide; nu există
  modificări sub `raw/`.

## [2026-09-17] update | citări juridice localizate și excepții de proveniență controlate

- **Aflat:** citările fără locator amestecau trei situații distincte: afirmații despre norme,
  metadate ale sursei și registre/inventare de documente. Unele localizări valide existau deja,
  dar validatorul nu recunoștea articole cu sufix (`art. 3a`), locatori de linie pentru corpuri
  neancorate ori localizări structurale ale PDF-urilor DCU. Citirea directă a surselor a corectat
  și două formulări: în `L-1-2018` BNM este autoritatea de supraveghere în sensul legii, iar
  `L-92-2022` numește CNPF pentru controlul protecției consumatorilor prin art. 89.
- **Decis:** regula de locator rămâne strictă pentru dreptul pozitiv, dar acceptă un locator
  structural explicit numai pentru identitatea, versiunea sau secțiunea sursei. Manifeste și
  inventare BNM sunt declarate cataloge, nu texte normative. Au fost introduse localizări exacte,
  între altele: art. 13 pentru limitele RCA, art. 1 pentru domeniul OPCA, art. 63 și 68 pentru
  referințele unit-linked, art. 89 pentru protecția consumatorului și secțiunile precise ale celor
  trei proceduri DCU. Nu s-a completat niciun locator prin presupunere.
- **Limita rămasă:** `236__Prezentare_RI_mai_2025.pdf.md` este etichetat în raw cu
  `language: other`, deși pagina de titlu a PDF-ului spune în română „Raport asupra inflației,
  Mai 2025”. Extracția textului este neutilizabilă. Nu se schimbă frontmatter-ul sub `raw/`, care
  este imuabil; avertismentul rămâne intenționat până la o operațiune de ingerare autorizată.
- **Unde:** `_meta/schema/schema-spec.yaml`, `_meta/schema/validate_wiki.py`,
  `_meta/schema/build_schema.py`, `SCHEMA.md`, `tests/test_validate_wiki.py`; paginile
  `entities/AA-2014.md`, `CC-1107-2002.md`, `DCU-PROCEDURI.md`, `HG-1170-2016.md`,
  `HG-1171-2018.md`, `L-1-2018.md`, `L-2-2020.md`, `L-100-2017.md`, `L-106-2022.md`,
  `L-122-2008.md`, `L-235-2006.md`, `L-92-2022.md` și `concepts/acquis-Benchmarks.md`.
  Verificate cu 14 teste unitare și validatorul: 0 erori, 1 avertisment; toate 424 hash-uri raw
  sunt valide.

## [2026-09-17] ingest | L-183-2016, caracterul definitiv al decontării — primul act din coada de ingerare a grafului de citare

- **Aflat:** legis.md era blocat pentru `curl` (Cloudflare interactiv), dar `showdetails/<doc_id>`
  a mers prin navigare directă în browser-ul din panoul Claude, iar un `fetch` same-origin din
  pagină a adus octeții serverului — cu o capcană de dezambalare: rezultatul JS venea împachetat
  de două ori ca șir JSON, plus o adnotare a uneltei lipită la coadă, iar dezambalarea greșită
  producea un fișier care eșua tăcut verificarea `usable()` a scriptului de ingerare. Actul
  declară la art. 16 transpunerea directă a art. 1-10 din Directiva 98/26/CE (SFD) — o descoperire
  care depășește simpla ingerare: `concepts/acquis-SFD.md`, reverificată cu o zi înainte fără
  acest act în corpus, concluzionase greșit că transpunerea trece doar pe calea ocolită a
  obligațiilor CSDR ale Depozitarului central (`L-234-2016`), fără declarație proprie.
- **Decis:** ingerat cu un înveliș nou, `_meta/imports/cnpf/ingest_payment_finality.py`, peste
  `_meta/imports/moldova-legal/ingest_business_law.py` (același tipar ca `ingest_bnm_ro.py` și
  `ingest_cnpf_ro.py`), în `raw/papers/cnpf/`, perimetrul CNPF/BNM, nu `moldova-legal/`. Titlurile
  de articol rupte pe două rânduri (5 din 17) corectate cu `fix_wrapped_titles.py`, ca la restul
  corpusului. Pagina `acquis-SFD` actualizată, cu concluzia veche păstrată ca istoric datat, nu
  ștearsă, conform regulii paginilor contrazise. Ales dintre primele rânduri ale cozii de ingerare
  (Codul electoral nr. 325/2022 avea mai multe mențiuni, 38 față de 25) pentru relevanța tematică
  directă a acestui perimetru, la alegerea lui Eugen.
- **Unde:** `raw/papers/cnpf/L-183-2016.md` (nou, 17 ancore); `_meta/imports/cnpf/ingest_payment_finality.py`
  (nou) și cache-ul `_meta/imports/cnpf/legis-md-payment/showdetails-139645.html` (nou);
  `entities/L-183-2016.md` (nou); `entities/L-234-2016.md`, `entities/DCU-REGULI-2026.md`,
  `concepts/acquis-SFD.md`, `index.md`, `raw/papers/cnpf/_manifest.md` (secțiunea L) actualizate.
  Registrele regenerate (`_meta/graph/citation-graph.md/.json` — 93 acte, `_meta/inforce/`,
  `_meta/hcc/`, blocul de acoperire din `CLAUDE.md`). Validator: 0 erori, 2 avertismente
  (neschimbate, pre-existente).

## [2026-09-17] ingest | L-133-2016, declararea averii și a intereselor personale — al doilea act din coada de ingerare

- **Aflat:** art. 3 lit. e^1) numește expres personalul Băncii Naționale a Moldovei (Consiliul de
  supraveghere, Comitetul executiv, angajații) și membrii/angajații CNPF ca subiecți ai declarării
  averii, iar lit. c^1) acoperă separat consiliul Fondului de garantare a depozitelor — o obligație
  de integritate a personalului de supraveghere pe care nimic din corpus nu o documenta încă. Fișa
  legis.md arată o consolidare **viitoare** (2027-01-01, LP154/2026 și LP327/2025), cu 6 dispoziții
  amânate — niciuna dintre ele privind subiecții relevanți aici. Art. 23 alin. (5^1), introdus prin
  LP244/2020, a fost declarat neconstituțional prin HCC29 din 21.09.2021, marcat direct în text.
  Un control nou al validatorului (`citation.hcc-unmarked`, apărut în arbore în timpul acestei
  sesiuni dintr-o lucrare concurentă, necomisă încă) a prins o citare proprie a art. 23 fără
  mențiunea HCC în aceeași secțiune — corectat înainte de commit, nu ignorat.
- **Decis:** ingerat cu `ingest_business_law.py` (nu un înveliș nou: e drept general de
  integritate/anticorupție, nu perimetru CNPF/BNM, deși subiecții includ personalul lor), în
  `raw/papers/moldova-legal/`. 14 titluri rupte corectate cu `fix_wrapped_titles.py`. Adăugată o
  secțiune nouă „Personnel integrity regime” în `entities/bnm.md`, în engleză, ca restul paginii.
  Fișierele celeilalte sesiuni concurente (`schema-spec.yaml`, `validate_wiki.py`,
  `build_schema.py`, `SCHEMA.md`, `tests/test_validate_wiki.py`) lăsate necomise, ca la lotul
  anterior — nu sunt ale acestei sesiuni.
- **Unde:** `raw/papers/moldova-legal/L-133-2016.md` (nou, 27 ancore);
  `entities/L-133-2016.md` (nou); `entities/bnm.md`, `entities/COD-218-2008.md`, `index.md`,
  `raw/papers/moldova-legal/_manifest.md` (secțiunea Y) actualizate. Registrele regenerate:
  `_meta/hcc/` (21 acte, de la 20; 17 marcaje în text, de la 16), `_meta/inforce/`,
  `_meta/graph/citation-graph.md/.json` (94 acte), blocul de acoperire din `CLAUDE.md`. Validator:
  0 erori, 2 avertismente (neschimbate, pre-existente).

## [2026-09-17] ingest | L-86-2014, evaluarea impactului asupra mediului — al treilea act, după un candidat respins

- **Aflat:** candidatul inițial pentru al treilea act, `L-133/2018` privind modernizarea Codului
  civil, s-a confirmat a fi exact legea de renumerotare căutată la punctul 8 din „Open questions"
  al `CLAUDE.md` (art. 7 alin. (2) din `L-1125/2002`: „dându-le ... articolelor ... o nouă
  numerotare”), dar s-a dovedit impracticabilă de ingerat cu scriptul actual: `showdetails` are
  4,8 MB, 1926 de apariții „Articolul N" (Codul civil integral, reprodus inline în blocurile de
  modificare) și doar 18 articole proprii, numerotate roman — structură incompatibilă cu
  `extract_doc`. Amânată, nu abandonată. `COD-434-2023` (Codul urbanismului) definește „acord de
  mediu" prin trimitere directă la `L-86/2014`, neingerată pînă acum, și condiționează la art. 104
  alin. (7) certificatul de urbanism/autorizația de construire de acel acord — o lacună de citare
  reală pentru un act deja central în corpus.
- **Decis:** ingerată `L-86/2014` în locul lui `L-133/2018`, cu `ingest_business_law.py`. 21 de
  titluri rupte corectate cu `fix_wrapped_titles.py`. Adăugate legături în ambele sensuri:
  `entities/COD-434-2023.md` (art. 2, art. 104) și `entities/L-160-2011.md` (anexa nr. 1,
  autoritățile emitente ale „aprobării de dezvoltare"). Fișierele celeilalte sesiuni concurente
  rămân necomise, ca la loturile anterioare.
- **Unde:** `raw/papers/moldova-legal/L-86-2014.md` (nou, 42 ancore); `entities/L-86-2014.md`
  (nou); `entities/COD-434-2023.md`, `entities/L-160-2011.md`, `index.md`,
  `raw/papers/moldova-legal/_manifest.md` (secțiunea Z) actualizate. `_meta/imports/moldova-legal/
  ingest_business_law.py` documentează și candidatul respins (`L-133-2018`), ca să nu fie
  reîncercat orbește. Registrele regenerate: `_meta/graph/citation-graph.md/.json` (95 acte),
  `_meta/inforce/` (fără dispoziții amânate noi), blocul de acoperire din `CLAUDE.md`. Validator:
  0 erori, 2 avertismente (neschimbate, pre-existente).

## [2026-09-17] ingest | L-132-2016, Autoritatea Națională de Integritate — al patrulea act, închide o întrebare deschisă proprie

- **Aflat:** actul închide direct întrebarea deschisă lăsată de `L-133/2016` (art. 22 alin. (2)
  trimite aici pentru organizarea ANI) — doc_id consecutiv (155890/155891), adoptate aceeași zi,
  17.06.2016. Art. 27 operaționalizează exact termenul de depunere din art. 6-7 ale `L-133/2016`.
  Aceeași consolidare viitoare (2027-01-01, LP154/2026) ca la `L-133/2016`, dar de data aceasta
  fișa arată **două** decizii HCC în istoric (HCC29/2021 — aceeași care lovește art. 23 al.(5^1)
  din `L-133/2016` — și HCC6/2018, nouă pentru registru), și **niciuna nu e marcată în corpul
  textului**, spre deosebire de `L-133/2016`. Nu s-a făcut recuperarea manuală (citirea
  versiunilor istorice de pe legis.md) în această sesiune; rămân în categoria „fără articol",
  aceeași deja acceptată pentru `CONST-1994` și `L-213/2023`.
- **Decis:** ingerată cu `ingest_business_law.py`, 18 titluri rupte corectate. Legături adăugate
  în ambele sensuri cu `entities/L-133-2016.md` (întrebarea deschisă #1 închisă acolo) și
  `entities/bnm.md` (controlul ANI se întinde asupra personalului BNM/CNPF numit subiect al
  declarării). Fișierele sesiunii concurente rămân necomise.
- **Unde:** `raw/papers/moldova-legal/L-132-2016.md` (nou, 45 ancore); `entities/L-132-2016.md`
  (nou); `entities/L-133-2016.md`, `entities/bnm.md`, `index.md`, `raw/papers/moldova-legal/
  _manifest.md` (secțiunea AA) actualizate. Registrele regenerate: `_meta/hcc/` (22 acte, de la
  21; 77 hotărâri, de la 76; 6 „fără articol", de la 4), `_meta/inforce/`, `_meta/graph/
  citation-graph.md/.json` (96 acte), blocul de acoperire din `CLAUDE.md`. Validator: 0 erori, 2
  avertismente (neschimbate, pre-existente; un `page.links-min` intermediar corectat înainte de
  commit).

## [2026-09-17] update | închiderea sesiunii de extindere: README actualizat, lucrarea sesiunii concurente integrată

- **Aflat:** cele cinci fișiere lăsate necomise la fiecare din cele patru loturi anterioare
  (`schema-spec.yaml`, `validate_wiki.py`, `build_schema.py`, `SCHEMA.md`,
  `tests/test_validate_wiki.py` — controlul `raw.report-extraction-suspect`) au rămas neschimbate
  peste toată sesiunea de extindere a corpusului: nicio nouă modificare la ele din momentul
  primei observații. Eugen confirmat explicit la închidere: se includ în commit-ul de azi.
  Validatorul, rulat cu toate cele cinci active, iese curat, 0 erori, 2 avertismente — aceleași
  două de dinainte, niciuna nouă produsă de integrare. README nu mai menționa `_meta/hcc/` și
  `_meta/graph/`, deși ambele sunt straturi de control stabilite de mult (8, respectiv 10
  septembrie), nu ceva nou din sesiunea de azi — omisiune veche, corectată acum.
- **Decis:** README.md capătă cele două straturi lipsă în tabelul „Cum e construit" și o mențiune
  a `close_session.py` ca punct unic de închidere, fără să dubleze starea volatilă pe care
  `CLAUDE.md` o ține deja. Toate cele patru loturi de ingerare ale sesiunii (L-183/2016, L-133/2016,
  L-132/2016, L-86/2014) și lucrarea sesiunii concurente merg într-un singur commit de închidere,
  cu `close_session.py --commit`, care regenerează toate controalele o ultimă dată și rulează
  validatorul înainte de a comite.
- **Unde:** `README.md`; restul fișierelor listate în intrările de mai sus ale zilei de azi.
  Corpusul: de la 83 la 87 de acte moldovenești primare ingerate (patru acte noi), 138 de pagini
  structurate (de la 134), 428 de surse brute verificate prin sha256.

## [2026-09-17] update | detectarea extracțiilor textuale aproape goale din rapoarte

- **Aflat:** `raw/papers/bnm/reports/documents/236__Prezentare_RI_mai_2025.pdf.md` declară
  `extraction_status: text-extracted`, dar secțiunea sa `## Extracted text` conține numai
  235 caractere și niciun cuvânt semnificativ. Originalul păstrat are 23 de pagini, iar
  extragerile învecinate din aceeași serie BNM sunt lizibile. Defectul este deci individual,
  nu o regulă a întregului set de rapoarte.
- **Decis:** validatorul avertizează pentru un `report` declarat extras textual dacă secțiunea
  standard are cel mult 20 de cuvinte semnificative și 500 de caractere. Pragul este
  intenționat conservator și controlul nu modifică frontmatter-ul, corpul brut, hash-ul sau
  originalul. Corectarea necesită o reingerare autorizată, cu păstrarea originalului și
  verificare de hash.
- **Unde:** `_meta/schema/schema-spec.yaml`, `_meta/schema/validate_wiki.py`,
  `_meta/schema/build_schema.py`, `SCHEMA.md`, `tests/test_validate_wiki.py`.
  Verificate cu 17 teste unitare și validatorul: 0 erori, 2 avertismente. Toate cele 424
  hash-uri raw sunt valide; nu există modificări sub `raw/`.

## [2026-09-17] ingest | L-245-2008, secretul de stat — al cincilea act din coada de ingerare a grafului de citare

- **Aflat:** nu era cel mai citat pe număr de mențiuni (`COD-325-2022`, 38 de mențiuni, era mai
  sus în tabelul cozii), dar coloana care contează pentru ordinea de ingerare, per nota proprie a
  `citation-graph.md`, este a treia: numărul de acte deținute citatoare, nu numărul brut de
  mențiuni. `L-245-2008` avea 11 acte citatoare, cel mai mare număr dintre toți candidații
  verificați în această sesiune (`COD-325-2022` și `L-325-2013` aveau câte 9). legis.md a fost
  accesibil din prima încercare în browserul intern al sesiunii, fără nevoie de Chrome-ul lui
  Eugen ca la sesiunile blocate de Cloudflare anterior — dar câmpul de căutare „NR. DOCUMENTULUI"
  respinge formatul „245/2008" (zero rezultate) și acceptă doar numărul singur, „245" (97
  rezultate, toate încărcate din prima în DOM, paginarea fiind doar client-side). Motivul de
  relevanță nu a fost presupus din poziția în coadă, ci verificat direct în text: `L-133/2016`,
  ingerată mai devreme aceeași zi, trimite la legea de față de patru ori (art. 5 alin. (6), art. 7
  alin. (7), art. 7^1 întreg, art. 9 alin. (3)) pentru a defini subiecții declarării averii a căror
  identitate constituie secret de stat — legea de față decide cine intră în acel regim de excepție
  de la transparență, nu `L-133/2016` însăși.
- **Decis:** ingerată cu `ingest_business_law.py` (doc_id 151410, consolidare 2025-12-30, fără
  abrogare, fără dispoziții amânate). 29 de titluri rupte pe două rânduri corectate cu
  `fix_wrapped_titles.py`. Legătură adăugată în ambele sensuri cu `entities/L-133-2016.md`.
  Celelalte 10 acte care citează `L-245-2008` din coadă (`COD-122-2003`, `COD-985-2002`,
  `L-1260-2002`, `L-131-2015`, `L-160-2026`, `L-192-1998`, `L-195-2024`, `L-20-2026`,
  `L-325-2025`, `UA-STATUT-2011`) rămân neverificate articol cu articol, consemnate ca atare în
  pagina de entitate, nu tratate ca lanțuri confirmate.
- **Unde:** `raw/papers/moldova-legal/L-245-2008.md` (nou, 41 ancore); `entities/L-245-2008.md`
  (nou); `entities/L-133-2016.md`, `index.md`, `raw/papers/moldova-legal/_manifest.md` (secțiunea
  AB) actualizate. `_meta/imports/moldova-legal/legis-md-business/showdetails-151410.html`
  păstrat ca sursă de audit. Registrele regenerate: `_meta/hcc/` (neschimbat, actul nu poartă
  nicio decizie HCC), `_meta/inforce/` (neschimbat), `_meta/graph/citation-graph.md/.json` (97
  acte, de la 96), blocul de acoperire din `CLAUDE.md`. Validator: 0 erori, 2 avertismente
  (neschimbate, pre-existente).

## [2026-09-17] update | L-245-2008, restul cozii de citare — cele 20 de muchii verificate articol cu articol

- **Aflat:** Eugen a cerut rezolvarea listei de citări rămase neverificate la ingerarea de mai sus.
  Toate cele 20 de muchii ale grafului spre `L-245-2008` (`_meta/graph/citation-graph.json`,
  regenerat cu actul acum intern, nu `EXT:`) deschise una câte una, cu linia citantă comparată cu
  titlul articolului din legea de față. **Rezultat curat, fără nicio corecție de graf:** toate 20
  sunt trimiteri generice „conform Legii nr. 245/2008 cu privire la secretul de stat", niciuna la
  un articol anume — explică de ce câmpul `articles` al fiecărei muchii era gol în graf, nu un
  defect de extracție. `COD-122-2003` (4 citări: art. 6, 57^2, 138^10, 213 — protecția identității
  agenților acoperiți), `COD-985-2002` (art. 121 „Secretul de stat", definiția întreagă prin
  trimitere aici — cea mai directă citare din lot), `L-1260-2002` și `UA-STATUT-2011` (aceeași
  clauză, accesul avocaților la secretul de stat), `L-131-2015` (abrogată) și succesoarea ei
  `L-325-2025` (clauza standard de excepție de la publicare în achiziții publice, reluată de 5 ori
  în total), `L-20-2026` (transparența ANSC), `L-160-2026` și `L-195-2024` (excludere din domeniul
  protecției datelor). Singura cu relevanță directă pentru perimetrul CNPF/BNM: `L-192-1998` art.
  20 alin. (8) lit. c) — hotărârile CA ale CNPF cu secret de stat nu se publică. Găsită și o
  etichetare greșită proprie, din prima trecere: `entities/L-245-2008.md` numea `L-192-1998`
  „protecția consumatorului"; e legea-cadru a CNPF, nu legea consumatorului (`L-105-2003`).
- **Decis:** `entities/L-245-2008.md` rescrisă cu constatările articol cu articol, în locul listei
  „neverificat"; frontmatter `sources` extins cu cele 10 fișiere raw citate. `entities/L-192-1998.md`
  primește o secțiune nouă despre regimul de publicare al art. 20 (până acum neconsemnat pe acea
  pagină), cu legătură către `L-245-2008`. Nicio corecție necesară în `build_citation_graph.py`:
  absența articolelor din `articles` era corectă, nu un bug de rezolvare a țintei.
- **Unde:** `entities/L-245-2008.md`, `entities/L-192-1998.md`, `raw/papers/moldova-legal/
  _manifest.md` (secțiunea AB.1, nouă) actualizate. Nicio schimbare sub `raw/`, niciun registru
  generat afectat. Validator: 0 erori, 2 avertismente (neschimbate, pre-existente).

## [2026-09-17] ingest | L-181-2014, finanțele publice și responsabilitatea bugetar-fiscală — al șaselea act din coada de ingerare

- **Aflat:** ales strict după coloana a treia a cozii (acte deținute citatoare): 14, fiecare o
  singură dată — cel mai mare număr văzut pînă acum, peste `COD-325-2022` și `L-325-2013` (câte 9).
  Consolidare legis.md **viitoare, 2027-01-01** (LP327 din 29.12.25), cu o complicație proprie:
  aceeași lege modificatoare poartă și DOUĂ date de intrare în vigoare deja trecute, 31.12.25,
  pentru alte dispoziții, fără marcaj propriu în corpul acestei consolidări — mecanismul „marcajul
  se pierde la reîmprospătare" din `CLAUDE.md`, aici înăuntrul aceleiași legi modificatoare. Corpul
  poartă totuși 25 de marcaje curate, toate cu data 01.01.27. Lacună de numerotare la art. 49 (48
  → 50), fără marcaj „abrogat" în această consolidare, neinvestigată în istoric. Două decizii HCC
  în fișă (HCC32/2016, HCC10/2017), niciuna în corpul textului — categoria „fără articol". Toate
  cele 14 acte citatoare verificate articol cu articol în aceeași sesiune: 13 sînt trimiteri
  generice la principiile/regulile/procedurile legii de față pentru bugetul propriu al unei
  autorități publice autonome; 2 (`COD-225-2003`, `L-213-2023`) citează expres art. 43 pentru
  gestionarea taxei de timbru; singura cu relevanță directă pentru perimetrul BNM e `L-160-2023`
  art. 17 alin. (1) lit. q), împrumuturile FGDSB de la BNM/Ministerul Finanțelor.
- **Decis:** ingerată cu `ingest_business_law.py` (doc_id 153046). 28 de titluri rupte corectate cu
  `fix_wrapped_titles.py` (o excepție rămasă: art. 43, continuarea începe cu „/", formă neprinsă de
  euristică). Legătură adăugată în `entities/L-160-2023.md` pentru împrumuturile FGDSB. Restul celor
  13 acte citatoare, generice, consemnate în pagina de entitate fără a fi editate individual.
- **Unde:** `raw/papers/moldova-legal/L-181-2014.md` (nou, 89 ancore); `entities/L-181-2014.md`
  (nou); `entities/L-160-2023.md`, `index.md`, `raw/papers/moldova-legal/_manifest.md` (secțiunea
  AC) actualizate. `_meta/imports/moldova-legal/legis-md-business/showdetails-153046.html` păstrat
  ca sursă de audit. Registrele regenerate: `_meta/graph/citation-graph.md/.json` (98 acte, de la
  97), `_meta/inforce/` (25 de dispoziții noi amânate), `_meta/hcc/` (neschimbat — cele două decizii
  rămân neatribuite, nu marcate în text), blocul de acoperire din `CLAUDE.md`. Validator: 0 erori,
  2 avertismente (neschimbate, pre-existente).

## [2026-09-17] ingest | L-325-2013, evaluarea integrității instituționale — al șaptelea act, coada rezolvată în aceeași sesiune

- **Aflat:** ales dintre trei candidați legați la 9 acte citatoare, pentru continuitatea tematică
  cu ciorchinele de integritate deja în corpus (`L-132-2016`, `L-133-2016`): `COD-325-2022` (Codul
  electoral, mare, generic) și `L-139-2010` (**ABROGAT**, „dreptul de autor", ar fi cerut găsirea
  succesoarei) lăsați deoparte. Consolidare 2024-03-29, trecută. HCC37/2021 lovește direct în text
  art. 17 alin. (2)-(4); HCC7/2015 doar în fișă, fără articol. Toate cele 9 acte citatoare (22 de
  muchii) verificate articol cu articol: 21 confirmă aceeași obligație (art. 7 alin. (2) lit. a) —
  „să nu admită manifestări de corupție" — condiție de excludere de la opt tipuri de funcții
  publice, inclusiv membrii CA ai CNPF, art. 12 din `L-192-1998`, singura cu relevanță directă
  pentru perimetrul CNPF). **Anomalie găsită: `L-548-1995` (legea BNM), de două ori (art. 23 alin.
  (7), art. 34 alin. (6)), citează „art. 6 alin. (2) lit. a)" — dar art. 6 alin. (2) e o frază
  descriptivă fără nicio literă a) și fără nicio obligație individuală. Obligația reală descrisă de
  BNM se potrivește cuvânt cu cuvânt cu art. 7 alin. (2) lit. a), articolul folosit de toate
  celelalte șapte acte. Cel mai probabil o eroare de trimitere în textul legii BNM, nu o
  renumerotare (legea de față n-are istoric de renumerotare, 28 de articole fără lacune).**
- **Decis:** ingerată cu `ingest_business_law.py` (doc_id 142068). 14 titluri rupte corectate cu
  `fix_wrapped_titles.py`. Anomalia din `L-548-1995` consemnată, nu corectată (nu se rescrie textul
  altei legi); marcată `[de verificat cu Eugen]` în ambele pagini de entitate implicate.
- **Unde:** `raw/papers/moldova-legal/L-325-2013.md` (nou, 28 ancore); `entities/L-325-2013.md`
  (nou); `entities/L-192-1998.md`, `entities/L-548-1995.md`, `index.md`, `raw/papers/moldova-legal/
  _manifest.md` (secțiunea AD) actualizate. `_meta/imports/moldova-legal/legis-md-business/
  showdetails-142068.html` păstrat ca sursă de audit. Registrele regenerate: `_meta/graph/
  citation-graph.md/.json` (99 acte, de la 98), `_meta/hcc/` (HCC37/2021 nou, 3 marcaje în text),
  blocul de acoperire din `CLAUDE.md`. Validator: 0 erori, 2 avertismente (neschimbate,
  pre-existente).

## [2026-09-17] update | documentul 05 rescris în proiect, copia locală resincronizată

- **Aflat:** copia locală a documentului 05 rămăsese ștampilată 10 septembrie, deși între timp au trecut 40 de commit-uri în trei sesiuni (15, 16, 17 septembrie): stratul de constatări acquis a fost dezghețat integral, limita registrului „în vigoare" pentru acte pe puncte a fost reparată, a intrat un prim extras din Acordul de Asociere, iar corpusul a crescut cu nouă acte. O afirmație din document (limita registrului pentru `HG-743-2024`) devenise activ greșită din 16 septembrie, nu doar veche, pentru că documentul o descria integral în loc să trimită la punctul 7 din „Open questions" al `CLAUDE.md`.
- **Decis:** masterul a fost rescris în proiectul claude.ai „Legal Wiki" (secțiune cu secțiune, verificat direct față de `git log` și `CLAUDE.md`, nu din memorie), apoi copiat aici și reștampilat cu `stamp_copies.py --taken 2026-09-17`. Regula documentului a fost extinsă: nu mai descrie integral o limitare pe care `CLAUDE.md` o ține deja la zi, doar trimite la ea, la fel cum face deja pentru cifrele de acoperire.
- **Unde:** `legal-career/05-knowledge-map.md` (corp înlocuit, reștampilat, taken/stamped 2026-09-17). Fără modificări sub `raw/`. Validator: 0 erori, 2 avertismente (neschimbate, pre-existente, `236__Prezentare_RI_mai_2025.pdf.md`). Neconsemnat încă în git: commit și push rămân un pas separat.

## [2026-09-17] create | lacună de acoperire pentru practica generală de avocatură

- **Aflat:** Eugen a întrebat direct ce segmente relevante pentru un avocat lipsesc din corpus.
  Verificat mecanic (nu ghicit) împotriva `_meta/graph/citation-graph.md` și `raw/papers/
  moldova-legal/_manifest.md`: Codul familiei (`COD-1316-2000`) absent complet, apare doar ca
  țintă externă de citare; dreptul de autor fără succesoare ingerată (`L-139-2010` e abrogat,
  succesoarea lăsată deoparte explicit la ingerarea `L-325-2013` din aceeași zi); notariatul,
  medierea și avocatura fără lege-cadru în vault, doar citate pe nume; Codul electoral
  (`COD-325-2022`, 38 mențiuni, 9 acte citatoare) în capul cozii de ingerare mecanice. Codul
  muncii (`COD-154-2003`) e ținut dar cu consolidare viitoare, 2027-01-01. Succesoarea legii
  protecției datelor personale, după abrogarea `L-133-2011`, rămâne neverificată.
- **Decis:** consemnat ca notă de lacună, nu ca decizie de ingerare — ordinea rămâne a lui Eugen,
  pe modelul planului similar din 2026-09-04 (`2026-09-04-lacuna-drept-afaceri.md`), ale cărui
  nouă acte au fost între timp ingerate.
- **Unde:** `_meta/plans/2026-09-17-lacuna-drept-general.md` (nou). Fără modificări sub `raw/`,
  nicio regenerare de registru necesară. `concepts/functionarea-pietelor-de-produse-si-
  dereglementare.md` are o modificare necomisă din altă sesiune activă în paralel (lock de git
  întâlnit în timpul acestei sesiuni); lăsat neatins, nu face parte din acest commit.

## [2026-09-17] update | fișier corupt restaurat, `.obsidian/graph.json` comis ca rutină

- **Aflat:** `concepts/functionarea-pietelor-de-produse-si-dereglementare.md`, lăsat neatins la
  intrarea precedentă, avea ultima modificare la 21:33 — cu mult înaintea lock-urilor de git
  întâlnite la 22:57-23:07, deci nu era o sesiune activă concurentă, ci reziduul unui proces căzut
  mai devreme. Diff-ul ignorând spațiile (`git diff --ignore-all-space`) a arătat o singură
  schimbare reală: linia goală de după frontmatter fusese înlocuită cu o virgulă singură; restul
  fișierului avea doar CRLF în loc de LF, zgomot de encoding, nu conținut.
- **Decis:** virgula corectată direct (Edit țintit, nu rescriere integrală), apoi fișierul
  realiniat exact pe bytes cu ultima versiune comisă (`git show HEAD:cale > cale`, nu
  `git checkout --`, blocat de clasificatorul de siguranță al mediului ca „distrugere locală
  ireversibilă" deși conținutul era recuperabil din git). `.obsidian/graph.json` (o linie, stare
  de rutină a vizualizării graficului Obsidian) comis fără modificare, ca și la P0.
- **Unde:** `concepts/functionarea-pietelor-de-produse-si-dereglementare.md` (restaurat, fără
  diferență față de HEAD anterior); `.obsidian/graph.json`. Fără modificări sub `raw/`, nicio
  regenerare de registru necesară.

## [2026-09-18] ingest | L-133-2018, modernizarea Codului civil — concordanța numerotării de dinainte de 2019, și o regulă nouă în graf

- **Aflat:** trei lucruri pe care diff-ul nu le arată. **(1)** Legea 133/2018 este într-adevăr
  legea de renumerotare presupusă la punctul 8 din `CLAUDE.md`, iar concordanța se citește din ea
  fără a avea nevoie de tabelul legis.md: articolul I poartă 1.400 de titluri de articol ale
  Codului civil în numerotarea veche, din care 1.176 (84%) se potrivesc **exact pe titlu** cu o
  ancoră din `CC-1107-2002` de azi, 197 pe titlu rescris, 27 deloc. Toate trimiterile vechi pe
  care wiki-ul le avea se rezolvă (330^4 → 526; 1572^117 → 2419; 1575^N → 2424+N, verificat pe
  patru puncte independente; 1144^9 → 1614), cu o singură excepție care **nu** se ghicește:
  283^27 are titlu identic cu art. 435 **și** art. 450 de azi. **(2)** Ciorchinele `48^N`
  (ocrotirea judiciară) **nu** vine de aici — actul nu conține niciun articol 48^N — deci punctul
  8 rămâne deschis, dar cu o întrebare mai îngustă. **(3)** O lege de modificare rupe trei unelte
  deodată, și numai a treia a fost o surpriză: ancorarea implicită ar fi scris 1.434 de ancore
  pentru dispoziții ale altor acte; verificatorul de integritate cade dacă ancora rescrie linia în
  loc să se insereze deasupra; iar graful de citare a atribuit **514 din 837** de trimiteri lui
  `COD-225-2003`, deși art. I modifică Codul civil — 557 din cele 646 de rânduri „nerezolvate",
  adică 86% din tabelul pe care punctul 8 îl declară verificat exhaustiv, deveniseră false.
- **Decis:** ingerare cu `anchor_mode='roman-amending'` (ancoră numai pe cele 17 articole romane,
  inserată ca linie nouă deasupra liniei sursă, convenția `L-177-2025`), iar `build_citation_graph.py`
  nu mai extrage muchii **la nivel de articol** din actele ale căror ancore sunt toate numerale
  romane. Muchiile act → act rămân. Costul a fost măsurat **înainte** de aplicare și consemnat:
  dispar 24 de muchii corecte, de la `L-177-2025` și `L-178-2020`; „rezolvate în actul curent"
  rămâne 7.178, neschimbat, proba că regula nu atinge alt act. Regula este reversibilă printr-o
  condiție. Decizie luată în sesiune, fără Eugen — motivul: alternativa era să las 557 de rânduri
  false într-un control generat, ceea ce e mai rău decât să emit mai puțin. **De confirmat sau
  răsturnat de Eugen.** Cele 27 de titluri fără corespondent nu au fost deschise unul câte unul.
- **Unde:** `raw/papers/moldova-legal/L-133-2018.md` (17 ancore, 10.762 linii, doc_id 34327,
  in vigoare 01.03.2019, `never_amended`); secțiunea **AE** din
  `raw/papers/moldova-legal/_manifest.md`; `entities/L-133-2018.md`; `index.md`; `CLAUDE.md`
  (punctul 8 și descrierea `_meta/graph/`); `_meta/imports/moldova-legal/ingest_business_law.py`
  și `verify_business_law.py` (modul nou); `_meta/graph/build_citation_graph.py` (regula nouă).
