# L1 - Librarian report (first Kill Team 2024 ingest)

- **Status:** Resolved - Implemented (awaiting QA)
- **Track / slice:** kill_team_2024_scaffold / L1 (Tier 0 - knowledge entrance)
- **Date:** 2026-08-17
- **Depends:** Preflight, S0 (both Resolved - Complete)
- **Locked model:** `claude-sonnet-5-thinking-high` - **used as dispatched, no waiver needed.** Standing exclusion honored: **never** `claude-fable-5-thinking-high`.
- **Sources:** Wahapedia Kill Team 3 Core Rules page (read in full, retrieved 2026-08-17); `raw/pointers/kill_team_2024_core.md` and `raw/pointers/kill_team_web_living_sources.md` (read in full, pointer stubs). The owned Core Rules PDF itself was **not** opened - the Librarian has no binary-file access, and the guardrail against copying it into the repo stands regardless.
- **Paths touched:** `KB/sources/kill_team_2024_core_rules.md`, `KB/concepts/{turning_points,activations_apl,orders_conceal_engage,cover_kill_team,control_range_kill_team,injured_operatives}.md`, `KB/glossary.md`, `KB/overview.md`, `KB/index.md`, `KB/log.md`, `KB/changelog.md`, `docs/handoffs/kill_team_2024_scaffold/slices/L1_*.md`, `docs/handoffs/kill_team_2024_scaffold/track_in.md`
- **`raw/` untouched:** YES
- **Promotion:** none into `docs/` or `games/`. One `KB/changelog.md` row added, recording why nothing was promoted
- **Commit:** none by this slice

---

## What was ingested

| Source | Class | Read? | KB page |
|--------|-------|-------|---------|
| Wahapedia - Kill Team 3 Core Rules | Living web reference | **In full**, retrieved 2026-08-17 | `KB/sources/kill_team_2024_core_rules.md` |
| `raw/pointers/kill_team_2024_core.md` | Pointer stub to 5 owned PDFs (Core Rules, lite rules, update log, universal equipment, sniper update) | Read in full **as a pointer**; the PDFs it points to are unopened | Same |
| `raw/pointers/kill_team_web_living_sources.md` | Pointer stub | Read in full | Same |

The distinction matters: this ingest cross-checked KT24's *structure* against a community aggregator, not against the owned PDF Games Workshop actually sells. Every page below says so and stays at `confidence: draft` because of it.

---

## Pages created (7)

| Path | Confidence | Note |
|------|-----------|------|
| `KB/sources/kill_team_2024_core_rules.md` | draft | Provenance, edition, coverage, fan-out; flags the owned PDF's update-log gap and Wahapedia's own "June 2026 vs February 2026" book-version discrepancy |
| `KB/concepts/turning_points.md` | draft | Strategy/Firefight phase structure; the "not a 40K battle round" distinction |
| `KB/concepts/activations_apl.md` | draft | Alternating single-operative activation, APL budget, counteract |
| `KB/concepts/orders_conceal_engage.md` | draft | Engage/Conceal; the Engage-vs-Engagement-Range collision |
| `KB/concepts/cover_kill_team.md` | draft | KT24 cover as a defender-side dice bonus, opposite direction from 40K's attacker-BS penalty |
| `KB/concepts/control_range_kill_team.md` | draft | Control Range; **the naming-deviation page** - see below |
| `KB/concepts/injured_operatives.md` | draft | Half-Wounds threshold; the Injured-vs-Battle-shock collision |

## Pages updated (5)

| Path | Change |
|------|--------|
| `KB/glossary.md` | New **"Kill Team 2024 (KT24 / 3rd Edition)"** section, 20 terms, all `draft`. Six existing 40K entries (Cover, Charge, Engagement Range, Command Point, plus the "Other game systems" Kill Team stub) gained **additive** collision-flag paragraphs - no 40K definition text was removed or altered. Frontmatter changed `system: warhammer_40k_11e` to `system: multi_system` / `systems: [...]`. Appended an "L1 note" dated 2026-08-17 |
| `KB/overview.md` | New **"Second system: Kill Team 2024"** section stating the cross-game rules-split / models-cross-over policy; "First system" section's "currently only system" claim corrected; "Current state" metrics table updated to cover both systems; frontmatter made multi-system; Related pages extended |
| `KB/index.md` | New **"Kill Team 2024 (KT24)"** section with its own Sources/Concepts tables, deliberately kept separate from the 40K tables rather than interleaved; status banner and frontmatter updated to multi-system |
| `KB/log.md` | Ingest entry `## [2026-08-17] ingest \| L1 kill_team_2024_scaffold ...` appended; frontmatter made multi-system |
| `KB/changelog.md` | One row: no promotion, reasoning stated (nothing above `draft`, owned PDF unread) |

