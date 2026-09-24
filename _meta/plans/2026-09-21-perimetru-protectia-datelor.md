# Perimetrul protecției datelor cu caracter personal: ce lipsește și în ce ordine se ingerează

Data: 2026-09-21. Sursă: întrebare a lui Eugen despre un ordin CNPDCP invocat ca „nr. 48 din
septembrie", verificată împotriva vault-ului (`entities/`, `raw/papers/`, `concepts/`,
`_meta/graph/citation-graph.md`) și a surselor publice, nu presupusă.

Statut: **executat la 2026-09-21, pașii 1–5, la decizia lui Eugen „tot planul".** Rezultatul, cu ce s-a
găsit și ce a rămas: secțiunea AK din `raw/papers/moldova-legal/_manifest.md` și intrarea din `log.md`. Ce
nu s-a făcut: Ordinul 38/2026 (negăsit pe legis.md), textul Protocolului 108+ (PDF imagine, fără OCR),
comparația L-160/2026 față de Directiva 2016/680, rîndul din matricea de transpunere. Corecții față de plan:
„15.05.2026" este data depunerii, nu a ratificării (legea: 20.03.2026); nr. 41/2026 și 581/2015 sînt
**decizii**, nu ordine; ordinul „48" tot nu există.

## De ce apare acum

Regimul protecției datelor s-a schimbat în întregime la **23.08.2026**. Trei acte au intrat
simultan în vault pe 10 septembrie, prin coada grafului de citare, nu printr-un plan:
[[L-195-2024]] (legea generală, transpune GDPR), [[L-160-2026]] (materia penală, transpune
Directiva 2016/680) și [[L-133-2011]], abrogată și păstrată pentru cele 19 acte care încă
trimit la ea.

Textul de nivel 1 este deci acoperit. Nimic altceva din acest perimetru nu este. Consecința
practică: o întrebare de conformitate a unei companii poate fi ancorată pe lege, dar nu pe
obligația concretă care o leagă, pentru că obligația concretă stă în ordinele CNPDCP, iar
ancora interpretativă stă în textul UE. Niciuna nu este în bază.

Acest plan închide și punctul 04 din `_meta/plans/2026-09-17-lacuna-drept-general.md`, care
lăsa deschisă întrebarea dacă succesoarea Legii 133/2011 este sau nu în corpus. Este, din
10 septembrie. Punctul acela poate fi marcat verificat.

## Ce lipsește, verificat fișier cu fișier

### 01. Stratul secundar CNPDCP: zero acte

`ls raw/papers/moldova-legal/ | grep -i cnpdcp` nu returnează nimic. `ls entities | grep -i
cnpdcp` nu returnează nimic. Nu există niciun ordin al autorității în vault.

Acest strat nu este istorie. **Art. 90 alin. (5) din [[L-195-2024]] menține în vigoare actele
emise „în temeiul art. 32 alin. (3) și alin. (5) lit. f) și i)" din Legea 133/2011**, nu toate
actele emise sub art. 32. Un ordin continuă să lege după 23.08.2026 doar dacă s-a întemeiat pe
unul dintre aceste alineate și nu a fost abrogat expres; pentru fiecare ordin se citește
preambulul și se verifică temeiul, nu se presupune. Actele identificate public (**din surse
externe, neverificate în vault**; statutul lor se confirmă la ingerare):

| act | obiect | observație |
|---|---|---|
| Ordin CNPDCP nr. 27 din 31.03.2022 | lista operațiunilor care cer evaluare de impact (DPIA) | publicat MO nr. 120-127 din 22.04.2022 |
| Ordin CNPDCP nr. 39 din 10.08.2026 | modifică Ordinul 27/2022, îl mută de pe L-133/2011 pe L-195/2024 | în vigoare 23.08.2026, legis.md doc 155868 |
| Ordin CNPDCP nr. 38/2026 | formularul tipizat al plângerii | listat în registrul CNPDCP |

