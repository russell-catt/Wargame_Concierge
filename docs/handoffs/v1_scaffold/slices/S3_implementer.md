# S3 - Implementer report (Rules + Setup + Keyword_Glossary)

- **Status:** Resolved - Implemented (awaiting QA)
- **Track / slice:** v1_scaffold / S3 (Tier 1 - implementation)
- **Date:** 2026-08-16
- **Model:** `claude-opus-5-thinking-high` (**waiver** - see below)
- **Depends:** L1 Resolved - Implemented
- **Paths touched:** `games/warhammer_40k_11e/rules/`, `games/warhammer_40k_11e/setup/`, `docs/handoffs/v1_scaffold/`
- **`KB/` untouched:** YES
- **`raw/` untouched:** YES
- **Commit:** none by this slice

---

## Model waiver

| Field | Value |
|-------|-------|
| **Locked model** (per [`track_in.md`](../track_in.md), Implementer - content) | `claude-sonnet-5-thinking-high` |
| **Availability** | **Blocked at dispatch** |
| **Model actually used** | `claude-opus-5-thinking-high` |
| **Basis** | Same-family substitute (Claude, thinking-high tier) |
| **Authorized by** | Coordinator, at dispatch |

This is the **fourth waiver on this track**, and the second on `claude-sonnet-5-thinking-high`. Combined with the two Librarian waivers, **every non-`composer` slice so far has run on `claude-opus-5-thinking-high`.** The locked matrix now describes a configuration that has never once been dispatched. Recommend the Coordinator either revise the matrix to match reality or accept that S4 and S5 will waive identically. Cross-family QA separation still holds - `gpt-5.6-sol-medium` is a different family.

---

## The headline: the rules documents were finally opened

L1's parting note was that the largest gap in this project was **unread sources**, and that opening `raw/pointers/rules_core.md` was S3's highest-value first action. That happened. This slice read, in full:

| Source | Version / date | Pages |
|--------|---------------|-------|
| `eng_01-06_warhammer40k_new40k_core_rules.pdf` | Core Rules | 88 |
| `eng_22-07_warhammer_40,000_universal_rules_updates.pdf` | Version 1.0, legal from 22 July 2026 | 1 |
| `eng_22-07_warhammer_40,000_event_companion-...pdf` | Version 1.1 | 93 |
| `eng_22-07_warhammer_40,000_faction_pack_necrons.pdf` | Version 1.1, legal from 22 July 2026 | 57 |
| `eng_22-07_warhammer_40,000_faction_pack_space_marines.pdf` | Version 1.1 | (contents and detachment rules only) |
| `Warhammer 40,000_ Munitorum Field Manual.pdf` | v1.2, printed from the MFM site 13 Aug 2026 | 7 |
| `11th - Terrain Footprints - A4 Scale - *.pdf` | 6 packs | image-only; confirmed as printable footprints |
| Wahapedia, Necrons faction page | retrieved 2026-08-16 | - |

Extraction was done into the system temp directory using PyMuPDF. **No PDF, image, or extracted dump was written into the repository.** The A4 terrain packs and the footprints booklet are image-only and yielded nothing but their copyright line, which is what confirmed they are printable footprint sheets rather than rules text.

**Consequence for the KB's trust model:** L1 recorded 0 `verified` game terms because no rules document had been read. That is no longer true of shipping content - the new `Keyword_Glossary.md` carries 80-plus terms sourced directly from the 11th Edition documents. `KB/glossary.md` has **not** been updated to match, because S3 does not write `KB/`. That reconciliation is the single most valuable thing L2 can do.

---

## Files created (6)

| Path | What it is |
|------|-----------|
| `games/warhammer_40k_11e/rules/Overview.md` | What a game is, the battle-round frame, VP scoring caps, army structure, battle sizes, what you need on the table, a realistic first game against the actual collection |
| `games/warhammer_40k_11e/rules/Turn_Structure.md` | Checklist for one player turn: Start of Turn, five phases, End of Turn, with move types, shooting types, and the fight sequence, plus a common-mistakes table |
| `games/warhammer_40k_11e/rules/Key_Concepts.md` | Datasheet anatomy, the four-step attack sequence, allocation groups, mortal wounds and hazard rolls, Objective Control, battle-shock, attached units, CP and stratagems |
| `games/warhammer_40k_11e/rules/Keyword_Glossary.md` | Six required categories plus faction pointers and a conflicts table. Every entry carries a status |
| `games/warhammer_40k_11e/setup/Board_Setup.md` | 44" x 60" battlefield, the 14-step pre-game sequence, deployment zones and territory, objective types, strategic reserves, a printable checklist, learning-game shortcuts |
| `games/warhammer_40k_11e/setup/Terrain_Basics.md` | Terrain areas vs features, the three categories, the four visibility rules, terrain and movement, how much terrain is enough, A4 footprint pack pointers |

