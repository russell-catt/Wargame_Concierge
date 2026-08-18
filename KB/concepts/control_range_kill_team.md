---
title: 1" Control Range (Kill Team 2024)
type: concept
system: kill_team_2024
created: 2026-08-17
updated: 2026-08-18
version: 0.5.0
sources: [kill_team_2024_core_rules, games/kill_team_2024/rules/Key_Concepts.md, games/kill_team_2024/setup/Terrain_Basics.md]
confidence: draft
tags: [concept, kill_team_2024, core_rules, control_range, markers, collision_flag]
---

# 1" Control Range (Kill Team 2024)

**Naming note.** The brief for this ingest suggested the filename `engagement_range_kill_team`, matching Warhammer 40,000's "Engagement Range" naming pattern. Kill Team 2024's actual printed term for its nearest equivalent concept is **control range** - a materially different zone with a different job. This page teaches it as **1" control range** and records the naming collision explicitly, per [`AGENTS.md`](../../AGENTS.md) Sec 9 ("never guess a rules term").

**L1 flag, then replace:** rewritten from shipping (**2026-08-18**). Volkus "ignore door for 1" control range visibility" does **not** make a non-visible target shootable — [[killzones_volkus_tomb_world]].

---

## The mechanic

**Control range** is the single most-used measurement in Kill Team. Something is within an operative's control range if it is **visible to, and within 1" of,** that operative. It is **mutual** - if A is within B's 1" control range, B is automatically within A's.

That 1" control range governs, among other things:

- **Contesting and controlling markers.** An operative contests a marker if the marker is within its 1" control range. A side **controls** a marker if the total **APL** of their operatives contesting it exceeds the opponent's total APL contesting it - not model count, and not Wounds. Control cannot change mid-action.
- **Whether cover applies.** An operative is in cover from a shooter only if there is intervening terrain within *its own* 1" control range (see [[cover_kill_team]]).
- **Fighting.** The Fight action requires an enemy operative within 1" control range; melee "assist" from supporting friendly operatives also keys off 1" control range.
- **Move restrictions.** Reposition and Dash cannot move an operative into an enemy's 1" control range (with a narrow exception when a friendly operative is already there); Charge is the action that is specifically allowed to end a move inside an enemy's 1" control range.

---

## Why it matters at the table

- **1" control range is visibility-gated, not just distance-gated.** Two operatives 6" apart with a wall between them are not within each other's 1" control range even though nothing is within 1" of anything - visibility is the first test, distance is the second.
- **Marker control is an APL race, not a body count.** A single high-APL operative contesting a marker can out-control several low-APL operatives contesting the same marker. This inverts the "numbers win" intuition a 40K-trained player might bring - see the collision note below.
- **Reposition politely avoids enemy 1" control range; Charge is the deliberate exception.** If you want to end a move next to an enemy operative without Charging, you generally cannot - Reposition and Dash are built to stop short, and only Charge (and Fall Back's narrower carve-out) is allowed to finish inside it.

---

## Kill Team vs 40K - do not conflate (collision flag)

| | Kill Team 2024 1" Control Range | Warhammer 40,000 11e Engagement Range |
|---|---|---|
| **Definition** | Visible **and** within 1" | A fixed zone of 2" horizontally and 5" vertically around a model - visibility is not part of the test |
| **What it decides** | Marker contest/control (by total APL), cover eligibility, Fight legality, move restrictions | Whether a unit is "in melee" for movement, shooting, and phase-transition purposes; a completely different, broader zone |
| **Requires visibility?** | **Yes** - not visible means not in 1" control range, regardless of distance | **No** - a purely geometric distance test |

The suggested filename for this page collided with 40K's term precisely because both games use a small radius around a model to gate melee-adjacent rules - but the KT24 mechanic (visibility-gated, 1", drives marker APL contests) and the 40K mechanic (non-visibility-gated, 2"/5", drives movement legality) are not interchangeable, and neither game calls the other's concept by the other's name. See the **1" Control Range** and **Engagement Range** entries in [[glossary]], filed side by side under this flag.

---

## Open questions

- Whether "visible" for 1" control-range purposes uses the same head-to-any-part-of-base test defined in the Visible key principle, or a simplified version at short range - Wahapedia's fragment implies the same test applies throughout, but confirm against the owned PDF.
- Killzone-specific 1" control-range modifiers (e.g. Vantage terrain height rules affecting visibility checks) - unread killzone pointers.

---

## Related pages

- [[cover_kill_team]] - cover is checked within 1" control range
- [[orders_conceal_engage]] - Conceal changes what counts as a valid target inside 1" control range
- [[valid_target]] · [[kill_team_terrain]] · [[killzones_volkus_tomb_world]]
- [[activations_apl]] - APL is both the action budget and the marker-control currency
- [[kill_team_2024_core_rules]] - source
- [[glossary]] - the 1" Control Range / Engagement Range collision flag
- [[index]]
