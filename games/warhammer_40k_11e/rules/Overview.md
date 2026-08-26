<!--
FILE: games/warhammer_40k_11e/rules/Overview.md
VERSION: v0.5.2 (2026-08-25)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, wd527_shipping S3; prior S2 tomb_world_ownership)

DOCUMENT_TYPE: Teaching Guide / Beginner Overview
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: Warhammer 40,000 - 11th Edition
REFERENCE_STATUS: Active - draft, spot-checked against owned PDFs 2026-08-16

SOURCES:
  - C:\Personal\40K\rules\eng_01-06_warhammer40k_new40k_core_rules.pdf (read 2026-08-16)
  - C:\Personal\40K\rules\eng_22-07_warhammer_40,000_event_companion-alyapl19us-b2drgwkji4.pdf (Version 1.1, read 2026-08-16)
  - C:\Personal\40K\rules\Warhammer 40,000_ Munitorum Field Manual.pdf (v1.2, read 2026-08-16)
  - reference/Source_Library.md
  - KB/analyses/inherited_docs_for_S3.md
  - games/warhammer_40k_11e/armies/necrons/Owned_Models_Inventory.md (ownership, corrected 2026-08-16)

PURPOSE:
  Answer "what actually happens in a game of Warhammer 40,000?" for someone who
  has never played. Covers the shape of a game, how you win, what an army is
  made of, and what you need on the table.

PRIMARY_AUDIENCE:
  - Parent and son learning 11th Edition together, from zero
  - Later sessions needing the shared vocabulary before army content

KEY_SECTIONS_EXPECTED:
  - What a game is
  - The shape of a game
  - How you win
  - What an army is made of
  - What you need to play
  - Your realistic first game

UPDATE_TRIGGER:
  Update when a new Core Rules version, Munitorum Field Manual, Event Companion,
  or balance dataslate changes battle sizes, scoring caps, or board size.
-->

# Overview - what a game of Warhammer 40,000 is

Everything below is written in plain language for a first-time player. Nothing here is copied from Games Workshop text; it is our own explanation of how the game works, checked against the owned Core Rules PDF on **2026-08-16**. Numbered IDs such as **01.01** point at [`Core_Rules_Quotes.md`](Core_Rules_Quotes.md).

**Contradiction check (2026-08-18):** the 2026-08-16 paraphrase was re-read against Core IDs **01.01**, **07.01–07.03**, **08.02**, and Event Companion board size. No rewrite required. Event non-Core CP cap (1 per battle round) was already in [`Keyword_Glossary.md`](Keyword_Glossary.md); Core **08.02** is still “both players gain 1 Core CP.”

---

## What a game actually is

Two players each command an **army** of miniatures (**01.01**). You take turns moving those models around a table dressed with scenery, shooting at each other, and fighting hand-to-hand. Dice decide whether attacks land and whether they hurt.

The single most important thing a beginner gets wrong: **you do not win by killing the most models.** You win by scoring **victory points (VP)**, and most VP come from standing on the right pieces of ground at the right moment. Killing things is a means to that end, not the end itself.

A game is a self-contained story that runs for **five battle rounds** and then stops, whether or not either army has been wiped out. If you have no models left, you still play out your remaining turns.

---

## The shape of a game

The game is built out of nested pieces. Learn these four words and the structure stops being confusing.

| Piece | What it is |
|-------|-----------|
| **Battle** | The whole game. Normally five battle rounds long. |
| **Battle round** (**07.01–07.03**) | One full cycle in which **both** players take a turn. Same player always goes first each round. |
| **Turn** | One player's go. Contains a Start of Turn step, five phases, and an End of Turn step. |
| **Phase** | One kind of activity - marshalling, moving, shooting, charging, fighting. |

The five phases always happen in the same order:

1. **Command** (**08**) - both players gain 1 Core Command Point (CP) (**08.02**); you check morale (battle-shock) on your shaky units (**08.03**, **01.07**).
2. **Movement** (**09**) - you move every unit, and reinforcements arrive from reserves.
3. **Shooting** (**10**) - your units fire ranged weapons.
4. **Charge** (**11**) - your units run into contact with the enemy.
5. **Fight** (**12**) - **both** players' units swing melee weapons. This is the only phase where your opponent acts during your turn.

The full step-by-step checklist lives in [`Turn_Structure.md`](Turn_Structure.md).

---

## How you win

Victory points are counted up at the end, and the higher total wins. A tie is a draw.

Under the tournament framework in the owned Event Companion (Version 1.1), VP come from three places, each capped:

| Source of VP | Cap | How it works |
|--------------|-----|--------------|
| **Primary Mission** | 45VP | Up to 15VP per battle round, almost always for controlling objectives |
| **Secondary Missions** | 45VP | Up to 15VP per battle round, from mission cards you hold |
| **Battle Ready army** | 10VP | A flat bonus for having your army painted to a basic standard |

