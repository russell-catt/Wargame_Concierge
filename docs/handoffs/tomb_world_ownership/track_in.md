# Track in — tomb_world_ownership

- **Project:** Wargame_Concierge
- **Track:** `tomb_world_ownership`
- **Status:** Closed - Complete
- **Git root:** `C:\Personal\Personal_Projects\Wargame_Concierge`
- **Plan reference:** `tomb_world_ownership_sync_cf3be3c8` (do not edit plan file)
- **Handoffs root:** `docs/handoffs/tomb_world_ownership/`
- **Playbook:** `docs/operations/multiagent_coordinator_strategy.md`

## Locked ownership decision (verbatim essence)

**Kill Team: Tomb World — owned, units game-ready:**

- 1× Cryptek Geomancer
- 2× Canoptek Tomb Crawlers
- 5× Canoptek Macrocytes
- 10× Necron Warriors (Tomb World)
- 3× Canoptek Scarab Swarms (Tomb World)

**Additional owned kits:**

- 10× Necron Warriors — unassembled, unpainted (second squad)
- 3× Canoptek Scarab Swarms — unassembled, unpainted (second set)
- 5× Immortals — unassembled (build before play)
- Hierotek Circle — game ready; datasheets TBD pending photos

**Totals:** 20 Warriors (10 ready + 10 sprue), 6 Scarab Swarms (3 ready + 3 sprue), plus Geomancer, Tomb Crawlers, Macrocytes, Immortals, Hierotek TBD.

Prefer Tomb World for learning games. Extra Warriors/Scarabs = assemble-to-expand. Do not re-shop owned kits. Prior "Tomb World not owned" claim was erroneous.

## Authoritative order

1. Project `Necron_Lists.md` (`games/warhammer_40k_11e/armies/necrons/Necron_Lists.md`)
2. `raw/` + `C:\Personal\40K\rules\Necron_Lists.md`
3. Army docs (`games/warhammer_40k_11e/armies/necrons/`)
4. KB

## Constraints

- **No GW binaries in git** — path pointers only
- **Librarian never writes `raw/`**; never commits
- **Subagents never commit or push** — Coordinator sole git owner at S4
- **Hierotek Circle TBD** — unit ID pending owner photos; open TODO
- **Deferred single commit at S4** — push authorized; include unpushed `5a7679c` if still ahead of remote

## Model matrix (locked)

| Role | Model slug |
|------|------------|
| Coordinator | `inherit` |
| Implementer — fast | `composer-2.5-fast` |
| Implementer — content | `claude-sonnet-5-thinking-high` |
| Librarian | `claude-fable-5-thinking-high` |
| QA — default | `gpt-5.6-sol-medium` |
| QA — light | `gemini-3.7-flash-high` |
| Final Sanity | `gpt-5.6-terra-medium` |

Record actual model in each `*_implementer.md`, `*_librarian.md`, and `*_qa.md`.

## Per-slice assignment

| Slice | Agent / model | QA model |
|-------|---------------|----------|
| **S0** | Implementer `composer-2.5-fast` | `gemini-3.7-flash-high` |
| **S1** | Implementer `composer-2.5-fast` | `gpt-5.6-sol-medium` |
| **S2** | Implementer `claude-sonnet-5-thinking-high` | `gpt-5.6-sol-medium` |
| **S3** | Implementer `claude-sonnet-5-thinking-high` | `gemini-3.7-flash-high` |
| **L1** | Librarian `claude-fable-5-thinking-high` | `gpt-5.6-sol-medium` |
| **L2** | Librarian `claude-fable-5-thinking-high` | `gemini-3.7-flash-high` |
| **S4** | Final Sanity `gpt-5.6-terra-medium`; Coordinator commits/pushes | — |

## Rollup

| Slice | Focus | Agent / model | QA model | Status |
|-------|--------|---------------|----------|--------|
| **S0** | Bootstrap handoffs + briefs | Implementer `composer-2.5-fast` | `gemini-3.7-flash-high` | In Progress |
| **S1** | FOUNDATION sync (project + raw + source) | Implementer `composer-2.5-fast` | `gpt-5.6-sol-medium` | pending |
| **S2** | Army docs + starters + inventory | Implementer `claude-sonnet-5-thinking-high` | `gpt-5.6-sol-medium` | pending |
| **S3** | Planning + distilled context + import pointer | Implementer `claude-sonnet-5-thinking-high` | `gemini-3.7-flash-high` | pending |
| **L1** | KB ownership ingest | Librarian `claude-fable-5-thinking-high` | `gpt-5.6-sol-medium` | pending |
| **L2** | Audit v1_scaffold L2 + lint | Librarian `claude-fable-5-thinking-high` | `gemini-3.7-flash-high` | pending |
| **S4** | Final Sanity + Coordinator commit/push | `gpt-5.6-terra-medium` + Coordinator | — | pending |

**Depends:** S0 → S1 → S2 → S3 → L1 → L2 → S4

## Git state

| Fact | Value |
|------|-------|
| Commit policy | Single deferred commit at **S4** |
| Push | Authorized at S4 |
| Unpushed | Include `5a7679c` ("Align Necron docs with confirmed FOUNDATION ownership.") if branch still ahead of remote |
| Owner | Coordinator alone commits/pushes at S4. Subagents never commit or push |

## S4 commit message (planned)

```
fix(necrons): Tomb World owned game-ready; dual Warriors/Scarabs inventory
```
