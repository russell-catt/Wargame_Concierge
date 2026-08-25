<!--
FILE: games/the_warcode/setup/Board_Setup.md
VERSION: v0.2 (2026-08-25)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, warcode_tactical_doctrine)

DOCUMENT_TYPE: Teaching Guide / Pre-game Checklist
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: The Warcode
REFERENCE_STATUS: Active — draft, beta v0.8.7-F (2026-08-23)

SOURCES:
  - raw/the_warcode/The Warcode Rulebook V.0.8.7-F.pdf (read via extract 2026-08-23)
  - raw/the_warcode/rulebook_v087f_extract.txt
  - raw/the_warcode/images/Core_Machine_placement.png (map topology, 2026-08-25)
  - raw/the_warcode/images/Core_Machine_obj_placement.png (D6 VP layouts, 2026-08-25)

PURPOSE:
  Everything between "we are going to play" and "Initiative Phase of round 1":
  board size, scenario prep, VP placement, deployment, and equipment.

PRIMARY_AUDIENCE:
  - Two players setting up their first Warcode game
  - A host preparing the 33" × 24" board before opponents arrive

KEY_SECTIONS_EXPECTED:
  - What you need
  - Board size
  - Setup sequence
  - VP placement
  - Deployment
  - Equipment distribution
  - Pre-game checklist

UPDATE_TRIGGER:
  Update when beta supersedes v0.8.7-F on board dimensions, setup order, or VP tables.
-->

# Board Setup — from empty table to round 1

The Warcode plays on a **fixed-size board** with **scenario-driven** objectives and deployment zones. This page teaches the **standard setup sequence** from the beta rulebook. **`confidence: draft`**, **v0.8.7-F**, read **2026-08-23**. Quotes: [`../rules/Rulebook_Quotes.md`](../rules/Rulebook_Quotes.md).

Terrain behaviour is in [`Terrain_Basics.md`](Terrain_Basics.md). Round flow after setup is in [`../rules/Turn_Structure.md`](../rules/Turn_Structure.md).

---

## What you need

| Item | Notes |
|------|-------|
| **Playing surface** | **33 inches × 24 inches** for standard scenarios |
| **Scenario** | Objectives, victory conditions, deployment areas, round count |
| **Squads** | Eight units per player (faction roster) |
| **Terrain** | Partial cover, full-cover walls, doors/doorways per map |
| **VP tokens** | Placed per scenario + random table (below) |
| **Measuring** | Inch ruler |
| **Dice and tokens** | D6, activation, ammo, Overwatch, equipment |

---

## Board size

Standard scenarios use a **33" × 24"** board.

> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.26 — "BOARD SIZE 33'' X 24''"

The sample scenario *Core of the Machine* labels **Deployment area A** (top) and **Deployment area B** (bottom) on opposite ends of the ship map, with VP tokens placed per the random table below.

**Map reference images** (read in place — do not copy binaries into shipping):

| Image | Path | Contents |
|-------|------|----------|
| Terrain layout | [`raw/the_warcode/images/Core_Machine_placement.png`](../../../raw/the_warcode/images/Core_Machine_placement.png) | Three rooms, deployment zones, 10 doors, cover legend |
| VP layouts | [`raw/the_warcode/images/Core_Machine_obj_placement.png`](../../../raw/the_warcode/images/Core_Machine_obj_placement.png) | Six D6 objective diagrams with inch callouts |