That is a 100VP ceiling, and **90 of those 100 points come from doing things on the board rather than from destroying the enemy.** Casual pick-up games do not have to use the event caps, but the shape is the same: objectives first.

Objectives are usually **terrain footprints** (**14.01**). You **control** one by having a higher total **Objective Control (OC)** from models inside that footprint than your opponent (**14.02**) — then the **mission card** says when you score VP for that control. See [`Key_Concepts.md`](Key_Concepts.md). This is why ten cheap infantry models can beat one expensive tank at the thing that actually scores.

---

## What an army is made of

Building a list is four decisions stacked on top of each other.

| Layer | What you choose | Where the rules live |
|-------|-----------------|---------------------|
| **Army faction** | Necrons, Space Marines, and so on. Fixes your **army rule** - a faction-wide ability every unit gets. | Faction pack / Codex |
| **Detachment** | A rules package inside your faction. Gives a **detachment rule** plus its own enhancements and stratagems. | Faction pack / Codex |
| **Units** | The actual squads and vehicles. Each has a **datasheet** listing its profile, weapons, abilities, and keywords. | Faction pack / app |
| **Points** | Every unit costs points. Your list must fit the agreed limit. | Munitorum Field Manual |

The two army rules in this project:

- **Necrons - Reanimation Protocols.** At the end of your Command phase, your units heal wounds back. Damage that fails to finish a unit tends to get undone. *(Confirmed in the owned Necrons Faction Pack v1.1, read 2026-08-16.)*
- **Space Marines - Oath of Moment.** You nominate an enemy unit each turn and your army attacks it better, which makes target priority the defining Space Marine decision. *(Named in the owned Space Marines Faction Pack; exact wording not yet transcribed - S5 owns this.)*

### Battle sizes

Games are played at named sizes. The owned Necrons Faction Pack references three by name:

| Battle size | Typical use |
|-------------|-------------|
| **Incursion** | Small games |
| **Strike Force** | The standard event and matched-play size |
| **Onslaught** | Large games |

> **Not verified:** the exact points limit attached to each size is set by the mission material and the Warhammer 40,000 app, and is **not stated in any PDF this project owns**. The commonly quoted figures are 1,000 / 2,000 / 3,000 points, but treat that as hearsay until checked. There is also a smaller **Combat Patrol** format, which the owned A4 terrain pack has a dedicated battlezone layout for.

For learning games, ignore all of this and agree a small number with your opponent. A few hundred points a side is plenty for a first game.

---

## What you need to play

| Thing | Detail |
|-------|--------|
| **Models** | Assembled miniatures for both armies |
| **A table** | Events use a rectangle **44" by 60"**. Smaller is fine for learning games |
| **Terrain** | Scenery, arranged in defined **terrain areas**. See [`../setup/Terrain_Basics.md`](../setup/Terrain_Basics.md) |
| **Dice** | A handful of six-sided dice (D6). Twenty or more saves a lot of re-rolling |
| **Tape measure** | Everything is measured in inches, and you may measure whenever you like |
| **A mission** | Tells you the deployment map, the objectives, and how VP are scored. Learning default: [`../setup/WD527_Monthly_Mission.md`](../setup/WD527_Monthly_Mission.md) (**Mission 38 — Converging Ambition**) |
| **Objective markers** | Flat circular markers, 40 mm across, where an objective is not already a piece of terrain |
| **Your rules** | Datasheets and points for your army |
| **Table aids** | Wound chart [`Wound_Roll_Reference.md`](Wound_Roll_Reference.md); system Letter 2-pager [`../setup/print/40k_system_quick_reference.html`](../setup/print/40k_system_quick_reference.html) (S4 ships the HTML) |

Board setup, deployment, and the pre-game checklist are in [`../setup/Board_Setup.md`](../setup/Board_Setup.md).

