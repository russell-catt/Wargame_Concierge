---
title: Glossary
type: glossary
system: multi_system
systems: [warhammer_40k_11e, kill_team_2024]
created: 2026-08-16
updated: 2026-08-17
sources: [necron_lists_owner_notes, source_library, local_library_pointers, docs/Game_System_Scaffold.md, kill_team_2024_core_rules]
confidence: draft
tags: [terminology, glossary, keywords, warhammer_40k, necrons, space_marines, kill_team_2024]
---

# Glossary

The single home for **Keyword** entries and every game term this KB uses. Check here before using a rules term anywhere else. Updated on every ingest that introduces or refines terminology.

Keywords do **not** get their own pages - see [`AGENTS.md`](../AGENTS.md) Sec 5 for the rule and the three-part test that promotes a term into `KB/concepts/`. Promoted terms keep a short entry here pointing at their page, so this stays the one lookup surface.

---

## Read this first

**This page is now multi-system (2026-08-17, `kill_team_2024_scaffold` L1).** Wargame_Concierge's second game system, **Kill Team 2024 (KT24 / 3rd Edition)**, has its own section below, clearly separated from the Warhammer 40,000 11e sections above and below it. **Kill Team and 40K are separate games with separate rules** - this page is the *one place* both systems' terminology lives, precisely so a shared word (Cover, Charge, Engage, Objective marker, Command Point...) never gets read as meaning the same thing in both. Every such term carries a **collision flag** in both its 40K entry and its Kill Team entry, cross-linking to the other. See the **Kill Team** entry under "Other game systems" below for the standing warning this project already carries against conflating the two systems' rules or models.

**Status after L2 40K pass (2026-08-16).** L0 seeded four terms, L1 expanded them to 32, and **L2 reconciled the page against the rules documents S3, S4 and S5 actually read.** Three new terms were added in that pass: Territory, Support, and Combat Doctrines.

**Game terms (29):**

| Status | Meaning | Count |
|--------|---------|-------|
| `verified` | Cross-checked against a rules source; retrieval date recorded | **24** |
| `draft` | Named by a source that was read; effect not cross-checked | 4 |
| `unverified` | Written from familiarity or a prior edition. **Confirm before use** | **0** |
| `unresolved` | Appeared in a source and maps to nothing recognised | 1 |

**Project vocabulary (7):** all `verified` - these describe this project's own conventions, not the game, so they can be confirmed from the repo itself. **Assemble-to-expand** is new in the `tomb_world_ownership` L1 pass.

**The headline reversed in L2.** L1's version of this block said "no game term is `verified`, because no rules document has been read yet." That is no longer true. S3 read the owned Core Rules, the Universal Rules Updates v1.0, both faction packs v1.1, and the Event Companion v1.1; S4 and S5 read the two Munitorum Field Manuals v1.2 and both detachment sections. Every `verified` entry below traces to one of those, read **2026-08-16**, or to the shipping glossary that records them.

**What `verified` still does not mean.** It means someone read it on 2026-08-16 and wrote down where. It does not mean a dataslate has not landed since - nothing in this repo records when the owned PDFs were downloaded. See [[warhammer_community]].

**The shipping surface.** [`games/warhammer_40k_11e/rules/Keyword_Glossary.md`](../games/warhammer_40k_11e/rules/Keyword_Glossary.md) is the player-facing glossary S3 owns; it is longer than this page and carries the weapon-ability keywords in full. **This page is the KB-side working surface and defers to it on any term both define.** Where the two ever disagree, that disagreement is a lint finding, not a preference.

---

## Entry format

**Term** *(canonical form)* - `status`
: Definition in plain language. Why a player cares. What is not yet confirmed.
- Faction / scope: where the term applies
- Verify against: where to check it
- See also: `[[related_page]]` *(illustrative - backticked so link lint does not read it as a real target)*

---

## Core rules and scoring

**Objective Control** *(OC)* - `verified` · **upgraded in L2**
: A characteristic on a model's profile representing how strongly it holds ground. Players total the OC of their eligible models within range of an objective marker; the higher total controls it. It is why a cheap, numerous unit can hold ground an elite unit cannot, and why the game is won by positioning rather than kill count.
: **Confirmed in 11th Edition (S3, owned Core Rules, read 2026-08-16):** control is re-checked at the end of **every phase and every turn**, and a **battle-shocked** unit contributes no OC at all.
- Faction / scope: core rules, system-wide
- Verify against: the shipping [`Keyword_Glossary.md`](../games/warhammer_40k_11e/rules/Keyword_Glossary.md) and `Key_Concepts.md`, both S3
- See also: **[[objective_control]]** - promoted to a concept page in L1, verified in L2

