# S2 — Brief (40K 11e shipping impact)

- **Track:** `dataslate_0826`
- **Slice:** S2
- **Status:** Ready
- **Depends:** QA-S1 PASS
- **Recommended models:** Implementer `claude-sonnet-5-thinking-high` · QA `gpt-5.6-sol-high`

## Inherited documentation

- S0 impact matrix (40K rows)
- [`../research/warcom_40k_balance_commentary_aug.md`](../research/warcom_40k_balance_commentary_aug.md) — Aug package framing (Orks excluded; FD map tweaks; Sep last monthly)
- Staging: Faction Packs v1.2 + Universal Rules v1.1 + MFM v1.3 research notes
- `games/warhammer_40k_11e/**` — Necrons + Space Marines lists, QRs, Key Concepts, setup/rules teaching
- AGENTS Sec 10 Codex wall

## Requirements

1. Walk impact matrix for **onboarded** factions (Necrons, SM); apply MFM v1.3 / FP v1.2 teaching deltas (S2c/S2d/S2e may own subsets — do not duplicate if those slices run).
2. Setup / Force Disposition: note WarCom map-layout adjustments (more six-objective Disruption maps; expansion terrain nudges) — paraphrase + pointer; do not invent map IDs without Event Companion PDF.
3. Stamp currency for Aug 26 package (MFM v1.3 / FP v1.2 / Universal Rules v1.1 as applicable) — not a fictional “Balance Dataslate” filename if none exists.
4. Do **not** dump Faction Pack / MFM tables; Codex wall intact.
5. Write `S2_implementer.md` with file list + no-op waivers (out-of-scope factions named in WarCom commentary = waiver).
6. Flag no-op paths explicitly.

## Exit criteria (QA verifies)

- [ ] Every changed file has currency stamp with locked 40K date
- [ ] Codex wall intact under `armies/**`
- [ ] Enhancement regression bar (qa-slice skill): prior Core IDs / teaching facts not silently deleted
- [ ] Legibility spot-check: QA reads ≥3 changed pages for scannability (headers, banners, no wall-of-text regressions)
- [ ] No binaries; no raw binary writes
- [ ] Subagent did not git commit/push

## Constraints

Prefer update-in-place. Wahapedia only as draft cross-check with retrieval date.
