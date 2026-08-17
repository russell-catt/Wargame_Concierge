# S4 - Implementer report (Necron starters + laminate guide)

- **Status:** Resolved - Implemented (awaiting QA)
- **Track / slice:** v1_scaffold / S4 (Tier 1 - implementation)
- **Date:** 2026-08-16
- **Model:** `claude-opus-5-thinking-high` (**waiver** - see below)
- **Depends:** S3 Resolved - Implemented
- **Paths touched:** `games/warhammer_40k_11e/armies/necrons/`, `docs/handoffs/v1_scaffold/`
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

**Fifth waiver on this track, third on `claude-sonnet-5-thinking-high`.** S3 predicted this exact outcome and recommended the Coordinator either revise the locked matrix or accept the pattern. Neither happened, and the pattern repeated. Every non-`composer` slice on this track has now run on `claude-opus-5-thinking-high`. Cross-family QA separation still holds - `gpt-5.6-sol-medium` is a different family.

---

## Files created (6)

All under `games/warhammer_40k_11e/armies/necrons/`.

| Path | What it is |
|------|-----------|
| `Reanimation_Protocols.md` | The army rule: end of your Command phase, D3 wounds, heal-before-rebuild ordering, what it will not do, the four habits it should change, and the five things that amplify it |
| `Canoptek_Court.md` | Power Matrix taught as a **territory definition first** and a dice effect second; per-phase re-check; wholly-within requirement; who gets nothing from it; enhancements with MFM costs; honest "not first, on this collection" recommendation |
| `Cryptek_Conclave.md` | **Technosorcerous Augmentations** with the name correction stated up front; the attached-unit keyword trick; a beginner's menu-choice table; enhancements with MFM costs; the Macrocytes correction |
| `Starter_250.md` | Two blockers stated plainly, a Hierotek Circle photo-ID checklist with candidate datasheets and costs, a 245-point provisional list, and a 190-point zero-purchase variant |
| `Starter_500.md` | Two costed paths - Cryptek Conclave 495 and Canoptek Court 490 - every entry tagged **OWNED**, **PURCHASE**, or `TBD`, plus a purchase-summary table and a cheaper 375-point variant |
| `Quick_Reference_Play_Guide.md` | The laminate. Exactly two pages, one `<!-- pagebreak -->`, required footer |

## Files modified (2)

| Path | Change |
|------|--------|
| `games/warhammer_40k_11e/armies/necrons/README.md` | v1.0 -> v2.0. Indexes all six new documents in three groups, and states the two corrections this slice ships |
| `docs/handoffs/v1_scaffold/track_in.md` | S4 row, waiver row, defect note |

Plus this report and `S4_brief.md`.

---

## Points: every figure printed by this slice, and where it came from

**Single source of record: `C:\Personal\40K\rules\Warhammer 40,000_ Munitorum Field Manual.pdf`, v1.2, printed from the MFM site 13 Aug 2026, extracted and read 2026-08-16.** Extraction went to `%TEMP%` with PyMuPDF; nothing was written into the repository.

| Unit / item | MFM v1.2 | Owner's note in `Necron_Lists.md` | Verdict |
|-------------|----------|-----------------------------------|---------|
| Necron Warriors (10 / 20) | **80 / 190** | 100 | Stale |
| Immortals (5 / 10) | **70 / 140** | 75 | Stale |
| Canoptek Scarab Swarms (3 / 6) | **40 / 80** | 40 | Matches |
| Canoptek Wraiths (3) | **95** first unit, **115** second | 125 | Stale, and the tiering was missing |
| Canoptek Wraiths (6) | **220** first, **240** second | - | Not previously recorded |
| Canoptek Doomstalker | **140** | 145 | Stale |
| Canoptek Macrocytes (5) | **70** | 85 | **Stale - new finding, S3 had not checked this one** |
| Canoptek Tomb Crawlers (2) | **50** | 85 | **Stale - new finding** |
| Cryptek Geomancer | **75** | 75 | Matches |
| Plasmancer | **55** | 65 | Stale |
| Technomancer | **80** first, **90** second | - | Newly recorded |
| Psychomancer / Chronomancer | **55** / **70** first, **80** second | - | Newly recorded |
| Royal Warden | **50** | - | Newly recorded |
| Lychguard (5 / 10) | **80 / 160** | 170 for 5 | **Stale by more than double** |
| Illuminor Szeras | **175** | 175 | Matches |
| Cryptothralls (2) | **60** | - | Newly recorded |
| Deathmarks (5 / 10) | **60 / 120** first-to-second unit | - | Newly recorded |
| Canoptek Court enhancements | Dimensional Sanctum 20, Hyperphasic Fulcrum 15, Autodivinator 15, Metalodermal Tesla Weave 10 | - | Newly recorded |
| Cryptek Conclave enhancements | Gauntlet of Compression 20, Gravitic Bolas 15, Quantum Abacus 15, Atomic Disintegrators 10 | - | Newly recorded |

