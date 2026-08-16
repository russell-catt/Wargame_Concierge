# L1 - Librarian report (first ingest)

- **Status:** Resolved - Implemented (awaiting QA)
- **Track / slice:** v1_scaffold / L1 (Tier 0 - knowledge entrance)
- **Date:** 2026-08-16
- **Depends:** S2 Resolved - Implemented (now marked **Done** in `track_in.md`)
- **Sources:** `raw/Necron_Lists.md`, `reference/Source_Library.md`, `raw/pointers/*.md` (8 stubs) - all read in full. Wahapedia and Warhammer Community **registered, not retrieved**
- **Paths touched:** `KB/**`, `docs/handoffs/v1_scaffold/slices/L1_*.md`, `docs/handoffs/v1_scaffold/track_in.md`
- **`raw/` untouched:** YES
- **Promotion:** none into `docs/` or `games/`. Two `KB/changelog.md` rows added (one no-promotion record, one rules correction)
- **Lint:** PASS - 0 broken wikilinks, 0 missing frontmatter, 0 missing confidence, 0 UTF-16 files
- **Commit:** none by this slice. **See the mid-slice commit finding below - a commit landed anyway**

---

## Model waiver

| Field | Value |
|-------|-------|
| **Locked model** (per [`track_in.md`](../track_in.md)) | `claude-fable-5-thinking-high` |
| **Availability** | **Unavailable at dispatch** |
| **Model actually used** | `claude-opus-5-thinking-high` |
| **Basis** | Same-family substitute (Claude, thinking-high tier) |
| **Authorized by** | Coordinator, at dispatch |

Recorded in the `track_in.md` waiver table as the third waiver on this track and the **second consecutive one for the Librarian role**. `claude-fable-5-thinking-high` has not been available at any dispatch so far, which makes it a locked model in name only. QA should still run `gpt-5.6-sol-medium` - a different family from the substitute, satisfying playbook Sec 18.7.

---

## What was ingested

| Source | Class | Read? | KB page |
|--------|-------|-------|---------|
| `raw/Necron_Lists.md` | Owner's own notes | **In full** | `KB/sources/necron_lists_owner_notes.md` |
| `reference/Source_Library.md` | Project catalog | **In full** | `KB/sources/source_library.md` |
| `raw/pointers/*.md` (8 stubs) | Pointer stubs | **In full** | `KB/sources/local_library_pointers.md` |
| Wahapedia | Living web reference | **No** | `KB/sources/wahapedia.md` (registration only) |
| Warhammer Community | Living web reference | **No** | `KB/sources/warhammer_community.md` (registration only) |

The last two are deliberate. Nothing was fetched, so nothing may carry a content retrieval date. Both pages say so at the top and are marked `confidence: stub`. Inheriting a date from a page that only registered a URL would be a lie about when a claim was checked - exactly the failure the retrieval-date rule exists to prevent.

---

## Pages created (17)

### KB sources (5)

| Path | Confidence |
|------|-----------|
| `KB/sources/necron_lists_owner_notes.md` | draft |
| `KB/sources/source_library.md` | verified (the *catalog* is verified, not its targets) |
| `KB/sources/local_library_pointers.md` | verified (same distinction) |
| `KB/sources/wahapedia.md` | stub |
| `KB/sources/warhammer_community.md` | stub |

### KB entity pages (10)

| Path | Confidence | Note |
|------|-----------|------|
| `KB/factions/necrons.md` | draft | Ownership, both detachment paths, the awkward collection shape |
| `KB/factions/space_marines.md` | stub | No source read; no inventory exists |
| `KB/detachments/canoptek_court.md` | draft | Power Matrix, expansion path, not currently playable |
| `KB/detachments/cryptek_conclave.md` | draft | Scientific Schemes; the cheaper path from owned models |
| `KB/detachments/gladius_task_force.md` | stub | Project decision only |
| `KB/concepts/power_matrix.md` | draft | **The correction** |
| `KB/concepts/reanimation_protocols.md` | unverified | Necron army rule |
| `KB/concepts/oath_of_moment.md` | unverified | Space Marine army rule |
| `KB/concepts/objective_control.md` | unverified | Core rules; S3 owns verification |
| `KB/analyses/inherited_docs_for_S3.md` | verified | The classification is verified, not the claims |