Inventarul complet al ordinelor în vigoare nu a fost stabilit. Se face din registrul propriu al
autorității, nu din căutare pe legis.md, pentru că nu toate ordinele apar acolo.

**Nota de metodă:** Ordinul „48 din septembrie" despre care s-a întrebat nu există public. Nu a
fost găsit nici pe legis.md, nici în registrul CNPDCP, nici în presa de specialitate. Cel mai
probabil este o confuzie de număr cu 39/2026. Se reverifică la ingerare; dacă apare, intră aici.

### 02. Ancorele UE: absente chiar și ca extrase

Cele 32 de extrase `UE-*.md` din vault sunt **toate** din perimetrul CNPF. Nici GDPR
(Regulamentul (UE) 2016/679), nici Directiva (UE) 2016/680 nu au fișier.

Graful de citare confirmă golul din interior: `EU-L-1995-46`, Directiva 95/46/CE, apare ca
țintă externă citată de [[L-195-2024]], iar GDPR apare o singură dată în textul legii, ca
referință, fără corespondent în bază.

Efectul asupra răspunsurilor este direct. Documentul 03 cere ca, acolo unde o regulă transpune
drept UE, textul UE să fie ancora interpretativă și divergența să fie raportată ca finding.
Fără textul UE, regula nu poate fi aplicată pe acest perimetru. Se poate spune că L-195/2024
transpune GDPR, dar nu se poate spune unde se abate.

### 03. Convenția 108 și Protocolul 108+

`grep -ril "Convenția 108"` pe `entities`, `concepts`, `comparisons` nu returnează nimic.

Protocolul de amendare a fost ratificat de Republica Moldova la **15.05.2026** și publicat în
Monitorul Oficial (dată din sursă externă, neverificată în vault; se confirmă la pasul 2). Este tratat internațional, deci **nivelul 2 al ierarhiei surselor** din
documentul 03, deasupra legii organice. Un perimetru care ține legea și nu ține tratatul pe
care legea îl execută are ierarhia ruptă la mijloc.

### 04. Pagina de concept: inexistentă

Cele 24 de pagini `concepts/acquis-*.md` acoperă exclusiv perimetrul financiar. Nu există
`acquis-DataProtection`. Nu există nicio comparație L-195/2024 față de GDPR.

## Planul, în ordinea în care fiecare pas îl face pe următorul verificabil

**Pas 1. Ordinele CNPDCP.** Se stabilește mai întâi inventarul ordinelor în vigoare din
registrul autorității, apoi se ingerează. Ordinul 27/2022 se ia în versiunea consolidată cu
39/2026, nu în cele două separat, pentru că versiunea consolidată este cea care leagă.
Structurate în puncte, deci fără ancore la nivel de articol, ca `HCNPF-14-5-2016` și
`HBN-127-2013`; citarea se face „pct. N" și nu este ancorată. Script pe modelul
`_meta/imports/cnpf/ingest_cnpf_ro.py`.

**Pas 2. Convenția 108+.** Text de nivel 2. Sursă: Monitorul Oficial pentru legea de ratificare,
Consiliul Europei pentru textul consolidat al convenției.

**Pas 3. Extrase GDPR și Directiva 2016/680.** Pe modelul fișierelor `UE-*`, din EUR-Lex.

**Pas 4. Stratul analitic.** Pagini de entitate pentru tot ce a intrat la pașii 1 la 3, plus
`concepts/acquis-DataProtection.md` cu maparea articol la articol L-195/2024 față de GDPR, și
rândul corespunzător în matricea de transpunere.

**Pas 5. Controalele.** `validate_wiki.py`, `build_coverage.py`, `build_inforce_register.py`,
`build_hcc_register.py`, `build_citation_graph.py`, apoi commit.

## Riscul de structură, care este motivul pentru care pașii 3 și 4 se decid separat

