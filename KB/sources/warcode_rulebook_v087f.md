---
title: The Warcode Rulebook V.0.8.7-F
type: source
system: the_warcode
created: 2026-08-23
updated: 2026-09-24
version: 0.9.1
sources: [raw/pointers/warcode_rulebook_v087f.md, raw/the_warcode/The Warcode Rulebook V.0.8.7-F.pdf, raw/the_warcode/rulebook_v087f_extract.txt, raw/the_warcode/contract_cards_transcription.txt, raw/the_warcode/protocol_cards_transcription.txt, raw/the_warcode/protocol_cards.ocr.txt, raw/the_warcode/spreadsheets/Warcode_Contract_Protocol_list.xlsx, raw/the_warcode/images/Core_Machine_placement.png, raw/the_warcode/images/Core_Machine_obj_placement.png, games/the_warcode/rules/Overview.md, warcode_rulebook_v089f]
confidence: draft
tags: [source, the_warcode, core_rules, beta, redmakers, quoting_policy]
---

# The Warcode Rulebook V.0.8.7-F

Historical free beta from RedMakers — superseded by [[warcode_rulebook_v089f]] on the same topic, but retained as provenance for unchanged pages and earlier shipping citations.

---

## Golden source

| Asset | Location |
|-------|----------|
| PDF | [`raw/the_warcode/The Warcode Rulebook V.0.8.7-F.pdf`](../../raw/the_warcode/The%20Warcode%20Rulebook%20V.0.8.7-F.pdf) |
| Pointer | [`raw/pointers/warcode_rulebook_v087f.md`](../../raw/pointers/warcode_rulebook_v087f.md) |
| Extract | [`raw/the_warcode/rulebook_v087f_extract.txt`](../../raw/the_warcode/rulebook_v087f_extract.txt) |
| Contract transcription | [`raw/the_warcode/contract_cards_transcription.txt`](../../raw/the_warcode/contract_cards_transcription.txt) |
| Protocol transcription | [`raw/the_warcode/protocol_cards_transcription.txt`](../../raw/the_warcode/protocol_cards_transcription.txt) |
| Protocol OCR | [`raw/the_warcode/protocol_cards.ocr.txt`](../../raw/the_warcode/protocol_cards.ocr.txt) |
| Owner spreadsheet | [`raw/the_warcode/spreadsheets/Warcode_Contract_Protocol_list.xlsx`](../../raw/the_warcode/spreadsheets/Warcode_Contract_Protocol_list.xlsx) |
| Core map / VP D6 images | [`raw/the_warcode/images/`](../../raw/the_warcode/images/) |

~37 pages. Protocol Cards and some layout pages may be flattened images — OCR before declaring gaps.

**Hierarchy:** V.0.8.9-F is current. This V.0.8.7-F source remains historical; omission is not a patch, and the 2026-09-24 delta check found pages 2–36 mechanically equivalent.

---

## Quote policy

| Layer | Verbatim Warcode rules? |
|-------|-------------------------|
| `games/the_warcode/rules/`, `setup/`, `factions/` | **Yes** — beta PDF in `raw/the_warcode/`; cite filename + page |
| `KB/` | **No** — teaching paraphrase, pointers, index only |

See [`.cursor/rules/warcode-quotes.mdc`](../../.cursor/rules/warcode-quotes.mdc).

---

## GW proper noun obfuscation (Warcode shipping)

**All Games Workshop proper nouns are banned in `games/the_warcode/**` shipping** — not only That other game's product title. This extends the existing Kill Team naming ban to every GW trademark and product name that could appear in comparative text, examples, or bridge copy.

| Banned (GW) | Use in `games/the_warcode/**` |
|-------------|-------------------------------|
| Warhammer | **Rawmallet** |
| 40,000 | **39.876** |
| 40K / 40k | **39.9** |
| Kill Team (and variants) | **That other game** / **Murder Platoon** |

**KB contract:** `KB/**` Warcode pages stay paraphrase and **may** document this policy and name the real systems for librarian context. When writing **collision flags** or **comparative bridges** meant to align with Warcode shipping examples, use **Rawmallet**, **39.9**, **39.876**, and **That other game** — never instruct shipping to paste GW product names. Cross-links to `games/kill_team_2024/` or `games/warhammer_40k_11e/` paths are fine as internal pointers; the obfuscated forms are for prose that would ship under `games/the_warcode/`.

Recorded **2026-08-24** (safety fix — `warcode_tactical_doctrine` naming policy).

---

## What this pass established

Teaching paraphrase from the extract, shipped under `games/the_warcode/rules/`:

| Topic | Shipping |
|-------|----------|
| Game shape | [`Overview.md`](../../games/the_warcode/rules/Overview.md) |
| Turn checklist | [`Turn_Structure.md`](../../games/the_warcode/rules/Turn_Structure.md) |
| Combat resolution | [`Key_Concepts.md`](../../games/the_warcode/rules/Key_Concepts.md) |
| Term lookup | [`Keyword_Glossary.md`](../../games/the_warcode/rules/Keyword_Glossary.md) |

**Historical roster state:** this edition contains Protagen Marines and Ulfari. The current edition adds MDR Executive Unit and Custodia Silens; see [[warcode_rulebook_v089f]].

**Transcribed 2026-08-25:** Full **8-card contract deck** (1 VP each; four faction target columns including MDR Executive Unit and Custodia Silens). **Protocol Cards** with Left/Centre/Right/Total map sections — see [`games/the_warcode/rules/Contract_Cards_Reference.md`](../../games/the_warcode/rules/Contract_Cards_Reference.md) and [`Protocol_Cards_Reference.md`](../../games/the_warcode/rules/Protocol_Cards_Reference.md). D6 VP placement diagrams captured from owner map PNGs in [`games/the_warcode/setup/Board_Setup.md`](../../games/the_warcode/setup/Board_Setup.md).

---

## Living web (secondary; rechecked 2026-09-24)

| URL | Use |
|-----|-----|
| https://pre-launch.thewarcode.com/ | Marketing, factions, VIP |
| https://gamefound.com/en/projects/redmakers/the-warcode | Historical campaign: creator-cancelled; platform ended 2026-09-18; no funds collected |

See [[warcode_web_prelaunch_2026_08]], [[warcode_gamefound_campaign_2026_09]],
and the current offer at [[warcode_kickstarter_relaunch_2026_09]].

---

## Open questions

- Default round count when a scenario omits it — marketing says four; rulebook text references "final round" without a universal default.

---

## Related pages

- [[warcode_rulebook_v089f]] — current mechanics source
- [[warcode_web_prelaunch_2026_08]] — historical marketing context
- [[warcode_action_points]] · [[warcode_ammo]] · [[warcode_overwatch]] · [[warcode_contracts]] · [[warcode_melee_lock]] — promoted concepts
- [[warcode_protagen_marines]] · [[warcode_ulfari]] · [[warcode_mdr]] · [[warcode_dominium]] — faction pages
- [`games/the_warcode/README.md`](../../games/the_warcode/README.md) — shipping entry point
