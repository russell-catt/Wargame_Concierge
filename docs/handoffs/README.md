# Wargame_Concierge handoffs

Multi-agent track artifacts (briefs, implementer reports, QA, Librarian reports, Final Sanity) live here.

**Playbook:** [`docs/operations/multiagent_coordinator_strategy.md`](../operations/multiagent_coordinator_strategy.md)

## Active tracks

| Track | Folder | Status |
|-------|--------|--------|
| Balance Dataslates Aug 2026 (40K + KT) | [`dataslate_0826/`](dataslate_0826/) | Open — plan package on `feature/dataslate_0826`; execution gated |
| v1 scaffold (40K 11e beginner content + Karpathy KB) | [`v1_scaffold/`](v1_scaffold/) | Closed - Complete |
| Tomb World ownership sync | [`tomb_world_ownership/`](tomb_world_ownership/) | In Progress |
| Kill Team 2024 scaffold (KT24 / 3e + Join Ops + 2e archive) | [`kill_team_2024_scaffold/`](kill_team_2024_scaffold/) | In Progress |
| Nemesis Ops research (OCR + joint_ops rename + nemesis_ops/) | [`nemesis_ops_research/`](nemesis_ops_research/) | Closed - Complete (commits pending) |
| Nemesis Ops OCR spot-check | [`nemesis_ops_ocr_spotcheck/`](nemesis_ops_ocr_spotcheck/) | Closed - Complete (commits pending) |
| Flowcharting UML (activity notation + valid-target sheet restyle) | [`flowcharting_uml/`](flowcharting_uml/) | Closed - Complete (this commit) |
| KT24 doc follow-ups (Letter print, freshness dates, complete cards) | [`kt24_doc_followups/`](kt24_doc_followups/) | Open (parked) |
| Cursor rules + skills (thin `.cursor/rules` + project skills citing AGENTS.md) | [`cursor_rules_skills/`](cursor_rules_skills/) | Closed - Complete (commits pending) |
| KB shipping back-fill (OC + Power Matrix from on-disk shipping) | [`kb_shipping_backfill/`](kb_shipping_backfill/) | Closed - Complete (commits pending) |
| Learn-to-play event (KT Volkus PM+Kommandos + first 40K Conclave) | [`learn_to_play_event/`](learn_to_play_event/) | Closed - Complete (commits pending) |
| SM Matched vs Casual (Legends) starters + Librarian KB pass | [`sm_matched_vs_casual/`](sm_matched_vs_casual/) | Closed — merged PR #7 |
| GW community-content footer + games/ compliance | [`gw_community_content/`](gw_community_content/) | Closed — Complete (commits pending) |
| The Warcode: Tactical Doctrine (system #3 + VIP review) | [`warcode_tactical_doctrine/`](warcode_tactical_doctrine/) | Closed — merged PR #16 |
| WD527 research (40K ref card, Mission 38, wound laminate) | [`wd527_research/`](wd527_research/) | Closed - Complete (commit pending) |

**Review queue:** Post-ship owner pass — [warcode_tactical_doctrine/to_review.md](warcode_tactical_doctrine/to_review.md).

## Artifact lifecycle (summary)

1. `track_in.md` — Coordinator constraints / rollup / model matrix
2. `slices/{Id}_brief.md` — Ready entrance (Implementer or Librarian)
3. `slices/{Id}_implementer.md` or `slices/L{n}_librarian.md` — Tier 1
4. `slices/{Id}_qa.md` or `slices/L{n}_lib_qa.md` — Tier 2 → Resolved - Complete
5. `track_*_final_report.md` — Tier 3 Final Sanity

**Librarian slices (Tier 0):** L0, L1, L2 — see playbook §18.5.

**Git:** Coordinator alone commits after each slice **Resolved - Complete**. Subagents do not commit or push.
