# S4 — Brief (Canoptek Circle full package + 40K inventory sync)

- **Status:** Resolved - Implemented (awaiting QA)
- **Track:** kill_team_2024_scaffold
- **Slice:** S4 (Implementer — teaching content)
- **Date:** 2026-08-17
- **Locked model:** `claude-sonnet-5-thinking-high`

## Requirements

Expand `games/kill_team_2024/teams/canoptek_circle/` from the S3 stub to a full team package:

1. `README.md` — identity, why play, links to every document in the folder
2. `Team_Rule_Guide.md` — Obelisk Node Matrix teaching paraphrase (place/move nodes, matrix formation, matrix buffs at APL/accuracy habit level). Cite Wahapedia (retrieved 2026-08-17) + local PDF pointer `eng_29-04_kill_team_team_rules_canoptek_circle-*.pdf`. No datasheet transcription, no full ploy text dump
3. `Owned_Models_Inventory.md` — map the Tomb World box (Geomancer 1, Tomb Crawlers 2, Macrocytes 5 = Accelerator + Reanimator + 3 Warriors) to the 8 Canoptek Circle operative slots. Assembly/paint carried from the Necron 40K inventory (game-ready). Base size / dual-legality fields, `pending check` where unaudited; 40K ruled-in noted
4. `Starter_Roster.md` — learning roster built entirely from owned models
5. `Quick_Reference_Play_Guide.md` — exactly two pages, visible `<!-- pagebreak -->` marker, Rising Tide footer with verify date. Page 1: during-game habits. Page 2: force-today snapshot
6. `operatives/Operatives_Index.md` — Geomancer, Tomb Crawler (weapon options noted), Accelerator, Reanimator, Warrior — plain-English roles, card-schema-ready fields, no full stat blocks
7. `cards/Card_Schema.md` — sketch of the Tarot-sleeve teaching card format, for S10 once photos land

### 40K sync (required)

Update `games/warhammer_40k_11e/armies/necrons/Owned_Models_Inventory.md` to note the Geomancer, Tomb Crawlers, and Macrocytes also have Kill Team Canoptek Circle provenance, with a dual-legality / base-size column (`pending check` allowed), cross-linked to the KT package. No new 40K datasheet mappings invented beyond what was already listed.

### Explicitly out of scope

- Opening/transcribing the local team PDF (not opened this slice — living Wahapedia page used instead, both cited)
- Real Tarot card content (blocked on S10 user photos)
- Weapon-option confirmation for Tomb Crawlers / Warriors (flagged `pending check`, resolves by physical inspection, not this slice)
- 40K dual-legality determination (flagged `pending check`, resolves when the 40K Necron faction pack is opened and cross-referenced)
- `KB/` writes, `raw/` writes, git commit

## Depends / User gate

| Dependency | Notes |
|------------|-------|
| S3 Resolved - Complete | Stub `README.md` + `_Owned_Teams_Inventory.md` existed |
| Preflight cross-game policy | `track_in.md` — inventories sync, rules stay separate |
| Do NOT commit | Coordinator / user gate |
| Do NOT push | Unless user asks |

## Entrance criteria

| Criterion | Attested |
|-----------|----------|
| `canoptek_circle/README.md` exists as S3 placeholder | YES (S3) |
| `_Owned_Teams_Inventory.md` lists Canoptek Circle row | YES (S3) |
| 40K Necron `Owned_Models_Inventory.md` lists Tomb World as game-ready | YES (`tomb_world_ownership` track) |
| Cross-game policy locked (inventories sync, rules separate) | YES (`track_in.md`) |

## Exit criteria

- All 7 `canoptek_circle/` deliverables exist with Rising Tide headers/footers (`games/**` convention — no YAML frontmatter stacked)
- `Team_Rule_Guide.md` cites Wahapedia (retrieved 2026-08-17) and the local PDF pointer; no full ploy text or datacard statlines reproduced
- `Owned_Models_Inventory.md` maps all 8 operative slots to the Tomb World box with base size and honest `pending check` dual-legality
- `Quick_Reference_Play_Guide.md` is exactly two pages with a visible `<!-- pagebreak -->` marker and a dated verify line
- `operatives/Operatives_Index.md` covers all 5 operative types with card-schema-ready fields and no APL/Move/Save/Wounds or weapon ATK/HIT/DMG values
- `cards/Card_Schema.md` is explicitly marked as a sketch, gated on S10
- 40K Necron `Owned_Models_Inventory.md` updated with KT provenance / base-size / dual-legality notes on the Geomancer, Tomb Crawler, and Macrocyte rows, cross-linked to the KT package, with the Necron Warriors naming collision flagged explicitly
- `_Owned_Teams_Inventory.md` and `teams/README.md` updated to reflect Canoptek Circle as full-package-complete
- No GW binaries added; `KB/` and `raw/` untouched
- `S4_implementer.md` filed with locked model recorded
- No commit, no push

## Recommended models

| Role | Model |
|------|-------|
| Implementer (teaching content) | `claude-sonnet-5-thinking-high` |
| QA | `gpt-5.6-sol-medium` |

## Tier 1 commands

```powershell
$root = 'C:\Personal\Personal_Projects\Wargame_Concierge'

@(
  'games\kill_team_2024\teams\canoptek_circle\README.md',
  'games\kill_team_2024\teams\canoptek_circle\Team_Rule_Guide.md',
  'games\kill_team_2024\teams\canoptek_circle\Owned_Models_Inventory.md',
  'games\kill_team_2024\teams\canoptek_circle\Starter_Roster.md',
  'games\kill_team_2024\teams\canoptek_circle\Quick_Reference_Play_Guide.md',
  'games\kill_team_2024\teams\canoptek_circle\operatives\Operatives_Index.md',
  'games\kill_team_2024\teams\canoptek_circle\cards\Card_Schema.md',
  'games\warhammer_40k_11e\armies\necrons\Owned_Models_Inventory.md',
  'games\kill_team_2024\teams\_Owned_Teams_Inventory.md',
  'games\kill_team_2024\teams\README.md',
  'docs\handoffs\kill_team_2024_scaffold\slices\S4_brief.md',
  'docs\handoffs\kill_team_2024_scaffold\slices\S4_implementer.md'
) | ForEach-Object { "{0,-75} {1}" -f $_, (Test-Path "$root\$_") }

Select-String -Path "$root\games\kill_team_2024\teams\canoptek_circle\Quick_Reference_Play_Guide.md" -Pattern '<!-- pagebreak -->' | Measure-Object

Select-String -Path "$root\games\warhammer_40k_11e\armies\necrons\Owned_Models_Inventory.md" -Pattern 'Canoptek Circle|pending check' -AllMatches | Measure-Object

@(Get-ChildItem $root -Recurse -Include *.pdf,*.webp -File -ErrorAction SilentlyContinue).Count -eq 0
git -C $root status --porcelain -- KB raw
```

## Feeds

- **S5** — Plague Marines full guide + Death Guard sync (same package template)
- **S6** — Angels of Death full guide + Space Marine sync
- **S10** — Photos unblock `cards/Card_Schema.md` content and the Tomb Crawler / Warrior weapon-option checks
- **L3** — Lint pass should verify the Necron Warriors / Canoptek Macrocyte Warrior naming-collision flag stays clear across both systems
