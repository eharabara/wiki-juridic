---
source_url: https://www.bnm.md/files/Nota%20tehnică%20-%20Indicele%20prețului%20imobilului%20rezidențial.pdf
source_record: https://www.bnm.md/ro/content/lege-pentru-modificarea-si-completarea-legii-nr-62-xvi-din-21-martie-2008-privind
ingested: 2026-07-12
sha256: 6d0cd142dd56fcef572cefa5fe49cf300a4d1d5687bbc46af128946589135264
source_file_sha256: 1b43e58476a8445f20f9c342fafb7dda1b997c8adfa8a06ed89ae34ddf3a279d
source_type: legal-text
publisher: Banca Națională a Moldovei
language: ro
extraction_status: text-extracted
archived_original: raw/papers/bnm/legal/original/015__Nota tehnică - Indicele prețului imobilului rezidențial.pdf
---

# Law No 94 of May 13, 2016 on amending and supplementing Law no. 62-XVI of March 21, 2008 on foreign exchange regulation

- **BNM catalogue class:** legislation
- **BNM record:** https://www.bnm.md/ro/content/lege-pentru-modificarea-si-completarea-legii-nr-62-xvi-din-21-martie-2008-privind
- **Preserved original:** `raw/papers/bnm/legal/original/015__Nota tehnică - Indicele prețului imobilului rezidențial.pdf`
- **Original filename at BNM:** `Nota tehnică - Indicele prețului imobilului rezidențial.pdf`

## Extracted text

Indicele prețului imobilului rezidențial (RPPI) – nota tehnică 
1. Cadrul 
Indicele prețului  imobilului rezidențial (RPPI) reprezintă o măsură a evoluției prețului bunurilor imobile 
rezidențiale din Chișinău. Un indice fiabil al prețului bunurilor imobile este esențial pentru analiza evoluțiilor 
și riscurilor asociate pieței imobiliare, precum și pentru descrierea gradului de interconectare dintre piața 
imobiliară și a gradului de soliditate financiară. 
2. Acoperire 
Actualmente, acoperirea indicelui RPPI este limitată la mun. Chișinău. Totodată, indicele reflectă evoluțiile 
din cadrul pieței primare (bunuri imobile tranzacționate pentru prima dată) și pieței secundare (bunuri 
imobile deja existente pe piață). Subindicii pentru piața primară și piața secundară sunt agregați prin 
ponderarea în baza datelor privind numărul de tranzacții oferite de către Departamentul Cadastru al 
Agenției Servicii Publice. 
3. Surse de date 
Banca Națională a Moldovei colectează datele cu privire la ofertele de vânzare a bunurilor imobile de pe 
platformele largi de listare. Datele sunt obținute automat în baza algoritmului de „web scraping” atât 
pentru piața primară, cât și pentru piața secundară. Colectarea datelor se efectuează de două ori pe lună, 
iar datele pentru ponderile de agregare sunt oferite de către Departamentul Cadastru la finele fiecărui an. 
4. Periodicitatea 
Indicele RPPI este calculat cu periodicitate trimestrială, în baza datelor pentru bunurile imobile care au fost 
puse la vânzare pe parcursul trimestrului corespunzător. Ponderile de agregare sunt actualizate anual și 
reprezintă media numărului total de tranzacții pentru anul respectiv.  
5. Perioada de bază 
Indicele RPPI este de tipul Laspeyres cu efectuarea legăturii în lanț de la an la an, anul 2019 fiind anul de 
referință.  
6. Diseminarea 
Indicele RPPI agregat urmează a fi diseminat împreună cu subindicii aferenți pieței primare și pieței 
secundare. Publicarea indicelui RPPI se va efectua trimestrial, pe parcursul următorului trimestru după 
trimestrul de gestiune. 
7. Metodologia – aspectele conceptuale 
În vederea compilării indicelui RPPI de calitate fiabile, sunt necesare datele cu privire la principalele 
caracteristici ale bunurilor imobile. Totodată, similar altor indici de preț, este nevoie de asigurat 
comparabilitatea datelor pe parcursul seriei temporale. Pentru indicele RPPI, această condiționalitate este 
dificilă, întrucât compararea directă a mai multor bunuri imobile cere ca acestea să fie cel puțin similare, dar 
în condiții ideale – identice pe parcursul seriei temporale. În general, nu este cazul bunurilor imobile 
rezidențiale, unde fiecare unitate de imobil este tranzacționată în medie doar o dată la 5-10 ani. Din cauza 
frecvenței reduse a tranzacționării și a eterogenității bunurilor imobile rezidențiale, pentru includerea în 
calcul a fluctuațiilor prețului sunt necesare anumite tehnici de ajustare calitativă. Acest fapt presupune că 


 
 
