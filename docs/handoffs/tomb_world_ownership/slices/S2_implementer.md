# S2 - Implementer Report (Army docs + starters)

- **Track:** `tomb_world_ownership`
- **Slice:** S2
- **Role:** Implementer (content)
- **Model:** `claude-sonnet-5-thinking-high` (Claude Sonnet 5, high reasoning effort) - matches the model matrix assignment in `track_in.md`. No substitution required, no same-family waiver needed.
- **Commit:** pending (no commit/push performed, per instructions - Coordinator owns the single deferred commit at S4)
- **Status:** Resolved - Implemented

---

## Read first (confirmed)

- `docs/handoffs/tomb_world_ownership/slices/S2_brief.md`
- `docs/handoffs/tomb_world_ownership/track_in.md`
- `games/warhammer_40k_11e/armies/necrons/Necron_Lists.md` (FOUNDATION SoT after S1 - confirmed it already reflects Tomb World as owned/game-ready, 385-pt subtotal, Hierotek TBD, and correct build-before-play/sprue totals for the second Warriors squad, second Scarab set, and Immortals)

**Encoding note:** the `Read` tool mis-decoded `S2_brief.md`, `track_in.md`, and `Necron_Lists.md` (rendered as mojibake, consistent with a UTF-8 file being interpreted as UTF-16LE). Confirmed via `powershell Get-Content -Encoding UTF8` that the files on disk are valid UTF-8 and read them correctly that way before editing. No file content was corrupted by this - it was purely a display artifact in one tool. Edits were made with `Write`/`StrReplace`, which produced clean, correct diffs (verified with `git diff`).

## Locked ownership applied

- **Kill Team: Tomb World - owned, game-ready:** 1x Cryptek Geomancer, 2x Canoptek Tomb Crawlers, 5x Canoptek Macrocytes, 10x Necron Warriors, 3x Canoptek Scarab Swarms.
- **Additional owned:** 10x Necron Warriors (2nd squad, unassembled), 3x Canoptek Scarab Swarms (2nd set, unassembled), 5x Immortals (unassembled), Hierotek Circle Kill Team (game-ready, datasheets TBD pending photos).
- **Totals:** 20 Warriors (10 ready + 10 sprue), 6 Scarab Swarms (3 ready + 3 sprue), plus Geomancer, Tomb Crawlers, Macrocytes, Immortals, Hierotek TBD.
- Tomb World is now the **preferred learning baseline** everywhere it's referenced; sprue extras are consistently tagged assemble-to-expand, never a blocker.

## Changes made

### 1. `games/warhammer_40k_11e/armies/necrons/Owned_Models_Inventory.md` (v1.1 -> v1.2)
- Moved Geomancer, Tomb Crawlers, Macrocytes, Warriors (1st squad), Scarab Swarms (1st set) into **Game-ready**, tagged "Kill Team: Tomb World."
- Kept Hierotek Circle in Game-ready (ID pending) as an *additional* set, not the only one.
- Kept 2nd Warriors squad, 2nd Scarab set, and Immortals under **Build before play**.
- **Removed** the "Explicitly NOT owned" section (previously falsely listed Tomb World as not owned) and replaced it with a correction note plus a new "Ownership totals" table (20 Warriors, 6 Scarabs, etc.).

### 2. `games/warhammer_40k_11e/armies/necrons/README.md` (v2.1 -> v2.2)
- Rewrote "Current collection status" table: Tomb World listed first as the game-ready preferred baseline; Hierotek Circle as an additional game-ready set (ID pending); sprue items unchanged; removed the "Not owned: Kill Team: Tomb World" row.
- Rewrote "Two corrections worth knowing" item 1 to state plainly that Tomb World is owned and that the prior "only Hierotek is table-ready" claim was wrong.
- Updated "Start here" pointer and file-index descriptions to reference the Tomb World force.

### 3. `games/warhammer_40k_11e/armies/necrons/Starter_250.md` (v1.1 -> v1.2)
- Replaced the Hierotek-blocked "two blockers" framing with a **playable-tonight Tomb World list**: Geomancer (75) + Warriors (80, MFM v1.2) + Tomb Crawlers (85) = **240/250 pts**, zero purchases, zero assembly.
- Noted this list works for either Canoptek Court or Cryptek Conclave.
- Demoted the Hierotek Circle photo-ID checklist to an optional, non-blocking alternate/expansion.
- Listed Macrocytes (Tomb World, game-ready but not needed at this size) and the sprue extras (2nd Warriors, 2nd Scarabs, Immortals) as clearly non-blocking, build-before-play/assemble-to-expand items.

