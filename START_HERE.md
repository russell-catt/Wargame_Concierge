<!--
FILE: START_HERE.md
VERSION: v0.9.1 (2026-08-27)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, track dataslate_0826 S4)

DOCUMENT_TYPE: Onboarding / Entry Point
PROJECT_NAME: Wargame_Concierge
PROJECT_STATUS: Active - v0.9.0 pre-external-review

SOURCES:
  - README.md
  - AGENTS.md (KB schema source of truth)
  - games/README.md
  - docs/handoffs/README.md
  - docs/operations/multiagent_coordinator_strategy.md

PURPOSE:
  First file anyone - human or AI - should open in this repo. Explains what the
  project is, sets the read order, and states the hard rules before any work
  starts.

PRIMARY_AUDIENCE:
  - The project owner returning after time away
  - A new AI session with no memory of this project
  - Anyone handed this repo cold

UPDATE_TRIGGER:
  Update when the read order changes, a new top-level entry point appears, or
  a new game system is onboarded.
-->

# START HERE

**Wargame_Concierge is a personal concierge for learning tabletop wargames.** It teaches the rules, walks through setting up a board, and helps build beginner army lists from the models actually sitting on the shelf.

**Systems in scope:**

| # | System | Start here |
|---|--------|------------|
| 1 | Warhammer 40,000, 11th Edition (Necrons + Space Marines) | [`games/warhammer_40k_11e/README.md`](games/warhammer_40k_11e/README.md) |
| 2 | Kill Team 2024 / 3e | [`games/kill_team_2024/README.md`](games/kill_team_2024/README.md) |
| 3 | The Warcode (RedMakers free beta) | [`games/the_warcode/README.md`](games/the_warcode/README.md) |

**Personal use only — never for sale.**

**Status:** **v0.9.0** (2026-08-25) — pre-external-review. **Next:** external user review and critique. Tracks: [`docs/handoffs/README.md`](docs/handoffs/README.md).

**Rules currency:** GW balance packages (40K, Kill Team) move on their own schedule. Check the system README in the table above for the current stamp — this file and `README.md` never carry package details themselves.

---

## Read order

| # | Read | Why |
|---|------|-----|
| 1 | **`START_HERE.md`** (this file) | What the project is, the rules, where to go |
| 2 | [`README.md`](README.md) | Project overview, directory map, copyright |
| 3 | [`KB/index.md`](KB/index.md) | Master catalog of the knowledge base |
| 4 | The system README for the game you are playing or editing (table above) | Shipping spine for that system |
| 5 | [`docs/Rehydration_Prompt.md`](docs/Rehydration_Prompt.md) | Full context rebuild for an AI session |

**If you are an AI agent about to write anything:** read [`AGENTS.md`](AGENTS.md) too. It is the schema source of truth and it is not optional.

---

## What lives where

The short version. The full map is in [`docs/Project_Structure.md`](docs/Project_Structure.md).

| Path | Contains | Who writes it |
|------|----------|---------------|
| [`raw/`](raw/) | Immutable allowed sources | Coordinator / Implementer copy-in only |
| [`KB/`](KB/) | The compounding knowledge base | **Librarian agent only** |
| [`docs/`](docs/) | Shipping reference: structure, planning, operations, handoffs | Implementers |
| [`games/`](games/) | Per-system teaching content | Implementers |
| [`reference/`](reference/) | External pattern docs and seed context | Read-only after creation |
| [`templates/`](templates/) | Rising Tide header and footer fragments | Copy from, do not edit |

---

## Hard rules

These are not style preferences. Breaking any of them is a defect.

1. **Never write under `raw/`.** Immutability is the point of the layer. Read it, cite it, summarize it elsewhere.
2. **Never commit GW binaries.** No GW PDFs or official images. Owned libraries at `C:\Personal\40K` and `C:\Personal\Kill Team` stay outside the repo — **markdown path pointers only**. Scoped exception: Warcode free-beta PDF under `raw/the_warcode/` (see [`AGENTS.md`](AGENTS.md) Sec 10).
3. **Teaching paraphrase in `KB/` and `docs/`.** Scoped verbatim quotes only under the paths in AGENTS Sec 10 (KT24, 40K WarCom-free Core, Warcode free beta).
4. **In `games/the_warcode/**` shipping,** never name GW proper nouns — use That other game / Rawmallet / 39.9 / 39.876.
5. **Subagents never `git commit` or `git push` unless the user explicitly gates it.** Coordinator is the sole git owner otherwise.
6. **Only the Librarian writes under `KB/`.** Everyone else reads it and promotes from it with approval.
7. **Write UTF-8, no BOM.**

---

## Where to go for what

| I want to... | Go to |
|--------------|-------|
| Understand the whole project | [`README.md`](README.md) |
| Know why this project exists | [`docs/Project_Origin_Story.md`](docs/Project_Origin_Story.md) |
| Find where a file should live | [`docs/Project_Structure.md`](docs/Project_Structure.md) |
| See decisions already made | [`docs/Project_Planning.md`](docs/Project_Planning.md) |
| Add a new game system | [`docs/Game_System_Scaffold.md`](docs/Game_System_Scaffold.md) |
| Look something up in the KB | [`KB/index.md`](KB/index.md), then [`KB/glossary.md`](KB/glossary.md) |
| Write or maintain KB pages | [`AGENTS.md`](AGENTS.md), then [`docs/operations/librarian_agent.md`](docs/operations/librarian_agent.md) |
| Run or review a work slice | [`docs/handoffs/README.md`](docs/handoffs/README.md) |
| Restart a cold AI session | [`docs/Rehydration_Prompt.md`](docs/Rehydration_Prompt.md) |
| Play The Warcode | [`games/the_warcode/README.md`](games/the_warcode/README.md) |

---

## One thing to know about trust

Warhammer 40,000 11th Edition and The Warcode free beta are both **moving**. Every KB page carries a `confidence` value — `verified`, `draft`, `stub`, or `unverified` — and every rules claim records the date it was read.

**Treat `unverified` and `stub` as "do not take to the table without checking."** An honest uncertainty marker is worth more here than a confident guess.

---

## Change Log

- v0.9.1 (2026-08-27): Added a "Rules currency" cue pointing at each system's own README for the current balance-package stamp (track `dataslate_0826` slice S4).
- v0.9.0 (2026-08-25): Snapshot v0.9.0; next milestone external user review and critique.
- v0.5.6 (2026-08-25): Three systems (Warcode); hard rules and read order refreshed.
- v0.5.1 (2026-08-23): Date stamp refresh (rule test #2).
- v0.5.0 (2026-08-18): Project-wide semver snapshot (x.y.z). Read order includes KT README / Patch_Manifest / Target_Eligibility.
- v1.0 (2026-08-16): Initial onboarding entry point. Created in slice S1.

## Attribution

- Project: Wargame_Concierge
- Maintainer: Russell Catt
- Structured using the Rising Tide framework

## Rising Tide Notes

- This document follows Rising Tide documentation standards.
- Keep the receipts. Make AI show their work.
- If the read order in this file is wrong, every downstream session starts wrong. Fix it first.
