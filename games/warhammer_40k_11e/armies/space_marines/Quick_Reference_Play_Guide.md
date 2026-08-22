<!--
FILE: games/warhammer_40k_11e/armies/space_marines/Quick_Reference_Play_Guide.md
VERSION: v0.6.0 (2026-08-21)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, slice S5)

DOCUMENT_TYPE: Play Aid / Laminate (exactly 2 pages)
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: Warhammer 40,000 - 11th Edition
FACTION: Space Marines
REFERENCE_STATUS: Active - sources read 2026-08-16; starter snapshot synced to owned Blood Ravens paths 2026-08-21

SOURCES:
  - C:\Personal\40K\rules\eng_01-06_warhammer40k_new40k_core_rules.pdf
  - C:\Personal\40K\rules\eng_22-07_warhammer_40,000_faction_pack_space_marines.pdf (v1.1)
  - C:\Personal\40K\rules\Warhammer 40,000_ Munitorum Field Manual_Marines.pdf (v1.2)
  - https://www.40k.app/factions/space-marines/detachments/gladius-task-force (retrieved 2026-08-16)
  - games/warhammer_40k_11e/armies/space_marines/Owned_Models_Inventory.md (photo ID 2026-08-21)

PURPOSE:
  Table-side laminate. Two printed pages, page break marked with an HTML
  comment. Everything a Space Marine beginner needs mid-game and nothing else.

PRINT_NOTE:
  Exactly two pages by design. Do not add sections - replace instead. No
  shopping content, no lore, no datasheet statlines.

CHANGE_LOG:
  - v0.6.0 (2026-08-21): Starter snapshot → owned Blood Ravens ladder (250–1000); ownership audited.
  - v1.0 (2026-08-16): Initial two-page laminate (slice S5).

ATTRIBUTION:
  - Project: Wargame_Concierge | Maintainer: Russell Catt
  - Warhammer 40,000 is a trademark of Games Workshop Limited. Personal
    teaching paraphrase; no publisher text or statlines reproduced.

RISING_TIDE_NOTES:
  - Follows Rising Tide documentation standards. The Change Log and Attribution
    footer is carried here in the header comment so the printed output stays
    exactly two pages, matching the Necron laminate.

UPDATE_TRIGGER:
  Update on any Core Rules, faction pack, or Munitorum Field Manual revision
  that changes a phase, the army rule, a Combat Doctrine, or the starter lists.
-->

# SPACE MARINES - TABLE REFERENCE | Page 1 of 2

## YOUR TURN, IN ORDER

| # | Phase | Do this |
|---|-------|---------|
| 0 | **Start of turn** | Resolve "start of your turn" triggers |
| 1 | **Command** | Both players +1CP. **PICK YOUR OATH TARGET.** **DECIDE: spend a doctrine?** Battle-shock rolls (2D6 vs Ld) for units battle-shocked or at/below half strength |
| 2 | **Movement** | Select **every** unit and give it a move type. Reserves arrive. Check coherency |
| 3 | **Shooting** | Pick unit, pick shooting type, pick targets, resolve attacks. **Shoot the oath target first** |
| 4 | **Charge** | Within 12", not engaged, did not Advance / Fall Back. Roll 2D6. Charging unit gets Fights First |
| 5 | **Fight** | Pile in 3" - fight (Fights First units first, then alternate) - consolidate 3" |
| 6 | **End of turn** | End-of-turn triggers, score mission VP, fix coherency |

