# L1 — Librarian report (KB ownership ingest)

- **Status:** Resolved - Implemented (awaiting QA)
- **Track / slice:** `tomb_world_ownership` / L1 (Librarian, Tier 0)
- **Date:** 2026-08-16
- **Model used:** `claude-opus-5-thinking-high` (**waiver** — see below)
- **Depends:** S3 Resolved - Complete (YES)
- **Commit:** pending — no commit, no push performed. The Coordinator owns the single deferred commit at S4
- **Tier 1 self-check:** **PASS**

---

## Model waiver

| Field | Value |
|-------|-------|
| Locked model (`track_in.md`) | `claude-fable-5-thinking-high` |
| Actual model | `claude-opus-5-thinking-high` |
| Reason | Locked model was **blocked / unavailable at dispatch** |
| Basis | Same-family substitute (Anthropic Claude, thinking-high tier) |
| QA separation | QA for L1 is `gpt-5.6-sol-medium` — **different family**, so playbook Sec 18.7 separation of duties still holds |
| Precedent | Same waiver shape as `v1_scaffold` S3, S4, S5, and L1 |

Recorded here per the `track_in.md` instruction to record the actual model in each `*_librarian.md`.

---

## Locked ownership now carried by the KB

Taken from `docs/handoffs/tomb_world_ownership/track_in.md` and the FOUNDATION section of `games/warhammer_40k_11e/armies/necrons/Necron_Lists.md` (authoritative order position 1).

**Game-ready — Kill Team: Tomb World, owned, assembled, painted, known datasheets:**

| Unit | Qty |
|------|-----|
| Cryptek Geomancer | 1 |
| Canoptek Tomb Crawlers | 2 |
| Canoptek Macrocytes | 5 |
| Necron Warriors | 10 |
| Canoptek Scarab Swarms | 3 |

**Also game-ready:** Hierotek Circle used set — 40K datasheets **TBD pending owner photos** (thread preserved everywhere it appeared).

**Owned, unassembled:** second Necron Warriors squad (10), second Canoptek Scarab Swarms set (3), Immortals (5).

**Totals:** 20 Necron Warriors, 6 Canoptek Scarab Swarms, plus Geomancer, Tomb Crawlers, Macrocytes, Immortals, Hierotek Circle.

**Preference recorded:** Tomb World is the preferred learning baseline. Spare Warriors and Scarabs are **assemble-to-expand**, not shopping targets. Do not re-shop owned kits.

---

## Rules removed as current guidance

| Retired rule | Where it lived | Disposition |
|--------------|----------------|-------------|
| **"Do not let Tomb World content leak into current advice."** | `KB/sources/necron_lists_owner_notes.md`, echoed in `KB/glossary.md` and `KB/analyses/inherited_docs_for_S3.md` | **Retired as a current rule.** Survives only as a named row on the `glossary` deprecated list, so it cannot quietly return as guidance |
| **"Kill Team: Tomb World — not owned / superseded historical only."** | `necron_lists_owner_notes`, `necrons` ("Explicitly not owned" section), `glossary`, `overview`, `inherited_docs_for_S3` | **Deleted as a fact.** No page in `KB/` now asserts it. Retained only as a deprecated claim and in append-only log history, which the new log entry explicitly corrects |

---

## KB files updated (11)

Six briefed targets, plus log and changelog, plus three additional pages that carried the same false ownership claims and were caught by the required grep sweep.

### Briefed targets

