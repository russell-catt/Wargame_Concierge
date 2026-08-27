# Pointer — Google Drive 40K + Kill Team dataslate folder (owner)

- **Track:** `dataslate_0826`
- **Captured:** 2026-08-27
- **Updated:** 2026-08-27 — owner reports **Kill Team dataslate** (and more files) added to folder
- **Open sharing link:** https://drive.google.com/drive/folders/1__0mxNLzh1ZcmPcNA_-8kPcw_12L3Kj6
- **Purpose:** Owner-shared cache of **40K** and **Kill Team** dataslate / update PDFs beyond pastes already filed.
- **Agent status (2026-08-27):** **Still blocked** — `drive.google.com` returns empty (egress). Re-requested allowlist for `drive.google.com` + `drive.usercontent.google.com`. No new files in agent `uploads/` yet (only Universal Rules v1.1 PDF from earlier).

## Expected (owner-reported; not yet inventory-verified)

| Item | Notes | Slice when readable |
|------|-------|---------------------|
| Kill Team Balance Dataslate (filename TBD) | Added to Drive folder 2026-08-27 | **S3** + pointer under `raw/pointers/kill_team_*` |
| Additional 40K dataslate files (TBD) | “More files” — list when fetch works | S2 / S1 as applicable |

## Inventory (fill when accessible)

| Filename | System | Product / version | Legal / stamp date | Local path expected | Research note | Slice |
|----------|--------|-------------------|--------------------|---------------------|---------------|-------|
| _TBD — Drive unread_ | 40K / KT | | | `C:\Personal\40K\rules\` or `C:\Personal\Kill Team\kill_team_2024\` | | |

## Already covered outside this folder (do not re-dump)

| Item | Research |
|------|----------|
| Necron MFM v1.3 | [`necron_mfm_v1_3.md`](necron_mfm_v1_3.md) |
| Space Marines MFM v1.3 | [`sm_mfm_v1_3.md`](sm_mfm_v1_3.md) |
| Universal Rules Updates v1.1 | [`40k_universal_rules_updates_v1_1.md`](40k_universal_rules_updates_v1_1.md) |
| SM Codex October preview | [`sm_codex_oct_preview.md`](sm_codex_oct_preview.md) |

## Constraints

- **Never commit GW PDFs** from Drive into git. Download to owner library / agent temp for read-only extract → markdown research only.
- KT quotes only under `games/kill_team_2024/` per AGENTS Sec 10; `KB/` stays paraphrase.
- Prefer saving KT sheet under `C:\Personal\Kill Team\kill_team_2024\` (or rules root) with WarCom/`eng_*` filename when known.

## Unblock options

1. **Preferred now:** Drop PDFs into [`raw/_dataslate_0826_staging/`](../../../raw/_dataslate_0826_staging/) on `feature/dataslate_0826` (temporary gitignore; CLEANUP before main).
2. Approve Drive egress domains, **or**
3. Upload PDFs to agent chat when drag works.

