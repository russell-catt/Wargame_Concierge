<!--
FILE: docs/Project_Structure.md
VERSION: v1.0 (2026-08-16)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, slice S1)

DOCUMENT_TYPE: Reference / Project Layout
PROJECT_NAME: Wargame_Concierge
PROJECT_STATUS: Active

SOURCES:
  - AGENTS.md (Sec 2 layer contract, Sec 3 directory structure)
  - README.md
  - docs/operations/librarian_agent.md
  - docs/handoffs/v1_scaffold/track_in.md

PURPOSE:
  Authoritative map of the repository. Defines what each directory holds, who
  is allowed to write there, and how to decide where a new file belongs.

PRIMARY_AUDIENCE:
  - Anyone adding a file to this repo
  - Implementer and Librarian agents
  - Reviewers checking that a slice put things in the right place

UPDATE_TRIGGER:
  Update when a directory is added, removed, or changes owner. Schema-level
  changes to KB/ layout belong in AGENTS.md first, then here.
-->

# Project Structure

Where everything lives, who owns it, and how to decide where something new goes.

**Schema authority:** `KB/` layout, entity types, and frontmatter are defined in [`../AGENTS.md`](../AGENTS.md). If this document and `AGENTS.md` disagree about `KB/`, `AGENTS.md` wins and this file is the bug.

---

## 1. The five trees

Everything in the repo sits in one of five trees. The distinction that matters is **who is allowed to write there**.

| Tree | Path | Writer | Contract |
|------|------|--------|----------|
| **Raw** | `raw/` | Coordinator / Implementer copy-in only | **Immutable** once written. Librarian reads, never writes |
| **Knowledge** | `KB/` | **Librarian agent only** | Working synthesis. Every page carries YAML frontmatter and a `confidence` value |
| **Shipping** | `docs/`, `games/` | Implementers; Librarian drafts promotions | Reviewed truth. Promotion from `KB/` requires approval and a changelog row |
| **Reference** | `reference/` | Written once, then read-only | External patterns and seed context. **Not project truth** |
| **Support** | `templates/`, `checkins/`, `prompts/`, `.obsidian/` | Anyone, with care | Scaffolding for the other four |

The first three are the Karpathy three-layer pattern: sources flow **`raw/` → `KB/` → shipping**, never backwards. Nothing is promoted into `docs/` or `games/` that has not been through `KB/` or through a slice with a brief.

---

## 2. Full layout

```text
Wargame_Concierge/
├── START_HERE.md                      Entry point and read order
├── README.md                          Project overview and directory map
├── AGENTS.md                          KB schema source of truth (Librarian contract)
├── .gitignore                         Blocks GW binaries, secrets, scratchpad
├── .obsidian/                         Obsidian vault config (structural placeholder)
│
├── raw/                               IMMUTABLE - allowed sources only
│   ├── README.md                      Layer contract and contents table
│   └── pointers/                      Path pointers to C:\Personal\40K and living URLs
│
├── KB/                                THE KNOWLEDGE BASE - Librarian owns
│   ├── index.md                       Master catalog; every page is listed here
│   ├── log.md                         Append-only chronological activity log
│   ├── overview.md                    High-level synthesis of the whole KB
│   ├── glossary.md                    Living terminology; home of all Keyword entries
│   ├── changelog.md                   Promotion log (KB -> docs/ or games/)
│   ├── ingest_procedure.md            How raw/ becomes KB/ in this project
│   ├── sources/                       One page per ingested source
│   ├── concepts/                      Rules ideas, phases, tactical principles
│   ├── factions/                      One page per army
│   ├── detachments/                   One page per detachment and its rules package
│   ├── units/                         One page per datasheet, in play terms
│   ├── setup/                         Deployment, terrain, missions, scoring
│   └── analyses/                      Matchups, list comparisons, filed answers
│
├── docs/                              SHIPPING - process and project reference
│   ├── README.md                      Documentation index
│   ├── Project_Structure.md           This file
│   ├── Project_Planning.md            Decisions, status, open questions
│   ├── Project_Origin_Story.md        Why the project exists
│   ├── Rehydration_Prompt.md          AI session bootstrap
│   ├── Game_System_Scaffold.md        Reusable checklist for a new game system
│   ├── operations/
│   │   ├── multiagent_coordinator_strategy.md    Normative multi-agent playbook
│   │   └── librarian_agent.md                    Librarian day-to-day operations
│   └── handoffs/
│       ├── README.md                  Active tracks index + artifact lifecycle
│       └── v1_scaffold/
│           ├── track_in.md            Constraints, model matrix, slice rollup
│           └── slices/                Per-slice briefs and reports
│
├── games/                             SHIPPING - per-system teaching content
│   ├── README.md                      What goes in a game subtree
│   └── warhammer_40k_11e/             First worked example (arrives S2 onward)
│
├── reference/                         READ-ONLY - patterns and seed context
│   ├── Initial_Prompt.md              The verbatim prompts that started the project
│   ├── Distilled_Project_Context.md   LLM-optimized context digest
│   └── llm-wiki.md                    Karpathy "LLM Wiki" pattern doc
│
├── templates/                         Rising Tide header/footer fragments (copy, do not edit)
├── checkins/                          Decision and build session notes
└── prompts/                           Prompt history and reusable agent prompts
```

Directories that exist but are still empty of content are placeholders created by an earlier slice. That is expected during `v1_scaffold`; see [`handoffs/v1_scaffold/track_in.md`](handoffs/v1_scaffold/track_in.md) for which slice fills each one.

---

## 3. `raw/` - immutable sources

