# S3 Implementer — dataslate_0826

**Slice:** S3 — Kill Team 2024 shipping impact
**Status:** Complete
**Date:** 2026-08-27
**Model:** `claude-sonnet-5-thinking-high` (per track model matrix)
**Authorization:** Owner 2026-08-27 — full track authorized, draft confidence accepted. Owner lock: no singular KT dataslate; package = Core update logs + team online rules. No PDF committed outside staging; no `git add`/`commit`/`push` run by this subagent.

## Summary

Read the KT package as **Core / killzone / mission-pack update logs combined with dated team online rules** (owner lock — no singular "balance dataslate" PDF exists or was hunted for). Extracted text from every staged PDF with `pypdf` (read in place under `raw/_dataslate_0826_staging/`, never copied into the repo). Applied the five known teaching deltas from research (Tomb World teleport/breach, Nemesis Towering Size, Hierotek regen-timing loophole, priority-team currency + verified deltas, stub-team currency notes), stamped **Rules currency: Kill Team quarterly balance — August 2026** on every touched page, and left Death Korps / Kommandos as an explicit no-op per the owner lock.

## Teams updated vs waived

| Team | Disposition | What changed |
|------|-------------|---------------|
| **Angels of Death** | **Updated** (priority full guide) | Chapter Tactics cross-checked against staged `eng_26-08_` pack; Hardy footnote (Aug '26 errata reverts the retaliation-softening bullet back in — table row already matched, now verified not assumed); Update log section; currency stamp; README stamp |
| **Canoptek Circle** | **Updated** (priority full guide) | Tomb Crawler Dimensional Banishment now has no effect on NEMESIS/Red Terror; Geomancer Obelisk Node Control mission-action exclusion widened (Pick Up Marker + Retrieve); Reanimation-token-vs-Hierotek commentary; Obelisk Node Matrix quote re-verified unchanged; currency stamp; README stamp |
| **Plague Marines** | **Updated** (priority full guide) | *Toxic weapon rule timing clarified (Poison token checked at start of action); teleport/Lumbering Death cross-reference to the Tomb World killzone page; Astartes + Poison quote blocks re-verified against Aug '26 pack — text unchanged; currency stamp; README stamp |
| **Hierotek Circle** | **Updated** (stub — regen-timing note) | Regeneration loophole note: Living Metal now explicitly resolves *before* Reanimation Protocols in the Ready step, so revive-related regen only kicks in the turn *after* an operative is brought back; currency stamp. No full Team_Rule_Guide.md exists yet — note added to `README.md` |
| **Celestian Insidiants** | **Updated** (stub — currency + note) | Currency stamp + short Aug 2026 package note (Weapons of the Witch Hunter PSYCHIC-denial commentary tightened) |
| **Deathwatch** | **Updated** (stub — currency + note) | Currency stamp + short Aug 2026 package note (Mission Tactics / Suffer Not the Alien wording clean-up — no practical change) |
| **Murderwing** | **Updated** (stub — currency + note) | Currency stamp + short Aug 2026 package note (Jump Pack Boost capped at 6"; Malicious Narcissism / Curseclaw rules commentary) |
| **Vespid Stingwings** | **Updated** (stub — currency + note) | Currency stamp + short Aug 2026 package note (Aerial Agility tightened; Communion Helm reworded) + teleport/Neutron Charge cross-reference to Tomb World page |
| **Death Korps** | **No-op (waived)** | Owner lock: no update this package. Not touched. |
| **Kommandos** | **No-op (waived)** | Owner lock: no update this package. Not touched. |
| Fellgor Ravagers, Goremongers, Raveners, Wolf Scouts | **Waived (out of scope)** | Not owned / not in this shipping scope, per owner lock item 6. WarCom top-five commentary for these teams already lives in [`../research/warcom_kt_balance_commentary_aug.md`](../research/warcom_kt_balance_commentary_aug.md) — no further action taken. Noted here only, not touched in `games/`. |

Non-team surfaces:

| Surface | Disposition | What changed |
|---------|-------------|---------------|
| **Killzone: Tomb World** | **Updated** | Teleport does not bypass "cannot end move closer" restrictions; teleport pad 2" equipment-terrain exclusion + control-range note + one-teleport-per-activation; Breach action tightened to a 2AP floor when combined with Charge/Shoot; older "teleport isn't moved" commentary cross-referenced to Plague Marines (Lumbering Death) and Vespid Stingwings (Neutron Charge); currency stamp |
| **Nemesis Ops (Custom Builder / How-To)** | **Updated** | Towering Size commentary: custom Nemesis should almost always keep Towering Size (Ambull/Archivist are the named ready-made exceptions, not a general licence); even Small custom Nemesis should keep the no-Conceal / always-valid-target behaviour; currency stamp |
| **Mission packs update log** (Tomb World Nov '25 grey drop zone, Typhon Aug '25 terrain swap) | **Read, not re-taught** | Both are `PREVIOUS ERRATA`, already superseded/historical by the time of this pass; no owned page currently states the stale version, so no correction needed. Flagged here for QA visibility. |

## Files changed

**Setup / killzones:**
- `games/kill_team_2024/setup/killzones/tomb_world.md`

**Nemesis Ops:**
- `games/kill_team_2024/nemesis_ops/Custom_Builder.md`
- `games/kill_team_2024/nemesis_ops/How_To_Create_A_Nemesis_Operative.md`

**Angels of Death:**
- `games/kill_team_2024/teams/angels_of_death/README.md`
- `games/kill_team_2024/teams/angels_of_death/Team_Rule_Guide.md`

**Canoptek Circle:**
- `games/kill_team_2024/teams/canoptek_circle/README.md`
- `games/kill_team_2024/teams/canoptek_circle/Team_Rule_Guide.md`

**Plague Marines:**
- `games/kill_team_2024/teams/plague_marines/README.md`
- `games/kill_team_2024/teams/plague_marines/Team_Rule_Guide.md`

**Hierotek Circle:**
- `games/kill_team_2024/teams/hierotek_circle/README.md`

**Stub teams (currency + short note only):**
- `games/kill_team_2024/teams/celestian_insidiants/README.md`
- `games/kill_team_2024/teams/deathwatch/README.md`
- `games/kill_team_2024/teams/murderwing/README.md`
- `games/kill_team_2024/teams/vespid_stingwings/README.md`

**New file:**
- `docs/handoffs/dataslate_0826/slices/S3_implementer.md` (this report)

## No-op waivers (explicit)

1. **Death Korps** — owner lock: no staged package update this pass. Not touched (no `README.md`/inventory edit, no currency stamp — owner lock says currency stamp is optional-only if a shared core is touched; Death Korps teaching does not reference any of the touched cores, so it was left as-is).
2. **Kommandos** — same as above. Not touched, including print HTML under `games/kill_team_2024/print/kt_kommandos_*.html` (no shared-core content in those files needed a stamp).
3. **Fellgor Ravagers, Goremongers, Raveners, Wolf Scouts** — not owned / not in this shipping scope (owner lock item 6). WarCom top-five commentary already captured in the research note; no `games/` teaching exists for these teams and none was created.

## Verified, not changed

- **Plague Marines Astartes + Poison quote blocks** (`Team_Rule_Guide.md`) — re-verified verbatim against the staged Aug '26 online rules pack (`eng_plague_marines_online_rules-*.pdf` p.3 live body); text is byte-for-byte the same as what's already quoted. No edit needed, noted in Change Log as a positive verification.
- **Canoptek Circle Obelisk Node Matrix quote block** — re-verified against the staged pack's "previous erratas" section; the quote already includes the "each turning point after the first" wording. No edit needed.
- **Angels of Death Hardy Chapter Tactic** — the existing teaching table row already described *both* effects (defence-dice-crit-on-shot and retaliation-damage-softening). The staged pack's live body only shows the first bullet, and the August '26 errata explicitly "reverts a previous change" to restore the second — meaning the existing row was already correct for the post-August state. Cross-checked and footnoted rather than left as an unverified assumption.
- **Kill Team-wide "previous errata"** items in the Tomb World and Mission Packs update logs (Nov '25 / Aug '25 dated) — read for context; nothing in the owned KB currently states the stale pre-errata version, so no correction was required.
- **Angels of Death team-selection wording** (Eliminator Sniper / Heavy Intercessor Gunner exclusivity, removed in a prior errata) — grepped across the Angels of Death folder; no page states the stale restriction, so nothing to fix.

## Copyright / quote-hierarchy compliance

- All teaching deltas above are **paraphrase**. No verbatim block longer than a short rules-commentary quote was copied from any staged PDF into `games/`, and every paraphrase cites the staging filename + page (e.g. `eng_hierotek_circle_online_rules-df98wqycag-bek3q27dqk.pdf` errata p.11) per the KT24 quote hierarchy.
- No staged PDF was copied into the repository at any path. All extraction was done in-place from `raw/_dataslate_0826_staging/` via a temporary `pypdf` script; no PDF or PDF-derived binary was written under `raw/` or committed.
- Every touched `README.md` / `Team_Rule_Guide.md` retains its existing `## Games Workshop notice` section unchanged; the currency stamp was added as an **additive** line, not a replacement of the GW notice.
- Currency stamp used verbatim everywhere it was applied: **"Rules currency: Kill Team quarterly balance — August 2026 (Core / update logs + team online rules) · teaching paraphrase · verify owned PDFs · confidence draft."**

## Waivers / open items for QA

1. **Package is Core update logs + team online rules, not a singular dataslate** — confirmed against the owner lock; every currency stamp cites this framing rather than a single filename/date.
2. **Angels of Death Team_Rule_Guide.md remains partially `draft`** — only the Chapter Tactics section was cross-checked against the staged pack this pass; Strategy/Firefight ploys and Faction Equipment are still sourced from the living Wahapedia page (retrieved 2026-08-17), not the owned/staged PDF. Flagged in `REFERENCE_STATUS`.
3. **Hierotek Circle, Celestian Insidiants, Deathwatch, Murderwing, Vespid Stingwings remain stub folders** — no full `Team_Rule_Guide.md` exists for any of them. The Aug 2026 notes added to their `README.md` files are a holding pattern so the deltas aren't lost before a future full-guide slice; they are not a substitute for a full cross-check.
4. **Event_Ready / AO2025 Tournament Companion pointer** — brief listed this as optional and not required for kitchen-table play; not added this pass (no regression risk either way, since nothing referencing it was touched).
5. No PDF was read outside `raw/_dataslate_0826_staging/`; no PDF was committed. No `git add` / `git commit` / `git push` was run by this subagent — that remains the Coordinator's responsibility per track lock.

## Not touched (S3 scope)

- `KB/` — Librarian-owned; not touched by Implementer.
- Death Korps, Kommandos (explicit no-op, see above).
- Fellgor Ravagers, Goremongers, Raveners, Wolf Scouts (waived, not owned/out of scope).
- 40K Necron / Space Marine faction packs and points manuals — separate slices (S1/S2*).
- `games/kill_team_2024/print/**` HTML cheat sheets — grepped for regression risk (Poison/Toxic/Hardy wording); no contradictions found, so none were edited to keep the regression bar clean for QA's legibility spot-check.
