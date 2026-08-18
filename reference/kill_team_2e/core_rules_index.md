<!--
FILE: reference/kill_team_2e/core_rules_index.md
VERSION: v0.5.0 (2026-08-18)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, slice S8)

DOCUMENT_TYPE: Reference / Archive Index
PROJECT_NAME: Wargame_Concierge
REFERENCE_STATUS: Archive — NOT current play truth

SOURCES:
  - Wahapedia Kill Team 2 core rules, https://wahapedia.ru/kill-team2/the-rules/core-rules/ (retrieved 2026-08-17)
  - reference/kill_team_2e/sources.md

PURPOSE:
  Beginner-facing structural index of Kill Team 2021 (2e) core rules, paraphrased
  for future-planning reference only. Not a substitute for the owned PDFs and
  not current play guidance.

UPDATE_TRIGGER:
  Update if the Wahapedia KT2 page changes structure, or a future slice decides
  to actually revisit 2e play (currently no plan to do so).
-->

# Kill Team 2e (2021) — core rules index

> ## ⚠️ NOT FOR CURRENT PLAY
> This page paraphrases **Kill Team 2021 (2nd Edition)** for **future-planning reference only**.
> **Current play truth is Kill Team 2024 (3e / KT24)** — see [`games/kill_team_2024/`](../../games/kill_team_2024/) and its `rules/` teaching spine.
> Do not use anything on this page to adjudicate a KT24 game. Where 2e and KT24 diverge, KT24 wins, always.

**Sources:** Wahapedia KT2 core rules (retrieved 2026-08-17) + owned local PDFs — see [`sources.md`](sources.md). This is a **teaching paraphrase / index**, not a transcription — no datacard statlines, weapon profiles, or rules text are reproduced verbatim. Read the owned PDFs for exact wording before ever using 2e material at the table.

---

## 1. What a game of KT2 is

A KT2 battle is fought between two **Kill Teams** (squads of **operatives**, i.e. individual miniatures with their own datacard) on a **killzone** — a 30"×22" board with terrain. Distances use **combat gauges** (graded symbols: ~1", 2", 3", 6") rather than a tape measure, though inches work too.

Three **ways to play** exist, sharing the same core mechanics with different mission sequences:

| Way to play | Character |
|---|---|
| **Open Play** | Free-form, permissive — good on-ramp |
| **Matched Play** | Balanced, competitive baseline |
| **Narrative Play** | Story-driven, campaign-linked (Spec Ops) |

---

## 2. Datacard anatomy (per operative)

Each operative's datacard carries, in paraphrase:

- **Operative type** and **keywords** (some in angle brackets — a choice you lock in when the operative joins your roster, e.g. Chapter)
- **Physical profile:** Movement (M), Action Point Limit (APL), Group Activation (GA, if >1 the operative activates as a squad), Defence (Df), Save (Sv, lower is better), Wounds (W)
- **Ranged / melee weapon profiles:** Attacks (A), Ballistic/Weapon Skill (BS/WS, lower is better), Damage (Normal / Critical), Special Rules, Critical Hit Rules
- **Abilities** (passive; a repeated ability from two sources doesn't stack) and **unique actions** (that operative's special moves, beyond the universal action list in §5)

**Dice:** six-sided (D6); a D3 = D6 halved, rounded up. Rolling **off** = both players roll, high roll wins, ties re-roll. Modifiers to a roll are cumulative and can push a result above/below the normal 1–6 range.

---

## 3. Battle structure — four Turning Points

A battle is **4 Turning Points**, each with three phases run in strict order:

