# Plan de restructurare a wiki-ului juridic

Data: 5 septembrie 2026
Folder vizat: `C:\Users\harab\wiki`
Stare: propunere, în așteptarea aprobării. Nu s-a modificat nimic în vault.

---

## 1. Ce s-a decis

Opt decizii, luate în discuția din 5 septembrie. Sunt notate aici pentru caexecuția să nu depindă de memoria conversației.

**D1. Un singur vault, două perimetre declarate.** Corpusul juridic și cel de politici rămân în același folder, dar fiecare pagină poartă un câmp `perimeter: legal | policy`. Regulile de verificare diferă între ele. Motivul: munca reală trece constant granița, iar o lacună de transpunere este juridică prin natură și politică prin consecință.

**D2. Traducerile BNM nu se ancorează.** Primesc `source_type: translation`. Se folosesc doar pentru a localiza o prevedere, care apoi se citează din textul românesc. O ancoră pe o traducere ar afirma ceva fals, anume că textul este autoritativ.

**D3. Șase legi bancare se ingerează în română, apoi corpusul englezesc se retrage.** Lista: 202/2017, 548/1995, 114/2012, 232/2016, 62/2008, 575/2003. Destinația: `raw/papers/bnm/legal-ro/`. Retragerea traducerilor se face numai după ce fiecare lege din listă este ingerată, ancorată și are pagină de entitate.

**D4. Schema devine verificabilă mecanic.** Un fișier de specificație ține regulile mecanice. Din el se generează atât partea corespunzătoare din `SCHEMA.md`, cât și verificatorul. Secțiunile de judecată rămân scrise de mână.

**D5. Control de versiuni: git local plus depozit privat pe GitHub.**

**D6. Lucrarea pe spețe iese din vault.** Un dosar de client și o bază de cunoaștere sunt lucruri diferite, cu durate de viață diferite. Separarea este condiția pentru ca vault-ul să poată fi trimis întreg pe GitHub fără o triere de fiecare dată.

**D7. Fișierele EMIR se arhivează, nu se șterg.** Motivul: paginile analitice care rămân își sprijină afirmațiile pe ele.

**D8. `log.md` se redefinește ca index.** Git înregistrează ce s-a schimbat. Jurnalul înregistrează ce s-a aflat și ce s-a decis.

**D9. Copiile din `legal-career/` se tratează diferențiat după ritmul lor de schimbare.** Cele șase documente de metodă primesc ștampilă de provenimență. Registrul de spețe se reîmprospătează din proiect la începutul oricărei sesiuni Cowork care atinge wiki-ul.

---

## 2. Ordinea lucrărilor și de ce este aceasta

Ordinea nu este arbitrară. Fiecare pas creează condiția pentru următorul.

Plasa de siguranță vine prima, pentru că orice altă operațiune devine reversibilă abia după ea. Separarea materialului de client vine înaintea sincronizării cu GitHub, pentru că un depozit se oglindește întreg și nu selectiv. Specificația și verificatorul vin înaintea ingerării celor șase legi, pentru că regula pe care CLAUDE.md a formulat-o deja spune: nicio ingerare fără controlul care o acoperă. Retragerea traducerilor vine ultima, pentru că înlocuitorul trebuie să existe înainte.

| Pas | Lucrare | Depinde de |
|---|---|---|
| P0 | Copie de rezervă, git local, prima înregistrare | nimic |
| P1 | Lucrarea pe spețe iese din vault | P0 |
| P2 | Depozit privat pe GitHub | P1 |
| P3 | Curățenie: EMIR, reziduuri, cale ruptă | P0 |
| P4 | Perimetre pe cele 83 de pagini | P0 |
| P5 | Specificație, `SCHEMA.md` generat, verificator | P4 |
| P6 | `log.md` restructurat | P5 |
| P7 | Ștampile pe copiile de metodă, reîmprospătare registru | P5 |
| P8 | Ingerarea celor șase legi bancare în română | P5 |
| P9 | Retragerea traducerilor englezești | P8 |

Pașii P0 până la P7 sunt o sesiune de lucru. P8 este o sesiune separată, pentru că ingerarea a șase legi cu ancorare și verificare este muncă de sine stătătoare. P9 vine după.

---

## 3. Ce se atinge, fișier cu fișier

Nimic din lista de mai jos nu se execută înainte de aprobare. Pentru mutări și ștergeri îți arăt din nou lista exactă în momentul operațiunii.

### 3.1 Fișiere care se MUTĂ, nu se șterg

