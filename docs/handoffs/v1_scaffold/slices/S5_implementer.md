# S5 - Implementer report (Space Marine Oath/Gladius + laminate)

- **Status:** Resolved - Implemented (awaiting QA)
- **Track / slice:** v1_scaffold / S5 (Tier 1 - implementation)
- **Date:** 2026-08-16
- **Model:** `claude-opus-5-thinking-high` (**waiver** - see below)
- **Depends:** S4 Resolved - Implemented
- **Paths touched:** `games/warhammer_40k_11e/armies/space_marines/`, `docs/handoffs/v1_scaffold/`
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

**Sixth waiver on this track, fourth on `claude-sonnet-5-thinking-high`.** S3 asked the Coordinator to either revise the locked matrix or accept the pattern; S4 repeated the request and predicted S5 would waive identically. It did. **Every non-`composer` slice on this track has now run on `claude-opus-5-thinking-high`, and the locked matrix still describes a configuration that has never been used once.** Cross-family QA separation continues to hold - `gpt-5.6-sol-medium` is a different family.

---

## Files created (5)

All under `games/warhammer_40k_11e/armies/space_marines/`.

| Path | What it is |
|------|-----------|
| `Oath_of_Moment.md` | The army rule: start-of-Command-phase selection, re-roll hits plus a conditional +1 to wound, the three "looks illegal but is not" targeting cases from the FAQ, a three-question choosing procedure, and why concentration beats spread |
| `Gladius_Task_Force.md` | Combat Doctrines taught as **three once-per-battle resources**. One section per doctrine - spend it when / typical turn / the trap - plus a tick-box tracker, the six stratagems with the two that bend the once-per-battle limit called out, the owned pack's four Gladius errata, and enhancement costs |
| `Starter_250.md` | **Three** costed paths (Primaris 235, Firstborn 250 exactly, no-character 240) because the collection is unaudited, plus an older-kit swap table and the Legends exclusion list |
| `Starter_500.md` | Each path grown to 500 (500 exact / 495 / 500 exact), a "what the second 250 points buys" capability table, and a purchase summary to be filled in only after the audit |
| `Quick_Reference_Play_Guide.md` | The laminate. Exactly two pages, one `<!-- pagebreak -->`, required footer |

## Files modified (2)

| Path | Change |
|------|--------|
| `games/warhammer_40k_11e/armies/space_marines/Owned_Models_Inventory.md` | v1.0 -> v2.0. **Fill-in structure preserved**; added a one-sitting audit procedure, a Firstborn/Primaris identification test, a Legends-vs-legal table with MFM costs, an "owned but Legends or unidentified" bucket, and a Chapter field |
| `games/warhammer_40k_11e/armies/space_marines/README.md` | v1.0 -> v2.0. Indexes all six documents in three groups; records the three things worth knowing before a first game |

Plus `docs/handoffs/v1_scaffold/track_in.md`, this report, and `S5_brief.md`.

---

## Points: every figure printed by this slice, and where it came from

**Single source of record: `C:\Personal\40K\rules\Warhammer 40,000_ Munitorum Field Manual_Marines.pdf`, v1.2, printed from the MFM site 13 Aug 2026, extracted and read 2026-08-16.** Extraction went to `%TEMP%` with PyMuPDF; nothing was written into the repository.

**This is a different file from the one S4 used.** The Necron lists were costed from `Warhammer 40,000_ Munitorum Field Manual.pdf`; Space Marines have their own 15-page MFM section. Anyone re-checking S5's numbers against the Necron MFM will find nothing.