| # | File | What changed |
|---|------|--------------|
| 1 | `KB/sources/necron_lists_owner_notes.md` | FOUNDATION table rebuilt into Game-ready / Build-before-play sections with totals; "Historical material inside the source" replaced by **"The Tomb World correction"** with a retired-claim table; the "leak" instruction withdrawn; Conclave remaining spend corrected to ~$310 / $155-220 to match the source of truth; Hierotek open question de-escalated from "blocks Phase 1 of both paths"; Macrocytes *Ignores Cover* lead marked disproven per S4 |
| 2 | `KB/factions/necrons.md` | Ownership section rewritten; **"Explicitly not owned" section removed entirely**; "awkward shape of this collection" framing replaced (it was built on the false premise); detachment-fit table and the provisional recommendation re-derived from game-ready models; Hierotek open question de-escalated |
| 3 | `KB/glossary.md` | **Kill Team: Tomb World** entry inverted from `not owned` to `owned, game-ready` with the full unit list; **Hierotek Circle** entry no longer claims sole game-readiness; project vocabulary `Game-ready` and `Build before play` re-scoped to the real inventory; **Assemble-to-expand** added as a new project term (project vocab 6 → 7); deprecated list rewritten with three ownership rows; L1 ownership note appended alongside the existing L2 lint note |
| 4 | `KB/overview.md` | Necron ownership table rebuilt with totals; two open threads re-derived; "only table-ready models are the ones nobody has identified" framing replaced; **Correction of record** paragraph replaces the "superseded and historical" line; new **"Resolved in L1 - `tomb_world_ownership`"** section; Current-state metrics refreshed (glossary count, last ingest); two knowledge-gap / open-question rows corrected |
| 5 | `KB/sources/source_library.md` | Ownership snapshot paragraph corrected; explicit statement that any snapshot still reading "Tomb World not owned" is stale and must be re-synced from the project armies copy rather than trusted |
| 6 | `KB/analyses/inherited_docs_for_S3.md` | Stable-ownership table rebuilt with totals and a "must not reintroduce" note for S3; teaching constraints re-derived from three to reflect that a playable army exists; `Keyword_Glossary` alignment note updated; Hierotek open thread re-scoped from "the first playable game" to "using the set in a list" |

### Appends

| # | File | What changed |
|---|------|--------------|
| 7 | `KB/log.md` | Appended `## [2026-08-16] ingest \| L1 - Tomb World ownership correction`. Follows the log's own append-only correction rule: the entry **explicitly corrects** the two earlier entries that recorded Tomb World as not owned, rather than editing them. Records the model waiver, the locked inventory, the retired rules, the per-page change table, and the process lesson |
| 8 | `KB/changelog.md` | Row added to the Promotions table as an **ownership correction, not a promotion**, under the existing "a rules claim in shipping content is corrected after verification" trigger. Approved-by left as `Pending Coordinator` |

### Additional pages caught by the grep sweep

The brief required grepping `KB/` for `not owned`, `Tomb World`, `superseded`, and `leak` and fixing live false claims. These three pages carried ownership claims that were false for the same reason, so they were corrected in scope.

| # | File | What changed |
|---|------|--------------|
| 9 | `KB/detachments/canoptek_court.md` | **"This detachment is not currently playable" reversed.** Fit table rebuilt — Tomb Crawlers, Macrocytes, and Scarab Swarms are owned Canoptek bodies; Phase 1 changed from "blocked on the Hierotek Circle identification" to playable from game-ready models |
| 10 | `KB/detachments/cryptek_conclave.md` | The path's Cryptek requirement is now satisfied by the **owned Geomancer** instead of a guess about the Hierotek box; fit table rebuilt; remaining spend corrected to ~$310 / $155-220; phases re-derived; "the assumption this whole path leans on" downgraded to an upside |
| 11 | `KB/units/necrons_unit_index.md` | Owned-units table rebuilt with the five Tomb World datasheets; "the best-researched units are unassembled, and the game-ready models are still unidentified" framing replaced; records that **Geomancer (`partial`), Canoptek Tomb Crawlers (`stub`), Canoptek Macrocytes (`stub`)** are mis-tagged `inventory_candidate` because S6 prioritised against the wrong inventory — flagged as a `games/` follow-up, not edited |

**`KB/index.md` deliberately unchanged.** Every row already carries `Updated: 2026-08-16` and no page summary line or confidence value changed, so index maintenance rules produce no edit. No page was created or deleted.

---

## Tier 1 self-check — PASS

