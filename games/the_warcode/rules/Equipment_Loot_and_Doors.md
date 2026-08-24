<!--
FILE: games/the_warcode/rules/Equipment_Loot_and_Doors.md
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
  Deep-dive on the equipment economy: buying gear before deployment, throwing
  grenades, using medkits, recovering dropped tokens from casualties, and
  controlling doors.

PRIMARY_AUDIENCE:
  - A player distributing 4 equipment points before round 1
  - A player deciding whether to grab a dead model's grenade mid-game

KEY_SECTIONS_EXPECTED:
  - Equipment points and the buy
  - Grenades: throw, scatter, blast
  - Grenade damage resolution
  - Medkits
  - Loot from casualties
  - Doors and door blocking

UPDATE_TRIGGER:
  A newer free beta changes equipment points, item costs, blast rules, or door
  interaction.
-->

# Equipment, loot, and doors

The small-item layer: four points of gear, tokens that outlive their carriers, and doors that rewrite the board. **`confidence: draft`**, beta **v0.8.7-F**, read **2026-08-23**. Full wording: [`Rulebook_Quotes.md`](Rulebook_Quotes.md).

---

## The buy

> Equipment is additional portable gear that a unit receives before the game begins. Players start with 4 equipment points, which can be spent on medkits or grenades, unless a unit's rules restrict this.
>
> NUMBER OF EQUIPMENT POINTS: 4
>
> EQUIPMENT COSTS:
> GRENADE: 2 POINTS
> MEDKIT: 2 POINTS
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.16 — "EQUIPMENT"

> Unless its rules say otherwise, a unit can carry only one piece of equipment: either one grenade or one medkit.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.16 — "EQUIPMENT"

Four points at two points each means **exactly two items**, spread across an eight-model squad. This is a genuinely small decision space — two grenades, two medkits, or one of each — and it happens **after deployment**, which is the part people miss. The setup sequence puts "distribute equipment" third, once both squads are already on the table, so you buy with full knowledge of where every enemy model stands. Do not decide the split in advance.

The rough guidance: grenades are proactive and medkits are reactive. Two grenades pressure clustered enemies and units hiding behind partial cover, which the blast ignores. Two medkits give 4 HP of staying power spread across a squad where most models have 8 HP. One of each hedges. On the tight 33" × 24" board with three rooms in the printed scenario, models cluster more than you expect, which pushes toward grenades.

Two units come with gear already:

> SPECIAL ABILITY: Starts the game with 2 grenades and cannot take other equipment.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.33 — "PROTAGEN MARINES TEAM LIST" (Blast)

Protagen **Blast** and Ulfari **Phantom** each arrive with two grenades free, outside the four-point budget and outside the one-item limit. That effectively means every squad fields at least two grenades before spending a point — worth remembering when you weigh a third.

---

## Grenades

> COST OF THROWING A GRENADE: 1 AP
>
> A grenade can be thrown up to 5 inches, measured from the base of the throwing unit. Place the token at any point within that distance.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.16 — "GRENADE"

> The blast radius of the grenade is 2 inches, measured from the edge of the token.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.16 — "GRENADE"

A 5 inch throw plus a 2 inch blast gives a **7 inch threat bubble** for 1 AP, and you place the token freely rather than rolling for scatter. That is a precision weapon, not a random one. The reach compares well with most guns in the game — only the rifle (7") and heavy weapon (8") beat it — and unlike them it needs no ammunition and no hit roll.

Blocked throws are placed rather than lost:

> If the throw ends on an enemy unit, friendly unit, or partial cover, the token is always placed at a shorter distance, meaning less than 5 inches.
>
> If the throw ends beyond an enemy unit, friendly unit, or partial cover, and the token cannot be placed within 5 inches, place it farther than 5 inches, next to the unit or cover that blocked the throw.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.16 — "GRENADE"

This mirrors the movement placement rule exactly — the token stops short of the obstacle, or is placed adjacent to it on the far side. Either way it lands somewhere, so a blocked throw is not a wasted AP; it is just a throw that landed closer than you wanted.

---

## Why grenades beat cover

> The grenade affects all units within its blast radius, including friendly units. A unit is within the blast radius if the measurement from the grenade token reaches its base. The grenade completely ignores partial cover and agility. Any unit within the blast radius immediately makes an armor penetration check.
>
> To determine the damage from the explosion, roll 2 dice for each unit within the blast radius and compare the results with that unit's armor value.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.17 — "GRENADE THROW EXAMPLE"