### 4. `games/warhammer_40k_11e/armies/necrons/Starter_500.md` (v1.1 -> v1.2)
- New shared foundation: the **full Tomb World box** (Geomancer + Warriors + Tomb Crawlers + Macrocytes + Scarab Swarms = 365 pts), explicitly marked "do not re-shop."
- **Path A (Canoptek Court, 500/500):** Tomb World foundation + 2nd Scarab set (owned, sprue) + Canoptek Wraiths (purchase) = 500. Cheaper no-purchase variant at 405 also given.
- **Path B (Cryptek Conclave, 490/500):** Tomb World foundation + Immortals (owned, sprue) + Plasmancer (`TBD`/purchase) = 490.
- Purchase summary table now explicitly shows Macrocytes and Tomb World's Scarab Swarms as **OWNED**, not shopping targets - satisfies the brief's explicit requirement to exclude owned Macrocytes/Tomb World Scarabs from shopping.

### 5. `games/warhammer_40k_11e/armies/necrons/Quick_Reference_Play_Guide.md` (v1.1 -> v1.2)
- Page 1 (rules/phases/combat sequence) unchanged - no ownership content there.
- **Page 2 "Starter Snapshot" rebuilt around the Tomb World force**: full ownership table (Geomancer, Warriors, Tomb Crawlers, Macrocytes, Scarab Swarms, plus sprue extras and Hierotek), and the 240/250, 500 (Court), and 490 (Conclave) totals matching `Starter_250.md`/`Starter_500.md`.

### 6. `games/warhammer_40k_11e/rules/Overview.md` (v1.0 -> v1.1)
- In "Your realistic first game," replaced "**Only the Hierotek Circle set is game-ready today**" with a corrected statement that the Kill Team: Tomb World force is game-ready today (preferred baseline), Hierotek Circle is also game-ready pending photo ID, and the second Warriors squad / second Scarab set / Immortals are owned-but-unassembled.
- Added `Owned_Models_Inventory.md` to sources; added a changelog entry.

## Tier 1 checks performed

1. **Ripgrep sweep for banned phrases** across `games/warhammer_40k_11e/**/*.md`: no live occurrence of "Tomb World not owned" or "only Hierotek is table-ready" remains anywhere - all matches are historical/changelog text explicitly documenting that the old claim was corrected, or unrelated Space Marines doc content (out of scope for this slice).
2. **Cross-file number consistency:** `Starter_250.md` (240/250), `Starter_500.md` (500 Path A / 490 Path B), and `Quick_Reference_Play_Guide.md` page 2 all use the same unit costs and totals (Geomancer 75, Warriors 80, Tomb Crawlers 85, Macrocytes 85, Scarab Swarms 40, Immortals 70) - verified by direct comparison.
3. **`git diff --stat`** on the six edited files shows clean, line-level diffs only (no binary/garbled content), confirming the earlier `Read`-tool mojibake never reached the actual files.
4. **`git status`** confirms no other files were touched by this slice's edits (the six target files are the only ones with new changes attributable to this session; the repository-wide "modified" flag on many unrelated files is a pre-existing `core.autocrlf`/line-ending normalization artifact already present before this session started, not caused by S2 - flagging for Coordinator/QA awareness, not fixed here per "do not re-shop" scope discipline and no-commit instruction).
5. **No commit or push performed** - working tree left as modified files only, per instructions.

## Exit criteria - self-check

- [x] Starters prefer Tomb World Phase 1 (`Starter_250.md` leads with the 240-pt Tomb World list, playable tonight)
- [x] Extras (2nd Warriors, 2nd Scarabs, Immortals) flagged sprue/unassembled everywhere they appear
- [x] No "only Hierotek is table-ready" language remains as a live claim
- [x] No false "Tomb World not owned" language remains as a live claim
- [x] `Starter_500.md` shopping/purchase summary excludes owned Macrocytes and Tomb World Scarab Swarms
- [x] `rules/Overview.md` ownership/starter-path language consistent with the other five files

## Notes for QA / Coordinator

- Points for Geomancer (75), Tomb Crawlers (85 for 2), and Macrocytes (85 for 5) are carried over from `Necron_Lists.md` (the FOUNDATION SoT) rather than independently re-verified against the Munitorum Field Manual PDF, since I did not have PDF access in this session. This is flagged in each file's header (`REFERENCE_STATUS`) as "pending independent MFM re-verification," consistent with the project's existing convention for flagging unverified figures (see `README.md`'s prior points-correction note). A future points-audit slice may want to confirm these against the MFM directly.
- Repo-wide `core.autocrlf` line-ending noise in `git status` (dozens of files outside this slice's scope showing as modified with empty `git diff` output) predates this session and was not introduced or fixed here.
