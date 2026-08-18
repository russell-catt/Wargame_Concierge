---
title: Activations and APL
type: concept
system: kill_team_2024
created: 2026-08-17
updated: 2026-08-18
version: 0.5.0
sources: [kill_team_2024_core_rules, games/kill_team_2024/rules/Key_Concepts.md, games/kill_team_2024/rules/Turn_Structure.md, games/kill_team_2024/rules/Keyword_Glossary.md]
confidence: draft
tags: [concept, kill_team_2024, core_rules, activation, apl, action_economy]
---

# Activations and APL

Kill Team's action economy: operatives activate one at a time, alternating between players, and each activation spends Action Points (AP) up to that operative's Action Point Limit (APL).

**L1 flag, then replace:** rewritten from shipping [`Key_Concepts.md`](../../games/kill_team_2024/rules/Key_Concepts.md) / [`Turn_Structure.md`](../../games/kill_team_2024/rules/Turn_Structure.md) (**2026-08-18**). **Heavy** is a shooter gate on activation **or counteraction** (does not prevent Guard). Page stays `draft` except where it points at [[valid_target]].

---

## The mechanic

**Activation order.** In the Firefight phase, the player with initiative activates one ready friendly operative; then the opponent activates one of theirs; repeat, strictly alternating, until one side has no ready operatives left. That side can then **counteract** instead of activating (see below) while the other side finishes activating its remaining operatives.

**Inside one activation:**

1. **Determine order** - choose Engage or Conceal for this operative (it keeps that order until it next activates). See [[orders_conceal_engage]].
2. **Perform actions** - spend AP on actions, up to the operative's **APL** (Action Point Limit, printed on its datacard). An operative cannot perform the *same action* more than once in one activation (an "action restriction") unless a specific rule overrides it. You do not have to declare the whole activation up front - you can perform one action, see the result, then decide the next.
3. **Expended** - once you are done, the operative flips to the dark side of its order token and cannot activate again this turning point.

**APL also gates objective control.** Beyond limiting actions, an operative's APL is the number totalled up to decide who controls a marker it is contesting - see [[control_range_kill_team]].

**Counteract.** If all your operatives are expended but your opponent still has ready ones, you may select one *expended, Engage-ordered* friendly operative to perform one free 1AP action (never Guard), capped at once per operative per turning point and at most a 2" move. This is **not an activation** - action restrictions from that operative's earlier activation do not carry over. **Heavy** still applies to a counteraction: you cannot use a Heavy weapon in a counteraction in which the operative moved (and cannot move in one in which it used the weapon), unless Heavy (x only). Close Quarters **On Guard** blocks counteract that turning point — [[killzones_volkus_tomb_world]]. The extra 1" for Accessible terrain counts against the 2" counteract cap ([[kill_team_terrain]]).

---

## Why it matters at the table

- **Going first is not free.** Activating first reveals your operative's choice before your opponent commits theirs, but it also means you commit without seeing their response. Reading the board correctly - who has the numbers left to punish an exposed operative - matters more than reflexively activating your best piece early.
- **The team that runs out of ready operatives first loses tempo, but gets counteract as a consolation.** An outnumbered kill team is not simply out of options once expended; a lone Engage survivor can still poke for 1AP each remaining opposing activation. That is a real, if limited, lever - factor it into whether "trading down to fewer operatives" is actually bad.
- **APL is a per-operative resource, not a shared pool.** A 2-APL operative and a 4-APL operative do not average out; a low-APL operative is fundamentally limited in what it can chain together (e.g. it may not be able to Reposition *and* Shoot *and* something else in one activation).
- **Action restrictions bite specific combos.** You cannot Reposition twice to double your move - use Dash for a second, shorter move instead, since Dash is a *different* action from Reposition and both can be paid for in one activation if APL allows.

---

## Kill Team vs 40K - do not conflate

40K has no per-model "activation" concept at all - within a phase, a player generally resolves that phase for their whole army, sequenced unit by unit at the player's discretion, not alternating with the opponent. Kill Team's **strict alternating single-operative activation** inside one phase is a structurally different game engine, not a renamed version of the 40K turn. There is also no 40K equivalent of **counteract** - the nearest 40K concept, Fire Overwatch, is a stratagem-gated reactive shoot, not a universal end-of-phase option. See [[glossary]] for both entries side by side.

---

## Open questions

- Precise wording of "some rare rules will change the cost of actions" and the 0AP floor - which KT24 rules (owned teams' unique actions, equipment) actually do this. Unread team pointers.
- Whether any owned killzone or mission pack changes the default four-turning-point Firefight structure in a way that affects activation count per side.

---

## Related pages

- [[turning_points]] - the phase this activation loop sits inside
- [[orders_conceal_engage]] - the order chosen at the start of every activation
- [[control_range_kill_team]] - where APL is totalled for marker control
- [[injured_operatives]] - how Wounds loss changes an activation's options
- [[valid_target]] · [[killzones_volkus_tomb_world]]
- [[kill_team_2024_core_rules]] - source
- [[glossary]] · [[index]]
