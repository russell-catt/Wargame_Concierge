---
title: Ingest Procedure
type: ingest_procedure
system: warhammer_40k_11e
created: 2026-08-16
updated: 2026-08-18
version: 0.5.1
sources: []
confidence: verified
tags: [procedure, ingest, workflow, copyright]
---

# Ingest Procedure

How a source becomes knowledge in this project. [`AGENTS.md`](../AGENTS.md) Sec 11 gives the generic workflow; this page is the **project-specific** version - what counts as an allowed source here, how wargame sources map to entity pages, and what to do about a new edition and Games Workshop copyright.

---

## Before anything: what may enter `raw/`

`raw/` is **immutable** and the Librarian **never writes to it**. Sources are placed there by the Coordinator or an Implementer slice (S2 owns the first import). The Librarian reads, summarizes, and links - nothing more.

| Allowed in `raw/` | Never in `raw/` (or anywhere in this repo) |
|-------------------|--------------------------------------------|
| Markdown notes written by the owner | Games Workshop PDFs |
| Imported list blueprints | Official datasheet images or scans |
| Pointer stubs to `C:\Personal\40K` | `.webp` / `.png` / `.jpg` / any binary |
| Research excerpts we author ourselves | Verbatim transcriptions of rules text **in `KB/`** (scoped shipping quotes live under `games/` per [`AGENTS.md`](../AGENTS.md) Sec 10) |
| Living-reference notes with URL + retrieval date | Anything copyrighted and redistributable |

Binaries are blocked by [`.gitignore`](../.gitignore). **Do not bypass it.** If a source only exists as a PDF, the correct move is a **pointer stub** in `raw/pointers/` recording the local path and what it contains - never a copy.

See [`raw/README.md`](../raw/README.md) for the layer contract and [`AGENTS.md`](../AGENTS.md) Sec 10 for the full copyright rules.

---

## The four source classes

Wargame sources behave differently and need different handling.

| Class | Example | Handling |
|-------|---------|----------|
| **Owned rules material** | A rulebook or codex PDF under `C:\Personal\40K` | Pointer only. Read it. **Paraphrase into `KB/`**. Numbered Core IDs may be cited (`01.01`). Verbatim quotes only in scoped `games/` paths. Never copy the PDF in. |
| **Living web reference** | Warhammer Community article, Wahapedia page | Record URL **and retrieval date**. Starts at `draft`. Re-check when a dataslate drops. |
| **Owner's own notes** | `Necron_Lists.md`, model inventory, game notes | Freely ingestable. Highest trust for ownership and preference facts; **not** authoritative for rules. |
| **Play experience** | Notes from a game actually played | Ingest into `KB/analyses/`. Authoritative for "what happened", never for "what the rule says". |

---

## Steps

### 1. Confirm the source is allowed

Check it against the table above. If it is a GW binary, stop and create a pointer stub instead.

### 2. Read it and agree on scope

Read the source in full. Discuss the key takeaways with the user and ask 1-3 clarifying questions if scope is unclear. For a large source, agree up front on **which entity pages it should produce** - a codex can easily fan out into a Faction, several Detachments, and a dozen Units, and that is better planned than discovered halfway through.

### 3. Write the Source page

Create `KB/sources/<source_name>.md` with frontmatter per [`AGENTS.md`](../AGENTS.md) Sec 6, plus:

- What the source is and what it covers
- **Provenance**: local path, or URL with **retrieval date**
- Which edition it describes (11e, 10e, or ambiguous) - this drives everything downstream
- Key facts extracted, in teaching paraphrase
- What it does **not** cover
- Which KB pages it fed

### 4. Fan out to entity pages

Map the source content onto entity types:

| Source content | Goes to |
|----------------|---------|
| Army-wide rule, faction identity, playstyle | `KB/factions/` |
| Detachment rule, enhancements, stratagems | `KB/detachments/` |
| A datasheet, in play terms | `KB/units/` |
| A phase, a rules mechanic, a tactical principle | `KB/concepts/` |
| Deployment, terrain, missions, scoring | `KB/setup/` |
| A game term or ability keyword | `KB/glossary.md` **only** - never its own page (Sec 5) |
| Matchup, comparison, synthesized answer | `KB/analyses/` |

Prefer **updating** an existing page over creating a near-duplicate.

### 5. Set confidence honestly

Every page gets a `confidence` value. Be conservative:

- One living-reference source, not cross-checked -> `draft`
- Written from memory or a 10e source -> `unverified`
- Cross-checked against a current 11e source of record -> `verified`, with the source and date in `sources:`

An honest `unverified` is worth more than a confident guess. This matters more than usual here: **11th Edition is new**, so treat anything carried over from 10th Edition as suspect until confirmed, and record the retrieval date on every living-reference claim.

### 6. Handle contradictions explicitly

If the source disagrees with what the KB already says, **do not silently overwrite**. Record both claims, note which source and edition each comes from, and flag it for the user. Edition change is the usual cause and it is useful information, not noise.

### 7. Update the glossary

Add every new or refined term to [[glossary]] in the same pass. If a term conflicts with an existing entry, flag it rather than replacing it.

### 8. Update index, overview, and log

- [[index]] - add rows for new pages, refresh summaries and confidence for changed ones
- [[overview]] - update only if the source shifts the big picture (source count, new faction, resolved open question)
- [[log]] - append:

```
## [YYYY-MM-DD] ingest | <source title>
Pages created: ...
Pages updated: ...
Key additions: ...
```

### 9. Self-check before closing

| Check | Requirement |
|-------|-------------|
| `raw/` untouched | No creates, edits, or deletes |
| No binaries added | `git status` shows markdown only |
| Every new page catalogued | A row in [[index]] |
| Every rules claim sourced | Path or URL + retrieval date |
| Confidence set on every page | No missing or inflated values |
| Links resolve both ways | Back-links added to related pages |
| Log appended | Entry at the bottom of [[log]] |
| No commit | Coordinator is the sole git owner |

---

## Scale expectations

A single meaningful ingest touches **5-15 pages**. That is correct, not excessive - the fan-out is the whole point of the pattern. Ingest one source at a time and stay involved rather than batching many at once; the cross-referencing quality is what makes the KB worth having.

---

## Ingest order for this project

The recommended sequence, matching the v1_scaffold track:

1. **Core rules and glossary terms** - the shared vocabulary everything else depends on (S3)
2. **Setup, missions, and scoring** - how games are actually won (S3)
3. **Necrons**: faction, then detachments, then the owned units (S4)
4. **Space Marines**: faction and a comparable starter detachment (S5)
5. **Full unit research** across both armies (S6)
6. **Analyses**: matchups, list options from the owned model pool

Do not start at unit datasheets. Without the core rules and setup pages, unit pages have nothing to link to and end up as orphans.

---

## Related pages

- [`AGENTS.md`](../AGENTS.md) - schema SoT: entity types, frontmatter, workflows
- [`docs/operations/librarian_agent.md`](../docs/operations/librarian_agent.md) - day-to-day Librarian operations
- [`raw/README.md`](../raw/README.md) - raw layer contract
- [[index]] - master catalog
- [[glossary]] - terminology
- [[log]] - activity record
