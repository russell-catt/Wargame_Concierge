<!--
FILE: games/kill_team_2024/rules/Keyword_Glossary.md
VERSION: v1.0 (2026-08-17)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, slice S1)

DOCUMENT_TYPE: Reference / Term Glossary
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: Kill Team - 2024 / 3rd Edition (KT24)
REFERENCE_STATUS: Draft - written from the living Wahapedia core rules and Approved Ops 2025 pages; not yet cross-checked against the owned Core Rules PDF

SOURCES:
  - raw/pointers/kill_team_2024_core.md (points at C:\Personal\Kill Team\kill_team_2024\779937548-Core-Rules-KILL-TEAM-3E-Full-Scan.pdf - not yet opened this slice)
  - https://wahapedia.ru/kill-team3/the-rules/core-rules/ (retrieved 2026-08-17)
  - https://wahapedia.ru/kill-team3/the-rules/approved-ops-2025/ (retrieved 2026-08-17)
  - https://wahapedia.ru/kill-team3/the-rules/tac-ops/ (retrieved 2026-08-17)
  - games/warhammer_40k_11e/rules/Keyword_Glossary.md (for 40K collision checks)
  - KB/glossary.md (Kill Team 2024 section) and KB/sources/kill_team_2024_core_rules.md (Librarian L1, landed in parallel with this slice - same living source, same collision flags, cross-checked as consistent)

PURPOSE:
  At-a-glance reference for every Kill Team rules term this project uses.
  One line of plain English per term, grouped by situation, with explicit
  flags where a term collides with a different Warhammer 40,000 meaning.

PRIMARY_AUDIENCE:
  - A player mid-game who has hit an unfamiliar term on a datacard
  - A 40K player who needs to know which familiar-sounding words mean
    something different here
  - Any later slice needing canonical Kill Team terminology

KEY_SECTIONS_EXPECTED:
  - How to read this glossary
  - Phase and activation
  - Movement and positioning
  - Shooting and fighting
  - Damage and operative state
  - Mission and scoring
  - Team, equipment, and rules
  - Collisions with 40K vocabulary

UPDATE_TRIGGER:
  Update when a new Core Rules printing, Approved Ops pack, or errata adds,
  renames, or changes a term. Cross-check against KB/glossary.md once L1
  ingests the Kill Team core rules, and mirror confirmed changes there.
-->

# Keyword Glossary - Kill Team 2024 / 3rd Edition

One line per term, in plain English, grouped by the situation you'll be in when you need it.

---

## How to read this glossary

Every entry carries a **status**, because this slice has read the living Wahapedia core rules pages but has **not yet opened the owned Core Rules PDF**.

| Status | Meaning |
|--------|---------|
| `draft` | Named and explained from a source read this slice (Wahapedia, retrieved **2026-08-17**), but not yet cross-checked against the owned PDF |
| `unverified` | Written from general familiarity, not directly confirmed by any source read this slice |

There are no `verified` entries yet. Every term here should be confirmed against `C:\Personal\Kill Team\kill_team_2024\779937548-Core-Rules-KILL-TEAM-3E-Full-Scan.pdf` before it settles an argument at the table.

**Cross-checked against the KB.** The Librarian's L1 pass landed [`KB/glossary.md`](../../../KB/glossary.md) (Kill Team 2024 section) and six concept pages in parallel with this slice, reading the same living Wahapedia source. The two independently arrived at the same status (`draft`, nothing `verified`) and the same collision flags. Where a KB concept page exists, its entry below links to it directly.

---

## Phase and activation

