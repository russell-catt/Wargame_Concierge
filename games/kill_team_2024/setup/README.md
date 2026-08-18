<!--
FILE: games/kill_team_2024/setup/README.md
VERSION: v0.5.0 (2026-08-18)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, slice S2)

DOCUMENT_TYPE: Index / Section README
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: Kill Team 2024 (3rd Edition / KT24)
REFERENCE_STATUS: Active - content authored in S2

SOURCES:
  - games/kill_team_2024/setup/Board_Setup.md
  - games/kill_team_2024/setup/Terrain_Basics.md
  - games/kill_team_2024/setup/killzones/README.md
  - docs/handoffs/kill_team_2024_scaffold/track_in.md

PURPOSE:
  Index for board and terrain setup, and the entry point for choosing which
  owned killzone to play on.

UPDATE_TRIGGER:
  Update when a setup document is added or revised, or when a killzone's
  ownership status changes.
-->

# Setup - Kill Team 2024 (3rd Edition)

**Status:** Populated in **S2**, cross-checked against the Wahapedia KT3 rules hub and community coverage of Approved Ops 2025, both read **2026-08-17**. Killzone-specific pages are teaching pages, not transcriptions of any official terrain reference sheet or mission map.

Everything that happens before turning point one, plus the terrain rules that make Kill Team the game it is.

---

## Documents

| File | What it covers |
|------|-----------------|
| [`Board_Setup.md`](Board_Setup.md) | What you need, killzone board size (30" x 22" unless stated otherwise), the shape of the game sequence (Setup -> Select Operatives -> Deploy -> Scouting -> Battle -> Score), drop zones and territory, a pre-game checklist, and beginner shortcuts |
| [`Terrain_Basics.md`](Terrain_Basics.md) | Terrain features as parts, the core terrain types (Heavy, Light, Exposed, Insignificant, Accessible, Blocking, Vantage), Cover vs Obscured, terrain and movement, and how to lay out a killzone that plays well |
| [`killzones/`](killzones/) | One page per owned kill zone - what it is, ownership status, and how to set it up |

---

## Play-now priority

For a first game between two beginners: **Volkus** or the **3e Starter Set**. See [`killzones/README.md`](killzones/README.md) for the full ownership table and why the other kill zones aren't first-game picks yet.

---

## The two things beginners get wrong

1. **Cover and Obscured are different questions.** Cover asks whether an operative can be targeted at all; Obscured asks how much a successful shot is worth once it's in. Both are explained in [`Terrain_Basics.md`](Terrain_Basics.md).
2. **The game sequence is per-mission-pack, not fixed.** The Starter Handbook, a box dossier, and the Approved Ops card pack each write their own numbered steps - `Board_Setup.md` teaches the shared *shape*, not a single canonical sequence.

---

## Related

- [`../critical_ops/README.md`](../critical_ops/README.md) - the owned mission/objective decks that plug into the game sequence
- [`../rules/README.md`](../rules/README.md) - the in-battle rules spine (orders, actions, phases)
- [`../README.md`](../README.md) - the Kill Team 2024 subtree entry point

---

## Change Log
- v0.5.0 (2026-08-18): Project-wide semver snapshot (x.y.z).
- v1.0 (2026-08-17): Replaced the S0 stub with a real index. Board_Setup, Terrain_Basics, and all five killzone pages authored (slice S2).
- v0.1 (2026-08-17): Stub created (slice S0).

## Attribution
- Project: Wargame_Concierge
- Maintainer: Russell Catt

## Rising Tide Notes
- This document follows Rising Tide documentation standards.
- **Verify before you play.** Cross-check anything in this section against the owned Core Book, mission packs, and killzone reference sheets - Games Workshop patches rules and terrain between publications. Content reflects sources read on **2026-08-17**.
