<!--
FILE: games/warhammer_40k_11e/armies/necrons/Cryptek_Conclave.md
VERSION: v0.5.0 (2026-08-18)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, slice S4; ownership corrected by Librarian, slice L2 of tomb_world_ownership; Hierotek photo ID 2026-08-17)

DOCUMENT_TYPE: Teaching Guide / Detachment
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: Warhammer 40,000 - 11th Edition
FACTION: Necrons
REFERENCE_STATUS: Active - detachment rule verified in the owned faction pack v1.1, read 2026-08-16; points verified against MFM v1.2

SOURCES:
  - C:\Personal\40K\rules\eng_22-07_warhammer_40,000_faction_pack_necrons.pdf (v1.1, Cryptek Conclave detachment, p.7-8; read 2026-08-16)
  - C:\Personal\40K\rules\Warhammer 40,000_ Munitorum Field Manual.pdf (v1.2, printed 2026-08-13; read 2026-08-16) - all points on this page
  - https://wahapedia.ru/wh40k10ed/factions/necrons (cross-check, retrieved 2026-08-16)
  - docs/handoffs/v1_scaffold/slices/S3_implementer.md Finding 2 (rule-name conflict)

PURPOSE:
  Teach the Cryptek Conclave detachment at beginner level, and correct the
  detachment rule name carried by older notes in this project.

PRIMARY_AUDIENCE:
  - A beginner choosing a first Necron detachment
  - Anyone reading older project notes that say "Scientific Schemes"

UPDATE_TRIGGER:
  Update when a faction pack version, balance dataslate, or Munitorum Field
  Manual revision changes the detachment rule, its enhancements, or their points.
-->

# Cryptek Conclave - the Technosorcerous Augmentations detachment

The Necron detachment where **Cryptek characters upgrade the guns of whoever they are standing with**, one ability at a time, every Shooting phase.

**Munitorum Field Manual v1.2 tags it:** `CRYPTEK CONCLAVE - 2DP - PRIORITY ASSETS`. As with the other detachment, "Priority Assets" is mission-type vocabulary and the `2DP` figure is not defined in any owned document - see [`Canoptek_Court.md`](Canoptek_Court.md).

---

## Name correction - read this before trusting older notes

| | |
|---|---|
| **Correct detachment rule name** | **Technosorcerous Augmentations** |
| **Wrong name still living in older project notes** | "Scientific Schemes" |
| **Source of the correction** | The owner's own Necrons Faction Pack **v1.1**, page 7, read 2026-08-16 |
| **Cross-check** | Wahapedia's Necrons page, retrieved 2026-08-16, names it identically |

"Scientific Schemes" appears nowhere in the owned faction pack and nowhere on Wahapedia. It came from the owner's pre-project blueprint notes, was flagged by slice S3, and is corrected here for shipping content.

**The KB has since caught up.** `KB/glossary.md` and `KB/detachments/cryptek_conclave.md` were renamed to Technosorcerous Augmentations in slice L2 of `tomb_world_ownership`, and "Scientific Schemes" is on the KB's deprecated list. The one place the old label still appears as a live term is [`Necron_Lists.md`](Necron_Lists.md), the imported source document, where it is preserved deliberately because that is what the source says. If you read the old name anywhere, this page wins.

---

## The detachment rule: Technosorcerous Augmentations

Two effects, both aimed at Cryptek models.

**1. Cryptek guns become mobile.** Ranged weapons on Cryptek models in your army gain `[ASSAULT]` - meaning they can still fire after the unit makes an advance move. See [`../../rules/Keyword_Glossary.md`](../../rules/Keyword_Glossary.md).

**2. Pick an upgrade every time a Cryptek unit shoots.** Each time a Cryptek unit is selected to shoot in your Shooting phase, choose **one** ability from a short menu, and every ranged weapon in that unit has it until the end of the phase. The menu is `[ANTI-INFANTRY 3+]`, `[ANTI-MOUNTED 4+]`, `[ASSAULT]`, `[HEAVY]`, and `[IGNORES COVER]`.

