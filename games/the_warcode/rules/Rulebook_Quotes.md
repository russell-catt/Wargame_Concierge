<!--
FILE: games/the_warcode/rules/Rulebook_Quotes.md
VERSION: v0.1.1 (2026-08-25)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, warcode_tactical_doctrine)

DOCUMENT_TYPE: Quote Appendix / Verbatim Rules Reference
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: The Warcode
REFERENCE_STATUS: Active — draft, beta v0.8.7-F (2026-08-23)

SOURCES:
  - raw/the_warcode/The Warcode Rulebook V.0.8.7-F.pdf (free public beta, RedMakers; retrieved 2026-08-23)
  - raw/the_warcode/rulebook_v087f_extract.txt (native text extract)
  - raw/the_warcode/protocol_cards.ocr.txt (Protocol Cards, via OCR)
  - raw/the_warcode/contract_cards_transcription.txt (Contract Cards, via typed transcription)
  - raw/the_warcode/protocol_cards_transcription.txt (Protocol Cards room variants, via typed transcription)
  - raw/the_warcode/spreadsheets/Warcode_Contract_Protocol_list.xlsx (owner spreadsheet source)

PURPOSE:
  Single verbatim reference surface for The Warcode free beta rulebook. Every
  block carries filename + page + section so a teaching page can paraphrase
  freely and point here for the exact wording.

PRIMARY_AUDIENCE:
  - A player settling a rules argument mid-game
  - An author writing teaching pages who needs the source wording

KEY_SECTIONS_EXPECTED:
  - Setup and game phases
  - Activation, AP, VP
  - Unit attributes and movement
  - Ranged combat, cover, Overwatch
  - Melee combat, Engage, Melee Lock
  - Equipment, grenades, medkits, doors
  - Worked examples
  - Contracts and re-rolls
  - Scenario, VP placement, Protocol Cards
  - Team lists (Protagen Marines, Ulfari)

UPDATE_TRIGGER:
  A newer free beta supersedes v0.8.7-F on any quoted topic, or a cleaner OCR
  pass replaces the Protocol Card / team list reconstructions.
-->

# Rulebook Quotes — The Warcode beta v0.8.7-F

Verbatim reference for the free public beta. **`confidence: draft`**, read **2026-08-23**.

Quoting is permitted here under `AGENTS.md` Sec 10 — The Warcode beta is a **free public distribution from RedMakers**, not a paid or protected pack. This subtree is **unofficial and unauthorized**. Teaching paraphrase lives in [`Key_Concepts.md`](Key_Concepts.md) and the deep-dive pages; this file is the wording those pages point at.

---

## How to read the citations

Every block ends with:

`Source: The Warcode Rulebook V.0.8.7-F.pdf — p.{N} — "{SECTION}"`

**`p.{N}` is the PDF file page** (the `===== PAGE N =====` marker in the extract), not the printed page number stamped in the page corner. The printed number runs one lower — PDF p.4 carries the printed "3". This matches the citation style already used in [`Turn_Structure.md`](Turn_Structure.md) and [`Key_Concepts.md`](Key_Concepts.md).

Blocks marked **via OCR** were read from rendered page images because the page is card art with no extractable text layer. Those cite [`protocol_cards.ocr.txt`](../../../raw/the_warcode/protocol_cards.ocr.txt) alongside the PDF page.

### Transcription notes

The native extract is column-flattened, so a printed paragraph arrives as a stack of short lines interleaved with diagram labels. In the blocks below:

- **Line wrapping is rejoined** into running sentences. No words are added, removed, or reordered.
- **Ligatures normalized** — the extract's `ﬁ` renders here as `fi` (`ﬁre` → `fire`).
- **Diagram callouts** (`Unit 1`, `6 inches`, `Partial cover`, `Full Cover (Wall)`) are omitted from prose blocks and summarized separately where they carry rules meaning.
- **Numeric profile values** on stat-card pages are scrambled by the flattening. Those are presented as **reconstructed tables**, clearly labeled, not as quotes.
- `[sic]` marks a typo present in the source.

---

## 1. Setup

> **SETUP**
>
> 1. READ THE SCENARIO — It sets out your objectives, the victory conditions, and any special rules.
> 2. DEPLOY UNITS — Roll a D6 to see who deploys first, then take turns placing one unit each.
> 3. DISTRIBUTE EQUIPMENT — Once all units are deployed, use your equipment points to arm them.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.2 — "SETUP"

The same page carries the table of contents, which is the cleanest available list of what the rulebook covers:

> SETUP · GAME PHASES · GAME PHASES OVERVIEW · UNIT ACTIVATION · ACTION POINTS (AP) · VICTORY POINTS (VP) · UNIT ATTRIBUTES · HEALTH · AGILITY · ARMOR · MOVEMENT RANGE · MOVEMENT · RANGED WEAPONS · SHOOTING RANGE · NUMBER OF SHOTS · ACTION POINTS (AP) FOR SHOOTING · AMMUNITION · ACTION POINTS (AP) FOR RELOADING · ARMOR PENETRATION · DAMAGE · CRITICAL DAMAGE · OVERWATCH · SHOOTING THROUGH FRIENDLY UNITS · MELEE WEAPONS · MELEE RANGE · MELEE STRENGTH · ACTION POINTS (AP) FOR MELEE COMBAT · ARMOR PENETRATION · MELEE DAMAGE · MELEE CRITICAL DAMAGE · SPECIAL FEATURES · ENGAGE · MELEE RADIUS IMPACT · MELEE COMBAT · MELEE LOCK · DISENGAGING FROM MELEE LOCK · ESCAPING FROM MELEE LOCK · EQUIPMENT · GRENADE · GRENADE THROW EXAMPLE · MEDKIT · ITEM PICKUP · OPENING AND CLOSING DOORS · DOOR BLOCKING · SHOOTING EXAMPLE · MELEE COMBAT EXAMPLE · CONTRACTS · RE-ROLL
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.2 — "CONTENTS"

---

## 2. Game phases

> The game is divided into rounds, each consisting of two phases:
>
> 1. INITIATIVE PHASE
> 2. TACTICAL PHASE
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.3 — "GAME PHASES"

> INITIATIVE PHASE: Roll a D6 to see who goes first. The player with the highest roll takes the first turn that round. In the first round, roll before deploying units to determine both the deployment order and who goes first. If there's a tie, both players re-roll until one wins.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.3 — "INITIATIVE PHASE"

> TACTICAL PHASE: Activate units and perform actions during this phase.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.3 — "TACTICAL PHASE"

> END OF THE ROUND: After the Tactical Phase, apply all unit effects that activate at the end of the round, then apply scenario effects (if any), and calculate Victory Points (VP).
>
> NEW ROUND: Start a new round following the same phases.
>
> FINAL ROUND: If this was the final round, determine the winner based on the conditions specified in the scenario.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.3 — "END OF THE ROUND"

The p.3 "GAME PHASES OVERVIEW" diagram sequences the round as: **SETUP** → **DEPLOYMENT** → **INITIATIVE PHASE (1)** → **TACTICAL PHASE (2)** → **END OF ROUND**, with End of Round expanded into **ACTIVATION OF END-OF-ROUND ABILITIES** → **ACTIVATION OF SCENARIO EVENT CARDS** → **VP CALCULATION**.

> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.3 — "GAME PHASES OVERVIEW"

---

## 3. Unit activation

> Each player takes turns activating one unit.
>
> Once activated, a unit with the corresponding token can perform actions using Action Points (AP):
>
> MOVE
> SHOOT
> RELOAD
> OVERWATCH
> MELEE COMBAT (if there are enemy units within melee range)
> ENGAGE
> DISENGAGE FROM MELEE LOCK (if the unit is within the melee range of an enemy unit)
> USE ABILITY (if the unit has an ability)
> USE EQUIPMENT (if the unit has equipment)
> INTERACT WITH MAP OBJECTS (e.g., doors)
> PASS (skipping a turn without triggering Overwatch)
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.4 — "UNIT ACTIVATION"

> After performing an action, flip the activation token to indicate that the unit can no longer perform actions in this round. At the start of a new round, flip all tokens back to the side to indicate that the unit can be activated.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.4 — "UNIT ACTIVATION"

Token faces on the same page read **"THE UNIT CAN BE ACTIVATED IN THIS ROUND."** and **"THE UNIT HAS ALREADY BEEN ACTIVATED IN THIS ROUND."**

---

## 4. Action Points (AP)

> Each unit has 2 Action Points (AP). Every action costs a specific number of AP (except for picking up items from the ground and opening/closing doors, which have special rules).
>
> Some units have abilities that give extra AP to another friendly unit.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.4 — "ACTION POINTS (AP)"

---

## 5. Victory Points (VP)

> Victory Points (VP) are earned by capturing points on the map and completing contracts. At the end of the game, the player with the most VP wins.
>
> VP tokens indicate the number of VP a player receives at the end of a round.
>
> To capture a VP, a unit must be within 1 inch of the VP token with no enemy units in that radius. If both allied and enemy units are present within this radius at the end of the round, the point becomes contested, and no player receives VP from it.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.4 — "VICTORY POINTS (VP)"

Diagram captions on the same page:

> In this example, Unit 1 is allied and controls the point.
>
> In this example, Unit 1 is allied, and Units 2 and 3 are enemies. This point is contested.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.4 — "VICTORY POINTS (VP)"

---

## 6. Unit attributes

> HEALTH, AGILITY, ARMOR, AND MOVEMENT RANGE are the main attributes of a unit. The parameters for the unit's ranged and melee weapons are listed below these primary attributes.
>
> THESE CONSTITUTE THE CORE CHARACTERISTICS OF A CHARACTER.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.5 — "UNIT ATTRIBUTES"

### Health

> The health value shows the number of health points the unit has. One point of damage removes one health point. When the health value drops to zero, the unit is killed, and its model is removed from the field.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.5 — "HEALTH"

### Agility

> The agility value shows how difficult it is to hit the unit in ranged and melee combat, and is used when making hit checks against the unit.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.5 — "AGILITY"

### Armor

> The armor value shows how difficult it is to penetrate the unit's armor in ranged and melee combat, and is used when making armor penetration checks against the unit.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.5 — "ARMOR"

### Movement Range

> The Movement Range value shows the maximum distance the unit can move in inches for 1 AP.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.5 — "MOVEMENT RANGE"

The sample card on p.5 is **COMMANDER RICKMAN** at **9 HP / 3 Agility / 6 Movement / 4 Armor**, carrying a **PISTOL** and a **VOLT SWORD**, with:

> WEAPON ABILITY: When rolling for armor penetration, re-roll each die that shows a 1 until it shows a higher value.
>
> LEADER: The player gains 2 re-roll points at the start of each round.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.5 — "UNIT ATTRIBUTES" (sample card)

---

## 7. Movement

> Movement is measured using an inch ruler. The standard movement distance for 1 AP is 6 inches. Measurement is taken from the base of the unit, which is placed at the edge of the point up to 6 inches away.
>
> Each unit has one of three Movement Ranges:
>
> SLOW: 5 INCHES
> STANDARD: 6 INCHES
> FAST: 7 INCHES
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.6 — "MOVEMENT"

### Moving through a friendly unit

> To move through a friendly unit, subtract 2 inches from the Movement Range.
>
> Example of moving through a friendly unit: Subtracting the 2-inch penalty from the standard Movement Range of 6 inches leaves 4 inches of movement through the friendly unit.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.6 — "MOVEMENT"

### Moving through partial cover

> To move through partial cover, subtract 1 inch from the Movement Range.
>
> Example of moving through partial cover: Subtract the 1-inch penalty from the standard Movement Range of 6 inches. That leaves 5 inches of movement through partial cover.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.6 — "MOVEMENT"

### Squeezing between a friendly unit and a wall

> If Unit 1 needs to move between a friendly Unit 2 and full cover (a wall), the distance between Unit 1 and the cover must be at least 1 inch. If the distance between Unit 2 and the cover is less than 1 inch, this movement counts as moving through a friendly unit.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.6 — "MOVEMENT"

### Where the model ends up

> If movement would end on a friendly unit or partial cover, place the unit directly in front of the obstacle.
>
> If the movement ends beyond a friendly unit or partial cover, and it's not possible to place the unit within 4 or 5 inches, place it farther than 4 or 5 inches, next to the friendly unit or partial cover that blocked the movement.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.7 — "MOVEMENT"

---

## 8. Ranged weapons

> There are various types of ranged weapons, each with its own parameters and special features.
>
> Every weapon profile includes its range, number of shots, ammunition capacity, AP cost for shooting, AP cost for reloading, armor penetration strength, damage per shot, and critical damage per shot.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.7 — "RANGED WEAPONS"

### Shooting range

> The range is measured using an inch ruler. Each ranged weapon profile has its own shooting range, measured from the base of the unit. If the measurement reaches the base of the Target, it is considered within range, and the unit can open fire, provided the Target is in line of sight and nothing blocks the shot.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.8 — "SHOOTING RANGE"

### Line of sight past full cover

> If the Target is behind full cover (impassable terrain such as walls, columns, etc.), shooting is possible only if 50% of the Target's base is in direct line of sight.
>
> For example, a 28mm base needs at least 14mm visible to the shooting unit.
>
> Here, only Unit 1 has a direct line of sight to the Target and can open fire.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.8 — "SHOOTING RANGE"

### Number of shots

> The number of shots shows how many dice to roll for the shooting check.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.8 — "NUMBER OF SHOTS"

### AP for shooting

> The number of AP shows the amount of AP needed to perform the shooting action.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.8 — "ACTION POINTS (AP) FOR SHOOTING"

---

## 9. Ammunition and reloading

> After shooting, subtract 1 from the indicated ammunition capacity value. For example, a weapon with 3 ammunition has 2 remaining after firing. Place a corresponding ammunition token next to the unit to track how much ammunition is left. The unit must always have at least 1 ammunition to perform the shooting action. Subtract 1 from the current ammunition value after each shooting action. If the ammunition value is 0, the unit cannot shoot until it reloads.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.9 — "AMMUNITION"

