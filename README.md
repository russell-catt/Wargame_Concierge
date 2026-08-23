<!--
FILE: README.md
VERSION: v0.5.1 (2026-08-23)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, slice S1)

DOCUMENT_TYPE: Project Overview
PROJECT_NAME: Wargame_Concierge
PROJECT_STATUS: Active - v0.5.1 snapshot

SOURCES:
  - START_HERE.md
  - AGENTS.md (KB schema source of truth)
  - docs/handoffs/v1_scaffold/track_in.md
  - reference/llm-wiki.md (Karpathy "LLM Wiki" pattern)

PURPOSE:
  Project overview and directory map. Explains the goals, the four-layer
  knowledge architecture, and where every kind of file belongs, with links out
  to the documents that go deeper.

PRIMARY_AUDIENCE:
  - New contributors
  - Reviewers
  - AI systems rebuilding context

KEY_SECTIONS_EXPECTED:
  - Overview
  - Goals
  - Structure
  - How to Use

UPDATE_TRIGGER:
  Update when project scope, directory layout, or the onboarding flow changes.
-->

# Wargame_Concierge

A personal knowledge base and teaching assistant for **learning tabletop wargames** - the rules, the board setup, and how to build a beginner army list out of the models you actually own.

**New here? Read [`START_HERE.md`](START_HERE.md) first.**

---

## Overview

Most wargame rulebooks are written as reference, not as teaching. They tell you what a rule *is* without telling you why it matters or when it decides a game. This project closes that gap for one player at a time: it reads the sources once, files what it learned, and answers questions from its own notes instead of re-deriving everything from scratch.

That "file it once, answer forever" behaviour is the Karpathy **LLM Wiki** pattern (see [`reference/llm-wiki.md`](reference/llm-wiki.md)), adapted here to wargames. Knowledge **compounds** - the same ground is never covered twice.

**First system:** Warhammer 40,000, 11th Edition (Necrons + Space Marines).
**Second system:** Kill Team 2024 — onboarded under [`games/kill_team_2024/`](games/kill_team_2024/README.md).
**Personal use only — this project must never be sold.**

The architecture is game-agnostic. [`docs/Game_System_Scaffold.md`](docs/Game_System_Scaffold.md) is the checklist for **system #3**.

---

## Goals

| Goal | What "done" looks like |
|------|------------------------|
| **Learn the rules** | Beginner-facing rules, turn structure, and key concepts that explain the *reasoning*, not just the wording |
| **Set up a board** | Deployment, terrain, objectives, and a pre-game checklist that works on a real table |
| **Build starter lists** | Small learning lists built from models actually owned, accounting for what still needs assembling |
| **Play without page-flipping** | Two-page print-and-laminate quick reference guides, one per faction |
| **Compound knowledge** | A `KB/` that grows with every source read and every question answered |
| **Stay reusable** | A scaffold that carries to a second game system without reinventing folders |

---

## The four-layer architecture

Every file in this repo belongs to exactly one layer. Do not conflate them - the contract is defined in [`AGENTS.md`](AGENTS.md) Sec 2.

| Layer | Path | Who writes | Contract |
|-------|------|-----------|----------|
| **Raw sources** | [`raw/`](raw/) | Coordinator / Implementer copy-in only | **Immutable.** No GW binaries, ever |
| **Knowledge base** | [`KB/`](KB/) | **Librarian agent** | Working synthesis: entity pages, index, log, glossary |
| **Shipping** | [`docs/`](docs/), [`games/`](games/) | Implementers | Player-facing truth, promoted from `KB/` after review |
| **Reference** | [`reference/`](reference/) | Read-only | External patterns and seed context. Not project truth |

> This project uses **`KB/`**, never `wiki/`. The Karpathy pattern names the middle layer `wiki/`; translate accordingly and do not create a `wiki/` directory.

`.obsidian/` at the repo root makes the whole repo an Obsidian vault, so `[[wikilinks]]` and graph view work across `KB/`, `docs/`, and `games/`.

---

## Structure map

```text
Wargame_Concierge/
├── START_HERE.md                  <- read this first
├── README.md                      <- you are here
├── AGENTS.md                      <- KB schema source of truth (Librarian contract)
├── .gitignore                     <- blocks GW binaries, secrets, scratchpad
├── .obsidian/                     <- Obsidian vault config
├── raw/                           <- immutable allowed sources
│   └── pointers/                  <- path pointers to C:\Personal\40K, C:\Personal\Kill Team, and living URLs
├── KB/                            <- the knowledge base (Librarian owns)
│   ├── index.md                   <- master catalog - start every lookup here
│   ├── log.md                     <- append-only activity log
│   ├── overview.md                <- high-level synthesis
│   ├── glossary.md                <- living terminology; home of all Keywords
│   ├── changelog.md               <- promotion log (KB -> docs/ or games/)
│   ├── ingest_procedure.md        <- how raw/ becomes KB/
│   └── sources|concepts|factions|detachments|units|setup|analyses/
├── docs/                          <- shipping reference
│   ├── README.md                  <- docs index
│   ├── Project_Structure.md       <- full layout and ownership rules
│   ├── Project_Planning.md        <- decisions, status, open questions
│   ├── Project_Origin_Story.md    <- why this project exists
│   ├── Rehydration_Prompt.md      <- AI session bootstrap
│   ├── Game_System_Scaffold.md    <- reusable checklist for a new game system
│   ├── operations/                <- playbook + Librarian day-to-day ops
│   └── handoffs/                  <- multi-agent track artifacts
├── games/                         <- per-system teaching content
│   ├── warhammer_40k_11e/         <- first system
│   └── kill_team_2024/            <- second system (Patch_Manifest, Target_Eligibility)
├── reference/                     <- external patterns and seed context
├── templates/                     <- Rising Tide header/footer fragments
├── checkins/                      <- decision and build session notes
└── prompts/                       <- prompt history and reusable agent prompts
```

