<!--
FILE: docs/Game_System_Scaffold.md
VERSION: v0.5.1 (2026-08-18)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, slice S1)

DOCUMENT_TYPE: Reference / Reusable Checklist
PROJECT_NAME: Wargame_Concierge
REFERENCE_STATUS: Active

SOURCES:
  - Cursor plan wargame_concierge_setup_ee78aead (content requirements, sections A-F)
  - AGENTS.md (layer contract, entity types, copyright rules)
  - docs/Project_Structure.md (repository layout)
  - docs/operations/librarian_agent.md (ingest / query / lint / promote loop)
  - docs/operations/multiagent_coordinator_strategy.md (slice and tier model)

PURPOSE:
  The reusable, game-agnostic checklist for bringing a new tabletop wargame
  into this repository. Says what to create, in what order, and what "done"
  looks like for each artifact, without assuming any particular game's rules
  or vocabulary.

PRIMARY_AUDIENCE:
  - Whoever onboards system #3 (KT24 is already onboarded)
  - Coordinator planning a new content track
  - AI systems asked to "add game X"

KEY_SECTIONS_EXPECTED:
  - Scope and how to use
  - A. Project spine
  - A2. Knowledge plane checklist
  - B. Per game system
  - C. Per faction / army
  - D. Cross-cutting reference types
  - E. Later tracks
  - F. Minimum viable new game

UPDATE_TRIGGER:
  Update when a new system exposes a gap in this checklist, or when an item
  here proves to be 40K-specific rather than general. Distil back into this
  file rather than solving it privately inside a game folder.
-->

# Game System Scaffold

The reusable checklist for adding a wargame to this repository.

**This document is deliberately game-agnostic.** It never assumes phases, dice, points, or army structure. Every item is phrased as a *job to be done*, and each one names the system-specific vocabulary it might map to only as an example.

**Warhammer 40,000, 11th Edition is the first worked example of this scaffold**; **Kill Team 2024 is onboarded** as system #2 under [`games/kill_team_2024/`](../games/kill_team_2024/README.md) (rules spine, Patch_Manifest, Target_Eligibility, setup/killzones, teams, ops). This checklist is the pattern for **system #3**. Copy the checklist, not a 40K folder name, and use the KT subtree as the second worked example (including `teams/` vs `armies/` vocabulary).

---

## How to use this document

| Situation | Do this |
|-----------|---------|
| Brand-new repository | Run **section A** once, then **A2**, then **B** onward for the first system |
| Adding a later system | Skip A - it already exists. Run **A2**, then **B**, **C**, **D**. Use `games/kill_team_2024/` as the second worked example |
| Just want to play *something* soon | Run **section F**, the minimum viable order, and come back for the rest |
| Planning a track | Sections B and C map cleanly onto slices; **E** is the backlog |

### Rule zero: translate the vocabulary once, in writing

Every system names the same underlying ideas differently. Before creating anything, write a **vocabulary mapping table** in that system's `games/{system_slug}/README.md` that maps this scaffold's generic terms onto the system's own words.

| Generic term used here | Means | Example mappings |
|-----------------------|-------|------------------|
| **Force** | The collection of models one player brings | army, warband, kill team, platoon, crew |
| **Force organisation** | The rules governing what may be in a force | detachment, battalion, faction list, roster |
| **Force-wide rule** | An ability every model in the force benefits from | army rule, faction ability, doctrine |
| **Sub-list rule package** | The chosen specialisation and the rules that come with it | detachment rule, subfaction, order of battle, theatre selector |
| **Unit entry** | The stats and rules for one unit | datasheet, warscroll, unit card, army list entry |
| **Round structure** | How a turn or battle round is sequenced | phases, alternating activations, initiative order, command sequence |
| **Scoring** | How the game is actually won | objectives, victory points, battle tactics, mission goals |
| **Force size** | The agreed measure that balances two forces | points, power level, reinforcement points, platoon selectors |

Get this table right and the rest of the scaffold reads naturally. Get it wrong and every downstream document argues with itself.

---

## A. Project spine

**Run once per repository.** These artifacts are system-independent - they hold the Rising Tide documentation frame and the Karpathy knowledge plane that every game sits inside.

If you are reading this in Wargame_Concierge, section A is **already complete**. It is documented here so the scaffold stands on its own when copied to a new repo.

