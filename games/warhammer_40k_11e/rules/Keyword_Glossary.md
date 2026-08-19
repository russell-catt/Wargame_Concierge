<!--
FILE: games/warhammer_40k_11e/rules/Keyword_Glossary.md
VERSION: v0.5.1 (2026-08-18)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, slice S3)

DOCUMENT_TYPE: Reference / Term Glossary
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: Warhammer 40,000 - 11th Edition
REFERENCE_STATUS: Active - draft, spot-checked against owned PDFs 2026-08-16

SOURCES:
  - C:\Personal\40K\rules\eng_01-06_warhammer40k_new40k_core_rules.pdf (read 2026-08-16)
  - C:\Personal\40K\rules\eng_22-07_warhammer_40,000_universal_rules_updates.pdf (v1.0, read 2026-08-16)
  - C:\Personal\40K\rules\eng_22-07_warhammer_40,000_faction_pack_necrons.pdf (v1.1, read 2026-08-16)
  - C:\Personal\40K\rules\eng_22-07_warhammer_40,000_event_companion-alyapl19us-b2drgwkji4.pdf (v1.1, read 2026-08-16)
  - https://wahapedia.ru/wh40k10ed/factions/necrons (retrieved 2026-08-16)
  - KB/glossary.md
  - KB/analyses/inherited_docs_for_S3.md

PURPOSE:
  At-a-glance, at-the-table reference for every rules term this project uses.
  One line of plain English per term, plus why it matters when that is not
  obvious. Grouped by the situation you will be in when you need it.

PRIMARY_AUDIENCE:
  - A player mid-game who has hit an unfamiliar keyword on a datasheet
  - Any later slice needing canonical terminology

KEY_SECTIONS_EXPECTED:
  - How to read this glossary
  - Movement and positioning
  - Shooting and weapons
  - Melee
  - Saves and damage
  - Mission and army
  - Faction pointers
  - Conflicts and deprecated terms

UPDATE_TRIGGER:
  Update when a Core Rules version, universal rules update, faction pack, or
  balance dataslate adds, renames, or changes a keyword. Mirror confirmed
  changes back into KB/glossary.md in the same pass.
-->

# Keyword Glossary - Warhammer 40,000 11th Edition

One line per term, in plain English. Weapon abilities are written the way they appear on a datasheet, in square brackets and capitals: `[BLAST]`.

Numbered Core IDs (example **13.08**) point at [`Core_Rules_Quotes.md`](Core_Rules_Quotes.md). This page stays beginner paraphrase. **40K Objective Control (OC)** is a datasheet characteristic (**14.02**); Kill Team uses **1" control range** and APL totals — not OC.

---

## How to read this glossary

Every entry carries a **status**, because 11th Edition is new and this project is honest about what it has actually checked.

| Status | Meaning |
|--------|---------|
| `verified` | Read directly in an owned 11th Edition PDF on **2026-08-16**. Safe to teach |
| `draft` | Named by a source we read, but the effect has not been cross-checked. Use the word, confirm the effect |
| `unverified` | Written from familiarity, no source read. **Confirm before you take it to a table** |

Anything not marked `verified` should be checked against your faction pack or the Warhammer 40,000 app before it decides a game.

---

## Movement and positioning

