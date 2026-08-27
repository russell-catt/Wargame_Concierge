<!--
FILE: games/warhammer_40k_11e/armies/necrons/Reanimation_Protocols.md
VERSION: v0.5.5 (2026-08-27)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, slice S6; wd527_shipping; dataslate_0826 S2)

DOCUMENT_TYPE: Teaching Guide / Army Rule
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: Warhammer 40,000 - 11th Edition
FACTION: Necrons
REFERENCE_STATUS: Active - verified against owned faction pack and Wahapedia, read 2026-08-16

SOURCES:
  - raw/_dataslate_0826_staging/eng_wh40k_faction_pack_necrons-eweoek106p-nqomxds3qr.pdf (Faction Pack v1.2, legal from 26 Aug 2026, staging read 2026-08-27) — confirms Reanimation Protocols still heals **D3** wounds per activation under v1.2, unchanged
  - C:\Personal\40K\rules\eng_22-07_warhammer_40,000_faction_pack_necrons.pdf (Version 1.1, legal from 22 July 2026; read 2026-08-16; superseded)
  - https://wahapedia.ru/wh40k10ed/factions/necrons (Army Rules section, retrieved 2026-08-16)
  - games/warhammer_40k_11e/rules/Turn_Structure.md (phase order)

PURPOSE:
  Teach the Necron army rule: when it fires, what it restores, what it will not
  do, and how it should change the way the army is played. Paraphrase only.

PRIMARY_AUDIENCE:
  - A first-time Necron player who has read Turn_Structure.md
  - Anyone building a Necron list who needs to know what durability is worth

UPDATE_TRIGGER:
  Update when a new faction pack version, balance dataslate, or FAQ changes the
  trigger, the amount reanimated, or any of the amplifiers listed here.
-->

# Reanimation Protocols - the Necron army rule

Think of your Necron units like robots with spare parts in a backpack. Every turn, they quietly fix themselves — for free. That is the whole army in one sentence, and it is the first rule to learn properly.

> **Necron army rule** (see owned Necron faction pack — not a Core Rules ID). Timing lines up with the end of the **Command phase** (`08.05`).

**Where to check it:** your own Necrons faction pack, `C:\Personal\40K\rules\eng_22-07_warhammer_40,000_faction_pack_necrons.pdf` (Version 1.1). Cross-checked against Wahapedia's Necrons Army Rules section on **2026-08-16**.

**System spine:** wound grid [`../../rules/Wound_Roll_Reference.md`](../../rules/Wound_Roll_Reference.md) · Force Dispositions [`../../setup/Chapter_Approved_Force_Dispositions.md`](../../setup/Chapter_Approved_Force_Dispositions.md) · Mission 38 [`../../setup/WD527_Monthly_Mission.md`](../../setup/WD527_Monthly_Mission.md) · system QR [`../../setup/print/40k_system_quick_reference.html`](../../setup/print/40k_system_quick_reference.html) · laminate [`Quick_Reference_Play_Guide.md`](Quick_Reference_Play_Guide.md).

---

## What the rule does

| Question | Answer |
|----------|--------|
| **Who gets it** | Every unit in your army with the Reanimation Protocols faction ability, while it is on the battlefield |
| **When** | At the **end of your Command phase** (`08.05`) — once per battle round, on your turn, before the **Movement phase** (`09.02`) |
| **How much** | Roll a **D3**. That is how many wounds the unit reanimates |
| **What it costs** | Nothing. No CP, no roll to see if it works, no choice to make |

Each reanimated wound is spent one at a time, in a fixed order:

1. **Heal first.** If any model in the unit is wounded but still alive, one of those models gets a lost wound back.
2. **Then rebuild.** Only when every surviving model is at full wounds does a reanimated wound bring a **destroyed model back with 1 wound remaining**.
3. **Stop at full.** Once the unit is back to its Starting Strength with everyone at full wounds, further reanimation does nothing.

That order has a consequence people miss at the table: **chip damage soaks up your reanimation**. A Warrior block with three models lightly wounded spends its D3 topping those up rather than standing anyone back up.

---

## What it does not do

- It does not bring back a unit that has been **wiped out**. Reanimation only reaches units still on the battlefield. Losing the last model of a unit is permanent.
- It does not fire on your opponent's turn. Damage taken during their turn sits on the unit until your next **Command phase** (`08.01`–`08.05`) — unless a **stratagem** (`15.01`) like Potentiality Syphon says otherwise (see owned faction pack).
- It does not choose for you which model returns - the rules do, and the returning model comes back on **1 wound**, so it can be killed again immediately.

---

## Why this changes how you play

**Partial damage is wasted damage.** Against most armies, whittling a unit down over two turns is progress. Against Necrons it often is not - the unit repairs in between, and the opponent has spent two turns of shooting to achieve roughly one turn of nothing. Your opponent must **kill outright or leave alone**, and splitting fire is punished harder against you than against anybody else.

Four habits follow from that, and they are the difference between a new Necron player and a good one:

- **Stand on the objective and take the hit.** The instinct to pull a damaged unit back is usually wrong. That unit is scoring **Objective Control** (`14.02`) on the terrain **footprint** (`14.01`) every phase it stays, and it will get some of the damage back at the end of your next **Command phase** (`08.05`).
- **Do not lose the last model.** A unit at one model is worth far more than a unit at zero, because one model reanimates and zero models never come back. Screening, coherency (**2″/9″**, `03.03`), and keeping a body out of blast range all matter more than they look.
- **Spread your own casualties, concentrate your enemy's.** You want your opponent's damage smeared thinly across several units. Deploy so no single unit is the only sensible target.
- **The rule is worth more the longer the game runs.** A Warrior block that survives four battle rounds has effectively been re-bought. Trading it away early throws that away, even at a favourable exchange rate.

