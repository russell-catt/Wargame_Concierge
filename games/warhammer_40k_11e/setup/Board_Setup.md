<!--
FILE: games/warhammer_40k_11e/setup/Board_Setup.md
VERSION: v0.5.2 (2026-08-23)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, slice S3)

DOCUMENT_TYPE: Teaching Guide / Pre-game Checklist
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: Warhammer 40,000 - 11th Edition
REFERENCE_STATUS: Active - draft, spot-checked against owned PDFs 2026-08-16

SOURCES:
  - C:\Personal\40K\rules\eng_22-07_warhammer_40,000_event_companion-alyapl19us-b2drgwkji4.pdf (v1.1, read 2026-08-16)
  - C:\Personal\40K\rules\eng_01-06_warhammer40k_new40k_core_rules.pdf (read 2026-08-16)
  - reference/Source_Library.md

PURPOSE:
  Everything that happens between "we are going to play" and "battle round one
  begins": table size, terrain, objectives, deployment, and who goes first.

PRIMARY_AUDIENCE:
  - Two beginners setting up their first game at the kitchen table
  - A player preparing a board before an opponent arrives

KEY_SECTIONS_EXPECTED:
  - Table size
  - The pre-game sequence
  - Deployment zones and territory
  - Objectives
  - Reserves
  - Learning-game shortcuts

UPDATE_TRIGGER:
  Update when a new Event Companion, mission deck, or Core Rules version
  changes board size, the mission sequence, or deployment rules.
-->

# Board Setup - getting from empty table to battle round one

The mission you play defines the specifics. This page teaches the shape that every mission follows, using the sequence in the owned Event Companion Version 1.1, read **2026-08-16**. Core IDs point at [`../rules/Core_Rules_Quotes.md`](../rules/Core_Rules_Quotes.md). Event Companion mission layouts and base-size lists are **not dumped** this track.

**Contradiction check (2026-08-18):** 44"×60" board and the fourteen-step sequence still match Event Companion v1.1 p.1–2. Non-Core CP cap (1 per battle round, excluding Core CP) is already in the shipping glossary. No rewrite.

---

## Table size

| Format | Size |
|--------|------|
| **Standard event battlefield** | **44" by 60"** (Event Companion v1.1) |
| Combat Patrol and other small formats | Smaller; the owned A4 terrain pack includes a dedicated Combat Patrol battlezone layout |
| Learning games | Whatever you have. A 4' x 4' or even a 3' x 4' surface works to teach the sequence |

Any flat surface counts as the battlefield. Model bases cannot cross its edge, so mark it clearly if your table is bigger than the play area.

---

## The pre-game sequence

Fourteen steps, in order. Steps 1 to 6 are paperwork; the table only starts filling up at step 4.

| # | Step | What you do |
|---|------|-------------|
| 1 | **Muster Armies** | Build your list to the agreed points limit, choose your army faction and detachment, **and write your Force Disposition** (from the MFM tag on that detachment — e.g. Priority Assets). See [`Chapter_Approved_Force_Dispositions.md`](Chapter_Approved_Force_Dispositions.md) |
| 2 | **Determine Mission** | Match your Force Disposition card to your opponent’s → each player gets their **Primary Mission** (often different). Optional **Twist** only if agreed / TO allows |
| 3 | **Determine a Layout** | Pick or randomise one of the recommended terrain layouts |
| 4 | **Create the Battlefield** | Lay out the **terrain areas** first, then place terrain features on them - see [`Terrain_Basics.md`](Terrain_Basics.md) |
| 5 | **Determine Attacker and Defender** | Agree which table edge is whose, then roll off; the winner picks a role |
| 6 | **Select Secondary Missions** | Secretly choose Fixed or Tactical secondaries, then reveal |
| 7 | **Declare Battle Formations** | Secretly note which units start embarked in transports and which start in **strategic reserves**, then reveal |
| 8 | **Deploy Armies** | Alternate setting up units **wholly within** your deployment zone, starting with the **Defender** |
| 9 | **Redeploy Units** | Resolve any abilities that move units after deployment, alternating, starting with the Attacker |
| 10 | **Determine First Turn** | Roll off; the winner takes the first turn |
| 11 | **Resolve Pre-battle Rules** | Scout moves and other pre-battle abilities, alternating, starting with whoever goes first |
| 12 | **Begin the Battle** | Battle round one starts |
| 13 | **End the Battle** | After five battle rounds. Play them all out even if an army is wiped |
| 14 | **Determine Victor** | Total VP. Most wins; a tie is a draw |

> **Deploying second is not a punishment.** The Defender puts models down first, which means the Attacker sees the whole enemy army before committing. Rolling off for first turn is separate from the Attacker/Defender decision.

---

## Deployment zones and territory

Your mission's deployment map defines four regions:

| Region | What it is |
|--------|-----------|
| **Attacker's deployment zone** | Where the Attacker sets up, wholly within |
| **Defender's deployment zone** | Where the Defender sets up, wholly within |
| **No Man's Land** | Everything in neither deployment zone. Where the game is decided |
| **Territory** | The **half** of the board containing a player's deployment zone. Larger than the deployment zone, and some detachment rules key off it |

"Wholly within" means every part of every base. Measure before you commit a big unit.

