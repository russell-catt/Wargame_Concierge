<!--
FILE: README.md
VERSION: v0.9.1 (2026-08-27)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, track dataslate_0826 S4)

DOCUMENT_TYPE: Project Overview
PROJECT_NAME: Wargame_Concierge
PROJECT_STATUS: Active - v0.9.0 pre-external-review

SOURCES:
  - START_HERE.md
  - AGENTS.md (KB schema source of truth)
  - docs/handoffs/README.md
  - games/README.md
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

A personal knowledge base and teaching assistant for **learning tabletop wargames** — the rules, the board setup, and how to build a beginner army list out of the models you actually own.

**New here? Read [`START_HERE.md`](START_HERE.md) first.**

---

## Overview

Most wargame rulebooks are written as reference, not as teaching. They tell you what a rule *is* without telling you why it matters or when it decides a game. This project closes that gap for one player at a time: it reads the sources once, files what it learned, and answers questions from its own notes instead of re-deriving everything from scratch.

That "file it once, answer forever" behaviour is the Karpathy **LLM Wiki** pattern (see [`reference/llm-wiki.md`](reference/llm-wiki.md)), adapted here to wargames. Knowledge **compounds** — the same ground is never covered twice.

| # | System | Path | Status |
|---|--------|------|--------|
| 1 | **Warhammer 40,000, 11th Edition** (Necrons + Space Marines) | [`games/warhammer_40k_11e/`](games/warhammer_40k_11e/) | Active — beginner spine + WD527 enhance |
| 2 | **Kill Team 2024** (KT24 / 3e) | [`games/kill_team_2024/`](games/kill_team_2024/) | Active — rules/reference shipped |
| 3 | **The Warcode** (RedMakers free beta v0.8.7-F) | [`games/the_warcode/`](games/the_warcode/) | Active — scaffold + card/map corpus |

**Personal use only — this project must never be sold.**

The architecture is game-agnostic. [`docs/Game_System_Scaffold.md`](docs/Game_System_Scaffold.md) is the checklist for the **next** system after these three.

---

## Goals

| Goal | What "done" looks like |
|------|------------------------|
| **Learn the rules** | Beginner-facing rules, turn structure, and key concepts that explain the *reasoning*, not just the wording |
| **Set up a board** | Deployment, terrain, objectives, and a pre-game checklist that works on a real table |
| **Build starter lists** | Small learning lists built from models actually owned, accounting for what still needs assembling |
| **Play without page-flipping** | Two-page print-and-laminate quick reference guides where the system warrants them |
| **Compound knowledge** | A `KB/` that grows with every source read and every question answered |
| **Stay reusable** | A scaffold that carries to another game system without reinventing folders |

---

## The four-layer architecture

Every file in this repo belongs to exactly one layer. Do not conflate them — the contract is defined in [`AGENTS.md`](AGENTS.md) Sec 2.

