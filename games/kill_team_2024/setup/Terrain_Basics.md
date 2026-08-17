<!--
FILE: games/kill_team_2024/setup/Terrain_Basics.md
VERSION: v1.0 (2026-08-17)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, slice S2)

DOCUMENT_TYPE: Teaching Guide / Terrain Reference
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: Kill Team 2024 (3rd Edition / KT24)
REFERENCE_STATUS: Active - draft, teaching paraphrase cross-checked against Wahapedia KT3 "Killzones" page (retrieved 2026-08-17); not yet spot-checked line-by-line against the owned printed rulebook

SOURCES:
  - raw/pointers/kill_team_2024_core.md (Core Rules, primary PDF owned; not read directly this slice)
  - Wahapedia Kill Team 3 - Killzones page - https://wahapedia.ru/kill-team3/the-rules/killzones/ (community cross-check, retrieved 2026-08-17)
  - Wahapedia Kill Team 3 - Core Rules page (Cover / Obscured key principles, retrieved 2026-08-17)
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

In Kill Team, terrain isn't backdrop - it's most of the game. Whether an operative can be shot, seen, or reached depends on exactly what category of terrain is between it and the enemy. This page teaches how terrain works and how to set up a killzone that plays fairly, at a level that doesn't require transcribing any official terrain template. Cross-checked against the Wahapedia KT3 "Killzones" and "Core Rules" pages, read **2026-08-17**.

---

## Terrain features are made of parts

The most useful habit in Kill Team: **stop thinking of a ruin, a wall, or a stronghold as one object.** Each terrain feature is built from several parts, and each part carries its own terrain type (sometimes more than one). A building's ground floor might be one type, its upper floor another, and a broken vent poking out of it a third.

If a rule tells you to ignore "Light terrain," it means ignore *the Light parts* of whatever feature you're looking at - not the whole model.

When you're using a specific killzone (Volkus, Tomb World, and so on), its own reference sheet or mission pack tells you the type of every part. When you improvise terrain of your own, agree the type of every part **out loud, before the first model moves**.

---

## The core terrain types

| Type | What it generally represents | What it does |
|------|-------------------------------|---------------|
| **Heavy** | Larger, solid scenery - buildings, ruins, bunkers | Can make a target **Obscured** (see below) |
| **Light** | Smaller scenery - rubble, barricades, low walls | Contributes to **Cover** (see below); interacts with rules like Vantage |
| **Exposed** | Very small features, or terrain with gaps too wide to hide behind | Never counts as intervening for Cover or Obscured - it can still get in the way of movement, but it gives no protection |
| **Insignificant** | Very small or low features | Ignored for climbing and dropping - operatives can move straight over it |
| **Accessible** | Doorways and similar gaps built into a wall | Operatives can move straight through, at the cost of roughly 1" of extra movement |
| **Blocking** | Small gaps or narrow windows that shouldn't let you see through | Breaks line of sight through that specific gap, even though the gap itself isn't a "real" piece of scenery |
| **Vantage** | Upper levels operatives can stand on | Lets an operative fire down with bonus accuracy against Engaged targets below, but also usually carries the Light type itself |

Some killzones add their own named types on top of these (walls that block movement outright, teleport pads, hatchways with open/closed states). Those live on the relevant killzone page under [`killzones/`](killzones/) rather than here - this page is the shared foundation every killzone builds on.

---

## Cover and Obscured

These are the two rules that make terrain matter when someone is shooting, and beginners often blur them together. They are not the same thing, and a target can't be both from the same piece of terrain.

### Cover

An operative is **in cover** from another operative if there's terrain between them within its control range (roughly, within 1" and visible to it) - but only if the two operatives are more than 2" apart. Being in cover matters differently depending on order:

- **Concealed and in cover:** not a valid target at all.
- **Engaged and in cover:** a valid target, but the defender gets a **cover save** - an extra defence die it can retain as a success.

### Obscured

An operative is **Obscured** from another operative if there's **Heavy** terrain between them - but that Heavy terrain has to be more than 1" from *both* operatives to count. Stand right up against a ruin and you stop being obscured by it.

Obscured doesn't stop you being targeted. Instead, when the attack happens:

- The attacker must **discard one success** rather than retain it.
- Any **critical successes** are treated as normal successes instead - no crits get through.

### Why the split matters

Cover asks "can I even be shot?" Obscured asks "if I'm shot, how much does it hurt?" A model tucked into a ruin with a Conceal order might be untouchable (Cover); a model standing in the open behind a distant wall might still be shot at, just less effectively (Obscured). Learn to ask both questions before you move an operative into position.

---

## Terrain and movement

Operatives generally can't move *through* solid terrain - only around it, over it, or off it.

| Action | The habit to remember |
|--------|------------------------|
| **Climbing** | An operative can climb terrain it's close to (roughly within 1" horizontally, 3" vertically) and visible to. Every climb costs a minimum of 2" of movement, even for a shorter step up |
| **Dropping** | Moving down costs nothing for the first 2" of any single drop during an action - only the excess counts against movement |
| **Jumping** | From a Vantage point more than 2" up, an operative can jump up to 4" horizontally in one go, then still needs to climb or drop from there |
| **Accessible terrain** | Costs roughly 1" extra to move through - useful for keeping a doorway from being a free highway |

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

---

## Change Log
- v1.0 (2026-08-17): Initial terrain guide (slice S2), cross-checked against the Wahapedia KT3 "Killzones" and "Core Rules" pages, both read 2026-08-17. No official terrain templates or mission maps reproduced.

## Attribution
- Project: Wargame_Concierge
- Maintainer: Russell Catt
- Warhammer 40,000: Kill Team is a trademark of Games Workshop Limited. This document is a personal teaching paraphrase and reproduces no publisher text.

## Rising Tide Notes
- This document follows Rising Tide documentation standards.
- **Verify before you play.** This page paraphrases a community cross-check (Wahapedia), not a line read of the owned Core Book PDF. Confirm Cover, Obscured, and terrain type wording against the owned rulebook before a tournament or a rules dispute. Content reflects sources read on **2026-08-17**.