| Term | What it means | When it matters | Status |
|------|---------------|-----------------|--------|
| **Normal Move** | Move up to the unit's Move (M) characteristic. Must start and end unengaged | Your default. Preserves shooting and charging | `verified` |
| **Advance** | Roll a D6 and add it to M for extra distance | Costs you the charge and normal shooting for the turn - only `[ASSAULT]` weapons may fire | `verified` |
| **Fall Back** | Disengage from melee, moving up to M | You cannot shoot, charge, or start an action afterwards. Two modes: *Ordered Retreat* if not battle-shocked, otherwise *Desperate Escape*, which costs hazard rolls and a battle-shock roll | `verified` |
| **Remain Stationary** | Deliberately do not move | Still counts as being "selected to move". Keeps `[HEAVY]` accuracy and the better indirect-fire hit rolls | `verified` |
| **Engagement Range** | Within 2" horizontally and 5" vertically of a model | The line between "in melee" and "free". Crossing it stops you shooting normally and stops most move types | `verified` |
| **Coherency** | Every model within 2" of one squadmate and within 9" of all of them | Checked after every move and at End of Turn. Breaking it destroys models | `verified` |
| **Pile In** | A 3" move at the start of the Fight phase, toward enemies you are engaged with | Free repositioning that pulls more of your models into contact before you swing | `verified` |
| **Consolidate** | A 3" move at the end of the Fight phase | The mode is forced: stay engaged, else engage an enemy within 3", else **move onto an objective within 3"**. That last one quietly wins games | `verified` |
| **Charge Move** | The move you make after a successful charge roll | Must end engaged with every unit you nominated, or the whole charge fails | `verified` |
| **Strategic Reserves** | Units held off the table at deployment, arriving later | Capped at 50% of your points. They arrive from the second battle round, and are destroyed if still off-table at the end of the third | `verified` |
| **Ingress Move** | The move a reserve unit makes to arrive | Set up within 6" of a battlefield edge, more than 8" from all enemies, and not in the opponent's deployment zone before round three | `verified` |
| **Deep Strike** | A unit ability that changes where reserves may arrive | Lets the unit ingress **anywhere** more than 8" from enemies, including behind enemy lines | `verified` |
| **Rapid Ingress** | Core stratagem (1CP) bringing a reserve unit in at the end of the opponent's Movement phase | Arriving off-sequence, before they can react. Not usable in battle round one | `verified` |
| **Infiltrators** | Deploy anywhere more than 8" from enemies and from the enemy deployment zone | Grabs midboard positions before turn one | `verified` |
| **Scouts X"** | A free pre-battle move of X inches | Happens before the first turn, and must end more than 8" from enemies | `verified` |
| **Surge Move** | A rules-triggered move toward the closest enemy unit | Usually a reaction granted by a faction ability | `verified` |
| **Taking to the skies** | A FLY unit's option to ignore terrain and models while moving, for 2" of distance | Turns awkward terrain into a straight line | `verified` |

---

## Shooting and weapons

