# Manifest §12 — What Needs Polish

- **Track:** warcode_tactical_doctrine
- **Retrieval date:** 2026-08-23
- **Citation legend:** see `00_what_this_is_not.md`
- **Framing for the review:** this is a **beta**. Findings below are offered as free QA, not as a verdict. Every item is reproducible from the public PDF.
- **Marketing tension to name:** the studio states "the rules are tight… the edge cases have been found and resolved" `[PL §04]`. The list below is the direct rebuttal. Say it once, without heat.

## A. Rules gaps (need a ruling, not a rewrite)

| # | Finding | Where | Confidence |
|---|---------|-------|-----------|
| A1 | **Round count is never stated.** The sequence says "if this was the final round… determine the winner", deferring to the scenario — and the beta scenario never gives a number. A reader cannot learn how long a game is from the rulebook. Marketing says 4. | `[RB pp.3, 26]` | verified |
| A2 | **Friendly fire is referenced but never resolved.** The rules say friendly fire "will not occur if 50% of the Target's base is in direct line of sight" — implying it *does* occur below that, with no procedure given for who is hit or how. | `[RB p.12]` | verified |
| A3 | **No global tie rule.** "The player with the most VP wins" is silent on equal VP. The only tie handling anywhere is one scenario's mutual destruction. | `[RB pp.4, 26]` | verified |
| A4 | **Contract accumulation unspecified.** The trigger is a gap of 1+ VP at the end of *any* round, so it fires most rounds — but nothing says whether unfulfilled contracts stack, cap, or replace. | `[RB p.22]` | verified |
| A5 | **Re-roll scope in melee is one-sided.** The attacker may re-roll the hit check before the defender blocks. Nothing says whether the **defender may re-roll its block dice**, which is the obvious next question at the table. | `[RB p.23]` | verified |
| A6 | **Penetration and damage share the same dice, but only in an example.** The worked example determines armour penetration and then reads damage off the *same* two dice. The rules chapters describe them as separate checks and never state the reuse. This also silently makes a penetration re-roll a damage re-roll. | `[RB pp.9, 10, 20]` | verified |
| A7 | **Do free grenades cost equipment points?** Two units "start the game with 2 grenades and cannot take other equipment". Unstated whether that consumes any of the squad's 4 equipment points. | `[RB pp.16, 33, 35]` | verified |
| A8 | **"Melee radius, which is usually 1 inch"** — "usually" implies exceptions, and no published unit provides one. Either state it as always 1" plus per-weapon overrides, or list the exception. | `[RB p.15]` | verified |
| A9 | **Overwatch's true cost is misstated.** It is priced at 1 AP, but "the unit cannot take any other action for the rest of the round" — so it consumes the whole 2 AP activation. Either say it ends the activation, or let the spare AP be used. | `[RB p.10]` | verified |
| A10 | **Event card scope undefined.** The round sequence lists "activation of scenario event cards"; the only concrete example is the scenario's own deck. Whether a general event deck exists is unclear — and marketing implies one. | `[RB pp.3, 26]` `[PL §01]` | verified |

## B. Reportable bugs (defects, not design questions)

These are the items worth sending to RedMakers verbatim via the VIP channel.

