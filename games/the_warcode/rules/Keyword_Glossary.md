<!--
FILE: games/the_warcode/rules/Keyword_Glossary.md
VERSION: v0.2 (2026-08-25)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, warcode_tactical_doctrine)

DOCUMENT_TYPE: Reference / Term Glossary
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: The Warcode
REFERENCE_STATUS: Active — draft, beta v0.8.7-F (2026-08-23)

SOURCES:
  - raw/the_warcode/The Warcode Rulebook V.0.8.7-F.pdf (read via extract 2026-08-23)
  - raw/the_warcode/rulebook_v087f_extract.txt
  - games/the_warcode/README.md

PURPOSE:
  At-a-glance reference for Warcode terms used in this teaching subtree.
  One line of plain English per term, grouped by when you need it.

PRIMARY_AUDIENCE:
  - A player mid-game who hit an unfamiliar term
  - Cross-game readers comparing Murder Platoon vocabulary

KEY_SECTIONS_EXPECTED:
  - How to read this glossary
  - Round and activation
  - Stats and weapons
  - Movement and terrain
  - Combat
  - Scoring and meta
  - Comparative bridges (Murder Platoon)

UPDATE_TRIGGER:
  Update when beta supersedes v0.8.7-F or comparative glossary expands in S8.
-->

# Keyword Glossary — The Warcode (beta v0.8.7-F)

One line per term. **`confidence: draft`**, read **2026-08-23**. Deep dives: [`Key_Concepts.md`](Key_Concepts.md). Verbatim text: [`Rulebook_Quotes.md`](Rulebook_Quotes.md).

---

## How to read this glossary

| Status | Meaning |
|--------|---------|
| `draft` | Paraphrased from the v0.8.7-F extract; confirm against owned PDF before tournaments |

All entries below are **`draft`** unless a future pass marks them verified. Card lookups: [`Contract_Cards_Reference.md`](Contract_Cards_Reference.md), [`Protocol_Cards_Reference.md`](Protocol_Cards_Reference.md).

---

## Round and activation

| Term | What it means | When it matters |
|------|---------------|-----------------|
| **Round** | One Initiative Phase + one Tactical Phase + End of Round | Scenario sets how many rounds until final scoring |
| **Initiative Phase** | D6 roll; winner activates first this round | Round 1 roll also sets deployment order |
| **Tactical Phase** | Alternating single-unit activations | The main decision window |
| **Activation** | One unit's turn to spend AP | Each unit activates once per round |
| **Activation token** | Flip after activating — back side means "already activated" | Prevents double-activating |
| **Action Point (AP)** | Currency for actions; **2 per activation** by default | Every move, shot, reload, etc. has a cost |
| **Pass** | Skip remaining AP without acting | Does **not** trigger Overwatch |

---

## Unit stats

| Term | What it means | When it matters |
|------|---------------|-----------------|
| **HP (Health)** | Wound count; 0 = model removed | Track against damage |
| **Agility (A)** | Hit threshold for attacks against this unit | Cover can raise it, max **5** |
| **Armor** | Base penetration difficulty | Modified by weapon penetration +/- |
| **Movement Range (M)** | Inches per 1 AP move | Slow 5 / Standard 6 / Fast 7 |
| **Melee Strength** | Attack dice in melee; also disengage target number | Defender rolls equal dice to block |
| **Leader** | Keyword on some units; grants **2 re-roll points** each round while alive | Re-roll economy anchor |

---

## Ranged weapons

| Term | What it means | When it matters |
|------|---------------|-----------------|
| **Shooting Range** | Max inches from base to target base | Must reach target base to fire |
| **Number of Shots** | Hit dice rolled when shooting | Each die ≥ Agility hits |
| **Ammunition** | Shots remaining before reload | Need ≥ 1 to shoot; −1 after each shot |
| **Reload** | AP action restoring ammo to max | Triggers Overwatch if in range |
| **Armor penetration (+/−/0)** | Adjusts target Armor for penetration rolls | + makes armor harder to beat |
| **Damage / Critical damage** | HP loss on penetrating hit; **6** = critical value | Stack damage from multiple hits |
| **Line of sight** | Shooter must see target base; blocked by full cover unless **≥50%** of target base is visible (e.g. 14 mm on a 28 mm base) | Declare before shooting; friendlies use same 50% rule |
| **Hit check** | Each shot/melee attack die must roll **≥ target Agility** (after modifiers) | Cover and Sniper change the threshold |
| **Penetration check** | Each hit die rolls **≥ effective Armour** (weapon pen modifies Armour) | + pen raises effective Armour; − pen lowers it |
| **Overwatch** | 1 AP reaction fire stance | Ends activation; see trigger list in Key_Concepts |

---

## Melee

| Term | What it means | When it matters |
|------|---------------|-----------------|
| **Melee range** | Inches from base to target base; also **1-inch radius** around unit for “in melee” | Inside radius: no shoot, no equipment, no abilities — fight or leave |
| **Melee Lock** | Bases **touching** an enemy | Cannot walk away without Disengage/Escape |
| **Melee combat** | AP action; opposed dice then penetration | Different from shooting sequence |
| **Engage** | 2 AP rush — move M+2" into melee | Common opener after a 1 AP approach |
| **Disengage** | 1 AP; D6 vs enemy Melee Strength to break Lock | Fail = enemy free counter-attack |
| **Escape** | 2 AP; same roll but you move even on fail | Expensive but reliable retreat |

---

## Movement and terrain

