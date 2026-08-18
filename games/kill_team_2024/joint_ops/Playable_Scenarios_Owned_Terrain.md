<!--
FILE: games/kill_team_2024/joint_ops/Playable_Scenarios_Owned_Terrain.md
VERSION: v0.5.0 (2026-08-18)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer + Librarian-assist, slice S9)

DOCUMENT_TYPE: Reference Matrix
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: Kill Team — 2024 / 3e (KT24)
REFERENCE_STATUS: Active — draft, retrieved 2026-08-17

SOURCES:
  - docs/handoffs/kill_team_2024_scaffold/track_in.md (ownership + play-now priority lock)
  - raw/pointers/kill_team_2024_missions.md
  - raw/pointers/kill_team_2024_terror_on_devlan.md
  - raw/pointers/kill_team_2024_screen_captures.md
  - raw/pointers/kill_team_2021_archive.md
  - Local mission pack PDFs (Terror on Devlan, Tomb World, Shadowhunt, Hivestorm, Volkus Compound) — read 2026-08-17
  - https://wahapedia.ru/kill-team3/the-rules/the-missions/ (retrieved 2026-08-17)
  - https://miniset.net/sets/gw-60010199077 ; Warhammer Community Shadowhunt pre-order article (retrieved 2026-08-17)

PURPOSE:
  Match every known Kill Team 2024 scenario against terrain actually owned, and
  say plainly whether it works for Join Ops (co-op/solo vs NPOs) today.

UPDATE_TRIGGER:
  Update when S2 lands killzone pages, when Tomb World terrain is assembled, or
  when a new mission pack ships.
-->

# Playable Scenarios × Owned Terrain

Every Kill Team 2024 scenario this project knows about, matched against what is physically ready to play on. **First sessions for the father-son pair are listed first.** Ownership statuses below are locked in `track_in.md` (Preflight, 2026-08-17); this page does not re-derive them, only applies them.

**Killzone pages now exist** (`setup/killzones/` — slice S2 landed during this session). Links below to `volkus.md`, `starter_set_3e.md`, `shadowhunt.md`, `tomb_world.md` resolve to real pages.

---

## First sessions (do these first)

| Scenario / source pack | Required killzone | Owned? | Join Ops suitable? | Notes |
|---|---|---|---|---|
| **Starter Handbook intro scenarios** (3e Starter Set box) | [3e Starter Set](../setup/killzones/starter_set_3e.md) — own slot-together MDF terrain, not Volkus | **Ready** | **Adapted** — simplified co-op-friendly sequence, not the formal Joint Ops mission pack | Gentlest true first game: Angels of Death vs Plague Marines (both owned, both priority teams), everything in one box, zero assembly. Play this before anything else if either player is brand new. |
| **Terror on Devlan — Mission 01: "The Hunt Begins"** (Terror on Devlan mission pack) | Killzone: [Volkus](../setup/killzones/volkus.md) | **Ready** | **Yes** — native Joint Ops | Self-contained: own kill team (Spectre Squad), own NPOs (Red Terror, Termagants, Ripper Swarms). Nothing extra to buy or assemble. Best single first *Joint Ops* session. |
| **Core Joint Ops — "Breach"** (Kill Team Core Book) | Killzone: [Volkus](../setup/killzones/volkus.md) | **Ready** | **Yes** — generic Joint Ops | Simplest possible generic on-ramp. Generic Trooper-tier NPOs from the Core Book; no expansion needed. Win = incapacitate every NPO; lose = lose every operative. The Core Book's alternate map for "any killzone that isn't close quarters" means this can also be attempted on the 3e Starter Set's own terrain if preferred. |
| **Core Joint Ops — "Sabotage"** (Kill Team Core Book) | Same as above | **Ready** | **Yes** | Adds a reinforcement-wave Strategic Gambit once half the NPOs are down; adds the Sabotage mission action on objective markers. |
| **Core Joint Ops — "Escape"** (Kill Team Core Book) | Same as above | **Ready** | **Yes** | Escape-the-board win condition (50%+ of operatives must exit); same reinforcement pressure as Sabotage. Good session-three escalation. |

