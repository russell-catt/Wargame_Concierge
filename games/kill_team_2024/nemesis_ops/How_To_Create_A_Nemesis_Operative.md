<!--
FILE: games/kill_team_2024/nemesis_ops/How_To_Create_A_Nemesis_Operative.md
VERSION: v0.6.0 (2026-08-27)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, slice S2 — nemesis_ops_ocr_spotcheck; dataslate_0826 S3)
DOCUMENT_TYPE: Teaching Guide
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: Kill Team — 2024 / 3e (KT24)
REFERENCE_STATUS: Active — process steps vision-verified 2026-08-17; no dossier datasheet numbers; Towering Size note aligned to Aug '26 mission packs update log (2026-08-27)

SOURCES:
  - raw/pointers/kill_team_2024_nemesis_operatives.md
  - C:\Personal\Kill Team\kill_team_2024\1063073009-Kill-Team-Nemesis-Operatives-Dossier.pdf (vision spot-check)
  - C:\Personal\Kill Team\kill_team_2024\1063073009-Kill-Team-Nemesis-Operatives-Dossier.ocr.txt (OCR outside git; process paraphrase only)
  - docs/handoffs/nemesis_ops_ocr_spotcheck/OCR_Spotcheck_Matrix.md
  - games/kill_team_2024/nemesis_ops/WarCom_Free_Statlines.md
  - raw/pointers/community_kt24_npo_cheat_sheet.md
  - `eng_mission_packs_update_log-51t6hsixc0-buxngu8xav.pdf` (staging, read 2026-08-27) — dataslate_0826 S3

PURPOSE:
  Beginner walkthrough for creating a Nemesis Operative with the Custom Builder.

UPDATE_TRIGGER:
  Re-check after FAQ/errata; dense weapon/trait tables remain book-only.
-->

# How to create a Nemesis Operative

**Confidence: verified** for Custom Builder **process steps** (allegiance → size → NPO behaviour → weapons → traits) after vision spot-check against the owned PDF (track `nemesis_ops_ocr_spotcheck`, 2026-08-17). **No datasheet numbers from the dossier appear on this page.** Full profiles live on blank datacards / the official app / WarCom downloads you own — not in this repo.

**Rules currency: Kill Team quarterly balance — August 2026** (Core / update logs + team online rules) · teaching paraphrase · verify owned PDFs · confidence `draft`.

---

## 1. What you need

| You need | Notes |
|----------|-------|
| A large model you already own (or will proxy) | Walker, battlesuit, monster, dreadnought-scale, etc. |
| Owned dossier (physical or OCR sidecar beside the PDF) | Pointer: [`raw/pointers/kill_team_2024_nemesis_operatives.md`](../../../raw/pointers/kill_team_2024_nemesis_operatives.md) |
| Two blank Nemesis NPO datacards | Card pack, Kill Team app, or WarCom blank downloads (per dossier) |
| Optional: WarCom free articles | Catalog: [`WarCom_Free_Statlines.md`](WarCom_Free_Statlines.md) — **no free full numeric profiles found** as of 2026-08-17 |
| Optional table aid | Community NPO cheat sheet — **draft / may be out of date**; pointer only |

---

## 2. Choose allegiance, size, and role axes

Complete the builder steps on the blank cards (dossier Custom Builder section):

