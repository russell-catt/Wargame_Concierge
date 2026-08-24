# QA — gw_community_content S1 + S2

**Slice:** S1 (print HTML) + S2 (rules / AGENTS / templates)  
**Date:** 2026-08-23  
**Result:** PASS

| # | Check | Result | Notes |
|---|-------|--------|-------|
| 1 | All `games/**/*.html` have `.gw-ip-banner` on page 1 (print/cheat sheet) | PASS | 19 print/cheat-sheet files |
| 2 | All print pages have `.gw-ip-footer` with endorsement sentence | PASS | 42 HTML files updated |
| 3 | Datacard `.ft` includes UNOFFICIAL micro footer | PASS | 23 card HTML files |
| 4 | No GW logos added | PASS | Text-only notices |
| 5 | Templates indexed | PASS | `Footer_Template_Gw_Print.md`, `Gw_Print_Banner.html` |
| 6 | `gw-unofficial-footer.mdc` created | PASS | Globs games html + md |
| 7 | AGENTS.md Sec 10 paragraph | PASS | v0.5.3 changelog row |
| 8 | QA skill GW checklist | PASS | `.cursor/skills/qa-slice/SKILL.md` |
| 9 | Quote-PDF policy documented in track_in | PASS | In-repo only unless gated |

**Status:** Resolved - Complete
