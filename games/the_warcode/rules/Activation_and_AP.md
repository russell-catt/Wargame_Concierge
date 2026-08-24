<!--
FILE: games/the_warcode/rules/Activation_and_AP.md
VERSION: v0.1 (2026-08-23)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, warcode_tactical_doctrine)

DOCUMENT_TYPE: Deep Dive / Teaching Guide
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: The Warcode
REFERENCE_STATUS: Active — draft, beta v0.8.7-F (2026-08-23)

SOURCES:
  - raw/the_warcode/The Warcode Rulebook V.0.8.7-F.pdf (free public beta, RedMakers; retrieved 2026-08-23)
  - raw/the_warcode/rulebook_v087f_extract.txt

PURPOSE:
  Deep-dive on the activation loop and the two-Action-Point economy: what an
  activation buys, what is free, and how AP scarcity shapes every decision.

PRIMARY_AUDIENCE:
  - A player who knows the round structure and wants to spend AP well
  - Cross-game readers used to Murder Platoon's action economy

KEY_SECTIONS_EXPECTED:
  - The activation loop
  - Two AP and what they buy
  - The free-action list
  - Movement as an AP purchase
  - Overwatch as an activation sink
  - AP traps and habits

UPDATE_TRIGGER:
  A newer free beta changes AP totals, the action list, or activation ordering.
-->

# Activation and AP — the two-point economy

Everything in The Warcode is rationed through **2 Action Points per unit per round**. **`confidence: draft`**, beta **v0.8.7-F**, read **2026-08-23**. Full wording: [`Rulebook_Quotes.md`](Rulebook_Quotes.md).

---

## The activation loop

> Each player takes turns activating one unit.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.4 — "UNIT ACTIVATION"

> After performing an action, flip the activation token to indicate that the unit can no longer perform actions in this round. At the start of a new round, flip all tokens back to the side to indicate that the unit can be activated.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.4 — "UNIT ACTIVATION"

Activation strictly alternates: you activate one unit, then your opponent activates one, and so on until every model on both sides has gone. With eight units a side, that is sixteen activations per round, and the initiative winner acts first in every pair. The token is the only bookkeeping the game asks for, and it is doing real work — flip it as the unit finishes, not when you remember, because a unit whose token still shows "can activate" will get activated twice by an honest opponent who is just reading the board.

The alternating structure is where most of the tactical tension lives. A unit you activate early is a unit your opponent can respond to with seven more activations; a unit you hold back is a unit that acts with better information but risks having nothing left worth doing. Going first is not automatically good.

---

## Two AP, and what they buy

> Each unit has 2 Action Points (AP). Every action costs a specific number of AP (except for picking up items from the ground and opening/closing doors, which have special rules).
>
> Some units have abilities that give extra AP to another friendly unit.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.4 — "ACTION POINTS (AP)"

Two AP is the whole budget, and it does not carry over. In practice this means an activation is almost always a **pair** of decisions, and the interesting question is which pair:

| Pair | What it gets you | When it is right |
|------|------------------|------------------|
| Move + Move | Up to 2× Movement Range | Repositioning to objectives, crossing open ground fast |
| Move + Shoot | Reposition then fire | The default aggressive activation |
| Shoot + Shoot | Two volleys from cover | You are already in position with ammo to spare |
| Move + Overwatch | Take a firing lane and hold it | Denying an approach; see the caveat below |
| Engage (2 AP) | Boosted move straight into melee | Closing the last gap when a normal move would fall short |
| Shoot + Reload | Empty the weapon, refill it | Ammo management on low-capacity guns |
| Move + Pass | Reposition without exposing further | Rare, but Pass has a specific Overwatch property |

Heavy weapons cost **2 AP to shoot**, which collapses the whole activation into a single trigger pull. A Bastion or a Doom that has not started the round in a good firing position essentially cannot both move and shoot — that constraint, not the profile, is what makes those units positional pieces.

---

## What is free

Two actions cost **no AP** at all, and both have a **1 inch** proximity requirement:

> Picking up items costs no AP, but the unit must be within 1 inch of it.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.18 — "ITEM PICKUP"

> Opening or closing a door costs no AP, but the unit must be within 1 inch of the doorway. A unit farther away spends 1 AP to move within 1 inch first. Each unit can open or close a door only once per activation.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.18 — "OPENING AND CLOSING DOORS"

Medkits are the third freebie — using one costs **0 AP** and happens once during the unit's activation. The pattern here is worth internalizing: the game charges you for the **movement** that puts you in range of a thing, then lets you interact for free. So the real cost of grabbing a dropped grenade, slamming a door, or patching a wounded friend is one move, and a move you were going to make anyway makes the interaction genuinely free.

