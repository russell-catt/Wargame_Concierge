# S1 Implementer — wd527_shipping

**Slice:** S1  
**Status:** Complete  
**Date:** 2026-08-25

## Done

Locked **Commentary (White Dwarf 527 — …)** blocks added to rules teaching docs from WD527 designer notes. No plan-file edit. No git commit.

## Files changed

| File | Change |
|------|--------|
| `games/warhammer_40k_11e/rules/Turn_Structure.md` | Three Commentary blocks + Change Log v0.5.2 |
| `games/warhammer_40k_11e/rules/Key_Concepts.md` | Three Commentary blocks + Change Log v0.5.3 |
| `games/warhammer_40k_11e/rules/README.md` | WD527 Commentary + shipping-track pointer + Change Log v0.5.2 |
| `docs/handoffs/wd527_research/slices/S1_implementer.md` | This report |

## Commentary titles added

### Turn_Structure.md

1. **Commentary (White Dwarf 527 — Movement changes):** — coherency 2"/9" (**03.03**); Ingress 6" edge (**20.04**); Deep Strike / ingress enemy gap >8"
2. **Commentary (White Dwarf 527 — Charge / Jack Rules Focus):** — roll 2D6 first before picking eligible targets
3. **Commentary (White Dwarf 527 — Pile-in / Consolidate):** — active player all units first, then opponent

### Key_Concepts.md

1. **Commentary (White Dwarf 527 — Attack sequence / allocation groups):** — CHARACTER alone; group by matching W/Sv/InSv
2. **Commentary (White Dwarf 527 — Leaders and Support):** — one Leader + one Support per bodyguard
3. **Commentary (White Dwarf 527 — Distance triad clarity):** — 2"/9" coherency vs 6" Ingress edge vs >8" enemy gap

### README.md

- Brief pointer to locked WD527 Commentary format and [`track_shipping_in.md`](../track_shipping_in.md)

## Regression check

- [x] Core rule IDs preserved (e.g. **03.03**, **08.02**, **09.04–09.07**, **10.04–10.07**, **11.02**, **12.02–12.08**, **05.01–05.04**, **14.01–14.02**, **19.01**)
- [x] Phase checklists intact (Start of Turn through End of Turn)
- [x] Correct numeric facts unchanged (2"/9" coherency, 6" Ingress edge, >8" gap, charge 2D6-first)
- [x] Max 6 sentences per Commentary body; no WD block-quotes
- [x] Cite line present on every Commentary block (Trinity Hobby **2026-08-22**; Tier **1.5**)

## Not touched (out of S1 scope)

- Plan file `wd527_shipping_enhance_bd8d901f`
- `setup/` teaching docs
- `armies/`
- Git commit / push
