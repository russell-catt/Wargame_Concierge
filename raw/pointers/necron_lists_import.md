# Pointer: Necron Lists (Imported)

**Catalog:** [`reference/Source_Library.md`](../../reference/Source_Library.md) — Imported markdown sources

## Copies

| Rank | Copy | Role |
|------|------|------|
| 1 | [`games/warhammer_40k_11e/armies/necrons/Necron_Lists.md`](../../games/warhammer_40k_11e/armies/necrons/Necron_Lists.md) | **Authoritative FOUNDATION.** Edit here first |
| 2 | [`raw/Necron_Lists.md`](../Necron_Lists.md) | Imported copy of the external source |
| 2 | `C:\Personal\40K\rules\Necron_Lists.md` | External source, outside the repo |

All three are kept byte-identical. If they diverge, the project copy wins and the other two are re-synced to it.

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

- **Direction of truth:** project copy → `raw/Necron_Lists.md` → `C:\Personal\40K\rules\Necron_Lists.md`. Never edit a lower copy to win an argument with a higher one.
- **After any FOUNDATION change:** re-copy to both other locations and confirm identical SHA-256 hashes before the slice closes.
- **Writers:** `raw/` is Coordinator/Implementer copy-in only. The Librarian reads it and never writes it.
- **Verification used:** `Get-FileHash` across the three paths. All three matched after the 2026-08-16 re-sync (`90C00E0D…C55EF`).
- **Encoding:** UTF-8, no BOM, in every copy.

## History

| Date | Event |
|------|-------|
| 2026-08-16 (Preflight) | External source patched to record confirmed ownership; Hierotek Circle TODO opened. Also recorded Tomb World as superseded — **erroneous** |
| 2026-08-16 (re-sync) | `raw/Necron_Lists.md` re-aligned to the other copies, treating Tomb-World-owned content as drift — **also erroneous** |
| 2026-08-16 (`tomb_world_ownership` S1) | **Correction.** Tomb World restored as owned and game-ready in all three copies; totals and shopping fixed; copies byte-identical again |
| 2026-08-16 (`tomb_world_ownership` S3) | This pointer realigned to the corrected FOUNDATION |

The earlier claim on this page that Tomb World is **not** current ownership was wrong and has been removed. Do not reintroduce it.
