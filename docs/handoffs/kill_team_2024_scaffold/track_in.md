# Track in — kill_team_2024_scaffold

- **Project:** Wargame_Concierge
- **Track:** `kill_team_2024_scaffold`
- **Status:** In Progress — major slices landed 2026-08-17; Final Sanity + commits pending user
- **Git root:** `C:\Personal\Personal_Projects\Wargame_Concierge`
- **Plan:** Cursor plan `kill_team_2024_scaffold_9ae107e8` (do not edit plan file)
- **Handoffs root:** `docs/handoffs/kill_team_2024_scaffold/`
- **Playbook:** `docs/operations/multiagent_coordinator_strategy.md`
- **Checklist:** `docs/Game_System_Scaffold.md` §§A2–F
- **External libraries (read-only):**
  - `C:\Personal\Kill Team\kill_team_2024\` (KT24 / 3e — primary)
  - `C:\Personal\Kill Team\kill_team_2021\` (KT21 / 2e — archive only)
- **Spine (Scaffold §A):** Already done — skip

## Goals

Add **Kill Team 2024 (KT24 / 3e)** as the second game system:

- Path pointers + KB ingest (`system: kill_team_2024`)
- Teaching content under `games/kill_team_2024/` (`teams/`, not `armies/`)
- Owned inventories, kill-zone refs, Critical Ops notes
- Full play guides: **Canoptek Circle**, **Plague Marines**, **Angels of Death**
- **Join Ops** pack: NPO catalog, NPO cheat sheet, playable-scenario matrix (father–son co-op)
- Read-only 2e archive under `reference/kill_team_2e/`
- Sync ruled-in KT miniatures into matching 40K inventories with **base-size / dual-legality** honesty

## Constraints

- **No GW binaries in git** — PDFs, webp, official images stay outside repo; markdown path pointers only
- **Teaching paraphrase only** — never transcribe datasheets / statlines / ploy text verbatim
- **Librarian never writes `raw/`**; never commits
- **Subagents never commit or push** — Coordinator sole git owner
- **Community Content** folder out of scope this track (including community NPO cheat sheets)
- **Screen_Captures** — path pointers only; White Dwarf / secondary trust; never override official rules PDFs
- Former flat `C:\Personal\Kill Team\rules\` paths are **obsolete** — use `kill_team_2024\` / `kill_team_2021\`
- **Do not commit** in this execution session unless the user explicitly asks; note pending commits below
- Hierotek Circle 40K photo-ID remains TBD (KT inventory can list operative names from team PDF without 40K mapping)
- S10 Tarot cards gated on user photos — skip until photos arrive

## Cross-game policy (locked)

Kill Team and Warhammer 40,000 are **separate games** (separate `system:` tags, separate rules/glossary pages). They share a **collection**:

| Rule | Detail |
|------|--------|
| Rules stay split | Never merge KT and 40K rules pages |
| Inventories sync | When a KT team inventory lands, list those miniatures in the matching 40K army inventory with provenance “Kill Team ownership” |
| Base-size legality | Owned ≠ dual-legal. Record base size, Legal for KT?, Legal for 40K? (or `pending check`) |
| Template | Canoptek Circle → Necron `Owned_Models_Inventory.md` (and related lists) with dual-legality notes |
| Cross-links | “Same physical models / different game rules” |

## Join Ops goals (father–son)

Required shipping deliverables under `games/kill_team_2024/join_ops/` (historical path; **live path renamed to `joint_ops/`** by follow-on track [`nemesis_ops_research`](../nemesis_ops_research/track_in.md) S0, 2026-08-17):

1. `NPO_Catalog.md` — all released NPOs / Nemesis Operatives to date
2. `NPO_Cheat_Sheet.md` — easy 1–2 page mid-game aid
3. `Playable_Scenarios_Owned_Terrain.md` — scenarios × owned kill zones
4. `README.md` — how Join Ops works + first-session shortlist

**Play-now priority:** Volkus and 3e Starter Set → Shadowhunt → Tomb World (after assembly) → 2e scatter as filler only.

## Ownership assumptions (Preflight lock — 2026-08-17)

### Owned teams (10 PDFs under `kill_team_2024\Teams\`)

| Team | Priority | Notes |
|------|----------|-------|
| Canoptek Circle | Full guide (S4) | Necron KT; 40K ruled-in template |
| Plague Marines | Full guide (S5) | Death Guard; 40K sync where mapping known |
| Angels of Death | Full guide (S6) | Space Marines; 40K sync where mapping known |
| Hierotek Circle | Stub (S3) | Game-ready used set in 40K inventory; **photo ID TBD** for 40K datasheets |
| Celestian Insidiants | Stub | |
| Death Korps | Stub | |
| Deathwatch | Stub | |
| Kommandos | Stub | |
| Murderwing | Stub | |
| Vespid Stingwings | Stub | |

Assembly/paint notes for the three guide teams: **not yet confirmed in detail** this Preflight — inventory rows use `pending check` until user confirms or photos arrive (S10). Hierotek remains photo-gated for 40K mapping.

### Kill zones

| Kill zone | Status |
|-----------|--------|
| Volkus | Ready (play-now) |
| 3e Starter Set | Ready (play-now) |
| Shadowhunt | Boards + tokens owned |
| Tomb World | Unassembled |
| 2e starter scatter | Filler terrain only |

### Critical Ops

Both physical decks owned (2024 + 2025) under `kill_team_2024\Critical Ops\`.

### Local library layout (confirmed 2026-08-17)

```
C:\Personal\Kill Team\
├── Community Content\          # OUT OF SCOPE
├── kill_team_2021\             # 2e archive PDFs
└── kill_team_2024\             # current play edition
    ├── Teams\                  # 10 team-rule PDFs
    ├── Critical Ops\2024\      # Cards (A4) 1–5.pdf
    ├── Critical Ops\2025\      # deck printables
    ├── Screen_Captures\        # WD517 Necrons + Procession PvE (.webp — never commit)
    ├── Core / lite / update logs / approved ops / universal equipment
    ├── Mission packs (Tomb World, Shadowhunt, Volkus, Hivestorm, Titus, Terror on Devlan, …)
    ├── Terror on Devlan Dossier
    └── Nemesis Operatives — dossier PDF present but image-scan/no OCR; mislabeled Nemesis Claw retailer listing deleted 2026-08-17 (nemesis_ops_research S0) — see open blockers
