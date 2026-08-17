---
title: Necron Lists (owner's notes)
type: source
system: warhammer_40k_11e
faction: Necrons
created: 2026-08-16
updated: 2026-08-17
sources: [raw/Necron_Lists.md, raw/pointers/necron_lists_import.md, kill_team_necron_photos]
confidence: draft
tags: [source, necrons, ownership, list_building, canoptek_court, cryptek_conclave]
---

# Necron Lists (owner's notes)

The owner's own Necron expansion blueprint: what is actually owned as of 2026-08-16, and two costed paths from that collection up to a 1,000-point army.

---

## What this source is

| Field | Value |
|-------|-------|
| Repo path | `raw/Necron_Lists.md` |
| Working copy | `games/warhammer_40k_11e/armies/necrons/Necron_Lists.md` (byte-identical after 2026-08-16 re-sync; prefer this copy if copies diverge) |
| External origin | `C:\Personal\40K\rules\Necron_Lists.md` (also byte-identical to working copy as of re-sync) |
| Source class | **Owner's own notes** ([[ingest_procedure]] Sec "four source classes") |
| Edition claimed | Warhammer 40,000, 11th Edition |
| Last updated at origin | 2026-08-16 (FOUNDATION rewritten to confirm **Kill Team: Tomb World owned and game-ready**; the earlier "not owned" reading was erroneous) |
| Retrieval date | 2026-08-16 |

This is a **planning document, not a rules document**. Per [[ingest_procedure]], owner's notes carry the *highest* trust for ownership and preference facts and **no** authority for rules text. Everything below is filed on that split: ownership facts are treated as confirmed, rules claims are treated as leads to verify.

---

## Confirmed ownership (2026-08-16)

The FOUNDATION section is the authoritative inventory for this project. It is mirrored in `games/warhammer_40k_11e/armies/necrons/Owned_Models_Inventory.md` and summarized on [[necrons]].

### Game-ready today

**Kill Team: Tomb World** - owned, assembled, painted, playable:

| Item | Qty | State |
|------|-----|-------|
| Cryptek Geomancer | 1 | **Game ready** |
| Canoptek Tomb Crawlers | 2 | **Game ready** |
| Canoptek Macrocytes | 5 | **Game ready** |
| Necron Warriors (Tomb World squad) | 10 | **Game ready** |
| Canoptek Scarab Swarms (Tomb World set) | 3 | **Game ready** |

Plus the set that is playable but not yet identified:

| Item | Qty | State |
|------|-----|-------|
| Hierotek Circle Kill Team (used set) | 1 set | Photo ID **done 2026-08-17** — Technomancer, Immortals, Despotek, Apprentek, Plasmacytes; see [[kill_team_necron_photos]] |

### Owned, build before play

| Item | Qty | State |
|------|-----|-------|
| Necron Warriors (second squad) | 10 | Purchased, **unassembled** |
| Canoptek Scarab Swarms (second set) | 3 | Purchased, **unassembled** |
| Immortals | 5 (1 squad) | Purchased, **unassembled** |

**Totals:** 20 Necron Warriors (10 game-ready + 10 on sprue), 6 Canoptek Scarab Swarms (3 game-ready + 3 on sprue), plus 1 Cryptek Geomancer, 2 Canoptek Tomb Crawlers, 5 Canoptek Macrocytes, 5 sprue Immortals, and Hierotek (Technomancer, 3 Immortal Guardians, Despotek, Apprentek, 2 Plasmacytes). See [[kill_team_necron_photos]].

Three consequences the source states plainly, and this KB carries forward:

- **There is a playable army today.** The Tomb World units are the **preferred learning baseline**: a complete, identified, painted force with known datasheets. The blueprint costs the five Tomb World datasheets at 385 points, a figure that still needs checking against the Munitorum Field Manual.
- **Extra Warriors and Scarabs are assemble-to-expand, not purchases.** Building the second squad merges the Warriors toward a 20-model block; building the second set doubles the Scarab swarms. Neither belongs on a shopping list.
- **Do not re-shop what is owned.** The source strikes the Tomb World box, the Immortals, both Warrior squads, and both Scarab sets off the retail list. An earlier version of the blueprint double-counted them.

---

## The two detachment paths

The source compares two Necron detachments as expansion routes from the same model pool. Both get their own KB page.

| | [[canoptek_court]] | [[cryptek_conclave]] |
|---|---|---|
| Wants | Canoptek constructs - Wraiths, Doomstalkers | Cryptek characters leading battleline infantry |
| Detachment rule | **Power Matrix** - hit re-rolls for units in territory the Necron player controls | **Scientific Schemes** - stacking ranged buffs and reanimation multipliers |
| Playstyle | Aggressive midfield pressure plus backline shooting | Defensive castle that wins by attrition and repeated revives |
| Owner's tier read | Highly competitive | Flavourful, casual-to-mid |
| Remaining spend (owner's CAD estimate) | ~$260 retail, target $130-180 second-hand | ~$310 retail, target $155-220 second-hand |

Both tier judgements come from this source alone and are **not** cross-checked against anything.

> **One of those rule names is wrong, and the row above deliberately keeps it.** The Cryptek Conclave rule is **Technosorcerous Augmentations**, confirmed on page 7 of the owned faction pack v1.1 and on [[wahapedia]], both read 2026-08-16. "Scientific Schemes" appears in neither. This is a source page, so it records what the source says and flags the conflict rather than rewriting it ([`AGENTS.md`](../../AGENTS.md) Sec 9). Use the corrected name everywhere else - see [[cryptek_conclave]] and the deprecated list in [[glossary]].
>
> Power Matrix, by contrast, survived its cross-check: the name is right, and only the exact wording is still unverified.

---

## The Power Matrix correction

**This source resolves an open question from L0.**

[[glossary]] seeded **Power Matrix** with an explicit warning that it might belong to *Kill Team* rather than Warhammer 40,000, on the reasoning that the Hierotek Circle is a Kill Team box. That reasoning was wrong.

This source names Power Matrix as the **main detachment rule of the Canoptek Court**, a Warhammer 40,000 detachment, in a table comparing 40K detachments at 40K points values. It is corroborated independently by `docs/Game_System_Scaffold.md`, whose vocabulary mapping gives "Power Matrix, the Canoptek Court detachment rule" as its worked example of a sub-list rule package.

The Hierotek Circle box is a real coincidence, not the origin of the term: the owner owns a Kill Team box *and* plays Necrons in 40K, and L0 joined the two. Corrected on [[power_matrix]] and in [[glossary]].

What is now settled, and what is not:

| Claim | Status |
|-------|--------|
| Power Matrix is a Warhammer 40,000 term, not Kill Team | **Resolved** - two independent in-repo sources |
| Power Matrix is the Canoptek Court detachment rule | **Resolved** - same two sources |
| It grants hit re-rolls tied to controlled territory | `draft` - owner's paraphrase only |
| Exactly what "controlled territory" means, and which attacks qualify | **Open** - needs the Necrons faction pack |

---

## Other rules leads worth verifying

Named by this source in passing, all `unverified` until an 11e source confirms them:

- **Scientific Schemes** as the Cryptek Conclave detachment rule - **disproven**: the rule is **Technosorcerous Augmentations**, read off the owned faction pack v1.1 and cross-checked on [[wahapedia]] on 2026-08-16. The source's label appears in neither. See [[cryptek_conclave]]
- Canoptek Macrocytes granting *Ignores Cover* to nearby infantry - **disproven**: S4 read the datasheet and found `[IGNORES COVER]` is a [[cryptek_conclave]] detachment option, not a Macrocytes aura. Worth flagging loudly now that the Macrocytes are game-ready
- Illuminor Szeras providing an armour-penetration aura to a nearby Warrior block
- A Plasmancer improving critical hits for the Immortals it leads
- Squad merging: Warriors to a 20-model block, Immortals to 10, Wraiths to 6
- Point values throughout (Warriors 100, Immortals 75, Scarabs 40, Wraiths 125, Doomstalker 145, Szeras 175, Lychguard 170, Plasmancer 65) - cross-check against the Munitorum Field Manual before list-building

The source also uses **"Data Package Detachment"** as a tier label ("3 Data Package Detachment", "2 Data Package Detachment"). That phrase does not map onto any 40K term this KB recognises. Flagged in [[glossary]] as unresolved.

---

## What this source does not cover

- Any core rules: turn sequence, phases, scoring, terrain
- The Necron army rule itself - Reanimation Protocols is never explained here
- Datasheet detail beyond names and points
- Space Marines, in any form
- Dual-legality of Hierotek Plasmacytes vs 40K Plasmacyte bases — photo ID of the set itself is **done** (2026-08-17); see [[kill_team_necron_photos]]

---

## The Tomb World correction

**Tomb World content is current advice, not historical material.** An earlier reading of this source recorded Kill Team: Tomb World as *not owned*, marked every list built on it superseded, and left a standing instruction not to let that content "leak" into current advice. That instruction is **withdrawn as a current rule**. The box is owned, its units are assembled and painted, and they are the preferred baseline for learning games.

What that reverses, concretely:

| Retired claim | Current fact |
|---------------|--------------|
| "Kill Team: Tomb World - not owned" | Owned. Geomancer, 2 Tomb Crawlers, 5 Macrocytes, 10 Warriors, 3 Scarab Swarms are all **game ready** |
| Tomb World lists are superseded path notes | They are the **current** Phase 1 lists for both detachment paths |
| "Do not let Tomb World content leak into current advice" | Retired. Tomb World *is* the current advice |
| The Hierotek Circle set is the only thing that can be fielded | Tomb World is the baseline; Hierotek is identified (Technomancer + Immortals; proxies for Plasmancer/Warden) |

The Hierotek Circle thread is **closed for identification** (2026-08-17). Remaining honesty: Apprentek/Warden are proxies; Plasmacytes likely not dual-legal.

The final third of the source is a Facebook Marketplace sourcing guide for Canada - keyword strategies and legacy box sets worth targeting. Useful, entirely non-rules, and not otherwise filed in the KB. Its bundle arithmetic now assumes 20 Warriors and 6 Scarab Swarms already owned, so duplicate battleline in a bundle carries little value.

---

## Pages this source fed

- [[necrons]] - ownership, playstyle framing, detachment options
- [[canoptek_court]] - detachment rule, expansion path, shopping state
- [[cryptek_conclave]] - detachment rule, expansion path, shopping state
- [[power_matrix]] - the attribution correction
- [[reanimation_protocols]] - referenced obliquely via "reanimation multipliers"
- [[glossary]] - Power Matrix resolved; Canoptek, Cryptek, Battleline and others added; this source's "Scientific Schemes" label deprecated in L2
- [[overview]] - ownership snapshot and open threads

---

## Open questions

- What 40K dual-legality remains for Hierotek Plasmacytes (25mm vs 28mm)? Identification of the set is **done**. **To-do: purchase 25–28mm base rings.**
- What does Power Matrix actually do in 11th Edition wording?
- Is "Data Package Detachment" a real term, a community coinage, or a drafting artifact?
- Are the listed points values current, or carried over from 10th Edition?

---

## Related pages

- [[source_library]] - the catalog this import is registered in
- [[local_library_pointers]] - the owned PDFs that would verify these claims
- [[necrons]] - the faction page this feeds
- [[kill_team_necron_photos]] - 2026-08-17 photo ID of Hierotek / Canoptek / NPO models
- [[index]] - master catalog
- [[ingest_procedure]] - source classes and confidence rules
