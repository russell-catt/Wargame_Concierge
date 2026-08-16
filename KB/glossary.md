---
title: Glossary
type: glossary
system: warhammer_40k_11e
created: 2026-08-16
updated: 2026-08-16
sources: [necron_lists_owner_notes, source_library, local_library_pointers, docs/Game_System_Scaffold.md]
confidence: draft
tags: [terminology, glossary, keywords, warhammer_40k, necrons, space_marines]
---

# Glossary

The single home for **Keyword** entries and every game term this KB uses. Check here before using a rules term anywhere else. Updated on every ingest that introduces or refines terminology.

Keywords do **not** get their own pages - see [`AGENTS.md`](../AGENTS.md) Sec 5 for the rule and the three-part test that promotes a term into `KB/concepts/`. Promoted terms keep a short entry here pointing at their page, so this stays the one lookup surface.

---

## Read this first

**Status after L1 (2026-08-16).** The L0 seed of four terms has been expanded to 32 from the first real ingest. Each is sorted by what actually backs it.

**Game terms (26):**

| Status | Meaning | Count |
|--------|---------|-------|
| `verified` | Cross-checked against a rules source; retrieval date recorded | **0** |
| `draft` | Named by a source that was read; effect not cross-checked | 13 |
| `unverified` | Written from familiarity or a prior edition. **Confirm before use** | 12 |
| `unresolved` | Appeared in a source and maps to nothing recognised | 1 |

**Project vocabulary (6):** all `verified` - these describe this project's own conventions, not the game, so they can be confirmed from the repo itself.

**No game term is `verified`, because no rules document has been read yet.** The owned core rules, both faction packs, and the points manuals are all catalogued and all unopened - see [[local_library_pointers]]. Until they are read, this page tells you the right words to use, not the right rules.

S3 owns the shipping `games/warhammer_40k_11e/rules/Keyword_Glossary.md` and draws from this page. See [[inherited_docs_for_S3]] for what is safe to promote.

---

## Entry format

**Term** *(canonical form)* - `status`
: Definition in plain language. Why a player cares. What is not yet confirmed.
- Faction / scope: where the term applies
- Verify against: where to check it
- See also: `[[related_page]]` *(illustrative - backticked so link lint does not read it as a real target)*

---

## Core rules and scoring

**Objective Control** *(OC)* - `unverified`
: A characteristic on a model's profile representing how strongly it holds ground. Players total the OC of their eligible models within range of an objective marker; the higher total controls it. It is why a cheap, numerous unit can hold ground an elite unit cannot, and why the game is won by positioning rather than kill count.
- Faction / scope: core rules, system-wide
- Verify against: `raw/pointers/rules_core.md` - objective control and scoring
- See also: **[[objective_control]]** - promoted to a concept page in L1

**Objective marker** - `unverified`
: The physical marker on the table whose control is scored. Control is decided by totalling Objective Control within range of it, and can flip as models move, die, or arrive.
- Faction / scope: core rules
- Verify against: `raw/pointers/rules_core.md`

**No Man's Land** - `unverified`
: The contested middle of the table, outside either deployment zone. Named in the owner's Necron notes as the ground [[canoptek_court]] wants to open up for its detachment rule.
- Faction / scope: core rules / deployment
- Verify against: `raw/pointers/rules_core.md`; terrain and deployment work in S3

**Battle round** - `unverified`
: One full cycle in which both players take a turn. Sequencing matters for any rule that triggers "at the start of" or "at the end of" something - notably [[reanimation_protocols]].
- Faction / scope: core rules
- Verify against: `raw/pointers/rules_core.md`

**Datasheet** - `draft`
: The rules entry for one unit: profile, weapons, abilities, keywords. This project's generic term for it is "unit entry" (`docs/Game_System_Scaffold.md` vocabulary mapping). Datasheet text is **never reproduced** in this repo - see [`AGENTS.md`](../AGENTS.md) Sec 10.
- Faction / scope: system-wide
- Verify against: faction pack pointers; [[wahapedia]] for lookup

