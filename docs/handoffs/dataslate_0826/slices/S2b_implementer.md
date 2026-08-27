# S2b Implementer — dataslate_0826

**Slice:** S2b — SM Codex October readiness (preview banners, Legendary Proxies / Legends honesty)
**Status:** Complete
**Date:** 2026-08-27
**Model:** `claude-sonnet-5-thinking-high` (per track model matrix)
**Authorization:** Owner 2026-08-27 — full track authorized, draft accepted; **no** early T5/S5 list rewrite; no git commit/push by this subagent.

## Summary

Added preview-only Codex: Space Marines (October, WarCom) callouts across the Blood Ravens Space Marines shipping surface: a central "SM Codex October readiness" section on `README.md` with the full **Legendary Proxies** mapping table and the **future Legends** vehicle list; an owner-paste note on `Owned_Models_Inventory.md`'s existing "is it Legends?" table; inline callout blockquotes on all four Matched starters (`Starter_{250,500,750,1000}_Matched.md`) and three of four Casual starters (`Starter_{500,750,1000}_Casual.md`, wherever Tactical / Devastator / Whirlwind actually appear); an additive one-line preview note on `Starter_250_Casual.md` (no Tac/Dev/Whirlwind on that list, so no inline callout needed); a single added line on the two-page `Quick_Reference_Play_Guide.md` laminate (page count unchanged); and a light-touch "SM Codex October preview" section on the three unit research stubs the brief names by path (`units/research/Tactical-Squad.md`, `Devastator-Squad.md`, `Whirlwind.md`). Every touched player-facing markdown page's `## Games Workshop notice` section also received the S1-locked additive **Preview note** footer line verbatim from `templates/Footer_Template_Gw_Print.md` / `track_in.md`. **No** Matched-play point totals, unit datasheets, or stat lines were changed — Tactical Squad and Devastator Squad keep their own MFM points and their own datasheet on every list; the Whirlwind keeps fielding as matched-legal on `Starter_1000_Matched.md`. This slice ran concurrently with **S2d** (SM MFM v1.3 stamp) on the same files; every edit was re-read immediately before writing to avoid clobbering S2d's concurrent `MFM v1.3` / `Rules currency` edits, and the two slices' additions now coexist cleanly in each file.

## Done (mapped to brief requirements)

