<!--
FILE: games/warhammer_40k_11e/armies/necrons/Reference_Guide_500_V1_Conclave.md
VERSION: v1.2 (2026-08-20)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (cloud agent)

DOCUMENT_TYPE: Play Reference / Math Guide
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: Warhammer 40,000 - 11th Edition
FACTION: Necrons
DETACHMENT: Cryptek Conclave
REFERENCE_STATUS: Active - companion to Army_List_500_V1_Conclave.md. Rules from Reanimation_Protocols.md and Cryptek_Conclave.md. Attack math from local Warrior/Immortal research.

SOURCES:
  - games/warhammer_40k_11e/armies/necrons/Army_List_500_V1_Conclave.md
  - games/warhammer_40k_11e/armies/necrons/Reference_Guide_250_Conclave.md
  - games/warhammer_40k_11e/armies/necrons/Reanimation_Protocols.md
  - games/warhammer_40k_11e/armies/necrons/Cryptek_Conclave.md
  - units/research/Necron-Warriors.md, Immortals.md, Canoptek-Scarab-Swarms.md

PURPOSE:
  Full Reanimation + Conclave buff math for the 500 V1 list (two Cryptek
  bricks, Warden proxy, Scarabs).

PRIMARY_AUDIENCE:
  - Games with Army_List_500_V1_Conclave.md

UPDATE_TRIGGER:
  Update when army rule, Conclave, or profiles change.
-->

# Reference guide - 500 pts V1 Cryptek Conclave

Companion to [`Army_List_500_V1_Conclave.md`](Army_List_500_V1_Conclave.md). Builds on [`Reference_Guide_250_Conclave.md`](Reference_Guide_250_Conclave.md).

**List in one line:** Geomancer (Atomic Disintegrators) + Technomancer + Apprentek→Plasmancer + Despotek→Warden + 10 Warriors + 5 Immortals + 6 Scarabs = **500**.

**Attachments:** Warriors ← Warden + Geomancer; Immortals ← Technomancer **or** Plasmancer proxy.

---

## 1. Reanimation Protocols - full math (500 list)

### Baseline (every unit, every your Command phase)

End of **Command phase** (`08.05`) — roll D3 per eligible unit on the board.

| Unit on the list | Starting wounds pool | Avg D3 / your CP | Notes |
|------------------|----------------------|------------------|-------|
| Warriors (10) | 10 × 1W = **10** | **2.0** | Plus Geomancer/Warden wounds if those models are in the unit |
| Immortals (5) | 5 × 1W = **5** | **2.0** | Plus attached Cryptek |
| Scarabs (6) | 6 × 4W = **24** | **2.0** | Heal multi-wound models before returning bases |
| Characters alone | if not attached | **2.0** each | Prefer them attached |

**Army-wide average per your Command phase** (3 units): 3 × 2.0 = **~6 wounds** returned across the force, free.

### Heal-first order (same as 250)

1. Heal wounded survivors.  
2. Then return destroyed models at **1W**.  
3. Stop at Starting Strength / full wounds.  
4. **Wiped unit = no reanimation.**

### Scarab-specific math

Scarabs have **4W each**. Chip damage often lands as "2 wounds on a base" rather than dead bases.

| Example | D3 = 2 |
|---------|--------|
| One Scarab base on 2W remaining (2 lost) | Both wounds heal that base to full - **0 bases returned** |
| Two bases destroyed, survivors full | Return **2** bases at **1W** each |

Multi-wound models make "heal first" eat reanimation before bodies come back - same rule, bigger bite.

### Stacking modifiers available on this collection

| Source | Extra math | On this 500 V1 list? |
|--------|------------|----------------------|
| Army rule D3 | +avg 2 / unit / your CP | **Yes - all units** |
| Macrocytes nanoscarab (+1 wound near, once/BR) | +1 | **No** - Macrocytes not in this list |
| Reanimator extra D3 | +avg 2 | **No** - not owned |
| Resurrection Orb → D6 once | avg 3.5 instead of 2 | **No** - no Overlord |
| **Conclave stratagem - Potentiality Syphon** (`15.01`, paraphrase) | Fires Reanimation in **opponent's Command phase** (`08.01`) if unit is on an objective (`14.02`); Cryptek unit gets **+1 wound** | **Yes - 1CP** when on objective |

### Off-turn reanimation math (Potentiality Syphon)

Confirm exact wording on your faction pack. Teaching model used here:

