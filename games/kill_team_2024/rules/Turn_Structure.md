<!--
FILE: games/kill_team_2024/rules/Turn_Structure.md
VERSION: v1.0 (2026-08-17)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, slice S1)

DOCUMENT_TYPE: Teaching Guide / Play Checklist
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: Kill Team - 2024 / 3rd Edition (KT24)
REFERENCE_STATUS: Draft - written from the living Wahapedia core rules page; not yet cross-checked against the owned Core Rules PDF

SOURCES:
  - raw/pointers/kill_team_2024_core.md (points at C:\Personal\Kill Team\kill_team_2024\779937548-Core-Rules-KILL-TEAM-3E-Full-Scan.pdf - not yet opened this slice)
  - https://wahapedia.ru/kill-team3/the-rules/core-rules/ (retrieved 2026-08-17)
  - KB/concepts/turning_points.md and KB/concepts/activations_apl.md (Librarian L1, landed in parallel with this slice - same living source, cross-checked as consistent)

PURPOSE:
  A do-this-then-this checklist for one turning point. Written to be readable
  at the table mid-game.

PRIMARY_AUDIENCE:
  - A player mid-game who has lost the thread
  - A first-time player walking through their first turning point

KEY_SECTIONS_EXPECTED:
  - The frame around a turning point
  - Strategy phase (Initiative, Ready, Gambit)
  - Firefight phase (activation loop, Counteract)
  - Common beginner mistakes

UPDATE_TRIGGER:
  Update when a new Core Rules printing or errata changes phase steps,
  the activation loop, or Counteract.
-->

# Turn Structure - the checklist for your turning point

Read top to bottom. Kill Team has only two phases, but almost all of the game's decisions live inside the second one.

Written from the living Wahapedia core rules page, retrieved **2026-08-17**. Status: `draft` - not yet cross-checked against the owned Core Rules PDF.

---

## The frame around a turning point

A **battle** is a sequence of **turning points**. Each turning point is: Strategy phase, then Firefight phase, completed in order and in full. Repeat until the battle ends (four turning points under Approved Ops 2025; other mission packs state their own length).

---

## 1. Strategy phase

*What you are deciding: who acts first this turning point, and whether to spend a ploy before anyone moves.*

### Initiative

- [ ] Determine who has **initiative** for this turning point.
  - **First turning point:** set by your mission pack's game sequence (often a roll-off at setup).
  - **Later turning points:** both players roll off; the **winner** decides who has initiative. On a tie, whoever did **not** have initiative last turning point decides. This tie-break beats the roll-off itself.
- [ ] The player with initiative resolves any of their own simultaneous-timing decisions first this turning point.

### Ready

- [ ] Each player gains **1 CP**. From the second turning point onward, the player **without** initiative gains **2 CP** instead.
- [ ] Every friendly operative is **readied** (order token flipped to its lighter, "ready" side).

### Gambit

- [ ] Starting with the player who has initiative, each player alternates either using one **STRATEGIC GAMBIT** (most commonly a **strategy ploy**) or passing.
- [ ] Keep alternating until **both players pass in succession** - that ends the step.
- [ ] You cannot use the same named STRATEGIC GAMBIT more than once per turning point.

---

## 2. Firefight phase

*What you are deciding: activation order. This is where the entire battle actually happens.*

The player with initiative activates first. Players then **alternate**, one operative per activation, for the whole phase.

- [ ] **Determine order.** Set the activating operative's order for this activation: **Conceal** or **Engage** (it keeps that order until it is next activated). See [`Key_Concepts.md`](Key_Concepts.md) for what each order permits.
- [ ] **Perform actions.** Spend the operative's **AP** on actions up to its **APL**, in any order, deciding one action at a time rather than declaring the whole activation up front. An operative cannot repeat the same action in one activation (action restrictions), with named exceptions on some datacards.
- [ ] **Expended.** When you are done with that operative, it becomes **expended** (order token flipped to its darker side) and cannot act again this turning point except by Counteracting.
- [ ] Activation passes to the opponent. Repeat until **one player has no ready operatives left**.

### Counteract

- [ ] If all of *your* operatives are expended but your opponent still has ready operatives left to activate, you may pick **one expended friendly operative that is on an Engage order** and let it perform **one free 1AP action** (not Guard).
  - It cannot move more than 2" while doing this.
  - Each operative can counteract **once per turning point**.
  - Counteracting is optional - and it is **not an activation**, so normal action restrictions from that operative's earlier activation do not carry over to it.
- [ ] The Firefight phase ends once every operative on both sides is expended.

---

## Common beginner mistakes

| Mistake | What actually happens |
|---------|----------------------|
| Treating phases like 40K's five | Kill Team has two phases; movement, shooting, and fighting all happen inside one operative's Firefight-phase activation |
| Declaring a whole activation up front | You may perform one action, see its result, then decide the next - nothing has to be pre-planned |
| Forgetting to set an order every activation | Every activation starts with choosing Conceal or Engage, even if you plan to leave it the same as before |
| Assuming Conceal operatives are safe from everything | Conceal only stops an operative being a valid target **while it is also in cover**; in the open it can still be shot |
| Skipping Counteract | It is easy to forget once your side runs out of ready operatives mid-phase - check every time your opponent activates after that point |
| Assuming both players gain 1 CP every turning point | Only true in the first turning point; after that the player without initiative gains 2 CP |

---

## Related pages

- [`Overview.md`](Overview.md) - what a game is and how you win
- [`Key_Concepts.md`](Key_Concepts.md) - APL, Orders, control range, cover, and Injured in full
- [`Keyword_Glossary.md`](Keyword_Glossary.md) - every term used above, one line each
- [`../../../KB/concepts/turning_points.md`](../../../KB/concepts/turning_points.md) - the Librarian's concept page for this exact structure, landed in parallel
- [`../../../KB/concepts/activations_apl.md`](../../../KB/concepts/activations_apl.md) - the activation loop, from the KB side

---

## Change Log
- v1.0 (2026-08-17): Initial phase checklist (slice S1), written from the living Wahapedia core rules page, retrieved 2026-08-17. Cross-cited against `KB/concepts/turning_points.md` and `KB/concepts/activations_apl.md`, landed by the Librarian (L1) in parallel with this slice from the same source.

## Attribution
- Project: Wargame_Concierge
- Maintainer: Russell Catt
- Kill Team is a trademark of Games Workshop Limited. This document is a personal teaching paraphrase and reproduces no publisher text.

## Rising Tide Notes
- This document follows Rising Tide documentation standards.
- **Verify before you play.** Cross-check anything here against the owned Core Rules PDF - this page currently rests on a living web source only, retrieved **2026-08-17**.