Two of the eight figures S3 checked matched; this slice checked ten more and found two further stale values (Macrocytes, Tomb Crawlers). **Every list total in the shipped documents was recomputed from the MFM column, not adjusted from the old one.**

**Second-unit pricing is now documented in shipping content.** Wraiths, Technomancer, Chronomancer, Deathmarks, Lokhust Destroyers, Skorpekh Destroyers, Tomb Blades and several others price later units higher. Nothing in the repo accounted for this before.

---

## Rules sources read

| Source | Version / date | Used for |
|--------|---------------|----------|
| `Warhammer 40,000_ Munitorum Field Manual.pdf` | v1.2, printed 13 Aug 2026 | All points; detachment tags; Leader / Support attachment lists |
| `eng_22-07_warhammer_40,000_faction_pack_necrons.pdf` | Version 1.1, legal from 22 July 2026 | Cryptek Conclave detachment in full; Rules Updates; FAQ; Macrocytes and Tomb Crawlers datasheets; reanimation amplifiers |
| `eng_22-07_warhammer_40,000_event_companion-...pdf` | Version 1.1 | Force Disposition / Primary Mission vocabulary; 44" x 60" battlefield; CP cap |
| `eng_01-06_warhammer40k_new40k_core_rules.pdf` | Core Rules | Strategic reserves cap; cross-checks against S3's `Key_Concepts.md` |
| Wahapedia, Necrons faction page | retrieved 2026-08-16 | Reanimation Protocols full wording; Canoptek Court Power Matrix, enhancements and stratagems (**not** in the owned faction pack, which carries only that detachment's errata) |

---

## Findings

### Finding 1 - the Cryptek Conclave rule is confirmed from the owner's own pack, in full

S3 flagged the name. This slice read the whole detachment on page 7 of the owned faction pack v1.1. **Technosorcerous Augmentations** has two effects: Cryptek ranged weapons gain `[ASSAULT]`, and each time a Cryptek unit is selected to shoot it picks one ability from a five-option menu for the phase. "Scientific Schemes" appears nowhere in the pack.

The teaching consequence is bigger than the name. Because an attached Cryptek gives its whole squad the Cryptek keyword, the menu ability lands on **the bodyguard squad's guns**, which is the entire reason the detachment works. That is now the headline of `Cryptek_Conclave.md`.

### Finding 2 - the Macrocytes `[IGNORES COVER]` claim is disproved, not just doubted

S3 Finding 7 suspected two rules had been conflated and handed it to S4. **Confirmed and closed.** The Canoptek Macrocytes datasheet in the owned faction pack v1.1 carries an aura that makes *enemy* units near them less accurate, plus wargear that can improve a nearby Canoptek unit's Weapon Skill or add a wound to a nearby unit's reanimation. No cover-ignoring anywhere. `[IGNORES COVER]` is one of the five options on the Cryptek Conclave menu. The two were run together in the owner's notes. Recorded in `Cryptek_Conclave.md`.

### Finding 3 - "Data Package Detachment" traced to its origin, and it is not a rules term

MFM v1.2 tags each detachment with a number and a mission type - `CANOPTEK COURT 3DP TAKE AND HOLD`, `CRYPTEK CONCLAVE 2DP PRIORITY ASSETS`. That `3DP` is almost certainly where the owner's "3 Data Package Detachment" phrasing came from.

Two halves, with different confidence:

- **The mission-type word is real vocabulary.** Take and Hold, Purge the Foe, Disruption, Reconnaissance and Priority Assets are the Primary Missions selected via Force Disposition cards in the Event Companion v1.1.
- **What `DP` expands to is not stated in any document this project owns.** It appears only in the MFM detachment table. The string "DP" does not occur in the Core Rules, the Event Companion, the faction pack, or the Wahapedia Necrons page.

Both detachment guides say this plainly rather than inventing an expansion. The glossary's existing "not a recognised term" ruling on "Data Package Detachment" stands and is now explained.

### Finding 4 - Wahapedia is useful here but is **not** ahead of the owned faction pack

S3 Finding 5 established the `wh40k10ed` URL path serves current content. Refining that, not contradicting it: Wahapedia's own Books table for Necrons lists the Faction Pack as **edition 10, version 1.3, March 2026**, while the owned pack is **Version 1.1, legal from 22 July 2026**. Wahapedia was the only available source for the full Canoptek Court detachment text - the owned faction pack carries only that detachment's *errata* - and its Power Matrix wording matches the owned FAQ exactly. But where the owned pack's Rules Updates section changes something (a Canoptek Court stratagem range dropping from 9" to 8", another's effect reworded, Crypteks moving from Leader to Support), **the owned pack wins**. `Canoptek_Court.md` tells the reader to read their own pack's Rules Updates before a game.

