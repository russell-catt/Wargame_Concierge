<!--
FILE: games/warhammer_40k_11e/README.md
VERSION: v1.0 (2026-08-16)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, slice S2)

DOCUMENT_TYPE: Game System Overview
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: Warhammer 40,000 — 11th Edition
REFERENCE_STATUS: Active — scaffold phase

SOURCES:
  - reference/Source_Library.md
  - docs/Game_System_Scaffold.md (Section B)
  - docs/Project_Planning.md Sec 3

PURPOSE:
  Entry point for the first worked example game system. States edition scope,
  vocabulary mapping, and how to learn 40K using this subtree.

PRIMARY_AUDIENCE:
  - Parent (Necrons) and son (Space Marines) learning together
  - AI sessions building rules and army content

KEY_SECTIONS_EXPECTED:
  - Edition scope
  - Vocabulary mapping
  - How to learn
  - Subtree map

UPDATE_TRIGGER:
  Update when edition changes, new factions are added, or scaffold sections
  are promoted from KB.
-->

# Warhammer 40,000 — 11th Edition

First worked example in Wargame_Concierge. **Edition in scope: 11th Edition (11e).**

Two forces in this track: **Necrons** (parent) and **Space Marines** (son).

---

## Vocabulary mapping

This subtree uses Games Workshop terms. Mapping from the [game-agnostic scaffold](../../docs/Game_System_Scaffold.md):

| Generic term | 40K 11e term |
|--------------|--------------|
| Force | Army |
| Force organisation | Detachment |
| Force-wide rule | Army rule |
| Sub-list rule package | Detachment rule (+ enhancements, stratagems) |
| Unit entry | Datasheet |
| Round structure | Battle round (movement, shooting, charge, fight phases) |
| Scoring | Primary objectives, victory points, battle tactics |
| Force size | Points (typically 500 → 1,000 for learning) |

---

## How to learn

1. **Sources first** — read [`reference/Source_Library.md`](../../reference/Source_Library.md) for local PDF paths and living web URLs. Cross-check every rules claim.
2. **Rules spine** — `rules/` documents (stubs now; full content in S3) explain what a game is, turn order, and key concepts.
3. **Setup** — `setup/` documents (stubs now; full content in S3) cover board size, deployment, and terrain.
4. **Pick a force** — start with [`armies/necrons/README.md`](armies/necrons/README.md) or [`armies/space_marines/README.md`](armies/space_marines/README.md).
5. **Match reality** — always check [`Owned_Models_Inventory.md`](armies/necrons/Owned_Models_Inventory.md) (Necrons) before building a list from what you actually own.

**Recommended first game size:** 250–500 points using game-ready models only.

---

## Subtree map

| Path | Status | Purpose |
|------|--------|---------|
| [`rules/README.md`](rules/README.md) | Stub | Rules teaching spine |
| [`setup/README.md`](setup/README.md) | Stub | Board and terrain setup |
| [`armies/necrons/`](armies/necrons/) | Partial | Parent's Necron force |
| [`armies/space_marines/`](armies/space_marines/) | Partial | Son's Space Marine force |

---

## Change Log
- v1.0 (2026-08-16): Initial scaffold (slice S2). README, army folders, Necron import.

## Attribution
- Project: Wargame_Concierge
- Maintainer: Russell Catt

## Rising Tide Notes
- This document follows Rising Tide documentation standards.
- Must remain understandable, reproducible, and reusable.