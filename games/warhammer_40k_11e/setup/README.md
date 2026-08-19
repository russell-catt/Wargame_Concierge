<!--
FILE: games/warhammer_40k_11e/setup/README.md
VERSION: v0.5.1 (2026-08-18)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, slice S3)

DOCUMENT_TYPE: Index / Section README
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: Warhammer 40,000 - 11th Edition
REFERENCE_STATUS: Active - content authored in S3

SOURCES:
  - C:\Personal\40K\rules\eng_22-07_warhammer_40,000_event_companion-alyapl19us-b2drgwkji4.pdf (v1.1, read 2026-08-16)
  - C:\Personal\40K\rules\eng_01-06_warhammer40k_new40k_core_rules.pdf (Section 13, read 2026-08-16)
  - C:\Personal\40K\Terrain\A4\ (path pointers only)
  - reference/Source_Library.md

PURPOSE:
  Index for board and terrain setup. Says what each document covers and where
  the printable terrain footprints live.

UPDATE_TRIGGER:
  Update when a setup document is added or revised, or when new terrain packs
  are acquired.
-->

# Setup - Warhammer 40,000 11th Edition

**Status:** Populated in **S3**, from the owned Event Companion v1.1 and Core Rules PDF, both read **2026-08-16**; rule-ID cites added **2026-08-18** (`40k_warcom_quotes`).

Everything that happens before battle round one, plus the terrain rules that shape the whole game.

This folder may quote WarCom-free Core / local `eng_*` with filename + page + rule ID. Teaching stays paraphrase. Event Companion mission layouts and base-size lists are **inventoried, not dumped**. **Warhammer 40,000 is Copyright Games Workshop Limited.** Personal use only; never for sale.

---

## Documents

| File | What it covers |
|------|----------------|
| [`Board_Setup.md`](Board_Setup.md) | Table size (44" x 60" for events), the fourteen-step pre-game sequence, deployment zones and territory, objective types, strategic reserves, a printable pre-game checklist, and shortcuts for a first game |
| [`Terrain_Basics.md`](Terrain_Basics.md) | Terrain areas vs terrain features, the three categories (Exposed / Light / Dense), the four visibility rules (Benefit of Cover, Hidden, Obscuring, Solid), terrain and movement, and how much terrain a table actually needs |

---

## Terrain footprint packs - local library

Printable terrain-area footprints are on the owner's machine and **stay outside this repository**. Path pointers only; no binaries are committed.

- **A4 packs:** `C:\Personal\40K\Terrain\A4\` - Combat Patrol Battlezone, Imperial World, Death World Jungle, Death World Snow, Maelstrom World, and a grey city-tone variant
- **Full-size footprint documents:** `C:\Personal\40K\rules\` - the terrain area footprints booklet plus per-battlezone PDFs

Full catalogue: [`reference/Source_Library.md`](../../../reference/Source_Library.md).

---

## The two things beginners get wrong

1. **Terrain areas come before terrain features.** Objectives, cover, Hidden, and Obscuring all key off the *area*, not the scenery model.
2. **Cover does not improve your save in 11th Edition.** It worsens the attacker's Ballistic Skill by 1. Both are explained in [`Terrain_Basics.md`](Terrain_Basics.md).

---

## Related

- [`../rules/README.md`](../rules/README.md) - the rules teaching spine
- [`../rules/Key_Concepts.md`](../rules/Key_Concepts.md) - Objective Control, which decides what setup is for
- [`../README.md`](../README.md) - the 40K subtree entry point

---

## Change Log
- v0.5.1 (2026-08-18): Quote permission + Core ID cites (track `40k_warcom_quotes`). Event Companion still inventoried, not dumped.
- v0.5.0 (2026-08-18): Project-wide semver snapshot (x.y.z).
- v2.0 (2026-08-16): Replaced the S2 stub with a real index. Board_Setup and Terrain_Basics authored (slice S3).
- v1.0 (2026-08-16): Stub created (slice S2).

## Attribution
- Project: Wargame_Concierge
- Maintainer: Russell Catt

## Rising Tide Notes
- This document follows Rising Tide documentation standards.
- **Verify before you play.** Cross-check anything in this section against the current Munitorum Field Manual and your faction pack - Games Workshop patches rules and points between publications. Content reflects sources read on **2026-08-16**.