| Unit / item | MFM Marines v1.2 | Notes |
|-------------|------------------|-------|
| Captain | **80** | Leader |
| Lieutenant | **45** | **Support**, not Leader - changed by the faction pack errata |
| Intercessor Squad (5 / 10) | **80 / 150** | Flat pricing |
| Assault Intercessor Squad (5 / 10) | **75 / 150** | Flat pricing |
| Assault Intercessors with Jump Packs (5) | **85** 1st-2nd, **95** 3rd+ | Tiered |
| Infernus Squad (5 / 10) | **85 / 180** | Flat |
| Hellblaster Squad (5 / 10) | **110 / 220** | Flat |
| Tactical Squad (10) | **140** | Firstborn, still legal |
| Scout Squad (5 / 10) | **65 / 120** 1st-2nd, **75 / 130** 3rd+ | Tiered |
| Devastator Squad (5 / 10) | **120 / 200** | Firstborn, still legal |
| Sternguard Veteran Squad (5) | **100** | |
| Vanguard Veteran Squad w/ Jump Packs (5) | **105** 1st-2nd, **115** 3rd+ | Tiered |
| Terminator Squad (5) / Assault (5) | **160 / 155** | |
| Dreadnought | **135** | Firstborn walker |
| Ballistus / Brutalis Dreadnought | **150** 1st-2nd, **160** 3rd+ | Tiered |
| Redemptor Dreadnought | **195** 1st-2nd, **210** 3rd+ | Tiered |
| Rhino / Razorback | **65 / 85** 1st-3rd, **75 / 95** 4th+ | Tiered |
| Predator Destructor / Annihilator | **140 / 135** 1st-2nd, **150 / 145** 3rd+ | Tiered |
| Land Raider / Crusader / Redeemer | **220 / 220 / 250** 1st-2nd | Tiered |
| Land Speeder / Whirlwind / Vindicator | **105 / 175 / 185** | Whirlwind and Vindicator tiered |
| Drop Pod | **60** 1st-3rd, **70** 4th+ | Tiered |
| Gladius Task Force enhancements | The Honour Vehement **15**, Adept of the Codex **20**, Artificer Armour **20**, Fire Discipline **25** | Detachment tagged `3DP PRIORITY ASSETS` |

**Every list total in the shipped documents was computed from this column.** The three 250-point paths total 235 / 250 / 240 and the three 500-point paths total 500 / 495 / 500.

---

## Rules sources read

| Source | Version / date | Used for |
|--------|---------------|----------|
| `Warhammer 40,000_ Munitorum Field Manual_Marines.pdf` | v1.2, printed 13 Aug 2026 | All points; detachment tags; Leader / Support attachment lists; enhancement costs |
| `eng_22-07_warhammer_40,000_faction_pack_space_marines.pdf` | Version 1.1, legal from 22 July 2026 | Oath of Moment replacement wording; Gladius errata; FAQs; the full Legends datasheet list; Combat Doctrine wording via the Blade of Ultramar detachment |
| `eng_01-06_warhammer40k_new40k_core_rules.pdf` | Core Rules | Leader / Support attachment rules; attached-unit ability inheritance |
| `eng_22-07_warhammer_40,000_event_companion-...pdf` | Version 1.1 | Searched for Detachment Point and enhancement-limit rules - **not present** |
| 40k.app, Gladius Task Force page | retrieved 2026-08-16 | Full Gladius stratagem and enhancement text - **not** in the owned faction pack, which carries only that detachment's errata |
| New Recruit 11e wiki, Gladius entry | retrieved 2026-08-16 | Independent cross-check of the detachment rule wording |

---

## Findings

### Finding 1 - the owned pack rewrites Oath of Moment, and adds a condition nothing in this repo recorded

The faction pack's Rules Updates section replaces the army rule wholesale. The re-roll-hits half is what everyone knows. The second half is not: **+1 to the Wound roll applies only if you are using a Codex: Space Marines Detachment *and* your army contains no Blood Angels, Dark Angels, Deathwatch or Space Wolves units** (including units from those factions' own MFM sections).

This is a list-building trap with real teeth for this specific collection. The son's Chapter is unknown, and a mixed shelf of marines is the normal way a first collection looks. One Death Company model downgrades the army rule for the whole game. It is now the headline caveat in `Oath_of_Moment.md`, a numbered item in the faction README, and a `(fill in)` field in the inventory worksheet.

The pack's FAQ also confirms three things that look wrong at the table and are not: the oath target may be **embarked in a transport**, may be **in Reserves**, and needs no line of sight. And it defines a Codex: Space Marines Detachment as every detachment in the Codex plus every detachment in the Faction Pack - so Gladius qualifies.

### Finding 2 - Gladius is not in the owned faction pack, and the workaround is sound

