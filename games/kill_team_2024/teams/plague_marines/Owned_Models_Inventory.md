<!--
FILE: games/kill_team_2024/teams/plague_marines/Owned_Models_Inventory.md
VERSION: v0.5.0 (2026-08-18)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, slice S5)

DOCUMENT_TYPE: Inventory / Worksheet Template
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: Kill Team - 2024 / 3rd Edition (KT24)
TEAM: Plague Marines
REFERENCE_STATUS: Worksheet - unfilled. Assembly/paint state pending user confirmation; no photo audit this slice.

SOURCES:
  - games/kill_team_2024/teams/_Owned_Teams_Inventory.md (track-level ownership ledger)
  - games/kill_team_2024/teams/plague_marines/operatives/Operatives_Index.md (the 7 named operatives to check off)
  - docs/handoffs/kill_team_2024_scaffold/track_in.md (Preflight lock - "pending check" default; S10 photo gate)

PURPOSE:
  Physical model checklist for the Plague Marines kill team, and the
  Death Guard / 40K sync note this slice is responsible for. Every list
  or roster document in this folder must be checked against this file.

UPDATE_TRIGGER:
  Update when models are assembled, painted, or photo-confirmed (S10).
  Update the 40K sync section if a Death Guard 40K army ever enters scope.
-->

# Plague Marines - Owned Models Inventory

**Status:** worksheet - **not yet filled in.** No photo audit has run this slice (2026-08-17); every row below defaults to `pending check` per the track's Preflight lock, exactly like the other two priority teams.

Record **assembly and paint state**, not just counts - "owned but unassembled" and "game ready" lead to different advice for a first game.

---

## Game-ready (table today)

| Operative | Qty | Assembly | Paint | Notes |
|-----------|-----|----------|-------|-------|
| *(fill in)* | | | | |

## Owned - build before play

| Operative | Qty | Assembly | Paint | Notes |
|-----------|-----|----------|-------|-------|
| *(fill in)* | | | | |

## Owned but unidentified

Models that exist physically but have not yet been matched to a named operative from [`operatives/Operatives_Index.md`](operatives/Operatives_Index.md).

| Item | Why it is here | What would resolve it |
|------|-----------------|------------------------|
| *(fill in)* | | |

## Explicitly NOT owned

| Item | Status | Notes |
|------|--------|-------|
| *(fill in)* | | |

---

## How to do the audit in one sitting

1. Lay out every Plague Marine model, including anything on sprue.
2. Match each one against the seven named operatives in [`operatives/Operatives_Index.md`](operatives/Operatives_Index.md) - Champion, Bombardier, Fighter, Heavy Gunner, Icon Bearer, Malignant Plaguecaster, Warrior. Team selection allows one of each; there is no "extra Warriors" pile the way a 40K squad has spare bodies.
3. Photograph anything unidentified - this feeds **S10**, which is user-gated on exactly these photos.
4. Fill in the tables above, then open [`Starter_Roster.md`](Starter_Roster.md) to tag roster slots against what actually exists.

---

## Death Guard / 40K sync note

**This is the S5 deliverable required by the track's cross-game policy** (see [`../../../../docs/handoffs/kill_team_2024_scaffold/track_in.md`](../../../../docs/handoffs/kill_team_2024_scaffold/track_in.md), "Inventories sync" row).

| Field | Value |
|-------|-------|
| **Faction** | Death Guard (Chaos Space Marines subfaction) - also playable in Warhammer 40,000 |
| **Existing 40K Death Guard inventory in this repo?** | **No.** The locked 40K track ([`../../../warhammer_40k_11e/README.md`](../../../warhammer_40k_11e/README.md)) covers Necrons and Space Marines only - no Death Guard army folder was in scope |
| **40K ruled-in status** | `pending / N/A this track` - there is nothing to sync these models *into* yet |
| **Base size / dual-legality** | `pending check` - the Wahapedia datacards list every operative on a 32mm base, matching standard Chaos Space Marine basing, but confirming the exact 40K datasheet mapping, points cost, and current basing kit is unresolved |
| **Assembly / paint** | `pending check` - see the audit tables above |
| **Cross-link created this slice** | [`../../../warhammer_40k_11e/armies/death_guard/README.md`](../../../warhammer_40k_11e/armies/death_guard/README.md) - a **minimal stub**, explicitly not a full 40K army tree, pointing back here |

**Why not build the full Death Guard 40K tree now:** the track lock names exactly two 40K forces this session (Necrons, Space Marines). Inventing army rule guides, detachments, or starter lists for a third faction that was never scoped would contradict that lock. The stub exists so a future session that *does* pick up Death Guard in 40K has a starting cross-link instead of nothing.

---

## Inventory rules

1. **Game-ready** = assembled, based, and fieldable under current KT24 rules.
2. **Build before play** = purchased but not yet assembled - never list it in a "play tonight" roster.
3. Team selection allows **one of each of the seven named operatives** - there is no shopping list for duplicates the way a 40K squad has spare models.
4. When Plague Marines are photo-identified (S10), replace the `pending check` rows with confirmed data and update `cross_check_status` in [`operatives/Operatives_Index.md`](operatives/Operatives_Index.md).
5. This file is the source of truth the Death Guard 40K stub cross-links to - keep them consistent if either changes.

---

## Related pages

- [`operatives/Operatives_Index.md`](operatives/Operatives_Index.md) - the seven operatives to check off
- [`Starter_Roster.md`](Starter_Roster.md) - roster built against this inventory
- [`README.md`](README.md) - package entry point
- [`../_Owned_Teams_Inventory.md`](../_Owned_Teams_Inventory.md) - track-level ownership ledger (10 teams)
- [`../../../warhammer_40k_11e/armies/death_guard/README.md`](../../../warhammer_40k_11e/armies/death_guard/README.md) - the minimal 40K cross-link stub

---

## Change Log

- v0.5.0 (2026-08-18): Project-wide semver snapshot (x.y.z).
- v1.0 (2026-08-17): Initial worksheet (slice S5) - empty audit tables, the Death Guard / 40K sync note (no existing 40K inventory, ruled-in `pending/N/A this track`, base size `pending check`), and the minimal 40K stub cross-link.

## Attribution

- Project: Wargame_Concierge
- Maintainer: Russell Catt
- Kill Team and Warhammer 40,000 are trademarks of Games Workshop Limited. This document is a personal teaching paraphrase and reproduces no publisher text or statlines.

## Rising Tide Notes

- This document follows Rising Tide documentation standards.
- **Verify before you play.** No ownership has been assumed or invented in this worksheet.
