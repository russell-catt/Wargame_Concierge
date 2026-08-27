# L1 — Librarian enhance — dataslate_0826

**Slice:** L1 — Librarian enhance (KB sync after S1–S3 shipping)
**Status:** Complete
**Date:** 2026-08-27
**Model:** `claude-sonnet-5-thinking-high`
**Authorization:** Owner 2026-08-27 — AUTHORIZED; never write `raw/`; never `git commit`/`git push`; KB YAML frontmatter only; teaching paraphrase; `confidence: draft` accepted.
**Skill:** [`.cursor/skills/librarian-enhance/SKILL.md`](../../../../.cursor/skills/librarian-enhance/SKILL.md)

## Summary

Read the completed shipping slices (S1, S2b, S2c, S2d, S2e, S3) and synced `KB/` to match: recosted the one owned unit whose points actually moved (Necron Warriors), confirmed and recorded the one faction whose points did **not** move (Space Marines), added four new glossary terms (three disembark-move terms from Universal Rules Updates v1.1, one Legendary Proxies term from the SM Codex October preview, explicitly distinguished from the pre-existing Warhammer Legends entry), refreshed `KB/index.md` summaries, and back-linked every touched page plus two additional existing source pages (`warcom_free_core_rules_11e`, `nemesis_operatives`, `kill_team_2024_core_rules`) to the new L0 package sources.

## Sync checklist (librarian-enhance)

- [x] **Sources** — L0's three new source pages already carry retrieval dates and tier notes; this pass added a supersession back-link from `warcom_free_core_rules_11e.md` (July v1.0 → Aug v1.1) rather than creating a duplicate.
- [x] **Entities** — `KB/units/necron_warriors.md` (points recost), `KB/factions/necrons.md` (Phase 1 list total), `KB/factions/space_marines.md` (currency stamp + Oct preview pointer). No Kill Team KB entity pages exist for Tomb World killzone / Nemesis Ops / Hierotek Circle beyond the source pages already updated — S3's teleport/breach/Towering/regen deltas are recorded on [[kt_aug_2026_balance_package]] (L0) rather than duplicated onto entity stubs that don't yet exist in `KB/`.
- [x] **Index** — `KB/index.md` refreshed: three new source rows, five updated one-liners (Necron Warriors, Necrons, Space Marines, warcom_free_core_rules_11e, plus the new KT source row), frontmatter version bump.
- [x] **Log** — `KB/log.md` two entries appended: one `ingest` (L0 source stubs) and one `enhance` (L1 sync).
- [x] **Back-links** — every new source cross-links the other two; entity pages link back to the sources; two pre-existing sources (`nemesis_operatives`, `kill_team_2024_core_rules`) gained a forward link to `kt_aug_2026_balance_package`.
- [x] **Glossary** — four new terms, all `draft`: Disembark move (context), Assault disembark move (`18.06`), Shock disembark move (`18.07`), Legendary Proxies. No conflicts with existing entries — Legendary Proxies is explicitly written to *not* be confused with the pre-existing Warhammer Legends entry (different mechanism: borrows a datasheet vs. keeps its own Legends stats), and both entries now cross-link.

## Contradiction / conflict check

None found. Shipping (S2c/S2d/S2e/S3) and prior KB claims agree everywhere checked:

- Necron Warriors 80→85 is a genuine points move, not a KB error — recosted, not flagged.
- Space Marines MFM v1.3 confirmed **no** change to any owned Blood Ravens cost — KB now states this explicitly rather than staying silent on it.
- SM Codex October preview is explicitly **not yet legal** — KB glossary and faction page both state "not table-legal yet" to prevent premature adoption.
- KT package (Tomb World, Nemesis Ops, Hierotek) already matched the shipping paraphrase in the L0 source page; no entity-level KB page existed to drift, so no correction was needed there.

## Pages created (L0, listed here for the combined receipt)

- `KB/sources/40k_aug_2026_balance_package.md`
- `KB/sources/kt_aug_2026_balance_package.md`
- `KB/sources/sm_codex_oct_2026_preview.md`

## Pages updated (L1)

- `KB/units/necron_warriors.md` — MFM v1.3 points (85), version 0.1.2 → 0.1.3
- `KB/factions/necrons.md` — Phase 1 Conclave list total (250 pts), version 0.5.2 → 0.5.3
- `KB/factions/space_marines.md` — MFM v1.3 currency (no change) + Codex Oct preview section, version 0.6.1 → 0.6.2
- `KB/sources/warcom_free_core_rules_11e.md` — v1.0 marked superseded, version 0.5.1 → 0.5.2
- `KB/sources/nemesis_operatives.md` — back-link to `kt_aug_2026_balance_package`
- `KB/sources/kill_team_2024_core_rules.md` — back-link to `kt_aug_2026_balance_package`
- `KB/glossary.md` — four new terms, term-count table updated, version 0.5.4 → 0.5.5
- `KB/index.md` — three new source rows, five refreshed summaries, version 0.5.8 → 0.5.9
- `KB/log.md` — two appended entries (`ingest` L0, `enhance` L1)

## No-op waivers (explicit)

- **Kill Team entity pages** (killzones, Nemesis Ops, team pages) — no `KB/setup/` or `KB/factions/` page exists yet for Tomb World killzone, Nemesis Ops, or any KT24 team, so there is nothing in `KB/` to drift against the S3 shipping changes. The teaching deltas (teleport/breach, Towering Size, Hierotek regen timing) are fully captured on [`kt_aug_2026_balance_package.md`](../../../../KB/sources/kt_aug_2026_balance_package.md) instead. Waived as a no-op for entity sync; flag for a future KT24 setup/team KB scaffold if the owner wants per-killzone or per-team KB pages.
- **`KB/overview.md`** — not touched. Nothing in this track shifts the KB's big picture (still three systems, still Necrons/SM primary, still draft-heavy); a points recost and a preview banner don't warrant an overview rewrite.
- **`KB/changelog.md`** — not touched. This track ships into `games/`, not into a KB→docs/games promotion; changelog is for KB promotions, and no KB page was promoted this pass.

## Compliance

- No file written under `raw/`.
- No PDF read or committed by the Librarian.
- No `git add` / `git commit` / `git push` run.
- Every touched `KB/` page keeps YAML frontmatter only (no Rising Tide headers); every new/updated claim keeps `confidence: draft` and a retrieval date where it traces to a living/owner-paste source.

## Exit criteria (self-check against L1 brief)

- [x] Source pages no longer stubs-only where shipping claims rely on them — all three L0 pages carry teaching paraphrase + shipping-impact tables, not bare stubs.
- [x] Log entries for this track (ingest + enhance).
- [x] librarian-enhance checklist PASS (see above) — no waivers needed except the two explicit no-ops recorded.
- [x] No `raw/` writes; YAML frontmatter valid on every touched page.
- [x] Subagent did not git.
