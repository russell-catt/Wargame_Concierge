# S0 — Brief (naming + file scaffold)

- **Track:** `sm_matched_vs_casual`
- **Slice:** S0
- **Status:** Draft — awaiting track authorization
- **Depends:** Preflight Complete + user auth + working branch
- **User gate:** authorize track
- **Recommended models:** Implementer `inherit` · QA different family when available

## Inherited documentation

- [`track_in.md`](../track_in.md) naming lock
- `games/warhammer_40k_11e/armies/space_marines/Starter_{250,500,750,1000}.md`
- SM `README.md`, `Owned_Models_Inventory.md`

## Requirements

1. Document Matched / Casual / shim convention in SM `README.md` (short dual-path section).
2. Create `Starter_{N}_Matched.md` by copying current `Starter_{N}.md` content (all four N).
3. Create `Starter_{N}_Casual.md` stubs: banner **Casual — Legends allowed**, link to Matched twin, empty Legends add-on table, “do not use in matched play.”
4. Replace each `Starter_{N}.md` with a **thin shim**: one paragraph + links to Matched (default) and Casual.
5. Write `S0_implementer.md` Tier 1 self-check.

## Exit criteria (QA verifies)

- [ ] Eight new files exist (`*_Matched` + `*_Casual` × 4)
- [ ] Four shims at old paths; old deep links still resolve
- [ ] Every Matched/Casual page has the correct banner
- [ ] No Legends units costed on Matched files yet beyond what current starters already say (S1–S2 will scrub)
- [ ] No `raw/` writes; no binaries; UTF-8 no BOM
- [ ] Subagent did not git commit/push

## Constraints

Codex wall. Prefer update-in-place over extra near-duplicates outside the naming scheme.