The second effect is the detachment. It is a **per-unit, per-phase decision**, not an army-wide buff, and choosing well is the skill the detachment teaches.

> **The keyword trick that makes it work.** "Cryptek unit" means a unit with the Cryptek keyword - and once a Cryptek character is attached to a squad of Warriors or Immortals, the whole attached unit carries that keyword. So the upgrade lands on **ten Warriors' guns**, not on the character's pistol. This is why the detachment is built around attaching characters, and why an unattached Cryptek is close to a wasted pick.

### Choosing from the menu, as a beginner

| Situation | Pick | Why |
|-----------|------|-----|
| Shooting infantry sitting in the open | `[ANTI-INFANTRY 3+]` | Wounds on a 3+ regardless of Toughness comparisons |
| Target is in cover | `[IGNORES COVER]` | Cover in 11th Edition worsens your Ballistic Skill; this cancels it |
| You advanced and still want to shoot | `[ASSAULT]` | Turns a wasted move into a full volley |
| You stood still and want more punch | `[HEAVY]` | Bonus to hit for remaining stationary |
| Facing bikes and fast skimmers | `[ANTI-MOUNTED 4+]` | The niche pick - only when the target actually has the keyword |

Default for a new player: `[IGNORES COVER]` far more often than you would guess, because most opponents will be standing in terrain.

---

## How it plays, for a beginner

**The gameplan in one line:** two blocks of infantry with a Cryptek in each, parked on objectives, shooting well and refusing to die.

- **Attach before the game.** Leaders and Support characters join their bodyguard unit during the pre-game Declare Battle Formations step - not mid-game. Decide this while writing the list.
- **A squad can take one Leader and one Support.** The owned faction pack v1.1 moved Crypteks (Chronomancer, Geomancer, Plasmancer, Psychomancer, Technomancer, Orikan) from **Leader** to **Support**, which is what makes a Cryptek plus a Royal Warden or Overlord on the same squad legal. Confirm on your own datasheets before list-building.
- **The Munitorum Field Manual tells you who can attach to whom.** Each character entry lists its legal bodyguard units - Plasmancer and Psychomancer list Immortals and Necron Warriors; the Technomancer adds Canoptek Wraiths. Check there before you plan an attachment.
- **You are not going to chase the enemy.** This army stands on objectives and out-lasts. If you find yourself moving three units per turn, you are playing the other detachment.
- **The off-turn reanimation trick.** One of the detachment's stratagems fires a unit's Reanimation Protocols during **your opponent's Command phase**, if the unit is on an objective - and a Cryptek unit reanimates one extra wound. That is a second helping of the army rule every round. See [`Reanimation_Protocols.md`](Reanimation_Protocols.md).

---

## Enhancements and stratagems

Points from **Munitorum Field Manual v1.2**; effects paraphrased from the owned faction pack v1.1.

| Enhancement | Pts | What it is for |
|-------------|-----|----------------|
| Gauntlet of Compression | 20 | Adds 6" of range to every ranged weapon in the bearer's unit - the best beginner pick, since it fixes the army's short reach |
| Gravitic Bolas | 15 | Slows and hampers a unit the bearer shot - a defensive brake on a charge you do not want |
| Quantum Abacus | 15 | A chance of CP back whenever the bearer's unit is targeted by a stratagem |
| Atomic Disintegrators | 10 | Adds anti-Monster and anti-Vehicle options to the detachment rule's menu |

The stratagems cover: ignoring hit-roll and Ballistic Skill modifiers, granting an invulnerable save to a Warriors or Immortals unit that is being shot at, punishing the killing of a Cryptek, lending the Cryptek keyword to a nearby model, picking a **second** ability from the detachment menu, and the off-turn reanimation described above. Six stratagems, all 1CP, all read off your own pack before the game.

---

## Fit with the collection (2026-08-16)

