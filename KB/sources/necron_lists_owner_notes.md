---
title: Necron Lists (owner's notes)
type: source
system: warhammer_40k_11e
faction: Necrons
created: 2026-08-16
updated: 2026-08-16
sources: [raw/Necron_Lists.md, raw/pointers/necron_lists_import.md]
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
| Last updated at origin | 2026-08-16 (Preflight ownership patch; raw re-synced same day after a stale Tomb-World-owned drift) |
| Retrieval date | 2026-08-16 |

This is a **planning document, not a rules document**. Per [[ingest_procedure]], owner's notes carry the *highest* trust for ownership and preference facts and **no** authority for rules text. Everything below is filed on that split: ownership facts are treated as confirmed, rules claims are treated as leads to verify.

---

## Confirmed ownership (2026-08-16)

The FOUNDATION section is the authoritative inventory for this project. It is mirrored in `games/warhammer_40k_11e/armies/necrons/Owned_Models_Inventory.md` and summarized on [[necrons]].

| Item | Qty | State |
|------|-----|-------|
| Necron Warriors | 10 (1 squad) | Purchased, **unassembled** |
| Canoptek Scarab Swarms | 3 | Purchased, **unassembled** |
| Immortals | 5 (1 squad) | Purchased, **unassembled** |
| Hierotek Circle Kill Team (used set) | 1 set | Assembled and painted - **game ready**; datasheet mapping pending photos |
| Kill Team: Tomb World | - | **Not owned.** Superseded historical assumption |

Two consequences the source states plainly, and this KB carries forward:

- **Build before play.** The only thing that can be put on a table today is the Hierotek Circle set. Warriors, Scarabs, and Immortals are bought but on sprue, so no teaching content should assume they are available for a first game.
- **Do not re-shop what is owned.** The source explicitly strikes Immortals, Scarabs, and the first box of Warriors off the retail list. An earlier version of the blueprint double-counted them.

---

## The two detachment paths

The source compares two Necron detachments as expansion routes from the same model pool. Both get their own KB page.

| | [[canoptek_court]] | [[cryptek_conclave]] |
|---|---|---|
| Wants | Canoptek constructs - Wraiths, Doomstalkers | Cryptek characters leading battleline infantry |
| Detachment rule | **Power Matrix** - hit re-rolls for units in territory the Necron player controls | **Scientific Schemes** - stacking ranged buffs and reanimation multipliers |
| Playstyle | Aggressive midfield pressure plus backline shooting | Defensive castle that wins by attrition and repeated revives |
| Owner's tier read | Highly competitive | Flavourful, casual-to-mid |
| Remaining spend (owner's CAD estimate) | ~$260 retail, target $130-180 second-hand | ~$375 retail, target $190-265 second-hand |

Both rule names and both tier judgements come from this source alone and are **not** cross-checked against the Necrons faction pack. Treat the *names* as reliable and the *effects* as unverified.

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

- **Scientific Schemes** as the Cryptek Conclave detachment rule
- Canoptek Macrocytes granting *Ignores Cover* to nearby infantry
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
- Which Hierotek Circle models map to which 40K datasheets - the central open TODO

---

## Historical material inside the source

Roughly a third of the document describes lists built around **Kill Team: Tomb World** (Cryptek Geomancer, Canoptek Tomb Crawlers, Canoptek Macrocytes). The source marks all of it superseded and verify-only. It is retained as a path note in case the box is ever bought.

**Do not let Tomb World content leak into current advice.** It is the single most likely stale-data mistake in this collection, and it already caused one round of bad shopping maths.

The final third is a Facebook Marketplace sourcing guide for Canada - keyword strategies and legacy box sets worth targeting. Useful, entirely non-rules, and not otherwise filed in the KB.

---

## Pages this source fed

- [[necrons]] - ownership, playstyle framing, detachment options
- [[canoptek_court]] - detachment rule, expansion path, shopping state
- [[cryptek_conclave]] - detachment rule, expansion path, shopping state
- [[power_matrix]] - the attribution correction
- [[reanimation_protocols]] - referenced obliquely via "reanimation multipliers"
- [[glossary]] - Power Matrix resolved; Scientific Schemes, Canoptek, Cryptek, Battleline and others added
- [[overview]] - ownership snapshot and open threads

---

## Open questions

- What is in the Hierotek Circle set, and which 40K datasheets do those models use? Blocks Phase 1 of both paths.
- What does Power Matrix actually do in 11th Edition wording?
- Is "Data Package Detachment" a real term, a community coinage, or a drafting artifact?
- Are the listed points values current, or carried over from 10th Edition?

---

## Related pages

- [[source_library]] - the catalog this import is registered in
- [[local_library_pointers]] - the owned PDFs that would verify these claims
- [[necrons]] - the faction page this feeds
- [[index]] - master catalog
- [[ingest_procedure]] - source classes and confidence rules
