# S2d Implementer — dataslate_0826

**Slice:** S2d — Space Marines MFM v1.3 stamp + Casual Legends cross-check
**Status:** Complete
**Date:** 2026-08-27
**Model:** `claude-sonnet-5-thinking-high` (per track model matrix)
**Authorization:** Owner 2026-08-27 — full track authorized, draft accepted. No git commit/push by this subagent. No PDF binaries touched. Codex wall respected on `games/warhammer_40k_11e/armies/**`.

## Summary

Re-stamped every Space Marines shipping page that cited **Munitorum Field Manual (Marines) v1.2** to **MFM Marines v1.3** (owner paste, retrieved 2026-08-27, per [`../research/sm_mfm_v1_3.md`](../research/sm_mfm_v1_3.md)), re-verified the Blood Ravens Matched-play core costs arithmetic against the v1.3 paste, and cross-checked the Casual starters' Bike Squad / Attack Bike / Astartes Servitors figures against the MFM v1.3 **Legends** section (previously sourced from the standalone Warhammer Legends Field Manual). **No point values changed on any Blood Ravens Matched or Casual starter** — every BR core cost the research note lists (Captain, Chaplain in Terminator Armour, Techmarine, Tactical Squad, Devastator Squad, Terminator Squad, Terminator Assault Squad, Whirlwind, Honour Vehement, Lieutenant with Combi‑weapon, and the four Casual Legends units) is confirmed unchanged, and every list total was re-added by hand to confirm the arithmetic still holds. The only real point movement in the v1.3 paste — Centurion Devastator Squad (6) → **365** (+15), Land Raider Redeemer → **260/280** (+10/+10), Librarian in Terminator Armour → **85** (+10) — landed on units that are **not owned** and **not in any Blood Ravens Matched/Casual starter**, so it is recorded as a research-only ▲ note on the three matching `units/research/*.md` stub pages plus the Land Raider Redeemer row in `Owned_Models_Inventory.md`'s Step 2 legality table, with **no starter-list edit**. Added the additive `Rules currency: Munitorum Field Manual — Space Marines v1.3 (WarCom/App) …` line (locked convention from `templates/Footer_Template_Gw_Print.md` §E) to the `## Games Workshop notice` section of every touched player-facing markdown page. Did **not** touch anything related to the October Codex Proxy rewrite (that is S2b's lane) — this slice's only interaction with S2b's concurrent work was re-reading each shared file immediately before editing so neither slice clobbered the other; both sets of additions now coexist cleanly (S2d's `MFM v1.3` / `Rules currency` lines, S2b's `Preview note` / inline Codex-October callouts).

## Done (mapped to brief requirements)

1. **Bumped all SM shipping citing MFM Marines v1.2 → v1.3**, with retrieval date and a pointer to the research note, on:
   - All 4 Matched starters (`Starter_{250,500,750,1000}_Matched.md`): header SOURCES + REFERENCE_STATUS, body "Points:" line, every points-table column header (`MFM Marines v1.2` → `v1.3`), Rising Tide footer note.
   - All 4 Casual starters (`Starter_{250,500,750,1000}_Casual.md`): same treatment plus the Legends-source cross-check (item 3 below).
   - `README.md`, `Quick_Reference_Play_Guide.md`, `Owned_Models_Inventory.md`, `Gladius_Task_Force.md` (enhancement cost table), `Anvil_Siege_Force.md`, `First_Company_Task_Force.md` (SOURCES pointer only — these two are `draft` detachment guides whose enhancement figures are public-ref, not MFM-cited).
   - The 4 thin `Starter_{250,500,750,1000}.md` shims got the additive `Rules currency` line only (they carry no points of their own).
   - Confirmed `raw/pointers/points_manuals.md` already carries the v1.3 owner-paste rows from track slice S1 — not re-touched, no duplicate work.
2. **Re-verified Blood Ravens Matched totals — no core cost change**, unit by unit against [`../research/sm_mfm_v1_3.md`](../research/sm_mfm_v1_3.md)'s "Owned Blood Ravens snapshot" table:
   - Captain 80 · Chaplain in Terminator Armour 75 · Techmarine 55 · Tactical Squad 140 · Devastator Squad 120/200 · Terminator Squad 160/320 · Terminator Assault Squad 155 (+5/TH) · Whirlwind 175/195 · Honour Vehement 15 · Lieutenant with Combi-weapon 95 — all **unchanged**.
   - Re-added every starter total by hand: 250 BR‑1 **235**, BR‑2 **220**; 500 BR core **500**, Chaplain variant **495**; 750 core **750**, Assault-Terminator variant **745**; 1000 artillery **965→980** (with HV), second-Tactical variant **945→985** (with Combi Lt swap) — all match the numbers already printed on the pages, so no arithmetic fix was needed.
   - Gladius Task Force enhancement table (Honour Vehement 15 · Adept of the Codex 20 · Artificer Armour 20 · Fire Discipline 25) re-verified unchanged and re-stamped v1.3.
3. **Casual Legends cross-check** — Bike Squad, Attack Bike, Astartes Servitors figures on all 4 Casual starters, `Owned_Models_Inventory.md`'s "Owned but Legends" section, and `README.md`/`Starter_250_Casual.md`'s points-mix line were checked against the new MFM v1.3 **Legends section** in the research note (Bike Squad 3/**80**, Attack Bike 1/**55**, Astartes Servitors 4/**55**) — **identical** to the standalone Warhammer Legends Field Manual figures already on every page. Source-of-truth citation moved from "Legends FM" / "Warhammer Legends Field Manual" to **`MFM v1.3 (Legends)`** in every points table and prose reference, per the brief's "update SoT cite if moving off standalone Legends Field Manual" instruction. No points changed.
4. **Currency lines added (additive)** — `Rules currency: Munitorum Field Manual — Space Marines v1.3 (WarCom/App) [, now including the Legends section on Casual pages] · teaching paraphrase · verify owned PDF.` appended after the existing `## Games Workshop notice` paragraph (and after S2b's `Preview note` line where both were present) on all 16 touched player-facing pages. Never replaced the UNOFFICIAL banner, footer A wording, or S2b's preview note — purely additive per `Footer_Template_Gw_Print.md` §E.
5. **▲ delta notes on Centurion / Redeemer / Termie Lib — research pages only, no scope expansion:**
   - `units/research/Centurion-Devastator-Squad.md` — added a one-paragraph "▲ MFM Marines v1.3" note: 6-model band **365** (+15). Not owned, no list edit.
   - `units/research/Land-Raider-Redeemer.md` — added: **260/280** (1st–2nd / 3rd+), +10/+10 vs the flat 250 under v1.2. Not owned, no list edit.
   - `units/research/Librarian.md` — added: **Librarian in Terminator Armour** rises to **85** (+10); flagged that this stub is the plain Librarian datasheet, not the Terminator-armoured one. Not owned, no list edit.
   - `Owned_Models_Inventory.md`'s Step 2 "is it Legends?" legality table split the old combined "Land Raider / Crusader / Redeemer" row so the Redeemer ▲ delta (260/280, was 250) is visible without touching Land Raider / Crusader (unchanged 220/220).
   - **Vulkan He'stan** is named in the research note's ▲ table but has **no** matching page under `units/research/` (confirmed via glob — zero results) and is not in the brief's task 4 list (Centurion/Redeemer/Termie Lib only) — correctly left untouched, no new stub created.
   - No other unit research stub was touched — all ~90 other `units/research/*.md` pages carry only the generic "Verify Munitorum Field Manual — research <date>" placeholder with no version number, which is exactly the "no full MFM dump" boundary the brief draws.
6. Did **not** apply any October Codex Proxy rewrite (Tactical→Intercessor / Devastator→Desolation counts-as, Whirlwind→Legends) to any Matched or Casual total — that is explicitly S2b's lane, confirmed by re-reading S2b's concurrent additions on every shared file and leaving its callouts and Preview-note lines untouched.
7. Wrote this `S2d_implementer.md`.

## Files changed

**Matched starters (4):**
- `Starter_250_Matched.md`, `Starter_500_Matched.md`, `Starter_750_Matched.md`, `Starter_1000_Matched.md` — MFM v1.2 → v1.3 stamp (header, body, every points-table header, footer); core costs re-verified unchanged; Change Log entry; `Rules currency` line.

**Casual starters (4):**
- `Starter_250_Casual.md`, `Starter_500_Casual.md`, `Starter_750_Casual.md`, `Starter_1000_Casual.md` — same stamp pass; Legends Source column moved to `MFM v1.3 (Legends)`; figures cross-checked unchanged; Change Log entry; `Rules currency` line.

**Shims (4, additive only):**
- `Starter_250.md`, `Starter_500.md`, `Starter_750.md`, `Starter_1000.md` — `Rules currency` line only (no points on these pages).

**Central hub / inventory / detachments (5):**
- `README.md` — SOURCES stamp; `Rules currency` line; Change Log (v1.11).
- `Quick_Reference_Play_Guide.md` — "STARTER SNAPSHOT" heading + SOURCES + footer date stamped to v1.3; `Rules currency` line; header CHANGE_LOG (v0.7.2).
- `Owned_Models_Inventory.md` — Step 2 legality table re-stamped v1.3, Land Raider Redeemer ▲ row split out; Legends citation moved to MFM v1.3 Legends section; `Rules currency` line; Change Log (v1.10).
- `Gladius_Task_Force.md` — enhancement table + DP-tag line stamped to v1.3, costs re-verified unchanged; `Rules currency` line; Change Log (v0.5.2).
- `Anvil_Siege_Force.md`, `First_Company_Task_Force.md` — SOURCES pointer stamped to v1.3 (enhancement figures on these `draft` pages remain public-ref, unaffected); `Rules currency` line; Change Log.

**Unit research (3, research-only ▲ notes):**
- `units/research/Centurion-Devastator-Squad.md`, `Land-Raider-Redeemer.md`, `Librarian.md` — one-paragraph ▲ delta note each, citing the research note; explicitly flagged not owned / not in any starter.

**New file:**
- `docs/handoffs/dataslate_0826/slices/S2d_implementer.md` (this report)

**21 files touched under `games/warhammer_40k_11e/armies/space_marines/` + 1 new handoff file.**

## Total point deltas (owner-facing summary)

| List / page | Delta |
|---|---|
| Every Blood Ravens Matched starter (250/500/750/1000) | **None.** All totals unchanged (235/220, 500/495, 750/745, 965/980/945/985). |
| Every Blood Ravens Casual starter (250/500/750/1000) | **None.** All totals unchanged (215, 475, 745, 995/1010). |
| Gladius Task Force enhancements | **None.** Honour Vehement 15, Adept of the Codex 20, Artificer Armour 20, Fire Discipline 25 all unchanged. |
| Centurion Devastator Squad (6) — not owned, research only | **+15** → 365 |
| Land Raider Redeemer — not owned, research + Step 2 table only | **+10 / +10** → 260 / 280 (1st–2nd / 3rd+) |
| Librarian in Terminator Armour — not owned, research only | **+10** → 85 |
| Vulkan He'stan | Named in research note, **no page exists**, out of task-4 scope — not created. |

## Not touched (explicitly out of scope for S2d)

- **October Codex Proxy rewrites** (Tactical→Intercessor, Devastator→Desolation, Whirlwind→Legends counts-as swaps) — that is slice **S2b**, which ran concurrently on the same files. Every S2b addition (inline preview callouts, `README.md`'s "SM Codex October readiness" section, the Preview-note footer line) was left untouched; files were re-read immediately before each of my edits so neither slice clobbered the other.
- **Full MFM dump** — the ~90 other `units/research/*.md` roster stubs (Tactical Squad, Devastator Squad, Whirlwind, Terminator Squad, etc.) were **not** touched; they carry no version-numbered points citation to bump, and adding full datasheet/point capture to all of them is out of this slice's stated non-goal.
- **Vulkan He'stan** — named in the research note's ▲ table, has no matching `units/research/` page, and is not named in the brief's task 4 — no new stub created, per "do not expand scope."
- **Necron / Kill Team work** — untouched, per brief non-goals.
- **KB/** — Librarian-owned; not touched by this Implementer slice.
- No PDF was read or committed. No binaries added. No `git add` / `git commit` / `git push` was run by this subagent.

## Waivers / open items for QA

1. **Owner-paste provenance:** the v1.3 figures are an owner paste (2026-08-27), not yet read from a saved PDF at `C:\Personal\40K\rules\`. Every touched page's SOURCES/footer explicitly says "owner paste, retrieved 2026-08-27" and points back to [`../research/sm_mfm_v1_3.md`](../research/sm_mfm_v1_3.md) — `draft` until the owner confirms a saved filename and it gets a PDF cross-check, consistent with `raw/pointers/points_manuals.md`'s existing provenance note from S1.
2. **`Anvil_Siege_Force.md` / `First_Company_Task_Force.md` enhancement figures remain unverified public-ref draft** (not MFM-cited) — only their SOURCES pointer was stamped to v1.3; the enhancement point values themselves still need the owned-PDF pass these pages already flagged as pending before this slice.
3. **Concurrency with S2b confirmed clean:** every shared file still carries exactly one `## Games Workshop notice` section and one `## Change Log` section; S2b's `Preview note` line and inline Codex-October callouts are intact alongside this slice's `Rules currency` line and MFM v1.3 stamps.
4. No git commit/push performed by this subagent, per instructions.
