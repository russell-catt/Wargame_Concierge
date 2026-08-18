<!--
FILE: reference/uml/README.md
VERSION: v0.5.0 (2026-08-18)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, track flowcharting_uml / S0)

DOCUMENT_TYPE: Reference / External notation snapshots
PROJECT_NAME: Wargame_Concierge
REFERENCE_STATUS: Active — not project truth

PURPOSE:
  Park offline HTML snapshots of uml-diagrams.org UML 2.5 activity-family
  pages so flowcharting in this repo has a local teaching reference.
  This folder is reference/, not shipping truth and not a Kill Team source.

UPDATE_TRIGGER:
  Update when snapshots are re-fetched or the house mapping in
  docs/operations/Flowcharting.md changes which pages we keep.
-->

# UML notation snapshots (`reference/uml/`)

**This folder is not project truth.** It is an external teaching reference parked here so agents do not scrape uml-diagrams.org on every session. Player-facing flowchart rules live in [`docs/operations/Flowcharting.md`](../../docs/operations/Flowcharting.md) after Librarian ingest. Kill Team rules still come only from owned PDFs.

## Credit (mandatory)

Notation reference is [uml-diagrams.org](https://www.uml-diagrams.org/), [About the site](https://www.uml-diagrams.org/about.html): **authored by Kirill Fakhroutdinov**. Copyright © 2009–2026 uml-diagrams.org. All rights reserved.

The site follows OMG UML 2.5. It is a **third-party teaching reference**, not an OMG spec dump and **not** a Kill Team rules source.

## Retrieval

| Field | Value |
|-------|--------|
| Retrieval date | **2026-08-18** |
| Method | Live HTML saved with `Invoke-WebRequest` (WebFetch returned HTTP 466) |
| Scope | Activity family + About only — **not** the whole site |

## Files in this folder

| Local file | Live URL | Role |
|------------|----------|------|
| [`UML_2_5_Diagrams_Overview.html`](UML_2_5_Diagrams_Overview.html) | https://www.uml-diagrams.org/uml-25-diagrams.html | UML 2.5 diagram taxonomy (moved from repo-root `UML-25.html`) |
| [`activity-diagrams.html`](activity-diagrams.html) | https://www.uml-diagrams.org/activity-diagrams.html | Activity, partition, activity edge |
| [`activity-diagrams-actions.html`](activity-diagrams-actions.html) | https://www.uml-diagrams.org/activity-diagrams-actions.html | Action (rounded rectangle) |
| [`activity-diagrams-controls.html`](activity-diagrams-controls.html) | https://www.uml-diagrams.org/activity-diagrams-controls.html | Initial, activity final, flow final, decision, merge, fork, join |
| [`about.html`](about.html) | https://www.uml-diagrams.org/about.html | Authorship and copyright provenance |

Snapshots keep the live site’s remote CSS/image URLs. Open them for the text; figures may need the network.

## What this project actually uses

Flowcharts here map to **UML activity diagrams**, not class or sequence diagrams. House mapping (shipping): filled-circle **initial**, rounded-rect **actions**, diamond **decisions** with `[YES]`/`[NO]` (or other) **guards** on edges, bullseye **activity final**. See [`KB/concepts/flowcharting_uml_activity.md`](../../KB/concepts/flowcharting_uml_activity.md).

## Change Log

- v0.5.0 (2026-08-18): Initial park of UML-25 overview + activity-family + About snapshots (track `flowcharting_uml` S0).