| Term | What it means | When it matters | Status |
|------|---------------|-----------------|--------|
| **Ballistic Skill (BS)** | The dice result a ranged attack needs to hit | Cover and Plunging Fire modify **BS**, not the save, in 11th Edition | `verified` |
| **`[RAPID FIRE X]`** | Add X extra attack dice if the target is within half range | Rewards closing the distance; a bolter genuinely doubles up | `verified` |
| **`[ASSAULT]`** | The unit may shoot with these weapons after Advancing | Lets an aggressive unit move and still contribute | `verified` |
| **`[HEAVY]`** | Add 1 to the hit roll if the unit is unengaged, did not arrive this turn, and no model moved more than 3" | Rewards standing still. Note it is a **+1 to hit**, not a movement penalty | `verified` |
| **`[CLOSE-QUARTERS]`** | The sidearm keyword. Lets a unit shoot while engaged, at the enemy it is engaged with | If a model uses one, it cannot also fire its other ranged weapons that turn | `verified` |
| **`[PISTOL]`** | **Identical to `[CLOSE-QUARTERS]` in every way.** Older wording, being phased out | Treat any Pistol weapon exactly as a Close-quarters weapon | `verified` |
| **`[TORRENT]`** | The attack hits automatically - no hit roll | Immune to hit modifiers and cover's BS penalty. Ideal against evasive targets | `verified` |
| **`[BLAST]`** | Extra attack dice scaling with target unit size - one more per five models | Punishes big blobs. **Cannot target an engaged unit at all** | `verified` |
| **`[CLEAVE X]`** | Like Blast, but for melee: X extra dice per five models, if all attacks go at one target | New in this edition. Rewards committing fully to one target | `verified` |
| **`[LETHAL HITS]`** | A critical hit (unmodified 6) may skip the wound roll and wound automatically | Optional - taking it forfeits any chance of a critical wound, so it can be wrong to use alongside `[DEVASTATING WOUNDS]` | `verified` |
| **`[SUSTAINED HITS X]`** | A critical hit generates X additional hits | Volume of attacks turns into more volume | `verified` |
| **`[DEVASTATING WOUNDS]`** | A critical wound ends the attack sequence and inflicts mortal wounds equal to the weapon's Damage | Bypasses saves entirely, but the mortals can only damage **one model per critical wound** - the rest are lost | `verified` |
| **`[IGNORES COVER]`** | The target cannot have the benefit of cover against this attack | Also beats abilities that grant cover, such as Stealth | `verified` |
| **`[TWIN-LINKED]`** | Re-roll the wound roll | Note it is the **wound** roll, not the hit roll | `verified` |
| **`[HAZARDOUS]`** | After the unit attacks, make one hazard roll per Hazardous weapon selected | On a 1-2 you take a mortal wound. Real risk on small elite units | `verified` |
| **`[INDIRECT FIRE]`** | Can shoot targets that are not visible | The trade is steep: the target gets cover, no hit re-rolls, and you only hit on a 4+ (or 6+ if you moved or nobody can see the target) | `verified` |
| **`[ANTI-X Y+]`** | Against a target with keyword X, an unmodified wound roll of Y+ is a critical wound | The specialist-killer keyword. Pairs directly with `[DEVASTATING WOUNDS]` | `verified` |
| **`[MELTA X]`** | Add X to Damage when the target is within half range | Turns a good anti-tank gun into a great one, if you can get close | `verified` |
| **`[PRECISION]`** | Lets you allocate attacks to a visible character inside a squad | The way to snipe a leader out of a bodyguard unit | `verified` |
| **`[LANCE]`** | Add 1 to wound rolls if the attacking unit charged this turn | Melee and charge-dependent despite sounding like a shooting term | `verified` |
| **`[ONE SHOT]`** | Usable once per battle | Save it | `verified` |
| **`[PSYCHIC]`** | The attack can ignore hit and BS/WS modifiers, and counts as a psychic attack | Some defences specifically counter psychic attacks | `verified` |
| **Snap shooting** | A restricted shooting mode used by Fire Overwatch: one target within 24", hits only on unmodified 6s | The core reactive shooting option | `verified` |
| **Plunging Fire** | +1 BS when shooting down at ground-level models from 3"+ of height, or as a TOWERING model within 12" | A concrete reason to climb ruins | `verified` |

---

## Melee

| Term | What it means | When it matters | Status |
|------|---------------|-----------------|--------|
| **Weapon Skill (WS)** | The dice result a melee attack needs to hit | The melee twin of BS | `verified` |
| **Charge** | Declare within 12" of an enemy, roll 2D6, move that far | You cannot charge after Advancing or Falling Back. A double 1 can never succeed | `verified` |
| **Fights First** | This unit is selected to fight before ordinary units | Automatically granted to anything that completed a charge this turn | `verified` |
| **`[EXTRA ATTACKS]`** | These attacks happen **in addition** to a model's normal melee weapon | Not a choice - you select the Extra Attacks weapon *and* a normal one | `verified` |
| **Normal Fight** | Your unit is engaged and attacks | The default | `verified` |
| **Overrun Fight** | A unit that became unengaged mid-phase gets an extra pile-in, then fights | Stops you being stranded when your target dies before you swing | `verified` |
| **Heroic Intervention** | Core stratagem (1CP) at the end of your **opponent's** Charge phase, letting one of your units charge back | Your answer to being charged. Two modes: strike back at a unit that just charged, or a shorter 6"-capped charge at anything nearby | `verified` |
| **Counter-offensive** | Core stratagem (2CP) giving one of your units Fights First and the next activation | The premium way to break your opponent's fight sequencing | `verified` |
| **Epic Challenge** | Core stratagem (1CP) giving a character's melee weapons `[PRECISION]` | Character duels | `verified` |

---

## Saves and damage

