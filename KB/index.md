---
title: KB Index
type: index
system: multi_system
systems: [warhammer_40k_11e, kill_team_2024]
created: 2026-08-16
updated: 2026-08-22
version: 0.5.5
sources: [necron_lists_owner_notes, source_library, local_library_pointers, kill_team_2024_core_rules, kill_team_necron_photos, uml_diagrams_org, warcom_free_core_rules_11e, wahapedia, their_number_is_legion_potentiality_syphon_250, kill_team_kommandos_teams_pdf, legends_field_manual_sm_2026_08]
confidence: verified
tags: [index, catalog, kb, kill_team_2024]
---

# KB Index

Master catalog of every page in this knowledge base. Read this first when answering a question: find the relevant pages here, then drill into them.

**Schema source of truth:** [`AGENTS.md`](../AGENTS.md) at the repo root. Entity types, YAML frontmatter, naming, and the ingest / query / lint workflows are defined there, not here. This file is the catalog only.

**Status:** lint complete for Warhammer 40,000 through slice **L2** of `tomb_world_ownership` (2026-08-16); Kill Team 2024 **v0.5.0 Librarian pass (2026-08-18)** rewrote L1 Wahapedia drafts from shipping (targeting subset `verified` on [[kill_team_2024_core_rules]] / [[valid_target]]; other Core topics still `draft`). Teams / ops trees remain index-only.

**Two systems now.** Everything in the typed sections below (Sources through Analyses) is `system: warhammer_40k_11e` unless it appears in **Project notation** (`system: multi_system`, not game rules) or the dedicated **Kill Team 2024 (KT24)** section. Kill Team and 40K stay split at every layer, including the index. Check a page's own `system:` frontmatter if in doubt.

> **Rules sources have now been read, but most `KB/` pages predate that reading.** The claim that used to sit here - "no rules document has been read" - was true at L1 and is false now: S3, S4 and S5 read the owned core rules, both faction packs, and Munitorum Field Manual v1.2, and [[glossary]] carries 24 `verified` game terms as a result. What has **not** happened is a back-fill: the faction, detachment and concept pages below still mostly rest on the owner's planning notes. Treat every `draft` and `unverified` row as "check before the table", and prefer the shipping teaching content under `games/warhammer_40k_11e/` where the two disagree.

---

## How to read this index

Each typed section is a table:

| Column | Meaning |
|--------|---------|
| Page | A `[[wikilink]]` to the KB page (backticked here so link lint does not read the example as a real target) |
| Summary | The one-line summary from the top of that page, copied verbatim |
| Confidence | `verified` / `draft` / `stub` / `unverified` - see [`AGENTS.md`](../AGENTS.md) Sec 6 |
| Updated | Date of the last substantive change |

Treat `unverified` and `stub` rows as "do not take to the table without checking."

---

## Core files

| Page | Summary | Confidence | Updated |
|------|---------|------------|---------|
| [[overview]] | High-level synthesis of the whole knowledge base and where the project stands | draft | 2026-08-19 |
| [[glossary]] | Living terminology; the single home for all Keyword entries | draft | 2026-08-19 |
| [[log]] | Append-only chronological record of ingests, queries, and lint passes | verified | 2026-08-19 |
| [[changelog]] | Promotion log: KB pages that shipped into `docs/` or `games/` | verified | 2026-08-18 |
| [[ingest_procedure]] | How a source in `raw/` becomes KB pages in this project | verified | 2026-08-16 |

---

## Sources

One page per ingested source. Location: `KB/sources/`.