| Ce | De unde | Unde | Mărime |
|---|---|---|---|
| Răspunsul despre drepturile acționarului la bancă | `Claude outputs/2026-09-04-raspuns-scurt-drepturi-actionar-banca.md` | folder de dosare, în afara vault-ului | 6 KB |
| Cele cinci fișiere EMIR | `queries/` | `_archive/emir-2026-07/` | 154 KB |
| Conținutul jurnalului, 1.212 linii | `log.md` | `_meta/log/2026-07-09.md` | 147 KB |

### 3.2 Foldere care se ȘTERG, toate goale sau fără conținut util

| Ce | Motiv |
|---|---|
| `C:\Users\harab\wiki\` (folder cu acest nume literal, în rădăcină) | Creat de un script care a primit o cale Windows sub un shell Linux. Conține doar un `_meta/lint` gol. |
| `Untitled/` | Gol, creat de Obsidian. |
| `raw/articles/`, `raw/transcripts/` | Goale. Sunt rămășițe ale schemei din iulie, care le definea. Schema rescrisă nu le mai prevede. |
| `_archive/raw/cnpf-extended-eurlex-before-20260709-150323` | Instantaneu de rezervă cu zero octeți. |
| `_archive/raw/eurlex-before-refresh-20260904-214146` | Instantaneu de rezervă cu zero octeți. |

Cele două instantanee goale merită o notă separată. Existau ca să te protejeze și nu conțin nimic. Sunt exact tipul de eroare tăcută pe care stratul de control a fost construit să îl prevină, doar că de data asta la nivelul rezervelor, nu al textului.

### 3.3 Fișiere care se MODIFICĂ

| Fișier | Ce se schimbă |
|---|---|
| `entities/bnm.md` | Calea ruptă către corpusul BNM, în trei locuri. Folderul s-a mutat în `legal/documents/`, referința nu a fost actualizată. Este singura legătură ruptă din tot vault-ul. |
| `comparisons/emir-concordance-skeleton.md` | Șase legături și patru referințe de cale, redirecționate către arhivă. |
| `concepts/acquis-CSDR-EMIR.md` | Cinci legături, redirecționate către arhivă. |
| `index.md` | Se scot cele cinci intrări EMIR. Se adaugă structura pe perimetre. |
| `raw/papers/cnpf/_manifest.md` | Două legături. Vezi punctul deschis 3 de mai jos. |
| `raw/papers/cnpf/md-2026-07-03-schelet-lege-emir.md` | Două legături. Vezi punctul deschis 3. |
| Cele 83 de pagini din `entities/`, `concepts/`, `comparisons/`, `queries/` | Se adaugă câmpul `perimeter`. Operațiune scriptată, verificată imediat după. |
| `CLAUDE.md` | Reguli noi: perimetre, jurnal ca index, reîmprospătarea registrului de spețe, rularea verificatorului. |
| `SCHEMA.md` | Rescriere. Partea mecanică devine generată, între marcaje. |
| `log.md` | Devine index scurt, cu trimitere la arhiva jurnalului. |

### 3.4 Fișiere care se CREEAZĂ

- `_meta/schema/schema-spec.yaml`, specificația mecanică, cu comentarii în limbaj obișnuit
- `_meta/schema/build_schema.py`, generatorul părții din `SCHEMA.md`
- `_meta/schema/validate_wiki.py`, verificatorul
- `.gitignore`
- `_archive/emir-2026-07/_PROVENANCE.md`, nota care spune de unde vin fișierele și de ce au fost retrase
- `_meta/log/2026-07-09.md`, arhiva jurnalului
- `README.md` în rădăcina depozitului, pentru GitHub

### 3.5 Ce NU se atinge

Textul legal din `raw/papers/`. Cele 400 de fișiere de sursă rămân neschimbate, cu excepția celor două referințe EMIR de la punctul 3.3, care sunt metadate, nu text normativ. Ancorele, hash-urile și frontmatter-ul rămân intacte.

`_meta/anchoring-work/` rămâne întreg, inclusiv cele cinci copii aproape identice ale Codului civil, circa 11 MB. Par redundante, dar una dintre ele, versiunea cu textul reunit, este proba pentru o decizie încă deschisă în CLAUDE.md, anume dacă se reunesc rândurile Codului civil. Nu se aruncă probe pentru o decizie nedată.

---

## 4. Ce intră în depozit și ce rămâne doar pe disc

Vault-ul are 691 MB. Din ele, 578 MB sunt PDF-uri și documente originale, în 336 de fișiere. Textul propriu-zis este 78,5 MB în 756 de fișiere.

În depozit intră textul. Nu intră folderele `original/`, adică 577 MB de documente descărcate de pe site-urile BNM, MDED și altele, și nu intră starea de interfață a Obsidian, care se schimbă la fiecare deschidere.

**Un risc pe care trebuie să îl vezi limpede.** Originalele rămân doar pe discul tău, fără nicio copie. Nu este o înrăutățire, pentru că nici acum nu au vreuna, dar după ce restul capătă protecție prin GitHub ele devin singura parte neprotejată. Sunt redescărcabile de la sursă, deci pierderea ar costa timp, nu conținut. Dacă vrei o soluție, cea mai simplă este o copie pe un disc extern sau într-un serviciu de stocare, în afara acestui plan.

---

## 5. Puncte deschise, pe care le decizi tu

**1. Unde stau dosarele de client.** Am nevoie de o cale în afara folderului `wiki`, de exemplu `C:\Users\harab\dosare`. Nu o pot crea singur, pentru că accesul meu se oprește la folderul wiki. Îmi spui calea și o ceri prin butonul de adăugare folder, sau îmi spui unde vrei și îți cer eu accesul.

**2. Numele depozitului de pe GitHub și confirmarea că e privat.** Chiar și după ce iese materialul de client, depozitul conține analiza ta, adică cele 83 de pagini. Este proprietatea ta intelectuală, nu material confidențial de client, dar merită confirmat explicit înainte de prima sincronizare.

**3. Cele două fișiere din `raw/` cu legături EMIR.** Regula folderului spune că `raw/` este imuabil. Poziția mea este că un manifest și o notă despre un document de lucru sunt metadate, nu text normativ, deci se pot edita. Dacă preferi ca `raw/` să rămână intact fără excepții, alternativa este să las acele două legături să indice către arhivă printr-o redirecționare notată în `_PROVENANCE.md`, iar verificatorul să le accepte ca excepție declarată. Prima variantă e mai curată, a doua e mai strictă.

**4. Legea 575/2003 privind garantarea depozitelor.** Nu sunt sigur că mai este în vigoare în această formă. Transpunerea directivei 2014/49/UE s-ar putea să se fi făcut printr-o lege nouă. Se lămurește la ingerare, când scriptul caută actul pe legis.md. Dacă a fost înlocuită, ingerăm actul care o înlocuiește și îți spun.

---

## 6. Riscuri și puncte de oprire

**Riscul principal este intervalul dintre prima modificare și prima înregistrare în git.** Se elimină făcând copia de rezervă și inițializarea git înaintea oricărei atingeri. Nimic nu se modifică până când prima înregistrare nu este confirmată.

**Modificarea în masă a celor 83 de pagini** este singura operațiune scriptată pe stratul structurat. Se face după prima înregistrare, deci este reversibilă printr-o singură comandă, și se verifică imediat cu verificatorul nou.

**Verificatorul poate semnala erori care existau dinainte.** Este scopul lui. Dacă apar, ți le arăt și decidem care se repară acum și care se notează ca lacună cunoscută. Nu repar în tăcere nimic ce ține de judecată.

Mă opresc și îți arăt rezultatul în trei momente: după copia de rezervă și prima înregistrare, înainte de orice modificare; înainte de mutări și ștergeri, cu lista exactă; și după prima rulare a verificatorului, cu lista a ce a găsit.

---

## 7. Ce se schimbă pentru tine, în practică

După P0 până la P7, wiki-ul arată la fel când îl deschizi în Obsidian, cu trei diferențe. Fiecare pagină spune din ce perimetru face parte. Jurnalul e scurt și se citește. Există o comandă care îți spune dacă ceva s-a stricat.

După P8, perimetrul bancar este acoperit în română, iar răspunsurile care ating băncile pot fi ancorate în loc de parțial ancorate. Aceasta este diferența practică cea mai mare, și e cea care a lipsit la prima ta speță reală în proiect.

După P9, corpusul englezesc iese din calea căutărilor și nu mai riști să citezi dintr-o traducere.

---

## 8. Ce actualizez în proiectul de pe claude.ai la final

Documentul 05, harta cunoștințelor, primește noua stare de acoperire și noile mecanisme de control. Documentul 03, regulile de lucru, primește regula perimetrelor. Registrul de spețe primește actualizarea punctului deschis din M-001 care s-a închis între timp, pentru că Codul contravențional este acum ingerat și ancorat.