| | Your CP | Opponent CP (stratagem) | Total / battle round |
|--|---------|-------------------------|----------------------|
| Normal Warrior brick on objective | D3 (avg 2) | D3+1 if Cryptek unit (avg 3) | **avg 5 wounds / BR** |
| Over 5 battle rounds | | | **~25 wounds** returned if never wiped and stratagem every opponent CP |

**CP budget:** stratagem is 1CP. You gain 1CP per Command phase baseline - you cannot fire it every opponent turn forever without other CP sources. Plan **2–3** off-turn procs per game unless Quantum Abacus / other refunds apply (not on this list).

### Attached characters and reanimation

Wounds on the Geomancer / Warden / Technomancer / Plasmancer proxy are part of the **unit** while attached. Reanimation can **heal** a wounded attached character before returning Warriors/Immortals. **Destroyed CHARACTER models are not revived into the bodyguard by ordinary RP** (core heal rules exclude CHARACTER from that revive step). WarCom July 2026 update: if a character revives under its own revive rule, it returns as a **unit of one**, not rejoined to the brick. Safe habit: keep the Cryptek toward the back of the coherency blob. Detail: `KB/analyses/their_number_is_legion_potentiality_syphon_250.md`.

---

## 2. Cryptek Conclave buffs - full package

### Always-on

| Buff | Who | Effect |
|------|-----|--------|
| `[ASSAULT]` on Cryptek guns | Geomancer, Technomancer, Plasmancer proxy | Those models may shoot after Advance |

### Menu (once per Cryptek unit per your Shooting phase)

Pick **one** when you select that unit to shoot:

