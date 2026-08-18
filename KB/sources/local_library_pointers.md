---
title: Local library pointers (raw/pointers)
type: source
system: warhammer_40k_11e
created: 2026-08-16
updated: 2026-08-16
version: 0.5.0
sources: [raw/pointers/rules_core.md, raw/pointers/faction_pack_necrons.md, raw/pointers/faction_pack_space_marines.md, raw/pointers/points_manuals.md, raw/pointers/terrain_footprints.md, raw/pointers/reference_sheet.md, raw/pointers/web_living_sources.md, raw/pointers/necron_lists_import.md]
confidence: verified
tags: [source, pointers, copyright, unread, backlog]
---

# Local library pointers (raw/pointers)

Eight stub files in `raw/pointers/` that stand in for owned PDFs the repo is not allowed to contain. Each one names a local path and what is inside it - nothing more.

---

## What these are

| Field | Value |
|-------|-------|
| Repo path | `raw/pointers/*.md` (8 stubs plus a directory README) |
| Authored by | Implementer, slice S2, 2026-08-16 |
| Source class | Pointer stubs - the sanctioned substitute for a copyrighted binary |
| Retrieval date | 2026-08-16 |
| Catalogued in | [[source_library]] |

A pointer stub is how this project obeys the no-binaries rule without losing the source. The stub is committed; the PDF is not. Anyone with the owner's machine can follow the path and read the real thing.

---

## The eight stubs

| Stub | Points at | Feeds |
|------|-----------|-------|
| `rules_core.md` | 11e core rules, universal rules updates, event companion | Turn sequence, phases, scoring (S3) |
| `faction_pack_necrons.md` | Necrons faction pack, plus the Wahapedia Necron hub | [[reanimation_protocols]], [[power_matrix]], [[canoptek_court]], [[cryptek_conclave]] |
| `faction_pack_space_marines.md` | Space Marines faction pack, plus the Wahapedia SM hub | [[oath_of_moment]], [[gladius_task_force]] |
| `points_manuals.md` | Munitorum Field Manual and the Space Marines supplement | Every points value in [[necron_lists_owner_notes]] |
| `terrain_footprints.md` | 5 footprint PDFs plus 6 A4 printables | Terrain and board setup (S3) |
| `reference_sheet.md` | Two White Dwarf quick-reference `.webp` images | At-a-glance play aid |
| `web_living_sources.md` | The four living web URLs | [[wahapedia]], [[warhammer_community]] |
| `necron_lists_import.md` | The owner's Necron notes, both repo copies | [[necron_lists_owner_notes]] |

Six of the eight point at material that would resolve most of this KB's open rules questions. **None of it has been read yet.** That is the honest state after L1: the pointers are catalogued, the documents behind them are not ingested.

---

## Reading order when someone does open them

Matching the ingest order in [[ingest_procedure]] - core rules before units, so that unit pages have something to link to:

1. `rules_core.md` - the shared vocabulary everything else depends on
2. `terrain_footprints.md` - how a legal table is built
3. `faction_pack_necrons.md` - the primary army
4. `points_manuals.md` - once there is a list worth costing
5. `faction_pack_space_marines.md` - the opposing force
6. `reference_sheet.md` - a play aid, useful last

---

## Rules that apply to anyone using these

- **Never copy the target into the repo.** The stub exists precisely so the binary does not have to.
- **Paraphrase for teaching.** Read the PDF, explain the rule in your own words, cite the pointer.
- Record a **retrieval date** on any claim, including claims from a local PDF - owned documents get errata'd too.
- `raw/pointers/README.md` is UTF-16LE and sits inside the immutable layer. It needs Coordinator authorization to touch, and the Librarian must not.

---

## What these do not cover

- Any content at all - a pointer is an address, not a document
- Whether the target file still exists or has been superseded
- Kill Team, Age of Sigmar, or any system beyond Warhammer 40,000

---

## Pages these fed

- [[source_library]] - the catalog these mirror
- [[inherited_docs_for_S3]] - which stub answers which S3 question
- [[canoptek_court]], [[cryptek_conclave]], [[gladius_task_force]] - each names its verification pointer

---

## Open questions

- Are the local PDFs current, or has a dataslate superseded them since download?
- The Necrons and Space Marines pointers both cross-check against Wahapedia URLs on a `wh40k10ed` path. See [[wahapedia]].

---

## Related pages

- [[source_library]] - full catalog
- [[necron_lists_owner_notes]] - the one source actually imported
- [[ingest_procedure]] - what may enter `raw/`
- [[index]] - master catalog