### Finding 5 - Hierotek Circle is still `TBD`, and this slice deliberately did not guess

Still blocked on user photos, exactly as at Preflight and S3. Rather than ship a placeholder or infer box contents, `Starter_250.md` carries a four-step photo-ID procedure and a table of **candidate datasheets to check against**, each already costed from MFM v1.2, so the identification converts into a legal list in minutes rather than another research pass. The table is labelled as lookup targets, not a claim about the box.

It also states the case nobody had written down: some Kill Team operatives have **no 40K datasheet at all**, and those models should be left out of matched play rather than approximated.

### Finding 6 - the laminate has two documented deviations from house convention

Both were judgement calls in service of the "exactly two pages" requirement, and both are reversible:

- **The Rising Tide Change Log, Attribution and Rising Tide Notes are carried in the file's header comment**, not as a printed footer. A printed footer block would have pushed page 2 onto a third page. The required one-line laminate footer *is* printed at the bottom of page 2.
- **The footer uses an ASCII hyphen** - `Verify vs Munitorum / faction pack - patches happen | 2026-08-16` - rather than the em dash in the brief, matching the ASCII-punctuation convention every other file in this repo follows and avoiding another encoding hazard.

If QA prefers the literal brief punctuation or a printed footer block, both are one-line changes.

### Finding 7 - the UTF-16 defect fired again, exactly as S3 documented

Every file written by this slice landed as UTF-16LE and was converted as the final action, after all edits were complete. S3's guidance held: converting early would have been undone. The read path also mis-detected `armies/necrons/README.md` as UTF-16 and rendered it as mojibake when it was valid UTF-8 - `Get-Content -Encoding UTF8` read it correctly. **Anyone reviewing this slice should read files that way rather than "fixing" a file that is already correct.**

`track_in.md` was the worst case: three separate string replacements, three separate re-encodings, three conversions back. The defect fires per edit, not per session.

**One pre-existing UTF-16LE file remains repo-wide: `docs/handoffs/v1_scaffold/slices/S3_qa.md`.** It was written after S3's own final byte-check, so S3's "0 UTF-16 files" attestation was true when made. S4 did **not** convert it - it belongs to the QA agent, and rewriting another slice's artifact is not this slice's call. Flagged for QA or the Coordinator. Every other markdown file in the repo is UTF-8 without BOM.

---

## Copyright compliance

| Check | Result |
|-------|--------|
| GW binaries added to repo | **None** |
| PDF text extracted into the repo | **No.** Extraction went to `%TEMP%` only |
| Verbatim rules text reproduced | **No.** Teaching paraphrase throughout; the only quoted fragments are bracketed keyword names and rule/enhancement names, which are unavoidable labels |
| Datasheet statlines reproduced | **No.** Macrocytes and Tomb Crawlers datasheets were read for Finding 2; no profile numbers were copied into any shipped file |
| Points values reproduced | Yes, and deliberately - a personal list-building aid needs unit costs. Only units relevant to this collection, no full price list |
| Local library referenced | Path pointers only |

---

## Tier 1 self-check

