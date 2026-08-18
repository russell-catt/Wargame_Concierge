<!--
FILE: games/warhammer_40k_11e/rules/Turn_Structure.md
VERSION: v0.5.0 (2026-08-18)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, slice S3)

DOCUMENT_TYPE: Teaching Guide / Play Checklist
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: Warhammer 40,000 - 11th Edition
REFERENCE_STATUS: Active - draft, spot-checked against owned Core Rules PDF 2026-08-16

SOURCES:
  - C:\Personal\40K\rules\eng_01-06_warhammer40k_new40k_core_rules.pdf (read 2026-08-16)
  - reference/Source_Library.md

PURPOSE:
  A do-this-then-this checklist for one player turn. Written to be readable at
  the table mid-game, so a beginner never has to ask "what happens next?".

PRIMARY_AUDIENCE:
  - A player mid-game who has lost the thread
  - A first-time player walking through their first turn

KEY_SECTIONS_EXPECTED:
  - Battle round frame
  - Start of Turn
  - Command / Movement / Shooting / Charge / Fight phases
  - End of Turn
  - Common mistakes

UPDATE_TRIGGER:
  Update when a new Core Rules version or rules update changes phase steps,
  move types, shooting types, or fight sequencing.
-->

# Turn Structure - the checklist for your turn

Read top to bottom. Each phase has a short "what you are actually deciding" note, because knowing the order is not the same as knowing what matters.

Checked against the owned Core Rules PDF on **2026-08-16**.

---

## The frame around your turn

A **battle round** is: start-of-round rules, then **both** players take a turn, then end-of-round rules. The same player takes the first turn every round - the mission tells you who.

Your turn is seven parts: a Start of Turn step, five phases, an End of Turn step.

---

## 0. Start of Turn

- [ ] Resolve anything that triggers "at the start of your turn".

---

## 1. Command phase

*What you are deciding: nothing much yet - this is bookkeeping and morale.*

- [ ] Resolve start-of-Command-phase triggers.
- [ ] **Both players gain 1 CP.** (This is "Core CP"; it is a normal Command Point.)
- [ ] **Battle-shock.** Make a battle-shock roll for each of your units that is either already battle-shocked, or at/below half-strength.
  - Roll 2D6 and compare against the unit's Leadership. Pass and nothing happens; a unit that was battle-shocked recovers.
  - Fail and the unit is **battle-shocked**: its OC drops to nothing, you cannot target it with stratagems, and it cannot perform actions.
- [ ] Use any abilities that trigger in the Command phase. **Necrons: Reanimation Protocols activate at the end of this phase.**
- [ ] Resolve end-of-Command-phase triggers, then mission triggers.

---

## 2. Movement phase

*What you are deciding: where the game is won. Most of your scoring is set up here.*

- [ ] Resolve start-of-phase triggers.
- [ ] **Select every unit, one at a time, and give each one a move type.** Yes, every unit - a unit that stays put has still been selected to "remain stationary".

Your options:

| Move type | Distance | Cost |
|-----------|----------|------|
| **Remain Stationary** | Nothing moves | None. Keeps [HEAVY] weapon bonuses and indirect-fire accuracy |
| **Normal Move** | Up to the unit's Move (M) | Must start and end unengaged |
| **Advance Move** | M + a D6 roll | Cannot charge or start an action this turn; can only shoot [ASSAULT] weapons |
| **Fall Back** | Up to M | Escapes melee, but cannot shoot, charge, or start an action this turn |
| **Disembark** | From a transport | Mode depends on what the transport did |
| **Ingress** | Arriving from reserves | Comes in from a battlefield edge, or anywhere if the unit has Deep Strike |

- [ ] **Falling back has two modes.** *Ordered Retreat* if the unit is not battle-shocked. Otherwise *Desperate Escape*: roll a hazard die per model, and the unit must then take a battle-shock roll.
- [ ] **Reserves arrive here.** Normally from the second battle round onward, set up within 6" of a battlefield edge and more than 8" from all enemies. Units with **Deep Strike** may instead appear anywhere more than 8" from enemies.
- [ ] Check **coherency** after every move: each model within 2" of at least one other model in its unit, and within 9" of all of them.
- [ ] Resolve end-of-phase triggers.

---

## 3. Shooting phase

*What you are deciding: which threat you remove, and whether you can afford to leave it alive.*

- [ ] Resolve start-of-phase triggers.
- [ ] Pick a unit and pick a **shooting type**:

| Shooting type | Use when |
|---------------|----------|
| **Normal** | Unengaged and did not Advance |
| **Assault** | Unengaged and **did** Advance - only [ASSAULT] weapons may fire |
| **Close-quarters** | Engaged in melee - only [CLOSE-QUARTERS] weapons, only at units you are engaged with |
| **Indirect** | Unengaged, did not Advance, has [INDIRECT FIRE] weapons - can hit targets you cannot see, at a heavy accuracy penalty and giving the target cover |

