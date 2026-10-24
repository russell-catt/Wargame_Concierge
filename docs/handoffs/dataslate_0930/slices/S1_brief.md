# S1 — Brief (Necron points)

- **Track:** `dataslate_0930`
- **Slice:** S1
- **Status:** Ready
- **Depends:** S0 QA PASS
- **Models:** Implementer grok-4.7 · QA `gpt-5.6-sol-medium`

## Inherited documentation

- [`track_in.md`](../track_in.md)
- [`research/mfm_v1_5_2026_09_30.md`](../research/mfm_v1_5_2026_09_30.md) — apply only the Necron delta table

## Requirements

Recost every Conclave list that contains Immortals, Tomb Crawlers, or the Doomstalker.

- Immortals 5: 70 → 65. Immortals 10: 140 → 130.
- Tomb Crawlers (2): 50 → 60.
- Doomstalker: 140 → 130. Close the 140-versus-145 note.
- Unchanged: Warriors 10 = 85, Scarabs, Macrocytes 70, characters, Gauntlet 20, Atomic Disintegrators 10.
- Every list stays on Cryptek Conclave at **2DP**.
- 1000 V1 target: body **905** + 30 enhancements = **935 / 1000**. Same attachments, same two enhancements.
- Update [`How_Your_Army_Works_1000.md`](../../../../games/warhammer_40k_11e/armies/necrons/How_Your_Army_Works_1000.md), [`Cryptek_Play_Pack_1000.md`](../../../../games/warhammer_40k_11e/armies/necrons/Cryptek_Play_Pack_1000.md), the 1000 roster print HTML, and regenerate that PDF outside git.
- Stamp the Necron army README and the 40K README so Necron points cite MFM v1.5 (retrieved 2026-10-01, `draft`). Space Marine lists stay on v1.3 in that currency line.

If a recost exceeds the list's cap, write the arithmetic and the smallest legal cut in the implementer report and on the list as an over-cap banner. Do not delete a unit or enhancement. Coordinator brings the cut to the owner. Known risk: the 250 list was exactly 250, and Crawlers +10 pushes it over.

No Necron weapon or Toughness rewrite.

## Exit criteria (QA verifies)

- [ ] Arithmetic matches the S0 table
- [ ] 1000 V1 is 935 with the same two enhancements
- [ ] Over-cap lists name a cut and do not apply it
- [ ] Codex wall intact
- [ ] 1000 roster HTML still has the UNOFFICIAL banner and the GW footer; PDF is 3 pages
- [ ] UTF-8, no BOM; no git

## Constraints

Teaching paraphrase. Do not dump the MFM.