Token captions on the same page read **"THE UNIT HAS 2 POINTS OF AMMUNITION LEFT"**, **"THE UNIT HAS 1 POINT OF AMMUNITION LEFT"**, **"THE UNIT HAS 0 POINTS OF AMMUNITION LEFT"**.

> To reload, spend the amount of AP specified for reloading. The weapon's ammunition is then restored to the maximum value indicated in its ammunition parameter.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.9 — "ACTION POINTS (AP) FOR RELOADING"

---

## 10. Armor penetration and damage (ranged)

> The armor penetration strength of a weapon is calculated based on its armor penetration value.
>
> A value with a "+" sign means you need to add the weapon's armor penetration value to the Target's armor value.
>
> A value with a "-" sign means you need to subtract the weapon's armor penetration value from the Target's armor value.
>
> A value with a "0" sign means you don't need to add or subtract anything from the Target's armor value.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.9 — "ARMOR PENETRATION"

> For example, if the Target has an armor value of 4 and the weapon has an armor penetration of +1, add 1 to the Target's armor value of 4. When shooting with this weapon, the Target's effective armor value becomes 5, so the weapon is less effective at penetrating armor.
>
> By contrast, if the weapon's armor penetration is -2, subtract 2 from the Target's armor value. When shooting with this weapon, the Target's effective armor value becomes 2, so the weapon is more effective at penetrating armor.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.9 — "ARMOR PENETRATION"

> The standard damage value shows the amount of damage inflicted by a shot that successfully hits and penetrates armor.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.9 — "DAMAGE"

> The critical damage value shows the amount of damage inflicted by a shot that rolled a 6 on the damage check.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.10 — "CRITICAL DAMAGE"

---

## 11. Overwatch

> A unit in Overwatch mode holds its fire and waits. If an enemy unit moves into its shooting range, or takes action while already inside that range, the Overwatch unit opens fire before the enemy unit completes its action.
>
> To activate Overwatch, a unit must spend 1 AP, have at least 1 ammunition, and be outside melee range of an enemy unit. To show that a unit is in Overwatch mode, place an Overwatch token next to it. Once the token is placed, the unit cannot take any other action for the rest of the round.
>
> A unit leaves Overwatch mode as soon as it fires or takes damage. After that, its token needs to be removed. Any units still in Overwatch at the end of the round leave it as well, and all remaining tokens are removed.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.10 — "OVERWATCH"

### What triggers Overwatch

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

### Overwatch worked cases

> Unit 1 is in Overwatch mode, and Target enters Unit 1's shooting range. Target stops because Unit 1 opens fire. After Unit 1 shoots, the Overwatch token is removed, and Target can continue its actions.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.10 — "OVERWATCH"

> Unit 1 is in Overwatch mode, and Target is already within Unit 1's shooting range when it declares an action (e.g., opening fire on Unit 1 or starting movement). Unit 1 opens fire before Target acts. After Unit 1 shoots, the Overwatch token is removed, and Target can perform its previously declared action.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.10 — "OVERWATCH"

> Unit 1 is in Overwatch mode. Target uses Engage. Unit 1 opens fire on Target first, then the Overwatch token is removed, and Target enters melee combat.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.11 — "OVERWATCH"

> Unit 1 is in Overwatch mode. Target starts moving and enters Unit 1's shooting range but stops behind full cover (impassable terrain). Under the normal shooting rules, Target is not in Unit 1's line of sight, so the movement does not trigger Overwatch. Target then throws a grenade, dealing damage to Unit 1. Unit 1 has taken damage, so the Overwatch token is removed and Unit 1 is no longer in Overwatch mode.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.11 — "OVERWATCH"

---

## 12. Partial cover

> Partial cover is any terrain object on the field that does not exceed the height of the units. Objects taller than the units count as full cover and are impassable. To move through partial cover, subtract 1 inch from the Movement Range. When shooting at a Target behind partial cover, or with partial cover on the line of fire, the Target's agility increases by 1 for each piece on that line.
>
> A unit's agility cannot exceed 5, regardless of the number of bonuses applied.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.11 — "PARTIAL COVER"

> Unit 1 opens fire on Target, which is behind partial cover. Target's agility without cover is 3, so in this case, its agility becomes 4.
>
> Unit 1 opens fire on Target. It is not behind partial cover, but partial cover is on the line of fire, so Target's agility still increases by 1.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.11 — "PARTIAL COVER"

### Shooting from behind or beside partial cover

> If partial cover stands between a shooting unit and its Target, and the unit is within 1 inch of that cover, the unit counts as being behind it and can shoot without interference.
>
> When shooting through partial cover, measure the distance to the cover in the direction of the Target. If the cover is within 1 inch, it does not interfere with the shot.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.12 — "PARTIAL COVER"

> If more than half of the Target's base is visible past the edge of the partial cover, the Target does not count as being behind it and receives no agility bonus.
>
> On a 28mm base, that means more than 14mm visible to the shooting unit.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.12 — "PARTIAL COVER"

> Unit 1 opens fire on Target. Target is not behind partial cover, but two pieces of partial cover are on the line of fire. Unit 1 is within 1 inch of piece 1, so piece 1 does not interfere with the shot. However, piece 2 does interfere and grants an agility bonus to Target.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.12 — "PARTIAL COVER"

> Unit 1 can shoot at both Target 1 and Target 2. The cover does not interfere with the shot at Target 1, but interferes with the shot at Target 2, because it is more than 1 inch away.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.12 — "PARTIAL COVER"

---

## 13. Shooting through friendly units

> A Target behind a friendly unit can still be shot at, but its agility increases by 1. A unit's agility cannot exceed 5, regardless of the number of bonuses applied. A Target with a base agility of 5 receives no bonus.
>
> Friendly fire will not occur if 50% of the Target's base is in direct line of sight. For example, a 28mm base needs at least 14mm visible to the shooting unit.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.12 — "SHOOTING THROUGH FRIENDLY UNITS"

---

## 14. Melee weapons

> There are various types of melee weapons, each with its own parameters and, in some cases, special features. Every weapon profile includes its melee range, melee strength, AP cost for melee combat, armor penetration strength, damage per hit, and critical damage per hit.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.13 — "MELEE WEAPONS"

### Melee range

> The range is measured using an inch ruler. Each melee weapon profile has its own melee range, measured from the base of the unit. If the measurement reaches the base of the Target, it is considered within melee range.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.13 — "MELEE RANGE"

### Melee strength

> Melee strength shows the number of attacks, meaning how many dice to roll in melee combat. The defender rolls dice equal to its melee strength when blocking those attacks. Melee strength also indicates the value the opponent must roll on a single die to disengage from Melee Lock.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.13 — "MELEE STRENGTH"

### AP for melee combat

> The number of AP shows the amount of AP needed to perform melee combat.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.13 — "ACTION POINTS (AP) FOR MELEE COMBAT"

### Armor penetration (melee)

