<!--
FILE: games/warhammer_40k_11e/rules/Key_Concepts.md
VERSION: v0.5.1 (2026-08-18)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, slice S3)

DOCUMENT_TYPE: Teaching Guide / Core Mechanics
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: Warhammer 40,000 - 11th Edition
REFERENCE_STATUS: Active - draft, spot-checked against owned Core Rules PDF 2026-08-16

SOURCES:
  - C:\Personal\40K\rules\eng_01-06_warhammer40k_new40k_core_rules.pdf (read 2026-08-16)
  - C:\Personal\40K\rules\eng_22-07_warhammer_40,000_faction_pack_necrons.pdf (v1.1, read 2026-08-16)
  - reference/Source_Library.md
  - KB/concepts/objective_control.md

PURPOSE:
  Explain the handful of mechanics that everything else in the game is built
  from: the attack sequence, saves and damage, objective control, battle-shock,
  and attached units.

PRIMARY_AUDIENCE:
  - A beginner who knows the turn order and now needs to know how dice resolve
  - Any later slice needing shared mechanical vocabulary

KEY_SECTIONS_EXPECTED:
  - Reading a datasheet
  - The attack sequence
  - Saves and damage
  - Mortal wounds and hazards
  - Objective Control
  - Battle-shock
  - Leaders and attached units
  - Command Points

UPDATE_TRIGGER:
  Update when a Core Rules version, universal rules update, or faction pack
  changes attack resolution, cover, objective control, or attached units.
-->

# Key Concepts - the mechanics everything else sits on

Five or six ideas do almost all the work in Warhammer 40,000. Learn these and most datasheet text becomes readable.

Checked against the owned Core Rules PDF on **2026-08-16**. Numbered IDs point at [`Core_Rules_Quotes.md`](Core_Rules_Quotes.md).

**Contradiction check (2026-08-18):** attack sequence (**05.01–05.04**), cover as a BS penalty (**13.08**), `[HEAVY]` as +1 to the hit roll (**24.16**), and OC re-check (**14.02**) match the 2026-08-16 paraphrase. No rewrite.

---

## Reading a datasheet

Every unit has a **datasheet**: its profile, weapons, abilities, and keywords. The profile characteristics are:

| Stat | Name | What it means |
|------|------|---------------|
| **M** | Move | How far the model moves, in inches |
| **T** | Toughness | How hard it is to wound |
| **Sv** | Save | Armour save, rolled as a dice result (e.g. 3+) |
| **InSv** | Invulnerable Save | A second save that ignores weapon AP. Not every model has one |
| **W** | Wounds | Damage it can absorb before it is destroyed |
| **Ld** | Leadership | Rolled against for battle-shock, as a dice result (e.g. 7+) |
| **OC** | Objective Control | How strongly it holds ground |

