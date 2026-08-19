<!--
FILE: games/warhammer_40k_11e/armies/necrons/Reference_Guide_250_Conclave.md
VERSION: v1.1 (2026-08-19)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (cloud agent)

DOCUMENT_TYPE: Play Reference / Math Guide
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: Warhammer 40,000 - 11th Edition
FACTION: Necrons
DETACHMENT: Cryptek Conclave
REFERENCE_STATUS: Active - companion to Army_List_250_Conclave.md. Rules paraphrased from Reanimation_Protocols.md and Cryptek_Conclave.md (faction pack v1.1 / Wahapedia cross-check 2026-08-16). Attack math uses local Warrior research profiles.

SOURCES:
  - games/warhammer_40k_11e/armies/necrons/Army_List_250_Conclave.md
  - games/warhammer_40k_11e/armies/necrons/Reanimation_Protocols.md
  - games/warhammer_40k_11e/armies/necrons/Cryptek_Conclave.md
  - games/warhammer_40k_11e/armies/necrons/units/research/Necron-Warriors.md
  - games/warhammer_40k_11e/rules/Key_Concepts.md

PURPOSE:
  Table-side explanation of Reanimation Protocols and Cryptek Conclave buffs
  for the 250 list, with full worked math.

PRIMARY_AUDIENCE:
  - First games with Army_List_250_Conclave.md

UPDATE_TRIGGER:
  Update when the army rule, Conclave menu, or Warrior profiles change.
-->

# Reference guide - 250 pts Cryptek Conclave

Companion to [`Army_List_250_Conclave.md`](Army_List_250_Conclave.md).

**List in one line:** Geomancer (Atomic Disintegrators) + 10 Warriors + 2 Tomb Crawlers + 3 Scarabs = **255** *(245 without enhancement)*. Geomancer attaches to Warriors.

---

## 1. Reanimation Protocols - full math

### When and how much

