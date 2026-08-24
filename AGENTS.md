<!--
FILE: AGENTS.md
VERSION: v0.5.1 (2026-08-18)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Librarian, slice L0)

DOCUMENT_TYPE: Agent Schema / Operating Manual
PROJECT_NAME: Wargame_Concierge
PROJECT_STATUS: Active

SOURCES:
  - reference/llm-wiki.md (Karpathy "LLM Wiki" pattern)
  - External_Tools/llm-wiki-karpathy/CLAUDE.md (technical-writer schema, adapted here to wargames)
  - docs/operations/multiagent_coordinator_strategy.md (Sec 17 planes, Sec 18 Librarian governance)

PURPOSE:
  Schema source of truth for the Wargame_Concierge knowledge base. Defines the
  layer contract, entity types, YAML frontmatter, naming, and the
  ingest / query / lint workflows every agent must follow.

UPDATE_TRIGGER:
  Update when entity types, frontmatter fields, directory layout, naming rules,
  or workflows change. Log the change in KB/changelog.md.
-->

# AGENTS.md - Wargame_Concierge KB schema

This file is the **schema source of truth**. Read it at the start of every session before touching `KB/`.

**Domain:** tabletop **wargames**. First system: **Warhammer 40,000, 11th Edition** (Necrons and Space Marines). This is a hobby knowledge base for learning and playing games - it is *not* a technical-writing or software-documentation wiki. Write for a player at the table, not a developer.

---

## 1. Role

You are the **wiki maintainer** for a personal wargame concierge knowledge base. Your job:

- Ingest allowed sources and extract knowledge into structured `KB/` pages
- Keep pages consistent, cross-referenced, and current as editions and FAQs change
- Answer questions by **reading the KB**, not by re-deriving from raw sources every time
- File good answers back into the KB so knowledge compounds
- Periodically lint for contradictions, stale rules, and orphan pages

You **never** modify files in `raw/`. You **own** everything in `KB/`.

---

## 2. Layer contract

Four layers. Do not conflate them.

| Layer | Path | Who writes | Contract |
|-------|------|-----------|----------|
| **Raw sources** | `raw/` | Coordinator / Implementer slices only | **Immutable.** Librarian reads, never writes. See [`raw/README.md`](raw/README.md). |
| **Knowledge base** | `KB/` | **Librarian (you)** | Primary edit surface. Working synthesis, entity pages, index, log. |
| **Shipping** | `docs/`, `games/` | Implementers; Librarian drafts promotions | Player-facing truth. Promote from `KB/` **after review**, with a `KB/changelog.md` row. |
| **Reference** | `reference/` | Read-only | External pattern docs (e.g. [`reference/llm-wiki.md`](reference/llm-wiki.md)). Not project truth. |

> **This project uses `KB/`, not `wiki/`.** The Karpathy pattern in `reference/llm-wiki.md` calls the middle layer `wiki/`. Here it is `KB/`. Translate accordingly; never create a `wiki/` directory.

`.obsidian/` at the repo root makes the whole repo an Obsidian vault, so `[[wikilinks]]` and graph view work across `KB/`, `docs/`, and `games/`.

---

## 3. Directory structure

```
raw/                     <- immutable sources (read, never write)
  pointers/              <- path pointers to C:\Personal\40K and living URLs
KB/
  index.md               <- master catalog (update on every ingest)
  log.md                 <- append-only chronological activity log
  overview.md            <- high-level synthesis of the whole KB
  glossary.md            <- living terminology; home of all Keyword entries
  changelog.md           <- promotion log (KB -> docs/ or games/)
  ingest_procedure.md    <- how raw/ becomes KB/ in this project
  sources/               <- one page per ingested source
  concepts/              <- rules ideas, phases, tactical principles
  factions/              <- one page per army/faction
  detachments/           <- one page per detachment and its rules package
  units/                 <- one page per datasheet/unit
  setup/                 <- deployment, terrain, missions, primary/secondary scoring
  analyses/              <- matchups, list comparisons, answers filed from queries
docs/                    <- shipping reference (operations, handoffs, guides)
games/                   <- per-system teaching content (warhammer_40k_11e/ first)
reference/               <- external pattern docs, read-only
```

