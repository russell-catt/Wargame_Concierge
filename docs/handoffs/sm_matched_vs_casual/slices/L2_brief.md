# L2 — Brief (lint SM churn + this track)

- **Track:** `sm_matched_vs_casual`
- **Slice:** L2
- **Status:** Draft — awaiting track authorization
- **Depends:** L1 Resolved - Complete
- **Recommended models:** Librarian `inherit` · Lib-QA different family

## Requirements

Lint in scope: all KB pages touched by L0/L1 + SM shipping references this track created.

Report then apply **approved** fixes only:

- Contradictions (Matched page still costing Legends; Casual missing banners)
- Edition drift / stale Legends claims
- Orphans, missing back-links
- Glossary inconsistency
- `unverified`/`stub` pages relied on by analyses
- Missing retrieval dates on living-ref claims

Append `KB/log.md` lint row. Propose fixes in `L2_librarian.md`; apply only what Coordinator/user approved (for this track: apply non-controversial link/glossary fixes; flag rules contradictions for human).

## Exit criteria (Lib-QA)

- [ ] Lint report lists issues found + fixes applied
- [ ] Log row present
- [ ] No silent history rewrite when source contradicts KB — contradictions flagged
- [ ] No `raw/` writes
