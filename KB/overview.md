---
title: Overview
type: overview
system: warhammer_40k_11e
created: 2026-08-16
updated: 2026-08-16
sources: [necron_lists_owner_notes, source_library, local_library_pointers, wahapedia, warhammer_community]
confidence: draft
tags: [overview, synthesis, warhammer_40k, necrons, space_marines]
---

# Knowledge Base Overview

The working synthesis of everything in this KB. Updated after any ingest that shifts the big picture.

---

## What Wargame_Concierge is

A personal **wargame concierge**: a knowledge base that helps its owner learn a tabletop wargame, build lists from models actually owned, and play games without constantly flipping through rulebooks.

It is built on the Karpathy "LLM Wiki" pattern (see [`reference/llm-wiki.md`](../reference/llm-wiki.md)): immutable sources in `raw/`, an LLM-maintained knowledge layer in `KB/`, and player-facing content promoted into `docs/` and `games/`. The point is **compounding** - each source read and each question answered gets filed, so the same ground is never re-covered from scratch.

The project is **game-agnostic by design**. `games/` holds one subtree per system, and the KB entity types (Faction, Detachment, Unit, Setup/Mission, Concept, Analysis) are deliberately generic enough to carry a second system later. Warhammer 40,000 is the first worked example, not the only intended one.

---

## First system: Warhammer 40,000, 11th Edition

**Warhammer 40,000 11th Edition** is the first and currently only system in scope. Everything in the KB today should carry `system: warhammer_40k_11e` in its frontmatter.

The edition is **new**, which shapes how this KB is written:

- Most rules knowledge starts at `confidence: unverified` or `draft` and gets promoted only after a cross-check
- Anything carried over from 10th Edition is suspect until confirmed - edition drift is an explicit lint category
- Living references (Warhammer Community, Wahapedia) move under us, so every rules claim records a **retrieval date**

**Audience:** a beginner learning the game. Content should teach the reasoning behind a rule or a play, not just state it.

---

## Armies in scope

Two factions, chosen because they are the models on hand.

### Necrons - primary

The learning army. Ownership confirmed 2026-08-16 (see the Preflight notes in [`track_in.md`](../docs/handoffs/v1_scaffold/track_in.md)):

| Models | Count | State |
|--------|-------|-------|
| Necron Warriors | 10 | Purchased, unassembled |
| Canoptek Scarab Swarms | 3 | Purchased, unassembled |
| Immortals | 5 | Purchased, unassembled |
| Hierotek Circle (used set) | 1 set | Game ready; datasheet mapping pending photo ID |

Full page: [[necrons]]. Two open threads worth carrying forward:

- **Hierotek Circle contents are not yet identified.** The set is game-ready and therefore the preferred starting point for early games, but its models still need to be mapped to 40K datasheets from user photos.
- **Everything else needs building before it can be played.** Early teaching content should account for build-before-play, not assume a painted army.

The collection has an awkward shape worth stating plainly: **the only table-ready models are the ones nobody has identified, and the only identified models are still on sprue.** Both halves are blocked, for opposite reasons. The photo ID is the cheaper of the two to unblock.

Two detachment paths are costed from this collection - [[canoptek_court]] and [[cryptek_conclave]]. On the models actually owned, the Conclave is the shorter route to a legal list, because Warriors and Immortals are exactly its battleline and the Hierotek Circle plausibly supplies the Cryptek character. That is a hypothesis resting on an unopened box, not a recommendation.

An earlier blueprint assumed **Kill Team: Tomb World**. That is **superseded and historical** - it does not describe current ownership and should not be treated as such.

### Space Marines - secondary

The comparison and opponent army, played by the owner's son. Used to teach contrast: a straightforward, forgiving faction set against the Necrons' resilience mechanics, with [[gladius_task_force]] as the target detachment. Built from **existing older kits**, so legacy and Firstborn datasheets stay in scope.

**No ownership inventory recorded yet** - the worksheet exists and is empty. See [[space_marines]]. This is the largest single unknown on that side, and it gates any S5 content: a starter list cannot be written for an uncatalogued collection.

---

## Current state