> The armor penetration strength of a weapon is calculated based on its armor penetration value.
>
> A value with a "+" sign means you need to add the weapon's armor penetration value to the Target's armor value.
>
> A value with a "-" sign means you need to subtract the weapon's armor penetration value from the Target's armor value.
>
> A value with a "0" sign means you don't need to add or subtract anything from the Target's armor value.
>
> For example, if the Target in melee combat has an armor value of 4 and the weapon has an armor penetration of +1, add 1 to the Target's armor value of 4. When engaging in melee combat with this weapon, the Target's effective armor value becomes 5, so the weapon is less effective at penetrating armor. By contrast, if the weapon's armor penetration is -1, subtract 1 from the Target's armor value of 4. When engaging in melee combat with this weapon, the Target's effective armor value becomes 3, so the weapon is more effective at penetrating armor.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.13 — "ARMOR PENETRATION"

### Melee damage and critical damage

> The standard damage value shows the amount of damage inflicted by a hit that successfully passes both the hit and armor penetration checks.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.14 — "MELEE DAMAGE"

> The critical damage value shows the amount of damage inflicted by a hit that rolled a 6 on the damage check.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.14 — "MELEE CRITICAL DAMAGE"

### Special features

> Melee weapons may have additional special features. If a weapon has special features, they are described below its main parameters.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.14 — "SPECIAL FEATURES"

---

## 15. Engage

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

---

## 16. Melee radius impact

> The melee range value also acts as a radius around the unit. Enemy units inside that radius are automatically in melee combat with that unit. They cannot shoot or perform other actions, except taking part in melee combat or using movement to leave the melee radius.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.14 — "MELEE RADIUS IMPACT"

> Unit 1 is in melee combat with Target 1 and Target 2 — in Melee Lock with Target 1, and in ordinary melee combat with Target 2. All three units can only fight in melee or leave melee combat. Target 2 can leave using ordinary movement. Unit 1 and Target 1 are in Melee Lock because their bases touch, so they can leave only by using Disengage or Escape from Melee Lock. No other actions are available to these units while they are engaged in melee combat.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.14 — "MELEE RADIUS IMPACT"

---

## 17. Melee combat and Melee Lock

> Melee combat begins when two or more enemy units enter the melee radius, which is usually 1 inch. Inside the melee radius, units cannot use ranged weapons, equipment, or any abilities that melee combat blocks. To leave melee combat, spend 1 AP on movement and move out of the melee radius. Melee Lock is the exception: leaving it requires Disengage or Escape from Melee Lock.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.15 — "MELEE COMBAT"

> Two units are in Melee Lock when their bases touch. A unit can be in Melee Lock with several enemy units at once.
>
> Melee Lock follows the same rules as melee combat, but it is harder to leave: instead of simply moving out, a unit must use Disengage or Escape from Melee Lock.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.15 — "MELEE LOCK"

### Disengaging from Melee Lock

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

> Unit 1 is in melee combat with Target 1 and Target 2, but in Melee Lock only with Target 1, whose melee strength is 4. Unit 1 rolls one D6 and needs a 4 or higher to break away. No roll is needed against Target 2, since their bases do not touch.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.15 — "DISENGAGING FROM MELEE LOCK"

### Escaping from Melee Lock

> COST OF ESCAPE FROM MELEE: 2 AP
>
> Escape from Melee Lock works the same as Disengage from Melee Lock, but even if the roll fails and the enemy unit attacks, the unit still escapes and moves a distance equal to its movement range.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.15 — "ESCAPING FROM MELEE LOCK"

---

## 18. Equipment

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
> If a unit carrying equipment is killed, the token stays on the ground where it died, and any unit without equipment of its own can pick it up.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.16 — "EQUIPMENT"

---

## 19. Grenades

> COST OF THROWING A GRENADE: 1 AP
>
> A grenade can be thrown up to 5 inches, measured from the base of the throwing unit. Place the token at any point within that distance.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.16 — "GRENADE"

> If the throw ends on an enemy unit, friendly unit, or partial cover, the token is always placed at a shorter distance, meaning less than 5 inches.
>
> If the throw ends beyond an enemy unit, friendly unit, or partial cover, and the token cannot be placed within 5 inches, place it farther than 5 inches, next to the unit or cover that blocked the throw.
>
> The blast radius of the grenade is 2 inches, measured from the edge of the token.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.16 — "GRENADE"

### Resolving the blast

> To determine the damage from the explosion, roll 2 dice for each unit within the blast radius and compare the results with that unit's armor value.
>
> The grenade affects all units within its blast radius, including friendly units. A unit is within the blast radius if the measurement from the grenade token reaches its base. The grenade completely ignores partial cover and agility. Any unit within the blast radius immediately makes an armor penetration check.
>
> If a unit is behind full cover but within the blast radius, make a line of sight check as with shooting to determine whether the fragments reach it. The check is made from the grenade token instead of the shooting unit.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.17 — "GRENADE THROW EXAMPLE"

The grenade profile block on p.17 reads **range 5", 1 AP, 2 dice, armor penetration -1, damage 1, critical damage 2**, with a **2 inch** explosion radius.

> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.17 — "GRENADE" (profile block)

### Grenade worked cases

> Unit 1 throws a grenade. Unit 2 is within the blast radius and undergoes a check. Unit 3 is outside the blast radius and does not. Unit 4 is within the blast radius, but full cover stands between it and the grenade token. Less than 50% of Unit 4's base is visible from the token, so the fragments cannot reach it and Unit 4 undergoes no check.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.17 — "GRENADE THROW EXAMPLE"

> Unit 1 throws a grenade. Unit 2, Unit 3, and Unit 4 are within the blast radius, and all undergo a check, since the grenade completely ignores partial cover.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.17 — "GRENADE THROW EXAMPLE"

> Unit 1 throws a grenade. Unit 2 and Unit 3 are within the blast radius and need to make checks.
>
> Unit 2 and Unit 3 have an armor value of 4, and the grenade has an armor penetration of -1, so a roll of 3 or higher is needed to penetrate.
>
> Unit 2 takes no damage because its rolls are lower than 3.
>
> Unit 3 rolls 4 and 6. Both are 3 or higher, so the armor is penetrated twice. The 6 counts as critical damage. Unit 3 takes 3 damage in total: 1 point for the 4, which is the grenade's normal damage, and 2 points for the 6, which is critical damage.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.18 — "GRENADE THROW EXAMPLE"

---

## 20. Medkit

> A medkit restores 2 HP, but never above the unit's maximum HP. A unit with a medkit can use it on itself or on a friendly unit within 1 inch once during its activation. Using a medkit costs no AP. Each medkit works only once, so remove its token from the field after use.
>
> Unit 1 has a medkit and can use it on itself, on Unit 2, or on Unit 3, since both are within 1 inch.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.18 — "MEDKIT"

---

## 21. Item pickup

> When a unit carrying equipment is killed, its grenade or medkit stays on the ground where it fell. Any unit not already carrying equipment can pick it up.
>
> Picking up items costs no AP, but the unit must be within 1 inch of it.
>
> Unit 1 spends 1 AP to move within 1 inch of a grenade lying on the ground and picks it up for free. With its remaining AP, Unit 1 can throw the grenade or take any other action costing 1 AP.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.18 — "ITEM PICKUP"

