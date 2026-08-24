<!--
FILE: games/kill_team_2024/critical_ops/README.md
VERSION: v0.5.0 (2026-08-18)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, slice S2)

DOCUMENT_TYPE: Teaching Guide / Section README
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: Kill Team 2024 (3rd Edition / KT24)
OWNERSHIP_STATUS: Both physical decks owned (2024 + 2025 vintages) - track_in.md, Preflight lock 2026-08-17
REFERENCE_STATUS: Active - draft, teaching paraphrase cross-checked against Wahapedia/Warhammer Community coverage of Approved Ops 2025 (retrieved 2026-08-17); not yet spot-checked card-by-card against the owned decks

SOURCES:
  - raw/pointers/kill_team_2024_critical_ops.md (owned deck printables, 2024 + 2025)
  - raw/pointers/kill_team_2024_approved_ops.md (Approved Ops 2025 tournament companion + update log)
  - Warhammer Community - "Kill Team Approved Ops 2025" preview (retrieved 2026-08-17)
  - Goonhammer - "Kill Team Approved Ops 2025" review (retrieved 2026-08-17)
  - Games Workshop Wiki (Fandom) - "Tac Ops" article, Critical Ops / Approved Ops product history (retrieved 2026-08-17)
  - ../setup/Board_Setup.md (game sequence this deck plugs into)

PURPOSE:
  Explain what the owned Critical Ops decks actually contain, a naming
  ambiguity worth flagging, and how they plug into the game sequence taught
  in setup/Board_Setup.md - without listing or transcribing individual cards.

UPDATE_TRIGGER:
  Update when a new yearly card pack is acquired, or when the owned decks are
  physically inventoried card-by-card.
-->

# Critical Ops - owned mission/objective decks

**Status: Both physical decks owned (2024 + 2025 vintages).** This page explains what they are and how they plug into a game; **table aid content (a printable cheat-sheet) is a separate S7 deliverable.**

---

## Terminology note - worth flagging up front

"**Critical Ops**" was the official product name for the 2022 card pack that first bundled Tac Ops, mission cards, and a matched-play sequence for the *previous* (2021/2e) edition. For the current (2024/3e) edition, Games Workshop's equivalent product is officially called "**Approved Ops**" (updated yearly - the owned local printables under `Critical Ops\2024\` and `Critical Ops\2025\` line up with Approved Ops-era content: Crit Op, Tac Op, and Game Sequence cards for 2024 and 2025).

This project keeps the **folder name `critical_ops/`** because that's how the owned decks are organised on disk (`C:\Personal\Kill Team\kill_team_2024\Critical Ops\2024\` and `\2025\`), but treat "Critical Ops" here as **this household's name for its owned Approved-Ops-era mission decks**, not as a claim that a product literally called "Critical Ops" exists for KT24. Flag this explicitly if it ever causes confusion against official Warhammer Community coverage, which uses "Approved Ops."

---

## What's in a deck like this

A yearly Approved-Ops-era pack is a card-based toolkit for building and running a matched-play mission, roughly:

| Card type | What it's for |
|-----------|---------------|
| **Crit Ops** | The primary objective for the battle - how most Victory Points get scored |
| **Tac Ops** | Secondary, chosen (not randomised) objectives - typically three archetypes such as Seek and Destroy, Recon, Security, Infiltration, plus a faction-specific option |
| **Map cards** | Terrain layouts for specific killzones (Volkus, Bheta-Decima, Tomb World, and general non-specific boards) |
| **Game Sequence / Scouting cards** | The numbered steps for setting up and running a matched-play battle - this is the pack-specific detail behind the general shape taught in [`../setup/Board_Setup.md`](../setup/Board_Setup.md) |
| **Initiative-modifier cards** | Compensation for losing roll-offs, so bad luck early doesn't snowball all game |

**No card text, art, or full lists are reproduced anywhere in this repository.** This page teaches the *categories* of card and how they're used, not their contents.

