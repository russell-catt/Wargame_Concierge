# S1 - Brief (Core RT docs + Game_System_Scaffold)

- **Status:** Resolved - Implemented (awaiting QA)
- **Track:** v1_scaffold
- **Slice:** S1 (Implementer, Tier 1)
- **Tier:** 1 - Implementation

> Retro-filled by the Implementer during S1 execution so the slice has a brief of record. Coordinator authors briefs normally.

## Requirements

1. `START_HERE.md` - onboarding entry point: what the project is, the read order (`START_HERE` → `README` → `KB/index.md` → `Rehydration_Prompt`), status `v1_scaffold` in progress
2. `README.md` - project overview, structure map, links to everything
3. `docs/README.md` - documentation index
4. `docs/Project_Structure.md` - layout covering `raw/`, `KB/`, `docs/`, `games/`, `reference/`
5. `docs/Project_Planning.md` - decisions of record, confirmed ownership, open items
6. `docs/Project_Origin_Story.md` - beginner-facing narrative: parent plays Necrons, son plays Space Marines
7. `docs/Rehydration_Prompt.md` - AI bootstrap: `AGENTS.md`, `KB/index.md`, last log entries, `track_in.md`
8. `docs/Game_System_Scaffold.md` - full reusable checklist, sections A-F, game-agnostic
9. `reference/Initial_Prompt.md`
10. `reference/Distilled_Project_Context.md`
11. `S1_brief.md` and `S1_implementer.md` under `docs/handoffs/v1_scaffold/slices/`
12. Update `track_in.md` with the S1 status

### Facts that must appear in the Planning documents

| Fact | Detail |
|------|--------|
| Repository | **Private** GitHub repo `russell-catt/Wargame_Concierge` |
| First system | Warhammer 40,000 11th Edition |
| Copyright | No GW binaries in git |
| Ownership confirmed | **2026-08-16** |
| Necron pool | 10 Necron Warriors purchased unassembled; 3 Canoptek Scarab Swarms purchased unassembled; 5 Immortals purchased unassembled |
| Hierotek Circle | Used Kill Team set, assembled and painted, **game ready**; unit ID **pending owner photos** |
| Superseded | Kill Team: Tomb World is no longer a valid ownership assumption |
| Living web refs | <https://www.warhammer-community.com/en-gb/> and <https://wahapedia.ru/> |
| Power Matrix | **The Canoptek Court detachment rule in 40K** - resolves the attribution thread L0 left open |

### `Game_System_Scaffold.md` section contract

| Section | Content |
|---------|---------|
| **A** | Project spine - Rising Tide documents + Karpathy KB, once per repo |
| **A2** | Knowledge plane checklist - per new game system |
| **B** | Per game system folders |
| **C** | Per faction / army |
| **D** | Cross-cutting reference types |
| **E** | Typical later tracks |
| **F** | Minimum viable new game, in checklist order |

Must be **game-agnostic**. 40K 11e appears only as a clearly labelled first worked example.

## Depends / User gate

| Dependency | Notes |
|------------|-------|
| **L0 Resolved - Complete** | YES - Tier 0 knowledge entrance PASS |
| Do NOT commit | Coordinator only |
| Do NOT push | S7 user gate |
| Do NOT write `raw/` | Karpathy layer contract |
| Do NOT write `KB/` | Librarian owns it. Corrections to KB content are raised for L1, not applied here |

## Entrance criteria

| Criterion | Attested |
|-----------|----------|
| L0 PASS - `AGENTS.md`, six KB core pages, `librarian_agent.md`, `.obsidian/` present | YES |
| S0 PASS - `templates/`, playbook, `docs/handoffs/`, `.gitignore` present | YES |
| Preflight ownership facts available in `track_in.md` | YES |
| Rising Tide templates readable for tone and header selection | YES |
| `reference/llm-wiki.md` present | YES |

## Exit criteria

