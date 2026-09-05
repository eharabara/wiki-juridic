# BNM — legile bancare în română (legal-ro) — manifest

Creat 2026-09-05, pasul P8 al planului de restructurare (decizia D3). Aceste fișiere sunt textul
românesc consolidat de pe legis.md al legilor bancare pe care corpusul BNM le avea doar ca traduceri
engleze neoficiale, neancorate. Regula D2: traducerea localizează, textul de aici se citează.

## Sursa și metoda

- Sursă: legis.md, endpoint `showdetails/<doc_id>`, extras în aceeași zi cu consultarea.
- Descărcare: legis.md a activat la 2026-09-05 după-amiază o verificare Cloudflare care blochează
  `curl`. HTML-ul a fost luat din Chrome-ul lui Eugen, după ce el a trecut verificarea, ca DOM
  serializat (`document.documentElement.outerHTML`), și păstrat în `_meta/imports/bnm/legis-md-ro/`.
  Consecință: fișierele HTML de probă sunt DOM-ul serializat de browser, nu octeții serverului;
  etichetele `<sup>` și structura `#contentdoc` sunt intacte, ceea ce este tot ce cere extractorul.
- Extracție: `_meta/imports/bnm/ingest_bnm_ro.py`, înveliș peste
  `_meta/imports/moldova-legal/ingest_business_law.py`, cu aceleași funcții de rezolvare a
  exponenților, extracție și asamblare. Verificare: `_meta/imports/bnm/verify_bnm_ro.py`, generat din
  `verify_business_law.py`, cu testul de fond identic: liniile de structură adăugate se scot și
  restul se compară linie cu linie cu extracția simplă din același HTML.
- doc_id-urile au fost găsite prin căutare în titlu, `search_type=1`, fără diacritice; rândul actului
  de bază apare cu marcajul „Modificat” și numărul `LP<nr>/<an>`.

## Actele

| Fișier | Act | doc_id | Consolidare | Ancore | Integritate | Note |
|---|---|---:|---|---:|---|---|
| `L-202-2017.md` | Legea nr. 202/2017 privind activitatea băncilor | 151445 | 2025-09-20 | 155 | PASS, 1559 linii | 149 de bază fără lacune, 6 cu exponent |
| `L-548-1995.md` | Legea nr. 548/1995 cu privire la BNM | 154046 | 2026-04-23 | 91 | PASS, 842 linii | **7 lacune fără marcaj în sursă**: 12, 13, 29, 30, 48, 54, 73; republicată 2015; `[de verificat]` |
| `L-114-2012.md` | Legea nr. 114/2012 servicii de plată și monedă electronică | 155331 | **2027-01-01, viitoare** | 131 | PASS, 1328 linii | o dispoziție cu intrare amânată, art. 103^1 alin. (4) lit. h) |
| `L-232-2016.md` | Legea nr. 232/2016 redresarea și rezoluția băncilor | 146912 | 2025-02-28 | 344 | PASS, 1443 linii | articole fără titlu, forma `Articolul N. –` |
| `L-62-2008.md` | Legea nr. 62/2008 reglementarea valutară | 152953 | 2025-12-31 | 73 | PASS, 1103 linii | titlul oficial poartă asterisc de republicare |
| `L-160-2023.md` | Legea nr. 160/2023 garantarea depozitelor în bănci | 137939 | 2023-10-01, nemodificată | 58 | PASS, 599 linii | **înlocuiește Legea 575/2003**, abrogată pe legis.md (doc_id 137950) |
| `L-550-1995.md` | Legea nr. 550/1995 cu privire la lichidarea băncilor (fosta Lege a instituțiilor financiare) | 146899 | 2025-02-28 | 20 | PASS, 348 linii | P8-bis; **denumire schimbată**; doar arts. 1–3 și 38^1–38^17 în vigoare, cap. I–VI abrogate |
| `L-250-2017.md` | Legea nr. 250/2017 supravegherea suplimentară a conglomeratelor financiare | 105629 | 2018-03-29, nemodificată | 23 | PASS, 251 linii | P8-bis; BNM și CNPF sub același regim |
| `L-239-2008.md` | Legea nr. 239/2008 transparența în procesul decizional | 142655 | 2024-07-05 | 20 | PASS, 148 linii | P8-bis; lege generală, aici doar pentru că BNM o ține în registrul său |

## Ce s-a schimbat față de lista D3

Lista D3 numea Legea 575/2003. legis.md o arată abrogată; actul curent este Legea 160/2023, în vigoare
din 01.10.2023, care transpune parțial Directiva 2014/49/UE. Decis de Eugen la 2026-09-05: se
ingerează înlocuitorul. Textul abrogat nu este ingerat; pentru spețe anterioare lui 01.10.2023 se
caută separat.

## P8-bis, 2026-09-05

După P9 au rămas în `raw/papers/bnm/legal/documents/` cinci traduceri engleze fără text românesc în
vault: 250/2017 (două variante), 550/1995 și 239/2008 (două variante). Cele trei acte au fost ingerate
în aceeași zi, pe aceeași metodă. Cloudflare a cerut din nou bifa lui Eugen la prima navigare:
verificarea expiră între sesiuni.

## Ce rămâne deschis

- Lacunele din `L-548-1995`, mai sus. Nu se corectează aici; se verifică la sursă.
- Legile de interpretare (185/2023 și 22/2020 pentru 202/2017; 265/2016 pentru 232/2016) nu sunt
  ingerate. Articolele interpretate nu se citează fără ele.
- Retragerea traducerilor engleze corespunzătoare: făcută la P9 pentru primele șase legi
  (`_archive/bnm-en-2026-09/`); pentru cele trei de la P8-bis, cele cinci fișiere engleze rămase
  se mută în aceeași arhivă când Eugen confirmă lista.