**Trust ladder:** tier **1** = Core / Event Companion / Chapter Approved (mechanics win); tier **1.5** = owned WD527 commentary and Mission 38 (`C:\Personal\40K\WD_527\`). See system [`../README.md`](../README.md) and shipping track [`docs/handoffs/wd527_research/track_shipping_in.md`](../../../docs/handoffs/wd527_research/track_shipping_in.md).

---

## Your realistic first game

This project has a specific collection behind it, and it constrains what a first game can look like.

- **The Kill Team: Tomb World force is game-ready today.** The Cryptek Geomancer, 2x Canoptek Tomb Crawlers, 5x Canoptek Macrocytes, 10x Necron Warriors, and 3x Canoptek Scarab Swarms are all assembled and painted - this is the preferred learning baseline. See [`../armies/necrons/Owned_Models_Inventory.md`](../armies/necrons/Owned_Models_Inventory.md).
- The **Hierotek Circle** set is assembled, painted, and **photo-IDed** (Technomancer, Immortals, Despotek, Apprentek, Plasmacytes). See [`../armies/necrons/Owned_Models_Inventory.md`](../armies/necrons/Owned_Models_Inventory.md) for legal datasheets vs kitchen-table proxies. It does not block playing Tomb World.
- A second Necron Warriors squad (10), a second Canoptek Scarab Swarms set (3), and a squad of Immortals (5) are owned but **unassembled** - build these to expand past the Tomb World force at larger points values.
- The Space Marine collection has not been audited yet.

A sensible learning path: read this page and [`Turn_Structure.md`](Turn_Structure.md), keep [`Wound_Roll_Reference.md`](Wound_Roll_Reference.md) at the table, then play a tiny game with two or three units per side and **no secondary missions** - just move, shoot, fight, and count OC on one objective. Add **Mission 38** ([`../setup/WD527_Monthly_Mission.md`](../setup/WD527_Monthly_Mission.md)) once the sequence feels automatic.

---

## Where to check anything here

| Question | Check |
|----------|-------|
| Core rules mechanics | `C:\Personal\40K\rules\eng_01-06_warhammer40k_new40k_core_rules.pdf` |
| Rules that changed after release | `C:\Personal\40K\rules\eng_22-07_warhammer_40,000_universal_rules_updates.pdf` |
| Board size, mission sequence, scoring caps | `C:\Personal\40K\rules\eng_22-07_warhammer_40,000_event_companion-alyapl19us-b2drgwkji4.pdf` |
| Points | `C:\Personal\40K\rules\Warhammer 40,000_ Munitorum Field Manual.pdf` |
| Everything, when in doubt | [`reference/Source_Library.md`](../../../reference/Source_Library.md) |

---

## Related pages

- [`Turn_Structure.md`](Turn_Structure.md) - the phase-by-phase checklist
- [`Key_Concepts.md`](Key_Concepts.md) - attacks, saves, objectives, morale
- [`Wound_Roll_Reference.md`](Wound_Roll_Reference.md) - S vs T wound matrix (Core **05.02**) + print laminate
- [`Keyword_Glossary.md`](Keyword_Glossary.md) - every term in one place
- [`../setup/Board_Setup.md`](../setup/Board_Setup.md) - table, deployment, objectives
- [`../setup/Terrain_Basics.md`](../setup/Terrain_Basics.md) - terrain categories and how much you need
- [`../setup/WD527_Monthly_Mission.md`](../setup/WD527_Monthly_Mission.md) - **Mission 38 — Converging Ambition**
- [`../setup/print/40k_system_quick_reference.html`](../setup/print/40k_system_quick_reference.html) - system Letter 2-pager (phases + attack sequence; S4 owns HTML body)
- [`../README.md`](../README.md) - subtree entry + trust ladder / WD527 provenance

---

## Games Workshop notice

**UNOFFICIAL.** This document is completely unofficial and in no way endorsed by Games Workshop Limited. Personal / no-charge use only — never for sale. Warhammer, Warhammer 40,000 and associated marks are trademarks of Games Workshop Limited. Used without permission. No challenge to their status intended. Warhammer 40,000 is Copyright Games Workshop Limited. Teaching notes by Russell Catt (Wargame Concierge). Games Workshop retains IP in the settings and characters. No official logos.

## Change Log
- v0.5.2 (2026-08-25): Cross-links — Mission 38, wound chart, system QR path, trust ladder (wd527_shipping S3). Teaching body unchanged.
- v0.5.1 (2026-08-18): Rule-ID cites; no paraphrase rewrite (track `40k_warcom_quotes` S3).
- v0.5.0 (2026-08-18): Project-wide semver snapshot (x.y.z).
- v1.1 (2026-08-16): Corrected "Your realistic first game" - Kill Team: Tomb World is owned and game-ready (preferred learning baseline), not just the Hierotek Circle set. Removed the "only Hierotek is table-ready" claim; flagged the second Warriors squad, second Scarab set, and Immortals as owned/unassembled (slice S2, `tomb_world_ownership`).
- v1.0 (2026-08-16): Initial teaching overview (slice S3). Written from the owned Core Rules PDF and Event Companion v1.1, both read 2026-08-16.

## Attribution
- Project: Wargame_Concierge
- Maintainer: Russell Catt
- Warhammer 40,000 is a trademark of Games Workshop Limited. This document is a personal teaching paraphrase and reproduces no publisher text.

## Rising Tide Notes
- This document follows Rising Tide documentation standards.
- **Verify before you play.** Cross-check anything here against the current Munitorum Field Manual and your faction pack - Games Workshop patches rules and points between publications. Content on this page reflects sources read on **2026-08-16**.
