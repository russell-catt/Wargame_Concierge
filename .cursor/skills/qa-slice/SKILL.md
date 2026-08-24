# QA slice skill

Tier-2 QA for Wargame_Concierge implementer slices. Playbook: [`docs/operations/multiagent_coordinator_strategy.md`](../../docs/operations/multiagent_coordinator_strategy.md).

## Standard checks

- Layer contract respected (`raw/` never written; `KB/` YAML only; no `wiki/`).
- UTF-8, no BOM.
- Copyright: teaching paraphrase in `KB/` and 40K armies; scoped quotes only on AGENTS Sec 10 paths.
- No GW binaries committed.
- Subagent did not `git commit` / `git push`.

## GW unofficial footer (when slice touches `games/`)

- [ ] Print HTML page 1 has **UNOFFICIAL** banner (`.gw-ip-banner`).
- [ ] Every print page has non-endorsement footer (`.gw-ip-footer`) including *completely unofficial and in no way endorsed by Games Workshop Limited*.
- [ ] No Games Workshop logos on shipping or print aids.
- [ ] Personal / no-charge / never for sale stated on exports.
- [ ] Player-facing markdown has `## Games Workshop notice` (not required on `units/research/`).
- [ ] No WarCom/GW PDF redistribution implied; event PDFs are paraphrase-first unless owner gated quote export.

Template: [`templates/Footer_Template_Gw_Print.md`](../../templates/Footer_Template_Gw_Print.md).

## Output

Write `slices/{Id}_qa.md` with PASS/FAIL rows and fix list. Mark slice **Resolved - Complete** only when PASS or waived with owner note.
