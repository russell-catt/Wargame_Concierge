# S2c — Brief (Necron MFM v1.3 points pass)

- **Track:** `dataslate_0826`
- **Slice:** S2c
- **Status:** Ready (research note filed)
- **Depends:** [`../research/necron_mfm_v1_3.md`](../research/necron_mfm_v1_3.md); preferably after S1 pointers; may start with owner auth before full dataslate lock
- **Recommended models:** Implementer `claude-sonnet-5-thinking-high` · QA `gpt-5.6-sol-high`

## Requirements

1. Recost all Necron Conclave / starter / army-list shipping that cite **MFM v1.2** Warrior (and other ▲) costs to **v1.3** — teaching paraphrase + version stamp; no full MFM dump.
2. Priority files: `Starter_250.md`, `Starter_500.md`, `Starter_Forces_500_750_1000.md`, `Army_List_*_Conclave.md`, Necron README/QR if they hardcode Warrior pts, research unit pages for ▲ units.
3. Re-total every list that claimed “exactly N points”; if over, adjust with owner-safe cuts (document choices) — do not invent free points.
4. Stamp footers/notices: MFM Necrons **v1.3** (+ paste/PDF retrieval date).
5. Update `raw/pointers/points_manuals.md` version line (Implementer — not Librarian).
6. Write `S2c_implementer.md` with before/after totals table.

## Non-goals

- Pasting the entire MFM unit table into git.
- Changing Force Disposition teaching unless paste contradicts (Conclave = Priority Assets — confirm only).
- SM Codex / KT work (other slices).

## Exit criteria (QA verifies)

- [ ] No shipping list still cites Warriors 10 @ 80 as current MFM
- [ ] Every retotalled list arithmetic checks
- [ ] Version stamps say v1.3
- [ ] Codex wall intact (no datasheet dumps)
- [ ] Legibility spot-check ≥3 Conclave list pages
- [ ] Subagent did not git

## Constraints

Owned PDF wins if paste conflicts. Mark `draft` until PDF path confirmed.
