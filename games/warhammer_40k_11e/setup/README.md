<!--
FILE: games/warhammer_40k_11e/setup/README.md
VERSION: v0.5.5 (2026-08-27)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, track dataslate_0826 S5)

DOCUMENT_TYPE: Index / Section README
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: Warhammer 40,000 - 11th Edition
REFERENCE_STATUS: Active - content authored in S3; WD527 Commentary S2; system QR print shipped S4

SOURCES:
  - C:\Personal\40K\rules\eng_22-07_warhammer_40,000_event_companion-alyapl19us-b2drgwkji4.pdf (v1.1, read 2026-08-16)
  - C:\Personal\40K\rules\eng_01-06_warhammer40k_new40k_core_rules.pdf (Section 13, read 2026-08-16)
  - C:\Personal\40K\Terrain\A4\ (path pointers only)
  - C:\Personal\40K\WD_527\ (owned digital backup; Trinity Hobby 2026-08-22)
  - reference/Source_Library.md

PURPOSE:
  Index for board and terrain setup. Says what each document covers and where
  the printable terrain footprints live.

UPDATE_TRIGGER:
  Update when a setup document is added or revised, or when new terrain packs
  are acquired.
-->

# Setup - Warhammer 40,000 11th Edition

**Status:** Populated in **S3**, from the owned Event Companion v1.1 and Core Rules PDF, both read **2026-08-16**; rule-ID cites added **2026-08-18** (`40k_warcom_quotes`); WD527 locked Commentary on Board / Terrain / Force Dispositions **2026-08-25** (`wd527_shipping` S2).

Everything that happens before battle round one, plus the terrain rules that shape the whole game.

This folder may quote WarCom-free Core / local `eng_*` with filename + page + rule ID. Teaching stays paraphrase. Event Companion mission layouts and base-size lists are **inventoried, not dumped**. **Warhammer 40,000 is Copyright Games Workshop Limited.** Personal use only; never for sale.

**WD527:** Locked **Commentary** blocks (teaching paraphrase + Trinity Hobby cite) live on [`Board_Setup.md`](Board_Setup.md), [`Terrain_Basics.md`](Terrain_Basics.md), and [`Chapter_Approved_Force_Dispositions.md`](Chapter_Approved_Force_Dispositions.md). Monthly mission: [`WD527_Monthly_Mission.md`](WD527_Monthly_Mission.md) (**Mission 38 — Converging Ambition**). Tier **1.5** — Core / Event Companion win on mechanics. See shipping track [`docs/handoffs/wd527_research/track_shipping_in.md`](../../../docs/handoffs/wd527_research/track_shipping_in.md).

**Rules currency:** no Aug 2026 package piece (Universal Rules v1.1 / Faction Pack v1.2 / MFM v1.3) changes board size, deployment, or terrain content on this page — grepped, no hits. Full package stamp: [`../README.md`](../README.md).

---

## Documents

