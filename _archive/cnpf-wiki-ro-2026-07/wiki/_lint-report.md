# _lint-report — rularea 2026-07-09

Domeniu: **31 pagini wiki** (14 legi + REG-ICF + 14 acquis + matrice + raport) și **15 înregistrări `raw/`**
(14 consemnări de lege + manifest). S-au aplicat cele cinci verificări din CLAUDE.md. Nimic nu s-a
corectat automat; contradicțiile juridice și conflictele de mandat rămân semnalate pentru aprobare.
Această rulare **înlocuiește rularea 4** și păstrează mai jos faptele deja rezolvate.

## Cauză-rădăcină sistemică (context pentru cele mai multe constatări)
**14 din 14** consemnări `raw/` conțin acum text de articol (extras de pe legis.md 2026-07-09, citate scurte
verbatim). Nucleul CNPF: **L-171-2012** (art.1, 2, 5, 6, 111 + anexa), **L-192-1998** (art.1, 2, 3, 6, 7, 8, 21–22),
**L-181-2023** (art.1, 2), **L-308-2017** (art.4, 15), **L-198-2020** (art.1, 27), **L-234-2016** (art.1, 23),
**L-2-2020** (art.1, 2), **L-1134-1997** (art.1, 38). Pivot: **L-178-2020** (art. I, VIII — transferul 01.07.2023).
Partea BNM (art.1/scop, intenționat concise): **L-1-2018**, **L-92-2022**, **L-106-2022** (art.1, 4),
**L-122-2008**, **L-139-2007** (art.4, 10). Rămâne de preluat doar textul consolidat **integral** al legilor mari
(ex. 171/2012 ~392 mii caractere); datele de consolidare legis.md sunt înscrise în `raw/` (vezi §3).

## Rezolvat și menținut (din rulările anterioare — nu regresa)
- **Proprietatea DCU** — consecvent pe [[L-234-2016]], [[L-171-2012]] și [[acquis-CSDR-EMIR]]: DCU aparține
  BNM (Legea 234/2016 art.23); Registrul de stat al valorilor mobiliare a trecut de la CNPF la DCU. Fără flag deschis.
- **ID-uri orfane rezolvate ca pagini:** L-MTPL → **L-106-2022** (RCA, confirmat MO 2022 129-133),
  **L-139-2007** (AEÎ, confirmat MO 2007 112-116), **REG-ICF** (reclasificat ca act subordonat sub L-171-2012).
- **Manifest consistent** — folosește ID-uri reale (L-106-2022, L-139-2007) cu referințe MO; „L-MTPL" eliminat.
- **Fundația celor 2 legi prioritare** — L-171-2012 și L-192-1998 au acum ancore la nivel de articol pentru
  afirmațiile principale din „Scop"/„Obiective"/„Atribuții".

## Acțiuni prioritare (în capul listei)
1. Inserează **textul consolidat integral** al L-171-2012 și L-192-1998 de pe legis.md (pas manual: pagina
   se încarcă dinamic, oglinda PDF CNPF blochează accesul automat) și reconfirmă numerele de articol
   (în special art.5 obiective la 171/2012 și realocarea art.8 post-2023 la 192/1998).
2. Adaugă un câmp **`data consolidării:`** în fiecare consemnare `raw/` — fără el, verificarea „consolidare
   învechită" nu poate fi făcută.
3. Repară **ancorele de articol suspendate** (vezi §1.b) și **cablează cele 3 noduri-orfan** (vezi §5).

## 1. Afirmații orfane (fără ancoră verificabilă la nivel de articol)
Taxonomie, de la cel mai grav la cel mai ușor:

**a. Ancore de articol suspendate — REMEDIAT 2026-07-09.** Cele trei cazuri au fost rezolvate prin
extragerea textului real de pe legis.md (via browser, JS render) și inserarea articolelor în `raw/`:
- [[L-181-2023]] — `raw/` conține acum **Art. 1** (Obiectul de reglementare) și **Art. 2** (Noțiuni principale).
- [[L-308-2017]] — `raw/` conține acum **Art. 4** (Entitățile raportoare; lit. c = perimetrul CNPF) și
  **Art. 15** (organele de supraveghere; lit. b = CNPF pentru art.4 alin.(1) lit. c) — ancoră fermă pentru rolul AML al CNPF.
