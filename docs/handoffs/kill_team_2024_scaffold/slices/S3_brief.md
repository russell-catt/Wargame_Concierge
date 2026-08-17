# S3 — Brief (Owned inventory + team stubs)

- **Status:** Resolved - Implemented (awaiting QA)
- **Track:** kill_team_2024_scaffold
- **Slice:** S3 (Implementer — structure)
- **Date:** 2026-08-17

## Requirements

1. **`games/kill_team_2024/teams/_Owned_Teams_Inventory.md`** — all 10 owned teams from `Teams\` PDFs with per-row fields:
   - Team name, priority (full guide / stub), assembly/paint, 40K ruled-in status, base size / dual-legality, pointer to [`raw/pointers/kill_team_2024_teams.md`](../../../raw/pointers/kill_team_2024_teams.md)
   - Hierotek: game-ready used set (40K track); photo ID TBD
   - Canoptek: note Tomb World models exist separately for related 40K force
   - Kill-zone ownership summary linking to [`setup/killzones/`](../../../games/kill_team_2024/setup/killzones/)
2. **Stub `README.md`** under seven non-priority team folders: `hierotek_circle`, `celestian_insidiants`, `death_korps`, `deathwatch`, `kommandos`, `murderwing`, `vespid_stingwings` — identity paragraph, inventory link, PDF pointer, “full guide out of scope this track”, 40K sync pending where relevant
3. **Placeholder folders** for three priority teams: `canoptek_circle/`, `plague_marines/`, `angels_of_death/` — short README noting S4–S6 will fill full packages
4. Update [`teams/README.md`](../../../games/kill_team_2024/teams/README.md) to index inventory and folders
5. **`S3_brief.md`**, **`S3_implementer.md`** under `docs/handoffs/kill_team_2024_scaffold/slices/`

### Explicitly out of scope

- Full Canoptek / Plague Marines / Angels packages (**S4–S6**)
- 40K inventory updates (**S4 template**)
- Team PDF ingestion / operative stat transcription
- `KB/` writes, `raw/` writes, git commit

## Depends / User gate

| Dependency | Notes |
|------------|-------|
| S0 Resolved - Complete | Tree + team pointers exist |
| Preflight ownership lock | `track_in.md` |
| L2 | May pipeline; not blocking structure-only S3 |
| Do NOT commit | Coordinator / user gate |
| Do NOT push | Unless user asks |

## Entrance criteria

| Criterion | Attested |
|-----------|----------|
| `raw/pointers/kill_team_2024_teams.md` lists 10 teams | YES (S0) |
| `games/kill_team_2024/teams/` stub exists | YES (S0) |
| Cross-game policy locked | YES (`track_in.md`) |

## Exit criteria

- `_Owned_Teams_Inventory.md` covers all 10 teams with required columns
- Dual-legality honesty: owned ≠ dual-legal explained; pending checks default
- Seven stub READMEs + three priority placeholders exist
- Kill-zone section present (inventory or link to `setup/killzones/`)
- `teams/README.md` indexes new artifacts
- Rising Tide headers on `games/**` files; no YAML frontmatter stacked
- No GW binaries added; **`KB/`** and **`raw/`** untouched
- **`S3_implementer.md`** filed with locked model recorded
- **No commit, no push**

## Recommended models

| Role | Model |
|------|-------|
| Implementer (structure) | `composer-2.5-fast` |
| QA (light) | `gemini-3.7-flash-high` |

## Tier 1 commands

```powershell
$root = 'C:\Personal\Personal_Projects\Wargame_Concierge'

@(
  'games\kill_team_2024\teams\_Owned_Teams_Inventory.md',
  'games\kill_team_2024\teams\canoptek_circle\README.md',
  'games\kill_team_2024\teams\plague_marines\README.md',
  'games\kill_team_2024\teams\angels_of_death\README.md',
  'games\kill_team_2024\teams\hierotek_circle\README.md',
  'games\kill_team_2024\teams\celestian_insidiants\README.md',
  'games\kill_team_2024\teams\death_korps\README.md',
  'games\kill_team_2024\teams\deathwatch\README.md',
  'games\kill_team_2024\teams\kommandos\README.md',
  'games\kill_team_2024\teams\murderwing\README.md',
  'games\kill_team_2024\teams\vespid_stingwings\README.md',
  'docs\handoffs\kill_team_2024_scaffold\slices\S3_brief.md',
  'docs\handoffs\kill_team_2024_scaffold\slices\S3_implementer.md'
) | ForEach-Object { "{0,-70} {1}" -f $_, (Test-Path "$root\$_") }

Select-String -Path "$root\games\kill_team_2024\teams\_Owned_Teams_Inventory.md" -Pattern 'Angels of Death|Canoptek Circle|Celestian|Death Korps|Deathwatch|Hierotek|Kommandos|Murderwing|Plague Marines|Vespid' -AllMatches | Measure-Object

@(Get-ChildItem $root -Recurse -Include *.pdf,*.webp -File -ErrorAction SilentlyContinue).Count -eq 0
git -C $root status --porcelain -- KB raw
```

## Feeds

- **S4** — Canoptek Circle full guide + Necron 40K sync template
- **S5** — Plague Marines full guide + Death Guard sync
- **S6** — Angels of Death full guide + Space Marine sync
- **S10** — Photos may resolve assembly/paint and Hierotek photo ID
