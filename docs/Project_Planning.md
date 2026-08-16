<!--
FILE: docs/Project_Planning.md
VERSION: v1.0 (2026-08-16)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, slice S1)

DOCUMENT_TYPE: Project Planning
PROJECT_NAME: Wargame_Concierge
PROJECT_PHASE: Bootstrap
STATUS: Active

SOURCES:
  - README.md
  - docs/handoffs/v1_scaffold/track_in.md (constraints, model matrix, Preflight notes)
  - docs/handoffs/v1_scaffold/slices/L0_librarian.md (schema decisions, open threads)
  - Cursor plan wargame_concierge_setup_ee78aead (locked decisions)
  - reference/Initial_Prompt.md (owner intent)

PURPOSE:
  Records what has been decided and why, the confirmed model ownership the
  content is built against, what is still open, and what happens next. The
  place to look before re-litigating a decision.

PRIMARY_AUDIENCE:
  - Project owner
  - Coordinator
  - Any agent about to make an assumption

CONTAINS:
  - Current status
  - Locked decisions
  - Confirmed ownership
  - Open questions
  - Immediate next actions

UPDATE_TRIGGER:
  Update after major decisions, slice completions, ownership changes, or when
  an open question is resolved.
-->

# Project Planning

Decisions of record for Wargame_Concierge. If a question here is marked resolved, treat it as settled unless new evidence arrives - and if it does, record the change rather than quietly rewriting the answer.

---

## 1. Current status

| Field | Value |
|-------|-------|
| Phase | Bootstrap |
| Active track | `v1_scaffold` |
| Track status | In progress |
| Slice order | Preflight → S0 → **L0** → **S1** → S2 → **L1** → S3 → S4 → S5 → S6 → **L2** → S7 |
| This document written in | **S1** |
| Live rollup | [`handoffs/v1_scaffold/track_in.md`](handoffs/v1_scaffold/track_in.md) |
| KB maturity | Level 1 (pilot), entered 2026-08-16 at L0 |
| Git state | One commit - the S0+L0 bootstrap, made by the Coordinator. **No remote yet**; push is a user gate at S7 |

---

## 2. Locked decisions

### Repository and hosting

| Decision | Detail | Decided |
|----------|--------|---------|
| **Repository** | **Private** GitHub repo `russell-catt/Wargame_Concierge` | 2026-08-16 |
| Location | `C:\Personal\Personal_Projects\Wargame_Concierge` | 2026-08-16 |
| Git root | **Standalone** - its own `.git`, not a `Personal_Projects` monorepo leaf | 2026-08-16 |
| Repo creation and push | Slice **S7**, behind an explicit user gate | 2026-08-16 |
| Git ownership | Coordinator alone commits. Subagents never commit or push | 2026-08-16 |

Private is a deliberate choice, not a default. The unit research corpus is personal structured notes derived from material the owner holds; keeping the repo private is part of the copyright posture below.

### Scope

| Decision | Detail |
|----------|--------|
| **First system** | **Warhammer 40,000, 11th Edition** - the first and currently only system in scope |
| Primary army | **Necrons** - the learning army, built from models owned |
| Secondary army | **Space Marines** - the opposing force, drawn from an existing pile of older models |
| Game-agnostic by design | `games/` holds one subtree per system; 40K 11e is the **first worked example**, not a special case |
| Second-system path | Follow [`Game_System_Scaffold.md`](Game_System_Scaffold.md) rather than inventing folders ad hoc |
| Out of scope for v1 | Factions beyond Necrons and Space Marines; a web app or army builder; automated list validation; a finished printable datasheet pack; print-CSS/PDF pipeline for the laminate guides |

### Copyright and sourcing

| Decision | Detail |
|----------|--------|
| **No GW binaries in git** | No PDFs, official datasheet images, `.webp`, or `.png`. Enforced by `.gitignore`; bypassing it is a defect |
| External library | `C:\Personal\40K` stays **outside** the repo. Markdown path pointers only |
| One exception, already taken | The Preflight slice edited `C:\Personal\40K\rules\Necron_Lists.md` at source. That single file is imported into the project in S2. Everything else in that directory is read-only |
| Writing style | **Teaching paraphrase only.** No verbatim datasheet statlines, stratagem text, or rules text |
| Citation | Every rules claim names where it can be checked, **with a retrieval date** |
| Unit research | Personal structured notes with source pointers - not a redistribution of official datasheets |

### Living web references