- [[L-198-2020]] — `raw/` conține acum **Art. 1** (obiect; supraveghere CNPF) și **Art. 27** (capital minim
  „125000 de euro"). Nota anterioară „art.6" era un fals pozitiv (acel art.6 aparține [[L-192-1998]] în linia de referințe).
Ancorele wiki respective se verifică acum față de text de articol real, nu doar numere.

**b. Suport doar la nivel de număr — REMEDIAT 2026-07-09.** Toate cazurile ridicate la text de articol real:
[[L-106-2022]] (art.1, 4), [[L-139-2007]] (art.4, 10), plus [[L-1134-1997]], [[L-234-2016]], [[L-2-2020]].

**c. Ancoră doar la nivel de pagină — REMEDIAT 2026-07-09.** [[L-1-2018]], [[L-92-2022]], [[L-122-2008]] au
acum **Art. 1** (scop) în `raw/`. [[L-178-2020]] a primit ancoră `[raw/L-178-2020 art. I, art. VIII]` pe pagina
wiki (art. VIII = intrarea în vigoare 01.07.2023; art. I = modificarea Legii 548/1995 BNM).

**e. Mis-citare — REZOLVAT 2026-07-09.** [[L-1134-1997]] atribuia „capital social minim 600.000 MDL" la
**art.38(2)**. Verificat pe textul amendator **Legea 18/2020, pct. 19**: cifra e corectă, dar articolul corect
este **art. 40 alin. (2)** („Capitalul social [...] nu poate fi mai mic de 600000 de lei"); art. 38 privește
înregistrarea acțiunilor la înființare. Pagina wiki și `raw/L-1134-1997` (art. 40) au fost corectate.

**d. Ancoră la o non-sursă:** [[L-171-2012]] — „BIMx — lansare toamna 2026" ancorat la `[știri 2026]`, nu la
`raw/`; secțiunile „Registre-cheie", „Acte subordonate" și „Jurnal de modificări" sunt neancorate.

Notă: paginile de acquis afirmă drept UE fără ancoră EUR-Lex (acceptabil pentru stratul de acquis; adaugă
referințe CELEX când sunt disponibile).

## 2. Conflicte de mandat (pagină CNPF a cărei competență a trecut la BNM în 2023)
- **Niciun mislabel.** Toate sectoarele transferate sunt corect `BNM (prudențial) / CNPF-rezidual`:
  [[L-1-2018]], [[L-92-2022]], [[L-106-2022]], [[L-139-2007]], [[L-122-2008]]; [[L-234-2016]] `BNM (primar)`.
  Paginile de piață de capital rămân corect `CNPF`.
- **Dependență inter-perimetru de urmărit (nu eroare):** [[L-181-2023]] (CNPF) se bazează pe datele
  birourilor de credit din [[L-122-2008]] (acum BNM) — un regim supravegheat de CNPF care depinde de unul
  supravegheat de BNM. De semnalat pe harta de delimitare; fără corecție automată.

## 3. Consolidare învechită — DOVEZI NOI (data consolidării afișată de legis.md, extras 2026-07-09)
Datele de consolidare au fost culese acum din legis.md și înscrise în `raw/`. Confirmă „învechit" cu probe:
  - **L-171-2012** — legis.md afișează consolidarea **30.11.2018**. Wiki consemnează amendamente până la
    **Legea 177/2025** (CFD) → sursa primară disponibilă e cu ~7 ani în urma stării wiki. **ÎNVECHIT confirmat.**
  - **L-192-1998** — legis.md afișează consolidarea **31.07.2015** (LP136/2015). Precede transferul din 2023;
    art.8 se referă încă la „piața financiară nebancară" ca întreg → transferul a operat prin [[L-178-2020]] și
    legile sectoriale, nu printr-o modificare textuală a 192/1998 în această versiune. **ÎNVECHIT confirmat.**
  - **L-1134-1997** — legis.md afișează consolidarea **29.12.2017**; precede republicarea 31.12.2020 și
    Legea 18/2020 (de unde vine cifra de capital) → vezi mis-citarea de la §1.e.
  - **L-234-2016** — consolidat incl. **LP292 din 21.10.2023** (relativ curent).
- *Concluzie:* pentru legile mari de piață de capital, chiar și sursa primară de pe legis.md e o consolidare
  învechită; alinierile CNPF post-2018 (ex. CFD 2025) trebuie căutate separat. Câmpul `data consolidării` e
  acum în `raw/` pentru legile extrase.

## 4. Lacune de transpunere (din _transposition-matrix și paginile de acquis)
- **Parțial / învechit** (aliniat la instrumente UE abrogate): [[acquis-MiFID]], [[acquis-MAR]],
  [[acquis-Prospectus]], [[acquis-Transparency]] (post-2013/50), [[acquis-UCITS]] (OPCVM V), CRA III.
- **Doar baza, frontiera netranspusă:** [[acquis-AIFMD]] — AIFMD II (2024/927) peste [[L-2-2020]].
- **Lacune dure probabile, fără ancoră** ([[acquis-CSDR-EMIR]] și adiacente): EMIR, CSDR (supravegherea DCU),
  PRIIPs, vânzări în lipsă, indici de referință, SFTR → cele mai valoroase întrebări de screening Cap. 9.
- **Divergență, nu lacună:** [[L-181-2023]] include debitori-consumatori, în afara domeniului Reg. 2020/1503
  (art.1(2), prin trimitere la Dir. 2008/48/CE). De consemnat ca divergență, nu ca transpunere fidelă.
- **Lacună de acoperire în stratul de acquis — REMEDIAT 2026-07-09.** S-au creat 6 pagini de acquis pentru
  domeniile Cluster 2 din afara nucleului Cap. 9: [[acquis-Insurance]] (Solvency II/IDD → [[L-92-2022]]),
  [[acquis-MTPL]] (2009/103 → [[L-106-2022]]), [[acquis-IORP]] (IORP II → [[L-198-2020]]), [[acquis-CompanyLaw]]
  (2017/1132 + SRD II → [[L-1134-1997]]), [[acquis-ConsumerCredit]] (2008/48 → CCD2 → [[L-1-2018]]),
  [[acquis-AML]] (2015/849 + pachetul 2024 → [[L-308-2017]]). Marcate cu domeniul și legate în [[_transposition-matrix]] §D.
- Toate cele **14** pagini de acquis (8 piață de capital + 6 conexe, adăugate 2026-07-09) au o ancoră moldovenească (nicio pagină de acquis fără măsură).
  Termenele din Acordul de Asociere rămân `[de verificat]`; niciuna marcată depășită încă.

## 5. Referințe încrucișate
- **Legături rupte: 0** — graful e închis; fiecare `[[...]]` are pagină-țintă (verificat programatic).
- **Noduri-orfan: 0 — REMEDIAT 2026-07-09.** Cele 3 pagini spre care nu ducea nicio legătură au fost
  cablate prin back-links: `[[REG-ICF]]` în [[L-171-2012]] (Acte subordonate); `[[L-106-2022]]` și
  `[[L-139-2007]]` în [[L-178-2020]] (sectoare transferate); `[[L-106-2022]]` în [[L-92-2022]].
  Verificat programatic: 0 orfane, 0 rupte.
- Minor — REMEDIAT: linia de referințe din [[L-192-1998]] a fost completată (`- [[L-2-2020]] · [[L-181-2023]]
  · [[L-198-2020]] — legi sectoriale...`); separatorul suspendat nu mai există.

## Rezumat de sănătate (rularea 2026-07-09)
- Pagini: **31 wiki** (14 legi + REG-ICF + 14 acquis + matrice + acest raport) · **15 raw** (14 consemnări + manifest).
- Graf de referințe: **închis, 0 rupte, 0 noduri-orfan** (cele 3 cablate 2026-07-09).
- Manifest: **consistent** (ID-uri reale, referințe MO confirmate).
- Fundație de sursă primară: **14 din 14** legi au acum text de articol în `raw/` (nucleul CNPF cu 2+ articole;
  pivotul L-178-2020 cu art. I/VIII; partea BNM cu art.1/scop). Rămâne de preluat doar textul consolidat
  **integral** al legilor mari; datele de consolidare afișate de legis.md sunt înscrise în `raw/`.
- Problema sistemică dominantă: `raw/` fără text consolidat și fără dată a consolidării → blochează
  ancorarea reală la articol și verificarea de consolidare.
- `[de verificat]`-uri rămase, înguste: texte consolidate integrale pentru toate legile (pas manual);
  numărul hotărârii CNPF pentru REG-ICF; calea pachetului AML 2024; lista exactă de capitole Cluster 2.
- **Onest:** structura, analiza de transpunere și delimitarea de mandat sunt solide și verificate; stratul
  de sursă primară e început (5 legi), nu complet. Ancorele suspendate din §1.a au fost rezolvate; rămân
  ancore doar la nivel de pagină (§1.c) — nu le folosi într-un livrabil fără a deschide întâi articolul pe legis.md.