cerințele de calitate față de indicele RPPI sunt înalte și sunt puternic influențate de gradul de detaliere a 
caracteristicilor bunurilor imobile incluse în calcul. 
8. Metodologia – Metoda hedonică bazată pe caracteristici 
Pentru a efectua ajustarea calitativă a tuturor caracteristicilor aferente bunurilor imobile de la trimestru la 
trimestru va fi aplicată Metoda de estimare hedonică bazată pe caracteristici. Metoda econometrică 
respectivă definește evoluția prețului bunului imobil „tipic”. Bunul imobil „tipic” se definește ca media 
caracteristicilor tuturor bunurilor imobile din fiecare strat (piața primară/secundară) pentru perioada de 
gestiune. Perioada de referință pentru anul curent este trimestrul patru al anului precedent. 
În vederea estimării indicelui se folosește specificația log-linear pentru fiecare substrat, iar regresia este 
estimată în fiecare trimestru folosind metoda celor mai mici pătrate (ordinary least squares). În acest sens, 
în model sunt inclus variabile precum suprafața totală a bunului imobile și numărul de camere. Ulterior se 
estimează un preț de referință (shadow price) pentru fiecare caracteristică în trimestrul curent și trimestrul 
de referință. Indicele prețului este calculat comparând  prețul unui bun imobil „tipic” din trimestrul curent 
cu prețul bunului imobil „tipic” din trimestrul de referință. 
Seria de timp pentru indicatorul RPPI agregat, precum și pentru toate substraturile menționate  se obține 
prin conectarea în lanț (chaining) a perioadei curente cu indicele înlănțuit din ultima perioadă a anului 
precedent. 
Ponderile pentru piața primară și respectiv piața secundară sunt actualizate anual și se bazează pe media 
numărului de tranzacții din ultimii trei ani în Chișinău pentru fiecare substrat. 
9. Metodologia – specificațiile matematice ale modelului hedonic 
Specificația log-linear pentru fiecare strat este următoarea: 
ln(𝑝𝑛𝑡) = 𝛽0
𝑡+ ∑𝛽𝑘
𝑡𝑧𝑛𝑘
𝑡+ 𝜀𝑛𝑡
𝐾
𝑘=1
 
unde 
 
ln(𝑝): logaritmul prețului; 
 
𝑡: perioada (trimestrul); 
 
𝑛: numărul de bunuri imobile în perioada t; 
 
𝛽0
𝑡: intercepta în perioada t; 
 
𝛽𝑘
𝑡: prețul de referință pentru caracteristica k în perioada t; 
 
𝑧𝑛𝑘
𝑡: valoarea caracteristicii k în perioada t pentru n bunuri imobile; 
 
𝑧𝑛𝑘
𝑡: eroarea aleatorie pentru prioada t și n bunuri imobile. 
 Ulterior se estimează regresii separate pe datele din perioada de referință (0) și perioada curentă (t) pentru 
fiecare strat în vederea estimării parametrilor (𝛽̂) pentru fiecare trimestru aferent stratului respectiv. Ca 
rezultat, în urma exponențierii rezultatelor, se obțin prețurile estimate ale bunurilor imobile pentru 
perioada de referință (0): 
𝑝̂𝑛0 = exp(𝛽̂0
0) exp [∑𝛽̂𝑘
0𝑧𝑛𝑘
0
𝐾
𝑘=1
] 


 
 
