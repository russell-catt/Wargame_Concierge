<!--
FILE: games/kill_team_2024/joint_ops/README.md
VERSION: v1.1 (2026-08-17)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer + Librarian-assist, slice S9)

DOCUMENT_TYPE: Game System Overview (subtree entry point)
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: Kill Team — 2024 / 3e (KT24)
REFERENCE_STATUS: Active — sources read 2026-08-17 (Core Book Joint Ops mission pack via Wahapedia mirror,
  Terror on Devlan dossier + mission pack PDFs, Tomb World mission pack PDF, Shadowhunt mission pack PDF,
  WarCom Nemesis Operatives preview, retailer listings, Lexicanum)

SOURCES:
  - raw/pointers/kill_team_2024_nemesis_operatives.md
  - raw/pointers/kill_team_2024_missions.md
  - raw/pointers/kill_team_2024_terror_on_devlan.md
  - raw/pointers/kill_team_2024_teams.md
  - raw/pointers/kill_team_web_living_sources.md
  - https://wahapedia.ru/kill-team3/the-rules/the-missions/ (retrieved 2026-08-17)
  - https://www.warhammer-community.com/en-gb/articles/mmvq6nnx/sunday-preview-take-on-the-red-terror/ (retrieved 2026-08-17)

PURPOSE:
  Entry point for the father-son Join Ops (official name: Joint Ops) co-op subtree.
  Explains what Joint Ops is, how two players share one kill team against NPOs,
  and gives a first-session shortlist against owned terrain.

UPDATE_TRIGGER:
  Update when S2 lands killzone pages, when new NPO content ships, or when the
  Nemesis Operatives dossier PDF becomes text-readable and can be cross-checked directly.
-->

# Join Ops — cooperative play against NPOs

**Official rulebook name: "Joint Ops."** This project's track brief calls it "Join Ops"; both names mean the same thing and are used interchangeably below. It is the **player-vs-environment (PvE)** side of Kill Team 2024 — one or two players, sharing **one kill team**, against enemies the game itself controls (**non-player operatives**, or **NPOs**).

This is the father-son priority deliverable for the `kill_team_2024_scaffold` track: a co-op mode that lets two people learn the game **together** instead of across the table from each other.

---

## What Joint Ops actually is

The Kill Team 2024 Core Book includes a **Joint Ops mission pack** as one of three included formats:

| Format | Mode | What it is |
|--------|------|------------|
| Preliminary Ops | PvP | Head-to-head, the on-ramp to competitive Approved Ops. Not Join Ops — out of scope here. |
| **Joint Ops** | **PvE, co-op or solo** | You (or you-and-a-partner, playing as **one** side) against procedurally-run NPOs |
| Multiplayer Ops | PvP, 3-4 players | Free-for-all. Not Join Ops — out of scope here. |

**If playing cooperatively, you are still one "player."** Two people do not each get their own Command Points, equipment, or reinforcements — they manage one pool between them. In practice this means: pick one kill team, split its operatives between the two of you (evenly if possible, round up for a harder game or down for an easier one), and each of you moves and rolls for your own models during the shared activation sequence. This is the exact rules structure a father-son pair needs: neither player is running a bigger army than the other, and there is no "my army vs your army" tension to manage.

**Alternative: one player as game master.** Instead of splitting the kill team, one player can run the NPOs (their movement, targeting, dice) while the other runs the whole kill team. This suits a session where one player already knows the rules and wants to referee while the newer player learns to play a full roster.

NPOs are not built like normal kill teams — they use pre-made **datacards** describing "standard soldiers" (sentries, troops, guards) or, in the bigger releases, named monsters and war machines. Each NPO datacard names a **behaviour** (see [`NPO_Cheat_Sheet.md`](NPO_Cheat_Sheet.md)) that tells the players exactly what it tries to do when activated — there is no guessing or improvising an opponent's mind.

### The three tiers of Joint Ops content owned