1. **Initiative phase** — ready all operatives (flip order tokens); determine who has initiative (roll-off after Turning Point 1, loser-of-previous-tie wins ties). Initiative breaks simultaneous-effect ordering and generally decides who acts first.
2. **Strategy phase** — each player generates 1 Command Point (CP); CPs bank between Turning Points. Players alternate spending CPs on **Strategic Ploys** (or passing) until both pass in a row; also alternate revealing eligible **Tac Ops** (selectable secondary objectives) in a **Target Reveal** step. **Tactical Ploys** (including the universal **Command Re-roll**, 1CP) are saved for use during the Firefight phase instead.
3. **Firefight phase** — players alternate activating one ready operative at a time (or a Group-Activation squad together) until all operatives have gone. Each activation: set/confirm an **order** (Engage or Conceal — see §6), generate APL action points, then spend them on actions (§5) until out of AP or actions.

> **Open question — KT24 comparison:** KT24 teaching docs now exist under [`games/kill_team_2024/rules/`](../../games/kill_team_2024/rules/) (slice S1, 2026-08-17). KT2's 4-Turning-Point / Initiative–Strategy–Firefight skeleton is part of the Kill Team lineage and may look broadly familiar, but do **not** assume any specific mechanic here (CP costs, ploy timing, activation caps) carries over unchanged. A deliberate side-by-side cross-check is still outstanding — treat every KT2↔KT24 comparison as unverified until that pass lands.

---

## 4. Orders: Engage vs Conceal

Every ready operative gets an order each activation (fixed to its pre-battle setup order on Turning Point 1, chosen freely afterward):

| Order | Trade-off |
|---|---|
| **Engage** | Can perform more actions (Shoot, Charge, Overwatch) but is a valid ranged target more easily |
| **Conceal** | Harder to target at range (invisible to shooters unless also in the open / unobscured / not in cover) but restricted in what it can do |

---

## 5. Universal actions (paraphrased, AP cost noted)

| Action | AP | Gist |
|---|---|---|
| **Normal Move** | 1 | Move up to M; can't start or end within an enemy's Engagement Range (unless a teammate already holds that enemy) |
| **Charge** | 1 | Move up to M+1 gauge increment; must end within Engagement Range of an enemy; blocked while Conceal |
| **Fall Back** | 2 | Move out of Engagement Range without ending back inside it; only usable while already engaged |
| **Dash** | 1 | Short move (~1 gauge), even if otherwise movement-restricted that activation |
| **Pass** | 1 | Do nothing; can be repeated to burn remaining AP |
| **Overwatch** | 0 | Reactive shot for an already-activated Engage operative, taken at a Ballistic Skill penalty, once per Turning Point, only usable while the opponent still has operatives left to activate |
| **Pick Up** | 1 | Take control of a nearby objective marker/token; carried tokens must be dropped before the carrier leaves the killzone |
| **Shoot** | 1 | Ranged attack — see §7; blocked by Conceal order or being in an enemy's Engagement Range |
| **Fight** | 1 | Melee attack against an enemy in Engagement Range — see §7 |

Plus **unique actions** (per-operative, on the datacard) and **mission actions** (per-mission briefing). **Free actions** trigger only when another rule grants them, cost no extra AP, but still count as "performed" for once-per-activation limits.

**Engagement Range** = mutual "in melee threat" zone: two operatives are in each other's Engagement Range if each is Visible to, and within ~1 gauge of, the other.

---

## 6. Attack resolution (paraphrased)

