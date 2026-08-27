---
title: Kill Team quarterly balance — Aug 2026 package
type: source
system: kill_team_2024
created: 2026-08-27
updated: 2026-08-27
version: 0.1.0
sources:
  - docs/handoffs/dataslate_0826/research/staging_kt_august_updates.md (retrieved 2026-08-27)
  - docs/handoffs/dataslate_0826/research/warcom_kt_balance_commentary_aug.md (owner paste, retrieved 2026-08-27)
  - raw/pointers/kill_team_2024_missions.md, raw/pointers/kill_team_2024_teams.md
confidence: draft
tags: [source, kill_team_2024, balance, quarterly, tomb_world, nemesis_ops, august_2026]
---

# Kill Team quarterly balance — Aug 2026 package

**There is no single titled "Balance Dataslate" file for Kill Team either.** The quarterly package is the **Core / killzone / mission-pack update logs combined with dated team online rules**, plus a WarCom "top five" commentary article naming design intent. Owner lock 2026-08-27 (same shape as the 40K package) — do not invent or hunt for a single dataslate filename.

**Confidence:** `draft`. Package pieces were read from staged PDFs (`raw/_dataslate_0826_staging/`, temporary, cleanup pending) and paraphrased into shipping under the KT24 Sec 10 quote exception; this KB page stays paraphrase only.

---

## Package pieces

| Piece | Stamp | Covers |
|-------|-------|--------|
| Killzone: Tomb World update log | Aug '26 | Teleport does not bypass "cannot end move closer" restrictions; teleport pad exclusions; breach action 2AP floor when combined with Charge/Shoot |
| Mission packs update log | Aug '26 | Nemesis Operatives: custom Nemesis should almost always keep Towering Size (Ambull/Archivist named exceptions only) |
| Team online rules (dated `eng_26-08_` etc.) | Aug '26 | Priority teams: Angels of Death, Canoptek Circle, Plague Marines. Stub-currency only: Hierotek Circle, Celestian Insidiants, Deathwatch, Murderwing, Vespid Stingwings |
| WarCom quarterly "top five" commentary | End-of-summer quarterly | Fellgor Ravagers, Goremongers, Hierotek Circle, Raveners, Wolf Scouts named — see teaching paraphrase below |

---

## Teaching paraphrase — WarCom "top five" (context; scope note below)

| Team | Change (paraphrase) |
|------|---------------------|
| Fellgor Ravagers | Frenzy ranged resistance dulled: a Shoot scoring 2+ normal successes can now incapacitate a frenzied target |
| Goremongers | Only one Aspirant may surge per turn; shooting profiles improved to compensate |
| **Hierotek Circle** | Regeneration loophole closed: revive-related regen now only kicks in the turn **after** an operative is brought back |
| Raveners | Durability down a couple of Wounds; must leave the Tunnel to complete the Dominate tac op |
| Wolf Scouts | Elemental-storm benefit now needs operatives **wholly within** the storm, not merely touching — much smaller effective area |

**Onboarded-scope note:** only **Hierotek Circle** is priority-relevant to this repo (regen-timing note, shipped). Fellgor Ravagers, Goremongers, Raveners, and Wolf Scouts are **not owned and out of shipping scope this pass** — recorded here for context, waived in `games/`.

## Teaching paraphrase — Core/killzone update logs (shipped)

- **Tomb World killzone:** teleport does not bypass "cannot end that move closer to…" restrictions; teleport pad keeps its 2" no-equipment-terrain rule and one-teleport-per-activation; Breach action cannot drop below **2AP** in an activation that also Charged or Shot.
- **Nemesis Ops:** custom Nemesis operatives should almost always keep **Towering Size** — even Small custom Nemesis keep the no-Conceal / always-valid-target behaviour; Ambull/Archivist are the only named ready-made exceptions.
- **Older/superseded errata** (Tomb World Nov '25 grey drop zone; Typhon Aug '25 terrain swap) — read for context, not re-taught; no owned page currently states the stale version.

---

## Shipping impact (complete as of this pass — S3)

| Surface | Disposition |
|---------|--------------|
| Killzone: Tomb World, Nemesis Ops (Custom Builder / How-To) | Updated — teleport/breach + Towering Size teaching |
| Angels of Death, Canoptek Circle, Plague Marines | Updated — full priority team guides cross-checked against staged packs |
| Hierotek Circle | Updated (stub) — regen-timing note added to `README.md`; no full `Team_Rule_Guide.md` yet |
| Celestian Insidiants, Deathwatch, Murderwing, Vespid Stingwings | Updated (stub) — currency + short package note only |
| Death Korps, Kommandos | **No-op, waived** — owner lock: no staged update this package |
| Fellgor Ravagers, Goremongers, Raveners, Wolf Scouts | **Waived, out of shipping scope** — not owned; commentary recorded here only |

Currency stamp used verbatim in shipping: `Rules currency: Kill Team quarterly balance — August 2026 (Core / update logs + team online rules) · teaching paraphrase · verify owned PDFs · confidence draft.`

---

## What this source does not cover

- A titled "Balance Dataslate" PDF for Kill Team — it does not exist this pass
- Full team-rule guides for stub teams (Hierotek, Celestian Insidiants, Deathwatch, Murderwing, Vespid Stingwings) — currency notes only, not a cross-check
- The 40K sibling package — see [[40k_aug_2026_balance_package]]

---

## Open questions

1. Canonical WarCom URL for the "top five" commentary article (egress blocked at capture time).
2. Expand shipping scope beyond priority teams + Hierotek note (owner call)?

---

## Related pages

- [[40k_aug_2026_balance_package]] — the 40K sibling package, same "no singular dataslate" shape
- [[kill_team_2024_core_rules]] — KT24 quote policy and Sec 10 exception this package ships under
- [[nemesis_operatives]] — Towering Size teaching context
- [[index]]
