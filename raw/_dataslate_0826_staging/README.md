# raw/_dataslate_0826_staging — TEMPORARY PDF drop zone

**Track:** `dataslate_0826`  
**Branch:** `feature/dataslate_0826`  
**Opened:** 2026-08-27  
**Owner gate:** User authorized temporary GW PDF staging on this branch so agents can read Drive files that cannot be dragged into chat. **Clean out before merge to `main`.**

## What goes here

Drop WarCom / owned dataslate PDFs for this track only, for example:

- Kill Team Balance Dataslate
- Any unread 40K dataslate / MFM / faction update sheets from the Drive folder
- Copies of files already pasted/uploaded if useful for cross-check

Prefer WarCom/`eng_*` filenames when known.

## Rules (non-negotiable)

1. **Temporary.** This folder is a branch-only staging area. Delete all PDFs + remove the `.gitignore` negation in the same cleanup commit before squash-merge to `main` (or immediately after extract if preferred).
2. **Not a new permanent Sec 10 exception.** Unlike `raw/the_warcode/`, these are GW binaries. Do not promote this pattern.
3. **Extract → research markdown** under `docs/handoffs/dataslate_0826/research/`. Shipping stays teaching paraphrase / scoped quotes only.
4. **Librarian never writes here.** Coordinator / Implementer only.
5. **Do not** copy these PDFs into `games/`, `KB/`, or `docs/` permanently.

## After drop (agent)

1. `ls` this folder; inventory into [`gdrive_40k_dataslates.md`](../../docs/handoffs/dataslate_0826/research/gdrive_40k_dataslates.md).
2. Extract text (pdftotext / pypdf); file research notes; lock dates in `track_in.md`.
3. Run authorized slices (S3 KT, etc.).
4. **Cleanup slice:** delete PDFs, restore `.gitignore`, update `raw/README.md`, confirm `git ls-files '*.pdf'` shows only Warcode exemptions.

## Expected local library (still preferred long-term)

| System | Path |
|--------|------|
| 40K | `C:\Personal\40K\rules\` |
| Kill Team | `C:\Personal\Kill Team\kill_team_2024\` |

Staging here does not replace those pointers after cleanup.
