---
title: Inherited docs for S3
type: analysis
system: warhammer_40k_11e
created: 2026-08-16
updated: 2026-08-17
sources: [necron_lists_owner_notes, source_library, local_library_pointers, wahapedia, warhammer_community, kill_team_necron_photos]
confidence: verified
tags: [analysis, handoff, s3, teaching_promotion, stable_facts]
---

# Inherited docs for S3

What L1 hands to S3: the facts stable enough to teach from, the claims that are not, and which unread pointer answers which question.

---

## How to read this page

S3 writes `rules/`, `setup/`, and the shipping `Keyword_Glossary` under `games/warhammer_40k_11e/`. That is **player-facing truth**, so it needs a clear line between what this KB actually knows and what it merely wrote down.

| Tier | Meaning | S3 may |
|------|---------|--------|
| **Stable** | Confirmed by a source, or a project decision of record | Teach it directly |
| **Named, not verified** | The term is right; the effect is one person's paraphrase | Name it, mark it, do not explain it as fact |
| **Unverified** | Written from familiarity with no source read | Do not ship. Read the pointer first |

`confidence: verified` on this page means the **classification** is verified - each row was checked against the source that supports it. It does not upgrade the underlying claims.

---

## Stable - ready to teach

### Ownership, confirmed 2026-08-16

| Fact | Detail |
|------|--------|
| **Kill Team: Tomb World** | **Owned and game-ready** - 1 Cryptek Geomancer, 2 Canoptek Tomb Crawlers, 5 Canoptek Macrocytes, 10 Necron Warriors, 3 Canoptek Scarab Swarms. Assembled, painted, known datasheets |
| Hierotek Circle Kill Team (used) | 1 set, assembled and painted, **game ready** - 40K datasheets **TBD pending photos** |
| Necron Warriors, second squad | 10, purchased, **unassembled** - assemble-to-expand |
| Canoptek Scarab Swarms, second set | 3, purchased, **unassembled** - assemble-to-expand |
| Immortals | 5 (1 squad), purchased, **unassembled** - build before play |
| Totals | **20 Necron Warriors, 6 Canoptek Scarab Swarms**, plus Geomancer, Tomb Crawlers, Macrocytes, Immortals, Hierotek Circle |

Sourced from the FOUNDATION section of `games/warhammer_40k_11e/armies/necrons/Necron_Lists.md`, mirrored in `raw/` and the S2 inventory, and summarized on [[necrons]].

**Superseded, and S3 must not reintroduce it:** an earlier version of this table recorded Kill Team: Tomb World as *not owned* and its lists as historical. That was erroneous. There is no "Tomb World is not owned" fact anywhere in this KB any more, and content that assumes one is wrong.

**Three teaching constraints follow:**

1. **There is a playable army today.** The Tomb World units are the preferred learning baseline - a full, identified, painted force. "Play this weekend" content should be written against them.
2. **Build before play still applies, but narrowly.** The Immortals are the only owned unit that cannot be fielded at all until built. The spare Warriors and Scarabs widen squads that already exist.
3. **Do not re-shop owned models.** An earlier blueprint double-counted the Immortals and a Warrior box. The corrected version strikes the Tomb World box, both Warrior squads, both Scarab sets, and the Immortals off the retail list.

### Terminology and attribution

| Fact | Support |
|------|---------|
| **Power Matrix is a Warhammer 40,000 term**, the [[canoptek_court]] detachment rule - **not** Kill Team | Two independent in-repo sources; supersedes the L0 glossary warning. See [[power_matrix]] |
| **Technosorcerous Augmentations** is the [[cryptek_conclave]] detachment rule | Owned faction pack v1.1 p.7 and [[wahapedia]], both 2026-08-16. **This row said "Scientific Schemes" when it was handed to S3.** S3 caught the conflict, S4 shipped the correct name, and L2 applied it across `KB/` |
| **Reanimation Protocols** is the Necron army rule | Consistent across every repo source |
| **Oath of Moment** is the Space Marine army rule | Consistent across every repo source |
| **Gladius Task Force** is the chosen Space Marine learning detachment | Project decision of record |
| The Hierotek Circle box is **not** evidence about any 40K rule | The L0 inference that produced the Power Matrix error |

### Project conventions S3 must follow

| Convention | Where |
|------------|-------|
| No GW binaries, no verbatim rules text, teaching paraphrase only | [`AGENTS.md`](../../AGENTS.md) Sec 10 |
| Every rules claim cites a source **with a retrieval date** | Same |
| `games/**` uses Rising Tide header and footer, `Snake_Case` filenames | [`AGENTS.md`](../../AGENTS.md) Sec 6 |
| `KB/**` uses YAML frontmatter only - the two must not stack | Same |
| Never write `raw/`; never commit | Sec 13 |

