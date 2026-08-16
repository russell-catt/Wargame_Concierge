# S1 - Implementer report (Core RT docs + Game_System_Scaffold)

- **Status:** Resolved - Implemented (awaiting QA)
- **Track / slice:** v1_scaffold / S1 (Tier 1 - implementation)
- **Date:** 2026-08-16
- **Depends:** L0 Resolved - Complete (Tier 0 knowledge entrance PASS)
- **Paths touched:** `START_HERE.md`, `README.md`, `docs/`, `reference/`, `docs/handoffs/v1_scaffold/`
- **`raw/` untouched:** YES
- **`KB/` untouched:** YES
- **Commit:** none by this slice - Coordinator is the sole git owner

---

## Model waiver

| Field | Value |
|-------|-------|
| **Locked model** (per [`track_in.md`](../track_in.md)) | `claude-sonnet-5-thinking-high` |
| **Availability** | **Blocked / unavailable at dispatch** |
| **Model actually used** | `claude-opus-5-thinking-high` |
| **Basis** | Same-family substitute (Claude, thinking-high tier) |
| **Authorized by** | Coordinator, at dispatch |

This is the **second** same-family waiver in this track. L0 substituted `claude-opus-5-thinking-high` for the locked Librarian model `claude-fable-5-thinking-high` for the same reason.

**QA is unaffected.** The locked QA model for S1 is `gpt-5.6-sol-medium`, which is a different family from the substitute, so the cross-family QA requirement in playbook Sec 18.7 still holds.

**For the Coordinator:** two consecutive slices have now run on a substitute. Worth deciding whether the locked matrix in [`track_in.md`](../track_in.md) should be revised, or whether each slice re-attempts its locked model and waives on failure.

---

## Files created (12)

### Root

| Path | Purpose |
|------|---------|
| `START_HERE.md` | Onboarding entry point: what the project is, the four-step read order, hard rules, and a task-to-document routing table |
| `README.md` | Project overview, goals, the four-layer architecture, full structure map, conventions, copyright policy, status |

### `docs/`

| Path | Purpose |
|------|---------|
| `docs/README.md` | Documentation index - project documents, operations, handoffs, and how to add a new document |
| `docs/Project_Structure.md` | Five-tree layer model, full annotated directory map, per-layer rules, and a "where does my file go" decision table |
| `docs/Project_Planning.md` | Decisions of record, confirmed 2026-08-16 ownership, open items, completed slices, next actions, known defects |
| `docs/Project_Origin_Story.md` | Beginner-facing narrative: the problem, what a wargame is, the two armies and why the pairing teaches well, project promises |
| `docs/Rehydration_Prompt.md` | Cold-session AI bootstrap: read order, paste-ready session block, commands, required facts, failure modes |
| `docs/Game_System_Scaffold.md` | The reusable game-agnostic checklist, sections A through F |

### `reference/`

| Path | Purpose |
|------|---------|
| `reference/Initial_Prompt.md` | All twelve seed turns captured verbatim with timestamps, plus what each established and what the seed did **not** cover |
| `reference/Distilled_Project_Context.md` | Single-read context digest with the authority named behind every block |

### Handoff artifacts

| Path | Purpose |
|------|---------|
| `docs/handoffs/v1_scaffold/slices/S1_brief.md` | Entrance and exit criteria, Tier 1 commands, Tier 2 expectations, model recommendations |
| `docs/handoffs/v1_scaffold/slices/S1_implementer.md` | This report |

`S1_brief.md` was retro-filled by the Implementer so the slice has a brief of record; briefs are normally Coordinator-authored.

### Files modified (1)

| Path | Change |
|------|--------|
| `docs/handoffs/v1_scaffold/track_in.md` | S1 row status; model waiver log; a note flagging stale S0 and L0 rows for the Coordinator |

---

## Exit criteria self-check (Tier 1)