```

## Model matrix (LOCKED)

| Role | Model |
|------|-------|
| Coordinator | `inherit` |
| Librarian | `claude-sonnet-5-thinking-high` (**never** `claude-fable-5-thinking-high`) |
| Implementer — structure / pointers | `composer-2.5-fast` |
| Implementer — teaching content | `claude-sonnet-5-thinking-high` |
| QA — default | `gpt-5.6-sol-medium` |
| QA — light | `gemini-3.7-flash-high` |
| Final Sanity | `gpt-5.6-terra-medium` |

If Sonnet unavailable: waive within Claude family to `claude-opus-5-thinking-high` only; record waiver. Never select fable. Keep Implementer and QA on different families for the same slice.

### Model waivers

| Slice | Locked | Actually used | Basis | Recorded in |
|-------|--------|---------------|-------|-------------|
| *(none yet)* | | | | |

## Rollup

| Slice | Focus | Agent / model | QA model | Status |
|-------|--------|---------------|----------|--------|
| **Preflight** | Lock ownership + cross-game policy | Coord / `composer-2.5-fast` | Coord light | Resolved - Complete (PASS) |
| **S0** | Pointers + tree stub + Source_Library + 2e README | `composer-2.5-fast` | Coord light | Resolved - Complete (PASS) |
| **L1** | Core rules ingest + glossary collisions | `claude-sonnet-5-thinking-high` | pending formal QA | Resolved - Complete |
| **S1** | Rules teaching docs | `claude-sonnet-5-thinking-high` | pending formal QA | Resolved - Complete |
| **S2** | Setup + killzones + Crit Ops README | `claude-sonnet-5-thinking-high` (Coord landed) | pending | Resolved - Complete |
| **L2** | Teams + killzones + Join Ops KB | `claude-sonnet-5-thinking-high` | — | Partial / deferred |
| **S3** | Owned inventory + 7 stubs | `composer-2.5-fast` | pending | Resolved - Complete |
| **S4** | Canoptek Circle full + 40K sync | `claude-sonnet-5-thinking-high` | pending | Resolved - Complete |
| **S5** | Plague Marines full | `claude-sonnet-5-thinking-high` | pending | Resolved - Complete (inventory worksheet) |
| **S6** | Angels of Death full + SM cross-link | `claude-sonnet-5-thinking-high` | pending | Resolved - Complete (inventory worksheet) |
| **S7** | Killzone QR + Crit Ops how-to | Coord / sonnet intended | pending | Resolved - Complete |
| **S9** | Join Ops pack | `claude-sonnet-5-thinking-high` | pending | Resolved - Complete (Nemesis local-PDF gaps recorded) |
| **L3** | Lint | Coord light note | — | Partial findings filed |
| **S8** | KT21 / 2e archive | `claude-sonnet-5-thinking-high` | pending | Resolved - Complete |
| **S10** | Photos → Tarot cards | — | — | **Blocked — no photos** |
| **Final Sanity** | Cross-slice audit | `gpt-5.6-terra-medium` | — | pending |

**Depends:** Preflight → S0 → L1 → S1 → S2 → (S9 pipelined) → L2 → S3 → S4 → S5 → S6 → S7 → S9 → L3 → S8 → FS → (S10 when photos)

## Pending commits (Coordinator)

This session created artifacts **without** `git commit` / `git push`. When ready, suggested batches:

1. Track bootstrap + Preflight + S0 (pointers, tree, Source_Library)
2. L1 KB ingest
3. S1–S3 + S2 setup (rules, inventory stubs, killzones)
4. S9 Join Ops (high value alone or with S2)
5. S4–S6 team packages + 40K cross-links
6. S7 + S8 + L3 note
7. Final Sanity after formal QA

**Do not commit** until the user explicitly asks.

## Secrets / copyright

- No `.env` or credentials
- No GW PDFs/images committed
- White Dwarf Screen_Captures stay outside git; cite as secondary trust
- Community Content never treated as authoritative

## Follow-on track note (2026-08-17)

Nemesis Operatives OCR, mislabeled-file deletion, and `join_ops` → `joint_ops` rename are owned by follow-on track [`nemesis_ops_research`](../nemesis_ops_research/track_in.md). **Live shipping path is `games/kill_team_2024/joint_ops/`** (renamed S0, 2026-08-17); new `nemesis_ops/` stubs ship from the same track. Do **not** mass-rewrite closed slice reports in this folder for path renames.

## Open blockers

| Item | Status |
|------|--------|
| Hierotek Circle photo ID (40K datasheet mapping) | Open — carry from 40K track |
| S10 user photos of owned teams | Blocked — no photos this session |
| 3e Starter Handbook PDF | Gap — not on disk; pointer stub `raw/pointers/kill_team_2024_starter_set.md` |
| Nemesis Operatives dossier PDF | **Moved to** `nemesis_ops_research` (full OCR pass — S1) |
| Mislabeled Nemesis Claw retailer listing (local) | **Deleted 2026-08-17** (nemesis_ops_research S0); primary source is dossier only |
| `join_ops/` shipping path | **Renamed to** `joint_ops/` (nemesis_ops_research S0, 2026-08-17) |
| Guide-team assembly/paint detail | Pending user confirmation; use pending-check rows |
| Critical Ops 2026 | Out of scope (note only) |
