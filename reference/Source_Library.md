<!--
FILE: reference/Source_Library.md
VERSION: v1.0 (2026-08-16)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, slice S2)

DOCUMENT_TYPE: Reference / Source Catalog
PROJECT_NAME: Wargame_Concierge
REFERENCE_STATUS: Active

SOURCES:
  - C:\Personal\40K (local owned library — path pointers only)
  - docs/Project_Planning.md Sec 3 (confirmed ownership)
  - docs/handoffs/v1_scaffold/slices/Preflight_qa.md

PURPOSE:
  Catalog of local and living web sources for Warhammer 40,000 11th Edition.
  Every entry is a path pointer or URL — never a binary copy.

PRIMARY_AUDIENCE:
  - Librarian (L1 ingest)
  - Implementers building rules and army content
  - QA cross-checking claims

KEY_SECTIONS_EXPECTED:
  - Copyright policy
  - Local library (C:\Personal\40K)
  - Living web references
  - Imported markdown sources

UPDATE_TRIGGER:
  Update when new PDFs are acquired, Wahapedia URLs change, or ownership edits
  are made to imported list documents.
-->

# Source Library

Catalog of **local path pointers** and **living web references** for this project. Nothing in this file is a copy of copyrighted publisher material — only where to find it.

**Mirror stubs:** [`raw/pointers/`](../raw/pointers/) contains ingest-ready pointer files that cite sections here.

---

## Copyright policy

| Rule | Detail |
|------|--------|
| **Never commit GW binaries** | No PDFs, webp, png, or official images in this repository |
| **Path pointers only** | Local files stay under `C:\Personal\40K`; the repo records paths |
| **Teaching paraphrase** | Written content in `docs/` and `games/` explains rules in our own words |
| **Cross-check before play** | Verify claims against owned PDFs and living web sources with a retrieval date |

---

## Local library — `C:\Personal\40K`

All paths below are on the owner's machine. **Do not copy these files into git.**

### Core rules and updates

| Path | Contents |
|------|----------|
| `C:\Personal\40K\rules\eng_01-06_warhammer40k_new40k_core_rules.pdf` | Core rules (11th Edition) |
| `C:\Personal\40K\rules\eng_22-07_warhammer_40,000_universal_rules_updates.pdf` | Universal rules updates |
| `C:\Personal\40K\rules\eng_22-07_warhammer_40,000_event_companion-alyapl19us-b2drgwkji4.pdf` | Event companion |

### Faction packs (11th Edition)

| Path | Contents |
|------|----------|
| `C:\Personal\40K\rules\eng_22-07_warhammer_40,000_faction_pack_necrons.pdf` | Necrons faction pack |
| `C:\Personal\40K\rules\eng_22-07_warhammer_40,000_faction_pack_space_marines.pdf` | Space Marines faction pack |

### Points documents

| Path | Contents |
|------|----------|
| `C:\Personal\40K\rules\Warhammer 40,000_ Munitorum Field Manual.pdf` | Munitorum Field Manual (general) |
| `C:\Personal\40K\rules\Warhammer 40,000_ Munitorum Field Manual_Marines.pdf` | Munitorum Field Manual (Space Marines supplement) |

### Terrain area footprints

| Path | Contents |
|------|----------|
| `C:\Personal\40K\rules\eng_12-06_warhammer40000_terrainareafootprints-biavo5zf9f-gxdahkydbj.pdf` | Terrain area footprints (rules booklet) |
| `C:\Personal\40K\rules\warhammer40k_terrain_area_footprint_imperial_world.pdf` | Imperial World footprint |
| `C:\Personal\40K\rules\warhammer40k_terrain_area_footprint_death_world_jungle-ou67vrxeys-0hosfodoj0.pdf` | Death World Jungle footprint |
| `C:\Personal\40K\rules\warhammer40k_terrain_area_footprint_death_world_snow-t3zsylosfg-hflqpgfj0n.pdf` | Death World Snow footprint |
| `C:\Personal\40K\rules\warhammer40k_terrain_area_footprint_maelstrom_world.pdf` | Maelstrom World footprint |

