# Preflight — Brief (plan package)

- **Track:** `sm_matched_vs_casual`
- **Slice:** Preflight
- **Status:** Resolved - Implemented (plan package on this PR); **execution gated** until user authorizes
- **Depends:** none
- **User gate:** authorize track + answer open questions before S0 execution
- **Recommended models:** Coordinator `inherit`

## Requirements

1. Create `docs/handoffs/sm_matched_vs_casual/` + `slices/`
2. Write `track_in.md` with goals, naming lock, Legends inventory, model matrix, slice map, Librarian scope, open questions
3. Stub briefs: Preflight, S0–S5, L0–L2
4. Register track in `docs/handoffs/README.md`
5. Minimal row in playbook handoffs table (`multiagent_coordinator_strategy.md`)

## Exit criteria

- [x] Track folder + `track_in.md` exist
- [x] Slice briefs S0–S5 and L0–L2 present
- [x] Handoffs README lists track as Open (awaiting auth)
- [ ] User authorized execution (blocks S0 In progress)
- [ ] Servitors Legends (PR #6) merged or cherry-picked before Casual S3/S4

## Constraints

Never write `raw/`. Plan-only until authorized. Subagents never git.
