# Prompturi de operare

Se inserează în Claude Code (sau în agent) după ce l-ai orientat spre acest folder.
Aplică regulile din CLAUDE.md.

## INGEST (INGESTIE)

> Citește întâi CLAUDE.md. Adaug o sursă nouă: <inserează text sau cale>.
> 1. Salvează textul verbatim în `raw/<ID>.md` (nu îl edita). Adaugă un rând în
>    `raw/_manifest.md` cu autoritatea de mandat și ancora de acquis.
> 2. Creează sau actualizează `wiki/<ID>.md` folosind șablonul de pagină de lege. Fiecare
>    frază trebuie să poarte o ancoră de articol `[<ID> art.N]`; ce nu poți ancora merge
>    la „Întrebări deschise", nu în corpul principal.
> 3. Setează câmpul `mandat:`. Dacă sursa privește asigurările, OCN, AEÎ sau birourile de
>    credit, implicit `BNM (prudențial) / CNPF-rezidual` și menționează transferul de la
>    1 iulie 2023, dacă textul nu spune altfel.
> 4. Actualizează fiecare pagină existentă care referențiază această sursă. Enumeră ce ai
>    schimbat. Nu afirma ca stabilit nimic marcat `[de verificat]`.

## QUERY (INTEROGARE)

> Răspunde doar din `wiki/`. Citează pagina și ancora de articol `raw/` din spatele fiecărei
> afirmații. Dacă răspunsul depinde de un element `[de verificat]` sau de o limită de mandat
> semnalată de lint, spune explicit, nu netezi. Dacă wiki-ul nu susține răspunsul, spune ce
> lipsește și ce sursă trebuie ingerată.

## LINT (VERIFICARE)

> Rulează verificările din CLAUDE.md peste `wiki/`. Scrie constatările în
> `wiki/_lint-report.md` grupate ca: afirmații orfane, conflicte de mandat, consolidare
> învechită, lacune de transpunere, referințe rupte. Pentru fiecare, dă pagina, problema și
> cea mai mică corecție — dar NU rezolva automat o contradicție juridică sau un conflict de
> mandat; acelea au nevoie de aprobarea mea.

## Note pentru acest wiki concret
- Limita de mandat e principala sursă de eroare. La îndoială, o sursă e `CNPF` doar dacă e
  de piață de capital; altfel tratează rolul CNPF ca protecție-consumatori reziduală și pune
  autoritatea prudențială ca BNM.
- Prioritizează textele consolidate de pe legis.md față de rezumatele secundare/ghidurile
  juridice; folosește ghidurile doar pentru a localiza prevederi, niciodată ca citare de referință.
