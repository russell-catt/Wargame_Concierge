<!--
FILE: games/warhammer_40k_11e/setup/Terrain_Basics.md
VERSION: v0.5.2 (2026-08-25)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, wd527_shipping S2)

DOCUMENT_TYPE: Teaching Guide / Terrain Reference
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: Warhammer 40,000 - 11th Edition
REFERENCE_STATUS: Active - draft, spot-checked against owned PDFs 2026-08-16

SOURCES:
  - C:\Personal\40K\rules\eng_01-06_warhammer40k_new40k_core_rules.pdf (Section 13, read 2026-08-16)
  - C:\Personal\40K\rules\eng_22-07_warhammer_40,000_event_companion-alyapl19us-b2drgwkji4.pdf (v1.1, read 2026-08-16)
  - C:\Personal\40K\Terrain\A4\ (printable A4 footprint packs - path pointers only)
  - C:\Personal\40K\WD_527\ (owned digital backup; Trinity Hobby 2026-08-22)
  - raw/white_dwarf_527/designer_commentary_notes.md
  - reference/Source_Library.md

PURPOSE:
  Explain terrain areas and terrain categories, what each category does to
  movement and visibility, and how much terrain a table actually needs.

PRIMARY_AUDIENCE:
  - A beginner dressing a table for the first time
  - A player deciding whether a piece of scenery is Light or Dense

KEY_SECTIONS_EXPECTED:
  - Terrain areas vs terrain features
  - The three categories
  - The four visibility rules
  - Terrain and movement
  - How much terrain is enough
  - Printable footprints

UPDATE_TRIGGER:
  Update when a Core Rules version, universal rules update, or Event Companion
  changes terrain categories, cover, the Hidden rule, or recommended footprints.
-->

# Terrain Basics - what the scenery actually does

Terrain in 11th Edition is not decoration. It is the reason armies do not simply shoot each other off the table on turn one. This page explains how it works and how much of it you need.

Checked against the owned Core Rules PDF (Section 13) on **2026-08-16**. IDs **13.01–13.11** and **06.01** live in [`../rules/Core_Rules_Quotes.md`](../rules/Core_Rules_Quotes.md).

**Contradiction check (2026-08-18):** Benefit of Cover still **worsens BS by 1** (**13.08**), Hidden is 15" detection (**13.09**), Obscuring blocks LOS across light/dense areas (**13.10**). Matches 2026-08-16 paraphrase. No rewrite.

---

## Terrain areas come first

The most common beginner mistake is putting scenery on the table and starting to play. 11th Edition works the other way round.

A **terrain area** is a defined region of the battlefield. You create one by:

- putting down a mat or base and placing terrain features **wholly within** it, or
- placing a single terrain feature directly on the table, or
- placing several features so that together they outline an area.

A **terrain feature** is the physical model - a ruin, a barricade, a crater.

Why the distinction matters:

- **Objectives are usually terrain areas.** A model is in range of a terrain objective by being inside that area, not by being within some distance of a marker.
- **Cover depends on being inside a terrain area**, not on hiding behind a wall.
- The Hidden and Obscuring rules both operate on terrain areas.

So: agree your terrain areas out loud, with your opponent, **before** the first model moves.

**Commentary (White Dwarf 527 — Rules Focus: Terrain Objectives):**

The WD527 battle report places **footprint cutouts** on the mat first, then ruins on top — the footprint is the terrain area, and for objectives the area itself is what you control. That order matches Core teaching here and on [`Board_Setup.md`](Board_Setup.md); Mission 38 uses the same footprint layout idea — [`WD527_Monthly_Mission.md`](WD527_Monthly_Mission.md).

