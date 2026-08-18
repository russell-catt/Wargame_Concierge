---
title: Flowcharting (UML activity)
type: concept
system: multi_system
created: 2026-08-18
updated: 2026-08-18
version: 0.5.0
sources: [uml_diagrams_org, reference/uml/activity-diagrams.html, reference/uml/activity-diagrams-actions.html, reference/uml/activity-diagrams-controls.html]
confidence: draft
tags: [concept, flowcharting, uml, activity_diagram, notation, multi_system]
---

# Flowcharting (UML activity)

House flowcharting maps to UML 2.5 activity diagrams: filled-circle start, rounded-rect actions, diamond decisions with guards, bullseye end.

This is **project notation**, not a Kill Team or 40K rules term. Rules text still comes from owned books. The teaching reference is [[uml_diagrams_org]] (Kirill Fakhroutdinov / uml-diagrams.org, retrieved **2026-08-18**).

---

## Why this page exists

Printable trees (valid-target sheet) and ops mermaid charts were drawing custom boxes. This page locks the **activity-diagram** subset so every new flowchart uses the same shapes.

We are **not** adopting class diagrams, sequence diagrams, or the rest of the UML 2.5 taxonomy.

---

## House mapping

Paraphrase of the activity-family snapshots — not a transcription:

| Shape | UML name | How we draw it | Role |
|-------|----------|----------------|------|
| Filled circle | Initial node | Small solid disk, optionally captioned `start` | Flow begins |
| Rounded rectangle | Action | Round-cornered rectangle; verb phrase inside | A step (`Stop — not eligible`, `VALID TARGET`) |
| Diamond | Decision node | Diamond; question inside | One incoming flow; **one** outgoing edge taken |
| `[YES]` / `[NO]` (or other) on the arrow | Guard | Square brackets on the **edge**, not inside the diamond | Which way the token goes |
| Bullseye | Activity final | Solid disk inside a hollow circle | Flow (and the activity) ends |

Color (orange question, red stop, green valid, blue sequence) is a **teaching overlay on** those shapes. Color is not a UML symbol and must not replace the diamond vs rectangle distinction.

Optional controls we usually skip on one-page sheets: merge (also a diamond, multiple in / one out), fork/join bars, flow-final (circled X — kills one flow, not the whole activity).

---

## Decision vs action (the common mistake)

If the box is asking a question, it is a **decision** (diamond) and the answers live on the leaving arrows as **guards**. If the box is telling the player what happens (`cannot Shoot`, `VALID TARGET ✓`, a SEQUENCE reminder), it is an **action** (rounded rectangle). Do not put `[YES]`/`[NO]` inside the diamond as the only copy of the branch.

---

## Where it ships

| Surface | How it uses this |
|---------|------------------|
| [`docs/operations/Flowcharting.md`](../../docs/operations/Flowcharting.md) | House guide |
| [`Target_Eligibility_Cheat_Sheet.html`](../../games/kill_team_2024/rules/Target_Eligibility_Cheat_Sheet.html) | Player print tree — UML shapes; **KT logic/cites unchanged** |
| Coordinator mermaid | Lite `{}` / `[]` / `(())` shapes; same playbook edges |

HTML class names: [`templates/flowchart_html_classes.md`](../../templates/flowchart_html_classes.md).

---

## Open questions

- Mermaid `(())` is a circle, not a true bullseye; good enough for lite ops charts.
- Print sheets may flatten diamonds slightly so question text still fits on one A4 landscape page.

---

## Related pages

- [[uml_diagrams_org]]
- [[glossary]]
- [[valid_target]] — the KT tree this notation is drawn on; UML does not rewrite that page
- [[index]]