Similar pentru perioada curentă (t): 
𝑝̂𝑛𝑡= exp(𝛽̂0
𝑡)exp [∑𝛽̂𝑘
𝑡𝑧𝑛𝑘
𝑡
𝐾
𝑘=1
] 
Indicele este compilat prin compararea prețului estimat pentru bunul imobil „tipic” în perioada curentă (t) și 
perioada de referință (0). Bunul imobil „tipic” se definește ca media caracteristicilor tuturor bunurilor 
imobile pentru perioada de gestiune (𝑧̅𝑘
0). 
Valoarea medie a caracteristicii în cazul variabilelor numerice se estimează prin media simplă. În cazul 
variabilelor categorice (ex. „Tipul clădirii”, „Starea apartamentului”), în vederea estimării bunului imobil 
„tipic” (pentru fiecare variabilă) se calculează frecvența relativă pentru fiecare opțiune posibilă. Prin urmare, 
suma frecvențelor relative pentru fiecare variabilă categorică este egală cu 1. 
În continuare, indicele RPPI poate fi obținut în 2 moduri. 
Prima opțiune este raportul dintre prețul estimat în perioada curentă (t) și prețul estimat pentru perioada 
de referință (0), pentru imobilul „tipic” (𝑧̅𝑘
0)  din perioada de referință (metoda Laspeyres).  
𝐼𝑡=
exp(𝛽̂0
𝑡) exp[∑
𝛽̂𝑘
𝑡𝑧̅𝑘
0
𝐾
𝑘=1
]
exp (𝛽̂0
0) exp [∑
𝛽̂𝑘
0𝑧̅𝑘
0
𝐾
𝑘=1
]
 
Cea de a doua opțiune presupune compilarea indicelui prin exponențierea diferenței dintre coeficienții de 
regresie pentru perioada curentă (t) și perioada de referință (0). Pentru parametrii aferenți caracteristicilor 
bunurilor imobile (𝛽𝑘), diferența respectivă poate fi multiplicată cu caracteristicile bunului imobil „tipic” 
(𝑧̅𝑘
0). Rezultatele respective sunt sumate și exponențiate în vederea obținerii indicelui RPPI: 
𝐼𝑡= exp (𝛽̂0
𝑡−𝛽̂0
0) exp [∑(𝛽̂𝑘
𝑡−𝛽̂𝑘
0)𝑧̅𝑘
0
𝐾
𝑘=1
] 
10. Înlănțuirea indicelui 
Caracteristicile bunului imobil „tipic” (𝑧̅𝑘
0) sunt actualizate anual. Caracteristicile medii estimate pentru 
trimestrul patru al anului precedent celui de gestiune sunt utilizate pentru toate patru trimestre ale anului 
de gestiune. Astfel, trimestru patru joacă rolul elementului de legătură în lanț la estimarea seriei de timp 
îndelungate. Următorul tabel va exemplifica procedeul respectiv (cu utilizarea datelor fictive): 
Trimestru 
Indice calculat în baza 
bunului imobil „tipic” 
din 2018T4 
Indice calculat în baza 
bunului imobil „tipic” din 
2019T4 
Indice calculat în baza 
bunului imobil „tipic” din 
2020T4 
Indicele RPPI înlănțuit 
(2019=100) 
2019T1 
100.5 
 
 
97.9 = (100.5/102.7)*100 
2019T2 
101.5 
 
 
98.9 = (100.5/102.7)*100 
2019T3 
105.4 
 
 
102.7 = (105.4/102.7)*100 
2019T4 
103.2 
100.0 
 
100.5 = (103.2/102.7)*100 


 
 
2020T1 
 
99.1 
 
99.6 = 99.1 * (100.5/100)  
2020T2 
 
99.5 
 
100.0  = 99.5 * (100.5/100) 
2020T3 
 
101.2 
 
101.7 = 101.2 * (100.5/100) 
2020T4 
 
100.8 
100.0 
101.3 = 100.8 * (100.5/100) 
2021T1 
 
 
100.4 
101.7 = 100.4 * (101.3/100) 
2021T2 
 
 
100.8 
102.2 = 100.8 * (101.3/100) 
2021T3 
 
 
99.8 
101.1 = 99.8 * (101.3/100) 
2021T4 
 
 
100.5 
101.8 = 100.5 * (101.3/100)
