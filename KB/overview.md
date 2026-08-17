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
| Cryptek Geomancer (Tomb World) | 1 | **Game ready** |
| Canoptek Tomb Crawlers (Tomb World) | 2 | **Game ready** |
| Canoptek Macrocytes (Tomb World) | 5 | **Game ready** |
| Necron Warriors (Tomb World squad) | 10 | **Game ready** |
| Canoptek Scarab Swarms (Tomb World set) | 3 | **Game ready** |
| Hierotek Circle (used set) | 1 set | Game ready; datasheet mapping pending photo ID |
| Necron Warriors (second squad) | 10 | Purchased, unassembled |
| Canoptek Scarab Swarms (second set) | 3 | Purchased, unassembled |
| Immortals | 5 | Purchased, unassembled |

**Totals:** 20 Warriors, 6 Scarab Swarms, plus the Geomancer, Tomb Crawlers, Macrocytes, Immortals, and the Hierotek Circle set.

Full page: [[necrons]]. Two open threads worth carrying forward:

- **Hierotek Circle contents are not yet identified.** The set is painted and fieldable, but its models still need mapping to 40K datasheets from user photos before it can appear in a list. It no longer gates the first game.
- **Three owned units still need building.** The second Warrior squad and second Scarab set are **assemble-to-expand** - they widen squads that already exist - while the Immortals are the one unit the collection cannot field at all until built.

The collection's shape, stated plainly: **there is a complete, painted, identified army available today.** The Kill Team: Tomb World units are the owner's preferred learning baseline, and everything else in the collection expands them.

Two detachment paths are costed from this collection - [[canoptek_court]] and [[cryptek_conclave]] - and Tomb World gives **both** of them a legal Phase 1 force, so the choice is no longer gated on a purchase or an identification. The Conclave stays the shorter route to a finished path, and it is now grounded in a real model rather than a hypothesis: the game-ready Geomancer is the Cryptek character it needs.

**Correction of record.** An earlier version of this KB recorded **Kill Team: Tomb World as not owned**, treated its lists as superseded history, and carried a standing rule against letting that content reach current advice. All of that was erroneous and is withdrawn. See the deprecated list in [[glossary]].

### Space Marines - secondary

The comparison and opponent army, played by the owner's son. Used to teach contrast: a straightforward, forgiving faction set against the Necrons' resilience mechanics, with [[gladius_task_force]] as the target detachment. Built from **existing older kits**, so legacy and Firstborn datasheets stay in scope.

**No ownership inventory recorded yet** - the worksheet exists and is empty. See [[space_marines]]. This is the largest single unknown on that side, and it gates any S5 content: a starter list cannot be written for an uncatalogued collection.

---

## Current state

| Metric | Value |
|--------|-------|
| Sources ingested | 5 (2 read in full, 3 registered only) |
| KB entity pages | 17 |
| KB core pages | 6 (index, log, overview, glossary, changelog, ingest_procedure) |
| Glossary terms | 36 - 24 game terms `verified` |
| Last ingest | 2026-08-16 (L1, `tomb_world_ownership` - ownership correction) |
| Last lint | 2026-08-16 (L2, `tomb_world_ownership` - full re-lint) |
| Schema version | AGENTS.md v1.0 (2026-08-16) |

The KB was bootstrapped in slice **L0** and took its first real ingest in **L1**, both on 2026-08-16. The ingest contract now has a worked example behind it rather than only a procedure.

**What that ingest did and did not establish.** It read the owner's Necron notes and the source catalog in full, and it registered the two living web references without opening them. It produced faction, detachment, and concept pages that are honest about resting on one planning document. It did **not** read a single rules document: the core rules, both faction packs, the terrain PDFs, and the points manuals are all sitting on the owner's disk, catalogued in [[local_library_pointers]], unopened.

So the shape of the gap has changed - twice. At L1 it was no longer "we do not have sources" but **"we have not read the sources we have."** That second gap has since closed on the shipping side: S3 read the core rules and setup, S4 and S5 read both faction packs and Munitorum Field Manual v1.2 for the faction starters, and S6 enumerated both unit rosters.

**The gap now is a back-fill gap.** The rules have been read into `games/`, not into `KB/`. The faction, detachment and concept pages here still mostly rest on the owner's planning notes, which is why they remain `draft` and `unverified` while the shipping teaching content carries verified rule text. Where the two disagree, the shipping content is newer and better sourced. Closing that gap - re-ingesting the shipping pages back into `KB/` - is the largest single piece of Librarian work outstanding.

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

## Resolved in L1 - `tomb_world_ownership` (2026-08-16)

- **Kill Team: Tomb World is owned and game-ready.** Five datasheets' worth of assembled, painted, identified models. The KB had recorded the box as *not owned* and its lists as superseded, which was wrong in the other direction from the Power Matrix error: this time the KB was confidently denying something the owner has on a shelf.
- **The "do not let Tomb World leak" rule is retired.** It was written as a guardrail against stale data and became the stale data itself. It now exists only as a deprecated-claim row, so it cannot return as guidance.
- **Dual Warriors and Scarabs recorded.** 20 Warriors and 6 Scarab Swarms owned, half of each game-ready and half on sprue.

The lesson is the mirror image of the Power Matrix one. A loud flag made that error cheap to fix; a *negative* ownership claim written as settled fact propagated across the KB before anyone checked it. Inventory claims should carry the same "verify against the owner" discipline as rules claims.

---

## Open questions

- What are the actual contents of the Hierotek Circle set, and which 40K datasheets do they map to?
- What does Power Matrix actually *say* in 11th Edition? The name is settled; the wording is not.
- Which Necron detachment best suits a beginner with this specific model pool? [[cryptek_conclave]] is the current hypothesis - now resting on owned, game-ready models rather than on an unopened box, so what remains unknown is the detachment rules, not the inventory.
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
- List-building from the owned pool - **unblocked** for the Tomb World units, which have known datasheets; only the Hierotek Circle half still waits on a photo ID, which no amount of reading fixes

---

## Related pages

- [[index]] - full catalog of KB pages
- [[glossary]] - terminology and Keyword entries
- [[inherited_docs_for_S3]] - what is stable enough to teach from
- [[necrons]] · [[space_marines]] - the two factions
- [[ingest_procedure]] - how sources become KB pages
- [[log]] - what has happened and when
- [`AGENTS.md`](../AGENTS.md) - schema source of truth
