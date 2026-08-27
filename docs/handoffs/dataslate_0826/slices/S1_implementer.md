# S1 Implementer — dataslate_0826

**Slice:** S1 — pointers + footer currency convention
**Status:** Complete
**Date:** 2026-08-27
**Model:** `claude-sonnet-5-thinking-high` (per track model matrix)
**Authorization:** Owner 2026-08-27 — full track authorized, G2 (draft) accepted; package shape locked — **no singular Balance Dataslate for 40K or KT**.

## Summary

Updated `raw/pointers/*` and `reference/Source_Library.md` to name the real Aug 2026 40K package (Universal Rules v1.1, Faction Pack v1.2 Necrons+SM, MFM v1.3) and the real KT quarterly balance package (Core/update-log surface + priority team online-rules updates), all retrieval-dated 2026-08-27 and `draft` confidence. Extended `templates/Footer_Template_Gw_Print.md` and `templates/Gw_Print_Banner.html` with an additive, optional "currency line" section (E) carrying the exact stamp text locked in `track_in.md`, without touching the existing UNOFFICIAL / non-endorsement banner (B), footer (A), markdown notice (C), or datacard micro (D) sections. No PDFs were read, copied, or committed as part of this slice — pointer text only, sourced from prior research notes and staging-inventory metadata already filed under `docs/handoffs/dataslate_0826/research/`.

## Done

1. **40K package pointers** — added dated rows for the Aug 2026 package pieces, explicitly marking each as superseding the prior July-dated file on the same topics (never silently overwritten — old rows kept with a supersede note):
   - `rules_core.md`: Universal Rules Updates v1.1 (legal 26 Aug 2026), new disembark move typing (`18.06`/`18.07`), supersedes v1.0 (22 Jul 2026).
   - `faction_pack_necrons.md`: Faction Pack v1.2 (legal 26 Aug 2026), teaching-relevant What's New / Rules Updates, Codex wall reminder.
   - `faction_pack_space_marines.md`: Faction Pack v1.2 (legal 26 Aug 2026), teaching-relevant What's New / Rules Updates, Codex wall reminder, Blood Ravens Matched cores noted unchanged.
   - `points_manuals.md`: MFM v1.3 rows for Necrons and Space Marines (owner-paste provenance, `draft`, deltas summarized, Legends section noted for SM Casual cross-check).
2. **KT package pointers** — named after the real Core/update-log + team-online-rules package (no fictional `balance_dataslate_kt_*.md` created):
   - `kill_team_2024_missions.md`: Aug 2026 Tomb World update log + Mission packs update log rows, superseding the Apr/Nov-dated logs on shared topics; Approved Ops 2025 tournament companion added as optional pointer.
   - `kill_team_2024_teams.md`: new "Aug 2026 quarterly balance" section with all 8 staged team online-rules updates, priority flagged (Angels of Death, Canoptek Circle, Plague Marines) vs inventory-only (Hierotek, Deathwatch, Celestian Insidiants, Murderwing, Vespid Stingwings), explicit no-singular-dataslate note.
3. **Living web source pointers** — retrieval dates refreshed to 2026-08-27 with egress-blocked note (WarCom L1–L3 canonical URLs still unresolved) in `web_living_sources.md` and `kill_team_web_living_sources.md`; both explicitly restate the owner lock that no singular Balance Dataslate article/PDF exists.
4. **`reference/Source_Library.md` catalog** — added/updated rows in Core rules and updates, Faction packs, Points documents, and the KT area table to match the pointer files above; version bumped v0.5.4 → v0.5.5 with a Change Log entry.
5. **Footer template currency-line section (E)** — added to `templates/Footer_Template_Gw_Print.md`:
   - 40K package stamp (preferred, multi-piece pages).
   - 40K piece-specific lines (Universal Rules v1.1, SM MFM v1.3, Necron MFM v1.3).
   - KT quarterly balance line (Core + team package, no singular dataslate).
   - SM Codex October preview note (pairs with, does not replace, the 40K package line).
   - Warcode / non-GW N/A stamp.
   - Usage notes: additive only, substitute versions as packages supersede, may combine with a second currency line (e.g. package + Codex preview), not a Sec 10 quote licence.
   - Template version bumped v1.0 → v1.1 with Change Log entry.
6. **HTML banner fragment** — mirrored the same currency-line snippets (E1–E5) into `templates/Gw_Print_Banner.html` as ready-to-copy `<p class="gw-currency-line">` blocks plus a matching CSS rule, version bumped v1.0 → v1.1. Banner (B), footer (A, both systems), and datacard (D) blocks are untouched.
7. Wrote this `S1_implementer.md`.

## Files touched

- `raw/pointers/rules_core.md` (update)
- `raw/pointers/faction_pack_necrons.md` (update)
- `raw/pointers/faction_pack_space_marines.md` (update)
- `raw/pointers/points_manuals.md` (update)
- `raw/pointers/kill_team_2024_missions.md` (update)
- `raw/pointers/kill_team_2024_teams.md` (update)
- `raw/pointers/web_living_sources.md` (update)
- `raw/pointers/kill_team_web_living_sources.md` (update)
- `reference/Source_Library.md` (update)
- `templates/Footer_Template_Gw_Print.md` (update)
- `templates/Gw_Print_Banner.html` (update)
- `docs/handoffs/dataslate_0826/slices/S1_implementer.md` (create)

## Not touched (S1 scope)

- `games/warhammer_40k_11e/**` shipping (Universal Rules quote pass, Faction Pack teaching, MFM list recost) — **S2 / S2c / S2d / S2e**.
- `games/kill_team_2024/**` shipping (Tomb World / Nemesis teleport teaching, priority team datacards) — **S3**.
- SM Codex October readiness / Legendary Proxies — **S2b**.
- Project/game core README currency lines — **S4 / S5**.
- `raw/_dataslate_0826_staging/` contents — untouched; cited as a **temporary cross-check** only, per `CLEANUP_brief.md`. No PDFs were opened, moved, or copied in this slice.
- `KB/` — Librarian-owned; not touched by Implementer.

## Notes on package shape (confirmed, not re-litigated)

Every pointer edited in this slice was named after a **real product** (Universal Rules Updates, Faction Pack, Munitorum Field Manual, killzone/mission-pack update log, team online rules) with its actual version/date stamp. No file, pointer, or footer line invents a singular "Balance Dataslate" for either 40K or KT, matching the owner lock recorded in `track_in.md` and `research/research_plan_restatement.md`.

## Blockers / open items for QA-S1 or later slices

- All new/updated pointer rows for the Aug 2026 package pieces are `draft` — none of the corresponding PDFs have been confirmed saved under `C:\Personal\40K\rules\` or `C:\Personal\Kill Team\kill_team_2024\Teams\` yet (owner action, tracked as open questions in `track_in.md`).
- MFM v1.3 (Necrons + Space Marines) provenance is an **owner paste**, not a PDF read in this pass, and is not present in the current `raw/_dataslate_0826_staging/` pull — flagged in `points_manuals.md` and `Source_Library.md`.
- WarCom canonical article URLs (L1–L3) remain unresolved (egress still blocks `news.warhammer.com` / `warhammer-community.com` as of this pass) — living-source pointers note this explicitly rather than guessing a URL.
- No git commit/push performed by this subagent, per instructions.
