<!--
FILE: games/kill_team_2024/setup/Board_Setup.md
VERSION: v1.0 (2026-08-17)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, slice S2)

DOCUMENT_TYPE: Teaching Guide / Pre-game Checklist
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: Kill Team 2024 (3rd Edition / KT24)
REFERENCE_STATUS: Active - draft, teaching paraphrase cross-checked against Wahapedia KT3 (retrieved 2026-08-17); not yet spot-checked line-by-line against the owned printed rulebook

SOURCES:
  - raw/pointers/kill_team_2024_core.md (Core Rules, primary PDF owned; not read directly this slice)
  - raw/pointers/kill_team_2024_approved_ops.md (Approved Ops 2025 tournament companion)
  - raw/pointers/kill_team_2024_missions.md (mission packs incl. Volkus Compound)
  - Wahapedia Kill Team 3 rules hub - https://wahapedia.ru/kill-team3/the-rules/ (community cross-check, retrieved 2026-08-17)
  - reference/Source_Library.md

PURPOSE:
  Everything that happens between "we are going to play" and "turning point one
  begins": what you need, table/killzone size habits, the shape of the game
  sequence, drop zones and territory, and a pre-game checklist.

PRIMARY_AUDIENCE:
  - Two beginners setting up their first game of Kill Team 2024
  - A player preparing a killzone before an opponent arrives

KEY_SECTIONS_EXPECTED:
  - What you need
  - Killzone (board) size
  - The shape of the game sequence
  - Drop zones and territory
  - Pre-game checklist
  - Learning-game shortcuts

UPDATE_TRIGGER:
  Update when a new Approved Ops card pack, Core Book errata, or mission pack
  changes the game sequence, board sizes, or deployment habits.
-->

# Board Setup - getting from empty table to turning point one

Kill Team is a **skirmish** game - small teams, tight boards, close-range decisions. Setup matters more here than in a big-army game: the terrain you place *is* the tactical puzzle. This page teaches the shape of setup that (almost) every killzone and mission pack follows. Cross-checked against the Wahapedia KT3 rules hub, read **2026-08-17**; the exact wording and numbered steps live in the owned Core Book and mission pack PDFs.

---

## What you need

| Item | Notes |
|------|-------|
| **Two kill teams** | Rosters built from a team's rules (`teams/`) |
| **A killzone** | A game board plus its terrain features - see [`killzones/`](killzones/) |
| **A mission pack** | Tells you how the battle is scored and how long it lasts - the Starter Handbook, a box's dossier, or the Approved Ops card pack |
| **A tape measure in inches** | Kill Team measures everything in inches, including on metric-labelled boards |
| **10+ six-sided dice per player** | More is faster - buy in bulk |
| **Tokens and markers** | Objective markers (40 mm), order tokens, and whatever your mission pack needs |

---

## Killzone (board) size

**Unless a specific killzone says otherwise, a Kill Team game board is 30" x 22"** (roughly 76 cm x 56 cm). Most boxed killzones stick to this:

| Owned killzone | Board | Notes |
|-----------------|-------|-------|
| [`Volkus`](killzones/volkus.md) | Standard 30" x 22" | Double-sided cityfight board |
| [`3e Starter Set`](killzones/starter_set_3e.md) | Standard-sized, double-sided | Ships in the box; no separate purchase needed |
| [`Tomb World`](killzones/tomb_world.md) | ~606 mm x 703 mm, laid out on a **6x7 grid** | Close-quarters killzone family (same lineage as Killzone: Gallowdark) - grid squares replace free inch measurement for setup, not for in-game distances |
| [`Shadowhunt`](killzones/shadowhunt.md) | Two **half-size** boards | Built for "Descent" missions that stack an upper and lower killzone; needs Volkus + Tomb World terrain to use fully |
| [`2e starter scatter`](killzones/starter_set_2e_scatter.md) | No board of its own (shipped with a paper mat) | Filler pieces only - see the page for why it can't replace a real killzone |

Any flat surface roughly this size works for a learning game. What matters is that both players agree on the boundary before terrain goes down.

---

## The shape of the game sequence

Every mission pack (the Starter Handbook, a box dossier, or the yearly Approved Ops card pack) writes its own numbered **game sequence**, and the exact steps differ pack to pack. But nearly all of them follow this shape:

### 1. Setup

- Each player selects a kill team.
- Agree the killzone and set up its terrain - using the mission pack's **map**, or improvised terrain if you're not using a specific map (see [`Terrain_Basics.md`](Terrain_Basics.md)).
- Place objective markers as the mission specifies (almost always on the killzone floor).
- **Roll off.** The winner decides who has initiative before the battle and picks a **drop zone**; the loser gets some form of compensation (in Approved Ops 2025, a card that lets them adjust a future initiative roll).

### 2. Select operatives and equipment

- Both players secretly choose which operatives from their roster are in the battle, then reveal together.
- Both players secretly choose equipment options, then reveal together.

### 3. Deploy

- Players alternate setting up operatives in **thirds** of their kill team (rounding up), starting with whoever has initiative.
- Every operative must be set up **wholly within** its own drop zone.
- Every operative starts with a **Conceal order** - nobody starts Engaged.

### 4. Scouting (or equivalent pre-battle step)