### Handoff artifacts (2)

`docs/handoffs/v1_scaffold/slices/L1_brief.md` (retro-filled, matching the L0 precedent) and this report.

## Pages updated (6)

| Path | Change |
|------|--------|
| `KB/glossary.md` | Power Matrix resolved; expanded 4 terms to 32; sectioned by scope; verification queue and deprecated list rewritten |
| `KB/index.md` | Rows for all 15 new pages; typed sections no longer empty; status header rewritten |
| `KB/overview.md` | Ownership detail, current-state metrics, a "Resolved in L1" section, rewritten gaps |
| `KB/log.md` | Ingest entry `## [2026-08-16] ingest \| L1 ...` appended |
| `KB/changelog.md` | Two rows and a paragraph explaining why L1 promoted nothing |
| `docs/handoffs/v1_scaffold/track_in.md` | S2 **Done**, L1 status, L1 waiver row, git state, defect table |

**Total: 17 created, 6 updated.** [`KB/ingest_procedure.md`](../../../../KB/ingest_procedure.md) expects 5-15 pages for a meaningful ingest; this ran slightly above that because the source named two full detachments and both army rules.

---

## The Power Matrix correction

The substantive finding of this slice.

**What L0 said.** `KB/glossary.md` seeded **Power Matrix** with an explicit warning that its game system was unresolved - it might belong to *Kill Team* rather than Warhammer 40,000, because the owner's Hierotek Circle is a Kill Team box. L0 told downstream slices not to build 40K content on it and queued it for L1/S4.

**What L1 found.** Two independent sources already inside the repo name it as a 40K detachment rule:

| Source | Evidence |
|--------|----------|
| `raw/Necron_Lists.md` | Its strategic-matrix table gives "**The Power Matrix**" as the **main detachment rule of the Canoptek Court**, in a comparison of two 40K detachments at 40K points values |
| `docs/Game_System_Scaffold.md` (S1) | Its generic-to-40K vocabulary mapping uses "Power Matrix, the Canoptek Court detachment rule" as the worked example of a sub-list rule package |

Different slices, different material, same conclusion, no connection to Kill Team.

**Why L0 was wrong, and why it was not careless.** The owner owns a Kill Team box *and* plays Necrons in 40K; both involve Crypteks. L0 was seeding vocabulary from general familiarity with no source in front of it, saw "Cryptek resource mechanic" and "Hierotek Circle" in the same note, and joined them. **The flag is the reason this cost one ingest instead of surfacing halfway through S4.** Writing the uncertainty down loudly worked exactly as intended.

**What is now settled, and what is not:**

| Claim | Status |
|-------|--------|
| A Warhammer 40,000 term, not Kill Team | **Resolved** |
| The Canoptek Court detachment rule | **Resolved** |
| Grants hit re-rolls tied to controlled territory | `draft` - owner's paraphrase, single source |
| What "controlled territory" means; whether melee, shooting, or both | **Open** - needs the Necrons faction pack |

Applied in five places so they cannot drift apart: `concepts/power_matrix.md` (full record), `glossary.md` (entry rewritten **and** the old claim added to the deprecated list), `detachments/canoptek_court.md`, `sources/necron_lists_owner_notes.md`, `overview.md`. The Hierotek Circle and Power Matrix are now formally unrelated - the set stays an open identification question, but it is not evidence about any rule.

---

## Ownership facts captured

Confirmed 2026-08-16, consistent across `raw/Necron_Lists.md` FOUNDATION, the S2 inventory, and `reference/Source_Library.md`:

