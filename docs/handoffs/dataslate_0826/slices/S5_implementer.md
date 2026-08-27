# S5 Implementer — dataslate_0826

**Slice:** S5 — game cores + footer stamp sweep
**Status:** Complete
**Date:** 2026-08-27
**Model:** `claude-sonnet-5-thinking-high` (per track model matrix)
**Authorization:** Owner 2026-08-27 — AUTHORIZED, draft confidence accepted. No `git add` / `git commit` / `git push` run by this subagent. **Never introduced banned GW proper nouns under `games/the_warcode/**`** — see the correction note below; the subtree was re-swept afterward and is confirmed clean.

## Summary

Ran the S5 editing pass on each game's core files (40K 11e, KT24, Warcode) per `track_in.md`'s inventory, then swept remaining high-traffic footers (QRs, Event_Ready, priority-team print HTML) that S2/S3 had not reached. All three game-system READMEs now carry a current "Rules currency" stamp. The 40K army READMEs (Necrons, Space Marines) were found **already current** — a concurrent slice (`dataslate_0826` S2) landed Faction Pack v1.2 stamps on both while this slice was running; both were read in full and verified, not re-edited, to avoid duplicate/conflicting Change Log entries.

**Self-caught error:** the first draft of the Warcode README's currency line used the words "40K" and "Kill Team" to describe the balance packages this system is unaffected by — both are on the AGENTS.md Sec 10 / `warcode-quotes.mdc` banned-proper-noun list for `games/the_warcode/**`. Caught immediately, corrected to remove both banned terms before finishing this slice, and the entire `games/the_warcode/` subtree was re-grepped for `kill team|warhammer|40,000|40k` (case-insensitive) afterward — zero hits outside the allowed obfuscation table itself. No banned term was left in any committed-to-disk state.

## Sweep coverage table

### 40K 11e

| Path | Disposition | What changed |
|------|-------------|---------------|
| `games/warhammer_40k_11e/README.md` | **Touched** | New "Rules currency: 40K Aug 2026 package" paragraph — Universal Rules v1.1 · Faction Pack v1.2 · MFM v1.3, `draft`, no singular dataslate file, pointer to both army READMEs (which also carries the Codex October preview note). v0.5.4 → v0.6.0. |
| `games/warhammer_40k_11e/rules/README.md` | **Touched** | Added a "Rules currency" pointer line naming this folder's piece of the package (Universal Rules v1.1, already stamped by S2e) and linking out to the system/army READMEs for the other two pieces. No rewrite of S2e's existing v1.1 content. v0.6.0 → v0.6.1. |
| `games/warhammer_40k_11e/setup/README.md` | **Touched** | Added a "Rules currency" line confirming (by grep, consistent with S2e's earlier check) that no Aug 2026 package piece touches board/deployment/terrain content here; pointer to the system README for the full stamp. v0.5.4 → v0.5.5. |
| `games/warhammer_40k_11e/armies/necrons/README.md` | **Verified, not re-edited** | Already at v0.5.6 with both `Rules currency: Munitorum Field Manual Necrons v1.3` and `Faction Pack v1.2` stamped by concurrent slice S2 (Change Log entries v0.5.5–v0.5.6). Header VERSION and top Change Log entry match. No discrepancy found. |
| `games/warhammer_40k_11e/armies/space_marines/README.md` | **Verified, not re-edited** | Already at v1.12 with MFM v1.3, Faction Pack v1.2, and the SM Codex October preview note all stamped by concurrent slices S2/S2b/S2d. Header VERSION and top Change Log entry match. No discrepancy found. |

### Kill Team 2024

| Path | Disposition | What changed |
|------|-------------|---------------|
| `games/kill_team_2024/README.md` | **Touched** | New "Rules currency: Kill Team quarterly balance — August 2026" line (Core/update logs + priority team online rules), `draft`, pointer to `S3_implementer.md` for team-by-team disposition; Death Korps/Kommandos no-op noted. v0.7 → v0.8. |
| `games/kill_team_2024/Event_Ready.md` | **Touched** | New currency line under Status, plus a re-print cue if the Plague Marines cheat sheets in the go-bag pre-date 2026-08-27. v1.1 → v1.2. Named explicitly in the brief as a high-traffic surface. |
| `games/kill_team_2024/rules/README.md` | **Touched** | New currency line clarifying that this shared teaching spine was not rewritten this pass — the package's actual teaching deltas (Tomb World teleport/Breach, Nemesis Towering Size) landed on `setup/killzones/tomb_world.md` and `nemesis_ops/` per S3, not here. Pointer to `S3_implementer.md`. v0.5.0 → v0.5.1. |
| `games/kill_team_2024/setup/killzones/volkus_QR.md` | **Touched (sweep)** | Added a compact currency line matching this file's existing minimalist "verify vs..." footer style; explicitly notes no Volkus-specific change was found in the staged Aug 2026 pack (Volkus was not one of S3's touched killzones — only Tomb World was). v1.1 → v1.2. |
| `games/kill_team_2024/setup/killzones/starter_set_3e_QR.md` | **Touched (sweep)** | Added a currency line under the existing GW notice (this file had no currency stamp of any kind before). v0.5.0 → v0.5.1. |
| `games/kill_team_2024/print/kt_pm_quick_reference.html` | **Touched (sweep)** | One-line currency footnote added before the page-2 UNOFFICIAL footer. Plague Marines is a **priority** team (fully updated by S3 on its markdown pages); this print pack had not been swept. UNOFFICIAL banner/footer verified intact, unchanged. |
| `games/kill_team_2024/print/kt_pm_faction_rules.html` | **Touched (sweep)** | Same currency footnote, before the page-2 footer. Banner/footer intact. |
| `games/kill_team_2024/print/kt_pm_starter_roster.html` | **Touched (sweep)** | Same currency footnote, before the single-page footer. Banner/footer intact. |
| `games/kill_team_2024/print/kt_pm_volkus_playbook.html` | **Touched (sweep)** | Same currency footnote, before the page-2 footer. Banner/footer intact. |
| `games/kill_team_2024/print/kt_kommandos_*.html` (4 files) | **Waived (explicit)** | Kommandos was an explicit **no-op** in S3 per the owner lock ("no update this package"). Adding a currency stamp to files whose content did not change would be misleading — consistent with S3's own reasoning for not touching the Kommandos markdown pages. Not touched. |
| `games/kill_team_2024/teams/*/README.md` (Angels of Death, Canoptek Circle, Plague Marines, Hierotek Circle, Celestian Insidiants, Deathwatch, Murderwing, Vespid Stingwings) | **Verified, not re-touched** | All 8 already carry the S3 currency stamp. Death Korps and Kommandos remain the explicit no-op pair. No action needed — already satisfies "≥5 KT pages show currency date" several times over. |

