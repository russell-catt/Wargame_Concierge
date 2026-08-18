<!--
FILE: games/kill_team_2024/rules/Target_Eligibility.md
VERSION: v0.5.0 (2026-08-18)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, slice P / quote restore; p.60 SELECT owner transcription)

DOCUMENT_TYPE: Rules Quote Appendix
GAME_SYSTEM: Kill Team — 2024 / 3e (KT24)
REFERENCE_STATUS: Owner verified 2026-08-18 against Full-Scan + Jun 17 update log + Jul 25 lite — personal use only; never for sale

SOURCES:
  - C:\Personal\Kill Team\kill_team_2024\779937548-Core-Rules-KILL-TEAM-3E-Full-Scan.pdf (read in place; image scan — transcribed 2026-08-17, owner-verified 2026-08-18)
  - C:\Personal\Kill Team\kill_team_2024\eng_jul25_kt_lite_rules-jmjv4hdamy-qlsqxdf83p.pdf
  - C:\Personal\Kill Team\kill_team_2024\eng_17-06_kill_team_key_downloads_core_rules_update_log-9dzdz0ewle-wutcyhpgzf.pdf
  - C:\Personal\Kill Team\kill_team_2024\eng_17-06_kill_team_key_downloads_universal_equipment-prsd0j8pih-ikfmigl0za.pdf
  - games/kill_team_2024/rules/Patch_Manifest.md

PURPOSE:
  Every core rule that gates or modifies selecting a valid target for Shoot.
  Each block is verbatim from a golden local PDF with filename + page cite.
  Obscured and Saturate are labelled for selection vs shooting sequence.

UPDATE_TRIGGER:
  Update when core rules update log or owned Full-Scan revision changes.
-->

# Target eligibility — quote appendix

