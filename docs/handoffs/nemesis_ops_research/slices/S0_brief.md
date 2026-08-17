# S0 — Brief (Cleanup + rename + stubs)

- **Status:** Ready
- **Track:** nemesis_ops_research
- **Slice:** S0
- **Intended Implementer model:** `composer-2.5-fast`
- **Intended QA model:** `gemini-3.7-flash-high`

## Requirements

1. **Delete** `C:\Personal\Kill Team\kill_team_2024\kill-team-nemesis-operatives-eng.pdf`
2. **Scrub live repo mentions** of filename `kill-team-nemesis-operatives-eng.pdf` from live surfaces (`games/`, `KB/`, `raw/pointers/`, `reference/`, root docs as needed). Historical closed slice reports under `docs/handoffs/kill_team_2024_scaffold/slices/` may keep historical mentions; note rename/delete in both tracks' `track_in.md` instead of mass-rewriting closed reports.
3. **Rename** `games/kill_team_2024/join_ops` → `joint_ops`
4. **Link sweep** all live shipping / KB / pointer / README links that pointed at `join_ops/` → `joint_ops/`
5. **Stub** `games/kill_team_2024/nemesis_ops/` with Rising Tide headers:
   - `README.md`
   - `How_To_Create_A_Nemesis_Operative.md` (REQUIRED stub)
   - `Custom_Builder.md`
   - `Mission_Packs.md`
   - `Worked_Examples.md`
   - `Modes_And_Cards.md`
   - `WarCom_Free_Statlines.md` (REQUIRED stub)
   - `Open_Questions.md`
6. **Update pointer** `raw/pointers/kill_team_2024_nemesis_operatives.md` → dossier only (remove eng.pdf row; note deletion date)
7. Update `games/kill_team_2024/README.md` subtree map for `joint_ops/` + `nemesis_ops/`
8. Note rename in `docs/handoffs/kill_team_2024_scaffold/track_in.md` and this track's `track_in.md`
9. File `S0_implementer.md` — **Commit: pending**

## Depends / User gate

| Dependency | Notes |
|------------|-------|
| Preflight Resolved - Complete | Required |
| Do NOT commit | Coordinator / user gate |
| Do NOT push | Never this track unless asked |

## Entrance criteria

| Criterion | Attested |
|-----------|----------|
| Preflight PDFs confirmed | Verify |
| OCR path locked in track_in | Verify |
| `join_ops/` exists | Verify |

## Exit criteria

- eng.pdf deleted from disk
- Zero live shipping/KB/pointer mentions of eng.pdf filename (historical handoff slice reports OK)
- `joint_ops/` exists; `join_ops/` gone
- Live links updated (no broken `join_ops/` shipping links)
- `nemesis_ops/` stubs including How_To_Create + WarCom_Free_Statlines
- Pointer = dossier only
- `S0_implementer.md` filed; Commit: pending

## Tier 1 commands

```powershell
$root = 'C:\Personal\Personal_Projects\Wargame_Concierge'
-not (Test-Path "C:\Personal\Kill Team\kill_team_2024\kill-team-nemesis-operatives-eng.pdf")
Test-Path "$root\games\kill_team_2024\joint_ops"
-not (Test-Path "$root\games\kill_team_2024\join_ops")
Test-Path "$root\games\kill_team_2024\nemesis_ops\How_To_Create_A_Nemesis_Operative.md"
Test-Path "$root\games\kill_team_2024\nemesis_ops\WarCom_Free_Statlines.md"
Select-String -Path "$root\games\**\*.md","$root\KB\**\*.md","$root\raw\pointers\*.md" -Pattern 'kill-team-nemesis-operatives-eng' -SimpleMatch -ErrorAction SilentlyContinue
Select-String -Path "$root\games\**\*.md","$root\KB\**\*.md" -Pattern 'join_ops' -SimpleMatch -ErrorAction SilentlyContinue
```

## Tier 2 expectations

QA confirms delete, rename, stubs, pointer dossier-only, and greps clean on live surfaces.

## Copyright

- Teaching stubs only; no datasheet transcription
- Do not copy PDFs into git
