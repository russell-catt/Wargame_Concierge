# S1 — Brief (pointers + footer currency convention)

- **Track:** `dataslate_0826`
- **Slice:** S1
- **Status:** Ready
- **Depends:** QA-S0 PASS
- **Recommended models:** Implementer `claude-sonnet-5-thinking-high` · QA `gpt-5.6-sol-high`

## Inherited documentation

- S0 locked dates + resolved URLs
- [`templates/Footer_Template_Gw_Print.md`](../../../../templates/Footer_Template_Gw_Print.md)
- [`raw/pointers/web_living_sources.md`](../../../../raw/pointers/web_living_sources.md)
- [`reference/Source_Library.md`](../../../../reference/Source_Library.md)

## Requirements

1. Add/update markdown pointers for the **40K Aug package** (Universal Rules / FP / MFM — not necessarily one dataslate file) and the **KT package** (**Core rules update + team updates** — **no** singular `balance_dataslate_kt_*.md` filename required; name pointers after real PDFs / package stamp).
2. Update `web_living_sources.md`, `kill_team_web_living_sources.md` (if present), and `Source_Library.md` catalog rows with **retrieval dates**.
3. Extend GW footer templates with the **optional currency lines** from `track_in.md` (incl. KT quarterly package stamp; do not remove UNOFFICIAL / non-endorsement sentences).
4. Note in pointer docs: PDFs stay outside git; read in place once owner saves them.
5. Write `S1_implementer.md`.

## Exit criteria (QA verifies)

- [ ] Pointers name WarCom URLs + package dates/stamps + local path expectations; KT not framed as a missing singular dataslate
- [ ] Template currency section present; banner/footer A–D still required
- [ ] No binaries committed
- [ ] Librarian did not need to write `raw/` (Implementer owns pointers)
- [ ] Subagent did not git commit/push

## Constraints

Never copy PDF bytes into the repo. UTF-8 no BOM.
