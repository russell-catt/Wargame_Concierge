<!--
FILE: games/warhammer_40k_11e/rules/Turn_Structure.md
VERSION: v0.6.0 (2026-08-27)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, track dataslate_0826 / S2e)

DOCUMENT_TYPE: Teaching Guide / Play Checklist
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: Warhammer 40,000 - 11th Edition
REFERENCE_STATUS: Active - draft, spot-checked against owned Core Rules PDF 2026-08-16; disembark move typing added 2026-08-27 per Universal Rules Updates v1.1

SOURCES:
  - C:\Personal\40K\rules\eng_01-06_warhammer40k_new40k_core_rules.pdf (read 2026-08-16)
  - raw/_dataslate_0826_staging/eng_wh40k_core&key_universal_rules_updates-lu3grocned-rphh78bl6k.pdf (Universal Rules Updates v1.1, legal 26 Aug 2026; staging copy, read 2026-08-27)
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

Checked against the owned Core Rules PDF on **2026-08-16**. Numbered IDs point at [`Core_Rules_Quotes.md`](Core_Rules_Quotes.md).

**Contradiction check (2026-08-18):** move types (**09.04–09.07**), shooting types (**10.04–10.07**), charge (**11.02**, **11.04**), pile-in/consolidate (**12.02–12.08**), and Core CP (**08.02**) match the 2026-08-16 paraphrase. No rewrite.

**Currency stamp (2026-08-27):** Universal Rules Updates **v1.1, legal 26 Aug 2026** cross-checked. Disembark move types gain two new named cases (`18.06` assault, `18.07` shock) — added to the Movement phase section below. No other move type changed.

---

## The frame around your turn

A **battle round** (**07**) is: start-of-round rules, then **both** players take a turn, then end-of-round rules. The same player takes the first turn every round - the mission tells you who.

Your turn is seven parts: a Start of Turn step, five phases, an End of Turn step.

---

## 0. Start of Turn

- [ ] Resolve anything that triggers "at the start of your turn".

---

## 1. Command phase

*What you are deciding: nothing much yet - this is bookkeeping and morale.*

- [ ] Resolve start-of-Command-phase triggers.
- [ ] **Both players gain 1 CP.** (This is "Core CP" — **08.02**; it is a normal Command Point.)
- [ ] **Battle-shock** (**08.03**, **01.07**). Make a battle-shock roll for each of your units that is either already battle-shocked, or at/below half-strength.
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
| **Remain Stationary** (**09.04**) | Nothing moves | None. Keeps [HEAVY] weapon bonuses and indirect-fire accuracy |
| **Normal Move** (**09.05**) | Up to the unit's Move (M) | Must start and end unengaged |
| **Advance Move** (**09.06**) | M + a D6 roll | Cannot charge or start an action this turn; can only shoot [ASSAULT] weapons |
| **Fall Back** (**09.07**) | Up to M | Escapes melee, but cannot shoot, charge, or start an action this turn |
| **Disembark** | From a transport | Mode depends on what the transport did |
| **Ingress** | Arriving from reserves | Comes in from a battlefield edge, or anywhere if the unit has Deep Strike |

- [ ] **Falling back has two modes.** *Ordered Retreat* if the unit is not battle-shocked. Otherwise *Desperate Escape*: roll a hazard die per model, and the unit must then take a battle-shock roll.
- [ ] **Reserves arrive here.** Normally from the second battle round onward, set up within 6" of a battlefield edge and more than 8" from all enemies. Units with **Deep Strike** may instead appear anywhere more than 8" from enemies.
- [ ] Check **coherency** after every move: each model within 2" of at least one other model in its unit, and within 9" of all of them.
- [ ] Resolve end-of-phase triggers.

**Commentary (White Dwarf 527 — Movement changes):**

Coherency is a dual test: every model within **2"** of another model in the unit, and within **9"** of every other model (**03.03**). Ingress sets up within **6"** of a battlefield edge (**20.04**) and more than **8"** from enemies; Deep Strike may appear anywhere more than **8"** from enemies. Do not conflate the 6" edge distance with the 9" coherency span — both Core numbers are real, for different jobs.

