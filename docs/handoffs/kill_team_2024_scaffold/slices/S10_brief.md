# S10 — Brief (Photos → Tarot unit cards) — USER-GATED

- **Status:** Blocked — awaiting user photos
- **Track:** kill_team_2024_scaffold
- **Slice:** S10

## Requirements (when unblocked)

1. Ingest user photos of owned kill teams (local path outside git binaries policy, or in-session attach)
2. Complete operative/unit breakdown per team (loadout, base size, dual-legality)
3. Printable teaching unit cards for Tarot sleeves (~70×120 mm footprint family)
4. Priority: Canoptek Circle, Plague Marines, Angels of Death; then remaining seven
5. Schema: `games/kill_team_2024/teams/{team}/cards/Card_Schema.md` + one card per operative
6. No GW card art / publisher scans

## Blocker

No photos provided this session (2026-08-17). Do not invent operative ownership from memory.

## Recommended models

| Role | Model |
|------|-------|
| Implementer | `claude-sonnet-5-thinking-high` |
| QA | `gpt-5.6-sol-medium` |
