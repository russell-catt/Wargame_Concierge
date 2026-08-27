# L0 — Brief (Librarian source stubs)

- **Track:** `dataslate_0826`
- **Slice:** L0
- **Status:** Ready (may start after S0 dates lock; before shipping finish OK for stubs)
- **Depends:** S0 dates locked (QA-S0 preferred)
- **Recommended models:** Librarian `claude-sonnet-5-thinking-high` · QA deferred to QA-L1 with L1

## Requirements

1. Create KB source stubs:
   - `KB/sources/warcom_balance_dataslate_40k_0826.md` (name may adjust to locked product title)
   - `KB/sources/warcom_balance_dataslate_kt_0826.md`
2. YAML frontmatter per AGENTS Sec 6; `confidence: draft`; retrieval dates; pointer paths in `sources:`.
3. One-line summaries suitable for `KB/index.md`.
4. Do **not** write under `raw/`.
5. Write `L0_librarian.md`.

## Exit criteria

- [ ] Two source pages exist with dates + WarCom URLs
- [ ] Teaching paraphrase only
- [ ] Index rows optional until L1
- [ ] Librarian did not git / did not write raw/

## Constraints

KB owns paraphrase; no dataslate dump.
