<!--
FILE: games/the_warcode/rules/Combat_Ranged_and_Melee.md
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
  Deep-dive on damage resolution: the shooting sequence, ammunition, cover and
  line of sight, Overwatch timing, and the very different melee flow with its
  defender block roll, Melee Lock, Disengage and Escape.

PRIMARY_AUDIENCE:
  - A player resolving their first firefight or brawl
  - Cross-game readers mapping Murder Platoon shooting habits onto a
    two-check, block-roll system

KEY_SECTIONS_EXPECTED:
  - The two checks that underpin everything
  - Shooting sequence
  - Ammunition
  - Cover, line of sight, shooting past friends
  - Overwatch timing
  - Melee: the block roll
  - Melee radius vs Melee Lock
  - Engage, Disengage, Escape
  - Re-rolls in combat

UPDATE_TRIGGER:
  A newer free beta changes hit/penetration resolution, cover modifiers,
  Overwatch triggers, or Melee Lock costs.
-->

# Combat — ranged and melee

Two checks, one shared damage rule, and two very different flows around them. **`confidence: draft`**, beta **v0.8.7-F**, read **2026-08-23**. Full wording: [`Rulebook_Quotes.md`](Rulebook_Quotes.md).

---

## The two checks everything runs on

Every attack in The Warcode passes through the same pair of D6 gates, and the target's two defensive stats guard one each:

> The agility value shows how difficult it is to hit the unit in ranged and melee combat, and is used when making hit checks against the unit.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.5 — "AGILITY"

> The armor value shows how difficult it is to penetrate the unit's armor in ranged and melee combat, and is used when making armor penetration checks against the unit.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.5 — "ARMOR"

**Agility is the hit gate; Armor is the wound gate.** Both are roll-equal-or-higher on a D6, so a stat of 3 is a two-thirds gate and a stat of 5 is a one-third gate. That is the whole probability model, and it is why the agility cap matters so much — the game explicitly refuses to let cover stack a target past 5.

Damage is also shared between the two flows. A penetration die showing **6** deals the weapon's **critical damage**; anything else that penetrates deals **normal damage**. The same die tells you whether you got through and how hard, which is why a shotgun's 3/4 split reads so differently from a pistol's 1/2.

The one asymmetry: melee adds a **defender block roll** between the hit and the penetration. Shooting does not.

---

## Shooting, step by step

> Unit 1 opens fire on Target with a shotgun.
>
> 1. Check that there is enough ammunition to shoot. Unit 1 has not fired yet, so it has full ammunition. Check that there is enough AP for the shot. Unit 1 was just activated this round and has 2 AP.
>
> 2. Check the range to Target. The range is less than 5 inches, so the shotgun can reach Target.
>
> 3. Check Target's agility. Roll 3 or higher to hit.
>
> 4. The shotgun has 2 shots, so roll 2 dice to check for hits. The rolls are 3 and 4. Both rolls beat Target's agility, so both shots hit.
>
> 5. Before the armor penetration check, compare the shotgun's penetration value with Target's armor value. Target's armor value is 4, and the shotgun's penetration is -1. This means Target's effective armor value against the shotgun is 3 (4 - 1 = 3). Roll 3 or higher to penetrate.
>
> 6. Both shots hit Target, so roll 2 dice to check for armor penetration. The rolls are 3 and 6. Both shots penetrate the armor, since Target's effective armor value is 3.
>
> 7. Determine the damage from those same rolls (3 and 6). The 3 indicates normal damage, since every roll except a 6 is normal damage. The 6 is critical damage.
>
> 8. Check the shotgun's damage values for each type of hit. The shotgun deals 3 normal damage and 4 critical damage, giving a total of 7 (3 + 4 = 7). Subtract 7 from Target's HP, leaving Target with 2 HP (9 - 7 = 2).
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.20 — "SHOOTING EXAMPLE"

Run that example once with real dice and the sequence sticks. The load-bearing detail is **step 5**: you resolve the armor arithmetic *before* rolling, so the penetration target number is fixed and visible. A `+` on the weapon **raises** the target's effective armor (worse for you); a `−` **lowers** it. Beginners consistently read the sign backwards because it is printed as a weapon stat but applied to the defender.

Seven damage from one shotgun activation against a 9 HP model shows how lethal this system is. There is no wound-allocation buffer and no save after penetration — two dice that both land can take a model to the edge of death. Positioning is the defence, not durability.

---

## Ammunition is the real leash

> The unit must always have at least 1 ammunition to perform the shooting action. Subtract 1 from the current ammunition value after each shooting action. If the ammunition value is 0, the unit cannot shoot until it reloads.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.9 — "AMMUNITION"

