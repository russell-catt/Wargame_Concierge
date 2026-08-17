<!--
FILE: games/kill_team_2024/rules/Key_Concepts.md
VERSION: v1.0 (2026-08-17)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, slice S1)

DOCUMENT_TYPE: Teaching Guide / Core Mechanics
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: Kill Team - 2024 / 3rd Edition (KT24)
REFERENCE_STATUS: Draft - written from the living Wahapedia core rules page; not yet cross-checked against the owned Core Rules PDF

SOURCES:
  - raw/pointers/kill_team_2024_core.md (points at C:\Personal\Kill Team\kill_team_2024\779937548-Core-Rules-KILL-TEAM-3E-Full-Scan.pdf - not yet opened this slice)
  - https://wahapedia.ru/kill-team3/the-rules/core-rules/ (retrieved 2026-08-17)
  - https://wahapedia.ru/kill-team3/the-rules/approved-ops-2025/ (retrieved 2026-08-17)
  - KB/concepts/activations_apl.md, KB/concepts/orders_conceal_engage.md, KB/concepts/control_range_kill_team.md, KB/concepts/cover_kill_team.md, KB/concepts/injured_operatives.md (Librarian L1, landed in parallel with this slice - same living source, cross-checked as consistent)

PURPOSE:
  Explain the mechanics everything else in Kill Team is built from: APL and
  activation, Orders, control range, cover, the attack sequence, Injured, and
  a high-level look at mission scoring.

PRIMARY_AUDIENCE:
  - A beginner who knows the two-phase turning-point structure and now needs
    to know how an activation actually resolves
  - Later slices needing shared mechanical vocabulary

KEY_SECTIONS_EXPECTED:
  - Reading a datacard
  - APL and activation
  - Orders - Conceal vs Engage
  - Control range
  - Cover and Obscured
  - The Shoot sequence
  - The Fight sequence
  - Damage, Wounded, and Injured
  - Mission scoring at a high level

UPDATE_TRIGGER:
  Update when a new Core Rules printing or errata changes APL rules, Orders,
  control range, cover, the attack sequence, or the Approved Ops scoring
  framework.
-->

# Key Concepts - the mechanics everything else sits on

A handful of ideas carry almost the whole game. Learn these and most datacard text becomes readable.

Written from the living Wahapedia core rules page, retrieved **2026-08-17**. Status: `draft` - not yet cross-checked against the owned Core Rules PDF.

---

## Reading a datacard

Every operative has a **datacard**: its stats, weapons, abilities, and keywords. The profile stats are:

| Stat | What it means |
|------|---------------|
| **APL** | Action Point Limit - the total AP an operative can spend during one activation |
| **Move** | Distance in inches for Reposition, Fall Back, and Charge |
| **Save** | The dice result needed on defence dice when the operative is shot or fought |
| **Wounds** | Starting wounds; reduced as damage lands |

Weapons carry **Atk** (attack dice rolled), **Hit** (result needed to score a success), and two **Dmg** values - Normal Dmg and Critical Dmg. Weapon rules such as `Blast X` or `Torrent X` appear alongside the weapon. Keywords in KEYWORD BOLD identify the operative for other rules; orange keywords with a skull are **faction keywords**, shared by every operative in that kill team.

> **We never reproduce datacard statlines in this repository.** Look them up in your kill team's rules or the Kill Team app.

---

## APL and activation

An operative's **Action Point Limit (APL)** is the AP it can spend in one activation. Each action has an AP cost; you cannot exceed the operative's APL, and (with rare exceptions) it cannot perform the **same action twice** in one activation.

**The ±1 cap.** Rare rules can raise or lower an operative's APL for an activation, but no matter how many separate rules apply, the net change is capped at **-1 or +1 from its normal APL** - this cap overrides the individual modifiers. An operative with a base APL of 2 can never be pushed below 1 or above 3 by stacking modifiers.

You do not have to declare a full activation up front: perform one action, see what happened, then choose the next.

Full concept page: [`../../../KB/concepts/activations_apl.md`](../../../KB/concepts/activations_apl.md).

---

## Orders - Conceal vs Engage

Every operative sits on one of two **orders**, chosen fresh each time it activates:

