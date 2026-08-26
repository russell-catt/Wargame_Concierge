# WD527 Ref Card Enhancement Report

**Track:** `wd527_shipping` · **Slice:** S4  
**Date:** 2026-08-25  
**Deliverable:** System Letter 2-pager quick reference (original teaching aid)

**Baseline source:** owned WD527 pull-out `C:\Personal\40K\WD_527\40K_ref-card.pdf` (tier **1.5**), topic-mapped in `raw/white_dwarf_527/reference_sheet_outline.md`.  
**Mechanics SoT:** Core Rules `eng_01-06_*` (tier **1**).  
**Provenance:** Owned digital backup purchased Trinity Hobby **2026-08-22**.

**Shipped paths:**

- Outline: `games/warhammer_40k_11e/rules/Quick_Reference_Card.md`
- Print HTML: `games/warhammer_40k_11e/setup/print/40k_system_quick_reference.html`
- PDF (outside repo): `C:\Personal\print_aids\40k_11e\40k_system_quick_reference.pdf`

---

## Baseline

WD527 Side A covers active player, terrain categories, turn sequence (07.02), Command (CP + battle-shock), Movement (move types + engagement), and Shooting (types + cover / Hidden / Obscuring). Side B covers Charge (2D6), Fight (pile / fight / consolidate), making attacks, and the Hit / Wound / Save / Damage sequence with an S vs T wound table pointer.

That topic map is the **layout inspiration only**. We did not copy magazine wording, art, or card graphics into the repo.

---

## Kept

| Topic | Why kept |
|-------|----------|
| Seven-step turn sequence | Table spine; matches teaching `Turn_Structure.md` |
| Command CP + battle-shock penalties | Highest-frequency Command mistakes |
| Move types + shooting types | Beginner decision trees |
| Charge **2D6 first** | WD Rules Focus alignment; Core **11.02** |
| Fight pile → fight → consolidate | Both-players sequencing |
| Full attack sequence Hit/Wound/Save/Damage | Shared with shooting and melee |
| Terrain Exposed / Light / Dense + BoC / Hidden / Obscuring | Setup ↔ mid-game visibility |
| Core IDs in brackets | Audit trail without dumping quote text |

---

## Enhanced

| Addition | Why |
|----------|-----|
| **Key distances strip (2" / 6" / 8" / 9")** | Explicit teaching of coherency vs ingress vs Deep Strike clearance (WD Commentary on Movement) |
| **Mini S vs T wound bands (2+/3+/4+/5+/6+)** on page 2 | Density rule: wound utility on every system table aid; still points to full laminate |
| **Link to `40k_wound_roll_reference`** | Dedicated S×T matrix stays separate — not replaced |
| **OC reminder [14]** | Scoring spine without mission dump |
| **At-table checklist** (common traps) | From `Turn_Structure.md` mistakes table |
| **UNOFFICIAL banner + every-page footer** | AGENTS Sec 10 / print policy |
| **Trinity Hobby 2026-08-22 cite** in small note | Locked provenance |
| **Two-column dense Letter fill** | Exactly 2 pages, not sparse |

---

## Omitted

| Omitted from WD pull-out / magazine | Why |
|-------------------------------------|-----|
| GW / WD artwork and card chrome | No GW binaries or art in git |
| Verbatim magazine / card rules text | Teaching paraphrase only; Codex wall |
| Full numeric S×T matrix on this sheet | Lives on wound laminate; duplicate would bloat or invite drift |
| Faction / detachment rules | System spine only |
| Mission 38 Primary tables | Separate print: `40k_wd527_mission` |
| Stratagem encyclopedia | Out of scope for 2 pages |
| Vertical engagement 5" detail beyond one line | Horizontal 2" + key strip prioritized |

---

## Trust

| Claim class | Tier | Notes |
|-------------|------|-------|
| Turn / phase / attack / terrain mechanics | **1** Core | Paraphrase cross-checked against owned Core IDs (read 2026-08-16 teaching spine) |
| Topic order / density priorities | **1.5** WD527 | Layout inspiration from owned pull-out + Trinity Hobby purchase date |
| Wound bands | **1** Core **05.02** | Same thresholds as `Wound_Roll_Reference.md` |
| Full S×T grid | **1** | Separate aid `40k_wound_roll_reference` — do not treat this QR as the matrix SoT |

**Conflict rule:** Core / Event Companion wins over WD commentary on any mechanical disagreement.

---

## Related

- Slice report: [`slices/S4_implementer.md`](slices/S4_implementer.md)
- Outline: [`../../../games/warhammer_40k_11e/rules/Quick_Reference_Card.md`](../../../games/warhammer_40k_11e/rules/Quick_Reference_Card.md)
- Wound laminate: [`../../../games/warhammer_40k_11e/setup/print/40k_wound_roll_reference.html`](../../../games/warhammer_40k_11e/setup/print/40k_wound_roll_reference.html)