The once-per-activation limit on doors exists to stop a unit from opening a door, shooting through it, and closing it again in the same activation. You get one door state change per unit per activation, so decide whether you are opening a lane or sealing one.

---

## Movement is the most-purchased action

> Movement is measured using an inch ruler. The standard movement distance for 1 AP is 6 inches.
>
> Each unit has one of three Movement Ranges:
>
> SLOW: 5 INCHES
> STANDARD: 6 INCHES
> FAST: 7 INCHES
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.6 — "MOVEMENT"

On a **33" × 24"** board, a standard unit crosses the long edge in roughly three AP — most of two activations. That is why the speed bands matter more than they look: a Fast unit at 7" per AP covers 14" in an activation against a Slow unit's 10", and on a board this size that is the difference between contesting an objective this round and next.

Both movement penalties come off the **Movement Range**, not off a fixed distance:

> To move through a friendly unit, subtract 2 inches from the Movement Range.
>
> To move through partial cover, subtract 1 inch from the Movement Range.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.6 — "MOVEMENT"

A Slow unit paying the friendly-unit penalty is moving **3 inches** for its AP. Squeezing past your own models is expensive; give your fast units clean lanes and let the slow ones go around.

---

## Overwatch eats the whole activation

> To activate Overwatch, a unit must spend 1 AP, have at least 1 ammunition, and be outside melee range of an enemy unit. To show that a unit is in Overwatch mode, place an Overwatch token next to it. Once the token is placed, the unit cannot take any other action for the rest of the round.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.10 — "OVERWATCH"

Read that last sentence carefully — Overwatch is priced at 1 AP but **spends 2**, because the second point is forfeited the moment the token goes down. Move-then-Overwatch is therefore a full activation for one conditional shot, and it is only worth it when the shot is likely: you cover a lane the opponent must cross, or you threaten a unit that has to act.

The compensation is that Overwatch fires **before** the enemy's declared action resolves, which is the only way in the game to act outside your own activation. Against an Engage in particular you get a free volley into the charging model before melee begins.

---

## Pass is a real action

> PASS (skipping a turn without triggering Overwatch)
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.4 — "UNIT ACTIVATION"

Pass is the only listed activation option that does **not** appear on the Overwatch trigger list (Shooting, Movement, Melee combat, Disengaging, Escaping, Using equipment, Reloading). A unit sitting inside an enemy's covered lane can burn its activation safely rather than eat an overwatch shot for a marginal reposition. It also lets you dump a low-value activation early to force your opponent to commit a real one, which matters in an alternating system.

---

## AP traps and habits

| Trap | Habit that fixes it |
|------|---------------------|
| Moving into range with 0 AP left to shoot | Count the second AP **before** the first move |
| Activating a heavy-weapon unit that must move | Position heavies on the round they can afford to; they shoot for 2 AP |
| Buying Overwatch with a unit that has better options | Overwatch costs the activation, not 1 AP |
| Walking through your own models | −2" is the worst penalty in the game; go around |
| Forgetting free interactions | Doors, pickups, and medkits are 0 AP once you are within 1" |
| Spending 2 AP on Escape when Disengage would do | Escape's extra AP only buys "you move even on a failed roll" |
| Leaving the activation token unflipped | Flip on completion, every time |

---

## Related pages

- [`Turn_Structure.md`](Turn_Structure.md) — where activation sits in the round
- [`Combat_Ranged_and_Melee.md`](Combat_Ranged_and_Melee.md) — what your AP actually resolves into
- [`Equipment_Loot_and_Doors.md`](Equipment_Loot_and_Doors.md) — the free-action surface in detail
- [`Rulebook_Quotes.md`](Rulebook_Quotes.md) — verbatim activation and AP text
- [`Keyword_Glossary.md`](Keyword_Glossary.md) — term lookup

---

## Open questions

- How many units grant **extra AP** to a friendly unit, and at what cost — the p.4 text promises the ability exists, but neither printed team list in the extract shows one.
- Whether granted AP can push a unit above 2 AP in a single activation, or only replaces spent points.
- Whether Pass can be declared after spending 1 AP, or only as the whole activation.

---

## Change Log

- v0.1 (2026-08-23): Initial deep-dive on activation and AP from beta v0.8.7-F extract.

## Attribution

- Project: Wargame_Concierge
- Maintainer: Russell Catt
- The Warcode is property of RedMakers. Unofficial, unauthorized personal learning notes — never for sale.

## Rising Tide Notes

- This document follows Rising Tide documentation standards.
- Two AP is the whole game. Everything else is a price list.
