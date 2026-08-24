<!--
FILE: games/kill_team_2024/rules/README.md
VERSION: v0.5.0 (2026-08-18)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, slice S1; patch sync slice P)

DOCUMENT_TYPE: Index / Section README
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: Kill Team - 2024 / 3rd Edition (KT24)
REFERENCE_STATUS: Active - teaching spine; targeting quotes owner-verified 2026-08-18 against Full-Scan + Jun 17 update log + Jul 25 lite

SOURCES:
  - raw/pointers/kill_team_2024_core.md
  - games/kill_team_2024/rules/Patch_Manifest.md
  - https://wahapedia.ru/kill-team3/the-rules/core-rules/ (retrieved 2026-08-17; living cross-check only)
  - docs/Game_System_Scaffold.md (Section B)

PURPOSE:
  Index for the Kill Team teaching spine. Says what each document covers and
  in what order a beginner should read them.

UPDATE_TRIGGER:
  Update when a rules document is added, retired, or substantially revised.
-->

# Rules - Kill Team 2024 / 3rd Edition

**Status:** Populated in **S1**, with targeting quotes and patch sync in **slice P (2026-08-18)**. Full-Scan Core Book, Jun 17 update log, and Jul 25 lite have been opened. **Hierarchy:** Full-Scan is baseline; dated `eng_*` patches supersede; Jul 25 lite is a simplified intro — **omission is not a patch.** Table disputes: [`Target_Eligibility.md`](Target_Eligibility.md). Ledger: [`Patch_Manifest.md`](Patch_Manifest.md).

Paraphrase pages (Overview, Turn Structure, Key Concepts, Glossary) remain teaching wording. They are **not** Full-Scan-only SoT.

---

## Read in this order

| # | File | What it covers |
|---|------|----------------|
| 1 | [`Overview.md`](Overview.md) | What a game of Kill Team is: turning points, the two-phase structure, how you win, what a kill team is made of, a coming-from-40K comparison table |
| 2 | [`Turn_Structure.md`](Turn_Structure.md) | A checklist for one turning point - Strategy phase (Initiative, Ready, Gambit) then Firefight phase (the activation loop and Counteract) |
| 3 | [`Key_Concepts.md`](Key_Concepts.md) | The mechanics everything else sits on: APL and the ±1 activation cap, Conceal vs Engage, 1" control range, cover/obscured, the Shoot and Fight sequences, Injured, and mission scoring at a high level |
| 4 | [`Keyword_Glossary.md`](Keyword_Glossary.md) | Every term in one place, grouped by phase/activation, movement, shooting/fighting, damage state, mission/scoring, and team/equipment - plus a dedicated table flagging terms that collide with a different 40K meaning |
| — | [`Target_Eligibility.md`](Target_Eligibility.md) | **Verbatim quote appendix** — every core rule that gates valid targets for Shoot (owned local PDFs; personal use) |
| — | [`Target_Eligibility_Cheat_Sheet.html`](Target_Eligibility_Cheat_Sheet.html) | **One-page printed valid-target tree** — UML 2.5 activity shapes ([`Flowcharting.md`](../../../docs/operations/Flowcharting.md)); every node traces to `Target_Eligibility.md`. Notation is not a rules source |
| — | [`Patch_Manifest.md`](Patch_Manifest.md) | **Errata ledger** — Full-Scan + Jun 17 update log + Jul 25 lite hierarchy |

Setup and kill zones live one level across in [`../setup/`](../setup/) (populated in S2).

**Open (parked):** US Letter landscape print for the cheat sheet, KT freshness dates from `eng_DD-MM_` PDFs, and complete operative cards — [`kt24_doc_followups/track_in.md`](../../../docs/handoffs/kt24_doc_followups/track_in.md).

---

## Confidence

Glossary rows for valid target, cover save, Heavy, Severe, and connected are tagged `patched 2026-08-18`. Other glossary entries remain `draft` until you confirm them in your book. Targeting quotes in [`Target_Eligibility.md`](Target_Eligibility.md) were owner-verified **2026-08-18**.

**Cross-checked against the KB.** The Librarian's L1 pass landed [`KB/glossary.md`](../../../KB/glossary.md) (Kill Team 2024 section) and six concept pages from Wahapedia. Slice P did **not** dump core rules into KB — paraphrase + pointer only. See the 2026-08-18 log entry.

Two things intentionally kept high-level rather than fully specified, per the S1 brief:

- **Ops and scoring.** `Key_Concepts.md` explains the shape of Crit Op / Kill Op / Tac Op scoring under Approved Ops 2025, but does not reproduce Approved Ops card text or per-mission Tac Op wording.
- **APL modifiers.** The ±1 net cap is stated as a rule; the specific rare abilities that raise or lower APL belong to team-specific content (S3-S6), not this shared spine.

---

## Sources

Every claim in this section traces to `raw/pointers/kill_team_2024_core.md`, [`Patch_Manifest.md`](Patch_Manifest.md), and the living Wahapedia Kill Team 3 pages listed in each document's header (retrieved **2026-08-17** where still used as a cross-check). See [`reference/Source_Library.md`](../../../reference/Source_Library.md) for the full local catalogue.

---

## Games Workshop notice

**UNOFFICIAL.** This document is completely unofficial and in no way endorsed by Games Workshop Limited. Personal / no-charge use only — never for sale. Warhammer, Kill Team and associated marks are trademarks of Games Workshop Limited. Used without permission. No challenge to their status intended. Kill Team is Copyright Games Workshop Limited 2024. Teaching notes by Russell Catt (Wargame Concierge). Games Workshop retains IP in the settings and characters. No official logos.

## Change Log
- v0.5.0 (2026-08-18): Cheat sheet restyled to UML activity shapes (track `flowcharting_uml`); link Flowcharting.md. Project-wide semver snapshot (x.y.z).
- v1.1 (2026-08-18): Slice P — Core PDFs opened; hierarchy Full-Scan + update log over lite; Patch_Manifest indexed; targeting owner-verified.
- v1.0 (2026-08-17): Replaced the S0 stub with a real index. Four rules documents authored (slice S1). Confidence section updated to cite the six KB concept pages the Librarian (L1) landed in parallel, from the same source.

## Attribution
- Project: Wargame_Concierge
- Maintainer: Russell Catt
- **Kill Team is Copyright Games Workshop Limited 2024**

## Rising Tide Notes
- This document follows Rising Tide documentation standards.
- **Verify before you play.** Targeting quotes owner-verified **2026-08-18**. Paraphrase pages still need the physical book for anything not in the quote appendix.
- The [`Target_Eligibility_Cheat_Sheet.html`](Target_Eligibility_Cheat_Sheet.html) footer must include: **Kill Team is Copyright Games Workshop Limited 2024**
