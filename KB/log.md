---
title: Log
type: log
system: multi_system
systems: [warhammer_40k_11e, kill_team_2024]
created: 2026-08-16
updated: 2026-08-25
version: 0.5.6
sources: []
confidence: verified
tags: [log, activity, append-only, kill_team_2024]
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

---

## [2026-08-17] ingest | L1 `kill_team_2024_scaffold` - first Kill Team 2024 ingest (core rules)

**The first ingest for the KB's second game system.** Kill Team 2024 (KT24 / 3rd Edition) joins Warhammer 40,000 11th Edition as a tracked system, with its own `system: kill_team_2024` pages and its own section in every multi-system core file.

**Track / slice:** `kill_team_2024_scaffold` / L1 (Librarian, Tier 0)
**Depends on:** Preflight, S0 (both Resolved - Complete)
**Model:** `claude-sonnet-5-thinking-high` (locked matrix value; **not** `claude-fable-5-thinking-high` per the standing exclusion in `track_in.md`). No waiver needed this slice.

**Sources ingested:**

| Source | Class | Read? |
|--------|-------|-------|
| Wahapedia - Kill Team 3 Core Rules, <https://wahapedia.ru/kill-team3/the-rules/core-rules/> | Living web reference | **In full**, retrieved 2026-08-17 |
| `raw/pointers/kill_team_2024_core.md` (owned Core Rules PDF, lite rules, update log, universal equipment, sniper update) | Pointer stub to owned PDFs | Registered only - the Librarian cannot open binaries |
| `raw/pointers/kill_team_web_living_sources.md` | Pointer stub | Read in full |

**Pages created (7):**

- Sources: `kill_team_2024_core_rules`
- Concepts: `turning_points`, `activations_apl`, `orders_conceal_engage`, `cover_kill_team`, `control_range_kill_team`, `injured_operatives`

**Pages updated (5):** `glossary` (new Kill Team 2024 section, 20 terms; 6 collision-flag pairs against existing 40K terms), `overview` (new "Second system" section; multi-system frontmatter and metrics), `index` (new Kill Team 2024 section with its own Sources/Concepts tables; multi-system frontmatter), `log` (this entry; multi-system frontmatter), `changelog` (no-promotion row, see below).

**Key additions:**

