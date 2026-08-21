---
title: Their Number is Legion and Potentiality Syphon (250 Conclave)
type: analysis
system: warhammer_40k_11e
faction: Necrons
created: 2026-08-19
updated: 2026-08-21
version: 0.2.1
sources:
  - "https://www.warhammer-community.com/en-gb/articles/rgqanids/warhammer-40000-july-update-what-you-need-to-know/ (retrieved 2026-08-20)"
  - "https://www.warhammer-community.com/en-gb/downloads/warhammer-40000/ (retrieved 2026-08-20)"
  - "https://assets.warhammer-community.com/warhammer40000_faqs&errata_necrons_eng_16.10.pdf (Necrons FAQ — Legion + activate-RP pattern; retrieved 2026-08-20)"
  - games/warhammer_40k_11e/armies/necrons/Reanimation_Protocols.md
  - games/warhammer_40k_11e/armies/necrons/Cryptek_Conclave.md
  - games/warhammer_40k_11e/armies/necrons/Army_List_250_Conclave.md
  - "C:\\Personal\\40K\\rules\\eng_22-07_warhammer_40,000_faction_pack_necrons.pdf (v1.1; shipping read 2026-08-16)"
  - "https://wahapedia.ru/wh40k11ed/factions/necrons/Necron-Warriors (retrieved 2026-08-20)"
  - "https://wahapedia.ru/wh40k11ed/factions/necrons (Potentiality Syphon + FAQ; retrieved 2026-08-20)"
confidence: draft
tags: [analysis, query, necrons, reanimation, cryptek_conclave, warriors, 250]
---

# Their Number is Legion and Potentiality Syphon (250 Conclave)

Filed answer for the 250-pt Cryptek Conclave Warrior brick: how **Their Number is Legion** interacts with Reanimation Protocols, and how the Conclave off-turn stratagem **Potentiality Syphon** works.

**Source order for this pass (2026-08-20):** Warhammer Community (primary living reference) → owned faction pack / shipping paraphrase → Wahapedia (secondary cross-check). Teaching paraphrase only — no GW text dump.

---

## Their Number is Legion (Necron Warriors)

Each time this unit's **Reanimation Protocols** activate (usually at the end of your **Command phase**, `08.05`), you may **re-roll the D3** that decides how many wounds are reanimated.

- Does **not** change heal-first / return-at-1W / stop-at-full / wiped-unit rules — only the die for the amount.
- Triggers whenever RP activates for that unit: end of **your Command phase** (`08.05`), **and** any **stratagem** (`15.01`) that activates RP (including Potentiality Syphon).
- On the 250 Conclave list: the **Warrior** unit has it; Scarabs and Tomb Crawlers do not.

**WarCom primary (FAQ pattern):** The published Necrons FAQ answers that when a stratagem activates Reanimation Protocols (example: Protocol of the Undying Legions), **other rules that apply to RP still apply**, naming **Their Number is Legion** explicitly. That is the official confirmation that Legion is not limited to the free end-of-Command trigger.

**Wahapedia secondary:** Same Legion paraphrase on the Warriors datasheet (`wh40k11ed`, retrieved 2026-08-20).

**Rough EV:** plain D3 ≈ 2.0 wounds; with an optional re-roll, expect slightly more when you re-roll a 1.

---

## What “heal-first” means

**Heal-first is not a separate named ability.** It is teaching shorthand for **step 1 of how Reanimation Protocols spends its D3 wounds** (see [[reanimation_protocols]] and shipping `Reanimation_Protocols.md`).

When RP activates, you roll a **D3** and spend those wounds **one at a time** in a fixed order:

1. **Heal first** — if any model in the unit is still on the table but missing wounds, put wounds back on those models.
2. **Then rebuild** — only after every survivor is at full wounds do you return a destroyed model at **1 wound**.
3. **Stop** when the unit is back to Starting Strength / everyone full.

Chip damage on survivors therefore soaks the roll before bodies stand back up.

---

## Potentiality Syphon (Cryptek Conclave)

**1CP** Strategic Ploy (`15.01`).

| Field | Teaching paraphrase |
|-------|---------------------|
| **When** | Your **opponent's Command phase** (`08.01`) |
| **Target** | One **NECRONS** unit from your army **within range of one or more objective markers** (`14.02`) |
| **Effect** | That unit's **Reanimation Protocols** activate. If it is a **CRYPTEK** unit, it also reanimates **+1 wound**. |

### How it stacks with the army rule

