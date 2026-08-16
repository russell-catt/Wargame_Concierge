---
title: KB Index
type: index
system: warhammer_40k_11e
created: 2026-08-16
updated: 2026-08-16
sources: []
confidence: verified
tags: [index, catalog, kb]
---

# KB Index

Master catalog of every page in this knowledge base. Read this first when answering a question: find the relevant pages here, then drill into them.

**Schema source of truth:** [`AGENTS.md`](../AGENTS.md) at the repo root. Entity types, YAML frontmatter, naming, and the ingest / query / lint workflows are defined there, not here. This file is the catalog only.

**Status:** bootstrapped in slice L0 (2026-08-16). No sources ingested yet - the typed sections below are empty on purpose and fill in from S2 onward.

---

## How to read this index

Each typed section is a table:

| Column | Meaning |
|--------|---------|
| Page | `[[wikilink]]` to the KB page |
| Summary | The one-line summary from the top of that page, copied verbatim |
| Confidence | `verified` / `draft` / `stub` / `unverified` - see [`AGENTS.md`](../AGENTS.md) Sec 6 |
| Updated | Date of the last substantive change |

Treat `unverified` and `stub` rows as "do not take to the table without checking."

---

## Core files

| Page | Summary | Confidence | Updated |
|------|---------|------------|---------|
| [[overview]] | High-level synthesis of the whole knowledge base and where the project stands | draft | 2026-08-16 |
| [[glossary]] | Living terminology; the single home for all Keyword entries | stub | 2026-08-16 |
| [[log]] | Append-only chronological record of ingests, queries, and lint passes | verified | 2026-08-16 |
| [[changelog]] | Promotion log: KB pages that shipped into `docs/` or `games/` | verified | 2026-08-16 |
| [[ingest_procedure]] | How a source in `raw/` becomes KB pages in this project | verified | 2026-08-16 |

---

## Sources

One page per ingested source. Location: `KB/sources/`.

*(Empty - nothing ingested yet. Sources arrive in S2. Drop an allowed source into `raw/`, then say "ingest [filename]".)*

---

## Concepts

Rules ideas and tactical principles. Location: `KB/concepts/`.

*(Empty - populates from S3 rules work.)*

---

## Factions

One page per army. Location: `KB/factions/`.

*(Empty - Necrons and Space Marines land in S4 and S5.)*

---

## Detachments

One page per detachment and its rules package. Location: `KB/detachments/`.

*(Empty - populates from S4 and S5.)*

---

## Units

One page per datasheet, written in play terms. Location: `KB/units/`.

*(Empty - populates from S4, S5, and the full research pass in S6.)*

---

## Setup / Missions

Deployment, terrain, missions, and scoring. Location: `KB/setup/`.

*(Empty - populates from S3.)*

---

## Analyses

Synthesized outputs: matchups, list comparisons, and query answers worth keeping. Location: `KB/analyses/`.

*(Empty - file your first query answer here to start compounding.)*

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