**Total: 7 created, 5 updated - 12 pages, within the `KB/ingest_procedure.md` 5-15 page expectation for a meaningful ingest.**

---

## The naming deviation this slice owns

**What the task suggested.** `engagement_range_kill_team.md`, pattern-matching Warhammer 40,000's "Engagement Range" term for the new KT24 concept page covering positional control.

**What Wahapedia's Core Rules page actually names it.** **Control Range** - "something is within an operative's control range if it's visible to and within 1" of that operative" - used to decide marker contests (by total APL), cover eligibility, Fight legality, and move restrictions.

**Why the difference matters, not just the label.** 40K's Engagement Range is a pure geometric test (2" horizontal / 5" vertical, no visibility component) deciding melee/movement legality. KT24's Control Range is visibility-gated at a much shorter 1" and decides a different set of questions (marker control by APL total, not melee legality alone). Naming the KT24 page after the 40K term would have implied a shared mechanic that does not exist - exactly the failure mode [`AGENTS.md`](../../../../AGENTS.md) Sec 9 exists to prevent ("never guess a rules term - check the glossary first").

**What was done about it.** Filed as `KB/concepts/control_range_kill_team.md`. The page opens with an explicit "Naming note" section recording the brief's suggestion, why it was not used, and pointing to the correct term. The deviation is also recorded in `glossary.md`'s new L1 note, in `KB/log.md`, and here - three independent places so it cannot quietly get "corrected" back to the wrong name by a future pass that only skims one of them.

---

## Collision flags applied

Six term pairs, each flagged **in both directions** (the 40K entry names and links the KT24 entry, and vice versa):

| Term | 40K meaning | KT24 meaning | Direction of difference |
|------|-------------|--------------|--------------------------|
| **Cover** | Worsens attacker's BS by 1 | Grants defender a free retained defence success | Opposite mechanical direction (attacker penalty vs defender bonus) |
| **Charge** | 12" declare, 2D6 roll, move that far | 1AP move action, Move+2", no roll | Different action types entirely - one is chance-based, one is deterministic |
| **Engagement Range / Control Range** | Fixed 2"/5" zone, no visibility test | Visibility-gated 1" zone, decides marker APL contests | The naming-deviation pair - see above |
| **Command Point (CP)** | Flat 1 CP/player/round, spent on stratagems | 1 CP normally but 2 CP for the non-initiative player, spent on ploys | Same *role* (resource for one-off effects), different gain rule and spend target |
| **Engage (order) vs Engagement Range** | N/A (40K has no order system) | A per-activation order state, unrelated to any distance | Not a shared mechanic at all - a pure naming collision |
| **Injured vs Battle-shock** | Failed Ld test, unit-strength-gated, zeroes OC/stratagem targeting/actions | Individual model's Wounds crossing a fixed threshold, worsens Move/Hit | Different trigger, different effect - "your unit got worse" is the only thing they share |

Applied on both sides in every case: the existing 40K entry in `glossary.md`'s core-rules section, and the new KT24 entry in the new section, each carrying a "**Collision flag**" paragraph naming and linking the other.

---

## Confidence and honesty check

Every one of the 7 new pages, and every one of the 20 new glossary terms, is `draft` - none is `verified`. This matches the reasoning `v1_scaffold`'s L1 used for its first 40K ingest, applied identically here: a single living-reference cross-check, not a read of the owned PDF, does not clear the bar for `verified`. No page in this slice overstates what was actually checked.

The **owned Core Rules PDF status** is the biggest open item this leaves behind: `raw/pointers/kill_team_2024_core.md` also names an unread Core Rules **update log** PDF, and Wahapedia's own book-version table shows a "June 2026" revision one step ahead of "February 2026" - meaning the rules have moved at least once since KT24 launched, and this pass cannot say whether the owned Full-Scan PDF reflects that move. Flagged on `kill_team_2024_core_rules.md` rather than guessed either way.

