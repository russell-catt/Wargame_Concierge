# L2 — Lint note (warcode_tactical_doctrine)

- **Status:** Resolved - Complete
- **Date:** 2026-08-25
- **Model:** Coordinator — card/map enhancement pass

## Findings

| Check | Result |
|-------|--------|
| `Kill Team` / `KT24` / `kill_team` under `games/the_warcode/` | **PASS** |
| `Warhammer` / `40,000` / `40K` / `40k` under `games/the_warcode/` | **PASS** (v0.5.5) |
| **S1b** contract/protocol transcription | **PASS** — xlsx sidecars + Rulebook_Quotes pp.24–25 closed |
| **S8** full keyword pass | **PASS** — Keyword_Glossary v0.2 + Comparative_Glossary extended |
| D6 VP placement table | **PASS** — Board_Setup.md |
| GATE lock | **Final** (2026-08-25) |
| VIP review gitignore | **PASS** — `.gitignore` + `git rm --cached` on feature-Warcode |
| Duplicate PDF at `raw/` root | **Removed** — canonical `raw/the_warcode/` only |

## Open / deferred

- TTS **parked indefinitely** (owner schedule)
- L1 KB unit pages — priority backlog separate track
- Merge `feature-Warcode` → `main` — **hold until user asks**
- First Game Walkthrough — owner has not table-tested yet

## Fixes applied (2026-08-25)

- Card/map enhancement pass: Contract + Protocol reference pages, map PNG ingest, §12 factual updates (review local only)
- Removed duplicate PDF outside `raw/the_warcode/`
