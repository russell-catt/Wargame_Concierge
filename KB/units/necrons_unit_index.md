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
| `starter` | 3 | Tagged as the owned models needed for the first games |
| `inventory_candidate` | 10 | Tagged as possible Hierotek Circle contents, pending photo ID |
| `roster` | 52 | Catalogued for completeness |

The three `starter` files are the three `full` files - **Necron Warriors**, **Immortals**, **Canoptek Scarab Swarms** - and the research effort lines up with the tagging, which was the right shape for a first pass.

**But the tagging is now wrong.** It was built against an inventory that recorded Kill Team: Tomb World as not owned, so three units the owner has assembled and painted sit in `inventory_candidate` as if they were unidentified guesses: **Geomancer** (`partial`), **Canoptek Tomb Crawlers** (`stub`), and **Canoptek Macrocytes** (`stub`). They are owned, game-ready, and identified. Re-tagging them `starter` is a `games/` edit, not a KB one - flagged for the Coordinator.

---

## The units that matter today

Ordered by what unblocks a game, not by datasheet order.

| Unit | Owned | Research | Where it is used |
|------|-------|----------|------------------|
| Necron Warriors | 20 - 10 **game ready**, 10 on sprue | `full` | Battleline in both detachment paths - [[cryptek_conclave]] wants them most |
| Canoptek Scarab Swarms | 6 - 3 **game ready**, 3 on sprue | `full` | Objective-flippers; the cheap [[canoptek_court]] Matrix tool |
| Cryptek Geomancer | 1, **game ready** | `partial` | The Cryptek character [[cryptek_conclave]] is built on; leads the Warrior squad in both Phase 1 lists |
| Canoptek Tomb Crawlers | 2, **game ready** | `stub` | Phase 1 screening in both paths |
| Canoptek Macrocytes | 5, **game ready** | `stub` | Phase 2 in both paths. Note the owner's *Ignores Cover* claim was **disproven** in S4 - see [[glossary]] |
| Immortals | 5, unassembled | `full` | Battleline; the Plasmancer's intended bodyguard unit. The one owned unit that must be built before it can be fielded |
| Plasmancer, Technomancer, Chronomancer, Psychomancer, Apprentek, Deathmarks, Cryptothralls | **Unknown** | `partial` | The `inventory_candidate` set - still blocked on the **Hierotek Circle photo ID** |
| Canoptek Wraiths, Canoptek Doomstalker | No | `stub` | The two units [[canoptek_court]] is built around, and neither is owned or researched |

**The research corpus is now mis-aligned with the collection.** Three units are game-ready and identified but thinly researched: the Geomancer is `partial` and the Tomb Crawlers and Macrocytes are `stub`, because S6 tagged research priority against an inventory that wrongly excluded Kill Team: Tomb World. The units most likely to hit a table first are not the best-researched ones. Re-prioritising those five Tomb World datasheets to `starter` is the highest-value follow-up on this corpus, and it belongs to the corpus owner under `games/`, not to the Librarian.

---

## What would earn a `KB/units/` page

A unit graduates from this pointer to its own page when all three hold:

1. Its research file is `full`, **and**
2. The models exist and can be put on a table, **and**
3. There is play content to write - how it is used, how it dies, what it pairs with - that is not already in [[cryptek_conclave]], [[canoptek_court]], or the shipping starter lists.

On today's collection, **five units clear condition 2** - the Tomb World Geomancer, Tomb Crawlers, Macrocytes, Warriors, and Scarab Swarms are assembled, painted, and identified. Only **Necron Warriors** and **Canoptek Scarab Swarms** also clear condition 1, so those are the first two pages this KB should expect to write, and they should wait until the units have actually been played. The Geomancer, Tomb Crawlers, and Macrocytes need their research files filled first.

---

## Known gaps in the corpus

Recorded here so a future session does not rediscover them.

- **Wahapedia URL path.** Every one of the 65 files cites a `wahapedia.ru/wh40k11ed/...` URL. The rest of the repo - S3, S4, S5, and [[wahapedia]] - cites `wh40k10ed`. **One of the two is wrong and neither has been confirmed.** See [[wahapedia]].
- **Local pack cross-check.** The three `full` files record `partial`; the other 62 record `pending`. No unit in this corpus has been fully cross-checked against the owned faction pack.
- **Points.** Captured only in the three `full` files, spot-checked against Munitorum Field Manual v1.2. Everything else says "verify Munitorum".
- **Statlines.** The three `full` files carry model profile and weapon profile tables. [`AGENTS.md`](../../AGENTS.md) Sec 10 and [`units/README.md`](README.md) both forbid transcribing statlines. Flagged for the Coordinator in the L2 report; `games/` is not the Librarian's surface to edit.
- **Hierotek Circle.** The `inventory_candidate` set is placeholders for a box nobody has photographed. Still worth doing, but it no longer gates a first game.
- **Priority drift from the Tomb World correction.** Three of those ten candidates - Geomancer, Canoptek Tomb Crawlers, Canoptek Macrocytes - are in fact **owned and game-ready** Kill Team: Tomb World models. Their research is thin (`partial`, `stub`, `stub`) precisely because the inventory they were prioritised against was wrong. This is the most consequential corpus gap today.

---

## Related pages

- [[necrons]] - the faction, the ownership record, and both detachment paths
- [[canoptek_court]] · [[cryptek_conclave]] - the detachments these units are chosen for
- [[space_marines_unit_index]] - the same overview for the opposing army
- [[wahapedia]] - the URL-path question that affects all 65 files
- [[reanimation_protocols]] - the army rule every unit here has
- [[index]] · [[glossary]]
