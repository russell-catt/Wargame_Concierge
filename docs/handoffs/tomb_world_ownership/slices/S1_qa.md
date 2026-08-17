# S1 - QA report

- **Status:** Resolved - Complete
- **Gate:** PASS
- **Track / slice:** `tomb_world_ownership` / S1
- **QA tier:** Tier 2 independent verification
- **Model used:** gpt-5.6-sol-medium
- **Commit / push:** None

## Gate result

**PASS.** Independent disk checks confirm that all three authoritative `Necron_Lists.md` copies are byte-identical and satisfy the S1 ownership, playability, totals, and shopping requirements.

## Spot-check table

| Check | Result | Evidence |
|---|---|---|
| Three authoritative copies agree | PASS | Project, `raw/`, and `C:\Personal\40K\rules\` copies contain the same ownership tables and expansion guidance. |
| Project ↔ raw byte identity | PASS | Exact byte comparison returned `True`; both SHA-256 hashes are `90C00E0D8A55017E2C035D66C876FB792EE337317865E53521A3B4BA553C55EF`. |
| Source-library copy matches | PASS | Exact byte comparison project ↔ personal returned `True`; source-library SHA-256 is the same. |
| Tomb World game-ready FOUNDATION | PASS | Geomancer ×1, Tomb Crawlers ×2, Macrocytes ×5, Warriors ×10, and Scarab Swarms ×3 are marked game-ready; subtotal 385 pts. |
| Hierotek Circle status | PASS | Game-ready physical set remains explicitly TBD pending photo identification and datasheet mapping. |
| Build-before-play inventory | PASS | Immortals ×5, extra Warriors ×10, and extra Scarab Swarms ×3 are owned and unassembled. |
| Ownership totals | PASS | 20 Warriors and 6 Scarab Swarms, correctly split between game-ready and sprue inventory. |
| Superseded ownership claim removed | PASS | Scoped grep of all three S1 authority files found zero active `Tomb World not owned`, `Superseded`, or `Historical / Superseded` matches. |
| Phase 1 playable and preferred | PASS | Both expansion paths prefer the playable-now Tomb World 260-point learning force; Hierotek is alternate after identification. |
| Shopping avoids owned-kit double-counts | PASS | Tomb World contents, first Immortals box, extra Warriors, and extra Scarabs are excluded from shopping; only one additional Immortals box is requested for the 10-model target. |

## Independent hash receipt

```text
games/warhammer_40k_11e/armies/necrons/Necron_Lists.md
90C00E0D8A55017E2C035D66C876FB792EE337317865E53521A3B4BA553C55EF

raw/Necron_Lists.md
90C00E0D8A55017E2C035D66C876FB792EE337317865E53521A3B4BA553C55EF

C:\Personal\40K\rules\Necron_Lists.md
90C00E0D8A55017E2C035D66C876FB792EE337317865E53521A3B4BA553C55EF
```

## Scope note

The superseded-claim grep above is scoped to the three S1 authoritative files defined by `S1_brief.md`. Other track slices own propagation into downstream army, planning, reference, and KB documents.

## Return to Coordinator

**Gate: PASS — S1 is Resolved - Complete.**
