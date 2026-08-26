# S3 Implementer — wd527_shipping

**Slice:** S3  
**Status:** Complete  
**Date:** 2026-08-25  
**Role:** Implementer  
**Git:** no commit (per slice gate)

## Goal

System Overview polish: Mission 38 / wound / system QR / trust-ladder cross-links; Source Library WD527 teaching pointers if thin; shipping rollup S0–S2 (and S3) Complete. No plan edit. No system QR HTML (S4). No armies / Turn_Structure / Key_Concepts / Board_Setup / Terrain / Chapter_Approved bodies.

## Done

1. **No top-level** `games/warhammer_40k_11e/Overview.md` — polished teaching overview [`games/warhammer_40k_11e/rules/Overview.md`](../../../games/warhammer_40k_11e/rules/Overview.md) instead:
   - Mission 38 + table aids (wound + system QR path) in “What you need to play”
   - Trust ladder paragraph → system README + `track_shipping_in.md`
   - Learning path mentions wound chart then Mission 38
   - Related pages expanded (wound, Mission 38, system QR, system README)
   - Changelog v0.5.2 — teaching body otherwise unchanged
2. **System README** light cross-link polish (S0 provenance / trust ladder sentence **untouched**):
   - How to learn → start at `rules/Overview.md`; Mission 38 bold; system QR noted S4
   - Subtree: Overview row; system QR status **Planned (S4)** (was falsely Active)
   - `REFERENCE_STATUS` / version → v0.5.4
3. **Source Library** WD527 block already had path pointers — added teaching links (Mission 38, wound, trust ladder, system QR path); v0.5.4
4. **`track_shipping_in.md`** slice rollup: S0–S3 **Complete** (was all Open/Pending)

## Files touched

- `games/warhammer_40k_11e/rules/Overview.md`
- `games/warhammer_40k_11e/README.md`
- `reference/Source_Library.md`
- `docs/handoffs/wd527_research/track_shipping_in.md`
- `docs/handoffs/wd527_research/slices/S3_implementer.md` (this file)

## Not touched (forbidden / out of scope)

- Plan file `wd527_shipping_enhance_bd8d901f`
- `games/warhammer_40k_11e/armies/**`
- `rules/Turn_Structure.md`, `rules/Key_Concepts.md`
- `setup/Board_Setup.md`, `Terrain_Basics.md`, `Chapter_Approved_Force_Dispositions.md` teaching bodies
- `setup/print/40k_system_quick_reference.html` (S4 creates)
- Git commit / push