**Detachment** - `draft`
: The rules package a list is built under, sitting between "army" and "unit". It supplies a **detachment rule**, plus enhancements and stratagems. Choosing one is the first real list-building decision, and it determines which units the army wants.
- Faction / scope: system-wide
- Verify against: `raw/pointers/rules_core.md`
- See also: [[canoptek_court]], [[cryptek_conclave]], [[gladius_task_force]]

**Detachment rule** - `draft`
: The army-wide ability granted by the chosen detachment - [[power_matrix]] for [[canoptek_court]], Scientific Schemes for [[cryptek_conclave]]. Distinct from the **army rule**, which applies regardless of detachment.
- Faction / scope: system-wide

**Army rule** - `draft`
: The faction-wide ability every list of that faction has, independent of detachment: [[reanimation_protocols]] for Necrons, [[oath_of_moment]] for Space Marines.
- Faction / scope: system-wide

**Battleline** - `draft`
: The role keyword for a faction's core infantry - Necron Warriors and Immortals in this collection. Detachments built on massed infantry, such as [[cryptek_conclave]], are described as feeding off battleline units.
- Faction / scope: system-wide
- Verify against: `raw/pointers/faction_pack_necrons.md`

**Leader / attached unit** - `unverified`
: A character joining a squad and fighting as part of it, conferring abilities on the whole unit. The owner's notes assume this throughout - a Plasmancer leading Immortals, Szeras behind a Warrior block.
- Faction / scope: core rules
- Verify against: `raw/pointers/rules_core.md`; the attachment rules changed between editions

**Points** *(pts)* - `draft`
: The cost of a unit, used to build lists to an agreed size. Values live in the Munitorum Field Manual and **move when a balance dataslate lands** - which is why every points figure in [[necron_lists_owner_notes]] needs re-checking.
- Faction / scope: system-wide
- Verify against: `raw/pointers/points_manuals.md`

**Armour Penetration** *(AP)* - `unverified`
: How much an attack degrades the target's save. Referenced in the owner's notes as an aura effect from Illuminor Szeras.
- Faction / scope: core rules
- Verify against: `raw/pointers/rules_core.md`

**Critical hit** - `unverified`
: An attack roll good enough to trigger additional effects. Named in the owner's notes as something a Plasmancer improves for the unit it leads.
- Faction / scope: core rules
- Verify against: `raw/pointers/rules_core.md`

**Ignores Cover** - `unverified`
: An ability that strips the defensive benefit a target would get from terrain. Written as `[IGNORES COVER]` in the owner's notes, which is the datasheet convention for a named ability.
- Faction / scope: core rules keyword
- Verify against: `raw/pointers/rules_core.md`

---

## Necrons

**Reanimation Protocols** - `unverified`
: The Necron army rule. Units recover during the game, returning destroyed models or restoring lost wounds. The strategic consequence - damage that does not finish a unit is often wasted - holds across editions even though the wording has not.
- Faction / scope: Necrons, army rule
- Verify against: `raw/pointers/faction_pack_necrons.md`
- See also: **[[reanimation_protocols]]** - promoted to a concept page in L1

**Power Matrix** - `draft` · **corrected in L1**
: The **[[canoptek_court]] detachment rule in Warhammer 40,000**. Units re-roll hit rolls while in territory the Necron player controls, which couples the army's accuracy to its map control.
: **The L0 entry was wrong and is superseded.** It warned that this might be a *Kill Team* term because the owner's Hierotek Circle is a Kill Team box. Two independent in-repo sources - `raw/Necron_Lists.md` and `docs/Game_System_Scaffold.md` - name it as a 40K detachment rule. The system attribution is **resolved**; the rule's exact wording is not.
- Faction / scope: Necrons, [[canoptek_court]] detachment rule - **Warhammer 40,000, not Kill Team**
- Verify against: `raw/pointers/faction_pack_necrons.md`, then [[wahapedia]]
- See also: **[[power_matrix]]** - promoted to a concept page in L1, with the full correction

**Scientific Schemes** - `draft`
: The [[cryptek_conclave]] detachment rule. Described in the owner's notes as stacking ranged profile buffs together with reanimation multipliers, producing a defensive army that wins by attrition. Name reliable, effect unverified.
- Faction / scope: Necrons, detachment rule
- Verify against: `raw/pointers/faction_pack_necrons.md`

