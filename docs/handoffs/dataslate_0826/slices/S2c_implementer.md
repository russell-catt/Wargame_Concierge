# S2c Implementer — dataslate_0826

**Slice:** S2c — Necron MFM v1.3 points pass
**Status:** Complete
**Date:** 2026-08-27
**Model:** `claude-sonnet-5-thinking-high` (per track model matrix)
**Authorization:** Owner 2026-08-27 — full track authorized, draft confidence accepted; Codex wall in force (paraphrase only under `games/warhammer_40k_11e/armies/**`); no PDF commits; no git commit/push by this subagent.

## Summary

Recosted every owned Necron Conclave / starter / army-list / Necron_Lists / QR page that cited Warriors 10 @ 80 or Plasmancer @ 55 (MFM v1.2) to **MFM Necrons v1.3** (owner paste 2026-08-27, `draft`): **Necron Warriors 10 models 80 → 85** (▲+5; 20-model band unchanged at 190), **Plasmancer 55 → 60** (▲+5). No other owned unit in this collection carries a v1.3 ▲ per the research note (Lokhust/Ophydian/Skorpekh deltas are not in any owned list). Every touched list was re-totalled by hand; where a v1.3 delta pushed a list over its stated cap, an **owner-safe cut** was applied and documented (never an invented free point) — in every case this meant dropping or swapping an **enhancement**, not cutting a unit. Two **pre-existing v1.2 arithmetic errors** (unrelated to the v1.3 delta, caught while re-adding every row) were also fixed and flagged. `raw/pointers/points_manuals.md` was already updated with v1.3 rows by slice S1 — verified consistent, not re-edited. Added an additive "Rules currency: … v1.3 …" line to every touched page's `## Games Workshop notice` section, and updated the print-HTML mini footnotes/point totals.

## Before / after totals

| List | Before (v1.2) | After (v1.3) | How it lands |
|------|----------------|--------------|--------------|
| `units/research/Necron-Warriors.md` (10-model cost) | 80 | **85** | Direct MFM re-cost |
| `units/research/Plasmancer.md` | 55 | **60** | Direct MFM re-cost |
| `Starter_250.md` — Tomb World list | 245 / 250 | **250 / 250** (exact) | Warriors ▲+5 only |
| `Starter_250.md` — 3-unit variant | 205 | **210** | Warriors ▲+5 only |
| `Army_List_250_Conclave.md` | 245 / 250 | **250 / 250** (exact) | Warriors ▲+5 only |
| `Starter_500.md` — Foundation (5 units) | 315 | **320** | Warriors ▲+5 only |
| `Starter_500.md` — Path A (Canoptek Court) | 355 | **360** | Warriors ▲+5 only |
| `Starter_500.md` — Path A full-500 (Wraiths) variant | claimed 450→500 (enhancement combo actually summed to 60, not 50 — pre-existing v1.2 bug) | **455 → 500** exact | Wraiths 95 + 3 enhancements (Atomic Disintegrators 10 + Gauntlet of Compression 20 + Gravitic Bolas 15 = 45); Quantum Abacus dropped |
| `Starter_500.md` — Path B (Cryptek Conclave) | 500 (incl. Atomic Disintegrators) | **500** (exact) | Warriors ▲+5, Plasmancer ▲+5 (+10); Atomic Disintegrators enhancement dropped (owner-safe cut, -10) |
| `Starter_500.md` — Path B cheaper no-proxy variant | 315 / 385 | **320 / 390** | Warriors ▲+5 only |
| `Starter_Forces_500_750_1000.md` — 500 V1 | 500 (incl. Atomic Disintegrators) | **500** (exact) | Warriors ▲+5, Plasmancer ▲+5 (+10); enhancement dropped (-10) |
| `Starter_Forces_500_750_1000.md` — 500 V2 | 500 (incl. Atomic Disintegrators) | **500** (exact) | Same fix as 500 V1 |
| `Army_List_500_V1_Conclave.md` | 500 (incl. Atomic Disintegrators) | **500** (exact) | Same fix as 500 V1 |
| `Starter_Forces_500_750_1000.md` — 750 V1 | claimed 750 (actual sum 740 — pre-existing v1.2 bug) | **750** (exact) | Warriors ▲+5 ×2, Plasmancer ▲+5 (+15); enhancement swap Quantum Abacus (15) → Atomic Disintegrators (10), -5 |
| `Starter_Forces_500_750_1000.md` — 750 V2 | claimed 750 (actual sum 740) | **750** (exact) | Same fix as 750 V1 |
| `Army_List_750_V1_Conclave.md` | claimed 750 (actual sum 740) | **750** (exact) | Same fix as 750 V1 |
| `Starter_Forces_500_750_1000.md` — 1,000 V1 ceiling (no purchase) | 720 (shortfall 280) | **725** (shortfall 275) | Plasmancer proxy ▲+5 (Warriors 20-band unchanged) |
| `Starter_Forces_500_750_1000.md` — 1,000 V2 | claimed 1,000 (actual sum 1,020 — pre-existing v1.2 bug) | **1,000** (exact) | Plasmancer ▲+5; enhancements cut to Gauntlet of Compression only (dropped Atomic Disintegrators + Gravitic Bolas, -25) |
| `Army_List_1000_V2_Conclave.md` | claimed 1,000 (actual sum 1,020) | **1,000** (exact) | Same fix as 1,000 V2 |
| `Necron_Lists.md` — Tomb World subtotal | 315 | **320** | Warriors ▲+5 only |
| `Necron_Lists.md` — Phase 1 preferred start (both options) | 205 | **210** | Warriors ▲+5 only |
| `Canoptek_Court.md` / `Cryptek_Conclave.md` fit tables | Warriors 80, Plasmancer 55 | Warriors **85**, Plasmancer **60** | Reference table only, no aggregate total on these pages |
| `Quick_Reference_Play_Guide.md` / print HTML QR | 245 "tonight" | **250** exact | Warriors ▲+5 only |

