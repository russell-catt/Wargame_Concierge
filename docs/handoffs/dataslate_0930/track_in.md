# Track in — dataslate_0930

- **Project:** Wargame_Concierge
- **Track:** `dataslate_0930`
- **Status:** Closed — Final Sanity 2026-10-01. No git until the owner gates it.
- **Handoffs root:** `docs/handoffs/dataslate_0930/`
- **Playbook:** [`docs/operations/multiagent_coordinator_strategy.md`](../../operations/multiagent_coordinator_strategy.md)
- **QA skill:** [`.cursor/skills/qa-slice/SKILL.md`](../../../.cursor/skills/qa-slice/SKILL.md)
- **Librarian enhance:** [`.cursor/skills/librarian-enhance/SKILL.md`](../../../.cursor/skills/librarian-enhance/SKILL.md)
- **Opened:** 2026-10-01

## Model pair

Implementer and QA are different families. A failed QA verdict returns to the Coordinator, who writes `slices/{Id}_reopen.md` before the Implementer touches the slice again. A second FAIL on one slice stops the track for the owner.

| Role | Family | Slug |
|------|--------|------|
| Coordinator / Implementer | Grok | grok-4.7 (this session) |
| QA (S0, S1, S2, L1) | GPT | `gpt-5.6-sol-medium` |
| Final Sanity | Claude | `claude-sonnet-5-5-high` |

Subagents do not commit or push. No git on this track unless the owner gates it. Proposed branch if gated: `cursor/dataslate-0930-mfm-v15-b7e0`.

## Goals

1. Record MFM v1.5 (30 Sep 2026) as the points source of record: live site primary, owner paste as the Legends capture.
2. Recost Necron Conclave lists for Immortals, Tomb Crawlers, and the Doomstalker. 1000 V1 becomes 935. Stay on Cryptek Conclave at 2DP.
3. If a recost breaks a points cap, show the arithmetic and the smallest legal cut, and do not delete a unit until the owner says yes.
4. Stale-banner the Space Marine 1000 list. Gladius is 3DP, over the 2DP budget at 1000. Do not recost it and do not change its detachment.
5. Write which 1DP Space Marine detachments fit the owned shelf. Owner picks before any list changes detachment.

## Non-goals

- Codex profiles, Toughness, or weapon statlines. The WarCom articles are commentary.
- Dumping an MFM points book into `games/` or `KB/`.
- Importing a Warmind profile, or any Warmind row the live MFM does not carry.
- Committing `raw/dataslate_Sep30/` (Apple Note zips with GW images).
- Unit cuts without an owner yes. Git without an owner gate.

## Detachment budget

Every list in this track is 1000 points at most, so it spends **2 Detachment Points in total**.

## QA return path

PASS: Coordinator marks the slice Resolved and writes the next brief.
FAIL: Coordinator writes `slices/{Id}_reopen.md` with the exact findings and hands it back. The same QA agent re-checks.
Second FAIL on one slice: stop and report to the owner.

## Slice order

S0 research note → S1 Necron recost → S2 Space Marine hold and 1DP fit → L1 Librarian → Final Sanity.
