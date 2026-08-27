<!--
FILE: games/kill_team_2024/setup/killzones/tomb_world.md
VERSION: v0.6.1 (2026-08-27)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, slice S2; patch sync slice P; dataslate_0826 S3)

DOCUMENT_TYPE: Teaching Guide / Killzone Reference
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: Kill Team 2024 (3rd Edition / KT24)
OWNERSHIP_STATUS: UNASSEMBLED (track_in.md, Preflight lock 2026-08-17)
REFERENCE_STATUS: Active - teaching paraphrase; Close Quarters Guard aligned to Jun 17 update log p.3 (2026-08-18); teleport/breach commentary aligned to Aug '26 killzone update log (2026-08-27)

SOURCES:
  - raw/pointers/kill_team_2024_missions.md (Killzone: Tomb World mission pack PDF, owned)
  - games/kill_team_2024/rules/Patch_Manifest.md
  - Wahapedia Kill Team 3 - Killzones page (Killzone: Tomb World section, retrieved 2026-08-17)
  - Games Workshop webstore - "Killzone: Tomb World" product listing (component list, retrieved 2026-08-17)
  - games/warhammer_40k_11e/armies/necrons/Owned_Models_Inventory.md (cross-game note on Tomb World operatives)
  - docs/handoffs/kill_team_2024_scaffold/track_in.md
  - `eng_killzone_tomb_world_update_log-ptyzlo3dfr-ivlzsazxnf.pdf` (staging, read 2026-08-27) - dataslate_0826 S3

PURPOSE:
  Teach what Killzone: Tomb World is and what "unassembled" specifically means
  here - the operatives are game-ready, the terrain is not - so priority is
  clear once bench time is available.

UPDATE_TRIGGER:
  Update once the terrain is assembled and painted, and again after a first
  Tomb World game is played.
-->

# Killzone: Tomb World - unassembled, terrain only

**Status: UNASSEMBLED.** Build before dedicated Tomb World missions. This page exists so setup is ready the moment the terrain sprue comes off the shelf.

**Rules currency: Kill Team quarterly balance — August 2026** (Core / update logs + team online rules) · teaching paraphrase · verify owned PDFs · confidence `draft`.

---

## What it is

**Killzone: Tomb World** is a Necron-themed terrain expansion built for **close-quarters** play - the same lineage as Killzone: Gallowdark, but with corridors, pillars, hatchways, breach points, a sarcophagus, and teleport pads standing in for a Tomb World's tunnels instead of a voidship's. The kit builds **25 modular terrain pieces from 74 plastic components**, plus a **double-sided game board** (roughly 606 mm x 703 mm), laid out on a **6x7 grid** for setup rather than free-inch placement.

Its walls are **Wall terrain** - a stricter type than the Heavy terrain on Volkus: you can't move through or see over/through Wall terrain at all, only around it, and hatchways/breach points switch between blocking and passable as they're opened during a battle.

---

## Why "unassembled" doesn't mean "not owned"

This is worth separating clearly, because two different things share the "Tomb World" name in this collection:

| Item | Status | Where it's tracked |
|------|--------|---------------------|
| **Tomb World operatives** (Cryptek Geomancer, Canoptek Tomb Crawlers, Canoptek Macrocytes, Necron Warriors, Canoptek Scarab Swarms) | **Assembled, painted, game-ready** | [`games/warhammer_40k_11e/armies/necrons/Owned_Models_Inventory.md`](../../../warhammer_40k_11e/armies/necrons/Owned_Models_Inventory.md) |
| **Killzone: Tomb World terrain** (25 pieces / 74 components) | **Unassembled** | This page; `teams/_Owned_Teams_Inventory.md` kill-zone summary |

The models can already stand in for a Necron force in a 40K game today (see the Necron inventory) - it's specifically the **terrain** for KT24 close-quarters missions that's on sprue. Don't let "Tomb World is game-ready" in the 40K inventory get confused with this killzone's build status.

---

## Setting it up (once assembled)

1. Build and (eventually) paint the 25 terrain pieces - unpainted terrain is entirely playable, priority is availability over finish.
2. Use the 6x7 grid printed on the board to place walls, pillars, and special pieces (sarcophagus, teleport pads, debris) per the mission map you're using.
3. Agree hatchway and breach point starting states (closed, per the core rules) before deployment.
4. Consider this killzone's Close Quarters rules (Gallowdark-lineage) as a step up in complexity from Volkus - a better second or third killzone than a first one.

### Close Quarters Guard (Gallowdark and Tomb World)

There is no separate Gallowdark killzone page yet. These two patches apply to **both** Close Quarters killzones (Jun 17 update log p.3):

- **Guard action:** the first bullet also fires if the operative **performs any action, moves, or is set up**.
- **On Guard:** if you use On Guard, that friendly operative **cannot counteract** that turning point.

Read the full Close Quarters section in the Core Book / mission pack before play — this is the errata delta, not the whole rule.

---

