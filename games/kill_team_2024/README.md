<!--
FILE: games/kill_team_2024/README.md
VERSION: v0.7 (2026-08-21)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, slice S0)

DOCUMENT_TYPE: Game System Overview
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: Kill Team — 2024 / 3e (KT24)
REFERENCE_STATUS: Active — scaffold phase

SOURCES:
  - reference/Source_Library.md
  - docs/Game_System_Scaffold.md (Section B)
  - docs/handoffs/kill_team_2024_scaffold/track_in.md

PURPOSE:
  Entry point for Kill Team 2024 teaching content. States edition scope,
  vocabulary mapping, and how to learn using this subtree.

UPDATE_TRIGGER:
  Update when edition changes, new teams ship, or scaffold sections promote from KB.
-->

# Kill Team — 2024 / 3e (KT24)

Second game system in Wargame_Concierge. **Edition in scope: Kill Team 2024 (3rd Edition / KT24).**

Priority learning teams this track: **Canoptek Circle**, **Plague Marines**, **Angels of Death**. Joint Ops (father–son co-op vs NPOs) is a first-class deliverable under `joint_ops/`; Nemesis Operatives deep-dive under `nemesis_ops/` (S0 stubs).

**Personal use only — this project must never be sold.**

**Rules quoting (KT24 only):** This subtree may reproduce **verbatim** rules text from owned local PDFs under `C:\Personal\Kill Team\kill_team_2024\` (read in place; never commit PDFs). **40K** quoting is a separate exception under `games/warhammer_40k_11e/rules/` and `setup/` only (WarCom-free Core + rule IDs) — not in this subtree. Army/Codex folders remain paraphrase.

**Not current play:** older Kill Team 2021 / 2e material lives under [`reference/kill_team_2e/`](../../reference/kill_team_2e/) only.

---

## Vocabulary mapping

| Scaffold term | Kill Team 2024 |
|---------------|----------------|
| Force | Kill team / team |
| Force organisation | Team roster / selection |
| Force-wide rule | Faction / team rule |
| Sub-list rule package | Equipment / ploys (strategic & firefight, as applicable) |
| Unit entry | Operative datacard |
| Round structure | Turning points / activation sequence |
| Scoring | Mission / Crit Op / Tac Op / Kill Op (Approved Ops / Critical Ops) |
| Force size | Operative count / team limits (not 40K points) |

**Folder naming:** use `teams/` (not `armies/`) and `setup/killzones/` so Kill Team vocabulary does not fake 40K structure.

---

## Cross-game note (40K)

Rules for Kill Team and Warhammer 40,000 stay **separate**. Owned KT miniatures may be listed in 40K inventories when ruled-in, with **base-size / dual-legality** honesty — ownership does not equal tournament legality in both games.

---

## How to learn

1. **Sources** — [`reference/Source_Library.md`](../../reference/Source_Library.md) and [`raw/pointers/`](../../raw/pointers/) (KT24 paths under `C:\Personal\Kill Team\kill_team_2024`).
2. **Rules spine** — `rules/` (Overview, turn structure, key concepts, glossary, [target-eligibility quotes](rules/Target_Eligibility.md), [cheat sheet](rules/Target_Eligibility_Cheat_Sheet.html), [patch manifest](rules/Patch_Manifest.md)). Full-Scan baseline; dated `eng_*` patches supersede; Jul 25 lite is intro only.
3. **Setup + kill zones** — `setup/` and `setup/killzones/` (S2). Prefer **Volkus** or **3e Starter** for first games. Table aids: [`volkus_QR.md`](setup/killzones/volkus_QR.md), [`starter_set_3e_QR.md`](setup/killzones/starter_set_3e_QR.md).
4. **Critical Ops** — `critical_ops/` for how owned decks plug in.
5. **Joint Ops** — `joint_ops/` for NPO catalog, cheat sheet, and owned-terrain scenarios (S9).
6. **Nemesis Operatives** — `nemesis_ops/` for Custom Builder, modes, and WarCom free stats (S0 stubs; fill S2).
7. **Teams** — `teams/` inventory + priority packages (S3–S6).
8. **Event pack-out** — [`Event_Ready.md`](Event_Ready.md) (**READY** 2026-08-21).

---

## Subtree map

| Path | Status | Purpose |
|------|--------|---------|
| [`rules/`](rules/) | **Populated** | Overview, turn structure, key concepts, keyword glossary; [target-eligibility quote appendix](rules/Target_Eligibility.md) + [cheat sheet](rules/Target_Eligibility_Cheat_Sheet.html) + [Patch_Manifest](rules/Patch_Manifest.md) (owner verified 2026-08-18) |
| [`setup/`](setup/) | **Populated (S2)** | Board setup, terrain basics, and five owned-killzone pages (Volkus, 3e Starter, Shadowhunt, Tomb World, 2e scatter) |
| [`critical_ops/`](critical_ops/) | **Populated (S2)** | How the owned Critical/Approved Ops decks plug into a game; table aid in S7 |
| [`joint_ops/`](joint_ops/) | Complete (S9) | Father–son Joint Ops / NPO aids |
| [`nemesis_ops/`](nemesis_ops/) | Stub (S0) | Nemesis Operatives dossier teaching (Custom Builder, modes, WarCom stats) |
| [`teams/`](teams/) | Inventory populated (S3) | Owned teams inventory + team packages |
| [`Event_Ready.md`](Event_Ready.md) | **READY 2026-08-21** | Learning-event go-bag checklist |

---

## Community thanks

Huge thanks to the [/r/killteam](https://www.reddit.com/r/killteam/) community for all the guides and cheat sheets I've read over the last 2 years.

Specific thanks to these users for guides used as **layout inspiration** in this subtree (rules text always comes from owned GW PDFs):

- [u/rdditonator](https://www.reddit.com/user/rdditonator/) — valid-target decision tree (`Can_I_Shoot.jpeg`)
- [u/Armagonix](https://www.reddit.com/user/Armagonix/) — KT24 cheat sheets (Vers 1.21, `kt24_reference_second.pdf`, `kt24_solo_reference.pdf`) and unit datacard template (`kt24_unit_datacards_template.pdf`)
- [u/burgerdrome](https://www.reddit.com/user/burgerdrome/) — line-of-sight flowchart (`Kill Team LOS Flowchart`, 2025-12-06)

---

## Games Workshop notice

**UNOFFICIAL.** This document is completely unofficial and in no way endorsed by Games Workshop Limited. Personal / no-charge use only — never for sale. Warhammer, Kill Team and associated marks are trademarks of Games Workshop Limited. Used without permission. No challenge to their status intended. Kill Team is Copyright Games Workshop Limited 2024. Teaching notes by Russell Catt (Wargame Concierge). Games Workshop retains IP in the settings and characters. No official logos.

## Change Log
- v0.7 (2026-08-21): Event_Ready checklist (READY); Volkus QR Condensed Stronghold Lethal 5+ callout linked.
- v0.5.0 (2026-08-18): Project-wide semver snapshot (x.y.z).
- v0.6 (2026-08-18): Slice P — Patch_Manifest; targeting quotes owner-verified vs Full-Scan + Jun 17 update log + Jul 25 lite.
- v0.5 (2026-08-17): KT24 verbatim-quote policy, community thanks, target-eligibility corpus + cheat sheet, Canoptek/Plague datacards (`kt24_rules_quotes` track).
- v0.4 (2026-08-17): `join_ops/` renamed to `joint_ops/` (nemesis_ops_research S0); `nemesis_ops/` stub subtree added.
- v0.3 (2026-08-17): `setup/` and `critical_ops/` marked Populated after slice S2 (Board_Setup, Terrain_Basics, five killzone pages, expanded Critical Ops README).
- v0.2 (2026-08-17): `join_ops/` marked Complete after slice S9 (Join Ops pack: README, NPO catalog, cheat sheet, owned-terrain scenario matrix).
- v0.1 (2026-08-17): S0 stub — vocabulary, subtree map, cross-game note.

## Attribution
- Project: Wargame_Concierge
- Maintainer: Russell Catt
- **Kill Team is Copyright Games Workshop Limited 2024**

## Rising Tide Notes
- This document follows Rising Tide documentation standards.
- Must remain understandable, reproducible, and reusable.