| Item | Qty | State |
|------|-----|-------|
| Necron Warriors | 10 (1 squad) | Purchased, **unassembled** |
| Canoptek Scarab Swarms | 3 | Purchased, **unassembled** |
| Immortals | 5 (1 squad) | Purchased, **unassembled** |
| Hierotek Circle Kill Team (used) | 1 set | Assembled + painted, **game ready** - datasheets **TBD pending photos** |
| Kill Team: Tomb World | - | **Not owned** - superseded historical reference |

Filed on `KB/factions/necrons.md`, `KB/analyses/inherited_docs_for_S3.md`, and `KB/overview.md`.

The observation worth carrying: **the only table-ready models are the unidentified ones, and the only identified models are unassembled.** Both halves are blocked for opposite reasons, and the photo ID is by far the cheaper unblock.

---

## Findings for the Coordinator

### Finding 1 - the agent editor writes UTF-16LE (fixed, but it will recur)

**Every markdown file written through the editor in this environment landed as UTF-16LE without BOM**, despite UTF-8 being an explicit slice constraint. This affected all 22 files L1 touched, including UTF-8 files that were merely edited - `KB/index.md` and `KB/glossary.md` were converted to UTF-16 by the act of editing them.

Detected by byte-checking rather than by reading, because the files *look* correct through the editor. The visible symptom was in git: `git show --stat` reported the new pages as `Bin 0 -> 8928 bytes`.

All 22 were converted to UTF-8 without BOM as the final step. A repo-wide scan now finds **0** UTF-16 markdown files.

**This will hit S3, S4, S5, and S6 identically.** Recommended exit check for every slice that writes markdown:

```powershell
Get-ChildItem $root -Recurse -Filter *.md -File |
  Where-Object { $_.FullName -notmatch '\\\.git\\' } |
  ForEach-Object {
    $b = [System.IO.File]::ReadAllBytes($_.FullName)
    if (($b | Select-Object -First 200 | Where-Object { $_ -eq 0 }).Count -gt 0) { $_.FullName }
  }
```

Recorded in the `track_in.md` defect table as a standing item.

### Finding 2 - a commit landed mid-slice, and it was not the Librarian

`be34342`, timestamped **2026-08-16 18:45**, was created **while L1 was running**. It contains exactly five files - the `KB/sources/*.md` pages L1 had just written - and reuses the S2 commit message, "Import Necron lists and scaffold 40K game tree (S2)."

**L1 did not commit.** No git write command was issued at any point; the working tree was left dirty as the contract requires. The commit was made by another actor with the repo open.

Two consequences:

- The S2 commit message now covers L1 content, and `10f7008` and `be34342` carry identical messages for different changes
- Those five blobs were committed while still UTF-16LE, so git recorded them as **binary**. They now show as modified because L1 converted them to UTF-8

Recommend re-committing with an accurate message once QA passes. Flagged in `track_in.md` under Git state.

### Finding 3 - the L0 UTF-16 defect list is stale, and `track_in.md` itself was on the wrong side of it

L0 listed five UTF-16LE files. **All five are UTF-8 today**, including `raw/pointers/README.md` - which L1 did not touch, and confirms was already UTF-8 rather than needing the authorization L0 warned about.

`docs/handoffs/v1_scaffold/track_in.md` **was** UTF-16LE and was never on the list. L1 converted it, which is why its diff is whole-file rather than a few rows. Flagged rather than done quietly, because a whole-file diff on the Coordinator's own tracking document should not be a surprise.

### Finding 4 - one filename deviates from the schema

`KB/analyses/inherited_docs_for_S3.md` keeps the capitalised `S3` because the brief named the file explicitly. [`AGENTS.md`](../../../../AGENTS.md) Sec 7 requires lowercase `snake_case` in `KB/`. It is the only such deviation, it is annotated in `KB/index.md`, and it is recorded here so L2 lint scores it as a known exception rather than a fresh defect. Renaming to `inherited_docs_for_s3.md` is a one-line fix if the Coordinator prefers the schema to win.