Weapons carry: **Range**, **A** (attacks), **BS/WS** (accuracy in shooting / melee), **S** (strength), **AP** (armour penetration, a negative modifier to the target's save), and **D** (damage per successful attack). Weapon abilities appear in square brackets, e.g. `[RAPID FIRE 1]`.

Keywords are the plumbing. A rule that says "INFANTRY units" applies to exactly the units with that keyword, and nothing else.

> **We never reproduce datasheet statlines in this repository.** Look them up in your faction pack or the Warhammer 40,000 app.

---

## The attack sequence

Shooting and fighting both funnel into the same four steps. Everything you will ever read about weapon abilities is a modification of one of these.

### Before rolling: select and target

1. **Select weapons.** Shooting: any ranged weapons the model has. Fighting: exactly one melee weapon per model.
2. **Select targets.** Shooting targets must be visible, in range, and unengaged. Melee targets must be units you are engaged with.
3. **Gather attack dice.** One D6 per attack, based on the weapon's A characteristic. Weapons making identical attacks are rolled together.

### The four rolls

**1. Hit roll** (**05.01**). Roll a D6 per attack dice. Meet or beat the weapon's BS (shooting) or WS (melee) and it hits.

- An unmodified **1 always fails**.
- An unmodified **6 is a critical hit** - still a hit, and it also switches on abilities like `[LETHAL HITS]` and `[SUSTAINED HITS]`.

**2. Wound roll** (**05.02**). Roll a D6 per hit, comparing the attack's Strength (S) to the target's Toughness (T):

| S versus T | You need |
|------------|----------|
| S is at least double T | The easiest roll |
| S is greater than T | Easier |
| S equals T | Even |
| S is less than T | Harder |
| S is half T or less | The hardest roll |

- An unmodified **1 always fails**; an unmodified **6 is a critical wound**, which switches on abilities like `[DEVASTATING WOUNDS]` and `[ANTI-X]`.

**3. Save roll** (**05.03**). Now the **defender** rolls, one D6 per wound. They pick between two options per attack:

- **Armour save:** modify the roll by the weapon's AP, then compare to Sv. AP -1 turns a rolled 3 into a 2.
- **Invulnerable save:** compare the unmodified roll to InSv. AP does nothing to it.

An unmodified **1 always fails**. A failed save means the attack gets through.

**4. Inflict damage** (**05.04**). Each attack that gets through costs the target model wounds equal to the weapon's D characteristic. At 0 wounds the model is destroyed. Excess damage from a single attack is lost - it does not spill onto the next model.

### Who takes the hits

The defender divides the unit into **allocation groups** (each character alone; other models grouped by matching W/Sv/InSv), declares the order they will be hit in, and works through the saves from worst roll to best.

The rules that matter here:

- A group with an already-wounded model must go first.
- **Characters cannot be put in front of ordinary models.** This is why a leader hiding in a squad is genuinely hard to snipe - and why `[PRECISION]` weapons, which override this, are prized.

---

## Mortal wounds and hazards

**Mortal wounds** skip hit, wound, and save entirely. Each one costs a model one wound directly. They always land on an already-wounded model first, and on non-characters before characters. If an attack inflicts both normal damage and mortal wounds, resolve the normal damage first.

**Hazard rolls** are the game's self-harm mechanic. Roll a D6; on a 1-2 the unit suffers a mortal wound (three if it is a Monster or Vehicle). Risky weapons (`[HAZARDOUS]`), desperate retreats, and bailing out of a wrecked transport all trigger them.

---

## Objective Control - how you actually win

Objectives are places on the table, usually a defined **terrain area** (**14.01**). A model is within range of a terrain objective simply by being inside that terrain area.

At the end of **every phase and every turn** (**14.02**):

1. Each player adds up the **OC** of all their models within range of the objective.
2. The higher total controls it. A tie means nobody controls it.

Consequences worth internalising:

- **Control flips constantly.** It is re-checked at the end of every phase, so a unit that walks on during your Movement phase can take an objective away without firing a shot.
- **Bodies beat quality.** Ten models with OC 1 out-hold one tank with OC 3.
- **A battle-shocked unit has no OC at all.** Morale failure can hand over an objective you thought was safe.
- **Secured** objectives are the exception: some rules let you keep control after your models leave, until the opponent out-controls you at the end of a phase.

Full concept page: [`../../../KB/concepts/objective_control.md`](../../../KB/concepts/objective_control.md).

---

## Battle-shock

Morale in 11th Edition is one roll with three sharp consequences.

**When:** in the Command phase (**08.03**), for each of your units that is already battle-shocked or is at/below half-strength. Some other rules force extra rolls.

**How:** roll 2D6 against the unit's Leadership (**01.06**, **01.07**). Pass and nothing happens - and a currently battle-shocked unit recovers.

**Fail, and while battle-shocked:**

- Its **OC becomes nothing**. It stops holding ground.
- You **cannot target it with stratagems**.
- It **cannot start or complete actions**.
- It can only Fall Back using *Desperate Escape*, which risks casualties.

"Half-strength" means half the models remaining for a multi-model unit, or half the wounds remaining for a single model. The core stratagem **Insane Bravery** (1CP, once per battle) auto-passes one roll.

---

## Leaders, Support, and attached units

Characters do not usually fight alone. Before the battle, a **Leader** unit or a **Support** unit is attached to an eligible **bodyguard** unit (**19.01**), and from then on they are **one unit** for every rules purpose.

What follows from that:

- Attacks target the combined unit and use the **bodyguard's Toughness**, not the character's.
- The attached unit has **all** the keywords of its components - which cuts both ways, since a `[ANTI-PSYKER]` weapon now bites the whole squad because the leader is a psyker.
- A leader's abilities apply to the whole unit **until the last model of that leader unit is destroyed**.
- The unit only counts as destroyed when the last model from the whole attached unit is gone.

> **11th Edition change worth flagging:** several Necron Crypteks moved from **Leader** to **Support** in the owned Faction Pack v1.1. Both form attached units, but a bodyguard unit can normally take one of each - so a Cryptek and a Leader character can stack on the same squad. Confirm per datasheet before list-building.

---

## Command Points and stratagems

Both players gain **1 CP** in the Command phase (**08.02**). You spend CP on **stratagems** (**15.01**) - one-off effects with a stated trigger, target, and effect.

The core restrictions:

- You cannot use the **same stratagem twice in one phase**.
- You cannot normally target the **same unit with two stratagems** in one phase.
- Battle-shocked units cannot be targeted by your stratagems at all.

Core stratagems every army has include Command Re-roll, Insane Bravery, Fire Overwatch, Smokescreen, Rapid Ingress, Heroic Intervention, and Counter-offensive. Your detachment adds more.

---

## Related pages

- [`Overview.md`](Overview.md) - what a game is and how you win
- [`Turn_Structure.md`](Turn_Structure.md) - when each of these happens
- [`Keyword_Glossary.md`](Keyword_Glossary.md) - one-line definitions for every term above
- [`../setup/Terrain_Basics.md`](../setup/Terrain_Basics.md) - cover, visibility, and the Hidden rule
- [`../../../KB/concepts/objective_control.md`](../../../KB/concepts/objective_control.md) - the KB concept page

---

## Change Log
- v0.5.1 (2026-08-18): Rule-ID cites; cover/Heavy/OC paraphrase confirmed (track `40k_warcom_quotes` S3).
- v0.5.0 (2026-08-18): Project-wide semver snapshot (x.y.z).
- v1.0 (2026-08-16): Initial core mechanics guide (slice S3), from the owned Core Rules PDF and Necrons Faction Pack v1.1, both read 2026-08-16.

## Attribution
- Project: Wargame_Concierge
- Maintainer: Russell Catt
- Warhammer 40,000 is a trademark of Games Workshop Limited. This document is a personal teaching paraphrase and reproduces no publisher text or statlines.

## Rising Tide Notes
- This document follows Rising Tide documentation standards.
- **Verify before you play.** Cross-check anything here against the current Munitorum Field Manual and your faction pack - Games Workshop patches rules and points between publications. Content on this page reflects sources read on **2026-08-16**.