Pașii 3 și 4 reintroduc exact asimetria pe care documentul 05 a trebuit deja să o corecteze o
dată: text moldovenesc integral comparat cu un extras UE de circa 170 de linii, ceea ce a produs
findings de transpunere care au trebuit înghețate pe 6 septembrie și reverificate pe 16. Dacă
pașii 3 și 4 se execută, se execută cu textul UE citit la sursă pentru orice concluzie de
divergență, nu din extras. Altfel se repetă greșeala cu un perimetru nou.

Pașii 1 și 2 nu au acest risc. Sunt text primar moldovenesc și tratat, nu comparație.

## Ce se cere de la Eugen

O singură decizie: pașii 1 și 2 acum, sau tot planul. Recomandarea din sesiunea de 21 septembrie
a fost 1 și 2 acum, 3 și 4 ca decizie separată.

## Rămas de făcut, consemnat la închiderea sesiunii din 2026-09-21

Executat în sesiune: pașii 1–5 (vezi secțiunea AK din `raw/papers/moldova-legal/_manifest.md`). Nu s-a făcut
ce urmează, în ordinea în care fiecare pas îl ajută pe următorul. Nimic de aici nu se presupune făcut.

1. **Făcut integral 2026-09-24.** Textul Protocolului 108+ (`Acord_ro-153723.pdf`, 20 pagini, imagine, fără
   OCR pe mașină) citit din imaginile randate (PyMuPDF, 200 dpi), ca la procedura de decontare DCU. Rezultat:
   `raw/papers/moldova-legal/CETS-223-2018.md`, neancorat dar text complet (preambul, art. 1-40, anexă).
   **Numărul de ratificări verificat direct pe pagina Consiliului Europei** (CETS 223, „Status as of
   24/09/2026"): **34, nu 38** — pragul de cinci ani (11.10.2023) a trecut de trei ani și Protocolul tot nu
   e în vigoare general; nu produce efecte nici măcar între cele 34 de state care l-au ratificat deja
   (Republica Moldova inclusă), pentru că art. 37 alin. (2) leagă și acea intrare în vigoare parțială de
   pragul de 38. Convenția 108 din 1981 rămâne singurul text internațional în vigoare. Rămas: comparația
   articol-cu-articol a Protocolului față de L-195/2024 și GDPR (nu s-a făcut, doar textul e ingerat).
   Detalii: secțiunea AL din `raw/papers/moldova-legal/_manifest.md`, `entities/L-36-2026.md`.
2. **Făcut 2026-09-24.** Ordinul CNPDCP nr. 38/2026 (formularul plîngerii) rămîne negăsit pe legis.md
   (căutare pe titlu confirmată fără rezultat), dar e ingerat din PDF (`raw/papers/moldova-legal/OCNPDCP-38-2026.md`),
   citit din imaginile paginilor, neancorat, ca `DCU-REGULI-2026`/`DCU-PROCEDURI`. Din 03.08.2026, nu
   septembrie cum bănuia acest plan; în vigoare 23.08.2026, abrogă Ordinul 44/2020.
3. **Făcut integral 2026-09-24 (finalizat în a doua sesiune).** Inventarul complet al actelor CNPDCP a fost
   verificat direct contra registrului autorității (datepersonale.md → Decizii/Ordine, Instrucțiuni Adoptate,
   Arhiva Decizii/Ordine, Regulamente CNPDCP, Proiecte), nu doar contra listei „adoptate" folosite la prima
   ingerare. Rezultat complet în `entities/CNPDCP-ORDINE.md`. Preambulul fiecărui act a fost citit.
   **Cele patru instrucțiuni sectoriale (electoral, poliție, educație, sănătate) au fost citite și temeiul lor
   verificat articol cu articol: toate patru invocă exact art. 20 alin. (1) lit. c) al L-133/2011, care nu e
   unul dintre cele două alineate pe care art. 90 alin. (5) L-195-2024 le menține (art. 32 alin. (3) și
   alin. (5) lit. f), i)), și niciuna nu are un ordin de salvare precum cel care l-a mutat pe 27/2022 pe
   L-195/2024 — toate patru și-au pierdut temeiul la 23.08.2026.** Instrucțiunile electorală și polițienească
   (scurte, PDF cu strat de text utilizabil) ingerate integral, text normativ verbatim:
   `raw/papers/moldova-legal/OCNPDCP-03-1-2013.md`, `raw/papers/moldova-legal/OCNPDCP-POLITIE-2013.md`.
   Educațională (18 pagini) și de sănătate (21 pagini) — doar temeiul confirmat din pagina 1 randată ca
   imagine, neingerate integral (PDF-uri lungi, extracție mecanică coruptă). Rămas neingerat separat, cu
   motiv explicit consemnat: decizia de încetare a prelucrării de către partidele politice din 11.12.2014
   și `DCNPDCP 08/2023` (identificată, dar nu ingerată separat — efectul ei
   asupra 581/2015 e deja corect reflectat prin marcaj), regulamentele CNPDCP (un singur act, fără relevanță
   juridică) și arhiva de decizii (decizii de speță, nu izvor de drept). **Găsit pe aceeași pagină, în afara
   scopului acestui punct: Ordinul CNPDCP nr. 48/2026**, negăsit la data acestui plan pentru că fusese
   publicat abia 16.09.2026 — vezi punctul 11 de mai jos.
