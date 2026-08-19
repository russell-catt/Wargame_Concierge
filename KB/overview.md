---
title: Overview
type: overview
system: multi_system
systems: [warhammer_40k_11e, kill_team_2024]
created: 2026-08-16
updated: 2026-08-18
version: 0.5.0
sources: [necron_lists_owner_notes, source_library, local_library_pointers, wahapedia, warhammer_community, kill_team_2024_core_rules, kill_team_necron_photos, uml_diagrams_org, warcom_free_core_rules_11e]
confidence: draft
tags: [overview, synthesis, warhammer_40k, necrons, space_marines, kill_team_2024]
---

# Knowledge Base Overview

The working synthesis of everything in this KB. Updated after any ingest that shifts the big picture.

---

## What Wargame_Concierge is

A personal **wargame concierge**: a knowledge base that helps its owner learn a tabletop wargame, build lists from models actually owned, and play games without constantly flipping through rulebooks.

It is built on the Karpathy "LLM Wiki" pattern (see [`reference/llm-wiki.md`](../reference/llm-wiki.md)): immutable sources in `raw/`, an LLM-maintained knowledge layer in `KB/`, and player-facing content promoted into `docs/` and `games/`. The point is **compounding** - each source read and each question answered gets filed, so the same ground is never re-covered from scratch.

The project is **game-agnostic by design**. `games/` holds one subtree per system. **Warhammer 40,000 11e** is the first worked example; **Kill Team 2024** is the second (onboarded). [`docs/Game_System_Scaffold.md`](../docs/Game_System_Scaffold.md) is the checklist for system #3.

**40K Core quotes (2026-08-18).** Track `40k_warcom_quotes` added a numbered-ID appendix under [`games/warhammer_40k_11e/rules/Core_Rules_Quotes.md`](../games/warhammer_40k_11e/rules/Core_Rules_Quotes.md). **KB stays paraphrase.** Cite IDs such as **01.01** and **06.01**; do not paste Core quote bodies here. **Codex wall** still holds for army folders. See [[warcom_free_core_rules_11e]]. **Necron lists:** Personal `C:\Personal\40K\Necron_Lists.md` wins if the games working copy diverges.

**Flowcharting (2026-08-18).** Print trees and ops mermaid charts use **UML 2.5 activity** shapes (start, action, decision+guards, end). That is project notation, not a rules term — see [[flowcharting_uml_activity]] and [[uml_diagrams_org]] (Kirill Fakhroutdinov / uml-diagrams.org). Shipping guide: [`docs/operations/Flowcharting.md`](../docs/operations/Flowcharting.md).

---

## First system: Warhammer 40,000, 11th Edition

**Warhammer 40,000 11th Edition** is the first system in scope, and still carries the great majority of KB content. Everything about it should carry `system: warhammer_40k_11e` in its frontmatter. **As of 2026-08-17 it is no longer the only system** - see the Kill Team 2024 section immediately below.

The edition is **new**, which shapes how this KB is written:

- Most rules knowledge starts at `confidence: unverified` or `draft` and gets promoted only after a cross-check
- Anything carried over from 10th Edition is suspect until confirmed - edition drift is an explicit lint category
- Living references (Warhammer Community, Wahapedia) move under us, so every rules claim records a **retrieval date**

**Audience:** a beginner learning the game. Content should teach the reasoning behind a rule or a play, not just state it.

---

## Second system: Kill Team 2024 (KT24 / 3rd Edition)

**Added 2026-08-17, track `kill_team_2024_scaffold`, slice L1; shipping-backed rewrite 2026-08-18 (v0.5.0).** This is the second game system the KB is designed to carry. Everything under this heading carries `system: kill_team_2024`.

**Kill Team and Warhammer 40,000 are two separate Games Workshop products:**

