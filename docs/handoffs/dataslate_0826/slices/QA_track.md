# QA — Track notes (Tier 2)

- **Track:** `dataslate_0826`
- **Model (locked):** `gpt-5.6-sol-high` — **must differ** from Implementer (`claude-sonnet-5-thinking-high`)
- **Skill:** [`.cursor/skills/qa-slice/SKILL.md`](../../../../.cursor/skills/qa-slice/SKILL.md)

## Per-slice QA artifacts

After each Implementer/Librarian slice reaches Tier 1, QA writes:

| After | Artifact |
|-------|----------|
| S0 | `S0_qa.md` |
| S1 | `S1_qa.md` |
| S2 | `S2_qa.md` |
| S2b | `S2b_qa.md` |
| S3 | `S3_qa.md` |
| S4 | `S4_qa.md` |
| S5 | `S5_qa.md` |
| L1 | `L1_lib_qa.md` |

## Required content in every `*_qa.md`

1. Model used (confirm ≠ Implementer family).
2. Gate: PASS / FAIL / PASS-with-caveats.
3. Exit-criteria checklist from the brief (tick/cross).
4. **Legibility spot-check table** (file → what was read → scannable? Y/N → notes).
5. Layer/copyright/footer checks per qa-slice skill.
6. On FAIL: `*_qa_reopen.md` + reopen Implementer.

## Legibility bar (this track)

A page fails legibility if any of:

- Currency / dataslate date buried where players cannot see it near the top or footer
- Banner/callout missing on list/QR pages that other siblings have
- Diff introduced a dense undifferentiated wall (>~40 lines without headers)
- Print HTML spills past locked page count without waiver

## Independence

QA re-reads files and pointers; does not rubber-stamp Implementer prose.
