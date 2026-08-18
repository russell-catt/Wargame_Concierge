---
title: Orders - Conceal and Engage
type: concept
system: kill_team_2024
created: 2026-08-17
updated: 2026-08-18
version: 0.5.0
sources: [kill_team_2024_core_rules, games/kill_team_2024/rules/Key_Concepts.md, games/kill_team_2024/rules/Target_Eligibility.md]
confidence: draft
tags: [concept, kill_team_2024, core_rules, orders, conceal, engage, stealth]
---

# Orders - Conceal and Engage

Every Kill Team operative carries one of two **orders** at all times, chosen fresh each time it activates: **Engage** or **Conceal**. The order is the single biggest tactical lever in the game - it decides whether an operative can act freely or hide, and it feeds directly into whether it is even a legal target.

**L1 flag, then replace:** rewritten from shipping (**2026-08-18**). Shoot-step valid-target wording uses visible to the **active** operative. See [[valid_target]] (`verified` targeting subset). This page stays `draft`.

---

## The mechanic

| Order | Can do | Cannot do | Targeting |
|-------|--------|-----------|-----------|
| **Engage** | Everything: Shoot, Charge, counteract, all universal actions | - | Valid target if visible to the shooter, cover or not |
| **Conceal** | Reposition, Dash, Fall Back, Fight (if already in 1" control range), Pick Up/Place Marker, Guard is unavailable (Guard is treated as Shoot) | **Shoot**, **Charge**, and **counteracting** | Valid target only if visible **and not in cover** |

Operatives are set up with a Conceal order at the start of the battle and can switch orders every time they are next activated - you are not locked into your starting choice, and you decide the new order at the top of each activation, before performing any actions.

**The core trade:** Conceal makes an operative disappear as a target while it sits in cover, at the cost of losing its two biggest offensive tools (Shoot, Charge) and its only reactive tool (counteract). Engage keeps every option live but makes the operative fully shootable regardless of cover.

---

## Why it matters at the table

- **Cover only protects a Conceal-ordered operative.** An Engage operative standing in the exact same cover is still a fully valid target - it just gets a cover save when it's actually shot at (see [[cover_kill_team]]). Cover is not a blanket defensive stat; it is conditional on the order you gave.
- **The order decision is made every activation, in the light of what just happened.** You are not stuck with a bad Conceal call from three turning points ago - the next time that operative activates, reassess.
- **Switching an operative to Engage the moment before it needs to Shoot or Charge is the standard pattern.** Sit in Conceal, invisible in cover, until the activation you actually want to act - then flip to Engage and spend the AP. The risk is that the switch happens on *your* activation, in full view of the opponent's remaining ready operatives, who can then react on their own activations.
- **Conceal locks out counteracting.** If your team is about to be the side that runs out of ready operatives, an operative you want as your counteract option for the rest of the turning point needs to be Engage-ordered *before* it goes expended, not Conceal.

---

## Kill Team vs 40K - do not conflate

**Naming collision, not a shared mechanic.** Kill Team's **Engage** is a per-operative *order* chosen each activation. Warhammer 40,000 has no order system at all; the nearest-sounding 40K term is **Engagement Range** (the fixed 2"-horizontal / 5"-vertical zone around a model that governs charging, falling back, and shooting restrictions - see [[glossary]]). The two words describe unrelated mechanics in unrelated games. Do not read a KT24 "Engage" as anything to do with 40K's Engagement Range, and vice versa.

---

## Open questions

- Whether any owned team's unique rules grant a third order state or modify Conceal/Engage behaviour - unread team pointers (`raw/pointers/kill_team_2024_teams.md`).
- Exact interaction between Conceal and the Guard action across killzones with heavy Vantage terrain - Wahapedia's fragment on Guard notes it is "treated as a Shoot action," which by the table above should make it unavailable on Conceal; confirm this reading against the owned PDF before teaching it as settled.

---

## Related pages

- [[activations_apl]] - where the order is chosen, at the top of every activation
- [[cover_kill_team]] - how cover interacts differently with each order
- [[valid_target]] - the selection test
- [[control_range_kill_team]] - the zone that Conceal's cover exemption depends on
- [[kill_team_2024_core_rules]] - source
- [[glossary]] - the "Engage" / "Engagement Range" collision flag
- [[index]]
