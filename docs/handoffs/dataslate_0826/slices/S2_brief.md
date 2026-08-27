# S2 — Brief (40K 11e shipping impact)

- **Track:** `dataslate_0826`
- **Slice:** S2
- **Status:** Ready
- **Depends:** QA-S1 PASS
- **Recommended models:** Implementer `claude-sonnet-5-thinking-high` · QA `gpt-5.6-sol-high`

## Inherited documentation

- S0 impact matrix (40K rows)
- `games/warhammer_40k_11e/**` — Necrons + Space Marines lists, QRs, Key Concepts, setup/rules teaching
- AGENTS Sec 10 Codex wall

## Requirements

1. Walk S0 impact matrix for 40K; for each hit, update teaching paraphrase (points callouts, detachment notes, list honesty, QR banners).
2. If local dataslate PDF missing: mark changed claims `draft` / “verify owned PDF” — do not invent numbers.
3. Stamp **Rules currency: Balance Dataslate \<date\>** on every touched player-facing md/HTML footer or Games Workshop notice.
4. Do **not** dump dataslate tables or Faction Pack text.
5. Write `S2_implementer.md` with file list + before/after intent per file.
6. Flag no-op paths explicitly (“unchanged — dataslate silent”).

## Exit criteria (QA verifies)

- [ ] Every changed file has currency stamp with locked 40K date
- [ ] Codex wall intact under `armies/**`
- [ ] Enhancement regression bar (qa-slice skill): prior Core IDs / teaching facts not silently deleted
- [ ] Legibility spot-check: QA reads ≥3 changed pages for scannability (headers, banners, no wall-of-text regressions)
- [ ] No binaries; no raw binary writes
- [ ] Subagent did not git commit/push

## Constraints

Prefer update-in-place. Wahapedia only as draft cross-check with retrieval date.
