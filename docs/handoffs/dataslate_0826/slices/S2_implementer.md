# S2 Implementer — dataslate_0826

**Slice:** S2 — 40K Faction Pack / package teaching beyond MFM/core/Codex slices
**Status:** Complete (gap-fill pass; siblings S2b/S2c/S2d/S2e already covered the substantive deltas)
**Date:** 2026-08-27
**Model:** `claude-sonnet-5-thinking-high` (per track model matrix)
**Authorization:** Owner 2026-08-27 — AUTHORIZED, draft accepted. Codex wall in force. No git commit/push by this subagent.

## Summary

Read [`S2_brief.md`](S2_brief.md), the Faction Pack v1.2 staging note, the WarCom August balance commentary, and all four sibling implementer reports (S2b Codex Oct preview, S2c Necron MFM v1.3, S2d SM MFM v1.3, S2e Universal Rules v1.1) before touching anything, per the brief's "do not duplicate" instruction.

**Finding: the substantive Faction Pack v1.2 teaching deltas were already correct on every shipping page that teaches them**, because the v1.1 → v1.2 items relevant to this collection are *carry-forward* facts (already errata'd in the v1.1 pass some slices back) rather than new v1.2 changes:

- Necrons: Reanimation Protocols already teaches **heal D3 wounds** ([`Reanimation_Protocols.md`](../../../games/warhammer_40k_11e/armies/necrons/Reanimation_Protocols.md)); Crypteks already taught as **Support, not Leader** ([`Cryptek_Conclave.md`](../../../games/warhammer_40k_11e/armies/necrons/Cryptek_Conclave.md)); Canoptek Court's Reactive Subroutines already taught at the errata'd **8" range** ([`Canoptek_Court.md`](../../../games/warhammer_40k_11e/armies/necrons/Canoptek_Court.md)).
- Space Marines: Gladius's Adaptive Strategy FAQ ("does not require an active Combat Doctrine") and the Squad Tactics **8" range** errata are already taught on [`Gladius_Task_Force.md`](../../../games/warhammer_40k_11e/armies/space_marines/Gladius_Task_Force.md).

What **was** actually missing was **currency**: five pages (both faction READMEs, `Cryptek_Conclave.md`, `Canoptek_Court.md`, `Reanimation_Protocols.md`, `Gladius_Task_Force.md`) still cited **Faction Pack v1.1** in their SOURCES header even though the teaching content already matched v1.2, and the WarCom Force Disposition / map-layout commentary had no pointer anywhere on the setup 2-pager. This slice closed both gaps additively, re-verified (not re-derived) the already-correct facts against the v1.2 staging note, and wrote explicit no-op waivers for everything else the brief named that either has no matching page in this collection or is not owned/not fielded.

## Done (mapped to brief requirements)

1. **FP v1.2 teaching deltas not covered by siblings** — checked all five staging-note items against shipping pages:
   - Reanimation Protocols heal D3 — **already correct**, re-stamped currency only.
   - Cryptek Support not Leader — **already correct**, re-stamped currency only.
   - Canoptek Court Reactive Subroutines 9"→8" — **already correct**, re-stamped currency only.
   - Gladius FAQ Adaptive Strategy — **already correct**, re-stamped currency only.
   - Teleport Homer 9"→8" — **not taught anywhere** (Terminator/Terminator-Assault/Captain-in-Terminator-Armour research pages are all `completeness: stub`, zero ability content) — **waiver**, no page to touch.
   - Cursed Legion (Unnatural Aggression) — **no page exists** for Cursed Legion in this collection — **waiver**, per the brief's own "only if page exists" instruction.
2. **Force Disposition / map commentary** — [`Chapter_Approved_Force_Dispositions.md`](../../../games/warhammer_40k_11e/setup/Chapter_Approved_Force_Dispositions.md) exists and is the right page. Added a `draft` paraphrase callout citing [`warcom_40k_balance_commentary_aug.md`](../research/warcom_40k_balance_commentary_aug.md): more six-objective Disruption layouts, nudged expansion-objective terrain footprints — **no map ID or layout letter invented**; explicitly flags that no Event Companion / Chapter Approved PDF is in hand for this pass, so layouts A/B/C on the page are left untouched.
3. **Package currency stamp on army READMEs** — both `README.md` files cited Faction Pack v1.1 in SOURCES with no v1.2 line anywhere. Added the staging PDF path, marked the v1.1 copy superseded, and added a **Faction Pack v1.2** clause to the `Rules currency` line, on both faction READMEs plus the four detachment/army-rule pages named above (`Cryptek_Conclave.md`, `Canoptek_Court.md`, `Reanimation_Protocols.md`, `Gladius_Task_Force.md`). Also fixed two pre-existing header/Change-Log `VERSION` mismatches found opportunistically while editing (`necrons/README.md` header said v0.5.4 while the top Change Log entry already said v0.5.5; `Cryptek_Conclave.md` / `Canoptek_Court.md` headers said v0.5.3 against v0.5.4 top entries) — corrected to match on every file this slice touched.
4. **No-op waivers for out-of-scope factions** — see below.
5. This report.

## Files changed

**Necrons (4):**
- `games/warhammer_40k_11e/armies/necrons/README.md` — SOURCES: added FP v1.2 staging path, marked v1.1 superseded; `Rules currency` line gains Faction Pack v1.2; header VERSION corrected v0.5.4→v0.5.6 (was already out of sync with Change Log); new Change Log entry.
- `games/warhammer_40k_11e/armies/necrons/Cryptek_Conclave.md` — SOURCES + `Rules currency` FP v1.2 stamp confirming Support-not-Leader unchanged; header VERSION corrected v0.5.3→v0.5.5; new Change Log entry.
- `games/warhammer_40k_11e/armies/necrons/Canoptek_Court.md` — SOURCES + `Rules currency` FP v1.2 stamp confirming Reactive Subroutines 8" range unchanged; header VERSION corrected v0.5.3→v0.5.5; new Change Log entry.
- `games/warhammer_40k_11e/armies/necrons/Reanimation_Protocols.md` — SOURCES FP v1.2 stamp confirming heal-D3 unchanged; added a `Rules currency` line to the GW notice section (this page did not have one before); header VERSION v0.5.4→v0.5.5; new Change Log entry.

**Space Marines (2):**
- `games/warhammer_40k_11e/armies/space_marines/README.md` — SOURCES: added FP v1.2 staging path, marked v1.1 superseded; `Rules currency` line gains Faction Pack v1.2; header VERSION v1.11→v1.12; new Change Log entry.
- `games/warhammer_40k_11e/armies/space_marines/Gladius_Task_Force.md` — SOURCES + `Rules currency` FP v1.2 stamp confirming Adaptive Strategy FAQ + Squad Tactics 8" unchanged; header VERSION v0.5.2→v0.5.3; new Change Log entry.

**Setup (1):**
- `games/warhammer_40k_11e/setup/Chapter_Approved_Force_Dispositions.md` — new `draft` paraphrase callout on the WarCom August recommended-layout watch (six-objective Disruption maps, nudged expansion terrain), sourced from `warcom_40k_balance_commentary_aug.md`, explicit no-invented-map-ID flag; SOURCES pointer added; header VERSION v1.1→v1.2; new Change Log entry.

**New file:**
- `docs/handoffs/dataslate_0826/slices/S2_implementer.md` (this report)

**7 shipping files touched + 1 new handoff file.**

## Waivers / no-op — out-of-scope factions (named in WarCom commentary)

Per `warcom_40k_balance_commentary_aug.md`: "Onboarded factions in this repo: Necrons and Space Marines... out of shipping scope except as context." Explicit no-op waivers, one per named faction:

| Faction | Commentary content | Waiver reason |
|---------|--------------------|----------------|
| **Chaos Daemons** | Slight points increase (Aug pass) | Not onboarded in this repo. No `games/warhammer_40k_11e/armies/` page exists. No action. |
| **Emperor's Children** | Slight points increase (Aug pass) | Not onboarded. No action. |
| **Adeptus Custodes** | Slight points increase (Aug pass) | Not onboarded. No action. |
| **Astra Militarum** | Targeted points reduction | Not onboarded. No action. |
| **Death Guard** | Targeted points reduction; Mortarion's Hammer + Contagion Engines detachment pairing unlocked | Not onboarded. No action. |
| **Aeldari** | Targeted points reduction | Not onboarded. No action. |
| **Orks** | Explicitly **excluded** from this balance pass (new Codex on pre-order) | Not onboarded, and WarCom itself defers Ork points to the Codex. No action either way. |

## Waivers / no-op — FP v1.2 items with no matching shipping page or not fielded

| Item | Research note says | Why waived |
|------|--------------------|-----------|
| **Cursed Legion — Unnatural Aggression** (Necrons) | Charge only targets affected enemy units; no Charge bonus even on success | No `Cursed_Legion.md` or equivalent page exists anywhere under `armies/necrons/`. Brief explicitly gates this on "only if page exists." |
| **Terminator / Assault Terminator Teleport Homer 9"→8"** (SM) | Range errata | `Terminator-Squad.md`, `Terminator-Assault-Squad.md`, `Captain-in-Terminator-Armour.md` are all `completeness: stub` research pages with **zero** ability content (every section reads "_Pending_"). Nothing currently teaches Teleport Homer to update. Filling in full datasheet ability text on these stubs would be a full-MFM/datasheet-style expansion, out of this currency-only slice's scope (consistent with S2d's "no full MFM dump" boundary on the same ~90 stub pages). |
| **Outrider Turbo-boost removed / Thunderous Impact** (SM) | New melee-charge bonus | `Outrider-Squad.md` is a `completeness: stub` research page; **no Casual or Matched starter fields Outriders** (grepped every `Starter_*.md` — zero hits). Waived per the brief's own "if Outriders appear" condition — they do not. |
| **Guilliman Supreme Strategist / Uriel Ventris stratagem-cost interaction** (SM) | Cross-link to Universal Rules v1.1 unnamed-stratagem 0CP interaction | No `Guilliman*.md` research page exists; Uriel Ventris is already handled as a "not owned, named character" row in S2b's Legendary Proxies table (no separate page). Neither character is owned or fielded. No page to cross-link from. |
| **Wardens of Ultramar — adds Support Core Ability** (SM) | Detachment change | No `Wardens_of_Ultramar.md` or equivalent detachment page exists — this collection only ships Gladius / 1st Company / Anvil detachment guides. No action. |
| **Armoured Speartip — Rapid Embarkation same-turn disembark/embark** (SM) | Detachment change | No `Armoured_Speartip.md` page exists. No action. |
| **Land Raider Crusader/Redeemer — `LAND RAIDER` keyword added** (SM) | Taxonomy-only keyword | `Land-Raider-Crusader.md` / `Land-Raider-Redeemer.md` are both `completeness: stub` with `Keywords: _Pending_`; neither is owned nor fielded on any starter (confirmed by S2d). A keyword-only note with no rules effect and no shipping consumer is not worth a stub edit in a currency-only pass — flagged here for QA visibility, not touched. |
| **FRAME removed from Legends** (Night Shroud — Necrons; Caestus/Fire Raptor/Javelin/Land Speeder variants/Sokar Stormbird/Storm Eagle/Thunderhawk Transporter/Xiphon — SM) | Legends datasheet attribute removed | None of these datasheets are owned, fielded, or have a research page beyond a stub (`Night-Scythe.md` is the only one with a page, and it is explicitly flagged "research only unless owned" by the FP v1.2 staging note itself). `FRAME` is a deployment-permission attribute with no teaching consequence at the stub level. No action. |
| **Hypercrypt / Resurrection Orb / Annihilation Legion detachment deltas** (Necrons) | Detachment-specific rules updates | No detachment page for Hypercrypt or Annihilation Legion exists (this collection ships only Canoptek Court + Cryptek Conclave). Resurrection Orb is already taught correctly on `Reanimation_Protocols.md`'s "Things that make it bigger" table (once per battle **per unit**, heals **D6**, one resurrect per turn — matches the v1.2 staging note exactly); re-verified, no change needed. |
| **Night Scythe stats** (Necrons) | M14", Hover, not AIRCRAFT, Deep Strike | Staging note itself says "Research only unless owned." Not owned. `Night-Scythe.md` stub left untouched. |

