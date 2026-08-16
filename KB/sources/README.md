# KB/sources/

One page per **ingested source**. This is the provenance layer: every rules claim elsewhere in the KB should trace back to a page here.

**Type:** `source` · **Filenames:** lowercase `snake_case` · **Schema:** [`AGENTS.md`](../../AGENTS.md) Sec 4, Sec 6

## What belongs here

A summary of a source that was actually read - an owner's notes file, a Warhammer Community article, a Wahapedia page, or a pointer to an owned PDF. Not the source itself.

## What must be on every page

| Field | Why |
|-------|-----|
| **Provenance** | Local path, or URL **with retrieval date**. A living-reference claim without a date is a lint finding. |
| **Edition** | 11e, 10e, or ambiguous. Drives the confidence of everything downstream. |
| **Coverage** | What the source does and does **not** cover. |
| **Fan-out** | Which KB pages this source fed. |

## Copyright

Never copy Games Workshop PDFs, datasheet images, or verbatim rules text into this repo. Summarize in teaching paraphrase and cite where the reader can check it. See [`AGENTS.md`](../../AGENTS.md) Sec 10 and [`raw/README.md`](../../raw/README.md).

## Example filenames

`necron_lists_owner_notes.md`, `wahapedia_necrons_2026_08.md`, `wh_community_11e_launch_2026_08.md`

See also: [`KB/ingest_procedure.md`](../ingest_procedure.md) · [`KB/index.md`](../index.md)
