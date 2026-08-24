<!--
FILE: games/the_warcode/README.md
VERSION: v0.1 (2026-08-23)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, warcode_tactical_doctrine S0)

DOCUMENT_TYPE: Game System Overview
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: The Warcode
REFERENCE_STATUS: Active — scaffold

SOURCES:
  - raw/the_warcode/The Warcode Rulebook V.0.8.7-F.pdf
  - https://pre-launch.thewarcode.com/ (retrieved 2026-08-23)
  - docs/Game_System_Scaffold.md
  - docs/handoffs/warcode_tactical_doctrine/track_in.md

PURPOSE:
  Entry point for The Warcode teaching content. Vocabulary mapping, read order,
  and subtree map. Unofficial and unauthorized learning notes.

UPDATE_TRIGGER:
  New free beta supersedes v0.8.7-F; Gamefound launch changes tiers or rules.
-->

# The Warcode

Third game system in Wargame_Concierge. **Edition in scope: free beta rulebook V.0.8.7-F** (RedMakers).

**This subtree is unofficial and unauthorized.** Personal learning only — not endorsed by RedMakers or Gamefound. See the [Gamefound project](https://gamefound.com/en/projects/redmakers/the-warcode).

**Rules quoting:** Under `rules/`, `setup/`, and `factions/` you may quote the free beta PDF verbatim (filename + page). See `AGENTS.md` Sec 10. Protocol Cards may need OCR.

**Naming safety:** No GW comparator proper nouns in this subtree. Use **That other game** / **Murder Platoon**, **Rawmallet**, **39.876**, and **39.9** only — full ban table in `AGENTS.md` Sec 10 and [`.cursor/rules/warcode-quotes.mdc`](../../.cursor/rules/warcode-quotes.mdc).

---

## Vocabulary mapping

| Scaffold term | The Warcode |
|---------------|-------------|
| Force | Squad (8 units) |
| Force organisation | Faction pick + equipment distribution |
| Force-wide rule | Faction / leader abilities, Protocol cards |
| Round structure | 4 fixed rounds; Initiative Phase → Tactical Phase (alternating unit activation) |
| Scoring | VP from map control + scenario; **Contracts** when behind |
| Force size | Fixed 8 units (not points-based) |
| Board | **33" × 24"** playing surface |

---

## How to learn

1. **Sources** — [`raw/the_warcode/`](../../raw/the_warcode/) + pointers; [pre-launch](https://pre-launch.thewarcode.com/)
2. **Rules spine** — `rules/` (Overview, Turn_Structure, Key_Concepts, Keyword_Glossary, Rulebook_Quotes)
3. **Deep-dives** — Activation, Combat, Equipment, Contracts, Scenarios
4. **Setup** — `setup/Board_Setup.md`, `Terrain_Basics.md`
5. **Guides** — vs That other game, proxy play, TTS, STL
6. **Factions** — Protagen Marines + Ulfari first; MDR / Dominium stubs
7. **Comparative glossary** — end-of-doc bridges to That other game
8. **VIP review** — `reviews/Agentic_Rules_and_Marketing_Review.md` (after GATE)

---

## Subtree map

| Path | Status | Purpose |
|------|--------|---------|
| [`rules/`](rules/) | Scaffold | Teaching + quotes + comparative glossary |
| [`setup/`](setup/) | Scaffold | Board and terrain |
| [`factions/`](factions/) | Scaffold | Squad packages |
| [`guides/`](guides/) | Scaffold | Cross-game and play aids |
| [`research/`](research/) | Scaffold | STL / printer notes |
| [`reviews/`](reviews/) | Scaffold | Agentic marketing review |

---

## Change Log

- v0.2 (2026-08-24): Naming safety — full GW obfuscation table (Rawmallet / 39.9 / 39.876 + That other game).
- v0.1 (2026-08-23): S0 stub — vocabulary, subtree, unofficial disclaimer.
