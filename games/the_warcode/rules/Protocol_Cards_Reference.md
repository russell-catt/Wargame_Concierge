<!--
FILE: games/the_warcode/rules/Protocol_Cards_Reference.md
VERSION: v0.1 (2026-08-25)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, warcode_tactical_doctrine S1b)

DOCUMENT_TYPE: Reference / Card Lookup
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: The Warcode
REFERENCE_STATUS: Active — draft, beta v0.8.7-F (2026-08-25)

SOURCES:
  - raw/the_warcode/The Warcode Rulebook V.0.8.7-F.pdf (free public beta, RedMakers; retrieved 2026-08-23)
  - raw/the_warcode/protocol_cards.ocr.txt (via OCR)
  - raw/the_warcode/protocol_cards_transcription.txt (via typed transcription)
  - raw/the_warcode/spreadsheets/Warcode_Contract_Protocol_list.xlsx (Protocols sheet)

PURPOSE:
  Row-by-row lookup for all 20 Core of the Machine protocol cards: title,
  map section (Left / Centre / Right / Total), flavour text, and rule text.

PRIMARY_AUDIENCE:
  - A player who just drew a protocol and needs to know which room(s) are hot
  - An author writing scenario tactics without re-reading OCR blocks

KEY_SECTIONS_EXPECTED:
  - 20-row master table
  - Hunt rule discrepancy footnote (FULL HEALTH vs all units)
  - Transcription error notes

UPDATE_TRIGGER:
  A newer free beta changes protocol effects, adds cards, or a physical re-read
  resolves the Hunt wording dispute.
-->

# Protocol Cards — reference table

Twenty activation cards for *Core of the Machine* (PDF pp.28–32). **`confidence: draft`**, OCR read **2026-08-23**, room variants transcribed **2026-08-25**. Verbatim OCR quotes: [`Rulebook_Quotes.md`](Rulebook_Quotes.md) Sec 29. Scenario context: [`Scenarios_and_Events.md`](Scenarios_and_Events.md).

Draw one at the **start of each round**. The **map section** on the card tells you which room(s) on the three-room ship map suffer the effect.

---

## Master table (20 rows)

Flavour for **Hunt** / **Total Hunt** rows marked *OCR* — the owner spreadsheet copied Magnet flavour by mistake for Centre, Right, and Total Hunt. Rule text follows the typed transcription unless noted.

