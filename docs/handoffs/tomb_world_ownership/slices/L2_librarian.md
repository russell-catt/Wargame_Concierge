# L2 - Librarian report (Audit of v1_scaffold L2, plus full re-lint)

- **Status:** Resolved - Implemented
- **Track / slice:** `tomb_world_ownership` / L2 (Librarian, Tier 0)
- **Date:** 2026-08-16
- **Depends on:** L1 (Resolved - Complete)
- **Verdict:** **RE-EXECUTED (full lint)**
- **Prior-L2 audit:** **PASS with delta** on exit criteria 1-4; criteria 5 and 6 **NO**
- **Commit:** pending - no commit, no push
- **raw/:** untouched by this slice (see Finding 12)

---

## Model waiver

| Field | Value |
|---|---|
| Locked model (brief) | `claude-fable-5-thinking-high` |
| Actual model | `claude-opus-5-thinking-high` |
| Reason | Locked model blocked / unavailable at dispatch |
| Basis | Same-family substitute (Anthropic, thinking-high tier) |
| QA separation | QA for L2 is `gemini-3.7-flash-high` - **different family**, so the cross-family QA requirement in playbook Sec 18.7 still holds |
| Precedent | The same waiver was taken at `v1_scaffold` L2 and at this track's S3, S4, S5 and L1 |

Recorded here, in `KB/log.md`, and in the L2 lint note appended to `KB/glossary.md`.

---

## Part 1 - Audit of the prior `v1_scaffold` L2 gate

Artifacts reviewed: `L2_brief.md`, `L2_librarian.md`, `L2_qa.md` under `docs/handoffs/v1_scaffold/slices/`, plus `AGENTS.md` Sec 11 (Lint) and Sec 13 (Guardrails).

**The instruction not to treat the prior "Verdict: complete" as sufficient was the right call.** Every claim below was re-checked against the current disk state after S1-L1, not against the prior report.

### Completeness checklist

| # | Criterion | Attestation | Evidence on disk today |
|---|---|---|---|
| 1 | Lint report exists and lists findings with severity | **YES** | `v1_scaffold/slices/L2_librarian.md` carries a five-row findings table with a Severity column (2 Medium, 1 Low, 2 Info) |
| 2 | Agreed fixes still present on disk | **YES - with delta** | Glossary Power Matrix correction present (`glossary.md` entry + deprecated-list row + `concepts/power_matrix.md`). Technosorcerous Augmentations present at `glossary.md` line 96 and in the L2 lint note. All `KB/units/*.md` are UTF-8. Both unit-index pointers present. **Delta:** the Technosorcerous fix was narrower than the report reads - see Finding 4 |
| 3 | `KB/log.md` + `KB/changelog.md` contain L2 entries | **YES** | `log.md` `## [2026-08-16] lint \| L2 v1_scaffold`; `changelog.md` L2 lint row. **Delta:** the changelog row was sitting *below* the Related pages section, outside the Promotions table - see Finding 10 |
| 4 | `necrons_unit_index.md` and `space_marines_unit_index.md` exist and link to shipping indexes | **YES** | Both exist, both UTF-8, both link to their `games/.../units/Unit_Index.md`. No 143-page duplicate corpus was created, which was the right call |
| 5 | Open items from prior L2 still accurate after the ownership correction | **NO** | Finding L2-5 (Hierotek TBD) is still accurate but has been **de-escalated** from blocker to non-blocking upside. Finding L2-4 ("research stubs incomplete; **owned units full**") is now **false**: after L1, three owned game-ready units are `partial`/`stub`/`stub`. See Finding 13 |
| 6 | Ownership lint - no active teaching/KB page still claims Tomb World "not owned" / superseded-as-current | **NO** | `KB/` **passes** - zero live denials. `games/` **failed** on three pages: two inside this slice's edit surface (now fixed, Findings 1-2) and one outside it (Finding 3, deferred) |

### Why a full re-lint rather than a targeted one

The re-execute rule fires on **either** a failed exit criterion 1-4 **or** L1 ownership edits reintroducing contradictions, orphans, or glossary drift.