| Term | What it means | When it matters |
|------|---------------|-----------------|
| **Partial cover** | Terrain **not taller than units**; passable at **−1"** from Movement Range | Each piece on **line of fire** adds **+1 Agility** to target (cap 5) |
| **Full cover (wall)** | Terrain **taller than units**; **impassable** | Blocks LoS unless ≥50% of target base visible |
| **Line of fire** | Cover between shooter and target, even if target is not “behind” it | Stacks +1 Agility per interfering partial-cover piece |
| **Shooter within 1" of cover** | Partial cover within 1" of shooter does **not** interfere with that shot | Lets you hug cover and still fire |
| **Target behind partial cover** | Target within 1" of partial cover counts as behind it for Agility | More than half base past edge → no bonus |
| **Move through friendly** | −2" from Movement Range | Plan lane discipline |
| **Door / Doorway** | Open-close at 0 AP within 1 inch | **Blocked** if any unit within 1 inch |
| **Door blocking** | Enemy (or mixed teams) within 1 inch stops door use | Control doorways tactically |

---

## Equipment and objects

| Term | What it means | When it matters |
|------|---------------|-----------------|
| **Equipment points** | **4 per player** pre-game | Buy grenades and medkits |
| **Grenade** | 2 pts; throw 1 AP; 5" range; 2" blast | Friendly fire in blast |
| **Medkit** | 2 pts; heal 2 HP at 0 AP once | Self or friend within 1 inch |
| **Item pickup** | 0 AP within 1 inch of dropped gear | Loot dead carriers |

---

## Scoring and meta

| Term | What it means | When it matters |
|------|---------------|-----------------|
| **Victory Point (VP)** | Scenario score; most VP wins (usually) | Earn from map tokens + contracts |
| **VP token** | Marker on board; scored end of round | Control within 1 inch, no enemy in radius |
| **Contested** | Both sides in 1 inch of same VP | Nobody scores that token |
| **Contract** | Secret elimination mission when trailing ≥ 1 VP | One card names a Target per faction — read the column matching your opponent |
| **Contract card ID** | Printed number on each contract (e.g. **6037**) | Eight unique cards in the beta deck; all award **1 VP** — see reference table |
| **Re-roll point** | Spend to repeat a whole roll | Leader + casualties feed the pool; not on initiative or protocol D6 |
| **Protocol card** | *Core of the Machine* activation card drawn **start of each round** | Map section picks which room(s) suffer the effect |
| **Protocol room** | **Left wing**, **central hex**, or **right wing** on the ship map | Card **Map section** column names Left / Centre / Right / Total |
| **Total protocol** | **Total Magnet**, **Total Hunt**, etc. | Affects **all three rooms** (flavour says “all rooms”; agree at table if rule text still says “this room”) |

---

## Protocol effect names (*Core of the Machine*)

| Protocol | What it does | When |
|----------|--------------|------|
| **Magnet** | **−3"** to Movement Range if movement **starts** in affected room(s) | During movement |
| **Hunt** | **3 damage** to units in room at end of round (OCR: **full health only**; spreadsheet: all units — see reference footnote) | End of round |
| **Electricity** | D6 per unit in room; **3 or less** → **3 damage** | End of round |
| **Poison** | **2 damage** to all units in room | End of round |
| **Silence** | Units in room **cannot use ranged weapons** | While in room that round |

Full 20-row deck: [`Protocol_Cards_Reference.md`](Protocol_Cards_Reference.md).

---

## Map and setup

| Term | What it means | When it matters |
|------|---------------|-----------------|
| **Board size** | **33" × 24"** standard playing surface | Scenario diagrams and VP placement |
| **Deployment area A / B** | Opposite ends of the map | Round 1 initiative sets who deploys first |
| **D6 VP placement** | One D6 before play picks 1 of **6** token layouts | Positions only — token **values** read from printed art |
| **Slow / Standard / Fast** | Movement Range **5 / 6 / 7** inches per 1 AP move | Profile speed bands on unit cards |

---

## Comparative bridges (Murder Platoon / That other game)

| Warcode term | Rough Murder Platoon analogue |
|--------------|------------------------------|
| **AP per activation (2)** | Action Point Limit per operative activation |
| **Alternating unit activation** | Alternating activations (one operative at a time) |
| **Agility** | Defence stat on hit rolls |
| **Armor + penetration** | Save / armour trade — different math, same job |
| **Melee Lock** | Engaged / within fight range — tighter when bases touch |
| **Overwatch** | Overwatch / guard reactions — read trigger list; not identical |
| **VP + Contracts** | Crit op / tac op scoring — contracts are catch-up bounty kills |

Use bridges for **memory**, not rules substitution.

---

## Related pages

- [`Key_Concepts.md`](Key_Concepts.md) — full mechanical explanations
- [`Turn_Structure.md`](Turn_Structure.md) — when terms trigger
- [`Rulebook_Quotes.md`](Rulebook_Quotes.md) — publisher wording
- [`Contract_Cards_Reference.md`](Contract_Cards_Reference.md) — eight-card contract deck
- [`Protocol_Cards_Reference.md`](Protocol_Cards_Reference.md) — twenty protocol rows
- [`../setup/Terrain_Basics.md`](../setup/Terrain_Basics.md) — cover types on the table
- [`../setup/Board_Setup.md`](../setup/Board_Setup.md) — D6 VP placement at setup

---

## Change Log

- v0.2 (2026-08-25): S8 corpus pass — protocol names, contract IDs, cover subtypes, map/setup terms; removed OCR-pending stubs; card reference cross-links.
- v0.1 (2026-08-23): Initial glossary from beta v0.8.7-F extract; comparative stubs for S8 expansion.

## Attribution

- Project: Wargame_Concierge
- Maintainer: Russell Catt
- The Warcode is property of RedMakers. Unofficial teaching paraphrase.

## Rising Tide Notes

- This document follows Rising Tide documentation standards.
- Add verified status only after line-by-line PDF cross-check.
