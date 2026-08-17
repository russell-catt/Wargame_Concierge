# S1 — Implementer report

- **Status:** Resolved - Implemented
- **Model used:** composer-2.5-fast
- **Commit:** pending (Coordinator commits at S4)

## Summary

Rewrote **FOUNDATION** in all three authoritative `Necron_Lists.md` copies to restore **Kill Team: Tomb World** as confirmed, game-ready ownership. Corrected the prior erroneous "Tomb World not owned / superseded" state. Restored playable Phase 1 lists (260 pts, Tomb World preferred). Fixed shopping double-counts for Macrocytes, Tomb World Scarabs/Warriors, and sprue inventory.

## Changes

### FOUNDATION (all three copies)

1. **Game-ready table** — Tomb World full datasheet list (Geomancer, Tomb Crawlers, Macrocytes, 10 Warriors, 3 Scarabs; 385 pts subtotal) plus Hierotek Circle TBD placeholder.
2. **Build-before-play table** — Immortals×5, Warriors×10 (2nd squad), Scarabs×3 (2nd set), all unassembled.
3. **Ownership totals** — 20 Warriors, 6 Scarab Swarms, plus Geomancer, Tomb Crawlers, Macrocytes, Immortals, Hierotek TBD.
4. Removed "Historical / Superseded: Kill Team: Tomb World" section and "not owned" language.

### Phase 1 / shopping fixes

- Both paths: Phase 1 preferred start = Tomb World 260-pt list (playable now).
- Phase 2: Macrocytes marked **owned, game ready** from Tomb World (no re-shop).
- Canoptek / Cryptek shopping: Tomb World contents, extra Warriors/Scarabs, and Immortals excluded from retail targets.
- Cryptek shopping: removed duplicate Warrior box need (20 owned); recalculated remaining retail ($310 CAD).

## Exit criteria self-check (Tier 1)

| Criterion | Result |
|-----------|--------|
| Three FOUNDATION copies agree on ownership facts and totals | PASS |
| Byte-check project ↔ `raw/Necron_Lists.md` (identical) | PASS |
| Source library `C:\Personal\40K\rules\Necron_Lists.md` matches | PASS |
| Game-ready table: Tomb World datasheets + Hierotek TBD | PASS |
| Build-before-play table: Immortals×5, Warriors×10, Scarabs×3 | PASS |
| Phase 1 playable with Tomb World preferred | PASS |
| Shopping no longer double-counts owned kits | PASS |
| No commit, no push | PASS |

**Tier 1 self-check: PASS**

## Commands run + results

```powershell
$root = "C:\Personal\Personal_Projects\Wargame_Concierge"
$project = "$root\games\warhammer_40k_11e\armies\necrons\Necron_Lists.md"
$raw = "$root\raw\Necron_Lists.md"
$personal = "C:\Personal\40K\rules\Necron_Lists.md"

Copy-Item -Path $project -Destination $raw -Force
Copy-Item -Path $project -Destination $personal -Force

Get-FileHash -Path $project,$raw,$personal -Algorithm SHA256 |
  Format-Table Path, Hash -AutoSize

Select-String -Path $project -Pattern "not owned|Superseded|Historical / Superseded"

git -C $root status --short -- "games/warhammer_40k_11e/armies/necrons/Necron_Lists.md" "raw/Necron_Lists.md"
```

| Check | Expected | Actual |
|-------|----------|--------|
| project SHA-256 | — | `90C00E0D8A55017E2C035D66C876FB792EE337317865E53521A3B4BA553C55EF` |
| raw SHA-256 | identical to project | `90C00E0D8A55017E2C035D66C876FB792EE337317865E53521A3B4BA553C55EF` |
| personal SHA-256 | identical to project | `90C00E0D8A55017E2C035D66C876FB792EE337317865E53521A3B4BA553C55EF` |
| project vs raw byte identity | True | True |
| project vs personal byte identity | True | True |
| "not owned" / "Superseded" grep | 0 matches | 0 matches |
| Git commit from S1 | None | None (modified only) |

## Files updated

1. `games/warhammer_40k_11e/armies/necrons/Necron_Lists.md` (authoritative)
2. `raw/Necron_Lists.md` (synced)
3. `C:\Personal\40K\rules\Necron_Lists.md` (synced)
4. `docs/handoffs/tomb_world_ownership/slices/S1_implementer.md` (this report)

## Notes

- Personal 40K copy is outside git; synced via file copy only.
- S2 (army docs + starters) depends on this FOUNDATION sync — unblocked.
- Hierotek Circle remains TBD pending photos; Tomb World is the preferred learning baseline until ID complete.
