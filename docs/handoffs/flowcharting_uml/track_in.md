# Track in — flowcharting_uml

- **Project:** Wargame_Concierge
- **Track:** `flowcharting_uml`
- **Status:** Closed - Complete
- **Git root:** `C:\Personal\Personal_Projects\Wargame_Concierge`
- **Plan:** Cursor plan `uml_flowchart_guidelines_7856e423` (do not edit plan file)
- **Handoffs root:** `docs/handoffs/flowcharting_uml/`
- **Playbook:** `docs/operations/multiagent_coordinator_strategy.md`
- **Date:** 2026-08-18
- **Project version:** v0.5.0

## Goals

1. Park UML-25 overview + activity-family + About snapshots under `reference/uml/` (not project truth)
2. Librarian ingest: source + concept + glossary paraphrase (no uml-diagrams.org prose dump)
3. Ship house flowcharting guide (`docs/operations/Flowcharting.md`)
4. Restyle **only** `Target_Eligibility_Cheat_Sheet.html` to UML activity shapes — **do not** change decision logic or PDF cites
5. Lite mermaid pass on coordinator playbook (same edges/meaning; no Sec 17–18 rewrite)
6. Credit **Kirill Fakhroutdinov** / uml-diagrams.org on every surface that uses the notation
7. One Coordinator commit at end; **do not push**

## Credit (locked)

[uml-diagrams.org About](https://www.uml-diagrams.org/about.html): **Authored by Kirill Fakhroutdinov**. Copyright © 2009–2026 uml-diagrams.org. All rights reserved. Third-party teaching reference; **not** a Kill Team rules source.

Name + About URL + copyright line required on: `reference/uml/README.md`, Source_Library row, KB source page, Flowcharting.md footer, Target_Eligibility_Cheat_Sheet.html footer, one-line caption under coordinator mermaid.

## Locked sources

| Source | Path / URL |
|--------|------------|
| UML 2.5 overview (was repo-root) | `reference/uml/UML_2_5_Diagrams_Overview.html` |
| Activity family live | https://www.uml-diagrams.org/activity-diagrams.html (+ actions, controls) |
| About / credit | https://www.uml-diagrams.org/about.html |
| Cheat sheet (S2 only) | `games/kill_team_2024/rules/Target_Eligibility_Cheat_Sheet.html` |
| Coordinator mermaid (S3 lite) | `docs/operations/multiagent_coordinator_strategy.md` §2 |

## Model matrix (locked)

| Role | Model |
|------|-------|
| Coordinator | `inherit` (end-to-end this session) |
| Librarian | same session (Tier 0 hat) |
| Implementer | same session |
| QA-G / QA-A | same session, independent re-read |
| Final Sanity | same session |

Coordinator wears all hats in one loop; slice artifacts still filed.

## Constraints

- Never treat uml-diagrams.org as a Kill Team rules source
- Do not scrape the whole uml-diagrams.org site
- Do not rewrite other historical `docs/handoffs/**` tracks
- Datacards unchanged
- No GW binaries
- Subagents do not commit; this Coordinator session **one commit, no push**
- `reference/` is not project truth
- KB = teaching paraphrase only

## Rollup

| Slice | Focus | Status |
|-------|--------|--------|
| Preflight | track_in + inventory | Resolved - Complete |
| S0 | Move UML-25, snapshot pages, Source_Library, README credit | Resolved - Complete |
| L1 | KB source + concept + glossary; index/overview/log | Resolved - Complete |
| S1 | Flowcharting.md + links + HTML class snippet | Resolved - Complete |
| QA-G | Guide vs activity-controls: diamonds, guards, start/end | Resolved - Complete |
| S2 | Restyle cheat sheet CSS/DOM only | Resolved - Complete |
| S3 | Lite mermaid | Resolved - Complete |
| QA-A | One landscape page; tree labels; mermaid meaning | Resolved - Complete |
| L2 | changelog promotion row | Resolved - Complete |
| FS | Track final report | Closed - Complete |

## Non-goals

- Class / sequence diagram adoption
- Datacard restyle
- OMG spec ingest
- Sec 17–18 playbook rewrite
