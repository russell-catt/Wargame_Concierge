---
title: KB Index
type: index
system: warhammer_40k_11e
created: 2026-08-16
updated: 2026-08-16
sources: [necron_lists_owner_notes, source_library, local_library_pointers]
confidence: verified
tags: [index, catalog, kb]
---

# KB Index

Master catalog of every page in this knowledge base. Read this first when answering a question: find the relevant pages here, then drill into them.

**Schema source of truth:** [`AGENTS.md`](../AGENTS.md) at the repo root. Entity types, YAML frontmatter, naming, and the ingest / query / lint workflows are defined there, not here. This file is the catalog only.

**Status:** lint complete, slice **L2** of `tomb_world_ownership` (2026-08-16). 5 sources, 17 entity pages. Bootstrapped in L0; first ingest in L1; the typed sections below carry content.

> **Rules sources have now been read, but most `KB/` pages predate that reading.** The claim that used to sit here - "no rules document has been read" - was true at L1 and is false now: S3, S4 and S5 read the owned core rules, both faction packs, and Munitorum Field Manual v1.2, and [[glossary]] carries 24 `verified` game terms as a result. What has **not** happened is a back-fill: the faction, detachment and concept pages below still mostly rest on the owner's planning notes. Treat every `draft` and `unverified` row as "check before the table", and prefer the shipping teaching content under `games/warhammer_40k_11e/` where the two disagree.

---

## How to read this index

Each typed section is a table:

| Column | Meaning |
|--------|---------|
| Page | A `[[wikilink]]` to the KB page (backticked here so link lint does not read the example as a real target) |
| Summary | The one-line summary from the top of that page, copied verbatim |
| Confidence | `verified` / `draft` / `stub` / `unverified` - see [`AGENTS.md`](../AGENTS.md) Sec 6 |
| Updated | Date of the last substantive change |

Treat `unverified` and `stub` rows as "do not take to the table without checking."

---

## Core files

| Page | Summary | Confidence | Updated |
|------|---------|------------|---------|
| [[overview]] | High-level synthesis of the whole knowledge base and where the project stands | draft | 2026-08-16 |
| [[glossary]] | Living terminology; the single home for all Keyword entries | draft | 2026-08-16 |
| [[log]] | Append-only chronological record of ingests, queries, and lint passes | verified | 2026-08-16 |
| [[changelog]] | Promotion log: KB pages that shipped into `docs/` or `games/` | verified | 2026-08-16 |
| [[ingest_procedure]] | How a source in `raw/` becomes KB pages in this project | verified | 2026-08-16 |

---

## Sources

One page per ingested source. Location: `KB/sources/`.

| Page | Summary | Confidence | Updated |
|------|---------|------------|---------|
| [[necron_lists_owner_notes]] | The owner's own Necron expansion blueprint: what is actually owned as of 2026-08-16, and two costed paths from that collection up to a 1,000-point army | draft | 2026-08-16 |
| [[source_library]] | The project's map of where the answers are: owned PDFs, living web references, and the copyright rule that keeps all of it outside git | verified | 2026-08-16 |
| [[local_library_pointers]] | Eight stub files standing in for owned PDFs the repo is not allowed to contain - and all still unread | verified | 2026-08-16 |
| [[wahapedia]] | The community rules aggregator used to cross-check datasheets - registered as a source, not yet read | stub | 2026-08-16 |
| [[warhammer_community]] | GW's own channel for FAQs, errata, and dataslates - the only source that can change what an owned PDF says. Registered, not yet read | stub | 2026-08-16 |

---

## Concepts

Rules ideas and tactical principles. Location: `KB/concepts/`.

| Page | Summary | Confidence | Updated |
|------|---------|------------|---------|
| [[objective_control]] | A characteristic on every model's profile representing how strongly it holds ground - and the metric that decides who wins | unverified | 2026-08-16 |
| [[power_matrix]] | The Canoptek Court detachment rule in 40K 11e: hit re-rolls in controlled territory. **Corrects the L0 Kill Team attribution** | draft | 2026-08-16 |
| [[reanimation_protocols]] | The Necron army rule: units recover during the game, which makes partial damage wasted damage | unverified | 2026-08-16 |
| [[oath_of_moment]] | The Space Marine army rule: nominate one enemy unit per turn and attack it better. Turns target priority into the defining decision | unverified | 2026-08-16 |