- **Rules stay split.** Collision flags in [[glossary]]. Neither entry describes the other system's mechanic.
- **Models can dual-use** with base-size honesty — [[kill_team_necron_photos]], [[necrons]].
- **Quote exception** is scoped to that subtree only. **Hierarchy:** Full-Scan Core Book is baseline; dated `eng_*` patches supersede; Jul 25 lite is intro — **omission is not a patch.** Ledger: [`Patch_Manifest.md`](../games/kill_team_2024/rules/Patch_Manifest.md). Targeting quotes: [`Target_Eligibility.md`](../games/kill_team_2024/rules/Target_Eligibility.md) (owner-verified **2026-08-18**). **40K** has a parallel exception under `games/warhammer_40k_11e/rules/` and `setup/` only — see [[warcom_free_core_rules_11e]].

**What the v0.5.0 Librarian pass did.** Flagged the L1 Wahapedia drafts, then replaced them with teaching paraphrase of shipping. [[kill_team_2024_core_rules]] is `verified` **for the targeting subset only**. New pages: [[valid_target]], [[kill_team_terrain]], [[killzones_volkus_tomb_world]]. Teams / joint_ops / nemesis_ops / critical_ops stay index-only.

**What is still open.** Ten owned team-rule PDFs as full KB faction/unit trees; ops card text; remaining Core chapters unread. Most KT24 glossary rows stay `draft`.

---

## Armies in scope

Two factions, chosen because they are the models on hand.

### Necrons - primary

The learning army. Ownership confirmed 2026-08-16 (see the Preflight notes in [`track_in.md`](../docs/handoffs/v1_scaffold/track_in.md)):

| Models | Count | State |
|--------|-------|-------|
| Cryptek Geomancer (Tomb World) | 1 | **Game ready** |
| Canoptek Tomb Crawlers (Tomb World) | 2 | **Game ready** |
| Canoptek Macrocytes (Tomb World) | 5 | **Game ready** |
| Necron Warriors (Tomb World squad) | 10 | **Game ready** |
| Canoptek Scarab Swarms (Tomb World set) | 3 | **Game ready** |
| Hierotek Circle (used set) | 1 set | **Photo ID done** — Technomancer, Immortals, Despotek, Apprentek, Plasmacytes |
| Necron Warriors (second squad) | 10 | Purchased, unassembled |
| Canoptek Scarab Swarms (second set) | 3 | Purchased, unassembled |
| Immortals | 5 | Purchased, unassembled |

**Totals:** 20 Warriors, 6 Scarab Swarms, Geomancer, Tomb Crawlers, Macrocytes, Technomancer, Immortals (Hierotek assembled + sprue), Apprentek, Hierotek Plasmacytes.

Full page: [[necrons]]. Open threads:

- **Hierotek photo ID is closed.** Legal 40K maps are Technomancer and Immortals; Apprentek/Warden are proxies; Plasmacytes likely not dual-legal (25mm vs 28mm).
- **Sprue still needs building.** Second Warriors, second Scarabs, 5 Immortals.

The collection's shape, stated plainly: **there is a complete, painted, identified army available today.** The Kill Team: Tomb World units are the owner's preferred learning baseline, and everything else in the collection expands them.

Two detachment paths are costed from this collection - [[canoptek_court]] and [[cryptek_conclave]] - and Tomb World gives **both** of them a legal Phase 1 force, so the choice is no longer gated on a purchase or an identification. The Conclave stays the shorter route to a finished path, and it is now grounded in a real model rather than a hypothesis: the game-ready Geomancer is the Cryptek character it needs.

**Correction of record.** An earlier version of this KB recorded **Kill Team: Tomb World as not owned**, treated its lists as superseded history, and carried a standing rule against letting that content reach current advice. All of that was erroneous and is withdrawn. See the deprecated list in [[glossary]].

### Space Marines - secondary

The comparison and opponent army, played by the owner's son. Used to teach contrast: a straightforward, forgiving faction set against the Necrons' resilience mechanics, with [[gladius_task_force]] as the target detachment. Built from **existing older kits**, so legacy and Firstborn datasheets stay in scope.