| # | Criterion (from `L1_brief.md` exit criteria) | Method | Result |
|---|---|---|---|
| 1 | All six briefed KB targets reflect Tomb World game-ready ownership | Read each file after editing; every one now names the five Tomb World units as game-ready | **PASS** |
| 2 | Dual Warriors / Scarabs inventory documented | Totals of 20 Warriors and 6 Scarab Swarms, split game-ready vs sprue, present on `necron_lists_owner_notes`, `necrons`, `overview`, `source_library`, `inherited_docs_for_S3`, `necrons_unit_index`, and both detachment pages | **PASS** |
| 3 | Hierotek TBD thread preserved | "TBD pending owner photos" retained on all six targets plus `glossary`; re-scoped from blocker to non-blocking, never deleted | **PASS** |
| 4 | "Do not let Tomb World leak" removed as a current rule | `rg` for `leak` across `KB/` returns only the deprecated-list row, the retirement notes, and the log entry describing the retirement. Zero live instances | **PASS** |
| 5 | "Tomb World not owned" removed as a current rule | `rg` for `not owned` / `Not owned` across `KB/` — every hit is a deprecated-claim row, an explicit correction note, or append-only log history superseded by the new entry. Zero live assertions | **PASS** |
| 6 | Grep sweep for `not owned`, `Tomb World`, `superseded`, `leak` completed and live false claims fixed | Two full `rg` passes over `KB/` before and after editing; three additional pages found and corrected beyond the briefed six | **PASS** |
| 7 | Log + changelog appended with an L1 ingest note | New dated log entry in the required `## [YYYY-MM-DD] verb \| subject` form; changelog Promotions row added | **PASS** |
| 8 | Waiver and actual model recorded | This report, plus the model line inside the new `KB/log.md` entry | **PASS** |
| 9 | **Librarian did not write `raw/`** | `raw/` last-write times are 8:49 PM and 9:09 PM, all **before** this session began at 9:21 PM; the two modified `raw/` files belong to earlier slices | **PASS** |
| 10 | Only `KB/` edited (plus this report) | Every edit targeted a path under `KB/`; no `games/`, `docs/`, or `reference/` file was modified. Corpus re-tagging and shipping-content fixes were **recorded as findings, not applied** | **PASS** |
| 11 | Facts sourced in authoritative order | Ownership taken from `track_in.md` and project `Necron_Lists.md` FOUNDATION (positions 1-2), not from the KB's own prior state | **PASS** |
| 12 | No GW binaries, no verbatim rules text | Text-only markdown edits; no datasheet or stratagem wording reproduced. Points figures are labelled as the owner's blueprint values needing a Munitorum check | **PASS** |
| 13 | **No commit, no push** | `git log --oneline -1` still `5a7679c`; `git status -sb` still `## main...origin/main [ahead 1]`; working tree shows modifications only | **PASS** |

**Tier 1 self-check: PASS.**

### Verification commands (verbatim)

```powershell
cd C:\Personal\Personal_Projects\Wargame_Concierge

# grep sweeps required by the brief
rg -n "not owned|Tomb World|superseded|leak" KB/
rg -n "only game-ready|not currently playable|only table-ready|only painted" KB/

# corpus values quoted in necrons_unit_index verified rather than assumed
Select-String -Path games/warhammer_40k_11e/armies/necrons/units/research/Geomancer.md, `
  games/warhammer_40k_11e/armies/necrons/units/research/Canoptek-Tomb-Crawlers.md, `
  games/warhammer_40k_11e/armies/necrons/units/research/Canoptek-Macrocytes.md `
  -Pattern "completeness|priority"

# raw/ untouched by this slice
Get-ChildItem -Path raw -Recurse -File | Select-Object FullName, LastWriteTime