Map topology and protocol-room boundaries: [`../rules/Scenarios_and_Events.md`](../rules/Scenarios_and_Events.md#core-of-the-machine-map-topology).

---

## Setup sequence (official order)

The rulebook lists three setup steps before play begins:

### 1. Read the scenario

- Objectives and **victory conditions**
- Special rules (e.g. *Core of the Machine* core activation cards each round)
- How many **rounds** constitute the final round
- Where **deployment areas** and terrain elements belong

> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.2 — "READ THE SCENARIO"

### 2. Deploy units

- **Round 1 initiative roll first** — highest D6 chooses who deploys first **and** who takes the first activation that round. Re-roll ties.
- Players then **alternate placing one unit at a time** until all models are deployed inside their deployment zones.

> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.2 — "DEPLOY UNITS"  
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.3 — "INITIATIVE PHASE"

### 3. Distribute equipment

- After **all** units are on the board, each player spends **4 equipment points** on grenades (2 pts each) and/or medkits (2 pts each), subject to unit restrictions.

> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.2 — "DISTRIBUTE EQUIPMENT"

---

## VP token placement

The **random VP placement** system applies to **all scenarios**:

- Before the game, roll **one D6**.
- The result selects which VP layout diagram to use for that session.
- Diagrams in the rulebook use *Core of the Machine* as the worked example — transfer the same roll concept to other scenarios when published.

> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.27 — "RANDOM VP PLACEMENT"

Place VP tokens on the board **before deployment** (both players see the spread, then roll initiative and deploy). Diagrams show **token positions only** — each token's VP value (1 or 2) still comes from the printed token art at setup.

**Worked example map:** [`raw/the_warcode/images/Core_Machine_obj_placement.png`](../../../raw/the_warcode/images/Core_Machine_obj_placement.png)

### D6 → layout summary

| D6 roll | VP tokens | Layout |
|---------|-----------|--------|
| **1**, **2**, or **3** | **3** | One token per wing + one in the central hex (identical diagrams) |
| **4** | **4** | Left wing, right wing, and **two** tokens stacked vertically in the hex centre |
| **5** | **5** | Corner pairs in both wings + one hex-centre token |
| **6** | **6** | Wing corner pairs + hex vertical pair + asymmetric right-wing pair |

### Measuring convention

All distances below are in **inches** on the **33" × 24"** board. Measure from the **inner edge** of each deployment zone boundary (the line where playable board begins), not from model bases.

**Landmarks on *Core of the Machine*:**

| Landmark | How to find it |
|----------|----------------|
| **Left board edge** | Short side at the wing end opposite the hex's flat sides |
| **Right board edge** | Opposite short side |
| **Left-wing / hex wall** | Vertical full-cover wall between the left wing and the central hex |
| **Hex / right-wing wall** | Vertical full-cover wall between the hex and the right wing |
| **Hex vertical midline** | Centre line through the hex (where the scenario **core** circle sits on the terrain map) |
| **Vertical centre of play** | **11.5"** from the top deployment boundary **and** **11.5"** from the bottom deployment boundary |

### D6 coordinate tables (*Core of the Machine*)

Use these tables with the diagram in [`Core_Machine_obj_placement.png`](../../../raw/the_warcode/images/Core_Machine_obj_placement.png). Each row is one VP token.

#### Rolls 1, 2, and 3 — three tokens (identical layouts)

| # | Room | Horizontal | Vertical |
|---|------|------------|----------|
| 1 | Left wing | **3"** from left board edge | **11.5"** from top boundary **and** **11.5"** from bottom boundary |
| 2 | Centre (hex) | **14"** right of the left-wing / hex wall, on hex midline | **11.5"** from top **and** bottom boundaries |
| 3 | Right wing | **3"** from right board edge | **11.5"** from top **and** bottom boundaries |

#### Roll 4 — four tokens

| # | Room | Horizontal | Vertical |
|---|------|------------|----------|
| 1 | Left wing | **3"** from left board edge | **11.5"** from top **and** bottom boundaries |
| 2 | Centre (hex) | Hex vertical midline | **8"** from top deployment boundary |
| 3 | Centre (hex) | Hex vertical midline | **8"** from bottom deployment boundary |
| 4 | Right wing | **3"** from right board edge | **11.5"** from top **and** bottom boundaries |

Centre pair gap: **6"** between the two hex tokens (23" play height minus 8" minus 8" minus token footprint).

#### Roll 5 — five tokens

| # | Room | Horizontal | Vertical |
|---|------|------------|----------|
| 1 | Left wing | **2.5"** right of left-wing / hex wall | **7.5"** from top deployment boundary |
| 2 | Left wing | **2.5"** right of left-wing / hex wall | **7.5"** from bottom deployment boundary |
| 3 | Centre (hex) | **14"** right of left-wing / hex wall, on hex midline | **11.5"** from top **and** bottom boundaries |
| 4 | Right wing | **2.5"** left of hex / right-wing wall | **7.5"** from top deployment boundary |
| 5 | Right wing | **2.5"** left of hex / right-wing wall | **7.5"** from bottom deployment boundary |

