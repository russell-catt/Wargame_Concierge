<!--
FILE: games/the_warcode/rules/Key_Concepts.md
VERSION: v0.1 (2026-08-23)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, warcode_tactical_doctrine)

DOCUMENT_TYPE: Teaching Guide / Core Mechanics
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: The Warcode
REFERENCE_STATUS: Active — draft, beta v0.8.7-F (2026-08-23)

SOURCES:
  - raw/the_warcode/The Warcode Rulebook V.0.8.7-F.pdf (read via extract 2026-08-23)
  - raw/the_warcode/rulebook_v087f_extract.txt

PURPOSE:
  Explain the mechanics everything else is built from: unit stats, AP economy,
  shooting and melee resolution, cover, overwatch, equipment, contracts, and
  re-rolls.

PRIMARY_AUDIENCE:
  - A beginner who knows turn order and needs dice resolution
  - Cross-game readers mapping Murder Platoon habits to The Warcode

KEY_SECTIONS_EXPECTED:
  - Reading a unit profile
  - Action Points
  - Shooting sequence
  - Melee and Melee Lock
  - Cover and line of sight
  - Overwatch
  - Equipment
  - Contracts and re-rolls

UPDATE_TRIGGER:
  Update when beta supersedes v0.8.7-F on combat resolution, cover, or scoring.
-->

# Key Concepts — the mechanics everything else sits on

Learn these and weapon profiles become readable. **`confidence: draft`**, beta **v0.8.7-F**, read **2026-08-23**. Verbatim passages: [`Rulebook_Quotes.md`](Rulebook_Quotes.md).

---

## Reading a unit profile

Every unit shows four core characteristics, then weapon lines:

| Stat | Meaning |
|------|---------|
| **HP (Health)** | Wound pool. Each damage removes 1 HP. At **0 HP**, remove the model. |
| **A (Agility)** | Difficulty to hit in **both** shooting and melee — attackers must meet or beat this on each die. |
| **Armor** | Base value for **armor penetration checks** against this unit. |
| **M (Movement Range)** | Inches moved for **1 AP** of normal movement. |

Movement speed bands: **Slow 5"**, **Standard 6"**, **Fast 7"** per 1 AP move.

Each **weapon profile** lists range, shots or melee strength, shoot/reload or melee AP costs, ammo (ranged), armor penetration modifier, normal damage, and critical damage. Some weapons add **weapon abilities** (for example, re-roll penetration dice showing 1).

**Leader** units grant **2 re-roll points** at the start of each round while alive.

---

## Action Points (AP)

- Each unit gets **2 AP** when activated in a round.
- Every action costs AP from its profile **except**:
  - Picking up ground equipment (must be within 1 inch)
  - Opening/closing doors (must be within 1 inch of the doorway)
  - Using a medkit (0 AP)
- Some friendly abilities grant **extra AP** to another unit — spend it in the same round.
- **Pass** ends the activation without spending remaining AP and **does not** trigger Overwatch.

---

## Movement penalties

Measure from the unit's base edge with an inch ruler.

| Obstacle | Penalty |
|----------|---------|
| **Partial cover** | −1" from Movement Range when moving **through** it |
| **Friendly unit** | −2" when moving **through** a friendly |
| **Full cover (wall)** | Impassable — plan routes around it |

If movement would end **on** a friend or partial cover, place the unit **in front of** the obstacle. If you cannot legally stop within range because of stacking penalties, place as far as allowed along the path, adjacent to what blocked you.