| # | Title | Map section | Flavour | Rule |
|---|-------|-------------|---------|------|
| 1 | Magnet | Left | The floor in the room became heavily magnetized. Movement becomes difficult. | All units that start their movement in this room suffer a -3 inch penalty to their movement profile |
| 2 | Total Magnet | Left, Centre, Right | The floor in the room became heavily magnetized. Movement becomes difficult. | All units that start their movement in this room suffer a -3 inch penalty to their movement profile |
| 3 | Magnet | Centre | The floor in the room became heavily magnetized. Movement becomes difficult. | All units that start their movement in this room suffer a -3 inch penalty to their movement profile |
| 4 | Magnet | Right | The floor in the room became heavily magnetized. Movement becomes difficult. | All units that start their movement in this room suffer a -3 inch penalty to their movement profile |
| 5 | Hunt | Left | Turrets Activate throughout the room. Target acquisition begins. | See [Hunt rule footnote](#hunt-rule-footnote) below |
| 6 | Total Hunt | Left, Centre, Right | *OCR:* Turrets Activate throughout all rooms. Target acquisition begins. | See [Hunt rule footnote](#hunt-rule-footnote) below |
| 7 | Hunt | Centre | *OCR:* Turrets Activate throughout the room. Target acquisition begins. | See [Hunt rule footnote](#hunt-rule-footnote) below |
| 8 | Hunt | Right | *OCR:* Turrets Activate throughout the room. Target acquisition begins. | See [Hunt rule footnote](#hunt-rule-footnote) below |
| 9 | Electricity | Left | Electrical Pulses start coursing through the room. It takes great effort to dodge electrical shocks. | At the end of the round, roll one D6 for each unit in the room. If the result is 3 or less, the unit takes 3 damage. |
| 10 | Total Electricity | Left, Centre, Right | Electrical Pulses start coursing through the room. It takes great effort to dodge electrical shocks. | At the end of the round, roll one D6 for each unit in the room. If the result is 3 or less, the unit takes 3 damage. |
| 11 | Electricity | Centre | Electrical Pulses start coursing through the room. It takes great effort to dodge electrical shocks. | At the end of the round, roll one D6 for each unit in the room. If the result is 3 or less, the unit takes 3 damage. |
| 12 | Electricity | Right | Electrical Pulses start coursing through the room. It takes great effort to dodge electrical shocks. | At the end of the round, roll one D6 for each unit in the room. If the result is 3 or less, the unit takes 3 damage. |
| 13 | Silence | Left | The room fills with unknown energy. All ranges [sic] weapons completely fail. | All units in the room cannot use ranged weapons. |
| 14 | Total Silence | Left, Centre, Right | The room fills with unknown energy. All ranges [sic] weapons completely fail. | All units in the room cannot use ranged weapons. |
| 15 | Silence | Centre | The room fills with unknown energy. All ranges [sic] weapons completely fail. | All units in the room cannot use ranged weapons. |
| 16 | Silence | Right | The room fills with unknown energy. All ranges [sic] weapons completely fail. | All units in the room cannot use ranged weapons. |
| 17 | Poison | Left | Caustic gas begins to seep throughout the room | At the end of the round, all units take 2 damage. |
| 18 | Total Poison | Left, Centre, Right | Caustic gas begins to seep throughout the room | At the end of the round, all units take 2 damage. |
| 19 | Poison | Centre | Caustic gas begins to seep throughout the room | At the end of the round, all units take 2 damage. |
| 20 | Poison | Right | Caustic gas begins to seep throughout the room | At the end of the round, all units take 2 damage. |

> Map sections and rule text: via typed transcription (raw/the_warcode/protocol_cards_transcription.txt)  
> Hunt / Total Hunt flavour (rows 6–8): via OCR (raw/the_warcode/protocol_cards.ocr.txt) — xlsx transcription error

---

## Hunt rule footnote

The **Hunt** and **Total Hunt** cards disagree between OCR and spreadsheet on who takes damage:

| Source | Wording |
|--------|---------|
| **OCR (printed card)** | AT THE END OF THE ROUND, ALL UNITS IN THE ROOM **WITH FULL HEALTH** TAKE 3 DAMAGE. |
| **Typed transcription (xlsx)** | At the end of the round, **all units in the room** take 3 damage. |

Until a second physical check resolves it:

- **Table play default:** use the **OCR / FULL HEALTH** reading if you want printed-card fidelity.
- **Alternate reading:** if **all units** is correct, wounded models in the room also take 3 damage at end of round — materially harsher for objective holders.

Total Hunt's OCR rule line still reads **"the room"** (singular) while the flavour says **all rooms** — same polish inconsistency flagged in [`Rulebook_Quotes.md`](Rulebook_Quotes.md) Sec 29.

---

## Transcription notes

- **Total Hunt flavour (row 6):** xlsx incorrectly copied Magnet text; OCR flavour used here.
- **Hunt Centre / Right flavour (rows 7–8):** xlsx incorrectly copied Magnet text; OCR Hunt flavour used here.
- **Silence flavour:** transcription preserves printed typo **"ranges weapons"** — OCR reads **"RANGED WEAPONS"**.
- **Total variants:** OCR flavour lines often say **"all rooms"** while rule lines still say **"this room"** or **"the room"** — flagged as beta polish bugs, not transcription errors.

---

## Related pages

- [`Rulebook_Quotes.md`](Rulebook_Quotes.md) — verbatim OCR quote blocks (Sec 29)
- [`Scenarios_and_Events.md`](Scenarios_and_Events.md) — when protocols fire in the round
- [`Contracts_and_VP.md`](Contracts_and_VP.md) — protocol kills that fulfil contracts
- [`../setup/Board_Setup.md`](../setup/Board_Setup.md) — three-room map layout

---

## Open questions

- **Hunt FULL HEALTH** — confirm against a physical card; affects whether damaged models can safely sit in a hunted room.
- Whether **Total** protocol rules intentionally hit all three rooms despite singular "this room" wording.
- Card-to-PDF-page mapping for each of the 20 faces (approximate pp.28–32 only).

---

## Change Log

- v0.1 (2026-08-25): Initial 20-row table; Hunt OCR vs transcription footnote; Total Hunt flavour from OCR (S1b).

## Attribution

- Project: Wargame_Concierge
- Maintainer: Russell Catt
- The Warcode is property of RedMakers. Unofficial, unauthorized personal learning notes — never for sale.

## Rising Tide Notes

- This document follows Rising Tide documentation standards.
- Left, Centre, Right, or all three — read the map section before you commit models to a room.
