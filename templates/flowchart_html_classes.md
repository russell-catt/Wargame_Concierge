<!--
FILE: templates/flowchart_html_classes.md
VERSION: v0.5.0 (2026-08-18)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, track flowcharting_uml / S1)

DOCUMENT_TYPE: Snippet / HTML class names
PROJECT_NAME: Wargame_Concierge
PROJECT_STATUS: Active

PURPOSE:
  Canonical CSS class names for UML activity shapes on printable HTML sheets.
  Pair with docs/operations/Flowcharting.md.

UPDATE_TRIGGER:
  Update when house class names change.
-->

# Flowchart HTML classes

Use these class names on printable activity trees. Guide: [`docs/operations/Flowcharting.md`](../docs/operations/Flowcharting.md).

| Class | Shape | Meaning |
|-------|--------|---------|
| `node-start` | Filled circle | Initial node |
| `node-action` | Rounded rectangle | Action / step / outcome |
| `node-decision` | Diamond | Decision (question) |
| `node-end` | Bullseye | Activity final |
| `guard` | Edge label | `[YES]` / `[NO]` / other guard |
| `tone-q` | Color overlay | Question (orange) — on a decision |
| `tone-n` | Color overlay | Stop / not valid (red) — on an action |
| `tone-y` | Color overlay | Valid (green) — on an action |
| `tone-s` | Color overlay | Sequence reminder (blue) — on an action |

Worked example: [`games/kill_team_2024/rules/Target_Eligibility_Cheat_Sheet.html`](../games/kill_team_2024/rules/Target_Eligibility_Cheat_Sheet.html). **Layout:** full-width flowchart on page 1; sequence strip + reference panel (stacked, not sidebar) on page 2.

## Change Log

- v0.5.0 (2026-08-18): Initial class table (track `flowcharting_uml` S1).

## Attribution

- Project: Wargame_Concierge
- Maintainer: Russell Catt
- Notation reference: [uml-diagrams.org About](https://www.uml-diagrams.org/about.html). **Authored by Kirill Fakhroutdinov.** Copyright © 2009–2026 uml-diagrams.org. All rights reserved.
