# S0 — Brief (Pointers + system tree stub)

- **Status:** Resolved - Complete
- **Track:** kill_team_2024_scaffold
- **Slice:** S0

## Requirements

1. Create `raw/pointers/` markdown stubs for Kill Team (path pointers only; never copy PDFs):
   - Core rules, lite rules, update logs, approved ops, universal equipment
   - Teams (10 owned team-rule PDFs)
   - Mission packs (Volkus, Shadowhunt, Tomb World, Hivestorm, Titus, Terror on Devlan, …)
   - Critical Ops 2024 + 2025 folders
   - Nemesis Operatives (+ dossier)
   - Terror on Devlan Dossier
   - Terrain templates if present
   - **Screen_Captures** (Necrons WD517 + Procession) — label **White Dwarf / secondary trust**; no `.webp` in git
   - KT21 / 2e local PDFs under `kill_team_2021\`
2. Stub `games/kill_team_2024/` tree:
   - `README.md` (edition + vocabulary mapping)
   - `rules/`, `setup/killzones/`, `critical_ops/`, `join_ops/`, `teams/`
3. Seed `reference/kill_team_2e/README.md` pointing at local `kill_team_2021\`
4. Update `reference/Source_Library.md` with Kill Team catalog rows
5. Update `raw/pointers/README.md` to mention Kill Team pointers
6. **No binaries.** Confirm zero new `.pdf` / `.webp` under the repo from this slice

## Depends / User gate

| Dependency | Notes |
|------------|-------|
| Preflight Resolved - Complete (or concurrent Coord lock) | Required |
| Do NOT commit | Coordinator / user gate |
| Do NOT push | Never this track unless asked |

## Entrance criteria

| Criterion | Attested |
|-----------|----------|
| Preflight ownership + policy locked in `track_in.md` | Verify |
| Library paths use `kill_team_2024\` / `kill_team_2021\` only | Verify |

## Exit criteria

- Pointer files resolve to current library layout
- WD Screen_Captures pointers state secondary trust class
- `games/kill_team_2024/` stub tree exists including `join_ops/`
- `reference/kill_team_2e/README.md` exists and is quarantined as non-play truth
- `Source_Library.md` has KT24 + KT21 + living web rows
- No GW binaries in git working tree additions
- `S0_implementer.md` filed

## Tier 1 commands

```powershell
$root = 'C:\Personal\Personal_Projects\Wargame_Concierge'
Test-Path "$root\raw\pointers\kill_team_2024_core.md"
Test-Path "$root\games\kill_team_2024\README.md"
Test-Path "$root\games\kill_team_2024\join_ops"
Test-Path "$root\reference\kill_team_2e\README.md"
Select-String -Path "$root\reference\Source_Library.md" -Pattern 'kill_team_2024' -Quiet
@(Get-ChildItem $root -Recurse -Include *.pdf,*.webp -File -ErrorAction SilentlyContinue).Count -eq 0
```

## Tier 2 expectations

QA confirms paths, no binaries, WD trust labelling, vocabulary uses `teams/` not `armies/`, and Source_Library rows exist.

## Recommended models

| Role | Model |
|------|-------|
| Implementer | `composer-2.5-fast` |
| QA | `gemini-3.7-flash-high` |

## Inherited documentation

- Plan S0 section + local library layout (2026-08-17)
- `track_in.md` ownership tables
- Prior pointer style: `raw/pointers/rules_core.md`
