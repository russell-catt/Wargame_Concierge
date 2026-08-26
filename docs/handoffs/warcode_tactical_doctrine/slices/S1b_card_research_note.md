# S1b — Card and map research note

- **Status:** Resolved - Complete
- **Date:** 2026-08-25
- **Track:** warcode_tactical_doctrine (card/map enhancement pass)
- **Sources:** `Warcode_Contract_Protocol_list.xlsx`, `protocol_cards.ocr.txt`, `rulebook_v087f_extract.txt`, map PNGs

## Contracts (8 cards)

| # | Protagen | Ulfari | MDR Executive Unit | Custodia Silens | VP |
|---|----------|--------|-------------------|-----------------|-----|
| 4186 | Commander Rickman | Soul Eater | Sergeant 139 | Justicar Julius | 1 |
| 9278 | Shellshocker | Phantom | Combat Medic | Cremator | 1 |
| 5039 | Bastion | Reaper | Machine Gunner | Confessor | 1 |
| 6037 | Blade | Shade | Grenadier | Punisher | 1 |
| 3697 | Blast | Stalker | Comms Operator | Tormentor | 1 |
| 4913 | Anvil | Doom | Corporal | Lancer | 1 |
| 3512 | Smasher | Ravener | Marksman | Assassin | 1 |
| 2984 | Hammer | Wraith | Private | Executor | 1 |

**Verdict:** Deck is complete and uniform (1 VP each). Resolves VIP review **B8** framing — deck is buildable; beta *play* still limited to two published rosters. MDR/Dominium names on cards match marketing faction labels (Custodia Silens = Dominium line).

**Shipping:** Quote via `contract_cards_transcription.txt`; cite PDF pp.24–25 `via typed transcription`.

## Protocols (20 rows)

Five effects × four map scopes: **Left**, **Centre**, **Right**, **Total** (Left, Centre, Right).

| Issue | Sources | Severity | Action |
|-------|---------|----------|--------|
| **Hunt — full health?** | OCR: "units **with full health** take 3 damage"; xlsx: "all units … take 3 damage" | **Closed** — OCR/PDF authoritative; xlsx error | Quote OCR in shipping; footnote xlsx |
| **Total Hunt flavour** | xlsx copies Magnet flavour; OCR has correct turret text | Low — transcription error | Use OCR/PDF flavour for Total Hunt in shipping |
| **Total Hunt/Centre/Right room Hunt** | xlsx Hunt non-Total rows also copy Magnet flavour for Centre/Right | Low — xlsx typos | Use OCR base "Hunt" flavour for room variants |
| **Silence typo** | xlsx: "ranges weapons"; OCR: "RANGED WEAPONS" | Low | Quote OCR spelling in block quotes |
| **Total variant scope** | OCR notes flavour says "all rooms" but rule text still says "this room" | Medium — polish bug | Retain in §12 B-series or design notes |
| **Room selection** | Card **map graphic** lights Left/Centre/Right or all three (Total); deployment top/bottom never lit | **Closed** — owner table read 2026-08-25 | Document in Scenarios + Protocol reference; §12 B10 closed |

## Map images

### Core_Machine_placement.png

- **Board:** 33" × 24"
- **Deployment:** Area A (top), Area B (bottom)
- **Rooms:** Left wing, central hex (6 doors), right wing — **three protocol rooms**
- **Terrain:** Full cover walls (solid), partial cover (dashed); 10 doorways total (6 into hex, 4 on diagonal deployment walls)
- **Centre feature:** Solid circle in hex (scenario core)

### Core_Machine_obj_placement.png

| D6 | VP tokens | Layout summary |
|----|-----------|----------------|
| 1–3 | 3 each | Left 3" / centre-left on hex / right 3" (identical) |
| 4 | 4 | Left 3", vertical pair at horizontal centre (8" from top/bottom deployment lines), right 3" |
| 5 | 5 | Four corners 2.5"×7.5" + centre-left on hex |
| 6 | 6 | Corner pairs + mid-right pair (asymmetric vertical spacing) |

**Verdict:** Closes Board_Setup open question on D6 mapping. Token **values** (1 vs 2 VP per token) still read from printed token art at setup — diagrams show positions only.

## Discrepancy routing

| Destination | Items |
|-------------|-------|
| **Rulebook_Quotes / reference tables** | Full contract deck; protocol room variants (OCR-primary for Hunt/Total flavour) |
| **§12 B bugs** | Hunt xlsx error only (OCR wins) |
| **§12 A gaps** | ~~Protocol target room draw~~ — closed: card map highlights |
| **Footnotes only** | xlsx Total Hunt flavour typo |

## Related outputs

- `raw/the_warcode/contract_cards_transcription.txt`
- `raw/the_warcode/protocol_cards_transcription.txt`
- `games/the_warcode/rules/Contract_Cards_Reference.md`
- `games/the_warcode/rules/Protocol_Cards_Reference.md`
