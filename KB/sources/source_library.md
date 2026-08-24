---
title: Source Library (catalog)
type: source
system: warhammer_40k_11e
created: 2026-08-16
updated: 2026-08-19
version: 0.5.2
sources: [reference/Source_Library.md, raw/pointers/]
confidence: verified
tags: [source, catalog, provenance, copyright, pointers]
---

# Source Library (catalog)

The project's map of where the answers are: every owned PDF under `C:\Personal\40K`, every living web reference, and the copyright rule that keeps all of it outside git.

---

## What this source is

| Field | Value |
|-------|-------|
| Repo path | `reference/Source_Library.md` |
| Authored by | Implementer, slice S2, 2026-08-16 |
| Source class | Project reference (a catalog of sources, not a source of rules) |
| Retrieval date | 2026-08-16 |
| Mirror stubs | `raw/pointers/` - see [[local_library_pointers]] |

It contains **no rules content whatsoever**, and that is deliberate. It is a pointer catalog. Reading it tells you which document to open on the owner's machine; it never tells you what that document says.

`confidence: verified` here means the *catalog* is verified - the paths and URLs were checked and the copyright policy is unambiguous. It says nothing about the accuracy of the material those paths point to.

---

## The copyright rule, restated

Four lines govern everything downstream, and they match [`AGENTS.md`](../../AGENTS.md) Sec 10:

1. No Games Workshop binaries in this repository - no PDFs, no `.webp`, no official images
2. Owned files stay under `C:\Personal\40K`; the repo records **paths only**
3. Shipping content is **teaching paraphrase** written in our own words
4. Every claim is cross-checked against an owned PDF or a living web source, with a **retrieval date**

The practical effect on this KB: a page may say *"the Necrons faction pack covers this - see the pointer"*, and may explain a rule in its own words once someone has read it. A page may never reproduce the rule's text.

---

## What the local library holds

Summarized by category. Full paths live in the source and in [[local_library_pointers]] - they are not duplicated here, because a path list maintained in two places drifts.

| Category | What is there | Verifies |
|----------|---------------|----------|
| Core rules and updates | 11e core rules, universal rules updates, event companion | Turn sequence, phases, scoring, [[objective_control]] |
| Faction packs | Necrons, Space Marines | [[reanimation_protocols]], [[oath_of_moment]], [[power_matrix]], detachment rules |
| Points documents | Munitorum Field Manual, plus the Space Marines supplement | Every points value in [[necron_lists_owner_notes]] |
| Terrain footprints | Rules booklet plus four world-specific footprints | Terrain and board setup (S3) |
| Terrain printables | Six A4-scale sheets, including Combat Patrol battlezone | Physical table setup |
| Reference sheet | Two White Dwarf quick-reference images (`.webp`, local only) | At-a-glance play reference |

**This is the highest-value unread material in the project.** The owner already has the documents that would move most of this KB from `unverified` to `verified`; nobody has read them into the KB yet. That is the single biggest gap, and it is a gap of effort rather than of access.

---

## Living web references

Registered here, filed in detail on their own pages:

| Reference | Page | Use |
|-----------|------|-----|
| Warhammer Community | [[warhammer_community]] | Official FAQs, errata, balance dataslates |
| Wahapedia | [[wahapedia]] | Unit/stat lookup when WarCom lacks the profile; also cross-check |

The catalog prefers `wh40k11ed` paths when present and flags `wh40k10ed` as edition-risk. Recorded on [[wahapedia]].

---

## Imported markdown, and the ownership snapshot

The catalog registers the one source that was actually copied into the repo - `Necron_Lists.md`, the owner's own notes, allowed because it is not GW material. Both repo copies were SHA-256 verified against the origin in S2.

It also carries an ownership snapshot duplicating the FOUNDATION table from those notes. Filed on [[necrons]]; if the copies ever disagree, prefer `games/warhammer_40k_11e/armies/necrons/Necron_Lists.md` unless the external Personal\40K source is clearly newer, then re-sync `raw/` from the winner.

**Ownership snapshot corrected 2026-08-16; Hierotek photo ID 2026-08-17.** Kill Team: Tomb World is owned and game-ready. Hierotek is identified (Technomancer, Immortals, Despotek, Apprentek, Plasmacytes) — see [[kill_team_necron_photos]]. Any snapshot that still says Tomb World is *not owned* or Hierotek is unidentified is stale. Totals: 20 Warriors, 6 Scarab Swarms.

---

## What this source does not cover

- Any rules content at all
- Space Marine ownership - the catalog has no inventory for the son's collection
- Kill Team, or any system other than Warhammer 40,000
- Which sources have actually been *read* - the catalog lists availability, not coverage

---

## Pages this source fed

- [[local_library_pointers]] - the pointer stub set
- [[wahapedia]] and [[warhammer_community]] - the two living references
- [[necron_lists_owner_notes]] - provenance for the import
- [[inherited_docs_for_S3]] - which pointer to open for which S3 deliverable

---

## Open questions

- Do the owned PDFs describe 11th Edition throughout, or are some carried over from 10th? The `eng_22-07` filenames suggest a July release date but do not confirm an edition.
- Is there a Space Marine equivalent of `Necron_Lists.md` anywhere in the local library?
- The event companion is catalogued but has no obvious consumer slice. Is competitive play in scope at all?

---

## Related pages

- [[local_library_pointers]] - ingest-ready path stubs
- [[necron_lists_owner_notes]] - the imported source
- [[gw_ip_guidelines]] - GW community IP guidelines (paraphrase; games/ footer policy)
- [[ingest_procedure]] - what may and may not enter `raw/`
- [[index]] - master catalog
