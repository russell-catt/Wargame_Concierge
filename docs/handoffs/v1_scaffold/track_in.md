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

### Model waivers

An unavailable locked model may be substituted **within the same family**, with the waiver recorded in the slice report. Implementer and QA must never collapse onto the same family for the same slice.

| Slice | Locked | Actually used | Basis | Recorded in |
|-------|--------|---------------|-------|-------------|
| L0 | `claude-fable-5-thinking-high` | `claude-opus-5-thinking-high` | Locked model unavailable at dispatch; same-family substitute | `slices/L0_librarian.md` |
| S1 | `claude-sonnet-5-thinking-high` | `claude-opus-5-thinking-high` | Locked model blocked/unavailable at dispatch; same-family substitute | `slices/S1_implementer.md` |
| L1 | `claude-fable-5-thinking-high` | `claude-opus-5-thinking-high` | Locked model unavailable at dispatch; same-family substitute | `slices/L1_librarian.md` |
| S3 | `claude-sonnet-5-thinking-high` | `claude-opus-5-thinking-high` | Locked model blocked at dispatch; same-family substitute | `slices/S3_implementer.md` |

**Coordinator decision now overdue:** four slices have run on a substitute, and **every non-`composer` slice on this track has run on `claude-opus-5-thinking-high`**. Neither `claude-fable-5-thinking-high` nor `claude-sonnet-5-thinking-high` has been available at any dispatch, so the locked matrix describes a configuration that has never been used. Either revise the Librarian and Implementer-content rows to match reality, or accept that S4, S5, and L2 will waive identically. Cross-family QA separation has held throughout — `gpt-5.6-sol-medium` is a different family from the substitute.

## Rollup

| Slice | Focus | Agent / model | QA model | Status |
|-------|--------|---------------|----------|--------|
| **Preflight** | Necron_Lists.md ownership patch | Implementer `composer-2.5-fast` | `gpt-5.6-sol-medium` | Resolved - Complete (PASS) |
| **S0** | RT bootstrap + raw/KB skeleton | Implementer `composer-2.5-fast` | `gemini-3.7-flash-high` | In Progress |
| **L0** | Karpathy KB bootstrap | Librarian `claude-fable-5-thinking-high` | `gpt-5.6-sol-medium` | pending |
| **S1** | Core RT docs + Game_System_Scaffold | Implementer `claude-opus-5-thinking-high` (waiver) | `gpt-5.6-sol-medium` | Resolved - Implemented (awaiting QA) |
| **S2** | Sources + Necron import | Implementer `composer-2.5-fast` | `gemini-3.7-flash-high` | **Done** |
| **L1** | Librarian ingest (Tier 0) | Librarian `claude-opus-5-thinking-high` (waiver) | `gpt-5.6-sol-medium` | **Resolved - Implemented (awaiting QA)** |
| **S3** | Rules + setup + Keyword_Glossary | Implementer `claude-opus-5-thinking-high` (waiver) | `gpt-5.6-sol-medium` | **Resolved - Implemented (awaiting QA)** |
| **S4** | Necron starters + laminate guide | Implementer `claude-sonnet-5-thinking-high` | `gpt-5.6-sol-medium` | pending |
| **S5** | SM Oath/Gladius + laminate | Implementer `claude-sonnet-5-thinking-high` | `gpt-5.6-sol-medium` | pending |
| **S6** | Full unit research (Necron + SM) | Opus + Sonnet parallel | `gpt-5.6-sol-medium` / `gemini-3.7-flash-high` | pending |
| **L2** | Librarian lint | Librarian `claude-fable-5-thinking-high` | `gemini-3.7-flash-high` | pending |
| **S7** | GitHub + Final Sanity | Coordinator + `gpt-5.6-terra-medium` | — | pending |

**Depends:** Preflight -> S0 -> **L0** -> S1 -> S2 -> **L1** -> S3 -> S4 -> S5 -> S6 -> **L2** -> S7

> **Rollup drift flagged by S1 (2026-08-16), not corrected here.** The **S0** row still reads "In Progress" and the **L0** row still reads "pending", but both slices are complete and both are contained in commit `1fa3b7c "Bootstrap Rising Tide spine and Karpathy KB schema (S0+L0)."` The L0 row also still names the locked Librarian model rather than the substitute that actually ran. S1 updated only its own row; the rest belongs to the Coordinator's bookkeeping and was left visibly stale rather than silently fixed. Actual models used are recorded in the Model waivers table above and in each slice report.

> **L1 (2026-08-16) updated the S2 and L1 rows only**, per the brief, and added its own waiver row. The S0 and L0 rows above are still stale and are still the Coordinator's to fix. L1 also **converted this file from UTF-16LE to UTF-8** — see Known repo defects.

> **S3 (2026-08-16) updated its own row only.** The S0 and L0 rows remain stale and remain the Coordinator's to fix. S3 found **this file had reverted to UTF-16LE** when the agent editor rewrote it mid-edit, and converted it back to UTF-8. The "Editor writes UTF-16LE" defect below is **live, not historical** — it fires on every edit, not just on file creation.

## Git state

| Fact | Value |
|------|-------|
| Commits | 4 - `1fa3b7c` (S0+L0), `698e000` (S1), `10f7008` and `be34342` (both "Import Necron lists and scaffold 40K game tree (S2).") |
| Remote | **None yet.** The private GitHub repo `russell-catt/Wargame_Concierge` is created at S7 |
| Push | User gate at S7 |
| Owner | Coordinator alone commits. Subagents never commit or push |

> **Flagged by L1 — a commit landed mid-slice.** `be34342` (2026-08-16 18:45) was created **while L1 was running** and swept in five `KB/sources/*.md` files that L1 had just written, under the S2 commit message. L1 did not commit — the Librarian never runs git write commands, and the working tree was left dirty as required. Two consequences for the Coordinator: the S2 commit message now covers L1 content, and those five blobs were committed while still UTF-16LE, so git recorded them as binary. L1 has since converted them to UTF-8, which is why they now appear modified. Recommend amending or re-committing with an accurate message once L1 QA passes.

## Secrets / copyright policy

- No `.env` or credentials in repo
- No GW PDFs/images committed
- Unit research = personal structured notes with Wahapedia/local PDF pointers — not redistribution of official datasheets

## Known repo defects (carried, not blocking)

| Defect | Detail | Owner |
|--------|--------|-------|
| Playbook dead links | `docs/operations/multiagent_coordinator_strategy.md` carries 26 relative links inherited from the `daily_report` repo pointing at directories that do not exist here. Prose is authoritative; links are not | Later cleanup slice |
| UTF-16LE files | **Resolved as of L1 (2026-08-16).** The five files listed by L0 (`checkins/README.md`, `prompts/README.md`, `docs/handoffs/README.md`, `slices/S0_brief.md`, `raw/pointers/README.md`) are all UTF-8 today. **This file was not on that list and was itself UTF-16LE**; L1 converted it, which is why its diff is whole-file. A repo-wide scan after L1 finds **0** UTF-16 markdown files. `raw/pointers/README.md` was never touched by L1 — it was already UTF-8 | Closed - verify at L2 |
| Editor writes UTF-16LE | New markdown written through the agent editor in this environment lands as **UTF-16LE without BOM** unless explicitly converted. L1 hit this on all 22 files it touched and converted them as a final step. **S3 (2026-08-16) confirmed it also fires on _edits to existing UTF-8 files_**, not just on creation - a single string replace into `track_in.md` silently re-encoded the whole file back to UTF-16LE. **Any slice writing or editing markdown must byte-check its output before reporting done** | All slices - **check before exit** |
