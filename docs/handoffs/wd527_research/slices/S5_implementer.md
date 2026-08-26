# S5 Implementer — wd527_shipping

**Slice:** S5  
**Status:** Complete  
**Date:** 2026-08-25  
**Role:** Implementer  
**Git:** no commit (per slice gate)  
**Plan file:** not edited

## Goal

Review Cursor rules/skills for research/enhance vs ingest; enhance QA + layer hard stops; create research-enhance, librarian-enhance, and WD Commentary rule; file review + this report.

## Done

| Deliverable | Path |
|-------------|------|
| Review doc | `docs/handoffs/wd527_research/Rules_Skills_Research_Enhance_Review.md` |
| QA skill enhance | `.cursor/skills/qa-slice/SKILL.md` |
| Research-enhance skill | `.cursor/skills/research-enhance/SKILL.md` |
| Librarian-enhance skill | `.cursor/skills/librarian-enhance/SKILL.md` |
| WD Commentary rule | `.cursor/rules/wd-commentary.mdc` |
| Layer hard-stop bullet | `.cursor/rules/layer-and-hard-stops.mdc` |
| This report | `docs/handoffs/wd527_research/slices/S5_implementer.md` |

## Inventory summary (at S5)

**Rules on disk:** `layer-and-hard-stops`, `40k-core-quotes`, `40k-armies-paraphrase`, `gw-unofficial-footer`, `kt24-quotes`, `warcode-quotes`, plus new `wd-commentary`.

**Skills on disk:** `qa-slice`, `github-commit-push-merge`, plus new `research-enhance`, `librarian-enhance`.

No `librarian-ingest` skill folder on disk — ingest remains AGENTS Sec 11 / librarian_agent.

## Key decisions applied

- **Create** research-enhance, librarian-enhance, wd-commentary (gaps).
- **Enhance** qa-slice + layer-and-hard-stops (existing surfaces).
- Research → enhance ≠ ingest; Librarian enhance = surgical KB sync or no-op waiver.
- Commentary ≤6 paraphrase; Tier 1.5 vs Core; 2-pager density both pages filled.

## Not in scope

- L1e KB sync itself (separate Librarian slice)
- Editing games/ teaching or print HTML
- Git commit / push
- Plan file `wd527_shipping_enhance_bd8d901f`
