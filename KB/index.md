---
title: KB Index
type: index
system: multi_system
systems: [warhammer_40k_11e, kill_team_2024, the_warcode]
created: 2026-08-16
updated: 2026-09-25
version: 0.9.1
sources: [necron_lists_owner_notes, source_library, local_library_pointers, kill_team_2024_core_rules, kill_team_necron_photos, uml_diagrams_org, warcom_free_core_rules_11e, wahapedia, their_number_is_legion_potentiality_syphon_250, kill_team_kommandos_teams_pdf, legends_field_manual_sm_2026_08, gw_ip_guidelines, warcode_rulebook_v087f, warcode_rulebook_v089f, warcode_tactical_doctrine_field_edition, warcode_web_prelaunch_2026_08, warcode_gamefound_campaign_2026_09, warcode_kickstarter_relaunch_2026_09, warcode_campaign_transition_2026_09, white_dwarf_527, 40k_aug_2026_balance_package, kt_aug_2026_balance_package, sm_codex_oct_2026_preview]
confidence: verified
tags: [index, catalog, kb, kill_team_2024, the_warcode]
---

# KB Index

Master catalog of every page in this knowledge base. Read this first when answering a question: find the relevant pages here, then drill into them.

**Schema source of truth:** [`AGENTS.md`](../AGENTS.md) at the repo root. Entity types, YAML frontmatter, naming, and the ingest / query / lint workflows are defined there, not here. This file is the catalog only.

**Status:** lint complete for Warhammer 40,000 through slice **L2** of `tomb_world_ownership` (2026-08-16); Kill Team 2024 **v0.5.0 Librarian pass (2026-08-18)** rewrote L1 Wahapedia drafts from shipping (targeting subset `verified` on [[kill_team_2024_core_rules]] / [[valid_target]]; other Core topics still `draft`). Teams / ops trees remain index-only.

**Three systems now.** Everything in the typed sections below (Sources through Analyses) is `system: warhammer_40k_11e` unless it appears in **Project notation** (`system: multi_system`, not game rules) or the dedicated **Kill Team 2024 (KT24)** or **The Warcode (the_warcode)** sections. Each game stays split at every layer, including the index. Check a page's own `system:` frontmatter if in doubt.

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
| [[log]] | Append-only chronological record of ingests, queries, and lint passes | verified | 2026-09-25 |
| [[changelog]] | Promotion log: KB pages that shipped into `docs/` or `games/` | verified | 2026-08-18 |
| [[ingest_procedure]] | How a source in `raw/` becomes KB pages in this project | verified | 2026-08-16 |

---

## Sources

One page per ingested source. Location: `KB/sources/`.

