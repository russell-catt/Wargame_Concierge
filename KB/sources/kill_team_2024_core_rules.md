---
title: Kill Team 2024 - Core Rules
type: source
system: kill_team_2024
created: 2026-08-17
updated: 2026-08-17
sources: [raw/pointers/kill_team_2024_core.md, raw/pointers/kill_team_web_living_sources.md, "https://wahapedia.ru/kill-team3/the-rules/core-rules/ (retrieved 2026-08-17)"]
confidence: draft
tags: [source, kill_team_2024, core_rules, living_reference]
---

# Kill Team 2024 - Core Rules

The core rulebook for **Kill Team 2024 (3rd Edition / KT24)**: turning points, activations, orders, actions, shooting and fighting sequences, and the key-principles glossary (control range, cover, obscured, visible, valid target). This is the second game system in Wargame_Concierge, entirely separate from Warhammer 40,000 - see the **Kill Team** entry in [[glossary]] for the standing warning against conflating the two.

---

## What this source is

| Field | Value |
|-------|-------|
| Primary reference | Local owned PDF - `C:\Personal\Kill Team\kill_team_2024\779937548-Core-Rules-KILL-TEAM-3E-Full-Scan.pdf` (pointer: [`raw/pointers/kill_team_2024_core.md`](../../raw/pointers/kill_team_2024_core.md)) |
| **Read by the Librarian this pass** | **Wahapedia's Kill Team 3 Core Rules page**, <https://wahapedia.ru/kill-team3/the-rules/core-rules/>, retrieved **2026-08-17** - a community consolidation covering the same rules content |
| Owned PDF status | **Not opened this pass.** The Librarian cannot open binaries; the pointer stub is the only allowed on-disk reference. Everything below is cross-checked against the living Wahapedia page, not the owned PDF directly |
| Also on disk, not yet read | Lite rules (Jul 2025), Core Rules update log, Universal equipment, Sniper rules update - all under the same pointer, all unopened |
| Edition | **Kill Team 2024 / 3rd Edition (KT24)**. The Wahapedia page's book table shows a **June 2026** last-update stamp for the Core Book, one version ahead of the February 2026 predecessor - i.e. **the rules have already been revised at least once since KT24 launched**, and the owned Full-Scan PDF's print date relative to that update is unknown |
| Scope | Turning point / phase structure, activation and order rules, the six universal actions (Reposition, Dash, Fall Back, Charge, Pick Up Marker, Place Marker, plus Shoot, Fight, Guard), the full Shoot and Fight sequences, and the alphabetical Key Principles glossary (Bases, Control Range, Damage, Cover, Datacards, Dice, Distances, Equipment, Intervening, Keywords, Killzone Floor, Markers, Obscured, Operatives, Orders, Ploys, Precedence, Roll-off, Valid Target, Visible) |
| Does **not** cover | Any specific kill team's faction rules, any killzone's terrain rules, any mission pack's Crit Ops / Tac Ops, equipment lists, or Nemesis Operative rules - all separate pointers, all unread |

---

## Key facts extracted (teaching paraphrase)

**Turning point structure.** A battle runs a fixed number of turning points (four, unless a mission pack says otherwise). Each turning point is a **Strategy phase** (Initiative -> Ready -> Gambit) followed by a **Firefight phase** (alternating activations until both sides are expended). See [[turning_points]].

**Activation and APL.** Activating an operative means giving it an order, then spending Action Points (AP) up to its Action Point Limit (APL) on actions, without repeating the same action twice in one activation. See [[activations_apl]].

**Orders.** Every operative is Engage or Conceal. Conceal blocks Shoot, Charge, and counteracting, but hides the operative from being a valid target while it is in cover. Engage does everything, including counteracting once all your operatives are expended. See [[orders_conceal_engage]].

**Control range, cover, and obscured.** Control range is the 1"-and-visible zone that governs contesting markers, fighting, and cover. Cover and Obscured are each checked per-shot between two operatives, and interact differently with a target's order. See [[cover_kill_team]] and [[control_range_kill_team]].

**Damage and Injured.** An operative below half its starting Wounds is Injured: -2" Move and its weapons' Hit stat worsens by 1. At 0 Wounds or less it is incapacitated, then removed. See [[injured_operatives]].

**Counteract replaces overwatch.** If one side has expended every operative but the other still has ready ones, an expended Engage operative can perform one free 1AP action (not Guard) instead of the opponent simply cycling through remaining activations - capped at once per operative per turning point and a 2" move limit.

**Command Points and ploys.** Both players get 1 CP in the Ready step; from turning point two onward the player without initiative gets 2 CP instead. CP buys Strategy ploys (Gambit step, `STRATEGIC GAMBIT`) or Firefight ploys (during activations). Every player can use the universal **Command Re-roll** firefight ploy (1CP, re-roll one attack or defence die) plus their kill team's own ploys.

**Precedence.** When rules conflict: (1) explicit wording wins, (2) designer's commentary, (3) non-core-book rules beat core-book rules, (4) "cannot" wording wins, (5) active/controlling player decides, (6) the player with initiative decides.

---

## What this source does not cover

- Any faction/kill-team-specific rule (equipment, ploys, unique actions) - those live in the ten team pointers under `raw/pointers/kill_team_2024_teams.md`
- Killzone terrain specifics (Vantage rules, climbing/jumping heights per board) - `raw/pointers/kill_team_2024_missions.md` and the killzone stubs
- Critical Ops, Approved Ops, or Nemesis Operatives content
- Whether the **June 2026 Core Book update** changed anything from the owned Full-Scan PDF's printing - **open question, flagged below**

---

## Open questions

- **Update-log gap.** The owned PDF is a "Full Scan" with no confirmed print/revision date on file, and Wahapedia's book table shows the Core Book at "June 2026" versus an earlier "February 2026" row. `raw/pointers/kill_team_2024_core.md` also lists a separate, unread **Core Rules update log PDF**. Until someone reads it, treat any KT24 rule as potentially one erratum behind. Flagged rather than guessed.
- Has the owned PDF itself been cross-checked against the Lite rules or the Sniper rules update? Not yet - both pointers are unread.
- Wahapedia's KT24 hub sits at a `kill-team3` URL path (unlike the 40K `wh40k10ed` path-drift issue on [[wahapedia]]) - no edition-path ambiguity observed here, but only one page was read.

---

## Pages this source fed

**Concepts (6, all new):** [[turning_points]], [[activations_apl]], [[cover_kill_team]], [[control_range_kill_team]], [[orders_conceal_engage]], [[injured_operatives]]

**Updated:** [[glossary]] (new Kill Team 2024 section + collision flags), [[overview]] (second-system note), [[index]]

---

## Related pages

- [[glossary]] - Kill Team 2024 terms and the 40K collision flags this source triggered
- [[glossary]] - the **Kill Team** entry there carries the standing "these are two separate games" warning
- `raw/pointers/kill_team_2024_core.md` - the owned PDF pointer, still unopened
- `raw/pointers/kill_team_web_living_sources.md` - the Wahapedia and Warhammer Community KT living references
- [[index]]