**No ownership inventory recorded yet** - the worksheet exists and is empty. See [[space_marines]]. This is the largest single unknown on that side, and it gates any S5 content: a starter list cannot be written for an uncatalogued collection.

---

## Current state

| Metric | Value |
|--------|-------|
| Systems in scope | 2 - `warhammer_40k_11e` (primary), `kill_team_2024` (second system, shipping + KB v0.5.0) |
| Sources ingested | 40K set + KT24 core (targeting **verified** 2026-08-18; other Core `draft`) + Nemesis/photo sources |
| KB entity pages | 40K set + KT24 (1 source, 7 concepts, 2 setup) |
| KB core pages | 6 (index, log, overview, glossary, changelog, ingest_procedure) — YAML `version: 0.5.0` |
| Glossary terms | 40K verified set + KT24 section expanded (Visible, Vantage, Seek, Blast, Torrent, Guard, Valid Target → [[valid_target]]) |
| Last ingest | 2026-08-18 (v0.5.0 — shipping → KB paraphrase; no quote dump) |
| Last lint | 2026-08-16 (L2, `tomb_world_ownership` - **40K only**) |
| Schema / project version | AGENTS.md **v0.5.0** (2026-08-18); git tags `v0.1.0` (bootstrap) and `v0.5.0` (this snapshot) |

The KB was bootstrapped in slice **L0** and took its first real ingest in **L1**, both on 2026-08-16. The ingest contract now has a worked example behind it rather than only a procedure.

**What that ingest did and did not establish.** It read the owner's Necron notes and the source catalog in full, and it registered the two living web references without opening them. It produced faction, detachment, and concept pages that are honest about resting on one planning document. It did **not** read a single rules document: the core rules, both faction packs, the terrain PDFs, and the points manuals are all sitting on the owner's disk, catalogued in [[local_library_pointers]], unopened.

So the shape of the gap has changed - twice. At L1 it was no longer "we do not have sources" but **"we have not read the sources we have."** That second gap has since closed on the shipping side: S3 read the core rules and setup, S4 and S5 read both faction packs and Munitorum Field Manual v1.2 for the faction starters, and S6 enumerated both unit rosters.

**The gap now is a back-fill gap.** The rules have been read into `games/`, not into `KB/`. The faction, detachment and concept pages here still mostly rest on the owner's planning notes, which is why they remain `draft` and `unverified` while the shipping teaching content carries verified rule text. Where the two disagree, the shipping content is newer and better sourced. Closing that gap - re-ingesting the shipping pages back into `KB/` - is the largest single piece of Librarian work outstanding.

---

## Key themes

Expect these to be the organizing ideas as content lands. They are hypotheses right now, not findings:

- **Resilience vs efficiency** - Necrons trade raw output for models that keep coming back; learning the army means learning when that trade pays
- **Objective play over kill count** - modern 40K is scored on objectives, so setup, screening, and scoring patterns matter more than damage tables
- **Build-before-play reality** - teaching content has to work for a partly unassembled collection
- **Edition freshness** - 11th Edition claims decay; the KB needs verification dates more than it needs volume

---

## Resolved in L1

- **Power Matrix is a Warhammer 40,000 term, not Kill Team.** L0 flagged the attribution as unresolved because the owner's Hierotek Circle is a Kill Team box. Two independent in-repo sources name it as the [[canoptek_court]] detachment rule. Corrected on [[power_matrix]] and in [[glossary]]; the Hierotek Circle and the rule are now formally unrelated.

The L0 flag is why this cost one ingest to fix rather than surfacing halfway through S4. Writing uncertainty down loudly is working.

## Resolved in L1 - `tomb_world_ownership` (2026-08-16)

- **Kill Team: Tomb World is owned and game-ready.** Five datasheets' worth of assembled, painted, identified models. The KB had recorded the box as *not owned* and its lists as superseded, which was wrong in the other direction from the Power Matrix error: this time the KB was confidently denying something the owner has on a shelf.
- **The "do not let Tomb World leak" rule is retired.** It was written as a guardrail against stale data and became the stale data itself. It now exists only as a deprecated-claim row, so it cannot return as guidance.
- **Dual Warriors and Scarabs recorded.** 20 Warriors and 6 Scarab Swarms owned, half of each game-ready and half on sprue.