### The Warcode

| Path | Disposition | What changed |
|------|-------------|---------------|
| `games/the_warcode/README.md` | **Touched** | Added the locked stamp verbatim: **"Last reviewed: 2026-08-27 · not affected by Games Workshop balance packages."** Self-corrected one draft sentence that had used two banned proper nouns before finishing (see Summary); final text uses no GW comparator proper noun. v0.3 → v0.4. |
| Rest of `games/the_warcode/**` | **Not touched, swept for compliance** | This system is explicitly unaffected by the Aug 2026 GW balance packages (RedMakers free beta, not a GW product) — the brief's N/A-stamp instruction applies only to the README. Ran a full-subtree grep for `kill team\|warhammer\|40,000\|40k` (case-insensitive) after finishing; zero hits outside the allowed obfuscation table in `.cursor/rules/warcode-quotes.mdc` (which is not under `games/`). |

## Print HTML UNOFFICIAL / footer spot-check (brief requirement 4)

Checked, no regressions:

| File | UNOFFICIAL banner | UNOFFICIAL footer | Currency line |
|------|--------------------|---------------------|----------------|
| `games/warhammer_40k_11e/setup/print/40k_system_quick_reference.html` | Present (unchanged) | Present, both pages (unchanged) | N/A — no package piece touches this page (verified 2026-08-27) |
| `games/warhammer_40k_11e/armies/necrons/print/40k_necrons_quick_reference.html` | Present (unchanged) | Present, both pages (unchanged) | Present — MFM v1.3 mini footnote, added by S2c, verified intact |
| `games/kill_team_2024/print/kt_pm_quick_reference.html` (+ 3 sibling PM print files) | N/A (compact single-banner style; footer only) | Present, all pages (unchanged) | **Added this slice** |
| `games/kill_team_2024/print/kt_kommandos_*.html` | N/A | Present (unchanged, not touched) | Intentionally absent — Kommandos no-op |

No print HTML lost its UNOFFICIAL banner or non-endorsement footer as a side effect of any edit in this slice.

## Exit criteria self-check

- [x] All three game READMEs current (40K, KT24, Warcode all carry a 2026-08-27 stamp)
- [x] Footer sample audit: **≥5 40K pages** carry a currency date (README + rules/README + setup/README this slice, plus ~20 army pages from S2/S2b/S2c/S2d already in place) and **≥5 KT pages** carry a currency date (README + rules/README + Event_Ready + 2 killzone QRs + 4 PM print files this slice, plus 8 team READMEs from S3 already in place) — well over the ≥5/≥5 bar, with justified skips (Kommandos no-op, low-traffic `units/research/`)
- [x] Warcode ban intact — self-caught and corrected during this slice; full-subtree grep confirms zero banned terms remain
- [x] Print UNOFFICIAL requirements not regressed (spot-check table above)
- [x] Legibility spot-check: `games/kill_team_2024/README.md` and one QR (`starter_set_3e_QR.md`) per system read back after editing — both remain scannable, one short additive line each, no wall-of-text
- [x] Subagent did not `git add` / `git commit` / `git push`