**Canoptek** - `draft`
: The Necron robotic-construct family: Scarab Swarms, Wraiths, Doomstalkers, and others. The theme [[canoptek_court]] is built around.
- Faction / scope: Necrons, keyword

**Cryptek** - `draft`
: The Necron engineer-character family - Plasmancer, Technomancer, Geomancer, and others. The theme [[cryptek_conclave]] is built around, and the likely content of the owned Hierotek Circle set.
- Faction / scope: Necrons, keyword

**Hierotek Circle** - `draft`
: A **Kill Team** boxed set of Necron Crypteks and attendants. The owner has one, used and fully painted, and it is currently the only game-ready part of the collection. **Its 40K datasheet mapping is unknown** and pending photographs.
: It is a set of models, not a rules term. L0 mistakenly treated it as evidence about [[power_matrix]]; it is not evidence about any 40K rule.
- Faction / scope: Necrons, models - **Kill Team product, usable as 40K models once identified**
- See also: [[necrons]]

**Kill Team: Tomb World** - `draft` · **not owned**
: A different Kill Team box, assumed in an earlier version of the owner's blueprint and since **confirmed not owned**. Its lists survive as historical path notes only. Do not let them drive shopping or teaching content.
- Faction / scope: Necrons, models - historical only
- See also: the deprecated list below

---

## Space Marines

**Oath of Moment** - `unverified`
: The Space Marine army rule. Each turn the player nominates one enemy unit and the army attacks it better. It concentrates output onto a single target, which makes target priority the defining Space Marine decision.
- Faction / scope: Space Marines, army rule
- Verify against: `raw/pointers/faction_pack_space_marines.md`
- See also: **[[oath_of_moment]]** - promoted to a concept page in L1

**Gladius Task Force** - `unverified`
: The generalist Space Marine detachment, chosen as the son's learning detachment because it asks least of a list built from unaudited older kits. Nothing about its rule is known.
- Faction / scope: Space Marines, detachment
- Verify against: `raw/pointers/faction_pack_space_marines.md`
- See also: [[gladius_task_force]]

**Firstborn / legacy datasheets** - `unverified`
: The older generation of Space Marine models, as distinct from Primaris. Explicitly in scope for this project because the son's army is built from existing old kits. Whether every such datasheet is still supported in 11th Edition is unknown and matters directly.
- Faction / scope: Space Marines
- Verify against: `raw/pointers/faction_pack_space_marines.md`

---

## Other game systems

**Kill Team** - `draft`
: A **separate Games Workshop game**, not a mode of Warhammer 40,000. Small squads, different rules, different points.
: It earns a glossary entry because conflating it with 40K already caused one error in this KB - see the Power Matrix entry above. Kill Team *models* can be used in 40K once matched to a datasheet; Kill Team *rules terms* have no standing in 40K content. **Keep the box and the ruleset separate.**
- Faction / scope: outside this KB's scope, except as a source of models

---

## Project vocabulary

Not game terms - the words this project uses about its own state. S3 should keep them consistent in shipping content.

**Game-ready** - `verified`
: Assembled, painted or at least based, and fieldable today. Currently true of exactly one thing: the Hierotek Circle set.

**Build before play** - `verified`
: Purchased but unassembled. Excluded from any "play this weekend" advice. Currently: 10 Warriors, 3 Scarab Swarms, 5 Immortals.

**Pointer stub** - `verified`
: A markdown file in `raw/pointers/` recording the local path to an owned PDF and what it contains. The sanctioned substitute for a binary this repo may not hold. See [[local_library_pointers]].

**Teaching paraphrase** - `verified`
: Explaining how a rule works in our own words, with the reasoning a player needs. The only way rules content is written here. Never a transcription. See [`AGENTS.md`](../AGENTS.md) Sec 10.

**Retrieval date** - `verified`
: The date a living reference was read, recorded on every claim drawn from one. A rules claim without one is a lint finding, because [[warhammer_community]] can invalidate an owned PDF overnight.

**Confidence** - `verified`
: The mandatory frontmatter field carrying how much a page can be trusted: `verified`, `draft`, `stub`, `unverified`. It is the KB's trust model; inflating it breaks it.

---

## Unresolved terms

