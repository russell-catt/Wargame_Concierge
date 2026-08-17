# S0 — Brief (Bootstrap handoffs)

- **Status:** Ready
- **Track:** `tomb_world_ownership`
- **Slice:** S0

## Requirements

1. Create `docs/handoffs/tomb_world_ownership/` and `docs/handoffs/tomb_world_ownership/slices/`
2. Write `track_in.md` with locked ownership decision, model matrix, per-slice assignments, rollup, depends chain, git notes
3. Write brief stubs: `S0_brief.md` through `S4_brief.md`, `L1_brief.md`, `L2_brief.md`
4. Update `docs/handoffs/README.md` — register track as Active (In Progress)
5. Update `docs/operations/multiagent_coordinator_strategy.md` handoffs table (minimal edit)
6. Write `S0_implementer.md` with Tier 1 self-check

## Exit criteria

- Paths exist under `docs/handoffs/tomb_world_ownership/`
- `track_in.md` records locked models and ownership decision
- All slice briefs present (S0–S4, L1–L2)
- `docs/handoffs/README.md` lists `tomb_world_ownership` as Active
- Playbook handoffs table includes `tomb_world_ownership` row
- `S0_implementer.md` status **Resolved - Implemented**
- **No commit, no push**

## Recommended models

| Role | Model |
|------|-------|
| Implementer | `composer-2.5-fast` |
| QA | `gemini-3.7-flash-high` |

## Depends

| Dependency | Notes |
|------------|-------|
| Plan `tomb_world_ownership_sync_cf3be3c8` | Read-only |
| v1_scaffold Closed - Complete | Prior track done; ownership correction follow-up |
| **Commit** | pending — Coordinator at S4 only |
| **Push** | pending — S4 only |