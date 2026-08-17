# L1 — Brief (KB ownership ingest)

- **Status:** Ready
- **Track:** `tomb_world_ownership`
- **Slice:** L1 (Librarian, Tier 0)

## Requirements

Update KB files to match locked FOUNDATION:

1. `KB/sources/necron_lists_owner_notes.md`
2. `KB/factions/necrons.md`
3. `KB/glossary.md`
4. `KB/overview.md`
5. `KB/sources/source_library.md`
6. `KB/analyses/inherited_docs_for_S3.md`

Append entries to `KB/log.md` and `KB/changelog.md`.

Remove **"do not let Tomb World leak"** as a current rule — Tomb World is owned and preferred for learning.

## Exit criteria

- All six KB targets reflect Tomb World game-ready ownership
- Dual Warriors / Scarabs inventory documented
- Hierotek TBD thread preserved
- Log + changelog appended with L1 ingest note
- **Librarian did not write `raw/`**
- **No commit, no push**

## Recommended models

| Role | Model |
|------|-------|
| Librarian | `claude-fable-5-thinking-high` |
| QA | `gpt-5.6-sol-medium` |

## Depends

| Dependency | Notes |
|------------|-------|
| S3 Resolved - Complete | YES |
| **Commit** | pending — S4 |
| **Push** | pending — S4 |