| Tier | Source | Needs beyond Core Rules? | Owned? |
|------|--------|---------------------------|--------|
| **1. Generic Joint Ops** (Breach / Sabotage / Escape) | Core Book, built in | No — generic Trooper/Tough/Warrior/Heavy NPOs ship with the rules | Yes |
| **2. Themed Joint Ops mission packs** | Terror on Devlan, Tomb World mission pack, Shadowhunt | The relevant killzone terrain + that box's own included NPO datacards | Partially — depends on killzone, see [`Playable_Scenarios_Owned_Terrain.md`](Playable_Scenarios_Owned_Terrain.md) |
| **3. Nemesis Operatives** | Nemesis Operatives dossier | The dossier's Custom Builder, or its dedicated Ambull / Archivist mission packs | Owned locally, but **flagged as a gap** — see [`NPO_Catalog.md`](NPO_Catalog.md) |

Full catalog of what each tier contains: [`NPO_Catalog.md`](NPO_Catalog.md). Mid-game table aid for running any of it: [`NPO_Cheat_Sheet.md`](NPO_Cheat_Sheet.md).

**Owned painted NPO stand-ins (2026-08-17):** Tomb World **Warriors ×10** (mixed gauss flayer / gauss reaper) and **Scarabs ×3**, plus Canoptek **Tomb Crawlers** and **Macrocytes**, can stand in as Tomb World NPOs once Killzone: Tomb World terrain is built. Photos: [`raw/pointers/kill_team_necron_photos.md`](../../../raw/pointers/kill_team_necron_photos.md). These are **not** a kill team — do not create `teams/necron_npos/`. Detail: [`NPO_Catalog.md`](NPO_Catalog.md).

---

## Who to play

Pick **one** kill team as the player side. This track's priority human teams, all with full guides landed:

- [Canoptek Circle](../teams/canoptek_circle/README.md) — Necron
- [Plague Marines](../teams/plague_marines/README.md) — Death Guard
- [Angels of Death](../teams/angels_of_death/README.md) — Space Marines

(Full team subtree: [`../teams/README.md`](../teams/README.md) and [`../teams/_Owned_Teams_Inventory.md`](../teams/_Owned_Teams_Inventory.md).) Any of the ten owned teams can play Joint Ops; these three have full teaching packages (team rules, starter roster, quick-reference guide) this track, so they are the natural first picks for a father-son session while everyone is also learning the team itself. Angels of Death and Plague Marines are also the two teams included in the 3e Starter Set box, so that killzone and these two teams naturally pair for a very first game.

---

## First-session shortlist (father-son priority)

**Play-now priority terrain, per the track lock: Volkus and the 3e Starter Set first, then Shadowhunt, then Tomb World once assembled, with 2e scatter as filler only.** Matched against what is actually playable in Joint Ops mode today:

0. **If neither player has ever played Kill Team, start with the [3e Starter Set](../setup/killzones/starter_set_3e.md)'s own built-in intro scenarios** on its included slot-together MDF terrain (from the Starter Handbook, not the Joint Ops mission pack). It is the gentlest possible on-ramp — simplified sequence, everything in one box — before moving to true Joint Ops below.
1. **Terror on Devlan, Mission 01 — "The Hunt Begins"** on **[Killzone: Volkus](../setup/killzones/volkus.md)**. This is the single best first *Joint Ops* session: it is a self-contained boxed release with its own NPOs (Red Terror, Termagants, Ripper Swarms) and its own kill team (Spectre Squad, playable as the shared side or set aside in favour of one of the three priority teams), on terrain that is ready now. Nothing further to buy or build. Full row in [`Playable_Scenarios_Owned_Terrain.md`](Playable_Scenarios_Owned_Terrain.md).
2. **Core Joint Ops — "Breach"** on **[Killzone: Volkus](../setup/killzones/volkus.md)**. The simplest possible generic on-ramp: generic Trooper-tier NPOs, no expansion required, one clear win/lose condition (incapacitate every NPO, or lose every operative). Good as a true "first ten minutes of Kill Team" teaching session before Terror on Devlan's campaign structure.
3. **Core Joint Ops — "Sabotage" then "Escape"**, same terrain, once Breach lands. Same generic NPOs, escalating objective complexity (sabotage all markers; then escape the board under pressure).