1. **Legendary Proxies / Legends honesty callouts** where Tactical Squad, Devastator Squad, and Whirlwind appear:
   - Inline `>` blockquote on `Starter_250_Matched.md` (BR-2's Tactical Squad only), `Starter_500_Matched.md`, `Starter_750_Matched.md`, `Starter_1000_Matched.md` (adds the Whirlwind clause), `Starter_500_Casual.md`, `Starter_750_Casual.md`, `Starter_1000_Casual.md` (adds the Whirlwind clause for its variant table). `Starter_250_Casual.md` has no Tac/Dev/Whirlwind (Captain + bikes only) so it got the footer line only, with a Change Log note explaining why no inline callout was added.
   - Each callout states plainly: the unit stays **current Faction Pack / MFM**, matched-legal, its own points, **until** the Codex actually ships; only then does it become a Legendary Proxy (Tac→Intercessor, Dev→Desolation) or move to Legends (Whirlwind); competitive play needs event-organiser permission.
   - Central mapping lives on `README.md` under a new **"SM Codex October readiness (preview — do not play yet)"** section (Legendary Proxies table including the two owned rows plus the three unowned named ones from the research note — Suppressor→Inceptor, Pedro Kantor→Captain, Uriel Ventris→Captain — and the future-Legends vehicle list with owned units bolded).
   - `Owned_Models_Inventory.md` — added an owner-paste note directly under the existing "Step 2 - is it Legends?" table (the single authoritative "still matched-legal?" reference for this collection), flagging which rows change and when, without altering any row in that table.
   - Light-touch unit research headers on `Tactical-Squad.md` (→ Intercessor Squad Legendary Proxy), `Devastator-Squad.md` (→ Desolation Squad Legendary Proxy), `Whirlwind.md` (→ future Legends) — the three units the brief names directly. Centurions / Razorback / Predator D+A / Vindicator / Dreadnought / Stormhawk / Stormtalon / Stormraven / Hammerfall Bunker are covered via the README future-Legends list + the Owned_Models_Inventory note (the brief's "README **or** research unit headers" option) rather than editing all 12 additional unowned/roster-only research stubs — kept to the brief's "light touch" instruction.
2. **Preview note footer line, per `track_in.md` (additive):** added the exact locked line to the `## Games Workshop notice` section of every touched player-facing markdown page:
   > `Preview note: Codex: Space Marines expected October (WarCom) · live lists still current Faction Pack / MFM until Codex — Legendary Proxies / Legends honesty on Firstborn paths.`
   This is the same line S1 already staged into `templates/Footer_Template_Gw_Print.md` §E and `docs/handoffs/dataslate_0826/track_in.md` — reused verbatim rather than inventing a second footer format, keeping one locked convention across the track.
3. **No early T5/S5 rewrite:** confirmed via grep across every touched file — `T5` / `S5` / "strength 5" / "toughness 5" appear **only** inside the README's clearly-labelled preview callout (explicitly framed as "nobody plays the October preview stats... at the table yet"), never on a live Matched/Casual points table or a unit research stat block. No Matched total, unit cost, or datasheet text was changed.
4. Wrote this `S2b_implementer.md`.

## Files changed

**Central hub / inventory (2):**
- `games/warhammer_40k_11e/armies/space_marines/README.md` — new "SM Codex October readiness" section (Legendary Proxies mapping table + future Legends vehicle list + event-permission note + preview footer line); SOURCES + Change Log updated (v1.10).
- `games/warhammer_40k_11e/armies/space_marines/Owned_Models_Inventory.md` — owner-paste note under the "is it Legends?" table; preview footer line in GW notice; SOURCES + version/Change Log updated (v1.9).

**Matched starters (4):**
- `Starter_250_Matched.md`, `Starter_500_Matched.md`, `Starter_750_Matched.md`, `Starter_1000_Matched.md` — inline SM Codex October preview blockquote + preview footer line + Change Log entry on each (v0.7.2 on all four; 1000 variant also flags the Whirlwind).

**Casual starters (4):**
- `Starter_250_Casual.md` — preview footer line only (no Tac/Dev/Whirlwind present); v1.2.
- `Starter_500_Casual.md`, `Starter_750_Casual.md` — inline callout + preview footer line; v1.2 each.
- `Starter_1000_Casual.md` — inline callout (Tac/Dev/Whirlwind, the Whirlwind variant table) + preview footer line; v1.2.

**Play aid (1):**
- `Quick_Reference_Play_Guide.md` — one added line under the Starter Snapshot table (no new section, 2-page constraint preserved); header Change Log entry (v0.7.1).

**Unit research (3):**
- `units/research/Tactical-Squad.md`, `Devastator-Squad.md`, `Whirlwind.md` — new "SM Codex October preview" section each, light touch, `draft` confidence, cites the research note.

**New file:**
- `docs/handoffs/dataslate_0826/slices/S2b_implementer.md` (this report)

**14 files touched under `games/warhammer_40k_11e/armies/space_marines/` + 1 new handoff file.**

## Not touched (explicitly out of scope for S2b)

- **Matched-play point totals / unit costs** — untouched. Tactical Squad, Devastator Squad, and Whirlwind keep their own MFM points on every list (concurrent slice S2d separately re-stamped these to MFM v1.3 with **unchanged** figures — verified compatible, not re-edited by this slice beyond adding the preview callout alongside).
- **Any datasheet swap** — no list was rewritten to field Intercessor/Desolation Squad points in place of Tactical/Devastator, and no list dropped the Whirlwind early. That swap is explicitly a **non-goal** per the brief and is called out as future follow-up work in every inline callout ("No stat/points swap on this page yet").
- **`KB/glossary.md` Legendary Proxies vs Legends stub** — brief requirement 4 is Librarian-owned (L1 slice per `track_in.md`'s dependency graph). Not touched by this Implementer slice; flagged below for the Librarian.
- **Centurion / Razorback / Predator D+A / Vindicator / Dreadnought / Stormhawk / Stormtalon / Stormraven / Hammerfall Bunker `units/research/*.md` stub files** — covered via the README future-Legends list + `Owned_Models_Inventory.md` note instead of touching all 12 files individually, per the brief's "README **or** research unit headers (light touch)" framing. QA should confirm this reading is acceptable; if not, these stubs are quick one-line additions in the same shape as the three that were touched.
- **Suppressor Squad / Pedro Kantor / Uriel Ventris research pages** — do not exist in this repo (not owned, not in `Unit_Index.md`); documented as "Not owned" in the README mapping table instead of creating new stub files for unowned named characters.
- **Starter_{250,500,750,1000}.md shims** — pure Matched/Casual redirect pages with no Tac/Dev/Whirlwind content; left untouched.
- `KB/` — Librarian-owned; not touched by Implementer.
- No PDF was read or committed. No `git add` / `git commit` / `git push` was run by this subagent.

## Concurrency note (S2d ran in parallel on the same files)

Slice **S2d** (SM MFM v1.3 stamp + Casual Legends cross-check) was actively editing the same eight Matched/Casual starter files while this slice ran. Every file was **re-read immediately before each edit** rather than relying on the initial read, so this slice's callouts and footer lines were inserted against S2d's latest content rather than overwriting it. Confirmed after the fact: every touched file still carries exactly one `## Games Workshop notice` section and one `## Change Log` section (no duplicates), S2d's `MFM v1.3` / `Rules currency` lines are intact, and this slice's `Preview note` line sits immediately after them, additive as required.

## Waivers / open items for QA

1. **Glossary stub (Legendary Proxies vs Legends)** is deferred to Librarian L1 per the track dependency graph — not a gap in this slice, just handed off as designed.
2. **12 non-owned/roster-only vehicle research stubs** (Centurions, Razorback, Predator D+A, Vindicator, Dreadnought, Stormhawk, Stormtalon, Stormraven, Hammerfall Bunker) were **not** individually edited — covered at the README/inventory level instead. QA should confirm this satisfies "light touch" or ask for the same one-section pattern added to each stub.
3. `Starter_250_Casual.md` got the footer line but no inline callout, since neither Tactical Squad, Devastator Squad, nor Whirlwind appear on that list (Captain + Bike Squad + Attack Bike only). Documented in-file via Change Log.
4. All research note content stays `draft` (owner paste 2026-08-27, no canonical WarCom URL yet per open questions in `track_in.md` / `sm_codex_oct_preview.md`) — every new callout and section cites that `draft` status explicitly.
5. No git commit/push performed by this subagent, per instructions.
