# Pointer: Necron Lists (Imported)

**Catalog:** [`reference/Source_Library.md`](../../reference/Source_Library.md) — Imported markdown sources

**Ranking (corrected 2026-08-18, track `40k_warcom_quotes`):** `C:\Personal\40K\Necron_Lists.md` is the **source of truth**. The games copy is a **working copy**. If they diverge, **Personal wins**. Do **not** sync or overwrite the Personal file from the repo.

## Copies

| Rank | Copy | Role |
|------|------|------|
| 1 | `C:\Personal\40K\Necron_Lists.md` | **Source of truth.** Personal library. Wins on divergence. Outside git. |
| 2 | [`games/warhammer_40k_11e/armies/necrons/Necron_Lists.md`](../../games/warhammer_40k_11e/armies/necrons/Necron_Lists.md) | **Working copy** in the 40K subtree. Edit for play notes; do not treat as SoT if Personal differs |
| 3 | [`raw/Necron_Lists.md`](../Necron_Lists.md) | Imported snapshot inside `raw/` (immutable layer). Do not use to overwrite Personal |

Ownership facts for play live in [`Owned_Models_Inventory.md`](../../games/warhammer_40k_11e/armies/necrons/Owned_Models_Inventory.md).

## Ownership recorded in FOUNDATION — 2026-08-16

**Kill Team: Tomb World is owned and its units are game-ready:** 1× Cryptek Geomancer, 2× Canoptek Tomb Crawlers, 5× Canoptek Macrocytes, 10× Necron Warriors, 3× Canoptek Scarab Swarms. It is the preferred learning baseline.

Also owned, still on sprue — assemble-to-expand, not blockers:

- 10× Necron Warriors — 2nd squad, unassembled and unpainted
- 3× Canoptek Scarab Swarms — 2nd set, unassembled and unpainted
- 5× Immortals — unassembled, build before play

Hierotek Circle Kill Team is an *additional* game-ready set; its 40K datasheets are **TBD pending owner photos**. That identification is open but does not block play.

**Totals:** 20 Necron Warriors (10 game-ready + 10 on sprue), 6 Canoptek Scarab Swarms (3 game-ready + 3 on sprue), plus the Geomancer, Tomb Crawlers, Macrocytes, Immortals, and the Hierotek set.

Do not re-shop owned kits.

## Sync expectations

- **Direction of truth:** Personal `C:\Personal\40K\Necron_Lists.md` wins. The games working copy may lag. **Never** overwrite Personal from the repo.
- **Writers:** `raw/` is Coordinator/Implementer pointer/import only. The Librarian reads it and never writes binaries.
- **This track (`40k_warcom_quotes`):** does not rewrite list content and does not copy the Personal file over the games copy.

## History

| Date | Event |
|------|-------|
| 2026-08-16 (Preflight) | External source patched to record confirmed ownership; Hierotek Circle TODO opened. Also recorded Tomb World as superseded — **erroneous** |
| 2026-08-16 (re-sync) | `raw/Necron_Lists.md` re-aligned to the other copies, treating Tomb-World-owned content as drift — **also erroneous** |
| 2026-08-16 (`tomb_world_ownership` S1) | **Correction.** Tomb World restored as owned and game-ready |
| 2026-08-16 (`tomb_world_ownership` S3) | Pointer realigned to the corrected FOUNDATION |
| 2026-08-18 (`40k_warcom_quotes` S1b) | **Ranking correction.** Personal path is SoT; games file is working copy; Personal wins on divergence. Previous ranking (games copy first, re-sync to Personal) was wrong. |

The earlier claim on this page that Tomb World is **not** current ownership was wrong and has been removed. Do not reintroduce it.
