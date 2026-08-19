# FS — Track report (`40k_warcom_quotes`)

**Date:** 2026-08-18  
**Plan:** `40k_warcom_rules_ingest_5f485290`  
**Git:** one commit + one push at close (user-authorized)

## Cross-slice audit

| Check | Result |
|-------|--------|
| No GW PDFs/binaries in git | PASS |
| Personal use / never for sale; 40K copyright on quote surface | PASS |
| Codex wall (no Faction Pack / MFM / Armageddon dump) | PASS |
| Necron lists: Personal `C:\Personal\40K\Necron_Lists.md` wins; games copy is working copy; Personal not overwritten | PASS |
| KB/docs paraphrase; quotes only under `games/warhammer_40k_11e/rules/` (+ setup cites) | PASS |
| Core PDF readable (text layer, 88 pages) | PASS — no read failures |
| QA-Q / QA-T | PASS |
| KT follow-ups untouched | PASS |

## Counts

| Item | Count |
|------|-------|
| Numbered Core IDs indexed | **156** (`01.01`–`24.38`) |
| Verbatim quote blocks | **112** |
| Stubs (ID + title + page) | **44** |

## July deltas

`eng_22-07_warhammer_40,000_universal_rules_updates.pdf` v1.0 (1 page): unnamed 0CP → −1CP; named-only multi-use; 12"→18" targeting; add-unit once/battle. Flagged on **15.x**. Event Companion v1.1 inventoried (44"×60", non-Core CP cap); not dumped.

## Contradictions flagged (no rewrite)

2026-08-16 teaching still matches Core: cover worsens BS by 1 (**13.08**); `[HEAVY]` adds 1 to the hit roll (**24.16**); OC re-check (**14.02**).

## Files created

- `docs/handoffs/40k_warcom_quotes/track_in.md`
- `docs/handoffs/40k_warcom_quotes/README.md`
- `docs/handoffs/40k_warcom_quotes/slices/QA_Q.md`
- `docs/handoffs/40k_warcom_quotes/slices/QA_T.md`
- `docs/handoffs/40k_warcom_quotes/track_report.md` (this file)
- `games/warhammer_40k_11e/rules/Core_Rules_Quotes.md`
- `KB/sources/warcom_free_core_rules_11e.md`

## PDF-read failures

None.