Exactly the situation S4 hit with Canoptek Court. The Space Marines Faction Pack v1.1 prints **new** detachments in full (Vengeful Hosts, Fulguris Task Force, Librarius Conclave, Subversion Assets, Armoured Speartip, Headhunter Task Force, Ceramite Sentinels, Blade of Ultramar, Hammer of Avernii and others) and gives Gladius Task Force only a four-item errata list.

Two independent public 11e references were used for the full text, and they agree with each other. More usefully, the pack itself provides an **internal** cross-check: the **Blade of Ultramar** detachment is printed in full and its Mastered Doctrines rule uses the three Combat Doctrines verbatim. The doctrine effects in `Gladius_Task_Force.md` are therefore confirmed from the owner's own PDF, not only from the web:

- Devastator - eligible to shoot in a turn it Advanced
- Tactical - eligible to shoot and declare a charge in a turn it Fell Back
- Assault - eligible to declare a charge in a turn it Advanced

Where the owned pack changes something, the owned pack wins, and those four changes are printed in their own section of the guide: Storm of Fire's target clause, Squad Tactics dropping 9" to 8", the Fire Discipline enhancement rewritten, and Armour of Contempt reworded across seven detachments.

### Finding 3 - `DP` is still unexplained, now confirmed from a second faction's angle

S4 traced "Data Package Detachment" to the MFM's `3DP` tag and could not find an expansion. S5 searched the Space Marines MFM, the Space Marines faction pack, the Core Rules and the Event Companion. **The string does not appear outside the MFM detachment table in any document this project owns.** Neither does any rule stating how many enhancements a detachment may take.

Both guides now say so plainly and route the reader to the Warhammer 40,000 app for army construction, matching the stance S3 and S4 took. Two slices, two factions, same gap - this is a genuine hole in the owned library, not an oversight.

### Finding 4 - the Legends list is the most useful thing in the pack for this collection

The faction pack's Legends section is 25 pages of datasheets, and reading it produced the single most practical output of this slice. Kits a father-and-son collection is very likely to contain are **not matched-play legal**: Assault Squad with and without jump packs, Command Squad, Bike Squad, Attack Bike Squad, Scout Bike Squad, Scout Sniper Squad, Land Speeder Tornado and Typhoon, Thunderfire Cannon, Venerable Dreadnought, Mortis Dreadnought, Relic Terminator Squad, and Company Veterans on bikes.

Meanwhile the Firstborn kits that **are** still fully legal - Tactical Squad, Devastator Squad, Scout Squad, plain Dreadnought, Rhino, Razorback, Predator, Land Raider, Land Speeder, Whirlwind, Vindicator, Drop Pod - are enough to build a complete 500-point army with no purchases at all.

The sharpest trap is the old Scouts box: it builds either a **Scout Squad** (legal, 65 for five) or a **Scout Sniper Squad** (Legends). Same sprue, opposite answers. This is now called out in the inventory worksheet and in `Starter_250.md`.

### Finding 5 - Lieutenants are Support units now, and that changed a list

The faction pack errata moves Ancient, Ancient in Terminator Armour, Apothecary, Apothecary Biologis, Bladeguard Ancient, Lieutenant, Lieutenant in Phobos Armour, Lieutenant in Reiver Armour and Wardens of Ultramar from **Leader** to **Support**.

The owned Core Rules confirm a bodyguard unit may take one Leader **and** one Support, and that a support unit attaches on its own without needing a Leader present. That legality check is what makes the Firstborn 250-point list work: Lieutenant (45) + Tactical Squad (140) + Scout Squad (65) = **250 exactly**, with the Lieutenant attached alone. The guide states the rule rather than assuming the reader knows it.

### Finding 6 - nothing was invented about the collection, and that shaped the whole slice

The audit is still not done. Rather than ship one list with imaginary ownership, S5 shipped **three costed paths at each size** covering the plausible outcomes - a modern Primaris box, an older Firstborn shelf, and squads with no HQ. Every row is tagged `TBD`. The inventory worksheet kept every `(fill in)` row it had and gained the identification help that makes the audit a twenty-minute job.

This is the same posture S4 took toward the Hierotek Circle, applied to a bigger unknown: ship the procedure and the costed candidates, flag what is not known, and do not guess.

### Finding 7 - the laminate carries the same two documented deviations as the Necron one

Deliberately identical to S4 so the pair prints and reads as a matched set:

