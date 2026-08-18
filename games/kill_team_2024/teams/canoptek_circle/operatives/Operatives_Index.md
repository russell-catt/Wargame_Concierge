<!--
FILE: games/kill_team_2024/teams/canoptek_circle/operatives/Operatives_Index.md
VERSION: v0.5.0 (2026-08-18)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, slice S4)

DOCUMENT_TYPE: Operative Role Index
GAME_SYSTEM: Kill Team — 2024 / 3e (KT24)
TEAM: Canoptek Circle
REFERENCE_STATUS: Draft — living Wahapedia source, retrieved 2026-08-17

SOURCES:
  - https://wahapedia.ru/kill-team3/kill-teams/canoptek-circle/ (retrieved 2026-08-17)
  - ../Owned_Models_Inventory.md, ../Starter_Roster.md

PURPOSE:
  One entry per operative, in plain English, with fields already shaped for
  the S10 Tarot-sleeve card schema (see ../cards/Card_Schema.md). No full
  stat blocks (APL/Move/Save/Wounds, weapon ATK/HIT/DMG) — role and habit
  only.

UPDATE_TRIGGER:
  Update when the local team PDF is cross-checked, or when S10 photos let
  these entries fill in a real card front.
-->

# Operatives Index — Canoptek Circle

Five operative types, eight bodies total. Each entry below is written to plug directly into the [Card Schema](../cards/Card_Schema.md) once S10 photography happens — the fields are deliberately card-shaped.

---

## Geomancer

| Field | Value |
|-------|-------|
| **Count in team** | 1 |
| **Base** | 50mm |
| **Keywords (role, not full list)** | Leader, Cryptek |
| **Plain-English role** | The team's anchor. Plants the Obelisk Nodes on turn one, re-anchors them each turn after, and can substitute a node for itself when doing objective actions. Also a genuinely dangerous melee piece with a multi-mode weapon. |
| **Signature habit** | "Objective control" for the Geomancer often means glancing at a nearby node instead of standing on the marker itself. |
| **Support given to others** | Can hand a nearby Canoptek a free 1AP action once per activation. |
| **Card-schema tags** | `leader`, `node-anchor`, `melee-capable`, `support-giver` |

---

## Tomb Crawler

| Field | Value |
|-------|-------|
| **Count in team** | 2 |
| **Base** | 50mm |
| **Keywords (role, not full list)** | Canoptek |
| **Plain-English role** | The team's tank/heavy hitter. Big base, high durability. Owned pair is **one of each weapon**: twin gauss reapers on one, transdimensional isolator on the other (legal max one isolator). |
| **Signature habit** | Hard to remove from an objective once it plants itself there; treat its control rating as reliable even under pressure. |
| **Support given to others** | None — a self-contained bruiser. |
| **Card-schema tags** | `heavy`, `durable` |

---

## Canoptek Macrocyte Accelerator

| Field | Value |
|-------|-------|
| **Count in team** | 1 |
| **Base** | 28mm |
| **Keywords (role, not full list)** | Canoptek, Macrocyte |
| **Plain-English role** | Tempo support. Spends its activation pushing a friendly Canoptek's action economy up, or an enemy's down, rather than fighting directly. |
| **Signature habit** | Use it *before* the operative you're buffing activates, or on an enemy right before their turn to act — timing is the whole trick. |
| **Support given to others** | Grants +APL to an ally, or −APL to an enemy, for a window of time. |
| **Card-schema tags** | `support`, `tempo-manipulation`, `fragile` |

---

## Canoptek Macrocyte Reanimator

| Field | Value |
|-------|-------|
| **Count in team** | 1 |
| **Base** | 28mm |
| **Keywords (role, not full list)** | Canoptek, Macrocyte |
| **Plain-English role** | Support/medic. Can pull a dying nearby Canoptek back from the brink once per turning point — at the cost of tempo for both operatives. Also tops up wounds elsewhere. |
| **Signature habit** | The save-a-model rule is not free — both operatives lose tempo next activation. Use it to save a key piece, not a Warrior you were happy to lose anyway. |
| **Support given to others** | Wound recovery and one "cheat death" trick per turning point. |
| **Card-schema tags** | `support`, `medic`, `fragile` |

---

## Canoptek Macrocyte Warrior

| Field | Value |
|-------|-------|
| **Count in team** | 3 |
| **Base** | 28mm |
| **Keywords (role, not full list)** | Canoptek, Macrocyte |
| **Plain-English role** | The disposable screen. Cheap, forgettable, but punishes an enemy in melee on the way out and is deliberately excluded from how the enemy's kill-count scoring treats it. Can be replenished mid-battle if your numbers drop. Owned three: **2 gauss scalpel, 1 tesla caster**. |
| **Signature habit** | Screen aggressively — this operative is built to trade, not to survive the battle. Losing all three and bringing one back is a normal turning point, not a crisis. |
| **Support given to others** | None directly, but its expendability protects the rest of the team's tempo. |
| **Card-schema tags** | `screen`, `expendable`, `replenishable` |

---

## Printable datacards

Stats and rules text live on the HTML datacards (quoted from the owned Teams PDF). Role notes above stay teaching-only.

| Operative | Datacard |
|-----------|----------|
| Geomancer | [`../cards/Geomancer.html`](../cards/Geomancer.html) |
| Tomb Crawler | [`../cards/Tomb_Crawler.html`](../cards/Tomb_Crawler.html) |
| Macrocyte Accelerator | [`../cards/Macrocyte_Accelerator.html`](../cards/Macrocyte_Accelerator.html) |
| Macrocyte Reanimator | [`../cards/Macrocyte_Reanimator.html`](../cards/Macrocyte_Reanimator.html) |
| Macrocyte Warrior | [`../cards/Macrocyte_Warrior.html`](../cards/Macrocyte_Warrior.html) |

Index of all five: [`../cards/Card_Schema.md`](../cards/Card_Schema.md).

---

## Related pages

- [`../README.md`](../README.md) — package entry point
- [`../Team_Rule_Guide.md`](../Team_Rule_Guide.md) — the Obelisk Node Matrix these operatives play around
- [`../Owned_Models_Inventory.md`](../Owned_Models_Inventory.md) — physical model mapping

---

## Change Log

- v0.5.0 (2026-08-18): Project-wide semver snapshot (x.y.z).
- v1.2 (2026-08-17): Linked printable HTML datacards (`kt24_rules_quotes` S4).
- v1.1 (2026-08-17): Tomb Crawler and Macrocyte Warrior loadouts photo-confirmed.
- v1.0 (2026-08-17): Initial operative index (slice S4) — five entries, card-schema-ready fields, no full stat blocks.

## Attribution

- Project: Wargame_Concierge · Maintainer: Russell Catt

## Rising Tide Notes

- This document follows Rising Tide documentation standards.
- Deliberately omits APL/Move/Save/Wounds and weapon ATK/HIT/DMG values — this is a role guide, not a datacard transcription.
