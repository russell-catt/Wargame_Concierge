# L2 — Brief (Audit v1_scaffold L2 + lint)

- **Status:** Ready
- **Track:** `tomb_world_ownership`
- **Slice:** L2 (Librarian, Tier 0)

## Requirements

1. Audit prior **v1_scaffold** L2 artifacts for completeness vs brief exit criteria:
   - `docs/handoffs/v1_scaffold/slices/L2_brief.md`
   - `docs/handoffs/v1_scaffold/slices/L2_librarian.md`
   - `docs/handoffs/v1_scaffold/slices/L2_qa.md`
2. Produce completeness checklist (YES/NO per exit criterion)
3. If audit incomplete **OR** ownership edits reintroduce drift → re-execute full Librarian lint
4. Clear false **"Tomb World not owned"** claims across KB
5. Write `L2_librarian.md` with audit results + lint report

## Exit criteria

- Completeness checklist against v1_scaffold L2 brief exit criteria
- Full lint run if triggered; drift items listed with fixes applied or flagged
- No remaining false Tomb World ownership denials in KB
- `L2_librarian.md` documents audit + lint
- Append `KB/log.md` + `KB/changelog.md`
- **No commit, no push**

## Recommended models

| Role | Model |
|------|-------|
| Librarian | `claude-fable-5-thinking-high` |
| QA | `gemini-3.7-flash-high` |

## Depends

| Dependency | Notes |
|------------|-------|
| L1 Resolved - Complete | YES |
| **Commit** | pending — S4 |
| **Push** | pending — S4 |