- **The Rising Tide Change Log, Attribution and Rising Tide Notes are carried in the file's header comment**, not as a printed footer, because a printed footer block would push page 2 onto a third page. The required one-line laminate footer *is* printed at the bottom of page 2.
- **ASCII punctuation throughout**, matching every other file in this repo.

The footer text is `Verify vs Munitorum / faction pack - patches happen | 2026-08-16`. The S5 brief specified `Verify vs Munitorum/faction pack | 2026-08-16`; the longer Necron-matching form was used so the two laminates are identical at the foot of the page. If QA prefers the literal brief string it is a one-line change.

### Finding 8 - the UTF-16 defect fired again, exactly as documented

Every file written by this slice was byte-checked as the final action, after all edits were complete, per S3's and S4's guidance. Results are in the self-check table below.

**`docs/handoffs/v1_scaffold/slices/S3_qa.md` was still UTF-16LE at the start of this slice** - S4 flagged it and correctly declined to convert another agent's artifact. S5 made the same call. It remains the Coordinator's or QA's to fix.

---

## Copyright compliance

| Check | Result |
|-------|--------|
| GW binaries added to repo | **None** |
| PDF text extracted into the repo | **No.** Extraction went to `%TEMP%` only |
| Verbatim rules text reproduced | **No.** Teaching paraphrase throughout; the only quoted fragments are bracketed keyword names and rule, stratagem and enhancement names, which are unavoidable labels |
| Datasheet statlines reproduced | **No.** No Move, Toughness, Save, Attacks or weapon profile appears in any shipped file |
| Points values reproduced | Yes, and deliberately - a personal list-building aid needs unit costs. Only units relevant to these lists and to the likely collection, not the full price list |
| Local library referenced | Path pointers only |

---

## Tier 1 self-check

| # | Criterion | Result | Evidence |
|---|-----------|--------|----------|
| 1 | Six documents present in the faction folder | PASS | `Test-Path` on each; see `S5_brief.md` |
| 2 | `armies/space_marines/README.md` indexes all of them | PASS | v2.0, three grouped tables |
| 3 | Army rule guide is paraphrase with a faction-pack pointer | PASS | `Oath_of_Moment.md` header and body |
| 4 | Oath purity condition taught, not omitted | PASS | Own section, plus README item 1 and an inventory field |
| 5 | Combat Doctrines taught as spend-decisions | PASS | One section per doctrine: spend it when / typical turn / the trap |
| 6 | Once-per-battle reminders present | PASS | Tick-box tracker in the guide and on laminate page 1 |
| 7 | Inventory worksheet keeps fill-in structure | PASS | Four `(fill in)` rows plus a `(fill in)` Chapter field retained |
| 8 | No ownership invented anywhere | PASS | Every list row tagged `TBD`; README collection status reads "Unknown" |
| 9 | Starter lists marked provisional | PASS | `REFERENCE_STATUS` on both, plus a dedicated section at the top of each |
| 10 | Older-kit / Firstborn swap notes present | PASS | Swap table plus Legends exclusion list in `Starter_250.md`; fuller table in the inventory |
| 11 | Every printed points value traced to MFM Marines v1.2 | PASS | points table above |
| 12 | List arithmetic correct | PASS | 235 / 250 / 240 and 500 / 495 / 500, recomputed from the MFM column |
| 13 | Laminate is exactly two pages | PASS | one `<!-- pagebreak -->`; page 1 and page 2 headed explicitly |
| 14 | Laminate page 1 content complete | PASS | phases, Oath cheat, doctrine cheat, 6-line combat sequence |
| 15 | Laminate page 2 content complete | PASS | starter snapshot, 8 do/don't pairs, keyword strip, pre-game and end-turn checklists |
| 16 | Laminate footer present and dated | PASS | Necron-matching variant - Finding 7 |
| 17 | No shopping, lore, or datasheet statlines in the laminate | PASS | purchase content lives in `Starter_500.md` only |
| 18 | Rising Tide header and footer on `games/**` files | PASS with 1 documented deviation | Finding 7 |
| 19 | No YAML frontmatter stacked on Rising Tide headers | PASS | no file starts with `---` |
| 20 | Terminology matches `Keyword_Glossary.md` | PASS | keyword strip cross-checked entry by entry; Leader and Support added |
| 21 | **`KB/` untouched** | PASS | `git status --porcelain -- KB` empty |
| 22 | **`raw/` untouched** | PASS | `git status --porcelain -- raw` empty |
| 23 | No GW binaries | PASS | 0 matches |
| 24 | All files UTF-8 without BOM | PASS | byte-checked as the final action |
| 25 | No commit, no push | PASS | no git write command issued |
| 26 | Links resolve | PASS | relative paths checked from `armies/space_marines/` |

