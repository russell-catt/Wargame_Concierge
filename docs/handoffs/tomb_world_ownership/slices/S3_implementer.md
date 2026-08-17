# S3 — Implementer Report (Planning + context sync)

- **Track:** `tomb_world_ownership`
- **Slice:** S3
- **Role:** Implementer (content)
- **Status:** Resolved - Implemented
- **Commit:** pending — no commit, no push performed. The Coordinator owns the single deferred commit at S4
- **Tier 1 self-check:** **PASS**

---

## Model waiver — explicit

| Field | Value |
|-------|-------|
| Locked model (`track_in.md`, Implementer — content) | `claude-sonnet-5-thinking-high` |
| **Model actually used** | **`claude-opus-5-thinking-high`** |
| Reason for substitution | Dispatch of the locked model was **blocked / unavailable** at dispatch time |
| Same-family? | **Yes** — both are Anthropic Claude models, so this is a within-family substitution and satisfies the track's substitution rule |
| Implementer/QA family separation | Preserved. QA for S3 is `gemini-3.7-flash-high` (Google), a different family |
| Authorized by | The dispatching Coordinator, in the S3 dispatch instruction |
| **Waiver recorded** | **Yes — this section is the record** |

No other deviation from the locked matrix.

---

## Read first (confirmed)

- `docs/handoffs/tomb_world_ownership/slices/S3_brief.md`
- `docs/handoffs/tomb_world_ownership/track_in.md`
- `games/warhammer_40k_11e/armies/necrons/Necron_Lists.md` — FOUNDATION, the source of truth for this slice
- Also read for continuity: `S1_implementer.md`, `S2_implementer.md`

**Encoding note (same artifact S2 reported).** The `Read` tool mis-decoded `S3_brief.md` and `track_in.md` on first read, rendering UTF-8 bytes as if they were UTF-16LE. Verified with `[System.IO.File]::ReadAllBytes` that the files on disk are valid UTF-8 and re-read them correctly with `Get-Content -Encoding UTF8` before editing anything. Display artifact only; no file was corrupted. The same tooling wrote *this* report as UTF-16LE on the first attempt - very likely how the earlier UTF-16 slice artifacts in this track were produced. It was converted in place to UTF-8 without a BOM and byte-verified, so it satisfies hard rule 7.

**`raw/` write authorization.** `raw/` is normally treated as immutable and the Librarian never writes it. The S3 brief explicitly names `raw/pointers/necron_lists_import.md` as an in-scope file, and `AGENTS.md` scopes `raw/` writes to "Coordinator / Implementer copy-in only", so this edit is authorized. No other path under `raw/` was touched — in particular `raw/Necron_Lists.md` was left exactly as S1 synced it.

---

## Locked ownership applied

- **Kill Team: Tomb World — owned, game-ready:** 1× Cryptek Geomancer, 2× Canoptek Tomb Crawlers, 5× Canoptek Macrocytes, 10× Necron Warriors, 3× Canoptek Scarab Swarms.
- **Also owned, on sprue:** 10× Necron Warriors (2nd squad, unassembled/unpainted), 3× Canoptek Scarab Swarms (2nd set, unassembled/unpainted), 5× Immortals (unassembled).
- **Hierotek Circle Kill Team:** an *additional* game-ready set; 40K datasheets TBD pending owner photos.
- **Totals:** 20 Warriors (10 ready + 10 sprue), 6 Scarab Swarms (3 ready + 3 sprue), plus Geomancer, Tomb Crawlers, Macrocytes, Immortals, Hierotek TBD.
- **Tomb World is the preferred learning baseline.** Extras are assemble-to-expand, never blockers. Do not re-shop owned kits. The prior "Tomb World not owned" claim was erroneous.

---

## Changes made

Three files, exactly as scoped by the brief. Nothing else was edited.

### 1. `docs/Project_Planning.md` (v1.0 → v1.1)

