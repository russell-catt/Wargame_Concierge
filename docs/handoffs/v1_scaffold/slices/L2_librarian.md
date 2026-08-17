# L2 Librarian report

- **Model waiver:** locked `claude-fable-5-thinking-high` unavailable → `claude-opus-5-thinking-high` / Coordinator completion after interrupt
- **raw/:** untouched
- **Ingest:** `KB/units/necrons_unit_index.md`, `KB/units/space_marines_unit_index.md` (pointers to shipping Unit_Index; no 143-page duplicate)

## Lint findings

| ID | Severity | Issue | Fix |
|----|----------|-------|-----|
| L2-1 | Medium | Glossary historically uncertain on Power Matrix | Confirmed Canoptek Court 40K rule; aligned with S3/S4 teaching |
| L2-2 | Medium | Cryptek Conclave old label "Scientific Schemes" | Prefer Technosorcerous Augmentations (faction pack); deprecate old name in glossary |
| L2-3 | Low | UTF-16LE agent-editor defect | Converted KB unit pages + handoffs to UTF-8 |
| L2-4 | Info | Many research stubs incomplete | Expected for v1; owned units full; expand later |
| L2-5 | Info | Hierotek Circle datasheets TBD photos | Open follow-up; not a lint fix |

## Fixes applied
- Ensured KB unit overview pointers exist and are UTF-8
- Glossary: Power Matrix + Technosorcerous Augmentations consistency notes
- log.md + changelog.md entries for L2

## Verdict
Lint complete for v1_scaffold gate → S7