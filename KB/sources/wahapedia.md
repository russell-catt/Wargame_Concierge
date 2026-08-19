---
title: Wahapedia (living reference)
type: source
system: warhammer_40k_11e
created: 2026-08-16
updated: 2026-08-19
version: 0.5.3
sources: [raw/pointers/web_living_sources.md, reference/Source_Library.md, AGENTS.md, their_number_is_legion_potentiality_syphon_250]
confidence: draft
tags: [source, living_reference, web, wahapedia, verification, datasheet]
---

# Wahapedia (living reference)

The community rules aggregator this project uses for **unit/stat (datasheet) lookup when WarCom does not publish those profiles**, and to cross-check detachment rules.

**Policy (AGENTS.md Sec 10):** owned pack → WarCom when it publishes the profile/amendment → Wahapedia allowed when WarCom does not. Prefer `wh40k11ed`; flag `wh40k10ed`; retrieval date + `draft` until owned-pack cross-check; PDF wins on conflict.

---

## What this source is

| Field | Value |
|-------|-------|
| Index | <https://wahapedia.ru/> |
| Necrons hub (prefer) | <https://wahapedia.ru/wh40k11ed/factions/necrons> |
| Necrons hub (legacy) | <https://wahapedia.ru/wh40k10ed/factions/necrons> — **edition-risk** |
| Source class | **Living web reference** ([[ingest_procedure]]) |
| Policy clarified | 2026-08-19 |
| **Content retrieved into KB** | Partial — Warriors + Necrons hub used **2026-08-19** for Legion / Syphon teaching paraphrase; full faction ingest not done |

---

## Pages this source fed

| Page | What was taken | Retrieved |
|------|----------------|-----------|
| [[their_number_is_legion_potentiality_syphon_250]] | Their Number is Legion; Potentiality Syphon paraphrase | 2026-08-19 |
| [[reanimation_protocols]] | Cross-check amplifiers / timing against shipping | 2026-08-19 |
| Shipping army lists under `games/.../necrons/` | Profile fills (MFM + Wahapedia; not KB dump) | 2026-08-19 |

Still named as the verification route on [[oath_of_moment]], [[power_matrix]], [[canoptek_court]], [[cryptek_conclave]], [[gladius_task_force]].

---

## How to cite

```yaml
sources: ["https://wahapedia.ru/wh40k11ed/factions/necrons/... (retrieved YYYY-MM-DD)"]
confidence: draft
```

**Never paste Wahapedia text into this repo.** Teaching paraphrase only ([`AGENTS.md`](../../AGENTS.md) Sec 10).

---

## Open questions

- Broader unit-by-unit KB ingest still outstanding
- Cloud egress for `wahapedia.ru` remains allowlist-dependent for some agents

---

## Related pages

- [[warhammer_community]] · [[source_library]] · [[local_library_pointers]] · [[index]]
