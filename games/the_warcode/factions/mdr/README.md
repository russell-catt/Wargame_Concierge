<!--
FILE: games/the_warcode/factions/mdr/README.md
VERSION: v0.4 (2026-09-24)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, warcode_tactical_doctrine)

DOCUMENT_TYPE: Faction Overview
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: The Warcode
REFERENCE_STATUS: Active — verified roster, beta v0.8.9-F (2026-09-24)

SOURCES:
  - raw/the_warcode/The-Warcode-Rulebook-V.0.8.9-F.pdf (pp.37–38; retrieved 2026-09-24)
  - raw/the_warcode/The-Warcode-Lorebook-Tactical-Doctrine-Field-Edition.pdf (pp.5, 21, 29–34)
  - raw/the_warcode/contract_cards_transcription.txt (MDR Executive Unit column, 2026-08-25)

PURPOSE:
  Verified faction overview, lore context, and roster index for the MDR Executive Unit.

UPDATE_TRIGGER:
  A newer rulebook changes the roster, or revised lore changes MDR.
-->

# MDR Executive Unit

**Coordinated support squad** — relay Sergeant 139’s Order and melee-penetration effect through the Comms Operator while the Medic sustains a clustered formation. **`confidence: verified`**

**Unofficial personal notes.** Not endorsed by RedMakers or Gamefound.

---

## Play identity

- All eight models share A 3, M 6, and Armour 3, so positioning and support effects distinguish them.
- **Order** gives one unactivated unit +1 AP for the round; **Comms Operator** relays its reach.
- Sergeant 139 also sets nearby friendly melee penetration to −1.
- **Combat Medic** heals nearby allies at round end; **Marksman** reduces a shooting target’s Agility.
- Grenadier and Combat Medic have fixed starting equipment and cannot take other equipment.

---

## Lore and doctrine

**Academy frame:** MDR is the largest state beyond Erda by population and economic output. It is an authoritarian republic led by Martin and a clone elite; its military is composed of Martin clones differentiated by their experience after cloning. (`The-Warcode-Lorebook-Tactical-Doctrine-Field-Edition.pdf` — PDF p.29 — Section 6.)

> **Huoxing is a planet; Mars is a settlement.** MDR controls the sealed settlements of Huoxing at 1.91 AU. The year-1689 founding congress met aboard Mars, then the largest settlement in the Kirkwood Belt. They are not alternate names for one place. (Lorebook PDF pp.5, 30 — Sections 2 and 6.)

**Cassini is shared space:** the academy gives MDR only partial control of Cassini's moon system, while also recording Protagen bases on some moons. MDR's broad relationships with stations there do not erase Protagen presence or create exclusive borders. (Lorebook PDF pp.5, 25, 29 — Sections 2, 5, and 6.)

**Faction testimony:** MDR and Protagen voices say Martin was built for Dominium's war, survived a later Purification, and became the republic's defender. Martin's own intercepted transmission supplies forceful testimony, but these accounts are not independently corroborated by the academy. (Lorebook PDF pp.30–33 — Section 6, “Martin”.)

**Hostile-source doctrine:** a Dominium general assesses the Executive Unit as highly coordinated because its members share Martin lineages and are selectively cloned for roles. This helps explain the squad's identity, but it is an enemy military assessment; the playable effects still come only from the current rulebook. (Lorebook PDF p.34 — Section 6, “The Clone Weapon”.)

Shared geography and source handling: [`../../lore/Theatre_of_Operations.md`](../../lore/Theatre_of_Operations.md) and [`../../lore/Source_Methodology.md`](../../lore/Source_Methodology.md).

---

## Roster

| Unit | Role |
|---|---|
| **Sergeant 139** | Leader; Order; melee-penetration aura |
| **Grenadier** | Rifle; fixed double-grenade loadout |
| **Combat Medic** | Rifle; fixed medkit; round-end area healing |
| **Machine Gunner** | Short-range large-caliber fire |
| **Corporal** | Rifle baseline |
| **Private** | Rifle baseline |
| **Marksman** | Rifle; shooting Agility reduction |
| **Comms Operator** | Relays Sergeant effects |

Full profiles and source wording: [`Squad_Datasheet.md`](Squad_Datasheet.md).

---

## How they win

Keep the Sergeant–Comms network intact, issue Order before the chosen unit activates, and use the Medic’s six-inch heal to reward a compact formation. The source leaves several relay, equipment, and end-of-round interactions unresolved; see the datasheet and rules deep dives before play.

---

## Related pages

- [`../../rules/Contract_Cards_Reference.md`](../../rules/Contract_Cards_Reference.md)
- [`../../lore/README.md`](../../lore/README.md)
- [`../../lore/Theatre_of_Operations.md`](../../lore/Theatre_of_Operations.md)
- [`../../lore/Source_Methodology.md`](../../lore/Source_Methodology.md)
- [`Squad_Datasheet.md`](Squad_Datasheet.md)
- [`../protagen_marines/README.md`](../protagen_marines/README.md)
- [`../ulfari/README.md`](../ulfari/README.md)
- [`../dominium/README.md`](../dominium/README.md)

---

## Change Log

- v0.4 (2026-09-24): Added attributed MDR history, Huoxing/Mars distinction, Cassini overlap, and doctrine context (S3).
- v0.3 (2026-09-24): Replaced stub with verified v0.8.9-F MDR roster overview (S2).
- v0.2 (2026-08-25): Contract-card MDR Executive Unit target names from spreadsheet (S8).
- v0.1 (2026-08-23): Marketing-only stub; no stats (warcode_tactical_doctrine).

## Attribution

- Project: Wargame_Concierge
- Maintainer: Russell Catt

## Rising Tide Notes

- Rules claims use the current free rulebook; unresolved interactions remain explicit.