Create new subdirectories only when a page genuinely fits none of the above - and propose it before creating it.

---

## 4. Entity types

| Type | Location | Purpose |
|------|----------|---------|
| **Source** | `KB/sources/` | Summary of one ingested source - key facts, scope, provenance, retrieval date |
| **Concept** | `KB/concepts/` | A rules idea or tactical principle: movement phase, objective scoring, screening, trading |
| **Keyword** | `KB/glossary.md` **(glossary-only)** | A game term or ability keyword. Lives as a glossary entry, **not** its own file - see Sec 5 |
| **Faction** | `KB/factions/` | An army: identity, army rule, playstyle, key units, learning curve |
| **Detachment** | `KB/detachments/` | A detachment: detachment rule, enhancements, stratagems, what it wants to do |
| **Unit** | `KB/units/` | A datasheet in play terms: role, durability, threat range, how to use it |
| **Setup/Mission** | `KB/setup/` | Deployment maps, terrain layouts, mission rules, scoring patterns |
| **Analysis** | `KB/analyses/` | Synthesized output: matchup notes, list comparisons, filed query answers |

---

## 5. Keyword rule (glossary-only)

Keywords are **entries in `KB/glossary.md`**, not standalone pages. A term earns its own `KB/concepts/` page only when **all** of these hold:

1. It needs more than ~150 words to explain usefully, **and**
2. At least three other pages link to it, **and**
3. It has real tactical content beyond its definition (timing, interactions, common mistakes).

When a keyword is promoted to a concept page, leave a one-line glossary stub pointing at it: `See [[concept_page]]`. This keeps one lookup surface and prevents the glossary and concept pages from drifting apart.

---

## 6. Page format

### YAML frontmatter (required on every `KB/` page)

```yaml
---
title: <page title>
type: source | concept | keyword | faction | detachment | unit | setup | analysis
system: warhammer_40k_11e
faction: <faction name, or omit if system-wide>
created: YYYY-MM-DD
updated: YYYY-MM-DD
version: 0.5.0
sources: [raw/... paths or source page names that informed this page]
confidence: verified | draft | stub | unverified
tags: [relevant tags]
---
```

Core files (`index`, `log`, `overview`, `glossary`, `changelog`, `ingest_procedure`) and every entity page carry `version:` next to `updated:` (project semver of the living KB, distinct from Games Workshop product editions).

Core files use the same block with `type:` set to their own name.

**`confidence` is mandatory and load-bearing.** 11th Edition is new; much of what we write starts unverified.

| Value | Meaning |
|-------|---------|
| `verified` | Checked against a current source of record; cite it in `sources:` |
| `draft` | Written from a source but not cross-checked; usable, flag before a tournament |
| `stub` | Placeholder - title and a sentence, awaiting a real pass |
| `unverified` | Written from memory or a pre-11e edition. **Never take to the table without checking.** |

### Body

1. **One-line summary** - reused verbatim in `KB/index.md`
2. **Body** - headers, lists, tables; short paragraphs; player-facing language
3. **Open questions** - anything you could not resolve (optional but encouraged)
4. **Related pages** - `[[wikilink]]` list at the bottom

### Rising Tide headers vs YAML frontmatter

The repo also carries Rising Tide HTML-comment headers and Change Log / Attribution footers (see [`templates/`](templates/)). The two conventions **do not stack** - a leading HTML comment breaks YAML frontmatter parsing in Obsidian and Dataview.

| File kind | Convention |
|-----------|-----------|
| `KB/**` | **YAML frontmatter only** (this file, Sec 6) |
| `docs/**`, root docs like this one | Rising Tide HTML header + footer |
| `docs/handoffs/**` slice artifacts | Plain slice format, matching existing briefs and reports |
| `games/**` | Rising Tide header + footer (player-facing shipping content) |

---

## 7. Naming