| Page | Summary | Confidence | Updated |
|------|---------|------------|---------|
| [[warcom_free_core_rules_11e]] | WarCom-free 11e Core PDF + July universal updates (v1.0, **superseded** by Aug v1.1); numbered-ID quote appendix in shipping; KB paraphrase only | draft | 2026-08-27 |
| [[megabattle_prep_notes_2026_09]] | Owner's Google-chat megabattle notes: three-sector joint war plan for the 945 Conclave + 1000 Gladius team and a packing / etiquette checklist; rules-checked into the megabattle section of both 1000 guides (Necron print 5 pp, Space Marine print 4 pp) | draft | 2026-09-25 |
| [[necron_lists_owner_notes]] | The owner's own Necron expansion blueprint: what is actually owned as of 2026-08-16, and two costed paths from that collection up to a 1,000-point army | draft | 2026-08-17 |
| [[source_library]] | The project's map of where the answers are: owned PDFs, living web references, and the copyright rule that keeps all of it outside git | verified | 2026-08-17 |
| [[local_library_pointers]] | Eight stub files standing in for owned PDFs the repo is not allowed to contain - and all still unread | verified | 2026-08-16 |
| [[wahapedia]] | Community aggregator — unit/stat when WarCom lacks profiles; Legion/Syphon + list fills retrieved 2026-08-19 | draft | 2026-08-19 |
| [[warhammer_community]] | GW FAQs, errata, dataslates — surveyed 2026-08-20 for Legion / Syphon / character revive | draft | 2026-08-20 |
| [[legends_field_manual_sm_2026_08]] | WarCom Legends Field Manual SM points (Servitors / Bike / Attack Bike) retrieved 2026-08-22 for Casual starters | draft | 2026-08-22 |
| [[gw_ip_guidelines]] | Paraphrase of GW community IP guidelines + WarCom download licence; unofficial footer policy for games/ shipping | draft | 2026-08-23 |
| [[white_dwarf_527]] | Owned WD527 tier 1.5 — commentary shipped to rules/setup/armies; system 2-pager + Mission 38 | verified | 2026-08-25 |
| [[40k_aug_2026_balance_package]] | No singular dataslate: Universal Rules v1.1 + Faction Pack v1.2 (Necrons/SM) + MFM v1.3 — Necron Warriors 80→85, SM cores unchanged, disembark move typing | draft | 2026-08-27 |
| [[sm_codex_oct_2026_preview]] | Separate product: Codex SM October 2026 preview — Legendary Proxies / Legends honesty, no early stat rewrite | draft | 2026-08-27 |

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
| [[objective_control]] | Sum OC of models on the terrain **footprint** (**14.01**); re-check every phase/turn (**14.02**); tie = nobody; mission card scores VP; Battle-shock zeroes OC; not KT 1" control | draft | 2026-08-23 |
| [[power_matrix]] | Canoptek Court rule: DZ always; NML/enemy if ≥ half markers; Cryptek/Canoptek two-tier hit re-rolls. **L0 Kill Team correction kept** | draft | 2026-08-20 |
| [[reanimation_protocols]] | Necron army rule: end of your Command phase, D3 wounds per unit (heal first, then return at 1W); wiped = gone. Back-filled from shipping 2026-08-19 | draft | 2026-08-19 |
| [[oath_of_moment]] | The Space Marine army rule: nominate one enemy unit per turn and attack it better. Turns target priority into the defining decision | unverified | 2026-08-16 |

---

## Factions

One page per army. Location: `KB/factions/`.

| Page | Summary | Confidence | Updated |
|------|---------|------------|---------|
| [[necrons]] | Primary army: attrition + Reanimation Protocols; Conclave lists from 250 up to the active 1000-point Doomstalker + Hierotek teaching pack (MFM v1.3, Aug 2026 package) | draft | 2026-09-25 |
| [[space_marines]] | Blood Ravens Codex SM Gladius force; exact 1000 pack splits turn-one shooters from the Chaplain-led Assault Terminator reserve | draft | 2026-09-25 |

---

## Detachments

One page per detachment and its rules package. Location: `KB/detachments/`.

| Page | Summary | Confidence | Updated |
|------|---------|------------|---------|
| [[canoptek_court]] | Canoptek constructs + Power Matrix (two-tier from shipping); Phase 1 shared 245-pt Tomb World force | draft | 2026-08-20 |
| [[cryptek_conclave]] | Cryptek infantry castle; Technosorcerous Augmentations + Potentiality Syphon; 250 list through the 1000 three-brick + Doomstalker teaching list | draft | 2026-09-25 |
| [[gladius_task_force]] | The generalist Space Marine teaching detachment: three once-per-battle movement permissions, flexible stratagems, and a Priority Assets mission identity | draft | 2026-09-25 |
| [[first_company_task_force]] | Elite Terminator / veteran detachment; best owned-shelf alternate to Gladius | draft | 2026-08-22 |
| [[anvil_siege_force]] | Gunline Remain-Stationary detachment; second owned-shelf alternate (Devs + Whirlwind) | draft | 2026-08-22 |

---

## Units

One page per datasheet, written in play terms. Location: `KB/units/`.

| Page | Summary | Confidence | Updated |
|------|---------|------------|---------|
| [[necron_warriors]] | Battleline brick; Their Number is Legion re-rolls RP D3; owned 10+10; MFM v1.3 10-model band 85 (▲+5) | draft | 2026-08-27 |
| [[techmarine]] | Owned Firstborn Techmarine: the exact Matched 1000 pack keeps him independent with Artificer Armour beside the Whirlwind for repair, accuracy and vehicle-side protection | draft | 2026-09-25 |
| [[astartes_servitors]] | Legends infantry ×4 with Techmarine; Casual Gladius only; Mindlock / Servitor Retinue | draft | 2026-08-22 |

