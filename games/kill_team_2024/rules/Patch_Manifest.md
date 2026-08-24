<!--
FILE: games/kill_team_2024/rules/Patch_Manifest.md
VERSION: v0.5.0 (2026-08-18)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, slice P)

DOCUMENT_TYPE: Patch Ledger / Source Hierarchy
GAME_SYSTEM: Kill Team — 2024 / 3e (KT24)
REFERENCE_STATUS: Active — built from owned Jun 17 update log + Jul 25 lite + Full-Scan baseline; owner spot-check 2026-08-18

SOURCES:
  - C:\Personal\Kill Team\kill_team_2024\779937548-Core-Rules-KILL-TEAM-3E-Full-Scan.pdf
  - C:\Personal\Kill Team\kill_team_2024\eng_17-06_kill_team_key_downloads_core_rules_update_log-9dzdz0ewle-wutcyhpgzf.pdf
  - C:\Personal\Kill Team\kill_team_2024\eng_jul25_kt_lite_rules-jmjv4hdamy-qlsqxdf83p.pdf
  - C:\Personal\Kill Team\kill_team_2024\eng_17-06_kill_team_key_downloads_universal_equipment-prsd0j8pih-ikfmigl0za.pdf
  - raw/pointers/kill_team_2024_core.md

PURPOSE:
  Ledger of core-rules errata and how shipping docs apply them. Not a quote dump.

UPDATE_TRIGGER:
  Update when a new dated eng_* core patch, lite reprint, or Full-Scan revision lands.
-->

# Patch manifest — Kill Team 2024 core rules

**Personal use only. Never for sale.** Read PDFs in place; never copy binaries into git.

## Hierarchy

Full-Scan = baseline. Dated `eng_*` **patches** (update log, team PDFs, universal equipment) supersede on the same topic. **Jul 25 lite is simplified intro rules** (lite p.1), not a full supersession of Core+log. Use lite to confirm short wording; never drop a Core or update-log sentence because lite omitted it.