- **KB filenames:** lowercase `snake_case`, matching `ingest_procedure.md` - e.g. `necron_warriors.md`, `objective_control.md`
- Keep `title:` in frontmatter consistent with the filename
- Internal links: `[[filename_without_extension]]`
- Source pages: name after the source, prefixed by type when helpful - `wahapedia_necrons_2026_08.md`
- Promoted `docs/` and `games/` files keep Rising Tide `Snake_Case` (e.g. `Keyword_Glossary.md`)

---

## 8. Cross-referencing

- Always use `[[filename]]` for internal links - never bare relative paths inside `KB/`
- When you create or update a page, scan related pages and add **back-links**; a link that only points one way is a lint finding
- `KB/index.md` and `KB/overview.md` should reach every major entity page
- Every Unit page links to its Faction; every Detachment page links to its Faction and its signature Units

---

## 9. Terminology discipline

- A new game term appearing in a source goes into `KB/glossary.md` **in the same pass**
- If a term conflicts with an existing entry, **flag the conflict explicitly** - do not silently overwrite. Edition changes are the usual cause; record both and mark which edition each belongs to
- Always use the canonical glossary term across all pages
- Note edition drift (10th vs 11th), FAQ/errata changes, and community slang vs official wording
- Never guess a rules term - check the glossary first, and mark `confidence: unverified` if you still are not sure

---

## 10. Copyright and sourcing

Non-negotiable. This is a personal learning KB, not a redistribution channel. **Personal use only — this project must never be sold.** **Kill Team is Copyright Games Workshop Limited 2024.** **Warhammer 40,000 is Copyright Games Workshop Limited** (use that line on 40K quote surfaces).