Pointer to the full research corpus: [[necrons_unit_index]].

---

## Setup / Missions

Deployment, terrain, missions, and scoring. Location: `KB/setup/`.

| Page | Summary | Confidence | Updated |
|------|---------|------------|---------|
| [[wd527_monthly_mission]] | Mission 38 Converging Ambition — five Disposition Primaries; WD527 Bunker; links system QR | verified | 2026-08-25 |

40K teaching setup also lives under `games/warhammer_40k_11e/setup/`. **Kill Team 2024** setup pages are catalogued in the KT24 section above ([[kill_team_terrain]], [[killzones_volkus_tomb_world]]).

---

## Analyses

Synthesized outputs: matchups, list comparisons, and query answers worth keeping. Location: `KB/analyses/`.

| Page | Summary | Confidence | Updated |
|------|---------|------------|---------|
| [[40k_core_docs_kb_consistency_2026_08_19]] | Filed query/lint 2026-08-19: shipping Core OK; KB OC/Matrix gaps **closed 2026-08-20** from shipping (`kb_shipping_backfill`) | draft | 2026-08-20 |
| [[their_number_is_legion_potentiality_syphon_250]] | Legion + Syphon teaching; heal-first explained; OQs closed 2026-08-20 (WarCom primary) | draft | 2026-08-21 |
| [[inherited_docs_for_S3]] | What L1 hands to S3: the facts stable enough to teach from, the claims that are not, and which unread pointer answers which question | verified | 2026-08-17 |
| [[sm_matched_vs_casual_starters]] | Blood Ravens Gladius Matched vs Casual split; exact Matched 1000 now fields shooters on table and Chaplain-led Assault Terminators in Deep Strike | draft | 2026-09-25 |
| [[sm_owned_detachment_fit]] | Beyond Gladius: 1st Company then Anvil fit the owned Terminator / gun shelves; others thin | draft | 2026-08-22 |
| [[wd527_orks_vs_blood_angels_walkthrough]] | WD527 First Contact battle report — setup through VP finish (BA 46–42) | verified | 2026-08-24 |

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
| [[kt_aug_2026_balance_package]] | No singular dataslate: Core/killzone/mission-pack update logs + priority team online rules — Tomb World teleport/breach, Nemesis Towering Size, Hierotek regen-timing note | draft | 2026-08-27 |

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

## The Warcode (the_warcode)

Third game system, scaffolded **2026-08-23** and refreshed **2026-09-24**. Current mechanics baseline is v0.8.9-F; the lorebook is narrative context only. Rules stay separate from **39.9 (Rawmallet)** and **That other game** at every layer.

### Sources (Warcode)

| Page | Summary | Confidence | Updated |
|------|---------|------------|---------|
| [[warcode_rulebook_v089f]] | Current free mechanics baseline for The Warcode: unchanged core, cards, maps, Protagen, and Ulfari material plus playable MDR Executive Unit and Custodia Silens rosters. | draft | 2026-09-24 |
| [[warcode_tactical_doctrine_field_edition]] | Narrative dossier for The Warcode theatre, chronology, and factions; useful for source-aware setting context but never a mechanics authority. | draft | 2026-09-24 |
| [[warcode_gamefound_campaign_2026_09]] | Historical record of the mixed digital-and-physical Gamefound campaign: launched 2026-09-15, publicly cancelled 2026-09-17, and recorded ended 2026-09-18 with no funds collected. | draft | 2026-09-24 |
| [[warcode_kickstarter_relaunch_2026_09]] | Retrieval-dated source record for the digital-only STL and Print & Play Kickstarter launched 2026-09-23 and scheduled to end 2026-10-23. | draft | 2026-09-24 |
| [[warcode_rulebook_v087f]] | Historical free beta from RedMakers — superseded by [[warcode_rulebook_v089f]] on the same topic, but retained as provenance for unchanged pages and earlier shipping citations. | draft | 2026-09-24 |
| [[warcode_web_prelaunch_2026_08]] | Historical pre-launch marketing snapshot for The Warcode — useful for dated publisher claims, but superseded for current mechanics, faction playability, and campaign offer. | draft | 2026-09-24 |