---

## Tier 1 self-check

| # | Criterion | Result | Evidence |
|---|-----------|--------|----------|
| 1 | 7 new pages created | PASS | `Test-Path` on each, see `L1_brief.md` Tier 1 commands |
| 2 | Frontmatter + `system: kill_team_2024` + `confidence` on every new page | PASS | 7/7 |
| 3 | Glossary carries a dedicated KT24 section | PASS | "Kill Team 2024 (KT24 / 3rd Edition)" heading present |
| 4 | Collision flags bidirectional, 40K side additive only | PASS | 6 term pairs; 40K entries gained flag paragraphs, no existing 40K text removed |
| 5 | Overview states the second system exists and the KT/40K miniature relationship | PASS | New "Second system" section |
| 6 | Index carries every new page, in a separated KT24 section | PASS | 7 rows across 2 KT24 sub-tables |
| 7 | Log entry dated 2026-08-17 | PASS | `## [2026-08-17] ingest \| L1 kill_team_2024_scaffold ...` |
| 8 | Changelog records the no-promotion reasoning | PASS | Row added |
| 9 | Every rules claim sourced with a verification route | PASS | Wahapedia URL + retrieval date, or owned-pointer path, on every claim |
| 10 | Naming deviation recorded (not silently applied) | PASS | Recorded on the page, in glossary, in log, and here |
| 11 | Wikilinks resolve | PASS | 0 broken - checked against the full `KB/` filename set including the 7 new pages |
| 12 | **`raw/` untouched** | PASS | No creates, edits, or deletes under `raw/` |
| 13 | No GW binaries added | PASS | 0 new `.pdf`/`.webp`/`.png`/`.jpg` |
| 14 | No verbatim rules text | PASS | Teaching paraphrase throughout; Wahapedia fragment quoted only in the cached fetch tool output, never pasted into a KB page |
| 15 | All files UTF-8 | PASS | Written directly as UTF-8; no editor round-trip through a UTF-16-prone path this pass |
| 16 | No commit by this slice | PASS | No git write command issued |
| 17 | Nothing promoted to `docs/` or `games/` | PASS | `changelog.md` states why |

---

## Lint (self-run, scoped to this slice's pages)

| Check | Result |
|-------|--------|
| Broken wikilinks in the 7 new pages + edited core files | **0** |
| Missing frontmatter on new pages | **0** of 7 |
| Missing `confidence` on new pages | **0** of 7 |
| Index rows missing for a new page | **0** |
| 40K glossary entries altered beyond an added collision-flag paragraph | **0** |
| Rules claims without a verification route | **0** |