| File | What it covers |
|------|----------------|
| [`Board_Setup.md`](Board_Setup.md) | Table size (44" x 60" for events), the fourteen-step pre-game sequence, deployment zones and territory, objective types, strategic reserves, a printable pre-game checklist, and shortcuts for a first game · WD527 Commentary (Disposition / Tactical; terrain objectives) |
| [`Chapter_Approved_Force_Dispositions.md`](Chapter_Approved_Force_Dispositions.md) | **2-pager:** Force Dispositions, Primary matching, layouts A/B/C, Twists, starter-event checklist · WD527 Commentary (pairing + Tactical) |
| [`WD527_Monthly_Mission.md`](WD527_Monthly_Mission.md) | **Mission 38 — Converging Ambition** (WD527 Bunker); owned-materials build notes |
| [`Terrain_Basics.md`](Terrain_Basics.md) | Terrain areas vs terrain features, the three categories (Exposed / Light / Dense), the four visibility rules (Benefit of Cover, Hidden, Obscuring, Solid), terrain and movement, and how much terrain a table actually needs · WD527 Commentary (footprints; Benefit of Cover) |
| Learn-to-play print bag | Combined Saturday checklist (KT + 40K): [`../../kill_team_2024/setup/Learn_to_Play_Print_Bag.md`](../../kill_team_2024/setup/Learn_to_Play_Print_Bag.md) — PDFs in `C:\Personal\print_aids\learn_to_play_event\` |

### Print aids (Letter → `C:\Personal\print_aids\40k_11e\`)

| HTML | PDF | Notes |
|------|-----|-------|
| [`print/40k_system_quick_reference.html`](print/40k_system_quick_reference.html) | `40k_system_quick_reference.pdf` | **Shipped S4** — system Letter 2-pager (WD topic map; Core IDs). Outline: [`../rules/Quick_Reference_Card.md`](../rules/Quick_Reference_Card.md) |
| [`print/40k_wound_roll_reference.html`](print/40k_wound_roll_reference.html) | `40k_wound_roll_reference.pdf` | Full S×T laminate — keep separate from system QR |
| [`print/40k_wd527_mission.html`](print/40k_wd527_mission.html) | `40k_wd527_mission.pdf` | Mission 38 — Converging Ambition |
| [`print/40k_chapter_approved_force_dispositions.html`](print/40k_chapter_approved_force_dispositions.html) | `40k_chapter_approved_force_dispositions.pdf` | Force Dispositions 2-pager |

Export: `python games/warhammer_40k_11e/setup/print/_html_to_pdf.py`

---

## Terrain footprint packs - local library

Printable terrain-area footprints are on the owner's machine and **stay outside this repository**. Path pointers only; no binaries are committed.

- **A4 packs:** `C:\Personal\40K\Terrain\A4\` - Combat Patrol Battlezone, Imperial World, Death World Jungle, Death World Snow, Maelstrom World, and a grey city-tone variant
- **Full-size footprint documents:** `C:\Personal\40K\rules\` - the terrain area footprints booklet plus per-battlezone PDFs

Full catalogue: [`reference/Source_Library.md`](../../../reference/Source_Library.md).

---

## The two things beginners get wrong

1. **Terrain areas come before terrain features.** Objectives, cover, Hidden, and Obscuring all key off the *area*, not the scenery model.
2. **Cover does not improve your save in 11th Edition.** It worsens the attacker's Ballistic Skill by 1. Both are explained in [`Terrain_Basics.md`](Terrain_Basics.md).

---

## Related

- [`../rules/README.md`](../rules/README.md) - the rules teaching spine
- [`../rules/Key_Concepts.md`](../rules/Key_Concepts.md) - Objective Control, which decides what setup is for
- [`../README.md`](../README.md) - the 40K subtree entry point

---

## Games Workshop notice

**UNOFFICIAL.** This document is completely unofficial and in no way endorsed by Games Workshop Limited. Personal / no-charge use only — never for sale. Warhammer, Warhammer 40,000 and associated marks are trademarks of Games Workshop Limited. Used without permission. No challenge to their status intended. Warhammer 40,000 is Copyright Games Workshop Limited. Teaching notes by Russell Catt (Wargame Concierge). Games Workshop retains IP in the settings and characters. No official logos.

## Change Log
- v0.5.5 (2026-08-27): Rules currency line — confirmed no Aug 2026 package piece touches this folder's content; pointer to `../README.md` for the package stamp (track `dataslate_0826` slice S5).
- v0.5.4 (2026-08-25): Print table — system QR shipped (S4) with PDF path + outline link; wound laminate kept separate.
- v0.5.3 (2026-08-25): WD527 Commentary + Mission 38 pointers; print list includes system QR (wd527_shipping S2).
- v0.5.2 (2026-08-23): Index Chapter_Approved_Force_Dispositions 2-pager.
- v0.5.1 (2026-08-18): Quote permission + Core ID cites (track `40k_warcom_quotes`). Event Companion still inventoried, not dumped.
- v0.5.0 (2026-08-18): Project-wide semver snapshot (x.y.z).
- v2.0 (2026-08-16): Replaced the S2 stub with a real index. Board_Setup and Terrain_Basics authored (slice S3).
- v1.0 (2026-08-16): Stub created (slice S2).

## Attribution
- Project: Wargame_Concierge
- Maintainer: Russell Catt

## Rising Tide Notes
- This document follows Rising Tide documentation standards.
- **Verify before you play.** Cross-check anything in this section against the current Munitorum Field Manual and your faction pack - Games Workshop patches rules and points between publications. Content reflects sources read on **2026-08-16**.