| Term | What it means | When it matters | Status |
|------|---------------|-----------------|--------|
| **Armour Save (Sv)** | A D6 roll to shrug off an attack, worsened by the weapon's AP | The default defence | `verified` |
| **Armour Penetration (AP)** | A negative modifier to the target's armour save | AP -2 makes a 3+ save behave like a 5+ | `verified` |
| **Invulnerable Save (InSv)** | An alternative save that **ignores AP entirely** | Now a profile characteristic in its own right. Defence against high-AP weapons - use whichever save is better per attack | `verified` |
| **Wounds (W)** | Damage a model absorbs before it is destroyed | Excess damage from one attack is lost, not carried to the next model | `verified` |
| **Damage (D)** | Wounds lost per attack that gets through | A D3 weapon is wasteful against 1-wound infantry | `verified` |
| **Feel No Pain X+** | Roll a D6 each time the model would lose a wound; on X+ the wound is not lost | Applies per wound, including to mortal wounds unless stated otherwise | `verified` |
| **Mortal wounds** | Damage that skips hit, wound, and save rolls | Only Feel No Pain and specific defences stop them | `verified` |
| **Hazard roll** | A D6; on a 1-2 the unit suffers a mortal wound, or 3 for a Monster/Vehicle | Triggered by Hazardous weapons, Desperate Escape, and emergency disembarks | `verified` |
| **Critical hit / critical wound** | An unmodified 6 on the hit or wound roll | Still an ordinary hit or wound, but it switches on Lethal Hits, Sustained Hits, Devastating Wounds, and Anti-X | `verified` |
| **Allocation group** | How the defender sorts a unit before taking saves | Characters cannot be placed ahead of ordinary models, which is what keeps leaders alive | `verified` |
| **Benefit of cover** (**13.08**) | Worsens the attacking weapon's **BS by 1** | This is an 11th Edition change - cover no longer improves your save. See [`../setup/Terrain_Basics.md`](../setup/Terrain_Basics.md) | `verified` |
| **Reanimation Protocols** | The Necron army rule: units heal wounds back at the end of your Command phase | See the Faction pointers section below | `verified` |
| **Deadly Demise X** | On a 6 when a model is destroyed, nearby units take X mortal wounds | Do not park your own squads next to your dying tank | `verified` |
| **Revived / returned models** | Destroyed models added back to a unit, never above starting strength | The general rule that Reanimation Protocols and resurrection abilities plug into | `verified` |

---

## Mission and army