| # | Bug | Repro | Severity | Confidence |
|---|-----|-------|----------|-----------|
| **B1** | **Movement fallback hardcodes 4" and 5".** The rule for placing a model when movement ends beyond a friendly unit or partial cover is written in literal inches ("within 4 or 5 inches"). Those numbers are the 6" standard speed minus the 2" friendly and 1" cover penalties. They are **wrong for Slow (5") and Fast (7")** units, both of which exist in the published rosters. Should read "reduced Movement Range". | `[RB p.7]` vs speeds on `[RB p.6]` and rosters `[RB pp.33–36]` | **High** — affects every game | verified |
| **B2** | **Duplicated paragraph.** Page 12 prints the same partial-cover example paragraph twice, word for word ("…Unit 1 is within 1 inch of piece 1, so piece 1 does not interfere… however, piece 2 does interfere and grants an agility bonus to Target."). | `[RB p.12]` | Low — cosmetic | verified |
| **B3** | **Inconsistent 50% boundary language.** Full cover and friendly-fire use "**at least** 50% / at least 14mm"; partial cover uses "**more than** half / more than 14mm". At exactly 14mm on a 28mm base the three rules disagree. | `[RB pp.8, 11, 12]` | Medium — edge case, but a common one | verified |
| **B4** | **Possible statline inconsistency — Smasher's sidearm.** Smasher's sidearm appears one step above the standard sidearm profile in the weapons chapter on both normal and critical damage, with no ability text and no other unit sharing the variant. Either an intentional unique that needs labelling, or a copy error. | `[RB pp.7, 34]` | Medium — balance-relevant | draft |
| **B5** | **Typo:** "armor penetratsion" in the melee example's weapon-ability line. | `[RB p.21]` | Low | verified |
| **B6** | **Glyph collision: capital O used for zero.** Armour-penetration values of zero are set as the letter "O", and page folios render 10/20/30 as "1O"/"2O"/"3O". On a datasheet where "0" is a meaningful modifier, this is a real legibility risk in print and it breaks text search and copy-paste. | `[RB pp.13, 11, 21, 31]` | Medium — print and accessibility | verified |
| **B7** | **Contents page stops halfway.** The table of contents ends at Contracts / Re-roll, listing nothing for the scenario, the random VP placement system, the Protocol Cards, or the two team lists — roughly a third of the book. | `[RB p.2]` vs `[RB pp.25–36]` | Medium — usability | verified |
| **B8** | **Contract deck cannot be built.** Contract cards name "one unit name from each available faction", but only two of four factions have published unit names. Any printed contract deck is half-unusable until MDR and Dominium ship. | `[RB p.22]`, rosters `[RB pp.33–36]` | High — blocks a core subsystem | verified |
| **B9** | **Card pages are flattened images.** Contract pages and all five Protocol Card pages carry no extractable text. They are unreadable to screen readers, unsearchable, and untranslatable, and they force OCR on anyone building reference material. | `[RB pp.23–24, 28–32]` | Medium — accessibility | verified |

## C. Design concerns (working as written; worth questioning)

- **Contracts fire on a 1 VP gap**, i.e. nearly every round. Combined with re-roll income from your own casualties, the losing player receives two compounding subsidies. Whether that keeps games close or blunts good play is a playtest question. `[RB pp.22, 23]` — confidence: draft
- **A 2 AP budget in a 4-round game leaves very few decisions** — roughly 64 activations per side across the whole game, minus deaths. This sits awkwardly against Dominium being marketed as rewarding planning "several activations ahead". `[RB p.4]` `[PL §02]` — confidence: draft
- **Medkit at 0 AP versus grenade at 1 AP** makes healing strictly better on tempo for the same equipment cost. `[RB pp.16, 18]` — confidence: draft
- **The agility cap of 5 makes at least one published unit immune to cover and screening bonuses entirely.** Elegant if intended, invisible if not — it is never called out. `[RB pp.11, 12, 36]` — confidence: draft
- **Heavy weapons cost 2 AP to fire on a 2 AP unit**, so a heavy platform can only ever shoot or move, never both. Deliberate-looking, but it makes those units nearly static and the rulebook never says so. `[RB pp.7, 34, 36]` — confidence: draft
- **Faction identity rests almost entirely on statlines.** Unless Protocol Cards carry more weight than expected, the differentiation layer is thin. See `06_faction_concepts.md`. — confidence: draft

## D. Documentation and production polish

- **Diagram-heavy layout does not survive text extraction**, so the PDF is poor as a searchable reference even where text exists — profile values extract as bare number runs with no labels. `[RB pp.7, 33–36]` — confidence: verified
- **No index, no quick-reference sheet, no one-page turn sequence** in the book as read. For a game selling itself on "twenty minutes to read the rules", a single-page player aid is the highest-value missing asset. — confidence: verified (absence)
- **No credits page** in the extract, so the marketing team roster cannot be cross-checked against the document. `[RB pp.1–37]` — confidence: verified (absence)
- **No version/date stamp visible in the extracted text** — the version lives in the filename only. A printed version line would help beta feedback triage enormously. — confidence: draft

## Recommended handling in the review

1. Lead §12 with the beta framing and the free-QA intent.
2. Present **B1** and **B8** as the two findings that most deserve a fix before launch.
3. Present section A as questions to the designers, not errors.
4. Offer to re-run this pass against the next free beta.

## Open questions

- Has any of this already been fixed in a beta newer than V.0.8.7-F?
- Is there a VIP-facing bug-report channel (Discord thread, form) that these should be filed through rather than the Facebook group?