**Objective marker** - `verified` · **upgraded in L2**
: The physical marker on the table whose control is scored. Control is decided by totalling Objective Control within range of it, and can flip as models move, die, or arrive.
: **Confirmed:** a 40 mm circular marker; a model is within range at **3" horizontally and 5" vertically**. Where the objective is a terrain area instead, a model is in range simply by being inside that area.
- Faction / scope: core rules
- Verify against: shipping `Keyword_Glossary.md`; `../games/warhammer_40k_11e/setup/Board_Setup.md`

**No Man's Land** - `verified` · **upgraded in L2**
: The contested middle of the table, outside either deployment zone, and where most objectives live. Named in the owner's Necron notes as the ground [[canoptek_court]] wants to open up for its detachment rule - which the verified [[power_matrix]] wording confirms.
- Faction / scope: core rules / deployment
- Verify against: shipping `Keyword_Glossary.md`; `Board_Setup.md`
- See also: **Territory**, below - the two are not the same region

**Territory** - `verified` · **new in L2**
: The half of the battlefield containing a player's deployment zone. Distinct from that player's **deployment zone** and from **No Man's Land**, and the distinction is load-bearing: [[power_matrix]] keys off regions, and reading "territory" loosely is the easiest way to play it wrong.
- Faction / scope: core rules; several detachment rules key off it
- Verify against: shipping `Keyword_Glossary.md`

**Battle round** - `verified` · **upgraded in L2**
: Start-of-round rules, then **both** players take a turn, then end-of-round rules. The same player takes the first turn every round; the mission says who. Sequencing matters for any rule triggering "at the start of" or "at the end of" something - notably [[reanimation_protocols]], which fires at the end of **your** Command phase and therefore once per round.
- Faction / scope: core rules
- Verify against: `../games/warhammer_40k_11e/rules/Turn_Structure.md` (S3, from the owned Core Rules, read 2026-08-16)

**Datasheet** - `verified` · **upgraded in L2**
: The rules entry for one unit: profile, weapons, abilities, keywords. This project's generic term for it is "unit entry" (`docs/Game_System_Scaffold.md` vocabulary mapping). Datasheet text is **never reproduced** in this repo - see [`AGENTS.md`](../AGENTS.md) Sec 10.
- Faction / scope: system-wide
- Verify against: your own faction pack or the Warhammer 40,000 app; [[wahapedia]] for lookup

**Detachment** - `verified` · **upgraded in L2**
: The rules package a list is built under, sitting between "army" and "unit". It supplies a **detachment rule**, plus enhancements and stratagems. Choosing one is the first real list-building decision, and it determines which units the army wants.
- Faction / scope: system-wide
- Verify against: shipping `Keyword_Glossary.md`
- See also: [[canoptek_court]], [[cryptek_conclave]], [[gladius_task_force]]

**Detachment rule** - `verified` · **upgraded in L2**
: The army-wide ability granted by the chosen detachment - [[power_matrix]] for [[canoptek_court]], **Technosorcerous Augmentations** for [[cryptek_conclave]], **Combat Doctrines** for [[gladius_task_force]]. Distinct from the **army rule**, which applies regardless of detachment.
- Faction / scope: system-wide

**Army rule** - `verified` · **upgraded in L2**
: The faction-wide ability every list of that faction has, independent of detachment: [[reanimation_protocols]] for Necrons, [[oath_of_moment]] for Space Marines.
- Faction / scope: system-wide

**Battleline** - `verified` · **upgraded in L2**
: The role keyword for a faction's core infantry - Necron Warriors and Immortals in this collection. Detachments built on massed infantry, such as [[cryptek_conclave]], feed off battleline units.
- Faction / scope: system-wide
- Verify against: shipping `Keyword_Glossary.md`

