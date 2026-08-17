<!--
FILE: games/kill_team_2024/teams/_Owned_Teams_Inventory.md
VERSION: v1.3 (2026-08-17)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, slice S3; slice S4 Canoptek Circle row update; slice S5 Plague Marines row update; slice S6 Angels of Death row update)

DOCUMENT_TYPE: Inventory / Checklist
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: Kill Team — 2024 / 3e (KT24)
REFERENCE_STATUS: Active — scaffold phase; dual-legality fields pending audit

SOURCES:
  - raw/pointers/kill_team_2024_teams.md (10 team PDFs, verified 2026-08-17)
  - docs/handoffs/kill_team_2024_scaffold/track_in.md (ownership lock)
  - games/warhammer_40k_11e/armies/necrons/Owned_Models_Inventory.md (Hierotek + Tomb World cross-ref)

PURPOSE:
  Master inventory for all 10 owned Kill Team 2024 teams. Tracks guide priority,
  assembly/paint state, 40K ruled-in status, and base-size / dual-legality honesty.

UPDATE_TRIGGER:
  Update when teams are assembled, painted, photo-IDed, or synced into 40K inventories
  (S4–S6 for priority teams; Hierotek photo ID when photos arrive).
-->

# Owned Kill Team 2024 — Teams Inventory

