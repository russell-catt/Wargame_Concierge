<!--
FILE: reference/Distilled_Project_Context.md
VERSION: v1.2 (2026-08-16)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, slice S1; ownership digest realigned in track tomb_world_ownership slice S3)

DOCUMENT_TYPE: Reference / Distilled Knowledge
PROJECT_NAME: Wargame_Concierge
REFERENCE_STATUS: Active

SOURCES:
  - reference/Initial_Prompt.md (seed intent)
  - AGENTS.md (schema source of truth)
  - docs/Project_Planning.md (decisions, ownership, open items)
  - docs/Project_Structure.md (layout and ownership)
  - docs/handoffs/v1_scaffold/track_in.md (track state, model matrix)
  - docs/handoffs/v1_scaffold/slices/L0_librarian.md (schema decisions)
  - docs/handoffs/tomb_world_ownership/track_in.md (locked ownership decision, current track state)
  - games/warhammer_40k_11e/armies/necrons/Necron_Lists.md (FOUNDATION - authoritative ownership)

PURPOSE:
  Single-read context digest for an LLM or a human who needs the whole project
  compressed into one file. Facts only, densely stated, with pointers to the
  authoritative document behind each block.

PRIMARY_AUDIENCE:
  - AI systems loading project context in one pass
  - Reviewers needing the whole picture quickly
  - Anyone writing a dispatch prompt for a subagent

KEY_SECTIONS_EXPECTED:
  - Scope
  - Source Summary
  - Distilled Findings
  - Caveats
  - References

UPDATE_TRIGGER:
  Update when a locked decision changes, a slice completes, ownership changes,
  or an open thread resolves. This file is a derivative - never let it become
  the place a fact lives first.
-->

# Distilled Project Context

Everything needed to work on Wargame_Concierge, compressed into one read.

**This is a derivative document.** Every block names the authority behind it. Where this file and its authority disagree, **the authority wins and this file is stale**.

---

## 1. Identity

| Field | Value |
|-------|-------|
| Project | **Wargame_Concierge** |
| Location | `C:\Personal\Personal_Projects\Wargame_Concierge` |
| Git | Standalone repository on `main`, one commit (`5a7679c`) ahead of the remote as of 2026-08-16. Coordinator is the only committer |
| Remote | **Private** GitHub repo `russell-catt/Wargame_Concierge` - created and first pushed at `v1_scaffold` S7 behind a user gate |
| Owner | Russell Catt |
| Framework | Rising Tide documentation standards |
| Knowledge pattern | Karpathy "LLM Wiki", adapted to wargames |
| Domain | Tabletop **wargames**. Not software, not technical writing |
| Status | Active. Track `tomb_world_ownership` in progress; `v1_scaffold` closed |

**Purpose in one sentence:** a personal concierge that teaches the rules of tabletop wargames, how to set up a board, and how to build beginner army lists from models actually owned.

---

## 2. Scope

| Dimension | In scope | Out of scope for v1 |
|-----------|----------|--------------------|
| System | Warhammer 40,000, **11th Edition** | Any other system - though the structure is game-agnostic by design |
| Factions | **Necrons** (learning army), **Space Marines** (opposing force) | Every other faction |
| Content | Rules teaching, board and terrain setup, starter lists, two-page laminate play guides, full unit research corpus | Web app, army builder, list validator, points sync, finished printable datasheet pack, print-CSS pipeline |
| Audience | Complete beginners - a parent and a son learning together | Competitive or tournament play |

40K 11e is the **first worked example** of [`../docs/Game_System_Scaffold.md`](../docs/Game_System_Scaffold.md), not a special case.

---

## 3. Architecture - four layers

Authority: [`../AGENTS.md`](../AGENTS.md) Sec 2.

| Layer | Path | Writer | Contract |
|-------|------|--------|----------|
| Raw sources | `raw/` | Coordinator / Implementer copy-in only | **Immutable.** Librarian reads, never writes |
| Knowledge base | `KB/` | **Librarian agent only** | YAML frontmatter, `confidence` on every page, `[[wikilinks]]`, `snake_case` filenames |
| Shipping | `docs/`, `games/` | Implementers | Rising Tide headers and footers, `Snake_Case` filenames, promoted after review |
| Reference | `reference/` | Write once, then read-only | External patterns and seed context. **Not project truth** |

