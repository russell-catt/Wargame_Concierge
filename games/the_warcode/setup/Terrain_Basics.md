<!--
FILE: games/the_warcode/setup/Terrain_Basics.md
VERSION: v0.1 (2026-08-23)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, warcode_tactical_doctrine)

DOCUMENT_TYPE: Teaching Guide / Terrain Reference
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: The Warcode
REFERENCE_STATUS: Active — draft, beta v0.8.7-F (2026-08-23)

SOURCES:
  - raw/the_warcode/The Warcode Rulebook V.0.8.7-F.pdf (read via extract 2026-08-23)
  - raw/the_warcode/rulebook_v087f_extract.txt

PURPOSE:
  Explain what partial cover, full cover, and doors actually do for movement,
  shooting, and grenades — without transcribing official map templates.

PRIMARY_AUDIENCE:
  - A beginner dressing a 33" × 24" board for the first time
  - A player deciding whether a shot or grenade reaches a target

KEY_SECTIONS_EXPECTED:
  - Two cover types
  - Movement through terrain
  - Shooting and cover
  - Doors and blocking
  - Grenades vs terrain
  - Layout habits

UPDATE_TRIGGER:
  Update when beta supersedes v0.8.7-F on cover, doors, or impassable terrain.
-->

# Terrain Basics — what the scenery actually does

In The Warcode, terrain controls **movement inches**, **Agility bonuses**, and **line of sight**. This page paraphrases the beta v0.8.7-F rules. **`confidence: draft`**, read **2026-08-23**. Verbatim text: [`../rules/Rulebook_Quotes.md`](../rules/Rulebook_Quotes.md).

Board dimensions and setup order: [`Board_Setup.md`](Board_Setup.md). Combat detail: [`../rules/Key_Concepts.md`](../rules/Key_Concepts.md).

---

## Two cover types

| Type | Height rule | Movement | Shooting |
|------|-------------|----------|----------|
| **Partial cover** | Does **not** exceed unit height | Passable; **−1 inch** when moving **through** it | Can block shots; see below |
| **Full cover (wall)** | **Taller** than units | **Impassable** | Shooting only if **≥ 50%** of target base visible |

Partial cover includes low obstacles, barrels, and rubble. Full cover includes walls, columns, and other impassable blockers shown on scenario maps.

> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.11 — "PARTIAL COVER"

---

## Movement through terrain and friends

Measure from the moving unit's **base edge** with an inch ruler.

| Situation | Effect on Movement Range |
|-----------|--------------------------|
| Normal open ground | Full M for 1 AP (Slow 5 / Standard 6 / Fast 7) |
| Move **through partial cover** | **−1 inch** |
| Move **through a friendly unit** | **−2 inches** |
| **Full cover** | Cannot move through — route around |

### Placement when blocked

- If movement would end **on** a friendly or on partial cover, place the unit **in front of** the obstacle.
- If penalties make the legal stop farther than expected, place **beyond** the obstacle, adjacent to what blocked you, along the path.

### Friend + wall spacing

When squeezing between a friendly and full cover: you need **at least 1 inch** to the wall, or the move counts as **through** the friendly (−2 inches).

---

## Shooting and partial cover

Three ideas to combine:

1. **Target behind partial cover** — if **more than half** the target base is **not** visible past the cover edge, the target gets **+1 Agility**. On a 28 mm base, that means ≤ 14 mm visible ⇒ bonus applies.

2. **Partial cover on the line of fire** — each interfering piece **not ignored** gives **+1 Agility** ( **maximum Agility 5** ).

3. **Shooter within 1 inch of cover on the line** — that piece **does not interfere**. Measure from shooter toward target; if the cover is within 1 inch of the shooter along that line, ignore it.

### Full cover and line of sight

If the target is behind **full cover**, you need **≥ 50% of its base** in direct line of sight (same 28 mm → 14 mm visible example as the rulebook).

### Shooting through friendlies

- Target behind an ally: **+1 Agility** (still capped at 5; a base Agility 5 target gains nothing).
- **No shot** if **< 50%** of the target base is visible past the friendly.

---

## Doors and doorways

Scenarios mark **doors** in **doorways** (often choke points between rooms).

| Action | Cost |
|--------|------|
| Open or close door | **0 AP** if within **1 inch** of doorway |
| Move into range first | **1 AP** move, then interact |

Each unit may open or close a given door **once per activation**.

### Door blocking

- If **any unit** is within **1 inch** of the doorway, the door is **blocked**.
- A **blocked** door cannot be opened or closed — including by the unit doing the blocking.
- If **two or more units from different teams** are within 1 inch of the same doorway, the door is blocked for **everyone**, regardless of which side they stand on.

> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.19 — "DOOR BLOCKING"

Use blocking to hold corridors or deny enemy rotation through the ship interior.

---

## Grenades vs terrain

- Grenade blasts use a **2-inch radius** from the token edge.
- Grenades **ignore partial cover and Agility** for affected units inside the blast.
- **Full cover** still matters: from the **grenade token**, if **< 50%** of a unit's base is visible, fragments do not reach it — no check.
- Friendly models in the blast **are hit** — include your own troops in risk assessment.

Throw placement follows movement-like rules: if the throw would end on a model or partial cover, place the token **shorter**; if beyond blockers, place **adjacent** to what stopped the throw.

---

## Overwatch and terrain

- Enemy moving into overwatch range **behind full cover** and out of line of sight **does not** trigger Overwatch for that move.
- Enemy **throwing a grenade** from cover can still damage an overwatching unit; taking damage **removes** Overwatch.

---

## Layout habits for a fair 33" × 24" table

- Mix **lanes** (partial cover) with **hard walls** (full cover) so Agility and movement penalties both matter.
- Place **doors** where fights should stall — blocking rules make doorways contest points.
- Leave **1-inch gaps** consciously — they decide whether cover interferes with shots.
- Avoid entirely open centres unless the scenario demands it; VP control within 1 inch rewards positional play.
- When proxying terrain from **Murder Platoon** killzones: treat **Vantage / Heavy** tall ruins as **full cover**, low barricades as **partial cover**, and hatches as **doorways** — visual match only, not a rules import.

---

## Related pages

- [`Board_Setup.md`](Board_Setup.md) — when terrain hits the table
- [`../rules/Key_Concepts.md`](../rules/Key_Concepts.md) — full shooting and overwatch
- [`../rules/Keyword_Glossary.md`](../rules/Keyword_Glossary.md) — quick term lookup

---

## Open questions

- Whether scenario-specific terrain traits (e.g. machine core rooms) add modifiers beyond standard cover — see Protocol / scenario cards when OCR completes.
- Official terrain height threshold for "exceeds unit height" if using non-standard model scales.

---

## Change Log

- v0.1 (2026-08-23): Initial terrain basics from beta v0.8.7-F extract.

## Attribution

- Project: Wargame_Concierge
- Maintainer: Russell Catt
- The Warcode is property of RedMakers. Unofficial teaching paraphrase.

## Rising Tide Notes

- This document follows Rising Tide documentation standards.
- When in doubt, measure base visibility in millimetres — the 50% rule is geometric, not narrative.