This is also why Necrons are a forgiving army to learn on. A positioning mistake that would cost another army a whole unit usually costs you some wounds and one turn of recovery.

**Commentary (White Dwarf 527 — Rules Focus: Terrain Objectives):**

Hold the **footprint**, not a floating marker idea — models inside the terrain area control it. Chip damage on a flag you still occupy is often wasted against Reanimation.

**Cite:** WD527, Rules Focus: Terrain Objectives; owned digital backup purchased Trinity Hobby **2026-08-22**; local scans `C:\Personal\40K\WD_527\`. Tier **1.5** — Core / Event Companion win on mechanics.

---

## Things that make it bigger

You do not need these to play, but they explain why certain models are worth their points. All are from the owned faction pack v1.1, read 2026-08-16.

| Source | Effect, in plain terms |
|--------|------------------------|
| **Canoptek Reanimator** | Friendly Necron units near it reanimate an extra D3 wounds when the rule fires |
| **Resurrection Orb** (Overlord, Lokhust Lord, Catacomb Command Barge) | Once per battle, a unit resurrects - reanimating D6 instead of D3. One unit per turn only |
| **Canoptek Macrocytes** (nanoscarab projector) | Once per battle round, a nearby Necron unit reanimates one extra wound |
| **Cryptek Conclave stratagem - Potentiality Syphon** (`15.01`) | Fires a unit's Reanimation Protocols **off-turn**, in your opponent's **Command phase** (`08.01`), if it is on an objective (`14.02`). See [`Cryptek_Conclave.md`](Cryptek_Conclave.md) |
| **Necron Warriors - Their Number is Legion** | Each time this unit's RP activates, re-roll the D3. WarCom FAQ: also applies when a stratagem activates RP. See `KB/analyses/their_number_is_legion_potentiality_syphon_250.md` |

The pattern is worth noticing: almost every Necron support piece pays into the same rule instead of adding a new one. **Stacking reanimation is the faction's design.**

---

## The one thing to get right in your first game

Put a physical reminder on the table - a dice, a token, a note on your list - that says **"end of Command phase: reanimate"**. Forgetting it is the single most common Necron beginner mistake, and it is a real loss: a missed D3 every round is roughly a free model per turn thrown away.

---

## Related pages

- [`Canoptek_Court.md`](Canoptek_Court.md) - detachment that compounds with reanimation through map control
- [`Cryptek_Conclave.md`](Cryptek_Conclave.md) - detachment that can trigger reanimation off-turn
- [`Starter_250.md`](Starter_250.md) - the learning list this rule is practised on
- [`Quick_Reference_Play_Guide.md`](Quick_Reference_Play_Guide.md) - the laminate version
- [`../../rules/Turn_Structure.md`](../../rules/Turn_Structure.md) - where the Command phase sits
- [`../../rules/Key_Concepts.md`](../../rules/Key_Concepts.md) - wounds, saves, Objective Control
- [`../../rules/Wound_Roll_Reference.md`](../../rules/Wound_Roll_Reference.md) - S vs T wound grid
- [`../../setup/WD527_Monthly_Mission.md`](../../setup/WD527_Monthly_Mission.md) - Mission 38 when that card is in use

---

## Games Workshop notice

**UNOFFICIAL.** This document is completely unofficial and in no way endorsed by Games Workshop Limited. Personal / no-charge use only — never for sale. Warhammer, Warhammer 40,000 and associated marks are trademarks of Games Workshop Limited. Used without permission. No challenge to their status intended. Warhammer 40,000 is Copyright Games Workshop Limited. Teaching notes by Russell Catt (Wargame Concierge). Games Workshop retains IP in the settings and characters. No official logos.

**Rules currency:** Faction Pack Necrons **v1.2** (legal 26 Aug 2026) · verify owned PDF.

## Change Log
- v0.5.5 (2026-08-27): dataslate_0826 S2 — stamped **Faction Pack v1.2** (legal 26 Aug 2026) in SOURCES. No rules-fact change: v1.2 confirms the army rule still heals **D3** wounds per activation, exactly as taught on this page since v1.0.
- v0.5.4 (2026-08-25): WD527 shipping S6 — system spine links; footprint/OC teaching; Terrain Objectives Commentary; GW notice.
- v0.5.3 (2026-08-20): Legion row — WarCom FAQ pattern + analysis link; character revive clarified via sibling guides.
- v0.5.0 (2026-08-18): Project-wide semver snapshot (x.y.z).
- v1.0 (2026-08-16): Initial army rule teaching guide (slice S4), written from the owned Necrons Faction Pack v1.1 and the Wahapedia Necrons army rule, both read 2026-08-16. Supersedes the `unverified` sketch in `KB/concepts/reanimation_protocols.md`.

## Attribution
- Project: Wargame_Concierge
- Maintainer: Russell Catt
- Warhammer 40,000 is a trademark of Games Workshop Limited. This document is a personal teaching paraphrase and reproduces no publisher text or statlines.

## Rising Tide Notes
- This document follows Rising Tide documentation standards.
- **Verify before you play.** Cross-check anything here against the current Munitorum Field Manual and your faction pack - Games Workshop patches rules and points between publications. Content on this page reflects sources read on **2026-08-16**.