| Order | Can do | Can't do | Targeting effect |
|-------|--------|----------|-------------------|
| **Engage** | Everything - move, Shoot, Charge, Fight, counteract | - | A valid target whenever it is visible |
| **Conceal** | Move, Fight, most non-Shoot/Charge actions | Cannot Shoot, cannot Charge, cannot counteract | **Not a valid target while it is also in cover** - visible or not |

Operatives start the battle on Conceal. The trade is the whole game in miniature: Engage operatives can act fully but are shootable the instant they are visible; Conceal operatives trade offence for safety, and only actually get that safety when they are also standing in cover. A Conceal operative caught in the open is still a fully valid target.

Full concept page: [`../../../KB/concepts/orders_conceal_engage.md`](../../../KB/concepts/orders_conceal_engage.md).

---

## Control range

**Control range** is the tightest-radius rule in the game, and it is doing constant work: something is within an operative's control range if it is **visible to, and within 1"** of that operative. It is mutual - if A is in B's control range, B is in A's control range too.

Control range governs:

- Whether you are **engaged** enough to Fight, or must Fall Back instead of Reposition
- Whether terrain is **intervening** for cover purposes
- Whether an operative is **in cover** at all (an operative cannot claim cover from something that isn't intervening within its own control range)
- **Contesting and controlling markers** - operatives contest a marker if it is within their control range; the side with the higher **total APL** contesting it controls it

> **40K collision:** do not confuse this with 40K's Engagement Range (2" horizontal / 5" vertical). Kill Team's control range is **1", visibility-gated, and does far more than gate melee** - it is also the basis for cover and for controlling markers. See [`Keyword_Glossary.md`](Keyword_Glossary.md).

Full concept page, with a side-by-side collision table: [`../../../KB/concepts/control_range_kill_team.md`](../../../KB/concepts/control_range_kill_team.md).

---

## Cover and Obscured

Two separate, stackable effects apply based on terrain between two operatives - checked from one operative's control range, not a straight blocking line:

| Effect | Trigger | What it does |
|--------|---------|--------------|
| **Cover** | Intervening terrain is within the *target's* control range (and the target is more than 2" from the shooter) | A Conceal target in cover is not a valid target at all. An Engage target in cover gives the defender **one free retained normal success** on defence dice (a **cover save**) before rolling the rest |
| **Obscured** | Intervening **Heavy** terrain lies between the two operatives, more than 1" from both | The attacker must **discard one success of their choice**, and none of their successes can be critical that activation |

A target can be in cover *or* obscured by the same terrain feature, never both from the same feature at once - the defender's controller picks which applies if both would otherwise be true.

Full concept page, with the 40K collision table: [`../../../KB/concepts/cover_kill_team.md`](../../../KB/concepts/cover_kill_team.md).

---

## The Shoot sequence

Shooting is one operative's action, resolved attacker-then-defender:

1. **Select weapon and target.** Pick one ranged weapon; the target must be a **valid target** (visible; and if it's on Conceal, also not in cover) with no friendly operative in its control range.
2. **Roll attack dice** - one D6 per the weapon's Atk stat. Meet or beat the weapon's Hit stat for a success; an unmodified 6 is always a **critical success**, an unmodified 1 is always a fail. If the target is **obscured**, discard one success and cap the rest at normal.
3. **Roll defence dice** - the defender rolls three D6 (minus one, replaced by a free normal success, if the target is in cover), each needing to meet or beat the operative's Save stat.
4. **Resolve defence dice.** The defender allocates successes to block: a normal success blocks a normal success; two normal successes block a critical success; a critical success blocks either.
5. **Resolve attack dice.** Every unblocked success inflicts damage - Normal Dmg for a normal success, Critical Dmg for a critical success.

---

## The Fight sequence

Fighting works differently from Shooting: **both** players roll and both can hurt each other in the same action.

1. **Select enemy and weapons.** The active operative picks an adjacent (in control range) enemy operative to fight; both players pick one melee weapon each.
2. **Roll attack dice simultaneously.** Same success/critical rules as shooting. A friendly operative **assisting** (also in that enemy's control range, and not in any other enemy's control range) improves the fighting operative's Hit stat by 1 per assist.
3. **Resolve attack dice, alternating, attacker first.** Each player in turn resolves one of their own successes as either a **strike** (inflict damage immediately) or a **block** (cancel one of the opponent's still-unresolved successes). This continues until one side is out of successes or one operative is incapacitated.

There is no separate "save roll" in melee - defence is entirely about racing to strike first or spending your own successes to block theirs.

---

## Damage, Wounded, and Injured

- **Damage** reduces an operative's remaining **Wounds**. At 0 or below, it is **incapacitated** and removed from the killzone (some rules let it perform one free action first).
- **Wounded** simply means "has taken damage" - fewer than its starting Wounds remaining.
- **Injured** is the harder threshold: fewer than **half** its starting Wounds remaining. An injured operative suffers **-2" Move** and its weapons' **Hit stat worsens by 1**. There is no squad-level morale test in Kill Team - Injured is the game's pressure mechanic, applied operative by operative.

> **40K collision:** Kill Team has no Battle-shock equivalent. Its closest analogue to "a unit under pressure" is Injured, which weakens one operative individually rather than testing a whole squad's Leadership.

Full concept page: [`../../../KB/concepts/injured_operatives.md`](../../../KB/concepts/injured_operatives.md).

---

## Mission scoring at a high level

Kill Team does not score primarily by counting bodies. Under the current **Approved Ops 2025** matched-play pack, VP come from three named **ops**, each capped at 6VP:

| Op | Scores for |
|----|-----------|
| **Crit Op** | Mission actions and controlling objective markers |
| **Kill Op** | Incapacitating enemy operatives |
| **Tac Op** | A secretly-chosen secondary objective from your kill team's archetype (Infiltration, Recon, Security, Seek & Destroy) |

Each player also secretly locks in one op as their **primary op** during the first turning point (a Strategic Gambit) and scores a bonus for it at battle's end. This is intentionally high-level - Approved Ops card text and per-mission Tac Op wording are not reproduced here. Casual and narrative mission packs (Volkus, Shadowhunt, the 3e Starter Set) use their own, usually simpler, objective structure - always check the mission pack you are actually playing.

> **40K collision:** "Kill Op" sounds like straightforward kill-count scoring, and largely is - but do not assume it behaves like 40K's secondary missions. It is one of exactly three ops in a fixed, capped framework, not one card among many.

---

## Related pages

- [`Overview.md`](Overview.md) - what a game is and how you win
- [`Turn_Structure.md`](Turn_Structure.md) - when each of these comes up
- [`Keyword_Glossary.md`](Keyword_Glossary.md) - one-line definitions for every term above, with 40K collisions flagged
- [`../../../KB/concepts/activations_apl.md`](../../../KB/concepts/activations_apl.md), [`../../../KB/concepts/orders_conceal_engage.md`](../../../KB/concepts/orders_conceal_engage.md), [`../../../KB/concepts/control_range_kill_team.md`](../../../KB/concepts/control_range_kill_team.md), [`../../../KB/concepts/cover_kill_team.md`](../../../KB/concepts/cover_kill_team.md), [`../../../KB/concepts/injured_operatives.md`](../../../KB/concepts/injured_operatives.md) - the Librarian's concept pages for this material, landed in parallel

---

## Change Log
- v1.0 (2026-08-17): Initial core mechanics guide (slice S1), from the living Wahapedia core rules and Approved Ops 2025 pages, both retrieved 2026-08-17. Cross-cited against five KB concept pages (`activations_apl`, `orders_conceal_engage`, `control_range_kill_team`, `cover_kill_team`, `injured_operatives`), landed by the Librarian (L1) in parallel with this slice from the same source.

## Attribution
- Project: Wargame_Concierge
- Maintainer: Russell Catt
- Kill Team is a trademark of Games Workshop Limited. This document is a personal teaching paraphrase and reproduces no publisher text or datacard statlines.

## Rising Tide Notes
- This document follows Rising Tide documentation standards.
- **Verify before you play.** Cross-check anything here against the owned Core Rules PDF - this page currently rests on a living web source only, retrieved **2026-08-17**.
