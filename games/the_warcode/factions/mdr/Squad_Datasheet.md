<!--
FILE: games/the_warcode/factions/mdr/Squad_Datasheet.md
VERSION: v0.1 (2026-09-24)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, warcode_kickstarter_refresh S2)

DOCUMENT_TYPE: Squad Datasheet / Quoted Profiles
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: The Warcode
REFERENCE_STATUS: Active — verified, beta v0.8.9-F (2026-09-24)

SOURCES:
  - raw/the_warcode/The-Warcode-Rulebook-V.0.8.9-F.pdf (pp.37–38)
  - raw/the_warcode/rulebook_v089f_extract.txt

PURPOSE:
  Complete MDR Executive Unit roster with current-PDF profile and ability cites.
-->

# MDR Executive Unit — squad datasheet

**`confidence: verified`** against **The-Warcode-Rulebook-V.0.8.9-F.pdf**, PDF pages **37–38**, section **“MDR EXECUTIVE UNIT — TEAM LIST.”**

**Profile key:** ranged = Shots · Range · Ammo · Shoot AP · Reload AP · Pen · Damage/Critical. Melee = Strength · Range · AP · Pen · Damage/Critical.

## Shared profiles

| Weapon | Profile |
|---|---|
| Rifle | 3 · 7" · 2 · 1 AP · 1 AP · 0 · 2/3 |
| Bayonet | 3 · 1" · 1 AP · 0 · 2/3 |
| Combat Knife | 2 · 1" · 1 AP · 0 · 2/3 |

Source: **The-Warcode-Rulebook-V.0.8.9-F.pdf — pp.37–38 — “MDR EXECUTIVE UNIT — TEAM LIST.”**

## Sergeant 139

**Core:** HP 9 · A 3 · M 6 · Armour 3
**Large-Caliber Pistol:** 5 · 6" · 2 · 1 AP · 1 AP · −1 · 1/2
**Volt Sword:** 4 · 1" · 1 AP · 0 · 2/3; re-roll armour-penetration dice showing 1 until higher.

- **Leader:** gain 2 re-roll points at the start of each round.
- **Order:** once per round, spend 1 AP to give a friendly, not-yet-activated unit within 7" +1 AP until round end. Place an order token. Cannot be used in melee.
- Friendly units within 7" improve melee penetration **to −1**.
- The Comms Operator can extend both ranges.

Source: **The-Warcode-Rulebook-V.0.8.9-F.pdf — p.37 — “MDR EXECUTIVE UNIT — TEAM LIST” (Sergeant 139).**

**Source gap:** “to −1” reads as setting the value, but does not explain already-better profiles or whether Sergeant 139 affects himself.

## Grenadier

**Core:** HP 8 · A 3 · M 6 · Armour 3
**Weapons:** Rifle; Bayonet.

Starts with **2 grenades** and cannot take other equipment.

Source: **The-Warcode-Rulebook-V.0.8.9-F.pdf — p.37 — “MDR EXECUTIVE UNIT — TEAM LIST” (Grenadier).**

## Combat Medic

**Core:** HP 8 · A 3 · M 6 · Armour 3
**Weapons:** Rifle; Bayonet.

Starts with **1 medkit** and cannot take other equipment. At round end, restores 1 HP to every friendly unit within 6"; does not heal itself and the ability is disabled while the Medic is in melee.

Source: **The-Warcode-Rulebook-V.0.8.9-F.pdf — p.37 — “MDR EXECUTIVE UNIT — TEAM LIST” (Combat Medic).**

## Machine Gunner

**Core:** HP 8 · A 3 · M 6 · Armour 3
**Large-Caliber Machine Gun:** 2 · 6" · 3 · 1 AP · 1 AP · −1 · 3/4
**Melee:** Combat Knife.

Source: **The-Warcode-Rulebook-V.0.8.9-F.pdf — p.37 — “MDR EXECUTIVE UNIT — TEAM LIST” (Machine Gunner).**

## Corporal

**Core:** HP 8 · A 3 · M 6 · Armour 3
**Weapons:** Rifle; Bayonet.

Source: **The-Warcode-Rulebook-V.0.8.9-F.pdf — p.38 — “MDR EXECUTIVE UNIT — TEAM LIST” (Corporal).**

## Private

**Core:** HP 8 · A 3 · M 6 · Armour 3
**Weapons:** Rifle; Bayonet.

Source: **The-Warcode-Rulebook-V.0.8.9-F.pdf — p.38 — “MDR EXECUTIVE UNIT — TEAM LIST” (Private).**

## Marksman

**Core:** HP 8 · A 3 · M 6 · Armour 3
**Weapons:** Rifle; Bayonet.

**Sniper:** when Marksman shoots, reduce the target’s Agility by 1.

Source: **The-Warcode-Rulebook-V.0.8.9-F.pdf — p.38 — “MDR EXECUTIVE UNIT — TEAM LIST” (Marksman).**

## Comms Operator

**Core:** HP 8 · A 3 · M 6 · Armour 3
**Weapons:** Rifle; Bayonet.

While within 7" of Sergeant 139, eligible friendly units within 7" of the Comms Operator can receive the Sergeant’s Order and melee-penetration effect.

Source: **The-Warcode-Rulebook-V.0.8.9-F.pdf — p.38 — “MDR EXECUTIVE UNIT — TEAM LIST” (Comms Operator).**

**Source gaps:** no line of sight is required for the relay, and the book does not state what happens if the Sergeant is destroyed.

## Equipment ambiguities

The book does not resolve whether Grenadier’s permanent “cannot take other equipment” restriction ends after both grenades are spent, how two carried grenades drop, or whether a partly spent load still blocks pickup. Use a table agreement; do not treat this sheet as a ruling.

## Related pages

- [`README.md`](README.md)
- [`../../rules/Activation_and_AP.md`](../../rules/Activation_and_AP.md)
- [`../../rules/Equipment_Loot_and_Doors.md`](../../rules/Equipment_Loot_and_Doors.md)
- [`../../rules/Rulebook_Quotes.md`](../../rules/Rulebook_Quotes.md)

## Change Log

- v0.1 (2026-09-24): Added verified v0.8.9-F roster and preserved profile interaction gaps (S2).

## Attribution

- Project: Wargame_Concierge
- Maintainer: Russell Catt
- The Warcode is property of RedMakers. Unofficial personal learning notes.