---

## Later sessions (terrain-gated or campaign continuation)

| Scenario / source pack | Required killzone | Owned? | Join Ops suitable? | Notes |
|---|---|---|---|---|
| **Terror on Devlan — Missions 02-09** (campaign continuation) | Killzone: [Volkus](../setup/killzones/volkus.md) | **Ready** | **Yes** | Continue the 9-mission branching campaign from Mission 01; path (green/red arrows) depends on winning or losing the prior mission. |
| **Joint Ops: Tomb World mission pack** (6 missions, e.g. "Recover Transponder") | Killzone: [Tomb World](../setup/killzones/tomb_world.md) | **Unassembled** | **Adapted** — blocked until built | NPOs are Necron constructs (Scarab Swarms, Warriors, Tomb Crawlers, Macrocytes) — same families already owned in the 40K Necron collection. Genuinely playable the day Tomb World terrain is assembled; not before. Being honest about this rather than papering over it. |
| **Joint Ops: Shadowhunt** (3 co-op missions, boss finale) | Descent killzone ([Volkus](../setup/killzones/volkus.md) **+** [Tomb World](../setup/killzones/tomb_world.md), upper/lower linked boards — see [`shadowhunt.md`](../setup/killzones/shadowhunt.md)) | **Boards + tokens owned**, but full Descent needs Tomb World assembled too | **Adapted** | The box ships 2 half-size cardboard boards and no terrain sprues of its own — it leans on owned Volkus and Tomb World terrain for the "real" 3D experience. Workaround confirmed in `shadowhunt.md` (S2) and a public review: fold an existing board to approximate the second level, or wait for Tomb World. Final mission is a named boss fight (C'tan Shard of the Nightbringer). Murderwing and Celestian Insidiants **team rules** are owned per `raw/pointers/kill_team_2024_teams.md`; whether this specific box's own models/dossier are owned is unconfirmed per `shadowhunt.md` — check the physical box. |
| **Adversary Ops: Shadowhunt** (3 competitive missions) | Same Descent killzone as above | Same as above | **PvP-only** | Same box, competitive counterpart pack. Listed for completeness — not a Join Ops mode. |
| **Nemesis Operatives — Ambull mission pack** (Joint Ops + Adversary Ops missions) | Any killzone (book doesn't fix one) | Ambull model not owned; dossier owned but unreadable (see gap below) | **Yes** in Joint Ops mode / **Adapted** in Adversary Ops mode | Needs either the Ambull model or the Custom Builder applied to an owned large model. Content largely unverified locally — see `NPO_Catalog.md` Gaps. |
| **Nemesis Operatives — Archivist mission pack** ("Betrayal" Joint Ops / "Negotiation" Adversary Ops) | Any killzone | Archivist (Zoat) model not owned; dossier owned but unreadable | **Yes** in Joint Ops mode / **Adapted** in Adversary Ops mode | Same caveats as Ambull row. |
| **Nemesis Operatives — Custom Builder, worked examples** (Armoured Sentinel, XV8 Crisis Battlesuit, Screamer-Killer, Redemptor Dreadnought) | Any killzone | None of the four example models owned | **Yes**, if a substitute owned large model is built with the Custom Builder | Illustrative examples in the book, not fixed NPOs — the actual playable content is "build your own." Locally unreadable; see gap. |

---

## PvP-only (out of Join Ops scope, listed for completeness)

| Scenario / source pack | Required killzone | Owned? | Join Ops suitable? | Notes |
|---|---|---|---|---|
| **Preliminary Ops mission pack** (Kill Team Core Book) | Killzone: Gallowdark, or a generic killzone via its alternate map | Ready | **PvP-only** | The competitive on-ramp before Approved Ops. Not Join Ops. |
| **Approved Ops 2025 tournament companion** | Varies by mission | Ready | **PvP-only** | Tournament matched-play framework; explicitly distinct from the owned physical Critical Ops decks. |
| **Multiplayer Ops mission pack** (3-4 players) | Two boards combined | Ready | **PvP-only** (multiplayer) | Free-for-all format; not a father-son two-vs-environment mode. |
| **Hivestorm launch mission — "The Great Gun Fires"** | Killzone: Volkus | Ready | **PvP-only** | Standard Crit Op (Transmission) mission using the normal game sequence; not a Joint Ops pack despite sharing Volkus terrain. |

---

## Secondary-trust / filler rows

| Scenario / source pack | Required killzone | Owned? | Join Ops suitable? | Notes |
|---|---|---|---|---|
| **White Dwarf / secondary trust — Procession PvE mission** | Not confirmed | Screenshots only, no killzone confirmed | **Unconfirmed** | Personal captures of WD content (`raw/pointers/kill_team_2024_screen_captures.md`). Real published material, but never overrides an official rules/mission-pack PDF, and confidence here is `draft` at best per that pointer's own trust-class rule. Do not run this as a father-son session until cross-checked against an official download or the held magazine issue. |
| **2e starter scatter terrain** (KT21 / archive) | N/A — 2e rules quarantined at `reference/kill_team_2e/` | Filler terrain only | **Not recommended** | The scatter pieces are physically usable as dressing on a 3e table; the 2e *rules* behind them are archive-only and never current play. Use for terrain variety only, never for scenario rules. |

---

## Ownership legend (from `track_in.md`)

| Term | Meaning |
|------|---------|
| Volkus ready | Killzone: Volkus terrain owned and assembled |
| 3e Starter ready | 3e Starter Set killzone owned and assembled |
| Shadowhunt boards + tokens | Shadowhunt boards and tokens confirmed owned; no terrain sprues of its own. Whether this specific box's dossier/teams are also owned is unconfirmed — see the Shadowhunt row above and `shadowhunt.md` |
| Tomb World unassembled | Kill Team: Tomb World terrain owned, not yet built |
| 2e scatter only | KT21 archive scatter terrain, filler use only |

**Resolved by S2 (landed during this session):** `volkus.md` and `starter_set_3e.md` are genuinely two different products, not one killzone under two names. **Killzone: Volkus** is the urban cityfight terrain family (strongholds, ruins, rubble) that first shipped with the Hivestorm launch box. The **3e Starter Set** is a separate, later (November 2024) box built around **Angels of Death vs Plague Marines** with its own slot-together MDF terrain and a simplified Starter Handbook, not Volkus terrain at all. Both are independently play-now ready; this page's earlier speculation that they might be the same killzone under two purchases was wrong, and is corrected here rather than silently dropped.

---

## Related pages

- [`README.md`](README.md) — how Join Ops works, first-session shortlist (summary of this page)
- [`NPO_Catalog.md`](NPO_Catalog.md) — what each mission pack's NPOs actually are
- [`NPO_Cheat_Sheet.md`](NPO_Cheat_Sheet.md) — running NPOs mid-game
- [`../setup/killzones/README.md`](../setup/killzones/README.md) — planned killzone pages (S2)
- [`raw/pointers/kill_team_2024_missions.md`](../../../raw/pointers/kill_team_2024_missions.md)
- [`raw/pointers/kill_team_2024_terror_on_devlan.md`](../../../raw/pointers/kill_team_2024_terror_on_devlan.md)
- [`raw/pointers/kill_team_2024_screen_captures.md`](../../../raw/pointers/kill_team_2024_screen_captures.md)

## Change Log
- v0.5.0 (2026-08-18): Project-wide semver snapshot (x.y.z).
- v1.0 (2026-08-17): Initial matrix (slice S9). First-session, later-session, PvP-only, and secondary-trust tiers.

## Attribution
- Project: Wargame_Concierge
- Maintainer: Russell Catt
- Warhammer 40,000: Kill Team is a trademark of Games Workshop Limited. Personal teaching paraphrase; no publisher text or statlines reproduced.

## Rising Tide Notes
- This document follows Rising Tide documentation standards.
- Must remain understandable, reproducible, and reusable.