---

## Blockers

None blocking S6.

| Thread | Status | Owner |
|--------|--------|-------|
| **Space Marine collection audit** | **Still open, and now the only thing between the son and a legal list.** The worksheet, the identification test, the Legends table and three costed paths at each size are shipped and waiting. Twenty minutes of work | User |
| **Chapter identity** | **New, and it has rules consequences.** If the collection mixes in Blood Angels, Dark Angels, Deathwatch or Space Wolves, the army rule loses its +1 to Wound. Needs recording during the audit | User |
| **`KB/` reconciliation** | Wider after this slice. `KB/concepts/oath_of_moment.md` is `unverified` and missing the purity condition; `KB/detachments/gladius_task_force.md` predates any verified doctrine text; `Keyword_Glossary.md` still carries Oath of Moment as `draft` and Gladius Task Force as `unverified`, both now upgradeable | L2 |
| **Detachment Points and enhancement limits** | Undefined in every owned PDF, now confirmed across two factions | Coordinator - consider sourcing the matched-play army construction rules |
| **`S3_qa.md` still UTF-16LE** | Unchanged since S4 flagged it. Not this slice's artifact to rewrite | QA / Coordinator |
| **Locked model matrix** | Six waivers, all the same substitution | Coordinator |

Closed by this slice: the Oath of Moment `draft` status, the Gladius Task Force `unverified` status, and the absence of any Space Marine list content.

---

## Inherited documentation (paste-ready for the S6 brief)

> **Read before starting:**
> - [`games/warhammer_40k_11e/rules/Keyword_Glossary.md`](../../../../games/warhammer_40k_11e/rules/Keyword_Glossary.md) - shared vocabulary. Use these exact terms.
> - [`games/warhammer_40k_11e/armies/space_marines/`](../../../../games/warhammer_40k_11e/armies/space_marines/) and [`../necrons/`](../../../../games/warhammer_40k_11e/armies/necrons/) - S4 and S5 shipped a matched pair. Unit research should serve the units these lists actually name.
>
> **Units S5's lists depend on, in priority order:** Intercessor Squad, Assault Intercessor Squad, Captain, Lieutenant, Hellblaster Squad, Infernus Squad, Tactical Squad, Scout Squad, Dreadnought, Ballistus Dreadnought, Rhino.
>
> **Two Space Marine facts that will bite unit research:** several datasheets price the **second or third copy** of a unit higher than the first, and a large number of older kits are **Legends** and have no matched-play datasheet at all. Check both before writing a unit page.
>
> **Sources:** Space Marines have a **separate** Munitorum Field Manual file - `Warhammer 40,000_ Munitorum Field Manual_Marines.pdf`. The faction pack prints only *new* detachments in full; anything from the Codex appears solely as errata, so full detachment text needs a public 11e reference reconciled against the pack's Rules Updates section.
>
> **Conventions:** `games/**` uses Rising Tide headers and footers, never YAML frontmatter. ASCII punctuation. Teaching paraphrase only; no statlines; no GW binaries; path pointers to `C:\Personal\40K`. Never write `raw/` or `KB/`. Never commit or push. **Byte-check your markdown for UTF-16 as your final action** - editing re-encodes, so converting early is wasted work. Read existing files with `Get-Content -Encoding UTF8` rather than trusting a mangled render.
>
> **Ownership blocker to expect:** the Space Marine collection is still unaudited and the Hierotek Circle is still unidentified. Neither has moved since Preflight. Write unit research that is useful regardless of which way those land.

---

## Next

**S6** - unit research for the units these two factions' lists name. **L2** - reconcile `KB/` against the corrections S3, S4 and S5 shipped, including the Oath of Moment purity condition and the two glossary confidence upgrades. **User** - the collection audit and the Chapter question.
