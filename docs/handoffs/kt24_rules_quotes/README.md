# KT24 rules quotes — track handoffs

**Track:** `kt24_rules_quotes`  
**Plan:** Cursor plan `warcom_kt24_datacards_631ae509` (do not edit plan file)  
**Playbook:** [`docs/operations/multiagent_coordinator_strategy.md`](../../operations/multiagent_coordinator_strategy.md)

## Purpose

Allow **verbatim quoting** of owned local Kill Team 2024 PDFs under `games/kill_team_2024/` only (personal use; **never for sale**). Ship a one-page target-eligibility cheat sheet and transcribe Canoptek Circle + Plague Marines datacards from local Teams PDFs.

## Golden sources (owner lock 2026-08-17)

- Core: [`raw/pointers/kill_team_2024_core.md`](../../../raw/pointers/kill_team_2024_core.md)
- Teams: [`raw/pointers/kill_team_2024_teams.md`](../../../raw/pointers/kill_team_2024_teams.md)
- Read PDFs **in place** under `C:\Personal\Kill Team\kill_team_2024\` — do **not** fetch WarCom this pass.

## Community inspiration (layout only — never commit binaries)

| Credit | Asset |
|--------|-------|
| [u/rdditonator](https://www.reddit.com/user/rdditonator/) | `Can_I_Shoot.jpeg` |
| [u/Armagonix](https://www.reddit.com/user/Armagonix/) | Vers 1.21, `kt24_reference_second.pdf`, `kt24_solo_reference.pdf`, datacard template |
| [u/burgerdrome](https://www.reddit.com/user/burgerdrome/) | LOS flowchart (2025-12-06) |

Local PDF wins on any rules disagreement.

## Slice order

S0 → S1 → S1 QA → L1 → S2 → S2 QA → S3 → S3 QA → S4 → S4 QA → S5 → S5 QA → L2 → Final Sanity

## Constraints

- Personal use only; project must never be sold
- **Librarian never writes `raw/`** — Implementer/Coordinator may update `raw/pointers/` per project practice
- Never commit PDF/JPG binaries
- 40K remains teaching paraphrase only
- Do not touch `docs/handoffs/tomb_world_ownership/**`
- Subagents never commit or push unless user asks

## Artifacts

| Slice | Brief | Report |
|-------|-------|--------|
| S1 | [`slices/S1_brief.md`](slices/S1_brief.md) | [`slices/S1_implementer.md`](slices/S1_implementer.md) |
| L1 | [`slices/L1_brief.md`](slices/L1_brief.md) | [`slices/L1_librarian.md`](slices/L1_librarian.md) |
| S2 | [`slices/S2_brief.md`](slices/S2_brief.md) | [`slices/S2_implementer.md`](slices/S2_implementer.md) |
| S3 | [`slices/S3_brief.md`](slices/S3_brief.md) | [`slices/S3_implementer.md`](slices/S3_implementer.md) |
| S4 | [`slices/S4_brief.md`](slices/S4_brief.md) | [`slices/S4_implementer.md`](slices/S4_implementer.md) |
| S5 | [`slices/S5_brief.md`](slices/S5_brief.md) | [`slices/S5_implementer.md`](slices/S5_implementer.md) |
| L2 | [`slices/L2_brief.md`](slices/L2_brief.md) | [`slices/L2_librarian.md`](slices/L2_librarian.md) |
| FS | [`slices/FS_brief.md`](slices/FS_brief.md) | [`slices/FS_final_report.md`](slices/FS_final_report.md) |
