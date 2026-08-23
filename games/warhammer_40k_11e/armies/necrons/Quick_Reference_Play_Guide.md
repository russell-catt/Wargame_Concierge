<!--
FILE: games/warhammer_40k_11e/armies/necrons/Quick_Reference_Play_Guide.md
VERSION: v0.5.3 (2026-08-23)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, slice S2; tomb_world_ownership sync)

DOCUMENT_TYPE: Play Aid / Laminate (exactly 2 pages)
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: Warhammer 40,000 - 11th Edition
FACTION: Necrons
REFERENCE_STATUS: Active - sources read 2026-08-16 (Core Rules, Necrons Faction Pack v1.1, MFM v1.2, Wahapedia)

SOURCES:
  - C:\Personal\40K\rules\eng_01-06_warhammer40k_new40k_core_rules.pdf
  - C:\Personal\40K\rules\eng_22-07_warhammer_40,000_faction_pack_necrons.pdf (v1.1)
  - C:\Personal\40K\rules\Warhammer 40,000_ Munitorum Field Manual.pdf (v1.2)
  - https://wahapedia.ru/wh40k10ed/factions/necrons (retrieved 2026-08-16)
  - games/warhammer_40k_11e/armies/necrons/Owned_Models_Inventory.md (ownership, corrected 2026-08-16)

PURPOSE:
  Table-side laminate. Two printed pages, page break marked with an HTML
  comment. Everything a Necron beginner needs mid-game and nothing else.

PRINT_NOTE:
  Exactly two pages by design. Do not add sections - replace instead. No
  shopping content, no lore, no datasheet statlines.

CHANGE_LOG:
  - v0.5.3 (2026-08-23): Event feedback — Objectives/OC (**14.01**/**14.02**) and Leader+Support deploy (**19.01**/**03.03**) pointers.
  - v1.2 (2026-08-16): Page 2 starter snapshot rebuilt around the owned, game-ready Kill Team: Tomb World force (Geomancer + Warriors + Tomb Crawlers = 240 pts). Sprue extras (2nd Warriors, 2nd Scarabs, Immortals) tagged build-before-play, not blockers (slice S2, `tomb_world_ownership`).
  - v1.1 (2026-08-16): Starter snapshot ownership re-verified against FOUNDATION (build-before-play + Hierotek TBD). *(Described Tomb World as not owned - superseded by v1.2.)*
  - v1.0 (2026-08-16): Initial two-page laminate (slice S4).

ATTRIBUTION:
  - Project: Wargame_Concierge | Maintainer: Russell Catt
  - Warhammer 40,000 is a trademark of Games Workshop Limited. Personal
    teaching paraphrase; no publisher text or statlines reproduced.

RISING_TIDE_NOTES:
  - Follows Rising Tide documentation standards. The Change Log and Attribution
    footer is carried here in the header comment so the printed output stays
    exactly two pages.

UPDATE_TRIGGER:
  Update on any Core Rules, faction pack, or Munitorum Field Manual revision
  that changes a phase, the army rule, the Power Matrix, or the starter lists.
-->

# NECRONS - TABLE REFERENCE | Page 1 of 2

## YOUR TURN, IN ORDER

| # | Phase | Do this |
|---|-------|---------|
| 0 | **Start of turn** (`07.02`) | Resolve "start of your turn" triggers |
| 1 | **Command** (`08.01`–`08.05`) | Both players +1 CP (`08.02`). **Battle-shock** (`08.03`, `01.07`) — roll 2D6 vs Leadership for shaken or half-strength units. **END OF PHASE: REANIMATE** (`08.05`) |
| 2 | **Movement** (`09.01`–`09.03`) | Select **every** unit and give it a move type. Reserves arrive. Check **coherency** (`03.03`) |
| 3 | **Shooting** (`10.01`–`10.03`) | Pick unit, pick shooting type (`10.04`–`10.07`), pick targets (`06.01` visibility), resolve attacks (`05.01`–`05.04`) |
| 4 | **Charge** (`11.01`–`11.03`) | Within 12", not engaged, did not Advance / Fall Back. Roll 2D6. Charging unit gets Fights First |
| 5 | **Fight** (`12.01`–`12.09`) | **Pile in** 3" (`12.02`) — **fight** (`12.04`, Fights First first) — **consolidate** 3" (`12.07`) |
| 6 | **End of turn** | End-of-turn triggers, score mission VP, fix coherency |