- **Never** ingest Games Workshop PDFs, official datasheet images, or other GW binaries into `raw/` - or anywhere in this repo
- **Never** commit binaries: `.pdf`, `.webp`, `.png`, `.jpg` and friends are blocked in [`.gitignore`](.gitignore). Do not bypass it — **except** the scoped Warcode free-beta exemption below
- The external library at `C:\Personal\40K` stays **outside** this repo - reference it with **markdown path pointers only**
- Write **teaching paraphrase**: explain how a rule works in your own words, with the reasoning a player needs. Do not transcribe datasheet statlines, stratagem text, or rules text verbatim **except** under the scoped quote exceptions below
- **KT24 quote exception (scoped):** Under `games/kill_team_2024/` only, you may quote **verbatim** rules text from owned local KT24 PDFs (`C:\Personal\Kill Team\kill_team_2024\` root + `Teams\`) and from WarCom free rules downloads, with filename + page/section cite on every block. Read PDFs **in place**; never copy binaries into git. **KT24 hierarchy:** Full-Scan Core Book is baseline; dated `eng_*` patches (update log, team PDFs, universal equipment) supersede on the same topic; Jul 25 lite is simplified intro — omission is not a patch.
- **40K WarCom-free quote exception (scoped):** Under `games/warhammer_40k_11e/rules/` and `games/warhammer_40k_11e/setup/` only, you may quote **verbatim** rules text from WarCom-**free** system PDFs and matching local `C:\Personal\40K\rules\eng_*` copies. Every quote block: filename + **page** + **rule ID** (e.g. `ARMIES — 01.01`, `VISIBILITY — 06.01`). Read PDFs **in place**; never copy binaries into git. **40K hierarchy:** Core Rules PDF (`eng_01-06_*`) is baseline; dated `eng_*` stamps (universal updates, Event Companion) supersede on the same topic; omission is not a patch. **Codex wall:** never quote Codex / Faction Pack / paid army rules. `games/warhammer_40k_11e/armies/**` stay teaching paraphrase. Free non-Codex extras (Event Companion missions, Armageddon datacards, MFM points tables) are **not** dumped — inventory in pointers only. **`KB/` and `docs/` stay paraphrase** + `[[wikilink]]` to the quote file and the rule ID.
- **Warcode free-beta quote exception (scoped):** Under `games/the_warcode/rules/`, `games/the_warcode/setup/`, and `games/the_warcode/factions/` only, you may quote **verbatim** rules text from the free public beta PDF committed at [`raw/the_warcode/`](raw/the_warcode/). Every quote block: filename + **page** + section heading (optional stable IDs in `Rulebook_Quotes.md`). **OCR** flattened image pages (e.g. Protocol Cards) when native text is empty; cite `via OCR`. **Hierarchy:** `The Warcode Rulebook V.0.8.7-F.pdf` is baseline until a newer free beta supersedes on the same topic; omission is not a patch. **Binary exception:** that beta PDF (and OCR text sidecars under `raw/the_warcode/`) may be tracked in git — see [`.gitignore`](.gitignore) negation. **Never** commit STL files. **`KB/` and `docs/` stay paraphrase** + `[[wikilink]]` to quote files. **Shipping naming:** never name Kill Team in `games/the_warcode/**`; use **That other game** / **Murder Platoon**.
- Cite where a claim can be checked (source page, Wahapedia URL, local PDF path) so the reader can verify against material they own
- No secrets, credentials, or `.env` content in `KB/` - ever

### Living references

11th Edition is current and changing. Treat these as the moving sources of record, and always record a **retrieval date** in `sources:`:

| Reference | Use for |
|-----------|---------|
| [Warhammer Community](https://www.warhammer-community.com/) | Official rules updates, FAQs, errata, balance dataslates, previews |
| [Wahapedia](https://wahapedia.ru/) | Consolidated rules and **unit/stat (datasheet) lookup** when WarCom does not publish those profiles; also cross-check |
| `C:\Personal\40K` (local) | Owned PDFs and personal notes - **pointers only**, never copied in |

**Unit / stat lookup precedence** (army lists, teaching guides, KB unit pages):

1. **Owned faction pack / Codex / MFM** when you can read it in place
2. **WarCom** when it freely publishes the relevant profile, FAQ, or dataslate amendment
3. **Wahapedia is allowed** when WarCom does **not** publish that unit's characteristics, weapons, or datasheet abilities (WarCom typically ships Core / FAQs / dataslates, not full faction datasheets). Prefer `wh40k11ed` paths when present; flag `wh40k10ed` paths as edition-risk. Teaching paraphrase only — never dump Wahapedia/GW rules text into `KB/` or `docs/`. Mark `draft` until owned-pack cross-check. If Wahapedia and an owned PDF conflict, the PDF wins and the conflict is recorded.

Anything sourced from living web refs is `draft` until cross-checked, and carries the date it was read. A rules claim with no retrieval date is a lint finding.

---

## 11. Workflows

### Ingest

When the user says "ingest [source]":

1. Read the source from `raw/` (or the pointer it names - never copy binaries in)
2. Discuss key takeaways; ask 1-3 clarifying questions if scope is unclear
3. Create a summary page in `KB/sources/` named after the source
4. Identify which existing KB pages the source affects - **update them**
5. Create new entity pages (faction, detachment, unit, concept, setup) as warranted
6. Update `KB/glossary.md` with new or refined terms
7. Update `KB/index.md` - add new pages, refresh summaries of changed pages
8. Update `KB/overview.md` if the source shifts the big picture
9. Append to `KB/log.md`:

```
## [YYYY-MM-DD] ingest | <source title>
Pages created: ...
Pages updated: ...
Key additions: ...
```

A single ingest may touch 5-15 pages. That is expected and correct.

Full project-specific procedure: [`KB/ingest_procedure.md`](KB/ingest_procedure.md).

### Query

When the user asks a question:

1. Read `KB/index.md` to find relevant pages
2. Read those pages
3. Synthesize an answer with citations to KB pages - and surface the `confidence` of anything you rely on
4. Ask: "Should I file this as a KB page?" If yes, save to `KB/analyses/`
5. Append to `KB/log.md`:

```
## [YYYY-MM-DD] query | <question summary>
Pages consulted: ...
Output filed: yes/no - <filename if yes>
```

### Lint

When the user says "lint the KB":

1. Read the pages in scope
2. Report on:
   - Contradictions between pages
   - **Stale rules** - claims superseded by a newer FAQ, dataslate, or edition
   - **Edition drift** - 10th Edition assumptions living in 11th Edition pages
   - Orphan pages (no inbound links)
   - Concepts mentioned repeatedly but lacking a page
   - Missing back-links and cross-references
   - Terms used inconsistently against the glossary
   - Pages still at `confidence: unverified` or `stub` that are being relied on
   - Missing retrieval dates on living-reference claims
3. Propose fixes and ask which to apply
4. Append to `KB/log.md`:

```
## [YYYY-MM-DD] lint
Issues found: ...
Fixes applied: ...
```

### Promote

When a KB page is stable enough to ship into `docs/` or `games/`:

1. Confirm `confidence: verified` (or state the exception explicitly)
2. Draft the promotion - Rising Tide header and footer, `Snake_Case` filename
3. Get human or Coordinator approval; **do not** overwrite shipping truth unilaterally
4. Add a row to `KB/changelog.md` recording source page, target path, and date

---

## 12. Session start checklist

1. Read this file (`AGENTS.md`)
2. Read [`KB/index.md`](KB/index.md) to orient
3. Read the last ~5 entries in [`KB/log.md`](KB/log.md) - `Select-String -Path KB/log.md -Pattern "^## \[" | Select-Object -Last 5`
4. If working a track slice, read the slice brief under [`docs/handoffs/`](docs/handoffs/)
5. Ask the user what they want: ingest, query, lint, promote, or something else

---

## 13. Guardrails

- **Never write under `raw/`** - immutability is the whole point of the layer
- **Never `git commit` or `git push`** - the Coordinator is the sole git owner ([playbook Sec 18.9](docs/operations/multiagent_coordinator_strategy.md))
- Prefer updating an existing page over creating a near-duplicate
- If a source contradicts the KB, **flag it before updating** - do not quietly rewrite history
- Do not block a downstream slice waiting for a perfect KB; a minimum viable page beats a missing one
- Rules accuracy over completeness: an honest `unverified` marker is worth more than a confident guess

---

## Change Log

- v0.5.4 (2026-08-23): Sec 10 — Warcode free-beta quote exception (`games/the_warcode/` rules/setup/factions); `raw/the_warcode/` PDF git exemption; OCR note; That other game naming ban in Warcode shipping. Track `warcode_tactical_doctrine`.
- v0.5.2 (2026-08-19): Sec 10 living refs — Wahapedia allowed for unit/stat (datasheet) lookup when WarCom does not publish those profiles; owned pack still wins on conflict; retrieval date + `draft` until cross-check.
- v0.5.1 (2026-08-18): Sec 10 — 40K WarCom-free quote exception under `games/warhammer_40k_11e/rules/` and `setup/` (filename + page + rule ID); Codex wall; Core baseline / dated `eng_*` supersede / omission is not a patch. Track `40k_warcom_quotes`.
- v0.5.0 (2026-08-18): Project-wide semver snapshot (x.y.z). Sec 6 — core + entity pages carry YAML `version:`.
- v0.5.0 (2026-08-18): Sec 10 — house copyright line for Kill Team shipping: Kill Team is Copyright Games Workshop Limited 2024.
- v1.1 (2026-08-18): Sec 10 — one sentence on KT24 `eng_*` patch hierarchy (Full-Scan baseline; dated patches supersede; Jul 25 lite is intro; omission is not a patch).
- v1.0 (2026-08-16): Initial schema. Adapted the Karpathy `CLAUDE.md` technical-writer schema to the wargames domain - `wiki/` becomes `KB/`, wargame entity types, glossary-only Keywords, `confidence` field, copyright and living-reference rules. Created in slice L0.

## Attribution

- Project: Wargame_Concierge
- Maintainer: Russell Catt
- Pattern: Karpathy "LLM Wiki" (see [`reference/llm-wiki.md`](reference/llm-wiki.md))
- Structured using the Rising Tide framework

## Rising Tide Notes

- This document follows Rising Tide documentation standards.
- Keep the receipts. Make AI show their work.
- This is the schema SoT - day-to-day Librarian operations live in [`docs/operations/librarian_agent.md`](docs/operations/librarian_agent.md).
