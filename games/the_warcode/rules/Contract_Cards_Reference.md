<!--
FILE: games/the_warcode/rules/Contract_Cards_Reference.md
VERSION: v0.2 (2026-09-24)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, warcode_tactical_doctrine S1b)

DOCUMENT_TYPE: Reference / Card Lookup
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: The Warcode
REFERENCE_STATUS: Active — verified equivalent, beta v0.8.9-F (2026-09-24)

SOURCES:
  - raw/the_warcode/The-Warcode-Rulebook-V.0.8.9-F.pdf (current; pp.24–25; verified equivalent 2026-09-24)
  - raw/the_warcode/The Warcode Rulebook V.0.8.7-F.pdf (free public beta, RedMakers; retrieved 2026-08-23)
  - raw/the_warcode/contract_cards_transcription.txt (via typed transcription)
  - raw/the_warcode/spreadsheets/Warcode_Contract_Protocol_list.xlsx (Contracts sheet)

PURPOSE:
  Quick lookup for all eight contract cards: card ID, VP value, and the named
  Target unit per faction. Use when drawing a contract or checking which model
  your opponent might be hunting.

PRIMARY_AUDIENCE:
  - A player who just drew a contract and needs the Target for their matchup
  - An author cross-checking contract targets against team lists

KEY_SECTIONS_EXPECTED:
  - Shared card boilerplate
  - Eight-card table with faction targets
  - How to read a contract at the table

UPDATE_TRIGGER:
  A newer free beta changes contract count, VP values, or target names; or a
  cleaner OCR pass supersedes the typed transcription.
-->

# Contract Cards — reference table

All eight contract cards from current PDF pp.24–25. **`confidence: verified`**: card-image resources are equivalent between v0.8.7-F and v0.8.9-F. Verbatim quotes: [`Rulebook_Quotes.md`](Rulebook_Quotes.md) Sec 25. Mechanics: [`Contracts_and_VP.md`](Contracts_and_VP.md).

---

## Shared boilerplate

Every card prints the same header:

> You have received a contract. Eliminate the target designated by enemy faction.

When you draw, read the card **secretly**, then pick the Target matching your **opponent's faction**. If that unit is already dead, show the card, bottom it, and draw again (rulebook p.22).

---

## All eight contracts

Each card awards **1 VP** on fulfilment.

| Card ID | VP | Protagen Marines | Ulfari | MDR Executive Unit | Custodia Silens |
|---------|----|------------------|--------|--------------------|-----------------|
| **4186** | 1 | Commander Rickman | Soul Eater | Sergeant 139 | Justicar Julius |
| **9278** | 1 | Shellshocker | Phantom | Combat Medic | Cremator |
| **5039** | 1 | Bastion | Reaper | Machine Gunner | Confessor |
| **6037** | 1 | Blade | Shade | Grenadier | Punisher |
| **3697** | 1 | Blast | Stalker | Comms Operator | Tormentor |
| **4913** | 1 | Anvil | Doom | Corporal | Lancer |
| **3512** | 1 | Smasher | Ravener | Marksman | Assassin |
| **2984** | 1 | Hammer | Wraith | Private | Executor |

> Source: The Warcode Rulebook V.0.8.7-F.pdf — pp.24–25 — "CONTRACTS" — via typed transcription (raw/the_warcode/contract_cards_transcription.txt)

**Confirmed:** all eight cards are worth **1 VP** — the p.22 worked example (Shade on card 6037) matches the table.

**Spelling note:** card 4186 prints **Justicar Julius**. The playable Custodia roster on PDF p.39 prints **Justiciar Julius**. These are treated as the same character while preserving each source spelling.

---

## At the table

1. End of round: if you trail by **1+ VP**, draw one contract.
2. Match the Target to the faction your opponent is playing.
3. Fulfil when that unit is eliminated — by you, by scenario events, or by any other means.
4. Announce, show the card, add **1 VP**, discard.

---

## Related pages

- [`Rulebook_Quotes.md`](Rulebook_Quotes.md) — verbatim contract rules and full card quotes (Sec 25)
- [`Contracts_and_VP.md`](Contracts_and_VP.md) — trigger, secrecy, and catch-up play
- [`Scenarios_and_Events.md`](Scenarios_and_Events.md) — scenario kills that can fulfil contracts for you

---

## Open questions

- Whether duplicate Target names can appear on different card IDs in a future expansion.

---

## Change Log

- v0.2 (2026-09-24): Updated current provenance, recorded card equivalence, and added Justicar/Justiciar source note (S2).
- v0.1 (2026-08-25): Initial eight-card table from typed transcription (S1b).

## Attribution

- Project: Wargame_Concierge
- Maintainer: Russell Catt
- The Warcode is property of RedMakers. Unofficial, unauthorized personal learning notes — never for sale.

## Rising Tide Notes

- This document follows Rising Tide documentation standards.
- One card, four names — only one is your hunt.