- Many mission packs give each player a small secret choice here (an extra equipment pick, a free pre-battle move, or a one-off free ploy) that also decides who has initiative in turning point one.
- Simpler intro missions (the Starter Handbook, most box-set scenarios) skip this and just roll off.

### 5. Play the battle

- The battle is a sequence of **turning points**. Each turning point is a Strategy Phase (ready operatives, gain Command Points, use Strategic Gambits) followed by a Firefight Phase (players alternate activating operatives until both sides are done).
- Matched-play missions typically run **four turning points**; intro/box-set missions may run fewer for a shorter first game. Check your mission pack.
- Whoever loses the initiative roll-off each turning point usually gets some compensation, and the player with initiative decides ties.

### 6. End the battle and score

- The mission pack's win condition (usually total Victory Points from a Crit Op and up to three Tac Ops) decides the winner.

> **This is the pattern, not the rulebook.** The turn-by-turn detail of the Strategy and Firefight phases (orders, actions, APL) is core-rules teaching content that belongs on the `rules/` pages once written. This page only covers getting the table ready and understanding the outer shape of a game.

---

## Drop zones and territory

- A **drop zone** is the region where you set up your operatives - always **wholly within** it.
- Mission maps typically give each player a drop zone in a corner or along an edge, sized so both teams start with breathing room and at least some terrain to hide behind.
- The area of the board nearer your drop zone is sometimes called your **territory**, and some faction and mission rules key off whether an operative or objective is in your territory versus your opponent's.
- **Drop zone shape and size are defined per mission map**, not fixed - a Volkus map, a Tomb World map, and a generic non-specific map can each hand you a different-shaped drop zone. Read the map you're using.

---

## Pre-game checklist

Print this, or keep it on your phone.

- [ ] Both rosters built and legal for the mission pack you're using
- [ ] Killzone agreed and its board laid flat
- [ ] Terrain features placed per the mission map (or per the asymmetric-setup guidance in [`Terrain_Basics.md`](Terrain_Basics.md) if there's no map)
- [ ] Every terrain part's category agreed out loud - Light, Heavy, Exposed, and so on
- [ ] Objective markers placed per the mission
- [ ] Roll-off resolved; drop zones assigned
- [ ] Operatives and equipment selected in secret and revealed together
- [ ] Kill teams deployed in thirds, wholly within drop zones, all starting Concealed
- [ ] Scouting step (or equivalent) resolved if your mission pack has one
- [ ] Dice, tape measure, tokens, and both teams' datacards to hand

---

## Learning-game shortcuts

For a genuine first game between two beginners, strip it down further:

1. **Use the Starter Set or Volkus with the simplest mission in the box.** Save the Approved Ops card pack (Crit Ops, Tac Ops, secret primary objectives) for once the core loop clicks - see [`../critical_ops/README.md`](../critical_ops/README.md).
2. Skip the Scouting step - just roll off for initiative in turning point one.
3. Play a single, obvious win condition (e.g. "control more objective markers at the end of the battle") rather than three secretly-selected Tac Ops.
4. Use fewer terrain features than a full layout calls for - a cluttered board is harder to referee than a sparse one while you're both learning line of sight.
5. Play three turning points instead of four if a full battle is dragging.

Add one real piece of the sequence back per game. By game three or four you'll be running Approved Ops without a cheat sheet.

---

## Where the specifics live

| Need | Source |
|------|--------|
| Exact game sequence, turning point count, orders/actions | `C:\Personal\Kill Team\kill_team_2024\779937548-Core-Rules-KILL-TEAM-3E-Full-Scan.pdf` and the Starter Handbook in the box |
| Matched-play sequence, Crit Ops, Tac Ops, initiative cards | `C:\Personal\Kill Team\kill_team_2024\Critical Ops\2024\` and `\2025\` - see [`../critical_ops/README.md`](../critical_ops/README.md) |
| Killzone-specific maps and drop zones | The mission pack for that killzone - see [`killzones/`](killzones/) |
| Full catalogue of every owned source | [`reference/Source_Library.md`](../../../reference/Source_Library.md) |

---

## Related pages

- [`Terrain_Basics.md`](Terrain_Basics.md) - terrain categories and how much terrain a killzone needs
- [`killzones/README.md`](killzones/README.md) - owned kill zones and their play-now status
- [`../critical_ops/README.md`](../critical_ops/README.md) - how the owned Critical Ops decks plug into the sequence above
- [`../rules/README.md`](../rules/README.md) - the in-battle rules spine (Strategy/Firefight phase detail lands here)

---

## Change Log
- v1.0 (2026-08-17): Initial board setup guide (slice S2), cross-checked against the Wahapedia KT3 rules hub and Approved Ops 2025 summary, both read 2026-08-17.

## Attribution
- Project: Wargame_Concierge
- Maintainer: Russell Catt
- Warhammer 40,000: Kill Team is a trademark of Games Workshop Limited. This document is a personal teaching paraphrase and reproduces no publisher text.

## Rising Tide Notes
- This document follows Rising Tide documentation standards.
- **Verify before you play.** This page teaches the *shape* of setup from a community cross-check (Wahapedia), not a line read of the owned Core Book or mission pack PDFs. Before your first real game, confirm the exact numbered game sequence, turning point count, and drop zone sizes in the mission pack you're actually using - the Starter Handbook, a box dossier, or the Approved Ops card pack. Content reflects sources read on **2026-08-17**.
