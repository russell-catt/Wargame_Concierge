# CLEANUP — Brief (remove staging PDFs before main)

- **Track:** `dataslate_0826`
- **Slice:** CLEANUP
- **Status:** Ready (run after extracts; **required before squash-merge to main**)
- **Depends:** S3 (and any other slices that needed staging PDFs) Complete or waived
- **Recommended models:** Implementer `claude-sonnet-5-thinking-high` · QA `gpt-5.6-sol-high`

## Requirements

1. Delete all files under `raw/_dataslate_0826_staging/` except keep or remove `README.md` (prefer delete entire folder once empty of PDFs, or leave README stating “staging closed”).
2. Remove the **TEMPORARY** `!raw/_dataslate_0826_staging/` negation block from `.gitignore`.
3. Revert `raw/README.md` staging row (or mark Closed / removed).
4. Confirm `git ls-files '*.pdf'` / `*.PDF` lists **only** Warcode-exempt paths (if any).
5. Confirm research notes + pointers cite `C:\Personal\…` (or WarCom URLs), not the deleted staging paths as SoT.
6. Write `CLEANUP_implementer.md`.

## Exit criteria (QA verifies)

- [ ] No GW PDFs remain in the tree or git index (except Warcode exemption)
- [ ] `.gitignore` TEMPORARY block gone
- [ ] Staging folder gone or PDF-empty with closed README
- [ ] Subagent did not leave binaries staged for main

## Constraints

User authorized temporary staging only. Cleanup is part of the ship bar for this track.
