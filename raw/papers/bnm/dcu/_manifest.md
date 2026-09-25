# DCU — Procedurile Depozitarului central unic (dcu.md) — manifest

Creat 2026-09-09, la cererea lui Eugen, ca ultimul strat al lanțului speței moștenitorului unui
acționar de bancă (8 septembrie 2026): Legea 202/2017 → Regulamentele BNM 127/2013 și 130/2013 →
Regulile DCU → Procedurile DCU. Regulile stau în `raw/papers/bnm/legal-ro/` fiindcă le aprobă final
BNM; Procedurile stau aici, în folder propriu, fiindcă le aprobă Comitetul executiv al DCU (art. 4
alin. (2) din Regulile DCU) și nu sunt acte ale BNM. Nu sunt pe legis.md și nu apar în Monitorul
Oficial; sursa este pagina `https://www.dcu.md/ro/reglementari/procedurile-dcu`, unde stau ca PDF,
câte unul pe procedură, cu cele două proceduri abrogate listate separat și neingerate.

## Sursa și metoda

- Descărcare: `curl` din Bash, direct de pe dcu.md (fără Cloudflare), 2026-09-09, cu acordul explicit
  al lui Eugen pentru întregul lot; originalele, cu hash, în `_meta/imports/bnm/dcu/proceduri/`.
- Extracție: `_meta/imports/bnm/ingest_dcu_proceduri.py`, sora lui `ingest_dcu_rules.py`: PyMuPDF,
  pagină cu pagină, se elimină doar spațiile de capăt și liniile goale. **Fără ancore**: procedurile
  sunt numerotate pe puncte, în forme diferite (1., 1.1., a), liste cu buline), fără articole și fără
  capitole. O trimitere la „pct. N" nu este ancorată; se citează prin titlul secțiunii, verificând
  în fișier.
- Verificare: `--verify` re-extrage și compară linie cu linie, controlează hash-ul PDF-ului
  (`source_file_sha256`), al extracției (`sha256_extraction`) și al corpului (`sha256`), și cere
  zero ancore. Cele opt extracții PyMuPDF: PASS; a noua extracție derivată din PDF-ul oficial:
  hash PDF și corp verificate, fără ancore.
- Fișa fiecărui act (aprobare, intrare în vigoare, modificări) este în pagina de titlu a PDF-ului,
  reprodusă ca text în fiecare fișier; nu este transcrisă de mână în frontmatter.

## Actele

| Fișier | Procedura | Aprobare (din pagina de titlu) | Pagini | Linii | Integritate | Note |
|---|---|---|---:|---:|---|---|
| `DCU-PROC-DECONTARE.md` | Proceduri privind operațiunile de decontare (VMC: vânzare, donație, **succesiune**; VMS și CBN; BVM și BAS; conturi; extras) | HCE DCU nr. 21/2020, în vigoare 23.12.2020; modificată prin HCE 29/2020, 2/2022 și 10/2024 | 28 | 988 | **PASS derivat** | PDF local fără strat de text exploatabil; text integral extras de pe PDF-ul oficial prin web_extract; original arhivat, sha256 `5ff70696aeb09e0d798947dfb5fb5182adec34d180bba4487e6319ba9392f864`; fără ancore |
| `DCU-PROC-INREGISTRARE-VM.md` | Proceduri privind înregistrarea emitentului și valorilor mobiliare | HCE DCU nr. 11/2020, în vigoare 10.04.2020; modificată prin HCE 19/2020 (aplicare 01.07.2020), 27/2020, 4/2023 | 13 | 709 | PASS | cuprinde lista acționarilor ca serviciu adițional |
| `DCU-PROC-PARTICIPANT.md` | Proceduri privind înregistrarea participantului DCU | HCE DCU nr. 22/2020, în vigoare 07.09.2020 | 2 | 72 | PASS | |
| `DCU-PROC-RECONCILIERE.md` | Proceduri de reconciliere | HCE DCU nr. 11/2020, modificată prin HCE 22/2023, în vigoare 14.06.2020 | 9 | 911 | PASS | text fragmentat de font |
| `DCU-PROC-INSOLVABILITATE.md` | Proceduri aplicate în cazul insolvabilității participantului | HCE DCU nr. 27/2021, în vigoare 25.10.2021 | 6 | 709 | PASS | text fragmentat de font |
| `DCU-PROC-DETINATOR.md` | Proceduri privind înregistrarea deținătorului de VM | HCE DCU nr. 23/2020, în vigoare 07.09.2020 | 2 | 58 | PASS | |
| `DCU-PROC-RECLAMATII.md` | Proceduri de soluționare a reclamațiilor (extras) | HCE DCU nr. 31/2018 | 4 | 100 | PASS | documentul se declară „extras" |
| `DCU-PROC-GARANTII.md` | Proceduri privind constituirea garanțiilor și apelurile în marjă | HCE DCU nr. 14/2021, în vigoare 05.07.2021 | 11 | 1034 | PASS | pagina de titlu poartă mențiunea **„DCU INTERN"**, deși e publicat pe pagina publică; text fragmentat de font |
| `DCU-PROC-COMISIOANE.md` | Proceduri privind modul de calcul și percepere a plăților și comisioanelor | HCE DCU nr. 23/2023, în vigoare 29.09.2023 | 28 | 1886 | PASS | text fragmentat de font |

Datele de aprobare din tabel sunt citite din pagina de titlu extrasă; acolo unde fontul a rupt
cifrele („14 | / 20 | 21"), reconstituirea este a manifestului, nu a textului, și se verifică în PDF.

## Două limite ale acestui lot

1. **Procedura de decontare are text derivat.** Este singura care descrie pasul succesiunii, deci exact
   cea care lipsea lanțului. PDF-ul local rămâne fără strat de text exploatabil, dar PDF-ul oficial
   `https://www.dcu.md/doc/Proceduri%20operatiuni%20decontare.pdf` a fost extras integral prin
   `web_extract` și păstrat în `raw/papers/bnm/dcu/DCU-PROC-DECONTARE.md`. Textul include secțiunile
   „Documente necesare", „Vizita la DCU", „Taxe și impozite" (p. 12–13) și „Anexa nr. 1. Scopul
   transferului" (p. 25–28). Rămân fără ancore de articol și trebuie verificate în PDF pentru citare
   externă.
2. **Fragmentarea textului de font.** Patru documente (reconciliere, insolvabilitate, garanții,
   comisioane) au fost produse cu un font care desparte diacriticele și cifrele în rulaje separate;
   extracția le redă pe rânduri separate („garan | ț iilor", „5 iu | l ie 202 | 1"). Textul este
   întreg, dar căutarea după cuvânt poate rata; o reconstituire prin lipirea fragmentelor de pe
   aceeași linie de bază este posibilă și repetabilă, dar nu a fost făcută, ca extracția să rămână
   cea implicită a bibliotecii, aceeași ca la Regulile DCU. De decis de Eugen dacă merită un pas
   separat.

## Ce rămâne deschis

- Validarea citatelor din procedura de decontare în PDF-ul oficial înainte de publicare externă; extrasul
  web este suficient pentru căutare locală, dar nu transformă automat textul în transcriere byte-verificată.
- Nota de copyright de pe fiecare pagină de titlu (Legea 139/2010): aceeași apreciere ca la Regulile
  DCU, a lui Eugen; vault-ul este privat.
- Documentele model (cereri, formulare) de pe pagina „Documente model" a dcu.md nu sunt ingerate.