## Codex wall / copyright compliance

- No datasheet statline, stratagem body text, or enhancement text was quoted from either Faction Pack. Every edit is a **source-citation refresh** (SOURCES header, `Rules currency` line, Change Log) plus one short teaching-paraphrase callout on the setup page — no verbatim rules text anywhere.
- The Force Disposition commentary callout on `Chapter_Approved_Force_Dispositions.md` paraphrases the WarCom owner paste; it does not quote it, and it explicitly refuses to invent map/layout IDs not present in an owned Event Companion / Chapter Approved PDF.
- `games/warhammer_40k_11e/armies/**` (Codex wall paths) received only citation refreshes, no new rules content beyond restating already-shipped facts.
- No PDF binary was read, copied, or committed. No `git add` / `git commit` / `git push` was run by this subagent.

## Not touched (explicitly out of scope for S2)

- MFM v1.3 points — S2c (Necrons) / S2d (Space Marines), already complete. Not re-touched.
- Universal Rules v1.1 core IDs / disembark move types — S2e, already complete. Not re-touched.
- SM Codex October preview / Legendary Proxies — S2b, already complete. Not re-touched.
- `games/warhammer_40k_11e/setup/print/40k_chapter_approved_force_dispositions.html` — the print HTML companion to `Chapter_Approved_Force_Dispositions.md` was **not** updated with the new WarCom commentary callout. Checked: it already does not carry any of the page's existing WD527 Commentary blocks either (grepped for "Commentary"/"WD527" — zero hits), so this is a pre-existing markdown/print-HTML sync gap predating this slice, not something this edit introduced. Flagged for QA/Coordinator; the 2-page print constraint (`PRINT_NOTE: Exactly two pages`) was not at risk since nothing was added to the HTML.
- `KB/**` — Librarian-owned; not touched by this Implementer slice.
- `Cryptek_Conclave_Primary_Missions.md`, `Owned_Models_Inventory.md`, and every starter/army-list page — no FP v1.2 teaching-fact changed on any of them (all relevant facts were already correct), so no currency stamp was added there; the faction-level README + the four detachment/army-rule pages are the load-bearing currency surfaces for Faction Pack citations in this collection.
- `First_Company_Task_Force.md` / `Anvil_Siege_Force.md` — these two `draft` detachment guides were never sourced from the owned Faction Pack (public 11e references only, per their own SOURCES headers) and the FP v1.2 research note does not name either detachment — no stamp added.