- All 10 shipping documents exist at the paths listed in Requirements
- Rising Tide HTML header + Change Log / Attribution / Rising Tide Notes footer on every `docs/`, root, and `reference/` document; `Rehydration_Prompt.md` uses the Version History footer per `templates/README.md`
- **No YAML frontmatter** on any of them - the two conventions do not stack
- `START_HERE.md` states the four-step read order and the project status
- `README.md` carries a structure map covering every top-level directory
- `docs/Project_Structure.md` covers `raw/`, `KB/`, `docs/`, `games/`, and `reference/` with a writer for each
- `docs/Project_Planning.md` carries every fact in the table above, including the Power Matrix resolution and the Tomb World supersession
- `docs/Project_Origin_Story.md` is readable by someone who has never played a wargame, and names the parent-Necrons / son-Space-Marines setup
- `docs/Rehydration_Prompt.md` names `AGENTS.md`, `KB/index.md`, the last log entries, and `track_in.md`, in that order, and contains a paste-ready session block
- `docs/Game_System_Scaffold.md` contains all six sections A, A2, B, C, D, E, F, is game-agnostic, and labels 40K 11e as the first worked example
- `reference/Initial_Prompt.md` preserves the seed request
- `reference/Distilled_Project_Context.md` is a single-read digest that names its authorities
- `track_in.md` reflects the S1 status
- All new files are **UTF-8 without BOM**
- **`raw/` untouched**; **`KB/` untouched**
- **No commit, no push**
- No GW binaries anywhere in the repo
- Internal relative links in the new files resolve to real paths

## Tier 1 commands

```powershell
$root = "C:\Personal\Personal_Projects\Wargame_Concierge"

# 1. All ten shipping docs plus two handoff artifacts exist
@(
  "START_HERE.md","README.md",
  "docs\README.md","docs\Project_Structure.md","docs\Project_Planning.md",
  "docs\Project_Origin_Story.md","docs\Rehydration_Prompt.md","docs\Game_System_Scaffold.md",
  "reference\Initial_Prompt.md","reference\Distilled_Project_Context.md",
  "docs\handoffs\v1_scaffold\slices\S1_brief.md",
  "docs\handoffs\v1_scaffold\slices\S1_implementer.md"
) | ForEach-Object { "{0,-62} {1}" -f $_, (Test-Path "$root\$_") }

# 2. Scaffold sections A-F present
Select-String -Path "$root\docs\Game_System_Scaffold.md" -Pattern "^## (A|A2|B|C|D|E|F)\."

# 3. Planning facts present
Select-String -Path "$root\docs\Project_Planning.md" -Pattern "russell-catt/Wargame_Concierge|Canoptek Court|Tomb World|Hierotek Circle|2026-08-16"

# 4. Rehydration read order present
Select-String -Path "$root\docs\Rehydration_Prompt.md" -Pattern "AGENTS.md|KB/index.md|KB/log.md|track_in.md"

# 5. Encoding - every S1 file UTF-8, no BOM, no UTF-16
# (see S1_implementer.md for the byte-level script and its output)

# 6. Layer contract - raw/ and KB/ untouched
Get-ChildItem "$root\raw" -Recurse -Force | Select-Object FullName, Length, LastWriteTime
Get-ChildItem "$root\KB" -Recurse -File -Force | Measure-Object Length -Sum

# 7. No binaries; no new commits from this slice
@(Get-ChildItem $root -Recurse -Include *.pdf,*.webp,*.png,*.jpg,*.jpeg,*.gif -File -Force -ErrorAction SilentlyContinue).Count
git -C $root log --oneline    # expect only the Coordinator's S0+L0 bootstrap commit
git -C $root status --short   # expect S1 files untracked
```

## Tier 2 expectations

QA independently verifies:

1. Every exit criterion above, with evidence
2. `Game_System_Scaffold.md` is genuinely **game-agnostic** - 40K vocabulary (phase, detachment, datasheet, points) appears only inside the labelled worked example or an explicit mapping table, never as an assumption in the generic checklist items
3. No `docs/` or `reference/` file carries YAML frontmatter, and no `KB/` file gained a Rising Tide HTML header
4. The read order in `START_HERE.md`, `README.md`, and `Rehydration_Prompt.md` is consistent across all three
5. Ownership facts in `Project_Planning.md` match `track_in.md` Preflight notes and `KB/overview.md` exactly - counts, states, and the Hierotek Circle open thread
6. The Power Matrix statement is recorded as a **project decision** in `docs/`, and the corresponding `KB/glossary.md` correction is **deferred to L1** rather than applied by this slice
7. `raw/` file list, sizes, and timestamps unchanged; no `KB/` file modified
8. `git log` shows no commit authored by this slice - only the Coordinator's S0+L0 bootstrap commit; `git status` shows the S1 files as untracked
9. Relative links in the S1-authored files resolve to real paths
10. All S1 files are UTF-8 without BOM