| Page | Summary | Confidence | Updated |
|------|---------|------------|---------|
| [[warcom_free_core_rules_11e]] | WarCom-free 11e Core PDF + July universal updates; numbered-ID quote appendix in shipping; KB paraphrase only | draft | 2026-08-18 |
| [[necron_lists_owner_notes]] | The owner's own Necron expansion blueprint: what is actually owned as of 2026-08-16, and two costed paths from that collection up to a 1,000-point army | draft | 2026-08-17 |
| [[source_library]] | The project's map of where the answers are: owned PDFs, living web references, and the copyright rule that keeps all of it outside git | verified | 2026-08-17 |
| [[local_library_pointers]] | Eight stub files standing in for owned PDFs the repo is not allowed to contain - and all still unread | verified | 2026-08-16 |
| [[wahapedia]] | Community aggregator — unit/stat when WarCom lacks profiles; Legion/Syphon + list fills retrieved 2026-08-19 | draft | 2026-08-19 |
| [[warhammer_community]] | GW FAQs, errata, dataslates — surveyed 2026-08-20 for Legion / Syphon / character revive | draft | 2026-08-20 |
| [[legends_field_manual_sm_2026_08]] | WarCom Legends Field Manual SM points (Servitors / Bike / Attack Bike) retrieved 2026-08-22 for Casual starters | draft | 2026-08-22 |

---

## Project notation (not game rules)

These pages are `system: multi_system`. They describe how this repo draws charts. They are **not** Kill Team or 40K rules.

### Sources (notation)

| Page | Summary | Confidence | Updated |
|------|---------|------------|---------|
| [[uml_diagrams_org]] | Offline snapshots of Kirill Fakhroutdinov's uml-diagrams.org activity-family pages; a notation teaching reference, **not** a wargame rules source | draft | 2026-08-18 |

### Concepts (notation)

| Page | Summary | Confidence | Updated |
|------|---------|------------|---------|
| [[flowcharting_uml_activity]] | House flowcharting maps to UML 2.5 activity diagrams: filled-circle start, rounded-rect actions, diamond decisions with guards, bullseye end | draft | 2026-08-18 |

---

## Concepts

Rules ideas and tactical principles. Location: `KB/concepts/`.

| Page | Summary | Confidence | Updated |
|------|---------|------------|---------|
| [[objective_control]] | Totals vs presence; terrain-area **14.01**; re-check every phase/turn **14.02**; tie = nobody; Battle-shock zeroes OC **08.03**; not KT 1" control range | verified | 2026-08-20 |
| [[power_matrix]] | Canoptek Court rule: DZ always; NML/enemy if ≥ half markers; Cryptek/Canoptek two-tier hit re-rolls. **L0 Kill Team correction kept** | draft | 2026-08-20 |
| [[reanimation_protocols]] | Necron army rule: end of your Command phase, D3 wounds per unit (heal first, then return at 1W); wiped = gone. Back-filled from shipping 2026-08-19 | draft | 2026-08-19 |
| [[oath_of_moment]] | The Space Marine army rule: nominate one enemy unit per turn and attack it better. Turns target priority into the defining decision | unverified | 2026-08-16 |

---

## Factions

One page per army. Location: `KB/factions/`.

| Page | Summary | Confidence | Updated |
|------|---------|------------|---------|
| [[necrons]] | Primary army: attrition + Reanimation Protocols; Phase 1 Conclave list 245 pts (MFM v1.2) | draft | 2026-08-19 |
| [[space_marines]] | Blood Ravens Codex SM Gladius force; Matched vs Casual starter split; owned Legends on Casual only | draft | 2026-08-22 |

---

## Detachments

One page per detachment and its rules package. Location: `KB/detachments/`.

| Page | Summary | Confidence | Updated |
|------|---------|------------|---------|
| [[canoptek_court]] | Canoptek constructs + Power Matrix (two-tier from shipping); Phase 1 shared 245-pt Tomb World force | draft | 2026-08-20 |
| [[cryptek_conclave]] | Cryptek infantry castle; Technosorcerous Augmentations + Potentiality Syphon; 245 Conclave list | draft | 2026-08-19 |
| [[gladius_task_force]] | The generalist Space Marine detachment named as the son's learning target. **Stub - no source read** | stub | 2026-08-16 |
| [[first_company_task_force]] | Elite Terminator / veteran detachment; best owned-shelf alternate to Gladius | draft | 2026-08-22 |
| [[anvil_siege_force]] | Gunline Remain-Stationary detachment; second owned-shelf alternate (Devs + Whirlwind) | draft | 2026-08-22 |

