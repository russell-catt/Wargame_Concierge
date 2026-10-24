# S1 — Reopen

- **Track:** `dataslate_0930`
- **Slice:** S1
- **From:** S1 QA FAIL (2026-10-01)
- **Status:** Handed back to the Implementer

## Findings to fix

1. `games/warhammer_40k_11e/armies/necrons/print/40k_roster_1000_v1_doomstalker_conclave.html` still says "If owned MFM says Doomstalker 145" and lists alternate totals. Remove that conditional. Doomstalker is 130. Then regenerate the 1000 roster PDF.
2. `games/warhammer_40k_11e/armies/necrons/Cryptek_Play_Pack_1000.md` still says a 145-point Doomstalker would make the list 950. Remove that sentence. The pack total stays 935.

Do not change other files. Do not delete a unit.
