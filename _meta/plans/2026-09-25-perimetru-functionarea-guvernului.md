# Perimetrul „funcționarea Guvernului” — plan de ingerare (2026-09-25)

Stare: **executat la 2026-09-25, 29 de acte ingerate** (rezultat, cifre și capcane în secțiunea AR a manifestului
moldova-legal; harta în `concepts/perimetrul-functionarea-guvernului.md`). Planul de mai jos e cel de dinaintea căutării:
lista „ce cred eu că există” a fost înlocuită de ce s-a găsit pe legis.md (Regulamentul Guvernului e HG 610/2018, nu 34/2019).
Cloudflare a cerut întâi verificarea interactivă (Turnstile) în Chrome-ul lui Eugen; a trecut-o el.

## Ce e deja în vault (nucleul)

`L-136-2017` (Guvernul), `L-98-2012` (administrația centrală), `L-100-2017` (actele normative), `L-239-2008`
(transparența decizională), `L-158-2008` (funcția publică), `L-199-2010` (demnitarii), `L-181-2014` (finanțe publice),
`L-131-2015` (achiziții), `L-260-2017` (Curtea de Conturi), `L-133-2016`/`L-132-2016`/`L-325-2013` (integritate),
`L-124-2022` (servicii electronice), `COD-116-2018` (cod administrativ). Harta: `concepts/perimetrul-drept-administrativ.md`.

## Ce lipsește, pe straturi (din memorie și din graf; TOT de verificat pe legis.md, nu e citabil)

Ce spune graful (`citation-graph.json`, trimiteri din actele nucleului către acte nedetinute), verificat în fișier:
`L-797-1996` Regulamentul Parlamentului (citat de L-100-2017), `L-595-1999` tratatele internaționale (L-100-2017, L-98-2012),
`L-155-2011` Registrul unic al funcțiilor publice (L-158-2008), `L-344-1994` și `L-173-2005` Găgăuzia (L-100-2017,
L-436-2006), `L-246-2017` întreprinderea de stat (L-148-2023), `L-82-2017` integritatea (7 acte o citează),
`L-123-2023` stagiile plătite în serviciul public (L-158-2008), `L-64-1990` (abrogată de L-136-2017, doar pentru istoric).

Ce cred eu că există și trebuie căutat (necitit, ipoteză):
1. **Actele Guvernului despre Guvern:** Regulamentul Guvernului; regulamentul Cancelariei de Stat; procedura de
   elaborare/avizare a proiectelor de acte normative; planificarea și evaluarea documentelor de politici publice;
   consultarea publică; comisiile guvernamentale și structura de personal.
2. **Ministerele:** regulamentele de organizare și funcționare (hotărâri de Guvern) — un act per minister; se ia
   numai ce e în vigoare la structura de după reorganizarea din 2021 și modificările ulterioare.
3. **Situații excepționale:** legea regimului stării de urgență/asediu/război; protecția civilă.
4. **Control și buget:** controlul financiar public intern; procesul bugetar din hotărâri de Guvern.
5. **Guvernare digitală:** interoperabilitatea, platforma de interoperabilitate, informatizarea.
6. **Proprietate de stat:** întreprinderea de stat (`L-246-2017`), administrarea de către Guvern.

## Ce NU intră fără cerere expresă

Legile speciale ale fiecărui minister/agenție, fiscalitatea, justiția, apărarea. Cererea e „funcționarea Guvernului”,
nu tot dreptul administrativ (acela a fost lotul din 24-25.09.2026, secțiunile AO și AP ale manifestului).

## Metoda (neschimbată)

Titlu cu titlu pe legis.md → lista de versiuni de pe pagina actului → cea mai nouă consolidare care nu e în viitor
(nu doc_id-ul din rândul de căutare) → verificare abrogare în fișă ȘI în antetul corpului (`check-repeal-before-ingesting`)
→ un singur blob cu hash pe parte → `ingest_business_law.py` → `fix_wrapped_titles.py` cu copie în `wiki-backups/` →
pagini de entitate → registrul consolidărilor viitoare → `close_session.py`.