# git hygiene
git log --oneline -1
git status -sb
```

---

## Tier 2 expectations (for QA — `gpt-5.6-sol-medium`)

1. Re-run the two grep sweeps over `KB/` and confirm **zero live** "Tomb World not owned" or "do not let Tomb World leak" assertions. Every surviving hit should be a deprecated-claim row, an explicit correction note, or append-only log history.
2. Confirm all six briefed targets carry the five Tomb World units as game-ready **and** the 20 Warriors / 6 Scarab Swarms totals.
3. Confirm the Hierotek Circle "datasheets TBD pending photos" thread survives on every page it previously appeared on.
4. Confirm `KB/log.md` was **appended**, not edited — the two earlier entries containing the false claim must still be present verbatim, with the new entry correcting them.
5. Confirm nothing outside `KB/` was modified by this slice, and that `raw/` write times predate the slice.
6. Confirm `git log --oneline -1` is still `5a7679c` and the branch is still exactly one ahead of `origin/main`.
7. Spot-check that the Cryptek Conclave remaining-spend figure reads ~$310 / $155-220 (matching `Necron_Lists.md`), not the stale ~$375 / $190-265.

---

## Remaining NON-KB false claims — for the Coordinator

Found while sweeping. **Not edited** — the Librarian's surface is `KB/` only. Items 1 and 2 were already raised by S3; this slice independently confirms both are still live.

| # | False claim | Location | Why it matters | Suggested owner |
|---|-------------|----------|----------------|-----------------|
| 1 | "Kill Team: Tomb World is superseded and historical, not current ownership." Plus an anti-pattern row: treating Tomb World as current inventory produces "starter lists built on models that are not owned" | `docs/Rehydration_Prompt.md` lines 136 and 200 | **Highest impact of the three.** This is what a cold session reads first, so it will actively re-teach the wrong ownership and re-import the retired rule | Implementer, S4 or a follow-up slice |
| 2 | "Kill Team: Tomb World — **Not owned** — superseded historical reference only" | `reference/Source_Library.md` line 145 | It is the authored source behind `KB/sources/source_library.md`. The KB page now contradicts its own upstream source, which will read as KB drift at lint time unless the source is fixed | Implementer, S4 or a follow-up slice |
| 3 | "False Tomb World ownership denials in `KB/` — **Open.** `KB/` still carries 'not owned / superseded' language inherited from `v1_scaffold`" | `reference/Distilled_Project_Context.md` line 232 | Now stale in the other direction: this slice closed that thread. Leaving it Open will send a future session hunting for `KB/` denials that no longer exist | Coordinator or L2 |
| 4 | **UTF-16LE encoded markdown.** `S1_qa.md`, `S2_implementer.md`, and `S2_qa.md` in this track slices folder are UTF-16LE rather than UTF-8 | `docs/handoffs/tomb_world_ownership/slices/` | Exactly the defect L0 flagged and L2 fixed for `v1_scaffold`: UTF-16 produces unreadable git diffs and can break Obsidian parsing. These will land in the S4 commit as binary-looking blobs. Not a Librarian surface | Coordinator or L2 |
| 5 | Research corpus priority tagging: **Geomancer**, **Canoptek Tomb Crawlers**, and **Canoptek Macrocytes** are tagged `inventory_candidate` ("possible Hierotek Circle contents, pending photo ID") with `partial` / `stub` / `stub` completeness | `games/warhammer_40k_11e/armies/necrons/units/Unit_Index.md` and the three matching files under `units/research/` | These are owned, painted, identified models that will hit a table first, yet they are the thinnest research files in the corpus, because S6 prioritised against the wrong inventory. Recorded on `KB/units/necrons_unit_index.md` as a finding | Implementer (a `games/` edit), post-S4 |

### Non-ownership KB staleness observed, deferred to L2 lint

Out of this slice's scope — flagged so L2 does not have to rediscover them.

- `KB/index.md` still says "**Nothing here is `verified` on rules.** No rules document has been read", and `KB/overview.md` still narrates "we have not read the sources we have" with S3/S4/S5 in the future tense. Both predate the rules ingest that `KB/glossary.md` records (24 game terms now `verified`). Ownership-neutral, so left alone.
- `KB/index.md` reports "5 sources, 15 entity pages"; two unit-index pages have since been added.
- `KB/glossary.md` names the Cryptek Conclave rule **Scientific Schemes** in the Necrons section while its own L2 lint note prefers **Technosorcerous Augmentations**. `KB/detachments/cryptek_conclave.md` also still uses the deprecated label throughout.

### Tooling note

`docs/handoffs/tomb_world_ownership/track_in.md` and `L1_brief.md` are clean UTF-8 with LF endings (verified with `Format-Hex`), but the file-read tool initially decoded them as UTF-16 and returned mojibake. Reading them through Python resolved it. Not a repo defect — no encoding fix was applied — but QA may hit the same and should not treat it as file corruption.

**This report was itself written as UTF-16LE by the editing tool and then converted in place to UTF-8 with LF endings.** Verified after conversion: 0 NUL bytes, 0 CRLF pairs, decodes cleanly as UTF-8. Worth knowing because the same tool behaviour is the likely origin of the three UTF-16 peer reports listed as finding 4 above, and because a reader may see this file mis-decoded even though it is valid.

---

## Constraints honoured

| Constraint | Status |
|------------|--------|
| Librarian never writes `raw/` | **Honoured** — `raw/` write times predate this slice |
| Edit `KB/` only | **Honoured** — plus this report, which is the slice's required artifact |
| No GW binaries in git | **Honoured** — no binaries touched; path pointers only |
| No verbatim rules text | **Honoured** — teaching paraphrase only |
| Subagents never commit or push | **Honoured** — `5a7679c` still HEAD, still one ahead of `origin/main` |
| Hierotek Circle TBD preserved as an open TODO | **Honoured** — retained on every page, re-scoped from blocking to non-blocking |
| Deferred single commit at S4 | **Respected** — `Commit: pending` |

---

## Next step

**L2** — audit `v1_scaffold` L2 plus lint, which should pick up the deferred non-ownership staleness listed above. Then **S4** Final Sanity, then the Coordinator's single commit and authorized push (including `5a7679c` if the branch is still ahead of remote).
