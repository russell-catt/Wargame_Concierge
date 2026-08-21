# S6 — Brief (KT Letter print PDFs)

- **Track:** `learn_to_play_event`
- **Slice:** S6
- **Status:** Ready
- **Depends:** S2 + S3 Resolved - Implemented
- **User gate:** none
- **Recommended models:** Implementer `inherit`; QA print-preview

## Requirements

KT Letter print pack under `games/kill_team_2024/print/`. Shared + PM + Kommandos 2-pagers. Valid-target cheat sheet: Letter landscape, 1 page OK. PDFs to **same** folder as S5 with `kt_` prefixes. Datacards optional multi-page, same folder.

## Exit criteria (QA verifies verbatim)

- [ ] Each listed KT aid exists
- [ ] Letter; ≤2 pages except datacards / valid-target sheet
- [ ] All S6 PDFs in `C:\Personal\print_aids\learn_to_play_event\`
- [ ] No `.pdf` in git

## Constraints

Same print CSS/pipeline as S5. Teaching `.md` may stay long; print HTML is the cut.