## Waivers / open items for QA

1. **Currency-only re-verification, not a re-read of the v1.2 PDF page-by-page.** Every "already correct" claim in this report was checked against the FP v1.2 **staging research note** (`staging_40k_faction_packs_v1_2.md`), which is itself `draft` pending owner confirmation of a saved path under `C:\Personal\40K\rules\`. If the owner's eventual saved v1.2 copy disagrees with the staging extract on any of the four re-stamped facts, that is a research-note correction, not an Implementer error — flag back to the research note if found.
2. **Two pre-existing VERSION header / Change Log mismatches were fixed opportunistically** (`necrons/README.md`, `Cryptek_Conclave.md`, `Canoptek_Court.md` — header VERSION lagged one entry behind the top Change Log line, predating this slice). QA should confirm this is an acceptable in-scope fix rather than a separate slice, consistent with S2c's precedent of fixing pre-existing arithmetic bugs opportunistically.
3. **Print HTML / markdown sync gap on `Chapter_Approved_Force_Dispositions.md`** is pre-existing (the page's own WD527 Commentary blocks are not in the print HTML either) — not introduced by this slice, but flagged for a future print-refresh pass.
4. **Land Raider `LAND RAIDER` keyword and the eight "FRAME removed from Legends" SM flyers/speeders** were judged not worth a stub edit (no rules effect at the stub-teaching level, nothing owned or fielded) — QA should confirm this reading or ask for a one-line note on the affected stub pages.
5. No PDF was read via any tool that would copy it; no `git add`/`git commit`/`git push` was run by this subagent.
