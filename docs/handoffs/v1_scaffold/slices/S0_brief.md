# S0 — Brief (Bootstrap)

- **Status:** Ready
- **Track:** v1_scaffold
- **Slice:** S0

## Requirements

1. Create `C:\Personal\Personal_Projects\Wargame_Concierge` as **own git root** (`git init`; no commit)
2. Copy ALL templates from `recipe_book/templates/` -> `templates/`
3. Copy and adapt `multiagent_coordinator_strategy.md` -> `docs/operations/` (Wargame headers; v1_scaffold handoffs table; L0/L1/L2 Librarian slices)
4. Create `docs/handoffs/README.md` + `v1_scaffold/` track folder with briefs and reports
5. Create `.gitignore` (no GW binaries; allow `.md` and `.obsidian`)
6. Create `raw/`, `KB/` skeleton dirs (no `index.md`, no `AGENTS.md`, no `.obsidian`)
7. Create stub READMEs: `checkins/`, `prompts/`, `games/`, `raw/pointers/`

## Depends / User gate

| Dependency | Notes |
|------------|-------|
| Preflight Resolved - Complete | YES |
| Do NOT commit | Coordinator only |
| Do NOT push | S7 user gate |

## Entrance criteria

| Criterion | Attested |
|-----------|----------|
| Preflight PASS | YES |
| `Necron_Lists.md` ownership updated at source | YES (2026-08-16) |

## Exit criteria

- Project directory exists with `git init` (no commits)
- All 11 template files under `templates/`
- Playbook adapted with v1_scaffold handoffs row + L0/L1/L2 references
- `track_in.md` with slice rollup + model matrix + Preflight notes
- Preflight + S0 briefs and Preflight implementer/QA reports present
- `raw/`, `KB/{sources,concepts,factions,detachments,units,setup,analyses}/` exist (stubs only)
- `.gitignore` blocks `*.pdf`, `*.webp`, secrets, scratchpad; allows markdown
- **No GW binaries copied**
- **No** `AGENTS.md`, `KB/index.md`, or `.obsidian/` created

## Tier 1 commands

```powershell
$root = "C:\Personal\Personal_Projects\Wargame_Concierge"
Test-Path "$root\.git"
Test-Path "$root\templates\README.md"
Test-Path "$root\docs\operations\multiagent_coordinator_strategy.md"
Test-Path "$root\docs\handoffs\v1_scaffold\track_in.md"
Test-Path "$root\KB\sources\.gitkeep"
Test-Path "$root\raw\README.md"
-not (Test-Path "$root\AGENTS.md")
-not (Test-Path "$root\KB\index.md")
-not (Test-Path "$root\.obsidian")
@(Get-ChildItem $root -Recurse -Include *.pdf,*.webp -File -ErrorAction SilentlyContinue).Count -eq 0
git -C $root status
```

## Tier 2 expectations

QA confirms paths, playbook handoffs table, track_in slice table, and absence of forbidden L0 artifacts / GW binaries.

## Recommended models

| Role | Model |
|------|-------|
| Implementer | `composer-2.5-fast` |
| QA | `gemini-3.7-flash-high` |

## Inherited documentation

- Plan: `wargame_concierge_setup_ee78aead.plan.md` S0 + Repo layout
- Playbook source: daily_report `multiagent_coordinator_strategy.md` v1.2
- Templates source: `recipe_book/templates/`
