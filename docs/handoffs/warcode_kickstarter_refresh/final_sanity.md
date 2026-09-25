<!--
FILE: docs/handoffs/warcode_kickstarter_refresh/final_sanity.md
VERSION: v0.1 (2026-09-24)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (independent Tier-3 Final Sanity)

DOCUMENT_TYPE: Track Final Sanity
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: The Warcode
TRACK: warcode_kickstarter_refresh

PURPOSE:
  Independent track-wide Final Sanity. Findings only. No implementation edits.
  No git commit or push.

UPDATE_TRIGGER:
  After a later shipping, KB, or provenance change invalidates this pass.
-->

# Final Sanity — warcode_kickstarter_refresh

- **Track:** `warcode_kickstarter_refresh`
- **Tier:** 3 Final Sanity
- **Date:** 2026-09-24
- **Branch:** `cursor/warcode-kickstarter-refresh-b7e0`
- **Plan:** Cursor plan `warcode_kickstarter_refresh_650fc0fb` (read-only)
- **Git:** read-only (`-c safe.directory=…` only). No `git config` write, no add/commit/push/stash mutate.
- **Implementation files:** not edited (this report only)
- **Overall verdict:** **PASS** (with documented **WAIVE** rows)

Independent third pass over the locked plan, `AGENTS.md` Sec 2/10/13, `track_in.md`, source ledger, impact matrix, R1–R4, Preflight/S2/S3/S4/L1, Q1–Q4 including remediation rechecks, and the current working tree versus `main`.

---

## Executive summary

Stages 0–5 are implemented on disk. Stage 6 Q1–Q4 final verdicts are **PASS**, with explicit acceptable **WAIVE** on Cursor plan YAML todos and owner-gated QR/VIP PDF re-export. Provenance hashes and page counts match the ledger. Four playable factions have rules, lore, campaign, and KB surfaces. Historical `warcode_tactical_doctrine` and Necron trees are untouched; stash `necron-500-v2-wip-before-warcode-refresh` remains. Banned GW comparator names, STLs, `wiki/`, UTF-8 BOM, JSON, and relative Markdown links check clean.

**Ship recommendation:** **Ready for one reviewable PR** after a **user-gated** commit of this working tree (the branch currently has **zero commits ahead of `main`**). Keep the PDF export waiver visible in the PR body. Do not apply or include the protected Necron stash.

---

