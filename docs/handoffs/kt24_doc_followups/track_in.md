# Track in — kt24_doc_followups

- **Project:** Wargame_Concierge
- **Track:** `kt24_doc_followups`
- **Status:** Open (parked; not scheduled)
- **Date filed:** 2026-08-18
- **Git root:** `C:\Personal\Personal_Projects\Wargame_Concierge`
- **Handoffs root:** `docs/handoffs/kt24_doc_followups/`
- **Playbook:** `docs/operations/multiagent_coordinator_strategy.md`
- **Parent tracks:** `flowcharting_uml` (cheat sheet restyle), `kt24_rules_quotes` (cards + quote exception)

Owner to-dos parked so they are not lost. **This filing does not implement** print layout, freshness stamps, or card completeness. Do not restyle the cheat sheet. Do not fill Geomancer. Do not commit.

## Goals (open work)

### 1. Print — US Letter landscape (not A4)

**Addressed 2026-08-26** — [`Target_Eligibility_Cheat_Sheet.html`](../../../games/kill_team_2024/rules/Target_Eligibility_Cheat_Sheet.html) uses Letter landscape, full-width flowchart (page 1), reference panel (page 2). Fixed 280px sidebar removed.

~~Format `games/kill_team_2024/rules/Target_Eligibility_Cheat_Sheet.html` so it prints on **US Letter landscape**.~~

### 2. Freshness dates on Kill Team docs/cards

Note the date of the **latest rule set** so users know if info is stale.

**Pattern:** parse `eng_DD-MM_` from owned `eng_*` team PDFs / pointers in `raw/pointers/kill_team_2024_teams.md`.

**Canoptek Circle example:**

| Item | Value |
|------|--------|
| Latest PDF | `eng_29-04_kill_team_team_rules_canoptek_circle-bizfljpjib-cb15prhbqo.pdf` |
| Freshness | **April 29, 2026** (`eng_29-04_` → 29 Apr) |
| Pointer | `raw/pointers/kill_team_2024_teams.md` |
| On-disk | `C:\Personal\Kill Team\kill_team_2024\Teams\` |

Apply the same pattern to **unit cards** and other KT documentation. Card footers today often show ingest date (e.g. Geomancer: `Source: local Teams PDF 2026-08-17`), which is not the ruleset date.

**Do not** mass-stamp dates in this filing pass. Implementation is later work.

### 3. Operative cards complete

Kill Team operative HTML cards must include **all rules and abilities**.

**Example (spot-read 2026-08-18):** `games/kill_team_2024/teams/canoptek_circle/cards/Geomancer.html` names three unique actions (`Geomantic Disturbance`, `Canoptek Control`, `Molecular Breach`) then defers with “see team PDF.” **1AP action costs and full action text are missing.**

Audit **all** cards under `games/kill_team_2024/teams/**/cards/` against local Teams PDFs (read in place; never copy binaries into git).

**Inventory as of filing (12 HTML cards):**

| Team | Cards |
|------|--------|
| Canoptek Circle | `Geomancer.html`, `Macrocyte_Accelerator.html`, `Macrocyte_Reanimator.html`, `Macrocyte_Warrior.html`, `Tomb_Crawler.html` |
| Plague Marines | `Bombardier.html`, `Champion.html`, `Fighter.html`, `Heavy_Gunner.html`, `Icon_Bearer.html`, `Plaguecaster.html`, `Warrior.html` |

Some cards already label 1AP abilities (e.g. Accelerator, Reanimator, Plaguecaster, Fighter). Completeness still needs a PDF audit — do not assume those four are done.

**Quoting:** Cards may quote verbatim under `games/kill_team_2024/` per `AGENTS.md` Sec 10. Teaching paraphrase in `KB/`. Personal use only. **Kill Team is Copyright Games Workshop Limited 2024.**

## Locked sources (read in place)

| Source | Path |
|--------|------|
| Team PDF pointers | `raw/pointers/kill_team_2024_teams.md` |
| Teams library | `C:\Personal\Kill Team\kill_team_2024\Teams\` |
| Cheat sheet | `games/kill_team_2024/rules/Target_Eligibility_Cheat_Sheet.html` |
| Cards glob | `games/kill_team_2024/teams/**/cards/` |
| Quote / copyright | `AGENTS.md` Sec 10 |

**KT24 hierarchy (do not invert):** Full-Scan Core Book is baseline; dated `eng_*` patches supersede on the same topic; Jul 25 lite is simplified intro — omission is not a patch.

## Constraints

- Personal use only — this project must never be sold
- Never ingest or commit GW PDFs/images
- Librarian never writes `raw/`
- Subagents do not `git commit` or `git push`
- Do not implement the three to-dos in the same session that only files this track
- Slices not scheduled yet — Coordinator splits when ready

## Rollup

| Item | Status |
|------|--------|
| Track filing (`track_in.md` + Active tracks row) | This pass |
| Optional one-line open note on `games/kill_team_2024/rules/README.md` | This pass |
| Slice 1 — US Letter print CSS | Open |
| Slice 2 — freshness dates from `eng_DD-MM_` | Open |
| Slice 3 — card completeness vs Teams PDFs | Open |
