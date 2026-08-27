---
title: 40K Aug 2026 balance package
type: source
system: warhammer_40k_11e
created: 2026-08-27
updated: 2026-08-27
version: 0.1.0
sources:
  - docs/handoffs/dataslate_0826/research/40k_universal_rules_updates_v1_1.md (retrieved 2026-08-27)
  - docs/handoffs/dataslate_0826/research/staging_40k_faction_packs_v1_2.md (retrieved 2026-08-27)
  - docs/handoffs/dataslate_0826/research/necron_mfm_v1_3.md (owner paste, retrieved 2026-08-27)
  - docs/handoffs/dataslate_0826/research/sm_mfm_v1_3.md (owner paste, retrieved 2026-08-27)
  - docs/handoffs/dataslate_0826/research/warcom_40k_balance_commentary_aug.md (owner paste, retrieved 2026-08-27)
  - raw/pointers/rules_core.md, raw/pointers/faction_pack_necrons.md, raw/pointers/faction_pack_space_marines.md, raw/pointers/points_manuals.md
confidence: draft
tags: [source, warhammer_40k_11e, balance, points, faction_pack, universal_rules, mfm, august_2026]
---

# 40K Aug 2026 balance package

**There is no single titled "Balance Dataslate" file for 40K.** The August 2026 balance pass is a **package of separately-versioned pieces**, all legal from **26 August 2026** unless noted: **Universal Rules Updates v1.1** (core), **Faction Pack v1.2** (Necrons + Space Marines, the only two onboarded factions), and **Munitorum Field Manual v1.3** (Necrons + Space Marines points), plus a WarCom "What's New?" commentary article for design intent. Owner lock 2026-08-27 — do not invent a fictional single-file dataslate name anywhere downstream.

