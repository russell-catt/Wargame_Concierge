# S5 — Brief (game cores + footer stamp sweep)

- **Track:** `dataslate_0826`
- **Slice:** S5
- **Status:** Ready
- **Depends:** QA-S4 PASS
- **Recommended models:** Implementer `claude-sonnet-5-thinking-high` · QA `gpt-5.6-sol-high`

## Inherited documentation

- Game core inventory in [`track_in.md`](../track_in.md)
- Footer convention (40K / KT currency; Warcode N/A)

## Requirements

1. Editing pass on **each game’s core files** (40K, KT24, Warcode) per inventory.
2. Sweep remaining player-facing GW footers / Games Workshop notices that S2/S3 missed but should show dataslate freshness (prefer high-traffic: QRs, Event_Ready, Learn-to-play, army/team READMEs). Document skip list for low-traffic `units/research/`.
3. Warcode: apply **Last reviewed / not affected by GW Balance Dataslates** stamp; do **not** introduce banned GW proper nouns.
4. Spot-check print HTML samples still have UNOFFICIAL banner + footer **plus** currency line where applicable.
5. Write `S5_implementer.md` with sweep coverage table.

## Exit criteria (QA verifies)

- [ ] All three game READMEs current
- [ ] Footer sample audit: ≥5 40K + ≥5 KT pages show currency date (or justified skip)
- [ ] Warcode ban intact (`qa-slice` Warcode checklist)
- [ ] Print UNOFFICIAL requirements not regressed
- [ ] Legibility spot-check on README + one QR per GW system
- [ ] Subagent did not git

## Constraints

Additive currency lines only. No GW logos. No binary commits.
