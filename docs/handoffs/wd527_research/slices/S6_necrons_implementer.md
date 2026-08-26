# S6 Implementer — Necrons portion (wd527_shipping)

**Slice:** S6 (Necrons folder only)  
**Status:** Complete  
**Date:** 2026-08-25  
**Role:** Implementer  
**Git:** no commit (per slice gate)  
**Plan:** not edited

## Goal

Enhance all top-level teaching/play guides under `games/warhammer_40k_11e/armies/necrons/` plus `print/*.html` for post-WD527 system truth: distance triad, footprint OC, Force Disposition callouts, locked Commentary where WD habits apply, system-spine links, Codex-wall paraphrase, 2-pager density, PDF regen.

## Pass checklist

| # | Check | Result |
|---|-------|--------|
| 1 | System facts: 6″ Ingress / >8″ Deep Strike / 9″ coherency; terrain-footprint OC; Force Disposition | **PASS** — QR, print aids, Reanimation, Court, Conclave, Primaries, first-game/setup HTML |
| 2 | Locked Commentary format where WD habit insight applies | **PASS** — Leaders+Support (QR, Conclave); Distance triad (QR); Terrain Objectives (Reanimation, Court) |
| 3 | Link Wound_Roll_Reference, system QR path, Mission 38, Chapter_Approved Force Dispositions | **PASS** — README + starters/lists/references/detachments/print README |
| 4 | Codex wall — paraphrase only | **PASS** — no faction-pack dumps; Core IDs as pointers only |
| 5 | Exactly-2-page MD/HTML fill both pages; no page 3 | **PASS** — see density table below |
| 6 | Regen PDFs after HTML change | **PASS** — `_html_to_pdf.py` (includes conclave primaries) → `C:\Personal\print_aids\learn_to_play_event\` |

## 2-pager density confirmation

| Aid | Pages | Fill notes |
|-----|-------|------------|
| `Quick_Reference_Play_Guide.md` | 2 | Page 1: Disposition + distances + phases + RP + detachments + combat + S vs T + Leaders Commentary. Page 2: starter + do/don’t + OC/attach + Distance Commentary + keywords + checklists |
| `Cryptek_Conclave_Primary_Missions.md` | 2 | Page 1: Disposition + distances + S vs T + Primaries 1–3. Page 2: Primaries 4–5 + toolkit + densified pre-game |
| `print/40k_necrons_quick_reference.html` | 2 `.page` | Both pages filled; UNOFFICIAL banner p1; S vs T + distances + phase content |
| `print/40k_reference_250_conclave.html` | 2 | Page 2 densified with S vs T, phase strip, Mission 38 |
| `print/40k_roster_250_conclave.html` | 2 | Page 2 densified with distances / S vs T / phases / Disposition checklist |
| `print/40k_conclave_primary_missions.html` | 2 | Both pages densified with spine + S vs T + phase strip |
| `print/40k_first_game_core.html` | 2 | Compacted after spill; Ingress row + Disposition/Mission 38; PDF verified **2 pages** |
| `print/40k_setup_terrain.html` | 2 | Spine + distances; Muster/Mission steps; page-2 phase strip + S vs T |

**Note:** `40k_system_quick_reference.html` is owned by S4 (path linked; file may land when S4 ships).

## Commentary blocks added

| File | Title |
|------|-------|
| `Quick_Reference_Play_Guide.md` | Leaders and Support; Distance triad clarity |
| `Cryptek_Conclave.md` | Leaders and Support |
| `Reanimation_Protocols.md` | Rules Focus: Terrain Objectives |
| `Canoptek_Court.md` | Rules Focus: Terrain Objectives |

All use locked paraphrase ≤6 sentences + Trinity Hobby **2026-08-22** Cite / tier **1.5**.

## Files touched

### Teaching markdown (top-level)

- `games/warhammer_40k_11e/armies/necrons/README.md`
- `games/warhammer_40k_11e/armies/necrons/Quick_Reference_Play_Guide.md`
- `games/warhammer_40k_11e/armies/necrons/Reanimation_Protocols.md`
- `games/warhammer_40k_11e/armies/necrons/Canoptek_Court.md`
- `games/warhammer_40k_11e/armies/necrons/Cryptek_Conclave.md`
- `games/warhammer_40k_11e/armies/necrons/Cryptek_Conclave_Primary_Missions.md`
- `games/warhammer_40k_11e/armies/necrons/Starter_250.md`
- `games/warhammer_40k_11e/armies/necrons/Starter_500.md`
- `games/warhammer_40k_11e/armies/necrons/Starter_Forces_500_750_1000.md`
- `games/warhammer_40k_11e/armies/necrons/Army_List_250_Conclave.md`
- `games/warhammer_40k_11e/armies/necrons/Army_List_500_V1_Conclave.md`
- `games/warhammer_40k_11e/armies/necrons/Army_List_750_V1_Conclave.md`
- `games/warhammer_40k_11e/armies/necrons/Army_List_1000_V2_Conclave.md`
- `games/warhammer_40k_11e/armies/necrons/Reference_Guide_250_Conclave.md`
- `games/warhammer_40k_11e/armies/necrons/Reference_Guide_500_V1_Conclave.md`
- `games/warhammer_40k_11e/armies/necrons/Necron_Lists.md`
- `games/warhammer_40k_11e/armies/necrons/Owned_Models_Inventory.md`

### Print

- `games/warhammer_40k_11e/armies/necrons/print/40k_necrons_quick_reference.html`
- `games/warhammer_40k_11e/armies/necrons/print/40k_reference_250_conclave.html`
- `games/warhammer_40k_11e/armies/necrons/print/40k_roster_250_conclave.html`
- `games/warhammer_40k_11e/armies/necrons/print/40k_conclave_primary_missions.html`
- `games/warhammer_40k_11e/armies/necrons/print/40k_first_game_core.html`
- `games/warhammer_40k_11e/armies/necrons/print/40k_setup_terrain.html`
- `games/warhammer_40k_11e/armies/necrons/print/README.md`
- `games/warhammer_40k_11e/armies/necrons/print/_html_to_pdf.py` (added `40k_conclave_primary_missions` to AIDS)

### Handoff

- `docs/handoffs/wd527_research/slices/S6_necrons_implementer.md` (this file)

## Out of scope (this subagent)

- `armies/space_marines/**`, `adepta_sororitas/**`, `death_guard/**`
- `units/research/**` deep rewrite
- Plan file edits
- Git commit / push
- Creating `setup/print/40k_system_quick_reference.html` (S4)

## PDFs regenerated

Run: `python games/warhammer_40k_11e/armies/necrons/print/_html_to_pdf.py`  
Target: `C:\Personal\print_aids\learn_to_play_event\`  

**Page-count verify (pypdf):** all six aids = **exactly 2 pages** (first_game_core re-tightened after an initial 3-page spill).