| # | Criterion | Result | Evidence |
|---|-----------|--------|----------|
| 1 | Six documents created | PASS | `Test-Path` on each; see `S4_brief.md` |
| 2 | `armies/necrons/README.md` indexes all six | PASS | v2.0, three grouped tables |
| 3 | Army rule guide is paraphrase with a faction-pack pointer | PASS | `Reanimation_Protocols.md` header and body |
| 4 | Power Matrix taught correctly (territory first, per-phase re-check, wholly-within) | PASS | verified against Wahapedia + owned FAQ |
| 5 | Cryptek Conclave rule named Technosorcerous Augmentations | PASS | correction table at the top of the page |
| 6 | "Scientific Schemes" appears only as a correction | PASS | one occurrence per file, both in do-not-use context |
| 7 | Hierotek Circle flagged `TBD`, not guessed | PASS | `Starter_250.md` checklist |
| 8 | Unassembled models marked build-before-play | PASS | every list table carries an ownership tag |
| 9 | 500-point list tags purchase vs owned | PASS | **OWNED** / **PURCHASE** / `TBD` on every row, plus a summary table |
| 10 | Every printed points value traced to MFM v1.2 | PASS | points table above |
| 11 | Laminate is exactly two pages | PASS | one `<!-- pagebreak -->`; page 1 and page 2 headed explicitly |
| 12 | Laminate page 1 content complete | PASS | phases, army rule cheat, Power Matrix cheat, 6-line combat sequence |
| 13 | Laminate page 2 content complete | PASS | starter snapshot, 7 do/don't pairs, keyword strip, pre-game and end-turn checklists |
| 14 | Laminate footer present and dated | PASS | ASCII-hyphen variant - Finding 6 |
| 15 | No shopping, lore, or datasheet statlines in the laminate | PASS | prices and background live in `Necron_Lists.md` only |
| 16 | Rising Tide header and footer on `games/**` files | PASS with 1 documented deviation | Finding 6 |
| 17 | No YAML frontmatter stacked on Rising Tide headers | PASS | no file starts with `---` |
| 18 | Terminology matches `Keyword_Glossary.md` | PASS | keyword strip cross-checked entry by entry against the S3 glossary |
| 19 | **`KB/` untouched** | PASS | `git status --porcelain -- KB` empty |
| 20 | **`raw/` untouched** | PASS | `git status --porcelain -- raw` empty |
| 21 | No GW binaries | PASS | 0 matches |
| 22 | All files UTF-8 without BOM | PASS | byte-checked as the final action |
| 23 | No commit, no push | PASS | no git write command issued |
| 24 | Links resolve | PASS | relative paths checked from `armies/necrons/` |

---

## Blockers

None blocking S5.

| Thread | Status | Owner |
|--------|--------|-------|
| **Hierotek Circle photo ID** | **Still open, and now the only thing between this collection and a legal 250-point list.** Procedure and costed candidates are shipped and waiting | User photos -> follow-up slice |
| **`KB/` reconciliation** | Wider than S3 recorded. `KB/concepts/reanimation_protocols.md` is still `unverified` and now contradicted by shipping content; `KB/concepts/power_matrix.md` still lists open questions this slice closed; both detachment pages carry stale points and the wrong rule name | L2 |
| **`raw/Necron_Lists.md` and its shipped copy** | Two more stale figures found (Macrocytes, Tomb Crawlers). The shipped copy now carries a "do not cost from this" warning from the README and both starter lists, but the numbers inside it are untouched - `raw/` is immutable and the shipped copy is an import | Coordinator decision |
| **Space Marine collection audit** | Unchanged | User -> S5 prep |
| **Locked model matrix** | Five waivers, all the same substitution | Coordinator |

Closed by this slice: the Necron points re-cost (S3 Finding 1), the Cryptek Conclave rule name for shipping content (S3 Finding 2), and the Macrocytes ability conflation (S3 Finding 7).

---

## Inherited documentation (paste-ready for the S5 brief)

> **Read before starting:**
> - [`games/warhammer_40k_11e/rules/Keyword_Glossary.md`](../../../../games/warhammer_40k_11e/rules/Keyword_Glossary.md) - shared vocabulary. Use these exact terms.
> - [`games/warhammer_40k_11e/armies/necrons/`](../../../../games/warhammer_40k_11e/armies/necrons/) - S4 shipped the shape S5 should mirror: one army-rule guide, one guide per detachment, two starter lists, one two-page laminate, and a README that indexes them.
>
> **The pattern that worked:** teach the detachment rule as *what decision it changes*, not as a restatement. Lead each list with an ownership reality check. Put the correction at the top of the page when older notes are wrong.
>
> **What S5 must do that S4 had to do the hard way:** re-cost **every** points value against the owned Munitorum Field Manual before writing a list - there is a separate `Warhammer 40,000_ Munitorum Field Manual_Marines.pdf` for Space Marines. Check for **first-unit / second-unit pricing**, which several datasheets now use and which no repo document accounted for before this slice.
>
> **Conventions:** `games/**` uses Rising Tide headers and footers, never YAML frontmatter. ASCII punctuation. Teaching paraphrase only; no statlines; no GW binaries; path pointers to `C:\Personal\40K`. Never write `raw/` or `KB/`. Never commit or push. **Byte-check your markdown for UTF-16 as your final action** - editing re-encodes, so converting early is wasted work. Read existing files with `Get-Content -Encoding UTF8` rather than trusting a mangled render.
>
> **Ownership blocker to expect:** the Space Marine collection has never been audited. Do for it what `Starter_250.md` does for the Hierotek Circle - ship the procedure and the costed candidates, flag the unknown, and do not guess.

---

## Next

**S5** - Space Marine Oath of Moment, Gladius Task Force, starter lists, and a matching laminate. **S6** - unit research for the units these lists name. **L2** - reconcile `KB/` against the four corrections this slice and S3 shipped.
