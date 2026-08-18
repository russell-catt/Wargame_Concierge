<!--
FILE: START_HERE.md
VERSION: v0.5.0 (2026-08-18)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, slice S1)

DOCUMENT_TYPE: Onboarding / Entry Point
PROJECT_NAME: Wargame_Concierge
PROJECT_STATUS: Active - v0.5.0 snapshot

SOURCES:
  - README.md
  - AGENTS.md (KB schema source of truth)
  - docs/handoffs/v1_scaffold/track_in.md (track state)
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
  the project moves off track v1_scaffold.
-->

# START HERE

**Wargame_Concierge is a personal concierge for learning tabletop wargames.** It teaches the rules, walks through setting up a board, and helps build beginner army lists from the models actually sitting on the shelf.

The first systems in scope are **Warhammer 40,000, 11th Edition** (Necrons + Space Marines) and **Kill Team 2024 / 3e** (rules/reference shipped — see [`games/kill_team_2024/README.md`](games/kill_team_2024/README.md)). **Personal use only — never for sale.**

**Status:** **v0.5.0** (2026-08-18). Tags `v0.1.0` / `v0.5.0`. Later tracks via [`docs/handoffs/README.md`](docs/handoffs/README.md).

---

## Read order

Four files, in this order. Stop after step 2 if you only need to find something.

| # | Read | Why |
|---|------|-----|
| 1 | **`START_HERE.md`** (this file) | What the project is, the rules, where to go |
| 2 | [`README.md`](README.md) | Project overview, directory map, links to everything |
| 3 | [`KB/index.md`](KB/index.md) | Master catalog of the knowledge base |
| 4 | [`games/kill_team_2024/README.md`](games/kill_team_2024/README.md) then [`Patch_Manifest.md`](games/kill_team_2024/rules/Patch_Manifest.md) and [`Target_Eligibility.md`](games/kill_team_2024/rules/Target_Eligibility.md) | KT24 shipping (if you are playing or editing Kill Team) |
| 5 | [`docs/Rehydration_Prompt.md`](docs/Rehydration_Prompt.md) | Full context rebuild for an AI session |

**If you are an AI agent about to write anything:** read [`AGENTS.md`](AGENTS.md) too. It is the schema source of truth for the knowledge base and it is not optional.

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
2. **Never commit GW binaries.** No PDFs, no official images, no `.webp`. The external library at `C:\Personal\40K` stays outside this repo and is referenced by **markdown path pointer only**. [`.gitignore`](.gitignore) enforces this - do not bypass it.
3. **Teaching paraphrase in `KB/` and 40K shipping.** Under `games/kill_team_2024/` only, verbatim quotes from owned local KT24 PDFs are allowed (cite filename + page). Full-Scan baseline; dated `eng_*` patches supersede; Jul 25 lite is intro — omission is not a patch.
4. **Subagents never `git commit` or `git push` unless the user explicitly gates it.** Coordinator is the sole git owner otherwise.
5. **Only the Librarian writes under `KB/`.** Everyone else reads it and promotes from it with approval.
6. **Write UTF-8, no BOM.** A handful of early files got this wrong and produce unreadable diffs.

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

---

## One thing to know about trust

Warhammer 40,000 11th Edition is **new**, and the sources move under us. Every KB page carries a `confidence` value - `verified`, `draft`, `stub`, or `unverified` - and every rules claim records the date it was read.

**Treat `unverified` and `stub` as "do not take to the table without checking."** An honest uncertainty marker is worth more here than a confident guess. Cross-check against the local library or [Wahapedia](https://wahapedia.ru/) before a real game.

---

## Change Log

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
