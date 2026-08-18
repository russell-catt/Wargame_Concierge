---
title: Cover (Kill Team 2024)
type: concept
system: kill_team_2024
created: 2026-08-17
updated: 2026-08-18
version: 0.5.0
sources: [kill_team_2024_core_rules, games/kill_team_2024/rules/Key_Concepts.md, games/kill_team_2024/rules/Keyword_Glossary.md, games/kill_team_2024/rules/Target_Eligibility.md, games/kill_team_2024/setup/Terrain_Basics.md]
confidence: draft
tags: [concept, kill_team_2024, core_rules, cover, obscured, vantage, collision_flag]
---

# Cover (Kill Team 2024)

**This page describes Kill Team's Cover rule, which is a different mechanic from Warhammer 40,000's Cover rule despite sharing the name.** Read the collision section before using "cover" in any cross-system sentence.

**L1 flag, then replace:** the 2026-08-17 Wahapedia draft is superseded below. Cover save, same-feature pick-one, 1"-ignores-only-that-part, Vantage Accurate, and **connected = same terrain feature** are aligned to shipping + owned PDFs **2026-08-18**. The page stays `draft` overall (not every terrain interaction was re-read); targeting-adjacent claims cite [[valid_target]] (`verified` subset).

One-line summary: KT24 Cover is a defender-dice bonus (and can make a Conceal target illegal); Obscured is a separate Heavy check; they cannot both apply from the same feature.

---

## The mechanic

An operative is **in cover** from a specific other operative if there is **intervening** terrain within its **control range**, and it is more than **2"** from that operative. Cover is per pair, not a global property of a ruin.

Two different effects:

1. **Targeting.** A **Conceal** operative in cover is **not a valid target**. An **Engage** operative in cover is still a valid target ([[orders_conceal_engage]], [[valid_target]]).
2. **Cover save.** When a target in cover is shot, the defender **collects three** defence dice, **retains one normal success without rolling**, and **rolls the remainder**. Saturate blocks retaining a cover save. A retained cover-save / Accurate die has **no numerical result**, cannot be re-rolled, and can only be retained once (Severe may **change** a retained die).

**Obscured** is a separate check: intervening **Heavy**. Being within 1" of Heavy ignores **only that part** of the feature, not the whole ruin. Effect: attacker **discards one success** of their choice, and remaining successes cannot be critical that sequence.

**Same feature, pick one.** A target cannot be in cover **and** obscured from the **same terrain feature** — the defender chooses (Jun 17 update log). "Heavy connected to Vantage" means any part of the **same terrain feature**.

**Vantage (SEQUENCE, not eligibility):** shooting an Engage target from Vantage, the weapon gains Accurate 1 if the target is at least 2" lower, or Accurate 2 if at least 4" below (Full-Scan p.60). Seek Light interaction is a FAQ on the quote appendix — see [[valid_target]].

---

## Why it matters at the table

- **Opposite of 40K cover.** KT24 helps the *defender's dice* (or removes the target). 40K 11e worsens the *attacker's* Ballistic Skill.
- **Conceal + terrain is the hide; Engage + terrain is a save.** Same wall, different order, different game.
- **2" denial.** Point-blank shots strip cover. Do not treat a barricade as permanent concealment against someone already in your face.
- **Pick cover vs obscured.** Cover save vs discarding an attack success and killing crits: against a low-volume high-crit gun, obscured can be the better pick.

---

## Kill Team vs 40K - do not conflate (collision flag)

| | Kill Team 2024 | Warhammer 40,000 11e |
|---|---|---|
| **What cover does** | Defender retains one normal defence success, or Conceal becomes illegal | Attacker's Ballistic Skill worsens by 1 |
| **Orders** | Conceal vs Engage changes whether cover blocks *selection* | No order system |
| **Range** | Intervening terrain in the target's 1" control range; denied within 2" | Terrain rules in 40K `Terrain_Basics.md`; no universal 2" denial |

See [[glossary]] for both Cover entries.

---

## Open questions

- Killzone-specific part types: see [[kill_team_terrain]] and [[killzones_volkus_tomb_world]] rather than inventing them here.
- Smoke (universal equipment): wholly within, obscured to operatives more than 2" (and vice versa) — indexed on Patch_Manifest, not expanded here.

---

## Related pages

- [[valid_target]] — selection test
- [[orders_conceal_engage]] — cover's targeting effect only applies to Conceal
- [[control_range_kill_team]] — the range cover is checked within
- [[kill_team_terrain]] — Heavy / Light / Vantage parts
- [[kill_team_2024_core_rules]] — source
- [[glossary]] · [[index]]
- Shipping: [`Key_Concepts.md`](../../games/kill_team_2024/rules/Key_Concepts.md), [`Terrain_Basics.md`](../../games/kill_team_2024/setup/Terrain_Basics.md), [`Patch_Manifest.md`](../../games/kill_team_2024/rules/Patch_Manifest.md)
