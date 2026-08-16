---
title: Overview
type: overview
system: warhammer_40k_11e
created: 2026-08-16
updated: 2026-08-16
sources: []
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

Two open threads worth carrying forward:

- **Hierotek Circle contents are not yet identified.** The set is game-ready and therefore the preferred starting point for early games, but its models still need to be mapped to 40K datasheets from user photos.
- **Everything else needs building before it can be played.** Early teaching content should account for build-before-play, not assume a painted army.

An earlier blueprint assumed **Kill Team: Tomb World**. That is **superseded and historical** - it does not describe current ownership and should not be treated as such.

### Space Marines - secondary

The comparison and opponent army. Used to teach contrast: a straightforward, forgiving faction set against the Necrons' resilience mechanics. No ownership inventory recorded yet.

---

## Current state

| Metric | Value |
|--------|-------|
| Sources ingested | 0 |
| KB entity pages | 0 |
| KB core pages | 6 (index, log, overview, glossary, changelog, ingest_procedure) |
| Last ingest | - |
| Last lint | - |
| Schema version | AGENTS.md v1.0 (2026-08-16) |

The KB was bootstrapped in slice **L0** on 2026-08-16. The scaffolding, schema, and conventions exist; the content does not yet. Sources arrive in **S2**, rules and setup in **S3**, faction starters in **S4** and **S5**, and full unit research in **S6**.

---

## Key themes

Expect these to be the organizing ideas as content lands. They are hypotheses right now, not findings:

- **Resilience vs efficiency** - Necrons trade raw output for models that keep coming back; learning the army means learning when that trade pays
- **Objective play over kill count** - modern 40K is scored on objectives, so setup, screening, and scoring patterns matter more than damage tables
- **Build-before-play reality** - teaching content has to work for a partly unassembled collection
- **Edition freshness** - 11th Edition claims decay; the KB needs verification dates more than it needs volume

---

## Open questions

- What are the actual contents of the Hierotek Circle set, and which 40K datasheets do they map to?
- Which Necron detachment best suits a beginner with this specific model pool?
- What Space Marine ownership, if any, exists - or is Space Marines a purely theoretical opponent for now?
- Which 11th Edition rules genuinely changed from 10th, and which carried over unchanged?
- What is the target game size for early games (Combat Patrol, Incursion, Strike Force)?

---

## Knowledge gaps

Areas with no coverage at all yet. These are the ingest priorities:

- Core 11th Edition rules: turn sequence, phases, objective scoring
- Deployment maps, terrain rules, and mission packs
- Necron army rule, detachments, and the datasheets for the owned models
- Space Marine army rule and a comparable starter detachment
- List-building at a defined points level from the owned model pool

---

## Related pages

- [[index]] - full catalog of KB pages
- [[glossary]] - terminology and Keyword entries
- [[ingest_procedure]] - how sources become KB pages
- [[log]] - what has happened and when
- [`AGENTS.md`](../AGENTS.md) - schema source of truth