- [ ] For each shooting unit: select weapons, select targets, then resolve the attack sequence (hit, wound, save, damage). Full detail in [`Key_Concepts.md`](Key_Concepts.md).
- [ ] Targets must normally be **visible**, **in range**, and **unengaged**. Enemy Monsters and Vehicles are the exception - you can shoot those while they are engaged, at -1 to hit.
- [ ] Resolve end-of-phase triggers.

---

## 4. Charge phase

*What you are deciding: whether a 2D6 gamble is worth it. Failing a charge usually means standing in the open.*

- [ ] Resolve start-of-phase triggers.
- [ ] Pick a unit that is eligible to charge. It must be **within 12" of an enemy unit**, not already engaged, and it must not have Advanced or Fallen Back this turn.
- [ ] **Roll 2D6.** That is your maximum charge distance.
- [ ] Nominate your charge targets - each must be within 12" and within the rolled distance - and move. Every model must end closer to a target, and engage a target if it can.
- [ ] If you cannot end up engaged with **all** nominated targets, the charge fails and nothing moves.
- [ ] A unit that completes a charge move has **Fights First** for the rest of the turn.
- [ ] Resolve end-of-phase triggers.

> Your opponent can respond at the end of this phase with the **Heroic Intervention** core stratagem (1CP) and charge you back.

---

## 5. Fight phase

*What you are deciding: activation order. Both players act here, alternating, so sequencing is a real skill.*

- [ ] Resolve start-of-phase triggers.
- [ ] **Pile In.** Both players make 3" pile-in moves with eligible units - you first, then your opponent. Models already in base contact cannot move.
- [ ] **Fight.**
  - Resolve all **Fights First** units first, alternating between players, starting with you.
  - Then alternate through everyone else, still starting with whoever is next in sequence.
  - Each fighting unit picks one melee weapon per model, picks targets it is engaged with, and resolves the attack sequence.
  - You **must** fight with every unit that can. Piling in and consolidating are optional.
- [ ] **Consolidate.** Both players make 3" consolidation moves - you first. The mode is forced by circumstance: stay engaged if you already are, otherwise engage an enemy within 3", otherwise move onto an objective within 3".
- [ ] Resolve end-of-phase triggers.

> **Objective Consolidation is a scoring tool, not an afterthought.** If nothing is close enough to fight, a 3" shuffle onto an objective can be worth more than the combat was.

---

## 6. End of Turn

- [ ] Resolve non-mission end-of-turn triggers.
- [ ] **Both players check their mission** and score any VP triggered at end of turn.
- [ ] Fix coherency: any unit that is out of coherency loses models until it is back in.

Your turn ends. Your opponent takes theirs. When both have gone, the battle round ends and mission end-of-round scoring happens.

---

## Common beginner mistakes

| Mistake | What actually happens |
|---------|----------------------|
| Forgetting to select a unit to move | Every unit must be selected in the Movement phase, even if only to remain stationary |
| Advancing then trying to charge | Advancing removes your charge for the turn unless a rule says otherwise |
| Assuming the Fight phase is yours alone | Both players fight in it, alternating |
| Scoring only at the end of the game | Most primary scoring is checked every battle round - board position **now** is what counts |
| Ignoring consolidation | 3" of free movement onto an objective, every Fight phase |
| Measuring cover as a save bonus | In 11th Edition, benefit of cover worsens the attacker's Ballistic Skill by 1 - see [`../setup/Terrain_Basics.md`](../setup/Terrain_Basics.md) |

---

## Related pages

- [`Overview.md`](Overview.md) - what a game is and how you win
- [`Key_Concepts.md`](Key_Concepts.md) - the attack sequence in detail
- [`Keyword_Glossary.md`](Keyword_Glossary.md) - every move type, weapon ability, and term
- [`../setup/Board_Setup.md`](../setup/Board_Setup.md) - everything that happens before turn one

---

## Change Log
- v0.5.0 (2026-08-18): Project-wide semver snapshot (x.y.z).
- v1.0 (2026-08-16): Initial phase checklist (slice S3), written from the owned Core Rules PDF read 2026-08-16.

## Attribution
- Project: Wargame_Concierge
- Maintainer: Russell Catt
- Warhammer 40,000 is a trademark of Games Workshop Limited. This document is a personal teaching paraphrase and reproduces no publisher text.

## Rising Tide Notes
- This document follows Rising Tide documentation standards.
- **Verify before you play.** Cross-check anything here against the current Munitorum Field Manual and your faction pack - Games Workshop patches rules and points between publications. Content on this page reflects sources read on **2026-08-16**.