Wing pairs: **7"** vertical gap between upper and lower tokens in each wing.

#### Roll 6 — six tokens

| # | Room | Horizontal | Vertical |
|---|------|------------|----------|
| 1 | Left wing | **2.5"** right of left-wing / hex wall | **7.5"** from top deployment boundary |
| 2 | Left wing | **2.5"** right of left-wing / hex wall | **7.5"** from bottom deployment boundary |
| 3 | Centre (hex) | Hex vertical midline | **6"** from top deployment boundary |
| 4 | Centre (hex) | Hex vertical midline | **6"** from bottom deployment boundary |
| 5 | Right wing | **2.5"** from **right board edge** | **3.5"** from top deployment boundary |
| 6 | Right wing | **2.5"** from **right board edge** | **3.5"** from bottom deployment boundary |

Centre pair gap: **10"** between hex tokens. Right-wing pair gap: **15"** (note roll 6 measures the right wing from the **outer board edge**, not the hex wall — mirror asymmetry vs roll 5).

---

## Deployment habits

- Stay inside your scenario's **deployment area** — the sample map marks **A** and **B** at opposite ends of the 33" × 24" board.
- **Alternate single-unit placement** creates natural spacing — avoid clumping unless your scenario allows it.
- Remember **doorways** and **1-inch blocking** rules when placing near entrances (see [`Terrain_Basics.md`](Terrain_Basics.md)).

---

## Equipment distribution checklist

- [ ] Each player has **4 equipment points** unless scenario overrides.
- [ ] Default limit: **one** grenade **or** one medkit per unit (check special abilities — some units start with two grenades and cannot take other equipment).
- [ ] Mark grenade/medkit tokens on carriers.
- [ ] Ammo tokens start at **maximum** for each ranged weapon.

---

## Pre-game checklist

- [ ] Confirm **33" × 24"** board and scenario terrain layout
- [ ] Roll D6 for **VP placement** layout
- [ ] Place VP tokens, doors, and terrain
- [ ] Roll D6 for **round 1 initiative** (deployment order + first activation)
- [ ] **Alternate deploy** all units
- [ ] **Spend equipment points** and mark loadouts
- [ ] Set all activation tokens to **"can activate"**
- [ ] Begin **Initiative Phase** of round 1 (re-roll initiative if not re-using round 1 deployment roll — see Turn Structure)

---

## Sample scenario pointer

*Core of the Machine* (rulebook p.25–26): infiltrate a damaged space drifter, score VP to sway the machine core, or eliminate the enemy squad. Each round starts with a **Core of the Machine** activation card applying negative effects to rooms. Tie on VP at game end → both teams lose per scenario text.

Full scenario quotes when [`Rulebook_Quotes.md`](../rules/Rulebook_Quotes.md) scenario section lands.

---

## Related pages

- [`Terrain_Basics.md`](Terrain_Basics.md) — cover, doors, movement
- [`../rules/Scenarios_and_Events.md`](../rules/Scenarios_and_Events.md) — *Core of the Machine* map topology and protocols
- [`../rules/Turn_Structure.md`](../rules/Turn_Structure.md) — round 1 initiative nuance
- [`../rules/Overview.md`](../rules/Overview.md) — what you are setting up toward

---

## Open questions

- **Default round count** when a scenario omits it — not in current extract.
- Whether deployment must be wholly within zones or allows forward scouting — confirm scenario text per map.
- **VP token values** at each printed position — diagrams show placement only; confirm 1 vs 2 VP from token art.

---

## Change Log

- v0.2 (2026-08-25): Full D6 → VP count and inch-coordinate tables for *Core of the Machine* from `Core_Machine_obj_placement.png`; map image pointers; D6 mapping open question closed.
- v0.1 (2026-08-23): Initial board setup from beta v0.8.7-F extract.

## Attribution

- Project: Wargame_Concierge
- Maintainer: Russell Catt
- The Warcode is property of RedMakers. Unofficial teaching paraphrase.

## Rising Tide Notes

- This document follows Rising Tide documentation standards.
- Photograph your VP layout when using the random table — rematches stay fair.