This is the grenade's whole reason to exist. It **skips the hit check entirely** — no agility, no cover modifier — and goes straight to armor penetration with 2 dice per model caught. Against the Ulfari, whose defence is Agility 4–5 on Armor 3, that is devastating: their good stat does nothing and their bad stat is all that stands between them and a −1 penetration weapon needing a 2+.

Full cover still works, though, because fragments need a sight line:

> If a unit is behind full cover but within the blast radius, make a line of sight check as with shooting to determine whether the fragments reach it. The check is made from the grenade token instead of the shooting unit.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.17 — "GRENADE THROW EXAMPLE"

The 50%-of-base test applies, measured **from the token**, not from the thrower. So a wall protects; a barricade does not. When you place the token, you are effectively choosing a new firing position for the line-of-sight check — place it to see around the wall, not just to cover the models.

The blast is genuinely indiscriminate. Your own models in radius take checks too, and there is no friendly-fire exemption here the way there is for shooting past a friend. Check the 2 inch bubble against your own bases before committing.

---

## Grenade damage, worked

> Unit 2 and Unit 3 have an armor value of 4, and the grenade has an armor penetration of -1, so a roll of 3 or higher is needed to penetrate.
>
> Unit 2 takes no damage because its rolls are lower than 3.
>
> Unit 3 rolls 4 and 6. Both are 3 or higher, so the armor is penetrated twice. The 6 counts as critical damage. Unit 3 takes 3 damage in total: 1 point for the 4, which is the grenade's normal damage, and 2 points for the 6, which is critical damage.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.18 — "GRENADE THROW EXAMPLE"

The grenade profile is **−1 penetration, 1 normal damage, 2 critical**, two dice per model. Against Armor 4 that is a 3+ on each die, and the realistic outcome is 1–3 damage per model caught. So a grenade is a **chip-and-spread** tool, not a killer — its value is hitting three models at once and stripping Overwatch, not deleting anything.

Two secondary effects matter as much as the damage. Any model that takes even 1 point **leaves Overwatch**, and the p.11 example shows that used deliberately from behind full cover, where the thrower never enters the firing lane. And damage taken means a model is no longer at full health, which switches off the Protocol "Hunt" trigger discussed in [`Scenarios_and_Events.md`](Scenarios_and_Events.md) — occasionally your own grenade is a favour.

---

## Medkits

> A medkit restores 2 HP, but never above the unit's maximum HP. A unit with a medkit can use it on itself or on a friendly unit within 1 inch once during its activation. Using a medkit costs no AP. Each medkit works only once, so remove its token from the field after use.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.18 — "MEDKIT"

Free to use, so the only cost is the movement that gets you within 1 inch of the patient — and none at all if you heal yourself. On models with 8 HP, 2 HP back is a quarter of the bar; against a shotgun that deals 3/4 per penetrating shot, it is not much. Medkits are best understood as **denying your opponent a kill this round** rather than as sustain.

That framing changes when you remember re-roll points: your opponent gains **1 re-roll point every time one of your units dies**. Keeping a wounded model alive denies both the model loss and the resource. Heal the model that is one hit from dying, not the one that looks ugliest.

The single-use token comes off the board after use, which means the medkit carrier becomes an ordinary model — and, per the pickup rules below, becomes eligible to pick up someone else's dropped gear.

---

## Loot from casualties

> If a unit carrying equipment is killed, the token stays on the ground where it died, and any unit without equipment of its own can pick it up.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.16 — "EQUIPMENT"

> Picking up items costs no AP, but the unit must be within 1 inch of it.
>
> Unit 1 spends 1 AP to move within 1 inch of a grenade lying on the ground and picks it up for free. With its remaining AP, Unit 1 can throw the grenade or take any other action costing 1 AP.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.18 — "ITEM PICKUP"

Gear is persistent battlefield furniture. Kill Blast or Phantom and their **two grenades** stay on the table where they fell, available to anyone who walks over — including the enemy. That makes grenade-carriers double-edged: they are worth killing, and worth killing *away* from your own lines.

The example spells out the tempo, and it is better than it looks: **move (1 AP) → pick up (free) → throw (1 AP)**. A model can cross ground, arm itself, and use the item in the same activation. There is no delay, no "next round" restriction. A grenade dropped 6 inches from a fresh model is a live grenade.

