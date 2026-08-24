# Manifest §7 — Core Game Loop

- **Track:** warcode_tactical_doctrine
- **Retrieval date:** 2026-08-23
- **Citation legend:** see `00_what_this_is_not.md`
- **Paraphrase guard:** procedural summary only. Verbatim rules text belongs in `games/the_warcode/rules/`.

## Setup (once)

1. **Read the scenario** — objectives, victory conditions, special rules `[RB p.2]`
2. **Roll D6 for map layout** — one of six capture-point placements on the 33"×24" board `[RB p.27]`
3. **Roll D6 for initiative**, which in round 1 also sets deployment order `[RB p.3]`
4. **Deploy alternately**, one unit each `[RB p.2]`
5. **Spend 4 equipment points** after deployment — grenades and medkits at 2 points each, one item per unit unless a rule says otherwise `[RB pp.2, 16]`

All: confidence **verified**. Note the ordering quirk: **units deploy before they are armed** `[RB p.2]`, so equipment is bought with full knowledge of both deployments.

## Round loop

**1. Initiative Phase** — both players roll D6, highest goes first this round; ties re-roll. Re-roll points cannot be spent here. `[RB pp.3, 23]` — confidence: verified

**2. Tactical Phase** — players alternate activating one unit at a time. An activated unit spends its 2 AP, then its token flips and it is done for the round. `[RB p.4]` — confidence: verified

**3. End of Round** — in order: end-of-round unit effects → scenario effects / event cards → **VP calculation**. `[RB p.3]` — confidence: verified

**4. Contracts check** — if the VP gap is 1 or more, the trailing player draws a secret contract before the next round. `[RB p.22]` — confidence: verified

**5. Re-roll refresh** — a player whose Leader is alive banks 2 re-roll points at the start of each round. `[RB p.23]` — confidence: verified

Repeat until the final round, then resolve the scenario's win condition. `[RB p.3]` — confidence: verified. **The core rules never state how many rounds a game lasts** — it is deferred to the scenario, and the beta scenario text does not state it either. Marketing says 4. See `10_rules_vs_marketing.md`.

## The activation menu (2 AP)

| Action | Cost | Note |
|--------|------|------|
| Move | 1 AP | Slow 5" / Standard 6" / Fast 7"; −1" through partial cover, −2" through a friendly `[RB p.6]` |
| Shoot | weapon-dependent | Needs range, line of sight, ≥1 ammo `[RB pp.8, 9]` |
| Reload | weapon-dependent | Restores ammo to max `[RB p.9]` |
| Overwatch | 1 AP | Ends the unit's round entirely `[RB p.10]` |
| Melee attack | weapon-dependent | Only inside melee range `[RB p.13]` |
| Engage | 2 AP | Movement +2" ending in melee `[RB p.14]` |
| Disengage from Melee Lock | 1 AP | D6 vs enemy melee strength; failure = free enemy attack `[RB p.15]` |
| Escape from Melee Lock | 2 AP | Always leaves, even on a failed roll `[RB p.15]` |
| Use ability / equipment | varies | Grenade 1 AP; **medkit 0 AP** `[RB pp.16, 18]` |
| Interact (doors) | **0 AP** | Within 1"; once per activation `[RB p.18]` |
| Pick up item | **0 AP** | Within 1"; only if not already carrying `[RB pp.17, 18]` |
| Pass | 0 AP | The only action that does **not** trigger Overwatch `[RB p.4]` |

All: confidence **verified**.

## Attack resolution (the game's core dice loop)

**Shooting** — three steps `[RB pp.8, 9, 20]` — confidence: verified:
1. **Hit** — roll dice equal to the weapon's shot count against the target's agility (raised by cover and friendly screens, capped at 5)
2. **Penetrate** — re-roll those hits against the target's armour, modified by the weapon's armour-penetration sign
3. **Damage** — each penetrating die deals normal damage; a **6 deals critical damage instead**; per-die results sum

**Melee** — adds a defence step `[RB pp.13, 21]` — confidence: verified:
1. Attacker rolls dice equal to its melee strength against the target's agility
2. **Defender rolls dice equal to its own melee strength to block** — each attack die is cancelled only by a defender die of equal or higher value
3. Unblocked hits go to armour penetration, then damage

The attacker may re-roll the melee hit check **only before the defender blocks**. `[RB p.23]` — confidence: verified

**Grenades bypass the front half of that loop entirely** — no hit roll, no agility, and partial cover is ignored; every model in the 2" blast goes straight to an armour-penetration check. Full cover still blocks via a line-of-sight check taken from the token. `[RB pp.16, 17]` — confidence: verified

## Scoring loop

- A capture point pays out only if a friendly unit is within 1" **and no enemy is**; mixed presence = contested, nobody scores. `[RB p.4]` — confidence: verified
- Evaluated at end of round, so a late-arriving model denies a whole round's income by standing there. `[RB p.3]` — confidence: verified
- Second income stream: **contracts**, awarded for being behind, paid on eliminating a named enemy unit — by any cause, including scenario effects. `[RB p.22]` — confidence: verified

## Loop-level observations for the review

- **Three interacting economies per round:** AP (tempo), ammunition (sustained output), re-roll points (reliability). Ammunition and re-rolls both carry across rounds; AP does not. — confidence: draft (inference)
- **The Overwatch/grenade interaction is the loop's most interesting pressure point.** Overwatch drops on damage taken, and grenades ignore cover and agility, so a grenade is the reliable way to open a covered firing lane — at the cost of one of only two grenades a squad can buy. `[RB pp.11, 16, 17]` — confidence: draft
- **Overwatch spends 1 AP but ends the unit's round**, so the second AP is forfeited. That is a real 2-AP price wearing a 1-AP label. `[RB p.10]` — confidence: verified
- **Melee Lock is the tempo sink**: entering costs 2 AP (Engage), leaving costs 1–2 AP plus a roll, and while locked the unit cannot shoot or use equipment. `[RB pp.14, 15]` — confidence: verified
- **Contracts fire almost every round.** The trigger is a gap of *one* VP, so any non-tied round hands the trailing player a card. Compounding, and the beta does not say whether contracts accumulate. `[RB p.22]` — confidence: verified (rule), draft (impact)

## Open questions

- Can a player hold multiple unfulfilled contracts at once?
- Are event cards drawn from a general deck, or only from scenario-specific decks like *Core of the Machine*? `[RB pp.3, 26]`