| Layer | Path | Who writes | Contract |
|-------|------|-----------|----------|
| **Raw sources** | [`raw/`](raw/) | Coordinator / Implementer copy-in only | **Immutable.** No GW binaries (scoped Warcode free-beta PDF exception) |
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
├── .gitignore                     <- blocks GW binaries; Warcode beta PDF negation
├── .obsidian/                     <- Obsidian vault config
├── raw/                           <- immutable allowed sources
│   ├── pointers/                  <- path pointers to C:\Personal\40K, Kill Team, Warcode, WD527
│   ├── the_warcode/               <- free beta PDF + OCR/transcription sidecars (allowed)
│   └── white_dwarf_527/           <- research notes (markdown only)
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
│   ├── warhammer_40k_11e/         <- system #1
│   ├── kill_team_2024/            <- system #2
│   └── the_warcode/               <- system #3
├── reference/                     <- external patterns and seed context
├── templates/                     <- Rising Tide + GW print footer fragments
├── checkins/                      <- decision and build session notes
└── prompts/                       <- prompt history and reusable agent prompts
```

Full detail: [`docs/Project_Structure.md`](docs/Project_Structure.md). Systems index: [`games/README.md`](games/README.md).

---

## How to use this repo

### As a player

1. Open [`KB/index.md`](KB/index.md) and find the topic.
2. Check the `confidence` column. Anything marked `unverified` or `stub` needs a cross-check before you rely on it at a table.
3. For terminology, go straight to [`KB/glossary.md`](KB/glossary.md).
4. Teaching content lives under [`games/`](games/) — pick the system subtree above.

### As an AI session

1. Read [`AGENTS.md`](AGENTS.md) — schema, entity types, frontmatter, workflows, copyright.
2. Read [`KB/index.md`](KB/index.md) to orient.
3. Read the last few entries in [`KB/log.md`](KB/log.md).
4. If working a slice, read the brief under [`docs/handoffs/`](docs/handoffs/).
5. Full bootstrap: [`docs/Rehydration_Prompt.md`](docs/Rehydration_Prompt.md).

### As an Obsidian vault

Open the repo root as a vault. `[[wikilinks]]` and the graph view span `KB/`, `docs/`, and `games/`.

---

## Working conventions

| Convention | Rule |
|-----------|------|
| **Headers** | `KB/**` uses YAML frontmatter only. `docs/**`, `games/**`, and root docs use Rising Tide HTML headers and footers. The two **do not stack** |
| **Filenames** | `KB/` uses lowercase `snake_case`. Shipping `docs/` and `games/` use Rising Tide `Snake_Case` |
| **Confidence** | Every KB page carries `verified` / `draft` / `stub` / `unverified`. Be conservative |
| **Retrieval dates** | Every living-reference rules claim records the date it was read |
| **Encoding** | UTF-8, no BOM |
| **Git** | Coordinator alone commits, except when the user explicitly gates commit+push |

---

## Copyright and sourcing

This is a personal learning knowledge base, **not** a redistribution channel. **Personal use only — never for sale.**

**Games Workshop IP (40K / Kill Team shipping):** Kill Team is Copyright Games Workshop Limited 2024. Warhammer 40,000 is Copyright Games Workshop Limited. Player-facing `games/warhammer_40k_11e/**` and `games/kill_team_2024/**` (especially print HTML) must carry an **UNOFFICIAL** banner and non-endorsement footer — see [`templates/Footer_Template_Gw_Print.md`](templates/Footer_Template_Gw_Print.md) and [`AGENTS.md`](AGENTS.md) Sec 10.

**The Warcode (RedMakers):** Free public beta may be quoted under `games/the_warcode/rules|setup|factions/` only. The beta PDF may live in [`raw/the_warcode/`](raw/the_warcode/) (gitignore exemption). In `games/the_warcode/**` shipping, **never** use GW proper nouns — use **That other game** / **Murder Platoon** / **Rawmallet** / **39.876** / **39.9** instead.

Hard rules:

- **Never** commit Games Workshop PDFs, official datasheet images, or other GW binaries. [`.gitignore`](.gitignore) blocks them — do not bypass it (**except** the scoped Warcode free-beta PDF / map PNG / xlsx under `raw/the_warcode/`)
- Owned libraries stay **outside** git: `C:\Personal\40K`, `C:\Personal\Kill Team` — markdown path pointers only
- Write **teaching paraphrase** in `KB/` and `docs/`
- **Scoped verbatim quotes (shipping only):**
  - KT24 → `games/kill_team_2024/` (owned local PDFs; Full-Scan baseline; dated `eng_*` supersede)
  - 40K WarCom-free Core → `games/warhammer_40k_11e/rules/` and `setup/` (filename + page + rule ID; **Codex wall** on army folders)
  - Warcode free beta → `games/the_warcode/rules|setup|factions/` (filename + page; OCR when needed)
- Cite where every claim can be checked, with a **retrieval date** on living refs

### Living references

| Reference | Use for |
|-----------|---------|
| [Warhammer Community](https://www.warhammer-community.com/en-gb/) | Official rules updates, FAQs, errata, balance dataslates |
| [Wahapedia](https://wahapedia.ru/) | Consolidated rules and datasheet lookup when WarCom does not publish profiles |
| `C:\Personal\40K` / `C:\Personal\Kill Team` | Owned PDFs — **pointers only** |
| [The Warcode pre-launch](https://pre-launch.thewarcode.com/) | Warcode marketing / VIP context (secondary to the free beta PDF) |

Patches happen. Re-check before a real game.

---

## Project status

**v0.9.0 (2026-08-25).** Three systems onboarded (Warcode applied). Phase: **pre-external-review**. **Next:** external user review and critique. Tracks: [`docs/handoffs/README.md`](docs/handoffs/README.md). Decisions: [`docs/Project_Planning.md`](docs/Project_Planning.md).

**Rules currency:** GW balance packages move faster than this file. Each system's own README carries the current stamp — see [`games/README.md`](games/README.md) for the per-system pointer table. This file never repeats the package details; it only points at where they live.

---

## Key documents

| Document | What it answers |
|----------|-----------------|
| [`START_HERE.md`](START_HERE.md) | Where do I begin? |
| [`AGENTS.md`](AGENTS.md) | How is the knowledge base structured? |
| [`games/README.md`](games/README.md) | Which game systems are in the repo? |
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

- v0.9.1 (2026-08-27): Project status — added a "Rules currency" pointer line to `games/README.md`'s per-system stamp table, so a reader lands on the current package/quarterly currency without this file duplicating it (track `dataslate_0826` slice S4).
- v0.9.0 (2026-08-25): Project snapshot v0.9.0; next milestone external user review and critique.
- v0.5.6 (2026-08-25): Three-system overview (Warcode); copyright/sourcing aligned with AGENTS Sec 10; structure map and status refreshed.
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
