# L2 — Lint note (warcode_tactical_doctrine)

- **Status:** Resolved - Complete
- **Date:** 2026-08-23
- **Model:** Coordinator light + gemini-style defect pass

## Findings

| Check | Result |
|-------|--------|
| `Kill Team` / `KT24` / `kill_team` under `games/the_warcode/` | **PASS** (zero matches after Comparative_Glossary fix) |
| §0 / §15 "unofficial and unauthorized" in Agentic review | **PASS** (present) |
| Beta PDF under `raw/the_warcode/` | Present; gitignore negation restored |
| Rulebook_Quotes + OCR Protocol Cards | Present |
| GATE lock file | Present (provisional user execution auth) |
| Comparative_Glossary.md | Present |
| Manifests R0–15 stubs | Present |

## Open / deferred

- TTS workshop URL still TBD (user Steam)
- Contract card pages 24–25 may need further OCR
- Duplicate PDF at `raw/The Warcode Rulebook...` — prefer only `raw/the_warcode/` copy in commits
- `_ocr_preview/*.png` gitignored — do not commit

## Fixes applied

- Removed forbidden "kill team" phrase from Comparative_Glossary bridge line
- Re-applied `.gitignore` Warcode PDF negation (had been missing from working tree)