## Skip list (low-traffic, not swept)

- `games/warhammer_40k_11e/armies/necrons/units/research/*.md` and `games/warhammer_40k_11e/armies/space_marines/units/research/*.md` — per-unit research stubs, not player-facing shipping pages; S2c/S2d already touched the specific unit files with an actual MFM v1.3 point delta (Necron Warriors, Plasmancer, Centurion Devastator Squad, Land Raider Redeemer, Librarian). The remaining ~90+ stub files carry no version-numbered points citation to bump and are explicitly out of scope per S2c/S2d's own "no full MFM dump" boundary — this slice did not add a blanket currency stamp to them, consistent with that precedent.
- `games/kill_team_2024/print/kt_kommandos_*.html` (4 files) — explicit no-op, see table above.
- `games/warhammer_40k_11e/armies/necrons/print/40k_setup_terrain.html`, `40k_first_game_core.html`, `40k_conclave_primary_missions.html` — S2c already grepped these for point figures and found none; re-verified, still no Warriors/Plasmancer figures present, so no currency stamp is warranted.

## Copyright / scope compliance

- No verbatim rules text was added by this slice — every edit is a short currency-pointer sentence or a compact footnote citing the package name, version/date, and `draft` status.
- `games/the_warcode/**`: naming-ban violation caught and corrected before this slice finished; subtree re-swept and confirmed clean (see Summary).
- No `raw/` binaries were added, moved, or committed.
- Every touched print HTML file's existing `.gw-ip-banner` / `.gw-ip-footer` content was left byte-for-byte unchanged; only an additional line was inserted.

## Files touched

**40K 11e:**
- `games/warhammer_40k_11e/README.md`
- `games/warhammer_40k_11e/rules/README.md`
- `games/warhammer_40k_11e/setup/README.md`

**Kill Team 2024:**
- `games/kill_team_2024/README.md`
- `games/kill_team_2024/Event_Ready.md`
- `games/kill_team_2024/rules/README.md`
- `games/kill_team_2024/setup/killzones/volkus_QR.md`
- `games/kill_team_2024/setup/killzones/starter_set_3e_QR.md`
- `games/kill_team_2024/print/kt_pm_quick_reference.html`
- `games/kill_team_2024/print/kt_pm_faction_rules.html`
- `games/kill_team_2024/print/kt_pm_starter_roster.html`
- `games/kill_team_2024/print/kt_pm_volkus_playbook.html`

**The Warcode:**
- `games/the_warcode/README.md`

**New file:**
- `docs/handoffs/dataslate_0826/slices/S5_implementer.md` (this report)

## Verified, not touched (see tables above for reasons)

- `games/warhammer_40k_11e/armies/necrons/README.md`
- `games/warhammer_40k_11e/armies/space_marines/README.md`
- `games/kill_team_2024/teams/{angels_of_death,canoptek_circle,plague_marines,hierotek_circle,celestian_insidiants,deathwatch,murderwing,vespid_stingwings}/README.md`
- `games/kill_team_2024/print/kt_kommandos_*.html`
- 40K `units/research/*.md` low-traffic stubs

## Waivers / open items for QA

1. **Self-caught Warcode naming violation** — flagging explicitly even though corrected, per the QA skill's Warcode checklist. Please re-verify with a fresh grep independent of this report's claim.
2. **Concurrent slice activity** — as in `S4_implementer.md`, this slice observed another agent instance actively editing `games/warhammer_40k_11e/armies/**` and `KB/**` files mid-session. Every file this slice touched was re-read immediately before editing; the two army READMEs this slice needed were already correct by the time they were checked, so no edit was made to them (see "Verified, not re-edited" rows above). QA should confirm the Necrons/SM README states are acceptable as landed by S2/S2b/S2c/S2d rather than expecting a diff from S5 on those two files.
3. **Volkus QR currency line states "no Volkus-specific change found"** — this is this slice's own grep/read against the S3 report's scope (S3 only touched Tomb World among killzones); if a later slice finds a Volkus-specific Aug 2026 delta, that line should be corrected rather than silently left.
4. No PDF was read or committed. No `git add` / `git commit` / `git push` was run by this subagent.

## Not touched (S5 non-goals)

- `KB/**` — Librarian-owned.
- Any new balance-figure recost — this slice is currency stamping and footer freshness only, not a new points/rules pass (that is S2c/S2d/S3's remit, already complete).
- Any `raw/` write.