| Metric | Value |
|--------|-------|
| Sources ingested | 5 (2 read in full, 3 registered only) |
| KB entity pages | 15 |
| KB core pages | 6 (index, log, overview, glossary, changelog, ingest_procedure) |
| Glossary terms | 32 - 0 game terms `verified` |
| Last ingest | 2026-08-16 (L1) |
| Last lint | - (L2) |
| Schema version | AGENTS.md v1.0 (2026-08-16) |

The KB was bootstrapped in slice **L0** and took its first real ingest in **L1**, both on 2026-08-16. The ingest contract now has a worked example behind it rather than only a procedure.

**What that ingest did and did not establish.** It read the owner's Necron notes and the source catalog in full, and it registered the two living web references without opening them. It produced faction, detachment, and concept pages that are honest about resting on one planning document. It did **not** read a single rules document: the core rules, both faction packs, the terrain PDFs, and the points manuals are all sitting on the owner's disk, catalogued in [[local_library_pointers]], unopened.

So the shape of the gap has changed. It is no longer "we do not have sources." It is **"we have not read the sources we have."** Rules and setup arrive in **S3**, faction starters in **S4** and **S5**, full unit research in **S6**, and a lint pass in **L2**.

---

## Key themes

Expect these to be the organizing ideas as content lands. They are hypotheses right now, not findings:

- **Resilience vs efficiency** - Necrons trade raw output for models that keep coming back; learning the army means learning when that trade pays
- **Objective play over kill count** - modern 40K is scored on objectives, so setup, screening, and scoring patterns matter more than damage tables
- **Build-before-play reality** - teaching content has to work for a partly unassembled collection
- **Edition freshness** - 11th Edition claims decay; the KB needs verification dates more than it needs volume

---

## Resolved in L1

- **Power Matrix is a Warhammer 40,000 term, not Kill Team.** L0 flagged the attribution as unresolved because the owner's Hierotek Circle is a Kill Team box. Two independent in-repo sources name it as the [[canoptek_court]] detachment rule. Corrected on [[power_matrix]] and in [[glossary]]; the Hierotek Circle and the rule are now formally unrelated.

The L0 flag is why this cost one ingest to fix rather than surfacing halfway through S4. Writing uncertainty down loudly is working.

---

## Open questions

- What are the actual contents of the Hierotek Circle set, and which 40K datasheets do they map to?
- What does Power Matrix actually *say* in 11th Edition? The name is settled; the wording is not.
- Which Necron detachment best suits a beginner with this specific model pool? [[cryptek_conclave]] is the current hypothesis, resting on an unopened box.
- What Space Marine ownership exists? The worksheet is empty and this gates all S5 content.
- Which 11th Edition rules genuinely changed from 10th, and which carried over unchanged?
- What is the target game size for early games (Combat Patrol, Incursion, Strike Force)?
- Do the Wahapedia URLs on a `wh40k10ed` path serve 11e content, or are they stale? See [[wahapedia]].
- Has a dataslate superseded the owned PDFs? Nothing records when they were downloaded, so this is currently unanswerable.

---

## Knowledge gaps

Areas with no real coverage. All but the last are blocked on **reading material the owner already has**:

- Core 11th Edition rules: turn sequence, phases, objective scoring - [[objective_control]] is a placeholder
- Deployment maps, terrain rules, and mission packs - no page exists
- Necron army rule detail - [[reanimation_protocols]] is `unverified`
- Space Marine army rule and detachment - [[oath_of_moment]] and [[gladius_task_force]] are `unverified` and `stub`
- Unit pages - none, deliberately: [[ingest_procedure]] puts core rules and setup first so unit pages have something to link to
- List-building from the owned pool - blocked on the Hierotek Circle photo ID, which no amount of reading fixes

---

## Related pages

- [[index]] - full catalog of KB pages
- [[glossary]] - terminology and Keyword entries
- [[inherited_docs_for_S3]] - what is stable enough to teach from
- [[necrons]] · [[space_marines]] - the two factions
- [[ingest_procedure]] - how sources become KB pages
- [[log]] - what has happened and when
- [`AGENTS.md`](../AGENTS.md) - schema source of truth
