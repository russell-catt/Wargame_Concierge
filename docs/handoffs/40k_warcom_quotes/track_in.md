# Track in — 40k_warcom_quotes

- **Project:** Wargame_Concierge
- **Track:** `40k_warcom_quotes`
- **Status:** Complete (2026-08-18)
- **Git root:** `C:\Personal\Personal_Projects\Wargame_Concierge`
- **Plan:** Cursor plan `40k_warcom_rules_ingest_5f485290`
- **Handoffs root:** `docs/handoffs/40k_warcom_quotes/`
- **Entrance:** User authorized full track execution 2026-08-18 (Implementer + Librarian + QA + Coordinator; one commit + push at FS)

## Goals

1. Scoped 40K verbatim quote exception under `games/warhammer_40k_11e/rules/` and `setup/` (WarCom-free + local `eng_*`); Codex wall elsewhere
2. Full numbered Core ID index; quotes only for teaching-spine + visibility/cover/armies
3. Teaching docs get rule-ID cites; KB/docs stay paraphrase
4. Necron lists: games copy is working copy; Personal `C:\Personal\40K\Necron_Lists.md` wins on divergence
5. One git commit + one push of the whole track at Final Sanity

## Golden sources (read-only, in place)

| Library | Path |
|---------|------|
| Core + July patches | `C:\Personal\40K\rules\` — see `raw/pointers/rules_core.md` |
| Personal Necron lists (SoT) | `C:\Personal\40K\Necron_Lists.md` |

**Retrieval:** WarCom free Core article + downloads page **2026-08-18**. Local `eng_*` files are source of record; WarCom is discovery.

## Local `eng_*` inventory vs WarCom (S0)

WarCom announcement (2026-06-01): [Download the free Core Rules now](https://www.warhammer-community.com/en-gb/articles/nhqt9wx3/new40k-rules-download-the-free-core-rules-now/). Downloads hub: [Warhammer 40,000 downloads](https://www.warhammer-community.com/en-gb/downloads/warhammer-40000/). July discovery: [July Update](https://www.warhammer-community.com/en-gb/articles/rgqanids/warhammer-40000-july-update-what-you-need-to-know/) (2026-07-22). Event Companion discovery: [Download the new Event Companions](https://www.warhammer-community.com/en-gb/articles/lszdpzmc/new40k-download-the-new-event-companions-today/).

Files found under `C:\Personal\40K\rules\` (not copied into git):

| Local file | Role this track | WarCom-free? |
|------------|-----------------|--------------|
| `eng_01-06_warhammer40k_new40k_core_rules.pdf` | Core baseline (88 pages, text layer) | Yes — free Core |
| `eng_22-07_warhammer_40,000_universal_rules_updates.pdf` | July SoT (1 page, v1.0, legal 22 Jul 2026) | Yes — free update |
| `eng_22-07_warhammer_40,000_event_companion-alyapl19us-b2drgwkji4.pdf` | Event framework v1.1 (93 pages) | Yes — free companion |
| `eng_12-06_warhammer40000_terrainareafootprints-*.pdf` | Terrain footprints booklet | Free extras — pointer only |
| `warhammer40k_terrain_area_footprint_*.pdf` | Battlezone footprints | Free extras — pointer only |
| `eng_22-07_warhammer_40,000_faction_pack_necrons.pdf` | **Codex wall** — do not quote | Faction pack |
| `eng_22-07_warhammer_40,000_faction_pack_space_marines.pdf` | **Codex wall** — do not quote | Faction pack |
| `Warhammer 40,000_ Munitorum Field Manual.pdf` | **Do not dump** points | MFM |
| `Warhammer 40,000_ Munitorum Field Manual_Marines.pdf` | **Do not dump** points | MFM |

No Armageddon datacard PDFs found in `C:\Personal\40K\rules\`. PDFs were **not** copied into the repo.

## Constraints

- Personal use only — **this project must never be sold**
- Never commit GW PDFs/images
- Librarian never writes `raw/` binaries; pointer markdown is Implementer
- Codex / Faction Pack / paid army rules: paraphrase only
- Do not fill KT follow-ups
- **Commit: one at FS, then one push** (user override of Coordinator-only git lock)

## Slice status

| Slice | Status | Notes |
|-------|--------|-------|
| S0 | Done | This file + local vs WarCom inventory |
| S1 | Done | Policy |
| S1b | Done | Pointers + Necron working-copy header |
| L1 | Done | KB source + glossary convention |
| S2 | Done | 156 IDs; 112 quote / 44 stub |
| QA-Q | Done | PASS |
| S3 | Done | Teaching ID cites; no rewrite |
| S4 | Done | Setup/terrain + OC vs KT 1" |
| S5 | Done | Free extras inventoried, not dumped |
| QA-T | Done | PASS |
| L2 | Done | Changelog + log |
| FS | Done | Track report + one commit + push |
