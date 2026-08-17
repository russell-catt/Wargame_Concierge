<!--
FILE: games/kill_team_2024/rules/Overview.md
VERSION: v1.0 (2026-08-17)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, slice S1)

DOCUMENT_TYPE: Teaching Guide / Beginner Overview
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: Kill Team - 2024 / 3rd Edition (KT24)
REFERENCE_STATUS: Draft - written from the living Wahapedia core rules page; not yet cross-checked against the owned Core Rules PDF

SOURCES:
  - raw/pointers/kill_team_2024_core.md (points at C:\Personal\Kill Team\kill_team_2024\779937548-Core-Rules-KILL-TEAM-3E-Full-Scan.pdf - not yet opened this slice)
  - https://wahapedia.ru/kill-team3/the-rules/core-rules/ (retrieved 2026-08-17)
  - https://wahapedia.ru/kill-team3/the-rules/approved-ops-2025/ (retrieved 2026-08-17)
  - games/kill_team_2024/README.md (vocabulary mapping)
  - KB/sources/kill_team_2024_core_rules.md and KB/concepts/turning_points.md (Librarian L1, landed in parallel with this slice - same living source, cross-checked as consistent)

PURPOSE:
  Answer "what actually happens in a game of Kill Team?" for someone who
  knows Warhammer 40,000 already and needs the skirmish-scale differences,
  or who is starting from zero.

PRIMARY_AUDIENCE:
  - A player who has read the 40K Overview and is now learning the second
    system in this project
  - A first-time Kill Team player walking through their first battle

KEY_SECTIONS_EXPECTED:
  - What a game actually is
  - The shape of a battle
  - How you win
  - What a kill team is made of
  - What you need to play
  - Coming from Warhammer 40,000

UPDATE_TRIGGER:
  Update when a new Core Rules printing, Approved Ops pack, or errata changes
  the turning-point structure, scoring framework, or battle length.
-->

# Overview - what a game of Kill Team is

Everything below is teaching paraphrase - our own explanation of how the game works, cross-checked against the living Wahapedia core rules page on **2026-08-17**. The owned Core Rules PDF has not been opened yet this slice; treat everything here as `draft` until it is.

---

## What a game actually is

Kill Team is a **skirmish** game: each player fields a handful of individually-sculpted **operatives** - roughly 6 to 20 depending on the team - rather than a 40K-scale army. You still move, shoot, and fight, but every model matters, cover is constant, and a single bad activation can lose you an operative for good.

You do not win by wiping out the enemy team. You win by scoring **Victory Points (VP)** from the mission's **ops** - almost always a mix of holding objective markers and taking down enemy operatives. Killing things helps, but it is one of several roads to VP, not the goal itself.

A game is called a **battle**. Under the current **Approved Ops 2025** matched-play framework, a battle runs a fixed **four turning points** and then stops, regardless of how many operatives are left on either side.

---

## The shape of a battle

Kill Team's structure is flatter than 40K's. Learn these four words:

| Piece | What it is |
|-------|-----------|
| **Battle** | The whole game. Four turning points under Approved Ops 2025. |
| **Turning point** | One full round. Contains a Strategy phase, then a Firefight phase. Both players act in both phases. |
| **Strategy phase** | Bookkeeping and setup for the turning point: who has initiative, gaining CP, readying operatives, playing strategy ploys. |
| **Firefight phase** | Where the battle actually happens: players alternate activating one ready operative at a time until both sides are done. |

There is no separate "movement phase" or "shooting phase" the way 40K has them. Each **operative**, when activated, can do almost anything in any order - move, shoot, fight, pick up a marker - as long as it can afford the **AP** (action points) cost and the order it is on allows it. That is the single biggest structural difference from 40K: **the phase tells you what kind of thing is happening; the operative's activation is where all the decisions live.**

Full phase-by-phase checklist: [`Turn_Structure.md`](Turn_Structure.md).

---

## How you win

VP come from **ops** - named scoring conditions revealed over the course of the battle. The current matched-play pack (**Approved Ops 2025**) uses three:

| Op | Scores VP for |
|----|---------------|
| **Crit Op** | Performing mission actions and controlling objective markers |
| **Kill Op** | Incapacitating enemy operatives |
| **Tac Op** | A secretly-selected secondary objective drawn from your kill team's archetype (Infiltration, Recon, Security, or Seek & Destroy) |

Each op caps at 6VP. At the start of the battle each player also secretly locks in one of the three as their **primary op**, and scores a bonus for it at the end. Casual and narrative mission packs (Volkus, Shadowhunt, the 3e Starter Set, and similar) use their own simpler op or objective structure - check the mission pack in play rather than assuming Approved Ops applies.

