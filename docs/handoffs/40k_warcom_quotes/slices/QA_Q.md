# QA-Q — Core quote spot-check (`40k_warcom_quotes`)

**Date:** 2026-08-18  
**PDF:** `C:\Personal\40K\rules\eng_01-06_warhammer40k_new40k_core_rules.pdf` (pypdf text layer; 88 pages)  
**July:** `C:\Personal\40K\rules\eng_22-07_warhammer_40,000_universal_rules_updates.pdf` (1 page, v1.0)

## Checks

| Item | Expected | Result |
|------|----------|--------|
| **01.01** Armies p.8 | Player commands an army of units of models; controlling player | **PASS** — quote matches PDF p.8 |
| **06.01** Visibility p.24 | 1 mm wide straight line from any part to any part; ignore models in both units; terrain **13.07** | **PASS** — quote matches PDF p.24 |
| **July delta** | Unnamed 0CP → −1CP; named-only multi-use; 12"→18" targeting; add-unit once/battle | **PASS** — sheet has no Core IDs; flagged on **15.x** in the index |
| Random index **15.02** COMMAND RE-ROLL p.56 | **stub** (not a teaching-spine quote body) | **PASS** — stub; title/page match PDF heading on p.56 |
| Random index **23.01** DEPLOYMENT p.74 | **stub** (Aircraft) | **PASS** — stub; Aircraft chapter |
| Random index **24.05** [BLAST] p.79 | **stub** (ability appendix, not dumped) | **PASS** — stub; page is CORE ABILITIES p.79 |

## Notes

- PDF extraction splits some words (`Enemy` as `Enem y` before cleanup). Quotes were cleaned only for those artifacts; rule meaning was not rewritten.
- Some quote blocks still trail the next heading token; readers should check the owned page if a block looks truncated.
- **No PDF-read failures.** Core, July universal updates, and Event Companion all had extractable text.

**Verdict:** PASS
