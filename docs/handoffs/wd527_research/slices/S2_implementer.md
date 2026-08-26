# S2 Implementer — wd527_shipping

**Slice:** S2  
**Status:** Complete  
**Date:** 2026-08-25  
**Role:** Implementer  
**Git:** no commit (per slice gate)

## Goal

Convert free-form WD527 designer notes on setup teaching docs into the locked Commentary format; add Disposition / Tactical and Benefit of Cover Commentary; index Mission 38 + system QR on setup README.

## Done

### Conversions (locked Commentary format)

| File | Action | Commentary title(s) |
|------|--------|---------------------|
| [`Board_Setup.md`](../../../games/warhammer_40k_11e/setup/Board_Setup.md) | **Converted** free-form “WD527 designer note” → locked block; **added** Disposition/Tactical after fourteen-step table; Mission 38 links on steps 2–3 | A New Era of War / Force Disposition; Rules Focus: Terrain Objectives |
| [`Terrain_Basics.md`](../../../games/warhammer_40k_11e/setup/Terrain_Basics.md) | **Converted** free-form footprint italic note → locked block; **added** Benefit of Cover alignment under BoC | Rules Focus: Terrain Objectives; Rules Focus: Benefit of Cover |
| [`Chapter_Approved_Force_Dispositions.md`](../../../games/warhammer_40k_11e/setup/Chapter_Approved_Force_Dispositions.md) | **Added** pairing + Tactical Commentary after matching section; densified step-6 secondary row + Mission 38 tip (2-pager teaching kept) | A New Era of War |
| [`README.md`](../../../games/warhammer_40k_11e/setup/README.md) | WD527 Commentary + Mission 38 pointer; print list includes **system QR** (`40k_system_quick_reference.html`); changelog v0.5.3 | — |

Every Commentary block uses teaching paraphrase (≤6 sentences) + exact Cite line (Trinity Hobby **2026-08-22**, `C:\Personal\40K\WD_527\`, tier **1.5**).

### Regression checks

- **Fourteen-step pre-game sequence:** intact — steps **1–14** still present in `Board_Setup.md` table (Muster → Determine Victor). Commentary sits *after* the table; step text only gained Mission 38 links on 2–3.
- **Terrain area-before-feature teaching:** intact / reinforced — “areas first” section unchanged in structure; Commentary restates footprints-then-ruins order.
- **No Mission 38 card dump:** only links to [`WD527_Monthly_Mission.md`](../../../games/warhammer_40k_11e/setup/WD527_Monthly_Mission.md); no Primary VP tables copied into Board/Disposition docs.
- **Plan file:** not edited.

## Files touched

- `games/warhammer_40k_11e/setup/Board_Setup.md` (v0.5.3)
- `games/warhammer_40k_11e/setup/Terrain_Basics.md` (v0.5.2)
- `games/warhammer_40k_11e/setup/Chapter_Approved_Force_Dispositions.md` (v1.1)
- `games/warhammer_40k_11e/setup/README.md` (v0.5.3)
- `docs/handoffs/wd527_research/slices/S2_implementer.md` (this file)

## Sources read

- `raw/white_dwarf_527/designer_commentary_notes.md`
- `games/warhammer_40k_11e/setup/WD527_Monthly_Mission.md`
- `docs/handoffs/wd527_research/track_shipping_in.md` (locked format)

## Not in scope

- Print HTML Commentary callouts (later shipping slices)
- `rules/` teaching files (S1)
- Army 2-pager revamps (S4+)
- Git commit / plan file edits
