# Q3 QA — Stage 6 campaign / community

- **Track:** `warcode_kickstarter_refresh`
- **Stage:** 6 (campaign/community surface)
- **Date:** 2026-09-24
- **First-pass verdict:** **FAIL** (exact fix list below)
- **Remediation recheck verdict:** **PASS**
- **Git:** not run
- **Implementation files:** not edited (this file only)

Dedicated shipping reviews and the campaign KB source/analysis pages keep the locked chronology, digital-only Kickstarter scope, claim classes, and TTS drift warning. First-pass FAIL rows (stale Gamefound wording on the historical v0.8.7-F source page, stale Stage 4/5 rollup, S4 header/changelog gaps) were remediated; see **Remediation recheck**.

Independent live re-fetch: Gamefound project page, Steam Workshop `3776386741`, Brückenkopf launch article, Tabletop Sentinel roundup, pre-launch site, Substack #166, and YouTube oEmbeds succeeded. Kickstarter project and FAQ pages returned **403 / Cloudflare** this pass; those URLs remain as recorded in R3 (retrieved 2026-09-24). Gamefound **updates #1 and #2** were also Cloudflare-blocked this pass; chronology for 2026-09-15 / 2026-09-17 therefore rests on R3 plus the still-visible final Gamefound project page.

## Result table

| Check | Result |
|-------|--------|
| Layer contract (no `raw/` writes; no `wiki/`; this QA wrote only this file) | PASS |
| UTF-8, no BOM on scoped campaign/planning/KB pages | PASS |
| Warcode GW proper-noun ban under `games/the_warcode/**` | PASS (0 matches) |
| Games Workshop print-footer / `## Games Workshop notice` on Warcode campaign pages | WAIVE (RedMakers unofficial language; GW footer N/A) |
| Print export `_export_pdf_config.json` parses; header has UNOFFICIAL + V.0.8.9-F + 2026-09-24 | PASS |
| Chronology: 2026-09-15 launch → 2026-09-17 cancellation statement → 2026-09-18 platform end / no funds → 2026-09-23 through 2026-10-23 Kickstarter | PASS on review pages, system README, and campaign KB pages; FAIL on `warcode_rulebook_v087f.md` living-web row |
| Kickstarter described as digital-only STL + Print & Play | PASS |
| Physical boxes as deferred publisher intent, not Kickstarter rewards; no date/guarantee | PASS |
| Live Kickstarter totals absent from shipping and KB; present only in timestamped R3 research | PASS |
| Final Gamefound counters labelled as platform display retrieved 2026-09-24 | PASS on postmortem + `warcode_gamefound_campaign_2026_09.md` |
| “Reach” attributed to RedMakers; not treated as proven cause | PASS |
| “Insufficient buzz” attributed to owner testimony only | PASS |
| Influencer/coverage disclosure labels and evidence limits vs R4 | PASS |
| No unsupported momentum or coverage-causation conclusions | PASS |
| TTS Workshop `3776386741` linked; visible v0.8.7 vs PDF v0.8.9-F; no unaudited-equivalence claim | PASS (Steam listing reconfirmed: “Current rules version: 0.8.7”) |
| Living URLs carry retrieval date 2026-09-24 on campaign shipping headers and campaign KB sources | PASS |
| Local Markdown links in scoped campaign/planning/KB files | PASS (campaign files resolve; see notes) |
| Librarian campaign KB pages exist (`warcode_gamefound_campaign_2026_09`, `warcode_kickstarter_relaunch_2026_09`, `warcode_campaign_transition_2026_09`) | PASS |
| Planning / index campaign URLs and Kickstarter window | PASS for facts; FAIL for Stage 4/5 rollup currency |
| S4-touched `Overview.md` / `Proxy_Play_at_Home.md` changelog and headers | FAIL |
| Legacy `Agentic_Rules_and_Marketing_Review.md` not linked from active Warcode shipping reviews | PASS |
| Live Kickstarter page independently re-fetched this QA | FAIL (blocked 403; see notes) |

## Scope read

- `AGENTS.md` Sec 10 (Warcode quote paths, naming ban, paraphrase in KB/docs)
- `docs/handoffs/warcode_kickstarter_refresh/research/R3_campaign_transition.md`
- `docs/handoffs/warcode_kickstarter_refresh/research/R4_community_coverage.md`
- `docs/handoffs/warcode_kickstarter_refresh/impact_matrix.md`
- `games/the_warcode/reviews/Gamefound_Postmortem_2026-09-18.md`
- `games/the_warcode/reviews/Kickstarter_and_Community_2026-09-24.md`
- `games/the_warcode/README.md`, `research/STL_Sources.md`, `guides/Tabletop_Simulator.md`, `guides/Proxy_Play_at_Home.md`, `rules/Overview.md`
- `games/README.md`, root `README.md`, `docs/Project_Planning.md`, `docs/handoffs/README.md`, `track_in.md`
- `KB/sources/warcode_gamefound_campaign_2026_09.md`, `KB/sources/warcode_kickstarter_relaunch_2026_09.md`, `KB/analyses/warcode_campaign_transition_2026_09.md`, plus `warcode_web_prelaunch_2026_08.md` and `warcode_rulebook_v087f.md` living-web rows
- `slices/S4_campaign_implementer.md`, `slices/L1_librarian_sync.md`