---

## 22. Doors

> Opening or closing a door costs no AP, but the unit must be within 1 inch of the doorway. A unit farther away spends 1 AP to move within 1 inch first. Each unit can open or close a door only once per activation.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.18 — "OPENING AND CLOSING DOORS"

### Door blocking

> If a unit is within 1 inch of the doorway, the door is considered blocked. A unit from the opposing team cannot open or close a blocked door.
>
> If two or more units from different teams are within 1 inch of the same doorway, the door is considered blocked for everyone, and no unit can open or close it.
>
> This applies regardless of which side of the door each unit stands on.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.19 — "DOOR BLOCKING"

---

## 23. Worked example — shooting

Unit 1 (shotgun) fires at Target (**9 HP / 3 Agility / 6 Movement / 4 Armor**). The shotgun profile in the example is **2 shots, 5" range, 2 ammunition, 1 AP shoot, 1 AP reload, armor penetration -1, damage 3, critical damage 4**.

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

*(The extract duplicates the leading digit on several steps — "8 8. Check…" — an artifact of the numbered-callout art layer, not the printed text.)*

---

## 24. Worked example — melee combat

> Melee combat is different from shooting: both the armor and agility of the Target are involved, as well as its defense (the Target rolls dice equal to its melee strength).
>
> Unit 1 spends 1 AP to move into melee range of Target, and then spends another 1 AP to attack. Unit 1 attacks with a combat knife, while Target defends with a Volt Sword.
>
> WEAPON ABILITY: When rolling for armor penetratsion [sic], re-roll each die that shows a 1 until it shows a higher value.
>
> 1. Check that there is enough AP to attack. Unit 1 has just moved for 1 AP and has 1 AP remaining.
>
> 2. Check Target's agility. Roll 3 or higher to hit.
>
> 3. Unit 1, as the attacker, rolls dice equal to its melee strength. It has 2 dice, so Unit 1 makes 2 attacks with the combat knife.
>
> 4. Target, as the defender, rolls dice equal to its melee strength. It has 4 dice, so Target rolls 4 dice against those attacks.
>
> 5. Compare the values on the attacker's and defender's dice. Each attack can be blocked only by a die with a value that matches or exceeds the attacker's die value. Here, only the attack of 3 is blocked, since the defender has a die of equal or higher value. The attack of 5 is not blocked, so only one of the hits gets through.
>
> 6. Make an armor penetration check.
>
> 7. If the armor is penetrated, determine damage.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.21 — "MELEE COMBAT EXAMPLE"

Target in this example is **9 HP / 3 Agility / 6 Movement / 4 Armor** with a **Volt Sword** (melee strength 4). The attacker uses a **Combat Knife** (melee strength 2).

---

## 25. Contracts

> If the difference in VP between players is 1 or more at the end of any round, the player with the lower VP receives a contract.
>
> That player draws one contract card and looks at it secretly. The card specifies one unit name from each available faction, and the Target is the unit from the faction the opponent is playing. If that unit is already dead, the player shows the card to the opponent, places it at the bottom of the deck, and draws another.
>
> A contract is fulfilled once the Target is eliminated, whether by the player, by scenario events, or by any other means. The player announces it, shows the card to the opponent, adds the VP specified on the card to their score, and discards it.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.22 — "CONTRACTS"

> EXAMPLE: At the end of round 2, Player A has 2 VP and Player B has 3 VP. Before the start of round 3, Player A receives one contract. Player B is playing the Ulfari, so Player A's Target is the unit Shade. If Shade is eliminated by Player A or by any other means, Player A gains 1 VP.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.22 — "OBJECTIVES OF THE CONTRACT"

PDF pages 24 and 25 are titled **CONTRACTS** and carry card art with no extractable text layer. The eight contract faces below were transcribed from the printed cards **via typed transcription** — see [`contract_cards_transcription.txt`](../../../raw/the_warcode/contract_cards_transcription.txt) and [`Warcode_Contract_Protocol_list.xlsx`](../../../raw/the_warcode/spreadsheets/Warcode_Contract_Protocol_list.xlsx). Teaching table: [`Contract_Cards_Reference.md`](Contract_Cards_Reference.md).

Every card shares the same header and awards **1 VP** on fulfilment.

### Contract 4186

> You have received a contract. Eliminate the target designated by enemy faction.
>
> **1 VP**
>
> Protagen Marines — Commander Rickman  
> Ulfari — Soul Eater  
> MDR Executive Unit — Sergeant 139  
> Custodia Silens — Justicar Julius
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — pp.24–25 — "CONTRACTS" — via typed transcription (raw/the_warcode/contract_cards_transcription.txt)

### Contract 9278

> You have received a contract. Eliminate the target designated by enemy faction.
>
> **1 VP**
>
> Protagen Marines — Shellshocker  
> Ulfari — Phantom  
> MDR Executive Unit — Combat Medic  
> Custodia Silens — Cremator
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — pp.24–25 — "CONTRACTS" — via typed transcription (raw/the_warcode/contract_cards_transcription.txt)

### Contract 5039

> You have received a contract. Eliminate the target designated by enemy faction.
>
> **1 VP**
>
> Protagen Marines — Bastion  
> Ulfari — Reaper  
> MDR Executive Unit — Machine Gunner  
> Custodia Silens — Confessor
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — pp.24–25 — "CONTRACTS" — via typed transcription (raw/the_warcode/contract_cards_transcription.txt)

### Contract 6037

> You have received a contract. Eliminate the target designated by enemy faction.
>
> **1 VP**
>
> Protagen Marines — Blade  
> Ulfari — Shade  
> MDR Executive Unit — Grenadier  
> Custodia Silens — Punisher
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — pp.24–25 — "CONTRACTS" — via typed transcription (raw/the_warcode/contract_cards_transcription.txt)

### Contract 3697

> You have received a contract. Eliminate the target designated by enemy faction.
>
> **1 VP**
>
> Protagen Marines — Blast  
> Ulfari — Stalker  
> MDR Executive Unit — Comms Operator  
> Custodia Silens — Tormentor
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — pp.24–25 — "CONTRACTS" — via typed transcription (raw/the_warcode/contract_cards_transcription.txt)

### Contract 4913

> You have received a contract. Eliminate the target designated by enemy faction.
>
> **1 VP**
>
> Protagen Marines — Anvil  
> Ulfari — Doom  
> MDR Executive Unit — Corporal  
> Custodia Silens — Lancer
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — pp.24–25 — "CONTRACTS" — via typed transcription (raw/the_warcode/contract_cards_transcription.txt)

### Contract 3512

> You have received a contract. Eliminate the target designated by enemy faction.
>
> **1 VP**
>
> Protagen Marines — Smasher  
> Ulfari — Ravener  
> MDR Executive Unit — Marksman  
> Custodia Silens — Assassin
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — pp.24–25 — "CONTRACTS" — via typed transcription (raw/the_warcode/contract_cards_transcription.txt)

### Contract 2984