Note the accounting: **one shooting action spends one ammunition**, regardless of how many dice that action rolls. A pistol firing 5 dice and a heavy weapon firing 4 dice each burn a single point. So the ammo stat is really a count of **activations of shooting**, and the heavy weapon's single point means one volley then a mandatory reload — its effective rate of fire is one shot every other activation, or worse.

Reload restores the weapon to its printed maximum for the listed AP. Because reloading is on the Overwatch trigger list, reloading inside an enemy firing lane invites a free shot; step back behind cover first when you can afford the movement.

---

## Cover and line of sight

Two terrain categories, and the difference is height:

> Partial cover is any terrain object on the field that does not exceed the height of the units. Objects taller than the units count as full cover and are impassable. To move through partial cover, subtract 1 inch from the Movement Range. When shooting at a Target behind partial cover, or with partial cover on the line of fire, the Target's agility increases by 1 for each piece on that line.
>
> A unit's agility cannot exceed 5, regardless of the number of bonuses applied.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.11 — "PARTIAL COVER"

Full cover blocks; partial cover taxes. The tax is **+1 Agility per interfering piece on the line of fire**, and crucially it applies whether the target is hugging the cover or the cover is merely *in the way* somewhere along the shot. Two pieces on the line means +2, and a base-3 model becomes a 5 — the cap. Against a target already at Agility 5, like the Ulfari Reaper, cover adds nothing at all.

The counterplay is standing close to your own cover:

> If partial cover stands between a shooting unit and its Target, and the unit is within 1 inch of that cover, the unit counts as being behind it and can shoot without interference.
>
> When shooting through partial cover, measure the distance to the cover in the direction of the Target. If the cover is within 1 inch, it does not interfere with the shot.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.12 — "PARTIAL COVER"

This is the single most valuable positional rule in the game. A shooter **hugging** a barricade shoots over it cleanly and still counts as behind it against return fire. A shooter standing two inches back from the same barricade taxes its own shot. Get your models on the terrain, not near it.

The mirror rule protects targets who are only half-hidden:

> If more than half of the Target's base is visible past the edge of the partial cover, the Target does not count as being behind it and receives no agility bonus.
>
> On a 28mm base, that means more than 14mm visible to the shooting unit.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.12 — "PARTIAL COVER"

Against **full** cover the test is a hard gate rather than a modifier — you need at least 50% of the base visible or there is no shot at all. The 14 mm figure on a 28 mm base is the practical measurement.

---

## Shooting past your own models

> A Target behind a friendly unit can still be shot at, but its agility increases by 1. A unit's agility cannot exceed 5, regardless of the number of bonuses applied. A Target with a base agility of 5 receives no bonus.
>
> Friendly fire will not occur if 50% of the Target's base is in direct line of sight. For example, a 28mm base needs at least 14mm visible to the shooting unit.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.12 — "SHOOTING THROUGH FRIENDLY UNITS"

Friendly models behave like a piece of partial cover for the enemy: +1 Agility, capped at 5. The friendly-fire clause is a safety valve — clear the 50% visibility bar and nothing bad happens to your own model. Below it, the implication is that you should not be taking the shot. Screening your own shooters with your own bodies is therefore mildly self-defeating; screening the **objective** is not.

---

## Overwatch timing

> A unit in Overwatch mode holds its fire and waits. If an enemy unit moves into its shooting range, or takes action while already inside that range, the Overwatch unit opens fire before the enemy unit completes its action.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.10 — "OVERWATCH"

> Actions that trigger Unit 1 to open fire before Target's declared action:
>
> SHOOTING
> MOVEMENT
> MELEE COMBAT
> DISENGAGING FROM MELEE LOCK
> ESCAPING FROM MELEE LOCK
> USING EQUIPMENT
> RELOADING
>
> Overwatch fire follows the normal shooting rules: line of sight, ammunition, etc.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.11 — "OVERWATCH"

Overwatch is an **interrupt**: the enemy declares, you shoot, then their declared action resolves. It does not cancel what they were doing. The list above is exhaustive, and **Pass is absent** — a unit caught in a covered lane can simply do nothing safely.

Two exits from Overwatch, both immediate: **firing** and **taking damage**. The rulebook's sharpest example shows the second being exploited deliberately — an enemy moves out of line of sight behind full cover (no trigger, because normal shooting rules apply and there is no shot), then lobs a grenade, and the damage strips Overwatch without ever entering the firing lane. If you are holding a lane, expect the grenade.

Everything still in Overwatch at end of round comes out of it, tokens removed. Overwatch never carries between rounds.

---

## Melee is a different game

> Melee combat is different from shooting: both the armor and agility of the Target are involved, as well as its defense (the Target rolls dice equal to its melee strength).
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.21 — "MELEE COMBAT EXAMPLE"