| Term | What it means | When it matters | Status |
|------|---------------|-----------------|--------|
| **Objective Control (OC)** (**14.02**) | A profile characteristic; totals decide who controls an objective | Re-checked at the end of **every phase and turn**. Numbers of bodies beat quality. **Not** KT 1" control range | `verified` |
| **Objective / terrain objective** | The place being fought over, usually a defined terrain area | A model is in range simply by being inside that terrain area | `verified` |
| **Objective marker** | A flat 40 mm circular marker, used where an objective is not a terrain area | Range is 3" horizontally and 5" vertically | `verified` |
| **Secured** | An objective that stays yours after your models leave | Until the opponent out-controls you at the end of a phase | `verified` |
| **Battle-shock** | A failed 2D6 Leadership roll. The unit loses its OC, cannot be targeted by your stratagems, and cannot act | Tested in the Command phase for units at or below half-strength | `verified` |
| **Leadership (Ld)** | The dice result a battle-shock or leadership roll must beat, rolled on 2D6 | Presented as a dice result such as 7+ | `verified` |
| **Half-strength** | Half the models remaining, or half the wounds for a single model | The trigger for battle-shock tests | `verified` |
| **Leader** | A character ability that attaches it to a bodyguard unit | The two become one unit for all rules purposes | `verified` |
| **Support** | A second attachment slot alongside Leader | New emphasis in 11th Edition - a bodyguard unit can normally take one Leader **and** one Support | `verified` |
| **Bodyguard unit** | The squad a Leader or Support unit attaches to | Its Toughness is used for the whole attached unit | `verified` |
| **Attached unit** | The combined Leader/Support plus bodyguard | Holds every keyword of its parts, which can expose it to Anti-X weapons it would otherwise dodge | `verified` |
| **Detachment** | The rules package your list is built under, between "army" and "unit" | Supplies a detachment rule, enhancements, and stratagems. Your first real list-building decision | `verified` |
| **Detachment rule** | The army-wide ability your chosen detachment grants | Distinct from the army rule, which you get regardless | `verified` |
| **Army rule** | The faction-wide ability every list of that faction has | Reanimation Protocols for Necrons, Oath of Moment for Space Marines | `verified` |
| **Enhancement** | A points-costed upgrade attached to one character | Limited per detachment | `draft` |
| **Stratagem** | A one-off effect bought with CP, with a stated When / Target / Effect | Once per stratagem per phase, and normally one stratagem per unit per phase | `verified` |
| **Command Point (CP)** | The currency for stratagems. Both players gain 1 each Command phase | Events cap non-core CP gain at 1 per battle round | `verified` |
| **Action** | A battlefield task a unit performs instead of shooting or charging | Blocked while battle-shocked, engaged, or after Advancing | `verified` |
| **Datasheet** | The rules entry for one unit | Never reproduced in this repo - look it up in your faction pack or the app | `verified` |
| **Battleline** | The role keyword for a faction's core infantry | Necron Warriors and Immortals in this collection | `verified` |
| **Points (pts)** | What each unit costs toward your list limit | Move with every balance dataslate. Always re-check the current Munitorum Field Manual | `verified` |
| **Battle size** | Incursion, Strike Force, or Onslaught | Names confirmed in the owned Necrons Faction Pack; **the points limit for each is not stated in any owned PDF** | `draft` |
| **Victory Points (VP)** | What you actually win with | Event caps: 45 primary, 45 secondary, 10 for a painted army | `verified` |
| **No Man's Land** | The part of the table in neither deployment zone | Where most objectives - and most of the game - live | `verified` |
| **Territory** | The half of the battlefield containing a player's deployment zone | Some detachment rules key off controlling territory | `verified` |

---

## Faction pointers

Faction rules live in the army guides, not here. These entries exist so you know what the word means when you meet it.

| Term | Faction | One line | Go to | Status |
|------|---------|----------|-------|--------|
| **Reanimation Protocols** | Necrons | The army rule: at the end of your Command phase, each of your units on the battlefield heals D3 wounds | [`../armies/necrons/README.md`](../armies/necrons/README.md), [`../../../KB/concepts/reanimation_protocols.md`](../../../KB/concepts/reanimation_protocols.md) | `verified` |
| **Power Matrix** | Necrons | The Canoptek Court detachment rule. It defines which regions of the board count as your army's Power Matrix - always your deployment zone, plus No Man's Land or the enemy zone while you control at least half the objective markers there. Cryptek and Canoptek units re-roll hit rolls of 1 anywhere, and re-roll the hit roll outright while wholly inside the Matrix | [`../../../KB/concepts/power_matrix.md`](../../../KB/concepts/power_matrix.md) | `verified` |
| **Canoptek Court** | Necrons | A Necron detachment built around Canoptek constructs. Confirmed as a **Warhammer 40,000** detachment, not a Kill Team term | [`../../../KB/detachments/canoptek_court.md`](../../../KB/detachments/canoptek_court.md) | `verified` |
| **Technosorcerous Augmentations** | Necrons | The Cryptek Conclave detachment rule: Cryptek ranged weapons gain `[ASSAULT]`, and each Shooting phase a Cryptek unit picks one extra weapon ability from a short list | [`../../../KB/detachments/cryptek_conclave.md`](../../../KB/detachments/cryptek_conclave.md) | `verified` |
| **Cryptek Conclave** | Necrons | A Necron detachment built around Cryptek characters and flexible ranged buffs | [`../../../KB/detachments/cryptek_conclave.md`](../../../KB/detachments/cryptek_conclave.md) | `verified` |
| **Cryptek** | Necrons | The Necron engineer-character family - Plasmancer, Technomancer, Chronomancer, and others | Necron guide | `verified` |
| **Canoptek** | Necrons | The Necron robotic-construct family - Scarab Swarms, Wraiths, Doomstalkers, Macrocytes | Necron guide | `verified` |
| **Oath of Moment** | Space Marines | The army rule: nominate an enemy unit and your army attacks it better | [`../armies/space_marines/README.md`](../armies/space_marines/README.md), [`../../../KB/concepts/oath_of_moment.md`](../../../KB/concepts/oath_of_moment.md) | `draft` |
| **Gladius Task Force** | Space Marines | The generalist Space Marine detachment chosen as this project's learning detachment | [`../../../KB/detachments/gladius_task_force.md`](../../../KB/detachments/gladius_task_force.md) | `unverified` |

