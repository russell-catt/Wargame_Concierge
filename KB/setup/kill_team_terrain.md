---
title: Kill Team Terrain Basics
type: setup
system: kill_team_2024
created: 2026-08-18
updated: 2026-08-18
version: 0.5.0
sources: [kill_team_2024_core_rules, games/kill_team_2024/setup/Terrain_Basics.md, games/kill_team_2024/setup/Board_Setup.md, games/kill_team_2024/rules/Patch_Manifest.md]
confidence: draft
tags: [setup, kill_team_2024, terrain, killzone, vantage]
---

# Kill Team Terrain Basics

How scenery actually works in Kill Team 2024: features are made of **parts**, each part has a type, and cover/obscured are checked from those types. Teaching paraphrase of [`Terrain_Basics.md`](../../games/kill_team_2024/setup/Terrain_Basics.md) (Accessible / Insignificant / parts aligned to owned Full-Scan **2026-08-18**; layout advice still began as Wahapedia **2026-08-17**).

**L1 flag:** there was no KT24 setup page after the Wahapedia core ingest. This page is new from shipping, not a silent upgrade of an old draft.

---

## Parts, not objects

Stop treating a ruin as one blob. A feature is several **parts**; a rule that ignores Light ignores Light *parts*, not the whole model. Agree every part's type **before** the first move. Killzone sheets (Volkus, Tomb World) name the types; improvised tables need the same conversation out loud.

| Type | Player-facing job |
|------|-------------------|
| **Heavy** | Can make a target **obscured** |
| **Light** | Feeds **cover**; Vantage is also Light |
| **Exposed** | Never intervening for cover or obscured |
| **Insignificant** | Ignored for climbing/dropping — identify before battle |
| **Accessible** | Move through (extra **1"**; only the **centre of the base** must pass). That extra inch **does** count against the 2" counteract cap |
| **Blocking** | A *gap* that breaks sight, not a solid wall |
| **Vantage** | Upper level you can **be placed** on; Accurate vs Engage targets below is **SEQUENCE**, not eligibility |
| **Ceiling** | Small-enough bases can pass underneath (update log) |

**Connected** (Vantage / obscured): "Heavy connected to Vantage" means any part of the **same terrain feature**.

---

## Cover and obscured (table habits)

- **Cover:** intervening terrain in the target's control range, and more than 2" from the shooter. Conceal + cover = not a valid target. Engage + cover = **cover save** (collect three defence dice, retain one **normal success**, roll the remainder).
- **Obscured:** intervening Heavy. Being within 1" of Heavy ignores **only that part**, not the whole ruin. Attacker discards one success; remaining successes cannot be critical that sequence.
- Same feature cannot apply both — defender picks ([[cover_kill_team]], [[valid_target]]).

---

## Movement habits

Climbing costs a minimum 2" vertical. First 2" of a drop in an action is free. Jumping from Vantage higher than 2" off the floor: up to 4" horizontally, then drop/climb; climb a rampart at the edge first if there is one.

Board size and drop zones: [`Board_Setup.md`](../../games/kill_team_2024/setup/Board_Setup.md) (standard killzone **30" × 22"**).

---

## Open questions

- Exact Volkus/Tomb World part lists still belong on the physical reference sheet, not here.
- Other owned killzones (Shadowhunt, 3e Starter, 2e scatter) are shipping pages only this pass.

---

## Related pages

- [[killzones_volkus_tomb_world]] — Door Fight and Close Quarters Guard
- [[cover_kill_team]] · [[valid_target]] · [[control_range_kill_team]]
- [[kill_team_2024_core_rules]] · [[glossary]] · [[index]]
- Shipping: [`Terrain_Basics.md`](../../games/kill_team_2024/setup/Terrain_Basics.md), [`Patch_Manifest.md`](../../games/kill_team_2024/rules/Patch_Manifest.md)