**The middle layer is `KB/`, never `wiki/`.** The Karpathy pattern doc says `wiki/`; translate and do not create that directory.

Eight KB entity types: Source, Concept, **Keyword (glossary-only)**, Faction, Detachment, Unit, Setup/Mission, Analysis.

Six KB core pages: `index`, `log`, `overview`, `glossary`, `changelog`, `ingest_procedure`.

Confidence scale: `verified` > `draft` > `stub` > `unverified`. Mandatory on every KB page. Because 11th Edition is new, most content starts unconfirmed.

`.obsidian/` at the repo root makes the whole repository an Obsidian vault. The inherited config is a structural placeholder only.

---

## 4. Hard rules

Violating any of these is a defect, not a style disagreement.

1. **Never write under `raw/`.**
2. **Never `git commit` or `git push`.** Coordinator is the sole git owner; pushes are user-gated. The `tomb_world_ownership` track takes one deferred commit at its S4.
3. **Never commit GW binaries** - no PDFs, official images, `.webp`, `.png`. `.gitignore` enforces it.
4. **Teaching paraphrase only.** No verbatim datasheet statlines, stratagem text, or rules text.
5. **Only the Librarian writes under `KB/`.**
6. **Every rules claim records a retrieval date.**
7. **UTF-8, no BOM.**
8. **Rising Tide headers and YAML frontmatter never stack** - a leading HTML comment breaks frontmatter parsing.

---

## 5. Confirmed model ownership - 2026-08-16

Authority: the FOUNDATION section of [`../games/warhammer_40k_11e/armies/necrons/Necron_Lists.md`](../games/warhammer_40k_11e/armies/necrons/Necron_Lists.md), restated in [`../docs/Project_Planning.md`](../docs/Project_Planning.md) Sec 3. Every list and starter must be written against this.

**Game-ready - on the table now.** Kill Team: Tomb World, assembled and painted:

| Models | Count | State |
|--------|-------|-------|
| Cryptek Geomancer | 1 | **Game ready** (Tomb World) |
| Canoptek Tomb Crawlers | 2 | **Game ready** (Tomb World) |
| Canoptek Macrocytes | 5 | **Game ready** (Tomb World) |
| Necron Warriors | 10 (1st squad) | **Game ready** (Tomb World) |
| Canoptek Scarab Swarms | 3 (1st set) | **Game ready** (Tomb World) |
| Hierotek Circle Kill Team (used set) | 1 set | **Game ready.** An additional set; 40K datasheets **TBD pending owner photos** |

**Build before play - owned, still on sprue:**

| Models | Count | State |
|--------|-------|-------|
| Necron Warriors | 10 (2nd squad) | Purchased, **unassembled, unpainted** - assemble-to-expand |
| Canoptek Scarab Swarms | 3 (2nd set) | Purchased, **unassembled, unpainted** - assemble-to-expand |
| Immortals | 5 (1 squad) | Purchased, **unassembled** - build before play |

**Totals:** **20 Necron Warriors** (10 game-ready + 10 on sprue), **6 Canoptek Scarab Swarms** (3 game-ready + 3 on sprue), plus 1 Geomancer, 2 Tomb Crawlers, 5 Macrocytes, 5 Immortals, and the Hierotek Circle set (TBD).

- **Kill Team: Tomb World is owned and game-ready, and is the preferred learning baseline.** Early games and starter lists are built on it.
- **Build-before-play applies only to the extras** - the second Warriors squad, the second Scarab set, and the Immortals. Owned, not blockers, not on the table until built.
- **Owned models are not shopping targets.** Never list the Tomb World contents, the extra Warriors or Scarabs, or the Immortals as future purchases. Do not re-shop owned kits.
- **The prior "Tomb World not owned / superseded" claim was erroneous** and was corrected across the repo in track `tomb_world_ownership` on 2026-08-16. Do not reintroduce it, and do not treat "only the Hierotek Circle set is game-ready" as current.
- **The Hierotek Circle photo ID is open but not blocking.** It decides which datasheets that set maps to, nothing more.
- **Space Marine ownership is not yet inventoried.** The force comes from existing older kits, which is why legacy and Firstborn datasheets remain in research scope.

