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

## [2026-08-16] ingest | L1 - first real ingest (Necron_Lists, Source_Library, pointers)

The first end-to-end ingest, which is what actually validates the contract written in [[ingest_procedure]]. Five sources filed, fifteen entity pages created, one L0 error corrected.

**Track / slice:** v1_scaffold / L1 (Librarian, Tier 0)
**Depends on:** S2 (Resolved - Implemented)
**Model:** `claude-opus-5-thinking-high` - waiver, locked `claude-fable-5-thinking-high` unavailable

**Sources ingested:**

| Source | Class | Read? |
|--------|-------|-------|
| `raw/Necron_Lists.md` | Owner's own notes | **In full** |
| `reference/Source_Library.md` | Project catalog | **In full** |
| `raw/pointers/*.md` (8 stubs) | Pointer stubs | **In full** |
| Wahapedia | Living web reference | **No** - registered only |
| Warhammer Community | Living web reference | **No** - registered only |

**Pages created (15):**

- Sources: `necron_lists_owner_notes`, `source_library`, `local_library_pointers`, `wahapedia`, `warhammer_community`
- Factions: `necrons`, `space_marines`
- Detachments: `canoptek_court`, `cryptek_conclave`, `gladius_task_force`
- Concepts: `power_matrix`, `reanimation_protocols`, `oath_of_moment`, `objective_control`
- Analyses: `inherited_docs_for_S3`

**Pages updated (4):** `glossary`, `index`, `overview`, `changelog`

**Key additions:**

- **Power Matrix attribution corrected.** L0 seeded the term with an explicit warning that it might belong to *Kill Team* rather than 40K, reasoning from the owner's Hierotek Circle box. Two independent in-repo sources - `raw/Necron_Lists.md` and `docs/Game_System_Scaffold.md` - name it as the **Canoptek Court detachment rule in Warhammer 40,000**. Resolved on `power_matrix`, corrected in `glossary`, and added to the deprecated list so the old claim cannot quietly return. The rule's *wording* remains unverified; only its system and detachment are settled.
- **Ownership captured as of 2026-08-16:** 10 Warriors, 3 Scarab Swarms, 5 Immortals - all purchased and unassembled; Hierotek Circle used set game-ready with datasheets TBD pending photos; Kill Team: Tomb World **not owned**.
- **Glossary expanded from 4 terms to 32**, sectioned by scope (core rules, Necrons, Space Marines, other systems, project vocabulary) for S3 `Keyword_Glossary` alignment. Four promoted terms now carry concept pages with glossary stubs pointing at them, per `AGENTS.md` Sec 5.
- **"Data Package Detachment" flagged `unresolved`** - it appears in the owner's notes as a tier label and maps to no recognised 40K term. Recorded rather than propagated.
- **Kill Team added as a glossary entry** specifically to keep the two game systems apart, since conflating them caused the one error this ingest had to fix.

**The honest headline:** no rules document was read. The owned core rules, both faction packs, the terrain PDFs, and the points manuals are all catalogued in `local_library_pointers` and all unopened. Zero game terms are `verified`. The project's gap moved from "no sources" to "unread sources", which is a better problem and a different one.

Nothing under `raw/` was created, modified, or deleted. No git commit, no push.

Next step: **S3** (rules + setup + Keyword_Glossary). Start by reading `raw/pointers/rules_core.md`; the handoff is `inherited_docs_for_S3`.

---

## [2026-08-16] lint | L2 v1_scaffold
Pages created: KB/units/necrons_unit_index.md, KB/units/space_marines_unit_index.md
Pages updated: glossary.md (Power Matrix + Technosorcerous Augmentations consistency)
Issues found: glossary drift (fixed), UTF-16 pages (fixed), research stubs (accepted), Hierotek TBD (open)
Fixes applied: see L2_librarian.md

## [2026-08-16] sync | Necron ownership re-align

Re-synced `raw/Necron_Lists.md` to the armies working copy after a working-tree drift that again treated **Kill Team: Tomb World** as owned. Project armies copy and `C:\Personal\40K\rules\Necron_Lists.md` were already byte-identical and correct; preferred the project copy. Committed HEAD already matched the correct FOUNDATION.

**Ownership confirmed (unchanged):** 10 Warriors, 3 Scarab Swarms, 5 Immortals (purchased, unassembled); Hierotek Circle used set game-ready (datasheets TBD pending photos); Tomb World **not owned**.

**Also updated:** `raw/pointers/necron_lists_import.md`, `KB/sources/necron_lists_owner_notes.md`, `KB/sources/source_library.md` (prefer armies copy on divergence), inventory/README/starters/laminate version bumps, `docs/Project_Planning.md` completed-to-date note.

---

## [2026-08-16] ingest | L1 - Tomb World ownership correction