- **Kill Team and 40K rules stay split, enforced structurally.** The new KT24 glossary section sits separate from the 40K sections, not interleaved, and every shared-sounding term (Cover, Charge, Engagement Range/Control Range, Command Point, Engage vs nothing, Injured vs Battle-shock) carries an explicit, bidirectional **collision flag** in both entries. This is the same discipline the Power Matrix error taught in the 40K track, applied pre-emptively this time instead of after a mistake.
- **One naming deviation from the brief, recorded rather than silently applied.** The brief suggested `engagement_range_kill_team.md` as a concept-page filename, pattern-matching 40K's term. KT24's actual rule is **Control Range** - a different mechanic (visibility-gated, 1", decides marker control by APL total) from 40K's Engagement Range (non-visibility-gated, 2"/5", decides melee/movement legality). Filed as `control_range_kill_team.md` per [`AGENTS.md`](../AGENTS.md) Sec 9 ("never guess a rules term"); the deviation and reasoning are recorded on the page itself, in `glossary.md`, and in `L1_librarian.md`.
- **Honest confidence throughout: everything is `draft`, nothing is `verified`.** The only KT24 material read this pass is a community aggregator (Wahapedia), not the owned Core Rules PDF - the Librarian cannot open binaries, and the pointer stub at `raw/pointers/kill_team_2024_core.md` stays exactly that. A `verified` KT24 page needs a future pass where a human (or an Implementer with file access) reads the owned PDF and the Librarian cross-checks against it.
- **Wahapedia's own book-version table flags a live risk.** The KT3 Core Rules page shows a "June 2026" Core Book update, one version ahead of "February 2026" - i.e. the rules have already been revised at least once since KT24 launched, and where the owned Full-Scan PDF sits relative to that update is unknown. Recorded as an open question on `kill_team_2024_core_rules`.
- **Second-system plumbing landed in the shared core files**, not just new pages: `glossary.md` and `overview.md` frontmatter changed from single-`system` to a `systems:` list, and `index.md` gained a visually separate Kill Team 2024 section rather than interleaving KT24 rows into the 40K tables.

**What was not done, on purpose:** no `KB/factions/`, `KB/detachments/`, or `KB/units/` KT24 pages - core rules and setup come before team/operative content, mirroring the 40K `ingest_procedure` ordering. The ten owned team-rule PDFs, killzone/mission-pack terrain, Critical Ops, and Nemesis Operatives are all unread pointers, catalogued but not opened.

Nothing under `raw/` was created, modified, or deleted. No git commit, no push - Coordinator-owned per the standing guardrail.

Next step: **S1** (KT24 rules teaching docs under `games/kill_team_2024/rules/`), then **S2** (setup + killzones). See `L1_librarian.md` for the full inherited-documentation block.


## [2026-08-17] ingest | nemesis_ops_research L1 — Nemesis OCR + WarCom

Pages created: `warcom_nemesis_operatives_free`, `community_kt24_npo_aids`
Pages updated: `nemesis_operatives`, `index`, `glossary` (Nemesis Ops term stubs)
Key additions: OCR available outside git; eng.pdf deleted; `join_ops` renamed to `joint_ops`; no dossier datasheet paste into KB; WarCom free full profiles = none found.

## [2026-08-17] lint | nemesis_ops_ocr_spotcheck
Pages consulted: nemesis_operatives.md, games/kill_team_2024/nemesis_ops/*, OCR_Spotcheck_Matrix.md
Output filed: yes — confidence bumps on How-To / Custom_Builder / Mission_Packs (process+titles verified); tables remain out of git
Key additions: OCR page-order vs printed-footer offset noted; Ambull/Archivist titles vision-confirmed

## [2026-08-17] ingest | Necron painted-model photo sync

Pages created: `kill_team_necron_photos` (KB source); `raw/pointers/kill_team_necron_photos.md` (Implementer); `games/kill_team_2024/teams/hierotek_circle/Owned_Models_Inventory.md`

Pages updated: `necrons`, `glossary`, `overview`, `index`, `log`, `changelog`, `necron_lists_owner_notes`, `source_library`, `cryptek_conclave`, `canoptek_court`, `necrons_unit_index`, `inherited_docs_for_S3`; shipping KT Canoptek/Hierotek inventories, `_Owned_Teams_Inventory`, Joint Ops `NPO_Catalog`; 40K `Owned_Models_Inventory`, `Necron_Lists` (games + raw FOUNDATION), `Starter_250`, `Starter_500`, `Cryptek_Conclave`, `Canoptek_Court`

Key additions:
- Canoptek Circle loadouts locked: Tomb Crawlers 1 twin gauss reapers + 1 transdimensional isolator; Macrocyte Warriors 2 gauss scalpel + 1 tesla caster
- Hierotek roster: Technomancer (cloak), Apprentek, Despotek, 3 Immortal Guardians, 2 Plasmacytes — not Plasmancer, not Deathmarks
- Proxies: Apprentek → casual Plasmancer; Despotek → Immortal default / casual Royal Warden
- Base-size gap: Hierotek Plasmacytes KT ⌀25mm vs legacy 40K Plasmacyte ⌀28mm — likely not dual-legal
- Warrior mix: 10 models, mixed gauss flayer / gauss reaper; Scarabs 3 bases
- Hierotek `WIN_*.jpg` renamed on disk; photos remain outside git

## [2026-08-17] query | Plasmacyte 25–28mm base rings

Pages consulted: hierotek_circle/Owned_Models_Inventory, necrons Owned_Models_Inventory, Starter_250, Necron_Lists, necrons faction page
Output filed: no new analysis page — shopping to-do filed on inventories
Key additions: **To-do: purchase 25–28mm base rings** (two) for Hierotek Plasmacytes; do not rebase; KT stays legal on 25mm

## [2026-08-17] ingest | kt24_rules_quotes (L1 + L2)

Pages created: (none — shipping-only corpus)
Pages updated: [[glossary]] (KT24 quote exception row), [[kill_team_2024_core_rules]], [[index]], [[changelog]], [[log]]
Key additions: Target eligibility quote appendix (35 blocks); one-page HTML cheat sheet; Canoptek 5 + Plague 7 HTML datacards; AGENTS Sec 10 KT24 exception; community thanks on KT README; pointers updated; Full-Scan OCR-via-transcription note; owner lock 2026-08-17; no WarCom fetch; no git commit

## [2026-08-18] query | KT24 target-eligibility owner verification + Slice P patch sync

Pages consulted: [[kill_team_2024_core_rules]], [[glossary]], [[index]], shipping `games/kill_team_2024/rules/Target_Eligibility.md` (and cheat sheet), Patch_Manifest, Key_Concepts, Keyword_Glossary, Turn_Structure, Overview, Terrain_Basics, volkus, tomb_world

Output filed: no — verification pass on shipping quotes, not a new analysis page

Key additions:
- Quote appendix restored from owner Full-Scan pastes + Jun 17 update log + Jul 25 lite (35 → 52 verbatim blocks)
- Hierarchy kept: Full-Scan baseline; dated `eng_*` patches supersede; lite is intro (omission ≠ patch)
- Slice P: Patch_Manifest.md created; Heavy counteract + Guard; Severe Punishing/Rending; Volkus Door Fight / fire step; Tomb World Close Quarters Guard
- KB paraphrase only (Cover / Obscured / Heavy / Severe / Connected stubs); no rule dump
- No git commit, no push, no `raw/` binaries

## [2026-08-18] ingest | v0.5.0 — games/kill_team_2024 shipping → KB paraphrase

**Track:** living-docs snapshot + Librarian pass (user-gated commit+push; Coordinator git-lock waived for this request).

Pages created: `valid_target`, `kill_team_terrain`, `killzones_volkus_tomb_world`

Pages updated: `kill_team_2024_core_rules` (targeting subset `verified`; other Core stays draft), `turning_points`, `activations_apl`, `orders_conceal_engage`, `cover_kill_team`, `control_range_kill_team`, `injured_operatives`, `glossary`, `index`, `overview`, `changelog`, `log`, `ingest_procedure` (`version:` field only)

Key additions:
- **Flag then replace** L1 Wahapedia drafts — did not pretend they were always verified
- Hierarchy: Full-Scan baseline; dated `eng_*` patches supersede; Jul 25 lite is intro; omission ≠ patch
- Cover save = collect three / retain one normal success; same-feature cover vs obscured pick-one; Heavy on activation **or** counteract (does not prevent Guard)
- Setup pages paraphrase Terrain_Basics / Volkus Door Fight / Tomb World Close Quarters Guard
- No quote dump, no datacard statlines, no `raw/` binaries
- Teams / joint_ops / nemesis_ops / critical_ops remain index-only

Nothing under `raw/` written. Git commit/tag/push is the explicit user-gated snapshot for this pass.

## [2026-08-18] ingest | flowcharting_uml — UML 2.5 activity notation

**Track / slice:** flowcharting_uml / L1 (Librarian hat) + L2 promotion row.

Pages created: `uml_diagrams_org`, `flowcharting_uml_activity`

Pages updated: `glossary` (activity, action, decision node, guard, initial/final), `index`, `overview`, `changelog`, `log`

Key additions:
- Teaching paraphrase of uml-diagrams.org activity family (retrieved **2026-08-18**); no prose dump
- Credit: Kirill Fakhroutdinov / uml-diagrams.org About; not a Kill Team rules source
- House mapping: filled-circle start, rounded-rect actions, diamond decisions with guards on edges, bullseye end
- `system: multi_system` — project notation, not a KT rules term
- Shipping (S1/S2, logged here for the ingest): `docs/operations/Flowcharting.md`; cheat sheet restyle only

Nothing under `raw/` written. Coordinator one commit at track close; no push.

## [2026-08-18] ingest | 40k_warcom_quotes L1 — WarCom-free 11e Core

**Track / slice:** 40k_warcom_quotes / L1 (Librarian)

Pages created: [[warcom_free_core_rules_11e]]

Pages updated: [[glossary]] (rule-ID citation convention; OC vs KT 1" control range), [[ingest_procedure]], [[index]], [[overview]], [[kill_team_2024_core_rules]] (40K quote-policy row)

Key additions:
- Retrieval **2026-08-18**; local Core + July `eng_22-07_*` pointers; WarCom URL as discovery
- KB paraphrase only; shipping quotes in `games/warhammer_40k_11e/rules/Core_Rules_Quotes.md`
- Confidence `draft` until QA-Q

Implementer (not Librarian) updated `raw/pointers/*.md`. No binaries. No Codex dump.

## [2026-08-18] ingest | 40k_warcom_quotes L2 — promotions + QA

**Track / slice:** 40k_warcom_quotes / L2 (Librarian) after QA-Q / QA-T PASS

Pages updated: [[changelog]], [[log]], [[overview]], [[warcom_free_core_rules_11e]] (QA scope noted; remains `draft` — 112 quote bodies not owner-verified line-by-line)

Key additions:
- Promotion rows for `AGENTS.md` Sec 10 and `Core_Rules_Quotes.md`
- QA-Q: 01.01, 06.01, July sheet, stubs 15.02 / 23.01 / 24.05 PASS
- QA-T: teaching still playable; Codex wall holds; Necron Personal-wins pointer consistent
- No Core paraphrase contradictions requiring rewrite (cover **13.08**, Heavy **24.16**, OC **14.02**)


## [2026-08-19] policy | Wahapedia unit/stat when WarCom unavailable

Pages updated: [[wahapedia]], [[warhammer_community]], [[ingest_procedure]], [[index]], [[source_library]] (via `reference/Source_Library.md`), `AGENTS.md` Sec 10, `docs/operations/librarian_agent.md`, army lists `Army_List_250_Conclave` / `Army_List_500_V1_Conclave`

Key additions:
- Precedence: owned pack → WarCom when it publishes profile/amendment → **Wahapedia allowed** for datasheet stats when WarCom does not publish them
- Prefer `wh40k11ed`; flag `wh40k10ed` as edition-risk; retrieval date + `draft` until owned-pack cross-check; PDF wins on conflict
- Cloud egress for `wahapedia.ru` still pending (allowlist request filed 2026-08-19); VERIFY blanks not filled this pass

Nothing under `raw/` written.

## [2026-08-19] lint | Necron plain-language + rule ID pass

Pages updated: 20+ games files under `games/warhammer_40k_11e/armies/necrons/` (teaching guides, army lists, reference guides, Quick Reference, 65 unit research files); KB [[necrons]], [[cryptek_conclave]], [[canoptek_court]], [[reanimation_protocols]], [[power_matrix]], [[necron_warriors]], [[their_number_is_legion_potentiality_syphon_250]], [[necrons_unit_index]] (unchanged body)

Key additions:
- Plain-language rewrites for phase order, reanimation, Conclave/Court detachment rules, and army list play scripts
- Core rule ID cites on phases and mechanics: `08.05` (Command/reanimate), `10.02` (Shooting), `14.02` (OC), `15.01` (stratagems), `19.01` (attached units), `13.08` (cover), etc.
- Generic **At the table (plain language)** block added to all 65 unit research files; Necron Warriors research expanded with unit-specific tips

Fixes applied: none beyond prose clarity (no rules contradictions found)

Gaps: Necron army rule and detachment rules have no Core IDs (faction pack only); Power Matrix wording still `draft` pending pack line-check

## [2026-08-19] query | Their Number is Legion + Potentiality Syphon (250 Conclave)
Pages consulted: Army_List_250_Conclave, Reference_Guide_250/500_V1_Conclave, Reanimation_Protocols, Cryptek_Conclave; Wahapedia Warriors + Necrons hub (search retrieve 2026-08-19)
Output filed: yes - [[their_number_is_legion_potentiality_syphon_250]]
Also updated: [[glossary]] (two keyword stubs), [[index]], [[reanimation_protocols]], [[cryptek_conclave]] back-links

## [2026-08-20] query | Close Legion/Syphon open questions (WarCom primary)

Pages consulted: WarCom July 2026 update article; WarCom 40K downloads hub; WarCom Necrons FAQ PDF (assets); Wahapedia `wh40k11ed` Warriors + Necrons hub; owned pack via shipping guides

Output filed: yes — updated [[their_number_is_legion_potentiality_syphon_250]]

Also updated: [[reanimation_protocols]], [[glossary]], [[necron_warriors]], [[warhammer_community]], [[index]], shipping `Reanimation_Protocols.md`, `Reference_Guide_250_Conclave.md`, `Reference_Guide_500_V1_Conclave.md`, `units/research/Necron-Warriors.md`

Key resolutions:
- Legion + Syphon wording confirmed (pack shipping + Wahapedia); WarCom FAQ: Legion applies when RP activated by other rules
- No WarCom dataslate amendment to Syphon +1 / objective target found (2026-08-20)
- Characters: ordinary RP does not revive CHARACTER into bodyguard; WarCom July — character revive returns as unit of one

## [2026-08-21] query | Clarify heal-first on Legion/Syphon analysis

Pages consulted: [[their_number_is_legion_potentiality_syphon_250]], [[reanimation_protocols]], shipping Reanimation_Protocols.md

Output filed: yes — enhanced [[their_number_is_legion_potentiality_syphon_250]] (heal-first section + Geomancer worked example)

Also updated: [[index]]

## [2026-08-21] ownership | Plague Marines photo ID

Pages created: (none in KB — shipping inventory only)
Pages updated: shipping `games/kill_team_2024/teams/plague_marines/Owned_Models_Inventory.md` (+ ledger, starter roster, Death Guard stub)

Key additions: Photo-confirmed game-ready Plaguecaster, Icon Bearer, Champion, Fighter, Warrior; Biologus Putrifier as 40K character; Heavy Gunner / Bombardier not confirmed. Binaries stay outside git.

## [2026-08-21] ownership | Plague Marines Bombardier + Icon Bearer follow-up

Pages updated: shipping Plague Marines inventory, starter roster, laminate, teams ledger, team README

Key additions: **Bombardier confirmed** (stick grenade, bandolier, drum pack); Icon Bearer close-up reinforced. Only **Heavy Gunner** remains unconfirmed (6/7 KT slots).

## [2026-08-21] ownership | Plague Marines Heavy Gunner — 7/7 complete

Pages updated: shipping Plague Marines inventory (+ ledger, starter roster, laminate, README, Death Guard stub)

Key additions: **Heavy Gunner confirmed** (Plague Belcher). Full **7/7** KT roster game-ready. Provenance: **Kill Team Starter Set** (owner). Biologus Putrifier remains separate 40K ownership.

## [2026-08-21] fix | Volkus Condensed Stronghold on QR + event READY

Pages created: shipping `games/kill_team_2024/Event_Ready.md`
Pages updated: `volkus.md`, `volkus_QR.md`, Patch_Manifest Condensed Stronghold row, KT README, killzones README

Key additions: Condensed Stronghold = Blast/Torrent/x" Devastating also **Lethal 5+** when target wholly within stronghold on floor or fire step (per secondary). Learning-event pack-out marked **READY**.

## [2026-08-21] ownership | Event kit — Volkus scatter + Universal Equipment

Pages updated: shipping `games/kill_team_2024/Event_Ready.md`

Key additions: Pack-out includes baggie of **Volkus scatter terrain** with **Universal Equipment**.

## [2026-08-21] ownership | Intercessor Squad (used) — 40K + Angels of Death

Pages updated: shipping Space Marine + Angels of Death inventories, teams ledger, both READMEs

Key additions: Five Primaris Intercessor-family models (used; Black Templars paint; **not** played as BT). KT: Intercessor Sergeant, Assault Intercessor Warrior, Intercessor Warriors ×3. 40K: Intercessor bodies ×4 + Assault Intercessor ×1. Full Angels of Death team still incomplete.

## [2026-08-21] ownership | Lieutenant Titus (40K only)

Pages updated: Space Marine inventory + README; Angels of Death inventory (explicit KT exclusion)

Key additions: Ultramarines Lieutenant Titus painted and game-ready for **40K**. Owner: **wrong base for Kill Team** — must not fill Angels of Death Captain/leader.

## [2026-08-21] ops | learn_to_play_event L1 - Kommandos source pointer + shipping links

**Track / slice:** `learn_to_play_event` / L1

Pages created: [[kill_team_kommandos_teams_pdf]]

Pages updated: [[index]] (KT sources row + sources list)

Key additions: Pointer-only source page for eng_17-06 Kommandos Teams PDF; shipping playbooks/print bag under games/kill_team_2024 (no datacard dump in KB). Confidence draft until table-tested.

No git commit (user gate / IMP-09).

## [2026-08-21] ownership | Blood Ravens + AoD dual-use + Deathwatch separate

Pages updated: shipping Space Marine `Owned_Models_Inventory.md`, `Starter_250.md` honesty; Angels of Death inventory; Deathwatch `Owned_Models_Inventory.md` + README; KT `_Owned_Teams_Inventory.md`; `raw/pointers/40k_pics_ownership.md`, `raw/pointers/40k_codexes.md`

Key additions: Blood Ravens Firstborn photo ID (Tacticals 10+8, Devs 5, Terminator squads, Assault Terminators mixed, Captain, Terminator Chaplain, Veteran Sgt, Techmarine+Servitors, Whirlwind, Lt+2 spares); bikes/Attack Bike Legends; Varras non-SM; AoD Pics specialists dual-use Codex SM; Deathwatch ~11 primed separate identity; Codex path pointers (paid, no large quotes, 10e label / rotates).

## [2026-08-21] shipping | Space Marines starters 250-1000 owned BR paths

Pages updated: games/warhammer_40k_11e/armies/space_marines/ — Starter_250, Starter_500, Starter_750 (new), Starter_1000 (new), README, Owned_Models_Inventory

Key additions: Owned Blood Ravens Gladius paths at 250/500/750/1000 from MFM Marines v1.2; Terminator Chaplain claw = Storm Shield in game; Lt with Combi-weapon named; Deathwatch still excluded.

## [2026-08-21] shipping | Space Marines folder consistency pass

Pages updated: README, Quick_Reference_Play_Guide, Starter_250/500/750/1000, Oath_of_Moment, Gladius_Task_Force, Owned_Models_Inventory (re-check section), units/README

Key additions: Synced Tac 10+10 / flamers / Dev weapons / dual-legal AoD / Gravis 40K-only across faction docs; QR starter snapshot replaced unaudited TBD table with owned BR ladder.

## [2026-08-22] query | Astartes Servitors datasheet check (1000 list)

Pages consulted: shipping Starter_1000, Owned_Models_Inventory; WarCom Legends Space Marines PDF (ASTARTES SERVITORS WARHAMMER LEGENDS); Munitorum Field Manual Space Marines matched-play list (no Servitors entry); Wahapedia Astartes-Servitors page (draft cross-check)

Output filed: yes — updated Starter_1000, inventory, README, Unit_Index

Key resolutions:
- Datasheet name: **Astartes Servitors** (4 models — owned count matches)
- **Warhammer Legends** — not matched-play; do not cost into Gladius 1000
- Techmarine remains matched-play (MFM 55); field alone on the 1000 list
- Friendly: Mindlock / Servitor Retinue with Techmarine OK by agreement

## [2026-08-22] ingest | SM Matched vs Casual starters + Legends FM

Pages created: KB/sources/legends_field_manual_sm_2026_08.md, KB/units/astartes_servitors.md, KB/units/techmarine.md, KB/analyses/sm_matched_vs_casual_starters.md; shipping Starter_*_Matched.md, Starter_*_Casual.md, Starter_N shims

Pages updated: KB/factions/space_marines.md, KB/glossary.md, KB/index.md, KB/overview.md; shipping README, Owned_Models_Inventory; docs/handoffs/sm_matched_vs_casual/*

Key additions: Dual-path Blood Ravens Gladius lists (Matched no Legends / Casual combined tables with Servitors+Bikes+Attack Bike); Legends FM points draft retrieved 2026-08-22; Servitors PR #6 merged into track branch.

## [2026-08-22] lint | sm_matched_vs_casual L2 (light)

Issues found: Legends points still draft pending owned PDF glance; space_marines faction was stale stub (fixed to draft); Matched/Casual banners required on all list files.

Fixes applied: faction page rewrite; glossary Warhammer Legends / matched play / Astartes Servitors; index rows; analysis page; inventory→Casual pointers.

## [2026-08-22] ingest | SM 1st Company + Anvil detachment writeups

Pages created: games/.../First_Company_Task_Force.md, Anvil_Siege_Force.md; KB/detachments/first_company_task_force.md, anvil_siege_force.md; KB/analyses/sm_owned_detachment_fit.md

Pages updated: SM README, Gladius related links, KB faction space_marines, glossary, index

Key additions: Teaching guides for top two non-Gladius fits (Terminators / gunline); both confidence draft pending owned PDF glance; Oath vs Anvil +1 Wound stacking flagged.

## [2026-08-22] query | Owned SM points total (incl. Legends + Intercessors)

Pages consulted: Owned_Models_Inventory, AoD inventory, Starter Matched points (MFM Marines v1.2), Legends FM (2026-08-22), NR/public cross-check for Titus/Gravis/Heavy Int/Eliminator

Output filed: no

Key answer: Fieldable legal shelf ≈ **1785** pts (Codex SM + Legends + one Intercessor Squad); **~1875** if Captain Titus allowed (UM Epic Hero caveat). Incomplete Assault Int / Heavy Int / Eliminator not costed. Deathwatch excluded.

## [2026-08-22] query | SM + Sisters “brothers and sisters” soup in 11e

Pages consulted: (none in KB — no Sororitas army-construction page); WarCom army-building article (soup not returning); Imperial Agents Assigned Agents (11e Faction Pack summary via living refs, retrieved 2026-08-22)

Output filed: no

Key answer: Full Codex SM + Codex Adepta Sororitas soup is **not** back in 11e. Modular detachments stay within one Army Faction. Limited Sisters via **Assigned Agents** (Imperial Agents retinue caps) or play Agents as the army; full mixed force only casual/narrative by agreement.

## [2026-08-22] ingest | Adepta Sororitas ownership (metal + Celestian Insidiants)

Pages created: games/warhammer_40k_11e/armies/adepta_sororitas/README.md, Owned_Models_Inventory.md; kill_team_2024/teams/celestian_insidiants/Owned_Models_Inventory.md

Pages updated: celestian_insidiants/README.md, _Owned_Teams_Inventory.md, games/warhammer_40k_11e/README.md

Key additions: Metal Canoness / Battle Sisters / Seraphim + Celestian Insidiants declared owned but **unpainted**. Insidiants confirmed as official **11e Adepta Sororitas** datasheet (not KT-only). Counts/bases TBD. No soup with SM.

## [2026-08-23] query | Event feedback — Objectives/OC + Leader/Support deploy pointers

Pages consulted: Key_Concepts, Core_Rules_Quotes (14.01, 14.02, 19.01, 03.03), Necron/SM Quick_Reference, Reference_Guide_250_Conclave, objective_control, glossary

Output filed: yes — shipping guide updates + [[objective_control]] refresh (not a new analyses page)

Key answer: Control = sum OC of models on the objective terrain footprint (14.01/14.02); score VP per mission card. Leader + Support may join one bodyguard (19.01) and deploy as one coherency unit (03.03); 250 Conclave = Geomancer Support + Warriors.

## [2026-08-23] ingest | Chapter Approved Force Dispositions + Conclave Primaries 2-pagers

Pages created: games/warhammer_40k_11e/setup/Chapter_Approved_Force_Dispositions.md (+ print HTML); games/warhammer_40k_11e/armies/necrons/Cryptek_Conclave_Primary_Missions.md (+ print HTML)

Pages updated: Board_Setup, setup/README; Necron + SM army lists, starters, reference guides, QRs, detachment pages — **Force Disposition** callouts; glossary Force Disposition entry; Necron/SM READMEs

Key additions: Pre-game matching + Twists 2-pager; all five Priority Assets Primaries for Cryptek Conclave with keys; Force Disposition must be written on every list (starter-event failure mode).

## [2026-08-23] ingest | gw_community_content — GW IP guidelines + games/ footer pass

Pages created: KB/sources/gw_ip_guidelines.md; templates/Footer_Template_Gw_Print.md; templates/Gw_Print_Banner.html; docs/handoffs/gw_community_content/track_in.md; .cursor/rules/gw-unofficial-footer.mdc; scripts/apply_gw_ip_footer.py; scripts/apply_gw_ip_notice_md.py

Pages updated: AGENTS.md Sec 10; templates/README.md; docs/handoffs/README.md; 42 games/**/*.html; 107 Tier B games/**/*.md; KB/index.md; necrons/print/README.md; .cursor/rules (layer, kt24-quotes, 40k-core-quotes, 40k-armies-paraphrase); .cursor/skills/qa-slice/SKILL.md

Key additions: UNOFFICIAL banner + non-endorsement footer on all print HTML and datacard micro-footers; ## Games Workshop notice on player-facing shipping; quote-PDF policy locked (in-repo only); warhammer.com legal retrieved 2026-08-23.

## [2026-08-24] policy | The Warcode — GW obfuscation shipping scrub

Pages updated: games/the_warcode/ (5 content files + README); AGENTS.md v0.5.5; .cursor/rules/warcode-quotes.mdc; qa-slice skill; handoffs warcode_tactical_doctrine; reference/Warcode_Tactical_Doctrine_Plan.md addendum

Key additions: Extended GW proper-noun ban beyond That other game — Rawmallet / 39.876 / 39.9 in all `games/the_warcode/**` shipping; schema + lint aligned; L2 handoff re-run PASS.

## [2026-08-24] policy | The Warcode — GW proper noun obfuscation (KB)

Pages updated: KB/sources/warcode_rulebook_v087f.md, warcode_web_prelaunch_2026_08.md; KB/glossary.md (Warcode section + collision flags); KB/index.md, overview.md; KB/concepts/warcode_action_points.md, warcode_melee_lock.md

Key additions: Documented full GW naming ban for `games/the_warcode/**` shipping — Rawmallet / 39.9 / 39.876 / That other game obfuscation table on [[warcode_rulebook_v087f]]; Warcode KB collision flags and comparative bridges updated to use obfuscated forms, not GW product names.

## [2026-08-25] ingest | The Warcode — card/map enhancement pass (S1b + S8)

Pages created: raw/the_warcode/contract_cards_transcription.txt, protocol_cards_transcription.txt; KB/concepts/warcode_protocol_cards.md; games/the_warcode/rules/Contract_Cards_Reference.md, Protocol_Cards_Reference.md; docs/handoffs/warcode_tactical_doctrine/slices/S1b_card_research_note.md; scripts/export_warcode_xlsx_sidecars.py

Pages updated: Rulebook_Quotes.md (pp.24–25 closed); Board_Setup.md (D6 VP table); Scenarios_and_Events.md; Keyword_Glossary.md + Comparative_Glossary.md (full S8); Contracts_and_VP.md; First_Game_Walkthrough.md; Quick_Reference_Play_Guide.md; faction MDR/Dominium READMEs; Agentic review §12/§203 (local, gitignored); GATE Final; to_review.md; KB/sources/warcode_rulebook_v087f.md; warcode_contracts.md; KB/index.md

Key additions: Owner xlsx + map PNGs ingested; eight contract cards + twenty protocol rows; D6 objective layouts; VIP review PDF-only share policy; merge to main held on feature-Warcode.


Pages created: KB/sources/warcode_rulebook_v087f.md, warcode_web_prelaunch_2026_08.md; KB/concepts/warcode_action_points.md, warcode_ammo.md, warcode_overwatch.md, warcode_contracts.md, warcode_melee_lock.md; KB/factions/warcode_protagen_marines.md, warcode_ulfari.md, warcode_mdr.md, warcode_dominium.md

Pages updated: KB/index.md, glossary.md, overview.md, log.md

Key additions: Third system `the_warcode` in KB — beta v0.8.7-F source + pre-launch web; five core concepts; four faction pages (two playable draft, two marketing stubs); glossary Warcode section with collision flags to That other game / 40K; all pages `confidence: draft` or `stub`, paraphrase only.

## [2026-08-24] ingest | wd527_research — White Dwarf 527 (40K)

Pages created: KB/sources/white_dwarf_527.md; KB/setup/wd527_monthly_mission.md; KB/analyses/wd527_orks_vs_blood_angels_walkthrough.md; raw/pointers/white_dwarf_527.md; raw/white_dwarf_527/*.md; games/warhammer_40k_11e/rules/Wound_Roll_Reference.md; games/warhammer_40k_11e/setup/WD527_Monthly_Mission.md; setup/print/40k_wound_roll_reference.html; setup/print/40k_wd527_mission.html; docs/handoffs/wd527_research/

Pages updated: Key_Concepts, Board_Setup, setup/README, rules/README; Necron/SM QRs; 40k_first_game_core.html; reference/Source_Library.md; KB/index.md

Key additions: Tier-1.5 WD527 trust; Mission 38 Converging Ambition; S×T wound laminate from Core 05.02; BA vs Orks battle walkthrough.

## [2026-08-24] query | Da Jump 6″ vs 9″ coherency

Pages consulted: white_dwarf_527; designer_commentary_notes; Core_Rules_Quotes 03.03 / 20.04 / 24.09; WarCom Armageddon Ork datasheets article

Output filed: yes — clarified in KB/sources/white_dwarf_527.md, raw/white_dwarf_527/designer_commentary_notes.md + battle_report_notes.md, KB/analyses/wd527_orks_vs_blood_angels_walkthrough.md: 9″ = coherency span, 6″ = Ingress edge distance; Da Jump does not change coherency.

## [2026-08-25] enhance | wd527_shipping — games/ Commentary + system 2-pager + army guides

Pages updated: KB/sources/white_dwarf_527.md (shipping surfaces); KB/setup/wd527_monthly_mission.md; KB/analyses/wd527_orks_vs_blood_angels_walkthrough.md (date bump; still accurate); KB/index.md summaries

Pages created: none (enhance sync, not full ingest)

Key additions: Shipping track surfaces listed on source page (rules/setup Commentary, system QR, army guide pass). Trinity Hobby 2026-08-22 provenance. Distance triad teaching confirmed unchanged in analysis. Librarian did not write raw/.

## [2026-08-26] layout | Target Eligibility cheat sheet render refactor

Pages updated: games/kill_team_2024/rules/Target_Eligibility_Cheat_Sheet.html, print/kt_shared_target_eligibility.html, print/_html_to_pdf.py, print/README.md, rules/README.md, setup/Learn_to_Play_Print_Bag.md, templates/flowchart_html_classes.md, docs/handoffs/kt24_doc_followups/track_in.md

Key additions: Removed fixed 280px sidebar; full-width flowchart (page 1) + sequence strip and reference panel (page 2). Playwright sync from rules/ before PDF export. Decision logic and PDF cites unchanged.

## [2026-08-27] ingest | dataslate_0826 L0 — Aug 2026 balance package source stubs

Pages created: KB/sources/40k_aug_2026_balance_package.md, KB/sources/kt_aug_2026_balance_package.md, KB/sources/sm_codex_oct_2026_preview.md

Pages updated: none this slice (index rows deferred to L1 per brief)

Key additions: Owner lock restated — **no singular "Balance Dataslate" exists** for either 40K or Kill Team; both are packages of separately-versioned pieces (40K: Universal Rules Updates v1.1 + Faction Pack v1.2 + Munitorum Field Manual v1.3; KT: Core/killzone/mission-pack update logs + dated team online rules), plus a WarCom commentary article each. Codex: Space Marines October 2026 preview filed as a **separate product**, readiness/honesty only. All three pages `confidence: draft`, retrieval 2026-08-27. Librarian did not write `raw/`; did not git.

## [2026-08-27] enhance | dataslate_0826 L1 — KB sync after S1–S3 shipping

Pages updated: KB/units/necron_warriors.md (MFM v1.3: 10-model band 80→85); KB/factions/necrons.md (Phase 1 Conclave list 245→250 pts); KB/factions/space_marines.md (MFM v1.3 currency, no owned point change; Codex Oct preview pointer added); KB/sources/warcom_free_core_rules_11e.md (July v1.0 marked superseded by Aug v1.1); KB/sources/nemesis_operatives.md, KB/sources/kill_team_2024_core_rules.md (back-links to kt_aug_2026_balance_package); KB/glossary.md (four new draft terms + updated counts); KB/index.md (three new source rows + refreshed summaries/dates on five touched pages)

Pages created: none (enhance sync per `.cursor/skills/librarian-enhance/SKILL.md`; new sources were L0's job)

Key additions: **Necron Warriors** MFM v1.3 recost (80→85, ▲+5) synced from shipping slice S2c; **Space Marines** confirmed no owned-cost change from MFM v1.3 (slice S2d) plus a preview-readiness pointer to the October Codex (slice S2b). **Glossary:** Assault disembark move (`18.06`) / Shock disembark move (`18.07`) / Disembark move (context) from Universal Rules Updates v1.1; **Legendary Proxies** distinguished explicitly from Warhammer Legends (different mechanism — borrows a datasheet vs keeps its own). No contradictions found between shipping and prior KB claims; no glossary term conflict. Librarian did not write `raw/`; did not git.