The lesson is the mirror image of the Power Matrix one. A loud flag made that error cheap to fix; a *negative* ownership claim written as settled fact propagated across the KB before anyone checked it. Inventory claims should carry the same "verify against the owner" discipline as rules claims.

## Resolved 2026-08-17 — Necron painted-model photo sync

- **Hierotek Circle identified.** Technomancer (cloak), Apprentek, Despotek, 3 Immortal Guardians, 2 Plasmacytes. Not Plasmancer, not Deathmarks. See [[kill_team_necron_photos]].
- **Canoptek Circle loadouts locked.** Tomb Crawlers 1 twin gauss reapers + 1 transdimensional isolator; Macrocyte Warriors 2 gauss scalpel + 1 tesla caster.
- **NPO Warriors counted as 10**, mixed flayer/reaper. Scarabs 3 bases.

---

## Open questions

- Dual-legality of Hierotek Plasmacytes (KT 25mm vs legacy 40K Plasmacyte 28mm) vs the faction pack. **To-do: purchase 25–28mm base rings.**
- What does Power Matrix actually *say* in 11th Edition? The name is settled; the wording is not.
- Which Necron detachment best suits a beginner with this specific model pool? [[cryptek_conclave]] is the current hypothesis - now resting on owned, game-ready models rather than on an unopened box, so what remains unknown is the detachment rules, not the inventory.
- What Space Marine ownership exists? The worksheet is empty and this gates all S5 content.
- Which 11th Edition rules genuinely changed from 10th, and which carried over unchanged?
- What is the target game size for early games (Combat Patrol, Incursion, Strike Force)?
- Do the Wahapedia URLs on a `wh40k10ed` path serve 11e content, or are they stale? See [[wahapedia]].
- Has a dataslate superseded the owned PDFs? Nothing records when they were downloaded, so this is currently unanswerable.

---

## Knowledge gaps

Areas with no real coverage. All but the last are blocked on **reading material the owner already has**:

- Core 11th Edition rules: turn sequence, phases, objective scoring - [[objective_control]] is a placeholder
- Deployment maps, terrain rules, and mission packs - no page exists
- Necron army rule detail - [[reanimation_protocols]] is `unverified`
- Space Marine army rule and detachment - [[oath_of_moment]] and [[gladius_task_force]] are `unverified` and `stub`
- Unit pages - none, deliberately: [[ingest_procedure]] puts core rules and setup first so unit pages have something to link to
- List-building from the owned pool - **unblocked** for Tomb World and for Hierotek's Technomancer/Immortals; Apprentek and Warden remain proxy-only
- **Kill Team 2024, core targeting** - shipping-backed; remaining Core chapters and team trees still open
- Core 11th Edition rules back-fill into KB from `games/warhammer_40k_11e/`

---

## Related pages

- [[index]] - full catalog of KB pages
- [[glossary]] - terminology and Keyword entries, now multi-system
- [[kill_team_2024_core_rules]] - the KT24 core-rules source page
- [[turning_points]] · [[activations_apl]] · [[orders_conceal_engage]] · [[cover_kill_team]] · [[control_range_kill_team]] · [[injured_operatives]] · [[valid_target]]
- [[kill_team_terrain]] · [[killzones_volkus_tomb_world]]
- [[inherited_docs_for_S3]] - what is stable enough to teach from
- [[kill_team_necron_photos]] - painted Necron photo ID (2026-08-17)
- [[necrons]] · [[space_marines]] - the two factions
- [[ingest_procedure]] - how sources become KB pages
- [[log]] - what has happened and when
- [[uml_diagrams_org]] · [[flowcharting_uml_activity]] - UML activity notation (not game rules)
- [`AGENTS.md`](../AGENTS.md) - schema source of truth