When moving near full cover with a friend in between: you need **≥ 1 inch** between you and the wall unless you are treating the move as **through** the friend (−2").

---

## Shooting — step by step

When a unit **Shoots**, walk this sequence (see rulebook worked example on p.20):

1. **Ammunition** — need at least **1** ammo remaining.
2. **AP** — pay the weapon's shoot AP cost.
3. **Range** — measure from shooter base to target base; must be within weapon range.
4. **Line of sight** — target must be visible; full cover needs **≥ 50% of target base** visible (e.g. 14 mm of a 28 mm base).
5. **Hit check** — roll dice equal to **Number of Shots**. Each die that rolls **≥ target Agility** (after cover modifiers) hits.
6. **Effective armor** — start from target Armor, then apply weapon penetration: **+** adds to armor (harder to pierce), **−** subtracts (easier to pierce), **0** leaves armor unchanged.
7. **Penetration check** — for each hit, roll ≥ effective armor to penetrate.
8. **Damage** — on each penetrating hit, **6 = critical damage** value; any other result = normal damage value. Subtract total from target HP.

After shooting, reduce ammo by **1** (track with tokens).

### Cover affecting shooting

- **Partial cover** between shooter and target: **+1 Agility** per interfering piece on the line of fire ( **Agility caps at 5** ).
- Shooter within **1 inch** of a partial-cover piece on the line: that piece **does not interfere**.
- Target **behind** partial cover: +1 Agility if not more than half the base is visible past the edge.
- Target **behind a friendly**: +1 Agility (still capped at 5); no shot if **< 50%** of target base is visible.

> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.11 — "PARTIAL COVER"

---

## Reloading

Pay the weapon's **reload AP cost**. Ammo resets to the profile maximum. Can trigger enemy Overwatch if the unit is in an enemy's overwatch range.

---

## Overwatch

- **Cost:** 1 AP, at least 1 ammo, **not in melee range** of an enemy.
- Place an **Overwatch token** — the unit takes **no other actions** this round.
- If an enemy in range performs a qualifying action, the overwatching unit **shoots first** (normal shooting rules), then removes its token.
- Qualifying enemy actions: **Shoot, Move, Melee combat, Disengage, Escape, Use equipment, Reload** — and **Engage** (overwatch fires, then melee proceeds).
- Overwatch **does not** trigger if the enemy moves behind full cover out of line of sight, or on **Pass**.
- Overwatch ends when the unit **fires**, **takes damage**, or the **round ends**.

---

## Melee combat

Melee is **not** the same dice flow as shooting.

1. **AP check** — pay melee AP (often after a 1 AP move into range).
2. **Agility** — attacker must roll ≥ target Agility on each attack die.
3. **Attacker rolls** dice equal to **Melee Strength** — each die is an attack value.
4. **Defender rolls** dice equal to its **Melee Strength** — each die can block one attack if the defender's die is **≥** the attacker's die value.
5. **Unblocked hits** proceed to **armor penetration** (same +/- modifier math as shooting).
6. **Damage** — 6 on penetration = critical damage; otherwise normal damage.

### Melee radius vs Melee Lock

- **Melee range** (usually 1 inch) is a **radius** around a unit. Enemies inside cannot shoot or take most actions except melee or leaving the radius.
- **Melee Lock** occurs when **bases touch**. Locked units cannot simply walk away — they must **Disengage** (1 AP) or **Escape** (2 AP).

**Disengage:** Roll D6 vs each locked enemy's Melee Strength; need **≥** to break free, then move your full Movement Range. On failure, you stay put and the enemy **immediately** attacks you in melee (no AP spent) with your melee strength **−1** for that defense.

**Escape:** Same roll, but you **always** move your Movement Range afterward even if the roll fails (enemy still counter-attacks on failure).

**Engage (2 AP):** Move up to **Movement Range + 2 inches** toward a target; if you reach the base, you enter melee. Normal move penalties apply.

---

## Equipment

Before the game, each player spends **4 equipment points**:

| Item | Cost | Use |
|------|------|-----|
| **Grenade** | 2 pts | Throw (1 AP) up to 5"; 2" blast; 2 dice per model in blast; ignores partial cover and Agility |
| **Medkit** | 2 pts | Restore **2 HP** (not above max) on self or friendly within 1"; **0 AP**; one use |

Default: **one** equipment piece per unit unless special rules say otherwise (some units start with two grenades and take no other gear).

Dropped gear stays where the carrier died; any unequipped unit within 1 inch can pick it up for **0 AP**.

---

## Victory Points and Contracts

**VP tokens:** End of round, if your unit is within **1 inch** and no enemy is in that radius, you score the token's VP. Both sides present → **contested**, no score.

**Contracts:** At end of any round where you trail by **≥ 1 VP**, draw one contract secretly. It names a target unit from the opponent's faction. If that unit dies (any cause), reveal the card and gain its VP, then discard. If the named unit is already dead, show the card, bottom the deck, redraw.

---

## Re-rolls

- **1 re-roll point** = repeat an **entire roll**, not a single die.
- **Gain 2** at round start while your **Leader** lives; **+1** immediately when **your** unit is killed.
- Cannot re-roll **initiative** or **event card** rolls.
- In melee, the attacker may re-roll the **hit check only** before the defender rolls blocks.

---

## Related pages

- [`Turn_Structure.md`](Turn_Structure.md) — when these mechanics fire in the round
- [`Keyword_Glossary.md`](Keyword_Glossary.md) — one-line term lookup
- [`Rulebook_Quotes.md`](Rulebook_Quotes.md) — verbatim combat and cover text
- [`Contract_Cards_Reference.md`](Contract_Cards_Reference.md) — contract Target names by faction
- [`Protocol_Cards_Reference.md`](Protocol_Cards_Reference.md) — end-of-round protocol effects
- [`../setup/Terrain_Basics.md`](../setup/Terrain_Basics.md) — cover and doors on the board

---

## Open questions

- Whether weapon abilities beyond the penetration re-roll appear on all factions — extract shows examples only.
- Protocol target **room** for non-Total cards — **Map section** is printed on each card; rules extract does not define a separate room draw.

---

## Change Log

- v0.2 (2026-08-25): Cross-links to card reference pages (S8).
- v0.1 (2026-08-23): Initial key concepts from beta v0.8.7-F extract.

## Attribution

- Project: Wargame_Concierge
- Maintainer: Russell Catt
- The Warcode is property of RedMakers. Unofficial teaching paraphrase.

## Rising Tide Notes

- This document follows Rising Tide documentation standards.
- Run the shooting example on p.20 of the PDF once with dice — it clicks faster than reading alone.
