# S3 — Brief (Kill Team 2024 shipping impact)

- **Track:** `dataslate_0826`
- **Slice:** S3
- **Status:** Ready — **blocked on KT dataslate source** (Drive unread; awaiting upload or egress)
- **Depends:** QA-S1 PASS (may run parallel with S2*); KT dataslate PDF readable (Drive or chat upload)
- **Recommended models:** Implementer `claude-sonnet-5-thinking-high` · QA `gpt-5.6-sol-high`

## Inherited documentation

- S0 impact matrix (KT rows) — fill after extract
- [`../research/gdrive_40k_dataslates.md`](../research/gdrive_40k_dataslates.md) — owner Drive folder (KT dataslate reported added 2026-08-27)
- `games/kill_team_2024/**` — rules, teams (Canoptek Circle, Plague Marines, Angels of Death priority), print, Event_Ready
- KT24 quote hierarchy (Full-Scan baseline; dated `eng_*` supersede)

## Requirements

1. Extract KT Balance Dataslate (paraphrase + scoped quotes under Sec 10 only); lock date in `track_in.md`.
2. Walk impact matrix; update teaching docs / team notes / print aids as needed.
3. If dataslate patches a quoted surface: update quote + cite (filename + page) **or** demote to paraphrase — never leave a superseded verbatim block unmarked.
4. Stamp KT **Rules currency** line with locked KT dataslate date on touched GW notices/footers.
5. Write `S3_implementer.md` with file list + no-op waivers.
6. Do not expand into parked `kt24_doc_followups` unless dataslate forces a touch.
7. **Never commit the PDF.**

## Exit criteria (QA verifies)

- [ ] KT dataslate date locked; currency stamps match
- [ ] Quote hierarchy respected; superseded quotes flagged or updated
- [ ] Regression bar for cheat sheets / Event_Ready
- [ ] Legibility spot-check ≥3 changed pages
- [ ] No binaries; subagent did not git

## Constraints

Read PDFs in place / agent temp only. Personal use / never for sale language stays.
