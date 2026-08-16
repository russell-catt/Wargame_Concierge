---
title: Objective Control
type: concept
system: warhammer_40k_11e
created: 2026-08-16
updated: 2026-08-16
sources: [local_library_pointers]
confidence: unverified
tags: [concept, core_rules, scoring, objectives, oc, s3]
---

# Objective Control

A characteristic on every model's profile representing how strongly it holds ground. Totalling it decides who controls an objective marker - and controlling objectives is how games are won.

---

## Confidence: unverified

**The 11th Edition core rules have not been read.** The core rules pointer at `raw/pointers/rules_core.md` is unopened. This page states the mechanic as generally understood and marks what S3 must confirm.

S3 owns core rules and setup, and will either verify this page or replace it. It exists now because [[necrons]], [[space_marines]], [[canoptek_court]], [[cryptek_conclave]], [[power_matrix]], and [[reanimation_protocols]] all reason about objectives and need a shared page to point at.

---

## The mechanic

Each model has an **Objective Control** characteristic, usually written **OC**. To resolve who controls an objective marker, each player adds up the OC of their eligible models within range of it. The higher total controls it.

The consequences are what make it interesting:

- **Control is a total, not a presence check.** Ten models with low OC can out-hold two models with high OC. Numbers matter in a way that raw quality does not always overcome.
- **Cheap units earn their place.** A unit that cannot kill anything can still be the reason a game is won, which is unintuitive for anyone arriving from a game scored on casualties.
- **It can be contested and flipped.** Control changes as models move, die, or arrive, so an objective held comfortably on one turn is not held on the next.

---

## Why it is the most important thing a beginner learns

Modern 40K is scored on objectives, not on kills. A player can remove more of the opponent's army and still lose by a wide margin - and new players lose this way constantly, because killing things is visible and satisfying while standing on a marker is neither.

Everything else in this KB is downstream of it:

- [[reanimation_protocols]] is valuable *because* a unit that survives keeps holding ground. Durability with nothing to stand on is worth much less.
- [[power_matrix]] couples accuracy to controlled territory, so for [[canoptek_court]] objective control is simultaneously the win condition and a damage buff.
- [[cryptek_conclave]] wins by standing on objectives and refusing to be removed. That plan is only coherent if standing there scores.
- [[oath_of_moment]] is about concentrating damage - and the right target is usually chosen by what is contesting an objective, not by what looks most dangerous.

**The habit to build:** before moving anything, ask which objectives are contested this turn and what would change that. Then move.

---

## What must be confirmed for 11th Edition

| Question | Why it matters |
|----------|----------------|
| Is OC calculated the same way in 11e? | The whole page depends on it |
| What is "within range" of an objective marker? | Determines actual model placement, inch by inch |
| Which models count as eligible - do Battle-shocked or fleeing units still contribute? | A common and decisive edge case |
| How do abilities that modify or ignore OC work now? | Several factions have them; they invert the numbers game |
| When is control checked, and when is scoring measured? | The difference between holding an objective and scoring it |

The last one deserves emphasis: *holding* and *scoring* are checked at different moments, and misunderstanding which is which is one of the most common beginner errors in the game.

---

## Handover to S3

This page is the KB-side working surface. S3 owns:

- `games/warhammer_40k_11e/rules/Key_Concepts.md` - scoring explained for a player
- `games/warhammer_40k_11e/rules/Keyword_Glossary.md` - the at-a-glance OC entry
- `games/warhammer_40k_11e/setup/Board_Setup.md` - objective placement

See [[inherited_docs_for_S3]].

---

## Related pages

- [[reanimation_protocols]] · [[oath_of_moment]] - the two army rules, both aimed at this
- [[power_matrix]] - couples territory control to accuracy
- [[necrons]] · [[space_marines]] - the two factions
- [[local_library_pointers]] - the unread core rules
- [[inherited_docs_for_S3]] · [[index]] · [[glossary]]
