# S2 — Brief (Setup + killzones + Critical Ops README)

- **Status:** Resolved - Complete
- **Track:** kill_team_2024_scaffold
- **Slice:** S2

## Requirements

1. Create `games/kill_team_2024/setup/Board_Setup.md` — table/killzone size habits, deployment/pre-game checklist at beginner level. Cite mission packs generally; Volkus and the 3e Starter Set are play-now.
2. Create `games/kill_team_2024/setup/Terrain_Basics.md` — cover/obscuring/intervening at teaching level; enough terrain; do not transcribe official templates.
3. Create five kill-zone pages under `games/kill_team_2024/setup/killzones/`:
   - `volkus.md` — READY, play-now
   - `starter_set_3e.md` — READY, play-now
   - `shadowhunt.md` — boards + tokens owned
   - `tomb_world.md` — UNASSEMBLED
   - `starter_set_2e_scatter.md` — filler only, not a full killzone substitute
4. Expand `games/kill_team_2024/critical_ops/README.md` — how the owned 2024 + 2025 decks plug into a game; point to `raw/pointers/kill_team_2024_critical_ops.md`; no card art or transcription of full card text/lists.
5. Update `games/kill_team_2024/setup/README.md` and `games/kill_team_2024/setup/killzones/README.md` from S0 stubs to real indexes.

## Depends / User gate

| Dependency | Notes |
|------------|-------|
| Preflight + S0 Resolved - Complete | Required — ownership lock + tree stubs |
| Ownership table (`track_in.md`) | Volkus/3e Starter Ready; Shadowhunt boards+tokens; Tomb World unassembled; 2e scatter filler |
| Mission pack pointers (`raw/pointers/kill_team_2024_missions.md`) | Required for killzone citations |
| Do NOT commit | Coordinator / user gate |
| Do NOT push | Never this track unless asked |

## Entrance criteria

| Criterion | Attested |
|-----------|----------|
| `setup/` and `setup/killzones/` stub READMEs exist (S0) | YES |
| Ownership table locked in `track_in.md` | YES |
| `raw/pointers/kill_team_2024_missions.md` and `kill_team_2024_critical_ops.md` exist | YES |

## Exit criteria

- Two people can set up **Volkus** or the **3e Starter Set** from these docs alone, honestly flagging what still needs checking in owned PDFs
- No official terrain templates, mission maps, or card lists transcribed
- No binaries added
- All five killzone statuses match the `track_in.md` / `teams/_Owned_Teams_Inventory.md` lock
- `setup/README.md` and `killzones/README.md` read as real indexes, not stubs
- `S2_implementer.md` filed

## Tier 1 commands

```powershell
$root = 'C:\Personal\Personal_Projects\Wargame_Concierge'
Test-Path "$root\games\kill_team_2024\setup\Board_Setup.md"
Test-Path "$root\games\kill_team_2024\setup\Terrain_Basics.md"
Test-Path "$root\games\kill_team_2024\setup\killzones\volkus.md"
Test-Path "$root\games\kill_team_2024\setup\killzones\starter_set_3e.md"
Test-Path "$root\games\kill_team_2024\setup\killzones\shadowhunt.md"
Test-Path "$root\games\kill_team_2024\setup\killzones\tomb_world.md"
Test-Path "$root\games\kill_team_2024\setup\killzones\starter_set_2e_scatter.md"
Select-String -Path "$root\games\kill_team_2024\critical_ops\README.md" -Pattern 'kill_team_2024_critical_ops' -Quiet
@(Get-ChildItem $root -Recurse -Include *.pdf,*.webp -File -ErrorAction SilentlyContinue).Count -eq 0
```

## Tier 2 expectations

QA confirms: killzone statuses match the ownership lock; Cover vs Obscured explained without transcribing rules text verbatim; no card art/lists in `critical_ops/README.md`; every page carries a Rising Tide header/footer with a retrieval date; honest "verify against owned PDFs" language present on every new page; no binaries.

## Recommended models

| Role | Model |
|------|-------|
| Implementer | `claude-sonnet-5-thinking-high` (LOCKED) |
| QA | `gpt-5.6-sol-medium` |

## Inherited documentation

- Plan S2 section + `track_in.md` ownership tables (2026-08-17)
- Prior setup-page style: `games/warhammer_40k_11e/setup/Board_Setup.md`, `Terrain_Basics.md`, `setup/README.md`
- `raw/pointers/kill_team_2024_missions.md`, `kill_team_2024_critical_ops.md`, `kill_team_2024_core.md`, `kill_team_2024_approved_ops.md`
