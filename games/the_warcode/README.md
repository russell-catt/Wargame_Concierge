<!--
FILE: games/the_warcode/README.md
VERSION: v0.7 (2026-09-24)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, track dataslate_0826 S5; warcode_tactical_doctrine S0 provenance)

DOCUMENT_TYPE: Game System Overview
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: The Warcode
REFERENCE_STATUS: Active

SOURCES:
  - raw/the_warcode/The-Warcode-Rulebook-V.0.8.9-F.pdf
  - raw/the_warcode/The-Warcode-Lorebook-Tactical-Doctrine-Field-Edition.pdf
  - raw/the_warcode/The Warcode Rulebook V.0.8.7-F.pdf
  - https://pre-launch.thewarcode.com/ (retrieved 2026-08-23)
  - https://gamefound.com/en/projects/redmakers/the-warcode (retrieved 2026-09-24)
  - https://www.kickstarter.com/projects/redmakers/the-warcode-stl-campaign (retrieved 2026-09-24)
  - https://steamcommunity.com/sharedfiles/filedetails/?id=3776386741 (retrieved 2026-09-24)
  - docs/Game_System_Scaffold.md
  - docs/handoffs/warcode_tactical_doctrine/track_in.md
  - docs/handoffs/warcode_kickstarter_refresh/research/R3_campaign_transition.md
  - docs/handoffs/warcode_kickstarter_refresh/research/R4_community_coverage.md

PURPOSE:
  Entry point for The Warcode teaching content. Vocabulary mapping, read order,
  and subtree map. Unofficial and unauthorized learning notes.

UPDATE_TRIGGER:
  New free beta supersedes v0.8.9-F; campaign status changes.
-->

# The Warcode

Third game system in Wargame_Concierge. **Edition in scope: free beta rulebook V.0.8.9-F** (RedMakers), checked **2026-09-24**.

**This subtree is unofficial and unauthorized.** Personal learning only — not endorsed by RedMakers, Gamefound, Kickstarter, or Steam.

**Source quoting:** Under `rules/`, `setup/`, `factions/`, and `lore/` you may quote the free publications verbatim with filename, PDF page, and section. The lorebook is narrative context only; mechanics defer to rulebook v0.8.9-F. Card references: [`rules/Contract_Cards_Reference.md`](rules/Contract_Cards_Reference.md), [`rules/Protocol_Cards_Reference.md`](rules/Protocol_Cards_Reference.md).

**Naming safety:** No GW comparator proper nouns in this subtree. Use **That other game** / **Murder Platoon**, **Rawmallet**, **39.876**, and **39.9** only — full ban table in `AGENTS.md` Sec 10 and [`.cursor/rules/warcode-quotes.mdc`](../../.cursor/rules/warcode-quotes.mdc).

**Last reviewed: 2026-09-24 · not affected by unrelated balance packages.** This subtree ships from RedMakers' free publications; balance-package work elsewhere in the repository has no bearing on these pages.

---

## Vocabulary mapping

| Scaffold term | The Warcode |
|---------------|-------------|
| Force | One of four fixed squads (8 units) |
| Force organisation | Faction pick + equipment distribution |
| Force-wide rule | Faction / leader abilities, Protocol cards |
| Round structure | 4 fixed rounds; Initiative Phase → Tactical Phase (alternating unit activation) |
| Scoring | VP from map control + scenario; **Contracts** when behind |
| Force size | Fixed 8 units (not points-based) |
| Board | **33" × 24"** playing surface |

---

## How to learn

1. **Sources** — [`raw/the_warcode/`](../../raw/the_warcode/) + pointers; [pre-launch](https://pre-launch.thewarcode.com/)
2. **Rules spine** — `rules/` (Overview, Turn_Structure, Key_Concepts, Keyword_Glossary, Rulebook_Quotes, **Contract_Cards_Reference**, **Protocol_Cards_Reference**)
3. **Deep-dives** — Activation, Combat, Equipment, Contracts, Scenarios
4. **Setup** — `setup/Board_Setup.md`, `Terrain_Basics.md`
5. **Guides** — vs That other game, proxy play, TTS, STL
6. **Factions** — Protagen Marines, Ulfari, MDR Executive Unit, and Dominium’s Custodia Silens
7. **Lore** — [`lore/`](lore/) for theatre, timeline, and source methodology
8. **Comparative glossary** — [`rules/Comparative_Glossary.md`](rules/Comparative_Glossary.md) bridges Warcode terms to That other game
9. **Campaign reviews** — [`reviews/Gamefound_Postmortem_2026-09-18.md`](reviews/Gamefound_Postmortem_2026-09-18.md) and [`reviews/Kickstarter_and_Community_2026-09-24.md`](reviews/Kickstarter_and_Community_2026-09-24.md)

---

## Campaign status — checked 2026-09-24

- The mixed-format Gamefound campaign launched **2026-09-15**; RedMakers posted its cancellation statement **2026-09-17**; Gamefound records the platform end on **2026-09-18** with no funds collected.
- The current Kickstarter launched **2026-09-23** and is scheduled through **2026-10-23**. It offers digital STL and Print & Play rewards only.
- Physical boxes are deferred publisher intent, not Kickstarter rewards; no date or guarantee is established.
- Live Kickstarter totals are volatile and remain in timestamped research rather than durable shipping pages.
- A public [Steam Workshop item](https://steamcommunity.com/sharedfiles/filedetails/?id=3776386741) is available, but its listing visibly says rules **v0.8.7**. Verify play against the current **v0.8.9-F** PDF.

---

## Subtree map

| Path | Status | Purpose |
|------|--------|---------|
| [`rules/`](rules/) | Active | Teaching + quotes + comparative glossary + **card references** |
| [`setup/`](setup/) | Scaffold | Board and terrain |
| [`factions/`](factions/) | Active | Four verified squad packages |
| [`lore/`](lore/) | Active | Shared setting, chronology, and evidence method |
| [`guides/`](guides/) | Scaffold | Cross-game and play aids |
| [`research/`](research/) | Scaffold | STL / printer notes |
| [`reviews/`](reviews/) | Active | Closed Gamefound postmortem + current Kickstarter/community analysis |

| [`rules/Contract_Cards_Reference.md`](rules/Contract_Cards_Reference.md) | Active | Eight-card contract deck lookup |
| [`rules/Protocol_Cards_Reference.md`](rules/Protocol_Cards_Reference.md) | Active | Twenty-row protocol deck (*Core of the Machine*) |

---

## Change Log

- v0.7 (2026-09-24): Added exact campaign-transition status, current digital-only Kickstarter scope, TTS v0.8.7 drift warning, and two tracked campaign review pages (S4).
- v0.6 (2026-09-24): Added Stage 3 lore navigation, source scope, and mechanics firewall.
- v0.5 (2026-09-24): Current rules baseline v0.8.9-F; four playable factions and new MDR/Custodia roster links (S2).
- v0.4 (2026-08-27): Added the locked "Last reviewed — not affected by Games Workshop balance packages" currency stamp; no GW proper nouns introduced (track `dataslate_0826` slice S5).
- v0.3 (2026-08-25): Read order + subtree — Contract_Cards_Reference, Protocol_Cards_Reference (S8).
- v0.2 (2026-08-24): Naming safety — full GW obfuscation table (Rawmallet / 39.9 / 39.876 + That other game).
- v0.1 (2026-08-23): S0 stub — vocabulary, subtree, unofficial disclaimer.