**Cite:** WD527, Movement changes; owned digital backup purchased Trinity Hobby **2026-08-22**; local scans `C:\Personal\40K\WD_527\`. Tier **1.5** — Core / Event Companion win on mechanics.

**Disembark move types (currency: Universal Rules Updates v1.1, legal 26 Aug 2026):** an ordinary **disembark move** (Core **18.04**) needs the TRANSPORT to have remained stationary or made a normal move that phase — it cannot have Advanced or Fallen Back. Two special cases now have their own names, because some faction/wargear rules grant permissions the base disembark move does not:

- **Assault disembark move** (**18.06**) — used instead of a normal disembark move when a rule lets your unit be eligible to **declare a charge** after disembarking from a TRANSPORT that made a **normal move** that turn.
- **Shock disembark move** (**18.07**) — used instead of a normal disembark move when a rule lets your unit **disembark from a TRANSPORT that Advanced** that turn.

Neither ID grants the permission by itself — a separate ability has to allow the charge or the disembark-after-advance first. **v1.1** just gives the resulting move a name other rules can key off. Verbatim quotes: [`Core_Rules_Quotes.md`](Core_Rules_Quotes.md) (August `eng_*` deltas section).

---

## 3. Shooting phase

*What you are deciding: which threat you remove, and whether you can afford to leave it alive.*

- [ ] Resolve start-of-phase triggers.
- [ ] Pick a unit and pick a **shooting type**:

| Shooting type | Use when |
|---------------|----------|
| **Normal** (**10.04**) | Unengaged and did not Advance |
| **Assault** (**10.05**) | Unengaged and **did** Advance - only [ASSAULT] weapons may fire |
| **Close-quarters** (**10.06**) | Engaged in melee - only [CLOSE-QUARTERS] weapons, only at units you are engaged with |
| **Indirect** (**10.07**) | Unengaged, did not Advance, has [INDIRECT FIRE] weapons - can hit targets you cannot see, at a heavy accuracy penalty and giving the target cover |

- [ ] For each shooting unit: select weapons, select targets, then resolve the attack sequence (hit, wound, save, damage). Full detail in [`Key_Concepts.md`](Key_Concepts.md).
- [ ] Targets must normally be **visible**, **in range**, and **unengaged**. Enemy Monsters and Vehicles are the exception - you can shoot those while they are engaged, at -1 to hit.
- [ ] Resolve end-of-phase triggers.

---

## 4. Charge phase

*What you are deciding: whether a 2D6 gamble is worth it. Failing a charge usually means standing in the open.*

- [ ] Resolve start-of-phase triggers.
- [ ] Pick a unit that is eligible to charge (**11.02**). It must be **within 12" of an enemy unit**, not already engaged, and it must not have Advanced or Fallen Back this turn.
- [ ] **Roll 2D6.** That is your maximum charge distance.
- [ ] Nominate your charge targets - each must be within 12" and within the rolled distance - and move. Every model must end closer to a target, and engage a target if it can.
- [ ] If you cannot end up engaged with **all** nominated targets, the charge fails and nothing moves.
- [ ] A unit that completes a charge move has **Fights First** for the rest of the turn.
- [ ] Resolve end-of-phase triggers.

**Commentary (White Dwarf 527 — Charge / Jack Rules Focus):**

*Roll charge distance before picking targets.* Roll 2D6 first; that roll both caps how far you can move and which enemies are eligible. A failed reach to a far target does not let you switch to a closer enemy that was outside the rolled distance.

**Cite:** WD527, Charge / Jack Rules Focus; owned digital backup purchased Trinity Hobby **2026-08-22**; local scans `C:\Personal\40K\WD_527\`. Tier **1.5** — Core / Event Companion win on mechanics.

> Your opponent can respond at the end of this phase with the **Heroic Intervention** core stratagem (1CP) and charge you back.

---

## 5. Fight phase

*What you are deciding: activation order. Both players act here, alternating, so sequencing is a real skill.*

- [ ] Resolve start-of-phase triggers.
- [ ] **Pile In** (**12.02**, **12.03**). Both players make 3" pile-in moves with eligible units - you first, then your opponent. Models already in base contact cannot move.
- [ ] **Fight.**
  - Resolve all **Fights First** units first, alternating between players, starting with you.
  - Then alternate through everyone else, still starting with whoever is next in sequence.
  - Each fighting unit picks one melee weapon per model, picks targets it is engaged with, and resolves the attack sequence.
  - You **must** fight with every unit that can. Piling in and consolidating are optional.
- [ ] **Consolidate** (**12.07**, **12.08**). Both players make 3" consolidation moves - you first. The mode is forced by circumstance: stay engaged if you already are, otherwise engage an enemy within 3", otherwise move onto an objective within 3".
- [ ] Resolve end-of-phase triggers.

**Commentary (White Dwarf 527 — Pile-in / Consolidate):**

Pile-in and consolidate are separate steps. The active player moves all eligible units first, then the opponent does. Sequencing matters when both sides want the same scrap of board.

**Cite:** WD527, Pile-in / Consolidate; owned digital backup purchased Trinity Hobby **2026-08-22**; local scans `C:\Personal\40K\WD_527\`. Tier **1.5** — Core / Event Companion win on mechanics.

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

## Games Workshop notice

**UNOFFICIAL.** This document is completely unofficial and in no way endorsed by Games Workshop Limited. Personal / no-charge use only — never for sale. Warhammer, Warhammer 40,000 and associated marks are trademarks of Games Workshop Limited. Used without permission. No challenge to their status intended. Warhammer 40,000 is Copyright Games Workshop Limited. Teaching notes by Russell Catt (Wargame Concierge). Games Workshop retains IP in the settings and characters. No official logos.

## Change Log
- v0.6.0 (2026-08-27): Universal Rules Updates v1.1 (legal 26 Aug 2026) currency pass — added assault disembark move (`18.06`) / shock disembark move (`18.07`) teaching paraphrase to the Movement phase; track `dataslate_0826` slice S2e.
- v0.5.2 (2026-08-25): WD527 Commentary blocks — Movement (2"/9", Ingress 6", Deep Strike >8"), Charge (2D6 first), Pile-in/Consolidate (active then opponent); track `wd527_shipping` S1.
- v0.5.1 (2026-08-18): Rule-ID cites; no paraphrase rewrite (track `40k_warcom_quotes` S3).
- v0.5.0 (2026-08-18): Project-wide semver snapshot (x.y.z).
- v1.0 (2026-08-16): Initial phase checklist (slice S3), written from the owned Core Rules PDF read 2026-08-16.

## Attribution
- Project: Wargame_Concierge
- Maintainer: Russell Catt
- Warhammer 40,000 is a trademark of Games Workshop Limited. This document is a personal teaching paraphrase and reproduces no publisher text.

## Rising Tide Notes
- This document follows Rising Tide documentation standards.
- **Verify before you play.** Cross-check anything here against the current Munitorum Field Manual and your faction pack - Games Workshop patches rules and points between publications. Content on this page reflects sources read on **2026-08-16**.