---

## Units

One page per datasheet, written in play terms. Location: `KB/units/`.

| Page | Summary | Confidence | Updated |
|------|---------|------------|---------|
| [[necron_warriors]] | Battleline brick; Their Number is Legion re-rolls RP D3; owned 10+10 | draft | 2026-08-19 |
| [[techmarine]] | Owned Firstborn Techmarine; matched-legal alone; unlocks Servitors on Casual lists | draft | 2026-08-22 |
| [[astartes_servitors]] | Legends infantry ×4 with Techmarine; Casual Gladius only; Mindlock / Servitor Retinue | draft | 2026-08-22 |

Pointer to the full research corpus: [[necrons_unit_index]].

---

## Setup / Missions

Deployment, terrain, missions, and scoring. Location: `KB/setup/`.

40K setup remains empty (S3 shipping lives under `games/warhammer_40k_11e/setup/`). **Kill Team 2024** setup pages are catalogued in the KT24 section above ([[kill_team_terrain]], [[killzones_volkus_tomb_world]]).

---

## Analyses

Synthesized outputs: matchups, list comparisons, and query answers worth keeping. Location: `KB/analyses/`.

| Page | Summary | Confidence | Updated |
|------|---------|------------|---------|
| [[40k_core_docs_kb_consistency_2026_08_19]] | Filed query/lint 2026-08-19: shipping Core OK; KB OC/Matrix gaps **closed 2026-08-20** from shipping (`kb_shipping_backfill`) | draft | 2026-08-20 |
| [[their_number_is_legion_potentiality_syphon_250]] | Legion + Syphon teaching; heal-first explained; OQs closed 2026-08-20 (WarCom primary) | draft | 2026-08-21 |
| [[inherited_docs_for_S3]] | What L1 hands to S3: the facts stable enough to teach from, the claims that are not, and which unread pointer answers which question | verified | 2026-08-17 |
| [[sm_matched_vs_casual_starters]] | Blood Ravens Gladius Matched vs Casual split; when to use which; Legends fit compromises by points level | draft | 2026-08-22 |
| [[sm_owned_detachment_fit]] | Beyond Gladius: 1st Company then Anvil fit the owned Terminator / gun shelves; others thin | draft | 2026-08-22 |

*(Filename keeps the capitalised `S3` by explicit request in the L1 brief; it is the one deviation from lowercase `snake_case` in `KB/`.)*

---

## Kill Team 2024 (KT24 / 3rd Edition)

Second game system, added **2026-08-17** (`kill_team_2024_scaffold`, slice L1). Every page below carries `system: kill_team_2024`. Kept as its own section, not interleaved with the 40K tables above, per the cross-game policy locked in [`docs/handoffs/kill_team_2024_scaffold/track_in.md`](../docs/handoffs/kill_team_2024_scaffold/track_in.md) - **rules stay split between the two games at every layer.**

### Sources (KT24)