## PASS / FAIL / WAIVE matrix

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | Plan Stage 0 provenance/policy implemented | **PASS** | New PDFs + extracts + pointers + `raw/the_warcode/README.md`; `AGENTS.md` changelog **v0.9.1**; `.cursor/rules/warcode-quotes.mdc` lore path + v0.8.9-F hierarchy |
| 2 | Plan Stage 1 R1–R4 + impact gate | **PASS** | `research/R1_rules_delta.md` … `R4_community_coverage.md`; `impact_matrix.md` **APPROVED — proceed**; first-contact conflict preserved, not harmonized |
| 3 | Plan Stage 2 rules + four faction packages | **PASS** | MDR/Custodia datasheets; Protagen/Ulfari rechecked; quotes Sec 33–34 + ambiguity register; Q1 visual pp.37–40 **PASS** after recheck |
| 4 | Plan Stage 3 lore spine + faction lore | **PASS** | `games/the_warcode/lore/` four-file spine; lore sections on all four faction READMEs; Q2 recheck **PASS** |
| 5 | Plan Stage 4 campaign/community | **PASS** | Dated Gamefound postmortem + Kickstarter analysis; STL/TTS/README/planning updates; Q3 recheck **PASS** |
| 6 | Plan Stage 5 Librarian sync | **PASS** | Four new sources + campaign analysis; v087f/pre-launch retained; MDR/Dominium `draft`; `KB/log.md` 2026-09-24 L1 entry; report `L1_librarian_sync.md` Complete |
| 7 | Q1 rules/interactions final verdict | **PASS** | First FAIL (Overwatch exhaustiveness) remediated; recheck **PASS**. Residual QR dates were later cleared (QR now v0.8.9-F / read 2026-09-24) |
| 8 | Q2 lore final verdict | **PASS** | Recheck Q2-1–Q2-4 **PASS**. Heading-string / footer-link leftovers remain **warnings**, not FAIL |
| 9 | Q3 campaign final verdict | **PASS** | Recheck **PASS**. Live Kickstarter refetch **WAIVE** (403/Cloudflare; local handling correct) |
| 10 | Q4 policy/output final verdict | **PASS** | Recheck fixes 1–7 **PASS**. Standing **WAIVE** on plan YAML todos and PDF re-export |
| 11 | PDFs, hashes, provenance | **PASS** | Rulebook SHA-256 `4dc9efc7…c93d`, 41 pages; lorebook `9e794544…c244`, 40 pages; matches `source_ledger.md` and `raw/pointers/warcode_rulebook_v089f.md`. v0.8.7-F retained. Extracts present |
| 12 | Four-faction rules / lore / campaign / KB | **PASS** | Shipping READMEs + datasheets; lore README links all four; reviews + system README campaign block; KB faction pages + index rows for v089f, lorebook, Gamefound, Kickstarter, campaign analysis |
| 13 | No scope leakage (40K/KT/Necron) | **PASS** | `git diff --stat main` empty for `games/warhammer_40k_11e/armies/necrons`, `games/kill_team_2024`, `games/warhammer_40k_11e/rules` |
| 14 | Historical track frozen | **PASS** | `git diff --stat main -- docs/handoffs/warcode_tactical_doctrine` empty. Directory not listed in implementer touch lists |
| 15 | Plan file body unedited | **WAIVE** | Outside git. Stage 0–6 markdown body still matches the locked track. YAML todos marked completed except `qa-final-ship: in_progress`. LastWriteTime **2026-09-24 13:20:03** (unchanged since Q4). Acceptable Cursor plan-tracker noise; body not rewritten |
| 16 | Relative links | **PASS** | 312 local file links under `games/the_warcode/**/*.md`; **broken=0**. Comparative glossary inbound from system README |
| 17 | GW proper-noun ban | **PASS** | 0 matches in `games/the_warcode/**` for Kill Team / Warhammer / 40,000 / 40K / 40k |
| 18 | No STL / extra binaries | **PASS** | Workspace `*.stl` = 0. Tracked PDFs remain Warcode exemption; new v0.8.9-F + lorebook PDFs untracked under `raw/the_warcode/` (gitignore negation). No in-repo export PDF. Map PNGs + xlsx still present from prior track |
| 19 | UTF-8, no BOM | **PASS** | 148 scoped md/json/txt/mdc files: `bom=0`, UTF-8 decode failures `0` |
| 20 | JSON sidecar | **PASS** | `_export_pdf_config.json` parses; header `UNOFFICIAL — The Warcode V.0.8.9-F — v1.5 (2026-09-24)` |
| 21 | Protected Necron stash | **PASS** | `stash@{0}: On main: necron-500-v2-wip-before-warcode-refresh` — `Cryptek_Play_Pack_500.md`, `print/README.md`, `print/_html_to_pdf.py` (+10/−4). Working-tree Necron diff vs `main` empty |
| 22 | Layer contract / no `wiki/` | **PASS** | No `wiki/` directory. Librarian wrote `KB/**` + L1 report. Preflight wrote allowed `raw/the_warcode/`. This FS wrote only this file |
| 23 | Lore quotes scoped; KB paraphrase | **PASS** | Lore path `games/the_warcode/lore/**` (+ existing rules/setup/factions). Sampled KB Warcode pages paraphrase; no fenced lorebook dumps in `KB/sources/warcode_rulebook_v089f.md` / faction pages |
| 24 | Ambiguity register preserved (no invented rulings) | **PASS** | `Rulebook_Quotes.md` “Current-source ambiguity register” lists all eight impact-matrix items unresolved |
| 25 | Legacy VIP markdown not linked | **PASS** | No shipping links to `Agentic_Rules_and_Marketing_Review.md`; file absent (gitignored) |
| 26 | QR / VIP PDF re-export | **WAIVE** | Process exists (Markdown sources + `_export_pdf_config.json`). Re-export **not** run: VIP markdown absent; no Markdown-PDF CLI in this environment; creating PDFs in-repo forbidden. Owner export outside git (`C:\Personal\print_aids/` / email) |
| 27 | One reviewable PR shape | **PASS** | Single feature branch; all track files are uncommitted working-tree + untracked adds; no mixed Necron/KT/historical-track diffs. Awaiting user-gated commit |