**Leader / attached unit** - `verified` · **upgraded in L2**
: A character joining a squad and fighting as part of it. The two become **one unit for all rules purposes**, the bodyguard's Toughness is used for the whole thing, and the attached unit holds **every keyword of its parts** - which can expose it to `[ANTI-X]` weapons it would otherwise dodge.
: **Two things L1 could not know.** Attachment happens during the pre-game **Declare Battle Formations** step, not mid-game. And 11th Edition adds a second slot, **Support**, so a bodyguard unit can normally take one Leader **and** one Support.
: The owner's assumptions turned out to be sound - a Plasmancer can lead Immortals - but the Plasmancer is now a **Support**, not a Leader, which is what makes a Cryptek plus a Royal Warden on the same squad legal. See [[cryptek_conclave]].
- Faction / scope: core rules
- Verify against: shipping `Keyword_Glossary.md`; `Key_Concepts.md`

**Support** - `verified` · **new in L2**
: The second attachment slot alongside Leader, given new emphasis in 11th Edition. The owned Necrons Faction Pack v1.1 moved the Crypteks (Chronomancer, Geomancer, Plasmancer, Psychomancer, Technomancer, Orikan) from Leader to Support. **Check your own datasheet** - this moved recently and older printings disagree.
- Faction / scope: core rules
- Verify against: shipping `Keyword_Glossary.md`; your own datasheets

**Points** *(pts)* - `verified` · **upgraded in L2**
: The cost of a unit, used to build lists to an agreed size. Values live in the Munitorum Field Manual - **v1.2, printed 2026-08-13** is the version this project has read - and they **move when a balance dataslate lands**.
: **Every points figure in [[necron_lists_owner_notes]] was wrong.** S3 found six of eight stale, S4 found two more, and S4 re-costed everything the shipping content prints. Space Marines have their own separate Munitorum file. Several datasheets now use **first-unit / second-unit pricing**, so a list cannot be costed by multiplication.
- Faction / scope: system-wide
- Verify against: the owned Munitorum Field Manual v1.2, and re-check before any event

**Armour Penetration** *(AP)* - `verified` · **upgraded in L2**
: A negative modifier to the target's armour save - AP -2 makes a 3+ save behave like a 5+. An **invulnerable save ignores AP entirely**, so use whichever save is better per attack.
- Faction / scope: core rules
- Verify against: shipping `Keyword_Glossary.md`

**Critical hit / critical wound** - `verified` · **upgraded in L2**
: An **unmodified 6** on the hit or wound roll. It is still an ordinary hit or wound, but it switches on `[LETHAL HITS]`, `[SUSTAINED HITS X]`, `[DEVASTATING WOUNDS]`, and `[ANTI-X Y+]`.
- Faction / scope: core rules
- Verify against: shipping `Keyword_Glossary.md`

**`[IGNORES COVER]`** - `verified` · **upgraded in L2**
: The target cannot have the benefit of cover against this attack, and it also beats abilities that grant cover, such as Stealth. Worth knowing precisely, because **cover in 11th Edition worsens the attacker's Ballistic Skill by 1** rather than improving the target's save.
: **The owner's note about this keyword was wrong.** It attributed `[IGNORES COVER]` to a Canoptek Macrocytes aura; S4 checked the datasheet and disproved it. `[IGNORES COVER]` is one of the options on the [[cryptek_conclave]] detachment menu - the two rules had been run together. See the deprecated list.
- Faction / scope: core rules keyword
- Verify against: shipping `Keyword_Glossary.md`

**Cover** - `verified` · **collision flag added 2026-08-17**
: Worsens the *attacking* weapon's Ballistic Skill by 1. Cover is a property of terrain and positioning checked in the shooting sequence; it does not touch the target's save directly. This is an 11th Edition change from the prior "cover improves your save" wording - see the deprecated list.
: **Collision flag.** Kill Team 2024 also has a rule called "Cover", and it works the opposite way round - it grants the *defender* a free retained defence success rather than penalising the attacker's accuracy. **Do not read one system's Cover into the other.** See **Cover** in the Kill Team 2024 section below and [[cover_kill_team]] for the full comparison table.
- Faction / scope: core rules
- Verify against: shipping `Keyword_Glossary.md` ("Benefit of cover")

