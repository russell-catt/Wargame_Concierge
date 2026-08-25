<!--
FILE: games/warhammer_40k_11e/rules/Wound_Roll_Reference.md
VERSION: v1.0 (2026-08-24)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (wd527_research S2)

DOCUMENT_TYPE: Rules Reference / Play Aid
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: Warhammer 40,000 - 11th Edition
REFERENCE_STATUS: Active - verified against Core 05.02

SOURCES:
  - C:\Personal\40K\rules\eng_01-06_warhammer40k_new40k_core_rules.pdf p.18 (WOUND ROLLS — 05.02)
  - games/warhammer_40k_11e/rules/Core_Rules_Quotes.md (05.02)
  - C:\Personal\40K\WD_527\40K_ref-card.pdf (tier 1.5 layout inspiration only)

PURPOSE:
  Numeric Strength vs Toughness wound chart for table lookup. Recalculated
  from tier-1 Core — not traced from White Dwarf artwork.

PRIMARY_AUDIENCE:
  - Any player resolving shooting or melee wounds

PRINT_NOTE:
  Laminate: games/warhammer_40k_11e/setup/print/40k_wound_roll_reference.html

UPDATE_TRIGGER:
  Core Rules FAQ changes to 05.02 wound thresholds.
-->

# Wound roll reference — Strength vs Toughness

Roll one D6 per hit. Compare weapon **Strength (S)** to target **Toughness (T)**. You need **this result or higher** on the die (**Core 05.02**).

| S vs T | Required roll |
|--------|---------------|
| S is **twice** (or more than twice) T | **2+** |
| S is **greater than** T (but less than 2×T) | **3+** |
| S **equals** T | **4+** |
| S is **less than** T (but greater than half T) | **5+** |
| S is **half** T or less | **6+** |

- Unmodified **1** always fails.  
- Unmodified **6** is a **critical wound** (Devastating Wounds, Anti-X, etc.).  
- Abilities that skip or replace the wound roll (e.g. Lethal Hits into mortals, Anti-INFANTRY 3+) use their own text — this table is the default S vs T test.

Full quote: [`Core_Rules_Quotes.md`](Core_Rules_Quotes.md) — **05.02**.

---

## Lookup matrix (S 1–14 × T 1–14)

Read **row = attack Strength**, **column = target Toughness**. Cell = minimum D6 result to wound.

| S \\ T | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 | T9 | T10 | T11 | T12 | T13 | T14 |
|--------|----|----|----|----|----|----|----|----|----|-----|-----|-----|-----|-----|
| **S1** | 4+ | 6+ | 6+ | 6+ | 6+ | 6+ | 6+ | 6+ | 6+ | 6+ | 6+ | 6+ | 6+ | 6+ |
| **S2** | 2+ | 4+ | 5+ | 6+ | 6+ | 6+ | 6+ | 6+ | 6+ | 6+ | 6+ | 6+ | 6+ | 6+ |
| **S3** | 2+ | 3+ | 4+ | 5+ | 5+ | 6+ | 6+ | 6+ | 6+ | 6+ | 6+ | 6+ | 6+ | 6+ |
| **S4** | 2+ | 2+ | 3+ | 4+ | 5+ | 5+ | 5+ | 6+ | 6+ | 6+ | 6+ | 6+ | 6+ | 6+ |
| **S5** | 2+ | 2+ | 3+ | 3+ | 4+ | 5+ | 5+ | 5+ | 5+ | 6+ | 6+ | 6+ | 6+ | 6+ |
| **S6** | 2+ | 2+ | 2+ | 3+ | 3+ | 4+ | 5+ | 5+ | 5+ | 5+ | 5+ | 6+ | 6+ | 6+ |
| **S7** | 2+ | 2+ | 2+ | 3+ | 3+ | 3+ | 4+ | 5+ | 5+ | 5+ | 5+ | 5+ | 5+ | 6+ |
| **S8** | 2+ | 2+ | 2+ | 2+ | 3+ | 3+ | 3+ | 4+ | 5+ | 5+ | 5+ | 5+ | 5+ | 5+ |
| **S9** | 2+ | 2+ | 2+ | 2+ | 3+ | 3+ | 3+ | 3+ | 4+ | 5+ | 5+ | 5+ | 5+ | 5+ |
| **S10** | 2+ | 2+ | 2+ | 2+ | 2+ | 3+ | 3+ | 3+ | 3+ | 4+ | 5+ | 5+ | 5+ | 5+ |
| **S11** | 2+ | 2+ | 2+ | 2+ | 2+ | 3+ | 3+ | 3+ | 3+ | 3+ | 4+ | 5+ | 5+ | 5+ |
| **S12** | 2+ | 2+ | 2+ | 2+ | 2+ | 2+ | 3+ | 3+ | 3+ | 3+ | 3+ | 4+ | 5+ | 5+ |
| **S13** | 2+ | 2+ | 2+ | 2+ | 2+ | 2+ | 3+ | 3+ | 3+ | 3+ | 3+ | 3+ | 4+ | 5+ |
| **S14** | 2+ | 2+ | 2+ | 2+ | 2+ | 2+ | 2+ | 3+ | 3+ | 3+ | 3+ | 3+ | 3+ | 4+ |

**Examples:** Bolter S4 vs T4 → **4+**. Melta S9 vs T6 → **3+**. Las cannon S12 vs T10 → **2+**.

---

## Related

- [`Key_Concepts.md`](Key_Concepts.md) — full attack sequence  
- [`../setup/print/40k_wound_roll_reference.html`](../setup/print/40k_wound_roll_reference.html) — 2-page print laminate  
- [`../armies/necrons/print/40k_first_game_core.html`](../armies/necrons/print/40k_first_game_core.html) — first-game companion

---

## Games Workshop notice

**UNOFFICIAL.** This document is completely unofficial and in no way endorsed by Games Workshop Limited. Personal / no-charge use only — never for sale. Warhammer, Warhammer 40,000 and associated marks are trademarks of Games Workshop Limited. Used without permission. No challenge to their status intended. Warhammer 40,000 is Copyright Games Workshop Limited. Teaching notes by Russell Catt (Wargame Concierge). Games Workshop retains IP in the settings and characters. No official logos.

## Change Log

- v1.0 (2026-08-24): Initial matrix from Core 05.02 (wd527_research S2).

## Attribution

- Project: Wargame_Concierge
- Maintainer: Russell Catt