**Confidence:** `draft` throughout. Universal Rules v1.1 and Faction Pack v1.2 were read from a staged PDF (`raw/_dataslate_0826_staging/`, temporary, cleanup pending); MFM v1.3 for both factions is an **owner paste**, not yet cross-checked against a saved PDF under `C:\Personal\40K\rules\`. Upgrade to `verified` only after that PDF cross-check happens.

---

## Package pieces

| Piece | Version / legal date | What it covers |
|-------|----------------------|-----------------|
| Universal Rules Updates | **v1.1**, legal **26 Aug 2026** | Core / Codex-wide fixes; supersedes July v1.0 on the same topics |
| Faction Pack — Necrons | **v1.2**, legal 26 Aug 2026 | Rules/FAQ layer (not points): stratagem wording, Support attach cleanup, Legends FRAME removal |
| Faction Pack — Space Marines | **v1.2**, legal 26 Aug 2026 | Rules/FAQ layer: Gladius FAQ, Terminator teleport homer, Outrider rework, Legends FRAME removal |
| Munitorum Field Manual — Necrons | **v1.3** (owner paste) | Points: **Necron Warriors 10-model band 80 → 85** (▲+5); several other unowned units ▲ |
| Munitorum Field Manual — Space Marines | **v1.3** (owner paste) | Points: Centurion Devastator Squad, Land Raider Redeemer, Librarian in Terminator Armour ▲ (all unowned); Blood Ravens core costs **unchanged** |
| WarCom "What's New?" commentary | Aug package intent | Points direction (Daemons/EC/Custodes ▲, AM/DG/Aeldari targeted ▼; Orks excluded, new Codex on pre-order); Force Disposition map-layout tweaks; last **monthly** pass before returning to **quarterly** in September |

Every piece keeps its own version number and legal date; nothing here should be cited as "the dataslate."

---

## Teaching paraphrase — what changed for this collection

### Universal Rules Updates v1.1 (net-new item)

Items 1–4 (unnamed 0CP stratagems, multi-use stratagem naming, 12"→18" ranged-targeting restrictions, once-per-battle on respawn stratagems) repeat July's v1.0 intent unchanged. The **new** item in v1.1 is **disembark move typing**:

- A disembark that follows a TRANSPORT's **Normal move** this turn, where the disembarking unit then charges, is now a named **assault disembark move**.
- A disembark from a TRANSPORT that **Advanced** this turn is now a named **shock disembark move**.

These are new Core rule IDs, not new permissions by themselves — see [[assault_disembark_move]] / [[shock_disembark_move]] stubs in [[glossary]].

### Faction Pack v1.2 (rules/FAQ, no points)

Necrons: Cursed Legion's Unnatural Aggression stratagem no longer grants a Charge bonus even on success; a Legends FRAME callout dropped from Night Shroud. Space Marines: Armoured Speartip's Rapid Embarkation now allows embarking the same turn a unit disembarked; several Legends flyers/speeders lose a FRAME callout. Neither faction pack changes a single point value — that is MFM's job.

### Munitorum Field Manual v1.3 — the only points-owning piece

**Necrons (owned collection impact):** Necron Warriors 10-model band **80 → 85** (▲+5, 20-model band unchanged at 190); Plasmancer **55 → 60** (▲+5). Every other v1.3 ▲ in the paste (Lokhust Lord, Lokhust Destroyers, Lokhust Heavy Destroyers, Ophydian Destroyers, Skorpekh Lord) touches units not fielded by any owned list.

**Space Marines (owned collection impact):** **None.** The only v1.3 ▲ (Centurion Devastator Squad +15, Land Raider Redeemer +10/+10, Librarian in Terminator Armour +10) lands on units not owned and not in any Blood Ravens Matched/Casual starter. Every core Blood Ravens cost (Captain, Tactical Squad, Devastator Squad, Terminator Squad, Whirlwind, etc.) is unchanged, and the MFM v1.3 paste's new **Legends** section confirms the Casual starters' Bike Squad / Attack Bike / Astartes Servitors figures match what was already sourced from the standalone Legends Field Manual.

### WarCom commentary (context, not a rules change in itself)

Frames the field as broadly balanced; targets a handful of outlier factions (none onboarded in this repo) with points moves; opens some previously-restricted detachment pairings; nudges Force Disposition recommended map layouts (more six-objective maps for Disruption players). **September is the last monthly pass**; balance returns to **quarterly** afterward.

---

## Shipping impact (already complete as of this pass)

| Slice | What shipped | Status |
|-------|---------------|--------|
| S1 | `raw/pointers/rules_core.md`, `faction_pack_necrons.md`, `faction_pack_space_marines.md`, `points_manuals.md` — package rows + supersession notes; footer currency-line template | Complete |
| S2c | Necron MFM v1.3 recost across every owned Conclave/starter/army-list page (Warriors 80→85, Plasmancer 55→60); two pre-existing v1.2 arithmetic bugs fixed opportunistically | Complete |
| S2d | SM MFM v1.3 currency stamp + Casual Legends cross-check; no owned point changed; ▲ research notes on 3 unowned units | Complete |
| S2e | Universal Rules v1.1 quote pass in `Core_Rules_Quotes.md` (`18.06`/`18.07` verbatim, filename+page+ID); teaching paraphrase in `Turn_Structure.md`, `Keyword_Glossary.md`, `Quick_Reference_Card.md` | Complete |

See also [[sm_codex_oct_2026_preview]] — a **separate product** (October Codex preview), not part of this August package, tracked on its own source page.

---

## What this source does not cover

- A titled "Balance Dataslate" PDF for 40K — it does not exist this pass
- Any faction outside Necrons / Space Marines (Daemons, Emperor's Children, Custodes, Astra Militarum, Death Guard, Aeldari, Orks named in WarCom commentary as context only)
- Codex: Space Marines October content — separate product, see [[sm_codex_oct_2026_preview]]
- Kill Team — see [[kt_aug_2026_balance_package]]

---

## Open questions

1. Confirm the owner has saved the Universal Rules v1.1 and both Faction Pack v1.2 PDFs under `C:\Personal\40K\rules\` (staging copy is branch-only, temporary, cleanup pending).
2. Confirm the MFM v1.3 owner paste against a saved PDF for both Necrons and Space Marines — upgrade `draft` → `verified` once done.
3. Canonical WarCom URL for the "What's New?" commentary article (egress blocked at capture time).

---

## Related pages

- [[warcom_free_core_rules_11e]] — prior (July v1.0) Universal Rules source page; superseded on the same topics by this package
- [[necron_warriors]] · [[necrons]] — points-impacted unit/faction pages
- [[space_marines]] — confirmed-unchanged faction page
- [[sm_codex_oct_2026_preview]] — separate October product
- [[kt_aug_2026_balance_package]] — the Kill Team sibling package
- [[glossary]] — Assault Disembark Move / Shock Disembark Move stubs
- [[index]]
