# Track in — nemesis_ops_research

- **Project:** Wargame_Concierge
- **Track:** `nemesis_ops_research`
- **Status:** Closed - Complete (2026-08-17) — commits pending user ask
- **Git root:** `C:\Personal\Personal_Projects\Wargame_Concierge`
- **Plan:** Cursor plan `nemesis_ops_research_pass_38a9066b` (do not edit plan file)
- **Handoffs root:** `docs/handoffs/nemesis_ops_research/`
- **Playbook:** `docs/operations/multiagent_coordinator_strategy.md`
- **Parent context:** Follow-on to [`kill_team_2024_scaffold`](../kill_team_2024_scaffold/track_in.md) (S9 Join Ops gapped on unreadable dossier)
- **External libraries (read-only except OCR sidecar write + eng.pdf delete):**
  - `C:\Personal\Kill Team\kill_team_2024\` — dossier primary; eng.pdf delete target
  - `C:\Personal\Kill Team\Community Content\` — two locked PDFs only (S1b)

## Goals

1. Delete `kill-team-nemesis-operatives-eng.pdf` and scrub live repo mentions of that filename
2. Rename `games/kill_team_2024/join_ops` → `joint_ops` (official Joint Ops naming) + link sweep
3. Full OCR of Nemesis Operatives Dossier → searchable sidecar **outside git**
4. Research Warhammer Community for freely published Nemesis / NPO / Custom Builder statlines
5. Use two Community Content PDFs (NPO cheat sheet + KT24 cheat sheet) as `draft` secondary only
6. Ship `games/kill_team_2024/nemesis_ops/` including required `How_To_Create_A_Nemesis_Operative.md`
7. Reconcile `joint_ops/NPO_Catalog.md` §5; Gaps honest
8. KB source/index/log + lint; Formal QA; Final Sanity

## Constraints

- **No GW binaries in git** — PDFs, OCR output, page images, Community Content binaries stay outside repo
- **Teaching paraphrase only** — never transcribe dossier OCR datasheets/statlines into the repo
- **WarCom free stats OK** with URL + retrieval date
- **Community numbers** = `draft` / `unverified` only; never unmarked as official; always stale-risk flagged
- **Trust ladder:** 1) WarCom free → 2) owned dossier OCR (process paraphrase only) → 3) Community PDFs
- **Librarian never writes `raw/`**; never commits
- **Subagents never commit or push** — Coordinator sole git owner
- **Do not commit** unless user explicitly asks; note pending commits below
- **Historical handoffs:** do not mass-rewrite closed scaffold slice reports; note rename in both tracks' `track_in.md`
- **Never** use `claude-fable-5-thinking-high`

## Locked decisions

| Decision | Choice |
|----------|--------|
| Rename | `join_ops` → `joint_ops` |
| New dir | `games/kill_team_2024/nemesis_ops/` |
| Primary owned PDF | Dossier only |
| Mislabeled PDF | **Delete** eng.pdf; scrub live mentions |
| OCR path | Beside dossier: `C:\Personal\Kill Team\kill_team_2024\1063073009-Kill-Team-Nemesis-Operatives-Dossier.ocr.txt` (or searchable OCR PDF equivalent) |
| Community Content pair | See below |
| Required shipping page | `How_To_Create_A_Nemesis_Operative.md` |

### Community Content pair (locked)

1. `C:\Personal\Kill Team\Community Content\The Kill Team 24 NPO Cheat Sheet Vers 1.1 ALTERNATIVE TEST.pdf`
2. `C:\Personal\Kill Team\Community Content\The Kill Team 24 Cheat Sheet Vers 1.21.pdf`

### OCR path (locked)

| Item | Path |
|-------|------|
| Source PDF | `C:\Personal\Kill Team\kill_team_2024\1063073009-Kill-Team-Nemesis-Operatives-Dossier.pdf` |
| Sidecar (S1) | `C:\Personal\Kill Team\kill_team_2024\1063073009-Kill-Team-Nemesis-Operatives-Dossier.ocr.txt` |
| Delete target | `C:\Personal\Kill Team\kill_team_2024\kill-team-nemesis-operatives-eng.pdf` |

## Model matrix (LOCKED)

| Role | Model |
|------|-------|
| Coordinator | `inherit` |
| Librarian | `claude-sonnet-5-thinking-high` (**never** `claude-fable-5-thinking-high`) |
| Implementer — structure / OCR / rename | `composer-2.5-fast` |
| Implementer — teaching / WarCom research | `claude-sonnet-5-thinking-high` |
| QA — default | `gpt-5.6-sol-medium` |
| QA — light | `gemini-3.7-flash-high` |
| Final Sanity | `gpt-5.6-terra-medium` |

If Sonnet unavailable: waive within Claude family to `claude-opus-5-thinking-high` only; record waiver. Keep Implementer and QA on different families for the same slice.

### Model waivers

| Slice | Locked | Actually used | Basis | Recorded in |
|-------|--------|---------------|-------|-------------|
| S1 resume + S1b–FS | Sonnet / sol / terra | Coord `inherit` hats | Parallel children stalled/incomplete; no new subagents on continue | This track_in + final report |

## Slice sequence

```
Preflight → S0 → (S1 ∥ S1b) → L1 → S2 → S3 → L2 → Final Sanity
```

## Rollup

| Slice | Focus | Agent / model | QA model | Status |
|-------|--------|---------------|----------|--------|
| **Preflight** | Confirm PDFs; lock OCR path; briefs | Coord / inherit | Coord light | Resolved - Complete |
| **S0** | Delete mislabeled file; rename joint_ops; stubs | `composer-2.5-fast` | `gemini-3.7-flash-high` | Resolved - Complete |
| **S1** | Full dossier OCR sidecar | `composer-2.5-fast` + Coord resume | Coord light (intended sol) | Resolved - Complete |
| **S1b** | WarCom free stats + Community PDFs | Coord (intended Sonnet) | Coord light | Resolved - Complete |
| **L1** | KB ingest (OCR + WarCom; no OCR paste) | Coord (intended Sonnet) | Coord light | Resolved - Complete |
| **S2** | Fill nemesis_ops/ + How-To | Coord (intended Sonnet) | Coord light | Resolved - Complete |
| **S3** | Slim catalog §5; Gaps; greps | Coord (intended Sonnet) | Coord light | Resolved - Complete |
| **L2** | Lint links/confidence/dates | Coord (intended Sonnet) | Coord light | Resolved - Complete |
| **Final Sanity** | Cross-slice audit + final report | Coord (intended terra) | — | Closed - Complete |

## Pending commits (Coordinator)

This track creates artifacts **without** `git commit` / `git push` until the user asks. Suggested batches when ready:

1. Track bootstrap + Preflight + S0 (delete scrub notes, rename, stubs)
2. S1 pointer OCR metadata + S1b WarCom/community pointers (no OCR binary)
3. L1 KB ingest
4. S2 nemesis_ops shipping pages
5. S3 joint_ops reconcile + L2 lint
6. Final Sanity report

**Do not commit** until the user explicitly asks.

## Cross-track note (rename — applied S0, 2026-08-17)

`kill_team_2024_scaffold` historically shipped under `games/kill_team_2024/join_ops/`. This track renamed that directory to **`joint_ops/`** and added **`nemesis_ops/`** stubs. Closed scaffold slice reports under `docs/handoffs/kill_team_2024_scaffold/slices/` are **not** mass-rewritten; both tracks' `track_in.md` record the rename and mislabeled-file deletion.

## Secrets / copyright

- No `.env` or credentials
- No GW PDFs / OCR / Community Content binaries committed
- Teaching paraphrase in git only
- Dossier OCR datasheets forbidden in repo
- WarCom free numbers only with URL + retrieval date
- Community claims always `draft` + stale-risk

## Open blockers

| Item | Status |
|-------|--------|
| OCR tool availability (tesseract / ocrmypdf) | **Resolved S1** — Tesseract 5.4.0 + PyMuPDF 1.27.2; sidecar beside dossier |
| WarCom free-statline coverage unknown until S1b | **Resolved 2026-08-17 (S1b): no free numeric statlines exist for any Nemesis Operatives content.** See `games/kill_team_2024/nemesis_ops/WarCom_Free_Statlines.md`. |
| Hierotek / S10 / scaffold leftovers | Out of scope this track |
