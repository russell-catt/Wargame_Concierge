# Manifest §10 — Rules vs Marketing (claim table)

- **Track:** warcode_tactical_doctrine
- **Retrieval date:** 2026-08-23
- **Citation legend:** see `00_what_this_is_not.md`
- **Method:** each public marketing claim tested against the free beta rulebook. Verdicts: **Confirmed** (rules implement it), **Partial** (implemented but overstated or differently), **Not in beta** (plausible, simply absent), **Contradicted** (rules say otherwise), **Unfalsifiable** (no test available from sources read).

## Specification claims

| # | Claim | Source | Rules check | Verdict | Confidence |
|---|-------|--------|-------------|---------|-----------|
| 1 | 2 players, head-to-head | `[PL §hero]` | Two-player throughout; teams never referenced | **Confirmed** | verified |
| 2 | 8 units per squad | `[PL §01]` | Both beta rosters total exactly 8 `[RB pp.33–36]` | **Confirmed** | verified |
| 3 | **4 rounds, fixed length** | `[PL §hero]` | Rules defer round count to the scenario ("if this was the final round") and **never state a number**; the beta scenario text does not state one either `[RB pp.3, 26]` | **Not in beta** | verified (absence) |
| 4 | ~120 min playtime | `[PL §hero]` | No timing guidance anywhere | **Unfalsifiable** | verified (absence) |
| 5 | ~10 min setup | `[PL §hero]` | Setup is 5 steps incl. two D6 rolls and alternating deployment `[RB pp.2, 27]`; plausible, untimed | **Unfalsifiable** | draft |
| 6 | 33" × 24" playing surface | `[PL §06]` | Diagram labels 33'' and 24'' | **Confirmed** | verified |
| 7 | 6 randomized map layouts | `[PL §06]` | "Roll one D6… the result determines the VP placement", six diagrams `[RB p.27]` | **Confirmed** | verified |
| 8 | 4 balanced factions | `[PL §01, §02]` | Two rosters published; MDR and Dominium absent entirely | **Partial** | verified |
| 9 | 1 event card per round | `[PL §01]` | Round sequence includes scenario event cards; beta scenario draws one activation card per round `[RB pp.3, 26]` | **Confirmed** | verified |
| 10 | 16+ age rating | `[PL §hero]` | No content rating in the rulebook; tone is consistent with it | **Unfalsifiable** | draft |

## Mechanics claims

| # | Claim | Source | Rules check | Verdict | Confidence |
|---|-------|--------|-------------|---------|-----------|
| 11 | "Ammo runs out. Reload costs" | `[PL §03]` | Per-weapon ammunition, token-tracked, 0 ammo blocks shooting, reload costs AP `[RB p.9]` | **Confirmed** | verified |
| 12 | "Overwatch rewards positioning" | `[PL §03]` | 1 AP reactive fire; interrupts movement, shooting, reloading, equipment, melee, disengage, escape; normal LoS rules apply `[RB pp.10, 11]` | **Confirmed** | verified |
| 13 | "Loot the fallen — friend or foe" | `[PL §03]` | Equipment tokens persist where a unit died; any unequipped unit picks up for 0 AP within 1" `[RB pp.16, 17]` | **Confirmed** | verified |
| 14 | "Secret assassination targets" | `[PL §03]` | Contracts drawn secretly by the trailing player, naming an enemy unit, worth VP on elimination by any cause `[RB p.22]` | **Confirmed** | verified |
| 15 | **"Map events are known in advance"** | `[PL §03]` | The beta scenario draws a **random** activation card **at the start of each round** — the opposite of known in advance `[RB p.26]` | **Contradicted** | verified |
| 16 | "Every variable… your opponent's ammo state… unfolds differently each time" | `[PL §01]` | Ammunition is tracked with visible tokens beside the model, so it is **public**, not hidden information `[RB p.9]` | **Partial** — real variable, but not concealed | verified |
| 17 | "Terrain creates cover, chokepoints, and lines of sight" | `[PL §06]` | Partial/full cover, agility bonuses per cover piece on the line of fire, doors and door-blocking `[RB pp.11, 12, 18, 19]` | **Confirmed** | verified |
| 18 | Ulfari "average armor, but high agility" | `[PL §02]` | Agility a step above Protagen; armour a step **below** — "average" flatters it with only two rosters public `[RB pp.33–36]` | **Partial** | draft |
| 19 | Ulfari "most dangerous in melee" | `[PL §02]` | Protagen field both the higher melee-attack unit and the harder-hitting melee weapon `[RB pp.34, 35–36]` | **Contradicted** (on the published rosters) | draft |
| 20 | Dominium "degrades morale" | `[PL §02]` | **No morale, fear, pinning, or suppression system exists** in the beta text | **Not in beta** | verified (absence) |
| 21 | MDR "command abilities… every unit's position affects what the squad can do next" | `[PL §02]` | Core rules reserve "abilities that give extra AP to another friendly unit"; no such unit in either published roster `[RB p.3]` | **Not in beta** | verified |
| 22 | "Lean ruleset… twenty minutes to read the rules" | `[PL §01]` | ~37 pp, diagram-dense, plus unread Protocol Card and Contract layers `[RB pp.23–24, 28–32]` | **Partial** | draft |
| 23 | "Doesn't need a new edition to play differently next week" | `[PL §03]` | Variance sources are real: D6 map layout, per-round event card, ammo state, loot, contracts | **Confirmed** | draft |

