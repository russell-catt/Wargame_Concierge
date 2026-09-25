# S3 — Lore implementer report

- **Track:** `warcode_kickstarter_refresh`
- **Stage:** 3
- **Date:** 2026-09-24
- **Status:** Complete
- **Narrative baseline:** `The-Warcode-Lorebook-Tactical-Doctrine-Field-Edition.pdf`
- **Mechanics baseline:** `The-Warcode-Rulebook-V.0.8.9-F.pdf`

## Result

Shipped the shared lore spine and integrated concise, faction-specific lore and doctrine into all four playable-faction overviews. The implementation preserves the lorebook's academy-dossier frame, labels interested and hostile source voices, and keeps project synthesis separate.

The lorebook remains narrative context only. All tactical application and playable effects point to rulebook v0.8.9-F.

## Files added

- `games/the_warcode/lore/README.md`
- `games/the_warcode/lore/Theatre_of_Operations.md`
- `games/the_warcode/lore/Historical_Timeline.md`
- `games/the_warcode/lore/Source_Methodology.md`
- `docs/handoffs/warcode_kickstarter_refresh/slices/S3_lore_implementer.md`

## Files updated

- `games/the_warcode/README.md`
- `games/the_warcode/factions/dominium/README.md`
- `games/the_warcode/factions/mdr/README.md`
- `games/the_warcode/factions/protagen_marines/README.md`
- `games/the_warcode/factions/ulfari/README.md`

No `KB/`, `raw/`, or campaign file was edited.

## Required lore locks

- Huoxing is taught as the MDR-controlled planet; Mars is the distinct Kirkwood Belt settlement where the year-1689 congress met.
- Blackout is separated into policy/event/epoch usage; Blackout War is attributed to a historical monograph; Silence War is attributed to factional usage.
- MDR's partial Cassini control is reconciled with Protagen moon bases as overlapping presence, not exclusive ownership.
- Custodia Silens is identified as a playable Dominium formation, not a synonym for the entire faction; lore context comes from the lorebook and playability from rulebook pp.39–40.
- The Burning's printed phase durations total 151 years despite the stated 142-year epoch; the date ranges imply 77 rather than 86 years for the final phase. The discrepancy is flagged, not silently repaired.
- The unqualified Ulfari station-destruction hook was removed.
- First contact now compares the older publisher context with the non-hostile Erebus-7 record and Dominium suppression/escalation orders.
- The shipping text does not claim those orders were completed, that Erebus-7 was destroyed, who began every later clash, or that all later violence was fabricated.
- Ulfari intent remains unknown because the dossier contains no clearly Ulfari-authored source.

## Source and quotation handling

- Academy structural prose, faction-authored testimony, hostile military assessments, records, and project interpretation are distinguished in the new methodology and faction sections.
- No verbatim lore excerpt was added. Location callouts and teaching summaries are paraphrases with PDF-page and section citations.
- The lorebook's Tactical Application section is treated as a redirect to the current rulebook, never as mechanics authority.

## Navigation and backlinks

- The system README links the new lore directory in both the learning path and subtree map.
- The lore README links all three shared lore references and all four faction overviews.
- Every faction overview links back to the shared lore spine.
- Theatre, timeline, and methodology pages cross-link where their topics overlap.

## Verification

- **Banned-name scan:** case-insensitive scan of `games/the_warcode/**` for every prohibited comparator name and number form returned 0 matches.
- **Link check:** all relative Markdown `.md` links in the Warcode shipping tree resolve (`broken=0`).
- **First-contact scan:** no unqualified station-destruction statement remains; completion/fabrication language appears only as explicit limits on what the evidence proves.
- **Required-topic scan:** the lore spine contains Huoxing/Mars, war-name distinctions, Cassini overlap, Custodia Silens, Burning arithmetic, and v0.8.9-F mechanics routing.
- **Diagnostics:** no linter errors were reported for the new lore directory or updated overview/faction files.
- **Scope:** no `KB/`, `raw/`, or campaign file was changed by this stage.
- **Git:** not run.

## Handoff

Ready for Stage 3 QA. Review should focus on source-voice labels, citation precision, and the first-contact non-overclaim boundary.