> Melee strength shows the number of attacks, meaning how many dice to roll in melee combat. The defender rolls dice equal to its melee strength when blocking those attacks. Melee strength also indicates the value the opponent must roll on a single die to disengage from Melee Lock.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.13 — "MELEE STRENGTH"

**Melee Strength does three jobs**: it is your attack dice, your block dice, and the number an enemy must beat on a D6 to break away from you. One stat, three roles — a Volt Sword's 4 means four attacks, four blocks, and a 4+ needed to escape you.

The block step is the flow that has no shooting equivalent:

> 5. Compare the values on the attacker's and defender's dice. Each attack can be blocked only by a die with a value that matches or exceeds the attacker's die value. Here, only the attack of 3 is blocked, since the defender has a die of equal or higher value. The attack of 5 is not blocked, so only one of the hits gets through.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.21 — "MELEE COMBAT EXAMPLE"

Attacker rolls Melee Strength dice and keeps those that met the target's Agility. Defender rolls its own Melee Strength dice and pairs them off — each defence die cancels one attack die of **equal or lower** value. Survivors go to armor penetration and damage as normal.

The consequence is that **high attack rolls are hard to block**. A 6 can only be stopped by a 6. This makes melee much swingier than the raw dice counts suggest: a Combat Knife (strength 2) that rolls 5 and 6 can punch through a Volt Sword's four defence dice, while four mediocre attacks bounce off two good blocks. Volume helps, but quality of roll decides.

Against a low-strength defender the maths is brutal in the other direction. A Fist (strength 1) defends with a single die, so a Combat Claws attacker rolling five dice will land most of them.

---

## The melee radius, and the lock inside it

> The melee range value also acts as a radius around the unit. Enemy units inside that radius are automatically in melee combat with that unit. They cannot shoot or perform other actions, except taking part in melee combat or using movement to leave the melee radius.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.14 — "MELEE RADIUS IMPACT"

> Two units are in Melee Lock when their bases touch. A unit can be in Melee Lock with several enemy units at once.
>
> Melee Lock follows the same rules as melee combat, but it is harder to leave: instead of simply moving out, a unit must use Disengage or Escape from Melee Lock.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.15 — "MELEE LOCK"

There are **two tiers of engagement**, and the difference is base contact:

