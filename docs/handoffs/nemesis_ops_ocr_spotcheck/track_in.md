# Track in — nemesis_ops_ocr_spotcheck

- **Project:** Wargame_Concierge
- **Track:** `nemesis_ops_ocr_spotcheck`
- **Status:** In Progress
- **Git root:** `C:\Personal\Personal_Projects\Wargame_Concierge`
- **Plan:** Cursor plan `ocr_spot-check_track_45ee8380` (do not edit plan file)
- **Handoffs root:** `docs/handoffs/nemesis_ops_ocr_spotcheck/`
- **Playbook:** `docs/operations/multiagent_coordinator_strategy.md`
- **Parent:** Closed track `nemesis_ops_research` (gap #1 — OCR accuracy)

## Goals

1. Vision-verify Nemesis Operatives Dossier OCR against PDF page images for a locked sample (≥20 pages)
2. Score PASS / PARTIAL / FAIL / TABLE in `OCR_Spotcheck_Matrix.md`
3. Patch shipping claims only where OCR misled process/title/naming; bump confidence only on vision PASS
4. Never paste dossier datasheet numbers into git
5. Update KB + pointer; optional local `.ocr.spotcheck.md` outside git

## Locked sources

| Source | Path |
|--------|------|
| PDF | `C:\Personal\Kill Team\kill_team_2024\1063073009-Kill-Team-Nemesis-Operatives-Dossier.pdf` |
| OCR | `C:\Personal\Kill Team\kill_team_2024\1063073009-Kill-Team-Nemesis-Operatives-Dossier.ocr.txt` |
| Shipping | `games/kill_team_2024/nemesis_ops/` |
| Seed noise | `docs/handoffs/nemesis_ops_research/slices/S1_implementer.md` |

## Spot-check bands (locked)

| Band | Pages | Priority |
|------|-------|----------|
| A — Front / TOC | 1–11 | Medium |
| B — Custom Builder | 12–31 | High |
| C — Worked examples | within B / flagged | High |
| D — Mission packs | 32–79 (esp. 61–62, 73–74) | High |
| E — Dense tables | S1 noise: 3,13,22–24,33,59–60,64,71–72 | High (flag only) |

## Model matrix (locked)

| Role | Model |
|------|-------|
| Coordinator | `inherit` |
| Librarian | `claude-sonnet-5-thinking-high` (never fable) |
| Implementer — matrix / reports | `composer-2.5-fast` |
| Implementer — vision / patches | `claude-sonnet-5-thinking-high` |
| QA — default | `gpt-5.6-sol-medium` |
| QA — light | `gemini-3.7-flash-high` |
| Final Sanity | `gpt-5.6-terra-medium` |

## Constraints

- No GW binaries / OCR sidecars in git
- No datasheet transcription from dossier into repo
- Commits only when user asks
- Cover may remain FAIL; tables stay TABLE / unverified for numbers

## Rollup

| Slice | Focus | Status |
|-------|--------|--------|
| Preflight | Confirm PDF/OCR; lock matrix | Resolved - Complete |
| S0 | Build spot-check matrix | Resolved - Complete |
| S1 | Vision ≥20 pages High bands first | Resolved - Complete |
| S2 | Patch shipping + Open_Questions | Resolved - Complete |
| L1 | KB source/log | Resolved - Complete |
| S3 | Pointer + local spotcheck annotation | Resolved - Complete |
| Final Sanity | Cross-check + final report | Closed - Complete |

## Pending commits

All track artifacts + shipping confidence bumps — user gate.
