# S4 — Brief (Final Sanity + git gate)

- **Status:** Ready
- **Track:** `tomb_world_ownership`
- **Slice:** S4 (Final Sanity, Tier 3)

## Requirements

1. **Final Sanity** (`gpt-5.6-terra-medium`) — cross-slice consistency check:
   - Rollup complete; all slices Resolved - Complete
   - FOUNDATION, army docs, planning, KB agree on Tomb World ownership
   - No orphan false "Tomb World not owned" claims
2. **Coordinator commit + push** — single deferred commit for entire track
3. Commit message:

   ```
   fix(necrons): Tomb World owned game-ready; dual Warriors/Scarabs inventory
   ```

4. Include unpushed `5a7679c` if branch still ahead of remote
5. Write `track_tomb_world_ownership_final_report.md`

## Exit criteria

- Tier 3 Final Sanity PASS
- One Coordinator commit covering S0–L2 work (+ any prior unpushed commits squashed or included per Coordinator decision)
- Push to remote authorized and executed
- Final report written
- Track status → **Closed - Complete**

## Recommended models

| Role | Model |
|------|-------|
| Final Sanity | `gpt-5.6-terra-medium` |
| Coordinator | `inherit` (commit/push) |

## Depends

| Dependency | Notes |
|------------|-------|
| L2 Resolved - Complete | YES |
| All prior slices Resolved - Complete | YES |
| **Commit** | Coordinator executes here |
| **Push** | Authorized at S4 |