---

## Tier 1 self-check

| # | Criterion | Result | Evidence |
|---|-----------|--------|----------|
| 1 | All 15 KB pages created | PASS | `Test-Path` on each; see `L1_brief.md` Tier 1 commands |
| 2 | Frontmatter on every KB page | PASS | 21 non-README pages, all start `---` |
| 3 | `confidence` on every KB page | PASS | 21/21 |
| 4 | Confidence honest, not inflated | PASS | **0** game terms and **0** rules pages marked `verified`; the 3 `verified` pages are a catalog, a pointer list, and a classification |
| 5 | Power Matrix resolved as the Canoptek Court 40K rule | PASS | 5 pages agree; 0 pages still call the attribution unresolved |
| 6 | Old Kill Team claim on the deprecated list | PASS | `glossary.md` deprecated table |
| 7 | Glossary expanded for S3 alignment | PASS | 4 terms to 32, sectioned by scope |
| 8 | Every new page has an index row | PASS | 15 rows across 5 typed sections |
| 9 | Index confidence matches page frontmatter | PASS | checked row by row |
| 10 | Log entry dated 2026-08-16 | PASS | `## [2026-08-16] ingest \| L1 - first real ingest ...` |
| 11 | Changelog rows added | PASS | 2 rows plus a no-promotion rationale |
| 12 | Wikilinks resolve | PASS | 0 broken. The 2 hits a naive regex returns are the `[[related_page]]` and `[[wikilink]]` format examples inherited from L0; L1 backticked both, so a code-span-aware lint reports 0 |
| 13 | L0's forward links now resolve | PASS | `[[necrons]]` and `[[space_marines]]` exist |
| 14 | Ownership facts match Preflight | PASS | 3 repo documents agree |
| 15 | **`raw/` untouched** | PASS | 11 files, sizes and timestamps unchanged; `git status` shows nothing under `raw/` |
| 16 | No GW binaries | PASS | 0 files matching `*.pdf,*.webp,*.png,*.jpg,*.jpeg,*.gif` |
| 17 | No verbatim rules text | PASS | teaching paraphrase throughout; points figures cited to the owner's notes and flagged for Munitorum cross-check |
| 18 | All files UTF-8 | PASS | **after conversion** - see Finding 1. 0 UTF-16 markdown files repo-wide |
| 19 | No commit by this slice | PASS | no git write command issued - **but see Finding 2** |
| 20 | Nothing promoted to `docs/` or `games/` | PASS | `changelog.md` states why |

---

## Lint

| Check | Result |
|-------|--------|
| Broken wikilinks in `KB/` | **0** |
| Missing frontmatter | **0** of 21 |
| Missing `confidence` | **0** of 21 |
| Index rows missing for a page | **0** |
| Confidence drift between page and index | **0** |
| Rules claims without a verification route | **0** |
| UTF-16 markdown files repo-wide | **0** (22 converted) |
| Orphan pages | **0** - every entity page is reachable from `index.md` and linked from at least one sibling |
| Filename schema deviations | **1**, known and annotated (Finding 4) |

Not run: contradiction and edition-drift checks across shipping content. Those belong to **L2** and need S3-S6 content to exist first.

---

## Blockers

None blocking S3. S3 can start immediately by opening `raw/pointers/rules_core.md`.

Four threads carried rather than resolved:

| Thread | Status | Owner |
|--------|--------|-------|
| **Hierotek Circle photo ID** | Still open from Preflight. Blocks the first playable game and Phase 1 of both Necron paths | User photos -> S4 |
| **Space Marine collection audit** | Inventory worksheet is empty. Blocks all S5 content | User -> S5 prep |
| **Wahapedia `wh40k10ed` URL path** | Faction URLs sit on a 10th Edition path while described as 11e. Edition-drift risk on every future cross-check | S3 |
| **Owned PDFs possibly superseded** | Nothing records when they were downloaded, so "has a dataslate landed since?" is currently unanswerable | S3 |

