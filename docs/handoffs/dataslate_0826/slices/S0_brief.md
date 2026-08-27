# S0 — Brief (resolve links + inventory)

- **Track:** `dataslate_0826`
- **Slice:** S0
- **Status:** Ready — blocked on WarCom egress or owner paste
- **Depends:** Preflight Complete + user auth for execution beyond research notes
- **Recommended models:** Implementer `composer-2.5-fast` · QA `gpt-5.6-sol-high`

## Inherited documentation

- [`track_in.md`](../track_in.md) — L1–L3 URLs, trust ladder, locked date table (fill here)

## Requirements

1. Resolve L1, L2, L3 optiext URLs to canonical `warhammer-community.com` article (or downloads) URLs.
2. Record for each: title, publish date, system (40K / KT / both), PDF / dataslate product names, one-paragraph paraphrase of what changed (no rules dump).
3. Fill **Locked dates** table in `track_in.md` (40K package stamps + KT **Core + team** package stamp — KT has **no** singular dataslate date).
4. Inventory expected local paths under `C:\Personal\40K\rules\` and `C:\Personal\Kill Team\kill_team_2024\` (exist / missing).
5. Draft **impact matrix**: factions, teams, and shipping paths likely affected (Necrons, Space Marines, Canoptek Circle, Plague Marines, Angels of Death, QRs, lists, MFM points callouts).
6. Write `S0_implementer.md` with verbatim fetch commands / failure notes.

## Exit criteria (QA verifies)

- [ ] All three links resolved **or** Blocked with owner paste waiver
- [ ] Dataslate dates locked in `track_in.md`
- [ ] Impact matrix lists concrete paths under `games/`
- [ ] No GW binaries in git; no `raw/` binary writes
- [ ] Teaching paraphrase only in notes
- [ ] Subagent did not git commit/push

## Constraints

If egress fails, do **not** invent article contents. Stop at Blocked + ask owner to paste titles/dates/PDF names.
