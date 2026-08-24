<!--
FILE: games/the_warcode/rules/Turn_Structure.md
VERSION: v0.1 (2026-08-23)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, warcode_tactical_doctrine)

DOCUMENT_TYPE: Teaching Guide / Play Checklist
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: The Warcode
REFERENCE_STATUS: Active — draft, beta v0.8.7-F (2026-08-23)

SOURCES:
  - raw/the_warcode/The Warcode Rulebook V.0.8.7-F.pdf (read via extract 2026-08-23)
  - raw/the_warcode/rulebook_v087f_extract.txt

PURPOSE:
  A do-this-then-this checklist from empty table through end of game. Written
  to be readable at the table mid-game.

PRIMARY_AUDIENCE:
  - A player mid-game who has lost the thread
  - A first-time player walking through their first round

KEY_SECTIONS_EXPECTED:
  - Pre-game setup
  - Round frame
  - Initiative Phase
  - Tactical Phase / unit activation
  - End of Round
  - Common mistakes

UPDATE_TRIGGER:
  Update when beta supersedes v0.8.7-F on phase order, activation rules, or
  end-of-round sequencing.
-->

# Turn Structure — the checklist for a round

Read top to bottom. **`confidence: draft`**, beta **v0.8.7-F**, read **2026-08-23**. Page cites point at [`Rulebook_Quotes.md`](Rulebook_Quotes.md).

Pre-game board work is in [`../setup/Board_Setup.md`](../setup/Board_Setup.md).

---

## Before round 1 — game setup

Complete these steps **once**, before the Initiative Phase of round 1:

- [ ] **Read the scenario** — objectives, victory conditions, special rules, deployment zones, and how many rounds the game lasts.
- [ ] **Prepare the board** — 33" × 24" surface, terrain, doors, VP tokens (see [`../setup/Board_Setup.md`](../setup/Board_Setup.md)).
- [ ] **Roll D6 for initiative (round 1)** — highest roll chooses **who deploys first** *and* **who activates first** in round 1. Re-roll ties.
- [ ] **Deploy units** — players alternate placing **one unit each** until all squads are on the board.
- [ ] **Distribute equipment** — each player has **4 equipment points** to buy grenades (2 pts) and/or medkits (2 pts) for units, unless unit rules forbid other gear.

> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.2 — "SETUP"  
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.3 — "INITIATIVE PHASE"

---

## The frame around every round

Each **round** = **Initiative Phase** → **Tactical Phase** → **End of Round**.

From round 2 onward, the initiative roll only decides **activation order** for that round (deployment is already done).

---

## 1. Initiative Phase

*What you are deciding: who activates first this round.*

- [ ] Both players roll **one D6**.
- [ ] **Highest roll** takes the first activation in the upcoming Tactical Phase.
- [ ] **Tie?** Both re-roll until one player wins.

---

## 2. Tactical Phase

*What you are deciding: which unit acts, and how it spends its 2 AP.*

Players **alternate activating exactly one unit** until every unit has activated or passed.

### When you activate a unit

- [ ] Confirm the unit's activation token shows **"can activate this round."**
- [ ] The unit has **2 Action Points (AP)** for this activation (unless an ability modified AP — rare).
- [ ] Perform one or more **actions**, paying AP each time, until you **Pass** or cannot afford further actions.
- [ ] After the unit finishes its activation, flip its token to **"already activated."**

### Actions available on activation

| Action | Typical AP cost | Notes |
|--------|-----------------|-------|
| **Move** | 1 | Up to Movement Range in inches; penalties for friends/partial cover apply |
| **Shoot** | Weapon profile | Needs ammo ≥ 1 and line of sight |
| **Reload** | Weapon profile | Restores ammo to maximum |
| **Overwatch** | 1 | Needs ammo ≥ 1; not in melee; no further actions this round |
| **Melee combat** | Weapon profile | Only if enemy within melee range |
| **Engage** | 2 | Boosted move (+2") into melee |
| **Disengage from Melee Lock** | 1 | Roll D6 vs enemy melee strength |
| **Escape from Melee Lock** | 2 | Same roll as Disengage; you move even on failure |
| **Use ability** | Per ability | If the unit has one |
| **Use equipment** | Usually 1 (grenade throw) | Medkit use costs **0 AP** |
| **Interact** | 0 AP | Pick up ground items; open/close doors when in range |
| **Pass** | — | Skip remaining AP; **does not** trigger enemy Overwatch |

> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.4 — "UNIT ACTIVATION"

**Pick up items** and **open/close doors** cost **0 AP** when the unit is already within 1 inch; otherwise spend 1 AP to move into range first.

### Activation loop

- [ ] First player activates one unit → second player activates one unit → repeat.
- [ ] Continue until **both** players have activated every unit (or passed with all units).

---

## 3. End of Round

*What you are deciding: nothing — resolve triggers and score.*

Resolve in this order:

- [ ] **End-of-round unit abilities** — effects that fire "at end of the round."
- [ ] **Scenario effects** — event / Protocol cards if the scenario uses them.
- [ ] **Victory Point calculation** — uncontested VP tokens within 1 inch of friendly units score; contested tokens score for nobody.
- [ ] **Contracts** — if VP difference is **1 or more**, the trailing player draws one contract (see [`Key_Concepts.md`](Key_Concepts.md)).
- [ ] **Flip all activation tokens** back to "can activate" for the new round.
- [ ] **Remove Overwatch tokens** from any units still overwatching.

> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.3 — "END OF THE ROUND"

### Final round

- [ ] If the scenario says this was the **last round**, determine the winner from scenario victory conditions (VP total, elimination, tie rules).
- [ ] Otherwise, return to **Initiative Phase** for the next round.

---

## Common mistakes

| Mistake | Correct habit |
|---------|----------------|
| Activating the same unit twice in one round | One activation per unit per round — token flip is the reminder |
| Shooting with 0 ammo | Reload first, or pick a different action |
| Forgetting Overwatch ends your activation | Overwatch costs 1 AP and **locks out** all other actions that round |
| Passing to bait Overwatch | **Pass does not trigger Overwatch** — only the listed enemy actions do |
| Scoring VP mid-round | VP tokens pay out at **end of round** only |
| Opening a door blocked by an enemy within 1 inch | Door is **blocked** — see [`../setup/Terrain_Basics.md`](../setup/Terrain_Basics.md) |

---

## Related pages

- [`Overview.md`](Overview.md) — big-picture game shape
- [`Key_Concepts.md`](Key_Concepts.md) — how shooting and melee resolve inside an activation
- [`Keyword_Glossary.md`](Keyword_Glossary.md) — quick term lookup
- [`Rulebook_Quotes.md`](Rulebook_Quotes.md) — verbatim phase text
- [`../setup/Board_Setup.md`](../setup/Board_Setup.md) — deployment and VP placement

---

## Open questions

- Exact ordering when multiple end-of-round triggers conflict — confirm in full rulebook if scenarios stack effects.
- Default round count when a scenario omits it — not stated in the current extract.

---

## Change Log

- v0.1 (2026-08-23): Initial turn-structure checklist from beta v0.8.7-F extract.

## Attribution

- Project: Wargame_Concierge
- Maintainer: Russell Catt
- The Warcode is property of RedMakers. Unofficial teaching paraphrase.

## Rising Tide Notes

- This document follows Rising Tide documentation standards.
- Keep activation tokens visible — they are the round's memory.
