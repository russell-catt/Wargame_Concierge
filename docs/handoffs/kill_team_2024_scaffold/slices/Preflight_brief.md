# Preflight — Brief (Kill Team ownership + cross-game policy)

- **Status:** Resolved - Complete
- **Track:** kill_team_2024_scaffold
- **Slice:** Preflight

## Requirements

1. Lock ownership assumptions into `docs/handoffs/kill_team_2024_scaffold/track_in.md`:
   - 10 teams from `C:\Personal\Kill Team\kill_team_2024\Teams\`
   - Kill zones: Volkus ready, 3e Starter ready, Tomb World unassembled, Shadowhunt boards/tokens, 2e starter scatter
   - Critical Ops: both 2024 + 2025 physical decks owned
   - Cross-game sync policy (ruled-in + base-size / dual-legality)
   - Join Ops goals listed
2. Confirm local library roots resolve: `kill_team_2024\` and `kill_team_2021\` (never obsolete `rules\` path)
3. Note Hierotek photo-ID still TBD for 40K; KT inventory may list operative names without 40K mapping
4. Note guide-team assembly/paint detail pending user confirmation where unknown
5. Write `Preflight_implementer.md` recording what was locked

## Depends / User gate

| Dependency | Notes |
|------------|-------|
| User authorized plan execution | YES (2026-08-17) |
| Plan file `kill_team_2024_scaffold_9ae107e8` | Read-only |

## Entrance criteria

| Criterion | Attested |
|-----------|----------|
| Track folder + `track_in.md` exist | YES (bootstrap) |
| Local library paths exist on disk | Verify in Tier 1 |

## Exit criteria

- Ownership tables for teams, kill zones, Crit Ops written into `track_in.md`
- Cross-game miniature-sync + base-size legality policy locked in `track_in.md`
- Join Ops deliverables named
- Model matrix present (Librarian = sonnet; **never fable**)
- Hierotek / photo / S10 blockers noted
- `Preflight_implementer.md` filed

## Tier 1 checks

```powershell
Test-Path 'C:\Personal\Kill Team\kill_team_2024'
Test-Path 'C:\Personal\Kill Team\kill_team_2021'
@(Get-ChildItem 'C:\Personal\Kill Team\kill_team_2024\Teams\*.pdf').Count -eq 10
Test-Path 'C:\Personal\Kill Team\kill_team_2024\Critical Ops\2024'
Test-Path 'C:\Personal\Kill Team\kill_team_2024\Critical Ops\2025'
```

## Tier 2 expectations

Light QA: confirm `track_in.md` contains ownership tables, cross-game policy, model matrix (no fable), and blockers. No content under `games/` required yet.

## Recommended models

| Role | Model |
|------|-------|
| Implementer | `composer-2.5-fast` (or Coordinator wearing hat) |
| QA | `gemini-3.7-flash-high` |

## Inherited documentation

- Plan: `kill_team_2024_scaffold_9ae107e8.plan.md`
- `docs/Game_System_Scaffold.md` §§A2–F
- Prior track format: `docs/handoffs/v1_scaffold/`
