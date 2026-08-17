# S6 — Implementer report (Angels of Death full package + 40K Space Marine sync)

- **Status:** Resolved - Implemented (awaiting QA)
- **Track:** kill_team_2024_scaffold
- **Slice:** S6 (Implementer — teaching content)
- **Model used:** `claude-sonnet-5-thinking-high` (LOCKED)
- **Date:** 2026-08-17
- **Paths touched:** `games/kill_team_2024/teams/angels_of_death/`, `games/kill_team_2024/teams/_Owned_Teams_Inventory.md`, `games/kill_team_2024/teams/README.md`, `games/warhammer_40k_11e/armies/space_marines/Owned_Models_Inventory.md`, `games/warhammer_40k_11e/armies/space_marines/README.md`, `docs/handoffs/kill_team_2024_scaffold/slices/`
- **`KB/` untouched:** YES
- **`raw/` untouched:** YES
- **Commit:** none by this slice

> **Supersedes** an earlier minimal `S6_implementer.md` stub (marked "Coordinator closeout") that recorded only a link-only cross-game stub in the 40K Space Marine inventory. This report documents the full S6 package and the full sync table that stub deferred.

---

## Sources read this slice

| Source | Retrieved / status |
|--------|---------------------|
| [Wahapedia — Angel of Death](https://wahapedia.ru/kill-team3/kill-teams/angel-of-death/) | Fetched 2026-08-17 — full page: operative selection list, both Faction Rules (Chapter Tactics, Astartes), 4 Strategy Ploys, 4 Firefight Ploys, 4 Faction Equipment items, all 9 datacards, keywords. **Note:** the URL in the task text used the plural "angels-of-death" and 404s; the live Wahapedia slug is singular "angel-of-death" — confirmed via search and recorded in every source citation this slice |
| [tabletopbattles.com — KT24 Angels of Death review](https://www.tabletopbattles.com/kill-team-2024-review-angels-of-death) | Fetched 2026-08-17 (Goonhammer-network published review) — used only for tactical framing (why the sniper/gunner choice matters, roster shape); no text copied, all pages here paraphrased fresh |
| `raw/pointers/kill_team_2024_teams.md` → local team-rules PDF | **Not opened this slice** — pointer only, per Librarian-never-opens-binaries convention. Package is `draft` pending that cross-check |
| `games/kill_team_2024/rules/{Overview,Turn_Structure,Key_Concepts}.md` | Read for shared-mechanic vocabulary (APL, Orders, control range, Injured) reused in the laminate and team rule guide |
| `games/kill_team_2024/teams/canoptek_circle/*`, `games/kill_team_2024/teams/plague_marines/*` (S4/S5 output) | Read mid-slice — confirmed file set, header conventions, and cross-game-note style matched this package |
| `games/warhammer_40k_11e/armies/space_marines/{README,Owned_Models_Inventory,Quick_Reference_Play_Guide}.md`, `units/Unit_Index.md` | Read to confirm 40K datasheet names (Captain, Intercessor Squad, Assault Intercessor Squad, Eliminator Squad, Heavy Intercessor Squad) for the sync table, and to find the earlier Coordinator-closeout stub already sitting in the inventory file |

---

## Created

### Angels of Death package (7 files)

| Path | Purpose |
|------|---------|
| `games/kill_team_2024/teams/angels_of_death/README.md` | Package entry point — replaced S3 placeholder; identity, roster shape (1 leader + 5-of-6 operatives, only Intercessor Warrior repeatable), document index, 40K cross-game note |
| `games/kill_team_2024/teams/angels_of_death/Team_Rule_Guide.md` | Astartes and Chapter Tactics taught in full (all 8 tactics summarized); 4 strategy ploys, 4 firefight ploys, 4 faction equipment items given as one-line paraphrased gists — no ploy/equipment text transcribed |
| `games/kill_team_2024/teams/angels_of_death/Owned_Models_Inventory.md` | Empty audit worksheet (roster checklist by operative, with base size and matching 40K datasheet name) + the Space Marine 40K sync cross-link |
| `games/kill_team_2024/teams/angels_of_death/Starter_Roster.md` | Two original six-operative rosters (sniper-forward / gun-line) built fresh from the team's own selection rule, explaining the Eliminator-vs-Heavy-Intercessor trade-off — not copied from any published sample list |
| `games/kill_team_2024/teams/angels_of_death/Quick_Reference_Play_Guide.md` | Two-page laminate — Astartes/Chapter Tactics/ploy cheat sheet, build note on page 1; operative role table, do/don't, pre/post-game checklists on page 2 |
| `games/kill_team_2024/teams/angels_of_death/operatives/Operatives_Index.md` | 9-entry role table (3 leaders + 6 operative-list entries) — role paragraph, base size, one build-defining trait each. **No APL/Move/Save/Wounds or weapon Atk/Hit/Dmg** |
| `games/kill_team_2024/teams/angels_of_death/cards/Card_Schema.md` | Field-contract schema only (matches the S4/S5 pattern) — **no per-operative cards generated**, explicitly deferred to S10 |

### Handoffs (2 files)

| Path |
|------|
| `docs/handoffs/kill_team_2024_scaffold/slices/S6_brief.md` |
| `docs/handoffs/kill_team_2024_scaffold/slices/S6_implementer.md` (this file, supersedes the Coordinator-closeout stub) |

## Modified

| Path | Change |
|------|--------|
| `games/kill_team_2024/teams/_Owned_Teams_Inventory.md` | Angels of Death row: priority → "Full guide — S6 complete"; 40K ruled-in → `known` (mapped to Space Marine Captain/Intercessor-family units). Added a "Cross-game notes (Space Marine teams)" section. Bumped to v1.3 with changelog entry |
| `games/kill_team_2024/teams/README.md` | Folder-map row for `angels_of_death/` updated to "S6 complete"; top-line status updated to "S3–S6 complete"; changelog v0.5 entry |
| `games/warhammer_40k_11e/armies/space_marines/Owned_Models_Inventory.md` | Replaced the earlier link-only Coordinator stub with a full **"Kill Team ownership sync — Angels of Death"** section: a 5-row table mapping 40K datasheet → KT operative(s) → base size (Wahapedia) → provenance ("Kill Team (Angels of Death)") → dual-legal (`pending check`), plus explicit guardrails against treating "available via KT ownership" as confirmed ownership or dual-legality. Bumped to v2.2 with changelog entry (retains the earlier v2.1 entry as history) |
| `games/warhammer_40k_11e/armies/space_marines/README.md` | Added a one-line cross-game backlink under Sources pointing at the new sync section; bumped to v2.1 with changelog entry |

---

## 40K sync decision (per brief)

| Field | Value | Rationale |
|-------|-------|-----------|
| Existing 40K Space Marine inventory? | **Yes** | Full army folder already exists (`games/warhammer_40k_11e/armies/space_marines/`), unlike Death Guard in S5 |
| 40K ruled-in | `known` — mapped to specific datasheets | Angels of Death is built entirely from Intercessor-family kits with a clean 1:1 mapping to existing 40K unit research files |
| Base size | Recorded from the living Wahapedia KT datacard footer (physical spec, not rules text): Captain 40mm, Intercessor-family sergeants/warriors/gunners 32mm, Eliminator Sniper and Heavy Intercessor Gunner 40mm | Needed for the dual-legality check; explicitly **not** treated as a 40K legality claim on its own |
| Dual-legal for 40K on this base? | `pending check`, every row | No faction-pack base-size audit performed this slice — would be inventing legality otherwise |
| Assembly / paint | `pending check` | No photo audit this slice (S10 gate), matching the KT-side worksheet |
| SM inventory rows moved into Game-ready? | **No** | Explicitly guarded against in the new section — the underlying 40K collection audit (S5) is still unresolved, so nothing here is promoted out of the sync table |

---

## Exit criteria

| Criterion | Result |
|-----------|--------|
| 7 package files created | PASS |
| `operatives/` and `cards/` subfolders present | PASS |
| Exactly one `<!-- pagebreak -->` in the laminate | PASS |
| No datasheet statlines or verbatim ploy/equipment/ability text | PASS — every table paraphrases role/effect in plain language; base sizes are the only numeric datacard fact carried over, and only because the brief specifically needs them for the dual-legality check |
| Full "Kill Team ownership sync" mapping table in the 40K Space Marine inventory, superseding the link-only stub | PASS |
| Provenance tagged "Kill Team (Angels of Death)"; dual-legality/ownership honestly `pending check` | PASS |
| `_Owned_Teams_Inventory.md` + `teams/README.md` updated | PASS |
| Rising Tide headers, no stacked YAML frontmatter | PASS |
| No GW binaries added | PASS |
| `KB/` / `raw/` untouched | PASS |
| No commit, no push | PASS |

---

## Deferred to later slices

| Item | Target |
|------|--------|
| Opening/cross-checking the local Angels of Death team-rules PDF | Future pass — status stays `draft` until then |
| Space Marine 40K collection audit (Game-ready/build-before-play/Legends fill-in) | Unchanged S5 open item — out of scope for S6 |
| Actual assembly/paint audit for the KT team | User confirm / S10 photos |
| Per-operative printable cards | S10 (user-photo-gated) |
| Base-size / dual-legality confirmation against the 40K Space Marine faction pack | Future audit pass |

---

## Tier 1 self-check

Run commands in `S6_brief.md` at QA closeout.

---

## Pending commit

Bundle with S4 + S5 when Coordinator / user authorizes git, per `track_in.md`'s recommended gate ("S4 / S5 / S6 (each Resolved-Complete)").