Points from **Munitorum Field Manual v1.2**; ownership from [`Owned_Models_Inventory.md`](Owned_Models_Inventory.md).

> **Ownership on this page was corrected on 2026-08-16 (slice L2, `tomb_world_ownership`).** The original v1.0 table was built against an inventory that wrongly recorded **Kill Team: Tomb World as not owned**, which is why it listed the Warriors and Scarabs as unassembled and left the owned **Cryptek Geomancer** off the table entirely.

**Game-ready today - Kill Team: Tomb World.**

| Unit | MFM v1.2 | Owned? | Note |
|------|----------|--------|------|
| Cryptek Geomancer | *not yet costed from MFM v1.2* | **Yes - game ready** | **The Cryptek this whole detachment needs.** Attach it to the Warriors and the detachment works |
| Necron Warriors (10) | **80** | **Yes - game ready** | The detachment's bread and butter, and the Geomancer's bodyguard unit |
| Canoptek Tomb Crawlers (2) | *not yet costed from MFM v1.2* | **Yes - game ready** | Screening. No Cryptek synergy, but they buy the castle time |
| Canoptek Macrocytes (5) | *not yet costed from MFM v1.2* | **Yes - game ready** | Phase 2 bodies. See the Macrocytes correction below |
| Canoptek Scarab Swarms (3) | **40** | **Yes - game ready** | Objective-grabbers; no Cryptek synergy |

**Game-ready today - Hierotek Circle (photo ID 2026-08-17).**

| Unit | MFM v1.2 | Owned? | Note |
|------|----------|--------|------|
| Technomancer | **80** first / **90** second | **Yes - game ready** | Second Cryptek (Canoptek Cloak). Attaches to Wraiths, Immortals or Warriors |
| Immortal Guardians (3) + Despotek | *see Immortals 70 for 5* | Assembled; add to sprue Immortals. Despotek defaults to Immortal; Warden is proxy-only | |
| Apprentek | — | KT-only; casual Plasmancer proxy. Not a purchased Plasmancer | |
| Hierotek Plasmacytes (2) | — | KT-legal; 40K likely not until **25–28mm base rings** | |

**Owned but on sprue - build before play.**

| Unit | MFM v1.2 | Owned? | Note |
|------|----------|--------|------|
| Necron Warriors (second 10, merging to 20) | **190** for 20 | Yes - on sprue | Merging to 20 is legal, and a 20-body block is what the rule wants |
| Immortals (5) | **70** | Yes - on sprue | Better guns, fewer bodies |
| Canoptek Scarab Swarms (second 3, merging to 6) | **80** for 6 | Yes - on sprue | Merging to 6 is legal |

**Not owned.**

| Unit | MFM v1.2 | Note |
|------|----------|------|
| Immortals (second box, merging to 10) | **140** for 10 | Merging to 10 is legal |
| Plasmancer | **55** | Cheapest Cryptek; attaches to Immortals or Warriors. **Not in Hierotek** — Apprentek is a kitchen-table proxy only. Buy for events. |
| Royal Warden | **50** | Cheap **Leader**, so it stacks with a Cryptek Support. **Not owned** — Despotek is a casual proxy (32mm). |
| Lychguard (5) | **80** | Bodyguard wall. The old note's 170 for five was badly wrong |
| Illuminor Szeras | **175** | Expensive; leave until well past 500 points |

> **Three points figures are missing on purpose.** The Geomancer, Tomb Crawlers and Macrocytes were not costed from Munitorum Field Manual v1.2, because the slice that read the MFM did so believing those models were not owned. Cost them from your own MFM before your first list.

> **Points health warning.** [`Necron_Lists.md`](Necron_Lists.md) carries stale figures - Lychguard at 170 for five (actually **80**), Warriors at 100 (actually **80**), Immortals at 75 (actually **70**), Plasmancer at 65 (actually **55**). Everything on this page was read from the owned Munitorum Field Manual v1.2 on **2026-08-16**.

