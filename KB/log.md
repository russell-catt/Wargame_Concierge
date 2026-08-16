---
title: Log
type: log
system: warhammer_40k_11e
created: 2026-08-16
updated: 2026-08-16
sources: []
confidence: verified
tags: [log, activity, append-only]
---

# KB Log

Append-only chronological record of everything that happens to this KB: ingests, queries, lint passes, and bootstraps.

**Append only.** Add new entries at the bottom; never edit or delete an existing entry. If an earlier entry was wrong, write a new entry that corrects it.

Every entry starts with `## [YYYY-MM-DD] <verb> | <subject>` so the log stays greppable:

```powershell
Select-String -Path KB/log.md -Pattern "^## \[" | Select-Object -Last 5
```

---

## [2026-08-16] bootstrap | L0 - Karpathy KB bootstrap

Knowledge base scaffolded for **Wargame_Concierge**, adapting the Karpathy "LLM Wiki" pattern to the wargames domain. First system in scope: Warhammer 40,000 11th Edition (Necrons, Space Marines).

**Track / slice:** v1_scaffold / L0 (Librarian, Tier 0)
**Depends on:** S0 (Resolved - Complete)

Schema and operations created:
- `AGENTS.md` (repo root) - schema source of truth, adapted from the Karpathy `CLAUDE.md` technical-writer schema
- `docs/operations/librarian_agent.md` - day-to-day Librarian operations across L0/L1/L2

KB core pages created:
- `KB/index.md` - master catalog, bootstrapped with typed sections empty
- `KB/log.md` - this file
- `KB/overview.md` - project synthesis, 40K 11e scope, Necron ownership as of 2026-08-16
- `KB/glossary.md` - seeded with 4 terms, all `unverified`
- `KB/changelog.md` - promotion log, opened with the L0 row
- `KB/ingest_procedure.md` - raw to KB procedure for this project
- `README.md` stubs in all 7 typed KB directories

Supporting:
- `reference/llm-wiki.md` verified byte-identical to the upstream source (already present from S0)
- `.obsidian/` verified at the repo root - the whole repo is an Obsidian vault

Key schema decisions (all recorded in `AGENTS.md`):
- The knowledge layer is **`KB/`**, not `wiki/` - the Karpathy naming is translated, and no `wiki/` directory exists
- Entity types adapted to wargames: Source, Concept, Keyword, Faction, Detachment, Unit, Setup/Mission, Analysis
- **Keyword is glossary-only** - terms live in `KB/glossary.md` and are promoted to `KB/concepts/` only on a stated three-part test
- Added a **`confidence`** frontmatter field (`verified` / `draft` / `stub` / `unverified`) because 11th Edition is new and most early content is unconfirmed
- Rules claims from living references must carry a **retrieval date**; a missing date is a lint finding
- KB pages use **YAML frontmatter only**; Rising Tide HTML headers are reserved for `docs/` and `games/`, because the two conventions cannot stack without breaking frontmatter parsing
- KB filenames are lowercase `snake_case`, deviating from the Karpathy kebab-case to match `ingest_procedure.md` and the rest of the repo

Content state: **scaffolding only.** 0 sources ingested, 0 entity pages. Glossary terms are seeded, not researched - all 4 are flagged for expansion in L1/S3.

Flagged for the Coordinator:
- Three S0-authored markdown files are UTF-16LE encoded, which produces unreadable git diffs and can break Obsidian parsing. Not corrected here (they belong to another slice). See the L0 Librarian report.
- `Power Matrix` may belong to Kill Team rather than 40K 11e. Attribution must be resolved before it is used in any 40K content.

Nothing under `raw/` was created, modified, or deleted. No git commit, no push.

Next step: **S1** (core RT docs + Game_System_Scaffold), then S2 sources, then **L1** for the first real ingest.

---