**Move types:** Remain Stationary (`09.04`, keeps `[HEAVY]`) | Normal (`09.05`, M") | Advance (`09.06`, M + D6, no charge, `[ASSAULT]` only) | Fall Back (`09.07`, no shoot / charge) | Disembark | Ingress from reserves.

**Shooting types:** Normal (`10.04`) | Assault (`10.05`, advanced) | Close-quarters (`10.06`, engaged) | Indirect (`10.07`, unseen target, big penalty, gives cover `13.08`).

---

## ARMY RULE - REANIMATION PROTOCOLS

> **End of YOUR Command phase** (`08.05`). Every unit on the battlefield. Roll D3 wounds. Free. *(Necron army rule — see faction pack.)*

Spend each reanimated wound in this order:

1. **Heal** one lost wound on a surviving wounded model.
2. Only when all survivors are full: **return one destroyed model with 1 wound**.
3. At Starting Strength and full wounds: nothing further happens.

| It does | It does not |
|---------|-------------|
| Fire every one of your turns, for free | Bring back a **wiped-out** unit - ever |
| Heal before it rebuilds | Fire on your opponent's turn |
| Stack with Reanimator / Resurrection Orb (D6) / Macrocytes | Let you choose which model returns |

**Consequence:** keep the last model alive. Stand on the objective. Chip damage against you is wasted damage.

---

## DETACHMENT - CANOPTEK COURT: POWER MATRIX

**Which ground is yours** (re-check at the **start of every phase** (`07.02`)):

| Region | In your Matrix when |
|--------|---------------------|
| Your deployment zone | **Always** |
| No Man's Land | You control **half or more** of its objective markers (`14.02`) |
| Enemy deployment zone | You control **half or more** of its objective markers (`14.02`) |

*No objective markers in a region = that region is never yours.*

**What you get** - **CRYPTEK** and **CANOPTEK** units only:

- Anywhere: **re-roll hit rolls of 1**.
- **Wholly within** the Matrix: **re-roll the hit roll** (any miss). One model outside = weaker version.

*Warriors, Immortals and Lychguard get nothing from this rule. They hold ground so the constructs benefit.*

**Cryptek Conclave instead?** Each time a **Cryptek unit** shoots in the **Shooting phase** (`10.02`), pick one: `[ANTI-INFANTRY 3+]` `[ANTI-MOUNTED 4+]` `[ASSAULT]` `[HEAVY]` `[IGNORES COVER]`. Attach the Cryptek (`19.01`) so the whole squad counts.

---

## COMBAT SEQUENCE

1. **Hit** (`05.01`) - D6 per attack vs BS (shooting) or WS (melee). Unmodified 1 always fails; unmodified 6 is a critical hit.
2. **Wound** (`05.02`) - D6 per hit, S vs T. Unmodified 1 always fails; unmodified 6 is a critical wound.
3. **Save** (`05.03`) - defender rolls: armour save modified by AP, **or** invulnerable save ignoring AP. Unmodified 1 fails.
4. **Damage** (`05.04`) - each unsaved attack costs D wounds. Excess damage is lost, it does not spill to the next model.
5. **Allocation** - defender chooses the order; already-wounded group goes first; **characters cannot be put in front**.
6. **Cover in 11e** (`13.08`) worsens the attacker's **Ballistic Skill by 1** - it is not a save bonus.

<!-- pagebreak -->

# NECRONS - TABLE REFERENCE | Page 2 of 2

## STARTER SNAPSHOT - Kill Team: Tomb World force (owned, game-ready)

| Unit | Models | Pts | State |
|------|--------|-----|-------|
| Cryptek Geomancer | 1 | **75** | **OWNED** - Tomb World |
| Necron Warriors | 10 | **80** | **OWNED** - Tomb World |
| Canoptek Tomb Crawlers | 2 | **50** | **OWNED** - Tomb World (MFM v1.2) |
| Canoptek Macrocytes | 5 | **70** | **OWNED** (MFM v1.2) |
| Canoptek Scarab Swarms | 3 / 6 | **40 / 80** | **OWNED** (build 2nd 3 before play) |
| Immortals / Technomancer | 5 / 1 | **70 / 80** | Immortals sprue; Technomancer Hierotek **OWNED** |
| Plasmancer (Support) | 1 | **55** | Not owned — buy / Apprentek proxy |

**250 tonight:** Geomancer 75 + Warriors 80 + Crawlers 50 (+ Scarabs 40) = **245**. **Attach Geomancer to Warriors** (`19.01`).
**500 Court / Conclave:** see army READMEs — Court wants Macrocytes/Scarabs/Wraiths; Conclave adds Immortals + Plasmancer.

---

## DO / DON'T

| | |
|---|---|
| **DO** stand on the objective and take the hit - you reanimate, they wasted a turn | **DON'T** pull a damaged unit back out of scoring range |
| **DO** protect the **last model** of a unit - one model reanimates, zero never returns | **DON'T** let a unit get wiped when a 2" move would have hidden a body |
| **DO** count No Man's Land objectives at the **start** of each phase (`07.02`) | **DON'T** assume the Matrix from last phase still applies |
| **DO** attach characters during pre-game setup (`19.01`) — Leader **and** Support may join the same bodyguard | **DON'T** plan to attach mid-game - you cannot |
| **DO** deploy an attached unit as **one coherency blob** (`03.03`) | **DON'T** set Leader/Support up as separate units from their bodyguard |
| **DO** consolidate 3" onto an objective when there is nothing to fight (`12.07`) | **DON'T** skip pile-in and consolidation, they are free movement |
| **DO** re-check control at the end of every phase (`14.02`) - it flips constantly | **DON'T** count a battle-shocked unit's OC - it is zero (`08.03`) |
| **DO** pick one ability per Cryptek unit each **Shooting phase** (`10.02`) and say it out loud | **DON'T** forget Command phase reanimation (`08.05`). Put a token on the table |

---

## OBJECTIVES & CONTROL (Ch. 14)

- **Terrain objectives (`14.01`):** the mission's terrain **footprint** *is* the objective. A model counts while it is **inside that terrain area**.
- **Level of control (`14.02`):** at end of **every phase and turn**, **sum OC** of your models in range. Higher total controls; **tie = nobody**.
- **Score VP** when the **mission card** says (often end of turn) for objectives you control — control first, then score.
- Battle-shocked units contribute **0 OC** (`08.03`).

## ATTACH & DEPLOY (Ch. 19)

- **Form (`19.01`):** before battle, each Leader/Support attaches to one eligible bodyguard. Normally **one Leader + one Support** per bodyguard → **one unit**.
- **250 Conclave:** Geomancer (**Support**) + Warriors. At 500+, add a **Leader** (e.g. Royal Warden) to the **same** brick if the datasheet allows.
- **Deploy (`03.03`):** set up **all** attached models together in coherency (2"/9" horizontal tests). Cannot attach mid-game.

---

## KEYWORD MINI-STRIP

`[ASSAULT]` fire after advancing • `[HEAVY]` +1 to hit if unengaged and nothing moved over 3" • `[RAPID FIRE X]` +X attacks within half range • `[LETHAL HITS]` critical hit may skip the wound roll (optional) • `[SUSTAINED HITS X]` critical hit = +X hits • `[DEVASTATING WOUNDS]` critical wound = mortal wounds equal to Damage • `[IGNORES COVER]` target gets no cover benefit • `[TWIN-LINKED]` re-roll the **wound** roll • `[ANTI-X N+]` wound roll of N+ against keyword X is critical • `[BLAST]` +1 attack per five models in the target, never against an engaged unit • `[CLEAVE X]` Blast for melee: +X dice per five models, all attacks at one target • `[PRECISION]` can pick out an attached character • `[HAZARDOUS]` 1-2 on the hazard die costs you a mortal wound • `[INDIRECT FIRE]` shoot unseen, heavy penalty, gives cover • `[MELTA X]` +X Damage within half range • `[CLOSE-QUARTERS]` / `[PISTOL]` identical - shoot while engaged.

**OC** (`14.02`) = sum of OC on models **in the objective's terrain footprint** (`14.01`) • **InSv** invulnerable save (ignores AP) • **Ld** rolled on 2D6 against a target such as 7+ • **Engagement Range** (`03.04`) 2" horizontally, 5" vertically • **Coherency** (`03.03`) within 2" of one model and 9" of all • **Leader / Support** (`19.01`) attach pre-game; deploy as one unit.

---

## PRE-GAME CHECKLIST

- [ ] Terrain on the table **before** deployment. Agree what is Light / Dense / Obscuring.
- [ ] Objective **terrain footprints** agreed (`14.01`) — note which are in No Man's Land.
- [ ] Detachment named. Enhancements written down. **Leader/Support attached to bodyguards now** (`19.01`).
- [ ] Attached units will deploy in **coherency** (`03.03`) as one blob.
- [ ] Reserves declared (max 50% of your points).
- [ ] Reanimation token on the table edge.

## END-OF-TURN CHECKLIST

- [ ] Score your mission VP.
- [ ] Fix coherency - out-of-coherency units lose models.
- [ ] Note which objectives you hold going into your opponent's turn.
- [ ] Did you reanimate this turn? If not, it is gone - do not take it later.

---

*Verify vs Munitorum / faction pack - patches happen | 2026-08-16*
