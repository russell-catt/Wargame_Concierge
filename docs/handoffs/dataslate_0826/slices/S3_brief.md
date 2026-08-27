# S3 — Brief (Kill Team 2024 shipping impact)

- **Track:** `dataslate_0826`
- **Slice:** S3
- **Status:** Ready — package sources in staging (update logs + team packs); **not** blocked on a singular dataslate PDF
- **Depends:** QA-S1 PASS (may run parallel with S2*); KT package readable in staging
- **Recommended models:** Implementer `claude-sonnet-5-thinking-high` · QA `gpt-5.6-sol-high`

## Inherited documentation

- S0 impact matrix (KT rows) — fill after extract
- [`../research/gdrive_40k_dataslates.md`](../research/gdrive_40k_dataslates.md) — Drive folder
- [`../research/warcom_kt_balance_commentary_aug.md`](../research/warcom_kt_balance_commentary_aug.md) — quarterly top five
- [`../research/staging_kt_august_updates.md`](../research/staging_kt_august_updates.md) — Tomb World / Mission packs logs
- `games/kill_team_2024/**` — rules, teams (Canoptek Circle, Plague Marines, Angels of Death priority), print, Event_Ready
- KT24 quote hierarchy (Full-Scan baseline; dated `eng_*` supersede)

## Requirements

1. Extract / use **KT package** as **Core rules update combined with team updates** (owner lock: **no singular dataslate PDF** — do not hunt for or block on one).
2. **In scope:** priority teams (Canoptek, Plague Marines, Angels of Death) currency vs staged online rules; Tomb World teleport/breach; Nemesis Towering; **Hierotek regen timing** (commentary + online pack) if teaching mentions Hierotek/Apprentek.
3. **Waiver unless owner expands:** Fellgor, Goremongers, Raveners, Wolf Scouts — keep in research note only.
4. Stamp KT **Rules currency: Kill Team quarterly balance — August 2026 (Core / update logs + team online rules)** on touched GW notices/footers.
5. Write `S3_implementer.md` with file list + no-op waivers.
6. Do not expand into parked `kt24_doc_followups` unless package forces a touch.
7. **Never commit permanent PDF copies** outside staging; CLEANUP before main.

## Exit criteria (QA verifies)

- [ ] KT package stamp locked (not a singular dataslate date); currency stamps match
- [ ] Quote hierarchy respected; superseded quotes flagged or updated
- [ ] Regression bar for cheat sheets / Event_Ready
- [ ] Legibility spot-check ≥3 changed pages
- [ ] No binaries; subagent did not git

## Constraints

Read PDFs in place / agent temp only. Personal use / never for sale language stays.
