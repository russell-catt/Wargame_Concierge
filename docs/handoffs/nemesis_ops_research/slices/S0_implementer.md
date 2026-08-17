# S0 — Implementer report (Cleanup + rename + stubs)

- **Status:** Resolved - Implemented (pending QA)
- **Track:** nemesis_ops_research
- **Slice:** S0
- **Model used:** composer-2.5-fast
- **Commit:** pending (Coordinator gate — do not commit/push)

## Work performed

1. Deleted mislabeled local PDF from disk (Nemesis Claw retailer listing, not Nemesis Operatives rules).
2. Scrubbed live `kill-team-nemesis-operatives-eng` filename mentions from `games/`, `KB/`, `raw/pointers/` — replaced with deletion note; primary source is dossier only. Historical scaffold slice reports left unchanged.
3. Renamed `games/kill_team_2024/join_ops/` → `joint_ops/` via `Move-Item` (directory was untracked; `git mv` reported empty source).
4. Link sweep: updated live paths in shipping, KB, pointers, killzone QR, both tracks' `track_in.md`; updated `FILE:` headers inside renamed `joint_ops/` files.
5. Created `games/kill_team_2024/nemesis_ops/` stub subtree (8 files, Rising Tide headers + VERIFY footers).
6. Updated `raw/pointers/kill_team_2024_nemesis_operatives.md` to dossier-only; noted deletion and OCR pending S1.
7. Updated `games/kill_team_2024/README.md` subtree map for `joint_ops/` + `nemesis_ops/`.
8. Updated rollup in `docs/handoffs/nemesis_ops_research/track_in.md` — S0 → Resolved - Implemented.

## Commands run + results

| Command / check | Result |
|-----------------|--------|
| `Remove-Item "C:\Personal\Kill Team\kill_team_2024\kill-team-nemesis-operatives-eng.pdf"` | PASS — file deleted |
| `git mv games/kill_team_2024/join_ops joint_ops` | FAIL — untracked empty source for git |
| `Move-Item games/kill_team_2024/join_ops joint_ops` | PASS — `joint_ops/` exists, `join_ops/` gone |
| `Test-Path ...\nemesis_ops\How_To_Create_A_Nemesis_Operative.md` | PASS |
| `Test-Path ...\nemesis_ops\WarCom_Free_Statlines.md` | PASS |
| `Select-String` eng.pdf on `games/**`, `KB/**`, `raw/pointers/*.md` | PASS — zero matches |
| `Select-String join_ops` on `games/**`, `KB/**` | PASS — only historical Change Log lines in `games/kill_team_2024/README.md` (v0.2/v0.4); no live shipping links |

## Files touched

| Action | Path |
|--------|------|
| Delete (external) | `C:\Personal\Kill Team\kill_team_2024\kill-team-nemesis-operatives-eng.pdf` |
| Rename dir | `games/kill_team_2024/join_ops/` → `joint_ops/` (4 files) |
| Update | `games/kill_team_2024/joint_ops/README.md`, `NPO_Catalog.md`, `NPO_Cheat_Sheet.md`, `Playable_Scenarios_Owned_Terrain.md` |
| Update | `games/kill_team_2024/README.md` |
| Update | `games/kill_team_2024/setup/killzones/starter_set_3e_QR.md` |
| Create | `games/kill_team_2024/nemesis_ops/README.md` |
| Create | `games/kill_team_2024/nemesis_ops/How_To_Create_A_Nemesis_Operative.md` |
| Create | `games/kill_team_2024/nemesis_ops/Custom_Builder.md` |
| Create | `games/kill_team_2024/nemesis_ops/Mission_Packs.md` |
| Create | `games/kill_team_2024/nemesis_ops/Worked_Examples.md` |
| Create | `games/kill_team_2024/nemesis_ops/Modes_And_Cards.md` |
| Create | `games/kill_team_2024/nemesis_ops/WarCom_Free_Statlines.md` |
| Create | `games/kill_team_2024/nemesis_ops/Open_Questions.md` |
| Update | `raw/pointers/kill_team_2024_nemesis_operatives.md` |
| Update | `KB/sources/nemesis_operatives.md` |
| Update | `docs/handoffs/nemesis_ops_research/track_in.md` |
| Update | `docs/handoffs/kill_team_2024_scaffold/track_in.md` |
| Create | `docs/handoffs/nemesis_ops_research/slices/S0_implementer.md` (this file) |

## Exit criteria self-check

| Criterion | Result |
|-----------|--------|
| Mislabeled PDF deleted from disk | PASS |
| Zero live shipping/KB/pointer mentions of eng.pdf filename | PASS |
| `joint_ops/` exists; `join_ops/` gone | PASS |
| Live links updated (no broken `join_ops/` shipping links) | PASS |
| `nemesis_ops/` stubs incl. How_To_Create + WarCom_Free_Statlines | PASS |
| Pointer = dossier only | PASS |
| `S0_implementer.md` filed | PASS |
| Commit | **pending** (per track gate) |

## Blockers / notes

- **`git mv` unavailable** for rename because `join_ops/` was not yet tracked; used filesystem `Move-Item` instead. Coordinator should stage `joint_ops/` and `nemesis_ops/` on first commit batch.
- **OCR tool availability** still open for S1 (not in S0 scope).
- **WarCom free-statline coverage** unknown until S1b (not in S0 scope).
- Historical scaffold handoff slice reports intentionally retain `join_ops/` and eng.pdf mentions.

## Copyright

Teaching paraphrase stubs only. No datasheet transcription. No PDFs copied into git.