---

## 6. Sources and trust

| Source | Type | Trust |
|--------|------|-------|
| `C:\Personal\40K` | Local owned library: core rules, faction packs, points documents | Highest. **Outside the repo** - path pointers only |
| <https://www.warhammer-community.com/en-gb/> | Official updates, FAQs, errata, dataslates | Authoritative but perishable - record a retrieval date |
| <https://wahapedia.ru/> | Consolidated rules and datasheet lookup; the S6 research surface | Convenience; can lag or differ. Always cross-check |
| This repository's own notes | Teaching paraphrase | **Least** authoritative. When it disagrees with a real document, the document wins |

**Patches happen.** Re-check before any real game.

One authorized exception to the read-only source library: the Preflight slice edited `C:\Personal\40K\rules\Necron_Lists.md` at source to record confirmed ownership. That single file is imported into the project at S2, and the `tomb_world_ownership` track re-synced all three copies at S1.

### Authoritative order for Necron ownership facts

When copies disagree about what is owned, the higher rank wins. Fix the lower copy; never argue upward. This ladder governs **ownership only** - for points, the owned Munitorum Field Manual is authoritative and FOUNDATION's figures are stale.

| Rank | Source |
|------|--------|
| 1 | [`../games/warhammer_40k_11e/armies/necrons/Necron_Lists.md`](../games/warhammer_40k_11e/armies/necrons/Necron_Lists.md) - project FOUNDATION |
| 2 | [`../raw/Necron_Lists.md`](../raw/Necron_Lists.md) plus the external source `C:\Personal\40K\rules\Necron_Lists.md` |
| 3 | Army docs under [`../games/warhammer_40k_11e/armies/necrons/`](../games/warhammer_40k_11e/armies/necrons/) - inventory, README, starters, play guide |
| 4 | [`../KB/`](../KB/) pages |

The rank-1 and rank-2 copies were byte-identical after the S1 re-sync. Sync expectations live in [`../raw/pointers/necron_lists_import.md`](../raw/pointers/necron_lists_import.md).

---

## 7. Agents and workflow

| Role | Owns |
|------|------|
| **Coordinator** | Briefs, dispatch, rollup, **sole git commit**; push only after a user gate. Currently one deferred commit at `tomb_world_ownership` S4 |
| **Librarian** | Tier 0 knowledge plane: ingest, query, lint, index. Never writes `raw/`. Never commits |
| **Implementer** | Tier 1: shipping content under `docs/`, `games/`, `reference/` |
| **QA** | Tier 2: independent re-check against the brief's exit criteria |
| **Final Sanity** | Tier 3: cross-slice consistency, including KB index and log hygiene |

Artifact lifecycle per slice: `{Id}_brief.md` → `{Id}_implementer.md` or `L{n}_librarian.md` → `{Id}_qa.md` → *Resolved - Complete* → Coordinator commits.

**Model discipline:** each track locks its own per-role matrix in its `track_in.md` - currently [`../docs/handoffs/tomb_world_ownership/track_in.md`](../docs/handoffs/tomb_world_ownership/track_in.md). Every report records the model **actually** used. An unavailable model may be substituted within the same family, with the waiver recorded in the report. Implementer and QA never share a model family for the same slice.

---

## 8. Track state as of 2026-08-16

Authority: [`../docs/handoffs/tomb_world_ownership/track_in.md`](../docs/handoffs/tomb_world_ownership/track_in.md).

### Current track: `tomb_world_ownership` - Necron ownership correction

Order: **S0 → S1 → S2 → S3 → L1 → L2 → S4**

| Slice | Focus | State |
|-------|-------|-------|
| S0 | Bootstrap handoffs and briefs | Complete |
| S1 | FOUNDATION re-sync across project, `raw/`, and the external source | Complete |
| S2 | Army docs, inventory, starters, play guide | Complete |
| **S3** | Planning, this distilled context, import pointer | **This slice** |
| L1 | KB ownership ingest | Pending |
| L2 | Audit the `v1_scaffold` L2 lint and clear false ownership denials in `KB/` | Pending |
| S4 | Final Sanity, then the Coordinator's single deferred commit and push | Pending |

