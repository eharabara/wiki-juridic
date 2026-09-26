---
copy_of: legal-career/06-matter-log.md
master: claude.ai project "Legal Wiki"
taken: '2026-09-26'
stamped: '2026-09-26'
sha256_body: a49a2ebd75310fa7b77dc2776e8e88f5b479d1cde528a4ed0ab0aef7f65b27d5
local_notes: false
refresh: every-session
---
> **Copy.** Taken 2026-09-21 from the claude.ai project "Legal Wiki", document `legal-career/06-matter-log.md`.
> The project holds the master, and new matters are logged there, not here.
> This copy exists so that work done in this folder can see what positions already stand.

# 06. Matter log

Status: active. Append only, except for corrections.

The register of substantive legal work done in this project. Its purpose is narrow and practical: so that a position taken once does not have to be re-argued from scratch, and so that a position later found wrong is visibly corrected rather than quietly forgotten.

## Entry format

Copy this block for each new matter.

```
### M-000 | Short title
Date:
Persona:
Question:
Position:
Sources relied on:
Confidence: anchored / partially anchored / not anchored
Open points:
Status: live / settled / superseded
```

Notes on the fields:

- **Position.** The conclusion in two or three sentences. Not the reasoning, which lives in the conversation. This log is an index, not an archive.
- **Sources relied on.** Article-level, per document 03.
- **Confidence.** Carried over from the answer. An entry with no confidence state is incomplete.
- **Open points.** What was not resolved, and what fact or verification would resolve it.
- **Status.** A matter becomes *settled* when the position has been used externally without challenge. It becomes *superseded* when a later matter reverses it, and the reversing entry is named.

## Correction rule

When a position is reversed, the original entry is not deleted. Its status changes to superseded, a line is added naming the entry that replaced it, and the new entry states why the earlier reading was wrong. Reversals carry more information than clean records, because they show which parts of the analysis were fragile.

## Prior work carried into this project

Recorded for continuity. These were done before the project was set up and are listed without full entries.

- Cross-border loan structure, Italian-resident lender to Moldovan-resident borrower. Legal memo covering Moldova's foreign exchange framework, BNM notification requirements, AML obligations, and tax treatment. Relevant to persona P5.
- CNPF perimeter findings on mandate boundaries, transposition gaps, and acquis alignment, produced during the wiki build. Relevant to persona P2 and recorded in document 05.

## Matters

### M-001 | Bank shareholder: access to shareholder list and AGA materials, estate administrator, deadline to contest AGA decisions
Date: 2026-09-04
Persona: P1 Corporate Legal Specialist
Question: Five questions from a client holding shares in a Moldovan bank. (1) Right to a copy of the shareholder list before the AGA. (2) Remedies if the bank refuses. (3) Access to materials and lists of past AGAs, and any deadline. (4) Whether heirs can instruct an administrator of the estate (administrator al masei succesorale) holding the bank shares. (5) Deadline to contest an AGA decision of a bank.
Position: Law 202/2017 art. 36(1)-(2) applies the JSC law to banks except the listed articles; art. 21, 55, 58 and 91 of Law 1134/1997 are not excluded. (1) Consultation of the list yes (art. 21(1)(b), 55(1), 55(2)(a)), copy no (art. 55(1) final sentence, 55(7)); bank overlay art. 54 Law 202/2017 (BNM opinion, 7 days, no change in last 3 days). (2) Refusal of a copy is lawful; refusal of consultation breaches art. 55; remedies: written request (art. 26(3)), CNPF and BNM, court action, and as cumulative ground to contest the decision (art. 58(5)(f) JSC law; art. 202(2)(c) Civil Code). (3) Past materials accessible under art. 91(1), within 5 working days, against cost-based payment, last 5 financial years (art. 91(3)); lists of past AGAs expressly excluded (art. 91(1)(e)); only via court as evidence. (4) Heirs have no power of instruction: administration ordered by the notary (art. 2436), heirs' right to administer and dispose suspended (art. 2439(1)), administrator acts in the interest of creditors and heirs with power of disposal (art. 2440(1)); heirs keep reporting, transfer, liability and revocation rights (art. 2441, 2440(2), 2443(2)). Bank overlay: qualifying holding (1%, art. 3) acquired by succession needs BNM prior approval; rights suspended by law until approval (art. 46(1)-(2) Law 202/2017). (5) No special deadline in Law 202/2017 (full text checked). Grounds art. 58(5) JSC law; relative nullity 6 months (art. 202(5) Civil Code) running from knowledge of the ground (art. 395(5)); absolute nullity imprescriptible (art. 328(3)); standing limited by art. 202(4) and art. 58(6) JSC law.
Sources relied on: Law 1134/1997 art. 21(1)(b)-(c), 26(2)-(3), 52(2), 55(1)-(3), 55(7), 56(3), 58(5)-(6), 91(1)-(3) (wiki, L-1134-1997, consolidation 2028-01-01, art. 73^3 and 73^4 not yet in force and not used). Law 202/2017 art. 3, 36(1)-(2), 45, 46, 52, 54, 144 (legis.md doc_id 146910, consolidation LP314/2024 in force 28.02.2025, outside wiki). Civil Code art. 202, 328(3), 395(5), 2412-2417, 2430(1), 2436-2443 (wiki, CC-1107-2002, text with LP251/2025 in force 01.04.2026). Contravention Code art. 302(1) and (3) (legis.md doc_id 132411, consolidation 2022, outside wiki).
Confidence: partially anchored. Anchored for the JSC law and the Civil Code; Law 202/2017 read from legis.md outside the wiki; Contravention Code and Insolvency Law not anchored.
Open points: (a) current version of art. 302 Contravention Code and which authority (CNPF or BNM) ascertains it for banks; (b) BNM regulation on holdings in bank capital: whether succession is an "objective circumstance" under art. 46(1) Law 202/2017. Closed 2026-09-08 by M-002: yes, Regulation 127/2013 point 8 lists succession, inheritance and donation; (c) art. 74, 77, 83, 92, 93 of Insolvency Law 149/2012 applied to the estate administrator by art. 2439(1) Civil Code, possibly a removal mechanism; (d) whether a heir who requested the administration can ask the notary to end it (Civil Code silent); (e) the client's facts were not available: whether the client is heir or administrator, and the size of the holding.
Deliverable: 2026-09-04-raspuns-scurt-drepturi-actionar-banca.md (short answer in Romanian, delivered in session).
Status: live