**Charge** - `verified` · **collision flag added 2026-08-17**
: Declare a charge within 12" of an enemy unit, roll 2D6, and move up to that distance to end engaged with every unit you declared against. Cannot be attempted after Advancing or Falling Back; a double 1 always fails.
: **Collision flag.** Kill Team 2024 also has an action called "Charge" - a 1AP move action, no dice roll involved, that lets the active operative move Move+2" and must end within 1" control range of an enemy operative. Same word, unrelated resolution. See **Charge** in the Kill Team 2024 section below.
- Faction / scope: core rules
- Verify against: shipping `Keyword_Glossary.md`

**Engagement Range** - `verified` · **collision flag added 2026-08-17**
: A fixed zone of 2" horizontally and 5" vertically around a model. Being inside an enemy unit's Engagement Range is what "in melee" means for movement, shooting, and phase-transition purposes - a pure geometric distance test, independent of visibility.
: **Collision flag.** Kill Team 2024 has no term called "Engagement Range" - its nearest equivalent is **Control Range**, a visibility-gated 1" zone with a different job (marker contests by APL total, cover eligibility, Fight legality). The two are not interchangeable despite the naming brief for the `kill_team_2024_scaffold` L1 pass suggesting the filename `engagement_range_kill_team` by pattern-matching this term. See [[control_range_kill_team]] for the full comparison.
- Faction / scope: core rules
- Verify against: shipping `Keyword_Glossary.md`

**Command Point (CP)** - `verified` · **collision flag added 2026-08-17**
: The currency spent on stratagems. Both players gain 1 CP in the Command phase each battle round.
: **Collision flag.** Kill Team 2024 also has Command Points, gained in the Ready step of the Strategy phase and spent on ploys instead of stratagems - similar *idea* (a resource economy for one-off effects), different *gain rule* (KT24 gives the player *without* initiative 2 CP instead of 1, from turning point two onward; 40K gives both players 1 flat). See **Command Point (CP)** in the Kill Team 2024 section below.
- Faction / scope: core rules
- Verify against: shipping `Keyword_Glossary.md`

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

**Technosorcerous Augmentations** - `draft` - **renamed in L2**
: The [[cryptek_conclave]] detachment rule. Two effects: ranged weapons on Cryptek models gain `[ASSAULT]`, and each time a Cryptek unit is selected to shoot it picks one ability from a short menu for that phase. Because an attached Cryptek character lends its keyword to the whole squad, the pick lands on the bodyguard unit's guns, not on the character's pistol.
: **"Scientific Schemes" was the wrong name and is deprecated.** It came from the owner's pre-project notes and appears nowhere in the owned faction pack v1.1 or on [[wahapedia]]. Both were checked on 2026-08-16.
- Faction / scope: Necrons, [[cryptek_conclave]] detachment rule
- Deprecated label: Scientific Schemes - see the deprecated list below
- Verify against: `raw/pointers/faction_pack_necrons.md`, then [[wahapedia]]

**Canoptek** - `draft`
: The Necron robotic-construct family: Scarab Swarms, Wraiths, Doomstalkers, and others. The theme [[canoptek_court]] is built around.
- Faction / scope: Necrons, keyword

**Cryptek** - `draft`
: The Necron engineer-character family - Plasmancer, Technomancer, Geomancer, and others. The theme [[cryptek_conclave]] is built around, and the likely content of the owned Hierotek Circle set.
- Faction / scope: Necrons, keyword

**Hierotek Circle** - `draft`
: A **Kill Team** boxed set of Necron Crypteks and attendants. The owner has one, used and fully painted, so it is game-ready in the physical sense - but **its 40K datasheet mapping is unknown** and pending photographs, which is what keeps it out of lists. It is no longer the only game-ready part of the collection; Kill Team: Tomb World is both painted and identified.
: It is a set of models, not a rules term. L0 mistakenly treated it as evidence about [[power_matrix]]; it is not evidence about any 40K rule.
- Faction / scope: Necrons, models - **Kill Team product, usable as 40K models once identified**
- See also: [[necrons]]

**Kill Team: Tomb World** - `draft` · **owned, game-ready**
: A Kill Team box the owner owns, assembled and painted: **1 Cryptek Geomancer, 2 Canoptek Tomb Crawlers, 5 Canoptek Macrocytes, 10 Necron Warriors, 3 Canoptek Scarab Swarms**. Its models map to known 40K datasheets, which makes it the **preferred baseline for learning games** and the Phase 1 force for both Necron detachment paths.
: **An earlier KB entry said this box was "confirmed not owned" and its lists historical only.** That was wrong. The old standing instruction not to let Tomb World content "leak" into current advice is withdrawn - it is the current advice.
- Faction / scope: Necrons, models - **owned; current, not historical**
- See also: [[necrons]], [[necron_lists_owner_notes]], and the deprecated list below

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

