<!--
FILE: docs/handoffs/warcode_kickstarter_refresh/qa/Q2_lore_qa.md
VERSION: v0.2 (2026-09-24)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (independent Stage 6 lore QA)

DOCUMENT_TYPE: QA Report
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: The Warcode
TRACK: warcode_kickstarter_refresh

SOURCES:
  - AGENTS.md Sec 10
  - docs/handoffs/warcode_kickstarter_refresh/research/R2_lore_intelligence.md
  - docs/handoffs/warcode_kickstarter_refresh/impact_matrix.md
  - raw/the_warcode/lorebook_tactical_doctrine_field_edition_extract.txt
  - games/the_warcode/lore/**
  - games/the_warcode/factions/{dominium,mdr,protagen_marines,ulfari}/README.md
  - KB/sources/warcode_tactical_doctrine_field_edition.md and related faction/glossary pages

PURPOSE:
  Independent Stage 6 lore QA. Findings only; no implementation edits.

UPDATE_TRIGGER:
  After a later lorebook/shipping change invalidates the recheck.
-->

# Q2 — Stage 6 lore QA

- **Track:** `warcode_kickstarter_refresh`
- **Stage:** 6 (lore)
- **Date:** 2026-09-24
- **First-pass status:** FAIL
- **Recheck status:** **PASS**
- **Git:** not run
- **Implementation files:** not edited (this report only)

Checked against R2, the coordinator impact matrix, lorebook extract (PDF pages, not printed folios), shipping lore spine, four faction overviews, and related KB pages. Core first-contact, Huoxing/Mars, Cassini overlap, Burning arithmetic, Custodia-as-formation, Ulfari-motive, order-vs-completion, mechanics-firewall, and KB-paraphrase locks hold. Source-voice mixing and a few citation gaps fail the R2 evidence hierarchy.

## Exit criteria

| # | Criterion | Result | Evidence |
|---|-----------|--------|----------|
| 1 | Lore citations use lorebook filename convention, PDF page (not printed folio), and locatable section/heading | **FAIL** | PDF-page convention is followed and sampled pages match the extract. Custodia litany is asserted without a p.25 cite. First-contact heading strings are inconsistent (full Chancellery title vs shortened). Shipping uses dotted section IDs (`3.1`) while the PDF uses hyphenated IDs (`3-1`); this matches R2, so it is noted, not independently failed. |
| 2 | Academy vs faction-authored vs hostile-source vs project interpretation kept distinct | **FAIL** | Methodology ladder and most faction labels are correct. Protagen academy-frame paragraph imports MDR “confederation” language and cites Nakamura pp.20–21 as academy. Theatre operational reading attributes Ulfari “extra-system presence” to academy geography. |
| 3 | Calendar and five-epoch timeline consistent with PDF p.5 / Section 3 | **PASS** | 28h / 39d / 12 months / 468d year; Year 0 = Dominium appearance; Foundation 0–238, Burning 238–380, Golden Age 380–1648, Blackout 1648–2026, Arrival 2026. Transition-year caveat present for 238 and 380. |
| 4 | Burning arithmetic warning present; 86-year figure not silently “corrected” | **PASS** | `Historical_Timeline.md` states 9+56+86=151 vs 142-year epoch, and heading ranges 238–247 / 247–303 / 303–380 → 9+56+77=142. Extract PDF p.8 confirms the 86-year attrition line. |
| 5 | Huoxing (planet) ≠ Mars (Kirkwood settlement) | **PASS** | Theatre callout; MDR README callout; timeline founding note; KB glossary and [[warcode_mdr]] / lore source page. Extract: Huoxing PDF p.5; Mars congress PDF p.30 encyclopedia extract. |
| 6 | Blackout / Blackout War / Silence War not treated as neutral synonyms | **FAIL** | Blackout (policy/event/epoch) and Blackout War (Meridian Institute monograph, PDF p.20) are correctly split. Silence War is over-narrowed to “Protagen and MDR-aligned” with an “anti-Dominium political frame,” omitting Dominium military usage on PDF p.34 (`The Clone Weapon`). |
| 7 | Cassini overlap: MDR partial control compatible with Protagen moon bases | **PASS** | Theatre and MDR README treat academy p.5 partial control, academy p.25 Protagen bases, and academy p.29 “most stations” as overlapping presence, not exclusive borders. |
| 8 | Custodia Silens is a Dominium formation, not the faction synonym; playability from rulebook | **PASS** | Dominium README and KB [[warcode_dominium]] state the split. Rulebook extract PDF p.39 opens `TEAM LIST` / `CUSTODIA SILENS` (continues p.40). Lorebook litany is p.25; Erebus-7 deployment order is p.37. |
| 9 | First-contact conflict preserved; marketing station-destruction not taught as fact | **PASS** | Unqualified hook removed. Timeline, Ulfari README, methodology, impact-matrix handling, and KB all present dated marketing context vs non-hostile Erebus-7 carrier record. Erebus-7 is called a carrier/vessel, not a station. |
| 10 | Orders not treated as completed operations | **PASS** | Shipping and KB repeat that the file records orders/plans, not confirmed execution, station destruction, initiator of later clashes, or fabricated-later-violence. |
| 11 | No invented Ulfari political objective, native name origin, or responsibility for starting hostilities | **PASS** | Explicit source gap; hostile combat profile labeled as Dominium briefing after the hostility order (PDF p.38). Ulfari README flags unit-name origin as project interpretation. |
| 12 | Mechanics firewall: lorebook is narrative only; AP/profiles/abilities from v0.8.9-F | **PASS** | Lore README, Source_Methodology, and all four faction lore sections route play to the current rulebook. Tactical Application cite PDF p.40 Section 8 matches extract. |
| 13 | KB remains teaching paraphrase (no lorebook block quotes / profile dumps) | **PASS** | [[warcode_tactical_doctrine_field_edition]], four faction pages, glossary warnings, and pre-launch source page paraphrase the conflict. No fenced lorebook excerpts found under `KB/**` Warcode pages. |
| 14 | GW proper-noun ban in `games/the_warcode/**` | **PASS** | Independent scan of that tree for `Kill Team`, `Warhammer`, `40,000`, `40K`, `40k` returned no hits. Station-destruction language appears only as the rejected historical claim. |
| 15 | Layer contract for this QA pass | **PASS** | This QA wrote only this report. Did not write `raw/`, `KB/`, or shipping implementation files. Did not run git. |

## What already meets the lock

- Academy dossier frame and “how to read” box in `Source_Methodology.md`.
- Inward-to-outward theatre route; Kepler/Hydron left unspecified; no invented moon map.
- Year-1689 MDR founding attributed to the Free Systems Encyclopedia extract, not academy connective prose.
- Year-2001 `Freedom to Leave` flagged as Blackout-epoch retrospective (PDF p.17).
- Sed Festival / mind-control non-canon; Dominium origin unknown; Martin/Purification attributed.
- Impact-matrix first-contact resolution is implemented in shipping and paraphrased in KB.

## FAIL findings (exact fixes)

### Q2-1 — Protagen academy frame mixes MDR testimony and a named monograph

**File:** `games/the_warcode/factions/protagen_marines/README.md` (Lore and doctrine, academy-frame paragraph)

**Problem:** The academy connective on PDF p.25 says Protagen “became a **state** by uniting the stations of the Abyron Belt.” “Confederation of stations” is Captain Tomas Ng (MDR, PDF p.26). PDF pp.20–21 “corporation / opening days of the Blackout War” sit inside Dr. Stefan Nakamura’s Meridian Institute monograph, not academy Section 5.

**Fix:**

1. In the **Academy frame** sentence, write “became a state by uniting Abyron Belt stations” (or close paraphrase of p.25 only).
2. Keep “confederation / collective security” only in the already attributed **Internal tension** paragraph (Ng p.26).
3. Cite academy Protagen facts to **PDF p.25 — Section 5** (guerrilla depth and Cassini bases are there). If Nakamura is kept, label it named scholarship: PDF p.20 — Section 3.6, “The Blackout War: From Insurrection to Equilibrium.”

### Q2-2 — Theatre operational reading mislabels Ulfari as academy geography

**File:** `games/the_warcode/lore/Theatre_of_Operations.md` (Operational reading)

**Problem:** The Ulfari bullet (“confirmed extra-system presence”) is closed as “project synthesis from the cited academy geography.” Section 2 does not establish Ulfari. Extra-system origin is Dominium internal analysis PDF p.35 part II; academy Epoch 5 (PDF p.5) says “external intelligence.”

**Fix:** Remove the Ulfari bullet from the geography synthesis, **or** give it its own labeled line: academy Epoch 5 (external intelligence, PDF p.5, Section 3.1) plus Dominium internal extra-system assessment (PDF p.35, Section 7), then keep “no mapped territory / no self-authored account” as project interpretation.

### Q2-3 — Silence War speaker set is too narrow

**File:** `games/the_warcode/lore/Historical_Timeline.md` (Three related war terms)

**Problem:** “Protagen and MDR-aligned faction accounts” plus “anti-Dominium political frame” erases that General Dorian Stepanenko (Praefectura Militaris Dominium) also uses “Silence War” on PDF p.34. Morales p.26, Dey p.30, and Zhao p.31 are real; the political-frame claim is over-tight.

**Fix:** Rewrite the Silence War bullet to list speakers/affiliations (Protagen press; Protagen officer; MDR address; Dominium military briefing) and keep only: same long conflict, not a synonym for Blackout/Blackout War, preserve speaker. Optionally mirror that nuance in `KB/glossary.md` (“factional usage” is acceptable if it is not defined as anti-Dominium-only).

### Q2-4 — Custodia litany claim lacks its lorebook cite

**File:** `games/the_warcode/factions/dominium/README.md` (Formation, not faction synonym)

**Problem:** The sentence that the lorebook “identifies its litany and the detachment ordered toward Erebus-7” is followed only by the rulebook roster cite (PDF pp.39–40). Litany is PDF p.25 (`PRE-DEPLOYMENT LITANY, CUSTODIA SILENS`, Sacred Herald). The detachment order is PDF p.37 part V. pp.35–37 are cited on the previous paragraph for the file as a whole, not for the litany.

**Fix:** Split cites: lorebook PDF p.25 — Section 4, Pre-Deployment Litany; lorebook PDF p.37 — Section 7 part V for the Erebus-7 deployment order; rulebook PDF pp.39–40 — “Team List — Custodia Silens” for playability only.

## WARN (do not block if Q2-1–Q2-4 are fixed; still worth doing)

1. **Golden Age academy vs inserts.** Timeline Epoch 3 correctly refuses to pick a winner among prosperity / corporate / oligarchic inserts (PDF pp.17–19) but does not state the academy structural line on PDF p.5 (1,268 years, “longest peaceful period”). Add one academy-labeled sentence so inserts are not the only voice.
2. **First-contact heading string.** Use one locatable title everywhere: `Dominium Security Chancellery — Internal Analysis — First Contact Event` (extract PDF p.35). Shortening to “Internal Analysis — First Contact Event” is findable but inconsistent with the timeline.
3. **Dominium related-pages.** Add `Theatre_of_Operations.md` beside the timeline/methodology links (MDR and Protagen already do).
4. **Section ID punctuation.** If shipping ever diverges from R2, prefer PDF `3-1` / `3-4` over dotted `3.1` / `3.4`.

## Out of scope / not failed here

- Protagen and Ulfari README `REFERENCE_STATUS` still naming v0.8.7-F is a rules-provenance header issue, not a lore-lock break.
- No Games Workshop notice on Warcode lore pages: these pages use the RedMakers unofficial line; GW footer rules apply to GW IP surfaces.
- S3 chose paraphrase-plus-cite instead of scoped verbatim lore quotes; that is allowed, not a defect.
- Uncaptured pre-launch exact wording remains historical marketing context, as locked in the impact matrix.

## Remediation recheck (2026-09-24)

Coordinator remediation was verified in the current workspace. Implementation was not changed by this recheck. Git was not run.

| ID | First pass | Recheck | Evidence |
|---|---|---|---|
| Q2-1 | FAIL | **PASS** | Protagen academy frame now says “became a state by uniting Abyron Belt stations” and cites only PDF p.25 Section 5. Nakamura is a separate **Named scholarship** line (PDF p.20, Blackout War monograph). Internal tension still attributes collective-security/autonomy critique to the MDR critic (p.26) and the Marine-cost admission to the Protagen scientist (p.28). “Confederated” is gone from the academy paragraph. |
| Q2-2 | FAIL | **PASS** | Theatre operational reading now synthesizes only Dominium / MDR / Protagen from academy geography. Ulfari is a separate **Ulfari source boundary**: academy Epoch 5 external intelligence (PDF p.5, Section 3.1) plus Dominium internal extra-system assessment (PDF p.35, Section 7, full Chancellery title, part II). No mapped territory / no self-authored account remains labeled as a source limit. |
| Q2-3 | FAIL | **PASS** | Silence War bullet lists Protagen press, Protagen officer, MDR address, and Dominium military briefing; it no longer claims an anti-Dominium-only frame. Cite expanded to PDF pp.26, 30–31, 34. KB glossary still says “factional usage” without the over-tight political frame (acceptable leftover). |
| Q2-4 | FAIL | **PASS** | Dominium formation paragraph splits cites: lorebook PDF p.25 Section 4, “Pre-Deployment Litany, Custodia Silens”; lorebook PDF p.37 Section 7 part V for the Erebus-7 order; rulebook PDF pp.39–40, “Team List — Custodia Silens” for playability. |

### Exit criteria flipped by the recheck

Criteria 1, 2, and 6 were FAIL on first pass because of Q2-4, Q2-1/Q2-2, and Q2-3. They are **PASS** after remediation.

### Warning improvements

| WARN | Recheck | Notes |
|---|---|---|
| 1 Golden Age academy vs inserts | **Addressed** | Epoch 3 now labels the academy structural line (longest peaceful period, 1,268 years, PDF p.5 Section 3.1) before inserted disagreements (pp.17–19 Section 3.5). |
| 2 First-contact heading string | **Partial** | Timeline and Theatre Ulfari-boundary cites use the full Chancellery title. Short form remains on Theatre Erebus-7, Source_Methodology case study, Dominium internal-contradiction paragraph, and Ulfari README. Still locatable; not a FAIL. |
| 3 Dominium Theatre back-link | **Addressed in lore block** | Shared chronology/source-handling line now includes `Theatre_of_Operations.md`. Footer **Related pages** still omits it. Non-blocking. |
| 4 Section ID punctuation | **Unchanged** | Shipping still follows R2 dotted `3.1` / `3.4` rather than PDF `3-1` / `3-4`. Non-blocking. |

No new FAIL items. Previously PASSed locks (calendar, Burning arithmetic, Huoxing/Mars, Cassini, Custodia-as-formation, first-contact conflict, order-vs-completion, Ulfari motives, mechanics firewall, KB paraphrase-only) remain intact.

## Verdict

**PASS.** Q2-1 through Q2-4 are remediated. Residual heading-string and footer-link inconsistencies are warnings only. Stage 6 lore QA may be treated as resolved.

## Change Log

- v0.2 (2026-09-24): Remediation recheck; Q2-1–Q2-4 PASS; final verdict PASS.
- v0.1 (2026-09-24): Independent Stage 6 lore QA; FAIL on four source-voice/citation items.

## Attribution

- Project: Wargame_Concierge
- Maintainer: Russell Catt

## Rising Tide Notes

- Independent QA; no silent harmonization of source voices.