Full detail, including which slice creates what: [`docs/Project_Structure.md`](docs/Project_Structure.md).

---

## How to use this repo

### As a player

1. Open [`KB/index.md`](KB/index.md) and find the topic.
2. Check the `confidence` column. Anything marked `unverified` or `stub` needs a cross-check before you rely on it at a table.
3. For terminology, go straight to [`KB/glossary.md`](KB/glossary.md).
4. Teaching content lands under [`games/`](games/) as slices S3 through S6 complete.

### As an AI session

1. Read [`AGENTS.md`](AGENTS.md) - schema, entity types, frontmatter, workflows.
2. Read [`KB/index.md`](KB/index.md) to orient.
3. Read the last few entries in [`KB/log.md`](KB/log.md).
4. If working a slice, read the brief under [`docs/handoffs/`](docs/handoffs/).
5. Full bootstrap: [`docs/Rehydration_Prompt.md`](docs/Rehydration_Prompt.md).

### As an Obsidian vault

Open the repo root as a vault. `[[wikilinks]]` and the graph view span `KB/`, `docs/`, and `games/`. The inherited `.obsidian/` config is a structural placeholder only - Obsidian generates its own settings on first open.

---

## Working conventions

| Convention | Rule |
|-----------|------|
| **Headers** | `KB/**` uses YAML frontmatter only. `docs/**`, `games/**`, and root docs use Rising Tide HTML headers and footers. The two **do not stack** - a leading HTML comment breaks frontmatter parsing |
| **Filenames** | `KB/` uses lowercase `snake_case`. Shipping `docs/` and `games/` use Rising Tide `Snake_Case` |
| **Confidence** | Every KB page carries `verified` / `draft` / `stub` / `unverified`. Be conservative |
| **Retrieval dates** | Every living-reference rules claim records the date it was read. A claim with no date is a lint finding |
| **Encoding** | UTF-8, no BOM |
| **Git** | Coordinator alone commits, except when the user explicitly gates commit+push |

---

## Copyright and sourcing

This is a personal learning knowledge base, **not** a redistribution channel.

- **Never** commit Games Workshop PDFs, official datasheet images, or other GW binaries. [`.gitignore`](.gitignore) blocks them; do not bypass it
- The owned library at `C:\Personal\40K` stays **outside** this repo - markdown path pointers only
- Write **teaching paraphrase** in `KB/` and `docs/`. **Quote exceptions (shipping only):** KT24 under `games/kill_team_2024/`; 40K WarCom-free Core under `games/warhammer_40k_11e/rules/` and `setup/` (filename + page + rule ID). **Codex wall** on 40K army folders. Core / Full-Scan baseline; dated `eng_*` supersede; omission is not a patch
- Cite where every claim can be checked, so a reader can verify against material they own

### Living references

11th Edition is current and changing. These are the moving sources of record:

| Reference | Use for |
|-----------|---------|
| [Warhammer Community](https://www.warhammer-community.com/en-gb/) | Official rules updates, FAQs, errata, balance dataslates |
| [Wahapedia](https://wahapedia.ru/) | Consolidated rules and datasheet lookup for cross-checking |
| `C:\Personal\40K` (local) | Owned PDFs and personal notes - **pointers only** |

Patches happen. Re-check before a real game.

---

## Project status

**v0.5.0 snapshot (2026-08-18).** Tags `v0.1.0` (bootstrap) and `v0.5.0`. KT24 rules/reference landed. Later tracks: [`docs/handoffs/README.md`](docs/handoffs/README.md). 40K beginner spine: [`docs/handoffs/v1_scaffold/track_in.md`](docs/handoffs/v1_scaffold/track_in.md) (historical).

---

## Key documents

| Document | What it answers |
|----------|-----------------|
| [`START_HERE.md`](START_HERE.md) | Where do I begin? |
| [`AGENTS.md`](AGENTS.md) | How is the knowledge base structured? |
| [`docs/README.md`](docs/README.md) | What documentation exists? |
| [`docs/Project_Structure.md`](docs/Project_Structure.md) | Where does this file go? |
| [`docs/Project_Planning.md`](docs/Project_Planning.md) | What has been decided, and what is open? |
| [`docs/Project_Origin_Story.md`](docs/Project_Origin_Story.md) | Why does this exist? |
| [`docs/Game_System_Scaffold.md`](docs/Game_System_Scaffold.md) | How do I add another game? |
| [`docs/Rehydration_Prompt.md`](docs/Rehydration_Prompt.md) | How does an AI pick up where it left off? |
| [`docs/operations/multiagent_coordinator_strategy.md`](docs/operations/multiagent_coordinator_strategy.md) | How does the multi-agent workflow run? |
| [`docs/operations/librarian_agent.md`](docs/operations/librarian_agent.md) | How does the Librarian operate day to day? |

---

## Change Log

- v0.5.1 (2026-08-23): Date stamp refresh.
- v0.5.0 (2026-08-18): Project-wide semver snapshot (x.y.z). Second system KT24; read-order and quote exception.
- v1.0 (2026-08-16): Initial project overview - goals, four-layer architecture, structure map, conventions, copyright policy. Created in slice S1.

## Attribution

- Project: Wargame_Concierge
- Maintainer: Russell Catt
- Pattern: Karpathy "LLM Wiki" (see [`reference/llm-wiki.md`](reference/llm-wiki.md))
- Structured using the Rising Tide framework

## Rising Tide Notes

- This document follows Rising Tide documentation standards.
- Keep the receipts. Make AI show their work.
- Must remain understandable, reproducible, and reusable.
