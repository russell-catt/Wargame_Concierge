<!--
FILE: games/warhammer_40k_11e/README.md
VERSION: v0.5.1 (2026-08-18)
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

**Personal use only — this project must never be sold.**

**Rules quoting (40K rules/setup only):** [`rules/`](rules/) and [`setup/`](setup/) may reproduce **verbatim** WarCom-**free** Core text (and matching local `C:\Personal\40K\rules\eng_*`) with filename + page + **rule ID**. **Codex wall:** [`armies/`](armies/) stays teaching paraphrase — never quote Codex / Faction Pack / paid army rules. **Hierarchy:** Core PDF is baseline; dated `eng_*` stamps supersede on the same topic; omission is not a patch. Citation spine: [`rules/Core_Rules_Quotes.md`](rules/Core_Rules_Quotes.md).

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
2. **Rules spine** — `rules/` teaching paraphrase plus [`rules/Core_Rules_Quotes.md`](rules/Core_Rules_Quotes.md) for numbered Core IDs.
3. **Setup** — `setup/` documents cover board size, deployment, and terrain (IDs cited; Event Companion inventoried, not dumped).
4. **Pick a force** — start with [`armies/necrons/README.md`](armies/necrons/README.md) or [`armies/space_marines/README.md`](armies/space_marines/README.md).
5. **Match reality** — always check [`Owned_Models_Inventory.md`](armies/necrons/Owned_Models_Inventory.md) (Necrons) before building a list from what you actually own.

**Recommended first game size:** 250–500 points using game-ready models only.

---

## Subtree map

| Path | Status | Purpose |
|------|--------|---------|
| [`rules/README.md`](rules/README.md) | Active | Rules teaching spine + numbered quote appendix |
| [`setup/README.md`](setup/README.md) | Stub | Board and terrain setup |
| [`armies/necrons/`](armies/necrons/) | Partial | Parent's Necron force |
| [`armies/space_marines/`](armies/space_marines/) | Partial | Son's Space Marine force |
| [`armies/adepta_sororitas/`](armies/adepta_sororitas/) | **Ownership stub only** | Metal Sisters + Celestian Insidiants declared 2026-08-22; **unpainted**; no teaching package yet |
| [`armies/death_guard/`](armies/death_guard/) | **Cross-link stub only** | Not in 40K teaching scope — pointer for Plague Marines KT miniatures ([`kill_team_2024` track](../../docs/handoffs/kill_team_2024_scaffold/track_in.md)); no army package |

---

## Change Log
- v0.5.2 (2026-08-22): Adepta Sororitas ownership stub (metal + Celestian Insidiants); unpainted.
- v0.5.1 (2026-08-18): WarCom-free quote exception for `rules/` + `setup/`; Codex wall on `armies/`; Core_Rules_Quotes link (track `40k_warcom_quotes`).
- v0.5.0 (2026-08-18): Project-wide semver snapshot (x.y.z).
- v1.1 (2026-08-17): Noted Death Guard folder as KT cross-link stub only (slice S5, kill_team_2024_scaffold) — locked 40K forces remain Necrons + Space Marines.
- v1.0 (2026-08-16): Initial scaffold (slice S2). README, army folders, Necron import.

## Attribution
- Project: Wargame_Concierge
- Maintainer: Russell Catt

## Rising Tide Notes
- This document follows Rising Tide documentation standards.
- Must remain understandable, reproducible, and reusable.