---

## How the owned decks plug into a game

Using the game-sequence shape from [`../setup/Board_Setup.md`](../setup/Board_Setup.md):

1. **Setup** - draw a Map card matching the killzone you're using (or a non-specific one) to decide terrain placement; draw or agree a shared Crit Op and place its objective markers.
2. **Turning point one, Strategy Phase** - each player secretly picks one of the available Ops types to be their **Primary Op** for bonus scoring at the end of the game.
3. **Through the battle** - Tac Ops score as their card specifies (some reveal immediately, some only when first scored). Initiative-modifier cards get spent by whoever loses roll-offs.
4. **End of battle** - Primary Ops are revealed and scored on top of whatever else was scored during the game.

Both owned vintages (2024, 2025) should work for this - the 2025 pack is described as the *current* one where the two differ, per Warhammer Community's own framing of updating this pack yearly.

---

## When to introduce these decks

Per the learning-game shortcuts in [`../setup/Board_Setup.md`](../setup/Board_Setup.md): **skip this deck for the very first game or two.** Secret Primary Op selection, three chosen Tac Ops, and initiative-modifier cards are exactly the kind of bookkeeping that overwhelms two brand-new players. Use the Starter Handbook's own simplified missions ([`../setup/killzones/starter_set_3e.md`](../setup/killzones/starter_set_3e.md)) or a single obvious win condition first, then bring in Crit Ops/Tac Ops once the core loop (orders, actions, cover) is comfortable.

---

## Do not

- Scan, photograph, or otherwise reproduce card art
- Transcribe full Tac Op or Crit Op text into any repo file
- Assume the 2024 and 2025 decks are interchangeable without checking - Approved Ops content is explicitly described as updated yearly

---

## What to check in the owned decks

- Whether the "2024" folder is genuinely an Approved-Ops-era 2024 pack or an older Critical Ops-branded product - the naming ambiguity above is a hypothesis, not a confirmed fact
- Exact card counts and archetypes present in each owned vintage
- Which Map cards are included for which killzones (Volkus coverage matters most given the play-now priority)

---

## Related pages

- [`../setup/Board_Setup.md`](../setup/Board_Setup.md) - the game sequence this deck plugs into
- [`../setup/killzones/README.md`](../setup/killzones/README.md) - killzones these decks provide maps for
- [`../../../raw/pointers/kill_team_2024_critical_ops.md`](../../../raw/pointers/kill_team_2024_critical_ops.md) - local printable paths

---

## Games Workshop notice

**UNOFFICIAL.** This document is completely unofficial and in no way endorsed by Games Workshop Limited. Personal / no-charge use only — never for sale. Warhammer, Kill Team and associated marks are trademarks of Games Workshop Limited. Used without permission. No challenge to their status intended. Kill Team is Copyright Games Workshop Limited 2024. Teaching notes by Russell Catt (Wargame Concierge). Games Workshop retains IP in the settings and characters. No official logos.

## Change Log
- v0.5.0 (2026-08-18): Project-wide semver snapshot (x.y.z).
- v1.0 (2026-08-17): Expanded from S0 stub to a teaching page (slice S2) - deck contents, terminology-drift flag (Critical Ops vs Approved Ops), how it plugs into the game sequence, and when to introduce it. No card art or full text transcribed.
- v0.1 (2026-08-17): S0 stub - ownership note and pointer link only.

## Attribution
- Project: Wargame_Concierge
- Maintainer: Russell Catt
- Warhammer 40,000: Kill Team is a trademark of Games Workshop Limited. This document is a personal teaching paraphrase and reproduces no publisher text, card art, or card lists.

## Rising Tide Notes
- This document follows Rising Tide documentation standards.
- **Verify before you play.** The Critical Ops/Approved Ops naming note above is a hypothesis based on file-path patterns, not a confirmed read of the owned decks. Confirm exact card contents and vintage against the physical decks before matched play. Content reflects sources read on **2026-08-17**.
