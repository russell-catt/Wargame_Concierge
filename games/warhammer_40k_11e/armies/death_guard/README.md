<!--
FILE: games/warhammer_40k_11e/armies/death_guard/README.md
VERSION: v0.5.0 (2026-08-18)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, slice S5 - kill_team_2024_scaffold)

DOCUMENT_TYPE: Cross-Link Stub (NOT a faction package)
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: Warhammer 40,000 - 11th Edition
FACTION: Death Guard
REFERENCE_STATUS: Stub - out of scope this track. No 40K rules content in this file.

SOURCES:
  - games/kill_team_2024/teams/plague_marines/Owned_Models_Inventory.md (the Death Guard / 40K sync note that created this stub)
  - docs/handoffs/kill_team_2024_scaffold/track_in.md (cross-game policy - "Inventories sync" row)
  - games/warhammer_40k_11e/README.md (locked scope: Necrons + Space Marines only, this track)

PURPOSE:
  A minimal cross-link so a future 40K Death Guard track has somewhere to
  start from. Records that the Plague Marines Kill Team models are the
  same physical miniatures as a 40K Death Guard force, with base-size and
  dual-legality left honestly unresolved. Deliberately not a faction
  package - no army rule guide, no detachment, no starter list, no unit
  research exists here.

UPDATE_TRIGGER:
  Replace this stub with a real faction package only if Death Guard is
  explicitly brought into 40K scope by a future track. Until then, update
  only the sync fields below if the Kill Team side changes.
-->

# Death Guard - cross-link stub (not a full army package)

**This is not a faction package.** The `kill_team_2024_scaffold` track locks Warhammer 40,000 scope to **Necrons and Space Marines only** (see [`../../README.md`](../../README.md)). This file exists solely so the Plague Marines Kill Team miniatures - which are Death Guard models and could in principle field a 40K army - have a documented cross-link rather than silence.

Do not add an army rule guide, detachment guide, starter lists, or unit research here without a track that explicitly brings Death Guard into 40K scope. That would invent a full army tree this slice was told not to build.

---

## Cross-game sync status

| Field | Value |
|-------|-------|
| **Same physical models as** | [`../../../kill_team_2024/teams/plague_marines/`](../../../kill_team_2024/teams/plague_marines/) - Kill Team Plague Marines |
| **40K ruled-in status** | `pending / N/A this track` |
| **Base size / dual-legality** | `pending check` - Kill Team datacards show 32mm bases; exact 40K datasheet mapping and current basing kit unconfirmed |
| **Assembly / paint** | `pending check` - see the Kill Team side's [`Owned_Models_Inventory.md`](../../../kill_team_2024/teams/plague_marines/Owned_Models_Inventory.md) |
| **40K rules content in this folder** | None. Kill Team and 40K rules stay separate per the track's cross-game policy - see [`../../../kill_team_2024/README.md`](../../../kill_team_2024/README.md) |

---

## If Death Guard ever enters 40K scope

Follow [`docs/Game_System_Scaffold.md`](../../../../docs/Game_System_Scaffold.md) Section C from scratch - README, army rule guide, detachment guide, `Owned_Models_Inventory.md`, starter lists, two-page laminate, unit index and research. Do not copy this stub forward; it has none of that content.

---

## Related pages

- [`../../README.md`](../../README.md) - 40K subtree entry point (locked scope: Necrons, Space Marines)
- [`../../../kill_team_2024/teams/plague_marines/README.md`](../../../kill_team_2024/teams/plague_marines/README.md) - the full Kill Team package this stub cross-links to
- [`../../../kill_team_2024/teams/plague_marines/Owned_Models_Inventory.md`](../../../kill_team_2024/teams/plague_marines/Owned_Models_Inventory.md) - the Death Guard / 40K sync note

---

## Change Log

- v0.5.0 (2026-08-18): Project-wide semver snapshot (x.y.z).
- v0.1 (2026-08-17): Initial minimal cross-link stub (slice S5, `kill_team_2024_scaffold`) - sync status fields only, explicitly not a faction package.

## Attribution

- Project: Wargame_Concierge
- Maintainer: Russell Catt
- Warhammer 40,000 is a trademark of Games Workshop Limited.

## Rising Tide Notes

- This document follows Rising Tide documentation standards.
- This stub intentionally contains no rules content - it is a sync pointer, not a package.