**Kill Team** - `draft` · **now a full system in scope, see below (2026-08-17)**
: A **separate Games Workshop game**, not a mode of Warhammer 40,000. Small squads, different rules, different points.
: It earns a glossary entry because conflating it with 40K already caused one error in this KB - see the Power Matrix entry above. Kill Team *models* can be used in 40K once matched to a datasheet; Kill Team *rules terms* have no standing in 40K content. **Keep the box and the ruleset separate.**
: **Kill Team 2024 (KT24 / 3rd Edition) is now a tracked system with its own KB pages** - `system: kill_team_2024` - as of the `kill_team_2024_scaffold` track. The line above still holds: this entry described the relationship correctly before a single KT24 page existed, and nothing about that relationship has changed now that pages do.
- Faction / scope: outside 40K's scope; own system below
- See also: the **Kill Team 2024** section below, [[kill_team_2024_core_rules]]

---

## Kill Team 2024 (KT24 / 3rd Edition)

**Second game system, added 2026-08-17 (`kill_team_2024_scaffold` L1).** Everything in this section carries `system: kill_team_2024` in its source pages. **These are not Warhammer 40,000 terms.** Where a word is shared with the 40K sections above, both entries carry a **collision flag** pointing at each other - check both before assuming they mean the same thing. All terms below are `draft`: cross-checked against Wahapedia's Kill Team 3 Core Rules page (retrieved 2026-08-17), not yet against the owned Core Rules PDF, which the Librarian cannot open. See [[kill_team_2024_core_rules]].

**Turning Point** - `draft`
: One round of a KT24 battle: a Strategy phase then a Firefight phase, repeated a fixed number of times (four by default). No 40K equivalent term - the nearest 40K idea is **Battle round**, which is structured completely differently (each player takes a full sequential turn, rather than both sides interleaving single-operative activations). See [[turning_points]].
- Faction / scope: Kill Team 2024, core rules, system-wide
- Verify against: `kill_team_2024_core_rules`, then the owned Core Rules PDF

**Strategy phase** / **Firefight phase** - `draft`
: The two phases inside every Turning Point. Strategy handles Initiative, Ready (CP gain, readying operatives), and Gambit (Strategy ploys). Firefight is where operatives actually activate and act.
- Faction / scope: Kill Team 2024, core rules
- See also: [[turning_points]]

**Activation** - `draft`
: The unit of play in the Firefight phase: one operative, chosen by its controlling player, given an order then spending AP on actions until its player is done, then flipped to expended. Players strictly alternate single-operative activations. No 40K equivalent - 40K has no per-model activation inside a phase. See [[activations_apl]].
- Faction / scope: Kill Team 2024, core rules
- See also: **Command Point (CP)** below (gained at Ready, spent on ploys)

**APL (Action Point Limit)** - `draft`
: The AP budget an operative can spend during one activation, printed on its datacard. Also the value totalled to decide marker control (see Control Range, below).
- Faction / scope: Kill Team 2024, core rules
- See also: [[activations_apl]]

**Order: Engage** - `draft` · **collision flag**
: One of two states chosen every time an operative activates. Engage lets it act fully (Shoot, Charge, counteract) but makes it a valid target regardless of cover.
: **Collision flag.** Not related to 40K's **Engagement Range** (a fixed geometric zone, not a per-model order). See [[orders_conceal_engage]] and the Engagement Range collision entry in the core-rules section above.
- Faction / scope: Kill Team 2024, core rules
- Verify against: `kill_team_2024_core_rules`

**Order: Conceal** - `draft`
: The other order state. Blocks Shoot, Charge, and counteracting, but the operative is not a valid target while it is in cover.
- Faction / scope: Kill Team 2024, core rules
- See also: [[orders_conceal_engage]]

