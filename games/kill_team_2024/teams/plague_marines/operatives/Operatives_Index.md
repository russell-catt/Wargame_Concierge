<!--
FILE: games/kill_team_2024/teams/plague_marines/operatives/Operatives_Index.md
VERSION: v0.5.0 (2026-08-18)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, slice S5)

DOCUMENT_TYPE: Roster Index
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: Kill Team - 2024 / 3rd Edition (KT24)
TEAM: Plague Marines
REFERENCE_STATUS: Draft — role paraphrase; statlines on HTML datacards from owned Teams PDF (2026-08-17)

SOURCES:
  - C:\Personal\Kill Team\kill_team_2024\Teams\eng_29-04_kt_teamrules_plague_marines-liggy6zl51-fa8nryqey9.pdf (datacards + Team_Rule_Guide; read in place 2026-08-17)
  - raw/pointers/kill_team_2024_teams.md
  - ../cards/*.html (verbatim statlines — see Card_Schema.md)

PURPOSE:
  Master roster table for the seven named Plague Marine operatives - role,
  base size, keywords, and a one-line paraphrase of what makes each one
  worth picking. Deliberately excludes APL / Move / Save / Wounds and
  weapon Atk / Hit / Dmg values - those are the datacard statline and are
  never reproduced in this repository.

UPDATE_TRIGGER:
  Update when the owned team-rules PDF is opened, when the Kill Team app
  revises an operative, or when S10 photo-IDs the owned models against
  this list.
-->

# Plague Marines - Operatives Index

Seven named operatives, no duplicates — your kill team can only include each of these once. **Statlines:** open the HTML datacard in [`../cards/`](../cards/Card_Schema.md). This index answers "which operative do I want for this job" in plain English.

---

## Roster table

| Operative | Datacard | Role slot | Base size | Faction keywords | Signature trait (paraphrase) | Cross-check status |
|-----------|----------|-----------|-----------|-------------------|-------------------------------|---------------------|
| **Plague Marine Champion** | [`../cards/Champion.html`](../cards/Champion.html) | Leader | 32mm | PLAGUE MARINE, CHAOS, HERETIC ASTARTES, LEADER, CHAMPION | Can heal itself off enemy operatives that carry your Poison token and take damage nearby | `verified` — Teams PDF datacard |
| **Plague Marine Bombardier** | [`../cards/Bombardier.html`](../cards/Bombardier.html) | Grenadier / support | 32mm | PLAGUE MARINE, CHAOS, HERETIC ASTARTES, BOMBARDIER | Improved grenade access and accuracy; a dedicated way to spend Blight/Krak grenades without eating into other operatives' limited uses | `verified` — Teams PDF datacard |
| **Plague Marine Fighter** | [`../cards/Fighter.html`](../cards/Fighter.html) | Melee specialist | 32mm | PLAGUE MARINE, CHAOS, HERETIC ASTARTES, FIGHTER | Has a bespoke area-melee action that hits every adjacent operative at once, friend or foe, and can spread Poison while doing it | `verified` — Teams PDF datacard |
| **Plague Marine Heavy Gunner** | [`../cards/Heavy_Gunner.html`](../cards/Heavy_Gunner.html) | Ranged fire support | 32mm | PLAGUE MARINE, CHAOS, HERETIC ASTARTES, HEAVY GUNNER | Carries the team's area-effect ranged weapon - best against clustered or approaching enemies | `verified` — Teams PDF datacard |
| **Plague Marine Icon Bearer** | [`../cards/Icon_Bearer.html`](../cards/Icon_Bearer.html) | Support / objective specialist | 32mm | PLAGUE MARINE, CHAOS, HERETIC ASTARTES, ICON BEARER | Counts as having a higher APL when contesting or controlling markers; makes the Contagion strategy ploy free while in enemy territory | `verified` — Teams PDF datacard |
| **Malignant Plaguecaster** | [`../cards/Plaguecaster.html`](../cards/Plaguecaster.html) | Psyker / support caster | 32mm | PLAGUE MARINE, CHAOS, HERETIC ASTARTES, PSYKER, MALIGNANT PLAGUECASTER | Two dedicated psychic actions - one applies Poison or punishes an already-poisoned target at range, the other heals a nearby friendly operative | `verified` — Teams PDF datacard |
| **Plague Marine Warrior** | [`../cards/Warrior.html`](../cards/Warrior.html) | Troop / generalist | 32mm | PLAGUE MARINE, CHAOS, HERETIC ASTARTES, WARRIOR | Its own defensive trait upgrades incoming defence-die results, on top of the team's shared Disgustingly Resilient | `verified` — Teams PDF datacard |

---

## Role-slot summary

| Job at the table | Best-suited operative(s) |
|-------------------|---------------------------|
| Lead / anchor | Champion |
| Apply Poison at range | Malignant Plaguecaster, Bombardier (grenades), any boltgun-armed operative with Plague Rounds equipped |
| Area denial / clustered targets | Heavy Gunner, Fighter (melee cluster) |
| Objective holding | Icon Bearer (APL bonus for control), Warrior |
| Sustain / support | Malignant Plaguecaster (healing action), Champion (Poison-fuelled self-heal) |

---

## Related pages

- [`../Team_Rule_Guide.md`](../Team_Rule_Guide.md) - the faction rules and ploys these operatives share
- [`../Starter_Roster.md`](../Starter_Roster.md) - a first-game roster built from this table
- [`../cards/Card_Schema.md`](../cards/Card_Schema.md) - seven printable HTML datacards (verbatim stats from owned Teams PDF)
- [`../README.md`](../README.md) - package entry point

---

## Change Log

- v0.5.0 (2026-08-18): Project-wide semver snapshot (x.y.z).
- v1.1 (2026-08-17): Datacard links + Teams PDF cross-check (`kt24_rules_quotes` S5).
- v1.0 (2026-08-17): Initial operatives index (slice S5) - seven operatives, role slots, base size, keywords, and paraphrased signature traits from the living Wahapedia Plague Marines page retrieved 2026-08-17. No statlines included by design.

## Attribution

- Project: Wargame_Concierge
- Maintainer: Russell Catt
- Kill Team is a trademark of Games Workshop Limited. This document is a personal teaching paraphrase and reproduces no publisher text or datacard statlines.

## Rising Tide Notes

- This document follows Rising Tide documentation standards.
- **Verify before you play.** Role paraphrases here; statlines on HTML datacards are quoted from the owned Teams PDF (2026-08-17). Cross-check Full-Scan target-eligibility quotes against your physical Core Book if needed — see [`../../rules/Target_Eligibility.md`](../../rules/Target_Eligibility.md).
