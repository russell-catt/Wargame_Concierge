<!--
FILE: games/warhammer_40k_11e/rules/README.md
VERSION: v0.6.0 (2026-08-27)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, track dataslate_0826 / S2e)

DOCUMENT_TYPE: Index / Section README
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: Warhammer 40,000 - 11th Edition
REFERENCE_STATUS: Active - content authored in S3

SOURCES:
  - C:\Personal\40K\rules\eng_01-06_warhammer40k_new40k_core_rules.pdf (read 2026-08-16)
  - reference/Source_Library.md
  - docs/Game_System_Scaffold.md (Section B)

PURPOSE:
  Index for the rules teaching spine. Says what each document covers and in
  what order a beginner should read them.

UPDATE_TRIGGER:
  Update when a rules document is added, retired, or substantially revised.
-->

# Rules - Warhammer 40,000 11th Edition

**Status:** Teaching spine from **S3** (owned PDFs, read **2026-08-16**); numbered quote appendix from track **`40k_warcom_quotes`** (read **2026-08-18**); Universal Rules Updates **v1.1** currency pass from track **`dataslate_0826`** slice **S2e** (read **2026-08-27**).

Teaching pages stay **beginner paraphrase**. Verbatim Core text lives only in [`Core_Rules_Quotes.md`](Core_Rules_Quotes.md) (WarCom-free + local `eng_*`; filename + page + rule ID). Army / Codex / Faction Pack rules are **not** quoted here. **Warhammer 40,000 is Copyright Games Workshop Limited.** Personal use only; never for sale.

**Hierarchy:** Core (`eng_01-06_*`) is baseline; dated `eng_*` (Universal Rules Updates, Event Companion) supersede on the same topic; omission is not a patch. **Universal Rules Updates v1.1 (legal 26 Aug 2026) supersedes v1.0 (legal 22 Jul 2026) on the same topics** — v1.1 also adds disembark move typing (`18.06`/`18.07`), new in this edition.

**WD527 Commentary:** Teaching pages in this folder carry locked **Commentary (White Dwarf 527 — …)** blocks (tier **1.5** paraphrase + Cite line). Mechanics still lose to Core / Event Companion. Shipping track: [`docs/handoffs/wd527_research/track_shipping_in.md`](../../../docs/handoffs/wd527_research/track_shipping_in.md).

---

## Read in this order

| # | File | What it covers |
|---|------|----------------|
| 1 | [`Overview.md`](Overview.md) | What a game of 40K is: battle rounds, how you win, what an army is made of, battle sizes, what you need on the table |
| 2 | [`Turn_Structure.md`](Turn_Structure.md) | A checklist for one player turn, phase by phase, with the common beginner mistakes |
| 3 | [`Key_Concepts.md`](Key_Concepts.md) | The mechanics everything else sits on: the attack sequence, saves and damage, Objective Control, battle-shock, attached units |
| — | [`Wound_Roll_Reference.md`](Wound_Roll_Reference.md) | Numeric S×T wound chart (Core 05.02); [`../setup/print/40k_wound_roll_reference.html`](../setup/print/40k_wound_roll_reference.html) |
| — | [`Quick_Reference_Card.md`](Quick_Reference_Card.md) | System Letter 2-pager outline (WD527 topic map); print [`../setup/print/40k_system_quick_reference.html`](../setup/print/40k_system_quick_reference.html) |
| 4 | [`Keyword_Glossary.md`](Keyword_Glossary.md) | Every term in one place, grouped by movement, shooting, melee, saves, and mission - with a confidence status on each |
| — | [`Core_Rules_Quotes.md`](Core_Rules_Quotes.md) | Numbered Core ID index; verbatim quotes for teaching-spine + visibility/cover/armies; stubs for the rest |

Setup and terrain live one level across, in [`../setup/`](../setup/):

- [`../setup/Board_Setup.md`](../setup/Board_Setup.md) - table size, pre-game sequence, deployment, objectives
- [`../setup/Terrain_Basics.md`](../setup/Terrain_Basics.md) - terrain categories, cover and visibility, how much terrain is enough

---

## Confidence

The glossary tags every term `verified`, `draft`, or `unverified`. Anything not `verified` has not been checked against an owned 11th Edition source and should be confirmed before it settles an argument at the table.

Two items are flagged as open:

- **Battle-size points limits** are not stated in any PDF this project owns; they come from the mission material and the Warhammer 40,000 app.
- **The Cryptek Conclave detachment rule name** conflicts between the owner's notes ("Scientific Schemes") and the owned Necrons Faction Pack v1.1 ("Technosorcerous Augmentations"). Recorded in the glossary, unresolved, flagged for the Librarian.

---

## Sources

Every claim in this section can be checked against the local library catalogued in [`reference/Source_Library.md`](../../../reference/Source_Library.md). The primary source for all four documents is the owned Core Rules PDF, supplemented by the Universal Rules Updates, the Event Companion, and the Necrons Faction Pack.

---

## Games Workshop notice

**UNOFFICIAL.** This document is completely unofficial and in no way endorsed by Games Workshop Limited. Personal / no-charge use only — never for sale. Warhammer, Warhammer 40,000 and associated marks are trademarks of Games Workshop Limited. Used without permission. No challenge to their status intended. Warhammer 40,000 is Copyright Games Workshop Limited. Teaching notes by Russell Catt (Wargame Concierge). Games Workshop retains IP in the settings and characters. No official logos.

## Change Log
- v0.6.0 (2026-08-27): Universal Rules Updates v1.1 (legal 26 Aug 2026) currency pass — hierarchy note updated (v1.1 supersedes v1.0; disembark move typing `18.06`/`18.07` new); track `dataslate_0826` slice S2e.
- v0.5.3 (2026-08-25): Index Quick_Reference_Card + system QR print (wd527_shipping S4).
- v0.5.2 (2026-08-25): Pointer to WD527 Commentary blocks + `wd527_shipping` track (slice S1).
- v0.5.1 (2026-08-18): Quote appendix + WarCom-free exception (track `40k_warcom_quotes`). Teaching pages remain paraphrase with rule-ID cites.
- v0.5.0 (2026-08-18): Project-wide semver snapshot (x.y.z).
- v2.0 (2026-08-16): Replaced the S2 stub with a real index. Four rules documents authored (slice S3).
- v1.0 (2026-08-16): Stub created (slice S2).

## Attribution
- Project: Wargame_Concierge
- Maintainer: Russell Catt

## Rising Tide Notes
- This document follows Rising Tide documentation standards.
- **Verify before you play.** Cross-check anything in this section against the current Munitorum Field Manual and your faction pack - Games Workshop patches rules and points between publications. Content reflects sources read on **2026-08-16**.