### Terrain printables (A4)

| Path | Contents |
|------|----------|
| `C:\Personal\40K\Terrain\A4\11th - Terrain Footprints - A4 Scale - Combat Patrol Battlezone.pdf` | Combat Patrol battlezone |
| `C:\Personal\40K\Terrain\A4\11th - Terrain Footprints - A4 Scale - Imperial World.pdf` | Imperial World (A4) |
| `C:\Personal\40K\Terrain\A4\11th - Terrain Footprints - A4 Scale - Death World Jungle.pdf` | Death World Jungle (A4) |
| `C:\Personal\40K\Terrain\A4\11th - Terrain Footprints - A4 Scale - Death World Snow.pdf` | Death World Snow (A4) |
| `C:\Personal\40K\Terrain\A4\11th - Terrain Footprints - A4 Scale - Maelstrom World.pdf` | Maelstrom World (A4) |
| `C:\Personal\40K\Terrain\A4\11th - Terrain Footprints - A4 Scale (Grey City Tone).pdf` | Grey city tone variant |

### Reference sheet (images — local only)

| Path | Contents |
|------|----------|
| `C:\Personal\40K\reference_sheet\quick-reference-sheet-included-in-this-months-white-dwarf-1.webp` | Quick reference sheet (part 1) |
| `C:\Personal\40K\reference_sheet\quick-reference-sheet-included-in-this-months-white-dwarf-2.webp` | Quick reference sheet (part 2) |

> **Note:** `.webp` reference images stay outside the repo. Path pointers only.

---

## Living web references

Use these for edition drift checks. Record a **retrieval date** on any claim sourced from the web.

| Source | URL | Use |
|--------|-----|-----|
| **Warhammer Community** | https://www.warhammer-community.com/en-gb/ | Official FAQs, balance datasheets, announcements |
| **Wahapedia (index)** | https://wahapedia.ru/ | Community rules reference; cross-check against owned PDFs |
| **Wahapedia — Necrons** | https://wahapedia.ru/wh40k10ed/factions/necrons | Necron faction hub (11th Edition content) |
| **Wahapedia — Space Marines** | https://wahapedia.ru/wh40k10ed/factions/space-marines | Space Marines faction hub (11th Edition content) |

---

## Imported markdown sources

These files were **copied into the repo** as allowed personal notes (not GW PDFs).

| Repo path | Origin | Notes |
|-----------|--------|-------|
| [`raw/Necron_Lists.md`](../raw/Necron_Lists.md) | `C:\Personal\40K\rules\Necron_Lists.md` | **Preflight-updated 2026-08-16.** Expansion blueprint with confirmed ownership. Authoritative for Necron collection planning. |
| [`games/warhammer_40k_11e/armies/necrons/Necron_Lists.md`](../games/warhammer_40k_11e/armies/necrons/Necron_Lists.md) | Same source | Working copy in the 40K game subtree |

### Ownership snapshot (from Preflight import)

Confirmed **2026-08-16** in the FOUNDATION section of `Necron_Lists.md`:

| Item | Qty | Status |
|------|-----|--------|
| Necron Warriors | 10 (1 squad) | Purchased, unassembled |
| Canoptek Scarab Swarms | 3 | Purchased, unassembled |
| Immortals | 5 (1 squad) | Purchased, unassembled |
| Hierotek Circle Kill Team (used) | 1 set | Assembled + painted (game ready); unit ID pending photos |
| Kill Team: Tomb World | — | **Not owned** — superseded historical reference only |

---

## Change Log
- v1.0 (2026-08-16): Initial catalog (slice S2). Local library paths, living web refs, Preflight Necron_Lists import noted.

## Attribution
- Project: Wargame_Concierge
- Maintainer: Russell Catt

## Rising Tide Notes
- This document follows Rising Tide documentation standards.
- Must remain understandable, reproducible, and reusable.