## Owner-safe cuts and pre-existing-bug fixes (documented, not invented)

1. **500-point Conclave lists (Starter_500 Path B, Starter_Forces 500 V1/V2, Army_List_500_V1_Conclave):** the v1.3 Warriors + Plasmancer delta is exactly +10. All four lists carried a 10-pt **Atomic Disintegrators** enhancement on the Geomancer. Dropping that enhancement absorbs the +10 exactly, with no unit cuts. Documented as a waiver in each file's Change Log; the Geomancer's ability block now notes the enhancement is optional and not included on the budget list.
2. **750-point Conclave lists (Starter_Forces 750 V1/V2, Army_List_750_V1_Conclave):** while re-adding every row to apply the +15 delta (two Warrior units ▲+5 each, Plasmancer ▲+5), the roster's four-enhancement stack (Gauntlet of Compression 20 + Gravitic Bolas 15 + Quantum Abacus 15 = 50) was found to sum to **60**, not the 50 assumed in the v1.2 printing — a pre-existing addition error, not caused by this recost. Fix: drop Quantum Abacus, add Atomic Disintegrators (10) instead, landing the three-enhancement stack at 45 and the whole list exactly on 750.
3. **1,000-point Conclave lists (Starter_Forces 1,000 V2, Army_List_1000_V2_Conclave):** the claimed "1,000" total was actually **1,020** when every row was re-added — a second pre-existing v1.2 arithmetic error, independent of the +5 Plasmancer delta. Fix: keep only Gauntlet of Compression (20) as the enhancement, dropping Atomic Disintegrators (10) and Gravitic Bolas (15), landing exactly on 1,000.
4. **Starter_500.md Path A "full 500 variant" (Wraiths + enhancement, prose note, not a table):** the four-enhancement combo quoted there (10+20+15+15) also summed to 60, not the 50 claimed. Fixed to a three-enhancement combo (Atomic Disintegrators 10 + Gauntlet of Compression 20 + Gravitic Bolas 15 = 45) that lands the new 455-point base (foundation 360 + Wraiths 95) exactly on 500.

None of these cuts touch a unit; all are enhancement swaps/drops on characters that already had spare enhancement slack, and all are called out explicitly in-line and in each file's Change Log so the owner can override before an event.

## Files touched

**Unit research (paraphrase only, cite update):**
- `games/warhammer_40k_11e/armies/necrons/units/research/Necron-Warriors.md`
- `games/warhammer_40k_11e/armies/necrons/units/research/Plasmancer.md`

**Starter / army lists / reference guides (recost + re-total + GW currency line):**
- `games/warhammer_40k_11e/armies/necrons/Starter_250.md`
- `games/warhammer_40k_11e/armies/necrons/Starter_500.md`
- `games/warhammer_40k_11e/armies/necrons/Starter_Forces_500_750_1000.md`
- `games/warhammer_40k_11e/armies/necrons/Army_List_250_Conclave.md`
- `games/warhammer_40k_11e/armies/necrons/Army_List_500_V1_Conclave.md`
- `games/warhammer_40k_11e/armies/necrons/Army_List_750_V1_Conclave.md`
- `games/warhammer_40k_11e/armies/necrons/Army_List_1000_V2_Conclave.md`
- `games/warhammer_40k_11e/armies/necrons/Reference_Guide_250_Conclave.md`
- `games/warhammer_40k_11e/armies/necrons/Reference_Guide_500_V1_Conclave.md`

