<!--
FILE: games/warhammer_40k_11e/README.md
VERSION: v0.6.0 (2026-08-27)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, track dataslate_0826 S5)

DOCUMENT_TYPE: Game System Overview
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: Warhammer 40,000 — 11th Edition
REFERENCE_STATUS: Active — WD527 shipping (trust ladder + Mission 38 spine)

SOURCES:
  - reference/Source_Library.md
  - docs/Game_System_Scaffold.md (Section B)
  - docs/Project_Planning.md Sec 3

PURPOSE:
  Entry point for the first worked example game system. States edition scope,
  vocabulary mapping, and how to learn 40K using this subtree.

PRIMARY_AUDIENCE:
  - Parent (Necrons) and son (Space Marines) learning together
  - AI sessions building rules and army content

KEY_SECTIONS_EXPECTED:
  - Edition scope
  - Vocabulary mapping
  - How to learn
  - Subtree map

UPDATE_TRIGGER:
  Update when edition changes, new factions are added, or scaffold sections
  are promoted from KB.
-->

# Warhammer 40,000 — 11th Edition

First worked example in Wargame_Concierge. **Edition in scope: 11th Edition (11e).**

Two forces in this track: **Necrons** (parent) and **Space Marines** (son).

**Personal use only — this project must never be sold.**

Importing commentary from user's digital backup of White Dwarf 527, purchased from Trinity Hobby on Aug 22, 2026.