**This entry corrects the two entries above.** Both recorded **Kill Team: Tomb World as not owned**, and the 2026-08-16 sync entry described a working-tree state that "again treated Tomb World as owned" as a drift to be reverted. That was backwards. The box **is** owned, its units are assembled and painted, and the "not owned" reading was the error.

**Track / slice:** `tomb_world_ownership` / L1 (Librarian, Tier 0)
**Depends on:** S3 (Resolved - Complete)
**Model:** `claude-opus-5-thinking-high` - **waiver**: locked `claude-fable-5-thinking-high` was blocked/unavailable at dispatch. Same Anthropic family. QA is `gpt-5.6-sol-medium` (different family, so the cross-family QA requirement still holds).

**Locked ownership now recorded across the KB:**

*Game-ready - Kill Team: Tomb World, assembled and painted, known datasheets:*

| Unit | Qty |
|------|-----|
| Cryptek Geomancer | 1 |
| Canoptek Tomb Crawlers | 2 |
| Canoptek Macrocytes | 5 |
| Necron Warriors | 10 |
| Canoptek Scarab Swarms | 3 |

*Also game-ready:* Hierotek Circle used set - datasheets still **TBD pending owner photos**.

*Owned, unassembled:* second Necron Warriors squad (10), second Canoptek Scarab Swarms set (3), Immortals (5).

**Totals:** 20 Necron Warriors, 6 Canoptek Scarab Swarms, plus Geomancer, Tomb Crawlers, Macrocytes, Immortals, and Hierotek Circle.

**Rules removed as current guidance:**

- **"Do not let Tomb World content leak into current advice."** Written as a guardrail against stale data, it had become the stale data. Retired to the [[glossary]] deprecated list so it cannot return as guidance.
- **"Kill Team: Tomb World - not owned."** Deleted as a fact everywhere in `KB/`; retained only as a named, deprecated claim.

**KB pages updated (11 files):**

| Page | What changed |
|------|--------------|
| `sources/necron_lists_owner_notes` | FOUNDATION table rewritten; "Historical material" section replaced by "The Tomb World correction"; Conclave spend corrected to ~$310 / $155-220 |
| `factions/necrons` | Ownership section rewritten; "Explicitly not owned" removed; detachment-fit and recommendation rewritten around game-ready models |
| `glossary` | Tomb World entry inverted to owned/game-ready; Hierotek entry no longer claims sole game-readiness; `Game-ready` and `Build before play` re-scoped; **Assemble-to-expand** added; deprecated list rewritten; L1 ownership note appended |
| `overview` | Ownership table rewritten with totals; "awkward shape" framing replaced; new "Resolved in L1 - tomb_world_ownership" section; glossary metrics and last-ingest row refreshed |
| `sources/source_library` | Ownership snapshot corrected; stale "not owned" snapshots explicitly marked untrustworthy |
| `analyses/inherited_docs_for_S3` | Stable-ownership table rewritten with totals; teaching constraints re-derived; Hierotek thread de-escalated |
| `detachments/canoptek_court` | "Not currently playable" reversed - Tomb World supplies real Canoptek bodies; Phase 1 unblocked |
| `detachments/cryptek_conclave` | Cryptek requirement satisfied by the owned Geomancer rather than a Hierotek guess; spend corrected; phases re-derived |
| `units/necrons_unit_index` | Owned-units table rebuilt; priority mis-tagging of Geomancer / Tomb Crawlers / Macrocytes recorded as a `games/` follow-up |
| `log`, `changelog` | This entry and the promotion row |

**Also corrected in passing:** the owner's *Ignores Cover* claim for Canoptek Macrocytes is now flagged as disproven on `necron_lists_owner_notes`, matching what [[glossary]] already recorded from S4. It matters more now that the Macrocytes are game-ready.

**The lesson, stated for future sessions.** The Power Matrix error was cheap to fix because L0 wrote its uncertainty down loudly. This error was expensive because a **negative ownership claim** was written as settled fact, propagated across the KB, and then defended by a guardrail rule. Inventory claims deserve the same "verify against the owner" discipline as rules claims, and a *denial* deserves it most.

Nothing under `raw/` was created, modified, or deleted. No git commit, no push - the single deferred commit is Coordinator-owned at S4.

Next step: **L2** (audit + lint), then **S4** (Final Sanity, then commit and push).

---

## [2026-08-16] lint | L2 - audit of `v1_scaffold` L2, plus full re-lint

**Track / slice:** `tomb_world_ownership` / L2 (Librarian, Tier 0)
**Depends on:** L1 (Resolved - Complete)
**Model:** `claude-opus-5-thinking-high` - **waiver**: locked `claude-fable-5-thinking-high` was blocked/unavailable at dispatch. Same Anthropic family. QA is `gemini-3.7-flash-high` (different family, so the cross-family QA requirement holds).