> You have received a contract. Eliminate the target designated by enemy faction.
>
> **1 VP**
>
> Protagen Marines — Hammer  
> Ulfari — Wraith  
> MDR Executive Unit — Private  
> Custodia Silens — Executor
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — pp.24–25 — "CONTRACTS" — via typed transcription (raw/the_warcode/contract_cards_transcription.txt)

---

## 26. Re-roll

> A re-roll is a chance to repeat an entire roll, not just one die. Each re-roll costs 1 re-roll point.
>
> Re-roll points come from two sources. A player whose Leader is alive gains 2 re-roll points at the start of each round, and stops gaining them once that unit is killed. A player also gains 1 point immediately each time one of their own units is killed.
>
> Re-roll points cannot be spent on the initiative roll, which decides who goes first in the round, or on event cards that call for a roll.
>
> In melee combat, the attacker can re-roll the hit check only before the defender rolls to block.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.23 — "RE-ROLL"

---

## 27. Scenario — «Core of the Machine»

> The action takes place inside a long-abandoned and heavily damaged space drifter. Your mission is to infiltrate and take full control of the ship. As soon as your team reaches the machine's core, it activates security protocols. However, due to severe damage, the machine cannot distinguish between friend and foe. You also discover that you are not alone. A countdown begins, and there isn't enough time to escape the ship. You need to reprogram the "core" to mark your team as "friendly" and the opposing team as "hostile," thereby activating automatic turrets to eliminate the enemy. If neither team succeeds in persuading the "core", both teams will be marked as "hostile" and will be destroyed when the time runs out.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.26 — "SCENARIO «CORE OF THE MACHINE»"

> GAMEPLAY MECHANICS:
>
> CORE OF THE MACHINE: At the start of each round, draw a random "Core of the Machine" activation card with negative effects for one or more of the three rooms (effect descriptions are on the card).
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.26 — "SCENARIO «CORE OF THE MACHINE»"

> Victory Conditions:
>
> 1. Eliminate all enemy units.
> 2. Accumulate more VP than the opponent to sway the "Core of the machine" to your side.
>
> If both teams have the same number of VP at the end of the game, everyone perishes as the "core" marks everyone as "hostile" and destroys them.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.26 — "SCENARIO «CORE OF THE MACHINE»"

Map legend on the same page:

> Deployment area - A
> Deployment area - B
> - Partial cover
> - Full Cover (Wall)
> - Door
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.26 — "SCENARIO «CORE OF THE MACHINE»"

---

## 28. Random VP placement

> RANDOM VP PLACEMENT
>
> The random VP placement system applies to all scenarios. Before the game begins, roll one D6. The result determines the VP placement for that game. The diagrams below use the scenario "Core of the Machine" as an example. BOARD SIZE 33'' X 24''
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.27 — "RANDOM VP PLACEMENT"

The page shows **six** labeled layouts (one per D6 result), each with **Deployment area - A** and **Deployment area - B**. The extract preserves the dimension callouts but not their placement, so the individual layouts cannot be reconstructed from text. Recurring measurements in the flattened list include **33''**, **24''**, **16,5''**, **14''**, **13''**, **11,5''**, **10''**, **8''**, **7,5''**, **7''**, **6''**, **3,5''**, **3''**, **2,5''** and **15''** — read the printed diagrams for actual positions.

> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.27 — "RANDOM VP PLACEMENT"

---

## 29. Protocol Cards (via OCR + room variants)

PDF pages 28–32 are titled **PROTOCOL CARDS** and are pure card art — the native extract yields only the heading. The card text below was read **via OCR** from rendered page images and is recorded in [`protocol_cards.ocr.txt`](../../../raw/the_warcode/protocol_cards.ocr.txt). **Map-section variants** (Left / Centre / Right / Total) come from typed transcription in [`protocol_cards_transcription.txt`](../../../raw/the_warcode/protocol_cards_transcription.txt). Full 20-row table: [`Protocol_Cards_Reference.md`](Protocol_Cards_Reference.md).

These are the "Core of the Machine" activation cards drawn at the start of each round. Five protocol types — **Magnet**, **Hunt**, **Electricity**, **Silence**, **Poison** — each appear as a **single-room** card (**Left**, **Centre**, or **Right**) or a **Total** card affecting all three rooms.

### Room variants (Left / Centre / Right / Total)

| Protocol | Map section | Applies to |
|----------|-------------|------------|
| Magnet | Left | Left room only |
| Magnet | Centre | Centre room only |
| Magnet | Right | Right room only |
| Total Magnet | Left, Centre, Right | All three rooms |
| Hunt | Left | Left room only |
| Hunt | Centre | Centre room only |
| Hunt | Right | Right room only |
| Total Hunt | Left, Centre, Right | All three rooms |
| Electricity | Left | Left room only |
| Electricity | Centre | Centre room only |
| Electricity | Right | Right room only |
| Total Electricity | Left, Centre, Right | All three rooms |
| Silence | Left | Left room only |
| Silence | Centre | Centre room only |
| Silence | Right | Right room only |
| Total Silence | Left, Centre, Right | All three rooms |
| Poison | Left | Left room only |
| Poison | Centre | Centre room only |
| Poison | Right | Right room only |
| Total Poison | Left, Centre, Right | All three rooms |

> Source: The Warcode Rulebook V.0.8.7-F.pdf — pp.28–32 — "PROTOCOL CARDS" — map sections via typed transcription (raw/the_warcode/protocol_cards_transcription.txt)

