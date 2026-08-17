# S1b — Brief (WarCom free stats + Community Content)

- **Status:** Ready
- **Track:** nemesis_ops_research
- **Slice:** S1b
- **Intended Implementer model:** `claude-sonnet-5-thinking-high`
- **Intended QA model:** `gpt-5.6-sol-medium`

## Requirements

1. **Warhammer Community survey** for freely published Nemesis Operative / NPO / Custom Builder profiles. Search terms: Nemesis Operatives Dossier, Custom Builder, Ambull, Archivist, Zoat, Armoured Sentinel, Crisis Battlesuit, Screamer-Killer, Redemptor, NPO preview, Joint Ops, Adversary Ops.
2. Fill `games/kill_team_2024/nemesis_ops/WarCom_Free_Statlines.md` with a catalog table:
   - URL, title, retrieval date (2026-08-17 or actual fetch date), free statline/profile numbers published? (yes/no), which units/traits/numbers shown
   - Explicitly mark “no free WarCom statline found” where true — do not invent numbers
3. **Open and read** (outside git; never commit):
   - `C:\Personal\Kill Team\Community Content\The Kill Team 24 NPO Cheat Sheet Vers 1.1 ALTERNATIVE TEST.pdf`
   - `C:\Personal\Kill Team\Community Content\The Kill Team 24 Cheat Sheet Vers 1.21.pdf`
4. Cite community sheets as `draft` secondary with **stale-risk** always flagged; use for behaviour checklist ideas only where useful
5. Add `raw/pointers/` stubs for the two Community Content paths (no binary copy)
6. Prefer WarCom over community for numbers; dossier OCR for builder process (S2) — this slice does not paste OCR into git
7. File `S1b_implementer.md` — Commit: pending

## Depends

| Dependency | Notes |
|------------|-------|
| S0 Resolved - Implemented (stubs exist) | Required |
| May run in parallel with S1 | Yes |
| Do NOT commit Community PDFs | Absolute |

## Exit criteria

- `WarCom_Free_Statlines.md` catalog complete with retrieval dates
- Community vs official trust clear on every community-derived claim
- Two community pointer stubs exist
- No invented numbers
- `S1b_implementer.md` filed

## Copyright

- WarCom free stats OK with URL + date
- Community numbers never unmarked as official
- No dossier OCR paste into repo
