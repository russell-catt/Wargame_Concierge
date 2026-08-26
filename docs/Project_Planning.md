<!--
FILE: docs/Project_Planning.md
VERSION: v0.9.0 (2026-08-25)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer)

DOCUMENT_TYPE: Project Planning
PROJECT_NAME: Wargame_Concierge
PROJECT_PHASE: Pre-external-review
STATUS: Active

SOURCES:
  - README.md
  - AGENTS.md
  - games/README.md
  - docs/handoffs/README.md
  - docs/handoffs/v1_scaffold/track_in.md (constraints, model matrix, Preflight notes)
  - docs/handoffs/tomb_world_ownership/track_in.md (locked ownership decision, 2026-08-16)
  - docs/handoffs/warcode_tactical_doctrine/ (system #3 closed)
  - games/warhammer_40k_11e/armies/necrons/Necron_Lists.md (FOUNDATION - authoritative ownership)
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
| Phase | **Pre-external-review** — three systems onboarded |
| Snapshot | **v0.9.0** (2026-08-25) |
| Systems | 40K 11e · Kill Team 2024 · **The Warcode** (free beta v0.8.7-F) — [`../games/README.md`](../games/README.md) |
| Closed tracks | Indexed in [`handoffs/README.md`](handoffs/README.md) — includes `warcode_tactical_doctrine`, WD527 research/shipping, KT scaffold / quotes / Nemesis, `v1_scaffold`, Tomb World ownership |
| Next milestone | **External user review and critique** of shipping teaching content (and VIP review PDF for Warcode, emailed separately) |
| KB | Living; Librarian enhance passes after shipping tracks |
| Git | Coordinator sole git owner except explicit user-gated commit+push |
| Live rollup | [`handoffs/README.md`](handoffs/README.md) |

---

## 2. Locked decisions

### Repository and hosting

| Decision | Detail | Decided |
|----------|--------|---------|
| **Repository** | **Private** GitHub repo `russell-catt/Wargame_Concierge` | 2026-08-16 |
| Location | `C:\Personal\Personal_Projects\Wargame_Concierge` | 2026-08-16 |
| Git root | **Standalone** - its own `.git`, not a `Personal_Projects` monorepo leaf | 2026-08-16 |
| Git ownership | Coordinator alone commits. Subagents never commit or push unless user-gated | 2026-08-16 |

Private is a deliberate choice, not a default. The unit research corpus is personal structured notes derived from material the owner holds; keeping the repo private is part of the copyright posture below.

### Scope

| Decision | Detail |
|----------|--------|
| **System #1** | **Warhammer 40,000, 11th Edition** — Necrons (learning) + Space Marines (opposing pile) |
| **System #2** | **Kill Team 2024** — onboarded under `games/kill_team_2024/` |
| **System #3** | **The Warcode** — onboarded under `games/the_warcode/` (RedMakers free beta; GW proper-noun ban in shipping) |
| Game-agnostic by design | `games/` holds one subtree per system; scaffold for the **next** system |
| Out of scope for v0.9 | Web app / army builder; automated list validation; selling the project; MDR/Dominium datasheets until RedMakers publish |

### Copyright and sourcing

| Decision | Detail |
|----------|--------|
| **No GW binaries in git** | No GW PDFs or official images. Enforced by `.gitignore` |
| **Warcode free-beta exception** | PDF + OCR/xlsx/map sidecars may live under `raw/the_warcode/` (not GW) |
| External libraries | `C:\Personal\40K`, `C:\Personal\Kill Team` stay **outside** the repo — path pointers only |
| Writing style | **Teaching paraphrase** in `KB/` and `docs/` |
| **Scoped verbatim quotes** | KT24 → `games/kill_team_2024/`; 40K WarCom-free Core → `games/warhammer_40k_11e/rules|setup/`; Warcode beta → `games/the_warcode/rules|setup|factions/` |
| **Warcode shipping naming** | Never GW proper nouns in `games/the_warcode/**` — That other game / Rawmallet / 39.9 / 39.876 |
| **GW unofficial footers** | Required on 40K / KT print HTML and player-facing army shipping — see `templates/Footer_Template_Gw_Print.md` |
| Citation | Every rules claim names where it can be checked, **with a retrieval date** |

### Living web references

11th Edition and living web sources move. Anything drawn from them carries the date it was read.

| Reference | URL | Use |
|-----------|-----|-----|
| Warhammer Community | <https://www.warhammer-community.com/en-gb/> | Official rules updates, FAQs, errata, balance dataslates |
| Wahapedia | <https://wahapedia.ru/> | Consolidated rules and datasheet lookup when WarCom does not publish profiles |
| The Warcode pre-launch | <https://pre-launch.thewarcode.com/> | Marketing / VIP context (secondary to free beta PDF) |

**Patches happen.** Cross-check owned PDFs before a real game. Wahapedia is convenience and can lag.

### Architecture and process

| Decision | Detail |
|----------|--------|
| Knowledge pattern | Karpathy "LLM Wiki", adapted to wargames. `raw/` → `KB/` → shipping `docs/` + `games/` |
| Middle layer is `KB/` | **Never** `wiki/` |
| Schema source of truth | [`../AGENTS.md`](../AGENTS.md); day-to-day in [`operations/librarian_agent.md`](operations/librarian_agent.md) |
| Librarian ownership | Librarian owns all `KB/` writes, never writes `raw/`, and never commits |
| Documentation framework | Rising Tide in `docs/` / `games/` / root; YAML in `KB/`. **Do not stack** |
| Workflow | Multi-slice, multi-agent playbook with Tier 0–3 checks |
| Obsidian | Repo root is a vault |
| Encoding | UTF-8, no BOM |

---

## 3. Confirmed Necron ownership - 2026-08-16

This is the model pool every Necron list, starter, and teaching document must be written against. Confirmed by the owner on **2026-08-16**. The authoritative record is the FOUNDATION section of [`../games/warhammer_40k_11e/armies/necrons/Necron_Lists.md`](../games/warhammer_40k_11e/armies/necrons/Necron_Lists.md); the tables below restate it and lose to it in any disagreement.

### Game-ready - on the table now

**Kill Team: Tomb World** - owned, assembled, painted, playable:

| Models | Count | State | Notes |
|--------|-------|-------|-------|
| Cryptek Geomancer | 1 | **Assembled, painted - game ready** | Tomb World |
| Canoptek Tomb Crawlers | 2 | **Assembled, painted - game ready** | Tomb World |
| Canoptek Macrocytes | 5 | **Assembled, painted - game ready** | Tomb World |
| Necron Warriors | 10 (1st squad) | **Assembled, painted - game ready** | Tomb World |
| Canoptek Scarab Swarms | 3 (1st set) | **Assembled, painted - game ready** | Tomb World |
| Hierotek Circle Kill Team (used set) | 1 set | **Assembled and painted - game ready** | An *additional* game-ready set. 40K datasheets **TBD pending owner photos** |

### Build before play - owned, still on sprue

| Models | Count | State | Notes |
|--------|-------|-------|-------|
| Necron Warriors | 10 (2nd squad) | **Purchased, unassembled, unpainted** | Assemble-to-expand beyond the Tomb World squad |
| Canoptek Scarab Swarms | 3 (2nd set) | **Purchased, unassembled, unpainted** | Assemble-to-expand beyond the Tomb World swarms |
| Immortals | 5 (1 squad) | **Purchased, unassembled** | Already owned - do **not** list as a future purchase without adjusting shopping totals |

### Ownership totals

| Models | Total | Split |
|--------|-------|-------|
| Necron Warriors | **20** | 10 game-ready (Tomb World) + 10 on sprue |
| Canoptek Scarab Swarms | **6** | 3 game-ready (Tomb World) + 3 on sprue |
| Cryptek Geomancer | 1 | Game-ready |
| Canoptek Tomb Crawlers | 2 | Game-ready |
| Canoptek Macrocytes | 5 | Game-ready |
| Immortals | 5 | On sprue |
| Hierotek Circle Kill Team | 1 set | Game-ready, datasheets TBD |

Three consequences that content must respect:

- **Tomb World is the preferred learning baseline.** It is owned, painted, and playable today, so early teaching content and starter lists are built on it rather than gated behind assembly or the Hierotek photo ID.
- **Build-before-play applies only to the extras.** The second Warriors squad, the second Scarab set, and the Immortals are assemble-to-expand. They are owned, they are not blockers, and no list may count them as on the table until they are built.
- **Owned models are not shopping targets.** Any expansion or collection blueprint must tag the Tomb World contents, the extra Warriors and Scarabs, and the Immortals as already purchased so phase totals do not double-count them. Do not re-shop owned kits.

### Correction: the "Tomb World not owned" claim was erroneous

| Field | Value |
|-------|-------|
| Prior claim | Kill Team: Tomb World was recorded as **superseded and historical, not current ownership** - introduced in the Preflight slice and propagated through `v1_scaffold` into this document, `reference/`, the army docs, and `KB/` |
| Reality | **The owner owns Kill Team: Tomb World and its units are game-ready.** The supersession was never true, so there is nothing here to keep as history beyond this correction note |
| Corrected in | Track [`tomb_world_ownership`](handoffs/tomb_world_ownership/track_in.md), 2026-08-16 - FOUNDATION re-sync at S1, army docs and starters at S2, this document and the distilled context at S3, `KB/` at L1 and L2 |
| Standing instruction | Do not reintroduce "Tomb World not owned", "Tomb World superseded", or "only the Hierotek Circle set is game-ready" in any form. Any older draft that says so is wrong and predates this correction |

### Authoritative order for ownership facts

When copies disagree, the higher row wins. This ladder governs **ownership only** - for points, the owned Munitorum Field Manual v1.2 is authoritative and FOUNDATION's figures are stale.

| Rank | Source |
|------|--------|
| 1 | [`../games/warhammer_40k_11e/armies/necrons/Necron_Lists.md`](../games/warhammer_40k_11e/armies/necrons/Necron_Lists.md) - project FOUNDATION |
| 2 | [`../raw/Necron_Lists.md`](../raw/Necron_Lists.md) and the external source `C:\Personal\40K\rules\Necron_Lists.md` |
| 3 | Army docs under [`../games/warhammer_40k_11e/armies/necrons/`](../games/warhammer_40k_11e/armies/necrons/) |
| 4 | [`../KB/`](../KB/) pages |

### Space Marine ownership

**Not yet inventoried.** The son's force comes from a pile of older models already in the house, which is why legacy and Firstborn datasheets stay in scope for the S6 research pass. An inventory worksheet is part of slice S5; provisional lists before then are theoretical and should say so.

---

## 4. Open items

### Hierotek Circle photo identification - OPEN

| Field | Value |
|-------|-------|
| Status | **Open**, blocked on owner photos |
| Raised | Preflight, 2026-08-16 |
| Blocks | Which 40K datasheets the Hierotek models represent. It does **not** block early games - the Tomb World force is owned, game-ready, and fully identified |
| Owner action | Post photos of the assembled set |
| Then | Librarian ingests the identification; the Necron starters pick Hierotek up as an expansion option |
| Interim handling | Placeholder subsection in the Necron list; no starter list may claim a specific Hierotek datasheet until this closes. Starters lead with Tomb World in the meantime |

Still worth closing, but no longer critical path. It dropped from blocker to nice-to-have once Tomb World was confirmed owned and game-ready.

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
| **Preflight** | Necron ownership patched into `C:\Personal\40K\rules\Necron_Lists.md` at source; Hierotek Circle TODO opened. Also marked Tomb World superseded - **that part was erroneous and has since been reverted** (Sec 3) |
| **Ownership re-sync** | `raw/Necron_Lists.md` re-aligned to the armies and `C:\Personal\40K` copies; inventory/README/KB source notes bumped. Treated Tomb-World-owned content as drift - **also erroneous, corrected in the `tomb_world_ownership` track** |
| **S0** | Repo bootstrap: `git init` (no commits), Rising Tide `templates/`, adapted playbook, `docs/handoffs/` with the `v1_scaffold` track, `.gitignore`, `raw/` and `KB/` skeletons |
| **L0** | Karpathy KB bootstrap: `AGENTS.md` schema, `librarian_agent.md`, all six KB core pages, typed-directory guides, glossary seeded with four terms, `.obsidian/` vault |
| **S1** | Core Rising Tide documents: `START_HERE.md`, `README.md`, this file and its siblings under `docs/`, `Game_System_Scaffold.md`, and the `reference/` seed context |
| **`tomb_world_ownership` S1** | FOUNDATION restored in all three `Necron_Lists.md` copies: Tomb World owned and game-ready, 20 Warriors / 6 Scarab Swarms totals, shopping double-counts removed |
| **`tomb_world_ownership` S2** | Army docs, owned-models inventory, the 250- and 500-point starters, and the quick-reference play guide rebuilt on the Tomb World force |
| **`tomb_world_ownership` S3** | This document, [`../reference/Distilled_Project_Context.md`](../reference/Distilled_Project_Context.md), and [`../raw/pointers/necron_lists_import.md`](../raw/pointers/necron_lists_import.md) realigned to FOUNDATION |

---

## 6. Immediate next actions

## 5. Next actions

**Primary (v0.9.0):** **External user review and critique** — share selected shipping guides (and the Warcode VIP review PDF by email, not via GitHub) and collect feedback.

| # | Action | Owner |
|---|--------|-------|
| 1 | External review pass on teaching content (40K / KT24 / Warcode) | Owner + reviewers |
| 2 | First table tests: KT24 Volkus/3e Starter; Warcode First Game Walkthrough; 40K Conclave | Owner |
| 3 | Optional: L1 Warcode unit KB pages; MDR/Dominium when beta publishes | Later track |
| 4 | Optional: ingest remaining Core chapters / team trees into KB when needed | Librarian |
| 5 | Playbook 26 dead links remain a known issue — do not rewrite Sec 17–18 | Later cleanup |

### Known defects carried forward

| Defect | Detail | Suggested owner |
|--------|--------|-----------------|
| Dead links in the playbook | `operations/multiagent_coordinator_strategy.md` has 26 relative links inherited from the `daily_report` repo that point at directories which do not exist here. The prose is authoritative; the links are not | A later cleanup slice |
| UTF-16 encoded files | Some early README / slice artifacts may still be UTF-16LE against the UTF-8-no-BOM rule | Coordinator |
| Points drift between FOUNDATION and army docs | FOUNDATION prices ownership; MFM prices costs — keep the distinction explicit | Points-verification when needed |

---

## Change Log

- v0.9.0 (2026-08-25): Three systems onboarded (Warcode); copyright/sourcing refreshed; phase **pre-external-review**; next milestone external critique.
- v0.5.0 (2026-08-18): Project-wide semver snapshot (x.y.z). Status: KT24 rules/reference landed; tags `v0.1.0` / `v0.5.0`; Coordinator git owner except this user-gated commit+push.
- v1.1 (2026-08-16): Ownership correction, track `tomb_world_ownership` slice S3. Sec 3 rewritten against FOUNDATION: Kill Team: Tomb World is **owned and game-ready** (Geomancer, 2 Tomb Crawlers, 5 Macrocytes, 10 Warriors, 3 Scarab Swarms), with the second Warriors squad, second Scarab set, and Immortals owned on sprue, and totals of 20 Warriors and 6 Scarab Swarms. Removed the "Superseded: Kill Team: Tomb World" section and replaced it with a correction note recording that the prior claim was erroneous. Added the authoritative order for ownership facts. Downgraded the Hierotek Circle photo ID from blocker to open-but-non-blocking. Refreshed current status, completed-to-date, and next actions for the current track.
- v1.0 (2026-08-16): Initial planning record - locked decisions, confirmed 2026-08-16 Necron ownership, Tomb World superseded, Power Matrix resolved to the Canoptek Court detachment rule, Hierotek Circle photo ID open, next actions. Created in slice S1. *(The Tomb World supersession recorded here was erroneous - see v1.1.)*

## Attribution

- Project: Wargame_Concierge
- Maintainer: Russell Catt
- Structured using the Rising Tide framework

## Rising Tide Notes

- This document follows Rising Tide documentation standards.
- Keep the receipts. Make AI show their work.
- A decision recorded without its reasoning is a decision that gets re-litigated.