Git: `main` is one commit (`5a7679c`) ahead of `origin/main`. This track takes a **single deferred commit at S4**; that commit includes the unpushed one.

### Prior track: `v1_scaffold` - closed, complete

Order was **Preflight → S0 → L0 → S1 → S2 → L1 → S3 → S4 → S5 → S6 → L2 → S7**: repo bootstrap, KB bootstrap, core Rising Tide documents, source library and Necron import, first ingest, beginner rules and setup, Necron and Space Marine starters plus laminate guides, the full unit research pass, a Librarian lint, and the private GitHub repo. **Its ownership content was wrong about Tomb World throughout** - that is what the current track exists to fix.

**KB maturity: level 1 (pilot).** The ingest contract was proven at `v1_scaffold` L1.

---

## 9. Open threads

| Thread | State | Resolves at |
|--------|-------|-------------|
| **Hierotek Circle photo ID** | **Open but not blocking.** Decides which 40K datasheets that set maps to. The Tomb World force is game-ready and identified, so early games are unblocked. Waiting on owner photos | Owner photos, then a Librarian ingest |
| **False Tomb World ownership denials in `KB/`** | **Closed — resolved at L1 (2026-08-16).** Nine KB pages corrected; deprecated list retains the old claim for audit only. L2 lint confirms no live denials remain | — |
| **Power Matrix attribution** | **Resolved 2026-08-16: it is the Canoptek Court detachment rule in 40K**, not a Kill Team mechanic. Detachment-scoped, not army-wide | Corrected at `v1_scaffold` L1 |
| Space Marine inventory | Not yet recorded | A later slice |
| Beginner-appropriate Necron detachment | Undecided. Tomb World supports either Canoptek Court or Cryptek Conclave | A later slice |
| Target game size for early games | Undecided. Size it against the game-ready Tomb World pool | A later slice |
| Points drift between FOUNDATION and the army docs | FOUNDATION lists 10 Warriors at 100; the army docs and starters read 80 from Munitorum Field Manual v1.2 on 2026-08-16. FOUNDATION's points are stale - it is authoritative for **ownership**, not for costs | A points-verification slice |
| Stale ownership rows in the detachment docs | `Canoptek_Court.md` and `Cryptek_Conclave.md` still tag the first Warriors squad and Scarab set as unassembled, and Scarabs as "half" owned | A follow-up slice |
| Playbook dead links | 26 relative links inherited from the `daily_report` repo point at directories that do not exist here. Prose is authoritative; links are not | A later cleanup slice |
| UTF-16 files | `checkins/README.md`, `prompts/README.md`, `docs/handoffs/README.md`, `raw/pointers/README.md`, and several slice artifacts in both tracks are UTF-16LE, against hard rule 7 | Coordinator - note that the `raw/` file needs explicit authorization |

---

## 10. Vocabulary

Terms this project uses in a specific way.

| Term | Meaning here |
|------|--------------|
| **KB** | The knowledge base at `KB/`. The Karpathy "wiki" layer, renamed |
| **Slice** | One unit of work in a track, with a brief, a report, and QA |
| **Track** | A numbered sequence of slices toward a milestone - currently `v1_scaffold` |
| **Tier 0-3** | Knowledge entrance, implementation, QA, final sanity |
| **Ingest** | Reading a source and fanning it out across five to fifteen KB pages |
| **Promote** | Moving reviewed knowledge from `KB/` into `docs/` or `games/`, with a changelog row |
| **Lint** | A KB health check: contradictions, stale rules, edition drift, orphans, confidence drift |
| **Confidence** | The per-page trust marker. `unverified` means do not take it to the table |
| **Edition drift** | 10th Edition assumptions surviving in 11th Edition pages. An explicit lint category |
| **Living reference** | A source that changes under us and therefore needs a retrieval date |
| **Path pointer** | A markdown note recording where an external file lives, instead of copying it in |
| **Model waiver** | A recorded substitution when a locked model is unavailable |

---

## 11. Caveats

