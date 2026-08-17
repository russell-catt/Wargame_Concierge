<!--
FILE: games/kill_team_2024/teams/plague_marines/cards/Card_Schema.md
VERSION: v1.0 (2026-08-17)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, slice S5)

DOCUMENT_TYPE: Reusable Schema / Field Contract
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: Kill Team - 2024 / 3rd Edition (KT24)
TEAM: Plague Marines
REFERENCE_STATUS: Schema only - no cards generated yet. Blocked on user photos per S10.

SOURCES:
  - games/warhammer_40k_11e/armies/space_marines/units/_schema.md (the 40K unit-research schema pattern this is adapted from)
  - docs/Game_System_Scaffold.md Sec E ("Printable per-unit cards") and Sec C ("Unit research file contents")
  - docs/handoffs/kill_team_2024_scaffold/slices/S10_brief.md (the slice that will fill this schema in)

PURPOSE:
  Define the stable field contract that one printable operative card will
  follow, before any card is generated. Filling in actual cards is S10 -
  user-gated on photos of the owned Plague Marines models - so this file
  intentionally contains no per-operative data.

UPDATE_TRIGGER:
  Update if a field proves insufficient once S10 starts generating real
  cards. Distil any Plague-Marines-specific lesson back into this schema
  before the next team's card_schema copies it.
-->

# Card Schema - Plague Marines operative cards

**No cards exist yet.** This file only defines the shape one card will take once S10 (photos -> Tarot-format unit cards, ~70x120mm) is unblocked. Do not invent per-operative card content ahead of that slice.

---

## Why a schema file, separate from the cards

Kill Team datacard statlines are never reproduced verbatim in this repository (see [`../Team_Rule_Guide.md`](../Team_Rule_Guide.md) and [`../operatives/Operatives_Index.md`](../operatives/Operatives_Index.md)). A printable card generated from this schema must stay inside that same rule: it teaches *how to use* the operative, and it may cite base size, role, and keywords, but it does not restate ATK/HIT/DMG or APL/Move/Save/Wounds numbers - those live only in the owned PDF or the Kill Team app.

---

## Required fields per card

| Field | Meaning |
|-------|---------|
| `operative_name` | Exact name matching [`Operatives_Index.md`](../operatives/Operatives_Index.md) |
| `slug` | `snake_case` filename stem, e.g. `plague_marine_champion` |
| `role_slot` | One of: Leader, Grenadier/support, Melee specialist, Ranged fire support, Support/objective specialist, Psyker/support caster, Troop/generalist |
| `base_size_mm` | Physical base diameter - photo-confirmed once owned models are identified, not assumed from the datacard alone |
| `faction_keywords` | List, matching `Operatives_Index.md` |
| `signature_trait_paraphrase` | One or two sentences, teaching paraphrase only - no statline, no verbatim ability text |
| `job_one_liner` | The single sentence a beginner reads to decide whether to activate this operative this turn |
| `assembly_state` | Assembled / on sprue / converted - from the owned collection, once photo-IDed |
| `paint_state` | Painted / primed / bare / unknown |
| `photo_source` | Which user photo (filename or session reference) this card's assembly/paint fields were confirmed against |
| `research_date` | Date the card's content was last checked against a source |
| `cross_check_status` | `draft` (Wahapedia only, current default) / `verified` (checked against the owned PDF) |
| `sources` | Pointer(s) used - at minimum the Wahapedia URL and retrieval date |

---

## Conventions

- **UTF-8, no BOM.** No binaries, no scanned card art, no publisher photography - describe the model in words if a visual reference is needed.
- **One file per operative** under `cards/`, named `{slug}.md`, once S10 runs.
- **Field names are locked** once the first real card is generated - add fields rather than renaming them, so the corpus does not fragment mid-team.
- **This schema is reusable.** Canoptek Circle and Angels of Death should copy this file's structure into their own `cards/Card_Schema.md` rather than re-deriving it.

---

## What S10 needs before it can fill this in

1. User photos of the owned Plague Marines models (session attachment or a local path outside the binaries policy).
2. Per-operative assembly and paint confirmation from those photos.
3. A cross-check pass against the owned team-rules PDF (still unopened as of this slice) so `cross_check_status` can move from `draft` to `verified`.

Until then, this file is the only artifact under `cards/` - see [`../../../../docs/handoffs/kill_team_2024_scaffold/slices/S10_brief.md`](../../../../docs/handoffs/kill_team_2024_scaffold/slices/S10_brief.md).

---

## Related pages

- [`../operatives/Operatives_Index.md`](../operatives/Operatives_Index.md) - the seven operatives this schema will cover
- [`../Team_Rule_Guide.md`](../Team_Rule_Guide.md) - the no-statline-transcription rule this schema follows
- [`../Owned_Models_Inventory.md`](../Owned_Models_Inventory.md) - assembly/paint state, once audited
- [`../../../../games/warhammer_40k_11e/armies/space_marines/units/_schema.md`](../../../../games/warhammer_40k_11e/armies/space_marines/units/_schema.md) - the 40K schema pattern this was adapted from

---

## Change Log

- v1.0 (2026-08-17): Initial schema (slice S5) - field contract only, no cards. Adapted from the 40K unit-research `_schema.md` pattern and the Game System Scaffold's per-unit research contents.

## Attribution

- Project: Wargame_Concierge
- Maintainer: Russell Catt
- Kill Team is a trademark of Games Workshop Limited. This document is a personal teaching paraphrase and reproduces no publisher text, art, or datacard statlines.

## Rising Tide Notes

- This document follows Rising Tide documentation standards.
- Keep the receipts. No card content should be invented ahead of S10's photo-gated pass.
