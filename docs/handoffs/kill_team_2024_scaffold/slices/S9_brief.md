# S9 — Brief (Join Ops pack)

- **Status:** Resolved - Complete
- **Track:** kill_team_2024_scaffold
- **Slice:** S9
- **Locked model:** `claude-sonnet-5-thinking-high` (Implementer + Librarian-assist) — **never** `claude-fable-5-thinking-high`

## Requirements

Create under `games/kill_team_2024/join_ops/`:

1. `README.md` — What Join Ops / Joint Ops is (cooperative or solo vs NPOs); how two players share one kill team vs NPOs; link to priority human teams (Canoptek Circle, Plague Marines, Angels of Death); first-session shortlist favoring Volkus and 3e Starter; cite Nemesis Operatives local PDFs.
2. `NPO_Catalog.md` — Catalog of released NPO / Nemesis Operative content to date, teaching paraphrase only, primary local SoT pointers to the two owned Nemesis Operatives PDFs, cross-checked against Wahapedia's Kill Team 3 missions page and WarCom/Lexicanum, known example Nemesis types from public summaries, generic NPO behaviour archetypes, GAPS marked where a release is known online but missing/unreadable locally. **Never transcribe datasheet numbers/statlines.**
3. `NPO_Cheat_Sheet.md` — 1–2 page print-friendly mid-game table aid: activation/behaviour reminders, common action loop, cover/engagement habits, do this/don't forget prompts. Distinct from Community Content cheat sheets (out of scope).
4. `Playable_Scenarios_Owned_Terrain.md` — Matrix of scenario × required killzone × owned? × Join Ops suitable? × notes, first sessions at top, honest about unassembled Tomb World, White Dwarf/secondary-trust row labelled.

Also optionally create a `KB/sources/` stub for Nemesis Operatives if L1 hadn't covered it (system: `kill_team_2024`).

Write `S9_brief.md` and `S9_implementer.md` under `docs/handoffs/kill_team_2024_scaffold/slices/`.

## Hard constraints

- No binaries (no `.pdf`/`.webp`/etc. added to the repo)
- No `git commit` / `git push` — Coordinator-owned
- UTF-8
- Teaching paraphrase only — never transcribe datasheet numbers, statlines, or ploy/mission text verbatim
- Community Content out of scope

## Depends / User gate

| Dependency | Notes |
|------------|-------|
| Preflight, S0 | Resolved - Complete |
| S2 (killzone pages) | May still be running when S9 starts — link real pages if present, otherwise link planned paths under `setup/killzones/` and update once S2 lands |
| L1 (KB ingest) | May or may not have covered Nemesis Operatives specifically — check before creating the optional KB stub |

## Entrance criteria

| Criterion | Attested |
|-----------|----------|
| `join_ops/` stub exists (from S0) | Verify |
| Two Nemesis Operatives PDFs resolve on disk | Verify |
| Mission-pack and terror-on-devlan pointers resolve | Verify |

## Exit criteria

- All four `join_ops/` files created, paraphrased, dated 2026-08-17
- `NPO_Catalog.md` cites both local Nemesis Operatives PDFs and cross-checks Wahapedia/WarCom/Lexicanum, with a Gaps section
- `NPO_Cheat_Sheet.md` prints to roughly 1–2 pages and is explicitly distinguished from Community Content sheets
- `Playable_Scenarios_Owned_Terrain.md` lists first sessions at top, has an honest Tomb World row, and a labelled White Dwarf/secondary-trust row
- No datasheet numbers/statlines anywhere in the four files
- `S9_implementer.md` filed with file list and gaps
- Zero new binaries added to the repo working tree

## Tier 1 commands

```powershell
$root = 'C:\Personal\Personal_Projects\Wargame_Concierge'
Test-Path "$root\games\kill_team_2024\join_ops\README.md"
Test-Path "$root\games\kill_team_2024\join_ops\NPO_Catalog.md"
Test-Path "$root\games\kill_team_2024\join_ops\NPO_Cheat_Sheet.md"
Test-Path "$root\games\kill_team_2024\join_ops\Playable_Scenarios_Owned_Terrain.md"
@(Get-ChildItem $root -Recurse -Include *.pdf,*.webp -File -ErrorAction SilentlyContinue).Count -eq 0
```

## Tier 2 expectations

QA confirms: no statline transcription; Nemesis Operatives gap (unreadable dossier scan + mislabeled second file) is clearly flagged rather than papered over; first-session shortlist matches the track's Volkus/3e-Starter priority; Community Content is never cited; killzone links resolve correctly against whatever S2 state exists at review time.

## Recommended models

| Role | Model |
|------|-------|
| Implementer + Librarian-assist | `claude-sonnet-5-thinking-high` |
| QA | `gpt-5.6-sol-medium` |

## Inherited documentation

- `track_in.md` — Join Ops goals, ownership tables, play-now priority (Volkus + 3e Starter → Shadowhunt → Tomb World → 2e filler)
- `raw/pointers/kill_team_2024_nemesis_operatives.md`, `kill_team_2024_missions.md`, `kill_team_2024_terror_on_devlan.md`, `kill_team_2024_screen_captures.md`, `kill_team_web_living_sources.md`
- S0 pointer/stub style precedent
