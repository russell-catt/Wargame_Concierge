# S2 — Brief (Sources + Necron import)

- **Status:** Resolved — Implemented (awaiting QA)
- **Track:** v1_scaffold
- **Slice:** S2 (Implementer, Tier 1)
- **Tier:** 1 — Implementation

## Requirements

1. `reference/Source_Library.md` — local library path pointers under `C:\Personal\40K`, living web refs, copyright note, Preflight Necron_Lists import note
2. Copy `C:\Personal\40K\rules\Necron_Lists.md` → `raw/Necron_Lists.md` AND `games/warhammer_40k_11e/armies/necrons/Necron_Lists.md`
3. `games/warhammer_40k_11e/` scaffold: README, rules/setup stubs, army READMEs, inventories, units stubs
4. `raw/pointers/` stubs pointing at Source_Library paths (markdown only)
5. `S2_brief.md`, `S2_implementer.md`; update `track_in.md`

### Ownership facts (must match Preflight)

| Item | Qty | Status |
|------|-----|--------|
| Necron Warriors | 10 | Purchased, unassembled |
| Canoptek Scarab Swarms | 3 | Purchased, unassembled |
| Immortals | 5 | Purchased, unassembled |
| Hierotek Circle Kill Team | 1 set | Game ready; unit ID pending photos |
| Kill Team: Tomb World | — | **Not owned** |

## Depends / User gate

| Dependency | Notes |
|------------|-------|
| S1 Resolved — Implemented | YES |
| Do NOT commit | Coordinator only |
| Do NOT push | S7 user gate |
| MAY write `raw/` | Necron_Lists.md import only (Coordinator authorized) |
| Do NOT write `KB/` | Librarian owns it |

## Entrance criteria

| Criterion | Attested |
|-----------|----------|
| S1 shipping docs exist | YES |
| Preflight-updated `Necron_Lists.md` at source | YES |
| `docs/Project_Planning.md` Sec 3 ownership facts | YES |

## Exit criteria

- `reference/Source_Library.md` exists with paths only (no binaries)
- Necron_Lists.md copied to both repo paths; byte-identical to source
- `games/warhammer_40k_11e/` subtree per scaffold Section B/C stubs
- `Owned_Models_Inventory.md` (Necrons) mirrors Preflight FOUNDATION
- `raw/pointers/` contains markdown stubs (no binaries)
- Handoffs present; `track_in.md` updated
- All new files UTF-8 without BOM
- **`KB/` untouched**
- **No commit, no push**
- No GW binaries in repo

## Tier 1 commands

```powershell
$root = "C:\Personal\Personal_Projects\Wargame_Concierge"
$src = "C:\Personal\40K\rules\Necron_Lists.md"

@(
  "reference\Source_Library.md",
  "raw\Necron_Lists.md",
  "games\warhammer_40k_11e\README.md",
  "games\warhammer_40k_11e\armies\necrons\Necron_Lists.md",
  "games\warhammer_40k_11e\armies\necrons\Owned_Models_Inventory.md",
  "docs\handoffs\v1_scaffold\slices\S2_brief.md",
  "docs\handoffs\v1_scaffold\slices\S2_implementer.md"
) | ForEach-Object { "{0,-70} {1}" -f $_, (Test-Path "$root\$_") }

(Get-FileHash $src).Hash -eq (Get-FileHash "$root\raw\Necron_Lists.md").Hash
(Get-FileHash $src).Hash -eq (Get-FileHash "$root\games\warhammer_40k_11e\armies\necrons\Necron_Lists.md").Hash
(Get-ChildItem "$root\raw\pointers" -Filter *.md).Count
```

## Recommended models

| Role | Model |
|------|-------|
| Implementer | `composer-2.5-fast` |
| QA | `gemini-3.7-flash-high` |

## Feeds

**L1** ingests from `raw/Necron_Lists.md` and pointer stubs. **S3** fills rules/setup stubs.