**Shooting sequence:** select weapon → select a valid target (visible, no friendly operative already engaging it) → roll attack dice (hits ≥ weapon's BS; a 6 always hits and is a **critical hit**; a 1 always misses) → defender rolls defence dice equal to Defence (successes ≥ Save; a 1 always fails; a 6 is a **critical save**; being in **Cover** banks one automatic normal save before rolling) → defender spends successful saves to cancel attacker hits (1 normal save cancels 1 normal hit; 2 normal saves cancel 1 critical hit; 1 critical save cancels either) → attacker resolves remaining hits as Normal or Critical Damage → incapacitated operatives are removed after all shots from that action resolve.

**Fight sequence** is similar but simultaneous and alternating: both roll melee attack dice at once, then attacker and defender **alternate** resolving hits, each choosing to **strike** (deal damage) or **parry** (cancel an opposing hit) per hit resolved. **Combat Support**: each extra friendly operative also engaging (and not double-engaged elsewhere) improves the fighter's Weapon Skill by 1 for that combat.

**Damage:** operatives track Wounds; 0 or less = incapacitated (removed, abilities lost). **Mortal wounds** bypass defence dice entirely. Below half Wounds = **injured** (Movement, BS, and WS all worsen by 1 gauge/point).

---

## 7. Objectives, line of sight, and terrain (paraphrased)

- **Objective control:** friendly operatives control a marker/token if their combined APL within range exceeds the enemy's combined APL in range; a carried token is always controlled by its carrier.
- **Line of Sight (LoS):** an Engage-order target is in LoS if Visible and not Obscured; a Conceal-order target additionally must not be in Cover. **Visible** = an unobstructed line from the shooter's head to the target model. **Obscured** = blocked by intervening Heavy/Obscuring terrain beyond a short tolerance. **Cover** = within range of a terrain feature or another base along the sightline, granting the shooting-sequence save bonus.
- **Terrain traits** (paraphrased): **Heavy** (blocks LoS, gives Cover), **Light** (gives Cover unless a Vantage Point says otherwise), **Traversable** (can be vaulted mid-move), **Insignificant** (no rules effect), **Scalable** (ignores a small climbing rounding penalty), **Barricades** (Light + Traversable, pre-set terrain), **Vantage Point** (elevated position with its own targeting rules for and against operatives standing on it).
- **Moving through terrain:** **Traverse** (short AP-free-distance vault), **Jump** (gap crossing, needs a successful D6 test in the base rules — the Balance Dataslate errata makes jump tests automatic), **Climb** (vertical move counted against Movement), **Drop** (descend without climbing), and **Fly** (ignores most of the above, including vertical distance).

---

## 8. Vocabulary quick-map (2e → general Kill Team lineage)

| KT2 term | Rough meaning |
|---|---|
| Turning Point | One full round (Initiative → Strategy → Firefight) |
| Command Point (CP) | Resource spent on Ploys |
| Strategic Ploy | CP-spend used in the Strategy phase |
| Tactical Ploy | CP-spend saved for use during Firefight (incl. universal Command Re-roll) |
| Tac Op | Selectable secondary objective |
| Order (Engage/Conceal) | Per-activation stance choice |
| Fire Team | A named sub-selection block used by some 2e kill teams (Compendium) |

Full KT24 vocabulary mapping (current play) lives in [`games/kill_team_2024/README.md`](../../games/kill_team_2024/README.md) — **do not assume the two tables align 1:1** until someone actually checks.

---

## Open questions

- Which specific KT2 mechanics (if any) survived into KT24 unchanged vs. which were reworked — deferred until a deliberate side-by-side against [`games/kill_team_2024/rules/`](../../games/kill_team_2024/rules/) (S1 has landed; the comparison pass has not).
- Whether this archive is ever revisited for an actual 2e game night, or stays permanently reference-only (current track intent: reference-only, filler terrain use of 2e scatter pieces aside).

## Related pages

- [`reference/kill_team_2e/README.md`](README.md) — quarantine notice, must-read first
- [`reference/kill_team_2e/sources.md`](sources.md) — local + web sourcing for this page
- [`reference/Source_Library.md`](../Source_Library.md) — full project source catalog
- [`games/kill_team_2024/README.md`](../../games/kill_team_2024/README.md) — current play truth (KT24)

## Change Log
- v0.5.0 (2026-08-18): Project-wide semver snapshot (x.y.z).
- v0.1 (2026-08-17): Initial paraphrased index built from Wahapedia KT2 core rules (slice S8).

## Attribution
- Project: Wargame_Concierge
- Maintainer: Russell Catt

## Rising Tide Notes
- This document follows Rising Tide documentation standards.
- Teaching paraphrase only — no publisher rules text reproduced verbatim.
