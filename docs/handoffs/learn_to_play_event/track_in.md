# Track in — learn_to_play_event

- **Project:** Wargame_Concierge
- **Track:** `learn_to_play_event`
- **Status:** Closed - Complete (2026-08-21; git commit pending user gate / IMP-09)
- **Git root:** `C:\Personal\Personal_Projects\Wargame_Concierge`
- **Plan:** Cursor plan `kt24_volkus_l2p_8a130bf1` (do not edit plan file)
- **Handoffs root:** `docs/handoffs/learn_to_play_event/`
- **Playbook:** `docs/operations/multiagent_coordinator_strategy.md`
- **Entrance:** User authorized full track execution 2026-08-21 (Coordinator + sequential hats; **no git commit/push** unless user gates)

## Goals

1. **Kommandos** full KT24 package from owned Teams PDF (quotes, cards, QR, roster, Volkus playbook).
2. **Plague Marines** kid-level refresh: legal 6-op roster, 12yo QR, kid Volkus playbook.
3. **40K** first-game Letter print pack for 245-pt Cryptek Conclave.
4. **KT** Letter 2-page print pack (shared + PM + Kommandos).
5. Combined print bag; all PDFs in `C:\Personal\print_aids\learn_to_play_event\`.
6. KB paraphrase pointers only (no datacard dump).

## Matchup buckets (locked)

- **Elite:** plague_marines, angels_of_death, deathwatch, murderwing
- **Horde:** death_korps, vespid_stingwings, celestian_insidiants
- **Balanced:** canoptek_circle, hierotek_circle, kommandos (+ other non-elite/non-horde)

## Constraints

- Never write `raw/`. Never create `wiki/`. UTF-8 no BOM.
- Never commit GW binaries or generated `*.pdf` (`.gitignore`).
- KT24 quotes only under `games/kill_team_2024/` with filename + page. `KB/` paraphrase.
- 40K armies: Codex wall (paraphrase). Core IDs OK as pointers.
- Subagents never git. Coordinator commit only if user gates.
- Do not edit frozen slices from other tracks.

## Model matrix

| Role | Model | Notes |
|------|--------|-------|
| Coordinator | `inherit` | Parent session |
| Librarian / Implementer / QA | `inherit` (sequential hats) | Prefer different QA family when available; same-session independent re-read recorded honestly |

## Slice rollup

| Slice | Status | Notes |
|-------|--------|-------|
| Preflight | Resolved - Complete | Folder + track_in + handoffs README row |
| L0 | Resolved - Complete | KT PDF receipt; PM=6; Kommandos=Nob+9 |
| S1 | Resolved - Complete | Kommandos full package |
| S1 QA | Resolved - Complete | PASS |
| S2 | Resolved - Complete | Kommandos Volkus playbook |
| S2 QA | Resolved - Complete | PASS |
| S3 | Resolved - Complete | PM kid refresh |
| S3 QA | Resolved - Complete | PASS |
| S5 | Resolved - Complete | 40K Letter PDFs |
| S5 QA | Resolved - Complete | PASS |
| S6 | Resolved - Complete | KT Letter PDFs (same folder) |
| S6 QA | Resolved - Complete | PASS |
| S4 | Resolved - Complete | Combined print bag |
| S4 QA | Resolved - Complete | PASS |
| L1 | Resolved - Complete | KB Kommandos source pointer |
| FS | Closed - Complete | `track_learn_to_play_event_final_report.md` |

## Git policy

**IMP-09 deferred commit** unless user gates. Subagents never commit or push.
