---
title: Changelog
type: changelog
system: warhammer_40k_11e
created: 2026-08-16
updated: 2026-08-17
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
| 2026-08-16 | L1 (`tomb_world_ownership`) | **Ownership correction, not a promotion.** **Kill Team: Tomb World recorded as owned and game-ready** (Geomancer, 2 Tomb Crawlers, 5 Macrocytes, 10 Warriors, 3 Scarab Swarms), with dual Warriors / Scarabs inventory (20 / 6) and the Hierotek Circle datasheet TBD preserved. The prior "not owned" claim and the standing **"do not let Tomb World leak"** rule are both retired to the deprecated list. Logged here under the "rules claim in shipping content is corrected after verification" trigger, because the false claim had already reached `games/` and `docs/`. Nine content pages updated, plus [[log]] and this file; see [[log]] for the per-page table. | [[necron_lists_owner_notes]] | `KB/**` (10 pages); shipping surfaces are S1-S3's to correct | Pending Coordinator |
| 2026-08-16 | L1 | **Rules correction, not a promotion.** `Power Matrix` re-attributed from "possibly Kill Team, unresolved" to the **Canoptek Court detachment rule in Warhammer 40,000 11e**, on two independent in-repo sources. Logged here per the "rules claim corrected after verification" trigger above. The claim had not reached shipping content, so nothing downstream needed amending. | [[power_matrix]] | `KB/glossary.md` (entry + deprecated list) | Pending Coordinator |
| 2026-08-16 | L2 lint (`v1_scaffold`) | Unit index pointers; glossary consistency; UTF-8 cleanup. *(Row relocated into this table by L2 of `tomb_world_ownership` - it had been appended below the Related pages section, outside the table.)* | - | `KB/units/*`, `KB/glossary.md` | Pending Coordinator |
| 2026-08-16 | L2 (`tomb_world_ownership`) | **Rules correction, not a promotion.** The Cryptek Conclave detachment rule renamed across `KB/` from the owner's informal **"Scientific Schemes"** to **Technosorcerous Augmentations**, with both effects recorded from the owned faction pack v1.1 (p.7, read 2026-08-16) and cross-checked on Wahapedia. The `v1_scaffold` L2 pass recorded this as a *preference* but left four `KB/` pages carrying the old label; this pass applies it and deprecates the old name. Source pages keep the old label with a conflict flag, per [`AGENTS.md`](../AGENTS.md) Sec 9. Logged under the "rules claim in shipping content is corrected after verification" trigger. | [[cryptek_conclave]] | `KB/glossary.md`, `KB/detachments/cryptek_conclave.md`, `KB/factions/necrons.md`, `KB/concepts/power_matrix.md`, `KB/sources/necron_lists_owner_notes.md`, `KB/analyses/inherited_docs_for_S3.md` | Pending Coordinator |
| 2026-08-16 | L2 (`tomb_world_ownership`) | **Ownership correction reaching shipping content.** Two `games/` Necron detachment guides were still reasoning from the retired "Tomb World not owned" claim after L1 corrected `KB/`, and so contradicted it. `Canoptek_Court.md` v1.1 - fit table rebuilt into game-ready / on-sprue / not-owned, and the verdict "not first, on this collection" reversed, since four of five game-ready Tomb World units are Cryptek or Canoptek. `Cryptek_Conclave.md` v1.1 - fit table rebuilt, the omitted owned **Cryptek Geomancer** added, and "the whole path hinges on whether the Hierotek Circle contains a Cryptek" downgraded to an upside. Both flag the Geomancer, Tomb Crawlers and Macrocytes as **not yet costed from MFM v1.2**. No rules content changed on either page. | [[necrons]], [[canoptek_court]], [[cryptek_conclave]] | `games/warhammer_40k_11e/armies/necrons/Canoptek_Court.md`, `.../Cryptek_Conclave.md` | Pending Coordinator |
| 2026-08-17 | L1 (`kill_team_2024_scaffold`) | **First Kill Team 2024 ingest - no promotion into `docs/` or `games/`.** 1 source page and 6 concept pages created, all `confidence: draft`, cross-checked only against a living web reference (Wahapedia). The owned Core Rules PDF is unopened. Nothing here meets the `verified` bar Sec 11 requires for promotion, matching the reasoning that kept L1 of `v1_scaffold` from promoting anything. `KB/glossary.md` and `KB/overview.md` also became multi-system in this pass (new `systems:` frontmatter field). | [[kill_team_2024_core_rules]] | - (none) | n/a |
| 2026-08-17 | L2 (`kt24_rules_quotes`) | **KT24 shipping — quote exception, not KB dump.** Target eligibility verbatim corpus + one-page HTML cheat sheet; Canoptek (5) + Plague (7) HTML datacards from local Teams PDFs. Policy: `AGENTS.md` Sec 10 + `games/kill_team_2024/README.md`. KB: policy row in [[glossary]], [[kill_team_2024_core_rules]] updated — no datacard text in KB. | [[kill_team_2024_core_rules]], `raw/pointers/kill_team_2024_*` | `games/kill_team_2024/rules/Target_Eligibility*.md/html`, `games/kill_team_2024/teams/{canoptek_circle,plague_marines}/cards/*.html` | Pending Coordinator |

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
