# Wargame_Concierge handoffs

Multi-agent track artifacts (briefs, implementer reports, QA, Librarian reports, Final Sanity) live here.

**Playbook:** [`docs/operations/multiagent_coordinator_strategy.md`](../operations/multiagent_coordinator_strategy.md)

## Active tracks

| Track | Folder | Status |
|-------|--------|--------|
| v1 scaffold (40K 11e beginner content + Karpathy KB) | [`v1_scaffold/`](v1_scaffold/) | Closed - Complete |
| Tomb World ownership sync | [`tomb_world_ownership/`](tomb_world_ownership/) | In Progress |
| Kill Team 2024 scaffold (KT24 / 3e + Join Ops + 2e archive) | [`kill_team_2024_scaffold/`](kill_team_2024_scaffold/) | In Progress |
| Nemesis Ops research (OCR + joint_ops rename + nemesis_ops/) | [`nemesis_ops_research/`](nemesis_ops_research/) | Closed - Complete (commits pending) |
| Nemesis Ops OCR spot-check | [`nemesis_ops_ocr_spotcheck/`](nemesis_ops_ocr_spotcheck/) | Closed - Complete (commits pending) |
| Flowcharting UML (activity notation + valid-target sheet restyle) | [`flowcharting_uml/`](flowcharting_uml/) | Closed - Complete (this commit) |

## Artifact lifecycle (summary)

1. `track_in.md` — Coordinator constraints / rollup / model matrix
2. `slices/{Id}_brief.md` — Ready entrance (Implementer or Librarian)
3. `slices/{Id}_implementer.md` or `slices/L{n}_librarian.md` — Tier 1
4. `slices/{Id}_qa.md` or `slices/L{n}_lib_qa.md` — Tier 2 → Resolved - Complete
5. `track_*_final_report.md` — Tier 3 Final Sanity

**Librarian slices (Tier 0):** L0, L1, L2 — see playbook §18.5.

**Git:** Coordinator alone commits after each slice **Resolved - Complete**. Subagents do not commit or push.
