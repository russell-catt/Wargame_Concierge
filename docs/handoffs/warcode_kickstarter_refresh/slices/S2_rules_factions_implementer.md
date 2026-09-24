# S2 — Rules and factions implementer report

- **Track:** `warcode_kickstarter_refresh`
- **Stage:** 2
- **Date:** 2026-09-24
- **Status:** Complete
- **Mechanics baseline:** `The-Warcode-Rulebook-V.0.8.9-F.pdf`

## Result

Updated the shipping rules corpus to the current v0.8.9-F baseline. Preserved the verified equivalence of core rules, contracts, protocols, maps, Protagen Marines, and Ulfari; added complete MDR Executive Unit and Custodia Silens roster coverage from PDF pp.37–40.

No ruling was invented for any source ambiguity. Historical v0.8.7-F quote citations remain where their page content is verified equivalent; each affected surface now records current v0.8.9-F provenance.

## Files changed

### Added

- `games/the_warcode/factions/mdr/Squad_Datasheet.md`
- `games/the_warcode/factions/dominium/Squad_Datasheet.md`
- `docs/handoffs/warcode_kickstarter_refresh/slices/S2_rules_factions_implementer.md`

### Updated

- `games/the_warcode/README.md`
- `games/the_warcode/First_Game_Walkthrough.md`
- `games/the_warcode/Quick_Reference_Play_Guide.md`
- `games/the_warcode/factions/mdr/README.md`
- `games/the_warcode/factions/dominium/README.md`
- `games/the_warcode/factions/protagen_marines/README.md`
- `games/the_warcode/factions/protagen_marines/Squad_Datasheet.md`
- `games/the_warcode/factions/ulfari/README.md`
- `games/the_warcode/factions/ulfari/Squad_Datasheet.md`
- `games/the_warcode/guides/Proxy_Play_at_Home.md`
- `games/the_warcode/guides/Warcode_vs_That_Other_Game.md`
- `games/the_warcode/rules/Activation_and_AP.md`
- `games/the_warcode/rules/Combat_Ranged_and_Melee.md`
- `games/the_warcode/rules/Comparative_Glossary.md`
- `games/the_warcode/rules/Contract_Cards_Reference.md`
- `games/the_warcode/rules/Contracts_and_VP.md`
- `games/the_warcode/rules/Equipment_Loot_and_Doors.md`
- `games/the_warcode/rules/Key_Concepts.md`
- `games/the_warcode/rules/Keyword_Glossary.md`
- `games/the_warcode/rules/Overview.md`
- `games/the_warcode/rules/Protocol_Cards_Reference.md`
- `games/the_warcode/rules/Rulebook_Quotes.md`
- `games/the_warcode/rules/Scenarios_and_Events.md`
- `games/the_warcode/rules/Turn_Structure.md`
- `games/the_warcode/setup/Board_Setup.md`
- `games/the_warcode/setup/Terrain_Basics.md`

No lore or campaign file was edited.

## Rules work completed

- Extended `Rulebook_Quotes.md` with current-source MDR pp.37–38 and Custodia pp.39–40 sections.
- Replaced the MDR and Dominium marketing stubs with verified faction overviews.
- Added all eight profiles for each new squad, including weapon profiles, abilities, filename, PDF page, and section citations.
- Recorded Protagen pp.33–34 and Ulfari pp.35–36 equivalence without rebuilding stable profile surfaces.
- Updated Contracts provenance and preserved card 4186’s `Justicar Julius` spelling alongside the roster’s `Justiciar Julius`.
- Added Order and Inspiration to AP teaching.
- Corrected the claim that the p.11 Overwatch action list is exhaustive.
- Added Hand Flamethrower, Burning, Directed/Focused Energy, Agility reduction, and Lancer lock exceptions.
- Added restricted loadouts, pickup/drop gaps, medkit immunity, and Burning-removal gaps.
- Added the Inspired-activation window and unresolved unit-effect ordering before protocol/scenario effects and VP.
- Refreshed overview, key concepts, glossary, comparative guide, proxy guide, walkthrough, and quick reference for four playable squads.

## Ambiguity register preservation

All required items remain explicit and unresolved:

1. `Justicar Julius` / `Justiciar Julius`.
2. Directed Energy / Focused Energy.
3. Hand Flamethrower ammo 3 / “never needs reloading.”
4. Inspiration ordering and repeat targeting.
5. Ability use absent from the p.11 Overwatch list.
6. No lower floor or stacking order for Agility reductions.
7. End-of-round ordering among Combat Medic, Burning, Influence, and Choke, followed by protocol/scenario effects and VP.
8. Equipment pickup, multi-item drop, medkit immunity, and Burning-removal interactions.

Additional Sergeant aura/Comms relay, Burning friendly-fire, Choke duration, Directed Energy critical-source, and Lancer geometry gaps are also retained.

## Verification

- **Source profile check:** compared both new datasheets against `rulebook_v089f_extract.txt` and current PDF pp.37–40.
- **Current-provenance scan:** all 28 changed Warcode shipping files contain v0.8.9-F provenance or an explicit current-baseline equivalence note.
- **Banned-name scan:** case-insensitive scan of `games/the_warcode/**/*.md` for the prohibited comparator names and number variants returned **0 matches**.
- **Stale four-faction scan:** no active statement remains that MDR/Custodia are future, stub-only, or unplayable; remaining “stub” hits are historical change-log entries or the unrelated digital-play placeholder.
- **Ambiguity scans:** each of the eight required ambiguity groups has at least one rules-facing hit; the central register is in `rules/Rulebook_Quotes.md`.
- **Link check:** all relative Markdown `.md` links in the 30-file `games/the_warcode` corpus resolve.
- **Scope check:** no file under `raw/`, `KB/`, lore, campaign, or unrelated game trees was edited.
- **Git:** not run.

## Handoff

Ready for Stage 2 QA. Review should concentrate on visual confirmation of reconstructed profile columns on PDF pp.37–40 and density/readability of the two new squad sheets.