The OCR blocks below quote the **room** and **Total** rules text. Flavour and rule wording for **Hunt** differ between OCR and transcription — see the Hunt footnote under [`Protocol "Hunt" (room)`](#protocol-hunt-room).

### Protocol "Magnet" (room)

> THE FLOOR IN THE ROOM BECOMES HEAVILY MAGNETIZED. MOVEMENT BECOMES DIFFICULT.
>
> ALL UNITS THAT START THEIR MOVEMENT IN THIS ROOM SUFFER A -3 INCH PENALTY TO THEIR MOVEMENT PROFILE.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — pp.28–32 — "PROTOCOL CARDS" — via OCR (raw/the_warcode/protocol_cards.ocr.txt)

### Protocol "Total Magnet"

> THE FLOOR IN ALL ROOMS BECOMES HEAVILY MAGNETIZED. MOVEMENT BECOMES DIFFICULT.
>
> ALL UNITS THAT START THEIR MOVEMENT IN THIS ROOM SUFFER A -3 INCH PENALTY TO THEIR MOVEMENT PROFILE.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — pp.28–32 — "PROTOCOL CARDS" — via OCR (raw/the_warcode/protocol_cards.ocr.txt)

*OCR note: the flavor line says all rooms, but the rule line still reads "this room". Flagged as a polish bug, not a reading.*

### Protocol "Hunt" (room)

> TURRETS ACTIVATE THROUGHOUT THE ROOM. TARGET ACQUISITION BEGINS.
>
> AT THE END OF THE ROUND, ALL UNITS IN THE ROOM WITH FULL HEALTH TAKE 3 DAMAGE.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — pp.28–32 — "PROTOCOL CARDS" — via OCR (raw/the_warcode/protocol_cards.ocr.txt)

**Hunt rule footnote — OCR vs transcription:** OCR reads **"WITH FULL HEALTH"** on the printed card. The owner spreadsheet transcription reads **"all units in the room take 3 damage"** with no full-health qualifier. Until a second physical check resolves it, treat **FULL HEALTH** as the printed-card reading and **all units** as the spreadsheet reading. See [`Protocol_Cards_Reference.md`](Protocol_Cards_Reference.md).

### Protocol "Total Hunt"

> TURRETS ACTIVATE THROUGHOUT ALL ROOMS. TARGET ACQUISITION BEGINS.
>
> AT THE END OF THE ROUND, ALL UNITS IN THE ROOM WITH FULL HEALTH TAKE 3 DAMAGE.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — pp.28–32 — "PROTOCOL CARDS" — via OCR (raw/the_warcode/protocol_cards.ocr.txt)

*OCR note: rule text still reads "the room" singular. Total Hunt flavour confirmed from OCR — the spreadsheet transcription incorrectly copied Magnet flavour for this row.*

### Protocol "Electricity" (room)

> ELECTRICAL PULSES START COURSING THROUGH THE ROOM. IT TAKES GREAT EFFORT TO DODGE THE ELECTRICAL SHOCKS.
>
> AT THE END OF THE ROUND, ROLL ONE D6 FOR EACH UNIT IN THE ROOM. IF THE RESULT IS 3 OR LESS, THE UNIT TAKES 3 DAMAGE.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — pp.28–32 — "PROTOCOL CARDS" — via OCR (raw/the_warcode/protocol_cards.ocr.txt)

### Protocol "Total Electricity"

> ELECTRICAL PULSES START COURSING THROUGHOUT ALL ROOMS. …
>
> AT THE END OF THE ROUND, ROLL ONE D6 FOR EACH UNIT IN THE ROOM. IF THE RESULT IS 3 OR LESS, THE UNIT TAKES 3 DAMAGE.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — pp.28–32 — "PROTOCOL CARDS" — via OCR (raw/the_warcode/protocol_cards.ocr.txt)

### Protocol "Silence" (room)

> THE ROOM FILLS WITH UNKNOWN ENERGY. ALL RANGED WEAPONS COMPLETELY FAIL. ALL UNITS IN THE ROOM CANNOT USE RANGED WEAPONS.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — pp.28–32 — "PROTOCOL CARDS" — via OCR (raw/the_warcode/protocol_cards.ocr.txt)

### Protocol "Total Silence"

> ALL ROOMS FILLS [sic] WITH UNKNOWN ENERGY. ALL RANGED WEAPONS COMPLETELY FAIL. ALL UNITS IN THE ROOM CANNOT USE RANGED WEAPONS.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — pp.28–32 — "PROTOCOL CARDS" — via OCR (raw/the_warcode/protocol_cards.ocr.txt)

### Protocol "Poison" (room)

> CAUSTIC GAS BEGINS TO SEEP THROUGHOUT THE ROOM. NO RESPIRATORY PROTECTION SYSTEM CAN PROVIDE COMPLETE SAFETY. POISONING IS INEVITABLE.
>
> AT THE END OF THE ROUND, ALL UNITS IN THE ROOM TAKE 2 DAMAGE
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — pp.28–32 — "PROTOCOL CARDS" — via OCR (raw/the_warcode/protocol_cards.ocr.txt)

### Protocol "Total Poison"

> CAUSTIC GAS BEGINS TO SEEP THROUGHOUT ALL ROOMS. …
>
> AT THE END OF THE ROUND, ALL UNITS IN THE ROOM TAKE 2 DAMAGE
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — pp.28–32 — "PROTOCOL CARDS" — via OCR (raw/the_warcode/protocol_cards.ocr.txt)

---

## 30. Weapon profile reference (reconstructed)

These tables are **reconstructed** from the flattened extract, not quoted. The rulebook prints them as icon-and-number card art, so the extract delivers bare digits with no labels. Values are cross-checked against the p.20 shooting example and the p.5 sample card wherever possible. **Verify against the printed cards before a competitive game.**

### Ranged weapons (p.7 catalogue)

| Weapon | Shots | Range | Ammo | Shoot AP | Reload AP | Armor pen. | Damage | Critical |
|--------|-------|-------|------|----------|-----------|------------|--------|----------|
| **Pistol** | 5 | 6" | 3 | 1 | 1 | +1 | 1 | 2 |
| **Shotgun** | 2 | 5" | 2 | 1 | 1 | −1 | 3 | 4 |
| **Rifle** | 3 | 7" | 2 | 1 | 1 | 0 | 2 | 3 |
| **Heavy Weapon** | 4 | 8" | 1 | 2 | 1 | −2 | 2 | 3 |
| **Grenade** (p.17) | 2 dice | 5" throw, 2" blast | — | 1 | — | −1 | 1 | 2 |

> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.7 — "RANGED WEAPONS"; p.17 — "GRENADE"

The shotgun row is confirmed by the p.20 worked example (2 shots, "less than 5 inches", −1 penetration, 3 normal / 4 critical damage). The grenade row is confirmed by the p.18 worked example (armor 4 − 1 = 3 to penetrate; 1 normal / 2 critical).

### Melee weapons (from team list cards)

| Weapon | Melee strength | Range | Melee AP | Armor pen. | Damage | Critical | Special |
|--------|----------------|-------|----------|------------|--------|----------|---------|
| **Volt Sword** | 4 | 1" | 1 | 0 | 2 | 3 | Re-roll each armor-penetration die showing 1 until it shows higher |
| **Combat Knife** | 2 | 1" | 1 | 0 | 2 | 3 | — |
| **Combat Claws** | 5 | 1" | 1 | 0 | 1 | 2 | — |
| **Razor Blade** | 4 | 1" | 1 | −1 | 2 | 3 | — |
| **Combat Axe** | 3 | 1" | 1 | −2 | 3 | 4 | Enemy units within 1 inch are in Melee Lock, even if bases do not touch |
| **Fist** | 1 | 1" | 1 | +1 | 1 | 2 | — |

> Source: The Warcode Rulebook V.0.8.7-F.pdf — pp.5, 13–14, 21, 33–36 — weapon cards

The Combat Axe special is printed on the **Smasher** card:

> WEAPON ABILITY: Enemy units within 1 inch are in Melee Lock with this unit, even if their bases do not touch.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.34 — "PROTAGEN MARINES TEAM LIST"

---

## 31. Team list — Protagen Marines

**Reconstructed** from PDF pages 33–34. Same caveat as above: the extract flattens the cards to bare digits. Eight units.

| Unit | HP | Agility | Movement | Armor | Ranged | Melee | Notes |
|------|----|---------|----------|-------|--------|-------|-------|
| **Commander Rickman** | 9 | 3 | 6" | 4 | Pistol | Volt Sword | **LEADER** |
| **Blast** | 8 | 3 | 6" | 4 | Shotgun | Combat Knife | Starts with 2 grenades, no other equipment |
| **Hammer** | 8 | 3 | 6" | 4 | Shotgun | Combat Knife | — |
| **Anvil** | 8 | 3 | 6" | 4 | Shotgun | Combat Knife | — |
| **Bastion** | 8 | 3 | 5" | 4 | Heavy Weapon | Fist | Slow; 2 AP to shoot |
| **Blade** | 8 | 3 | 6" | 4 | Pistol | Combat Claws | Melee strength 5 |
| **Shellshocker** | 8 | 2 | 5" | 5 | Shotgun | Fist | Slow, low agility, heaviest armor in the list |
| **Smasher** | 8 | 3 | 6" | 4 | Pistol (dmg 2 / crit 3) | Combat Axe | Axe locks enemies within 1" without base contact |

> Source: The Warcode Rulebook V.0.8.7-F.pdf — pp.33–34 — "PROTAGEN MARINES TEAM LIST"

Printed unit abilities:

> LEADER: The player gains 2 re-roll points at the start of each round.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.33 — "PROTAGEN MARINES TEAM LIST" (Commander Rickman)

> SPECIAL ABILITY: Starts the game with 2 grenades and cannot take other equipment.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.33 — "PROTAGEN MARINES TEAM LIST" (Blast)

**Flag:** Smasher's pistol shows **damage 2 / critical 3** where every other pistol in the extract shows **1 / 2**. Either a variant profile or a card typo — confirm against the printed card.

---

## 32. Team list — Ulfari

**Reconstructed** from PDF pages 35–36. Eight units.

| Unit | HP | Agility | Movement | Armor | Ranged | Melee | Notes |
|------|----|---------|----------|-------|--------|-------|-------|
| **Soul Eater** | 9 | 4 | 6" | 3 | Pistol | Razor Blade | **LEADER** |
| **Ravener** | 8 | 4 | 6" | 3 | Rifle | Combat Knife | — |
| **Wraith** | 8 | 4 | 6" | 3 | Pistol | Razor Blade | — |
| **Phantom** | 8 | 4 | 7" | 3 | Pistol | Combat Knife | Fast; starts with 2 grenades, no other equipment |
| **Stalker** | 8 | 4 | 6" | 3 | Shotgun | Combat Knife | — |
| **Doom** | 8 | 3 | 6" | 3 | Heavy Weapon | Fist | 2 AP to shoot |
| **Reaper** | 8 | 5 | 7" | 3 | *(none in extract)* | Razor Blade | Fast, agility 5 — the cap |
| **Shade** | 8 | 4 | 6" | 3 | Rifle | Combat Knife | **Sniper** |

> Source: The Warcode Rulebook V.0.8.7-F.pdf — pp.35–36 — "ULFARI TEAM LIST"

Printed unit abilities:

> LEADER: The player gains 2 re-roll points at the start of each round.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.35 — "ULFARI TEAM LIST" (Soul Eater)

> SPECIAL ABILITY: Starts the game with 2 grenades and cannot take other equipment.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.35 — "ULFARI TEAM LIST" (Phantom)

> SPECIAL ABILITY: Sniper — When this unit shoots, the Target's agility is reduced by 1.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.36 — "ULFARI TEAM LIST" (Shade)

**Flag:** the extract shows **no ranged weapon** on Reaper's card — the flattened block gives only a Razor Blade. Either the card is melee-only by design or the extract dropped a profile. Confirm against the printed card.

**Faction shape at a glance:** across both lists, Ulfari trade **Armor 3** for **Agility 4–5**; Protagen sit at **Armor 4–5** with **Agility 2–3**. Shade is the contract Target named in the p.22 example.

---

## Gaps in the extract

Things the beta PDF contains that this file cannot quote, because the pages carry no extractable text layer:

| PDF page(s) | Content | Status |
|-------------|---------|--------|
| p.1 | Cover | No text |
| pp.24–25 | **Contract cards** — individual card faces and VP values | **Closed** — typed transcription in Sec 25; teaching table in [`Contract_Cards_Reference.md`](Contract_Cards_Reference.md). All eight cards award **1 VP**. |
| pp.28–32 | **Protocol Cards** | Transcribed **via OCR** (Sec 29) plus **Left / Centre / Right / Total** map sections via typed transcription — see [`Protocol_Cards_Reference.md`](Protocol_Cards_Reference.md). |
| p.27 | Six random VP layout diagrams | Positions documented in [`../setup/Board_Setup.md`](../setup/Board_Setup.md); dimension callouts in Sec 28. |
| pp.5, 33–36 | Unit and weapon stat cards | Reconstructed as tables in Sec 30–32, not quoted. |
| p.37 | Trailing page | Empty in extract |

Other open items:

- The rulebook does not state a **default round count** anywhere in the extracted text; scenarios are expected to set it. The project README records 4 fixed rounds from the pre-launch site, which is **not** confirmed by this PDF.
- No **points values** or list-building costs appear — squads look fixed at 8 units.
- Only one scenario («Core of the Machine») is printed.

---

## Related pages

- [`Overview.md`](Overview.md) — what the game is
- [`Turn_Structure.md`](Turn_Structure.md) — round checklist
- [`Key_Concepts.md`](Key_Concepts.md) — teaching paraphrase of everything above
- [`Keyword_Glossary.md`](Keyword_Glossary.md) — one-line term lookup
- [`Activation_and_AP.md`](Activation_and_AP.md) — deep-dive on the AP economy
- [`Combat_Ranged_and_Melee.md`](Combat_Ranged_and_Melee.md) — deep-dive on resolution
- [`Equipment_Loot_and_Doors.md`](Equipment_Loot_and_Doors.md) — deep-dive on gear and map objects
- [`Contracts_and_VP.md`](Contracts_and_VP.md) — deep-dive on scoring
- [`Scenarios_and_Events.md`](Scenarios_and_Events.md) — deep-dive on the scenario and Protocol Cards
- [`Contract_Cards_Reference.md`](Contract_Cards_Reference.md) — all eight contract targets by faction
- [`Protocol_Cards_Reference.md`](Protocol_Cards_Reference.md) — 20 protocol rows with map sections
- [`../setup/Board_Setup.md`](../setup/Board_Setup.md) — board, deployment, and VP layout placement
- [`../setup/Terrain_Basics.md`](../setup/Terrain_Basics.md) — cover and doors

---

## Change Log

- v0.1.1 (2026-08-25): Sec 25 — eight contract cards via typed transcription (pp.24–25 gap closed). Sec 29 — Left/Centre/Right/Total room variants; Hunt OCR vs transcription footnote. Gaps table updated; links to Contract and Protocol reference pages.
- v0.1 (2026-08-23): Initial verbatim appendix from beta v0.8.7-F native extract plus Protocol Cards OCR. Reconstructed weapon and team-list tables with flags on Smasher's pistol and Reaper's missing ranged profile.

## Attribution

- Project: Wargame_Concierge
- Maintainer: Russell Catt
- The Warcode is property of RedMakers. Unofficial, unauthorized personal learning notes — never for sale.
- Quoted under the free public beta exception in `AGENTS.md` Sec 10.

## Rising Tide Notes

- This document follows Rising Tide documentation standards.
- Keep the receipts. Make AI show their work.
- Quotes here are the receipt; teaching pages paraphrase and link back.
