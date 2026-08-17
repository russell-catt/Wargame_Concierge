# Preflight — Brief (Nemesis Ops Research)

- **Status:** Ready
- **Track:** nemesis_ops_research
- **Slice:** Preflight
- **Role:** Coordinator
- **Intended model:** inherit (Coordinator)

## Requirements

1. Confirm on disk:
   - Dossier: `C:\Personal\Kill Team\kill_team_2024\1063073009-Kill-Team-Nemesis-Operatives-Dossier.pdf`
   - Delete target: `C:\Personal\Kill Team\kill_team_2024\kill-team-nemesis-operatives-eng.pdf`
   - Community pair (both present)
2. Lock OCR sidecar path beside dossier (`.ocr.txt` preferred)
3. Note WarCom free-statline research scope for S1b
4. Confirm `join_ops/` exists for rename in S0
5. File Preflight result into `track_in.md` rollup + this report

## Exit criteria

- Track Ready (Preflight Resolved - Complete)
- `track_in.md` exists with model matrix, OCR path, Community pair, copyright rules
- `S0_brief.md` Ready
- No blockers that prevent S0 delete/rename/stub work

## Tier 1 commands

```powershell
Test-Path "C:\Personal\Kill Team\kill_team_2024\1063073009-Kill-Team-Nemesis-Operatives-Dossier.pdf"
Test-Path "C:\Personal\Kill Team\kill_team_2024\kill-team-nemesis-operatives-eng.pdf"
Test-Path "C:\Personal\Kill Team\Community Content\The Kill Team 24 NPO Cheat Sheet Vers 1.1 ALTERNATIVE TEST.pdf"
Test-Path "C:\Personal\Kill Team\Community Content\The Kill Team 24 Cheat Sheet Vers 1.21.pdf"
Test-Path "C:\Personal\Personal_Projects\Wargame_Concierge\games\kill_team_2024\join_ops"
```
