# S1 — Implementer (vision vs OCR)

- **Status:** Resolved - Complete
- **Model:** `claude-sonnet-5-thinking-high` (Coordinator wearing content hat)
- **Date:** 2026-08-17

## Method

1. Concord OCR text for High-band pages.
2. Render PDF pages via PyMuPDF to `C:\Personal\Kill Team\kill_team_2024\_spotcheck_renders\` (**outside git**).
3. Vision-read renders for pages: 4, 15, 16, 22, 25, 61, 62, 71, 74 (and OCR concordance for remainder of matrix).

## Indexing note

**OCR `===== PAGE N =====` = PDF page order (1-based).** Printed footer on body pages is typically **N−1** (e.g. OCR PAGE 62 shows printed **61** Ambull game sequence). Matrix uses OCR page numbers; vision scores still apply.

## High-band results (summary)

| Focus | OCR pages | Vision | Notes |
|-------|-----------|--------|-------|
| Builder steps / allegiance / size / behaviours | 15–17, 20 | PASS | Behaviours: Brawler, Marksman, Battler, Guardian confirmed on printed Behaviour page |
| Armoured Sentinel / Spectre example | 25 | PASS | Example walkthrough; datacard region = TABLE (no numbers into git) |
| Ambull missions | 61–62 | PASS | **The Hidden Enemy (Joint Ops)** / **Decaying Generatorium (Adversary Ops)** confirmed on Ambull game sequence |
| Archivist missions | 73–74 | PASS | **Betrayal (Joint Ops)** / **Negotiation (Adversary Ops)** confirmed |
| Art / datacard splash | 22, 59, 71 | FAIL / TABLE | Full-bleed art or labelled model plates; OCR unreliable for prose; never import stats |
| TOC | 4 | PARTIAL | Contents bands match: Builder 12–31, Mission packs 32–79; Ambull / Archivist named |

## Exit

≥26 pages scored; High bands complete; **zero** datasheet numbers written to git this slice.
