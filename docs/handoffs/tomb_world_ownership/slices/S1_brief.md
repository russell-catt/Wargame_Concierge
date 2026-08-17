# S1 — Brief (FOUNDATION sync)

- **Status:** Ready
- **Track:** `tomb_world_ownership`
- **Slice:** S1

## Requirements

Rewrite **FOUNDATION** section in all three authoritative copies:

1. `games/warhammer_40k_11e/armies/necrons/Necron_Lists.md` (project)
2. `raw/Necron_Lists.md`
3. `C:\Personal\40K\rules\Necron_Lists.md` (source library)

Content must reflect:

- **Tomb World game-ready** — Geomancer, Tomb Crawlers, Macrocytes, 10 Warriors, 3 Scarab Swarms
- **Build before play** — Immortals ×5, second Warriors ×10, second Scarabs ×3 (unassembled)
- **Restore playable Phase 1** — Tomb World as preferred learning baseline
- **Fix shopping double-counts** — do not re-shop owned kits; correct erroneous "Tomb World not owned" claims

## Exit criteria

- All three FOUNDATION copies agree on ownership facts and totals
- Byte-check project copy ↔ `raw/Necron_Lists.md` (identical)
- Source library copy updated to match
- Shopping / expansion sections no longer double-count owned kits
- **No commit, no push**

## Recommended models

| Role | Model |
|------|-------|
| Implementer | `composer-2.5-fast` |
| QA | `gpt-5.6-sol-medium` |

## Depends

| Dependency | Notes |
|------------|-------|
| S0 Resolved - Complete | YES |
| **Commit** | pending — S4 |
| **Push** | pending — S4 |