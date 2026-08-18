<!--
FILE: docs/README.md
VERSION: v0.5.0 (2026-08-18)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, slice S1)

DOCUMENT_TYPE: Folder README / Documentation Index
PROJECT_NAME: Wargame_Concierge
PROJECT_STATUS: Active

SOURCES:
  - README.md
  - AGENTS.md
  - docs/handoffs/v1_scaffold/track_in.md

PURPOSE:
  Index of everything under docs/. Says what each document answers and which
  audience it is written for, so a reader can pick the right one without
  opening all of them.

UPDATE_TRIGGER:
  Update when a document is added to, removed from, or renamed within docs/.
-->

# `docs/` - documentation index

Shipping reference for Wargame_Concierge: how the project is laid out, what has been decided, how the agents operate, and how to add the next game system.

**Layer note:** `docs/` is the **shipping** layer. It holds reviewed, player-facing and process-facing truth. Working synthesis lives one layer down in [`KB/`](../KB/) and is promoted here after review, with a row in [`KB/changelog.md`](../KB/changelog.md). See [`AGENTS.md`](../AGENTS.md) Sec 2.

---

## Project documents

| Document | Answers | Audience |
|----------|---------|----------|
| [`Project_Structure.md`](Project_Structure.md) | Where does this file belong, and who owns that directory? | Anyone adding a file |
| [`Project_Planning.md`](Project_Planning.md) | What has been decided, what is confirmed, what is still open? | Owner, Coordinator |
| [`Project_Origin_Story.md`](Project_Origin_Story.md) | Why does this project exist, and who is it for? | Newcomers, beginners |
| [`Rehydration_Prompt.md`](Rehydration_Prompt.md) | How does a cold AI session rebuild full context? | AI systems, owner during recovery |
| [`Game_System_Scaffold.md`](Game_System_Scaffold.md) | What do I create when adding a new wargame? | Whoever onboards system #3 (KT24 is onboarded) |

---

## Operations

Process documents for the multi-agent workflow. Location: [`operations/`](operations/).

| Document | Answers |
|----------|---------|
| [`operations/multiagent_coordinator_strategy.md`](operations/multiagent_coordinator_strategy.md) | The normative playbook: roles, tiers, slice state machine, git rules, Librarian governance (Sec 18) |
| [`operations/librarian_agent.md`](operations/librarian_agent.md) | Librarian day-to-day: the query / ingest / lint / promote loop and the L0-L1-L2 maturity model |

> **Known issue:** `multiagent_coordinator_strategy.md` carries 26 dead relative links inherited from the `daily_report` repo it was adapted from. The prose is authoritative; those links are not. Flagged by the Librarian in [`handoffs/v1_scaffold/slices/L0_librarian.md`](handoffs/v1_scaffold/slices/L0_librarian.md).

---

## Handoffs

Multi-agent track artifacts - briefs, implementer reports, QA reports, Librarian reports. Location: [`handoffs/`](handoffs/).

| Entry point | Contents |
|-------------|----------|
| [`handoffs/README.md`](handoffs/README.md) | **Later tracks index** (`tomb_world_ownership`, `kill_team_2024_scaffold`, `kt24_rules_quotes`, Nemesis, …) and the artifact lifecycle |
| [`handoffs/v1_scaffold/track_in.md`](handoffs/v1_scaffold/track_in.md) | Historical: 40K beginner scaffold constraints and rollup |

Shipping KT24 rules/reference: [`../games/kill_team_2024/rules/Patch_Manifest.md`](../games/kill_team_2024/rules/Patch_Manifest.md), [`Target_Eligibility.md`](../games/kill_team_2024/rules/Target_Eligibility.md).

Handoff **slice** artifacts are frozen — do not edit briefs/QA/reports. Everything else under `docs/` uses the Rising Tide header and footer.

---

## Related, outside `docs/`

| Path | Why you would go there |
|------|------------------------|
| [`../START_HERE.md`](../START_HERE.md) | Entry point and read order |
| [`../README.md`](../README.md) | Project overview and directory map |
| [`../AGENTS.md`](../AGENTS.md) | **Schema source of truth** for the knowledge base |
| [`../KB/index.md`](../KB/index.md) | Master catalog of KB pages |
| [`../reference/`](../reference/) | Seed prompt, distilled context, and the Karpathy pattern doc |
| [`../templates/`](../templates/) | Rising Tide header and footer fragments |
| [`../games/`](../games/) | Per-system teaching content |

---

## Adding a document here

1. Pick the matching Rising Tide header and footer from [`../templates/README.md`](../templates/README.md).
2. Fill the header honestly - `SOURCES` and `UPDATE_TRIGGER` are the fields that decay fastest and matter most.
3. Add a row to the right table above. An unindexed document is one nobody finds.
4. Write UTF-8, no BOM.
5. Leave the commit to the Coordinator.

---

## Change Log

- v0.5.0 (2026-08-18): Project-wide semver snapshot (x.y.z). Later tracks via handoffs/README.md; Patch_Manifest / Target_Eligibility.
- v1.0 (2026-08-16): Initial documentation index covering project documents, operations, and handoffs. Created in slice S1.

## Attribution

- Project: Wargame_Concierge
- Maintainer: Russell Catt
- Structured using the Rising Tide framework

## Rising Tide Notes

- This document follows Rising Tide documentation standards.
- Must remain understandable, reproducible, and reusable.