**Detachment guides / blueprint / faction README (fit-table recost + GW currency line):**
- `games/warhammer_40k_11e/armies/necrons/Canoptek_Court.md`
- `games/warhammer_40k_11e/armies/necrons/Cryptek_Conclave.md`
- `games/warhammer_40k_11e/armies/necrons/Necron_Lists.md`
- `games/warhammer_40k_11e/armies/necrons/README.md`
- `games/warhammer_40k_11e/armies/necrons/Quick_Reference_Play_Guide.md`

**Print HTML (mini footnote + point totals):**
- `games/warhammer_40k_11e/armies/necrons/print/40k_necrons_quick_reference.html`
- `games/warhammer_40k_11e/armies/necrons/print/40k_roster_250_conclave.html`
- `games/warhammer_40k_11e/armies/necrons/print/40k_reference_250_conclave.html`

**New file:**
- `docs/handoffs/dataslate_0826/slices/S2c_implementer.md` (this report)

## Verified, not touched

- `raw/pointers/points_manuals.md` — already carries v1.3 Necron rows (Warriors 80→85, Plasmancer 55→60, plus the other faction ▲ deltas not present in any owned list) from slice **S1**. Read and cross-checked; numbers match this pass exactly. No edit needed.
- `Owned_Models_Inventory.md` — physical model checklist, carries no point costs. No edit needed.
- Unaffected unit research pages (`Geomancer.md`, `Canoptek-Tomb-Crawlers.md`, `Canoptek-Macrocytes.md`, `Canoptek-Scarab-Swarms.md`, `Immortals.md`, `Technomancer.md`, `Royal-Warden.md`, `Lychguard.md`, `Illuminor-Szeras.md`) — no v1.3 ▲ per the research note; left at MFM v1.2.
- `Lokhust-Lord.md`, `Lokhust-Destroyers.md`, `Lokhust-Heavy-Destroyers.md`, `Ophydian-Destroyers.md`, `Skorpekh-Lord.md` — carry v1.3 ▲ per the research note, but **no owned Necron list in this repo fields any of these units**, so no shipping page needed a recost. Left as-is; flagged here for QA visibility.
- `games/warhammer_40k_11e/armies/necrons/print/40k_conclave_primary_missions.html`, `40k_first_game_core.html`, `40k_setup_terrain.html` — grepped, no Warriors/Plasmancer point figures present.

## Codex wall / copyright compliance

No MFM table was pasted into any file. Every edit is a teaching paraphrase of a single unit's point value (a fact, not rules text) plus arithmetic. No datasheet statlines were reproduced or altered. All touched player-facing markdown pages under `games/warhammer_40k_11e/armies/necrons/` retain their `## Games Workshop notice` section and now carry an additive `**Rules currency:** Munitorum Field Manual Necrons **v1.3** (owner paste 2026-08-27) · verify owned PDF.` line per the brief. `units/research/*.md` pages are not player-facing shipping and were left without a GW notice section, consistent with existing convention.

## Waivers / open items for QA

1. **MFM Necrons v1.3 provenance is an owner paste**, not a PDF read — every touched page is stamped `draft` and cites `docs/handoffs/dataslate_0826/research/necron_mfm_v1_3.md`. Re-verify against the owned PDF once the owner confirms a saved path under `C:\Personal\40K\rules\` (tracked in `raw/pointers/points_manuals.md`, set by S1).
2. **Two pre-existing v1.2 arithmetic bugs were fixed opportunistically** (750-point enhancement stack summing to 60 not 50; 1,000-point enhancement stack summing to 1,020 not 1,000) while re-totalling for the Warriors/Plasmancer delta. These are flagged inline and in each Change Log as "also fixes a pre-existing v1.2 arithmetic slip" — QA should confirm this is an acceptable in-scope fix rather than a separate slice.
3. **Enhancement swaps are teaching choices, not the only valid fix.** Every "owner-safe cut" chosen here keeps the unit roster identical and only touches enhancement selection. The owner may prefer a different enhancement combination — all combinations and their pts are still documented on each page.
4. No PDF was read or committed. No `git add` / `git commit` / `git push` was run by this subagent.

## Not touched (S2c scope)

- Space Marines MFM v1.3 recost — separate slice (S2d per track model matrix, if scoped).
- KT24 team balance updates — separate slice (S3).
- `KB/` — Librarian-owned; not touched by Implementer.
- Detachment stratagem/enhancement **rules text** — no rules content changed, only point costs and arithmetic.