| Create | Purpose | Done when |
|--------|---------|-----------|
| `START_HERE.md` | Entry point: what the project is, read order, hard rules | A cold reader knows where to go next in under two minutes |
| `README.md` | Project overview, structure map, links, status | Every top-level directory is explained and linked |
| `docs/README.md` | Documentation index | Every file in `docs/` has a row saying what it answers |
| `docs/Project_Structure.md` | Layout, per-directory ownership, placement rules | A contributor can decide where a new file goes without asking |
| `docs/Project_Planning.md` | Decisions, confirmed facts, open questions, next actions | Nothing already decided gets re-litigated |
| `docs/Project_Origin_Story.md` | Why the project exists, who it is for | Readable by someone who has never played a wargame |
| `docs/Rehydration_Prompt.md` | AI session bootstrap | A memoryless session can rebuild context and state the current slice |
| `docs/Game_System_Scaffold.md` | This checklist | Game-agnostic; no system's vocabulary leaks into the generic items |
| `reference/Initial_Prompt.md` | The verbatim seed request | Original intent stays auditable against later drift |
| `reference/Distilled_Project_Context.md` | Compressed context digest for LLM ingestion | Loadable in one read; no contradiction with the source documents |
| `reference/Source_Library.md` | Catalog of local and web sources | Every source is reachable by pointer or URL, with its trust level stated |
| `reference/{pattern_doc}.md` | The knowledge pattern being followed (here, `llm-wiki.md`) | Present and unmodified from upstream |
| `AGENTS.md` | **Knowledge-base schema source of truth** | Entity types, frontmatter, naming, workflows, and copyright rules all defined |
| `docs/operations/librarian_agent.md` | Librarian day-to-day operations | Distinct from the schema; points at `AGENTS.md` for schema questions |
| `docs/operations/{coordinator_playbook}.md` | Multi-slice / multi-agent normative playbook | Roles, tiers, slice state machine, and git ownership are unambiguous |
| `docs/handoffs/` | Track artifacts: index, `track_in.md`, per-slice briefs and reports | A reviewer can reconstruct who did what, with which model, and why |
| `raw/` | Immutable allowed sources, plus `raw/pointers/` | Contract stated in `raw/README.md`; no publisher binaries |
| `KB/` | The compounding knowledge base | Core pages exist: index, log, overview, glossary, changelog, ingest procedure |
| `.obsidian/` | Vault config so the repo browses as a graph | Wikilinks resolve across `KB/`, `docs/`, and `games/` |
| `templates/` | Rising Tide header and footer fragments | Every document type has a named header and footer |
| `checkins/` | Decision and build session notes | Exists and is used, not just present |
| `prompts/` | Prompt history and reusable agent prompts | Dispatch prompts are recoverable after the fact |
| `.gitignore` | Blocks publisher binaries, secrets, scratchpad | A `git status` after adding a PDF shows nothing |

### Spine acceptance checks

- [ ] `START_HERE.md` and `README.md` agree on the read order
- [ ] Every directory in the repo is described in `docs/Project_Structure.md`
- [ ] `AGENTS.md` names one knowledge directory and forbids creating a second
- [ ] `.gitignore` blocks the publisher binary formats **before** any source is copied in
- [ ] No commits contain copyrighted binaries - check history, not just the working tree
- [ ] All files are UTF-8 without BOM

---

## A2. Knowledge plane checklist

**Run for every new game system.** This is the loop that makes knowledge compound instead of evaporating. It runs *before and alongside* the content work in sections B and C - not after.

The knowledge plane is separate from the execution plane on purpose: the Librarian builds understanding, Implementers ship documents built on that understanding.

### The four steps

1. **Seed `raw/`.** Drop allowed sources and pointer stubs into `raw/`. For a new system this is usually: a pointer to the local rulebook and army-pack library, the living web references, and any personal notes or collection lists already written. Nothing copyrighted, nothing binary.
2. **Ingest.** The Librarian reads each source and fans it out across the knowledge base: one page per source, then the entity pages it touches - concepts, forces, sub-lists, units, setup, and the glossary. A meaningful ingest touches five to fifteen pages. Index and log get updated in the same pass.
3. **Promote.** Stable, cross-checked knowledge is promoted from the knowledge base into `games/{system_slug}/` as teaching content, with approval and a changelog row. Promotion is a review event, not a copy operation.
4. **Lint.** Before calling the system "ready to play", run a full health check: contradictions, stale rules, edition drift, orphan pages, one-way links, terminology drift, confidence drift, and missing retrieval dates. Fix what is agreed; log the rest.

