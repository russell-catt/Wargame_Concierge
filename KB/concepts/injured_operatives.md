---
title: Injured Operatives
type: concept
system: kill_team_2024
created: 2026-08-17
updated: 2026-08-18
version: 0.5.0
sources: [kill_team_2024_core_rules, games/kill_team_2024/rules/Key_Concepts.md]
confidence: draft
tags: [concept, kill_team_2024, core_rules, damage, injured, wounds, collision_flag]
---

# Injured Operatives

Kill Team's wound-threshold debuff: an operative that has lost more than half its starting Wounds becomes **Injured**, and gets measurably worse until it dies or the game ends.

**L1 flag, then replace:** rewritten from shipping [`Key_Concepts.md`](../../games/kill_team_2024/rules/Key_Concepts.md) (**2026-08-18**). **Incapacitated** and **removed from the killzone** are separate timing windows. Some rules allow one free action (excluding Place Marker) before removal; if wounds hit 0, a heal-on-incap action does not stop removal afterwards (update log). Page stays `draft`.

---

## The mechanic

Damage reduces an operative's current Wounds. Two thresholds matter, and they are distinct:

- **Wounded** - the operative has fewer than its *starting* Wounds remaining. Purely descriptive; nothing changes mechanically at this threshold by itself.
- **Injured** - the operative has fewer than **half** its starting Wounds remaining. This is the threshold that actually does something:
  - **-2" to its Move stat.**
  - **Worsen the Hit stat of all its weapons by 1** (so a 3+ weapon becomes 4+), both ranged and melee.

At **0 Wounds or less**, the operative is **incapacitated**, then **removed from the killzone**. Those are separate moments so some rules can fire in between. Some rules allow one free action (excluding Place Marker) before removal; that operative's player orders those rules.

---

## Why it matters at the table

- **Injured is a hard threshold, not a sliding scale.** An operative one Wound above half strength fights at full effectiveness; one Wound below half, it is Move -2" and Hit worse-by-1 across the board, on every weapon. Chip damage that crosses the halfway line is disproportionately valuable - a shot that merely "wounds" does little on its own, but the shot that crosses the Injured line changes that operative's whole rest of the game.
- **Injured stacks against an already-losing position.** A slower, less accurate operative is worse at both disengaging *and* retaliating, which is why Injured operatives are frequently the ones a controlling player chooses to spend on high-risk actions (a doomed Charge, a Guard sit) rather than protect.
- **Watch for Injured crossing into Conceal viability.** An Injured operative that Falls Back into cover with a Conceal order still gets the full targeting protection [[cover_kill_team]] describes - being Injured does not remove the not-a-valid-target benefit. Injured degrades what an operative *does*, not whether it can be targeted.
- **Marker carrying survives incapacitation, briefly.** The free Place Marker action on incapacitation (0AP, overrides most "cannot" rules) means killing a marker-carrier does not automatically drop the marker wherever it likes for you - the dying player still chooses where to place it, within 1" control range.

---

## Kill Team vs 40K - do not conflate

**Injured (KT24) and Battle-shocked (40K) are not the same idea, despite both being "your unit got worse" mechanics.** Injured is triggered by a **model's own Wounds** crossing a fixed threshold, is checked continuously, and degrades Move and Hit. Battle-shock is triggered by a **failed Leadership test** in the Command phase (itself gated by unit strength, not an individual model's wounds), and it zeroes a unit's Objective Control, blocks stratagem targeting, and blocks actions - see the **Battle-shock** entry in the shipping [`Keyword_Glossary.md`](../../games/warhammer_40k_11e/rules/Keyword_Glossary.md). Neither mechanic maps onto the other; do not describe an Injured KT24 operative as "battle-shocked," and do not describe a battle-shocked 40K unit as "injured."

---

## Open questions

- Whether any owned team's rules modify the Injured thresholds or effects (a common KT24 design space for "tanky" operatives) - unread team pointers.
- Exact wording of which free actions besides Place Marker an incapacitated operative can perform under specific rules - Wahapedia's fragment names Place Marker explicitly and says "excluding Place Marker" elsewhere for a different free-action cap; confirm the full rule against the owned PDF before teaching edge cases.

---

## Related pages

- [[activations_apl]] - Injured's Hit and Move penalties apply during activations
- [[cover_kill_team]] - Injured does not affect targeting/cover eligibility
- [[kill_team_2024_core_rules]] - source
- [[glossary]] - the Injured / Battle-shock collision flag
- [[index]]
