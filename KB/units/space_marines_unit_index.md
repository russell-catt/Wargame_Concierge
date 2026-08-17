---
title: Space Marines unit index (KB overview)
type: unit
system: warhammer_40k_11e
faction: Space Marines
created: 2026-08-16
updated: 2026-08-16
sources: [games/warhammer_40k_11e/armies/space_marines/units/Unit_Index.md, docs/handoffs/v1_scaffold/slices/S6_sm_implementer.md]
confidence: draft
tags: [unit, space_marines, index, s6, research_corpus, pointer, firstborn]
---

# Space Marines unit index (KB overview)

The KB's entry point into the 78-file Space Marine unit research corpus that S6 built under `games/`. A **pointer and a health report**, not a copy of the corpus.

**The corpus itself:** [`games/warhammer_40k_11e/armies/space_marines/units/Unit_Index.md`](../../games/warhammer_40k_11e/armies/space_marines/units/Unit_Index.md) - one row per datasheet, with a Wahapedia URL, a priority, and a `chapter_unique` column the Necron index does not have.

The reasoning for pointing rather than duplicating is the same as on [[necrons_unit_index]]: a `KB/units/` page has to add play knowledge the research file does not already carry, and almost none of these files carry enough to add to.

---

## What S6 actually delivered

| Metric | Space Marines |
|--------|---------------|
| Index rows | 78 |
| Research files | 78 (counts match - QA verified) |
| Schema | `units/_schema.md` v1, 2026-08-16 |
| Research date | 2026-08-16 |

### Completeness, by the corpus's own field

| `completeness` | Count |
|----------------|-------|
| `full` | **0** |
| `partial` | 9 |
| `stub` | 69 |

**No Space Marine unit is fully researched.** The Necron side has three `full` files; this side has none. That gap is not an oversight - it follows directly from the ownership gap, because nobody knows which of these 78 datasheets the son actually has models for.

### Priority, by the corpus's own field

| `priority` | Count | Meaning |
|------------|-------|---------|
| `starter` | 9 | Provisional Gladius learning-list candidates |
| `roster` | 59 | Catalogued for completeness |
| `chapter_unique` | 10 | Blood Angels, Dark Angels, Space Wolves, Black Templars, Deathwatch |

The nine `starter` files are the nine `partial` files. The corpus put its effort exactly where the learning list is expected to be, then stopped at the inventory wall.

---

## The `chapter_unique` column is a rules problem, not a labelling one

The corpus tags ten datasheets to a specific Chapter: Death Company Marines and Sanguinary Guard (BA), Deathwing Terminator Squad and Ravenwing Black Knights (DA), Wolf Guard and Thunderwolf Cavalry (SW), Primaris Crusader Squad and Sword Brethren (BT), Deathwatch Veterans and Proteus Kill Team (DW).

**Fielding any of them costs the army the +1 to Wound half of [[oath_of_moment]].** S5 verified from the owned Space Marines Faction Pack v1.1 that the bonus applies only to a Codex: Space Marines detachment containing no Blood Angels, Dark Angels, Deathwatch or Space Wolves units. A single such model, painted in with the rest of the force, downgrades the army rule for the whole game.

So this column is the highest-value thing in the corpus. When the collection audit happens, **checking it against these ten rows is the first question to ask**, ahead of counting bodies.

---

## Firstborn and Legends coverage

The corpus does the thing this project specifically needed: it tags the older kits.

| Tag | Examples |
|-----|----------|
| `Firstborn` | Tactical Squad, Devastator Squad, Command Squad, Bike Squad, Attack Bike Squad |
| `Legends` | Assault Squad, Assault Squad with Jump Packs, Scout Sniper Squad, Venerable Dreadnought, and the Firstborn entries above where marked |

That matters because the son's army is built from **existing older kits** ([[space_marines]]). A datasheet marked Legends is not tournament-legal, and knowing which of the old boxes fall in that bucket is a real answer to a real question - even though the underlying files are stubs.

The corpus documents itself as a **curated sample**, not the full 11e Space Marine roster. Epic Heroes in particular are largely absent. That is stated in the index and is the right call for a teaching repo.

---

## What blocks everything here

**The collection has still never been audited.** The inventory worksheet at `games/warhammer_40k_11e/armies/space_marines/Owned_Models_Inventory.md` is an empty template, unchanged since S5 shipped it with the identification procedure filled in.

Until it is filled:

- No research file can be prioritised over another with any confidence
- The nine `starter` files are a guess at a list, not a list
- The Chapter question above cannot be answered, so the army rule's real strength is unknown
- No `KB/units/` page can be written, because a unit page describes models someone owns

This is a **twenty-minute user task** gating every remaining piece of Space Marine content in the project. It is the single highest-leverage item on the board and has been since S5.

---

## Known gaps in the corpus

- **Wahapedia URL path.** All 78 files cite `wahapedia.ru/wh40k11ed/...`; S3-S5 and [[wahapedia]] cite `wh40k10ed`. Unresolved on both sides - see [[wahapedia]].
- **Local pack cross-check.** Every file records `pending`. Nothing here has been checked against the owned Space Marines faction pack.
- **Points.** No file carries a costed figure; each defers to the separate Munitorum Field Manual Marines PDF.
- **Zero `full` files**, so nothing in this corpus is safe to build a list from without opening a source first.

---

## Related pages

- [[space_marines]] - the faction, and the empty inventory that gates this
- [[oath_of_moment]] - the army rule the `chapter_unique` column threatens
- [[gladius_task_force]] - the learning detachment the `starter` tags aim at
- [[necrons_unit_index]] - the same overview for the primary army
- [[wahapedia]] - the URL-path question that affects all 78 files
- [[index]] · [[glossary]]