### Per-system knowledge checklist

| Check | Why it matters |
|-------|----------------|
| [ ] Every page carries the system tag in its frontmatter | Two systems in one knowledge base must never blur |
| [ ] Every page carries an honest confidence value | The confidence field is the whole trust model |
| [ ] Every rules claim from a living source records a retrieval date | Publishers patch; an undated claim cannot be aged |
| [ ] The glossary gained an entry for every new term, in the same pass | Terminology drift is cheap to prevent and expensive to fix |
| [ ] Terms that collide with an existing system's vocabulary are flagged, not overwritten | The same word can mean different things in two games |
| [ ] The index has a row for every page created | An uncatalogued page is invisible to every future session |
| [ ] The activity log has an entry for every ingest, query, and lint | Reconstructing "when did we learn this" depends on it |
| [ ] At least one full ingest has run end to end before content slices start | The ingest contract is only proven by using it |
| [ ] A lint pass is clean, or its findings are recorded, before "ready to play" | Ready-to-play is a claim about accuracy |

### Guard against these

| Anti-pattern | Consequence |
|--------------|-------------|
| Writing teaching content before any ingest | Content with nothing to cite, and nothing to correct it later |
| Unit pages before core rules and setup pages | Unit pages have nothing to link to and become orphans |
| Building tooling, queues, or machine-readable indexes early | Over-automation before the pattern has proven itself at small scale |
| Letting a second system share the first system's pages | Silent cross-contamination of rules that only look similar |

---

## B. Per game system

**Create under `games/{system_slug}/`.** One subtree per system. The slug is lowercase and version-bearing where editions matter - for example `warhammer_40k_11e`, so a future edition can live beside it rather than overwriting it.

| Create | Purpose | Done when |
|--------|---------|-----------|
| `README.md` | Edition and version in scope; the vocabulary mapping table from rule zero; how to use this subtree to learn the game; links to the source catalog | A reader knows which edition this describes and which words map to which |
| `rules/Overview.md` | What a game of this system *is*: force size options, how you win, how a force is put together, how long a game runs | A beginner can describe the shape of a game before knowing any rule |
| `rules/Turn_Structure.md` | The round structure as a beginner checklist - what happens, in what order, and what is easy to forget | Usable as a literal walkthrough for a first game |
| `rules/Key_Concepts.md` | Core resolution ideas: how an attack resolves, how defence works, morale or equivalent, how scoring works | Explains *why* each mechanic exists, not just how it resolves |
| `rules/Keyword_Glossary.md` | Searchable at-a-glance reference for the terms that appear on unit entries and come up mid-game | Grouped into scannable sections, one line per term, no wall of text |
| `setup/Board_Setup.md` | Table size, deployment, objective placement, pre-game sequence and checklist | Two people can set up a legal table from this file alone |
| `setup/Terrain_Basics.md` | Terrain categories, footprints, how terrain interacts with the rules, and what "enough terrain" looks like | Answers "is my table too empty?" concretely |
| `armies/` or `factions/` | One folder per force in scope | Naming matches the system's own word for a force |

### Notes on the Keyword Glossary

This is the single most-used document during a real game, so it earns specific constraints:

- **Grouped sections, not one alphabetical wall.** Group by where the term bites: movement and positioning, ranged attacks, close combat, defence and damage, mission and force-level terms.
- **One line per entry.** Term, then a plain-English meaning. Add a "when it matters" line only where the timing is the whole point.
- **Force-flavoured pointers, not force-specific text.** If a term belongs to one force, give it a one-line pointer to that force's guide and keep the full explanation there.
- **Paraphrase.** Never transcribe the publisher's wording.
- **Spot-check renamed terms.** Editions rename things quietly. Check the living references for anything carried over from a previous edition.

### System acceptance checks