4. **Decizia 581/2015**, statutul. Decizie pentru Eugen: se tratează ca în vigoare (legis.md, site) sau ca
   fără temei (art. 90)? De confirmat la Centru, nu în vault.
5. **Ordinul 31/2026, temeiul.** Nepotrivirea art. 28 alin. (7) față de art. 46 e notată ca finding. De
   verificat dacă Centrul a rectificat preambulul sau are o poziție publică.
6. **Decizia (UE) 2021/914, textul ingerat 2026-09-24; comparația cu Ordinul 31/2026 făcută în aceeași zi
   (opt divergențe verificate, în `concepts/acquis-DataProtection.md`; rămas: anexele 1–3 ale ordinului,
   absente din textul legis.md).**
   CELEX 32021D0914, text integral RO din Cellar (redirect 303 urmat): 4 articole proprii, 26 de
   considerente, și anexa — clauzele contractuale standard (SCC) propriu-zise, patru module. Fișier:
   `raw/papers/moldova-legal/UE-2021-914.md`, script nou `_meta/imports/eu/ingest_eu_scc.py` (structura unei
   decizii diferă de o directivă/regulament: conținutul greu stă în anexă, nu în articole — vezi
   `entities/UE-2021-914.md` pentru capcana de extracție, un tabel imbricat care dubla sub-punctele (i)-(iv)
   la prima încercare, corectată înainte de acceptare). **Comparația clauzelor din [[OCNPDCP-31-2026]] cu
   anexa acestei decizii nu s-a făcut** — doar textul e ingerat. Deciziile Comisiei privind caracterul
   adecvat enumerate în preambulul Deciziei 41/2026 rămân neingerate.
7. **Făcut 2026-09-24.** Legea comunicațiilor electronice nr. 72/2025, al doilea temei al Ordinului 40/2026
   (art. 115 alin. (10), verificat în text), ingerată ca `L-72-2025` prin Chrome-ul lui Eugen (`fetch` same-origin,
   descărcare blob a unui singur fișier). Vezi `entities/L-72-2025.md`; capcane: intrarea în vigoare amînată în
   proză (art. 127), art. 126 expirat.
8. **Făcut 2026-09-24.** L-160/2026 față de Directiva (UE) 2016/680: numerotarea NU coincide (46 articole
   față de 65, spre deosebire de L-195/GDPR care se potrivesc 1-la-1 pînă la art. 50) — comparație structurală
   completă plus patru constatări verificate în text: Directiva art. 18 (drepturile persoanei vizate în
   dosare/cazier penal) lipsește real din L-160, nu doar ca numerotare; amenda unică de 2 000 000 lei (art. 43)
   nu e o divergență de plafon pentru că Directiva nu fixează unul (spre deosebire de GDPR); L-160 nu își
   redefinește noțiunile, trimite integral la art. 4 din L-195/2024 plus doi termeni proprii; procedura de
   amendă și de plîngere trimit efectiv la L-195, nu o duplică. Detalii: `concepts/acquis-DataProtection.md`.
