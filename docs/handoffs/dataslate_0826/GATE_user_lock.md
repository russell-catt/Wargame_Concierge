# GATE — User lock (dataslate_0826)

**Track:** `dataslate_0826`  
**Branch:** `feature/dataslate_0826`  
**Date opened:** 2026-08-27

## PDF staging workflow (locked 2026-08-27)

Drive / chat drag failed for remaining files. Owner plan:

1. Drop GW dataslate PDFs into **`raw/_dataslate_0826_staging/`** on this branch (temporary `.gitignore` negation).
2. Agent reads → research markdown → authorized slices.
3. **CLEANUP** before merge to `main`: delete PDFs + remove gitignore negation.

Staging README: [`raw/_dataslate_0826_staging/README.md`](../../../raw/_dataslate_0826_staging/README.md)

## Blockers before full execution

| # | Gate | Status |
|---|------|--------|
| G1 | WarCom egress / pastes / uploads / Drive | **Partial** — pastes + Universal Rules upload; Drive still blocked |
| G1d | Remaining PDFs via **`raw/_dataslate_0826_staging/`** | **PASS** — 13 PDFs pulled 2026-08-27; inventory filed |
| G2 | Owner confirms long-term copies under `C:\Personal\…` (or accepts `draft`) | Open |
| G3 | Owner authorizes multi-slice execution | Open |
| G-clean | **CLEANUP** staging PDFs + gitignore before squash-merge | Required |

## Drop then say

> PDFs dropped in `raw/_dataslate_0826_staging/` — inventory and extract.

## Authorize execution

> Authorize dataslate_0826 — run S0 through FS on `feature/dataslate_0826` (cleanup before merge).
