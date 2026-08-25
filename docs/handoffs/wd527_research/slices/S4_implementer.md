# S4 Implementer — wd527_shipping

**Slice:** S4  
**Status:** Complete  
**Date:** 2026-08-25  
**Role:** Implementer  
**Git:** no commit (per slice gate)

## Goal

Ship original system Letter **2-pager** quick reference (WD527 topic map as layout inspiration; Core-first mechanics) + enhancement report. Do not replace the dedicated wound laminate.

## Done

1. **Outline (optional md):** [`games/warhammer_40k_11e/rules/Quick_Reference_Card.md`](../../../games/warhammer_40k_11e/rules/Quick_Reference_Card.md) — Side A/B topic map with teaching paraphrase + Core IDs.
2. **Print HTML (exactly 2 pages, dense):** [`games/warhammer_40k_11e/setup/print/40k_system_quick_reference.html`](../../../games/warhammer_40k_11e/setup/print/40k_system_quick_reference.html)
   - Page 1: UNOFFICIAL banner; turn sequence; Command / Movement / Shooting; distances 2"/6"/8"/9"; terrain categories + visibility strip; WD/Trinity note; footer.
   - Page 2: Charge (2D6 first); Fight; attack sequence; mini S vs T bands; link to `40k_wound_roll_reference`; OC + checklist; footer.
3. **PDF outside repo:** `C:\Personal\print_aids\40k_11e\40k_system_quick_reference.pdf` (via `_html_to_pdf.py`).
4. **Enhancement report:** [`../WD527_Ref_Card_Enhancement_Report.md`](../WD527_Ref_Card_Enhancement_Report.md) — Baseline / Kept / Enhanced / Omitted / Trust.
5. **Setup README:** print table expanded with system QR status + PDF path.
6. **`_html_to_pdf.py`:** added `40k_system_quick_reference` to AIDS list.
7. **Rules README:** indexed `Quick_Reference_Card.md`.

### Regression / constraints

- Dedicated wound HTML **not** deleted or replaced.
- No GW art / binaries in git; PDF outside repo.
- Plan file not edited.
- No git commit.

## Files touched

- `games/warhammer_40k_11e/rules/Quick_Reference_Card.md` (create)
- `games/warhammer_40k_11e/setup/print/40k_system_quick_reference.html` (create)
- `games/warhammer_40k_11e/setup/print/_html_to_pdf.py` (AIDS list)
- `games/warhammer_40k_11e/setup/README.md` (print table)
- `games/warhammer_40k_11e/rules/README.md` (index row)
- `docs/handoffs/wd527_research/WD527_Ref_Card_Enhancement_Report.md` (create)
- `docs/handoffs/wd527_research/slices/S4_implementer.md` (this file)

## Sources read

- `raw/white_dwarf_527/reference_sheet_outline.md`
- `docs/handoffs/wd527_research/track_shipping_in.md` (density + trust)
- `games/warhammer_40k_11e/setup/print/40k_wound_roll_reference.html` + `templates/Gw_Print_Banner.html`
- `games/warhammer_40k_11e/rules/Turn_Structure.md`, `Key_Concepts.md`, `Wound_Roll_Reference.md`

## Not in scope

- Army 2-pager revamps (later slices)
- Mission 38 / Force Disposition HTML changes
- Git commit / plan file edits
