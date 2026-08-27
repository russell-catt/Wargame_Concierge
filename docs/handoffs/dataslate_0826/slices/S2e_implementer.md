# S2e Implementer — dataslate_0826

**Slice:** S2e — Universal Rules Updates v1.1 (core)
**Status:** Complete
**Date:** 2026-08-27
**Model:** `claude-sonnet-5-thinking-high` (per track model matrix)
**Authorization:** Owner 2026-08-27 — AUTHORIZED, draft confidence accepted; no PDF commits; no `git commit`/`git push` by this subagent.

## Summary

Read the staging PDF `raw/_dataslate_0826_staging/eng_wh40k_core&key_universal_rules_updates-lu3grocned-rphh78bl6k.pdf` in place (1 page, text layer OK — verified with `file` and the PDF reader; never copied or committed). Confirmed it is **Universal Rules Updates — Version 1.1**, legal matched play from **26 August 2026**, superseding July v1.0 on the same topics (items 1–4 repeat with the same intent) and adding one net-new item: **disembark move typing**, assigning two brand-new Core IDs — `18.06` **ASSAULT DISEMBARK MOVE** and `18.07` **SHOCK DISEMBARK MOVE**.

`raw/pointers/rules_core.md` already carried the correct v1.1 row and supersession note from slice **S1** — verified consistent, not re-edited (S1 explicitly left "quote pass + `Core_Rules_Quotes.md` update" as S2e's job).

Updated `games/warhammer_40k_11e/rules/Core_Rules_Quotes.md`:
- Marked the **July `eng_22-07_*` deltas (v1.0)** section **SUPERSEDED**, kept for history, "do not teach from this section."
- Added a new **August `eng_*` deltas (v1.1) — CURRENT** section: stratagem items 1–4 repeated with the same intent (still flagged against `15.x`, no new Core IDs), plus **verbatim quote blocks** for `18.06` and `18.07`, each citing **filename + p.1 + rule ID** per Sec 10.
- Added both new IDs to the Full Core ID index table (between `18.05` and `19.01`) and updated the ID/quote counts (156 → +2 new IDs; 112 → 114 quoted).
- Updated the file's Source hierarchy line, header `SOURCES`/`VERSION`, and Change Log.

Added **teaching paraphrase** (no verbatim text) for the two new move types to the three teaching surfaces that actually cover movement/transports:
- `Turn_Structure.md` — Movement phase section, a new "Disembark move types" callout with a currency stamp, explaining that `18.06`/`18.07` name the move but do not themselves grant the underlying permission.
- `Quick_Reference_Card.md` — one-line addition to the Movement (**09**) side, per the research note's suggestion ("add one-line disembark note if space").
- `Keyword_Glossary.md` — Movement and positioning table gains three rows: **Disembark Move** (`18.04`, `verified`, for context) and the two new terms **Assault Disembark Move** (`18.06`) / **Shock Disembark Move** (`18.07`), both `draft` (named by a source read, effect not yet cross-checked against an owned local PDF).

Added **currency stamps** — `Universal Rules Updates v1.1, legal 26 Aug 2026` — to every touched rules surface: `Core_Rules_Quotes.md`, `Turn_Structure.md`, `Keyword_Glossary.md`, `Quick_Reference_Card.md`, and `README.md` (hierarchy line updated to name v1.1 as current and note the new IDs).

## Files changed

- `games/warhammer_40k_11e/rules/Core_Rules_Quotes.md` — July v1.0 section marked superseded; new August v1.1 section with verbatim `18.06`/`18.07` quotes (filename + p.1 + rule ID); two new index rows; header/version/Change Log updated.
- `games/warhammer_40k_11e/rules/Turn_Structure.md` — teaching paraphrase for assault/shock disembark move in the Movement phase; currency stamp; header/version/Change Log updated.
- `games/warhammer_40k_11e/rules/Keyword_Glossary.md` — three new glossary rows (Disembark Move, Assault Disembark Move, Shock Disembark Move); currency stamp; header/version/Change Log updated.
- `games/warhammer_40k_11e/rules/Quick_Reference_Card.md` — one-line disembark-typing note on the Movement side; header/version/Change Log updated.
- `games/warhammer_40k_11e/rules/README.md` — hierarchy line names v1.1 as current, supersedes v1.0, adds `18.06`/`18.07`; Status line and Change Log updated.
- `docs/handoffs/dataslate_0826/slices/S2e_implementer.md` — this report (new file).

## Verified, not touched

- `raw/pointers/rules_core.md` — already correct from slice S1 (v1.1 row, supersession note, S2e ownership of the quote pass). Read and cross-checked against the staging PDF; no discrepancy found.
- `games/warhammer_40k_11e/rules/Overview.md`, `Key_Concepts.md` — read in full; neither currently teaches transports/disembarking (`Overview.md` covers army composition and win conditions; `Key_Concepts.md` covers the attack sequence, mortal wounds, OC, battle-shock, and attached units). Adding a disembark-typing paraphrase to either would be a scope-creeping new subject, not a currency update, so both were left untouched. Flagged here per the brief's "as needed."
- `games/warhammer_40k_11e/setup/*` — grepped for `disembark`/`TRANSPORT`; no hits. Not a "touched rules surface" for this slice.
- `KB/sources/` — Librarian-owned; a v1.1 source page is explicitly called out in the research note as an L0/L1 Librarian job, not this Implementer slice.

## Copyright / Sec 10 compliance

- The staging PDF was read **in place** and never copied into git; no PDF was added, modified, or committed by this subagent.
- Every verbatim quote block under `games/warhammer_40k_11e/rules/Core_Rules_Quotes.md` carries **filename + page + rule ID** (`eng_wh40k_core&key_universal_rules_updates-lu3grocned-rphh78bl6k.pdf` — p.1 — `MOVE TYPES FOR DISEMBARKING UNITS — 18.06` / `18.07`), flagged explicitly as the **branch-only staging copy** pending the owner's confirmed save path under `C:\Personal\40K\rules\` (per `raw/pointers/rules_core.md`).
- All other touched surfaces (`Turn_Structure.md`, `Keyword_Glossary.md`, `Quick_Reference_Card.md`, `README.md`) stay **teaching paraphrase only** — no verbatim rules text reproduced outside `Core_Rules_Quotes.md`.
- `Keyword_Glossary.md` marks the two new terms `draft` (named by a read source, effect not yet cross-checked against an owned local PDF) rather than `verified`, per the confidence rubric.

## Waivers / open items for QA

1. **Filename provenance:** the only readable copy of the v1.1 sheet is the branch-only staging file (with `&` in the name, from the chat upload). The owner's permanent local filename under `C:\Personal\40K\rules\` is unconfirmed and may differ (without the `&`). Every citation to this source flags it as the staging copy; `raw/pointers/rules_core.md` already carries the same caveat from S1. Re-verify the citation filename once the owner confirms the saved path.
2. **`draft` vs `verified` on the two new glossary terms:** intentional — the source is a read PDF but not yet cross-checked against a confirmed permanent local copy. Do not upgrade to `verified` until that cross-check happens.
3. **Overview.md / Key_Concepts.md were not touched** — neither currently teaches transports; judged out of scope for a currency-only pass. Flagging for QA to confirm this reading of "as needed" is acceptable, or to request a minimal transports mention be added to `Key_Concepts.md` in a follow-up.
4. No PDF was read via any tool that would copy it; no `git add`/`git commit`/`git push` was run by this subagent. Pre-existing staging PDFs under `raw/_dataslate_0826_staging/` (including the v1.1 sheet) already appear tracked in git from prior slices in this session's `git status` — that predates this slice's work and is outside S2e's remit, but is flagged here for the Coordinator/QA in case cleanup before merge to `main` is still pending.

## Not touched (S2e scope)

- MFM / points work — other slices (S2c/S2d).
- Army datasheet paraphrase beyond the transport/disembark callout added to the glossary and movement-phase teaching pages.
- Dumping the full Core PDF or the full v1.1 sheet beyond the disembark-typing quote blocks required by the brief.
- `KB/**` — Librarian-owned.