## Recommended models

| Role | Model | Notes |
|------|-------|-------|
| Implementer | `claude-sonnet-5-thinking-high` | Locked matrix - **blocked / unavailable at dispatch** |
| Implementer (actual) | `claude-opus-5-thinking-high` | **Model waiver** - same-family substitute; recorded in `S1_implementer.md` |
| QA | `gpt-5.6-sol-medium` | Different family from the Implementer, per playbook Sec 18.7 |

## Inherited documentation

> **Tier 0 - Knowledge ready: PASS.** The KB schema and catalog exist; every path below is real.
>
> **Read before starting:**
> - [`AGENTS.md`](../../../../AGENTS.md) - **schema source of truth.** Entity types, YAML frontmatter, naming, copyright rules, and the ingest / query / lint workflows. Read this first.
> - [`KB/index.md`](../../../../KB/index.md) - master catalog. Every KB page is listed here; add a row for anything you create.
> - [`KB/log.md`](../../../../KB/log.md) - activity log. Append an entry for any KB work.
> - [`docs/operations/librarian_agent.md`](../../../operations/librarian_agent.md) - Librarian day-to-day operations and the L0/L1/L2 slice pattern.
> - [`KB/ingest_procedure.md`](../../../../KB/ingest_procedure.md) - how `raw/` becomes `KB/`; what may and may not enter `raw/`.
> - [`KB/overview.md`](../../../../KB/overview.md) - project scope, 40K 11e, confirmed Necron ownership as of 2026-08-16.
> - [`KB/glossary.md`](../../../../KB/glossary.md) - terminology. **All 4 seeded terms are `unverified`** - do not treat them as rules truth.
>
> **Conventions that apply to any file you write:**
> - `KB/**` uses **YAML frontmatter only**; `docs/**` and `games/**` use Rising Tide headers and footers. Do not stack them.
> - KB filenames: lowercase `snake_case`. Promoted `docs/` and `games/` filenames: Rising Tide `Snake_Case`.
> - Every KB page needs a `confidence` value. Be conservative - `unverified` beats a confident guess.
> - Rules claims cite where they can be checked, **with a retrieval date**.
> - **Teaching paraphrase only.** No GW binaries, no verbatim datasheet or stratagem text. Path pointers to `C:\Personal\40K` are the correct way to reference owned material.
> - Write **UTF-8**, not UTF-16 - several existing files got this wrong and produce unreadable diffs.
>
> **Hard rules:** never write under `raw/`; never `git commit` or `git push` (Coordinator only).
>
> **Known issue:** `docs/operations/multiagent_coordinator_strategy.md` contains 26 dead relative links inherited from the `daily_report` repo. The prose is authoritative; the links are not.
>
> **Open threads:** Hierotek Circle datasheet mapping (pending user photos); `Power Matrix` attribution - **resolved during S1 dispatch: it is the Canoptek Court detachment rule in 40K.** The glossary correction belongs to L1.

Also inherited:

- Track input: [`track_in.md`](../track_in.md) - model matrix, constraints, Preflight ownership notes
- Playbook: [`multiagent_coordinator_strategy.md`](../../../operations/multiagent_coordinator_strategy.md)
- Prior slices: [`S0_implementer.md`](S0_implementer.md), [`L0_librarian.md`](L0_librarian.md)
- Plan of record: Cursor plan `wargame_concierge_setup_ee78aead` (read-only; do not edit)

## Feeds

**S2** (sources + Necron import) takes S1 Resolved - Complete as its entrance criterion. The inherited block in [`S1_implementer.md`](S1_implementer.md) is paste-ready for the S2 brief, and `docs/Project_Structure.md` now defines where every S2 artifact belongs.

**L1** inherits the Power Matrix correction as a concrete, actionable KB edit.
