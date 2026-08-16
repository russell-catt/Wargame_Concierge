# Preflight — Brief (Necron ownership patch)

- **Status:** Resolved - Complete
- **Track:** v1_scaffold
- **Slice:** Preflight

## Requirements

1. Edit **only** `C:\Personal\40K\rules\Necron_Lists.md` in place
2. Replace FOUNDATION with confirmed 2026-08-16 ownership table
3. Reconcile Tomb World as superseded/historical (not current ownership)
4. Adjust Canoptek Court / Cryptek Conclave shopping so owned Warriors, Scarabs, Immortals are not double-counted as retail targets
5. Add Hierotek Circle placeholder + `TODO: Hierotek Circle photo ID -> map to 40K datasheets`
6. Rewrite Phase 1/2 to prefer game-ready Hierotek once IDed; flag unassembled kits as build-before-play

## Depends / User gate

| Dependency | Notes |
|------------|-------|
| User authorized plan execution | YES (2026-08-16) |
| Wargame_Concierge repo | Not required for Preflight |

## Entrance criteria

| Criterion | Attested |
|-----------|----------|
| User confirmed Necron ownership (2026-08-16) | YES |
| Source file exists at `C:\Personal\40K\rules\Necron_Lists.md` | YES |

## Exit criteria

- FOUNDATION table lists Warriors (10), Scarabs (3), Immortals (5), Hierotek Circle (game ready; ID pending)
- Tomb World **not** presented as current ownership
- Shopping phases exclude owned kits from retail "Need" without adjustment notes
- Hierotek photo ID TODO present
- Phase 1/2 acknowledge build-before-play and prefer Hierotek when IDed

## Tier 1 checks

- Read `Necron_Lists.md` FOUNDATION + shopping sections
- Confirm ownership table matches user-confirmed inventory

## Tier 2 expectations

QA independently reads source file; verifies all five exit criteria with evidence quotes.

## Recommended models

| Role | Model |
|------|-------|
| Implementer | `composer-2.5-fast` |
| QA | `gpt-5.6-sol-medium` |

## Inherited documentation

- Cursor plan: `wargame_concierge_setup_ee78aead.plan.md` Preflight section
- Prior blueprint assumed Kill Team: Tomb World — reconcile against confirmed ownership