---

## Plan-stage implementation (locked plan vs disk)

| Plan stage | Required artifacts | Status |
|---|---|---|
| Track structure | `docs/handoffs/warcode_kickstarter_refresh/` + branch `cursor/warcode-kickstarter-refresh-b7e0` | Present. Historical `warcode_tactical_doctrine/` frozen |
| 0 | Both free PDFs, hashes, extracts, pointers, policy | Present. OCR not required (covers / trailing art only) |
| 1 | R1–R4 + signed impact matrix | Present; coordinator **APPROVED** |
| 2 | Quotes provenance, MDR/Custodia packages, four-faction teaching, register | Present |
| 3 | `lore/` spine; faction lore; first-contact conflict; Huoxing/Mars; war-name split; Cassini overlap; Custodia-as-formation | Present |
| 4 | Gamefound postmortem; Kickstarter analysis; digital-only framing; TTS v0.8.7 drift; export JSON stamp | Present |
| 5 | KB sources, factions, concepts, glossary, overview, index, log | Present (`version: 0.9.1` on sampled pages) |
| 6 | Independent QA + this Final Sanity | Q1–Q4 rechecks **PASS**; this report |

Plan YAML todo `qa-final-ship` remains `in_progress` until Coordinator closes the track after this file — expected.

---

## File and change summary

**Git identity:** `HEAD` == `main` (`rev-list main...HEAD` = `0 0`). Latest `main` commit observed: `6fcf984` (Necron Conclave 1000; unrelated). **Entire track is uncommitted.**

**Modified vs `main` (53 files, +1102 / −604):** policy (`AGENTS.md`, `warcode-quotes.mdc`), project indexes (`README.md`, `docs/Project_Planning.md`, `docs/handoffs/README.md`, `games/README.md`, `reference/Source_Library.md`, `raw/the_warcode/README.md`), Warcode shipping rules/setup/guides/factions, Warcode KB concepts/factions/glossary/index/log/overview/historical sources, export JSON.

**Untracked (in-scope):**

- `raw/the_warcode/The-Warcode-Rulebook-V.0.8.9-F.pdf`
- `raw/the_warcode/The-Warcode-Lorebook-Tactical-Doctrine-Field-Edition.pdf`
- `raw/the_warcode/rulebook_v089f_extract.txt`
- `raw/the_warcode/lorebook_tactical_doctrine_field_edition_extract.txt`
- `raw/pointers/warcode_rulebook_v089f.md`
- `raw/pointers/warcode_lorebook_tactical_doctrine.md`
- `games/the_warcode/lore/` (README, Theatre, Timeline, Methodology)
- `games/the_warcode/factions/mdr/Squad_Datasheet.md`
- `games/the_warcode/factions/dominium/Squad_Datasheet.md`
- `games/the_warcode/reviews/Gamefound_Postmortem_2026-09-18.md`
- `games/the_warcode/reviews/Kickstarter_and_Community_2026-09-24.md`
- `KB/sources/warcode_rulebook_v089f.md`
- `KB/sources/warcode_tactical_doctrine_field_edition.md`
- `KB/sources/warcode_gamefound_campaign_2026_09.md`
- `KB/sources/warcode_kickstarter_relaunch_2026_09.md`
- `KB/analyses/warcode_campaign_transition_2026_09.md`
- `docs/handoffs/warcode_kickstarter_refresh/` (ledger, matrix, research, slices, QA, this report)

