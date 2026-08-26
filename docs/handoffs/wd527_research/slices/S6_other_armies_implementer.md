# S6 Implementer — wd527_shipping (other armies / non-Necrons)

**Slice:** S6 (non-Necrons portion)  
**Status:** Complete  
**Date:** 2026-08-25  
**Role:** Implementer  
**Git:** no commit (per slice gate)  
**Plan file:** not edited  
**Out of scope:** `armies/necrons/**` (other agent); `units/**` deep rewrite; new print HTML

## Goal

Align Space Marines top-level teaching/play docs + thin Adepta Sororitas / Death Guard stubs with the WD527 shipping spine (6″/8″/9″ triad, terrain-footprint OC, Force Disposition, Wound / Mission 38 / Chapter Approved / system QR links). Densify SM 2-pager laminate. Codex wall paraphrase only.

## Done

### Space Marines — laminate (exactly 2 pages)

| File | Action |
|------|--------|
| [`Quick_Reference_Play_Guide.md`](../../../games/warhammer_40k_11e/armies/space_marines/Quick_Reference_Play_Guide.md) | **v0.7.0** — both pages filled; imported S vs T quick bands, **6″/8″/9″** distance table, Mission 38 + system QR + Disposition on page 1 banner; charge “2D6 first”; Ingress note on move types; pre-game Mission 38 checkbox. **No print HTML** — README claims md laminate only; no `print/` folder claimed. |

### Space Marines — teaching + inventory + starters

| File | Action |
|------|--------|
| [`README.md`](../../../games/warhammer_40k_11e/armies/space_marines/README.md) | System spine table; Force Disposition **Commentary** (locked format); shipping track link |
| [`Oath_of_Moment.md`](../../../games/warhammer_40k_11e/armies/space_marines/Oath_of_Moment.md) | Wound-band tip; spine Related links |
| [`Gladius_Task_Force.md`](../../../games/warhammer_40k_11e/armies/space_marines/Gladius_Task_Force.md) | Leaders/Support **Commentary**; spine links |
| [`First_Company_Task_Force.md`](../../../games/warhammer_40k_11e/armies/space_marines/First_Company_Task_Force.md) | Charge **Commentary** + distance triad note; spine links |
| [`Anvil_Siege_Force.md`](../../../games/warhammer_40k_11e/armies/space_marines/Anvil_Siege_Force.md) | Terrain-footprint OC tip; spine links |
| [`Owned_Models_Inventory.md`](../../../games/warhammer_40k_11e/armies/space_marines/Owned_Models_Inventory.md) | System spine Related block |
| All `Starter_*_Matched.md` / `Starter_*_Casual.md` | System spine Related block + changelog |
| All `Starter_{250,500,750,1000}.md` shims | One-line system spine pointers |

### Thin armies — pointers only (no invented Codex rules)

| File | Action |
|------|--------|
| [`adepta_sororitas/README.md`](../../../games/warhammer_40k_11e/armies/adepta_sororitas/README.md) | System pointer table (wound / Mission 38 / Disposition / system QR / track) |
| [`adepta_sororitas/Owned_Models_Inventory.md`](../../../games/warhammer_40k_11e/armies/adepta_sororitas/Owned_Models_Inventory.md) | Same spine Related |
| [`death_guard/README.md`](../../../games/warhammer_40k_11e/armies/death_guard/README.md) | Same system pointer table; still not a faction package |

### Commentary blocks added (locked format)

| Doc | Title |
|-----|-------|
| SM README | A New Era of War (Force Disposition pairing) |
| Gladius | Leaders and Support |
| 1st Company | Charge (2D6 first) |

Thin SoS/DG: **links only** (no Commentary).

## Regression / constraints

- **Codex wall:** paraphrase only on all army pages; no Faction Pack dumps.
- **Print HTML:** not created for SM (README does not claim laminate HTML; no missing HTML under a claimed `print/` path).
- **Necrons:** untouched.
- **2-pager:** `DOCUMENT_TYPE: Play Aid / Laminate (exactly 2 pages)` retained; page break marker intact; page 2 densified with wound bands + distances without inventing page 3 content in the teaching body (GW notice remains markdown footer, same pattern as Necrons QR).

## Inventory of files touched (by army)

### Space Marines (`games/warhammer_40k_11e/armies/space_marines/`)

1. `README.md`
2. `Quick_Reference_Play_Guide.md`
3. `Oath_of_Moment.md`
4. `Gladius_Task_Force.md`
5. `First_Company_Task_Force.md`
6. `Anvil_Siege_Force.md`
7. `Owned_Models_Inventory.md`
8. `Starter_250.md`
9. `Starter_250_Matched.md`
10. `Starter_250_Casual.md`
11. `Starter_500.md`
12. `Starter_500_Matched.md`
13. `Starter_500_Casual.md`
14. `Starter_750.md`
15. `Starter_750_Matched.md`
16. `Starter_750_Casual.md`
17. `Starter_1000.md`
18. `Starter_1000_Matched.md`
19. `Starter_1000_Casual.md`

### Adepta Sororitas

20. `games/warhammer_40k_11e/armies/adepta_sororitas/README.md`
21. `games/warhammer_40k_11e/armies/adepta_sororitas/Owned_Models_Inventory.md`

### Death Guard

22. `games/warhammer_40k_11e/armies/death_guard/README.md`

### Handoff

23. `docs/handoffs/wd527_research/slices/S6_other_armies_implementer.md` (this file)

## Not in scope / deferred

- Necrons army revamp (parallel agent)
- SM `units/**` research rewrite
- Creating `space_marines/print/*.html`
- Git commit / plan edits
- Fabricating Sisters or Death Guard detachment guides

## Sources read

- `docs/handoffs/wd527_research/track_shipping_in.md` (locked Commentary + 2-pager density)
- `raw/white_dwarf_527/designer_commentary_notes.md`
- `games/warhammer_40k_11e/rules/Key_Concepts.md` · `Turn_Structure.md` · `Wound_Roll_Reference.md`
- `games/warhammer_40k_11e/README.md` · `setup/README.md`