### M-002 | Bank shareholder: heir holding only a certificat de calitate de moștenitor, participation and vote at the AGA
Date: 2026-09-08
Persona: P1 Corporate Legal Specialist (banking overlay of Law 202/2017 applied inside it)
Question: The deceased held 10% of a bank. The heir has accepted the inheritance and holds only a certificat de calitate de moștenitor, not yet the certificat de moștenitor. Can the heir participate and vote at the AGA?
Position: No, at three independent levels. (1) Civil law: the certificat de calitate legitimises the heir towards third parties but does not produce the effects of the certificat de moștenitor (art. 2548(3) Civil Code); the heir cannot dispose of the estate until the certificate is received (art. 2390(7)); with co-heirs the estate stays in indiviziune until then (art. 2486(1)). Acceptance retroacts to death (art. 2389(2), 2165), but that does not reach the AGA. (2) Corporate and securities law: ownership of shares registered at the Depozitarul central unic arises on registration in the account (art. 11(5) Law 171/2012); the AGA list of a bank may include only persons who had shareholder status at the reference date (art. 54(1^1) Law 202/2017; art. 20(1), 52(2), 56(1) Law 1134/1997) and is invalid without BNM's written opinion (art. 54(5)). Until re-registration the registered holder is the deceased and nobody votes those shares; re-registration needs the certificat de moștenitor. (3) Banking law: 10% is a deținere calificată (threshold 1%, art. 3 Law 202/2017); inheritance is an "objective circumstance" (BNM Regulation 127/2013 point 8, under art. 46(1)), so no prior approval is needed to acquire, but voting, convening, agenda, candidate and dividend rights are suspended by law from acquisition until BNM approval (art. 46(1)); shares count for quorum, not for decisions (art. 45(3)). Deadlines: inform BNM within 15 days, apply within 60 days (art. 46(2)); otherwise forced sale within 3 months (art. 46(4)), extendable (art. 52(6)), then cancellation and new issue (art. 52^1(2)). Advice: run the notarial procedure and the BNM approval in parallel; the heir may apply as achizitor potențial before DCU registration, an approval being valid at least 3 months (art. 47(9)). Counter-argument (heir is owner from death, art. 56(3) JSC law limits proof of status to identification) rejected as weak: defeated by art. 11(5) Law 171/2012 and art. 54(1^1) Law 202/2017, and in any event by the art. 46(1) suspension.
Addendum 2026-09-08 (art. 2492 Civil Code, what the heir can do): correction, the custode is not available after acceptance, custody ordered under art. 2412(1)(c) ends by law on acceptance (art. 2492(1) second sentence). Refined position: on the civil reading the heir is owner from death without registration (art. 425(1)) and administrator by law of the estate (art. 2492(1)); conservation acts alone, administration by majority of quotas (art. 1947(1)), disposal jointly (art. 2494(1)) and blocked until registration (art. 425(3)) and, for the heir in possession, until the certificate (art. 2390(7)). Vote stays suspended; attendance and information rights are defensible via art. 425(1), 2492, 2548(3) and art. 56(3) JSC law. BNM does not expressly require the certificat de moștenitor: Law 202/2017 art. 45(6) defers registration procedure to BNM acts; Regulation 127/2013 asks only for the concerted-action declaration; Regulation 130/2013 point 12 defers transfer documents to CNPF acts and point 14 provides that shares acquired under art. 46 (objective circumstances) are registered without BNM prior approval (current text quoted by the bank on 2026-09-09; 2016 consolidation read on legis.md). The certificate requirement comes from the Civil Code (art. 2542(1), 2390(7), 425(3)) and the DCU rules.
Addendum 2026-09-09 (art. 77(8)(c) Law 1134/1997 event occurred; adversarial review; bank's argument): art. 77 applies to banks (art. 36(2) Law 202/2017 does not exclude it); the buyback right is not among the rights suspended by art. 46(1); with a decision taken while the deceased was registered, the right arose in his patrimony (art. 77(11)) and passed by succession (art. 2162(3)); the heir may file the request within 3 months of the contract taking effect (art. 77(10), (11^2)) as a conservation act (art. 2492(1)), signed by the sole heir or by all co-heirs, but cannot execute the sale before certificate and registration; the estate administrator route (art. 2436, 2440(1)) is plausible but untested against art. 425(3) and DCU rules; the bank needs BNM approval to reduce own funds (art. 62 Law 202/2017). Corrections from the review: the ban in art. 52(4) Law 202/2017 attaches to art. 45(2) and 52(1) measures, not to the art. 46(4) route (error removed); art. 425 applies to DCU accounts only through art. 413(2)(i) and yields to special law under art. 413(3), so the civil reading is presented as a reading; art. 2390(7) literally covers the heir in possession; sole-heir and co-heir hypotheses separated; the concerted-action presumption sits in the art. 3 definition, art. 45(5) only lets BNM presume from its findings; "acționar minoritar" is undefined. Fiscal consequence added: inheritance non-taxable for RM citizens (Fiscal Code art. 20(i)); basis is market value at acquisition (art. 42(1)(d)); gain per art. 40(1), 50% included (art. 40(7)), 12% (art. 15(a)); document the market value at the date of death now. Bank's argument (Reg. 130/2013 point 14, Reg. 127/2013 point 9: no holding yet, clocks run from registration on the certificate) accepted on procedure, rejected where it denies civil acquisition or rights born before death: the securities reading of "data dobândirii" is the operative one, the 60-day risk is small, urgency moves to the certificate and the art. 77 term; early BNM application kept as a voting strategy (approval before registration means the art. 46(1) suspension never starts).
Sources relied on: Civil Code art. 202(5), 395(5) (carried from M-001, not re-read), 413, 425, 1945-1950, 2162, 2163, 2165, 2389, 2390, 2391, 2412-2414, 2436-2440, 2486-2494, 2498, 2499, 2505, 2542, 2548, 2549 (wiki, CC-1107-2002, text with LP251/2025 in force 01.04.2026). Law 1134/1997 art. 20, 21, 22, 26, 36, 52, 55, 56, 57, 77, 81, 82 (wiki, L-1134-1997; deferred art. 73^3 and 73^4 not used). Law 202/2017 art. 3, 36, 45-48, 51, 52, 52^1, 54, 62 (wiki, L-202-2017 Romanian, consolidation 25.10.2025). Law 171/2012 art. 10(2)(g), 11(5) (wiki; deferred repeal of art. 38 and 141^1 not used). Law 234/2016 transitional provisions (4)(a) and (7) (wiki). Fiscal Code art. 15, 17, 20, 40, 42 (wiki, COD-1163-1997, consolidation 01.07.2026; deferred provisions do not touch these articles). BNM Regulation 127/2013 points 8 and 9 (wiki, English translation, raw/papers/bnm/legal/documents/094, markers to 2021; point 9 Romanian text quoted by the bank). BNM Regulation 130/2013 points 12-15 (legis.md doc_id 92112, 2016 consolidation, outside wiki; point 14 current text quoted by the bank, to confirm on bnm.md). BNM Regulation 29 on CMEOV, annex (wiki, English translation).
Confidence: partially anchored. Anchored for the Civil Code, Law 1134/1997, Law 202/2017, Law 171/2012, Law 234/2016 and the Fiscal Code. Not anchored: Regulation 127/2013 points 8-9 and Regulation 130/2013 points 12-15 (translation and outside-wiki consolidations), DCU rules on succession, BNM practice on the art. 46(2) start date, transmission of the art. 77(11) right and the conservation qualification of the request (reasoning on text), regime of dividends declared after death.
Open points: (a) current Romanian text of Regulation 127/2013 point 8 and Regulation 130/2013 point 14 on bnm.md; (b) DCU rules on transfer by succession, whether a certificat de calitate is accepted for any operation, and whether the DCU executes on an estate administrator's instruction; (c) BNM practice on the start date of the art. 46(2) clocks (bank says registration); (d) with co-heirs, single representative (art. 20(2) Law 1134/1997) and the art. 3 concerted-action presumption; (e) facts: date the contract took effect, date of the decision, date of death, sole heir or co-heirs, citizenship of the heir; (f) whether dividends declared after death are paid after BNM approval; (g) whether "acționar minoritar" in art. 77(8) is read by the bank as including a 10% holder.
Closes: M-001 open point (b).
Deliverable: 2026-09-09-pozitia-mostenitorului-certificat-de-calitate.md (working note in Romanian, project folder legal-career, revised twice on 2026-09-09).
Status: live