| # | Criterion | Result | Evidence |
|---|-----------|--------|----------|
| 1 | All 10 shipping documents exist at the required paths | PASS | See the file table above; `Test-Path` output below |
| 2 | Rising Tide HTML header on every `docs/`, root, and `reference/` document | PASS | 10/10 files open with `<!--` and a `FILE:` line |
| 3 | Correct footer per document type | PASS | 9 use Change Log / Attribution / Rising Tide Notes; `Rehydration_Prompt.md` uses the Version History table per `templates/README.md` |
| 4 | No YAML frontmatter on any shipping document | PASS | No file begins with `---` |
| 5 | `START_HERE.md` states the four-step read order and project status | PASS | `START_HERE` → `README` → `KB/index.md` → `Rehydration_Prompt`; status `v1_scaffold` in progress |
| 6 | `README.md` structure map covers every top-level directory | PASS | 13 top-level entries mapped |
| 7 | `Project_Structure.md` covers `raw/`, `KB/`, `docs/`, `games/`, `reference/` with a writer for each | PASS | Sec 1 five-tree table; Sec 3-6 per-layer detail |
| 8 | `Project_Planning.md` carries every required ownership and decision fact | PASS | See the fact-by-fact table below |
| 9 | `Project_Origin_Story.md` is beginner-readable and names the parent/son split | PASS | Includes a "what a tabletop wargame actually is" primer with no assumed vocabulary |
| 10 | `Rehydration_Prompt.md` names `AGENTS.md`, `KB/index.md`, the last log entries, and `track_in.md` in order | PASS | Sec 1 read-order table; Sec 2 paste-ready block |
| 11 | `Game_System_Scaffold.md` contains sections A, A2, B, C, D, E, F | PASS | 7 section headings matched |
| 12 | Scaffold is game-agnostic with 40K 11e as a labelled worked example | PASS | Generic vocabulary throughout, with a translation table in "rule zero" and a single labelled 40K section |
| 13 | `reference/Initial_Prompt.md` preserves the seed request | PASS | 12 turns, verbatim, with timestamps |
| 14 | `reference/Distilled_Project_Context.md` is a single-read digest naming its authorities | PASS | 12 sections, each pointing at its source of truth |
| 15 | `track_in.md` reflects the S1 status | PASS | S1 row updated; waiver logged |
| 16 | All new files UTF-8 **without BOM** | PASS | Strict UTF-8 decode succeeds on all 12; zero null bytes; no BOM. **See the note below** |
| 17 | **`raw/` untouched** | PASS | Inventory and timestamps identical to the S0/L0 state |
| 18 | **`KB/` untouched** | PASS | `git status` reports no modification under `KB/` |
| 19 | No new commit, no push | PASS | Only the Coordinator's pre-existing S0+L0 commit is in the log |
| 20 | No GW binaries anywhere in the repo | PASS | 0 files matching the blocked extensions |
| 21 | Relative links in S1 files resolve | PASS | 157 relative links checked, 0 broken |

### Fact-by-fact check on the Planning documents

| Required fact | Present | Where |
|---------------|---------|-------|
| Private repo `russell-catt/Wargame_Concierge` | YES | `Project_Planning.md` Sec 2, `README.md`, `Distilled_Project_Context.md` Sec 1 |
| 40K 11e first system | YES | `Project_Planning.md` Sec 2, plus every overview document |
| No GW binaries in git | YES | `Project_Planning.md` Sec 2, `START_HERE.md`, `README.md`, `Distilled_Project_Context.md` Sec 4 |
| Ownership confirmed 2026-08-16 | YES | `Project_Planning.md` Sec 3 heading and table |
| 10 Necron Warriors, purchased unassembled | YES | `Project_Planning.md` Sec 3 |
| 3 Canoptek Scarab Swarms, purchased unassembled | YES | `Project_Planning.md` Sec 3 |
| 5 Immortals, purchased unassembled | YES | `Project_Planning.md` Sec 3 |
| Hierotek Circle used set: assembled + painted, game ready, unit ID pending photos | YES | `Project_Planning.md` Sec 3 and Sec 4 |
| Tomb World superseded as an ownership assumption | YES | `Project_Planning.md` Sec 3, sub-heading "Superseded" |
| Living web references | YES | `Project_Planning.md` Sec 2, `README.md`, `Distilled_Project_Context.md` Sec 6 |
| Power Matrix = Canoptek Court detachment rule (40K) | YES | `Project_Planning.md` Sec 4 as a **resolved** item, with the KB correction deferred to L1 |

