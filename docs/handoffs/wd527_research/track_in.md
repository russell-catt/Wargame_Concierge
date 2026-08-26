# Track in — wd527_research

- **Project:** Wargame_Concierge
- **Track:** `wd527_research`
- **Status:** Closed - Complete (2026-08-24; commit pending user gate)
- **Branch:** `feature-WD272_research`
- **Handoffs root:** `docs/handoffs/wd527_research/`
- **Playbook:** [`docs/operations/multiagent_coordinator_strategy.md`](../../operations/multiagent_coordinator_strategy.md)
- **Plan:** Cursor plan `wd527_research_track_e7babb1e` (do not edit plan file)

## Goals

1. Ingest owned **White Dwarf 527** 40K content (ref card, Mission 38, designer rules commentary, Blood Angels vs Orks battle report).
2. Ship **original wound-roll 2-pager** derived from Core **05.02** (not traced from WD art).
3. Rebuild **Mission 38: Converging Ambition** with owned-materials notes.
4. KB + shipping enhancements per manifest.

## Trust ladder (locked)

| Tier | Source | SoT for |
|------|--------|---------|
| **1** | Core PDF, Event Companion v1.1, Chapter Approved / MFM | Rules mechanics |
| **1.5** | Owned WD527 (`C:\Personal\40K\WD_527\`) | Commentary, mission card, battle report, ref layout |
| **2** | WarCom article | Pointers when issue unreadable |

Tier 1 wins on mechanical conflict; log conflicts in KB source page.

## Scan inventory (Preflight — locked 2026-08-24)

| File | Pages | Content |
|------|-------|---------|
| `40K_ref-card.pdf` | 2 | Quick Reference (phases + attack sequence / wound chart) |
| `40K_missions.pdf` | 2 | p1: Mission 38 Converging Ambition (40K); p2: AoS Battleplan 38 (out of scope) |
| `WD_527_1.pdf` | 24 | Lore, miniatures designers |
| `WD_527_2.pdf` | 24 | Rules commentary, battle report setup/deploy |
| `WD_527_3.pdf` | 14 | Battle report rounds 2–5 |

## Model matrix (Research-balanced)

| Role | Model |
|------|--------|
| Coordinator | `inherit` |
| Preflight / S1 / S2 | `composer-2.5-fast` |
| S3 / S5 / Librarian | `claude-sonnet-5-thinking-high` |
| QA | `gpt-5.6-sol-medium` |
| Final Sanity | `gemini-3.7-flash-high` |

## Constraints

- No GW images/binaries in git. PDFs stay at `C:\Personal\40K\WD_527\`.
- Librarian never writes `raw/`; Coordinator authors `raw/white_dwarf_527/`.
- Print HTML: UNOFFICIAL banner + footer per `templates/Gw_Print_Banner.html`.
- Subagents do not commit unless user gates.

## Slice rollup

| Slice | Status |
|-------|--------|
| Preflight | Resolved - Complete |
| L0 | Resolved - Complete |
| S1 | Resolved - Complete |
| S2 | Resolved - Complete |
| S3 | Resolved - Complete |
| S4 | Resolved - Complete |
| L1 | Resolved - Complete |
| S5 | Resolved - Complete |
| QA + Final Sanity | Resolved - Complete |
