<!--
FILE: reference/Source_Library.md
VERSION: v0.5.2 (2026-08-19)
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
  Catalog of local and living web sources for Warhammer 40,000 11th Edition
  and Kill Team 2024 / 2021. Every entry is a path pointer or URL — never a
  binary copy.

PRIMARY_AUDIENCE:
  - Librarian (ingest)
  - Implementers building rules and force/team content
  - QA cross-checking claims

KEY_SECTIONS_EXPECTED:
  - Copyright policy
  - Local library (C:\Personal\40K)
  - Local library (C:\Personal\Kill Team)
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
| **Warcode free beta exception** | `raw/the_warcode/*.pdf` may be committed (RedMakers free beta only — not GW). See `AGENTS.md` Sec 10 |
| **Path pointers only** | Local GW files stay under `C:\Personal\40K` or `C:\Personal\Kill Team`; the repo records paths |
| **Teaching paraphrase** | `KB/` and `docs/` explain rules in our own words. Scoped verbatim quotes: KT24 under `games/kill_team_2024/`; 40K WarCom-free Core under `games/warhammer_40k_11e/rules/` and `setup/` (filename + page + rule ID); Warcode free beta under `games/the_warcode/{rules,setup,factions}/`. Codex / Faction Pack / MFM points are not dumped |
| **Cross-check before play** | Verify claims against owned PDFs and living web sources with a retrieval date |
| **White Dwarf captures** | Secondary trust — never override official rules/team/mission/Nemesis PDFs |

---

## Local library — `C:\Personal\40K`

All paths below are on the owner's machine. **Do not copy these files into git.**

### Core rules and updates

| Path | Contents |
|------|----------|
| `C:\Personal\40K\rules\eng_01-06_warhammer40k_new40k_core_rules.pdf` | Core rules (11th Edition). WarCom-free baseline. Numbered IDs. Quote appendix: `games/warhammer_40k_11e/rules/Core_Rules_Quotes.md` |
| `C:\Personal\40K\rules\eng_22-07_warhammer_40,000_universal_rules_updates.pdf` | Universal rules updates v1.0 (22 Jul 2026). Dated stamp supersedes Core on the same topic |
| `C:\Personal\40K\rules\eng_22-07_warhammer_40,000_event_companion-alyapl19us-b2drgwkji4.pdf` | Event companion v1.1. Inventoried; mission layouts / base sizes **not dumped** |

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

## Local library — `C:\Personal\Kill Team`