## Files modified (3)

| Path | Change |
|------|--------|
| `games/warhammer_40k_11e/rules/README.md` | S2 stub replaced with a real index and a confidence note (v2.0) |
| `games/warhammer_40k_11e/setup/README.md` | S2 stub replaced with a real index and terrain pointer section (v2.0) |
| `docs/handoffs/v1_scaffold/track_in.md` | S3 row, waiver row, and defect-table note |

Plus this report and `S3_brief.md`.

---

## Findings

### Finding 1 - the owner's points values are stale, most of them badly

Cross-checked the eight points figures L1 classified as "named, not verified" against the owned **Munitorum Field Manual v1.2**. Six of eight are wrong.

| Unit | Owner's notes | MFM v1.2 | Delta |
|------|--------------|----------|-------|
| Necron Warriors (10) | 100 | **80** | -20 |
| Immortals (5) | 75 | **70** | -5 |
| Canoptek Scarab Swarms (3) | 40 | **40** | matches |
| Canoptek Wraiths (3) | 125 | **95** (first unit) | -30 |
| Canoptek Doomstalker | 145 | **140** | -5 |
| Illuminor Szeras | 175 | **175** | matches |
| Lychguard (5) | 170 | **80** | -90 |
| Plasmancer | 65 | **55** | -10 |

The Lychguard figure looks like it was recorded against a 10-model unit (160 in v1.2) and then some. **Every list in `raw/Necron_Lists.md` and everything derived from it needs re-costing.** S3 did not touch those documents - they belong to S4 and the Librarian.

Two useful side-effects of the same check:

- **The squad-merging assumptions are legal.** MFM v1.2 lists 20-model Warriors (190), 10-model Immortals (140), and 6-model Wraiths (220), so L1's open question is answered yes.
- **Wraiths cost more as a second unit** (115 / 240). Several Necron datasheets now carry first-unit and subsequent-unit pricing, which no repo document currently accounts for.

### Finding 2 - the Cryptek Conclave detachment rule is not called Scientific Schemes

The owned **Necrons Faction Pack v1.1** names the Cryptek Conclave detachment rule **Technosorcerous Augmentations** (Cryptek ranged weapons gain `[ASSAULT]`, and each Shooting phase a Cryptek unit selects one additional weapon ability from a short list). "Scientific Schemes" appears **nowhere** in that pack, and **nowhere** on the Wahapedia Necrons page retrieved 2026-08-16.

`KB/glossary.md` and `KB/detachments/cryptek_conclave.md` both carry "Scientific Schemes" as `draft`, sourced from the owner's notes. This is recorded in the shipping glossary's conflicts table and flagged here. **It was not silently corrected in `KB/`** - per [`AGENTS.md`](../../../../AGENTS.md) Sec 13, a source contradicting the KB gets flagged, not quietly rewritten, and S3 does not own `KB/` regardless.

### Finding 3 - Power Matrix is now fully verified, and it is a territory rule, not a re-roll rule

L1 resolved the system attribution and left the wording open. Both are now closed. Confirmed identically in the owned faction pack FAQ and on Wahapedia (2026-08-16):

- Your **deployment zone** is always within your army's Power Matrix.
- At the start of any phase, if you control at least half the objective markers in **No Man's Land**, that region joins your Matrix for the phase. The same applies to your **opponent's deployment zone**.
- Cryptek and Canoptek units re-roll hit rolls of 1 **anywhere**; wholly inside the Matrix they re-roll the hit roll outright.

The KB's paraphrase ("hit re-rolls within controlled territory") is directionally right but understates it: the rule is primarily a **definition of territory** that other Canoptek Court rules also key off. Upgraded to `verified` in the shipping glossary.

### Finding 4 - real 11th Edition changes that will trip anyone who learned 10th

These are in the teaching content, and matter for every later slice:

| Change | Detail |
|--------|--------|
| **Cover no longer helps your save** | Benefit of cover worsens the attacking weapon's **Ballistic Skill by 1** |
| **`[PISTOL]` is being replaced** | `[PISTOL]` and `[CLOSE-QUARTERS]` are functionally identical; the Core Rules state Pistol is superseded as the edition progresses |
| **The Hidden rule** | Infantry-type models in a terrain area containing Dense terrain, that have not shot this turn or last, are invisible beyond a **15" detection range** |
| **Terrain categories** | Exposed / Light / Dense, with Obscuring and Solid layered on top |
| **Invulnerable save is a profile characteristic** | `InSv` sits on the statline rather than in ability text |
| **Leadership is a dice result** | Presented as e.g. `7+`, rolled against on 2D6 |
| **`[CLEAVE X]`** | New melee ability - Blast for melee |
| **Support alongside Leader** | A bodyguard unit can normally take one Leader **and** one Support. Necron Crypteks moved from Leader to Support in Faction Pack v1.1 |
| **Overrun fights** | A unit whose target dies mid-phase gets an extra pile-in and can still fight |
| **Consolidation modes** | Ongoing / Engaging / Objective, and the mode is forced by circumstance rather than chosen freely |

