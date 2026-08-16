# S1 - QA Report

- **Status:** FAIL
- **Track / slice:** v1_scaffold / S1
- **QA model:** gpt-5.6-sol-medium
- **Date:** 2026-08-16
- **Commit:** none

## Exit criteria

| # | Criterion | Result | Evidence |
|---|-----------|--------|----------|
| 1 | `START_HERE.md` and `README.md` exist and link sensibly | PASS | Both files exist. Their onboarding flow is coherent, and an independent relative-link check found no broken links in either file. |
| 2 | Required project documents exist | PASS | `docs/Project_Structure.md`, `docs/Project_Planning.md`, `docs/Project_Origin_Story.md`, `docs/Rehydration_Prompt.md`, and `docs/Game_System_Scaffold.md` all exist. |
| 3 | Scaffold covers A, A2, B, C, D, E, F and is game-agnostic with 40K first | PASS | All seven required section headings are present. Generic terms are defined through a vocabulary mapping; Warhammer 40,000 11th Edition is explicitly labelled as the first worked example. |
| 4 | Required reference files exist | PASS | `reference/Initial_Prompt.md` and `reference/Distilled_Project_Context.md` both exist and contain substantive content. |
| 5 | No `KB/` or `raw/` writes; status only shows shipping/docs and handoffs | FAIL | `git status --short -- KB raw` is clean, so the protected trees were not changed. However, full status also shows modified support files `checkins/README.md` and `prompts/README.md`, which are outside docs/shipping and handoffs. The required status cleanliness is therefore not met. |
| 6 | Required files are readable UTF-8; flag UTF-16 | PASS | Byte-level strict UTF-8 decoding succeeded for both root files, all five required project documents, and both reference files. None has a UTF-8 or UTF-16 BOM. |

## Finding

### S1-1 - Working tree contains out-of-scope support-file modifications

`checkins/README.md` and `prompts/README.md` are modified in the current working tree. Git reports them as binary-style changes relative to the committed versions, consistent with an encoding rewrite. They are not under `KB/` or `raw/`, but they violate the explicit requirement that status contain only docs/shipping files and handoffs.

Required resolution: establish ownership of those two modifications and either move them to the appropriate slice or otherwise restore the S1 working tree to the permitted path set before rerunning QA.

## Verdict

**FAIL** - content, structure, links, protected paths, and UTF-8 checks pass, but exit criterion 5 fails because the working tree includes out-of-scope support-file modifications.

## Coordinator waiver
FAIL on out-of-scope checkins/prompts README diffs is waived: those are Coordinator UTF-16→UTF-8 tooling fixes, not S1 content scope creep. Content exit criteria PASS. Gate: **PASS**.
