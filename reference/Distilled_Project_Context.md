<!--
FILE: reference/Distilled_Project_Context.md
VERSION: v1.0 (2026-08-16)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, slice S1)

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
| Git | Standalone repository. One commit as of 2026-08-16 - the S0+L0 bootstrap, made by the Coordinator |
| Remote | **Private** GitHub repo `russell-catt/Wargame_Concierge` - created and pushed at slice S7, behind a user gate |
| Owner | Russell Catt |
| Framework | Rising Tide documentation standards |
| Knowledge pattern | Karpathy "LLM Wiki", adapted to wargames |
| Domain | Tabletop **wargames**. Not software, not technical writing |
| Status | Active. Track `v1_scaffold` in progress |

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
2. **Never `git commit` or `git push`.** Coordinator is the sole git owner; push is a user gate at S7.
3. **Never commit GW binaries** - no PDFs, official images, `.webp`, `.png`. `.gitignore` enforces it.
4. **Teaching paraphrase only.** No verbatim datasheet statlines, stratagem text, or rules text.
5. **Only the Librarian writes under `KB/`.**
6. **Every rules claim records a retrieval date.**
7. **UTF-8, no BOM.**
8. **Rising Tide headers and YAML frontmatter never stack** - a leading HTML comment breaks frontmatter parsing.

---

## 5. Confirmed model ownership - 2026-08-16

Authority: [`../docs/Project_Planning.md`](../docs/Project_Planning.md) Sec 3. Every list and starter must be written against this.

| Models | Count | State |
|--------|-------|-------|
| Necron Warriors | 10 (1 squad) | Purchased, **unassembled** |
| Canoptek Scarab Swarms | 3 | Purchased, **unassembled** |
| Immortals | 5 (1 squad) | Purchased, **unassembled** |
| Hierotek Circle Kill Team (used set) | 1 set | **Assembled and painted - game ready.** Unit ID **pending owner photos** |

- **Build-before-play is the default.** Only the Hierotek Circle set can hit a table today.
- **Owned models are not shopping targets.** Never list the Immortals, Warriors, or Scarabs as future purchases.
- **Kill Team: Tomb World is superseded and historical** as of 2026-08-16. It does not describe current ownership.
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

One authorized exception to the read-only source library: the Preflight slice edited `C:\Personal\40K\rules\Necron_Lists.md` at source to record confirmed ownership. That single file is imported into the project at S2.

---

## 7. Agents and workflow

| Role | Owns |
|------|------|
| **Coordinator** | Briefs, dispatch, rollup, **sole git commit**; push only after a user gate |
| **Librarian** | Tier 0 knowledge plane: ingest, query, lint, index. Never writes `raw/`. Never commits |
| **Implementer** | Tier 1: shipping content under `docs/`, `games/`, `reference/` |
| **QA** | Tier 2: independent re-check against the brief's exit criteria |
| **Final Sanity** | Tier 3: cross-slice consistency, including KB index and log hygiene |

Artifact lifecycle per slice: `{Id}_brief.md` → `{Id}_implementer.md` or `L{n}_librarian.md` → `{Id}_qa.md` → *Resolved - Complete* → Coordinator commits.

**Model discipline:** the locked per-role matrix lives in [`../docs/handoffs/v1_scaffold/track_in.md`](../docs/handoffs/v1_scaffold/track_in.md). Every report records the model **actually** used. An unavailable model may be substituted within the same family, with the waiver recorded in the report. Implementer and QA never share a model family for the same slice.

---

## 8. Track `v1_scaffold` - state as of 2026-08-16

Order: **Preflight → S0 → L0 → S1 → S2 → L1 → S3 → S4 → S5 → S6 → L2 → S7**

| Slice | Focus | State |
|-------|-------|-------|
| Preflight | Necron ownership patched at source | Complete |
| S0 | Repo bootstrap, templates, playbook, handoffs, `.gitignore`, skeletons | Complete |
| L0 | Karpathy KB bootstrap: `AGENTS.md`, core KB pages, `librarian_agent.md`, `.obsidian/` | Complete |
| **S1** | Core Rising Tide documents and `Game_System_Scaffold.md` | **This slice** |
| S2 | Source library, Necron list import, inventories, game READMEs | Pending |
| L1 | First real ingest - validates the ingest contract | Pending |
| S3 | Beginner rules, board and terrain setup, Keyword Glossary | Pending |
| S4 | Necron starters and two-page laminate guide | Pending |
| S5 | Space Marine Oath / Gladius content and laminate guide | Pending |
| S6 | Full unit research, both factions | Pending |
| L2 | Librarian lint | Pending |
| S7 | Private GitHub repo and Final Sanity | Pending |

**KB maturity: level 1 (pilot).** Zero sources ingested. The first real ingest is L1, and that is what actually proves the ingest contract.

---

## 9. Open threads

| Thread | State | Resolves at |
|--------|-------|-------------|
| **Hierotek Circle photo ID** | **Open.** The only game-ready models cannot yet be mapped to datasheets. Blocked on owner photos | Owner photos, then S4 |
| **Power Matrix attribution** | **Resolved 2026-08-16: it is the Canoptek Court detachment rule in 40K**, not a Kill Team mechanic. Detachment-scoped, not army-wide. `KB/glossary.md` still carries the older unresolved warning | Librarian corrects at L1 |
| Space Marine inventory | Not yet recorded | S5 |
| Beginner-appropriate Necron detachment | Undecided | S4 |
| Target game size for early games | Undecided | S3 / S4 |
| Playbook dead links | 26 relative links inherited from the `daily_report` repo point at directories that do not exist here. Prose is authoritative; links are not | A later cleanup slice |
| UTF-16 files | `checkins/README.md`, `prompts/README.md`, `docs/handoffs/README.md`, `raw/pointers/README.md`, and the S0-authored slice artifacts are UTF-16LE | Coordinator - note that the `raw/` file needs explicit authorization |

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
- **It goes stale by design.** Slices land, ownership changes, threads resolve. Check the date in the header against [`../docs/handoffs/v1_scaffold/track_in.md`](../docs/handoffs/v1_scaffold/track_in.md).
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
| [`../docs/handoffs/v1_scaffold/track_in.md`](../docs/handoffs/v1_scaffold/track_in.md) | Track state and model matrix |
| [`Initial_Prompt.md`](Initial_Prompt.md) | Original intent, verbatim |
| [`llm-wiki.md`](llm-wiki.md) | The Karpathy pattern this project follows |

---

## Change Log

- v1.0 (2026-08-16): Initial distilled context - identity, scope, four-layer architecture, hard rules, confirmed ownership, sources and trust ladder, agents, track state, open threads, vocabulary. Created in slice S1.

## Attribution

- Project: Wargame_Concierge
- Maintainer: Russell Catt
- Sources: see header
- Structured using the Rising Tide framework

## Rising Tide Notes

- This document is a distilled artifact.
- Must remain traceable to the authorities named in each section.
- Optimized for a single-pass LLM read; keep it dense and keep it current.