## What is already correct

Shipping reviews and the two campaign KB source pages plus the transition analysis preserve:

1. Gamefound launch **2026-09-15**
2. RedMakers cancellation statement **2026-09-17**
3. Gamefound platform end **2026-09-18**, **no funds collected**
4. Digital-only Kickstarter **2026-09-23 through 2026-10-23**

Live Gamefound project page (this QA) still shows cancelled, no funds, end 9/18/2026, and the same final display (63 backers, €7,894, 17.54% of €45,000, 2,800 following). That matches the labelled postmortem snapshot. Physical boxes are not described as Kickstarter rewards. Kickstarter live counters (`99` backers / `CA$8,637` / `538%`) appear only in R3. Coverage on the Kickstarter review uses R4 labels (supplied-preview GMG; independent/unknown newsletter; unknown Brückenkopf and Sentinel; independent-for-visible-post forum; publisher-owned videos/testimonials) and keeps melee-error / preview-build / not-a-Kickstarter-review limits. YouTube oEmbed confirms GMG title `FIRST LOOK! - WARCODE by RedMakers` and the two RedMakers videos.

## Exact fix list

Do not treat the slice **Resolved - Complete** until these are applied (or owner-waived). This QA does not apply them.

1. **`KB/sources/warcode_rulebook_v087f.md`** — In the living-web table (rechecked 2026-09-24), change the Gamefound row from `Campaign (Sep 2026)` to a historical cancelled label consistent with `warcode_gamefound_campaign_2026_09.md` (creator-cancelled; platform ended 2026-09-18; no funds collected). Point current offer to `[[warcode_kickstarter_relaunch_2026_09]]`.

2. **`docs/handoffs/warcode_kickstarter_refresh/track_in.md`** — Rollup still says Stage 4 QA pending and Stage 5 Pending. After L1, Stage 5 is Complete; Stage 4 is Implemented with this Stage 6 QA open. Update Status / Rollup so they do not claim Librarian sync is still pending.

3. **`docs/handoffs/README.md`** — Active-track cell still reads `In Progress — Stage 4 campaign/community implemented`. Update to current stage (Librarian complete; Stage 6 campaign QA FAIL pending the fixes above).

4. **`games/the_warcode/rules/Overview.md`** — HTML header still says `draft, beta v0.8.7-F (2026-08-23)` and the UPDATE_TRIGGER still keys off v0.8.7-F, while the body and Rising Tide note assume v0.8.9-F plus Kickstarter/TTS drift. Align header / UPDATE_TRIGGER / Change Log with v0.8.9-F and the S4 campaign sentence.

5. **`games/the_warcode/guides/Proxy_Play_at_Home.md`** — `REFERENCE_STATUS` is still `draft (2026-08-23)` and the Change Log has no S4 row for the digital-only Kickstarter STL pointer. Add an S4 changelog line and refresh the status date.

## Recommended (not required to flip FAIL)

- On the Gamefound postmortem and/or STL table, one sentence that the **cancelled** Gamefound page may still list mixed digital/physical rewards and pledge UI; those listings are historical, not a live mixed campaign.
- `STL_Sources.md` could name 2026-09-15 and 2026-09-17 as well as 2026-09-18; chronology is already complete on the system README and postmortem.
- Pre-launch site (re-fetched this QA) remains Gamefound-oriented; already flagged in `warcode_web_prelaunch_2026_08.md` open questions.
- `docs/handoffs/README.md` local links `cursor_rules_skills/` and `kb_shipping_backfill/` do not resolve in this workspace. Pre-existing index issue; not a Warcode campaign-fact error.

## Out of scope / not failed here

- AGENTS lore-quote path vs older `docs/Project_Planning.md` quote-exception line that still omits `lore/` (lore-stage residue, not campaign chronology).
- Kickstarter live totals as of this QA (page blocked; correctly omitted from shipping/KB).
- Whether reach or buzz caused cancellation (correctly left unknown).
- Whether the TTS **build** matches v0.8.9-F (listing label only; shipping does not claim equivalence).

## Link check detail

| URL | This QA |
|-----|---------|
| https://gamefound.com/en/projects/redmakers/the-warcode | 200; cancelled; no funds; ended 9/18/2026; counters match R3 |
| https://gamefound.com/en/projects/redmakers/the-warcode/updates/1 | Cloudflare challenge; not independently dated this pass |
| https://gamefound.com/en/projects/redmakers/the-warcode/updates/2 | Cloudflare challenge; not independently dated this pass |
| https://www.kickstarter.com/projects/redmakers/the-warcode-stl-campaign | 403 |
| https://www.kickstarter.com/projects/redmakers/the-warcode-stl-campaign/faqs | 403 |
| https://steamcommunity.com/sharedfiles/filedetails/?id=3776386741 | 200; rules 0.8.7; Kickstarter URL matches shipping |
| https://pre-launch.thewarcode.com/ | 200; still Gamefound-oriented marketing |
| https://www.brueckenkopf-online.com/2026/the-warcode-gamefound-laeuft/ | 200; dated 17.09.2026; “28 Tage” stale as R3/R4 warn |
| https://www.brueckenkopf-online.com/2026/the-warcode-preview-online/ | 200 |
| https://www.tabletopsentinel.com/columns/crowdfund-quest/crowdfund-quest-weekly-19-09-26-new-project-launches-over-the-last-week | 200; lists The Warcode |
| https://rpgwargamenews.substack.com/p/rpg-and-wargame-newsletter-166 | 200 |
| YouTube GMG / trailer / showcase oEmbed | 200; titles match R4 |