9. **Făcut 2026-09-24 pentru art. 4, 6, 9; capitolul III și art. 25–39 rămîn structurale.** Harta din
   `concepts/acquis-DataProtection.md` are acum comparație alineat cu alineat pentru art. 4 (trei diferențe
   reale: „marketing direct" și „cifră totală de afaceri" sînt adăugiri ale L-195, nu în GDPR art. 4; cinci
   noțiuni ale mecanismului UE cu mai multe autorități lipsesc, structural), art. 6 (alin. (2) are conținut
   diferit, nu doar formulare diferită; alin. (3) omite integral al doilea paragraf al GDPR despre ce poate
   conține temeiul juridic și cerința de proporționalitate) și art. 9 (patru diferențe: exemplele de la
   lit. d), excepția mai largă de la lit. f) — include procedura administrativă și extrajudiciară, nu doar
   instanța —, omiterea alternativei „organisme naționale competente" la alin. (3), lipsa clauzei de habilitare
   de la alin. (4)). Capitolul III și art. 25–39 rămîn comparate doar structural, cu un spotcheck punctual
   (art. 12, 33–39, fără divergență găsită dincolo de ce era deja consemnat). Considerentele (173) tot nu au
   fost folosite. **Art. 88, 90, 91 verificate cu ambele capete deschise, nu doar căutare de cuvinte**: art. 88
   (loc de muncă) confirmat absent atît din L-195 cît și din Codul muncii (COD-154-2003), care nu are un regim
   propriu de prelucrare a datelor angajaților; art. 90 (secretul profesional) — carve-out-ul punctual din
   art. 14 alin. (5) lit. d) există și în GDPR la același loc, deci nu e adăugire, dar clauza generală de
   habilitare a statelor membre lipsește real; art. 91 (biserici) confirmat absent, fără regim comprehensiv
   propriu pentru organizații religioase.
10. **Rîndul din matricea de transpunere** al perimetrului (documentul 05). Se adaugă în proiectul claude.ai
    „Legal Wiki", nu în copia din `legal-career/`. Include și legătura cu `AA-2014` (dacă Anexa XXVIII-A sau
    alt capitol cere transpunerea GDPR), neverificată.
11. **Ordinul „48" există, rezolvat 2026-09-24 — nu era o confuzie.** Ordinul CNPDCP nr. 48/2026, „Regulamentul
    privind efectuarea investigației" (67 puncte), adoptat 09.09.2026, publicat 16.09.2026 — deci după data
    acestui plan, ceea ce explică de ce nu apărea încă la căutarea din 21 septembrie. doc_id legis.md `156385`,
    ingerat integral, verificat text-cu-text (`_meta/imports/cnpdcp/verify_cnpdcp_ro.py`, 0 eșecuri din 8 acte).
    Abrogă Ordinul 25/2024. Detalii: `entities/CNPDCP-ORDINE.md`.
    **Codul legis.md al deciziilor 41/2026 și 581/2015** rămîne neconfirmat din fragmentul HTML.
12. **Registrul de spețe** (`legal-career/06-matter-log.md`): stampila `taken` a rămas din 19 septembrie;
    regula D9 cere registrul curent de la Eugen.

Metodă pentru pașii 2–3: `_meta/imports/cnpdcp/ingest_cnpdcp_ro.py`; HTML-ul din Chrome prin `fetch`
same-origin și POST către un receptor local (memoria `chrome-post-to-localhost-receiver`); actele UE prin
`_meta/imports/eu/ingest_eu_dataprotection.py`, cu CELEX-ul adăugat în `DOCS`.
