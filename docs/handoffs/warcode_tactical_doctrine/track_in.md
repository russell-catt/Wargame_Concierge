# Track in — warcode_tactical_doctrine

- **Project:** Wargame_Concierge
- **Track:** `warcode_tactical_doctrine`
- **Status:** In Progress — Preflight locked 2026-08-23
- **Git root:** `C:\Personal\Personal_Projects\Wargame_Concierge`
- **Branch:** `feature-Warcode`
- **Plan:** Cursor plan `warcode_tactical_doctrine_0b3c475b` (do not edit plan file)
- **Archive:** [`reference/Warcode_Tactical_Doctrine_Plan.md`](../../../reference/Warcode_Tactical_Doctrine_Plan.md)
- **Handoffs root:** `docs/handoffs/warcode_tactical_doctrine/`
- **Playbook:** `docs/operations/multiagent_coordinator_strategy.md`
- **Checklist:** `docs/Game_System_Scaffold.md` §§A2–F

## Goals

Bootstrap **The Warcode** as system #3 (`the_warcode`):

1. Commit free beta rulebook under `raw/the_warcode/` (gitignore exemption)
2. Full-quote rules corpus + deep-dives under `games/the_warcode/`
3. KB ingest (`system: the_warcode`) with That other game collision flags
4. Cross-game guides (vs That other game, proxy play, TTS, STL)
5. First-game walkthrough + Protagen / Ulfari quoted datasheets
6. Comparative glossary (That other game bridges)
7. Agentic Rules & Marketing Review (manifests → GATE → polished VIP doc)

## Locked decisions

| Decision | Choice |
|----------|--------|
| System slug | `the_warcode` |
| Force folder | `factions/` |
| Quote policy | Free beta → full verbatim under `games/the_warcode/{rules,setup,factions}/` + `raw/the_warcode/` |
| PDF in git | `raw/the_warcode/The Warcode Rulebook V.0.8.7-F.pdf` — allowed binary |
| VIP / STL | $1 VIP only; no beta STLs; proxies until Gamefound Field Commander |
| TTS | Workshop subscribed in Steam; TTS **not owned** yet |
| Cross-game naming (shipping) | **Never** in `games/the_warcode/**` (any casing): Kill Team; Warhammer; Warhammer 40,000 / Warhammer 40K; 40,000; 40K; 40k. Use **That other game** / **Murder Platoon** / **Rawmallet** / **39.876** / **39.9** (AGENTS Sec 10 v0.5.5) |
| §0 / §15 review voice | Must include words **unofficial and unauthorized** |
| OCR | Protocol Cards and image-flattened pages — OCR required |
| Branch | `feature-Warcode` → PR squash merge to `main` |

## Constraints

- **No GW binaries in git** (unchanged)
- **Warcode beta PDF is the sole PDF exemption** under `raw/the_warcode/`
- **No STL binaries** in git
- **KB / docs** stay paraphrase (except handoffs may say KT24 for agents)
- **Librarian never commits**; Coordinator sole git owner for commits when user gates
- Never `claude-fable-5-thinking-high`

## Model matrix (LOCKED)

| Role | Model |
|------|-------|
| Coordinator | `inherit` |
| Researcher (R1–R4) | `claude-sonnet-5-thinking-high` |
| Librarian (L0–L2) | `claude-sonnet-5-thinking-high` |
| Implementer — structure | `composer-2.5-fast` |
| Implementer — teaching / quotes / review | `claude-sonnet-5-thinking-high` |
| QA | `gemini-3.7-flash-high` |
| Final Sanity | `gpt-5.6-terra-medium` |

## Rollup

| Slice | Focus | Status |
|-------|--------|--------|
| Preflight | Lock constraints + model matrix | Resolved - Complete |
| S0 | PDF + schema + tree | Pending |
| R1–R4 | Review manifests | Pending |
| GATE | User lock | Pending |
| L0 / S1–S8 / S7 / L1 / L2 / FS | Per plan | Pending |

## Open blockers

- TTS workshop URL — user provides before/during S5
- GATE user sign-off required before S7 polish
- §13 non-agentic VIP view — user fills after S7

## Pending commits

Coordinator commits on user ask. Suggested batches after slices resolve.