| Term | What it means | When it matters | Status |
|------|---------------|-----------------|--------|
| **Turning point** | One full round: Strategy phase, then Firefight phase | The battle's basic unit of time - four per battle under Approved Ops 2025. KB: [`turning_points`](../../../KB/concepts/turning_points.md) | `draft` |
| **Strategy phase** | The setup step of a turning point: Initiative, Ready, Gambit | Where CP is gained and strategy ploys are played | `draft` |
| **Firefight phase** | The activation step: players alternate activating operatives until both sides are expended | Where all movement, shooting, and fighting actually happens | `draft` |
| **Initiative** | Who acts first, and who resolves simultaneous timing | Decided by roll-off from the second turning point on, with a tie going to whoever lacked initiative last turn | `draft` |
| **Ready** | The Strategy phase step where CP is gained and operatives are readied | Also the name of an operative's activatable state (see Order tokens) | `draft` |
| **Gambit** | The Strategy phase step where STRATEGIC GAMBITs (usually strategy ploys) are used | Alternates player to player; ends when both pass in a row | `draft` |
| **STRATEGIC GAMBIT** | A keyword marking a rule usable in the Gambit step | Strategy ploys are the most common, but not the only, example | `draft` |
| **Ploy (strategy / firefight)** | A CP-bought rules effect, split by which phase it's used in | Strategy ploys in the Gambit step; Firefight ploys any time in the Firefight phase | `draft` |
| **Command Point (CP)** | Currency spent on ploys | 1 CP per player in turning point one; from turning point two, the player **without** initiative gets 2 CP | `draft` |
| **Activation** | One operative's full turn: order, then actions, then Expended | The basic decision-making unit of the Firefight phase | `draft` |
| **APL (Action Point Limit)** | The AP an operative can spend in one activation | Net APL changes from all sources are capped at ±1 from normal. KB: [`activations_apl`](../../../KB/concepts/activations_apl.md) | `draft` |
| **AP (Action Points)** | The cost of each action | Cannot exceed the operative's APL for that activation; minimum action cost is always 0 | `draft` |
| **Action** | A thing an operative does during activation - universal, unique, mission, or free | Cannot repeat the same action twice in one activation (with named exceptions) | `draft` |
| **Free action** | An action performed only when another rule grants it, at no AP cost | Still counts as "having performed that action" for other rules | `draft` |
| **Expended** | An operative's state after finishing its activation | Cannot act again this turning point except via Counteract | `draft` |
| **Counteract** | A free 1AP action for an expended, Engage-order operative, usable only once your side has no ready operatives left | Not an activation - action restrictions from its earlier activation do not apply | `draft` |
| **Roll-off** | Both players roll one D6; higher wins, re-roll ties | Used for initiative and other head-to-head decisions | `draft` |

---

## Movement and positioning

| Term | What it means | When it matters | Status |
|------|---------------|-----------------|--------|
| **Reposition** | 1AP: move up to the operative's Move stat, in straight-line increments | The default move; cannot start within control range of an enemy | `draft` |
| **Dash** | 1AP: move up to 3" regardless of Move stat, no climbing | Cannot be used in the same activation as Charge | `draft` |
| **Fall Back** | 2AP: move away while starting within an enemy's control range | The only move that's allowed to start engaged; expensive at 2AP | `draft` |
| **Charge** | 1AP: Reposition plus an extra 2", must end within control range of an enemy | Not usable on a Conceal order, or if already in an enemy's control range | `draft` |
| **Control range** | Visible to, and within 1" of, an operative - mutual between both operatives | Gates Fight eligibility, cover, obscured, and marker control. KB: [`control_range_kill_team`](../../../KB/concepts/control_range_kill_team.md) | `draft` |
| **Visible** | An unobstructed 1mm-wide line from the operative's head to any part of the target's miniature | The basis for valid targets and for control range | `draft` |
| **Base** | The physical base a miniature stands on; used for all distance measuring | Bases can touch but never stack; friendly bases can pass through each other, enemy bases cannot | `draft` |
| **Climbing** | Moving up terrain within 1" horizontally / 3" vertically of it | Each climb counts as a minimum 2" vertical distance | `draft` |
| **Dropping** | Moving down off terrain, or after jumping | First 2" of any drop in an action is ignored | `draft` |
| **Jumping** | Leaving Vantage terrain higher than 2" from the killzone floor | Up to 4" horizontal distance, in one straight-line increment | `draft` |
| **Killzone floor** | The lowest level of the board | Anything on a marker that's on the floor is also treated as on the floor | `draft` |

