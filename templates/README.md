<!--
FILE: templates/README.md
VERSION: v0.5.0 (2026-08-18)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor

DOCUMENT_TYPE: Folder README
PROJECT_NAME: recipe_book

PURPOSE:
  Index of Rising Tide header/footer fragments and which document type each applies to.

UPDATE_TRIGGER:
  Update when new template types are added to this project.
-->

# Templates

Rising Tide **header/footer** fragments (from the Rising Tide meta-repo and Ross Video standards).

## Which template to use

| Document type | Header | Footer |
|---------------|--------|--------|
| Root / folder README | `Header_Template_README.md` | `Footer_Template_Standard.md` |
| Planning | `Header_Template_Project_Planning.md` | `Footer_Template_Standard.md` |
| Rehydration | `Header_Template_Rehydration_Prompt.md` | `Footer_Template_Rehydration.md` (Version History table) |
| Reference / distill | `Header_Template_Reference_Document.md` | `Footer_Template_Standard.md` |
| Design / technical note | `Markdown_Document_Template.md` | `Footer_Template_Standard.md` |
| Check-in session (full) | `Header_Template_Checkin_Notes.md` | footer section in that file |
| E-mail body fragments | *(none)* | HTML comment only in `data/build_lineup.md`, `data/summary_notes.md` |

Also present: `Markdown_Header_Template.md`, `Markdown_Footer_Template.md`, `Markdown_Document_Template.md` (generic).

## `email/` — Jinja e-mail body

| File | Role |
|------|------|
| [`email/##PROJECT##_PV_Daily_Status_Report_Template.htm`](email/##PROJECT##_PV_Daily_Status_Report_Template.htm) | Word-export HTML; Jinja2 variables; read as cp1252 |
| [`email/##PROJECT##_PV_Daily_Status_Report_Template_files/`](email/##PROJECT##_PV_Daily_Status_Report_Template_files/) | Word companion assets (must stay beside `.htm`) |

Rendered by [`scripts/render_release.py`](../scripts/render_release.py). Output goes to [`output/`](../output/).

## Not documented with RT markdown headers

- YAML / JQL config, Python scripts under `scripts/`, generated HTML under `output/`

---

## Change Log

- v0.5.0 (2026-08-18): Project-wide semver snapshot (x.y.z).
- v1.1 (2026-05-27): Documented `email/` Jinja template location.
- v1.0 (2026-05-26): Template index; added Reference and Check-in templates.

## Attribution

- Project: recipe_book
- Maintainer: Russell Catt
- Structured using the Rising Tide framework

## Rising Tide Notes

- Copy header/footer patterns when creating new markdown docs in this repo.