## Development and community claims

| # | Claim | Source | Check | Verdict | Confidence |
|---|-------|--------|-------|---------|-----------|
| 24 | 27 months in development | `[PL §08]` | Self-reported, no corroboration | **Unfalsifiable** | unverified |
| 25 | 237 playtests completed | `[PL §08]` | Self-reported | **Unfalsifiable** | unverified |
| 26 | 24k subscribers / 1,038 Discord | `[PL §08]` | Self-reported, undated snapshot | **Unfalsifiable** | unverified |
| 27 | Trailer 86,000 views in two weeks | `[PL §08]` | Self-reported; no platform link given | **Unfalsifiable** | unverified |
| 28 | "The rules are tight… edge cases have been found and resolved" | `[PL §04]` | **Directly testable and it fails** — see `12_needs_polish.md`: a duplicated paragraph, a hardcoded movement number that breaks for non-standard speeds, an exactly-50%-visibility boundary gap, a possible statline inconsistency, and no stated round count | **Contradicted** | verified |
| 29 | "The factions are balanced" | `[PL §04]` | Untestable: half the factions unpublished, zero games played by this project | **Unfalsifiable** | unverified |
| 30 | $1 VIP refundable, squad included free on all tiers | `[PL §10, §11]` | Marketing only; no terms document read | **Unfalsifiable** | draft |
| 31 | Gamefound campaign, September 2026, 09:00 UTC | `[PL §08, §11]` | Consistent across page and pointers; Gamefound project body login-walled `[GF]` `[PTR]` | **Confirmed (as stated intent)** | draft |

## Summary for the review

- **Confirmed:** 11 of 31 — and notably, **five of the six headline gameplay differentiators are real**.
- **Contradicted:** 3 — the "events known in advance" claim, "Ulfari most dangerous in melee", and "edge cases have been found and resolved".
- **Not in beta:** 3 — the 4-round length, Dominium's morale system, MDR's AP-sharing.
- **Partial:** 4. **Unfalsifiable:** 11 (mostly self-reported metrics).
- **Fair overall read:** the marketing describes the mechanics honestly. Where it overreaches, it overreaches on **polish and completeness claims**, not on what the game does.

## Open questions

- Is "map events are known in advance" describing an unpublished deck (event cards visible at round start for the following round), rather than the scenario activation cards? Worth a direct VIP question — this may be a copy error, not a design claim.
- Does a newer free beta state the round count?