The `Power Matrix` attribution thread from L0 is **closed**. Its wording remains open under the Hierotek-independent verification queue in `KB/glossary.md`.

---

## Inherited documentation (paste-ready for the S3 brief)

> **Tier 0 - Knowledge ready: PASS.** The KB now holds 5 sources and 15 entity pages. Every path below is real.
>
> **Read before starting:**
> - [`KB/analyses/inherited_docs_for_S3.md`](../../../../KB/analyses/inherited_docs_for_S3.md) - **start here.** Sorts every fact L1 produced into *stable enough to teach*, *named but unverified*, and *do not ship*. It also maps each open question to the pointer stub that answers it.
> - [`AGENTS.md`](../../../../AGENTS.md) - schema source of truth. Entity types, frontmatter, naming, copyright.
> - [`KB/index.md`](../../../../KB/index.md) - master catalog, now populated.
> - [`KB/glossary.md`](../../../../KB/glossary.md) - **32 terms, sectioned by scope**, which is the working surface the shipping `Keyword_Glossary` draws from.
> - [`KB/concepts/objective_control.md`](../../../../KB/concepts/objective_control.md) - the core-rules concept S3 owns verifying.
> - [`KB/log.md`](../../../../KB/log.md) - append an entry for any KB work.
>
> **What S3 may teach as fact:** the 2026-08-16 ownership (10 Warriors, 3 Scarab Swarms, 5 Immortals - all unassembled; Hierotek Circle game-ready with datasheets TBD; Tomb World **not owned**); that **Power Matrix is the Canoptek Court detachment rule in 40K, not a Kill Team term**; the army-rule and detachment names; and the project's own conventions.
>
> **What S3 must not teach as fact:** any rule effect. **Zero game terms are `verified`.** No rules document has been read - the core rules, both faction packs, the terrain PDFs, and the points manuals are all catalogued in [`KB/sources/local_library_pointers.md`](../../../../KB/sources/local_library_pointers.md) and all unopened. Opening `raw/pointers/rules_core.md` is S3's highest-value first action.
>
> **Do not propagate:** "Data Package Detachment" (unrecognised tier label from the owner's notes); Tomb World as current inventory; "need 1 box of Immortals" (they are owned); any suggestion that Power Matrix might be a Kill Team term.
>
> **Conventions that apply to anything you write:**
> - `KB/**` uses **YAML frontmatter only**; `games/**` and `docs/**` use Rising Tide headers and footers. Do not stack them.
> - Every KB page needs an honest `confidence`. Every rules claim needs a verification route **and a retrieval date**.
> - **Teaching paraphrase only.** No GW binaries, no verbatim datasheet or stratagem text.
> - **Write UTF-8 and byte-check before you finish** - the editor in this environment writes UTF-16LE by default. See Finding 1 in `L1_librarian.md` for the check.
>
> **Hard rules:** never write under `raw/`; never `git commit` or `git push` (Coordinator only).
>
> **Open threads:** Hierotek Circle datasheet mapping (user photos); Space Marine collection audit; whether Wahapedia's `wh40k10ed` URLs serve 11e content; whether a dataslate has superseded the owned PDFs.

---

## Next

**S3** - rules, setup, and the shipping `Keyword_Glossary`. Tier 0 entrance is satisfied; paste the inherited block above into `S3_brief.md`.

The KB stays at **maturity level 1 (pilot)** but the gate is now genuinely met: `librarian_agent.md` Sec 5 requires "one successful manual ingest", and this was it. Level 2 should wait until the ingest contract has survived a source that is an actual rules document, which has not happened yet.