**Move types:** Remain Stationary (keeps `[HEAVY]`) | Normal (M") | Advance (M + D6, no charge, `[ASSAULT]` only) | Fall Back (no shoot / charge) | Disembark | Ingress from reserves.

**Shooting types:** Normal | Assault (advanced) | Close-quarters (engaged) | Indirect (unseen target, big penalty, gives cover).

---

## ARMY RULE - OATH OF MOMENT

> **Start of YOUR Command phase. Name ONE enemy unit. Free. Lasts until your next Command phase.**

Against that unit, every model in your army with the ability gets:

1. **Re-roll the Hit roll** - any miss, shooting and melee.
2. **+1 to the Wound roll** - **only if** you are using a Codex: Space Marines Detachment **and** your army has no Blood Angels, Dark Angels, Deathwatch or Space Wolves units. One such model costs you this all game.

| It does | It does not |
|---------|-------------|
| Let you name a unit **inside a transport** | Require line of sight, range, or any intent to shoot |
| Let you name a unit still **in Reserves** | Carry over if you forget - a skipped pick is gone |
| Cover your opponent's turn too (melee, overwatch) | Apply to any unit except the one you named |

**Consequence:** concentrate. Kill the oath target first, then spill over. Splitting fire throws the army rule away.

---

## DETACHMENT - GLADIUS TASK FORCE: COMBAT DOCTRINES

**Start of your Command phase, optional. Applies to your WHOLE army. EACH ONE ONCE PER BATTLE.**

| Doctrine | Permits | Spend it when |
|----------|---------|---------------|
| **Devastator** | Shoot in a turn you **Advanced** | Round 1-2. Objectives are further than your Move and you cannot afford a silent turn |
| **Tactical** | Shoot **and** charge in a turn you **Fell Back** | The turn something you need gets stuck in a fight it cannot win. Do not hoard it |
| **Assault** | Charge in a turn you **Advanced** | The turn you commit. Huge threat range, but two dice rolls stacked |

**Spent:** ☐ Devastator ☐ Tactical ☐ Assault - tick as you burn them.

**Skipping a round is allowed and often right.** You do not have to pick one.

**Escape hatch:** **Adaptive Strategy** (1CP, Command phase) puts **one unit** into any doctrine, **even one already used**. Works with no doctrine active. **Storm of Fire** (1CP, `[IGNORES COVER]`, +1 AP under Devastator) · **Honour the Chapter** (1CP, `[LANCE]`, +1 AP under Assault) · **Squad Tactics** (1CP, reactive D6" move, full 6" under Tactical, within **8"**) · **Armour of Contempt** (1CP, worsen incoming AP by 1) · **Only in Death Does Duty End** (2CP, slain models still swing).

---

## COMBAT SEQUENCE

1. **Hit** - D6 per attack vs BS (shooting) or WS (melee). Unmodified 1 always fails; unmodified 6 is a critical hit. **Oath target: re-roll misses.**
2. **Wound** - D6 per hit, S vs T. Unmodified 1 always fails; unmodified 6 is a critical wound. **Oath target: +1, if your army qualifies.**
3. **Save** - defender rolls: armour save modified by AP, **or** invulnerable save ignoring AP. Unmodified 1 fails.
4. **Damage** - each unsaved attack costs D wounds. Excess damage is lost, it does not spill to the next model.
5. **Allocation** - defender chooses the order; already-wounded group goes first; **characters cannot be put in front**.
6. **Cover in 11e** worsens the attacker's **Ballistic Skill by 1** - it is not a save bonus.

<!-- pagebreak -->

# SPACE MARINES - TABLE REFERENCE | Page 2 of 2

## STARTER SNAPSHOT - owned Blood Ravens (MFM Marines v1.2)

**Paint:** Blood Ravens · **Rules:** Codex SM + Gladius. Detail: [`Owned_Models_Inventory.md`](Owned_Models_Inventory.md). Chaplain claw = **Storm Shield** in game.

| Unit | Models | Pts | Used in |
|------|--------|-----|---------|
| Chaplain in Terminator Armour | 1 | **75** | 250 · 500v · 750 · 1000 |
| Captain (Leader) | 1 | **80** | 250 · 500 · 750 · 1000 |
| The Honour Vehement | - | **15** | 750 · 1000 |
| Techmarine | 1 | **55** | 1000 |
| Tactical Squad | 10 | **140** | all BR paths (Tac1 has flamer) |
| Devastator Squad | 5 / 10 | **120 / 200** | 500+ (HB / MM / PC / LC / meltagun); **10** by reassigning Tactical bolters |
| Terminator Squad | 5 | **160** | 250 · 500 · 750×2 · 1000×2 |
| Whirlwind (1st) | 1 | **175** | 1000 |

**250 BR-1:** Chaplain 75 + Terminators 160 = **235**.
**250 BR-2:** Captain 80 + Tactical 140 = **220**.
**500:** Captain 80 + Tactical 140 + Devastators 120 + Terminators 160 = **500**.
**750:** + Chaplain 75 + 2nd Terminators 160 + Honour Vehement 15 = **750**.
**1000:** 750 core without HV + Techmarine 55 + Whirlwind 175 + HV 15 = **980**.

**Enhancements:** The Honour Vehement 15 · Adept of the Codex 20 · Artificer Armour 20 · Fire Discipline 25.
**Legends (friendly only):** Bike Squad · Attack Bike (gunner MM or HB).

---

## DO / DON'T

| | |
|---|---|
| **DO** pick the oath target before you move anything, and put a token on it | **DON'T** oath the scariest unit if you have no way to attack it this turn |
| **DO** shoot the oath target with everything before spilling over | **DON'T** split fire across four targets - that throws the army rule away |
| **DO** tick the doctrine box the moment you spend one | **DON'T** assume you can re-use a doctrine. Each is **once per battle** |
| **DO** skip a doctrine on a round that does not need one | **DON'T** hoard Tactical Doctrine while a squad sits stuck in combat |
| **DO** remember Adaptive Strategy (1CP) can re-grant a spent doctrine to one unit | **DON'T** forget it works even with no doctrine active |
| **DO** attach characters during pre-game setup | **DON'T** plan to attach mid-game - you cannot |
| **DO** consolidate 3" onto an objective when there is nothing to fight | **DON'T** skip pile-in and consolidation, they are free movement |
| **DO** check control at the end of every phase - it flips constantly | **DON'T** count a battle-shocked unit's OC - it is zero |

---

## KEYWORD MINI-STRIP

`[ASSAULT]` fire after advancing · `[HEAVY]` +1 to hit if unengaged and nothing moved over 3" · `[RAPID FIRE X]` +X attacks within half range · `[LETHAL HITS]` critical hit may skip the wound roll (optional) · `[SUSTAINED HITS X]` critical hit = +X hits · `[DEVASTATING WOUNDS]` critical wound = mortal wounds equal to Damage · `[IGNORES COVER]` target gets no cover benefit · `[TWIN-LINKED]` re-roll the **wound** roll · `[ANTI-X N+]` wound roll of N+ against keyword X is critical · `[LANCE]` +1 to wound if your unit charged this turn · `[BLAST]` +1 attack per five models in the target, never against an engaged unit · `[CLEAVE X]` Blast for melee: +X dice per five models, all attacks at one target · `[PRECISION]` can pick out an attached character · `[HAZARDOUS]` 1-2 on the hazard die costs you a mortal wound · `[MELTA X]` +X Damage within half range · `[TORRENT]` hits automatically · `[CLOSE-QUARTERS]` / `[PISTOL]` identical - shoot while engaged.

**OC** objective control · **InSv** invulnerable save (ignores AP) · **Ld** rolled on 2D6 against a target such as 7+ · **Leader** character that attaches to a squad · **Support** second attachment slot; can attach on its own · **Engagement Range** 2" horizontally, 5" vertically · **Coherency** within 2" of one model and 9" of all · **Objective marker** 3" horizontally, 5" vertically.

---

## PRE-GAME CHECKLIST

- [ ] Terrain on the table **before** deployment. Agree what is Light / Dense / Obscuring.
- [ ] Objective markers placed and counted - note which are in No Man's Land.
- [ ] Detachment named. Enhancement written next to its bearer. **Characters attached to squads now.**
- [ ] Three doctrine tick-boxes written at the top of your army list.
- [ ] Reserves declared (max 50% of your points).
- [ ] Oath token ready at the table edge.

## END-OF-TURN CHECKLIST

- [ ] Score your mission VP.
- [ ] Fix coherency - out-of-coherency units lose models.
- [ ] Note which objectives you hold going into your opponent's turn.
- [ ] Did you pick an oath target this turn? If not, it is gone - do not take it later.

---

*Verify vs Munitorum / faction pack - patches happen | 2026-08-16*