**Cite:** WD527, Rules Focus: Terrain Objectives (battle report); owned digital backup purchased Trinity Hobby **2026-08-22**; local scans `C:\Personal\40K\WD_527\`. Tier **1.5** — Core / Event Companion win on mechanics.

---

## The three categories

Every terrain feature belongs to exactly one category. Two features in the same terrain area can be different categories.

| Category | Typical scenery | Effect |
|----------|----------------|--------|
| **Exposed** | Craters, razorwire, scattered debris | Everything moves through freely. Offers the least protection |
| **Light** | Barricades, low walls, statuary | Everything moves through freely, but it makes its terrain area **obscuring** |
| **Dense** | Buildings, ruins, containers, woods | Blocks movement for larger models, and carries the **Solid** rule. The category that shapes a game |

Agree the category of every piece as you set up. It is a two-minute conversation that prevents a two-hour argument.

---

## The four visibility rules

Line of sight itself is **06.01**. Terrain then applies **13.07–13.11**.

### Benefit of Cover

A unit has the benefit of cover against a ranged attack if **every** model in it either:

- is INFANTRY, BEASTS, or SWARM and is inside a terrain area, or
- is not fully visible to the attacker because of intervening terrain features or obscuring terrain areas.

**What it does: it worsens the attacking weapon's Ballistic Skill by 1** (**13.08**).

> This is an 11th Edition change worth reading twice. Cover **no longer improves your armour save**. It makes the enemy less accurate. If you learned the older wording, unlearn it.

**Commentary (White Dwarf 527 — Rules Focus: Benefit of Cover):**

Designer play notes line up with Core **13.08**: INFANTRY, BEAST, or SWARM wholly inside a terrain area get Benefit of Cover (attacker BS worsened by 1). Vehicles and Monsters get it when intervening terrain means they are not fully visible. Footprints first still matter — being inside the agreed area is what unlocks the Infantry-style path to cover.

**Cite:** WD527, Rules Focus: Benefit of Cover (battle report); owned digital backup purchased Trinity Hobby **2026-08-22**; local scans `C:\Personal\40K\WD_527\`. Tier **1.5** — Core / Event Companion win on mechanics.

### Hidden

An INFANTRY, BEASTS, or SWARM model is **hidden** while it is inside a terrain area containing at least one **Dense** feature, and its unit did not make ranged attacks this turn or last turn.

A hidden model can only be seen by enemies within their **detection range**, which is **15"** unless something changes it (**13.09**).

This is the big new positional lever. A quiet unit sitting in a ruin is effectively invisible to anything more than 15" away - and shooting breaks the effect for two turns, not one.

### Obscuring

Any terrain area containing a **Light** or **Dense** feature is **obscuring**. If every line of sight between two models crosses one or more obscuring terrain areas - not counting an area one of them is standing in - those models simply **cannot see each other**.

This is what makes a properly furnished board playable for melee armies.

### Solid

Dense terrain features are **Solid**: you cannot draw line of sight through any enclosed gap in them within 3" of ground level. Windows, doorways, and bullet holes on the ground floor do not let you shoot through.

Above 3" the gaps work normally, which is why an upper floor is a firing position and a ground floor is a bunker.

---

## Terrain and movement

| Category | Who can move through it |
|----------|------------------------|
| **Exposed / Light** | Everything, horizontally and vertically |
| **Dense** | INFANTRY, BEASTS, and SWARM models move through horizontally and vertically. Other models can only cross sections 2" or less in height, or must climb over |

Other movement details worth knowing:

- **Climbing costs movement.** Distance moved up and down counts toward the move.
- **INFANTRY, BEASTS, SWARM, FLY, and MONSTER models can end a move on an upper surface**, provided the model is stable and no part of its base overhangs the edge.
- **Height pays.** A model on a section 3" or more high gets **Plunging Fire**: +1 Ballistic Skill against targets containing models at ground level.

---

## How much terrain is enough

Too little terrain produces a shooting gallery. The recommended event layouts use **sixteen terrain areas** on a 44" x 60" board:

| Terrain area footprint | Quantity |
|------------------------|----------|
| 6" x 4" | 4 |
| 10" x 2.5" | 2 |
| 6" x 2" | 4 |
| 7" x 11.5" | 4 |
| 8" x 11.5" polygon | 2 |

Rules of thumb from the Core Rules and the Event Companion:

- **Dense terrain is what balances the game.** Too few Dense features favours shooting armies and punishes melee armies.
- **Leave a gap between a terrain feature and the edge of its terrain area.** Models need somewhere to stand inside the area, which matters for cover, for Hidden, and for holding a terrain objective.
- **Leave lanes for big models.** Monsters and Vehicles cannot cross tall Dense terrain, so give them room to manoeuvre, especially near board edges.
- **You do not need matching scenery.** Anything roughly the right size works, provided both players agree its category before the game.
- For a learning game, aim for **four to six substantial pieces spread across the board**, with at least a couple you cannot see through.

---

## Printable footprints - local library

The owner has printable terrain-area footprint packs. **These stay outside this repository** - path pointers only, no copies committed.

### A4 packs

Location: `C:\Personal\40K\Terrain\A4\`

| Pack |
|------|
| `11th - Terrain Footprints - A4 Scale - Combat Patrol Battlezone.pdf` |
| `11th - Terrain Footprints - A4 Scale - Imperial World.pdf` |
| `11th - Terrain Footprints - A4 Scale - Death World Jungle.pdf` |
| `11th - Terrain Footprints - A4 Scale - Death World Snow.pdf` |
| `11th - Terrain Footprints - A4 Scale - Maelstrom World.pdf` |
| `11th - Terrain Footprints - A4 Scale (Grey City Tone).pdf` |

These are A4-rescaled versions of the A3 originals published on Warhammer Community. Printed and cut out, they give you physical terrain-area boundaries to lay on the table - which removes the single biggest source of setup disagreement.

### Full-size footprint documents

Location: `C:\Personal\40K\rules\`

| Document |
|----------|
| `eng_12-06_warhammer40000_terrainareafootprints-biavo5zf9f-gxdahkydbj.pdf` |
| `warhammer40k_terrain_area_footprint_imperial_world.pdf` |
| `warhammer40k_terrain_area_footprint_death_world_jungle-ou67vrxeys-0hosfodoj0.pdf` |
| `warhammer40k_terrain_area_footprint_death_world_snow-t3zsylosfg-hflqpgfj0n.pdf` |
| `warhammer40k_terrain_area_footprint_maelstrom_world.pdf` |

Full catalogue with descriptions: [`reference/Source_Library.md`](../../../reference/Source_Library.md).

---

## Setting up terrain - quick checklist

- [ ] Terrain **areas** placed and agreed first, using printed footprints where you have them
- [ ] Terrain **features** placed on those areas
- [ ] Every feature agreed out loud as Exposed, Light, or Dense
- [ ] Enough Dense terrain to break long fire lanes across the board
- [ ] Room left inside each terrain area for models to stand
- [ ] Lanes left for Monsters and Vehicles, especially near board edges
- [ ] Objectives placed, and everyone clear which terrain areas are objectives

---

## Related pages

- [`Board_Setup.md`](Board_Setup.md) - the full pre-game sequence this fits into
- [`WD527_Monthly_Mission.md`](WD527_Monthly_Mission.md) - Mission 38 footprint layout
- [`../rules/Key_Concepts.md`](../rules/Key_Concepts.md) - Objective Control and the attack sequence
- [`../rules/Keyword_Glossary.md`](../rules/Keyword_Glossary.md) - Ignores Cover, Indirect Fire, Plunging Fire, Stealth
- [`reference/Source_Library.md`](../../../reference/Source_Library.md) - every owned source and its path

---

## Games Workshop notice

**UNOFFICIAL.** This document is completely unofficial and in no way endorsed by Games Workshop Limited. Personal / no-charge use only — never for sale. Warhammer, Warhammer 40,000 and associated marks are trademarks of Games Workshop Limited. Used without permission. No challenge to their status intended. Warhammer 40,000 is Copyright Games Workshop Limited. Teaching notes by Russell Catt (Wargame Concierge). Games Workshop retains IP in the settings and characters. No official logos.

## Change Log
- v0.5.2 (2026-08-25): WD527 locked Commentary (terrain footprints; Benefit of Cover alignment) (wd527_shipping S2).
- v0.5.1 (2026-08-18): Rule-ID cites for cover/visibility (track `40k_warcom_quotes` S4).
- v0.5.0 (2026-08-18): Project-wide semver snapshot (x.y.z).
- v1.0 (2026-08-16): Initial terrain guide (slice S3), from the owned Core Rules PDF Section 13 and Event Companion v1.1, both read 2026-08-16. A4 footprint packs recorded as path pointers only.

## Attribution
- Project: Wargame_Concierge
- Maintainer: Russell Catt
- Warhammer 40,000 is a trademark of Games Workshop Limited. This document is a personal teaching paraphrase and reproduces no publisher text. The A4 footprint packs are community rescalings of Warhammer Community originals and remain outside this repository.

## Rising Tide Notes
- This document follows Rising Tide documentation standards.
- **Verify before you play.** Cross-check anything here against the current Munitorum Field Manual and your faction pack - Games Workshop patches rules and points between publications. Content on this page reflects sources read on **2026-08-16**.
