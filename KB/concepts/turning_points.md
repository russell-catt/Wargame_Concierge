---
title: Turning Points
type: concept
system: kill_team_2024
created: 2026-08-17
updated: 2026-08-18
version: 0.5.0
sources: [kill_team_2024_core_rules, games/kill_team_2024/rules/Turn_Structure.md, games/kill_team_2024/rules/Overview.md]
confidence: draft
tags: [concept, kill_team_2024, core_rules, turn_structure]
---

# Turning Points

Kill Team's round structure: a battle runs through a fixed number of **turning points**, each split into a **Strategy phase** and a **Firefight phase**, completed in order and in full before the next begins.

**L1 flag, then replace:** 2026-08-17 Wahapedia draft rewritten from shipping [`Turn_Structure.md`](../../games/kill_team_2024/rules/Turn_Structure.md) / [`Overview.md`](../../games/kill_team_2024/rules/Overview.md) (**2026-08-18**). Setup Conceal and ready/expended token sides confirmed against Full-Scan p.54; remaining checklist rows still began as Wahapedia. Page stays `draft`.

---

## The mechanic

A battle by default lasts **four turning points**, unless the mission pack says otherwise. Each turning point is:

1. **Strategy phase** - three steps in fixed order:
   - **Initiative**: whoever has initiative activates first and breaks simultaneous-timing ties. Turning point one is set by the mission pack's game sequence; from turning point two onward it is a roll-off, with a tie-break rule that favours whoever *didn't* have initiative last turning point.
   - **Ready**: both players gain Command Points (CP) - 1 each normally, but the player *without* initiative gets 2 from turning point two onward - and every friendly operative is readied (order token flipped to its **lighter** "ready" side; the darker side is **expended**). Operatives are given **Conceal** when **set up before the battle**; you change order when you activate.
   - **Gambit**: players alternate using a `STRATEGIC GAMBIT` (usually a Strategy ploy) or passing, until both have passed in a row. Each `STRATEGIC GAMBIT` can only be used once per turning point.
2. **Firefight phase**: players alternate activating one ready operative at a time, starting with whoever has initiative, until one side has no ready operatives left - after which the side with none left can **counteract** instead of activating, until the other side's operatives are all expended too.

Then the turning point ends and the next one begins the whole sequence again.

---

## Why it matters at the table

- **Initiative is a resource, not a coin flip.** After turning point one it is actively contested by roll-off, and the loser of that roll-off is compensated by choosing who gets initiative if the *next* roll-off ties. Track who has it and why.
- **The CP-gain asymmetry rewards losing initiative.** Not having initiative in a turning point gets you 2 CP instead of 1 in the Ready step - a deliberate counterweight to the tempo advantage the initiative player gets by activating first.
- **`STRATEGIC GAMBIT`s are locked to the Gambit step.** You cannot save a Strategy ploy for mid-Firefight use; if it is a Strategy ploy, it happens (or is skipped) before a single operative activates.
- **The Firefight phase is not "my turn, your turn."** Both sides interleave single-operative activations. Going second in *initiative* does not mean waiting for the whole opposing team to move first - see [[activations_apl]] for how activation order actually plays out, and how counteracting changes the endgame of an uneven Firefight phase.

---

## Kill Team vs 40K - do not conflate

Kill Team has **no equivalent of a Battle Round split into a Movement/Shooting/Charge/Fight phase per player**. A KT24 turning point's Firefight phase interleaves single-operative activations from both sides; a 40K battle round gives each player a full sequential turn. See the **Battle round** entry in [[glossary]] for the 40K side of this, and the collision flag recorded there.

---

## Open questions

- Mission packs that are not Approved Ops 2025 may change battle length — check the pack in play ([`Overview.md`](../../games/kill_team_2024/rules/Overview.md)).
- Remaining Strategy/Firefight rows still began as Wahapedia **2026-08-17**; confirm against the physical book for anything not on Full-Scan p.54 / Patch_Manifest.

---

## Related pages

- [[activations_apl]] - what happens inside the Firefight phase
- [[orders_conceal_engage]] - the order chosen at the start of each activation
- [[kill_team_2024_core_rules]] - source
- [[glossary]] - Kill Team 2024 terms and the 40K "Battle round" collision flag
- [[index]]
- Shipping: [`Turn_Structure.md`](../../games/kill_team_2024/rules/Turn_Structure.md)
