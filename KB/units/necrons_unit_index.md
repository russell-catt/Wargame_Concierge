---
title: Necrons unit index (KB overview)
type: unit
system: warhammer_40k_11e
faction: Necrons
created: 2026-08-16
updated: 2026-08-16
sources: [games/warhammer_40k_11e/armies/necrons/units/Unit_Index.md, docs/handoffs/v1_scaffold/slices/S6_necrons_implementer.md]
confidence: draft
tags: [unit, necrons, index, s6, research_corpus, pointer]
---

# Necrons unit index (KB overview)

The KB's entry point into the 65-file Necron unit research corpus that S6 built under `games/`. This page is a **pointer and a health report**, not a copy of the corpus.

**The corpus itself:** [`games/warhammer_40k_11e/armies/necrons/units/Unit_Index.md`](../../games/warhammer_40k_11e/armies/necrons/units/Unit_Index.md) - one row per datasheet, with the Wahapedia URL and priority for each.

---

## Why this page is a pointer and not 65 KB pages

[`AGENTS.md`](../../AGENTS.md) Sec 4 gives `KB/units/` one page per datasheet in play terms. Sixty-five of those would duplicate a corpus that already exists, already carries its own schema, and is **mostly stubs**. Duplicating stubs produces two things to keep in sync and no new knowledge.

The rule this KB follows instead: **a unit earns a `KB/units/` page when it has real play content** - role, durability, threat range, how it dies - beyond what the research file already records. Three units are close to that bar today; the rest are not. See "What would earn a page" below.

---

## What S6 actually delivered

| Metric | Necrons |
|--------|---------|
| Index rows | 65 |
| Research files | 65 (counts match - QA verified) |
| Schema | [`units/_schema.md`](../../games/warhammer_40k_11e/armies/necrons/units/_schema.md) v1, 2026-08-16 |
| Research date | 2026-08-16 |

### Completeness, by the corpus's own field

| `completeness` | Count | What it means |
|----------------|-------|---------------|
| `full` | **3** | Profiles, weapons, keywords, and points captured |
| `partial` | 8 | Some fields filled, the rest marked `_Pending_` |
| `stub` | **54** | Name, slug, Wahapedia URL, and placeholders |

**Eighty-three percent of this corpus is a scaffold**, and it says so honestly in its own frontmatter. That is a reasonable S6 outcome - the roster is enumerated and every entry has a verification route - but it is not a researched army. Treat the corpus as a **map of where to look**, not as answers.

### Priority, by the corpus's own field

| `priority` | Count | Meaning |
|------------|-------|---------|
| `starter` | 3 | Owned models, needed for the first games |
| `inventory_candidate` | 10 | Possible Hierotek Circle contents, pending photo ID |
| `roster` | 52 | Catalogued for completeness |

The three `starter` files are the three `full` files, and they are the three units the owner actually owns: **Necron Warriors**, **Immortals**, **Canoptek Scarab Swarms**. The priority tagging and the research effort line up, which is the right shape for a first pass.

---

## The units that matter today

Ordered by what unblocks a game, not by datasheet order.

| Unit | Owned | Research | Where it is used |
|------|-------|----------|------------------|
| Necron Warriors | 10, unassembled | `full` | Battleline in both detachment paths - [[cryptek_conclave]] wants them most |
| Immortals | 5, unassembled | `full` | Battleline; the Plasmancer's intended bodyguard unit |
| Canoptek Scarab Swarms | 3, unassembled | `full` | Objective-flippers; the cheap [[canoptek_court]] Matrix tool |
| Plasmancer, Technomancer, Chronomancer, Psychomancer, Geomancer, Apprentek, Deathmarks, Cryptothralls | **Unknown** | `partial` | The `inventory_candidate` set - all blocked on the **Hierotek Circle photo ID** |
| Canoptek Wraiths, Canoptek Doomstalker | No | `stub` | The two units [[canoptek_court]] is built around, and neither is owned or researched |

The awkward shape from [[necrons]] survives into the research corpus unchanged: **the best-researched units are unassembled, and the game-ready models are still unidentified.**

---

## What would earn a `KB/units/` page

A unit graduates from this pointer to its own page when all three hold:

1. Its research file is `full`, **and**
2. The models exist and can be put on a table, **and**
3. There is play content to write - how it is used, how it dies, what it pairs with - that is not already in [[cryptek_conclave]], [[canoptek_court]], or the shipping starter lists.

On today's collection, **nothing clears condition 2.** The first page this KB should expect to write is `necron_warriors.md`, and it should wait until the box is built and the unit has been played.

---

## Known gaps in the corpus

Recorded here so a future session does not rediscover them.

- **Wahapedia URL path.** Every one of the 65 files cites a `wahapedia.ru/wh40k11ed/...` URL. The rest of the repo - S3, S4, S5, and [[wahapedia]] - cites `wh40k10ed`. **One of the two is wrong and neither has been confirmed.** See [[wahapedia]].
- **Local pack cross-check.** The three `full` files record `partial`; the other 62 record `pending`. No unit in this corpus has been fully cross-checked against the owned faction pack.
- **Points.** Captured only in the three `full` files, spot-checked against Munitorum Field Manual v1.2. Everything else says "verify Munitorum".
- **Statlines.** The three `full` files carry model profile and weapon profile tables. [`AGENTS.md`](../../AGENTS.md) Sec 10 and [`units/README.md`](README.md) both forbid transcribing statlines. Flagged for the Coordinator in the L2 report; `games/` is not the Librarian's surface to edit.
- **Hierotek Circle.** Ten `inventory_candidate` files are placeholders for a box nobody has photographed. This is still the cheapest unblock in the project.

---

## Related pages

- [[necrons]] - the faction, the ownership record, and both detachment paths
- [[canoptek_court]] · [[cryptek_conclave]] - the detachments these units are chosen for
- [[space_marines_unit_index]] - the same overview for the opposing army
- [[wahapedia]] - the URL-path question that affects all 65 files
- [[reanimation_protocols]] - the army rule every unit here has
- [[index]] · [[glossary]]