**Data Package Detachment** - `unresolved`
: Appears in [[necron_lists_owner_notes]] as a tier label - "3 Data Package Detachment" for [[canoptek_court]], "2 Data Package Detachment" for [[cryptek_conclave]]. It does not map onto any Warhammer 40,000 term this KB recognises.
: Possibly community shorthand, possibly a competitive-scene rating, possibly a drafting artifact. **Do not propagate it into shipping content** until someone can say what it means. Recorded rather than deleted, because the underlying judgement - that one detachment is stronger than the other - is worth keeping.
- Faction / scope: unknown
- Verify against: ask the owner; failing that, treat as non-standard and drop

---

## Verification queue

What has to be read to clear this page. Everything here is blocked on a document the owner already has.

| Term(s) | Blocked on | Target slice |
|---------|-----------|--------------|
| Objective Control, objective marker, battle round, No Man's Land, AP, critical hit, Ignores Cover, leader/attached | `raw/pointers/rules_core.md` | **S3** |
| Detachment, detachment rule, army rule, datasheet, battleline | `raw/pointers/rules_core.md` | **S3** |
| Reanimation Protocols, Power Matrix wording, Scientific Schemes, Canoptek, Cryptek | `raw/pointers/faction_pack_necrons.md` | **S4** |
| Oath of Moment, Gladius Task Force, Firstborn datasheets | `raw/pointers/faction_pack_space_marines.md` | **S5** |
| Points values | `raw/pointers/points_manuals.md` | S3 / S4 |
| Hierotek Circle datasheet mapping | **User photos** | S4 |
| Data Package Detachment | Ask the owner | Any |

Power Matrix's **system attribution** left this queue in L1. Its **wording** did not.

---

## Style conventions

How this KB writes about the game.

| Convention | Rule | Example |
|-----------|------|---------|
| Edition naming | "11th Edition" in prose, `warhammer_40k_11e` in frontmatter and paths | "new in 11th Edition" |
| Official term first | Official term, then community shorthand once in parentheses | "Objective Control (OC)" |
| No verbatim rules text | Paraphrase for teaching; never transcribe datasheet or stratagem wording | [`AGENTS.md`](../AGENTS.md) Sec 10 |
| Cite the check | Every rules claim names where it can be verified, with a retrieval date | "Wahapedia, read 2026-08-16" |
| Beginner voice | Explain why a rule matters, not just what it says | - |
| Name the system | Say "Kill Team" or "40K" explicitly when both could be meant | the Power Matrix correction |

---

## Deprecated / avoid list

| Avoid | Use instead | Reason |
|-------|-------------|--------|
| "Power Matrix may be a Kill Team term" | Power Matrix is the [[canoptek_court]] detachment rule in 40K | **Corrected in L1.** The L0 warning is superseded - see [[power_matrix]] |
| "Kill Team: Tomb World" as current inventory | The confirmed 2026-08-16 ownership | Superseded; historical only |
| Tomb World unit lists as shopping targets | The corrected retail lists in [[necron_lists_owner_notes]] | Caused double-counting of owned models |
| "Data Package Detachment" | Say plainly which detachment is stronger and why | Unrecognised term - see above |
| "Need 1 box of Immortals" | Immortals are **owned** (5, unassembled) | Corrected at Preflight; do not re-shop |
| Bare "OC" on first use | "Objective Control (OC)" | Expand on first use, then shorthand is fine |
| 10th Edition rules phrasing | 11th Edition wording, once verified | Edition drift is a lint category |

---

## Regional / variant terms

| Term | Context | Notes |
|------|---------|-------|
| "Necron lot", "Indomitus half", "Combat Patrol" | Second-hand marketplace listings | Seller shorthand from the owner's sourcing guide, not rules terms. "Combat Patrol" is also a 40K game size - which one is meant depends entirely on context |
| "Battleforce" | GW seasonal bundle boxes | A product term, not a rules term |

---

## Related pages

- [[index]] - master catalog
- [[overview]] - big-picture synthesis
- [[inherited_docs_for_S3]] - what S3 may safely promote from this page
- [[objective_control]] · [[reanimation_protocols]] · [[oath_of_moment]] · [[power_matrix]] - promoted concept pages
- [`AGENTS.md`](../AGENTS.md) - Sec 5 Keyword rule, Sec 9 terminology discipline
