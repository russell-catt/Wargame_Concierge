# S1 - Brief (Rules teaching content)

- **Status:** Resolved - Complete
- **Track:** kill_team_2024_scaffold
- **Slice:** S1 (Implementer, Tier 1)
- **Tier:** 1 - Implementation
- **Date:** 2026-08-17

## Requirements

1. `games/kill_team_2024/rules/Overview.md` - what a game of Kill Team is; battles run in turning points; win via VP from ops, not kill count; what a kill team is made of; what you need to play; a coming-from-40K comparison
2. `games/kill_team_2024/rules/Turn_Structure.md` - Strategy phase (Initiative, Ready, Gambit) then Firefight phase (activation loop: Determine Order, Perform Actions, Expended, Counteract), as a table-readable checklist
3. `games/kill_team_2024/rules/Key_Concepts.md` - APL and activation (net APL mod capped at ±1), Orders (Conceal vs Engage), control range, cover vs Obscured, the Shoot sequence, the Fight sequence, Wounded/Injured, mission scoring at a high level (Crit Op / Kill Op / Tac Op)
4. `games/kill_team_2024/rules/Keyword_Glossary.md` - grouped sections, one line per term, plus a dedicated table flagging terms that collide with a different 40K meaning (control range, cover, Charge, Fall Back, CP, Ploy/Stratagem, Save, Wounds, Leader, Objective marker, Datasheet/Datacard, Injured)
5. Update `games/kill_team_2024/rules/README.md` to index the four documents and state confidence

### Vocabulary discipline required by the plan

Use **team / operative**, never **army / unit**, throughout. Match the vocabulary mapping table already established in `games/kill_team_2024/README.md` (S0).

## Depends / User gate

| Dependency | Notes |
|------------|-------|
| S0 Resolved - Complete | YES - stub tree, pointers, and vocabulary mapping exist |
| L1 (KB ingest) | **Not required to block.** Per dispatch instructions: cite KB concepts if L1 has landed them; otherwise cite `raw/pointers/` and Wahapedia directly with a retrieval date, marked `confidence: draft` equivalent. L1 was still `pending` in `track_in.md` at S1 dispatch, so this slice began from the living Wahapedia source directly - **L1 then landed mid-slice** with a matching KB section; this slice reconciled and added KB citations throughout before filing (see `S1_implementer.md`) |
| Do NOT commit | Coordinator only |
| Do NOT push | Never this track unless asked |
| Do NOT write `KB/` | Librarian owns it |
| Do NOT write `raw/` | Immutable layer |
| Do NOT copy PDFs into the repo | Path pointers only |
| Do NOT update `track_in.md` rollup | Coordinator owns it; status noted in `S1_implementer.md` only |

## Entrance criteria

| Criterion | Attested |
|-----------|----------|
| `games/kill_team_2024/rules/README.md` stub exists from S0 | YES |
| `raw/pointers/kill_team_2024_core.md` exists, pointing at the owned local PDF | YES |
| `games/kill_team_2024/README.md` vocabulary mapping table exists | YES |
| A living reference (Wahapedia Kill Team 3 section) is reachable | YES - `https://wahapedia.ru/kill-team3/the-rules/core-rules/`, retrieved 2026-08-17 |

## Exit criteria

- Four new teaching documents exist under `games/kill_team_2024/rules/`
- `rules/README.md` indexes them with an accurate confidence statement
- Every rules claim is teaching paraphrase with a source and a retrieval date; no datacard statlines reproduced
- Glossary entries carry a `draft` / `unverified` status (no PDF cross-check happened this slice, so nothing is marked `verified`)
- Glossary contains a dedicated 40K-collision table
- Rising Tide header and footer on every file; **no YAML frontmatter stacked on top**
- Vocabulary is team/operative throughout, never army/unit
- No GW binaries in the repo
- All new/modified files UTF-8 without BOM
- **`KB/` untouched**, **`raw/` untouched**, **`track_in.md` untouched**
- No commit, no push

## Model

| Field | Value |
|-------|-------|
| Locked (Implementer - content) | `claude-sonnet-5-thinking-high` |
| Actually used | `claude-sonnet-5-thinking-high` |
| Waiver needed | No |
| QA | `gpt-5.6-sol-medium` (different family - playbook Sec 18.7 separation holds) |

## Tier 1 commands

```powershell
$root = 'C:\Personal\Personal_Projects\Wargame_Concierge'

@(
  "games\kill_team_2024\rules\Overview.md",
  "games\kill_team_2024\rules\Turn_Structure.md",
  "games\kill_team_2024\rules\Key_Concepts.md",
  "games\kill_team_2024\rules\Keyword_Glossary.md",
  "games\kill_team_2024\rules\README.md",
  "docs\handoffs\kill_team_2024_scaffold\slices\S1_brief.md",
  "docs\handoffs\kill_team_2024_scaffold\slices\S1_implementer.md"
) | ForEach-Object { "{0,-62} {1}" -f $_, (Test-Path "$root\$_") }

# UTF-8 / no UTF-16 null-byte check
Get-ChildItem "$root\games\kill_team_2024\rules" -Filter *.md -File | ForEach-Object {
  $b = [System.IO.File]::ReadAllBytes($_.FullName)
  $hasNull = ($b | Select-Object -First 400 | Where-Object { $_ -eq 0 }).Count -gt 0
  "{0,-20} utf16null={1}" -f $_.Name, $hasNull
}

# No GW binaries
(Get-ChildItem $root -Recurse -File -Include *.pdf,*.webp,*.png,*.jpg,*.jpeg |
  Where-Object { $_.FullName -notmatch '\\\.git\\' }).Count

# KB, raw, and track_in.md untouched
git -C $root status --porcelain -- KB raw docs/handoffs/kill_team_2024_scaffold/track_in.md
```

## Tier 2 expectations

QA confirms: four documents exist with Rising Tide headers/footers; glossary has the required grouped sections plus the 40K-collision table; every claim traces to a cited source with a retrieval date; no `verified` status claimed anywhere (no PDF was opened); vocabulary is team/operative throughout; no datacard statlines reproduced; `KB/`, `raw/`, and `track_in.md` are untouched.

## Recommended models

| Role | Model |
|------|-------|
| Implementer | `claude-sonnet-5-thinking-high` |
| QA | `gpt-5.6-sol-medium` |

## Inherited documentation

- `track_in.md` - goals, constraints, cross-game policy, model matrix
- `games/kill_team_2024/README.md` - vocabulary mapping (S0)
- `raw/pointers/kill_team_2024_core.md` - local PDF paths (S0)
- Prior 40K teaching-content pattern: `games/warhammer_40k_11e/rules/*.md` (`v1_scaffold` S3), used as the structural and tone template

## Open items handed to S2 / future rules pass

- **PDF cross-check outstanding.** This slice, and L1 (which landed mid-slice with a matching Kill Team 2024 KB section), both worked from the living Wahapedia core rules and Approved Ops 2025 pages only (retrieved 2026-08-17); the owned Core Rules PDF has not been opened by any slice yet. A future rules-verification pass should open it and upgrade both the KB pages and this shipping glossary from `draft` to `verified` where confirmed, flagging any conflicts rather than silently overwriting.
- **KB reconciliation - done.** L1's Kill Team 2024 KB section and six concept pages were reconciled against this slice's shipping docs before filing; no contradictions found (both used the same source, same day). Every shipping document now cites its matching KB page. No further reconciliation work is outstanding.
