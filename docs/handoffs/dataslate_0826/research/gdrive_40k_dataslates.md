# Pointer — Google Drive 40K dataslate folder (owner)

- **Track:** `dataslate_0826`
- **Captured:** 2026-08-27
- **Open sharing link:** https://drive.google.com/drive/folders/1__0mxNLzh1ZcmPcNA_-8kPcw_12L3Kj6
- **Purpose:** Owner-shared cache of additional **40K dataslate / update PDFs** beyond pastes already filed (Necron MFM v1.3, SM MFM v1.3, Universal Rules v1.1, SM Codex preview).
- **Agent status (2026-08-27):** **Blocked** — cloud egress returns empty response for `drive.google.com`. Allowlist requested. Inventory below stays empty until fetch succeeds or owner uploads files / pastes the folder listing.

## Inventory (fill when accessible)

| Filename | Product / version | Legal / stamp date | Local path expected | Research note | Slice |
|----------|-------------------|--------------------|---------------------|---------------|-------|
| _TBD_ | | | `C:\Personal\40K\rules\` | | |

## Already covered outside this folder (do not re-dump)

| Item | Research |
|------|----------|
| Necron MFM v1.3 | [`necron_mfm_v1_3.md`](necron_mfm_v1_3.md) |
| Space Marines MFM v1.3 | [`sm_mfm_v1_3.md`](sm_mfm_v1_3.md) |
| Universal Rules Updates v1.1 | [`40k_universal_rules_updates_v1_1.md`](40k_universal_rules_updates_v1_1.md) |
| SM Codex October preview | [`sm_codex_oct_preview.md`](sm_codex_oct_preview.md) |

## Constraints

- **Never commit GW PDFs** from Drive into git. Download to owner library / agent temp for read-only extract → markdown research only.
- Prefer saving copies under `C:\Personal\40K\rules\` with WarCom/`eng_*` filenames when known.
- Update [`raw/pointers/rules_core.md`](../../../../raw/pointers/rules_core.md) / [`points_manuals.md`](../../../../raw/pointers/points_manuals.md) in S1 after inventory locks.

## Unblock options

1. Approve Drive egress domains for this cloud environment, **or**
2. Upload individual PDFs to the agent (same as Universal Rules upload), **or**
3. Paste the folder file list (names + sizes) and upload only the unread ones.
