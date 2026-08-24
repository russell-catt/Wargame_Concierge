<!--
FILE: games/the_warcode/rules/Overview.md
VERSION: v0.1 (2026-08-23)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, warcode_tactical_doctrine)

DOCUMENT_TYPE: Teaching Guide / Beginner Overview
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: The Warcode
REFERENCE_STATUS: Active — draft, beta v0.8.7-F (2026-08-23)

SOURCES:
  - raw/the_warcode/The Warcode Rulebook V.0.8.7-F.pdf (read via extract 2026-08-23)
  - raw/the_warcode/rulebook_v087f_extract.txt
  - games/the_warcode/README.md

PURPOSE:
  Answer "what actually happens in a game of The Warcode?" for someone who has
  never played. Covers the shape of a game, how you win, what a squad is made
  of, and what you need on the table.

PRIMARY_AUDIENCE:
  - A player learning The Warcode from zero
  - Cross-game readers coming from Murder Platoon or 40K who need vocabulary first

KEY_SECTIONS_EXPECTED:
  - What a game is
  - The shape of a game
  - How you win
  - What a squad is
  - What you need to play
  - Your realistic first game

UPDATE_TRIGGER:
  Update when a newer free beta supersedes v0.8.7-F on the same topics, or when
  round count / force size is confirmed elsewhere in the rulebook.
-->

# Overview — what a game of The Warcode is

Everything below is teaching paraphrase from the free beta rulebook **V.0.8.7-F**, read **2026-08-23**. **`confidence: draft`** — usable for learning, but confirm scenario-specific details before a competitive table. Verbatim rule text lives in [`Rulebook_Quotes.md`](Rulebook_Quotes.md).

**This subtree is unofficial and unauthorized.** Personal learning only — not endorsed by RedMakers or Gamefound.

---

## What a game actually is

Two players each command a **squad** of miniatures on a fixed board. You take turns **activating one unit at a time**, spending **Action Points (AP)** to move, shoot, reload, fight in melee, use equipment, and interact with the map. Dice decide whether attacks hit, penetrate armor, and how much damage they deal.

The beginner trap to avoid: **killing every enemy model is not always the only win condition.** Most games score **Victory Points (VP)** from controlling map objectives and completing **Contracts**. Elimination and VP both matter — the scenario tells you which path wins.

---

## The shape of a game

The game runs in **rounds**. Each round has two phases:

| Phase | What happens |
|-------|----------------|
| **Initiative Phase** | Roll a D6. Highest roll goes first this round. In **round 1 only**, this roll also decides deployment order. Ties re-roll until broken. |
| **Tactical Phase** | Players alternate activating **one unit each**. An activated unit spends AP on actions until it passes or runs out of AP. |

After the Tactical Phase, resolve **end-of-round** effects (unit abilities, scenario events, VP scoring), then start the next round — unless it was the **final round**, in which case you determine the winner from the scenario.

> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.3 — "GAME PHASES OVERVIEW"

The full step-by-step checklist is in [`Turn_Structure.md`](Turn_Structure.md).

---

## How you win

**Victory Points (VP)** are the default scoring currency. You earn VP by:

- **Capturing VP tokens** on the map — a unit must be within **1 inch** of the token with **no enemy units** in that radius at end of round. If both sides have units in the radius, the point is **contested** and nobody scores it.
- **Completing Contracts** — if you trail by 1+ VP at end of a round, you draw a secret contract to eliminate a specific enemy unit for bonus VP.

At game end, **most VP wins** unless the scenario adds elimination or tie-break rules. The sample scenario *Core of the Machine* also allows winning by wiping the enemy squad or swaying the machine core with VP.

Contracts, re-rolls, and combat resolution are unpacked in [`Key_Concepts.md`](Key_Concepts.md).

---

## What a squad is

Each player fields a **fixed squad** from a faction roster — **eight units** in the beta lists shown in the rulebook (not a points-buy list). Before play you:

1. Pick your faction and units per scenario or roster rules.
2. **Deploy** units alternately after an initiative roll (round 1).
3. Spend **4 equipment points** per player on grenades and/or medkits (unless a unit's special rules restrict equipment).

Every unit has core stats — **Health (HP)**, **Agility (A)**, **Armor**, and **Movement Range (M)** — plus ranged and/or melee weapon profiles. Each unit receives **2 AP per round** when activated.

---

## What you need to play

| Item | Notes |
|------|-------|
| **Board** | **33" × 24"** playing surface for standard scenarios |
| **Squads** | Eight models per player (faction roster) |
| **Dice** | D6 for initiative, hit checks, penetration, disengage, grenades |
| **Measuring** | Inch ruler — movement, range, VP control, blast radii |
| **Tokens** | Activation, Overwatch, ammunition, VP, equipment, grenade blast |
| **Scenario** | Objectives, deployment zones, round count, special rules |
| **Protocol / event cards** | Scenario-dependent; some pages may need OCR — see open questions |

Terrain, doors, and cover types are covered in [`../setup/Terrain_Basics.md`](../setup/Terrain_Basics.md). Pre-game sequence lives in [`../setup/Board_Setup.md`](../setup/Board_Setup.md).

---

## Your realistic first game

1. Read [`Turn_Structure.md`](Turn_Structure.md) once — the alternating-activation loop is the heartbeat of the game.
2. Skim [`Keyword_Glossary.md`](Keyword_Glossary.md) when a stat icon or term confuses you mid-game.
3. Play the bundled **Core of the Machine** scenario on a 33" × 24" board with partial cover, full-cover walls, and doors.
4. Expect **close-range gunfights, overwatch traps, and melee locks** — movement through friends and cover costs inches, and agility bonuses from cover stack up fast.

If you know **Murder Platoon** (That other game's skirmish mode): think smaller fixed rosters, **AP per activation** instead of a shared pool, and **alternating single-unit activations** rather than "all my operatives, then all yours."

---

## Related pages

- [`Turn_Structure.md`](Turn_Structure.md) — round phases and activation checklist
- [`Key_Concepts.md`](Key_Concepts.md) — shooting, melee, cover, equipment, contracts
- [`Keyword_Glossary.md`](Keyword_Glossary.md) — terms at a glance
- [`Rulebook_Quotes.md`](Rulebook_Quotes.md) — verbatim beta text with page cites
- [`../setup/Board_Setup.md`](../setup/Board_Setup.md) — table size and pre-game sequence
- [`../setup/Terrain_Basics.md`](../setup/Terrain_Basics.md) — cover, doors, movement penalties

---

## Open questions

- **Round count:** The extract references a "final round" but does not state a default number of rounds for all scenarios. Confirm per scenario card or a rules page outside the current extract.
- **Protocol Cards:** Referenced for scenario events; OCR content not yet in the teaching corpus.

---

## Change Log

- v0.1 (2026-08-23): Initial teaching overview from beta v0.8.7-F extract (warcode_tactical_doctrine).

## Attribution

- Project: Wargame_Concierge
- Maintainer: Russell Catt
- The Warcode is property of RedMakers. This document is unofficial personal teaching paraphrase.

## Rising Tide Notes

- This document follows Rising Tide documentation standards.
- **Verify before you play.** Cross-check against the current free beta PDF — rules may change before Gamefound release.
