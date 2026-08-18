---
title: Valid Target
type: concept
system: kill_team_2024
created: 2026-08-18
updated: 2026-08-18
version: 0.5.0
sources: [kill_team_2024_core_rules, games/kill_team_2024/rules/Target_Eligibility.md, games/kill_team_2024/rules/Key_Concepts.md, games/kill_team_2024/rules/Keyword_Glossary.md]
confidence: verified
tags: [concept, kill_team_2024, core_rules, valid_target, shooting, targeting]
---

# Valid Target

The shooter's first question: is this enemy even legal to pick? **Valid target** is a selection test, not a damage test. Teaching paraphrase of shipping [`Target_Eligibility.md`](../../games/kill_team_2024/rules/Target_Eligibility.md) (owner-verified **2026-08-18**). Quotes stay in that appendix; this page does not reproduce them.

**L1 note (flag, then replace):** the 2026-08-17 Wahapedia draft treated targeting as a glossary stub only. This page is new, written from owner-verified shipping, not from that aggregator pass.

---

## The mechanic

An enemy is a **valid target** if:

1. It is **visible** to the operative doing the selecting (Shoot step wording: visible to the **active** operative).
2. **Order split:**
   - **Engage** — visible is enough.
   - **Conceal** — visible **and not in cover**.
3. For a **Shoot** action, no friendly operative is in the target's **control range**.

**Visible** is a 1 mm-wide unobstructed line from the shooter's head to any part of the target miniature. **In cover** is intervening terrain within the *target's* control range, and it is denied while the target is within 2" of the active operative. See [[cover_kill_team]] and [[orders_conceal_engage]].

Cover and **obscured** are different checks. Obscured (intervening Heavy) does **not** stop selection; it changes the attacker's dice after a valid target is chosen. A target cannot be in cover *and* obscured from the **same terrain feature** — the defender picks one (Jun 17 update log).

---

## Why it matters at the table

- **Conceal in cover is the hide.** Flip to Engage, or leave cover, and the same miniature is suddenly legal.
- **Closing to 2" strips cover.** A Conceal operative that felt safe behind a barricade is a valid target once you are on top of it.
- **Blast vs Torrent.** Blast secondaries are **not selected** as valid targets (they still resolve, and they copy the primary's cover/obscured). Torrent secondaries **must themselves be valid targets** and not in friendly control range.
- **Seek / Seek Light** (Vantage FAQ): you may elect Seek Light only in the stated Vantage case — it is a selection modifier, not a new order. Confirm the printed sentence in the quote appendix when it matters.
- **Heavy is a shooter gate, not a valid-target gate.** You cannot use a Heavy weapon in an activation **or counteraction** in which the operative moved (Heavy (x only) allows that move). Heavy **does not prevent Guard**.

**Volkus Door Fight** and Close Quarters **Guard** patches are killzone extras — they do not belong on the core valid-target tree. See [[killzones_volkus_tomb_world]].

---

## Kill Team vs 40K - do not conflate

40K has no "valid target" order test. Benefit of cover there worsens the attacker's Ballistic Skill; it does not make a unit illegal to choose. Do not import 40K "I can see you, so I can shoot you" into a Conceal-in-cover situation.

---

## Open questions

- Full-Scan print revision vs any later WarCom core download — targeting quotes are owner-verified 2026-08-18 against the owned Full-Scan + Jun 17 log + Jul 25 lite.
- Team-specific "cannot be selected" rules stay on team pages (out of scope this pass).

---

## Related pages

- [[cover_kill_team]] — cover, obscured, cover save, Vantage / connected
- [[orders_conceal_engage]] — Engage vs Conceal
- [[control_range_kill_team]] — 1" visibility-gated zone
- [[kill_team_terrain]] — intervening, Heavy, Light, Vantage
- [[kill_team_2024_core_rules]] — source + hierarchy
- [[glossary]] · [[index]]
- Shipping: [`Target_Eligibility.md`](../../games/kill_team_2024/rules/Target_Eligibility.md), [`Target_Eligibility_Cheat_Sheet.html`](../../games/kill_team_2024/rules/Target_Eligibility_Cheat_Sheet.html), [`Patch_Manifest.md`](../../games/kill_team_2024/rules/Patch_Manifest.md)