---

## Shooting and fighting

| Term | What it means | When it matters | Status |
|------|---------------|-----------------|--------|
| **Shoot** | 1AP action: attacker rolls attack dice, defender rolls defence dice, successes resolve | Cannot be performed on a Conceal order, or while in an enemy's control range | `draft` |
| **Fight** | 1AP action: both operatives roll and alternate resolving successes | Requires an enemy operative already within control range | `draft` |
| **Atk / Hit / Dmg** | Weapon stats: attack dice rolled, result needed to succeed, damage per normal/critical success | Read straight off the datacard - never reproduced here | `draft` |
| **Attack dice** | Dice rolled by the attacker in Shoot or Fight | One D6 per the weapon's Atk stat | `draft` |
| **Defence dice** | Dice rolled by the defender when shot | Three D6, minus one replaced by a free success if the target is in cover | `draft` |
| **Normal success** | An attack or defence die meeting or beating its target number | Blocks, or is blocked by, another normal success | `draft` |
| **Critical success** | An unmodified roll of 6 | Two normal successes are needed to block one critical success | `draft` |
| **Valid target** | An Engage operative that's visible, or a Conceal operative that's visible **and not in cover** | Checked before a Shoot action can even be declared | `draft` |
| **Cover** | Intervening terrain within the target's own control range (and target more than 2" from the shooter) | Removes Conceal targets from being valid at all; grants Engage targets a free "cover save" success. KB: [`cover_kill_team`](../../../KB/concepts/cover_kill_team.md) | `draft` |
| **Cover save** | The one free retained normal defence success granted by cover | Only applies to operatives that are in cover; rolled dice still follow after it | `draft` |
| **Obscured** | Intervening Heavy terrain more than 1" from both operatives | Forces the attacker to discard one success and caps the rest at normal (no criticals). KB: [`cover_kill_team`](../../../KB/concepts/cover_kill_team.md) | `draft` |
| **Intervening** | Terrain that lies between two operatives, checked via targeting/visibility lines when unclear | The basis for both cover and obscured | `draft` |
| **Blast X** | A weapon rule: after the primary target, shoot again at each other operative within X of it | Secondary targets are valid regardless of order; resolved as separate Shoot sequences | `draft` |
| **Torrent X** | A weapon rule: shoot the primary target and any other valid targets within X of it that aren't near friendly operatives | Similar to Blast but with its own targeting restriction | `draft` |
| **Guard** | 1AP action treated as a Shoot action; sets the operative on guard until it acts, is targeted nearby, or the turning point ends | Not usable on Conceal or while in an enemy's control range | `draft` |

---

## Damage and operative state

| Term | What it means | When it matters | Status |
|------|---------------|-----------------|--------|
| **Wounds** | An operative's starting hit points, from its datacard | Reduced by damage; at 0 or below the operative is incapacitated | `draft` |
| **Damage** | Wounds lost from a successful, unblocked attack | Normal Dmg for a normal success, Critical Dmg for a critical success | `draft` |
| **Wounded** | Has fewer than its starting Wounds remaining | The lighter of the two damage-state thresholds | `draft` |
| **Injured** | Has fewer than **half** its starting Wounds remaining | -2" Move, and its weapons' Hit stat worsens by 1. KB: [`injured_operatives`](../../../KB/concepts/injured_operatives.md) | `draft` |
| **Incapacitated** | Reduced to 0 or fewer Wounds | Removed from the killzone; some rules grant one free action first | `draft` |
| **Save** | The datacard stat used for defence dice | Read directly off the datacard; a lower number is better | `draft` |
| **Order (Conceal / Engage)** | The two activation stances an operative can be set to | Chosen fresh at the start of each activation; see [`Key_Concepts.md`](Key_Concepts.md). KB: [`orders_conceal_engage`](../../../KB/concepts/orders_conceal_engage.md) | `draft` |