### Teleport pad and breach point — August 2026 update log

Paraphrase from `eng_killzone_tomb_world_update_log-ptyzlo3dfr-ivlzsazxnf.pdf` (staging, read 2026-08-27). Verify against your owned Killzone: Tomb World mission pack PDF before play.

- **Teleport does not bypass "cannot end that move closer" restrictions.** Rules commentary confirms: if a rule says an operative "cannot end that move" closer to enemy operatives, dropzones, etc., **teleporting does not let you ignore that restriction.**
- **Teleport pad, tightened:** equipment terrain cannot be set up within 2" of a teleport pad; an operative touching a teleport pad that has another operative already on it is treated as being within that operative's control range; **an operative cannot teleport more than once per activation.**
- **Breach point / Breach action, tightened:** the action's AP discount (1 less AP, minimum 1AP) is gone from the errata history — the current wording is that the Breach action **cannot be performed for less than 2AP** during an activation/counteraction that also performed the Charge or Shoot action (or vice versa).
- **Older commentary (unchanged, still active):** teleporting is **not** treated as having moved for rules with a distance requirement — named examples: Brood Brothers **Alpha Predator**, Plague Marines **Lumbering Death**, Vespid Stingwings **Neutron Charge**. If a Plague Marines or Vespid Stingwings operative in this killzone teleports, it does not satisfy a "must have moved [X]"-style condition on those team rules.

---

## What to check in the owned PDFs before your first game

- Exact terrain piece list and grid placement, from the box insert or the owned Killzone: Tomb World mission pack PDF
- Whether the Canoptek Circle / Deathwatch team rules or NPO cards came bundled with this terrain (some retail bundles pair Tomb World terrain with those two teams and Necron Warriors/Scarab Swarm NPO minis) - cross-check against `teams/_Owned_Teams_Inventory.md`
- Close Quarters-specific rules (hatchways, breach points, teleport pads) read in full rather than from this summary

---

## Related pages

- [`README.md`](README.md) - all owned kill zones
- [`../../rules/Patch_Manifest.md`](../../rules/Patch_Manifest.md) - Close Quarters Guard errata
- [`shadowhunt.md`](shadowhunt.md) - depends on this terrain for full Descent missions
- [`../../teams/README.md`](../../teams/README.md) - Canoptek Circle and Deathwatch ownership
- [`../../teams/plague_marines/README.md`](../../teams/plague_marines/README.md) - Lumbering Death / teleport distance-requirement note
- [`../../teams/vespid_stingwings/README.md`](../../teams/vespid_stingwings/README.md) - Neutron Charge / teleport distance-requirement note
- [`../../../warhammer_40k_11e/armies/necrons/Owned_Models_Inventory.md`](../../../warhammer_40k_11e/armies/necrons/Owned_Models_Inventory.md) - the already-game-ready Tomb World operatives (40K side)

---

## Games Workshop notice

**UNOFFICIAL.** This document is completely unofficial and in no way endorsed by Games Workshop Limited. Personal / no-charge use only — never for sale. Warhammer, Kill Team and associated marks are trademarks of Games Workshop Limited. Used without permission. No challenge to their status intended. Kill Team is Copyright Games Workshop Limited 2024. Teaching notes by Russell Catt (Wargame Concierge). Games Workshop retains IP in the settings and characters. No official logos.

**Rules currency:** Kill Team quarterly balance — August 2026 (Core / update logs + team online rules) · teaching paraphrase · verify owned PDFs · confidence draft

## Change Log
- v0.6.1 (2026-08-27): QA reopen — add Games Workshop notice + currency line (dataslate_0826).
- v0.6.0 (2026-08-27): dataslate_0826 S3 — teleport vs "cannot end move closer" rules commentary; teleport pad / breach point AP tightening; older teleport-not-moved commentary cross-referenced to Plague Marines and Vespid Stingwings. Currency stamp: Kill Team quarterly balance — August 2026.
- v0.5.0 (2026-08-18): Project-wide semver snapshot (x.y.z).
- v1.1 (2026-08-18): Slice P — Close Quarters Guard (moves/set up; On Guard blocks counteract that TP). Shared with Gallowdark until that killzone page exists.
- v1.0 (2026-08-17): Initial killzone page (slice S2), cross-checked against Wahapedia KT3 Killzones and the GW webstore product listing, both read 2026-08-17. Cross-linked to the 40K Necron inventory to separate operative readiness from terrain build status.

## Attribution
- Project: Wargame_Concierge
- Maintainer: Russell Catt
- Warhammer 40,000: Kill Team is a trademark of Games Workshop Limited. This document is a personal teaching paraphrase and reproduces no publisher text, terrain diagram, or mission map.

## Rising Tide Notes
- This document follows Rising Tide documentation standards.
- **Verify before you play.** Cross-check terrain piece counts, grid layout, and Close Quarters rules against the owned Killzone: Tomb World mission pack PDF once assembly begins. Content reflects sources read on **2026-08-17**.