**Personal use only. Never for sale.** Quotes from owned local PDFs only; read in place at `C:\Personal\Kill Team\kill_team_2024\`.

**Source hierarchy:** Full-Scan Core Book is the baseline. Dated `eng_*` patches (Jun 17 update log, team PDFs, universal equipment) supersede on the same topic. Jul 25 lite is a **simplified intro** (lite p.1) — confirm short wording; **omission is not a patch.** Do not drop Core or update-log sentences because lite omitted them. Use lite over unpatched Full-Scan only where lite restates errata (Heavy counteract / Guard; Severe Punishing/Rending).

**Full-Scan note:** The Core Book PDF is image-only (no text layer). Quotes below from Full-Scan were transcribed from the owned scan on **2026-08-17** and owner-verified **2026-08-18**. Cross-check against your physical book if anything looks off.

Owner typing nits in pastes (then/than, ussing/using, precedance) were corrected to printed English. Printed difference **p.42 "active operative"** vs **p.55 "the operative"** is kept as printed.

---

## How to use this file

| Label | Meaning |
|-------|---------|
| **SELECT** | Governs whether an enemy operative may be chosen as a valid target |
| **SEQUENCE** | Applies after a valid target is selected (does not change eligibility) |
| **TERRAIN** | Terrain type definitions that feed cover / obscured / intervening |

Table disputes: this file is the quote appendix. Teaching paraphrase lives in [`Key_Concepts.md`](Key_Concepts.md) and [`Keyword_Glossary.md`](Keyword_Glossary.md). Patch ledger: [`Patch_Manifest.md`](Patch_Manifest.md).

---

## Valid target (Key Principles)

**Source:** `779937548-Core-Rules-KILL-TEAM-3E-Full-Scan.pdf` — p.55 — **SELECT**

> Some rules require you to select a valid target for an operative. This is most common when an operative is shooting, but some rare rules require it too.
>
> If the intended target has an **Engage order**, it's a valid target if it's **visible** to the operative.
>
> If the intended target has a **Conceal order**, it's a valid target if it's **visible** to the operative and **not in cover**.

---

## Valid target (Shoot action — Select Valid Target step)

**Source:** `779937548-Core-Rules-KILL-TEAM-3E-Full-Scan.pdf` — p.42 — **SELECT**

> **2. Select Valid Target**
>
> The attacker selects an enemy operative that's a valid target and has no friendly operatives within its control range.
>
> If the intended target has an Engage order, it's a valid target if it's visible to the active operative.
>
> If the intended target has a Conceal order, it's a valid target if it's visible to the active operative and not in cover.
>
> An operative is **visible** if the active operative can see it.
>
> An operative is **in cover** if there's intervening terrain within its control range. However, it cannot be in cover while within 2" of the active operative.

**Source:** `eng_jul25_kt_lite_rules-jmjv4hdamy-qlsqxdf83p.pdf` — p.2 — **SELECT** *(lite restatement of Shoot step 2)*

> 2. Attacker selects an enemy operative that's a valid target for the **active** operative and has no friendly operatives within its control range.

p.42 says **visible to the active operative**; p.55 says **visible to the operative**. Both are printed as-is — not an OCR error.

**Patch reminder:** Update log p.2 adds cover/obscured mutual exclusion after this Full-Scan text. That sentence is not on Full-Scan p.42. Effective table rule = p.42 + the errata block below.

---

## Select Valid Target — cover and obscured mutual exclusion (errata)

**Source:** `eng_17-06_kill_team_key_downloads_core_rules_update_log-9dzdz0ewle-wutcyhpgzf.pdf` — p.2 — **SELECT**

> **ACTIONS, SHOOT, SELECT VALID TARGET**
>
> Add following text:
>
> 'An operative cannot be in cover from and obscured by the same terrain feature. If it would be, the defender must select one of them (cover or obscured) for that sequence when their operative is selected as the valid target.'

Jul 25 lite does **not** restate this sentence. Keep applying the update log.

---

## Conceal order (not a valid target while in cover)

**Source:** `779937548-Core-Rules-KILL-TEAM-3E-Full-Scan.pdf` — p.54 — **SELECT**

> **Conceal Order**
>
> The operative cannot perform Shoot and Charge actions, and it cannot counteract. However, **it's not a valid target while it's in cover**.

> Operatives are given a Conceal order when they are set up before the battle. You can change an operative's order whenever it's activated.

**Source:** `eng_jul25_kt_lite_rules-jmjv4hdamy-qlsqxdf83p.pdf` — p.1 — **SELECT** *(lite restatement)*

> An operative with a Conceal order is not a valid target while in cover, but it cannot perform Shoot or Charge actions.

Lite p.1 omits **counteract**. That is shortening, not a patch — Full-Scan Conceal still cannot counteract unless a team rule lifts it.

Order-token ready/expended sides are **Turn_Structure**, not valid-target. Rest of Full-Scan p.54 is Ploys — not harvested here.

---

## Engage order

**Source:** `779937548-Core-Rules-KILL-TEAM-3E-Full-Scan.pdf` — p.54 — **SELECT**

> **Engage Order**
>
> The operative can perform actions as normal and can counteract.

---

## Visible

**Source:** `779937548-Core-Rules-KILL-TEAM-3E-Full-Scan.pdf` — p.55 — **SELECT**

> For something to be **visible**, the operative must be able to see it. To check visibility, look from behind the operative and determine if you can draw an unobstructed straight line 1mm in diameter from its head to any part of what it's trying to see. **Ignore operatives' bases** when determining this. An operative is always visible to itself.

**Source:** `eng_jul25_kt_lite_rules-jmjv4hdamy-qlsqxdf83p.pdf` — p.2 — **SELECT** *(lite restatement)*

> For something to be visible, the operative must be able to see it (look from behind the operative and see if you can draw an unobstructed straight line from its head to any part of what it's trying to see — excluding bases).

Lite omits **1mm diameter** and **always visible to itself**. Keep the Core extras. Do not strip them because lite is shorter.

---

## Cover

**Source:** `779937548-Core-Rules-KILL-TEAM-3E-Full-Scan.pdf` — p.47 — **SELECT**

> Cover is determined from one operative to another, usually when one of them is shooting. An operative is **in cover** if there's **intervening terrain within its control range**. However, it cannot be in cover while within 2" of the other operative. Intervening is explained on pg 51.

**Source:** `779937548-Core-Rules-KILL-TEAM-3E-Full-Scan.pdf` — p.47 — sidebar — **SELECT**

> An operative in cover with a Conceal order is not a valid target. An operative in cover with an Engage order is a valid target, but has a cover save (see Shoot action on pg 42).

"See Shoot action on pg 42" means the Shoot **action starts** on 42. Cover-save dice are on **p.43** (SEQUENCE, below).

**Source:** `eng_jul25_kt_lite_rules-jmjv4hdamy-qlsqxdf83p.pdf` — p.2 — **SELECT** *(lite restatement)*

> Cover is determined from one operative to another. An operative is in cover if there's intervening terrain within its control range. However, it cannot be in cover while within 2" of the other operative — it's too close to hide.

p.42 uses **within 2" of the active operative**; p.47 / lite use **within 2" of the other operative**. Same 2" gate; keep both as printed.

**Teaching note (p.47 diagrams, not extra rules):** Cover needs intervening terrain **and** that terrain within the target's 1" control range **and** the other operative more than 2" away. Terrain in 1" control range that is not intervening is not cover. Intervening terrain not in 1" control range is not cover. Within 2" you cannot be in cover ("too close to hide" on lite).

Wounds-tracking and incapacitated-before-removal from the same p.47 sidebar are **not** eligibility — see [`Key_Concepts.md`](Key_Concepts.md).

---

## Intervening and targeting lines

**Source:** `779937548-Core-Rules-KILL-TEAM-3E-Full-Scan.pdf` — p.51 — **SELECT / TERRAIN**

> Rules such as cover and obscured require you to determine if something is **intervening**, e.g. terrain. Most of the time this is easily determined – if it's between the operative and the intended target, it's intervening. Sometimes this will be unclear, so we use **targeting lines**.
>
> To use targeting lines, the operative's player draws imaginary straight lines 1mm in diameter from any point of its base to every facing part of the intended target's base. Anything at least one of these lines cross is intervening. Anything all of these lines cross is **wholly intervening**.
>
> Most commonly, targeting lines can be drawn in a two-dimensional (top down) manner for ease. However, if there's a difference in height between the operatives (e.g. one of them is on Vantage terrain), targeting lines should be drawn in a three-dimensional manner.

**Source:** `779937548-Core-Rules-KILL-TEAM-3E-Full-Scan.pdf` — p.51 — sidebar — **SELECT / TERRAIN**

> The operative's player decided from which point of the base targeting lines are drawn from. This can allow the operative to get a more favourable targeting angle - imagine the operative leaning right or left as appropriate.
>
> Intervening is determined from one operative to another, but some rare rules will require you to determine it from other things such as markers. In such instances, treat all parts of that thing as the 'base' when determining this.

**Teaching note (p.51 diagrams):** Origin choice on your own base can make a feature intervening or not. Wholly intervening = **all** targeting lines. Do not confuse that with smoke **wholly within** an area (universal equipment).

---

## 1" control range

**Source:** `779937548-Core-Rules-KILL-TEAM-3E-Full-Scan.pdf` — p.46 — **SELECT**

> Many rules relate to control range such as moving, fighting and using cover. Something is within an operative's **control range** if it's **visible to and within 1"** of that operative.
>
> Control range between operatives is mutual, therefore operatives are within each other's control range if one of them is visible to and within 1" of the other.

**Source:** `eng_jul25_kt_lite_rules-jmjv4hdamy-qlsqxdf83p.pdf` — p.2 — **SELECT** *(lite restatement)*

> Something is within an operative's control range if it's visible to and within 1" of that operative. Control range between operatives is mutual, therefore operatives are within each other's control range even if the above is only true for one of them.

**Source:** `779937548-Core-Rules-KILL-TEAM-3E-Full-Scan.pdf` — p.42 — **SELECT** *(friendly-in-1" control range gate)*

> The attacker selects an enemy operative that's a valid target and has **no friendly operatives within its control range**.

**Teaching note (p.46 diagrams):** 1" control range needs **visibility**, not just distance. Terrain can sit in an operative's 1" control range; two operatives within 1" of each other are **not** in each other's control range if terrain blocks visibility. That matters for "no friendly in the target's 1" control range" and "cannot Shoot while in enemy 1" control range."

---

## Enemy / friendly operatives

**Source:** `779937548-Core-Rules-KILL-TEAM-3E-Full-Scan.pdf` — p.54 — **SELECT**

> Operatives are the Citadel miniatures used in the game. **Your operatives are friendly operatives, and your opponent's operatives are enemy operatives.**

---

## Obscured

**Source:** `779937548-Core-Rules-KILL-TEAM-3E-Full-Scan.pdf` — p.53 — **SEQUENCE** *(target already valid)*

> Obscured is determined from one operative to another, usually when one of them is shooting. An operative is **obscured** if there's **intervening Heavy terrain**. However, it cannot be obscured by intervening Heavy terrain that's **within 1" of either operative**. Intervening is explained on pg 51.
>
> When an operative is shooting, if the target operative is obscured:
> - The attacker must discard one success of their choice instead of retaining it.
> - All the attacker's critical successes are retained as normal successes and cannot be changed to critical successes (this takes precedence over all other rules).

**Source:** `779937548-Core-Rules-KILL-TEAM-3E-Full-Scan.pdf` — p.53 — sidebar — **SEQUENCE / TERRAIN**

> Obscured is when an operative is a valid target, but intervening obstacles (usually terrain) make it a less efficient target. Imagine the operative having to target the enemy through the ruin or distant window.
>
> In other words, an operative being within 1" of a terrain feature doesn't prevent the whole terrain feature from being obscuring, only the part within 1" of the operative.

**Source:** `779937548-Core-Rules-KILL-TEAM-3E-Full-Scan.pdf` — p.42 — **SEQUENCE** *(Roll Attack Dice step — same obscured effect)*

> If the target operative is obscured:
> - The attacker must discard one success of their choice instead of retaining it.
> - All the attacker's critical successes are retained as normal successes and cannot be changed to critical successes (this takes precedence over all other rules).
>
> An operative is **obscured** if there's intervening Heavy terrain. However, it cannot be obscured by intervening Heavy terrain that's within 1" of either operative.

Hugging a ruin does **not** make the whole feature non-obscuring — only the **part** within 1" is ignored. A farther part of the same feature can still obscure. Update log p.2 still adds cover vs obscured from the **same** feature (defender picks one).

---

## Cover save (Shoot — defence dice)

**Source:** `779937548-Core-Rules-KILL-TEAM-3E-Full-Scan.pdf` — p.43 — **SEQUENCE**

> The defender collects three defence dice. If the target operative is in cover, they can retain one normal success without rolling it - this is known as a cover save. They roll the remainder.

Prefer this Full-Scan wording over Jul 25 lite p.2 (lite does not spell out collect-three / roll remainder as clearly). Saturate ("cannot retain cover saves") maps to this step.

**Teaching note (p.43 sidebar — owner summarised, not a full harvest):** Cover in this step usually applies to **Engage** — Conceal in cover would already have failed valid target. Blast / Torrent: operatives are not removed until the whole Shoot action is finished. Resolve Defence Dice (block table) and Resolve Attack Dice (Normal/Critical Dmg) stay in [`Key_Concepts.md`](Key_Concepts.md) — not this appendix.

**Teaching note (p.42 Roll Attack Dice success/fail/crit):** Owner confirmed those dice rules sit on Full-Scan p.42 with the obscured bullets above. Exact success/fail/crit sentences were not pasted for harvest — see the Core Book p.42 rather than a reconstructed quote.

---

## Terrain types (Light, Heavy, Blocking, Exposed, Vantage)

**Terrain parts — intro**

**Source:** `779937548-Core-Rules-KILL-TEAM-3E-Full-Scan.pdf` — p.58 — **TERRAIN**

> A terrain feature is composed of different parts, each of which is a type of terrain (one part can be more than one type). If you are using a terrain feature from a specific killzone, the type of each part of that terrain feature will be specified. If you are using a terrain feature from a killzone of your own creation, you must specify the type of each part of that terrain feature before the battle. The most common types of terrain are below, but some killzones have their own types.

**Teaching note (p.58 sidebar — owner summarised):** Always view terrain **in parts**, not as one feature of a single type. "Ignore Light terrain" means ignore **Light parts only**, not the whole feature. Same "parts not whole feature" idea as the p.53 obscured 1" sidebar. Mixture-of-Light-and-Heavy advice on that page is not a rule.

**Heavy — obscures**

**Source:** `779937548-Core-Rules-KILL-TEAM-3E-Full-Scan.pdf` — p.58 — **TERRAIN**

> Larger terrain is **Heavy**. It can obscure operatives.

**Light**

**Source:** `779937548-Core-Rules-KILL-TEAM-3E-Full-Scan.pdf` — p.59 — **TERRAIN**

> Smaller terrain is **Light**. It doesn't have any additional rules, but other rules interact with it differently (e.g. Vantage terrain on pg 60).

**Light on objective markers**

**Source:** `779937548-Core-Rules-KILL-TEAM-3E-Full-Scan.pdf` — p.59 — **TERRAIN** *(setup / eligibility-adjacent)*

> If you wish, objective markers can also have Light terrain using these miniatures. The 40mm base is still the marker, but the terrain attached to it is Light.

**Blocking**

**Source:** `779937548-Core-Rules-KILL-TEAM-3E-Full-Scan.pdf` — p.59 — **TERRAIN / SELECT**

> **Blocking** terrain is usually attributed to gaps between or underneath a terrain feature. **Visibility cannot be drawn through such gaps**, and for the purposes of cover and obscured, the gaps are intervening like the terrain around it.

**Teaching note (p.59 Blocking sidebar — owner summarised):** Blocking is **not physical terrain** — it is gaps operatives should not see through (rare, but needed). Examples on the page: gap under a pipe; door viewpoint; broken vent.

**Exposed — never intervening for cover/obscured**

**Source:** `779937548-Core-Rules-KILL-TEAM-3E-Full-Scan.pdf` — p.61 — **TERRAIN**

> **Exposed** terrain is usually very small, or terrain with large gaps that operatives shouldn't be able to take cover behind. For the purposes of cover and obscured, **it's never intervening**.

Accessible and Insignificant on p.61 are **movement**, not valid-target — see [`../setup/Terrain_Basics.md`](../setup/Terrain_Basics.md).

**Vantage — intro (also Light)**

**Teaching note (Full-Scan p.60 — TERRAIN / SELECT; owner summarised, not a full harvest):** Vantage is the upper levels you can be **placed** on. If terrain is **not** Vantage, you can move **over** it but cannot **finish a move or be set up** on it. **Vantage terrain is also Light terrain** — an operative on Vantage is often in cover vs lower shooters. See Core Book p.60.

**Vantage — Conceal + Light cover bypass**

**Source:** `779937548-Core-Rules-KILL-TEAM-3E-Full-Scan.pdf` — p.60 — **SELECT**

> Secondly, whenever you are selecting a valid target for an operative on Vantage terrain, operatives at least 2" lower than that operative with a Conceal order cannot use Light terrain for cover. Whilst this can allow such operatives to be targeted (assuming they're visible), it doesn't remove their cover save, and the defender can retain it as a critical success instead, or retain one additional cover save.

**Owner-verified 2026-08-18:** printed Core p.60 SELECT, owner transcription from the physical book.

**Vantage — Accurate vs Engage (SEQUENCE)**

**Teaching note (Full-Scan p.60 — SEQUENCE; owner summarised):** When shooting an **Engage** target from Vantage, the weapon gains **Accurate 1** if the target is at least 2" lower, or **Accurate 2** if at least 4" below. This does not change valid-target selection. See [`Key_Concepts.md`](Key_Concepts.md).

**Vantage — Heavy connected ignored for obscured**

**Source:** `779937548-Core-Rules-KILL-TEAM-3E-Full-Scan.pdf` — p.60 — **SEQUENCE**

> For the purposes of obscured, ignore Heavy terrain connected to Vantage terrain that the active operative or the intended target is on.

"Connected" = any part of the **same terrain feature** (update log p.5 commentary, quoted below). Vantage Conceal bypass and this obscured-ignore line both still apply.

Vantage movement around obstructions while staying on the level is setup, not eligibility.

---

## Weapon rules — valid target selection

**Source:** `779937548-Core-Rules-KILL-TEAM-3E-Full-Scan.pdf` — p.111 — unless noted

Do **not** dump the rest of the p.111 / lite p.3 weapon list into this appendix. Those rules are SEQUENCE (dice, damage, APL), not valid-target selection — except **Heavy** as a shooter gate (patched, below). **Severe** lives in [`Keyword_Glossary.md`](Keyword_Glossary.md) / [`Key_Concepts.md`](Key_Concepts.md).

### Range x — **SELECT**

> **Range x:** Only operatives within x of the active operative can be valid targets, e.g. Range 9".

**Source:** `eng_jul25_kt_lite_rules-jmjv4hdamy-qlsqxdf83p.pdf` — p.3 — **SELECT** *(lite)*

> Range x: Only operatives within x of the active operative can be valid targets, e.g. Range 9".

### Seek / Seek Light — **SELECT**

> **Seek:** When selecting a valid target, operatives with a Conceal order cannot use terrain for cover. If the rule is **Seek Light**, they cannot use **Light terrain** for cover. While this can allow operatives to be targeted (assuming they're visible), it doesn't remove their cover save (if any).

**Source:** `eng_jul25_kt_lite_rules-jmjv4hdamy-qlsqxdf83p.pdf` — p.3 — **SELECT** *(lite, identical wording)*

### Blast x — **SELECT** (secondary targets)

> **Blast x:** The target you select is the primary target. After shooting the primary target, shoot with this weapon against each secondary target in an order of your choice (roll each sequence separately). Secondary targets are other operatives visible to and within x of the primary target, e.g. Blast 2" (**they are all valid targets, regardless of a Conceal order**). Secondary targets are in cover and obscured if the primary target was.

**Source:** `eng_17-06_kill_team_key_downloads_core_rules_update_log-9dzdz0ewle-wutcyhpgzf.pdf` — p.2 — **SELECT** *(Torrent errata — same secondary-target pattern)*

> **APPENDIX, WEAPON RULES, TORRENT** — Change first sentence to read: 'Select a valid target as normal as the primary target, then select any number of other valid targets within x of the first valid target, but not within control range of friendly operatives, as secondary targets, e.g. Torrent 2".'

### Torrent x — **SELECT**

**Source:** `779937548-Core-Rules-KILL-TEAM-3E-Full-Scan.pdf` — p.111 — **SELECT**

> **Torrent x:** Select a valid target as normal as the primary target, then select any number of other valid targets within x of the first valid target, but not within control range of friendly operatives, as secondary targets, e.g. Torrent 2". Shoot with this weapon against all of them in an order of your choice (roll each sequence separately).

**Source:** `eng_jul25_kt_lite_rules-jmjv4hdamy-qlsqxdf83p.pdf` — p.3 — **SELECT** *(lite)*

> Torrent x: Select a valid target as normal as the primary target, then select any number of other valid targets within x of the first valid target, but not within control range of friendly operatives, as secondary targets, e.g. Torrent 2". Shoot with this weapon against all of them in an order of your choice (roll each sequence separately).

### Silent — **SELECT** (Shooter's Conceal)

> **Silent:** An operative can perform the Shoot action with this weapon while it has a Conceal order.

**Source:** `eng_jul25_kt_lite_rules-jmjv4hdamy-qlsqxdf83p.pdf` — p.3 — **SELECT** *(lite)*

### Saturate — **SEQUENCE** (cover save after valid target selected)

> **Saturate:** The defender **cannot retain cover saves**.

**Source:** `eng_jul25_kt_lite_rules-jmjv4hdamy-qlsqxdf83p.pdf` — p.3 — **SEQUENCE** *(lite)*

### Heavy — **SEQUENCE / shooter gates** (patched)

Use **update log p.2 + Jul 25 lite p.3**, not unpatched Full-Scan p.111 (activation-only). Lite restates the errata and keeps the Guard exception.

**Source:** `eng_17-06_kill_team_key_downloads_core_rules_update_log-9dzdz0ewle-wutcyhpgzf.pdf` — p.2 — **SEQUENCE** *(errata — first sentence)*

> **APPENDIX, WEAPON RULES, HEAVY**
>
> Change first sentence to read:
>
> 'An operative cannot use this weapon in an activation or counteraction in which it moved, and it cannot move in an activation or counteraction in which it used this weapon.'

**Source:** `eng_jul25_kt_lite_rules-jmjv4hdamy-qlsqxdf83p.pdf` — p.3 — **SEQUENCE** *(effective wording, including Guard)*

> Heavy: An operative cannot use this weapon in an activation or counteraction in which it moved, and it cannot move in an activation or counteraction in which it used this weapon. If the rule is Heavy (x only), where x is a move action, only that move is allowed, e.g. Heavy (Dash only). This weapon rule has no effect on preventing the Guard action.

---

## Shoot action restrictions (Conceal / 1" control range)

**Source:** `779937548-Core-Rules-KILL-TEAM-3E-Full-Scan.pdf` — p.42 — **SELECT** *(shooter gates)*

> An operative cannot perform this action while it has a **Conceal order**, or while **within control range of an enemy operative**.

**Source:** `eng_jul25_kt_lite_rules-jmjv4hdamy-qlsqxdf83p.pdf` — p.1 — **SELECT** *(lite)*

> An operative cannot perform this action while it has a Conceal order, or while within control range of an enemy operative.

---

## Universal equipment — smoke (obscured area)

**Source:** `eng_17-06_kill_team_key_downloads_universal_equipment-prsd0j8pih-ikfmigl0za.pdf` — p.4 — **SEQUENCE**

> While an operative is wholly within an area of smoke, it's **obscured** to operatives more than 2" from it, and vice versa.

*(Smoke placement requires visibility — same page: marker must be visible to operative, or on Vantage terrain visible to operative.)*

---

## Rules preventing selection as valid target (commentary)

**Source:** `eng_17-06_kill_team_key_downloads_core_rules_update_log-9dzdz0ewle-wutcyhpgzf.pdf` — p.4 — **SELECT**

> Q: Do rules that prevent an operative from being selected as a valid target (e.g. HERNKYN YAEGIR In Position) prevent that operative from being a secondary target for a weapon with the Blast X weapon rule?
>
> A: No, as secondary targets from Blast are not selected.

---

## Commentaries that change cover / Vantage / Blast (update log p.4–6)

**Source:** `eng_17-06_kill_team_key_downloads_core_rules_update_log-9dzdz0ewle-wutcyhpgzf.pdf` — p.4 — **SEQUENCE** *(Blast copies primary cover/obscured)*

> Q: Can you explain further what it means when a rule states that an operative is in cover and obscured if another target was (e.g. Blast X weapon rule, BLOODED Dark Favour).
>
> A: When determining cover and obscured for that operative, whatever was determined for the primary or original target is the same. For example, in the case of Blast, secondary targets are not in cover/obscured if the primary target was not, and they are if the primary target was.

**Source:** `eng_17-06_kill_team_key_downloads_core_rules_update_log-9dzdz0ewle-wutcyhpgzf.pdf` — p.5 — **SEQUENCE** *(Blast + Vantage improved cover save)*

> Q: There are secondary targets of a Shoot action as a result of the Blast weapon rule. The primary target had a Conceal order and was in cover from Light terrain, but was selected as a valid target as a result of the Vantage terrain rule so it received an improved cover save. Does each secondary target receive an improved cover save too?
>
> A: Yes.

**Source:** `eng_17-06_kill_team_key_downloads_core_rules_update_log-9dzdz0ewle-wutcyhpgzf.pdf` — p.5 — **SELECT** *(Vantage + Seek Light)*

> Q: If my operative is on Vantage terrain and shooting with a weapon with the Seek Light weapon rule against an operative in cover from Light terrain, can I elect to only use the Seek weapon rule, denying the improved cover saves from the Vantage terrain rule?
>
> A: Yes.

**Source:** `eng_17-06_kill_team_key_downloads_core_rules_update_log-9dzdz0ewle-wutcyhpgzf.pdf` — p.5 — **SEQUENCE / TERRAIN** *("connected" = same feature)*

> Q: In the third main feature of Vantage terrain, for the purposes of obscured, what does "Heavy terrain connected to Vantage terrain" mean?
>
> A: "Connected" here refers to any part of the same terrain feature.

**Source:** `eng_17-06_kill_team_key_downloads_core_rules_update_log-9dzdz0ewle-wutcyhpgzf.pdf` — p.4 — **SEQUENCE** *(cover save / Accurate die)*

> Q: If you automatically retain a dice as a success before rolling it (e.g. cover save, Accurate weapon rule), can that dice be re-rolled and does it have a numerical result?
>
> A: No to both.

**Source:** `eng_17-06_kill_team_key_downloads_core_rules_update_log-9dzdz0ewle-wutcyhpgzf.pdf` — p.5 — **SEQUENCE** *(retain once; Severe can change)*

> Q: While shooting, fighting or retaliating, if I retain a dice as a normal success (e.g. Accurate 1), can I use another rule to retain it again as a critical success (e.g. Rending)?
>
> A: No, a dice can only be retained once. Note, however, that some rules refer specifically to changing a retained dice (e.g. the Severe weapon rule) and that these allow a dice to be changed after being retained.

Volkus fire-step / door 1" control range visibility commentaries are killzone rules — [`../setup/killzones/volkus.md`](../setup/killzones/volkus.md), not this core tree. Door Fight is not merged into the generic valid-target path.

---

## Quote index (count)

Verbatim quote blocks only (teaching notes are not counted). A block is one Source heading plus its `>` lines; lite-only "identical wording" source lines without their own quote body are not extra blocks.

| Section | Blocks | Primary PDF |
|---------|--------|-------------|
| Valid target / orders | 8 | Full-Scan + lite (p.55; p.42 SELECT; lite Shoot step 2; update log pick-one; Conceal body; Conceal setup; Conceal lite; Engage) |
| Visible | 2 | Full-Scan + lite |
| Cover / intervening / targeting lines | 5 | Full-Scan + lite (Cover body; Cover sidebar; Cover lite; intervening body; intervening sidebar) |
| 1" control range / enemy operative | 4 | Full-Scan + lite |
| Obscured | 3 | Full-Scan (body; sidebar; p.42 dice) |
| Cover save (p.43) | 1 | Full-Scan |
| Terrain types | 8 | Full-Scan (parts intro; Heavy; Light; Light-on-markers; Blocking; Exposed; Vantage SELECT; Vantage connected) |
| Weapon rules (Range, Seek, Blast, Torrent, Silent, Saturate, Heavy) | 11 | Full-Scan + lite + update log |
| Shoot gates / equipment / Blast FAQ | 4 | Full-Scan + lite + universal equipment + update log |
| Update log p.4–6 targeting commentaries | 6 | Update log |
| **Total verbatim blocks** | **52** | |

Previous harvest: **35** blocks (v1.0, 2026-08-17).

---

## Related pages

- [`Target_Eligibility_Cheat_Sheet.html`](Target_Eligibility_Cheat_Sheet.html) — one-page decision tree (layout inspired by community sheets; rules from this file only)
- [`Patch_Manifest.md`](Patch_Manifest.md) — errata ledger (Full-Scan + Jun 17 update log + Jul 25 lite)
- [`README.md`](README.md) — rules spine index
- [`Key_Concepts.md`](Key_Concepts.md) — teaching paraphrase (not a substitute for quotes above)
- [`Keyword_Glossary.md`](Keyword_Glossary.md) — Heavy, Severe, connected, cover save
- [`Turn_Structure.md`](Turn_Structure.md) — order-token ready/expended
- [`../setup/Terrain_Basics.md`](../setup/Terrain_Basics.md) — Accessible / Insignificant / terrain parts
- [`../setup/killzones/volkus.md`](../setup/killzones/volkus.md) — Door Fight, ruins, strongholds (not the core tree)
- [`../setup/killzones/tomb_world.md`](../setup/killzones/tomb_world.md) — Close Quarters Guard

---

## Change Log

- v0.5.0 (2026-08-18): Project-wide semver snapshot (x.y.z).
- v1.1.1 (2026-08-18): Replaced reconstructed Full-Scan p.60 Vantage SELECT quote with owner printed transcription (for an operative on Vantage; with a Conceal order; such operatives; the defender can retain it). Removed the “confirm against printed Core p.60” reconstruction note.
- v1.1 (2026-08-18): Owner verified against Full-Scan + Jun 17 update log + Jul 25 lite. Restored omitted p.42 Engage/Conceal SELECT sentences (active operative); filled lite Shoot cites; p.43 cover save SEQUENCE; p.51 / p.53 sidebars; p.58 parts intro; p.59 marker-Light; p.60 fuller Vantage SELECT; patched Heavy (counteract + Guard); update log p.4–6 targeting commentaries. Quote index 35 → 52.
- v1.0 (2026-08-17): Initial quote harvest (`kt24_rules_quotes` S2). Full-Scan transcribed from image PDF; lite, update log, universal equipment extracted as text.

## Attribution

- Project: Wargame_Concierge · Maintainer: Russell Catt
- **Personal use only. Never for sale.**
- **Kill Team is Copyright Games Workshop Limited 2024**

## Rising Tide Notes

- Community cheat sheets (`Can_I_Shoot.jpeg`, Armagonix sheets, burgerdrome LOS flowchart) are layout inspiration only — not rules sources.
- Table disputes: quotes in this file beat paraphrase elsewhere in `games/kill_team_2024/`.