**Control Range** - `draft` · **collision flag**
: The 1"-and-visible zone around an operative that governs marker contests (by total APL, not model count), cover eligibility, Fight legality, and move restrictions.
: **Collision flag.** This is the closest KT24 concept to 40K's **Engagement Range**, but the two are built differently: Control Range is visibility-gated at 1" and decides marker/cover/Fight questions; Engagement Range is a pure 2"/5" distance test with no visibility component, deciding melee/movement legality. **Do not use "Engagement Range" for the KT24 term** - it does not exist in KT24. See [[control_range_kill_team]].
- Faction / scope: Kill Team 2024, core rules
- Verify against: `kill_team_2024_core_rules`

**Cover** (Kill Team) - `draft` · **collision flag**
: Grants the *defender* one free retained defence success ("cover save") when a target in cover is shot, and (combined with a Conceal order) can make the target not a valid target at all.
: **Collision flag.** Runs in the **opposite mechanical direction** from 40K's Cover, which worsens the *attacker's* Ballistic Skill instead of helping the defender's save. See the Cover entry in the core-rules section above and [[cover_kill_team]] for the full table.
- Faction / scope: Kill Team 2024, core rules
- Verify against: `kill_team_2024_core_rules`

**Obscured** - `draft`
: A separate check from Cover: intervening *Heavy* terrain (not within 1" of either operative) forces the attacker to discard one success and downgrades their critical successes to normal. An operative cannot be both in cover and obscured from the same terrain feature - the defender picks one.
- Faction / scope: Kill Team 2024, core rules
- See also: [[cover_kill_team]]

**Valid Target** - `draft`
: The targeting test for shooting (and some rare rules): an Engage-ordered operative is valid if visible; a Conceal-ordered operative is valid only if visible **and not in cover**.
- Faction / scope: Kill Team 2024, core rules
- See also: [[orders_conceal_engage]], [[cover_kill_team]]

**Counteract** - `draft`
: When one side has expended every operative but the other still has ready ones, an expended Engage-ordered operative can perform one free 1AP action (not Guard), capped at once per operative per turning point and a 2" move limit. Not an activation - action restrictions from that operative's own earlier activation don't apply.
: No 40K equivalent. The nearest 40K idea, Fire Overwatch, is a stratagem-gated reactive shoot rather than a universal end-of-phase option.
- Faction / scope: Kill Team 2024, core rules
- See also: [[activations_apl]]

**Injured** - `draft` · **collision flag**
: An operative below half its starting Wounds: -2" Move, and all its weapons' Hit stat worsens by 1.
: **Collision flag.** Do not conflate with 40K's **Battle-shock**. Injured triggers off an individual model's own Wounds; Battle-shock triggers off a failed Leadership test (itself gated by unit strength) and has entirely different effects (zeroes Objective Control, blocks stratagem targeting and actions). See [[injured_operatives]].
- Faction / scope: Kill Team 2024, core rules
- Verify against: `kill_team_2024_core_rules`

**Incapacitated** - `draft`
: An operative at 0 Wounds or less - the KT24 equivalent moment to a 40K model being destroyed. Separated from "removed from the killzone" so certain free actions (e.g. Place Marker) can trigger in between.
- Faction / scope: Kill Team 2024, core rules
- See also: [[injured_operatives]]

**Command Point (CP)** (Kill Team) - `draft` · **collision flag**
: Gained in the Ready step of the Strategy phase - 1 CP per player normally, but 2 CP for whichever player does **not** have initiative, from turning point two onward. Spent on ploys (Strategy ploys in the Gambit step, Firefight ploys during activations).
: **Collision flag.** 40K also has Command Points, but gains a flat 1 CP per player per battle round with no initiative-based asymmetry, and spends them on stratagems rather than ploys. See the Command Point entry in the core-rules section above.
- Faction / scope: Kill Team 2024, core rules
- Verify against: `kill_team_2024_core_rules`

**Ploy** - `draft`
: A CP-bought one-off rules effect. **Strategy ploys** are used in the Gambit step and are a type of `STRATEGIC GAMBIT`; **Firefight ploys** are used during activations. Every player has access to the universal **Command Re-roll** firefight ploy (1CP, re-roll one attack or defence die) plus their kill team's own ploys. Roughly analogous in *role* to a 40K stratagem, but gated by phase (Strategy vs Firefight) rather than by a stratagem's own stated timing window.
- Faction / scope: Kill Team 2024, core rules
- See also: **Command Point (CP)** (Kill Team), above

**Operative** - `draft`
: A KT24 model. "Friendly operative" / "enemy operative" from each player's perspective - the direct equivalent of a 40K model, but note KT24 has no unit grouping above the operative for activation purposes (each operative activates individually).
- Faction / scope: Kill Team 2024, core rules

**Datacard** - `draft`
: An operative's rules entry: type, stats (APL, Move, Save, Wounds), weapons, additional rules, keywords, base size. The KT24 equivalent of a 40K datasheet. **Never reproduced verbatim in this repo.**
- Faction / scope: Kill Team 2024, core rules
- Verify against: `kill_team_2024_core_rules`; your own team's rules

**Killzone** - `draft`
: The game board and terrain set a KT24 battle is played on - the rough KT24 equivalent of a 40K battlefield/board, but killzones are named, packaged terrain sets (Volkus, Shadowhunt, Tomb World, etc.) rather than a generic table.
- Faction / scope: Kill Team 2024, setup
- Verify against: `raw/pointers/kill_team_2024_missions.md` (unread)

**Marker** - `draft`
: A placed token affecting the game and nearby operatives. Objective markers are 40mm; all others are 20mm. Controlled by whichever side's contesting operatives have the higher total APL (see Control Range, above) - a different control mechanism from 40K's Objective Control characteristic.
- Faction / scope: Kill Team 2024, core rules
- See also: [[control_range_kill_team]]

---

## Project vocabulary

Not game terms - the words this project uses about its own state. S3 should keep them consistent in shipping content.

**Game-ready** - `verified`
: Assembled, painted or at least based, and fieldable today. Currently: the **Kill Team: Tomb World** units (Geomancer, 2 Tomb Crawlers, 5 Macrocytes, 10 Warriors, 3 Scarab Swarms) and the **Hierotek Circle** set. Only the Tomb World half is also *identified*, so only it can be put in a list.

**Build before play** - `verified`
: Purchased but unassembled. Excluded from any "play this weekend" advice. Currently: the second Warrior squad (10), the second Scarab Swarm set (3), and 5 Immortals.

**Assemble-to-expand** - `verified`
: Owned-but-unassembled models that duplicate a unit already game-ready, so building them widens an existing squad rather than adding a new capability. Currently the second Warrior squad and the second Scarab set. Distinct from **build before play**, which is the same physical state but gates a unit the collection does not otherwise have - the Immortals.

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
| Reanimation Protocols, Power Matrix wording, Canoptek, Cryptek | `raw/pointers/faction_pack_necrons.md` | **S4** - still outstanding for `KB/`; S4 read the pack for `games/` but the KB pages were not back-filled |
| ~~Scientific Schemes~~ | Same | **Done.** S4 read the pack; the rule is Technosorcerous Augmentations and the old label is deprecated |
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
| "Kill Team: Tomb World is not owned" / "Tomb World is historical only" | Tomb World is **owned and game-ready** - see [[necrons]] | **Corrected 2026-08-16.** The "not owned" claim was erroneous and drove several downstream pages |
| "Do not let Tomb World content leak into current advice" | Tomb World *is* the current advice, and the preferred learning baseline | Retired as a current rule in the same correction |
| Re-shopping Necron Warriors or Canoptek Scarab Swarms | 20 Warriors and 6 Scarab Swarms are **owned**; the unbuilt halves are assemble-to-expand | Double-counting owned models is the recurring error on this collection |
| "Scientific Schemes" as the [[cryptek_conclave]] detachment rule | **Technosorcerous Augmentations** - see the Necrons section above | **Corrected in L2.** The old label came from the owner's pre-project notes and appears in neither the owned faction pack v1.1 nor [[wahapedia]]. It survives only where a source page quotes the source verbatim |
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
- [[objective_control]] · [[reanimation_protocols]] · [[oath_of_moment]] · [[power_matrix]] - promoted 40K concept pages
- [[turning_points]] · [[activations_apl]] · [[orders_conceal_engage]] · [[cover_kill_team]] · [[control_range_kill_team]] · [[injured_operatives]] - promoted Kill Team 2024 concept pages
- [[kill_team_2024_core_rules]] - the KT24 core-rules source page
- [`AGENTS.md`](../AGENTS.md) - Sec 5 Keyword rule, Sec 9 terminology discipline

## L1 note - `kill_team_2024_scaffold` (2026-08-17)

- **Kill Team 2024 added as a full glossary section.** 20 new terms under "Kill Team 2024 (KT24 / 3rd Edition)", all `draft`, cross-checked against Wahapedia's Kill Team 3 Core Rules page (retrieved 2026-08-17). The owned Core Rules PDF is unopened by the Librarian - it is a pointer stub, not a readable file in this environment.
- **Six 40K terms gained explicit collision flags** against their KT24 counterparts: Cover, Charge, Engagement Range, and Command Point (CP) in the core-rules section above; Engage (via Orders) and Injured (via Battle-shock) flagged from the KT24 side. Every flag is bidirectional - each entry names and links the other system's entry.
- **Naming deviation recorded.** The ingest brief suggested `engagement_range_kill_team` as a concept-page filename. KT24's actual term is **Control Range**, a different mechanic (visibility-gated, 1", APL-based marker control) from 40K's Engagement Range (non-visibility-gated, 2"/5", movement/melee legality). Filed as `[[control_range_kill_team]]` instead, per [`AGENTS.md`](../AGENTS.md) Sec 9's "never guess a rules term."
- **No 40K game term's status changed in this pass.** This was a pure addition; nothing above the new section was rewritten except the "Other game systems" Kill Team stub, which was extended rather than replaced.

## L2 lint note (2026-08-16)

- **Power Matrix** — Canoptek Court detachment rule in Warhammer 40,000 11e (not Kill Team-only). See teaching guide under armies/necrons.
- **Cryptek Conclave rule name** — prefer **Technosorcerous Augmentations** (owned faction pack). Deprecated informal label: Scientific Schemes.
- Shipping Keyword_Glossary remains SoT for table keywords; this glossary is the KB working set.

## L1 ownership note — `tomb_world_ownership` (2026-08-16)

- **Kill Team: Tomb World is owned and game-ready.** The prior "not owned" entry was erroneous; the entry and the deprecated list are both rewritten.
- **"Do not let Tomb World content leak" is retired** as a current rule. It survives only as a deprecated-claim row, so the old instruction cannot quietly return as guidance.
- **Ownership vocabulary updated:** `Game-ready` and `Build before play` now describe the real inventory, and **Assemble-to-expand** was added for owned duplicates of already-fielded squads.
- No game term's `verified` / `draft` status changed in this pass. Ownership is not a rules claim.

## L2 lint note — `tomb_world_ownership` (2026-08-16)

- **The Technosorcerous Augmentations rename is now applied, not just preferred.** The `v1_scaffold` L2 pass recorded the preference in the note above but left the headword entry, [[cryptek_conclave]], [[necrons]], and [[power_matrix]] all still reading "Scientific Schemes". That intra-KB drift is closed in this pass, and the old label is now on the deprecated list.
- **Source pages keep the old label on purpose.** [[necron_lists_owner_notes]] quotes `raw/Necron_Lists.md`, which says "Scientific Schemes". Per [`AGENTS.md`](../AGENTS.md) Sec 9 the conflict is recorded there rather than overwritten — the source said what it said.
- **No ownership terms changed in this pass.** The L1 note above still stands as written. L2 re-ran the sweep and found no live Tomb World ownership denial anywhere in `KB/`.

## Kill Team 2024 — Nemesis Ops terms (nemesis_ops_research L1, 2026-08-17)

| Term | Definition (teaching paraphrase) | Confidence | Notes |
|------|-----------------------------------|------------|-------|
| Nemesis Operative | Boss-scale operative built or shipped for Joint Ops / Nemesis content; often NPO | draft | Distinct from **Nemesis Claw** player team |
| Nemesis Custom Builder | Dossier toolkit: allegiance → size → behaviour → weapons → traits | draft | Shipping How-To in `games/kill_team_2024/nemesis_ops/` |
| Joint Ops | Official co-op / solo PvE vs NPOs (project folder `joint_ops/`) | draft | Formerly path `join_ops/` |
| Adversary Ops | PvP-with-NPO-assist style missions (WarCom / packs) | draft | Naming overlaps **Nemesis Ops** in dossier |
| Nemesis Ops | Dossier mode wording alongside Joint Ops | draft | See Modes_And_Cards open naming note |
| NPO | Non-player operative | draft | Core + expansion packs |