---

## Objectives

Objectives are the points you are fighting over, and the maps mark three kinds:

| Type | Roughly where |
|------|---------------|
| **Home objective** | Inside or near your own deployment zone |
| **Central objective** | The middle of the board |
| **Expansion objective** | Contested ground toward the flanks and the enemy half |

Two mechanical details that trip beginners:

- **An objective is usually a terrain area, not a token.** If the map's objective point sits on a terrain area, that whole terrain area is the objective, and a model is in range simply by standing inside it.
- **Only where it does not** do you use a physical **objective marker**: a flat circular marker 40 mm across. Range to a marker is 3" horizontally and 5" vertically.

Control is decided by adding up **Objective Control (OC)** (**14.02**) and comparing totals, re-checked at the end of every phase and turn. See [`../rules/Key_Concepts.md`](../rules/Key_Concepts.md). **This is not Kill Team's 1" control range.**

---

## Strategic reserves

Decided at step 7, before anyone deploys:

- The combined points value of your reserves cannot exceed **50% of your points limit** (**20.01**).
- They arrive from the **second battle round** onward, via an ingress move (**20.03**, **20.04**).
- Normal arrivals come in within 6" of a battlefield edge, more than 8" from all enemies, and **not** in your opponent's deployment zone before the third battle round.
- Units with **Deep Strike** may instead arrive anywhere more than 8" from enemies.
- Anything still in reserve at the **end of the third battle round is destroyed**. Reserves are a timing tool, not a hiding place.

---

## Pre-game checklist

Print this, or keep it on your phone.

- [ ] Points limit agreed, both lists built to it
- [ ] Battlefield marked out - 44" x 60", or whatever you agreed
- [ ] Terrain **areas** defined and agreed before terrain features go down
- [ ] Every terrain feature agreed as **Exposed**, **Light**, or **Dense**
- [ ] Objectives placed per the layout; markers only where an objective is not a terrain area
- [ ] Primary Mission known by both players (**from Force Disposition matching** — each may have a different Primary)
- [ ] **Force Disposition written on both lists**
- [ ] Attacker and Defender decided; battlefield edges agreed
- [ ] Secondary Missions chosen and revealed
- [ ] Transports and strategic reserves declared and revealed
- [ ] Armies deployed, Defender first, alternating, wholly within deployment zones
- [ ] Redeployment abilities resolved
- [ ] First turn rolled off
- [ ] Pre-battle abilities (Scouts, Infiltrators already placed) resolved
- [ ] Dice, tape measure, and both armies' datasheets to hand

---

## Learning-game shortcuts

For a first game, cut everything that is not the core loop:

1. Use a small table and a small points limit.
2. Skip Secondary Missions entirely. Score only "who controls more objectives at the end of each battle round".
3. Use three objectives on a centre line rather than a full layout.
4. Deploy everything - no reserves for the first game or two.
5. Play three battle rounds, not five.

Add one piece of the real sequence back per game. By game four you will be running the whole thing without a checklist.

---

## Where the specifics live

This page teaches the pattern; the numbers come from the mission you are playing.

| Need | Source |
|------|--------|
| Board size, mission sequence, terrain layouts, scoring caps | `C:\Personal\40K\rules\eng_22-07_warhammer_40,000_event_companion-alyapl19us-b2drgwkji4.pdf` |
| Terrain rules, objectives, reserves | `C:\Personal\40K\rules\eng_01-06_warhammer40k_new40k_core_rules.pdf` |
| Printable terrain footprints (A4) | `C:\Personal\40K\Terrain\A4\` |
| Points | `C:\Personal\40K\rules\Warhammer 40,000_ Munitorum Field Manual.pdf` |
| Full catalogue of every owned source | [`reference/Source_Library.md`](../../../reference/Source_Library.md) |

---

## Related pages

- [`Terrain_Basics.md`](Terrain_Basics.md) - terrain categories, footprints, how much you need
- [`../rules/Overview.md`](../rules/Overview.md) - what a game is and how you win
- [`../rules/Turn_Structure.md`](../rules/Turn_Structure.md) - what happens once setup is done
- [`../rules/Key_Concepts.md`](../rules/Key_Concepts.md) - Objective Control and scoring

---

## Change Log
- v0.5.2 (2026-08-23): Link Force Disposition muster/matching; checklist row (starter-event feedback).
- v0.5.1 (2026-08-18): Rule-ID cites; Event Companion still inventoried not dumped (track `40k_warcom_quotes` S4/S5).
- v0.5.0 (2026-08-18): Project-wide semver snapshot (x.y.z).
- v1.0 (2026-08-16): Initial board setup guide (slice S3), from the owned Event Companion v1.1 and Core Rules PDF, both read 2026-08-16.

## Attribution
- Project: Wargame_Concierge
- Maintainer: Russell Catt
- Warhammer 40,000 is a trademark of Games Workshop Limited. This document is a personal teaching paraphrase and reproduces no publisher text.

## Rising Tide Notes
- This document follows Rising Tide documentation standards.
- **Verify before you play.** Cross-check anything here against the current Munitorum Field Manual and your faction pack - Games Workshop patches rules and points between publications. Content on this page reflects sources read on **2026-08-16**.