- **Sec 3 rebuilt against FOUNDATION.** Replaced the single four-row "unassembled" table with three tables: **Game-ready** (Tomb World's five entries plus Hierotek Circle as an *additional* game-ready set), **Build before play** (2nd Warriors squad, 2nd Scarab set, Immortals — all tagged unassembled/unpainted), and **Ownership totals** (20 Warriors, 6 Scarab Swarms, and every other line item).
- Rewrote the three "consequences" so Tomb World is the preferred learning baseline, build-before-play applies only to the extras, and owned kits are never shopping targets.
- **Deleted the "### Superseded: Kill Team: Tomb World" section.** Replaced it with **"### Correction: the 'Tomb World not owned' claim was erroneous"** — a table recording the prior claim, the reality, where it was corrected (S1/S2/S3/L1/L2), and a standing instruction not to reintroduce "Tomb World not owned", "Tomb World superseded", or "only the Hierotek Circle set is game-ready".
- **Added "### Authoritative order for ownership facts"**: FOUNDATION → `raw/` + external source → army docs → `KB/`, with an explicit note that the ladder governs ownership only and that FOUNDATION's *points* are stale.
- **Sec 4:** Hierotek Circle photo ID downgraded from blocker to open-but-non-blocking. Removed "The only game-ready models in the collection are the ones we cannot yet name."
- **Sec 5:** annotated the Preflight and Ownership-re-sync rows to say the Tomb World supersession they recorded was erroneous and has been reverted; added rows for `tomb_world_ownership` S1, S2, and S3.
- **Sec 1 / Sec 2 / Sec 6:** current status now names `tomb_world_ownership` as the active track with `v1_scaffold` closed, corrects the git row (`main` is one commit ahead of `origin/main` at `5a7679c`; single deferred commit at S4), retires the "push at S7" locked-decision row, and replaces the stale `v1_scaffold` next-actions list with the current track's remaining work.
- **Change Log:** v1.1 entry added; the v1.0 entry annotated to flag that its Tomb World supersession was erroneous.

### 2. `reference/Distilled_Project_Context.md` (v1.0 → v1.1)

- **Sec 5 ownership digest realigned:** game-ready Tomb World table, build-before-play table, explicit **Totals** line (20 Warriors / 6 Scarab Swarms plus the rest), and bullets stating Tomb World is owned, game-ready, and the preferred learning baseline.
- **Removed** "Kill Team: Tomb World is superseded and historical as of 2026-08-16. It does not describe current ownership." Replaced with a bullet stating the prior claim was **erroneous** and corrected, plus an instruction not to treat "only the Hierotek Circle set is game-ready" as current.
- **Sec 6 now names the authoritative order** — exit criterion for this slice — as a ranked table: project `Necron_Lists.md` (FOUNDATION) → `raw/Necron_Lists.md` + `C:\Personal\40K\rules\Necron_Lists.md` → army docs → `KB/`, pointing at the import pointer for sync expectations.
- **Sec 8 rewritten:** current `tomb_world_ownership` track with per-slice state and the deferred-commit git note; `v1_scaffold` recorded as closed, with a plain statement that its ownership content was wrong about Tomb World throughout.
- **Sec 9 open threads:** Hierotek ID marked open-but-not-blocking; added the open `KB/` ownership-denial thread, the FOUNDATION-vs-army-docs points drift, and the stale detachment-doc ownership rows.
- **Sec 1, 4, 7, 11, 12** refreshed: git/remote facts, the commit rule, the model-matrix pointer (now the current track), a caveat warning that anything written before this track denied Tomb World ownership, and reference rows for the current track plus FOUNDATION.
- **Change Log:** v1.1 entry added; v1.0 annotated.

### 3. `raw/pointers/necron_lists_import.md` (rewritten)

- **Copies table** now ranks the three copies (project FOUNDATION authoritative, then `raw/` and the external source) and states the project copy wins on divergence. Fixed a malformed link that mixed a backslash into the `armies\necrons` path.
- **Ownership section** states Tomb World is owned and game-ready with the full five-unit list, lists the **dual Warriors/Scarabs** (10 + 10 = 20, 3 + 3 = 6) and the Immortals as owned-on-sprue, and marks Hierotek Circle as an additional game-ready set with datasheets TBD.
- **New "Sync expectations" section** — the brief's exit criterion: direction of truth (project → `raw/` → external), re-copy plus SHA-256 confirmation after any FOUNDATION change, `raw/` writer rules, the verification command used, and UTF-8-no-BOM in every copy.
- **New History table** marking the Preflight supersession and the later "drift" re-sync as erroneous, and the S1 correction plus this S3 realignment as the fix.
- **Removed** the live claim "Tomb World is **not** current ownership", replaced by an explicit line saying it was wrong and must not be reintroduced.

---

## Tier 1 checks — PASS

| # | Check | Method | Result |
|---|-------|--------|--------|
| 1 | No live "Tomb World not owned" / "superseded" / "only Hierotek game-ready" claim in the three files | `Select-String` across all three for `not owned`, `superseded`, `Superseded`, `only the Hierotek`, `only game-ready`, `Tomb World` | **PASS** — every surviving hit is either an explicit correction note, a changelog annotation, a dated history row, or a pointer describing the *prior* track. Zero live denials |
| 2 | Planning docs state Tomb World owned **and game-ready** | Read back `Project_Planning.md` Sec 3 and `Distilled_Project_Context.md` Sec 5 | **PASS** |
| 3 | Totals correct: 20 Warriors, 6 Scarab Swarms, plus Geomancer / Crawlers / Macrocytes / Immortals / Hierotek TBD | Compared all three files against FOUNDATION and `track_in.md` line by line | **PASS** — identical in all three |
| 4 | Unit counts match FOUNDATION exactly (1 Geomancer, 2 Tomb Crawlers, 5 Macrocytes, 10 Warriors, 3 Scarabs game-ready; 10 + 3 + 5 on sprue) | Direct comparison with `Necron_Lists.md` FOUNDATION tables | **PASS** |
| 5 | Distilled context names the authoritative order (project `Necron_Lists` → raw + source → army docs → KB) | Read back Sec 6 ranked table | **PASS** — also mirrored in `Project_Planning.md` Sec 3 |
| 6 | Import pointer documents sync expectations | Read back the "Sync expectations" section | **PASS** |
| 7 | Relative link targets resolve | `Test-Path` on every path newly linked or referenced | **PASS** — 10/10 exist |
| 8 | Encoding: UTF-8, no BOM (hard rule 7) | Byte inspection of the first three bytes of each file | **PASS** — all three no-BOM UTF-8; the rewritten pointer was normalized to CRLF to match its siblings |
| 9 | Diffs are clean text, not garbled or binary | `git diff --stat` | **PASS** — 3 files, 208 insertions, 79 deletions, line-level only |
| 10 | Scope discipline: only the three briefed files modified | `git status --short` on the three paths, plus confirmation that `raw/Necron_Lists.md` is untouched | **PASS** |
| 11 | **No commit, no push** | `git log --oneline -1` still `5a7679c`; branch still one ahead of `origin/main`; working tree shows modifications only | **PASS** |

**Tier 1 self-check: PASS.**

---

## Exit criteria — self-check

- [x] Planning docs state Tomb World owned and game-ready
- [x] Totals: 20 Warriors, 6 Scarab Swarms, plus Geomancer / Crawlers / Macrocytes / Immortals / Hierotek TBD
- [x] Distilled context names the authoritative order: project `Necron_Lists` → raw + source → army docs → KB
- [x] Import pointer documents sync expectations
- [x] Supersession of Tomb World removed; the erroneous prior claim recorded as corrected
- [x] Only the three briefed files updated
- [x] No commit, no push

---

## Findings for the Coordinator — out of scope, not fixed

The brief limited S3 to three files, so these were flagged rather than edited. All three are recorded in the "Known defects carried forward" table in `Project_Planning.md` and in `Distilled_Project_Context.md` Sec 9 so they cannot be lost.

| # | Finding | Where | Suggested owner |
|---|---------|-------|-----------------|
| 1 | **Live false ownership denial.** "Kill Team: Tomb World is superseded and historical, not current ownership", plus an anti-pattern row warning that Tomb World models "are not owned" | `docs/Rehydration_Prompt.md` lines ~136 and ~200 | Implementer, S4 or a follow-up slice. This one matters most — the rehydration prompt is what a cold session reads first, so it will re-teach the wrong ownership |
| 2 | **Live false ownership denial.** "Kill Team: Tomb World — Not owned — superseded historical reference only" | `reference/Source_Library.md` line ~145 | Implementer, S4 or a follow-up slice |
| 3 | **Stale ownership rows in the detachment docs.** The first Warriors squad and first Scarab set are tagged "Yes - unassembled" when they are game-ready Tomb World units, and Scarab Swarms (6) is tagged "Half" owned when all 6 are owned | `games/.../necrons/Canoptek_Court.md` ~107-109 and `Cryptek_Conclave.md` ~114 | A follow-up slice. These are S2-scope army docs that S2 did not reach |
| 4 | **Points drift.** FOUNDATION prices 10 Necron Warriors at 100; the army docs and starters read 80 from Munitorum Field Manual v1.2 (2026-08-16), and `Canoptek_Court.md` carries an explicit points health warning that FOUNDATION's figures are stale. I therefore avoided quoting FOUNDATION point costs in the two planning docs and stated that the authority ladder governs ownership only | FOUNDATION vs army docs | A points-verification slice |
| 5 | **UTF-16LE slice artifacts** violating hard rule 7, in this track: `S1_qa.md`, `S2_implementer.md`, `S2_qa.md`. This report is UTF-8, no BOM | `docs/handoffs/tomb_world_ownership/slices/` | Coordinator |
| 6 | **`reference/Initial_Prompt.md`** mentions the Tomb World supersession, but that file is append-only and quoted verbatim as a record of *intent*, so it should probably be left alone rather than corrected | `reference/Initial_Prompt.md` ~line 125 | Coordinator's call |

---

## Notes

- Neither planning document is a place where ownership facts *live*; both now name FOUNDATION as the authority and say plainly that they lose to it in a disagreement.
- `KB/` was not touched — L1 and L2 own that, and only the Librarian writes there.
- `raw/Necron_Lists.md` was deliberately not touched; S1 already synced it and it remains byte-identical to the project copy.