---

## Conflicts and deprecated terms

Terms this project has got wrong before, or has found a source disagreeing with. Do not propagate them.

| Do not say | Say instead | Why |
|------------|-------------|-----|
| "Scientific Schemes is the Cryptek Conclave detachment rule" | **Technosorcerous Augmentations** | Two current sources disagree with the owner's notes. The owned Necrons Faction Pack v1.1 names the rule Technosorcerous Augmentations, and "Scientific Schemes" appears **nowhere** on the Wahapedia Necrons page (retrieved 2026-08-16). Most likely an older or informal name. **Flagged for the Librarian rather than overwritten - S3 does not write `KB/`** |
| "Power Matrix might be a Kill Team term" | Power Matrix is the Canoptek Court detachment rule in Warhammer 40,000 | Corrected in slice L1; now fully confirmed against the owned faction pack FAQ and Wahapedia, both 2026-08-16 |
| "Cover improves your save" | Cover worsens the attacker's BS by 1 | 10th Edition wording. It does not work that way now |
| "Pistol is its own thing" | Pistol and Close-quarters are identical; Close-quarters is the current term | Stated explicitly in the owned Core Rules |
| "Data Package Detachment" | Say plainly which detachment is stronger, and why | Not a recognised Warhammer 40,000 term |
| "Kill Team: Tomb World is not owned / superseded" | Tomb World is **owned and game-ready** (Geomancer, 2 Tomb Crawlers, 5 Macrocytes, 10 Warriors, 3 Scarabs); prefer it for learning games | Prior "not owned" claim was erroneous; corrected on the `tomb_world_ownership` track (2026-08-16) |
| Bare "OC" on first use | "Objective Control (OC)" | Expand once, then shorthand is fine |

---

## Related pages

- [`Core_Rules_Quotes.md`](Core_Rules_Quotes.md) - numbered Core IDs
- [`Overview.md`](Overview.md) - what a game is
- [`Turn_Structure.md`](Turn_Structure.md) - when each keyword comes up
- [`Key_Concepts.md`](Key_Concepts.md) - the mechanics these terms modify
- [`../setup/Terrain_Basics.md`](../setup/Terrain_Basics.md) - cover, visibility, Hidden
- [`../../../KB/glossary.md`](../../../KB/glossary.md) - the working KB terminology surface this page draws from

---

## Change Log
- v0.5.1 (2026-08-18): Rule-ID cites; OC vs KT 1" control range flag (track `40k_warcom_quotes` S3/S4).
- v0.5.0 (2026-08-18): Project-wide semver snapshot (x.y.z).
- v1.0 (2026-08-16): Initial shipping glossary (slice S3). Terms verified against the owned Core Rules PDF, Universal Rules Updates v1.0, Necrons Faction Pack v1.1, and Event Companion v1.1, all read 2026-08-16, plus the Wahapedia Necrons page retrieved 2026-08-16. Power Matrix upgraded to `verified` with its full effect. Records a new conflict on the Cryptek Conclave detachment rule name.

## Attribution
- Project: Wargame_Concierge
- Maintainer: Russell Catt
- Warhammer 40,000 is a trademark of Games Workshop Limited. This document is a personal teaching paraphrase and reproduces no publisher text.

## Rising Tide Notes
- This document follows Rising Tide documentation standards.
- **Verify before you play.** Cross-check anything here against the current Munitorum Field Manual and your faction pack - Games Workshop patches rules and points between publications. Content on this page reflects sources read on **2026-08-16**.