- **This file is a digest.** It compresses and therefore loses nuance. For anything load-bearing, read the authority named in the section.
- **It goes stale by design.** Slices land, ownership changes, threads resolve. Check the date in the header against [`../docs/handoffs/tomb_world_ownership/track_in.md`](../docs/handoffs/tomb_world_ownership/track_in.md).
- **Ownership was wrong once already.** Everything written before 2026-08-16's `tomb_world_ownership` track claimed Kill Team: Tomb World was not owned. If you are reading an older draft, distrust its ownership claims and come back to Sec 5.
- **It contains no rules content.** Nothing here is a claim about how Warhammer 40,000 works. Game knowledge lives in `KB/` with a confidence value and a citation, and nowhere else.
- **Never let a fact live here first.** If something is true only in this file, it is not yet recorded anywhere that matters.

---

## 12. References

| Document | Authority for |
|----------|--------------|
| [`../START_HERE.md`](../START_HERE.md) | Entry point and read order |
| [`../README.md`](../README.md) | Project overview and structure map |
| [`../AGENTS.md`](../AGENTS.md) | **Schema source of truth** - layers, entity types, frontmatter, workflows |
| [`../KB/index.md`](../KB/index.md) | What knowledge exists, and at what confidence |
| [`../docs/Project_Structure.md`](../docs/Project_Structure.md) | Layout and per-directory ownership |
| [`../docs/Project_Planning.md`](../docs/Project_Planning.md) | Decisions, ownership, open items |
| [`../docs/Project_Origin_Story.md`](../docs/Project_Origin_Story.md) | Motivation and audience |
| [`../docs/Game_System_Scaffold.md`](../docs/Game_System_Scaffold.md) | How to add a game system |
| [`../docs/Rehydration_Prompt.md`](../docs/Rehydration_Prompt.md) | Cold-session bootstrap |
| [`../docs/operations/librarian_agent.md`](../docs/operations/librarian_agent.md) | Librarian operations |
| [`../docs/handoffs/tomb_world_ownership/track_in.md`](../docs/handoffs/tomb_world_ownership/track_in.md) | **Current** track state, locked ownership, model matrix |
| [`../docs/handoffs/v1_scaffold/track_in.md`](../docs/handoffs/v1_scaffold/track_in.md) | Prior track state - closed; its ownership claims are superseded |
| [`../games/warhammer_40k_11e/armies/necrons/Necron_Lists.md`](../games/warhammer_40k_11e/armies/necrons/Necron_Lists.md) | **FOUNDATION** - authoritative Necron ownership |
| [`Initial_Prompt.md`](Initial_Prompt.md) | Original intent, verbatim |
| [`llm-wiki.md`](llm-wiki.md) | The Karpathy pattern this project follows |

---

## Change Log

- v1.2 (2026-08-16): Sec 9 — false Tomb World ownership denials in `KB/` marked Closed/resolved at L1. S4 coord preflight.
- v1.1 (2026-08-16): Ownership realignment, track `tomb_world_ownership` slice S3. Sec 5 rebuilt against FOUNDATION - Kill Team: Tomb World owned and game-ready, extras on sprue, totals of 20 Warriors and 6 Scarab Swarms - and the "superseded and historical" line replaced with an explicit note that the prior claim was erroneous. Added the authoritative order for ownership facts to Sec 6. Rewrote Sec 8 for the current track and the closed `v1_scaffold`. Downgraded the Hierotek Circle photo ID to non-blocking and added the open `KB/` ownership-denial thread. Refreshed git, model-matrix, and reference pointers.
- v1.0 (2026-08-16): Initial distilled context - identity, scope, four-layer architecture, hard rules, confirmed ownership, sources and trust ladder, agents, track state, open threads, vocabulary. Created in slice S1. *(Its ownership section wrongly recorded Tomb World as superseded - see v1.1.)*

## Attribution

- Project: Wargame_Concierge
- Maintainer: Russell Catt
- Sources: see header
- Structured using the Rising Tide framework

## Rising Tide Notes

- This document is a distilled artifact.
- Must remain traceable to the authorities named in each section.
- Optimized for a single-pass LLM read; keep it dense and keep it current.