---

## Commands (verbatim)

```powershell
$root = "C:\Personal\Personal_Projects\Wargame_Concierge"
$files = @(
  "START_HERE.md","README.md",
  "docs\README.md","docs\Project_Structure.md","docs\Project_Planning.md",
  "docs\Project_Origin_Story.md","docs\Rehydration_Prompt.md","docs\Game_System_Scaffold.md",
  "reference\Initial_Prompt.md","reference\Distilled_Project_Context.md",
  "docs\handoffs\v1_scaffold\slices\S1_brief.md",
  "docs\handoffs\v1_scaffold\slices\S1_implementer.md"
)

# Existence
$files | ForEach-Object { "{0,-62} {1}" -f $_, (Test-Path "$root\$_") }

# Encoding: BOM, null bytes, strict UTF-8 decode
$strict = New-Object System.Text.UTF8Encoding($false, $true)
foreach($f in $files){
  $b = [System.IO.File]::ReadAllBytes((Join-Path $root $f))
  $nul = 0; foreach($x in $b){ if($x -eq 0){ $nul++ } }
  $bom = ($b.Length -ge 3 -and $b[0] -eq 0xEF -and $b[1] -eq 0xBB -and $b[2] -eq 0xBF)
  try { [void]$strict.GetString($b); $ok = "valid" } catch { $ok = "INVALID" }
  "{0,-62} bytes={1,-7} bom={2,-6} nulls={3,-4} utf8={4}" -f $f, $b.Length, $bom, $nul, $ok
}

# Scaffold sections A-F
Select-String -Path "$root\docs\Game_System_Scaffold.md" -Pattern "^## [A-F]2?\. "

# Planning facts
Select-String -Path "$root\docs\Project_Planning.md" `
  -Pattern "russell-catt/Wargame_Concierge|Canoptek Court|Tomb World|Hierotek Circle|2026-08-16"

# Relative link resolution across all S1 files
# (regex '\]\(([^)\s]+)\)', skipping http/mailto/anchors, Test-Path each target)

# Layer contract
Get-ChildItem "$root\raw" -Recurse -Force | Select-Object FullName, Length, LastWriteTime

