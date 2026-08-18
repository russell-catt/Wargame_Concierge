<!--
FILE: games/kill_team_2024/setup/Terrain_Basics.md
VERSION: v0.5.0 (2026-08-18)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, slice S2; patch sync slice P)

DOCUMENT_TYPE: Teaching Guide / Terrain Reference
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: Kill Team 2024 (3rd Edition / KT24)
REFERENCE_STATUS: Active - teaching paraphrase; Accessible / Insignificant / parts aligned to owner Full-Scan p.58–61 + Jun 17 update log (2026-08-18)

SOURCES:
  - raw/pointers/kill_team_2024_core.md
  - games/kill_team_2024/rules/Patch_Manifest.md
  - games/kill_team_2024/rules/Target_Eligibility.md
  - Wahapedia Kill Team 3 - Killzones page - https://wahapedia.ru/kill-team3/the-rules/killzones/ (community cross-check, retrieved 2026-08-17)
  - reference/Source_Library.md

PURPOSE:
  Explain what a terrain feature's parts actually do - cover, obscuring,
  movement, climbing - and how to lay out a killzone that plays well, without
  transcribing any official mission map or terrain template.

PRIMARY_AUDIENCE:
  - A beginner dressing a killzone for the first time
  - A player deciding whether a piece of scenery blocks a shot

KEY_SECTIONS_EXPECTED:
  - Terrain features are made of parts
  - The core terrain types
  - Cover and Obscured
  - Terrain and movement
  - Setting up a killzone that plays well
  - Killzone-specific terrain

UPDATE_TRIGGER:
  Update when a Core Book errata, Approved Ops pack, or new killzone changes
  terrain type definitions, Cover, or Obscured.
-->

# Terrain Basics - what the scenery actually does

In Kill Team, terrain isn't backdrop - it's most of the game. Whether an operative can be shot, seen, or reached depends on exactly what category of terrain is between it and the enemy. This page teaches how terrain works and how to set up a killzone that plays fairly, at a level that doesn't require transcribing any official terrain template. Accessible / Insignificant / parts wording aligned to owned Core Book **2026-08-18**; other layout advice still began as Wahapedia paraphrase (retrieved **2026-08-17**).

---

## Terrain features are made of parts

The most useful habit in Kill Team: **stop thinking of a ruin, a wall, or a stronghold as one object.** Each terrain feature is built from several parts, and each part carries its own terrain type (sometimes more than one). A building's ground floor might be one type, its upper floor another, and a broken vent poking out of it a third.

If a rule tells you to ignore "Light terrain," it means ignore *the Light parts* of whatever feature you're looking at - not the whole model. A mix of Light and Heavy parts on one ruin is normal; you still resolve each part.

When you're using a specific killzone (Volkus, Tomb World, and so on), its own reference sheet or mission pack tells you the type of every part. When you improvise terrain of your own, agree the type of every part **out loud, before the first model moves**. Some killzones add extra types (for example **Ceiling**: small bases can move underneath).

---

## The core terrain types

| Type | What it generally represents | What it does |
|------|-------------------------------|---------------|
| **Heavy** | Larger, solid scenery - buildings, ruins, bunkers | Can make a target **Obscured** (see below) |
| **Light** | Smaller scenery - rubble, barricades, low walls | Contributes to **Cover** (see below); interacts with rules like Vantage |
| **Exposed** | Very small features, or terrain with gaps too wide to hide behind | Never counts as intervening for Cover or Obscured - it can still get in the way of movement, but it gives no protection |
| **Insignificant** | Very small or low features | Ignored for **climbing and dropping** — move over/across without going up and down. Identify these parts **before the battle** (rubble piles, storm bolters on a wall, and similar) |
| **Accessible** | Doorways and similar gaps built into a wall | You can move through (this overrides the usual base / terrain-and-movement restrictions). Costs an extra **1"** of movement. Only the **centre of the base** needs to pass — base size does not matter. Example: a door |
| **Blocking** | Small gaps or narrow windows that shouldn't let you see through | Breaks line of sight through that specific gap. Blocking is **gaps, not physical terrain** — rare, but needed |
| **Vantage** | Upper levels operatives can **be placed** on | Also **Light**. Lets an operative fire down (Accurate vs Engage targets below is SEQUENCE). If terrain is *not* Vantage, you can move over it but cannot finish a move or be set up on it |
| **Ceiling** | Overhangs / upper structure you can pass under | Operatives on small enough bases can move underneath regardless of height (update log). Often paired with Vantage on Volkus ruins |

Some killzones add their own named types on top of these (walls that block movement outright, teleport pads, hatchways with open/closed states). Those live on the relevant killzone page under [`killzones/`](killzones/) rather than here - this page is the shared foundation every killzone builds on.

---

## Cover and Obscured

These are the two rules that make terrain matter when someone is shooting, and beginners often blur them together. They are not the same thing, and a target can't be both from the same piece of terrain.

### Cover

An operative is **in cover** from another operative if there's terrain between them within its control range (roughly, within 1" and visible to it) - but only if the two operatives are more than 2" apart. Being in cover matters differently depending on order:

- **Concealed and in cover:** not a valid target at all.
- **Engaged and in cover:** a valid target, but the defender gets a **cover save** — collect three defence dice, retain one **normal success** without rolling, roll the remainder.

### Obscured

An operative is **Obscured** from another operative if there's **Heavy** terrain between them. Being within 1" of Heavy ignores **only that part** of the feature, not the whole ruin — a farther part of the same feature can still obscure.

Obscured doesn't stop you being targeted. Instead, when the attack happens:

- The attacker must **discard one success** rather than retain it.
- Any **critical successes** are treated as normal successes instead - no crits get through.

A target cannot be in cover **and** obscured by the **same** terrain feature — the defender picks one (Jun 17 update log). "Heavy connected to Vantage" means any part of the **same** terrain feature.

### Why the split matters

Cover asks "can I even be shot?" Obscured asks "if I'm shot, how much does it hurt?" A model tucked into a ruin with a Conceal order might be untouchable (Cover); a model standing in the open behind a distant wall might still be shot at, just less effectively (Obscured). Learn to ask both questions before you move an operative into position.

---

## Terrain and movement

Operatives generally can't move *through* solid terrain - only around it, over it, or off it.

| Action | The habit to remember |
|--------|------------------------|
| **Climbing** | An operative can climb terrain it's close to (roughly within 1" horizontally, 3" vertically) and visible to. Every climb costs a minimum of 2" of movement, even for a shorter step up |
| **Dropping** | Moving down costs nothing for the first 2" of any single drop during an action - only the excess counts against movement |
| **Jumping** | From Vantage higher than 2" from the killzone floor: up to 4" horizontally in one straight increment, then drop or climb from there. Climb a rampart at the edge first if there is one (update log) |
| **Accessible terrain** | Extra **1"** to move through; only the **centre of the base** needs to fit. That extra inch **does** count against the 2" counteract move cap — you usually cannot go through doors while counteracting |

None of this replaces reading your operative's actual Move stat and any rules on its datacard - this table is the shape of terrain interaction, not a substitute for the core rules.

---

## Setting up a killzone that plays well

Whether you're following a printed mission map or laying out your own terrain, a few habits keep a game fair and fun:

- **Avoid a mirror-image layout.** Asymmetric setups reward good generalship more than a perfectly symmetrical board does - vary size, position, and orientation even if both sides get "one stronghold, one ruin."
- **Give every drop zone some Heavy terrain right at its edge.** New operatives need somewhere to hide the moment they're set up, or a Vantage-camping opponent can pick them off before they've activated once.
- **Keep Vantage terrain out of drop zones.** It's more interesting if reaching a good firing position costs someone a turn of movement.
- **Concentrate the rest of your terrain between the drop zones**, not inside them. That's what creates fire lanes and forces real tactical decisions instead of a shooting gallery.
- **You don't need official scenery.** Any terrain of roughly the right footprint works, provided both players agree its type before the game - this matters more for a home-brew layout than for a boxed killzone with its own reference sheet.

---

## Killzone-specific terrain

The details above are the shared foundation. Each owned killzone adds its own terrain features and, sometimes, its own extra terrain types (Wall terrain that fully blocks movement and sight, hatchways and breach points with open/closed states, teleport pads, and so on). See the pages under [`killzones/`](killzones/) for what each owned board actually contains - **none of that detail is transcribed here**, and none of the official terrain templates or mission maps are reproduced anywhere in this repository.

---

## Related pages

- [`Board_Setup.md`](Board_Setup.md) - the pre-game sequence this fits into
- [`killzones/README.md`](killzones/README.md) - owned kill zones and their terrain
- [`../rules/README.md`](../rules/README.md) - the in-battle rules spine (orders, actions, weapon rules)
- [`../rules/Target_Eligibility.md`](../rules/Target_Eligibility.md) - verbatim cover / intervening / Vantage quotes
- [`../rules/Patch_Manifest.md`](../rules/Patch_Manifest.md) - errata ledger

---

## Change Log
- v0.5.0 (2026-08-18): Project-wide semver snapshot (x.y.z).
- v1.1 (2026-08-18): Slice P — Accessible (centre of base, extra 1", counteract 2" cap); Insignificant (identify before battle); parts / Ceiling; obscured 1" is parts-only; cover save collect-three.
- v1.0 (2026-08-17): Initial terrain guide (slice S2), cross-checked against the Wahapedia KT3 "Killzones" and "Core Rules" pages, both read 2026-08-17. No official terrain templates or mission maps reproduced.

## Attribution
- Project: Wargame_Concierge
- Maintainer: Russell Catt
- Warhammer 40,000: Kill Team is a trademark of Games Workshop Limited. This document is a personal teaching paraphrase and reproduces no publisher text.

## Rising Tide Notes
- This document follows Rising Tide documentation standards.
- **Verify before you play.** Accessible / Insignificant / parts / cover-save aligned to owned PDFs **2026-08-18**. Killzone templates and mission maps stay in the books you own.
