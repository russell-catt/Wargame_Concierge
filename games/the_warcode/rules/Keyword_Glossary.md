<!--
FILE: games/the_warcode/rules/Keyword_Glossary.md
VERSION: v0.1 (2026-08-23)
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

All entries below are **`draft`** unless a future pass marks them verified.

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
| **Line of sight** | Shooter can see target base | Full cover needs 50% base visible |
| **Overwatch** | 1 AP reaction fire stance | Ends activation; see trigger list in Key_Concepts |

---

## Melee

| Term | What it means | When it matters |
|------|---------------|-----------------|
| **Melee range** | Weapon reach; also **radius** around unit | Enemies inside are in melee combat |
| **Melee Lock** | Bases **touching** an enemy | Cannot walk away without Disengage/Escape |
| **Melee combat** | AP action; opposed dice then penetration | Different from shooting sequence |
| **Engage** | 2 AP rush — move M+2" into melee | Common opener after a 1 AP approach |
| **Disengage** | 1 AP; D6 vs enemy Melee Strength to break Lock | Fail = enemy free counter-attack |
| **Escape** | 2 AP; same roll but you move even on fail | Expensive but reliable retreat |

---

## Movement and terrain

| Term | What it means | When it matters |
|------|---------------|-----------------|
| **Partial cover** | Terrain ≤ unit height; passable with −1" move | Also adds Agility when on line of fire |
| **Full cover** | Taller than units; **impassable** wall | 50% base rule for shooting |
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
| **Contract** | Secret elimination mission when trailing ≥ 1 VP | Swing games when behind on points |
| **Re-roll point** | Spend to repeat a whole roll | Leader + casualties feed the pool |
| **Protocol card** | Scenario event (e.g. Core of the Machine) | OCR corpus pending — see Rulebook_Quotes |

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
- [`../setup/Terrain_Basics.md`](../setup/Terrain_Basics.md) — cover types on the table

---

## Change Log

- v0.1 (2026-08-23): Initial glossary from beta v0.8.7-F extract; comparative stubs for S8 expansion.

## Attribution

- Project: Wargame_Concierge
- Maintainer: Russell Catt
- The Warcode is property of RedMakers. Unofficial teaching paraphrase.

## Rising Tide Notes

- This document follows Rising Tide documentation standards.
- Add verified status only after line-by-line PDF cross-check.