| Tier | Condition | Effect | Cost to leave |
|------|-----------|--------|---------------|
| **Melee combat** | Enemy inside your melee radius (usually 1") | No shooting, no equipment, no blocked abilities | 1 AP move out |
| **Melee Lock** | Bases **touch** | Same restrictions | Disengage (1 AP, roll) or Escape (2 AP, roll) |

This is the shutdown mechanic. Getting a melee model into an enemy shooter's radius switches that shooter off entirely — it cannot fire, cannot use its grenade, cannot do anything but fight back or walk away. Against a heavy-weapon unit that costs 2 AP per shot, tying it up for a round is worth more than damage.

Note the interaction with **melee range as a stat**: it is a radius, so a weapon with longer melee range projects a bigger shutdown bubble. The Protagen **Smasher** takes this further, printing an ability that locks enemies within 1 inch *without* base contact — turning ordinary melee combat into full Melee Lock and denying the cheap 1 AP walk-out.

---

## Engage, Disengage, Escape

> Engage is a boosted movement toward the Target that ends in melee combat.
>
> COST OF ENGAGE: 2 AP
>
> MOVEMENT RANGE BONUS DURING ENGAGE: +2 INCHES
>
> For example, a unit with a movement range of 6 inches moves up to 8 inches. Melee combat begins once it reaches the Target. All standard penalties for moving through partial cover or friendly units apply.
>
> The measurement to the Target must reach its base, just as with shooting. If it does not reach the base, Engage is not possible.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.14 — "ENGAGE"

Engage is the whole activation for +2 inches and guaranteed contact. Compare it honestly against **Move + Move**, which gets a standard unit 12 inches with no melee: Engage is not about distance, it is about arriving *in melee* rather than next to someone. Measure before committing — a failed reach is not allowed, so you cannot Engage speculatively.

Breaking away costs a roll:

> COST OF DISENGAGE FROM MELEE LOCK: 1 AP
>
> To leave Melee Lock, roll a D6 against the enemy unit's melee strength. If the roll matches or beats that value, the unit breaks away and moves a distance equal to its movement range.
>
> If the roll is lower, the attempt fails. The unit stays where it is, and the enemy unit immediately attacks it in melee combat without spending AP. For this attack only, the unit that failed the check has its melee strength reduced by 1.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.15 — "DISENGAGING FROM MELEE LOCK"

> A unit in Melee Lock with several enemy units rolls one D6 against each of them in turn, and must succeed against every one to break away.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.15 — "DISENGAGING FROM MELEE LOCK"

> COST OF ESCAPE FROM MELEE: 2 AP
>
> Escape from Melee Lock works the same as Disengage from Melee Lock, but even if the roll fails and the enemy unit attacks, the unit still escapes and moves a distance equal to its movement range.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.15 — "ESCAPING FROM MELEE LOCK"

The failure penalty is severe and doubles up: you eat a **free** enemy attack *and* you defend it at **Melee Strength −1**, one fewer block die than normal. Locked against a strength-4 weapon you need a 4+, so a coin-flip that loses badly.

The choice between the two is a risk purchase. **Disengage** costs 1 AP and can strand you in place, taking a free hit, with your remaining AP possibly wasted. **Escape** costs 2 AP — your whole activation — and guarantees you leave, though a failed roll still gives the enemy its free swing. Escape when the model is valuable or nearly dead; Disengage when you can afford to fail and want the second AP for something else.

Multi-lock is the trap. Rolling against every locked enemy in turn and needing **all** of them to succeed makes a two-model lock roughly a 25–45% proposition depending on strengths. Do not let a key model get surrounded expecting to walk out later.

---

## Re-rolls in combat

> A re-roll is a chance to repeat an entire roll, not just one die. Each re-roll costs 1 re-roll point.
>
> In melee combat, the attacker can re-roll the hit check only before the defender rolls to block.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.23 — "RE-ROLL"

A re-roll is **all-or-nothing on the whole handful**, not a single die fix. Re-rolling four dice to save one bad result can easily make things worse — spend re-rolls when most of the roll failed, not when one die annoyed you.

The melee timing restriction is a real trap: once your opponent picks up their block dice, your hit check is locked. Decide before they roll, when you know only your own result.

Some weapons carry a free, targeted version of the same idea:

> WEAPON ABILITY: When rolling for armor penetration, re-roll each die that shows a 1 until it shows a higher value.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.5 — "UNIT ATTRIBUTES" (Volt Sword)

That one is per-die and free, which makes it strictly better than a re-roll point on the same check.

---

## Quick reference

| Situation | Modifier | Source page |
|-----------|----------|-------------|
| Target behind / beside partial cover | +1 Agility per interfering piece | p.11 |
| Shooter within 1" of the cover on the line | That piece does not interfere | p.12 |
| More than half target base visible past cover edge | No agility bonus | p.12 |
| Target behind a friendly unit | +1 Agility | p.12 |
| Any agility bonus | Caps at **5** | p.11–12 |
| Target behind full cover | Need ≥ 50% of base visible or no shot | p.8 |
| Weapon penetration `+N` | Target's effective armor **+N** (harder) | p.9 |
| Weapon penetration `−N` | Target's effective armor **−N** (easier) | p.9 |
| Penetration die shows 6 | Critical damage | p.10 |
| Sniper (Shade) | Target's agility **−1** when this unit shoots | p.36 |
| Failed Disengage | Free enemy attack; your melee strength **−1** for it | p.15 |

---

## Related pages

- [`Key_Concepts.md`](Key_Concepts.md) — condensed version of this page
- [`Activation_and_AP.md`](Activation_and_AP.md) — the AP that pays for all of this
- [`Equipment_Loot_and_Doors.md`](Equipment_Loot_and_Doors.md) — grenades, which ignore cover and agility entirely
- [`Rulebook_Quotes.md`](Rulebook_Quotes.md) — verbatim combat text and both worked examples
- [`../setup/Terrain_Basics.md`](../setup/Terrain_Basics.md) — what counts as partial vs full cover on your board

---

## Open questions

- Whether the defender in melee may re-roll its **block** dice with a re-roll point — the rules restrict the *attacker's* hit re-roll but say nothing about the defender.
- Whether a defender with 0 remaining AP still rolls block dice (the text implies defence is free, but never states it).
- Whether Overwatch triggers once per enemy action or once per enemy unit within a round — one firing removes the token, so in practice once.
- Whether melee range longer than 1" changes the base-contact definition of Melee Lock, or only the radius.
- Whether the Smasher's 1" lock ability also blocks the cheap 1 AP walk-out for enemies not in base contact — the wording implies yes.

---

## Change Log

- v0.1 (2026-08-23): Initial combat deep-dive from beta v0.8.7-F extract, including both worked examples and the full cover modifier set.

## Attribution

- Project: Wargame_Concierge
- Maintainer: Russell Catt
- The Warcode is property of RedMakers. Unofficial, unauthorized personal learning notes — never for sale.

## Rising Tide Notes

- This document follows Rising Tide documentation standards.
- Agility gates the hit, Armor gates the wound, and a 6 always hurts more.
