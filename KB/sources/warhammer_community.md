---
title: Warhammer Community (living reference)
type: source
system: warhammer_40k_11e
created: 2026-08-16
updated: 2026-08-19
version: 0.5.2
sources: [raw/pointers/web_living_sources.md, reference/Source_Library.md]
confidence: stub
tags: [source, living_reference, web, official, errata, dataslate]
---

# Warhammer Community (living reference)

Games Workshop's own channel for FAQs, errata, and balance dataslates - the only source in this project that can *change* what an owned PDF says. **Registered, not yet read.**

---

## What this source is

| Field | Value |
|-------|-------|
| URL | <https://www.warhammer-community.com/en-gb/> |
| Publisher | Games Workshop - **official** |
| Source class | **Living web reference**, highest authority in the project |
| Catalogued | 2026-08-16, from [[source_library]] |
| **Content retrieved** | **None.** URL registered only |

---

## Why it outranks everything else

The owned PDFs under `C:\Personal\40K` are snapshots. This site is the thing that invalidates them. When GW publishes a balance dataslate or an errata, a correct-when-downloaded faction pack becomes wrong, and nothing on the owner's disk announces the change.

The precedence this project uses:

| Rank | Source | When it wins |
|------|--------|--------------|
| 1 | Warhammer Community errata or dataslate | Always - it is the publisher amending itself |
| 2 | Owned GW PDF | Unless amended above |
| 3 | [[wahapedia]] | **Unit/stat (datasheet) lookup when WarCom does not publish that profile**; also cross-check. Owned PDF still wins on conflict. See [`AGENTS.md`](../../AGENTS.md) Sec 10. |
| 4 | Owner's notes ([[necron_lists_owner_notes]]) | Ownership and preference facts only, never rules |

WarCom rarely publishes full faction datasheets for free. For characteristics, weapons, and datasheet abilities needed in army lists, go to the owned pack first; if that is unavailable in-session and WarCom has no free profile, **use [[wahapedia]]** (prefer `wh40k11ed`, retrieval date, `draft` until pack cross-check).

A `verified` page whose supporting dataslate has since been superseded is **worse than an `unverified` one**, because it carries false confidence. That is why every rules claim in this KB records a retrieval date.

---

## What to check it for

- **Errata and FAQ** on the 11th Edition core rules and both faction packs
- **Balance dataslates** - these move points values, which invalidates list maths in [[necron_lists_owner_notes]] wholesale
- **Edition status** - whether the material catalogued as 11th Edition genuinely is
- Which Kill Team boxes map to which 40K datasheets, relevant to the outstanding **Hierotek Circle** identification on [[necrons]]

---

## How to cite it correctly

```yaml
sources: ["https://www.warhammer-community.com/... (retrieved YYYY-MM-DD)"]
confidence: draft
```

Promote to `verified` once the article is matched against the owned PDF it amends. Link the specific article, never just the site root - the front page turns over constantly and a bare domain cites nothing.

**No verbatim rules text**, official source or not ([`AGENTS.md`](../../AGENTS.md) Sec 10).

---

## What this source does not cover

- Anything, until it is read - this page is a registration
- Deep list-building or tactics; it publishes rules, not analysis
- A stable URL scheme - articles move and get replaced

---

## Pages this source fed

None yet. It is the named errata check for every `draft` and `unverified` rules claim currently in the KB.

---

## Open questions

- Has any dataslate landed since the owned PDFs were downloaded? Nothing in the repo records a download date, which makes this unanswerable today.
- Is there an official statement on how Kill Team boxes map to 40K datasheets, or is that community knowledge?

---

## Related pages

- [[wahapedia]] - the community cross-check
- [[source_library]] - the catalog
- [[local_library_pointers]] - the snapshots this source can invalidate
- [[index]] - master catalog
