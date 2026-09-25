# Track in — warcode_kickstarter_refresh

- **Project:** Wargame_Concierge
- **Track:** `warcode_kickstarter_refresh`
- **Status:** Resolved — Complete; ready for user-gated squash merge
- **Date opened:** 2026-09-24
- **Branch:** `cursor/warcode-kickstarter-refresh-b7e0`
- **Plan:** Cursor plan `warcode_kickstarter_refresh_650fc0fb` (read-only)
- **Historical track:** `docs/handoffs/warcode_tactical_doctrine/` (frozen)

## Goals

1. Version the freely distributed Rulebook v0.8.9-F and Tactical Doctrine lorebook.
2. Upgrade shipping rules for four playable factions without rebuilding unchanged material.
3. Add a source-aware lore teaching spine.
4. Preserve the Gamefound history and document the digital Kickstarter relaunch separately.
5. Synchronize the KB and complete independent QA.

## Locked decisions

| Decision | Lock |
|---|---|
| Rule hierarchy | v0.8.9-F supersedes v0.8.7-F on the same topic; omission is not a patch |
| Lore quotes | Allowed only under `games/the_warcode/lore/**`, with filename + PDF page + section |
| Other quote paths | Existing `rules/`, `setup/`, and `factions/` exception remains |
| KB and docs | Teaching paraphrase only |
| Gamefound | Preserve as dated postmortem |
| Kickstarter | Separate current, retrieval-dated analysis |
| STL files | Never commit |
| GW naming ban | Unchanged throughout `games/the_warcode/**` |
| Git | Subagents do not perform git operations |

## Rollup

| Stage | Scope | Status |
|---|---|---|
| 0 | Provenance and policy | Resolved — Complete |
| 1 | R1–R4 research and impact gate | Resolved — Approved |
| 2 | Rules and faction refresh | Complete |
| 3 | Lore teaching spine | Complete |
| 4 | Campaign and community refresh | Complete — QA remediation applied |
| 5 | Librarian synchronization | Resolved — Complete |
| 6 | Independent QA and Final Sanity | Resolved — Q1–Q4 PASS; Final Sanity PASS |

## Protected unrelated work

The local Necron 500-point work was stored in git stash
`necron-500-v2-wip-before-warcode-refresh` before this branch was created.
