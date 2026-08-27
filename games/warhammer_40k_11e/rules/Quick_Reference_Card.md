<!--
FILE: games/warhammer_40k_11e/rules/Quick_Reference_Card.md
VERSION: v1.1 (2026-08-27)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, track dataslate_0826 / S2e)

DOCUMENT_TYPE: Rules Outline / Play Aid Index
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: Warhammer 40,000 - 11th Edition
REFERENCE_STATUS: Active - teaching outline; mechanics from Core tier 1; disembark move typing added 2026-08-27 per Universal Rules Updates v1.1

SOURCES:
  - raw/white_dwarf_527/reference_sheet_outline.md (WD527 topic map; layout inspiration)
  - C:\Personal\40K\rules\eng_01-06_warhammer40k_new40k_core_rules.pdf (read 2026-08-16)
  - raw/_dataslate_0826_staging/eng_wh40k_core&key_universal_rules_updates-lu3grocned-rphh78bl6k.pdf (Universal Rules Updates v1.1, legal 26 Aug 2026; staging copy, read 2026-08-27)
  - C:\Personal\40K\WD_527\40K_ref-card.pdf (tier 1.5 layout inspiration only)
  - games/warhammer_40k_11e/rules/Turn_Structure.md
  - games/warhammer_40k_11e/rules/Key_Concepts.md
  - games/warhammer_40k_11e/rules/Wound_Roll_Reference.md

PURPOSE:
  Outline for the system Letter 2-pager quick reference. Topic map follows
  WD527 pull-out sides; body is our teaching paraphrase with Core IDs.

PRINT_NOTE:
  Letter 2-pager: games/warhammer_40k_11e/setup/print/40k_system_quick_reference.html
  PDF outside repo: C:\Personal\print_aids\40k_11e\40k_system_quick_reference.pdf
  Full S×T matrix stays on 40k_wound_roll_reference (do not merge).

UPDATE_TRIGGER:
  Core Rules change to turn sequence, charge, fight, attack sequence, or terrain categories.
-->

# Quick Reference Card — system outline

Teaching paraphrase for the table. Bracket numbers are **Core rule IDs**. Layout topic order follows the owned WD527 pull-out (`raw/white_dwarf_527/reference_sheet_outline.md`); **mechanics are Core-first** (tier 1). No GW art; no magazine transcription.

**Print:** [`../setup/print/40k_system_quick_reference.html`](../setup/print/40k_system_quick_reference.html) → `C:\Personal\print_aids\40k_11e\40k_system_quick_reference.pdf`