# Binaries and git
@(Get-ChildItem $root -Recurse -Include *.pdf,*.webp,*.png,*.jpg,*.jpeg,*.gif -File -Force -ErrorAction SilentlyContinue).Count
git -C $root log --oneline
git -C $root status --short
```

## Results

| Check | Expected | Actual |
|-------|----------|--------|
| Files created | 12 | 12, all `Test-Path` true |
| Strict UTF-8 decode | 12 valid | 12 valid |
| Null bytes | 0 per file | 0 per file |
| BOM | none | none |
| Scaffold section headings | 7 (A, A2, B, C, D, E, F) | 7 |
| Relative links checked | - | 157 |
| Broken relative links | 0 | 0 |
| `raw/` files | 2 files + 1 dir, unchanged | `raw/README.md` 810 bytes, `raw/pointers/README.md` 236 bytes, both last written 2026-08-16 17:44:07 - identical to the L0 inventory |
| `KB/` modifications | 0 | 0 - 20 files, 39,301 bytes; `git status` shows nothing under `KB/` |
| GW binaries in repo | 0 | 0 |
| New commits by this slice | 0 | 0 - log contains only `1fa3b7c Bootstrap Rising Tide spine and Karpathy KB schema (S0+L0).` |
| `git status` | S1 files untracked, nothing else modified | 11 untracked S1 files plus this report; no modifications outside `docs/handoffs/v1_scaffold/track_in.md` |

---

## Encoding: a real defect, caught and fixed

**Every file was initially written as UTF-16LE without a BOM.** The editing tool used for the first pass silently emitted UTF-16, which is precisely the defect the Librarian flagged in L0 against three S0-authored files.

It was caught by a byte-level check rather than by reading the files - UTF-16LE without a BOM renders correctly in most editors and only shows up as a problem in `git diff`, in tools that sniff for null bytes and conclude "binary", and in Obsidian's parser.

All 12 files were converted in place:

```powershell
$utf8 = New-Object System.Text.UTF8Encoding($false)   # no BOM
$text = [System.Text.Encoding]::Unicode.GetString([System.IO.File]::ReadAllBytes($p))
[System.IO.File]::WriteAllText($p, $text, $utf8)
```

Post-conversion: byte counts halved as expected, zero null bytes, no BOM, and a **strict** UTF-8 decode (`UTF8Encoding($false, $true)`, which throws on invalid sequences) succeeds on all 12. Non-ASCII content survived intact - the box-drawing characters in the structure maps decode as U+2514 and U+251C, not as replacement characters.

**Recommendation for QA and for later slices:** verify encoding at the byte level, not by opening the file. `Get-Content` and most editors will happily hide this. The one-line check is a null-byte count.

---

## Decisions made while implementing

| Decision | Reasoning |
|----------|-----------|
| `Rehydration_Prompt.md` uses the **Version History** footer; everything else uses the standard Change Log footer | [`templates/README.md`](../../../../templates/README.md) maps Rehydration documents to `Footer_Template_Rehydration.md`. The Reference document header template shows a Version History footer in its own body, but the template index maps Reference documents to the standard footer, so the index was treated as authoritative |
| Planned-but-absent files are named in **inline code**, not as markdown links | `reference/Source_Library.md` and the `games/warhammer_40k_11e/` subtree arrive in S2. Linking to them now would ship 5 broken links to satisfy a cosmetic preference |
| The Power Matrix resolution is recorded in `docs/`, **not** applied to `KB/glossary.md` | The Librarian owns `KB/`. `Project_Planning.md` Sec 4 records the resolution and explicitly assigns the glossary correction to L1 |
| `Initial_Prompt.md` reconstructed from the planning session transcript rather than paraphrased | The seed turns were recoverable verbatim with timestamps. A paraphrase would defeat the document's only purpose, which is auditing intent against drift |
| Section A of the scaffold is written as if the repo did not exist | The scaffold has to stand alone when copied into a new repository. Writing it as "already done here" would make it useless for its stated purpose |
| Stale S0 and L0 rows in `track_in.md` flagged, not edited | Those rows are the Coordinator's bookkeeping. Silently correcting another role's rollup would hide the drift rather than surface it |

---

## Findings for the Coordinator

**Finding 1 - `track_in.md` rollup rows are stale.** The rollup still shows **S0 as "In Progress"** and **L0 as "pending"**, but both are complete and both are in commit `1fa3b7c`. I updated only the S1 row and added a note; the S0 and L0 rows belong to the Coordinator's bookkeeping and I did not want to mask the drift by quietly fixing it.

**Finding 2 - the UTF-16 problem is wider than L0 reported.** L0 named three files. The actual list, verified this slice:

| File | Layer | Note |
|------|-------|------|
| `checkins/README.md` | support | |
| `prompts/README.md` | support | |
| `docs/handoffs/README.md` | shipping | |
| `docs/handoffs/v1_scaffold/track_in.md` | shipping | Now partially rewritten by this slice - see the encoding note below |
| `docs/handoffs/v1_scaffold/slices/S0_brief.md` | shipping | |
| `raw/pointers/README.md` | **raw - immutable** | **Needs explicit Coordinator authorization to touch.** Nobody may fix this under the standard layer contract |

`raw/pointers/README.md` is the interesting one: a defect sitting inside the immutable layer, which by contract cannot be corrected by the Librarian or by an Implementer. It needs a deliberate decision rather than a drive-by fix.

**Finding 3 - "no commits yet" was stale across the repo.** Several documents inherited the L0-era assumption that the repository had zero commits. Commit `1fa3b7c` landed between L0 and S1. Corrected in `Project_Planning.md`, `Rehydration_Prompt.md`, `Distilled_Project_Context.md`, and this slice's brief. Worth a general check: any statement of the form "as of now, X is empty" ages badly and should be phrased against a dated slice instead.

**Finding 4 - two consecutive model waivers.** See the waiver section above. This is a matrix question, not a slice question.

---

## Blockers

None blocking S2.

| Thread | Status | Owner |
|--------|--------|-------|
| **Hierotek Circle photo ID** | Open since Preflight. Recorded in `Project_Planning.md` Sec 4 as the highest-value open item | User photos → S4 |
| **Power Matrix glossary correction** | Resolved as a project decision in S1; `KB/glossary.md` still carries the older unresolved-attribution warning | **Librarian, L1** |
| **`raw/pointers/README.md` encoding** | Cannot be fixed under the layer contract | Coordinator decision |

---

## Inherited documentation (paste-ready for the S2 brief)

> **Tier 1 - S1 complete.** The Rising Tide documentation spine now exists. Every path below is real.
>
> **Read before starting:**
> - [`START_HERE.md`](../../../../START_HERE.md) - entry point, read order, hard rules.
> - [`README.md`](../../../../README.md) - project overview, four-layer architecture, structure map.
> - [`AGENTS.md`](../../../../AGENTS.md) - **schema source of truth** for anything touching `KB/`.
> - [`docs/Project_Structure.md`](../../../Project_Structure.md) - **where every new file belongs**, with a placement decision table. Consult this before creating anything in S2.
> - [`docs/Project_Planning.md`](../../../Project_Planning.md) - decisions of record. **Sec 3 is the confirmed model ownership every list and inventory must match.**
> - [`docs/Game_System_Scaffold.md`](../../../Game_System_Scaffold.md) - **Section B** is the contract for what `games/warhammer_40k_11e/` must contain; **Section D** defines the source types S2 catalogues.
> - [`reference/Distilled_Project_Context.md`](../../../../reference/Distilled_Project_Context.md) - the whole project in one read.
> - [`KB/index.md`](../../../../KB/index.md) - master catalog; still empty of entity pages, which is expected before L1.
>
> **Conventions:**
> - `docs/**` and `games/**`: Rising Tide HTML header + Change Log / Attribution / Rising Tide Notes footer, `Snake_Case` filenames.
> - `KB/**`: YAML frontmatter only, `snake_case`. **Do not write here** - the Librarian owns it.
> - `docs/handoffs/**`: plain slice format, no RT header.
> - **UTF-8, no BOM. Verify at the byte level** - count null bytes. Editors hide UTF-16LE, and S1 hit exactly this defect.
> - Teaching paraphrase only; no GW binaries; path pointers to `C:\Personal\40K` only.
>
> **Hard rules:** never `git commit` or `git push` (Coordinator only). `raw/` accepts copy-in **only** where the brief explicitly authorizes it - S2 is authorized to import the updated `Necron_Lists.md`, and nothing else.
>
> **S2-specific:** the file to import is the **Preflight-updated** `C:\Personal\40K\rules\Necron_Lists.md`, not an older Tomb-World-era version. Ownership in any inventory created must match `Project_Planning.md` Sec 3 exactly: 10 Warriors, 3 Canoptek Scarab Swarms, and 5 Immortals, all purchased and unassembled, plus one game-ready Hierotek Circle set with unit ID pending.
>
> **Known issues:** `docs/operations/multiagent_coordinator_strategy.md` has 26 dead relative links inherited from `daily_report` - prose authoritative, links not. Six files in the repo are UTF-16LE, one of them inside the immutable `raw/` layer.
>
> **Open threads:** Hierotek Circle datasheet mapping (pending user photos); the `Power Matrix` glossary correction (assigned to L1 - it is the **Canoptek Court detachment rule** in 40K).

---

## Next

**S2** - sources and the Necron import. Entrance criteria are satisfied; paste the block above into `S2_brief.md`.

**L1** is where the ingest contract is actually proven, and it now carries one concrete, actionable correction: re-scope the `Power Matrix` glossary entry to the Canoptek Court detachment and clear its row in the glossary verification queue.