---

## Named, not verified - mark these

S3 may use the names. It must not present the effects as fact.

| Term | What the source says | Missing |
|------|---------------------|---------|
| Power Matrix | Hit re-rolls within controlled territory | What "controlled territory" means; whether melee, shooting, or both |
| ~~Scientific Schemes~~ Technosorcerous Augmentations | The source claimed stacking ranged buffs plus reanimation multipliers | **Resolved after S3.** The name was wrong and the effect was half wrong - the reanimation half is a stratagem, not the detachment rule. See [[cryptek_conclave]] |
| Points values (Warriors 100, Immortals 75, Scarabs 40, Wraiths 125, Doomstalker 145, Szeras 175, Lychguard 170, Plasmancer 65) | Owner's notes | Cross-check against the Munitorum Field Manual - a dataslate may have moved them |
| Squad merging (Warriors to 20, Immortals to 10, Wraiths to 6) | Owner's notes | Whether these are legal unit sizes in 11e |
| Unit ability leads (Macrocytes granting *Ignores Cover*; Szeras AP aura; Plasmancer improving critical hits) | Owner's notes | All of it |
| **"Data Package Detachment"** (tier label, "3" and "2") | Owner's notes | Does not map to any recognised 40K term. **Do not propagate.** See [[glossary]] |

---

## Unverified - read the pointer first

Nothing in this group has a source behind it. Each row names the pointer that would fix it.

| Topic | KB page | Pointer to read |
|-------|---------|-----------------|
| Objective Control and scoring | [[objective_control]] | `raw/pointers/rules_core.md` |
| Turn sequence, phases, attack resolution | *(no page yet)* | `raw/pointers/rules_core.md` |
| Terrain categories and footprints | *(no page yet)* | `raw/pointers/terrain_footprints.md` |
| Deployment and board setup | *(no page yet)* | `raw/pointers/rules_core.md`, `raw/pointers/terrain_footprints.md` |
| Reanimation Protocols timing and amount | [[reanimation_protocols]] | `raw/pointers/faction_pack_necrons.md` |
| Oath of Moment benefit and timing | [[oath_of_moment]] | `raw/pointers/faction_pack_space_marines.md` |
| Points currency | - | `raw/pointers/points_manuals.md` |

**The largest gap in this project is not missing sources - it is unread ones.** The owner already has the core rules, both faction packs, the points manuals, and the terrain documents. Six of the eight pointer stubs address open questions on this page. Opening them is S3's highest-value first action, and the ingest order in [[ingest_procedure]] says to do it before any unit content.

---

## Keyword_Glossary alignment

[[glossary]] is the KB-side working surface; S3 owns the shipping `games/warhammer_40k_11e/rules/Keyword_Glossary.md`. Draw from the former, and keep three things intact:

- **The status marker.** Every term carries `verified` / `draft` / `unverified`. Dropping it in the shipping version would ship confidence the KB does not have.
- **Terms grouped by scope** - core rules, Necrons, Space Marines, project vocabulary. The KB glossary is already sectioned this way.
- **The deprecated list.** "Tomb World is not owned", the retired "do not let Tomb World leak" rule, and "Data Package Detachment" all need to stay flagged as claims **not** to reuse.

If S3 verifies a term against a source, update the KB glossary in the same pass and record the retrieval date. Verification that only lands in shipping content is lost to every future session.

---

## Open threads S3 inherits

| Thread | Blocks | Owner |
|--------|--------|-------|
| **Hierotek Circle photo ID** | **Closed 2026-08-17.** Technomancer + Immortals legal; Apprentek/Warden proxies; Plasmacytes likely not dual-legal | See [[kill_team_necron_photos]] |
| Space Marine collection audit | Any S5 content | User, S5 prep |
| Wahapedia `wh40k10ed` URL path - 10e or 11e? | Confidence of every web cross-check | S3, see [[wahapedia]] |
| Whether owned PDFs have been superseded by a dataslate | Confidence of everything | S3, see [[warhammer_community]] |

---

## Related pages

- [[objective_control]] - the core-rules concept S3 verifies first
- [[glossary]] - the working terminology surface
- [[necrons]] · [[space_marines]] - the two factions
- [[power_matrix]] - the correction S3 should not re-break
- [[kill_team_necron_photos]] - Hierotek photo ID closed 2026-08-17
- [[local_library_pointers]] - the unread material
- [[ingest_procedure]] · [[index]] · [[overview]]