Local relative links in the campaign review pages, Warcode README, STL/TTS/proxy/overview, root/games README, Project_Planning, and campaign KB pages resolve. Scoped files decode as UTF-8 with no BOM.

---

## Remediation recheck (2026-09-24)

Coordinator applied the five exact-fix items. This pass re-read those files plus campaign reviews, system README, STL/TTS, and campaign KB pages. Git was not run. Implementation files were not edited.

### Exact-fix items

| # | Required fix | Recheck | Result |
|---|--------------|---------|--------|
| 1 | `KB/sources/warcode_rulebook_v087f.md` historical cancelled Gamefound label + current-offer wikilink | Living-web row is `Historical campaign: creator-cancelled; platform ended 2026-09-18; no funds collected`. Follow-on line points to `[[warcode_gamefound_campaign_2026_09]]` and `[[warcode_kickstarter_relaunch_2026_09]]`. Phrase `Campaign (Sep 2026)` is gone. | **PASS** |
| 2 | `track_in.md` Stage 4/5 no longer pending Librarian | Status: `In Progress — Stage 6 QA remediation`. Stage 4 Complete (QA remediation applied); Stage 5 Resolved — Complete; Stage 6 In Progress — remediation and recheck. | **PASS** |
| 3 | `docs/handoffs/README.md` active-track cell | `In Progress — Stage 6 QA remediation` (no longer Stage 4 campaign/community implemented). | **PASS** |
| 4 | `Overview.md` header / UPDATE_TRIGGER / Change Log vs v0.8.9-F + S4 | `REFERENCE_STATUS: Active — draft, beta v0.8.9-F (2026-09-24)`. UPDATE_TRIGGER keys off v0.8.9-F. Change Log v0.3.1 records Kickstarter/TTS context (S4/QA). Rising Tide still warns Workshop v0.8.7. | **PASS** |
| 5 | `Proxy_Play_at_Home.md` status date + S4 changelog | `REFERENCE_STATUS: Active — draft (2026-09-24)`. Change Log v0.2.1: digital-only Kickstarter STL route (S4). Body still points to `STL_Sources.md`. | **PASS** |

### Previously FAIL rows (now)

| Check | Recheck result |
|-------|----------------|
| Chronology including `warcode_rulebook_v087f.md` living-web row | **PASS** |
| Planning / index Stage 4/5 rollup currency | **PASS** |
| S4-touched Overview / Proxy changelog and headers | **PASS** |
| Live Kickstarter independently re-fetched | **WAIVE** — 403/Cloudflare remains an acceptable documented limitation. Local handling is correct: retrieval-dated URLs, digital-only description, no live totals in shipping/KB, totals only in timestamped R3. |

### Campaign facts still intact

- 2026-09-15 → 2026-09-17 cancellation statement → 2026-09-18 platform end / no funds → 2026-09-23 through 2026-10-23 Kickstarter: present on system README, Gamefound postmortem, Kickstarter review, and `warcode_campaign_transition_2026_09.md`.
- Digital-only STL/PnP; physical boxes deferred intent, not rewards.
- Reach vs owner “insufficient buzz” still separated; no momentum/causation claims.
- TTS item `3776386741` still linked with v0.8.7 listing vs v0.8.9-F PDF.
- Live Kickstarter counters still absent from `games/the_warcode/**` and `KB/**`.
- GW proper-noun ban still 0 matches under `games/the_warcode/**`.
- Campaign living URLs still carry retrieval date 2026-09-24 on shipping headers and campaign KB sources.
- Scoped remediations and campaign files: UTF-8, no BOM. Local Markdown links on those files resolve (README `cursor_rules_skills/` / `kb_shipping_backfill/` remain pre-existing out-of-scope).

### Residual notes (do not fail)

- HTML `VERSION:` on Overview is still `v0.3` while the Change Log patch is `v0.3.1`; Proxy HTML `VERSION:` is still `v0.2` while the Change Log patch is `v0.2.1`. The required status/trigger/changelog text is present.
- Recommended cancelled-page reward-UI caveat and STL 15/17 date extras were not required to flip FAIL and were not treated as blockers.

**Final verdict: PASS.** Stage 6 campaign/community QA may be marked Resolved - Complete. Coordinator may bump `track_in.md` / handoffs README from “remediation” to campaign QA complete when ready.