The one gate is the carry limit — only a unit **without** equipment can pick something up. Your grenade-thrower cannot restock after throwing unless the throw emptied it. Practically, plan a second, empty-handed model to trail behind and collect.

---

## Doors

> Opening or closing a door costs no AP, but the unit must be within 1 inch of the doorway. A unit farther away spends 1 AP to move within 1 inch first. Each unit can open or close a door only once per activation.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.18 — "OPENING AND CLOSING DOORS"

Doors are free to operate and they change line of sight, which makes them the highest-leverage free action in the game. A closed door is full cover: it blocks shooting entirely and cannot be moved through. Opening one creates a firing lane; closing one deletes it.

The once-per-activation cap is what stops the obvious abuse — you cannot open a door, shoot through it, and close it again behind the same model. You get one state change, so you are always leaving the door in a state your opponent gets to act against. Opening a door to shoot means the return lane is open too.

---

## Door blocking

> If a unit is within 1 inch of the doorway, the door is considered blocked. A unit from the opposing team cannot open or close a blocked door.
>
> If two or more units from different teams are within 1 inch of the same doorway, the door is considered blocked for everyone, and no unit can open or close it.
>
> This applies regardless of which side of the door each unit stands on.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.19 — "DOOR BLOCKING"

Standing within 1 inch of a doorway is a **zone-of-control** play: you keep the right to operate the door and take it away from the enemy. This is how you lock a room open (to keep your shooting lane) or lock it shut (to seal a flank), and it costs nothing beyond standing there.

The contested case is the interesting one. Once models from both teams are within 1 inch, **nobody** can touch the door, whatever side they are on. So a door you have opened can be frozen open by an enemy model stepping up to it — a real risk when you crack a door to shoot and your opponent's fast model closes the distance. Freezing a door in a state that suits you is a legitimate objective in its own right, and on the three-room «Core of the Machine» map it interacts directly with which rooms a Protocol Card can trap people in.

---

## Quick reference

| Item / action | AP | Range | Effect |
|---------------|----|-------|--------|
| **Buy equipment** | — | Pre-game, after deployment | 4 points; grenade 2, medkit 2 |
| **Throw grenade** | 1 | 5" throw | 2" blast, 2 dice per model, −1 pen, 1 / 2 damage |
| **Use medkit** | **0** | Self or friendly within 1" | Restore 2 HP, not above max; once per activation; token removed |
| **Pick up item** | **0** | Within 1" | Only if not already carrying equipment |
| **Open / close door** | **0** | Within 1" of doorway | Once per activation per unit |
| **Block a door** | — | Within 1" of doorway | Enemy cannot operate it; both sides present = frozen |

---

## Related pages

- [`Key_Concepts.md`](Key_Concepts.md) — condensed equipment summary
- [`Activation_and_AP.md`](Activation_and_AP.md) — why free actions are the best value in the game
- [`Combat_Ranged_and_Melee.md`](Combat_Ranged_and_Melee.md) — cover rules the grenade ignores
- [`Scenarios_and_Events.md`](Scenarios_and_Events.md) — Protocol Cards that punish standing in the wrong room
- [`Rulebook_Quotes.md`](Rulebook_Quotes.md) — verbatim equipment, grenade, medkit and door text
- [`../setup/Terrain_Basics.md`](../setup/Terrain_Basics.md) — doors on the board

---

## Open questions

- Whether a unit may **drop** equipment voluntarily to pick up something better — only death is described as putting a token on the ground.
- Whether the two-grenade models (Blast, Phantom) can pick up a dropped item after throwing both, or whether "cannot take other equipment" is permanent.
- Whether a medkit can be used on a model in melee combat, given melee blocks "equipment" use — the medkit is free and the restriction is written against actions.
- Whether a grenade token remains on the board after detonating, or is removed immediately.
- Whether doors have HP or can be destroyed — nothing in the extract suggests so.

---

## Change Log

- v0.1 (2026-08-23): Initial equipment, loot and doors deep-dive from beta v0.8.7-F extract.

## Attribution

- Project: Wargame_Concierge
- Maintainer: Russell Catt
- The Warcode is property of RedMakers. Unofficial, unauthorized personal learning notes — never for sale.

## Rising Tide Notes

- This document follows Rising Tide documentation standards.
- Free actions still cost a move. Budget the move.