**Not in diff (must stay out of the PR):** Necron stash contents; `docs/handoffs/warcode_tactical_doctrine/**`; KT24; 40K Core.

**CRLF note:** Git warns LF→CRLF on several historical Warcode Markdown files. Not a FAIL.

---

## QA rollup

| QA | First pass | Recheck | Final |
|---|---|---|---|
| Q1 rules/interactions | FAIL (Overwatch exhaustiveness + header hygiene) | Must-fix + should-fix applied | **PASS** |
| Q2 lore | FAIL (Q2-1–Q2-4 source-voice/cites) | Four items remediated | **PASS** |
| Q3 campaign | FAIL (v087f Gamefound label, rollup currency, Overview/Proxy headers; live KS fetch) | Content fixes applied; live fetch **WAIVE** | **PASS** |
| Q4 policy/output | FAIL (stale v0.8.7 headers, two-faction next action, lore path in indexes, orphan glossary, STL related pages) | Fixes 1–7 **PASS**; export + plan YAML **WAIVE** | **PASS** |

No remaining Q* **FAIL** rows.

---

## Waivers (explicit, acceptable)

1. **QR / VIP PDF re-export** — Owner-gated. JSON sidecar is current (`UNOFFICIAL`, V.0.8.9-F, 2026-09-24). Do not commit exported PDFs. Restore gitignored VIP markdown locally if that PDF is still wanted.
2. **Cursor plan YAML todos** — Tracker statuses only; Stage 0–6 body unedited. Last write 2026-09-24 13:20:03.
3. **Live Kickstarter page refetch (Q3)** — 403/Cloudflare. Shipping/KB omit live totals; timestamps stay in R3. Not a shipping defect.
4. **Games Workshop print footer on Warcode pages** — N/A. RedMakers unofficial language; GW `.gw-ip-banner` not required on this subtree (Q3).

---

## Non-blocking leftovers (do not flip FAIL)

- `track_in.md` and `docs/handoffs/README.md` still say **Stage 6 QA remediation**. Accurate until Coordinator closes after this report; bump to Final Sanity complete / Closed when gated.
- `AGENTS.md` HTML header comment still says `VERSION: v0.9.0`; changelog already records **v0.9.1**. Load-bearing Sec 10 body is current.
- Q2 warnings: shortened first-contact heading strings on some pages; optional footer-link consistency.
- `KB/index.md` core-file table dates still show older rows for overview/glossary/log while those files were touched 2026-09-24.
- System README names four factions in prose and links `factions/`; per-file faction hops are on lore README, Overview, QR, and STL_Sources.

---

## Protected stash and PR hygiene

- Stash **must remain**. Do not `stash pop` onto this branch.
- Subagents did not commit (log shows only prior `main` history).
- Allowed binaries to add: the two new `raw/the_warcode/*.pdf` files (gitignore exemption). Never STL.
- Suggested PR scope: this branch’s working tree only; squash-merge when the user gates git.

---

## Ship recommendation

**PASS — ready for one reviewable PR.**

Coordinator should:

1. Update `track_in.md` / handoffs README rollup to Stage 6 Final Sanity **PASS** (optional hygiene before commit).
2. On **explicit user gate**, commit the listed modified + untracked Warcode/KB/handoff/policy files (UTF-8, no BOM).
3. Open a single squash-merge PR whose description states: **PDF export waived** (JSON current; owner re-export outside git); **plan YAML todos waived**; **Necron stash not included**.
4. Do not push until the user authorizes.

Track may be marked **Closed — Complete** after that gated PR lands.
