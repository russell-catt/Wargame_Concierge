# Track in — v1_scaffold

- **Project:** Wargame_Concierge
- **Track:** `v1_scaffold`
- **Status:** In Progress
- **Git root:** `C:\Personal\Personal_Projects\Wargame_Concierge` (standalone repo; not a Personal_Projects monorepo leaf)
- **Plan:** Cursor plan `wargame_concierge_setup_ee78aead` (do not edit plan file)
- **Handoffs root:** `docs/handoffs/v1_scaffold/`
- **Playbook:** `docs/operations/multiagent_coordinator_strategy.md`
- **External source library:** `C:\Personal\40K` (read-only; Preflight edit to `rules/Necron_Lists.md` only)

## Goals

Standalone Rising Tide-scaffolded repo for learning Warhammer 40,000 11th Edition:

- Karpathy-style **KB** (`raw/` -> `KB/` -> shipping `docs/` + `games/`)
- Real beginner teaching content (rules, setup, Necron + Space Marine starters)
- Multi-slice multi-agent workflow with locked models
- Private GitHub repo at S7 (push = user gate)

## Constraints

- **No GW binaries in git** — PDFs, webp, official images stay outside repo; markdown path pointers only
- **Librarian never writes `raw/`**; never commits
- **Subagents never commit or push** — Coordinator sole git owner
- **Do not create in S0:** `AGENTS.md`, `KB/index.md`, `.obsidian` (L0 Librarian)
- Copyright: teaching paraphrase only; Wahapedia/local PDF cross-check before play
- Hierotek Circle unit ID pending user photos — placeholder until ingest follow-up

## Preflight notes (2026-08-16)

- **Necron ownership updated** in `C:\Personal\40K\rules\Necron_Lists.md` before S0
- Confirmed: 10 Warriors, 3 Scarab Swarms, 5 Immortals (all purchased, unassembled); Hierotek Circle used set (game ready)
- **Tomb World** marked superseded/historical — not current ownership
- **Hierotek Circle TBD photos** — open TODO for datasheet mapping; Phase 1/2 prefer game-ready Hierotek once IDed

## Model matrix (locked)

| Role | Model slug |
|------|------------|
| Coordinator | `inherit` |
| Librarian | `claude-fable-5-thinking-high` |
| Implementer — fast | `composer-2.5-fast` |
| Implementer — content | `claude-sonnet-5-thinking-high` |
| Implementer — research (Necrons) | `claude-opus-5-thinking-high` |
| Implementer — research (SM parallel) | `claude-sonnet-5-thinking-high` |
| QA — default | `gpt-5.6-sol-medium` |
| QA — light | `gemini-3.7-flash-high` |
| Final Sanity | `gpt-5.6-terra-medium` |

Record actual model in each `*_implementer.md`, `*_librarian.md`, and `*_qa.md`.

## Rollup

| Slice | Focus | Agent / model | QA model | Status |
|-------|--------|---------------|----------|--------|
| **Preflight** | Necron_Lists.md ownership patch | Implementer `composer-2.5-fast` | `gpt-5.6-sol-medium` | Resolved - Complete (PASS) |
| **S0** | RT bootstrap + raw/KB skeleton | Implementer `composer-2.5-fast` | `gemini-3.7-flash-high` | In Progress |
| **L0** | Karpathy KB bootstrap | Librarian `claude-fable-5-thinking-high` | `gpt-5.6-sol-medium` | pending |
| **S1** | Core RT docs + Game_System_Scaffold | Implementer `claude-sonnet-5-thinking-high` | `gpt-5.6-sol-medium` | pending |
| **S2** | Sources + Necron import | Implementer `composer-2.5-fast` | `gemini-3.7-flash-high` | pending |
| **L1** | Librarian ingest (Tier 0) | Librarian `claude-fable-5-thinking-high` | `gpt-5.6-sol-medium` | pending |
| **S3** | Rules + setup + Keyword_Glossary | Implementer `claude-sonnet-5-thinking-high` | `gpt-5.6-sol-medium` | pending |
| **S4** | Necron starters + laminate guide | Implementer `claude-sonnet-5-thinking-high` | `gpt-5.6-sol-medium` | pending |
| **S5** | SM Oath/Gladius + laminate | Implementer `claude-sonnet-5-thinking-high` | `gpt-5.6-sol-medium` | pending |
| **S6** | Full unit research (Necron + SM) | Opus + Sonnet parallel | `gpt-5.6-sol-medium` / `gemini-3.7-flash-high` | pending |
| **L2** | Librarian lint | Librarian `claude-fable-5-thinking-high` | `gemini-3.7-flash-high` | pending |
| **S7** | GitHub + Final Sanity | Coordinator + `gpt-5.6-terra-medium` | — | pending |

**Depends:** Preflight -> S0 -> **L0** -> S1 -> S2 -> **L1** -> S3 -> S4 -> S5 -> S6 -> **L2** -> S7

## Secrets / copyright policy

- No `.env` or credentials in repo
- No GW PDFs/images committed
- Unit research = personal structured notes with Wahapedia/local PDF pointers — not redistribution of official datasheets