11th Edition is current and moving. Both are treated as sources of record that decay, so anything drawn from them carries the date it was read.

| Reference | URL | Use |
|-----------|-----|-----|
| Warhammer Community | <https://www.warhammer-community.com/en-gb/> | Official rules updates, FAQs, errata, balance dataslates, downloads |
| Wahapedia | <https://wahapedia.ru/> | Consolidated rules and datasheet lookup; the research surface for the full unit pass in S6 |

**Patches happen.** Cross-check against the local faction packs and Munitorum-equivalent points documents before trusting a number in a real game. Wahapedia is convenience, and it can lag or differ.

### Architecture and process

| Decision | Detail |
|----------|--------|
| Knowledge pattern | Karpathy "LLM Wiki", adapted to wargames. `raw/` → `KB/` → shipping `docs/` + `games/` |
| Middle layer is `KB/` | **Never** `wiki/`. The pattern doc says `wiki/`; this repo says `KB/` |
| Schema source of truth | [`../AGENTS.md`](../AGENTS.md), with day-to-day operations in [`operations/librarian_agent.md`](operations/librarian_agent.md) |
| Librarian ownership | The Librarian agent owns all `KB/` writes, never writes `raw/`, and never commits |
| Documentation framework | Rising Tide headers and footers in `docs/`, `games/`, and root docs; YAML frontmatter in `KB/`. **The two do not stack** |
| Workflow | Multi-slice, multi-agent, imported from the `daily_report` playbook, with locked per-role models and Tier 0-3 checks |
| Obsidian | Repo root is a vault; `.obsidian/` inherited as a structural placeholder only |
| Encoding | UTF-8, no BOM |

---

## 3. Confirmed Necron ownership - 2026-08-16

This is the model pool every Necron list, starter, and teaching document must be written against. Confirmed by the owner on **2026-08-16** and patched into the source list during the Preflight slice.

| Models | Count | State | Notes |
|--------|-------|-------|-------|
| Necron Warriors | 10 (1 squad) | **Purchased, unassembled** | Build before play |
| Canoptek Scarab Swarms | 3 | **Purchased, unassembled** | Build before play |
| Immortals | 5 (1 squad) | **Purchased, unassembled** | Already owned - do **not** list as a future purchase without adjusting shopping totals |
| Hierotek Circle Kill Team (used set) | 1 set | **Assembled and painted - game ready** | Unit identification **pending owner photos** |

Three consequences that content must respect:

- **Build-before-play is the default.** Everything except the Hierotek Circle set needs assembling first. Teaching content should not assume a painted army on the table.
- **The Hierotek Circle set is the only game-ready option today**, which makes it the preferred starting point for early games - once its contents are identified.
- **Owned models are not shopping targets.** Any expansion or collection blueprint must tag the Immortals, Warriors, and Scarabs as already purchased so phase totals do not double-count them.

### Superseded: Kill Team: Tomb World

An earlier blueprint assumed a **Kill Team: Tomb World** foundation. That assumption is **superseded and historical as of 2026-08-16.** It does not describe current ownership and must not be treated as such. It is retained only as a note explaining why older list drafts look the way they do, and is on the avoid-list in [`../KB/glossary.md`](../KB/glossary.md).

### Space Marine ownership

**Not yet inventoried.** The son's force comes from a pile of older models already in the house, which is why legacy and Firstborn datasheets stay in scope for the S6 research pass. An inventory worksheet is part of slice S5; provisional lists before then are theoretical and should say so.

---

## 4. Open items

### Hierotek Circle photo identification - OPEN

| Field | Value |
|-------|-------|
| Status | **Open**, blocked on owner photos |
| Raised | Preflight, 2026-08-16 |
| Blocks | Accurate starter lists; deciding which datasheets the game-ready models actually represent |
| Owner action | Post photos of the assembled set |
| Then | Librarian ingests the identification; S4 refreshes the Necron starters against it |
| Interim handling | Placeholder subsection in the Necron list; no starter list may claim a specific Hierotek datasheet until this closes |

This is the single highest-value open item. The only game-ready models in the collection are the ones we cannot yet name.

### Power Matrix - RESOLVED 2026-08-16