High-level detail on ops and Orders lives in [`Key_Concepts.md`](Key_Concepts.md); this is intentionally not a full ops writeup - Approved Ops card text is not reproduced here.

---

## What a kill team is made of

| Layer | What it is | Kill Team term |
|-------|-----------|-----------------|
| **Your force** | The full roster you own for a faction | **Kill team** |
| **Force-wide ability** | A rule every operative in the team gets | **Faction rule / team rule** |
| **Rules package** | Ploys and equipment your team can call on | **Strategic and Firefight ploys**, **equipment** |
| **Individual model** | One named or generic fighter, with its own stat line | **Operative**, on a **datacard** |

There is no points-based list-build the way 40K has a Munitorum Field Manual. Team selection is usually **by operative count and role slot**, set by your kill team's own rules and the mission pack's selection step - see [`../teams/README.md`](../teams/README.md) once team content lands.

> **Vocabulary discipline:** this project says **team** and **operative**, never **army** and **unit**, anywhere under `games/kill_team_2024/`. See the mapping table in [`../README.md`](../README.md).

---

## What you need to play

| Thing | Detail |
|-------|--------|
| **A kill team** | Assembled operatives for each player |
| **A killzone** | The board and terrain - Volkus, Gallowdark, Shadowhunt, and others each have their own kit |
| **A mission pack** | Tells you the game sequence, drop zones, and which ops apply |
| **Dice** | A minimum of ten D6 per player is the stated recommendation |
| **A measuring device in inches** | Kill Team measures in inches, same as 40K |
| **Tokens and markers** | Order tokens (Ready/Expended, Conceal/Engage), objective markers (40mm), other markers (20mm) |

Board and killzone specifics are in [`../setup/README.md`](../setup/README.md) once populated (S2).

---

## Coming from Warhammer 40,000

If you already know 40K, most of the friction is vocabulary and scale, not new ideas:

| You know this from 40K | Kill Team's version | The real difference |
|---|---|---|
| Army / unit | **Kill team / operative** | Every model is tracked and activates individually - there are no multi-model "units" |
| Battle round, five phases | **Turning point**, two phases (Strategy, Firefight) | Movement/shooting/fighting all happen inside one operative's activation, not in separate phases |
| Alternating unit activation (Fight phase only) | **Alternating operative activation, all battle** | You alternate one operative at a time for the whole Firefight phase, not just melee |
| Command Points (CP), stratagems | **Command Points (CP), ploys** | Same currency idea; ploys split into Strategic (Strategy phase) and Firefight (Firefight phase) |
| Engagement Range (2"/5") | **Control range (1")** | Much tighter - see [`Key_Concepts.md`](Key_Concepts.md) |
| Objective Control (OC) stat | **APL used to contest/control markers** | A model's APL, not a dedicated OC stat, decides who controls a marker |
| Battle-shock | *(no direct equivalent)* | Kill Team's pressure valve is the **Injured** state on individual operatives, not a squad-level morale test |

Full term-by-term list, including flagged collisions: [`Keyword_Glossary.md`](Keyword_Glossary.md). The Librarian's parallel KB pass reached the same collisions independently - see [`../../../KB/glossary.md`](../../../KB/glossary.md) (Kill Team 2024 section) and [`../../../KB/concepts/turning_points.md`](../../../KB/concepts/turning_points.md).

---

## Related pages

- [`Turn_Structure.md`](Turn_Structure.md) - the Strategy phase and Firefight phase, step by step
- [`Key_Concepts.md`](Key_Concepts.md) - APL, Orders, control range, cover, Injured, and mission scoring
- [`Keyword_Glossary.md`](Keyword_Glossary.md) - every term in one place, with 40K collisions flagged
- [`../README.md`](../README.md) - the vocabulary mapping table for this whole game system
- [`../setup/README.md`](../setup/README.md) - killzones and board setup (populated in S2)

---

## Change Log
- v1.0 (2026-08-17): Initial teaching overview (slice S1), written from the living Wahapedia core rules and Approved Ops 2025 pages, both retrieved 2026-08-17. Owned Core Rules PDF not yet opened - status `draft`. Cross-cited against `KB/concepts/turning_points.md` and `KB/sources/kill_team_2024_core_rules.md`, landed by the Librarian (L1) in parallel with this slice from the same source.

## Attribution
- Project: Wargame_Concierge
- Maintainer: Russell Catt
- Kill Team and Warhammer 40,000 are trademarks of Games Workshop Limited. This document is a personal teaching paraphrase and reproduces no publisher text or datacard statlines.

## Rising Tide Notes
- This document follows Rising Tide documentation standards.
- **Verify before you play.** Cross-check anything here against the owned Core Rules PDF and current Approved Ops pack - this page currently rests on a living web source only, retrieved **2026-08-17**.
