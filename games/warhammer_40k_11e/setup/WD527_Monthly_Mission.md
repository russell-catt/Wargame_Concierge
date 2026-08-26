<!--
FILE: games/warhammer_40k_11e/setup/WD527_Monthly_Mission.md
VERSION: v1.0 (2026-08-24)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (wd527_research S3)

DOCUMENT_TYPE: Teaching Mission / Play Aid
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: Warhammer 40,000 - 11th Edition
REFERENCE_STATUS: Active - verified from owned WD527 tier 1.5; cross-checked Event Companion sequence

SOURCES:
  - C:\Personal\40K\WD_527\40K_missions.pdf p1 (Mission 38)
  - raw/white_dwarf_527/mission_card_research.md
  - games/warhammer_40k_11e/setup/Board_Setup.md
  - games/warhammer_40k_11e/setup/Chapter_Approved_Force_Dispositions.md

PURPOSE:
  Player-facing Mission 38 Converging Ambition with build notes for owned terrain.

UPDATE_TRIGGER:
  New WD Bunker mission or Chapter Approved sequence change.
-->

# Mission 38 — Converging Ambition

**White Dwarf Bunker** monthly mission (WD527). Rival armies fight over a chain of vital sites; your **Force Disposition** sets your Primary scoring pattern.

> This card **replaces steps 2 and 3** of the standard Chapter Approved mission sequence. Run the rest of the fourteen-step pre-game from [`Board_Setup.md`](Board_Setup.md).

---

## Table and objectives

| Item | Spec |
|------|------|
| **Battlefield** | **44" × 60"** (standard event size) |
| **Deployment** | Opposing long-edge zones (see print card / sketch below) |
| **Deployment depth** | **14"** from each long edge (per WD card diagram) |
| **Centre dead zone** | **9"** radius — used for Reconnaissance scoring |
| **Objectives** | **5** — one centre + four corners, each **10"** from the nearest table corner |
| **Objective type** | Terrain **footprints** (area = objective) per 14.01 |

### ASCII layout (not to scale)

```
+--------------------------------------------------+
|  [O]                                    [O]      |  <- corner objs @ 10" from corners
|     +------------------------------------+       |
|     |         DEPLOY (14")             |       |
|     |                                    |       |
|  [O]              (9")                  [O]    |  <- centre obj
|     |                                    |       |
|     |         DEPLOY (14")             |       |
|     +------------------------------------+       |
|  [O]                                    [O]      |
+--------------------------------------------------+
```

---

## Pick your Primary (one Force Disposition)

Write your Disposition on the list at Muster. Score **your** block below.

### Purge the Foe

*End of your turn.*

| Condition | VP |
|-----------|-----|
| One or more enemy units destroyed this turn | 4 |
| More enemy units destroyed this turn than friendly units destroyed **last** turn | 6 |
| You control opponent's **home** objective | 10 |

### Reconnaissance

*End of your turn.*

| Condition | VP |
|-----------|-----|
| ≥3 friendly units wholly in **3** different quarters, none within 6" of centre | 3 |
| **Or** ≥4 units in **4** quarters (same centre rule) | 6 |
| Per enemy unit destroyed this turn | 2 |

### Take and Hold

*End of your Command phase **or** end of turn 5.*

| Condition | VP |
|-----------|-----|
| Per objective you control | 3 |
| Per objective above (not home) if you also control **home** | +2 cumulative |

### Priority Assets

*End of your Command phase **or** end of turn 5.*

| Condition | VP |
|-----------|-----|
| You control one or more objectives | 4 |
| One of those is **central** | +5 cumulative |
| You held that central at end of your **previous** Command phase | +5 cumulative |

### Disruption

*End of your turn.*

| Condition | VP |
|-----------|-----|
| Per objective you control | 4 |
| You control more objectives than opponent | 4 |
| Per table quarter with **no** enemy units | 2 |

**Caps:** align with your event — Chapter Approved Primaries are typically **45 VP** max (15 VP per battle round). See [`Chapter_Approved_Force_Dispositions.md`](Chapter_Approved_Force_Dispositions.md).

---

## Build this with what we own

### Terrain

1. **Lay terrain areas first** — print A4 footprints from `C:\Personal\40K\Terrain\A4\` (Imperial World or grey city tone for Armageddon ruins).  
2. Place **five objective footprints** before scenery models: centre + corners at 10" from corners; mark a **9"** centre circle for Reconnaissance.  
3. Add ruins/barricades **on** areas — WD battle report used industrial ruins with blue barricades; any dense/light mix works if footprints are clear.

### Lists

- **Kitchen table:** 500–1000 pts; WD report used showcase Armageddon boxes (Orks vs Blood Angels).  
- **This repo:** Necron Cryptek Conclave or SM starters — pick Dispositions from [`Chapter_Approved_Force_Dispositions.md`](Chapter_Approved_Force_Dispositions.md).

### Secondaries

Mission card covers **Primary** only. Agree Tactical vs Fixed secondaries per [`Board_Setup.md`](Board_Setup.md) step 6. WD battle report used **Tactical** (two new cards each turn).

### Quick checklist

- [ ] 44"×60" or scaled table marked  
- [ ] Five terrain-objective footprints placed  
- [ ] Force Disposition on both lists  
- [ ] Primary block identified per player  
- [ ] Steps 4–14 of Board_Setup  

---

## Related

- [`print/40k_wd527_mission.html`](print/40k_wd527_mission.html) — 1-page print summary  
- [`../../KB/setup/wd527_monthly_mission.md`](../../KB/setup/wd527_monthly_mission.md) — KB entity  
- [`../rules/Wound_Roll_Reference.md`](../rules/Wound_Roll_Reference.md) — wound laminate  

---

## Games Workshop notice

**UNOFFICIAL.** This document is completely unofficial and in no way endorsed by Games Workshop Limited. Personal / no-charge use only — never for sale. Warhammer, Warhammer 40,000 and associated marks are trademarks of Games Workshop Limited. Used without permission. No challenge to their status intended. Warhammer 40,000 is Copyright Games Workshop Limited. Teaching notes by Russell Catt (Wargame Concierge). Games Workshop retains IP in the settings and characters. No official logos.

## Change Log

- v1.0 (2026-08-24): Initial teaching rebuild (wd527_research S3).

## Attribution

- Project: Wargame_Concierge
- Maintainer: Russell Catt