**Audit of the `v1_scaffold` L2 gate:** PASS with a delta. Its four hard exit criteria all still hold on disk - the lint report exists with severities, the agreed fixes are present, `log` and `changelog` carry L2 entries, and both unit-index pointer pages exist and link to the shipping `Unit_Index.md` files. Two of its *open items* had gone stale, and its glossary fix turned out to be narrower than it read.

**Why a full re-lint rather than a targeted one.** The re-execute rule fires on either a failed exit criterion **or** L1 ownership edits reintroducing contradictions, orphans, or glossary drift. Criteria 1-4 passed; the second clause tripped. L1 correctly rewrote nine `KB/` pages around the true ownership, which left two shipping detachment guides asserting the opposite, and the deferred "Scientific Schemes" rename was still live in four `KB/` pages.

Issues found: 13 (3 High, 5 Medium, 3 Low, 2 Info). Fixed: 9. Flagged in place rather than guessed: 1 (missing MFM points). Deferred to the Coordinator: 2. Recorded only: 1.

**Ownership sweep result.** Zero live "Tomb World not owned / superseded" assertions remain in `KB/`. Every surviving string is a deprecated-claim row, an explicit correction note, or append-only log history that a later entry corrects. The two live denials outside `KB/` that L1 flagged - `docs/Rehydration_Prompt.md` and `reference/Source_Library.md` - were fixed by the Coordinator at S4 preflight and re-verified clean here. One live denial remains, in `games/warhammer_40k_11e/rules/Keyword_Glossary.md`, outside this slice's edit surface.

**Pages updated (13 files):**

| Page | What changed |
|------|--------------|
| `glossary` | **Scientific Schemes** headword replaced by **Technosorcerous Augmentations**, with both effects from the owned faction pack v1.1; deprecated-list row added for the old label; verification-queue row closed; L2 lint note appended |
| `detachments/cryptek_conclave` | Renamed throughout; the rule's two real effects and the attached-unit keyword mechanic written up; "what Scientific Schemes actually does" removed from Open questions because it is now known |
| `concepts/power_matrix` | Related-terminology paragraph renamed and re-levelled - the sibling rule is now better established than this one, not equally uncertain |
| `factions/necrons` | Terminology table renamed; `[[necrons_unit_index]]` back-link added; "No unit pages exist" replaced with an accurate statement |
| `factions/space_marines` | `[[space_marines_unit_index]]` back-link added |
| `sources/necron_lists_owner_notes` | Old label **kept** in the source-quoting table per Sec 9, with a conflict flag beside it; rules-lead row marked disproven |
| `analyses/inherited_docs_for_S3` | Two rows corrected - the name handed to S3 was wrong, and S3 caught it |
| `index` | "5 sources, 15 entity pages" corrected to 17; the "no rules document has been read" banner replaced - true at L1, false since S3 |
| `overview` | Entity-page count, last-lint row, and the "we have not read the sources we have" framing all corrected; the real remaining gap named as a `KB/` back-fill gap |
| `games/.../necrons/Canoptek_Court` | Ownership correction - see below |
| `games/.../necrons/Cryptek_Conclave` | Ownership correction - see below |
| `log`, `changelog` | This entry and the promotion rows |

**Two shipping teaching pages corrected under the ownership-lint mandate.** Both were `v1_scaffold` S4 output, both were written against the false inventory, and both now contradicted the `KB/` pages L1 had fixed:

- `Canoptek_Court.md` rated itself **"not first, on this collection - the models that are owned get nothing from the rule."** Four of the five game-ready Tomb World units are Cryptek or Canoptek and do benefit. Verdict reversed, fit table rebuilt.
- `Cryptek_Conclave.md` said **"the whole path hinges on one unanswered question: is there a Cryptek in the Hierotek Circle set?"** The owned Geomancer is that Cryptek. The photo ID is an upside now, not a dependency. The page had also omitted the Geomancer from its own fit table.

**A gap the ownership error left behind that nobody has closed.** The Geomancer, Tomb Crawlers and Macrocytes have **no Munitorum Field Manual v1.2 points** anywhere in the repo, because the slice that read the MFM did so believing those models were not owned. They are the models most likely to hit a table first. Both teaching pages now say so explicitly rather than guessing a number.

**The lesson, stated for future sessions.** L1 fixed the ownership fact and the `KB/` pages that asserted it. What it could not fix from its own surface were the pages that had silently *reasoned* from the false fact - a detachment verdict, a fit table, a research-priority tag. A false claim propagates twice: once as a statement, and once as everything derived from it. The second wave is harder to grep for, because it never repeats the words you would search on.

Nothing under `raw/` was created, modified, or deleted. No git commit, no push - the single deferred commit is Coordinator-owned at S4.

Next step: **S4** (Final Sanity, then commit and push).