### Concepts (Warcode)

| Page | Summary | Confidence | Updated |
|------|---------|------------|---------|
| [[warcode_action_points]] | Each activated unit normally receives 2 Action Points, while MDR Order enlarges a future normal activation and Custodia Inspiration creates a delayed one-AP activation. | draft | 2026-09-24 |
| [[warcode_ammo]] | Ranged weapons normally spend one ammunition per shooting action and reload to their printed maximum, but Custodia's Hand Flamethrower creates an unresolved exception. | draft | 2026-09-24 |
| [[warcode_overwatch]] | Overwatch commits a ranged unit to reaction fire, but the current rulebook leaves a gap between its broad action trigger and its narrower named-action list. | draft | 2026-09-24 |
| [[warcode_contracts]] | When trailing after round scoring, draw a secret Contract that names one enemy from the opponent's faction; all four target columns now map to playable rosters. | draft | 2026-09-24 |
| [[warcode_protocol_cards]] | The twenty-card Core of the Machine protocol deck is unchanged in v0.8.9-F: five hazard families across Left, Centre, Right, and Total map scopes. | draft | 2026-09-24 |
| [[warcode_melee_lock]] | Melee Lock normally begins at base contact and forces a risky Disengage or full-activation Escape, while Smasher and Lancer extend Lock to enemies within one inch. | draft | 2026-09-24 |

### Factions (Warcode)

| Page | Summary | Confidence | Updated |
|------|---------|------------|---------|
| [[warcode_protagen_marines]] | Engineering faction in heavy suits — hold ground and trade mobility for resilience; its eight-model roster is unchanged in v0.8.9-F. | draft | 2026-09-24 |
| [[warcode_ulfari]] | Outside-system aliens built to close fast and strike first — lighter armour, higher Agility, and an eight-model roster unchanged in v0.8.9-F. | draft | 2026-09-24 |
| [[warcode_mdr]] | Coordinated support faction whose playable MDR Executive Unit relays extra AP and melee pressure through a Sergeant–Comms network while a Combat Medic rewards compact positioning. | draft | 2026-09-24 |
| [[warcode_dominium]] | Dominium's playable Custodia Silens formation is a control-and-combination roster using Agility pressure, delayed activations, persistent damage, area fire, and extended Melee Lock. | draft | 2026-09-24 |

### Analyses (Warcode)

| Page | Summary | Confidence | Updated |
|------|---------|------------|---------|
| [[warcode_campaign_transition_2026_09]] | The Warcode moved from a cancelled mixed-format Gamefound campaign to a digital-only Kickstarter; the chronology is verified, while explanations for the change remain attributed claims rather than proven causes. | draft | 2026-09-24 |

*(Shipping teaching spine lives under `games/the_warcode/rules/` — KB paraphrase only; quotes scoped to shipping per warcode-quotes rule.)*

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
- [[warcode_rulebook_v089f]] · [[warcode_tactical_doctrine_field_edition]] · [[warcode_gamefound_campaign_2026_09]] · [[warcode_kickstarter_relaunch_2026_09]] - current Warcode sources
- [[warcode_rulebook_v087f]] · [[warcode_web_prelaunch_2026_08]] - historical Warcode sources
- [[warcode_campaign_transition_2026_09]] - Warcode campaign transition analysis
- [[40k_aug_2026_balance_package]] · [[kt_aug_2026_balance_package]] · [[sm_codex_oct_2026_preview]] - Aug 2026 balance package + Oct Codex preview (`dataslate_0826`, 2026-08-27)
- [`AGENTS.md`](../AGENTS.md) - schema source of truth

## Units (pointers)
- [[necrons_unit_index]] — Necrons research corpus overview
- [[space_marines_unit_index]] — Space Marines research corpus overview
