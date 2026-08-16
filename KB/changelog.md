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
