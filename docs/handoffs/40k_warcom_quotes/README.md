# 40K WarCom-free quotes — track handoffs

**Track:** `40k_warcom_quotes`  
**Plan:** Cursor plan `40k_warcom_rules_ingest_5f485290` (do not edit plan file)  
**Playbook:** [`docs/operations/multiagent_coordinator_strategy.md`](../../operations/multiagent_coordinator_strategy.md)

## Purpose

Allow **verbatim quoting** of WarCom-**free** 11e Core (and matching local `eng_*`) under `games/warhammer_40k_11e/rules/` and `setup/` only (personal use; **never for sale**). Index every numbered Core ID. Quote table-critical teaching-spine rules. Keep Codex / Faction Pack / MFM points out of the dump.

## Golden sources (retrieval 2026-08-18)

- Core: [`raw/pointers/rules_core.md`](../../../raw/pointers/rules_core.md)
- WarCom free Core: https://www.warhammer-community.com/en-gb/articles/nhqt9wx3/new40k-rules-download-the-free-core-rules-now/
- Read PDFs **in place** under `C:\Personal\40K\rules\` — do **not** copy binaries into git.

## Slice order

S0 → S1 → S1b → L1 → S2 → QA-Q → S3 → S4 → S5 → QA-T → L2 → Final Sanity

## Constraints

- Personal use only; project must never be sold
- **Librarian never writes `raw/` binaries** — Implementer may update `raw/pointers/`
- Never commit PDF/JPG binaries
- Codex wall: army folders stay paraphrase
- Necron lists: Personal path wins on divergence; do not overwrite Personal
- One commit + push at FS only

## Artifacts

| Slice | Report |
|-------|--------|
| S0 | [`track_in.md`](track_in.md) |
| QA-Q | [`slices/QA_Q.md`](slices/QA_Q.md) |
| FS | [`track_report.md`](track_report.md) |