| Field | Value |
|-------|-------|
| Question | Does **Power Matrix** belong to Warhammer 40,000 11th Edition, or to Kill Team? |
| Why it was open | The term arrived via the owner's Necron notes alongside the Hierotek Circle, which is a Kill Team box. The Librarian flagged the attribution as genuinely unresolved in L0 and seeded the glossary entry with a warning |
| **Resolution** | **Power Matrix is the Canoptek Court detachment rule in Warhammer 40,000.** It is a 40K detachment rule, not a Kill Team mechanic |
| Consequence | 40K content may depend on the term. It belongs with the Canoptek Court detachment, so it is detachment-scoped rather than army-wide - do not describe it as a Necron army rule |
| Confidence | Recorded here as a **project decision**. It still needs a source cross-check with a retrieval date before any page marks it `verified` |

**Follow-up owned by the Librarian, not by S1.** [`../KB/glossary.md`](../KB/glossary.md) still carries the unresolved-attribution warning, and this document cannot edit `KB/`. The correction should land in **L1**: update the Power Matrix entry, re-scope it to the Canoptek Court detachment, and clear the row in the glossary's verification queue.

### Other open questions

| Question | Blocked on | Target slice |
|----------|-----------|--------------|
| Which Necron detachment best suits a beginner with this exact model pool? | Hierotek Circle ID; detachment rules ingest | S4 |
| What Space Marine models actually exist? | Owner inventory | S5 |
| What game size are early games played at - Combat Patrol, Incursion, or Strike Force? | Owner preference; points totals for the owned pool | S3 / S4 |
| Which 11th Edition rules genuinely changed from 10th? | Core rules ingest | L1 / S3 |
| Do the two-page laminate guides actually print to two pages? | Draft existing | S4 / S5 |

---

## 5. Completed to date

| Slice | Delivered |
|-------|-----------|
| **Preflight** | Necron ownership patched into `C:\Personal\40K\rules\Necron_Lists.md` at source; Tomb World marked superseded; Hierotek Circle TODO opened |
| **S0** | Repo bootstrap: `git init` (no commits), Rising Tide `templates/`, adapted playbook, `docs/handoffs/` with the `v1_scaffold` track, `.gitignore`, `raw/` and `KB/` skeletons |
| **L0** | Karpathy KB bootstrap: `AGENTS.md` schema, `librarian_agent.md`, all six KB core pages, typed-directory guides, glossary seeded with four terms, `.obsidian/` vault |
| **S1** | Core Rising Tide documents: `START_HERE.md`, `README.md`, this file and its siblings under `docs/`, `Game_System_Scaffold.md`, and the `reference/` seed context |

---

## 6. Immediate next actions

| # | Action | Owner | Slice |
|---|--------|-------|-------|
| 1 | QA slice S1 against its brief | QA | S1 |
| 2 | Build `reference/Source_Library.md`; import the updated `Necron_Lists.md` into `raw/` and the 40K game subtree; add inventories and game READMEs | Implementer | S2 |
| 3 | First real ingest - validates the ingest contract end to end and clears the Power Matrix glossary correction | Librarian | L1 |
| 4 | Beginner rules, board and terrain setup, and the Keyword Glossary | Implementer | S3 |
| 5 | Necron starters and the two-page laminate play guide | Implementer | S4 |
| 6 | Post Hierotek Circle photos, then refresh the Necron starters | **Owner**, then Implementer | S4 follow-up |

### Known defects carried forward

| Defect | Detail | Suggested owner |
|--------|--------|-----------------|
| Dead links in the playbook | `operations/multiagent_coordinator_strategy.md` has 26 relative links inherited from the `daily_report` repo that point at directories which do not exist here. The prose is authoritative; the links are not | A later cleanup slice |
| UTF-16 encoded files | `checkins/README.md`, `prompts/README.md`, `docs/handoffs/README.md`, `raw/pointers/README.md`, and the S0-authored slice artifacts are UTF-16LE. They produce unreadable diffs and can fail to parse in Obsidian | Coordinator - note that `raw/pointers/README.md` sits under the immutable layer and needs an explicit authorization to touch |

---

## Change Log

- v1.0 (2026-08-16): Initial planning record - locked decisions, confirmed 2026-08-16 Necron ownership, Tomb World superseded, Power Matrix resolved to the Canoptek Court detachment rule, Hierotek Circle photo ID open, next actions. Created in slice S1.

## Attribution

- Project: Wargame_Concierge
- Maintainer: Russell Catt
- Structured using the Rising Tide framework

## Rising Tide Notes

- This document follows Rising Tide documentation standards.
- Keep the receipts. Make AI show their work.
- A decision recorded without its reasoning is a decision that gets re-litigated.