| Page | Summary | Confidence | Updated |
|------|---------|------------|---------|
| [[kill_team_2024_core_rules]] | Owned KT24 PDF pointers + quote policy; Full-Scan baseline, `eng_*` patches supersede, Jul 25 lite is intro (omission ≠ patch). Targeting subset owner-verified 2026-08-18 (Patch_Manifest + Target_Eligibility) | verified | 2026-08-18 |
| [[kill_team_kommandos_teams_pdf]] | Path pointer and ingest receipt for the owned Kommandos Teams PDF; shipping quotes under teams/kommandos — no KB datacard dump | draft | 2026-08-21 |
| [[nemesis_operatives]] | Nemesis Operatives dossier — OCR + vision spot-check 2026-08-17; process/titles verified in shipping; tables stay book-only | draft | 2026-08-17 |
| [[warcom_nemesis_operatives_free]] | WarCom preview articles surveyed for free Nemesis numeric profiles — none found (2026-08-17) | draft | 2026-08-17 |
| [[community_kt24_npo_aids]] | Community NPO/KT24 cheat sheets — draft secondary, stale-risk | unverified | 2026-08-17 |
| [[kill_team_necron_photos]] | Path pointer to owner photos of painted Necron models under `C:\Personal\Kill Team\Teams\` used to identify Canoptek Circle, Hierotek Circle, and Tomb World Warrior/Scarab NPOs. Binaries stay outside git. | draft | 2026-08-17 |

### Concepts (KT24)

| Page | Summary | Confidence | Updated |
|------|---------|------------|---------|
| [[turning_points]] | The Strategy-phase / Firefight-phase round structure that replaces 40K's battle round | draft | 2026-08-18 |
| [[activations_apl]] | The alternating single-operative activation loop and the APL action-point budget that gates it | draft | 2026-08-18 |
| [[orders_conceal_engage]] | Engage vs Conceal - the per-activation order that decides what an operative can do and whether it can be targeted | draft | 2026-08-18 |
| [[cover_kill_team]] | KT24 Cover / Obscured / cover save / Vantage — defender-dice bonus, opposite of 40K cover | draft | 2026-08-18 |
| [[control_range_kill_team]] | 1" Control Range - the visibility-gated zone behind marker control, cover, and Fight legality | draft | 2026-08-18 |
| [[injured_operatives]] | The half-Wounds threshold that worsens Move and Hit - not 40K Battle-shock | draft | 2026-08-18 |
| [[valid_target]] | Shoot selection test: visible + order/cover split; Blast/Torrent/Heavy/Seek notes. Quotes stay in shipping | verified | 2026-08-18 |

### Setup (KT24)

| Page | Summary | Confidence | Updated |
|------|---------|------------|---------|
| [[kill_team_terrain]] | Terrain features are parts (Heavy/Light/Vantage/Accessible); cover vs obscured | draft | 2026-08-18 |
| [[killzones_volkus_tomb_world]] | Volkus Door Fight / fire step; Tomb World Close Quarters Guard; operatives vs terrain ownership | draft | 2026-08-18 |

*(Teams, Critical Ops, Joint Ops, and Nemesis Operatives stay index-only this pass — source pages already exist; no faction/unit trees.) *

---

## Directory guides

Short per-directory README stubs restate the page contract for each entity type. They are navigation aids, **not** entity pages: exclude them from orphan-page lint findings and do not catalog them in the typed sections above.

| Directory | Guide |
|-----------|-------|
| `KB/sources/` | [`sources/README.md`](sources/README.md) |
| `KB/concepts/` | [`concepts/README.md`](concepts/README.md) |
| `KB/factions/` | [`factions/README.md`](factions/README.md) |
| `KB/detachments/` | [`detachments/README.md`](detachments/README.md) |
| `KB/units/` | [`units/README.md`](units/README.md) |
| `KB/setup/` | [`setup/README.md`](setup/README.md) |
| `KB/analyses/` | [`analyses/README.md`](analyses/README.md) |

---

## Index maintenance rules

- Add a row **immediately** after creating a page - an uncatalogued page is invisible to every future session
- Copy the page's one-line summary verbatim; if the summary changes, change it here too
- Update the `Updated` date on substantive changes only, not typo fixes
- Keep `Confidence` in sync with the page frontmatter; a drifted confidence value is a lint finding
- Mark orphan pages with `(orphan)` in the Summary column until they gain inbound links
- If a typed section passes ~10 rows, add sub-sections (by faction, then by role)

---

## Related pages

- [[overview]] - what this KB is about and where it stands
- [[glossary]] - terminology lookup
- [[uml_diagrams_org]] · [[flowcharting_uml_activity]] - project flowchart notation (not game rules)
- [[ingest_procedure]] - how to add to this catalog
- [`AGENTS.md`](../AGENTS.md) - schema source of truth

## Units (pointers)
- [[necrons_unit_index]] — Necrons research corpus overview
- [[space_marines_unit_index]] — Space Marines research corpus overview
