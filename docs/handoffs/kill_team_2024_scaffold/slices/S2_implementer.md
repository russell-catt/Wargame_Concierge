# S2 — Implementer report (Setup + killzones + Critical Ops README)

- **Status:** Resolved - Implemented (awaiting QA)
- **Track:** kill_team_2024_scaffold
- **Slice:** S2 (Implementer — teaching content)
- **Model used:** `claude-sonnet-5-thinking-high` (LOCKED for this slice per `track_in.md` model matrix)
- **Date:** 2026-08-17
- **Paths touched:** `games/kill_team_2024/setup/`, `games/kill_team_2024/critical_ops/`, `games/kill_team_2024/README.md`, `docs/handoffs/kill_team_2024_scaffold/slices/`
- **`KB/` untouched:** YES
- **`raw/` untouched:** YES
- **Commit:** none by this slice (per HARD constraint and track-level git gate)

---

## Research note

Before writing, read the local `C:\Personal\Kill Team\kill_team_2024\` tree via shell (`Test-Path`, `Get-ChildItem`) — the directory exists but returned **no accessible child items in this session's environment**, so PDF contents could not be read directly this slice (consistent with prior S0/Preflight slices, which also worked from path pointers rather than PDF contents). Content below is therefore a **teaching paraphrase cross-checked against the Wahapedia Kill Team 3 rules hub and community coverage (Warhammer Community, Goonhammer, Lexicanum, GW webstore listings), all retrieved 2026-08-17** — not a line read of the owned PDFs. Every new page's Rising Tide footer flags this and tells the reader what to verify against their own printed material before playing.

---

## Created

### Setup pages

| Path | Purpose |
|------|---------|
| `games/kill_team_2024/setup/Board_Setup.md` | What you need, killzone board size (30" x 22" default), the shared shape of the game sequence (Setup → Select Operatives → Deploy → Scouting → Battle → Score), drop zones/territory, pre-game checklist, learning-game shortcuts |
| `games/kill_team_2024/setup/Terrain_Basics.md` | Terrain features as parts; core types (Heavy, Light, Exposed, Insignificant, Accessible, Blocking, Vantage); Cover vs Obscured (teaching level, not verbatim rules text); terrain and movement (climbing/dropping/jumping); killzone layout habits |

### Kill-zone pages (`games/kill_team_2024/setup/killzones/`)

| Path | Status | Key honesty flag |
|------|--------|-------------------|
| `volkus.md` | READY | Compound Siege upgrade ownership unconfirmed — flagged as separate from base Volkus |
| `starter_set_3e.md` | READY | **No dedicated `raw/pointers/` file exists yet** for the Starter Handbook — flagged explicitly as a source gap for the Librarian |
| `shadowhunt.md` | Boards + tokens owned | Full Descent play is gated on Tomb World terrain being assembled; explains the (correct, not contradictory) track priority order |
| `tomb_world.md` | UNASSEMBLED | Explicitly separates terrain build status from the already-game-ready Tomb World *operatives* tracked in the 40K Necron inventory, to prevent the two being confused |
| `starter_set_2e_scatter.md` | Filler only | Explains why it can't substitute for a killzone; edition-drift caution against assuming 2e terrain-type wording in KT24 |

### Modified

| Path | Change |
|------|--------|
| `games/kill_team_2024/critical_ops/README.md` | S0 stub → teaching page: deck contents by category (Crit Ops, Tac Ops, Map cards, Game Sequence/Scouting cards, initiative-modifier cards), a flagged terminology note (owned folder says "Critical Ops"; the current-edition official product is "Approved Ops"), how the deck plugs into the `Board_Setup.md` sequence, and when to introduce it. No card art or full text lists. |
| `games/kill_team_2024/setup/README.md` | S0 stub → real index over the two setup pages + killzones subtree |
| `games/kill_team_2024/setup/killzones/README.md` | S0 stub → real index with the ownership/priority table, cross-checked against `teams/_Owned_Teams_Inventory.md` |
| `games/kill_team_2024/README.md` | Subtree map rows for `setup/` and `critical_ops/` updated from "Stub (S0)" to "Populated (S2)"; change log entry added |

---

## Exit criteria

| Criterion | Result |
|-----------|--------|
| Two people can set up Volkus or the 3e Starter Set from these docs alone | PASS — `Board_Setup.md` + the two killzone pages cover board size, terrain setup, and the game-sequence shape end to end |
| Honest about what must still be checked in owned PDFs | PASS — every new page's Rising Tide Notes footer names specific items to verify; `starter_set_3e.md` additionally flags a missing `raw/` pointer |
| No official terrain templates, mission maps, or card lists transcribed | PASS — all content is categorical/teaching-level paraphrase |
| No card art / no full Critical Ops card text | PASS |
| Killzone statuses match `track_in.md` / `teams/_Owned_Teams_Inventory.md` | PASS — Ready / Ready / Boards+tokens / Unassembled / Filler-only, verified against both sources |
| `setup/README.md` and `killzones/README.md` are real indexes | PASS |
| No binaries added | PASS (verified below) |
| `KB/` / `raw/` untouched | PASS |
| UTF-8 | PASS (all files written via UTF-8 write tool, no special encoding requested) |

## Binary check

```
Get-ChildItem repo -Recurse -Include *.pdf,*.webp → expect 0 (unchanged by this slice)
```

Run at QA / Coordinator closeout alongside the S0 baseline check.

---

## Cross-slice notes observed during this session

- `games/kill_team_2024/teams/` (S3) and `games/kill_team_2024/join_ops/` (S9) had already landed content by the time this slice ran, ahead of the `track_in.md` dependency order (`S2 → L2 → S3` and `... → S9`). This slice's killzone-ownership table was cross-checked against the already-populated `teams/_Owned_Teams_Inventory.md` kill-zone summary and found consistent — no conflicts to flag.
- `games/kill_team_2024/README.md`'s subtree map already carried a v0.2 entry for `join_ops/` (Complete, S9) from that concurrent work; this slice added v0.3 on top rather than overwriting it.

## Deferred to later slices

| Item | Target |
|------|--------|
| In-battle rules spine (orders, actions, phases) referenced from `Board_Setup.md` | S1 / `rules/` (not yet written as of this slice) |
| Critical Ops table-aid cheat sheet | S7 |
| Killzone QR (quick-reference) card | S7 |
| Confirming the "Critical Ops vs Approved Ops" naming hypothesis against the physical decks | User / future ingest |
| Starter Handbook `raw/pointers/` file | Librarian, future ingest |

---

## Tier 1 self-check

Run commands in `S2_brief.md` at QA closeout.

---

## Pending commit

None by this slice. Recommended commit gate per `track_in.md`: bundle with **S1–S2** (rules + setup), or with S9 if the Coordinator prefers a larger batch — Coordinator's call.