| Step | Rule |
|------|------|
| Timing | **End of your Command phase** (`08.05`) only (not the opponent's, unless a **stratagem** (`15.01`) says otherwise) |
| Who | Every eligible Necron unit still on the battlefield |
| Amount | Roll **D3** → that many wounds return to that unit |
| Cost | Free |

**D3 average:** (1+2+3)/3 = **2.0 wounds per unit per your Command phase**.

### Spend order (mandatory)

For each reanimated wound, in order:

1. **Heal** one lost wound on a surviving wounded model.
2. If every survivor is at full wounds: **return one destroyed model with 1 wound remaining**.
3. If the unit is already at Starting Strength and full wounds: that wound is wasted.

### Worked examples (10 Warriors, Starting Strength 10)

| Situation at end of your Command | D3 roll | What happens |
|----------------------------------|---------|--------------|
| 10 models, all full | any | Nothing (already full) |
| 10 models, three of them missing 1 wound each | 2 | Heal 2 of the 3 wounded models (1 still wounded) |
| 7 models left (3 destroyed), all survivors full | 2 | Return **2** Warriors at **1W** each → 9 models (two on 1W) |
| 7 models, one survivor on 0 wounds remaining wait - if wounded: 6 full + 1 on 0? | 2 | First heal the wounded to full (1 wound), then return 1 model at 1W |
| **0 models (unit wiped)** | — | **No reanimation.** Unit is gone |

### Expected durability over a game

Assume the Warrior brick stays on the board for **5 of your Command phases** and is never wiped:

| Metric | Math |
|--------|------|
| Wounds returned (average) | 5 × 2.0 = **10 wounds** |
| Equivalent full Warriors | ~**10 models worth** of healed/returned wounds over the game |
| If you forget reanimation once | −D3 ≈ **−2 wounds** that round - real loss |

**Their Number is Legion** (Warrior datasheet): may change how returns work - **read your sheet** and apply on top of this order. Do not skip the heal-first rule unless the datasheet explicitly overrides it.

### Tomb Crawlers

Same army rule: end of your Command phase, D3 wounds on that unit. They are **not** a Cryptek unit, so Conclave does not change their guns - only their survival.

---

## 2. Cryptek Conclave - Technosorcerous Augmentations

### Always-on (Cryptek models)

Ranged weapons on **Cryptek** models in your army gain `[ASSAULT]` (may shoot after Advance).

### Per shooting selection (the skill)

When a **Cryptek unit** is selected to shoot in your **Shooting phase** (`10.02`), choose **one**:

| Menu pick | Effect (plain) |
|-----------|----------------|
| `[ANTI-INFANTRY 3+]` | Wound Infantry on 3+ (ignore normal S vs T for that test) |
| `[ANTI-MOUNTED 4+]` | Wound Mounted on 4+ |
| `[ASSAULT]` | Unit's ranged weapons can shoot after Advance |
| `[HEAVY]` (`24.16`) | Bonus to hit if the unit **Remained Stationary** (`09.04`) *(confirm exact modifier on your pack)* |
| `[IGNORES COVER]` | Target does not get **Benefit of Cover** (`13.08`) against these attacks |

**Atomic Disintegrators (10 pts on Geomancer):** adds anti-**Monster** / anti-**Vehicle** options to that menu (exact keywords on your enhancement card - typically wounding those keywords on a set number).

**Keyword trick:** Geomancer attached to Warriors → the **whole attached unit** is a Cryptek unit → the menu applies to **all ten Warriors' guns**, not just the Geomancer.

Tomb Crawlers: **no menu**.

---

## 3. Full shooting math - Warriors + Geomancer

Profiles from local research (`Necron-Warriors.md`). Confirm `[HEAVY]` bonus and cover rules on your core rules / pack.

### Setup A - 10× gauss flayer, Remained Stationary, target T4 3+ Infantry **in cover**

**Pick `[IGNORES COVER]`** (beginner default in terrain).

| Step | Calculation | Result |
|------|-------------|--------|
| Attacks | 10 models × 1 A | **10** attacks (24" range) |
| Rapid Fire | If within 12": +1 A each → | **20** attacks |
| Hit (BS 4+) | Need 4+ on D6 → 1/2 hit | 10 × 0.5 = **5 hits** (or 20 × 0.5 = **10** if RF) |
| `[LETHAL HITS]` | 6s to hit auto-wound - already counted in hits; those skip wound roll | *(track 6s separately if you want precision)* |
| Wound vs T4 (S4) | Need 4+ → 1/2 | 5 × 0.5 = **2.5** wounds (non-lethal path) |
| Save 3+, AP 0, no cover | Need 3+ → 2/3 saved → 1/3 fail | 2.5 × 1/3 ≈ **0.83** unsaved |
| Damage | D1 each | ≈ **0.8 dead Warriors-equivalent** per volley at long range |

**If you had picked `[ANTI-INFANTRY 3+]` instead** (same target, ignore cover already via menu or open ground):

| Step | Math |
|------|------|
| Hits (no RF) | 5 expected |
| Wound on 3+ | 5 × 2/3 ≈ **3.33** wounds |
| Save 3+ AP0 | 3.33 × 1/3 ≈ **1.1** unsaved |

**Within Rapid Fire range + ANTI-INFANTRY 3+:** ~**2.2** unsaved wounds expected before Lethal Hits on 6s.

### Setup B - same guns, you **Advanced**

Without Conclave you often cannot shoot. With Conclave:

- Pick `[ASSAULT]` on the menu **or** rely on Geomancer's always-on `[ASSAULT]` for the character only - **for the Warriors you need the menu `[ASSAULT]`** (or they already have it from the pick).
- Then resolve as Setup A (usually worse target priority because you moved).

### Setup C - tough target (Vehicle / Monster)

Pick the **Atomic Disintegrators** anti-Vehicle or anti-Monster menu option (confirm wound number on the enhancement). Then:

| Step | Note |
|------|------|
| Hit | Still BS 4+ (or `[HEAVY]` if stationary) |
| Wound | Use the anti-X value from the enhancement instead of S4 vs high T |
| Save | AP 0 flayers bounce hard - this pick is for *wounding*, not for cracking armour; consider focusing Crawlers' better guns if their datasheet has higher AP |

---

## 4. Turn script (250)

1. **Command** (`08.01`–`08.05`) - +1 CP (`08.02`); **battle-shock** (`08.03`) if needed; **REANIMATE** Warriors (D3) and Crawlers (D3) at phase end (`08.05`).
2. **Movement** (`09.02`) - Warriors usually **Remain Stationary** (`09.04`) on home objective (`14.02`); Crawlers push mid.
3. **Shooting** (`10.02`) - Select Warriors (Cryptek unit): pick menu ability out loud; resolve flayers/reapers; then shoot Crawlers.
4. **Charge / Fight** (`11.02`, `12.04`) - only if it helps; this list wins by not dying.
5. Opponent's turn - remember: **no army-wide reanimation** until your next Command (`08.05`) unless you spend **Potentiality Syphon** (`15.01`) — see faction pack; more relevant at 500.

---

## Related pages

- [`Army_List_250_Conclave.md`](Army_List_250_Conclave.md)
- [`Reanimation_Protocols.md`](Reanimation_Protocols.md) · [`Cryptek_Conclave.md`](Cryptek_Conclave.md)
- [`Reference_Guide_500_V1_Conclave.md`](Reference_Guide_500_V1_Conclave.md)

---

## Change Log
- v1.0 (2026-08-19): Initial 250 Conclave reference with RP and shooting math.

## Attribution
- Project: Wargame_Concierge | Maintainer: Russell Catt
- Personal teaching paraphrase; verify modifiers on your core rules and datasheets.

## Rising Tide Notes
- Math uses expected values (averages). Dice vary. Dated **2026-08-19**.
