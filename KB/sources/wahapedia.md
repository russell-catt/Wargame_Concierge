---
title: Wahapedia (living reference)
type: source
system: warhammer_40k_11e
created: 2026-08-16
updated: 2026-08-16
version: 0.5.0
sources: [raw/pointers/web_living_sources.md, reference/Source_Library.md]
confidence: stub
tags: [source, living_reference, web, wahapedia, verification]
---

# Wahapedia (living reference)

The community rules aggregator this project uses to cross-check datasheets and detachment rules. **Registered as a source, not yet read** - no page content has been retrieved into the KB.

---

## What this source is

| Field | Value |
|-------|-------|
| Index | <https://wahapedia.ru/> |
| Necrons hub | <https://wahapedia.ru/wh40k10ed/factions/necrons> |
| Space Marines hub | <https://wahapedia.ru/wh40k10ed/factions/space-marines> |
| Source class | **Living web reference** - moves under us ([[ingest_procedure]]) |
| Catalogued | 2026-08-16, from [[source_library]] |
| **Content retrieved** | **None.** URLs registered only |

`confidence: stub` is doing real work here. This page records that the reference *exists* and how to use it. It records nothing the reference *says*, because nobody has opened it. Any future page that cites Wahapedia must carry its own retrieval date - inheriting this page's date would be a lie about when the claim was checked.

---

## Why this project uses it

The owner has the official PDFs already (see [[local_library_pointers]]), so Wahapedia is not the primary source of record. It earns its place for three things the PDFs do badly:

- **Speed.** Looking up one datasheet mid-game is faster than paging through a faction pack.
- **Consolidation.** Rules split across a core book, a faction pack, and a dataslate appear in one place.
- **Cross-checking.** If a KB page and Wahapedia disagree, that disagreement is itself the finding - usually an errata the KB missed.

It is a **community** aggregation, not a publisher. Where Wahapedia and an owned GW PDF conflict, the PDF wins and the conflict gets recorded rather than quietly resolved.

---

## The URL path question - open

Both faction URLs registered by S2 sit under **`wh40k10ed`** - a 10th Edition path segment - while the catalog describes them as 11th Edition content.

Three possibilities, none confirmed:

1. Wahapedia kept the legacy path and serves 11e content from it
2. The URLs genuinely point at 10th Edition pages and are stale
3. Wahapedia has an 11e path that S2 did not find

This matters more than a broken link would. **Edition drift is an explicit lint category in this project**, and a 10th Edition page mistaken for an 11th Edition one is exactly the failure mode the `confidence` field exists to catch. Anyone opening these URLs should confirm which edition they are reading *before* filing anything from them.

---

## How to cite it correctly

A claim sourced here is `draft` at best until a second source agrees. The frontmatter pattern:

```yaml
sources: ["https://wahapedia.ru/wh40k10ed/factions/necrons (retrieved YYYY-MM-DD)"]
confidence: draft
```

And in prose: name the edition you believe you read, not the edition you expected.

**Never paste Wahapedia text into this repo.** Aggregated rules text is still GW rules text. Paraphrase for teaching, cite the URL and the date ([`AGENTS.md`](../../AGENTS.md) Sec 10).

---

## What this source does not cover

- Anything at all, until someone reads it - this page is a registration
- Lore, modelling, or painting
- Which of its content is current versus superseded by a dataslate GW published yesterday

---

## Pages this source fed

None yet. It is named as the verification route on [[reanimation_protocols]], [[oath_of_moment]], [[power_matrix]], [[canoptek_court]], [[cryptek_conclave]], and [[gladius_task_force]] - all of which are waiting on it.

---

## Open questions

- Does `wh40k10ed` serve 11th Edition content, or is the path stale?
- Which is the faster verification route in practice: Wahapedia or the owned faction pack?

---

## Related pages

- [[warhammer_community]] - the official living reference
- [[source_library]] - the catalog
- [[local_library_pointers]] - the owned PDFs to cross-check against
- [[index]] - master catalog
