---
title: Wahapedia (living reference)
type: source
system: warhammer_40k_11e
created: 2026-08-16
updated: 2026-08-19
version: 0.5.2
sources: [raw/pointers/web_living_sources.md, reference/Source_Library.md, AGENTS.md]
confidence: stub
tags: [source, living_reference, web, wahapedia, verification, datasheet]
---

# Wahapedia (living reference)

The community rules aggregator this project uses for **unit/stat (datasheet) lookup when WarCom does not publish those profiles**, and to cross-check detachment rules. **Registered as a source; page content not yet retrieved into the KB** (cloud egress for `wahapedia.ru` was still blocked as of 2026-08-19).

---

## What this source is

| Field | Value |
|-------|-------|
| Index | <https://wahapedia.ru/> |
| Necrons hub (prefer) | <https://wahapedia.ru/wh40k11ed/factions/necrons> |
| Necrons hub (legacy path) | <https://wahapedia.ru/wh40k10ed/factions/necrons> — **edition-risk** |
| Space Marines hub | Prefer `wh40k11ed` when present; else `wh40k10ed` with flag |
| Source class | **Living web reference** - moves under us ([[ingest_procedure]]) |
| Catalogued | 2026-08-16, from [[source_library]]; policy clarified 2026-08-19 |
| **Content retrieved** | **None into KB yet.** URLs + policy registered |

`confidence: stub` still applies to *content* retrieval. This page records that the reference exists and **when agents may use it**. Any future page that cites Wahapedia must carry its own retrieval date - inheriting this page's date would be a lie about when the claim was checked.

---

## When this project uses it (allowed)

Per [`AGENTS.md`](../../AGENTS.md) Sec 10 and [[warhammer_community]] precedence:

1. **Owned faction pack / Codex / MFM** when readable in place — still preferred SoT for datasheets
2. **[[warhammer_community]]** when it freely publishes the profile, FAQ, or dataslate amendment
3. **Wahapedia is allowed** for characteristics, weapons, and datasheet abilities when WarCom does **not** publish that unit's profile (typical: WarCom ships Core / FAQs / dataslates, not full faction datasheets)

Also useful for:

- **Speed** mid-game lookup vs paging a faction pack
- **Consolidation** of split rules into one place
- **Cross-checking** — disagreement with a KB page is itself a finding (often missed errata)

It is a **community** aggregation, not a publisher. Where Wahapedia and an owned GW PDF conflict, the PDF wins and the conflict gets recorded rather than quietly resolved.

---

## The URL path question

Prefer **`wh40k11ed`** paths when they resolve. Legacy **`wh40k10ed`** paths remain registered and are **edition-risk**: confirm which edition the page serves *before* filing stats. Edition drift is an explicit lint category.

---

## How to cite it correctly

A claim sourced here is `draft` at best until the owned pack (or a WarCom amendment) agrees. Frontmatter pattern:

```yaml
sources: ["https://wahapedia.ru/wh40k11ed/factions/necrons/... (retrieved YYYY-MM-DD)"]
confidence: draft
```

And in prose: name the edition path you read (`wh40k11ed` vs `wh40k10ed`), not the edition you expected.

**Never paste Wahapedia text into this repo.** Aggregated rules text is still GW rules text. Paraphrase for teaching, cite the URL and the date ([`AGENTS.md`](../../AGENTS.md) Sec 10). Army list teaching tables under `games/warhammer_40k_11e/armies/` may carry paraphrased profile summaries with the same cite discipline.

---

## What this source does not cover

- Anything at all in the KB body until someone retrieves it - content is still empty
- Lore, modelling, or painting as SoT
- Beating a WarCom dataslate or an owned PDF on conflict

---

## Pages this source fed

None yet from a live retrieve. Named as the verification / fill-in route on [[reanimation_protocols]], [[oath_of_moment]], [[power_matrix]], [[canoptek_court]], [[cryptek_conclave]], [[gladius_task_force]], and the Necron Conclave army lists under `games/warhammer_40k_11e/armies/necrons/`.

---

## Open questions

- Does `wh40k11ed` resolve for all Necron units used in starter lists (Geomancer, Tomb Crawlers, Technomancer, Plasmancer, Royal Warden)?
- When does cloud egress for `wahapedia.ru` land so agents can fill VERIFY blanks?

---

## Related pages

- [[warhammer_community]] - the official living reference (errata / dataslates win)
- [[source_library]] - the catalog
- [[local_library_pointers]] - the owned PDFs to cross-check against
- [[index]] - master catalog