All paths below are on the owner's machine. **Do not copy these files into git.**  
Obsolete: former flat `C:\Personal\Kill Team\rules\` — use `kill_team_2024\` / `kill_team_2021\` only.

**Mirror stubs:** `raw/pointers/kill_team_*.md`

### Kill Team 2024 (KT24 / 3e) — current play

| Area | Pointer file | Notes |
|------|--------------|-------|
| Core / lite / update logs / universal equipment / sniper | [`raw/pointers/kill_team_2024_core.md`](../raw/pointers/kill_team_2024_core.md) | Primary: `779937548-Core-Rules-KILL-TEAM-3E-Full-Scan.pdf` |
| Approved Ops | [`raw/pointers/kill_team_2024_approved_ops.md`](../raw/pointers/kill_team_2024_approved_ops.md) | Tournament companion + update log |
| Teams (10 owned) | [`raw/pointers/kill_team_2024_teams.md`](../raw/pointers/kill_team_2024_teams.md) | Angels of Death, Canoptek Circle, Celestian Insidiants, Death Korps, Deathwatch, Hierotek Circle, Kommandos, Murderwing, Plague Marines, Vespid Stingwings |
| Mission packs | [`raw/pointers/kill_team_2024_missions.md`](../raw/pointers/kill_team_2024_missions.md) | Volkus, Shadowhunt, Tomb World, Hivestorm, Titus, Terror on Devlan, terrain templates |
| Critical Ops 2024 + 2025 | [`raw/pointers/kill_team_2024_critical_ops.md`](../raw/pointers/kill_team_2024_critical_ops.md) | Physical decks owned; printables on disk |
| Nemesis Operatives / NPO | [`raw/pointers/kill_team_2024_nemesis_operatives.md`](../raw/pointers/kill_team_2024_nemesis_operatives.md) | Join Ops SoT |
| Terror on Devlan Dossier | [`raw/pointers/kill_team_2024_terror_on_devlan.md`](../raw/pointers/kill_team_2024_terror_on_devlan.md) | Dossier + mission pack |
| Screen_Captures (White Dwarf) | [`raw/pointers/kill_team_2024_screen_captures.md`](../raw/pointers/kill_team_2024_screen_captures.md) | **Secondary trust** — WD517 Necrons + Procession PvE; never commit `.webp` |

Root: `C:\Personal\Kill Team\kill_team_2024\`

### Kill Team 2021 (KT21 / 2e) — archive only

| Area | Pointer file | Notes |
|------|--------------|-------|
| Core book + compendium | [`raw/pointers/kill_team_2021_archive.md`](../raw/pointers/kill_team_2021_archive.md) | Not for current play; see [`reference/kill_team_2e/`](kill_team_2e/) |

Root: `C:\Personal\Kill Team\kill_team_2021\`

**Out of scope this track:** `C:\Personal\Kill Team\Community Content\` (homebrew / community sheets — not authoritative).

---

## Living web references

Use these for edition drift checks. Record a **retrieval date** on any claim sourced from the web.

**Unit / stat lookup precedence** (see [`AGENTS.md`](../AGENTS.md) Sec 10): owned faction pack → WarCom when it publishes the profile/amendment → **Wahapedia allowed** when WarCom does not publish that datasheet. Prefer `wh40k11ed` when present; flag `wh40k10ed`. Teaching paraphrase; `draft` until owned-pack cross-check; owned PDF wins on conflict.

### Warhammer 40,000

| Source | URL | Use |
|--------|-----|-----|
| **Warhammer Community** | https://www.warhammer-community.com/en-gb/ | Official FAQs, balance dataslates, announcements |
| **WarCom — free Core (2026-06-01)** | https://www.warhammer-community.com/en-gb/articles/nhqt9wx3/new40k-rules-download-the-free-core-rules-now/ | Discovery; local Core PDF is SoT |
| **WarCom — 40K downloads** | https://www.warhammer-community.com/en-gb/downloads/warhammer-40000/ | Free downloads hub (retrieved 2026-08-18) |
| **WarCom — July update (2026-07-22)** | https://www.warhammer-community.com/en-gb/articles/rgqanids/warhammer-40000-july-update-what-you-need-to-know/ | Discovery; local `eng_22-07_*` is SoT |
| **Wahapedia (index)** | https://wahapedia.ru/ | Community rules + **unit/stat lookup when WarCom lacks the profile**; cross-check owned PDFs |
| **Wahapedia — Necrons (11e path)** | https://wahapedia.ru/wh40k11ed/factions/necrons | Prefer when available; retrieval date required |
| **Wahapedia — Necrons (10e path)** | https://wahapedia.ru/wh40k10ed/factions/necrons | **Flag:** `wh40k10ed` — edition-risk; use only if 11e path missing |
| **Wahapedia — Space Marines (10e path)** | https://wahapedia.ru/wh40k10ed/factions/space-marines | Same 10e path flag; prefer `wh40k11ed` when present |

### Kill Team

| Source | URL | Use |
|--------|-----|-----|
| **Warhammer Community — Kill Team** | https://www.warhammer-community.com/en-gb/kill-team/ | Official KT downloads, FAQs, updates |
| **Wahapedia — Kill Team 3 / KT24** | https://wahapedia.ru/kill-team3/ | Community KT24 reference; cross-check owned PDFs |
| **Wahapedia — Kill Team 2 (archive)** | https://wahapedia.ru/kill-team2/the-rules/core-rules/ | 2e archive only — not current play |

Pointer: [`raw/pointers/kill_team_web_living_sources.md`](../raw/pointers/kill_team_web_living_sources.md)

---

## Notation references (not game rules)

`reference/` is **not project truth.** These pages teach how this repo draws flowcharts. They are **not** Kill Team or 40K sources.

| Source | URL / path | Use | Retrieved |
|--------|------------|-----|-----------|
| **uml-diagrams.org** (Kirill Fakhroutdinov) | https://www.uml-diagrams.org/ · [About](https://www.uml-diagrams.org/about.html) · local [`uml/`](uml/README.md) | UML 2.5 **activity** notation (actions, decision/guards, initial/final). Offline snapshots: activity family + About only. | **2026-08-18** |

**Credit:** [uml-diagrams.org About](https://www.uml-diagrams.org/about.html): **Authored by Kirill Fakhroutdinov**. Copyright © 2009–2026 uml-diagrams.org. All rights reserved. Third-party teaching reference; **not** a Kill Team rules source.

House mapping ships in [`docs/operations/Flowcharting.md`](../docs/operations/Flowcharting.md).

---

## Imported markdown sources

These files were **copied into the repo** as allowed personal notes (not GW PDFs).

| Repo path | Origin | Notes |
|-----------|--------|-------|
| [`raw/Necron_Lists.md`](../raw/Necron_Lists.md) | `C:\Personal\40K\Necron_Lists.md` | Imported snapshot. **Personal path is SoT** |
| [`games/warhammer_40k_11e/armies/necrons/Necron_Lists.md`](../games/warhammer_40k_11e/armies/necrons/Necron_Lists.md) | Same Personal file | **Working copy.** If they diverge, Personal wins. Do not overwrite Personal |

### Ownership snapshot (from FOUNDATION — 2026-08-16)

Confirmed in the FOUNDATION section of `Necron_Lists.md`. **Kill Team: Tomb World is owned and game-ready** — the preferred learning baseline.

**Game-ready (Tomb World + Hierotek):**

| Item | Qty | Status |
|------|-----|--------|
| Cryptek Geomancer | 1 | Game ready (Tomb World) |
| Canoptek Tomb Crawlers | 2 | Game ready (Tomb World) |
| Canoptek Macrocytes | 5 | Game ready (Tomb World) |
| Necron Warriors | 10 (1st squad) | Game ready (Tomb World) |
| Canoptek Scarab Swarms | 3 (1st set) | Game ready (Tomb World) |
| Hierotek Circle Kill Team (used) | 1 set | Game ready; 40K datasheets TBD pending photos |

**Build before play (owned, on sprue):**

| Item | Qty | Status |
|------|-----|--------|
| Necron Warriors | 10 (2nd squad) | Purchased, unassembled |
| Canoptek Scarab Swarms | 3 (2nd set) | Purchased, unassembled |
| Immortals | 5 (1 squad) | Purchased, unassembled |

**Totals:** 20 Warriors (10 game-ready + 10 sprue), 6 Scarab Swarms (3 game-ready + 3 sprue), plus Geomancer, Tomb Crawlers, Macrocytes, Immortals, and Hierotek Circle (TBD).

---

## The Warcode (system #3)

Free public beta — **binary may live in git** under `raw/the_warcode/` (not GW).

| Source | Path / URL | Use | Retrieved |
|--------|------------|-----|-----------|
| Rulebook V.0.8.7-F | [`raw/the_warcode/The Warcode Rulebook V.0.8.7-F.pdf`](../raw/the_warcode/The%20Warcode%20Rulebook%20V.0.8.7-F.pdf) | Primary rules truth | **2026-08-23** |
| Pre-launch site | https://pre-launch.thewarcode.com/ | Marketing, factions, VIP | **2026-08-23** |
| Gamefound | https://gamefound.com/en/projects/redmakers/the-warcode | Campaign Sep 2026 | **2026-08-23** |
| VIP Facebook | https://www.facebook.com/groups/1548626022918599 | Community | **2026-08-23** |
| Pointers | [`raw/pointers/warcode_*.md`](../raw/pointers/) | Ingest stubs | **2026-08-23** |
| Plan archive | [`reference/Warcode_Tactical_Doctrine_Plan.md`](Warcode_Tactical_Doctrine_Plan.md) | Track plan snapshot | **2026-08-23** |

Quote appendix: `games/the_warcode/rules/Rulebook_Quotes.md`. Shipping naming: never Kill Team — **That other game** / **Murder Platoon**.

---

## Change Log
- v0.5.3 (2026-08-23): The Warcode free beta — `raw/the_warcode/` PDF allowed; living web + VIP pointers (track `warcode_tactical_doctrine` S0).
- v0.5.2 (2026-08-19): Living web — Wahapedia allowed for unit/stat lookup when WarCom does not publish profiles; 11e Necrons path preferred; 10e paths flagged as edition-risk.
- v0.5.1 (2026-08-18): WarCom-free Core quote path; July `eng_*` hierarchy; Wahapedia 10e URL flag; Necron lists Personal-wins ranking (track `40k_warcom_quotes`).
- v0.5.1 (2026-08-18): uml-diagrams.org notation row + Fakhroutdinov credit (track `flowcharting_uml` S0).
- v0.5.0 (2026-08-18): Project-wide semver snapshot (x.y.z).
- v1.2 (2026-08-17): Kill Team 2024 + 2021 library rows, living KT web refs, Screen_Captures secondary-trust note (slice S0, kill_team_2024_scaffold).
- v1.1 (2026-08-16): Ownership snapshot aligned to FOUNDATION — Tomb World owned and game-ready; dual Warriors/Scarabs; Immortals sprue; Hierotek TBD. Removed stale "Not owned — superseded" row. S4 coord preflight.
- v1.0 (2026-08-16): Initial catalog (slice S2). Local library paths, living web refs, Preflight Necron_Lists import noted.

## Attribution
- Project: Wargame_Concierge
- Maintainer: Russell Catt

## Rising Tide Notes
- This document follows Rising Tide documentation standards.
- Must remain understandable, reproducible, and reusable.