---

## Factions

One page per army. Location: `KB/factions/`.

| Page | Summary | Confidence | Updated |
|------|---------|------------|---------|
| [[necrons]] | The owner's primary army: an attrition faction that recovers models as fast as most opponents remove them | draft | 2026-08-16 |
| [[space_marines]] | The opposing army, played by the son: straightforward and forgiving, built from existing older kits, used to teach contrast | stub | 2026-08-16 |

---

## Detachments

One page per detachment and its rules package. Location: `KB/detachments/`.

| Page | Summary | Confidence | Updated |
|------|---------|------------|---------|
| [[canoptek_court]] | The Necron detachment built around robotic constructs, whose rule is the Power Matrix - hit re-rolls in controlled territory | draft | 2026-08-16 |
| [[cryptek_conclave]] | The Necron detachment built around Cryptek characters leading massed infantry, stacking buffs and reanimation | draft | 2026-08-16 |
| [[gladius_task_force]] | The generalist Space Marine detachment named as the son's learning target. **Stub - no source read** | stub | 2026-08-16 |

---

## Units

One page per datasheet, written in play terms. Location: `KB/units/`.

*(Empty - populates from S4, S5, and the full research pass in S6. Deliberately not started: no datasheet source has been read, and [[ingest_procedure]] puts core rules and setup before units.)*

---

## Setup / Missions

Deployment, terrain, missions, and scoring. Location: `KB/setup/`.

*(Empty - populates from S3. The terrain and core-rules pointers that would fill it are catalogued in [[local_library_pointers]] and unread.)*

---

## Analyses

Synthesized outputs: matchups, list comparisons, and query answers worth keeping. Location: `KB/analyses/`.

| Page | Summary | Confidence | Updated |
|------|---------|------------|---------|
| [[inherited_docs_for_S3]] | What L1 hands to S3: the facts stable enough to teach from, the claims that are not, and which unread pointer answers which question | verified | 2026-08-16 |

*(Filename keeps the capitalised `S3` by explicit request in the L1 brief; it is the one deviation from lowercase `snake_case` in `KB/`.)*

---

## Directory guides

Short per-directory README stubs restate the page contract for each entity type. They are navigation aids, **not** entity pages: exclude them from orphan-page lint findings and do not catalog them in the typed sections above.

| Directory | Guide |
|-----------|-------|
| `KB/sources/` | [`sources/README.md`](sources/README.md) |
| `KB/concepts/` | [`concepts/README.md`](concepts/README.md) |
| `KB/factions/` | [`factions/README.md`](factions/README.md) |
| `KB/detachments/` | [`detachments/README.md`](detachments/README.md) |
| `KB/units/` | [`units/README.md`](units/README.md) |
| `KB/setup/` | [`setup/README.md`](setup/README.md) |
| `KB/analyses/` | [`analyses/README.md`](analyses/README.md) |

---

## Index maintenance rules

- Add a row **immediately** after creating a page - an uncatalogued page is invisible to every future session
- Copy the page's one-line summary verbatim; if the summary changes, change it here too
- Update the `Updated` date on substantive changes only, not typo fixes
- Keep `Confidence` in sync with the page frontmatter; a drifted confidence value is a lint finding
- Mark orphan pages with `(orphan)` in the Summary column until they gain inbound links
- If a typed section passes ~10 rows, add sub-sections (by faction, then by role)

---

## Related pages

- [[overview]] - what this KB is about and where it stands
- [[glossary]] - terminology lookup
- [[ingest_procedure]] - how to add to this catalog
- [`AGENTS.md`](../AGENTS.md) - schema source of truth

## Units (pointers)
- [[necrons_unit_index]] — Necrons research corpus overview
- [[space_marines_unit_index]] — Space Marines research corpus overview
