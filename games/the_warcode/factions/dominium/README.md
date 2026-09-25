<!--
FILE: games/the_warcode/factions/dominium/README.md
VERSION: v0.4 (2026-09-24)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, warcode_tactical_doctrine)

DOCUMENT_TYPE: Faction Overview
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: The Warcode
REFERENCE_STATUS: Active — verified roster, beta v0.8.9-F (2026-09-24)

SOURCES:
  - raw/the_warcode/The-Warcode-Rulebook-V.0.8.9-F.pdf (pp.39–40; retrieved 2026-09-24)
  - raw/the_warcode/The-Warcode-Lorebook-Tactical-Doctrine-Field-Edition.pdf (pp.4, 13, 22–25, 35–39)
  - raw/the_warcode/contract_cards_transcription.txt (Custodia Silens column, 2026-08-25)

PURPOSE:
  Verified Dominium overview, Custodia Silens lore context, and roster index.

UPDATE_TRIGGER:
  A newer rulebook changes Custodia Silens, or revised lore changes Dominium.
-->

# Dominium — Custodia Silens

**Control-and-combination faction** — Custodia Silens mixes Agility debuffs, delayed activations, persistent damage, area fire, and extended Melee Lock. **`confidence: verified`**

**Unofficial personal notes.** Not endorsed by RedMakers or Gamefound.

---

## Play identity

- **Justiciar Julius** reduces nearby visible enemies’ Agility.
- **Confessor** gives already-activated allies delayed 1-AP activations.
- **Tormentor** supplies armour-ignoring fire plus persistent Influence and Choke damage.
- **Cremator** spreads Burning around its target; **Lancer** locks enemies within 1" without base contact.
- Punisher and Confessor cannot carry equipment or be healed by medkits.

---

## Lore and doctrine

**Academy frame:** Dominium is the theocratic empire controlling Erda, its roughly 50 billion inhabitants, orbital access, and more than one hundred subordinate states. Since year 1648 it has enforced the Blackout: isolation beyond the star system, suppression of external signals, and strict control of long-range detection. (`The-Warcode-Lorebook-Tactical-Doctrine-Field-Edition.pdf` — PDF pp.4, 22 — Sections 2 and 4.)

**Faction-authored position:** Dominium public and devotional sources portray the Father and Mother as guardians of life in a hostile cosmos. They frame obedience, isolation, and merciless enforcement as protection. This is Dominium ideology, not neutral academy judgment. (Lorebook PDF pp.13, 22, 25, 39 — Sections 3.4, 4, and 7.)

**Internal contradiction:** the Dominium first-contact file records a non-hostile encounter at Erebus-7, then treats disclosure as a threat to Blackout's legitimacy. It proposes information manipulation and orders witness elimination, evidence destruction, and forced hostility if the non-human cannot be neutralized. The file records plans and orders, not confirmed completion. (Lorebook PDF pp.35–37 — Section 7, “Internal Analysis — First Contact Event,” parts I–V.)

**Formation, not faction synonym:** Custodia Silens is an operational Dominium formation. A faction devotional source preserves its pre-deployment litany (Lorebook PDF p.25 — Section 4, “Pre-Deployment Litany, Custodia Silens”), while the internal first-contact file records the detachment order toward Erebus-7 (Lorebook PDF p.37 — Section 7, part V). Playability comes from the complete roster in **The-Warcode-Rulebook-V.0.8.9-F.pdf**, PDF pp.39–40, “Team List — Custodia Silens.” Lore never substitutes for those mechanics.

Shared chronology and source handling: [`../../lore/Historical_Timeline.md`](../../lore/Historical_Timeline.md), [`../../lore/Theatre_of_Operations.md`](../../lore/Theatre_of_Operations.md), and [`../../lore/Source_Methodology.md`](../../lore/Source_Methodology.md).

---

## Roster

| Unit | Role |
|---|---|
| **Justiciar Julius** | Leader; visible-enemy Agility debuff |
| **Assassin** | Fast; fixed double-grenade loadout |
| **Punisher** | 10-HP heavy; equipment and medkit restrictions |
| **Cremator** | Hand Flamethrower; Burning; Volt Sword |
| **Confessor** | Delayed allied reactivation |
| **Tormentor** | Directed Energy; Influence; Choke |
| **Executor** | Shotgun baseline |
| **Lancer** | Extended Melee Lock |

Full profiles and source wording: [`Squad_Datasheet.md`](Squad_Datasheet.md).

---

## Source inconsistencies

- Contract 4186 says **Justicar Julius**; the roster says **Justiciar Julius**. Preserve the spelling tied to each surface.
- Tormentor’s profile is **Directed Energy**, but one backlash sentence says **Focused Energy**.
- Hand Flamethrower prints ammo 3 and no reload cost while saying it never needs reloading.

These and the Inspiration, Overwatch, Agility-floor, end-of-round, and equipment gaps are recorded in [`Squad_Datasheet.md`](Squad_Datasheet.md); none is resolved here.

---

## Related pages

- [`../../rules/Contract_Cards_Reference.md`](../../rules/Contract_Cards_Reference.md)
- [`../../lore/README.md`](../../lore/README.md)
- [`../../lore/Historical_Timeline.md`](../../lore/Historical_Timeline.md)
- [`../../lore/Source_Methodology.md`](../../lore/Source_Methodology.md)
- [`Squad_Datasheet.md`](Squad_Datasheet.md)
- [`../mdr/README.md`](../mdr/README.md)
- [`../protagen_marines/README.md`](../protagen_marines/README.md)
- [`../../guides/Warcode_vs_That_Other_Game.md`](../../guides/Warcode_vs_That_Other_Game.md)

---

## Change Log

- v0.4 (2026-09-24): Added attributed Dominium doctrine, first-contact contradiction, and Custodia formation scope (S3).
- v0.3 (2026-09-24): Replaced stub with verified v0.8.9-F Custodia Silens overview (S2).
- v0.2 (2026-08-25): Contract-card Custodia Silens target names from spreadsheet (S8).
- v0.1 (2026-08-23): Marketing-only stub; no stats (warcode_tactical_doctrine).

## Attribution

- Project: Wargame_Concierge
- Maintainer: Russell Catt

## Rising Tide Notes

- Source contradictions are documented, not silently harmonized.
