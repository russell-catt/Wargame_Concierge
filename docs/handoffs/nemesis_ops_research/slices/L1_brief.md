# L1 — Brief (KB ingest from OCR + WarCom)

- **Status:** Ready (dispatch after S1 + S1b Resolved - Implemented)
- **Track:** nemesis_ops_research
- **Slice:** L1
- **Intended Librarian model:** `claude-sonnet-5-thinking-high` (**never** fable)
- **Intended QA model:** `gpt-5.6-sol-medium`

## Requirements

1. Refresh `KB/sources/nemesis_operatives.md` — OCR now available (cite pointer + tool/date); eng.pdf deleted; confidence remains honest (process claims from OCR paraphrase; no datasheet paste)
2. Add WarCom source page(s) for free-statline articles used in `WarCom_Free_Statlines.md` (URL + retrieval date)
3. Optional KB source page(s) for the two community PDFs with low trust / stale-risk note (or fold into one community sources stub)
4. Concepts: Custom Builder / create-a-Nemesis if content earns a `KB/concepts/` page; else glossary stubs in `KB/glossary.md`
5. Update `KB/index.md`, `KB/overview.md` if needed, append `KB/log.md`
6. **Never** paste dossier OCR verbatim / datasheets into KB
7. File `L1_librarian.md` — Commit: pending

## Depends

S1 + S1b Resolved - Implemented (or Complete).

## Exit criteria

- KB sources refreshed; index/log updated
- No OCR datasheet text in KB
- Community sources clearly draft/secondary
- `L1_librarian.md` filed