- [ ] Rules teaching documents paraphrase; verbatim publisher text appears only under a scoped quote exception (`games/kill_team_2024/`, or `games/warhammer_40k_11e/rules/` and `setup/` for WarCom-free 40K Core with rule IDs). Army/Codex folders stay paraphrase.
- [ ] Terminology matches the knowledge base glossary - divergence is a lint finding
- [ ] The vocabulary mapping table exists in the subtree README
- [ ] Edition or version is stated on every rules document
- [ ] Nothing in `docs/` outside a labelled example has become system-specific

---

## C. Per faction / army

**Create under `games/{system_slug}/armies/{force_slug}/`** (or `factions/`, per the system's own vocabulary). Repeat this whole section for each force in scope. Two forces is the practical minimum, because a solo force cannot teach a game.

| Create | Purpose | Done when |
|--------|---------|-----------|
| `README.md` | Who plays this force and why; its identity in one paragraph; default sub-list; links to the starters and the play guide | A reader can decide whether this force suits them |
| Force-wide rule guide | The ability every unit shares: what it does, when it triggers, and the habits it should build | Explains the tactical consequence, not just the trigger |
| Sub-list rule package guide | The chosen specialisation - its rule, its enhancements, its stratagem-equivalents, and what the list *wants to do* | A player knows what this list is trying to achieve on turn one |
| `Owned_Models_Inventory.md` | Checklist of physical models: count, assembly state, paint state, provenance | Every list document can be checked against reality |
| Expansion / collection blueprint | Optional: the path from what is owned to a full force | Already-owned models are tagged as owned, **never** counted as purchases |
| `Starter_{small}.md` | A minimal learning list - fewest moving parts that still teaches the force | Buildable from owned models, or explicit about what is missing |
| `Starter_{medium}.md` | A step up in size and complexity | Adds one new idea over the small list, not five |
| `Quick_Reference_Play_Guide.md` | **Two-page print-and-laminate** table card | Prints to exactly two pages; usable without opening anything else |
| `units/Unit_Index.md` | Master roster table with roles, keywords, cost, source URL, cross-check status, priority | Row count matches the number of research files |
| `units/_schema.md` | The stable field contract every research file follows | Field names will not change when the corpus grows |
| `units/research/{Unit}.md` | One structured research file per unit entry | Owned and starter units have no empty required fields |

### The inventory document is load-bearing

For a hand-me-down or partly built collection, `Owned_Models_Inventory.md` is what keeps every other document honest. Record **assembly and paint state**, not just counts - "owned but unassembled" and "game ready" lead to completely different advice for someone who wants to play this weekend.

### Two-page play guide constraints

These are locked because the artifact has a physical constraint: it must fit on a laminated card beside the table.

| Constraint | Detail |
|-----------|--------|
| Length | **Exactly two pages** when printed from markdown preview or a browser |
| Orientation | Portrait, letter or A4 |
| Page break | An explicit, visible break marker between page 1 and page 2 |
| Type size | Large enough to read at arm's length across a table |
| Density | Bullets and tables, denser than teaching prose |
| Excluded | Full unit entries, shopping notes, extended lore |
| Footer | A verify-against-current-sources line, plus a date and version |

**Page 1 - "During the game":** round-structure checklist; force-wide rule cheat box; sub-list rule cheat box, including anything once-per-game; and the core attack resolution sequence in four to six lines.

**Page 2 - "Your force today":** a snapshot of the starter list with each unit's job stated in a few words; five to eight do-this / do-not-do-this beginner prompts; a mini-strip of the eight to twelve terms this force leans on most; and pre-game and end-of-turn reminders.

### Unit research file contents

Whatever the system, capture these fields so a later track can generate printable cards without re-researching:

- Identity: name, slug, source URL, **research date**
- Composition and unit size options
- Profile characteristics as the system defines them
- Weapons: ranged and melee, with their characteristics and any weapon keywords
- Abilities: name plus a plain-English or structured effect note
- Attachment and leader options
- Keywords, including force keywords
- Cost, dated, with a note to verify against the current points document
- List-building notes: what it is for, and one beginner tip
- Source attestation: which source, and which local document was cross-checked - or "pending"

### Force acceptance checks

- [ ] Every list document is buildable from the inventory, or states plainly what is missing
- [ ] Already-owned models are never listed as future purchases
- [ ] The play guide prints to two pages - verified by actually printing it
- [ ] `Unit_Index.md` row count equals the number of files in `units/research/`
- [ ] Units the owner actually plays have no empty required schema fields
- [ ] Every research file records a research date and a cross-check status

---

## D. Cross-cutting reference types

These types recur in every system. Recognising which type an artifact is tells you where it lives, who owns it, and how much to trust it.

| Type | What it is | Where it lives | Trust rule |
|------|-----------|----------------|------------|
| **Authoritative local library** | The publisher material the owner legally holds: core rules, faction packs, points documents | **Outside the repo.** Referenced by path pointer under `raw/pointers/` | Highest authority; never copied in |
| **Living web sources** | Publisher news, FAQs, errata, downloads; a trusted searchable community wiki | Cited by URL, always with a retrieval date | Authoritative but **perishable** - re-check before play |
| **Teaching documents** | Paraphrased beginner explanations | `games/{system_slug}/rules/`, `setup/` | As good as their citations; carry a confidence value |
| **Table aids** | Two-page laminate guides, keyword glossary | `games/{system_slug}/` and per force | Must be current or they are actively harmful mid-game |
| **List-building** | Starter lists now; validated lists later, built from the research corpus | Per force | Only as valid as the inventory and points data behind them |
| **Research corpus** | Structured per-unit notes feeding future generated artifacts | `units/research/` per force | Dated snapshots, not live data |
| **Knowledge base** | The compounding synthesis layer | `KB/` | Confidence-graded; the Librarian's surface |
| **Operations and process** | Track briefs, slice reports, playbooks | `docs/operations/`, `docs/handoffs/` | Process truth, not game truth |

### The trust ladder

When two sources disagree, resolve in this order:

1. The current official document the owner holds locally
2. The publisher's most recent online update, FAQ, or errata
3. A trusted community wiki
4. This repository's own notes

Notes are the **least** authoritative source in the stack. That is by design: this repository is a teaching layer over the sources, not a replacement for them. When it disagrees with a real document, the real document wins and the disagreement gets recorded rather than quietly overwritten.

---

## E. Later tracks

The backlog that becomes available once a system's first scaffold is complete. None of these are worth starting early; each one consumes something the earlier work produces.

| Later deliverable | Depends on | Why wait |
|-------------------|-----------|----------|
| Printable per-unit cards | A complete research corpus and a stable field schema | Generating cards from an unstable schema means generating them twice |
| Mission pack and matched-play cheat sheets | `rules/` and `setup/` complete | Mission nuance is meaningless before the base rules are understood |
| Additional forces | Section C, repeated | Each force is a self-contained repeat, not a new pattern |
| List validator or points sync | Research corpus plus a current points document | Automating against unverified data automates the errors |
| A second game system | This entire scaffold, re-run from A2 | The scaffold is the deliverable; re-running it is the point |
| Print-CSS or PDF export pipeline | Play guides that already print correctly as markdown | Solve the layout problem before automating it |
| Rules-question answering from the knowledge base | Enough ingested sources for the index to be worth consulting | An empty knowledge base answers nothing |

**Sequencing principle:** every item here becomes cheap once its dependency exists and expensive if started before. Resist starting them early.

---

## F. Minimum viable new game

The shortest honest path from "we own some models" to "we played a game." Run in order. Each step is usable on its own, so stopping early still leaves something of value.

| # | Step | Produces | Stop-here value |
|---|------|----------|-----------------|
| 1 | **Source catalog entry** - local library pointers plus the living web references for this system | A row in the source catalog and pointer stubs in `raw/` | You know where the answers are |
| 2 | **System subtree** - `games/{slug}/README.md` with the vocabulary mapping, plus `rules/Overview.md`, `rules/Turn_Structure.md`, `rules/Keyword_Glossary.md` | The shape of the game and its language | You can follow along in someone else's game |
| 3 | **Board and terrain** - `setup/Board_Setup.md` and `setup/Terrain_Basics.md` | A legal, playable table | You can set up |
| 4 | **First force** - README, force-wide rule, sub-list rule package | One force you understand | You can pilot something |
| 5 | **Inventory and starter lists** - `Owned_Models_Inventory.md` plus a small and a medium starter | Lists built from real models | You have something legal to put on the table |
| 6 | **Two-page play guide** | The laminated card | **You can play a game.** This is the milestone |
| 7 | **Unit index and research** - owned and played models first, then the rest of the roster | The durable research corpus | You can build your own lists |
| 8 | **Opposing force** - repeat section C for a second force | Two-player learning at home | You can teach someone else |

**Step 6 is the goal.** Everything before it is necessary; everything after it is improvement. A project that reaches step 6 and stops has succeeded.

### Minimum viable acceptance

- [ ] Two people can set up a legal table using only `setup/`
- [ ] Both forces have a starter list buildable from models actually owned
- [ ] Both play guides print to two pages
- [ ] Every rules claim in the above can be traced to a source with a date
- [ ] The knowledge base has ingested the sources those documents rest on
- [ ] A lint pass has run and its findings are recorded

---

## The worked example: Warhammer 40,000, 11th Edition

The first and currently only instantiation of this scaffold. Reading it alongside the generic checklist is the fastest way to understand what each item actually looks like.

| Scaffold item | 40K 11e instantiation |
|---------------|----------------------|
| System slug | `warhammer_40k_11e` |
| Force | Army |
| Force organisation | Detachment |
| Force-wide rule | Army rule - Reanimation Protocols for Necrons, Oath of Moment for Space Marines |
| Sub-list rule package | Detachment rule - for example Power Matrix, the Canoptek Court detachment rule |
| Unit entry | Datasheet |
| Round structure | Phases within a battle round |
| Scoring | Objective control and mission scoring |
| Force size | Points, at defined game sizes |
| Local library | `C:\Personal\40K` - **pointers only**, never copied in |
| Living web sources | [Warhammer Community](https://www.warhammer-community.com/en-gb/), [Wahapedia](https://wahapedia.ru/) |
| Forces in scope | Necrons (learning army), Space Marines (opposing force) |
| Track delivering it | `v1_scaffold` - see [`handoffs/v1_scaffold/track_in.md`](handoffs/v1_scaffold/track_in.md) |

Two things this example demonstrates that are easy to miss in the abstract:

**The edition is new, so the confidence model does real work.** Much of what gets written starts `unverified` and is promoted only after a cross-check. Carrying assumptions from the previous edition is an explicit, named lint category. A system with a stable, long-settled edition would lean on this far less.

**The collection is partly unassembled, so the inventory drives the content.** The starter lists are written against ten unassembled Warriors, three Scarab Swarms, five Immortals, and one game-ready Hierotek Circle set whose contents are still pending identification. That is not an inconvenience to work around - it is the actual situation the teaching content has to serve, and section C's inventory requirement exists precisely because of it.

---

## Anti-patterns

Distilled from building the first system. Each one costs more than it looks like it will.

| Anti-pattern | What goes wrong |
|--------------|-----------------|
| Copying the 40K folder instead of the checklist | You inherit 40K's vocabulary and assumptions into a game that does not share them |
| Skipping the vocabulary mapping table | Every subsequent document quietly argues with the system's own rulebook |
| Writing unit research before rules and setup | Research files have nothing to link to; they become an orphaned pile |
| Treating a community wiki as authoritative | Convenient, sometimes wrong, occasionally out of date - always cross-check |
| Omitting retrieval dates | A claim with no date cannot be aged, so it can never be safely retired |
| Building lists against models not yet owned | The lists are unplayable, and the inconsistency is discovered at the table |
| Letting the play guide grow to three pages | It stops being a laminated card and becomes another document nobody opens |
| Marking pages `verified` to feel finished | Destroys the one signal that makes the whole knowledge base trustworthy |
| Solving a general problem inside one game folder | The next system re-solves it from scratch. Distil it back into this file instead |

---

## Change Log

- v0.5.0 (2026-08-18): Project-wide semver snapshot (x.y.z). KT24 onboarded; scaffold is the pattern for system #3.
- v1.0 (2026-08-16): Initial reusable scaffold - sections A through F, vocabulary mapping, per-section acceptance checks, trust ladder, 40K 11e worked example, anti-patterns. Created in slice S1.

## Attribution

- Project: Wargame_Concierge
- Maintainer: Russell Catt
- Distilled from the `v1_scaffold` track and the Karpathy "LLM Wiki" pattern
- Structured using the Rising Tide framework

## Rising Tide Notes

- This document follows Rising Tide documentation standards.
- Must remain understandable, reproducible, and reusable.
- When a new system exposes a gap here, fix it **here** - not privately inside a game folder.
