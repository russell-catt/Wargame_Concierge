# S5 — Implementer report (Plague Marines full package + 40K sync note)

- **Status:** Resolved - Implemented (awaiting QA)
- **Track:** kill_team_2024_scaffold
- **Slice:** S5 (Implementer — teaching content)
- **Model used:** `claude-sonnet-5-thinking-high` (LOCKED)
- **Date:** 2026-08-17
- **Paths touched:** `games/kill_team_2024/teams/plague_marines/`, `games/kill_team_2024/teams/_Owned_Teams_Inventory.md`, `games/kill_team_2024/teams/README.md`, `games/warhammer_40k_11e/armies/death_guard/README.md`, `docs/handoffs/kill_team_2024_scaffold/slices/`
- **`KB/` untouched:** YES
- **`raw/` untouched:** YES
- **Commit:** none by this slice

---

## Sources read this slice

| Source | Retrieved / status |
|--------|---------------------|
| [Wahapedia — Plague Marines](https://wahapedia.ru/kill-team3/kill-teams/plague-marines/) | Fetched 2026-08-17 — full page: faction rules, strategy ploys, firefight ploys, faction equipment, all 7 datacards, keywords |
| `raw/pointers/kill_team_2024_teams.md` → local team-rules PDF | **Not opened this slice** — pointer only, per Librarian-never-opens-binaries convention. Package is `draft` pending that cross-check |
| `games/kill_team_2024/rules/{Overview,Turn_Structure,Key_Concepts}.md` | Read for shared-mechanic vocabulary (control range, APL, orders, cover) reused in the laminate and team rule guide |
| `docs/Game_System_Scaffold.md` Sec C | Read for the two-page laminate constraints and unit-index/schema conventions, adapted to KT vocabulary |
| `games/kill_team_2024/teams/canoptek_circle/*` (S4 output) | Read mid-slice once it landed — confirmed file set, header conventions, and cross-game-note style matched this package |

---

## Created

### Plague Marines package (7 files)

| Path | Purpose |
|------|---------|
| `games/kill_team_2024/teams/plague_marines/README.md` | Package entry point — replaced S3 placeholder; team-in-a-paragraph, document index, 40K cross-game note |
| `games/kill_team_2024/teams/plague_marines/Team_Rule_Guide.md` | Astartes / Poison / Disgustingly Resilient taught in full; 4 strategy ploys, 4 firefight ploys, 4 faction equipment items given as one-line paraphrased gists — no ploy/equipment text transcribed |
| `games/kill_team_2024/teams/plague_marines/Owned_Models_Inventory.md` | Empty audit worksheet (game-ready / build-before-play / unidentified / not-owned tables) + the Death Guard / 40K sync note |
| `games/kill_team_2024/teams/plague_marines/Starter_Roster.md` | Role-coverage table across all 7 operatives; suggested first-four roster; flags the unconfirmed team-size limit |
| `games/kill_team_2024/teams/plague_marines/Quick_Reference_Play_Guide.md` | Two-page laminate — turning-point checklist, faction rule cheat box, ploy cheat strip, shoot/fight-at-a-glance on page 1; roster snapshot, do/don't, keyword strip, pre/post-game checklists on page 2 |
| `games/kill_team_2024/teams/plague_marines/operatives/Operatives_Index.md` | 7-row table — role slot, base size (32mm, all), faction keywords, paraphrased signature trait, cross-check status. **No APL/Move/Save/Wounds or weapon Atk/Hit/Dmg** |
| `games/kill_team_2024/teams/plague_marines/cards/Card_Schema.md` | Field-contract schema only (adapted from the 40K `units/_schema.md` pattern) — **no per-operative cards generated**, explicitly deferred to S10 |

### Minimal 40K cross-link stub (1 file)

| Path | Purpose |
|------|---------|
| `games/warhammer_40k_11e/armies/death_guard/README.md` | Sync-status fields only (40K ruled-in: `pending / N/A this track`; base size: `pending check`) and an explicit statement that this is **not** a faction package. No army rule guide, detachment, starter list, or unit research created |

### Handoffs (2 files)

| Path |
|------|
| `docs/handoffs/kill_team_2024_scaffold/slices/S5_brief.md` |
| `docs/handoffs/kill_team_2024_scaffold/slices/S5_implementer.md` |

## Modified

| Path | Change |
|------|--------|
| `games/kill_team_2024/teams/_Owned_Teams_Inventory.md` | Plague Marines row: priority → "Full guide - complete (S5)"; 40K ruled-in → `pending / N/A this track`. Added a "Cross-game note (Plague Marines — Death Guard)" section. Updated the "N/A" key-table row to reflect the new usage. Bumped to v1.2 with changelog entry |
| `games/kill_team_2024/teams/README.md` | Folder-map row for `plague_marines/` updated to "S5 complete"; changelog v0.4 entry |

---

## 40K sync decision (per brief)

| Field | Value | Rationale |
|-------|-------|-----------|
| Existing 40K Death Guard inventory? | **No** | Locked 40K scope this track is Necrons + Space Marines only (`games/warhammer_40k_11e/README.md`) |
| 40K ruled-in | `pending / N/A this track` | Nothing to sync into; avoids inventing an army |
| Base size / dual-legality | `pending check` | Wahapedia datacards show 32mm bases for all 7 operatives; exact 40K datasheet mapping unconfirmed |
| Assembly / paint | `pending check` | No photo audit this slice, per track default |
| SM inventory touched? | **No** | Correctly not forced — Space Marines is a different 40K faction; the note belongs with Death Guard, not Space Marines |
| Minimal stub created? | **Yes** | `games/warhammer_40k_11e/armies/death_guard/README.md` — sync fields + explicit "not a package" statement, no rules content |

---

## Exit criteria

| Criterion | Result |
|-----------|--------|
| 7 package files created | PASS |
| `operatives/` and `cards/` subfolders present | PASS |
| Exactly one `<!-- pagebreak -->` in the laminate | PASS |
| No datasheet statlines or verbatim ploy/equipment text | PASS — reviewed every table against the Wahapedia source; all entries are paraphrased gists or role/keyword facts (base size, faction keywords), never Atk/Hit/Dmg, APL/Move/Save/Wounds, or reproduced ability sentences |
| Death Guard / 40K sync note present, honest | PASS |
| Minimal 40K stub created, not a full army tree | PASS |
| `_Owned_Teams_Inventory.md` + `teams/README.md` updated | PASS |
| Rising Tide headers, no stacked YAML frontmatter | PASS |
| No GW binaries added | PASS |
| `KB/` / `raw/` untouched | PASS |
| No commit, no push | PASS |

---

## Deferred to later slices

| Item | Target |
|------|--------|
| Opening/cross-checking the local Plague Marines team-rules PDF | Future pass — status stays `draft` until then |
| Actual assembly/paint audit | User confirm / S10 photos |
| Per-operative printable cards | S10 (user-photo-gated) |
| Full Death Guard 40K army package (if ever scoped) | A future, explicitly-scoped track — see the stub's "If Death Guard ever enters 40K scope" section |
| Team-size / roster-limit confirmation | Cross-check against the local PDF or Kill Team app |

---

## Tier 1 self-check

Run commands in `S5_brief.md` at QA closeout.

---

## Pending commit

Bundle with S4 + S6 when Coordinator / user authorizes git, per `track_in.md`'s recommended gate ("S4 / S5 / S6 (each Resolved-Complete)").