**As of 2026-08-17.** Ten team-rule PDFs confirmed under `C:\Personal\Kill Team\kill_team_2024\Teams\`. Path catalog: [`raw/pointers/kill_team_2024_teams.md`](../../../raw/pointers/kill_team_2024_teams.md).

**Vocabulary:** Kill Team uses **team / operative**, not army / unit. Rules for KT and Warhammer 40,000 stay separate even when the same physical models appear in both games.

---

## Dual-legality reminder

| Concept | Meaning |
|---------|---------|
| **Owned** | You have the team PDF and (usually) the miniatures |
| **Dual-legal** | The same model on its current base is tournament-legal in **both** KT and 40K |
| **Pending check** | Base size, kit age, or datasheet mapping not yet audited — **do not assume dual-legality** |

Ownership does not equal dual-legality. S4–S6 and photo audits fill in the `pending check` cells.

---

## Team roster (10)

| Team | Folder | Priority | Assembly / paint | 40K ruled-in | Base size / dual-legality | Team PDF |
|------|--------|----------|------------------|--------------|----------------------------|----------|
| **Angels of Death** | [`angels_of_death/`](angels_of_death/) | **Full guide — S6 complete** | pending check | **known** — mapped to Space Marine Captain/Intercessor-family units in 40K inventory | pending check | [Teams pointer](../../../raw/pointers/kill_team_2024_teams.md) |
| **Canoptek Circle** | [`canoptek_circle/`](canoptek_circle/) | Full guide — **S4 complete** | Game ready — Tomb World box (assembled & painted) | Known — Geomancer, Tomb Crawlers, Macrocytes; see [40K Necron inventory](../../warhammer_40k_11e/armies/necrons/Owned_Models_Inventory.md) | Base sizes known (Wahapedia); dual-legal vs. 40K faction pack **pending check** | [Teams pointer](../../../raw/pointers/kill_team_2024_teams.md) |
| **Celestian Insidiants** | [`celestian_insidiants/`](celestian_insidiants/) | Stub | pending check | pending | pending check | [Teams pointer](../../../raw/pointers/kill_team_2024_teams.md) |
| **Death Korps** | [`death_korps/`](death_korps/) | Stub | pending check | pending | pending check | [Teams pointer](../../../raw/pointers/kill_team_2024_teams.md) |
| **Deathwatch** | [`deathwatch/`](deathwatch/) | Stub | pending check | pending | pending check | [Teams pointer](../../../raw/pointers/kill_team_2024_teams.md) |
| **Hierotek Circle** | [`hierotek_circle/`](hierotek_circle/) | Stub | **Game ready** — used set, assembled & painted (40K track) | **known** — listed in Necron inventory; **photo ID TBD** for exact 40K datasheets | pending check | [Teams pointer](../../../raw/pointers/kill_team_2024_teams.md) |
| **Kommandos** | [`kommandos/`](kommandos/) | Stub | pending check | pending | pending check | [Teams pointer](../../../raw/pointers/kill_team_2024_teams.md) |
| **Murderwing** | [`murderwing/`](murderwing/) | Stub | pending check | pending | pending check | [Teams pointer](../../../raw/pointers/kill_team_2024_teams.md) |
| **Plague Marines** | [`plague_marines/`](plague_marines/) | **Full guide - complete (S5)** | pending check | pending / N/A this track | pending check | [Teams pointer](../../../raw/pointers/kill_team_2024_teams.md) |
| **Vespid Stingwings** | [`vespid_stingwings/`](vespid_stingwings/) | Stub | pending check | pending | pending check | [Teams pointer](../../../raw/pointers/kill_team_2024_teams.md) |

### Cross-game notes (Necron teams)

- **Canoptek Circle** — KT team distinct from the **Kill Team: Tomb World** 40K learning force, though it shares most of the same physical models. **S4 complete:** the Geomancer, both Tomb Crawlers, and all five Macrocytes (1 Accelerator + 1 Reanimator + 3 Warriors) map exactly onto the 8-operative Canoptek Circle roster — see [`canoptek_circle/Owned_Models_Inventory.md`](canoptek_circle/Owned_Models_Inventory.md). The 40K Necron inventory ([`games/warhammer_40k_11e/armies/necrons/Owned_Models_Inventory.md`](../../warhammer_40k_11e/armies/necrons/Owned_Models_Inventory.md)) now cross-links back with base sizes; dual-legality (same base, both games) remains **pending check** until the 40K faction pack is audited. Necron Warriors and Scarab Swarms are **not** part of this KT team — note the Necron Warriors / "Canoptek Macrocyte Warrior" naming collision only.
- **Hierotek Circle** — same physical used set is **game ready** in the Necron 40K inventory; exact datasheet mapping remains **photo ID TBD**. Do not block KT play on 40K ID.

### Cross-game notes (Space Marine teams)

- **Angels of Death** — **S6 complete.** Every operative is built from Intercessor-family kits also usable in the 40K Space Marine collection (Captain, Assault Intercessor Squad, Intercessor Squad, Eliminator Squad, Heavy Intercessor Squad) — see [`angels_of_death/Owned_Models_Inventory.md`](angels_of_death/Owned_Models_Inventory.md) for the operative-to-datasheet mapping and base sizes. The 40K Space Marine inventory ([`games/warhammer_40k_11e/armies/space_marines/Owned_Models_Inventory.md`](../../warhammer_40k_11e/armies/space_marines/Owned_Models_Inventory.md)) now carries a matching "Kill Team ownership sync" section. Both the KT team PDF cross-check and the 40K collection audit are still **pending check** — nothing here is assumed dual-legal.

### 40K ruled-in column key

| Value | Meaning |
|-------|---------|
| **known** | Miniatures already tracked in a 40K army inventory (may still lack datasheet ID) |
| **pending** | Sync planned when the matching full guide slice runs (S4–S6) or audit completes |
| **N/A** | No 40K faction mapping attempted, because no matching 40K army is in this track's scope (e.g. Plague Marines / Death Guard) |

---

## Kill zones owned

Play surfaces and mission boards live under [`../setup/killzones/`](../setup/killzones/). Summary from track lock:

| Kill zone | Status | Play priority |
|-----------|--------|---------------|
| **Volkus** | Ready | Play now |
| **3e Starter Set** | Ready | Play now |
| **Shadowhunt** | Boards + tokens owned | After first sessions |
| **Tomb World** | Unassembled | Build before dedicated Tomb World missions |
| **2e starter scatter** | Filler terrain only | Casual / Join Ops filler |

Detail pages for each zone are **S2 / S7** deliverables. Use Volkus or the 3e Starter for first games.

---

## Related

- [`README.md`](README.md) — teams subtree index
- [`../../README.md`](../../README.md) — KT24 system entry + vocabulary
- [`../../../docs/handoffs/kill_team_2024_scaffold/track_in.md`](../../../docs/handoffs/kill_team_2024_scaffold/track_in.md) — ownership lock

---

## Change Log

- v1.3 (2026-08-17): S6 — Angels of Death row updated to full-guide-complete: 40K ruled-in marked known (mapped to Space Marine Captain/Intercessor-family units), assembly/paint and dual-legality still pending check. Added Cross-game notes (Space Marine teams) section.
- v1.2 (2026-08-17): S5 — Plague Marines row updated to full-guide-complete. 40K ruled-in set to `pending / N/A this track` — Death Guard has no 40K army folder in this track's locked scope (Necrons + Space Marines only). Added the Plague Marines cross-game note, pointing at the new minimal `games/warhammer_40k_11e/armies/death_guard/README.md` stub — explicitly not a full army package.
- v1.1 (2026-08-17): S4 — Canoptek Circle row updated to full-guide-complete: assembly/paint, 40K ruled-in, and base-size detail filled in from the new `canoptek_circle/` package; dual-legality still marked pending check. Cross-game note expanded with the Necron Warriors naming-collision flag.
- v1.0 (2026-08-17): S3 inventory — 10 teams, dual-legality fields, kill-zone summary, Hierotek + Canoptek cross-game notes.

## Attribution

- Project: Wargame_Concierge
- Maintainer: Russell Catt

## Rising Tide Notes

- This document follows Rising Tide documentation standards.
- Verify operative counts and equipment against owned team PDFs before tournament play.