### Finding 5 - Wahapedia's `wh40k10ed` URL path serves current 11th Edition content

L1 carried this as an open thread assigned to S3. **Resolved.** The page at `https://wahapedia.ru/wh40k10ed/factions/necrons` (retrieved 2026-08-16) lists the detachments introduced in the owned Faction Pack v1.1 - Starshatter Arsenal, Cryptek Conclave, Cursed Legion, Pantheon of Woe - and reproduces the current Power Matrix wording. The `10ed` path segment is a legacy URL, not a content indicator. Wahapedia is usable for 11th Edition cross-checks; keep recording retrieval dates.

### Finding 6 - battle-size points limits are in none of the owned PDFs

Incursion, Strike Force, and Onslaught are named in the Necrons Faction Pack's battle-size table. The **points limit attached to each is not stated in any document this project owns** - it lives in the mission material and the Warhammer 40,000 app. The commonly cited 1,000 / 2,000 / 3,000 figures are recorded in `Overview.md` as explicitly unverified rather than presented as fact.

### Finding 7 - one unit-ability claim looks conflated

The owner's notes credit **Canoptek Macrocytes** with granting `[IGNORES COVER]`. In the owned faction pack, Macrocytes carry a Harassment Swarm aura and wargear abilities; `[IGNORES COVER]` is one of the options the **Cryptek Conclave detachment rule** offers. Likely two rules run together. Recorded for **S4**, not resolved here.

### Finding 8 - the UTF-16 defect held, and the read path has the same problem

L1's Finding 1 stands, and it is worse than recorded. Markdown written through the agent editor in this environment lands as UTF-16LE - **and so does markdown merely *edited* through it.** A single string replacement into `track_in.md`, a file that was UTF-8 at the time, silently re-encoded the entire file back to UTF-16LE. It did this on every subsequent edit as well, which is why this slice had to convert that one file four separate times.

Two practical consequences for anyone following:

- **Convert last, not first.** A conversion performed before further edits will be undone by those edits.
- **A failed string replacement on a file you know contains the string is an encoding symptom, not a content error.** Byte-check before assuming the file changed under you.

All eleven files this slice wrote or modified were byte-checked as the final action and are UTF-8 without BOM.

New, related observation for QA: the **file-read** path in this environment sometimes mis-detects existing UTF-8 files as UTF-16 and renders them as mojibake - `S2_brief.md`, `S2_implementer.md`, and the S2 `rules/README.md` all did this. The files themselves are fine; `Get-Content -Encoding UTF8` reads them correctly. Anyone reviewing this slice should use `Get-Content -Encoding UTF8` rather than trusting a mangled render, and should not "fix" a file that is already correct.

---

## Copyright compliance

| Check | Result |
|-------|--------|
| GW binaries added to repo | **None.** 0 files matching `*.pdf,*.webp,*.png,*.jpg,*.jpeg` outside `.git` |
| PDF text extracted into the repo | **No.** Extraction went to `%TEMP%` only |
| Verbatim rules text reproduced | **No.** Teaching paraphrase throughout; the longest quoted fragments are keyword names in square brackets, which are unavoidable labels |
| Datasheet statlines reproduced | **No.** `Key_Concepts.md` explains what each characteristic means and states explicitly that statlines are never reproduced here |
| Points values reproduced | Only the eight cross-checked figures, and only inside this report as a defect finding - not in shipping content |
| Local library referenced | Path pointers only, including the A4 terrain packs |

---

## Tier 1 self-check