---

## Mission and scoring

| Term | What it means | When it matters | Status |
|------|---------------|-----------------|--------|
| **Victory Points (VP)** | What decides the winner | Scored from ops; most VP is not from kills alone | `draft` |
| **Crit Op** | Approved Ops 2025 op: score for mission actions and controlling objective markers | Capped at 6VP | `draft` |
| **Kill Op** | Approved Ops 2025 op: score for incapacitating enemy operatives | Capped at 6VP; not the only way to score from kills, and not the whole game | `draft` |
| **Tac Op** | Approved Ops 2025 op: a secretly-chosen secondary objective from your kill team's archetype | Capped at 6VP; revealed on its own stated trigger | `draft` |
| **Primary op** | Whichever of the three ops a player secretly locks in during turning point one | Scores a bonus at battle's end equal to half that op's VP, rounded up | `draft` |
| **Archetype** | A Tac Op category: Infiltration, Recon, Security, Seek & Destroy | Which archetypes you can pick from is set by your kill team's rules | `draft` |
| **Marker** | A token placed on the killzone; objective markers are 40mm, all others are 20mm | Contested and controlled based on operatives' control range and total APL | `draft` |
| **Contest / control a marker** | Contest: within control range of it. Control: your side's total APL contesting it beats the enemy's | Control cannot change mid-action | `draft` |
| **Mission action** | An action defined by the mission pack or killzone rather than the core rules | Where Pick Up Marker / Place Marker usually live | `draft` |

---

## Team, equipment, and rules

| Term | What it means | When it matters | Status |
|------|---------------|-----------------|--------|
| **Kill team** | Your full collection of operatives for a faction | Roughly the Kill Team equivalent of an "army," but not points-built the same way | `draft` |
| **Operative** | One Citadel miniature, individually tracked | The base unit of everything in this game - never grouped like a 40K squad | `draft` |
| **Datacard** | The rules entry for one operative: stats, weapons, abilities, keywords | Never reproduced in this repository | `draft` |
| **Keyword** | A tag used to target certain rules at certain operatives | Faction keywords (orange, skull icon) identify every operative in a kill team | `draft` |
| **Equipment (universal / faction)** | Pre-battle-selected rules options | Each option can be selected once per player per game | `draft` |
| **Base size** | The physical base diameter stated on the datacard, in mm | Relevant to dual-legality checks against 40K basing | `draft` |

---

## Collisions with 40K vocabulary

Terms that sound the same as a Warhammer 40,000 term but **mean something different** in Kill Team. Never assume the 40K definition carries over.

