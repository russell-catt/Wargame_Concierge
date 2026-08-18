<!--
FILE: games/warhammer_40k_11e/armies/necrons/README.md
VERSION: v0.5.0 (2026-08-18)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, slice S2; tomb_world_ownership sync)

DOCUMENT_TYPE: Faction Overview
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: Warhammer 40,000 - 11th Edition
FACTION: Necrons

SOURCES:
  - C:\Personal\40K\rules\eng_22-07_warhammer_40,000_faction_pack_necrons.pdf (v1.1, read 2026-08-16)
  - C:\Personal\40K\rules\Warhammer 40,000_ Munitorum Field Manual.pdf (v1.2, read 2026-08-16)
  - https://wahapedia.ru/wh40k10ed/factions/necrons (retrieved 2026-08-16)
  - games/warhammer_40k_11e/armies/necrons/Necron_Lists.md (FOUNDATION, corrected 2026-08-16)
  - docs/handoffs/tomb_world_ownership/track_in.md (locked ownership decision)

PURPOSE:
  Entry point for the parent's Necron force. Indexes the army rule guide, both
  detachment guides, the starter lists, and the laminate play guide.

UPDATE_TRIGGER:
  Update when ownership changes, unit research lands, or a Munitorum Field Manual revision changes costs.
-->

# Necrons - 11th Edition

**Player:** Parent (Russell)

Ancient undying machines waking from tomb worlds. Necrons excel at **reanimation**, **methodical shooting**, and **Canoptek construct** synergies. Two detachment paths are documented from this collection: **Canoptek Court** and **Cryptek Conclave**.

**Start here:** [`Reanimation_Protocols.md`](Reanimation_Protocols.md) for the army rule, then [`Starter_250.md`](Starter_250.md) for a first game using the owned **Kill Team: Tomb World** force.

---

## Current collection status (2026-08-16)

| Category | Detail |
|----------|--------|
| **Game-ready now (preferred learning baseline)** | **Kill Team: Tomb World** - Cryptek Geomancer (1), Canoptek Tomb Crawlers (2), Canoptek Macrocytes (5), Necron Warriors (10), Canoptek Scarab Swarms (3). All assembled and painted. |
| **Also game-ready** | Hierotek Circle (photo ID 2026-08-17): Technomancer, 3 Immortal Guardians, Despotek, Apprentek, 2 Plasmacytes. See inventory for legal vs proxy. |
| **Owned, build before play (assemble-to-expand)** | 10 more Warriors (2nd squad), 3 more Scarab Swarms (2nd set), 5 Immortals - all unassembled |
| **Ownership totals** | 20 Warriors, 6 Scarab Swarms, Geomancer, Tomb Crawlers, Macrocytes, Technomancer, Immortals (Hierotek assembled + sprue), Apprentek/Plasmacytes (see dual-legality) |

See [`Owned_Models_Inventory.md`](Owned_Models_Inventory.md) for the checklist.

---

## Documents in this folder

### Learn the army

| File | Purpose |
|------|---------|
| [`Reanimation_Protocols.md`](Reanimation_Protocols.md) | The army rule: when it fires, what it restores, and how it changes your decisions |
| [`Canoptek_Court.md`](Canoptek_Court.md) | Detachment guide - the Power Matrix, and how a beginner uses controlled territory |
| [`Cryptek_Conclave.md`](Cryptek_Conclave.md) | Detachment guide - **Technosorcerous Augmentations** (the rule older notes miscalled "Scientific Schemes") |

### Play a game

| File | Purpose |
|------|---------|
| [`Starter_250.md`](Starter_250.md) | First-game learning list built from the game-ready Tomb World force, plus Hierotek named map |
| [`Starter_500.md`](Starter_500.md) | Both detachment paths at ~500 points, every entry tagged Tomb World / sprue / purchase |
| [`Quick_Reference_Play_Guide.md`](Quick_Reference_Play_Guide.md) | **Two-page laminate** for the table - phases, army rule, Power Matrix, combat sequence, do/don't |

### Collection and research

| File | Purpose |
|------|---------|
| [`Owned_Models_Inventory.md`](Owned_Models_Inventory.md) | Physical model checklist - the ownership source of truth |
| [`Necron_Lists.md`](Necron_Lists.md) | Expansion blueprint and shopping tracker (imported). **Its points are stale for units other than Tomb World - cost Warriors/Immortals/Scarabs from the starter lists instead** |
| [`units/README.md`](units/README.md) | Unit research stub (S6) |

---

## Two corrections worth knowing

1. **Kill Team: Tomb World is owned.** A prior version of these docs incorrectly stated Tomb World was not owned and that Hierotek Circle was the only table-ready set. Both statements were wrong: Tomb World's five units (Geomancer, 2x Tomb Crawlers, 5x Macrocytes, 10x Warriors, 3x Scarab Swarms) are assembled, painted, and game-ready, and are now the preferred learning baseline. Hierotek Circle is also game-ready but its exact datasheets remain TBD.
2. **The Cryptek Conclave detachment rule is Technosorcerous Augmentations**, not "Scientific Schemes". Confirmed in the owned faction pack v1.1 and on Wahapedia, both 2026-08-16.

---

## Sources

- Local: [`reference/Source_Library.md`](../../../../reference/Source_Library.md) - Necrons faction pack and Munitorum Field Manual paths
- Web: [Wahapedia Necrons](https://wahapedia.ru/wh40k10ed/factions/necrons)
- Shared rules spine: [`../../rules/README.md`](../../rules/README.md) and [`../../setup/README.md`](../../setup/README.md)

---

## Change Log
- v0.5.0 (2026-08-18): Project-wide semver snapshot (x.y.z).
- v2.2 (2026-08-16): Corrected collection status - Kill Team: Tomb World is owned and game-ready (preferred learning baseline), not a "not owned" historical reference. Hierotek Circle remains an additional game-ready set, ID pending. Updated document index and corrections list accordingly (slice S2, `tomb_world_ownership`).
- v2.1 (2026-08-16): Re-confirmed collection status against current `Necron_Lists.md` FOUNDATION after raw/ copy re-sync. *(This version incorrectly stated Tomb World was not owned - superseded by v2.2.)*
- v2.0 (2026-08-16): Indexed the six S4 documents - army rule guide, both detachment guides, two starter lists, and the laminate. Added the points and rule-name corrections.
- v1.0 (2026-08-16): Initial faction README and inventory (slice S2).

## Attribution
- Project: Wargame_Concierge
- Maintainer: Russell Catt
- Warhammer 40,000 is a trademark of Games Workshop Limited. This document is a personal teaching paraphrase and reproduces no publisher text or statlines.

## Rising Tide Notes
- This document follows Rising Tide documentation standards.
- **Verify before you play.** Cross-check anything here against the current Munitorum Field Manual and your faction pack - Games Workshop patches rules and points between publications. Content on this page reflects sources read on **2026-08-16**.
