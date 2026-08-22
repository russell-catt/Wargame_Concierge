# L0 — Brief (KB ingest — SM Matched/Casual + Legends)

- **Track:** `sm_matched_vs_casual`
- **Slice:** L0
- **Status:** Draft — awaiting track authorization
- **Depends:** S2 Complete (Matched truth); **re-sync after S4** Casual lands
- **Recommended models:** Librarian `inherit` · Lib-QA different family when available

## Inherited documentation

AGENTS.md §§2, 6, 9–11; `KB/ingest_procedure.md`; shipping under `games/.../space_marines/` after S2/S4; Servitors Legends notes from inventory / PR #6.

## Requirements

1. Read all SM shipping docs changed by this track (and recent Servitors/starter churn).
2. Create/update as warranted:
   - `KB/sources/` — WarCom Legends SM PDF + Marines MFM stubs with **retrieval dates**
   - `KB/glossary.md` — Warhammer Legends, matched play, Astartes Servitors (glossary-only)
   - `KB/factions/` — Space Marines / Blood Ravens draft if missing
   - `KB/units/` — Techmarine, Astartes Servitors (Legends), key list units as stubs/drafts
   - `KB/analyses/` — short note that Matched vs Casual list lines exist (detail in L1)
3. Update `KB/index.md`, append `KB/log.md` ingest row.
4. Teaching paraphrase only; Codex wall; never write `raw/`.

## Exit criteria (Lib-QA)

- [ ] Frontmatter valid on every new/updated KB page (`confidence` mandatory)
- [ ] Glossary terms added same pass; conflicts flagged not overwritten
- [ ] Wikilinks + back-links for touched pages
- [ ] Index + log updated
- [ ] No verbatim datasheet/stratagem dumps; no binaries
- [ ] Re-sync note if L0 ran before S4 — second pass logged