**Trust ladder:** tier **1** = Core / Event Companion / Chapter Approved (mechanics win); tier **1.5** = owned WD527 commentary and Mission 38 (local scans `C:\Personal\40K\WD_527\`). See shipping track [`docs/handoffs/wd527_research/track_shipping_in.md`](../../docs/handoffs/wd527_research/track_shipping_in.md).

**Rules quoting (40K rules/setup only):** [`rules/`](rules/) and [`setup/`](setup/) may reproduce **verbatim** WarCom-**free** Core text (and matching local `C:\Personal\40K\rules\eng_*`) with filename + page + **rule ID**. **Codex wall:** [`armies/`](armies/) stays teaching paraphrase — never quote Codex / Faction Pack / paid army rules. **Hierarchy:** Core PDF is baseline; dated `eng_*` stamps supersede on the same topic; omission is not a patch. Citation spine: [`rules/Core_Rules_Quotes.md`](rules/Core_Rules_Quotes.md).

**Rules currency: 40K Aug 2026 package** — Universal Rules Updates **v1.1** (legal 26 Aug 2026; disembark move typing `18.06`/`18.07`, see [`rules/README.md`](rules/README.md)) · Faction Pack **v1.2** (Necrons + Space Marines) · Munitorum Field Manual **v1.3** — all `draft` (owner paste / staging pull, retrieved 2026-08-27). **No singular "Balance Dataslate" file** — this is Core/universal updates plus faction and points-manual pieces (owner lock, [`docs/handoffs/dataslate_0826/track_in.md`](../../docs/handoffs/dataslate_0826/track_in.md)). Per-army detail: [`armies/necrons/README.md`](armies/necrons/README.md), [`armies/space_marines/README.md`](armies/space_marines/README.md) (also carries the **Codex: Space Marines October** preview note). Teaching paraphrase — verify owned PDFs before tournament play.

---

## Vocabulary mapping

This subtree uses Games Workshop terms. Mapping from the [game-agnostic scaffold](../../docs/Game_System_Scaffold.md):

| Generic term | 40K 11e term |
|--------------|--------------|
| Force | Army |
| Force organisation | Detachment |
| Force-wide rule | Army rule |
| Sub-list rule package | Detachment rule (+ enhancements, stratagems) |
| Unit entry | Datasheet |
| Round structure | Battle round (movement, shooting, charge, fight phases) |
| Scoring | Primary objectives, victory points, battle tactics |
| Force size | Points (typically 500 → 1,000 for learning) |

---

## How to learn

1. **Sources first** — read [`reference/Source_Library.md`](../../reference/Source_Library.md) for local PDF paths and living web URLs. Cross-check every rules claim.
2. **Rules spine** — start with [`rules/Overview.md`](rules/Overview.md), then teaching paraphrase plus [`rules/Core_Rules_Quotes.md`](rules/Core_Rules_Quotes.md) for numbered Core IDs. Wound chart: [`rules/Wound_Roll_Reference.md`](rules/Wound_Roll_Reference.md).
3. **Setup** — `setup/` documents cover board size, deployment, and terrain (IDs cited; Event Companion inventoried, not dumped). Monthly mission: [`setup/WD527_Monthly_Mission.md`](setup/WD527_Monthly_Mission.md) (**Mission 38 — Converging Ambition**). System table laminate: [`setup/print/40k_system_quick_reference.html`](setup/print/40k_system_quick_reference.html) (Letter 2-pager; S4 owns HTML body).
4. **Pick a force** — start with [`armies/necrons/README.md`](armies/necrons/README.md) or [`armies/space_marines/README.md`](armies/space_marines/README.md).
5. **Match reality** — always check [`Owned_Models_Inventory.md`](armies/necrons/Owned_Models_Inventory.md) (Necrons) before building a list from what you actually own.

**Recommended first game size:** 250–500 points using game-ready models only.

---

## Subtree map

| Path | Status | Purpose |
|------|--------|---------|
| [`rules/README.md`](rules/README.md) | Active | Rules teaching spine + numbered quote appendix |
| [`rules/Overview.md`](rules/Overview.md) | Active | Beginner system overview (shape of a game → first table) |
| [`rules/Wound_Roll_Reference.md`](rules/Wound_Roll_Reference.md) | Active | S vs T wound matrix (Core 05.02) + print laminate |
| [`setup/README.md`](setup/README.md) | Active | Board, terrain, Force Dispositions, Mission 38 |
| [`setup/WD527_Monthly_Mission.md`](setup/WD527_Monthly_Mission.md) | Active | Mission 38 — Converging Ambition (WD527) |
| [`setup/print/40k_system_quick_reference.html`](setup/print/40k_system_quick_reference.html) | Planned (S4) | System Letter 2-pager (phases + attack sequence) |
| [`armies/necrons/`](armies/necrons/) | Partial | Parent's Necron force |
| [`armies/space_marines/`](armies/space_marines/) | Partial | Son's Space Marine force |
| [`armies/adepta_sororitas/`](armies/adepta_sororitas/) | **Ownership stub only** | Metal Sisters + Celestian Insidiants declared 2026-08-22; **unpainted**; no teaching package yet |
| [`armies/death_guard/`](armies/death_guard/) | **Cross-link stub only** | Not in 40K teaching scope — pointer for Plague Marines KT miniatures ([`kill_team_2024` track](../../docs/handoffs/kill_team_2024_scaffold/track_in.md)); no army package |

---

## Games Workshop notice

**UNOFFICIAL.** This document is completely unofficial and in no way endorsed by Games Workshop Limited. Personal / no-charge use only — never for sale. Warhammer, Warhammer 40,000 and associated marks are trademarks of Games Workshop Limited. Used without permission. No challenge to their status intended. Warhammer 40,000 is Copyright Games Workshop Limited. Teaching notes by Russell Catt (Wargame Concierge). Games Workshop retains IP in the settings and characters. No official logos.

## Change Log
- v0.6.0 (2026-08-27): Rules currency line — 40K Aug 2026 package (Universal Rules v1.1 · Faction Pack v1.2 · MFM v1.3), `draft`, pointer to army READMEs for detail; no singular dataslate file (track `dataslate_0826` slice S5).
- v0.5.4 (2026-08-25): S3 polish — Overview in How to learn + subtree; system QR marked Planned (S4); Mission 38 bold in setup step (provenance / trust ladder untouched).
- v0.5.3 (2026-08-25): WD527 shipping — Trinity Hobby provenance; trust ladder; Mission 38 / wound / system 2-pager rows; setup Active.
- v0.5.2 (2026-08-22): Adepta Sororitas ownership stub (metal + Celestian Insidiants); unpainted.
- v0.5.1 (2026-08-18): WarCom-free quote exception for `rules/` + `setup/`; Codex wall on `armies/`; Core_Rules_Quotes link (track `40k_warcom_quotes`).
- v0.5.0 (2026-08-18): Project-wide semver snapshot (x.y.z).
- v1.1 (2026-08-17): Noted Death Guard folder as KT cross-link stub only (slice S5, kill_team_2024_scaffold) — locked 40K forces remain Necrons + Space Marines.
- v1.0 (2026-08-16): Initial scaffold (slice S2). README, army folders, Necron import.

## Attribution
- Project: Wargame_Concierge
- Maintainer: Russell Catt

## Rising Tide Notes
- This document follows Rising Tide documentation standards.
- Must remain understandable, reproducible, and reusable.