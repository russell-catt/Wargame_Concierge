<!--
FILE: games/kill_team_2024/setup/killzones/volkus.md
VERSION: v0.5.0 (2026-08-18)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, slice S2; patch sync slice P)

DOCUMENT_TYPE: Teaching Guide / Killzone Reference
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: Kill Team 2024 (3rd Edition / KT24)
OWNERSHIP_STATUS: READY - play-now priority (track_in.md, Preflight lock 2026-08-17)
REFERENCE_STATUS: Active - teaching paraphrase; Door Fight / ruin / stronghold / fire-step aligned to Jun 17 update log (2026-08-18)

SOURCES:
  - raw/pointers/kill_team_2024_missions.md (Volkus Compound mission pack PDF, owned)
  - raw/pointers/kill_team_2024_core.md (Core Rules - base Killzone: Volkus terrain rules)
  - games/kill_team_2024/rules/Patch_Manifest.md
  - Wahapedia Kill Team 3 - Killzones page (Killzone: Volkus section, retrieved 2026-08-17)
  - Warhammer Community - Kill Team: Brutal and Cunning preview (Killzone: Volkus standalone release, retrieved 2026-08-17)
  - docs/handoffs/kill_team_2024_scaffold/track_in.md

PURPOSE:
  Teach what Killzone: Volkus is, what it's for, and how to set it up for a
  first game, without transcribing its terrain reference sheet or mission maps.

UPDATE_TRIGGER:
  Update when the Compound Siege upgrade is confirmed owned, when a Volkus
  mission map is actually laid out and played, or when Approved Ops adds new
  Volkus maps.
-->

# Killzone: Volkus - play-now cityfight terrain

**Status: READY.** Volkus is one of the two recommended killzones for a first game (alongside the [3e Starter Set](starter_set_3e.md)).

---

## What it is

Killzone: Volkus is the **urban cityfight** terrain family introduced with the Kill Team: Hivestorm box for the 2024 edition. It represents the ruined hive city of Fissilicus on the planet Volkus - fought over across several Kill Team releases (Hivestorm, Brutal and Cunning, Shadowhunt). Terrain is a mix of multi-level **strongholds** (buildings with an accessible upper Vantage floor), **large and small ruins**, and rubble pieces of varying size - roughly: two strongholds, two large ruins, two small ruins, and a handful of rubble pieces per standard set. Confirm exact counts against the owned terrain sprue or reference sheet before you rely on this for a tournament.

The board is a standard **30" x 22"** double-sided killzone board (see [`../Board_Setup.md`](../Board_Setup.md)).

---

## What makes it play differently

- **Strongholds are the signature feature.** Their upper level(s) are **Ceiling and Vantage**.
- **Cityfight adds Volkus-only rules** that do **not** belong on the core valid-target tree ([`../../rules/Target_Eligibility.md`](../../rules/Target_Eligibility.md)):
  - **Door Fight:** in the Select Enemy Operative step, pick an enemy on the **killzone floor**, within **2"** of, and on the **other side of**, a door the active operative is **touching**.
  - **Condensed Stronghold** (update log): the stronghold weapon interaction cares whether the target is **wholly within** a stronghold and on the **killzone floor or a fire step**.
  - Being on a **fire step** does **not** let you ignore the rest of the stronghold for **obscured**.
- **Doors and windows matter for line of sight.** A large ruin's **upper level is Ceiling and Vantage**; its **door is Accessible and Heavy**. For **control range**, ignore that door when determining visibility — but ignoring the door for CR does **not** let you Shoot a target that is not actually **visible**.
- **Stronghold extra parts** (update log; confirm against your terrain sheet): barrels on Stronghold A are Blocking and Heavy; small broken ramparts on Stronghold A's Vantage edge are Insignificant and Exposed; the gap on Stronghold B's lower Vantage is Accessible; Stronghold B's highest roof is one friendly operative at a time, placed to one side (treat-as-there for CR, visibility, and distance if the base will not fit).

For the shared vocabulary (Heavy, Light, Vantage, Cover, Obscured) see [`../Terrain_Basics.md`](../Terrain_Basics.md).

---

## Setting it up

1. If you have a specific Volkus mission map (from the Approved Ops card pack, Hivestorm, or the owned **Volkus Compound mission pack**), lay terrain out exactly as it shows.
2. If you're playing a non-specific mission, use the asymmetric-setup guidance in [`../Terrain_Basics.md`](../Terrain_Basics.md): a stronghold and a large ruin near each drop zone for early cover, rubble and small ruins filling the lanes between.
3. Agree every part's terrain type before deployment - especially which windows are Barred, which vents are Blocking, and which upper floors are Vantage.

---

## Missions

- **Everyday play:** the core-book Preliminary Ops / Joint Ops missions (from Hivestorm) or the current Approved Ops card pack's Volkus maps - see [`../../critical_ops/README.md`](../../critical_ops/README.md) for how those decks plug in.
- **Owned advanced content - Volkus Compound:** the owned **Volkus Compound mission pack** PDF is an asymmetric siege scenario (one team attacks, one defends a compound) built around the **Killzone Upgrade: Compound Siege** terrain (stockades, bunkers, fire steps). Treat this as a second-session upgrade, not a first-game pick - confirm whether the Compound Siege terrain itself is owned before planning a session around it; if it isn't, the mission pack's PvE/ruse sections may still be usable with reduced terrain, but check the PDF.

---

## What to check in the owned PDFs before your first game

- Exact terrain piece counts and which parts of each piece are Heavy vs Light vs Exposed (Core Book terrain reference sheet or the Volkus box insert)
- Whether the Compound Siege terrain upgrade is physically owned, separate from the base Volkus set
- Door Fight and the stronghold-specific weapon interaction, read in full rather than from this summary

---

## Related pages

- [`README.md`](README.md) - all owned kill zones
- [`starter_set_3e.md`](starter_set_3e.md) - the other play-now recommendation
- [`shadowhunt.md`](shadowhunt.md) - uses Volkus terrain (folded in half) for its "Descent" upper level
- [`../Terrain_Basics.md`](../Terrain_Basics.md) - Cover, Obscured, and the shared terrain vocabulary
- [`../../rules/Patch_Manifest.md`](../../rules/Patch_Manifest.md) - Volkus errata rows
- [`../../critical_ops/README.md`](../../critical_ops/README.md) - matched-play mission decks that include Volkus maps

---

## Change Log
- v0.5.0 (2026-08-18): Project-wide semver snapshot (x.y.z).
- v1.1 (2026-08-18): Slice P — Door Fight, Large ruin Ceiling+Vantage / door CR, Stronghold parts, Condensed Stronghold, fire step does not ignore stronghold for obscured, door CR ≠ Shoot if not visible.
- v1.0 (2026-08-17): Initial killzone page (slice S2), cross-checked against Wahapedia KT3 Killzones and the Warhammer Community Brutal and Cunning preview, both read 2026-08-17.

## Attribution
- Project: Wargame_Concierge
- Maintainer: Russell Catt
- Warhammer 40,000: Kill Team is a trademark of Games Workshop Limited. This document is a personal teaching paraphrase and reproduces no publisher text, terrain template, or mission map.

## Rising Tide Notes
- This document follows Rising Tide documentation standards.
- **Verify before you play.** Cross-check terrain counts, part types, and mission maps against the owned Core Book, Hivestorm box insert, and Volkus Compound mission pack PDF. Content reflects sources read on **2026-08-17**.