**The whole point of this layer is that it does not change.** A KB page can cite `raw/some_source.md` and that citation stays true.

| Allowed in `raw/` | Never in `raw/` |
|-------------------|-----------------|
| Markdown notes authored by the project | Games Workshop PDFs |
| Imported personal lists (e.g. the updated Necron list) | Official datasheet images, `.webp`, `.png` |
| Source library path pointers | Anything copyrighted and redistributed |
| Research excerpts written in our own words | Secrets, credentials, `.env` content |

The external library at `C:\Personal\40K` stays **outside** this repo permanently. Reference it with markdown path pointers under `raw/pointers/`.

**Who may write:** Coordinator or an Implementer slice explicitly authorized to copy a source in. The Librarian **never** writes here.

---

## 4. `KB/` - the knowledge base

The compounding layer. Full contract in [`../AGENTS.md`](../AGENTS.md); the essentials:

| Rule | Detail |
|------|--------|
| **Owner** | Librarian agent only |
| **Header style** | YAML frontmatter only - **never** a Rising Tide HTML header (it breaks frontmatter parsing in Obsidian and Dataview) |
| **Filenames** | lowercase `snake_case` |
| **Links** | `[[wikilink]]` for internal links, never bare relative paths inside `KB/` |
| **Confidence** | Mandatory on every page: `verified` / `draft` / `stub` / `unverified` |
| **Cataloguing** | Every new page gets a row in `KB/index.md` in the same pass |
| **Logging** | Every ingest, query, and lint appends to `KB/log.md` |

Eight entity types map to the typed subdirectories, except **Keyword**, which is glossary-only and lives as an entry in `KB/glossary.md` rather than as its own file.

---

## 5. `docs/` and `games/` - shipping

Reviewed, player-facing and process-facing truth.

| Rule | Detail |
|------|--------|
| **Header style** | Rising Tide HTML comment header + Change Log / Attribution / Rising Tide Notes footer |
| **Exception** | `docs/handoffs/**` slice artifacts use the plain slice format - no RT header or footer |
| **Filenames** | Rising Tide `Snake_Case` (e.g. `Keyword_Glossary.md`) |
| **Promotion** | A `KB/` page becomes a shipping page only after review, with a row added to `KB/changelog.md` |

`docs/` holds project and process reference. `games/` holds per-system teaching content, one subtree per system - `games/warhammer_40k_11e/` is the first. The checklist for what a game subtree contains is [`Game_System_Scaffold.md`](Game_System_Scaffold.md), section B.

---

## 6. `reference/` - read-only context

Material that informs the project without being project truth.

| File | Role |
|------|------|
| `Initial_Prompt.md` | The verbatim seed prompts, preserved so intent is auditable |
| `Distilled_Project_Context.md` | Compressed context digest optimized for LLM ingestion |
| `llm-wiki.md` | Karpathy's "LLM Wiki" pattern doc, copied verbatim |
| `Source_Library.md` | Local and web source catalog - **created in slice S2** |

Do not cite `reference/` as a rules authority. It explains *how we work*, not *how the game works*.

---

## 7. Where does my file go?

| If it is... | Put it in | Header style | Filename |
|-------------|-----------|--------------|----------|
| An allowed source, copied in unchanged | `raw/` | none required | source's own name |
| A pointer to an external file or URL | `raw/pointers/` | none required | descriptive |
| Working synthesis about the game | `KB/<type>/` | YAML frontmatter | `snake_case` |
| A game term or keyword | an entry in `KB/glossary.md` | (part of that page) | n/a |
| Reviewed teaching content for a system | `games/{system_slug}/` | Rising Tide | `Snake_Case` |
| Project or process reference | `docs/` | Rising Tide | `Snake_Case` |
| A slice brief or report | `docs/handoffs/{track}/slices/` | plain slice format | `{Id}_{role}.md` |
| An external pattern or seed document | `reference/` | Rising Tide | `Snake_Case` |
| Notes from a working session | `checkins/` | Rising Tide check-in template | dated |
| A reusable agent prompt | `prompts/` | none required | descriptive |

Still unsure? Ask which **layer** it belongs to first - raw, knowledge, shipping, or reference. The directory follows from the layer.

---

## 8. Constraints that shape the layout

| Constraint | Consequence for structure |
|-----------|---------------------------|
| No GW binaries in git | `.gitignore` blocks `*.pdf`, `*.webp`, `*.png`, `*.jpg` and friends; the owned library lives outside the repo and is reached by pointer |
| `raw/` is immutable | Corrections go in a new `KB/` page that flags the contradiction, never by editing the source |
| Librarian never commits | The working tree stays dirty after a Librarian slice; the Coordinator commits |
| Repo is an Obsidian vault | `.obsidian/` at the root; wikilinks must resolve across `KB/`, `docs/`, and `games/` |
| Game-agnostic by design | One subtree per system under `games/`; nothing 40K-specific in `docs/` outside a clearly labelled example |
| Standalone git root | This repo is **not** a leaf of a `Personal_Projects` monorepo - it has its own `.git` |

---

## Change Log

- v1.0 (2026-08-16): Initial layout reference - five trees, full directory map, per-layer rules, placement decision table. Created in slice S1.

## Attribution

- Project: Wargame_Concierge
- Maintainer: Russell Catt
- Schema authority: [`AGENTS.md`](../AGENTS.md)
- Structured using the Rising Tide framework

## Rising Tide Notes

- This document follows Rising Tide documentation standards.
- Must remain understandable, reproducible, and reusable.
- If a directory exists that this file does not describe, one of the two is wrong.
