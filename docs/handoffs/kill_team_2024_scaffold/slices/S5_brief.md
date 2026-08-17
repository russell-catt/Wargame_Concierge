# S5 — Brief (Plague Marines full package + 40K sync note)

- **Status:** Resolved - Implemented (awaiting QA)
- **Track:** kill_team_2024_scaffold
- **Slice:** S5 (Implementer — teaching content)
- **Date:** 2026-08-17

## Requirements

Expand `games/kill_team_2024/teams/plague_marines/` from the S3 placeholder to a full package matching the S4 (Canoptek Circle) pattern:

1. `README.md` — package entry point, team-at-a-glance, document index, 40K cross-game note
2. `Team_Rule_Guide.md` — the three faction rules (Astartes, Poison, Disgustingly Resilient) plus a paraphrased, non-transcribed tour of strategy ploys, firefight ploys, and faction equipment
3. `Owned_Models_Inventory.md` — physical model worksheet + the Death Guard / 40K sync note
4. `Starter_Roster.md` — first-game roster built by role coverage across the team's seven operatives (no points system in KT)
5. `Quick_Reference_Play_Guide.md` — **exactly two pages**, page break marked with `<!-- pagebreak -->`
6. `operatives/Operatives_Index.md` — master table of the seven named operatives, no statlines
7. `cards/Card_Schema.md` — stable field contract for future printable cards (S10, user-photo-gated)

**Sources:** Wahapedia [Plague Marines page](https://wahapedia.ru/kill-team3/kill-teams/plague-marines/), fetched, retrieval date 2026-08-17; local PDF pointer `eng_29-04_kt_teamrules_plague_marines-*.pdf` via `raw/pointers/kill_team_2024_teams.md` (not opened this slice).

**Teaching paraphrase only** — no datasheet statline (APL/Move/Save/Wounds, weapon Atk/Hit/Dmg) or ploy/equipment text transcription anywhere in the package.

### 40K sync requirement

Death Guard (Plague Marines' 40K faction) has **no existing 40K army inventory** in this repo, and the locked 40K track scope is Necrons + Space Marines only:

- Document `40K ruled-in: pending / N/A this track` and `base size: pending check` in `Owned_Models_Inventory.md` — do not invent ownership or dual-legality.
- Do not force the note into the Space Marines inventory (wrong faction).
- Optionally create a **minimal cross-link stub** under `games/warhammer_40k_11e/` if no Death Guard folder exists — explicitly not a full army tree.

### Explicitly out of scope

- Full 40K Death Guard army package (README beyond a minimal stub, army rule guide, detachment, starter lists, unit research)
- Opening/transcribing the local team-rules PDF (pointer only, not opened this slice)
- Actual printable operative cards (S10 — user-photo-gated)
- `KB/`, `raw/` writes, git commit

## Depends / User gate

| Dependency | Notes |
|------------|-------|
| S3 Resolved - Complete | `plague_marines/` placeholder + `_Owned_Teams_Inventory.md` row exist |
| S4 (Canoptek Circle) | Pattern to match — completed in parallel this session |
| Do NOT commit | Coordinator / user gate |
| Do NOT push | Unless user asks |

## Entrance criteria

| Criterion | Attested |
|-----------|----------|
| `plague_marines/README.md` S3 placeholder exists | YES |
| `_Owned_Teams_Inventory.md` has a Plague Marines row | YES (S3) |
| Cross-game policy locked (`track_in.md`) | YES |
| Wahapedia Plague Marines page reachable | YES — fetched 2026-08-17 |

## Exit criteria

- All 7 required files exist under `games/kill_team_2024/teams/plague_marines/`, plus `operatives/` and `cards/` subfolders
- `Quick_Reference_Play_Guide.md` has exactly one `<!-- pagebreak -->` marker splitting page 1 / page 2 content
- No datasheet statlines or verbatim ploy/equipment/ability text anywhere in the package
- `Owned_Models_Inventory.md` contains the Death Guard / 40K sync note with honest `pending` / `N/A this track` values
- Minimal Death Guard 40K cross-link stub created at `games/warhammer_40k_11e/armies/death_guard/README.md` — no full army tree
- `_Owned_Teams_Inventory.md` and `teams/README.md` updated to reflect S5 complete
- Rising Tide headers on all `games/**` files; no YAML frontmatter stacked
- No GW binaries added; `KB/` and `raw/` untouched
- `S5_implementer.md` filed with locked model recorded
- No commit, no push

## Recommended models

| Role | Model |
|------|-------|
| Implementer (teaching content) | `claude-sonnet-5-thinking-high` (LOCKED) |
| QA | `gpt-5.6-sol-medium` |

## Tier 1 commands

```powershell
$root = 'C:\Personal\Personal_Projects\Wargame_Concierge'

@(
  'games\kill_team_2024\teams\plague_marines\README.md',
  'games\kill_team_2024\teams\plague_marines\Team_Rule_Guide.md',
  'games\kill_team_2024\teams\plague_marines\Owned_Models_Inventory.md',
  'games\kill_team_2024\teams\plague_marines\Starter_Roster.md',
  'games\kill_team_2024\teams\plague_marines\Quick_Reference_Play_Guide.md',
  'games\kill_team_2024\teams\plague_marines\operatives\Operatives_Index.md',
  'games\kill_team_2024\teams\plague_marines\cards\Card_Schema.md',
  'games\warhammer_40k_11e\armies\death_guard\README.md',
  'docs\handoffs\kill_team_2024_scaffold\slices\S5_brief.md',
  'docs\handoffs\kill_team_2024_scaffold\slices\S5_implementer.md'
) | ForEach-Object { "{0,-75} {1}" -f $_, (Test-Path "$root\$_") }

Select-String -Path "$root\games\kill_team_2024\teams\plague_marines\Quick_Reference_Play_Guide.md" -Pattern '<!-- pagebreak -->' -AllMatches | Measure-Object

Select-String -Path "$root\games\kill_team_2024\teams\_Owned_Teams_Inventory.md" -Pattern 'Plague Marines' -AllMatches | Measure-Object

@(Get-ChildItem $root -Recurse -Include *.pdf,*.webp,*.png,*.jpg -File -ErrorAction SilentlyContinue).Count -eq 0
git -C $root status --porcelain -- KB raw
```

## Feeds

- **S6** — Angels of Death full guide + Space Marine sync (same pattern, third and final priority team)
- **S10** — `cards/Card_Schema.md` filled in per-operative once user photos land
- **L3** — Lint pass across all three full-guide packages
