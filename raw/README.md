# raw/ — immutable sources

**Purpose:** Allowed source material copied or authored for this project. Treat as **read-only** after ingest unless Coordinator authorizes a correction.

**Also:** `C:\Personal\Kill Team` stays outside git — KT24 path pointers only (same rule as 40K).

## Rules

- **Allowed:** Markdown notes, imported list blueprints, Source_Library pointer stubs, Wahapedia research excerpts we author.
- **Never commit:** Games Workshop PDFs, official images, webp/png binaries, or other copyrighted GW assets.
- **External libraries:** `C:\Personal\40K` and `C:\Personal\Kill Team` remain outside this repo — use path pointers only.

## Contents (populated by slice)

| Path | Added by | Notes |
|------|----------|-------|
| `Necron_Lists.md` | S2 | Copy after Preflight ownership patch (2026-08-16) |
| `pointers/` | S2 | Source_Library ingest stubs — see [`reference/Source_Library.md`](../reference/Source_Library.md) |
| `pointers/40k_pics_ownership.md` | 2026-08-21 | Blood Ravens + AoD + Deathwatch photo paths |
| `pointers/40k_codexes.md` | 2026-08-21 | Owned SM + Necrons Codex PDFs (paid, no quote) |
| `the_warcode/` | warcode_tactical_doctrine S0 | **Allowed binary:** free beta rulebook PDF (RedMakers — not GW) |
| `_dataslate_0826_staging/` | dataslate_0826 (TEMPORARY) | Owner-gated GW PDF drop on `feature/dataslate_0826` only — **delete before merge to main** |
| `pointers/warcode_*.md` | warcode_tactical_doctrine S0 | Rulebook, VIP community, STL path pointers |
| `pointers/white_dwarf_527.md` | wd527_research Preflight | Owned WD527 PDFs at `C:\Personal\40K\WD_527\` |
| `white_dwarf_527/` | wd527_research S1 | Research transcriptions (markdown only) |

Librarian **never writes** under `raw/` (Karpathy layer contract).

**Exception:** `raw/the_warcode/*.pdf` may be committed — free public beta only; see `.gitignore` negation and `AGENTS.md` Sec 10.