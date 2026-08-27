# S2e — Brief (40K Universal Rules Updates v1.1)

- **Track:** `dataslate_0826`
- **Slice:** S2e
- **Status:** Ready (research note filed from uploaded PDF — PDF **not** in git)
- **Depends:** [`../research/40k_universal_rules_updates_v1_1.md`](../research/40k_universal_rules_updates_v1_1.md)
- **Recommended models:** Implementer `claude-sonnet-5-thinking-high` · QA `gpt-5.6-sol-high`

## Requirements

1. Update `raw/pointers/rules_core.md`: v1.1 legal **26 Aug 2026** supersedes July v1.0 on same topics; expected local path; WarCom filename from upload.
2. Update `games/warhammer_40k_11e/rules/Core_Rules_Quotes.md`: Aug v1.1 section; retain stratagem deltas 1–4; **add** disembark → `18.06` / `18.07` paraphrase or scoped verbatim quote (filename + p.1).
3. Touch teaching surfaces that still say July-only universal updates (`Overview`, Key Concepts, glossary if needed, system/army QRs).
4. Footer/currency stamps: Universal Rules Updates **v1.1 (26 Aug 2026)**.
5. Do **not** commit the uploaded PDF binary.
6. Write `S2e_implementer.md`.

## Non-goals

- MFM / SM Codex work (other slices).
- Dumping entire Core PDF.
- Changing army datasheet paraphrase beyond transport/disembark callouts.

## Exit criteria (QA verifies)

- [ ] July v1.0 clearly superseded in pointers + Core_Rules_Quotes
- [ ] Disembark v1.1 teaching present with `18.06`/`18.07` cites
- [ ] No PDF binary in git status
- [ ] Sec 10 quote rules respected
- [ ] Legibility spot-check ≥2 rules pages + 1 QR
- [ ] Subagent did not git

## Constraints

UTF-8 no BOM. Teaching paraphrase in KB when Librarian follows.