**Baseline note:** WD527 quick-reference pull-out used as layout inspiration only. Owned digital backup purchased Trinity Hobby **2026-08-22**; local `C:\Personal\40K\WD_527\`. Tier **1.5**.

---

## Side A — Turn sequence and early phases

### Active player / terrain header

- **Active player** (**01.03**): whose turn it is vs opposing player.
- **Terrain** (**13**): Exposed / Light / Dense features; obscuring areas. Areas before features — see [`../setup/Terrain_Basics.md`](../setup/Terrain_Basics.md).

### Turn sequence (**07.02**)

1. Start of Turn  
2. Command — CP, battle-shock, abilities  
3. Movement — move types; reserves  
4. Shooting — ranged attacks  
5. Charge — charge moves  
6. Fight — both players melee  
7. End of Turn — non-mission then mission scoring  

### Command (**08**)

Start → **Gain Core CP** (**08.02**, both +1) → **Battle-shock** (**08.03**) → Command abilities → End.

Battle-shocked: OC 0, no stratagem targeting, no actions.

### Movement (**09**)

Remain Stationary / Normal / Advance / Fall Back / Disembark / Ingress (**09.02** family).

- Engagement range: **2"** horizontal, **5"** vertical  
- Coherency (**03.03**): **2"** to a squadmate + **9"** to all models in the unit  
- Ingress: within **6"** of a battlefield edge, more than **8"** from enemies (**20.04**); Deep Strike: anywhere more than **8"** from enemies  
- Disembark (**18.04**): TRANSPORT not Advanced/Fallen Back. **v1.1 (26 Aug 2026):** charge-after-normal-move disembark = **assault disembark move (18.06)**; disembark-after-Advance = **shock disembark move (18.07)** — both need a separate rule granting the permission

### Shooting (**10**)

Normal / Assault / Close-quarters / Indirect.

- Benefit of Cover (**13.08**): worsen attacker BS by 1 (not a save bonus)  
- Hidden (**13.09**): dense keywords; detection **15"**  
- Obscuring (**13.10**): blocks LOS from outside the area  

### Key distances strip

| Distance | Use |
|----------|-----|
| **2"** | Engagement (horizontal); coherency adjacency |
| **6"** | Ingress from board edge |
| **8"** | Reserves / Deep Strike clearance from enemies |
| **9"** | Coherency unit span |

---

## Side B — Charge, fight, attack sequence

### Charge (**11**)

**Roll 2D6 first** (**11.02**) — that distance caps targets and move. Eligible: on battlefield, within **12"** of an enemy, unengaged, did not Advance or Fall Back. End within **1"** of target / become engaged. Completing a charge grants **Fights First**.

### Fight (**12**)

Pile In (**12.02**, 3") → Fight (alternating; Fights First first) → Consolidate (**12.07**, 3"). Both players act; active player piles/consolidates first.

### Making attacks (**04**) / Attack sequence (**05**)

Select weapons → targets → resolve.

1. **Hit** (**05.01**) — unmod 1 fails; unmod 6 critical hit; ≥ BS/WS hits  
2. **Wound** (**05.02**) — S vs T bands (below); unmod 1 fails; unmod 6 critical wound  
3. **Save** (**05.03**) — armour (AP applies) or invulnerable (no AP)  
4. **Damage** (**05.04**) — D wounds; excess does not spill  

### Mini wound bands (**05.02**)

| Band | Need |
|------|------|
| S ≥ 2×T | **2+** |
| S > T | **3+** |
| S = T | **4+** |
| S < T but > ½T | **5+** |
| S ≤ ½T | **6+** |

Full matrix laminate: [`Wound_Roll_Reference.md`](Wound_Roll_Reference.md) · [`../setup/print/40k_wound_roll_reference.html`](../setup/print/40k_wound_roll_reference.html) — **do not replace** with this card.

---

## Related

- [`Turn_Structure.md`](Turn_Structure.md) — full phase checklist  
- [`Key_Concepts.md`](Key_Concepts.md) — attack sequence detail  
- [`Wound_Roll_Reference.md`](Wound_Roll_Reference.md) — S×T grid  
- Enhancement report: [`../../../docs/handoffs/wd527_research/WD527_Ref_Card_Enhancement_Report.md`](../../../docs/handoffs/wd527_research/WD527_Ref_Card_Enhancement_Report.md)

---

## Games Workshop notice

**UNOFFICIAL.** This document is completely unofficial and in no way endorsed by Games Workshop Limited. Personal / no-charge use only — never for sale. Warhammer, Warhammer 40,000 and associated marks are trademarks of Games Workshop Limited. Used without permission. No challenge to their status intended. Warhammer 40,000 is Copyright Games Workshop Limited. Teaching notes by Russell Catt (Wargame Concierge). Games Workshop retains IP in the settings and characters. No official logos.

## Change Log
- v1.1 (2026-08-27): Universal Rules Updates v1.1 (legal 26 Aug 2026) currency pass — added disembark move typing line (`18.06` assault / `18.07` shock) to Movement (**09**) side; track `dataslate_0826` slice S2e.
- v1.0 (2026-08-25): Initial outline from WD527 topic map + Core IDs (wd527_shipping S4).

## Attribution
- Project: Wargame_Concierge
- Maintainer: Russell Catt

## Rising Tide Notes
- This document follows Rising Tide documentation standards.
- **Verify before you play.** Cross-check against owned Core Rules; content reflects sources read **2026-08-16**.