1. **Allegiance** — Pick one allegiance keyword for the operative (examples named in the book include major 40K faction families such as Imperium, Chaos, Aeldari, Necron, Ork, T’au Empire, Tyranid, Leagues of Votann). That keyword gates who can share a kill team with it, and it unlocks an **allegiance trait** later.
2. **Size** — Choose Small / Medium / Large. Larger size means a tougher, more powerful Nemesis and (in Joint Ops / Nemesis Ops packs) fewer other operatives alongside it. Prefer a size that matches the model’s base and the killzone — very large bases can be awkward on tight maps. **Keep Towering Size almost always** — August 2026 rules commentary treats removing it as the exception (named exceptions: Ambull, Archivist), not a default option; even a Small custom Nemesis should usually keep the no-Conceal / always-valid-target behaviour Towering Size grants. Detail: [`Custom_Builder.md`](Custom_Builder.md#step-2-addendum--keep-towering-size-august-2026-commentary).
3. **Behaviour (NPO only)** — If the Nemesis is a **non-player** operative, pick a behaviour that drives its orders and action priorities (the book’s families include melee-forward, shooting-forward, and mixed patterns such as Brawler / Marksman / Guardian / Battler). If it is a **player** Nemesis, you choose its orders like a normal operative (with the book’s action restrictions for Nemesis).

Details and trait lists: [`Custom_Builder.md`](Custom_Builder.md).

---

## 3. Pick weapons and special rules (categories, not card dumps)

4. **Weapons** — Select weapons up to the count allowed by size. Weapons with a “Selection x” style cost consume multiple slots. Unused weapon selections convert into **extra nemesis trait** picks. Choose profiles that look like what the model is actually carrying — do not invent loadouts the miniature does not represent.
5. **Traits** — Apply the allegiance trait, then pick nemesis traits that match the story (tough, aggressive, accurate, etc.). You cannot stack the same trait twice. Rules text is written as if the Nemesis were friendly; if it is an enemy NPO, apply the book’s “flip perspective” guidance.

**Do not copy weapon tables or trait point values from OCR into this repo.** Fill numbers on your physical/app datacard from the owned book.

---

## 4. Plug the finished Nemesis into play

| Mode | How the Nemesis shows up |
|------|---------------------------|
| **Joint Ops (co-op / solo PvE)** | Boss or pack threat controlled by NPO behaviour + Threat Principle / activation tools in the mission pack |
| **Adversary Ops / Nemesis Ops** | Head-to-head where one or both sides use Nemesis support — dossier uses **Nemesis Ops** alongside Joint Ops; WarCom often says **Adversary Ops** for Archivist’s PvP mission — see [`Modes_And_Cards.md`](Modes_And_Cards.md) |
| **Named packs** | Ambull and Archivist packs ship ready-made Nemesis + missions ([`Mission_Packs.md`](Mission_Packs.md)) |
| **Custom Builder examples** | Sentinel / Crisis / Screamer-Killer / Redemptor illustrate the toolkit ([`Worked_Examples.md`](Worked_Examples.md)) |

Core Nemesis feel (qualitative from dossier teaching pages + WarCom): high durability, can activate more than once per turning point, extreme threat if ignored.

---

## 5. Worked mini-example (qualitative)

**Goal:** Build a narrative Imperial walker-style Nemesis for a Joint Ops boss fight.

1. Allegiance: Imperium (so it can ally with Imperial kill teams when friendly, or oppose them when hostile).
2. Size: Medium or Large — match the model’s footprint.
3. Behaviour (as NPO): Marksman- or Guardian-leaning if the model is a gun platform; Brawler if it is a melee monster.
4. Weapons: one primary gun that matches the kit + a close-combat option if present; leave unused slots for extra traits if you want more special rules than guns.
5. Traits: allegiance trait + narrative picks (e.g. tough / focused fire themes — exact names on the cards).

**Numbers:** Prefer a unit that has a **WarCom-free** numeric profile. As of 2026-08-17, **none** of the Custom Builder showcase units have a free WarCom full profile — see [`WarCom_Free_Statlines.md`](WarCom_Free_Statlines.md). Fill stats from the owned dossier / blank card, not from this guide.

---

## 6. Optional community table aid

For generic NPO **behaviour priority** habits (not Nemesis builder math), you may glance at:

`C:\Personal\Kill Team\Community Content\The Kill Team 24 NPO Cheat Sheet Vers 1.1 ALTERNATIVE TEST.pdf`  
Pointer: [`raw/pointers/community_kt24_npo_cheat_sheet.md`](../../../raw/pointers/community_kt24_npo_cheat_sheet.md)

**draft / may be out of date.** Verify every claim against Core Rules + dossier before play. Do not treat community numbers as official.

---

## VERIFY (before play)

| Check | Status |
|-------|--------|
| Process steps vision-checked vs owned PDF 2026-08-17 | **verified** (spot-check matrix) |
| Datasheet numbers taken from owned book/app — **not** this repo | required |
| WarCom free numeric profiles | none found 2026-08-17 |
| Community sheet | optional aid only; stale-risk |
| Ambull / Archivist mission titles | vision-confirmed — see [`Mission_Packs.md`](Mission_Packs.md) |
| Towering Size commentary (Aug '26 mission packs update log) | read from staging 2026-08-27; cross-check owned dossier |

## Related pages

- [`Custom_Builder.md`](Custom_Builder.md)
- [`Mission_Packs.md`](Mission_Packs.md)
- [`Modes_And_Cards.md`](Modes_And_Cards.md)
- [`../joint_ops/README.md`](../joint_ops/README.md)
- [`../../../docs/handoffs/nemesis_ops_ocr_spotcheck/OCR_Spotcheck_Matrix.md`](../../../docs/handoffs/nemesis_ops_ocr_spotcheck/OCR_Spotcheck_Matrix.md)

## Games Workshop notice

**UNOFFICIAL.** This document is completely unofficial and in no way endorsed by Games Workshop Limited. Personal / no-charge use only — never for sale. Warhammer, Kill Team and associated marks are trademarks of Games Workshop Limited. Used without permission. No challenge to their status intended. Kill Team is Copyright Games Workshop Limited 2024. Teaching notes by Russell Catt (Wargame Concierge). Games Workshop retains IP in the settings and characters. No official logos.

## Change Log
- v0.6.0 (2026-08-27): dataslate_0826 S3 — Towering Size commentary note at step 2 (Aug '26 mission packs update log); currency stamp.
- v0.5.0 (2026-08-18): Project-wide semver snapshot (x.y.z).
- v1.1 (2026-08-17): OCR spot-check — process steps → `verified`; VERIFY table updated.
- v1.0 (2026-08-17): S2 required How-To (process paraphrase; no dossier numbers).
- v0.1 (2026-08-17): S0 stub.

## Attribution
- Project: Wargame_Concierge
- Maintainer: Russell Catt
- Warhammer 40,000: Kill Team is a trademark of Games Workshop Limited. Personal teaching paraphrase only.

## Rising Tide Notes
- This document follows Rising Tide documentation standards.
