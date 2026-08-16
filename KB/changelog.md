---
title: Changelog
type: changelog
system: warhammer_40k_11e
created: 2026-08-16
updated: 2026-08-16
sources: []
confidence: verified
tags: [changelog, promotion, governance]
---

# KB Changelog

The **promotion log**. One row every time KB knowledge is promoted into shipping content under `docs/` or `games/`, or whenever the schema itself changes.

This is not the activity log - day-to-day ingests, queries, and lint passes go in [[log]]. This file answers a narrower question: *what player-facing content came from which KB page, and when?*

---

## When to add a row

- A KB page is promoted into `docs/` or `games/`
- A promoted page is materially revised or superseded
- The schema in [`AGENTS.md`](../AGENTS.md) changes (entity types, frontmatter, naming, workflows)
- A rules claim in shipping content is corrected after verification

Promotion requires human or Coordinator approval first - see [`AGENTS.md`](../AGENTS.md) Sec 11 (Promote). The Librarian drafts; it does not ship unilaterally, and it never commits.

---

## Promotions

| Date | Slice | Change | KB source | Target | Approved by |
|------|-------|--------|-----------|--------|-------------|
| 2026-08-16 | L0 | KB bootstrap - schema, core pages, and typed directory guides created. `AGENTS.md` v1.0 established as schema SoT; `librarian_agent.md` added for day-to-day ops. No content promotion: 0 sources ingested, 0 entity pages. | - (bootstrap) | `AGENTS.md`, `KB/*`, `docs/operations/librarian_agent.md` | Pending Coordinator |
| 2026-08-16 | L1 | First ingest - 5 sources, 15 entity pages. **No promotion into `docs/` or `games/`.** Everything stays in `KB/` because 0 game terms reached `verified` and no rules document was read. | - | - (none) | n/a |
| 2026-08-16 | L1 | **Rules correction, not a promotion.** `Power Matrix` re-attributed from "possibly Kill Team, unresolved" to the **Canoptek Court detachment rule in Warhammer 40,000 11e**, on two independent in-repo sources. Logged here per the "rules claim corrected after verification" trigger above. The claim had not reached shipping content, so nothing downstream needed amending. | [[power_matrix]] | `KB/glossary.md` (entry + deprecated list) | Pending Coordinator |

**Why L1 promoted nothing.** [`AGENTS.md`](../AGENTS.md) Sec 11 requires `confidence: verified`, or a stated exception, before a page ships. After L1 the KB holds one planning document and a source catalog - enough for a working synthesis, not enough for player-facing truth. The material that would change that is catalogued in [[local_library_pointers]] and unread. [[inherited_docs_for_S3]] sets out exactly which facts are stable enough for S3 to teach from.

---

## Schema versions

| Version | Date | Change |
|---------|------|--------|
| v1.0 | 2026-08-16 | Initial schema. Karpathy `CLAUDE.md` adapted to wargames: `wiki/` becomes `KB/`; wargame entity types; glossary-only Keywords; `confidence` field and retrieval-date requirement added for a new edition; `snake_case` KB filenames. |

---

## Related pages

- [[log]] - chronological activity record
- [[index]] - master catalog
- [`AGENTS.md`](../AGENTS.md) - schema source of truth
- [`docs/operations/librarian_agent.md`](../docs/operations/librarian_agent.md) - promotion workflow in practice