1. Free RP still fires at the **end of your Command phase** (`08.05`) (D3 per eligible unit on the board).
2. Syphon is a **second** activation in the same battle round, paid with CP (`15.01`), only while the chosen unit is on an objective (`14.02`) during the opponent's **Command phase** (`08.01`).
3. Spend order is the same as normal RP (heal-first → return models at 1W → stop at Starting Strength / full). **Wiped units still get nothing.**
4. Their Number is Legion still applies on this activation (WarCom FAQ pattern above).

### On the 250 Conclave list

| Unit | On objective + Syphon | Cryptek? | Amount model |
|------|----------------------|----------|--------------|
| Geomancer + Warriors | Yes | **Yes** (attached Geomancer) | D3 **+1**, and Warriors may **re-roll the D3** |
| Tomb Crawlers | If on objective | No | Plain D3 |
| Scarab Swarms | If on objective | No | Plain D3 |

**CP budget:** 1CP per use; baseline gain is ~1 CP per your Command phase. Plan a few key procs (usually the Warrior brick), not every opponent turn.

### Attached characters (resolved)

While the Geomancer is **attached** (`19.01`), he and the Warriors are **one unit** for RP’s spend order. His missing wounds count as “wounded survivors in the unit,” so they are eligible for **heal-first** — a damaged-but-alive Cryptek can be healed by the unit’s RP before any destroyed Warriors return.

**Worked example:** 8 Warriors left (all full), Geomancer on **2 of 4 wounds**, you roll **D3 = 2**.

- Both wounds go into **healing the Geomancer** (toward full).
- **No Warriors return** this activation, because heal-first isn’t finished until every survivor (including him) is full.

**Destroyed CHARACTER models are not returned by ordinary unit heal/RP into the bodyguard** — core heal/regain wording excludes CHARACTER from the “revive a destroyed model into this unit” step (Wahapedia core cross-check; matches shipping attached-unit teaching). Heal-first only helps while the Cryptek is **still alive but damaged**.

**WarCom primary (July 2026 update article):** when a slain character *is* able to revive under a rule that brings them back, they return as a **unit of one**, not rejoined into the Warrior brick. That was called out specifically against “unkillable” Warrior+character blobs. Habit: keep the Cryptek screened; if both brick and Cryptek die, you do not get the whole blob back as one unit.

---

## Open questions — resolved (2026-08-20)

| Former open question | Resolution | Primary | Secondary |
|----------------------|------------|---------|-------------|
| Confirm exact Legion + Syphon wording vs pack v1.1 | **Closed.** Shipping guides already paraphrased from owned pack v1.1 (`eng_22-07_*`, legal 22 Jul 2026, read 2026-08-16). Wahapedia `wh40k11ed` lists Faction Pack **11 / 1.1 / July 2026** and matches: Legion = re-roll D3 on RP activate; Syphon = opponent’s Command, objective-range target, RP activate, **+1 wound if CRYPTEK**. WarCom FAQ confirms Legion applies whenever RP is activated by another rule. | WarCom FAQ + downloads hub; owned pack via shipping | Wahapedia Warriors + Necrons hub |
| Has a dataslate changed Syphon’s +1 Cryptek wound or objective-range wording? | **Closed for now — no.** Survey of WarCom July 2026 update article, downloads hub, and searchable Necrons FAQ/errata assets (retrieved **2026-08-20**) found **no amendment** to Potentiality Syphon’s target or +1 Cryptek effect. March 2026 balance commentary focused on C’tan / MONSTER exclusions, not Syphon. Re-check WarCom downloads after the next dataslate. | WarCom articles + FAQ PDF | Wahapedia still shows +1 / objective-range Syphon |
| Do dead characters return via Warrior RP? | **Closed.** Ordinary RP/heal does **not** revive CHARACTER models into the bodyguard. Separate character-revive rules (WarCom July update) return the character as a **solo unit**, not as part of the Warriors. | WarCom July update article | Wahapedia heal/RP wording (excluding CHARACTER) |

**Still `draft`:** this page is teaching paraphrase pending an owner line-check of the physical pack PDF in-session; WarCom + Wahapedia closed the named open questions.

---

## Related pages

- [[reanimation_protocols]] · [[cryptek_conclave]] · [[necrons]] · [[necron_warriors]]
- [[glossary]] — **Their Number is Legion**, **Potentiality Syphon**
- [[warhammer_community]] · [[wahapedia]]
- Shipping: `games/warhammer_40k_11e/armies/necrons/Army_List_250_Conclave.md`, `Reanimation_Protocols.md`, `Cryptek_Conclave.md`
- [[index]]