**One more correction from S3, closed here.** The old notes claimed Canoptek Macrocytes grant `[IGNORES COVER]` to nearby infantry. They do not. Checked on the Macrocytes datasheet in the owned faction pack v1.1: their aura makes **enemies** less accurate near them, and their wargear can add a wound to a nearby unit's reanimation. `[IGNORES COVER]` is one of the options on **this detachment's** menu - the two rules had been run together.

---

## Should a beginner pick this detachment?

**Yes, on this collection.** The Warriors and Scarabs are painted and on a shelf, the Immortals are a box away, it forgives standing still, and it needs one cheap character rather than two expensive constructs. The owner's older notes rate it the weaker of the two detachments; over a first ten games that difference is invisible, and being able to field the list at all is not.

**And the character question is already answered.** The Tomb World **Cryptek Geomancer** is owned, painted, and identified - a real Cryptek to attach to a real squad of ten painted Warriors. Nothing here waits on anything.

> **This section used to end differently.** v1.0 said "the whole path hinges on one unanswered question: is there a Cryptek in the Hierotek Circle set?" That was a consequence of the erroneous "Tomb World not owned" claim. Photo ID 2026-08-17 added a second Cryptek — **Technomancer** — plus Immortal bodies. Apprentek is not a legal Plasmancer. See [`Starter_250.md`](Starter_250.md) and [`Owned_Models_Inventory.md`](Owned_Models_Inventory.md).

---

## Related pages

- [`Canoptek_Court.md`](Canoptek_Court.md) - the other detachment, and its territory rule
- [`Reanimation_Protocols.md`](Reanimation_Protocols.md) - the army rule this detachment doubles up on
- [`Starter_250.md`](Starter_250.md) / [`Starter_500.md`](Starter_500.md) - costed lists
- [`Owned_Models_Inventory.md`](Owned_Models_Inventory.md) - what actually exists
- [`../../rules/Keyword_Glossary.md`](../../rules/Keyword_Glossary.md) - `[ASSAULT]`, `[HEAVY]`, `[ANTI-X]`, `[IGNORES COVER]`
- [`../../rules/Key_Concepts.md`](../../rules/Key_Concepts.md) - Leaders, Support, and attached units

---

## Change Log
- v0.5.0 (2026-08-18): Project-wide semver snapshot (x.y.z).
- v1.2 (2026-08-17): Hierotek photo ID — Technomancer owned; Plasmancer remains a purchase or Apprentek proxy.
- v1.1 (2026-08-16): **Ownership correction** (slice L2, `tomb_world_ownership`). The v1.0 fit table was built on the erroneous claim that Kill Team: Tomb World was not owned: it tagged the Warriors and Scarabs "unassembled", and it omitted the owned **Cryptek Geomancer** altogether. Table split into game-ready / on-sprue / not-owned and rebuilt around the five owned Tomb World units, with Tomb Crawlers and Macrocytes added. Three units flagged as not yet costed from MFM v1.2. The beginner verdict no longer "hinges on" whether the Hierotek Circle contains a Cryptek - the owned Geomancer fills that role, and the photo ID is an upside rather than a dependency. The KB-drift note updated: `KB/` was renamed to Technosorcerous Augmentations in the same slice. No rules content changed.
- v1.0 (2026-08-16): Initial detachment teaching guide (slice S4). Detachment rule name corrected to Technosorcerous Augmentations from the owned faction pack v1.1; all points re-costed from Munitorum Field Manual v1.2; the Macrocytes `[IGNORES COVER]` claim disproved from the datasheet.

## Attribution
- Project: Wargame_Concierge
- Maintainer: Russell Catt
- Warhammer 40,000 is a trademark of Games Workshop Limited. This document is a personal teaching paraphrase and reproduces no publisher text or statlines.

## Rising Tide Notes
- This document follows Rising Tide documentation standards.
- **Verify before you play.** Cross-check anything here against the current Munitorum Field Manual and your faction pack - Games Workshop patches rules and points between publications. Content on this page reflects sources read on **2026-08-16**.