`[ANTI-INFANTRY 3+]` · `[ANTI-MOUNTED 4+]` · `[ASSAULT]` · `[HEAVY]` · `[IGNORES COVER]`  
**+ Atomic Disintegrators:** anti-Monster / anti-Vehicle options (on Geomancer's Warriors brick).

### Two bricks = two picks

| Unit shooting | Bearer | Menu applies to |
|---------------|--------|-----------------|
| Warriors | Geomancer (+ Warden Leader) | All Warrior + character ranged weapons in that unit |
| Immortals | Technomancer **or** Plasmancer proxy | All Immortal + that Cryptek's ranged weapons |

You may pick **different** abilities for each brick in the same Shooting phase (e.g. Warriors `[IGNORES COVER]`, Immortals `[ANTI-INFANTRY 3+]`).

### Royal Warden (Despotek proxy) - non-Conclave math

Not a Cryptek. Value is **Leader slot** so Geomancer (Support) can share the Warrior unit, plus datasheet utilities (Fall Back and shoot/charge; once-per-battle un-battleshock - **confirm sheet**). No Technosorcerous menu from the Warden alone.

---

## 3. Full shooting math

### Brick A - 10 Warriors (gauss flayer assumed) + Geomancer menu

Target: T4, 3+ save Infantry, **in cover**, you Remained Stationary, long range (no Rapid Fire).

**Pick `[IGNORES COVER]`.**

| Step | Formula | Expected |
|------|---------|----------|
| Attacks | 10 × 1 | 10 |
| Hit BS 4+ | × 1/2 | 5 hits |
| Wound S4 vs T4 | × 1/2 | 2.5 wounds |
| Save 3+ AP0 | fail × 1/3 | **≈ 0.83 unsaved (D1)** |

**Pick `[ANTI-INFANTRY 3+]`** (open ground or already ignoring cover):

| Step | Expected |
|------|----------|
| Hits | 5 |
| Wound on 3+ | 5 × 2/3 ≈ 3.33 |
| Save 3+ AP0 | ≈ **1.11 unsaved** |

**Within 12" (Rapid Fire 1):** double attacks → roughly **×2** the unsaved totals above (~1.7 or ~2.2).

`[LETHAL HITS]` on 6s to hit: each 6 skips the wound roll (still needs to beat the save). Rough add: ~10 attacks → ~1.67 rolls of 6 → those auto-wound, then same save.

### Brick B - 5 Immortals with gauss blasters + Cryptek menu

Target: same T4 3+ Infantry in cover. **Pick `[IGNORES COVER]`.**

| Step | Formula | Expected |
|------|---------|----------|
| Attacks | 5 × 2 = 10 | 10 |
| Hit BS 3+ | × 2/3 | ≈ 6.67 hits |
| Wound S5 vs T4 | S>T → 3+ → × 2/3 | ≈ 4.44 wounds |
| Save 3+ with AP-1 | save becomes 4+ → fail 1/2 | ≈ **2.22 unsaved (D1)** |

**Pick `[ANTI-INFANTRY 3+]`** instead:

| Step | Expected |
|------|----------|
| Hits | ≈ 6.67 |
| Wound on 3+ | ≈ 4.44 (same as S5 vs T4 actually) |
| vs higher T Infantry (e.g. T6) | ANTI-INFANTRY 3+ is the upgrade - S5 would wound T6 on 5+ (1/3); anti 3+ is 2/3 |

**Both bricks same phase (IGNORES COVER):** ≈ 0.83 + 2.22 ≈ **3.0 unsaved wounds** into that target before Lethal Hits / reapers / character guns.

### Scarabs

No shooting. Melee: 6 bases × 6 A = 36 attacks WS 5+ S2 AP0 - chaff clear only. Reanimation keeps them annoying.

---

## 4. Durability math - why Conclave + RP stacks

### Opponent must wipe, not chip

| Opponent plan | vs this list |
|---------------|--------------|
| Deal 3 wounds to Warriors / turn | You return avg 2 / your CP → net −1 / round; unit lives |
| Deal 10 wounds in one activation | Unit may wipe → **no reanimation** - this is the correct way to kill you |
| Split fire across Warriors + Immortals + Scarabs | Three separate D3s refill three pools - worst plan vs Necrons |

### Combined "effective wounds" over 5 rounds (no wipe, no stratagem)

| Unit | Starting W | + avg RP | Rough effective W pool |
|------|------------|----------|-------------------------|
| Warriors | 10 | +10 | ~20 |
| Immortals | 5 | +10 | ~15 |
| Scarabs | 24 | +10 | ~34 |
| **Force** | **39** | **+30** | **~69 wound-equivalents** if never wiped |

Off-turn stratagem on the Warrior brick a few times adds another ~3 avg wounds per use.

---

## 5. Turn script (500 V1)

1. **Your Command** (`08.01`–`08.05`) - +1 CP (`08.02`); **battle-shock** (`08.03`); **REANIMATE** all three units at phase end (`08.05`) — say the number out loud.
2. **Movement** (`09.02`) - Warriors/Immortals usually hold objectives (`14.02`); Scarabs **Advance** (`09.06`)/screen; use Conclave menu `[ASSAULT]` (`10.05`) if a brick must move and shoot.
3. **Shooting** (`10.02`) - Warriors: announce menu pick → resolve. Immortals: announce **different** pick if needed → resolve.
4. **Opponent Command** (`08.01`) - consider **Potentiality Syphon** (`15.01`, 1CP) on an objective Cryptek unit for off-turn D3 (+1).
5. Never leave a unit at 0 models if you can leave it at 1 — wiped units never reanimate.

---

## 6. Proxy honesty card (show opponent)

| Model on table | Playing as | Pts |
|----------------|------------|-----|
| Apprentek | Plasmancer | 55 |
| Despotek | Royal Warden | 50 |
| Technomancer | Technomancer (legal) | 80 |
| Immortal Guardians | Immortals | in the 5 |

---

## Related pages

- [`Army_List_500_V1_Conclave.md`](Army_List_500_V1_Conclave.md)
- [`Reference_Guide_250_Conclave.md`](Reference_Guide_250_Conclave.md)
- [`Reanimation_Protocols.md`](Reanimation_Protocols.md) · [`Cryptek_Conclave.md`](Cryptek_Conclave.md)
- [`Starter_Forces_500_750_1000.md`](Starter_Forces_500_750_1000.md)

---

## Change Log
- v1.2 (2026-08-20): Character note — WarCom July revive-as-solo-unit + RP excludes CHARACTER from bodyguard revive; link analysis.
- v1.1 (2026-08-19): Core rule IDs / plain-language pass (from main).
- v1.0 (2026-08-19): Initial 500 V1 Conclave reference with RP stacking math, dual-brick Conclave picks, Immortal/Warrior shooting math, off-turn stratagem model.

## Attribution
- Project: Wargame_Concierge | Maintainer: Russell Catt
- Personal teaching paraphrase; confirm stratagem/enhancement numbers on your pack.

## Rising Tide Notes
- Expected-value math only. Verify character abilities and Potentiality Syphon on your faction pack. Dated **2026-08-19**.
