# S6 — Brief (Angels of Death full package + 40K Space Marine sync)

- **Status:** Resolved - Implemented (awaiting QA)
- **Track:** kill_team_2024_scaffold
- **Slice:** S6 (Implementer — teaching content)
- **Model used:** `claude-sonnet-5-thinking-high` (LOCKED)
- **Date:** 2026-08-17

## Requirements

Expand `games/kill_team_2024/teams/angels_of_death/` from the S3 placeholder to a full package matching the S4 (Canoptek Circle) / S5 (Plague Marines) pattern:

1. `README.md` — package entry point, team-at-a-glance, roster shape, document index, 40K cross-game note
2. `Team_Rule_Guide.md` — the two faction rules (Astartes, Chapter Tactics) plus a paraphrased, non-transcribed tour of the four strategy ploys, four firefight ploys, and four faction equipment items
3. `Owned_Models_Inventory.md` — physical model worksheet + the Space Marine 40K sync mapping
4. `Starter_Roster.md` — first-game rosters built from the team's own 1-leader + 5-operative selection rule (no points system in KT), covering the team's one real build decision (Eliminator Sniper vs. Heavy Intercessor Gunner)
5. `Quick_Reference_Play_Guide.md` — **exactly two pages**, page break marked with `<!-- pagebreak -->`
6. `operatives/Operatives_Index.md` — role summary for all 9 named operatives (3 leaders + 6 operative-list entries), no statlines
7. `cards/Card_Schema.md` — stable field contract for future printable cards (S10, user-photo-gated)

**Sources:** Wahapedia [Angel of Death page](https://wahapedia.ru/kill-team3/kill-teams/angel-of-death/) (note: singular "angel-of-death" on the live site, not the plural URL in the original task text — confirmed via search, fetched, retrieval date 2026-08-17); secondary published review (tabletopbattles.com, Goonhammer network) cross-checked for tactical framing only, also retrieved 2026-08-17; local PDF pointer `eng_28-01_kill_team_team_rules_angels_of_death-*.pdf` via `raw/pointers/kill_team_2024_teams.md` (not opened this slice).

**Teaching paraphrase only** — no datasheet statline (APL/Move/Save/Wounds, weapon Atk/Hit/Dmg) or ploy/equipment/ability text transcription anywhere in the package. Base sizes (a physical spec, not rules text) are recorded where they serve the dual-legality cross-check.

### 40K sync requirement

Space Marines (Angels of Death's 40K faction) **already has a full 40K army folder** in this repo (`games/warhammer_40k_11e/armies/space_marines/`), unlike Plague Marines/Death Guard in S5:

- Add a **"Kill Team ownership sync" section** to `games/warhammer_40k_11e/armies/space_marines/Owned_Models_Inventory.md` mapping each Angels of Death operative to its likely 40K datasheet (Captain, Intercessor Squad, Assault Intercessor Squad, Eliminator Squad, Heavy Intercessor Squad), with base size, provenance tagged **"Kill Team (Angels of Death)"**, and dual-legality/ownership left `pending check` throughout.
- Do **not** move any synced rows into the existing "Game-ready" / "Owned - build before play" tables — the 40K collection itself is still an unaudited worksheet (S5 status, unchanged this slice).
- Cross-link both directions: KT package → 40K inventory, 40K `README.md`/inventory → KT package.
- Note: a Coordinator closeout pass had already added a minimal link-only stub to the 40K inventory before this slice started; S6 supersedes it with the full mapping table required by the brief.

### Explicitly out of scope

- Auditing or filling in the Space Marine 40K collection itself (still the S5 worksheet — unrelated to this slice)
- Opening/transcribing the local team-rules PDF (pointer only, not opened this slice)
- Actual printable operative cards (S10 — user-photo-gated)
- `KB/`, `raw/` writes, git commit

## Depends / User gate

| Dependency | Notes |
|------------|-------|
| S3 Resolved - Complete | `angels_of_death/` placeholder + `_Owned_Teams_Inventory.md` row exist |
| S4 (Canoptek Circle), S5 (Plague Marines) | Pattern to match — both completed in parallel this session |
| Do NOT commit | Coordinator / user gate |
| Do NOT push | Unless user asks |

## Entrance criteria

| Criterion | Attested |
|-----------|----------|
| `angels_of_death/README.md` S3 placeholder exists | YES |
| `_Owned_Teams_Inventory.md` has an Angels of Death row | YES (S3) |
| Cross-game policy locked (`track_in.md`) | YES |
| Wahapedia Angel of Death page reachable | YES — fetched 2026-08-17 (singular URL) |
| Space Marines 40K army folder exists to sync into | YES (`games/warhammer_40k_11e/armies/space_marines/`) |

## Exit criteria

- All 7 required files exist under `games/kill_team_2024/teams/angels_of_death/`, plus `operatives/` and `cards/` subfolders
- `Quick_Reference_Play_Guide.md` has exactly one `<!-- pagebreak -->` marker splitting page 1 / page 2 content
- No datasheet statlines or verbatim ploy/equipment/ability text anywhere in the package
- `games/warhammer_40k_11e/armies/space_marines/Owned_Models_Inventory.md` contains a full "Kill Team ownership sync" mapping table with honest `pending check` values, provenance tagged, superseding the earlier link-only stub
- `_Owned_Teams_Inventory.md` and `teams/README.md` updated to reflect S6 complete
- Rising Tide headers on all `games/**` files; no YAML frontmatter stacked
- No GW binaries added; `KB/` and `raw/` untouched
- `S6_implementer.md` filed with locked model recorded, superseding the earlier Coordinator-closeout stub
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
  'games\kill_team_2024\teams\angels_of_death\README.md',
  'games\kill_team_2024\teams\angels_of_death\Team_Rule_Guide.md',
  'games\kill_team_2024\teams\angels_of_death\Owned_Models_Inventory.md',
  'games\kill_team_2024\teams\angels_of_death\Starter_Roster.md',
  'games\kill_team_2024\teams\angels_of_death\Quick_Reference_Play_Guide.md',
  'games\kill_team_2024\teams\angels_of_death\operatives\Operatives_Index.md',
  'games\kill_team_2024\teams\angels_of_death\cards\Card_Schema.md',
  'docs\handoffs\kill_team_2024_scaffold\slices\S6_brief.md',
  'docs\handoffs\kill_team_2024_scaffold\slices\S6_implementer.md'
) | ForEach-Object { "{0,-75} {1}" -f $_, (Test-Path "$root\$_") }

Select-String -Path "$root\games\kill_team_2024\teams\angels_of_death\Quick_Reference_Play_Guide.md" -Pattern '<!-- pagebreak -->' -AllMatches | Measure-Object

Select-String -Path "$root\games\kill_team_2024\teams\_Owned_Teams_Inventory.md" -Pattern 'Angels of Death' -AllMatches | Measure-Object

Select-String -Path "$root\games\warhammer_40k_11e\armies\space_marines\Owned_Models_Inventory.md" -Pattern 'Kill Team ownership sync' -AllMatches | Measure-Object

@(Get-ChildItem $root -Recurse -Include *.pdf,*.webp,*.png,*.jpg -File -ErrorAction SilentlyContinue).Count -eq 0
git -C $root status --porcelain -- KB raw
```

## Feeds

- **S7** — Killzone QR + Crit Ops how-to (unrelated content, but closes out the priority-team trio started S4–S6)
- **S10** — `cards/Card_Schema.md` filled in per-operative once user photos land
- **L3** — Lint pass across all three full-guide packages (Canoptek Circle, Plague Marines, Angels of Death)
