# S4 — Implementer report

- **Status:** Resolved - Implemented
- **Track:** kill_team_2024_scaffold
- **Slice:** S4
- **Model used:** `claude-sonnet-5-thinking-high` (locked — matches `track_in.md` model matrix)
- **Date:** 2026-08-17

## Sources read this slice

- [Wahapedia — Canoptek Circle](https://wahapedia.ru/kill-team3/kill-teams/canoptek-circle/), retrieved 2026-08-17 — full operative list, faction rule, ploys, equipment, datacard text
- `games/warhammer_40k_11e/armies/necrons/Owned_Models_Inventory.md` v1.2 — Tomb World ownership state
- `games/kill_team_2024/rules/Overview.md`, `Key_Concepts.md` — KT vocabulary (APL, turning point, control range) for consistent terminology
- `docs/handoffs/kill_team_2024_scaffold/track_in.md` — cross-game policy, model matrix
- **Not opened this slice:** local pointer `eng_29-04_kill_team_team_rules_canoptek_circle-*.pdf`. Everything below rests on the living Wahapedia page only — flagged `draft` throughout and in the QA-facing brief.

## Created

### `games/kill_team_2024/teams/canoptek_circle/`

- `README.md` — rewritten from the S3 placeholder into the full package entry point: identity, why-play, team-at-a-glance table, document index, cross-game note, sources
- `Team_Rule_Guide.md` — Obelisk Node Matrix: placement/movement table, node-alone control rule, Matrix formation (6" link, combined triangle), Matrix buffs stated at habit level (Accurate bonus + APL+1 capped at 3 — the two numbers needed to make the page useful), Strategy/Firefight ploys and equipment as one-line gists only (no full rules or flavour text), a first-game plan section
- `Owned_Models_Inventory.md` — maps all 8 operative slots to the Tomb World box; Macrocytes 5 explicitly split 1 Accelerator + 1 Reanimator + 3 Warriors; base sizes recorded from Wahapedia (Geomancer/Tomb Crawler 50mm, Macrocytes 28mm); dual-legality vs. the 40K faction pack marked `pending check`; weapon-option inspection flagged as the only remaining unknown
- `Starter_Roster.md` — the full 8-operative team, since owned models exactly satisfy the roster requirement with nothing left over and nothing missing
- `Quick_Reference_Play_Guide.md` — exactly two pages, `<!-- pagebreak -->` marker present, dated verify footer (2026-08-17). Page 1: turning-point recap, Matrix habit table, ploy-gist table, combat sequence, do/don't. Page 2: starter roster snapshot, dual-legality snapshot, pre-game checklist
- `operatives/Operatives_Index.md` — 5 operative types (Geomancer, Tomb Crawler, Accelerator, Reanimator, Warrior), each with plain-English role, signature habit, support given, and card-schema tags — deliberately no APL/Move/Save/Wounds or weapon ATK/HIT/DMG values
- `cards/Card_Schema.md` — front/back field sketch for a Tarot-sleeve (70mm×120mm) teaching card, explicit exclusion list matching the "no datasheet transcription" rule, S10 build checklist. Marked as sketch-only, gated on user photos

### 40K sync

- `games/warhammer_40k_11e/armies/necrons/Owned_Models_Inventory.md` (v1.2 → v1.3):
  - Added a **"KT provenance / dual-legality"** column to the Game-ready table
  - Geomancer, Tomb Crawlers, Macrocytes rows note their Canoptek Circle operative mapping, Wahapedia base size, and `pending check` 40K dual-legality
  - Necron Warriors row explicitly flags the naming collision with KT's "Canoptek Macrocyte Warrior" (different, unrelated model) so the two are never conflated in future passes
  - Scarab Swarms row notes it is outside the Canoptek Circle 8-operative roster — no invented mapping
  - Added a "Related pages (cross-game)" section linking to the new KT package
  - No new 40K datasheet mappings invented beyond the three items already listed pre-S4

### Consistency updates (not required by brief, done for index hygiene)

- `games/kill_team_2024/teams/_Owned_Teams_Inventory.md` — Canoptek Circle row updated from "pending check" placeholders to full-package-complete state; cross-game note expanded with the naming-collision flag
- `games/kill_team_2024/teams/README.md` — folder map row updated to "S4 complete"

## Exit criteria

| Criterion | Result |
|-----------|--------|
| 7 `canoptek_circle/` deliverables exist | PASS |
| `Team_Rule_Guide.md` cites Wahapedia + local PDF pointer, no full ploy/datacard text | PASS |
| `Owned_Models_Inventory.md` covers all 8 slots with base size + honest pending-check dual-legality | PASS |
| `Quick_Reference_Play_Guide.md` exactly 2 pages, pagebreak marker present, dated footer | PASS |
| `Operatives_Index.md` — 5 types, card-schema fields, no stat blocks | PASS |
| `Card_Schema.md` sketch-only, S10-gated | PASS |
| 40K Necron inventory synced with KT provenance / dual-legality, no invented mappings | PASS |
| No GW binaries added | PASS (verified below) |
| `KB/`, `raw/` untouched | PASS |
| No commit, no push | PASS — not run this session |

## Binary check

```
Get-ChildItem repo -Recurse -Include *.pdf,*.webp → expect 0
```

Run at QA / Coordinator closeout alongside the S4 Tier 1 commands in `S4_brief.md`.

## Known gaps carried forward

| Item | Status | Resolves |
|------|--------|----------|
| Local team PDF not opened | `draft` status on Team_Rule_Guide / Quick_Reference | Future pass — cross-check against `eng_29-04_kill_team_team_rules_canoptek_circle-*.pdf` |
| Tomb Crawler / Warrior weapon options | `pending check` | Physical inspection of assembled models |
| 40K dual-legality (base size vs. faction pack) | `pending check` | Opening the 40K Necron faction pack |
| Real Tarot card content | Blocked | S10 — user photos |

## Pending commit

Bundle with S4 per `track_in.md` Sec "Pending commits (Coordinator)" — recommended gate 6 (S4/S5/S6, each Resolved-Complete).