| Term | Kill Team meaning | 40K meaning | Why it matters |
|------|--------------------|-------------|-----------------|
| **Control range** | 1", mutual, visibility-gated - gates Fight, cover, and marker control | Engagement Range: 2" horizontal / 5" vertical - gates melee and most move types | Roughly four times tighter, and does far more work in Kill Team |
| **Cover** | Grants a free retained defence success (a "cover save"), or removes a Conceal target from being valid at all | Worsens the attacker's Ballistic Skill by 1 | Kill Team's cover helps the *defender's dice*; 40K's cover hurts the *attacker's dice* |
| **Charge** | 1AP action, deterministic (Move + 2"), no dice roll | 2D6 roll for maximum charge distance, can fail outright | Kill Team's Charge always succeeds distance-wise if you have the AP and the inches |
| **Fall Back** | 2AP action; disengages from an already-engaged operative | A move type chosen for the whole unit at Movement phase, with Ordered Retreat / Desperate Escape modes | Different cost structure and no battle-shock interaction in Kill Team |
| **Command Point (CP)** | Same currency concept, but income is 1/2 CP asymmetric by initiative, not a flat 1 CP each | Both players gain a flat 1 CP per Command phase | Do not assume even income between players |
| **Ploy** | Kill Team's version of a stratagem, split into Strategy-phase and Firefight-phase types | Stratagem - one list, usable in the phase its trigger specifies | Same idea, different name and a phase-based split 40K doesn't have |
| **Save** | A single datacard stat compared against 3 defence dice, with cover adding a free success | Two separate mechanics: Armour Save (Sv, modified by AP) and Invulnerable Save (InSv, ignores AP) | Kill Team has one save track, not two |
| **Wounds** | Same general idea (hit points), but paired with an **Injured** threshold at half-Wounds that debuffs the model directly | Wounds track damage capacity; there's no per-model "half-wounds" penalty state | 40K's closest analogue (battle-shock) applies at the unit level, not per model |
| **Leader** | A keyword identifying certain operatives (e.g. team leaders), with its own datacard abilities | An attachment role: a Leader character joins a bodyguard unit to form one combined unit | Not the same mechanic - Kill Team has no unit-attachment system at all |
| **Objective marker** | 40mm marker; controlled by comparing total APL of operatives contesting it within 1" control range | Controlled by comparing total Objective Control (OC) of models within a stated range (often 3"/objective-area-based) | Different stat drives control (APL vs OC), and the range that counts is much tighter |
| **Datasheet / Datacard** | Datacard - one operative's full rules entry | Datasheet - one unit's full rules entry, which may cover many models | Same role, different name; never call a Kill Team datacard a "datasheet" in this project's KT content |
| **Injured** | A per-operative damage-state threshold (below half Wounds): -2" Move, weapons' Hit worsens by 1 | No equivalent - 40K's closest concept, battle-shock, is a unit-level morale test, not a wound threshold | Do not describe Injured as "Kill Team's battle-shock" - the trigger and effect are both different |

---

## Related pages

- [`Overview.md`](Overview.md) - what a game is
- [`Turn_Structure.md`](Turn_Structure.md) - when each term comes up
- [`Key_Concepts.md`](Key_Concepts.md) - the mechanics these terms modify
- [`../README.md`](../README.md) - the top-level vocabulary mapping (team/operative, not army/unit)
- [`../../warhammer_40k_11e/rules/Keyword_Glossary.md`](../../warhammer_40k_11e/rules/Keyword_Glossary.md) - the 40K glossary this page cross-checks collisions against
- [`../../../KB/glossary.md`](../../../KB/glossary.md) - the Kill Team 2024 section of the working KB glossary, landed by L1 in parallel with this slice, with matching collision flags
- [`../../../KB/sources/kill_team_2024_core_rules.md`](../../../KB/sources/kill_team_2024_core_rules.md) - the Librarian's source page for the same living Wahapedia reference used here

---

## Change Log
- v1.0 (2026-08-17): Initial shipping glossary (slice S1). Terms drafted from the living Wahapedia core rules, Approved Ops 2025, and Tac Ops pages, all retrieved 2026-08-17. Owned Core Rules PDF not yet opened - every entry is `draft`, none `verified`. Added a dedicated 40K-collision table per plan requirement. Cross-cited against `KB/glossary.md` (Kill Team 2024 section) and six KB concept pages, landed by the Librarian (L1) in parallel with this slice from the same source - independently arrived at matching collision flags.

## Attribution
- Project: Wargame_Concierge
- Maintainer: Russell Catt
- Kill Team and Warhammer 40,000 are trademarks of Games Workshop Limited. This document is a personal teaching paraphrase and reproduces no publisher text.

## Rising Tide Notes
- This document follows Rising Tide documentation standards.
- **Verify before you play.** Cross-check every entry against the owned Core Rules PDF - this page currently rests on living web sources only, retrieved **2026-08-17**.
