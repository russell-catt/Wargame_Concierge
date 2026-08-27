# GATE — User lock (dataslate_0826)

**Track:** `dataslate_0826`  
**Branch:** `feature/dataslate_0826`  
**Date opened:** 2026-08-27

## Owner authorization (2026-08-27)

| Gate | Decision |
|------|----------|
| Research plan | **OK** — proceed |
| Execution | **Authorize full track** (S0 → FS) |
| G2 local PDF copies | **Accept `draft`** for now (no wait on `C:\Personal\…` confirm) |
| KT teams | **Update teams provided in staging**; owned teams with **no** update this package = **no-op** (Death Korps, Kommandos) |
| Package shape | **No singular dataslate** (40K or KT) — Core/universal + faction/team updates |

## PDF staging workflow (locked 2026-08-27)

1. Drop GW PDFs into **`raw/_dataslate_0826_staging/`** (temporary `.gitignore` negation).
2. Agent reads → research markdown → authorized slices.
3. **CLEANUP** before merge to `main`: delete PDFs + remove gitignore negation.

Staging README: [`raw/_dataslate_0826_staging/README.md`](../../../raw/_dataslate_0826_staging/README.md)

## Blockers before full execution

| # | Gate | Status |
|---|------|--------|
| G1 | WarCom egress / pastes / uploads / Drive | **Partial** — pastes + staging; Drive unused |
| G1d | Staging PDFs | **PASS** — 14 PDFs |
| G-KT | KT package shape | **PASS** — Core + team updates |
| G-40K | 40K package shape | **PASS** — Universal Rules + FP + MFM |
| G2 | Local `C:\Personal\…` copies | **WAIVED — accept `draft`** |
| G3 | Owner authorizes multi-slice execution | **PASS — full track** |
| G-clean | **CLEANUP** staging PDFs + gitignore before squash-merge | Required before merge |

## Authorize execution (received)

> Research plan OK. Go for full track. Accept draft for now. Update the teams provided. Other owned teams received no update.

## Drop then say

> PDFs dropped in `raw/_dataslate_0826_staging/` — inventory and extract.
