---
title: Cover (Kill Team 2024)
type: concept
system: kill_team_2024
created: 2026-08-17
updated: 2026-08-17
sources: [kill_team_2024_core_rules]
confidence: draft
tags: [concept, kill_team_2024, core_rules, cover, obscured, collision_flag]
---

# Cover (Kill Team 2024)

**This page describes Kill Team's Cover rule, which is a different mechanic from Warhammer 40,000's Cover rule despite sharing the name.** Read the collision section below before using "cover" in any cross-system sentence.

---

## The mechanic

An operative is **in cover** (from a specific other operative, usually a would-be shooter) if there is intervening terrain within its **control range** - but it can never be in cover while within 2" of the operative checking. Cover is checked per pair of operatives, not as a battlefield-wide property of a piece of terrain.

Cover's two effects, and they are different effects triggered at different points:

1. **Targeting.** A **Conceal**-ordered operative in cover is **not a valid target at all** - it cannot be shot. An **Engage**-ordered operative in cover is still a fully valid target (see [[orders_conceal_engage]]).
2. **Defence dice ("cover save").** If an Engage operative in cover *is* shot, its controlling player gets to **retain one normal success on their defence roll automatically**, without rolling it, before rolling their remaining defence dice as normal.

**Obscured is a separate, related check** with its own trigger (intervening *Heavy* terrain specifically, and never within 1" of either operative), and its own effect on the *attacker's* dice: the attacker must discard one success of their choice, and any critical successes are downgraded to normal successes for that shot. An operative can be in cover **or** obscured from the same terrain feature, never both at once - the defender chooses which applies if both would otherwise trigger.

---

## Why it matters at the table

- **Cover in KT24 is a defence-dice bonus, not an accuracy penalty on the shooter.** This is the exact inverse of how 40K 11e's cover works - see the collision section.
- **Cover's targeting effect only fires for Conceal.** Positioning an Engage operative in identical terrain gets it the cover save when shot at, but does nothing to stop it being targeted in the first place. If you want an operative to disappear from the enemy's target list entirely, it needs both the terrain *and* the Conceal order.
- **The 2" cover-denial rule punishes point-blank shots.** Terrain stops being "cover" the moment the shooter closes to within 2" of the target, which discourages using cover as a permanent screen against an enemy that has already closed the distance.
- **Obscured and cover are mutually exclusive per shot, defender's choice.** Know which one is better for you in the moment: cover gives you a free retained success; obscured takes away one of the attacker's successes and downgrades their crits. Against a low-volume, high-accuracy shooter, obscured (denying a crit) can matter more than the cover save.

---

## Kill Team vs 40K - do not conflate (collision flag)

| | Kill Team 2024 | Warhammer 40,000 11e |
|---|---|---|
| **What cover does** | Grants the *defender* one free retained defence success ("cover save") | Worsens the *attacker's* Ballistic Skill by 1 - see the shipping [`Keyword_Glossary.md`](../../games/warhammer_40k_11e/rules/Keyword_Glossary.md) "Benefit of cover" entry |
| **Who it can protect** | Only a target that is otherwise a valid target - and it can make a **Conceal** operative not a valid target at all | Any eligible unit in cover; there is no order system to interact with |
| **Range/trigger** | Intervening terrain within the target's 1" control range, denied within 2" of the shooter | Determined by the terrain rules in [`Terrain_Basics.md`](../../games/warhammer_40k_11e/setup/Terrain_Basics.md); no universal 2" denial rule |

**These are not the same rule with different numbers - they are opposite mechanical directions** (attacker penalty vs defender bonus). This is flagged explicitly in [[glossary]] because it is exactly the kind of term collision that causes a table mistake if a player carries a 40K habit into a Kill Team game, or vice versa.

---

## Open questions

- Whether any owned killzone (Volkus, Shadowhunt, Tomb World terrain, etc.) defines terrain features with non-default cover/Vantage properties - unread killzone pointers.
- The Vantage-terrain interaction mentioned in third-party KT24 reviews (Vantage now grants cover, plus `Accurate 1/2` for shooters on Vantage against Engage targets) was not confirmed on the Wahapedia core-rules page read this pass - needs its own cross-check before teaching as core rule rather than reviewer summary.

---

## Related pages

- [[orders_conceal_engage]] - cover's targeting effect only applies to Conceal
- [[control_range_kill_team]] - the range cover is checked within
- [[kill_team_2024_core_rules]] - source
- [[glossary]] - the Cover collision-flag entry, both systems side by side
- [[index]]