**Not run:** a full repo-wide re-lint across the 40K content (that is `v1_scaffold`'s L2 territory, out of scope here) and any check requiring the owned KT24 PDFs to be open.

---

## Findings for the Coordinator

### Finding 1 - Wahapedia's KT3 book-version table shows the rules have already moved once

The Core Rules page's "Books" table lists the Core Book at **June 2026**, one row above an earlier **February 2026** version. This means KT24's Core Rules have received at least one revision since the game's original launch, and this pass has no way to know whether the owned `779937548-Core-Rules-KILL-TEAM-3E-Full-Scan.pdf` reflects the June 2026 state or the February 2026 (or earlier) state. `raw/pointers/kill_team_2024_core.md` separately lists an unread **Core Rules update log** PDF that most likely answers this. Recommend prioritizing that PDF early in S1, before teaching content locks in specific numbers from the Full-Scan PDF.

### Finding 2 - the owned PDF remains completely unread by any Librarian pass

Every KT24 claim in this ingest traces to Wahapedia, not to the PDF the owner actually paid for. This is structurally identical to the gap `v1_scaffold` L0/L1 opened for 40K (schema and glossary seeded from familiarity/aggregators, core rules not yet read) - and it closed the same way there: an Implementer slice with file access (S3) opened the owned PDFs and the Librian's next pass (L2) reconciled the KB against what was actually read. Recommend the same shape here: S1/S2 (Implementer, file access) reads the owned PDF and lite rules; a later Librarian slice (L2 or equivalent) upgrades `draft` to `verified` where the two sources agree, and flags anywhere they don't.

### Finding 3 - no filename or encoding defects found this pass

Unlike `v1_scaffold` L1 (which hit a UTF-16LE defect across every written file), this environment wrote all 12 touched files as UTF-8 directly. No byte-level conversion was required. Flagged here only so QA does not spend time re-deriving the check `v1_scaffold` needed - it is not needed this time, but confirm rather than assume.

---

## Blockers

None blocking S1. S1 can start immediately using `kill_team_2024_core_rules.md` as its Tier 0 handoff.

Threads carried rather than resolved:

| Thread | Status | Owner |
|--------|--------|-------|
| Owned Core Rules PDF, lite rules, update log, universal equipment, sniper update - all unread | Open from Preflight/S0 | S1/S2 (Implementer, file access) |
| Wahapedia June 2026 vs February 2026 Core Book version gap | New this pass | S1, before teaching content locks in numbers |
| Ten owned team-rule PDFs, killzones, Critical Ops, Nemesis Operatives | Open from Preflight/S0 | S2-S9 per `track_in.md` rollup |
| Hierotek Circle 40K photo ID | Carried from the 40K track | User photos |

---

## Inherited documentation (paste-ready for the S1 brief)

> **Tier 0 - Knowledge ready: PASS.** The KB now holds 1 KT24 source page and 6 KT24 concept pages, all `draft`. Every path below is real.
>
> **Read before starting:**
> - [`KB/sources/kill_team_2024_core_rules.md`](../../../../KB/sources/kill_team_2024_core_rules.md) - what was cross-checked, what was not, and the update-log gap
> - [`AGENTS.md`](../../../../AGENTS.md) - schema source of truth, now covering two systems
> - [`KB/index.md`](../../../../KB/index.md) - master catalog, Kill Team 2024 section
> - [`KB/glossary.md`](../../../../KB/glossary.md) - the new KT24 section, **and every collision flag** - read these before writing any shipping glossary content, so the same six terms don't get redefined inconsistently
> - [`KB/overview.md`](../../../../KB/overview.md) - the cross-game policy in plain prose
> - [`KB/log.md`](../../../../KB/log.md) - append an entry for any KB work
>
> **What S1 may teach as fact:** the turning-point / Strategy-Firefight structure; activation/APL/counteract mechanics; Engage/Conceal orders; Control Range; Cover and Obscured as described; the Injured threshold - all as understood from Wahapedia's Core Rules page, retrieved 2026-08-17.
>
> **What S1 must not teach as fact without its own check:** any exact wording that might have changed between the February 2026 and June 2026 Core Book revisions Wahapedia's table shows; anything from the lite rules, update log, universal equipment, or sniper-rules-update PDFs (all unread); any team-specific, killzone-specific, or Critical-Ops content.
>
> **Do not propagate:** "Engagement Range" as a Kill Team term (it is Control Range - see the naming-deviation note on `control_range_kill_team.md`); any suggestion that KT24 Cover works like 40K Cover, or that KT24 Injured works like 40K Battle-shock.
>
> **Conventions that apply to anything you write:**
> - `KB/**` uses YAML frontmatter only; `games/**` and `docs/**` use Rising Tide headers and footers
> - Every claim needs an honest `confidence` and a verification route; living-reference claims need a retrieval date
> - **Teaching paraphrase only.** No GW binaries, no verbatim rules text
> - `games/kill_team_2024/` uses `teams/`, not `armies/`, per the vocabulary mapping in its `README.md`
>
> **Hard rules:** never write under `raw/`; never `git commit` or `git push` (Coordinator only); never use `claude-fable-5-thinking-high`.
>
> **Open threads:** the owned PDFs remain unread; the June 2026 update-log gap; ten team PDFs, killzones, Critical Ops, Nemesis Operatives all pending; Hierotek Circle 40K photo ID (carried from the 40K track).

---

## Next

**S1** - Kill Team 2024 rules teaching docs under `games/kill_team_2024/rules/`. Tier 0 entrance is satisfied; paste the inherited block above into `S1_brief.md`. Recommend S1 open the owned Core Rules PDF and the update log first, since this slice could only cross-check against a community aggregator.
