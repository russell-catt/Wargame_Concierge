---
title: Their Number is Legion and Potentiality Syphon (250 Conclave)
type: analysis
system: warhammer_40k_11e
faction: Necrons
created: 2026-08-19
updated: 2026-08-19
version: 0.1.0
sources:
  - games/warhammer_40k_11e/armies/necrons/Army_List_250_Conclave.md
  - games/warhammer_40k_11e/armies/necrons/Reanimation_Protocols.md
  - games/warhammer_40k_11e/armies/necrons/Cryptek_Conclave.md
  - games/warhammer_40k_11e/armies/necrons/Reference_Guide_250_Conclave.md
  - games/warhammer_40k_11e/armies/necrons/Reference_Guide_500_V1_Conclave.md
  - "https://wahapedia.ru/wh40k11ed/factions/necrons/Necron-Warriors (retrieved 2026-08-19)"
  - "https://wahapedia.ru/wh40k11ed/factions/necrons (Potentiality Syphon; retrieved 2026-08-19)"
confidence: draft
tags: [analysis, query, necrons, reanimation, cryptek_conclave, warriors, 250]
---

# Their Number is Legion and Potentiality Syphon (250 Conclave)

Filed answer for the 250-pt Cryptek Conclave Warrior brick: how **Their Number is Legion** interacts with Reanimation Protocols, and how the Conclave off-turn stratagem **Potentiality Syphon** works. Teaching paraphrase only — verify on the owned Necrons faction pack before events.

---

## Their Number is Legion (Necron Warriors)

Each time this unit's **Reanimation Protocols** activate (usually at the end of your **Command phase**, `08.05`), you may **re-roll the D3** that decides how many wounds are reanimated.

- Does **not** change heal-first / return-at-1W / stop-at-full / wiped-unit rules — only the die for the amount.
- Triggers whenever RP activates for that unit: end of **your Command phase** (`08.05`), **and** any **stratagem** (`15.01`) that activates RP (including Potentiality Syphon).
- On the 250 Conclave list: the **Warrior** unit has it; Scarabs and Tomb Crawlers do not.

**Rough EV:** plain D3 ≈ 2.0 wounds; with an optional re-roll, expect slightly more when you re-roll a 1.

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
3. Spend order is the same as normal RP (heal survivors → return models at 1W → stop at Starting Strength / full). **Wiped units still get nothing.**
4. Other RP modifiers that apply when protocols activate (e.g. Their Number is Legion) still apply — see also FAQ pattern on other “activate RP” stratagems.

### On the 250 Conclave list

| Unit | On objective + Syphon | Cryptek? | Amount model |
|------|----------------------|----------|--------------|
| Geomancer + Warriors | Yes | **Yes** (attached Geomancer) | D3 **+1**, and Warriors may **re-roll the D3** |
| Tomb Crawlers | If on objective | No | Plain D3 |
| Scarab Swarms | If on objective | No | Plain D3 |

**CP budget:** 1CP per use; baseline gain is ~1 CP per your Command phase. Plan a few key procs (usually the Warrior brick), not every opponent turn.

**Character note:** While attached, Geomancer wounds are part of the unit for heal-first. Dead characters typically do not return as bodyguard models — keep the Cryptek screened. Confirm on core rules / datasheet.

---

## Open questions

- Confirm exact Potentiality Syphon and Their Number is Legion wording on owned faction pack v1.1 (Wahapedia used 2026-08-19; `draft` until pack cross-check).
- Whether any dataslate has changed the +1 Cryptek wound or the objective-range wording since pack v1.1.

---

## Related pages

- [[reanimation_protocols]] · [[cryptek_conclave]] · [[necrons]] · [[necron_warriors]]
- [[glossary]] — **Their Number is Legion**, **Potentiality Syphon**
- Shipping: `games/warhammer_40k_11e/armies/necrons/Army_List_250_Conclave.md`, `Reanimation_Protocols.md`, `Cryptek_Conclave.md`
- [[index]] · [[wahapedia]]