Criteria 1-4 all passed, so the first clause did not fire. **The second clause did, twice:**

1. L1 correctly rewrote nine `KB/` pages around the true ownership. That left two shipping detachment guides asserting the opposite of their own corrected KB counterparts - a live KB-to-`games/` contradiction that did not exist before L1 ran.
2. The "Scientific Schemes" rename that prior L2 recorded as a *preference* was still live as a headword and across four `KB/` pages, which L1 observed and explicitly deferred to L2 lint.

More than ownership strings needed cleanup, so this is a **full Karpathy lint** per `AGENTS.md` Sec 11, not a grep-and-fix pass.

---

## Part 2 - Lint findings

13 findings: 3 High, 5 Medium, 3 Low, 2 Info. 9 fixed, 1 flagged in place rather than guessed, 2 deferred to the Coordinator, 1 recorded only.

| ID | Sev | Category | Finding | Disposition |
|---|---|---|---|---|
| 1 | **High** | Contradiction / false ownership | `games/.../necrons/Canoptek_Court.md` rated itself **"not first, on this collection - the models that make Power Matrix sing are the ones not yet owned, and the models that are owned get nothing from the rule."** Four of the five game-ready Tomb World units are Cryptek or Canoptek and do benefit. Its fit table also tagged the Warriors and Scarabs "unassembled" and omitted the Geomancer, Tomb Crawlers and Macrocytes entirely. Directly contradicted `KB/detachments/canoptek_court.md`, which L1 corrected to "playable today" | **FIXED** (v1.1) |
| 2 | **High** | Contradiction / false ownership | `games/.../necrons/Cryptek_Conclave.md` ended with **"the whole path hinges on one unanswered question: is there a Cryptek in the Hierotek Circle set?"** The owned Geomancer *is* that Cryptek. The page also omitted the Geomancer from its own fit table and tagged the Warriors and Scarabs "unassembled". Contradicted `KB/detachments/cryptek_conclave.md` | **FIXED** (v1.1) |
| 3 | **High** | False ownership denial | `games/.../rules/Keyword_Glossary.md` line 219, in the "Do not say" table: `\| "Kill Team: Tomb World" as owned inventory \| The confirmed 2026-08-16 ownership \| Superseded; historical reference only \|`. This instructs the reader **not** to treat Tomb World as owned - the exact inverted claim this track exists to remove, in shipping teaching content | **DEFERRED** - outside the Librarian edit surface (`rules/`, not `armies/necrons/`). See Part 4 |
| 4 | Medium | Terminology / glossary drift | The Cryptek Conclave rule name. `v1_scaffold` L2 recorded "prefer Technosorcerous Augmentations" in a lint note but left **Scientific Schemes** as the live glossary headword and as the name used throughout `KB/detachments/cryptek_conclave.md`, `KB/factions/necrons.md` and `KB/concepts/power_matrix.md`. `glossary.md` therefore contradicted itself - line 96 used the correct name, line 159 used the deprecated one. Violates `AGENTS.md` Sec 9 | **FIXED** across 6 KB pages |
| 5 | Medium | Stale claim | `KB/index.md` banner: **"Nothing here is `verified` on rules. No rules document has been read."** True at L1, false since S3 - the core rules, both faction packs and Munitorum Field Manual v1.2 have all been read, and `glossary.md` carries 24 `verified` game terms. The page-count "15 entity pages" was also stale (17) | **FIXED** |
| 6 | Medium | Stale claim | `KB/overview.md` carried the same shape of error: entity-page count 15, `Last lint` empty, and the framing **"we have not read the sources we have"** with a forward-looking plan naming S3/S4/S5/S6/L2 as future work. All of those have run | **FIXED** - and the *real* remaining gap named: the rules were read into `games/`, not back-filled into `KB/` |
| 7 | Medium | Missing back-links | `AGENTS.md` Sec 8: "a link that only points one way is a lint finding." `necrons_unit_index` linked to `[[necrons]]`, `[[canoptek_court]]`, `[[cryptek_conclave]]` and `[[wahapedia]]`; none linked back. Same for `space_marines_unit_index`. Both unit indexes were reachable only from `KB/index.md` and from each other | **FIXED** - back-links added on both faction pages |
| 8 | Medium | Data gap left by the ownership error | The **Geomancer, Canoptek Tomb Crawlers and Canoptek Macrocytes have no Munitorum Field Manual v1.2 points anywhere in the repo.** The slice that read the MFM did so believing they were not owned, so it never costed them. They are the models most likely to reach a table first | **FLAGGED IN PLACE** - both teaching pages now say "not yet costed from MFM v1.2" rather than guessing a number (`AGENTS.md` Sec 13: an honest marker beats a confident guess) |
| 9 | Low | Encoding | Four handoff artifacts in this track were **UTF-16LE**, not UTF-8: `S1_qa.md`, `S2_implementer.md`, `S2_qa.md` (flagged by L1) and `L1_qa.md` (written at 21:37 during this slice, after L1's own sweep). UTF-16 produces unreadable git diffs, can break Obsidian parsing, and lands in the S4 commit as binary-looking blobs. L1 assigned this to "Coordinator **or L2**"; `v1_scaffold` L2-3 set the precedent of L2 doing it | **FIXED** - all four converted to UTF-8 / LF, content byte-for-byte preserved. Repo-wide sweep of 300+ markdown files now returns **0** UTF-16 files |
| 10 | Low | Formatting | The `v1_scaffold` L2 changelog row had been appended to the **end of the file**, below the Related pages section, so it rendered as a stray table fragment outside the Promotions table | **FIXED** - relocated into the table, with a note saying so |
| 11 | Low | Stale cross-reference | `Cryptek_Conclave.md` stated: "Still carrying the old name, and not corrected by this slice: `KB/glossary.md`, and `KB/detachments/cryptek_conclave.md`." Both were corrected in this pass, so the note became false the moment Finding 4 was fixed | **FIXED** in the same pass |
| 12 | Info | Guardrail breach (not mine) | `git status` shows **`raw/Necron_Lists.md` and `raw/pointers/necron_lists_import.md` modified** against HEAD. `AGENTS.md` Sec 13 makes `raw/` immutable. File mtimes are 20:49 and 21:09; this session began at 21:36, so these predate it - an earlier slice wrote them (S1's report describes rewriting "all three authoritative copies") | **DEFERRED** - Coordinator decision before the S4 commit. See Part 4 |
| 13 | Info | Prior-L2 open item now false | `v1_scaffold` L2 finding L2-4 read "Many research stubs incomplete - expected for v1; **owned units full**; expand later." After the ownership correction that is wrong: Geomancer is `partial`, Tomb Crawlers and Macrocytes are `stub`, and all three are owned and game-ready | **RECORDED** - already captured on `KB/units/necrons_unit_index.md`; the corpus re-tag is a `games/` edit. See Part 4 |

### Lint categories checked and clean

Run against `KB/` per `AGENTS.md` Sec 11, cross-checked into `games/warhammer_40k_11e/armies/necrons/`:

| Category | Result |
|---|---|
| YAML frontmatter complete on every `KB/` page | **0 defects** (22 pages, all 8 required fields) |
| Broken `[[wikilinks]]` | **0** - the two apparent hits are backticked syntax examples in `index.md` and `glossary.md`, correctly excluded |
| Orphan pages (no inbound link) | **0** |
| Rising Tide header vs YAML frontmatter stacking (Sec 6) | **0** - no `KB/` page carries an HTML header; both edited `games/` pages keep their Rising Tide header and footer |
| GW binaries / verbatim rules text introduced | **None.** All edits are teaching paraphrase; no statlines added |
| Retrieval dates on living-reference claims | Present on every rules claim touched (faction pack v1.1 p.7 and Wahapedia, both 2026-08-16) |
| Edition drift (10th vs 11th) | No new instances; the existing `Keyword_Glossary.md` cover/pistol rows already handle the known ones |
| Encoding | 0 UTF-16 markdown files repo-wide after Finding 9 |

---

## Part 3 - Ownership sweep result

Sweep patterns, run repo-wide over `KB/`, `games/`, `docs/`, `reference/` and the root docs:

```powershell
"not owned|Not owned|is not owned|unowned|do not own"
"superseded|historical only|historical-only|not currently|no longer current"
"only game-ready|not currently playable|only table-ready|only the Hierotek|do not let Tomb World|Tomb World leak"
"Scientific Schemes|Technosorcerous"
```

| Surface | Result |
|---|---|
| `KB/` | **CLEAN.** Zero live denials. Every surviving hit is a deprecated-claim row, an explicit correction note, or append-only `log.md` history that the L1 entry at line 131 explicitly corrects - which is the log's own correction rule working as designed |
| `games/.../armies/necrons/` | **CLEAN after this slice.** Findings 1-2 fixed. Remaining hits are dated change-log annotations marking their own prior versions as erroneous, plus `Quick_Reference_Play_Guide.md` line 136 "Canoptek Wraiths - Not owned", which is **true** and must stay |
| `games/.../rules/` | **ONE LIVE DENIAL** - Finding 3, deferred |
| `docs/Rehydration_Prompt.md` | **CLEAN.** L1 flagged lines 136 and 200; the Coordinator fixed both at S4 preflight. Re-verified: the only surviving mention is a failure-mode row warning *against* denying ownership, which is the correct direction |
| `reference/Source_Library.md` | **CLEAN.** L1 flagged line 145; fixed at S4 preflight, change-log row v1.1 records the removal |
| `reference/Distilled_Project_Context.md` | **CLEAN.** The open thread L1 flagged as stale-in-the-other-direction is now marked "Closed - resolved at L1" |
| `docs/handoffs/**` | Historical slice artifacts. Denials there are append-only records of what each slice believed at the time, in a closed track. **Not live content, deliberately not edited** |

**The two items the brief told me to list for the Coordinator rather than edit are both already fixed.** `docs/Rehydration_Prompt.md` and `reference/Source_Library.md` were corrected by the Coordinator at S4 preflight, between L1 and this slice. Nothing is outstanding on either.

---

## Part 4 - Remaining for the Coordinator before S4

| # | Item | Why it is not mine | Suggested action |
|---|---|---|---|
| 1 | **`games/.../rules/Keyword_Glossary.md` line 219** - live false ownership denial (Finding 3) | The Librarian surface for this slice is `KB/` plus `games/.../armies/necrons/`. This file is under `rules/` | Replace the row with the inverse: *Do not say* "Kill Team: Tomb World is superseded / historical reference only"; *Say instead* the confirmed 2026-08-16 ownership. **Also line 214** of the same table says the Scientific Schemes conflict is "Flagged for the Librarian rather than overwritten" - that is now done, so the row can record the rename as applied |
| 2 | **`raw/` is dirty against HEAD** (Finding 12) - `raw/Necron_Lists.md`, `raw/pointers/necron_lists_import.md` | `AGENTS.md` Sec 13 forbids the Librarian from writing `raw/`, and these predate this session | Decide before committing: the FOUNDATION content in them is *correct*, so this is a provenance question, not a content one. Either accept the change with a note recording that a slice wrote through the immutability boundary, or restore from HEAD and re-derive |
| 3 | **Unit research corpus priority re-tag** (Finding 13) | `games/.../units/research/` is corpus-owner surface | Re-tag **Geomancer**, **Canoptek Tomb Crawlers** and **Canoptek Macrocytes** from `inventory_candidate` to `starter`, and fill their research files. They are owned, painted and identified, and they are currently the thinnest-researched units in the corpus |
| 4 | **Missing MFM v1.2 points** (Finding 8) | Requires reading the owner's Munitorum Field Manual | Cost the Geomancer, Tomb Crawlers and Macrocytes. Both detachment guides currently carry an explicit placeholder rather than a guess |
| 5 | **`KB/` back-fill gap** | Large enough to be its own slice, not a lint fix | The rules were read into `games/` by S3-S5 but never re-ingested into `KB/`, so KB faction, detachment and concept pages remain `draft`/`unverified` while shipping content is verified. Now stated plainly in `KB/overview.md` |
| 6 | **Carried from L1 QA** | Cosmetic | L1's changelog row says "nine content pages updated, plus log and this file" while its Target cell says `KB/** (10 pages)`. Count-only discrepancy, no guidance impact |

---

## Files changed by this slice

**`KB/` (11 files)** - `glossary.md`, `index.md`, `overview.md`, `log.md`, `changelog.md`, `concepts/power_matrix.md`, `detachments/cryptek_conclave.md`, `factions/necrons.md`, `factions/space_marines.md`, `sources/necron_lists_owner_notes.md`, `analyses/inherited_docs_for_S3.md`

**`games/warhammer_40k_11e/armies/necrons/` (2 files)** - `Canoptek_Court.md` v1.1, `Cryptek_Conclave.md` v1.1. Both under the ownership-lint mandate; both keep their Rising Tide header and footer; neither had rules content changed.

**`docs/handoffs/tomb_world_ownership/slices/` (5 files)** - this report, plus UTF-8 conversion of `S1_qa.md`, `S2_implementer.md`, `S2_qa.md`, `L1_qa.md` (encoding only, content preserved).

**Not touched:** `raw/**`, `reference/**`, `docs/Rehydration_Prompt.md`, `games/.../rules/**`, `games/.../space_marines/**`.

---

## Constraints honoured

| Constraint | Status |
|---|---|
| Librarian never writes `raw/` | **Honoured** - `raw/` mtimes are 20:49 and 21:09, before this session began at 21:36 |
| No `git commit`, no `git push` | **Honoured** - `git log --oneline -1` is still `5a7679c`; working tree shows modifications only |
| No GW binaries | **Honoured** - text-only markdown edits |
| No verbatim rules text | **Honoured** - the Technosorcerous Augmentations write-up is teaching paraphrase, matching what S4 already shipped |
| Flag contradictions rather than quietly rewriting (Sec 13) | **Honoured** - `KB/sources/necron_lists_owner_notes.md` **keeps** "Scientific Schemes" where it quotes the source, with a conflict flag beside it |
| Subagents never commit or push | **Honoured** - `Commit: pending` |

---

## Tooling note

Several markdown files in this track render as mojibake through the agent file-read tool while being valid UTF-8 on disk (`track_in.md`, `L1_brief.md`, `L1_librarian.md`, `L2_brief.md`, `S4_coord_preflight_notes.md`). The trigger appears to be **LF-only line endings combined with non-ASCII characters and no BOM** - the reader's encoding detector guesses UTF-16LE and byte-swaps. It is not a repo defect and no file was changed for it; reading the bytes through PowerShell decodes them correctly.

**This report is deliberately written ASCII-only** so QA does not hit the same detector. That is separate from Finding 9, which was four files that really were UTF-16 on disk.

**The editing tool then wrote this report itself as UTF-16LE**, which is exactly the Finding 9 defect reproducing in real time, and is almost certainly how all five files in Finding 9 were produced. It was caught by the verification sweep and converted in place to UTF-8 with LF endings. Verified after conversion: 36,914 bytes to 18,457, 0 NUL bytes, 0 non-ASCII bytes, decodes cleanly as UTF-8. The same thing happened to the L1 report, so this is a reproducible agent-editor defect rather than a one-off - **any slice writing a handoff artifact here should verify its own file's encoding before declaring done.** A repo-wide sweep of every markdown file now returns 0 UTF-16 files.

---

## Gate

**Prior-L2 audit: PASS with delta (criteria 1-4 YES, 5-6 NO). This slice: RE-EXECUTED - full Librarian lint.**

**Status: Resolved - Implemented. Commit: pending.**

Next: **S4** (Final Sanity, then the Coordinator's single deferred commit and authorised push).
