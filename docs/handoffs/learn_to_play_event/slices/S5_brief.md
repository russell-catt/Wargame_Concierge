# S5 — Brief (40K Letter print PDFs)

- **Track:** `learn_to_play_event`
- **Slice:** S5
- **Status:** Ready
- **Depends:** Preflight (parallel with L0/S1 OK)
- **User gate:** none
- **Recommended models:** Implementer `inherit`; QA print-preview

## Requirements

2-page Letter heading-styled HTML under `games/warhammer_40k_11e/armies/necrons/print/` for: roster, 250 reference, Necron QR, first-game core, setup/terrain. Write PDFs only to `C:\Personal\print_aids\learn_to_play_event\` with `40k_` prefix. Codex wall.

## Exit criteria (QA verifies verbatim)

- [ ] Each listed aid exists (HTML)
- [ ] `@page` US Letter; heading hierarchy
- [ ] QA print-preview ≤2 pages per aid
- [ ] Every S5 PDF in the one print folder
- [ ] No `.pdf` committed to git

## Constraints

Armies paraphrase only. No Faction Pack dump.