| # | Criterion | Result | Evidence |
|---|-----------|--------|----------|
| 1 | Six teaching documents created | PASS | `Test-Path` on each; see `S3_brief.md` Tier 1 commands |
| 2 | Both section READMEs index them | PASS | `rules/README.md` and `setup/README.md` at v2.0 |
| 3 | Required glossary categories present | PASS | Movement, Shooting, Melee, Saves/damage, Mission/army, Faction pointers |
| 4 | Every keyword named in the plan is covered | PASS | All 35 named terms present; Pistol covered together with its replacement |
| 5 | Glossary entries carry a status | PASS | every row tagged `verified`, `draft`, or `unverified` |
| 6 | Rules claims have a verification route and retrieval date | PASS | source block in every header; footer repeats the date |
| 7 | Rising Tide header and footer on every `games/**` file | PASS | 8 files |
| 8 | No YAML frontmatter stacked on Rising Tide headers | PASS | no file starts with `---` |
| 9 | Required footer wording present | PASS | "Verify before you play... Munitorum Field Manual and your faction pack", dated 2026-08-16, on all 8 |
| 10 | Teaching paraphrase only | PASS | see Copyright compliance |
| 11 | A4 terrain packs referenced by path only | PASS | `Terrain_Basics.md` and `setup/README.md` |
| 12 | Terms align with `KB/glossary.md` | PASS with 1 flagged conflict | Finding 2 |
| 13 | Deprecated terms not propagated | PASS | Tomb World, "Data Package Detachment", and the Kill Team misattribution all appear only on the do-not-use list |
| 14 | Ownership facts consistent with Preflight | PASS | `Overview.md` repeats the 2026-08-16 inventory and the build-before-play constraint |
| 15 | **`KB/` untouched** | PASS | `git status --porcelain -- KB` empty |
| 16 | **`raw/` untouched** | PASS | `git status --porcelain -- raw` empty |
| 17 | No GW binaries | PASS | 0 matches |
| 18 | All files UTF-8 without BOM | PASS | byte-checked; 0 UTF-16 markdown files repo-wide |
| 19 | No commit, no push | PASS | no git write command issued |
| 20 | Links resolve | PASS | relative paths checked from each file's own directory |

---

## Blockers

None blocking S4 or S5.

Four threads handed on:

| Thread | Status | Owner |
|--------|--------|-------|
| **Necron points re-costing** | **New and material.** Six of eight owner-note figures are wrong; every derived list needs rebuilding | S4 |
| **Cryptek Conclave rule name conflict** | Flagged, not applied. `KB/glossary.md` and `KB/detachments/cryptek_conclave.md` still say "Scientific Schemes" | Librarian (L2) |
| **KB glossary reconciliation** | Shipping content now has 80-plus verified terms; `KB/glossary.md` still records 0 verified game terms | Librarian (L2) |
| **Hierotek Circle photo ID** | Unchanged from Preflight. Still blocks the first playable game | User photos -> S4 |
| **Space Marine collection audit** | Unchanged. Still blocks S5 | User -> S5 prep |

Closed by this slice: the Wahapedia URL-path thread (Finding 5), the "have the owned PDFs been superseded?" thread (all three 22-07 documents are Version 1.0/1.1 legal from 22 July 2026, and the MFM copy is v1.2 dated 13 August 2026 - current as of this slice), and the Power Matrix wording thread (Finding 3).

---

## Inherited documentation (paste-ready for the S4 brief)

> **Read before starting:**
> - [`games/warhammer_40k_11e/rules/Keyword_Glossary.md`](../../../../games/warhammer_40k_11e/rules/Keyword_Glossary.md) - the shared vocabulary. Use these exact terms.
> - [`games/warhammer_40k_11e/rules/Key_Concepts.md`](../../../../games/warhammer_40k_11e/rules/Key_Concepts.md) - the attack sequence and Objective Control, so unit content does not re-explain them.
> - [`KB/analyses/inherited_docs_for_S3.md`](../../../../KB/analyses/inherited_docs_for_S3.md) - still the best map of what is and is not verified.
>
> **What is now verified fact:** the core rules mechanics, terrain and cover, the pre-game sequence, the 44" x 60" event battlefield, the Reanimation Protocols army rule (end of your Command phase, heal D3 wounds), and the Power Matrix detachment rule in full.
>
> **What S4 must fix before writing lists:** **every points value in `raw/Necron_Lists.md` is suspect.** Re-cost against the owned Munitorum Field Manual v1.2 - see Finding 1 in `S3_implementer.md`. Note that several Necron datasheets now price a second unit higher than the first.
>
> **What S4 must not repeat:** "Scientific Schemes" as the Cryptek Conclave detachment rule (Finding 2), and the claim that Canoptek Macrocytes grant `[IGNORES COVER]` (Finding 7).
>
> **Conventions:** `games/**` uses Rising Tide headers and footers, never YAML frontmatter. Teaching paraphrase only; no GW binaries; path pointers to `C:\Personal\40K`. Never write `raw/` or `KB/`. Never commit or push. **Byte-check your markdown for UTF-16 as your final action** - editing an existing UTF-8 file re-encodes it, so converting early is wasted work (Finding 8). Read existing files with `Get-Content -Encoding UTF8` rather than trusting a mangled render.

---

## Next

**S4** - Necron starter content and the laminate guide, beginning with a points re-cost. **S5** - Space Marine Oath of Moment and Gladius Task Force. **L2** - reconcile `KB/glossary.md` against the now-verified shipping glossary, and resolve the Cryptek Conclave conflict.