Everything else — Tomb World's own Joint Ops mission pack, Shadowhunt's Joint Ops pack, and the Nemesis Operatives dossier's Ambull/Archivist content — is catalogued for later sessions in [`Playable_Scenarios_Owned_Terrain.md`](Playable_Scenarios_Owned_Terrain.md), honestly marked against what is actually assembled and readable today.

---

## Sourcing and honesty notes

- **Nemesis Operatives** primary owned source is the dossier only: `C:\Personal\Kill Team\kill_team_2024\1063073009-Kill-Team-Nemesis-Operatives-Dossier.pdf` — see [`raw/pointers/kill_team_2024_nemesis_operatives.md`](../../../raw/pointers/kill_team_2024_nemesis_operatives.md). A mislabeled local copy (Nemesis Claw retailer listing, not Nemesis Operatives rules) was **deleted 2026-08-17**; primary source is dossier only. **Data gap:** the dossier PDF is an unOCR'd image scan with no extractable text (OCR pending slice S1). Everything said about Nemesis Operatives content here and in the catalog is paraphrased from public secondary sources (Warhammer Community preview, retailer listings, Lexicanum), dated 2026-08-17, at `confidence: draft`. Dedicated teaching pages live under [`../nemesis_ops/`](../nemesis_ops/) (stubs until S2). **Cross-check against the physical book pages before relying on this for a Nemesis Operatives session.**
- **Community Content is out of scope.** `C:\Personal\Kill Team\Community Content\` is never used as a source for this pack.
- **Killzone pages now exist.** Slice S2 landed during this session and wrote `setup/killzones/volkus.md`, `starter_set_3e.md`, `shadowhunt.md`, `tomb_world.md`, and `starter_set_2e_scatter.md`. Links below point at those real pages. S2's own findings independently confirm this page's terrain calls (Volkus and the 3e Starter Set both play-now ready; Shadowhunt gated on Tomb World assembly; Tomb World terrain unassembled while its operatives are already game-ready in the 40K Necron inventory).

---

## Subtree contents

| Page | Purpose |
|------|---------|
| `README.md` (this file) | What Joint Ops is; how the father-son co-op works; first-session shortlist |
| [`NPO_Catalog.md`](NPO_Catalog.md) | Every released NPO / Nemesis Operative tier to date, paraphrased, with gaps flagged |
| [`NPO_Cheat_Sheet.md`](NPO_Cheat_Sheet.md) | Print-friendly mid-game table aid: behaviour loops, Threat Principle, do/don't |
| [`Playable_Scenarios_Owned_Terrain.md`](Playable_Scenarios_Owned_Terrain.md) | Every Joint Ops (and adjacent) mission matched against owned terrain and assembly state |

Killzone pages this README links to directly (S2, now live): [`../setup/killzones/volkus.md`](../setup/killzones/volkus.md), [`../setup/killzones/starter_set_3e.md`](../setup/killzones/starter_set_3e.md), [`../setup/killzones/shadowhunt.md`](../setup/killzones/shadowhunt.md), [`../setup/killzones/tomb_world.md`](../setup/killzones/tomb_world.md).

---

## Change Log
- v1.1 (2026-08-17): Owned painted Tomb World NPO stand-ins (Warriors, Scarabs, Canoptek Crawlers/Macrocytes) — pointer to photos and `NPO_Catalog.md`.
- v1.0 (2026-08-17): Full Join Ops pack (slice S9). Replaces the S0 stub.

## Attribution
- Project: Wargame_Concierge
- Maintainer: Russell Catt
- Warhammer 40,000: Kill Team is a trademark of Games Workshop Limited. Personal teaching paraphrase; no publisher text or statlines reproduced.

## Rising Tide Notes
- This document follows Rising Tide documentation standards.
- Must remain understandable, reproducible, and reusable.
