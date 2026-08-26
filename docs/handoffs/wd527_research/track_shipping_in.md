# Track in — wd527_shipping

- **Project:** Wargame_Concierge
- **Track:** `wd527_shipping` (follow-on to `wd527_research`)
- **Status:** Closed — Complete (2026-08-25; commit pending user gate)
- **Branch:** `feature-WD272_research`
- **Handoffs root:** `docs/handoffs/wd527_research/`
- **Parent research:** [`track_in.md`](track_in.md) (Closed — Complete)
- **Plan:** Cursor plan `wd527_shipping_enhance_bd8d901f` (do not edit plan file)

## Goals

1. Lock Commentary format and README Trinity Hobby provenance for WD527.
2. Commentary-cited enhancements on `rules/` + `setup/` teaching docs.
3. Ship original system Letter 2-pager quick reference + enhancement report.
4. Revamp all army guides under `games/warhammer_40k_11e/armies/**` (2-pager density).
5. Review/enhance Cursor rules/skills for research/enhance vs ingest; Librarian enhance (L1e).

## Trust ladder (locked)

| Tier | Source | SoT for |
|------|--------|---------|
| **1** | Core PDF, Event Companion v1.1, Chapter Approved / MFM | Rules mechanics |
| **1.5** | Owned WD527 (`C:\Personal\40K\WD_527\`) | Commentary, mission card, battle report, ref layout |
| **2** | WarCom article | Pointers when issue unreadable |

Tier 1 wins on mechanical conflict.

## Locked Commentary format

**Body is teaching paraphrase, not a full block-quote of White Dwarf.** Up to **6 sentences** when needed. Cite line always present. Do not paste long magazine excerpts.

```markdown
**Commentary (White Dwarf 527 — <section or Rules Focus title>):**

<1–6 sentences teaching paraphrase in our own words. Not a full WD block-quote.
Optional: one short italic phrase only if a named Rules Focus label needs anchoring.>

**Cite:** WD527, <article/section name>; owned digital backup purchased Trinity Hobby **2026-08-22**; local scans `C:\Personal\40K\WD_527\`. Tier **1.5** — Core / Event Companion win on mechanics.
```

**Rules:**

- Convert free-form WD notes in Board_Setup / Terrain_Basics into this format.
- Paraphrase only (max 6 sentences). No multi-paragraph magazine quotes.
- Never dump Mission 38 card text, datasheets, or ref-card art.
- Print HTML: compact commentary callout + UNOFFICIAL banner/footer.

## Required README provenance sentence

Exact string for [`games/warhammer_40k_11e/README.md`](../../../games/warhammer_40k_11e/README.md):

> Importing commentary from user's digital backup of White Dwarf 527, purchased from Trinity Hobby on Aug 22, 2026.

## 2-pager density (locked)

Any doc claiming exactly 2 pages must use both pages. Prefer army tips; fill thin sheets from system spine (S vs T wound utility required on table aids; phase strip / distances / OC / Force Disposition / Mission 38 as needed). Never spill to page 3.

## Slice rollup

| Slice | Status |
|-------|--------|
| S0 | Resolved - Complete |
| S0 QA | Resolved - PASS |
| S1 | Resolved - Complete |
| S1 QA | Resolved - PASS |
| S2 | Resolved - Complete |
| S2 QA | Resolved - PASS |
| S3 | Resolved - Complete |
| S3 QA | Resolved - PASS |
| S4 | Resolved - Complete |
| S4 QA | Resolved - PASS |
| S6 | Resolved - Complete |
| S6 QA | Resolved - PASS |
| S5 | Resolved - Complete |
| S5 QA | Resolved - PASS |
| L1e | Resolved - Complete |
| L1e QA | Resolved - PASS |
| Final Sanity | Resolved - PASS |

Final report: [`track_wd527_shipping_final_report.md`](track_wd527_shipping_final_report.md)

## Constraints

- No GW images/binaries in git. PDFs stay outside repo.
- Librarian never writes `raw/`.
- Print HTML: UNOFFICIAL banner + footer.
- Subagents do not commit unless user gates.
