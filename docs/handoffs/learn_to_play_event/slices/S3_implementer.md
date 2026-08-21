# S3 — Implementer report (Plague Marines kid refresh)

- **Track:** `learn_to_play_event`
- **Slice:** S3
- **Status:** Resolved - Implemented
- **Model:** `inherit`
- **Date:** 2026-08-21
- **Commit:** pending (IMP-09 deferred; subagent never git)

## Exit criteria self-check

| Criterion | Result |
|-----------|--------|
| Roster = 1 Champion + 5 unique = 6; no "suggested first four" as legal list | PASS — `Starter_Roster.md` |
| QR kid-checkable; still 2 pages (`<!-- pagebreak -->`); SOURCES owned PDF; snapshot says 6 | PASS — `Quick_Reference_Play_Guide.md` |
| Playbook four questions + vs Kommandos; cites volkus.md | PASS — `Volkus_Playbook.md` |
| README reflects PDF opened / cross-checked | PASS — `README.md` |
| Optional "What it means" after quotes (quotes kept) | PASS — `Team_Rule_Guide.md` |
| No raw/ writes; no GW binaries; HTML cards untouched | PASS |

## Files touched

| Path | Change |
|------|--------|
| `games/kill_team_2024/teams/plague_marines/Starter_Roster.md` | Legal 6-op roster from owned PDF; ownership pending check |
| `games/kill_team_2024/teams/plague_marines/Quick_Reference_Play_Guide.md` | 12yo rewrite; 2 pages; Astartes/Poison kid phrasing |
| `games/kill_team_2024/teams/plague_marines/Volkus_Playbook.md` | **Created** — Volkus + elite/horde/balanced + vs Kommandos |
| `games/kill_team_2024/teams/plague_marines/Team_Rule_Guide.md` | "What it means" after each quote |
| `games/kill_team_2024/teams/plague_marines/README.md` | PDF cross-check; 6-op; playbook indexed |

## Not touched

- `cards/*.html` (existing HTML cards kept)
- `raw/`
- git commit --trailer "Co-authored-by: Cursor <cursoragent@cursor.com>" / push

## Notes for QA

- Saturday table picks Champion + Warrior + Heavy Gunner + Fighter + Icon Bearer + Bombardier; Plaguecaster optional swap.
- Poison kid line: put a token; they get hurt when they activate.
- Astartes kid line: two Shoots OR two Fights, not mixed.