**Team PDFs:** Under `Teams\`, filename date stamps apply the same way — a later `eng_*` stamp for the **same team** wins. Team-specific errata is a separate pass unless the update log names a team rule.

**Sniper PDF** (`kt_sniper_rules_eng_20-…`, Aug 2020 stamp): out of scope for core targeting unless you field sniper operatives with special target rules.

Quote appendix for table disputes: [`Target_Eligibility.md`](Target_Eligibility.md).

---

## Seed rows (eligibility + shooter gates)

| Rule topic | Update log ref | Lite ref | Supersedes Full-Scan? | Docs to touch |
|------------|----------------|----------|----------------------|---------------|
| Cover and obscured from the **same** terrain feature — defender picks one | p.2 SELECT VALID TARGET | Not restated (omission ≠ patch) | **Adds** to p.42 / p.53 | Target_Eligibility, cheat sheet, Key_Concepts |
| Torrent first sentence — primary + other valid targets within x, not in friendly 1" control range | p.2 TORRENT | p.3 (matches) | Matches current Full-Scan p.111 | Target_Eligibility (already harvested) |
| Blast secondaries are **not selected** — “cannot be selected” does not stop them | p.4 FAQ | — | Commentary on p.111 Blast | Target_Eligibility |
| Blast copies primary cover/obscured | p.4 FAQ | p.3 Blast already says this | Clarifies p.111 | Target_Eligibility |
| Blast + Vantage improved cover save copies to secondaries | p.5 FAQ | — | Commentary on p.60 / Blast | Target_Eligibility |
| Vantage + Seek Light — may elect Seek only | p.5 FAQ | — | Commentary on p.60 / Seek | Target_Eligibility, cheat sheet |
| “Heavy connected to Vantage” = any part of the **same terrain feature** | p.5 FAQ | — | Clarifies p.60 | Target_Eligibility, Keyword_Glossary, cheat sheet |
| Cover save / Accurate auto-retain: no re-roll, no numerical result; retain once (Severe may **change**) | p.4–5 FAQ | — | Sequence | Target_Eligibility, Key_Concepts |
| **Heavy** — activation **or counteraction**; Heavy (x only); **does not prevent Guard** | p.2 HEAVY (first sentence) | p.3 (full wording + Guard) | **Yes** — unpatched p.111 was activation-only | Target_Eligibility, Keyword_Glossary |
| **Severe** — Devastating and Piercing Crits still apply; Punishing and Rending do not | p.2 SEVERE | p.3 | **Yes** | Keyword_Glossary, Key_Concepts — not Target_Eligibility weapon dump |
| Smoke — wholly within, obscured to operatives >2" (and vice versa) | — | — | Universal equipment p.4 | Target_Eligibility |

---

## Killzone / Close Quarters (not the core valid-target tree)

| Rule topic | Update log ref | Docs to touch |
|------------|----------------|---------------|
| Gallowdark & Tomb World Close Quarters — Guard: add performs any action, **moves or is set up**; On Guard: cannot counteract that TP | p.3 | [`../setup/killzones/tomb_world.md`](../setup/killzones/tomb_world.md) |
| Volkus Door Fight — Select Enemy Operative = enemy on killzone floor, within 2" of, other side of a door the active operative is touching | p.3 | [`../setup/killzones/volkus.md`](../setup/killzones/volkus.md) |
| Volkus Large ruin — upper level Ceiling and Vantage; door Accessible and Heavy; ignore door for 1" control range visibility | p.3 | volkus.md |
| Volkus Stronghold — upper level(s) Ceiling and Vantage; extra parts (barrels, ramparts, gap, Stronghold B roof) | p.3 | volkus.md |
| Volkus Condensed Stronghold — Blast / Torrent / x" Devastating also **Lethal 5+** if target wholly within stronghold and on killzone floor or fire step (per-target for secondaries) | p.2 | volkus.md, volkus_QR.md |
| Volkus fire step — do **not** ignore the rest of the stronghold for obscured | p.5 FAQ | volkus.md |
| Ignoring a door for 1" control range visibility does **not** let you Shoot a target that is not visible | p.6 FAQ | volkus.md |

---

## Other update-log items (paraphrase elsewhere)

Damage (one free action before remove), distances (carried marker), datacard stat timing, precedence #5 active player, Counteract 2" / once per TP / excl. Guard, Jumping from Vantage, Ceiling terrain, Bheta-Decima equipment — see [`Key_Concepts.md`](Key_Concepts.md), [`Turn_Structure.md`](Turn_Structure.md), [`../setup/Terrain_Basics.md`](../setup/Terrain_Basics.md). Remaining p.4–6 commentaries (Guard AP, Hot, ploys, etc.) stay out of the eligibility appendix.

---

## Owner verification

| Date | What |
|------|------|
| 2026-08-18 | Owner Full-Scan Tier A (pp. 42–61, 111) + update log p.2–6 + Jul 25 lite pp.1–3. Quote restores in Target_Eligibility.md; cheat sheet synced. |

---

## Related pages

- [`Target_Eligibility.md`](Target_Eligibility.md)
- [`Target_Eligibility_Cheat_Sheet.html`](Target_Eligibility_Cheat_Sheet.html)
- [`README.md`](README.md)
- [`../../../raw/pointers/kill_team_2024_core.md`](../../../raw/pointers/kill_team_2024_core.md)

---

## Games Workshop notice

**UNOFFICIAL.** This document is completely unofficial and in no way endorsed by Games Workshop Limited. Personal / no-charge use only — never for sale. Warhammer, Kill Team and associated marks are trademarks of Games Workshop Limited. Used without permission. No challenge to their status intended. Kill Team is Copyright Games Workshop Limited 2024. Teaching notes by Russell Catt (Wargame Concierge). Games Workshop retains IP in the settings and characters. No official logos.

## Change Log

- v0.5.0 (2026-08-18): Project-wide semver snapshot (x.y.z).
- v1.0 (2026-08-18): Initial ledger (slice P). Hierarchy: Full-Scan baseline; dated `eng_*` patches supersede; Jul 25 lite is intro subset.

## Attribution

- Project: Wargame_Concierge · Maintainer: Russell Catt
- **Personal use only. Never for sale.**
- **Kill Team is Copyright Games Workshop Limited 2024**

## Rising Tide Notes

- This document follows Rising Tide documentation standards.
- Keep the receipts. Make AI show their work.
