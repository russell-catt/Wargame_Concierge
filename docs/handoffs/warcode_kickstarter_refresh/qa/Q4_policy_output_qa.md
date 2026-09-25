# Q4 — Stage 6 policy / output QA

- **Track:** `warcode_kickstarter_refresh`
- **Stage:** 6 (output/policy QA only)
- **Date:** 2026-09-24
- **QA model:** Cursor Grok 4.6 (independent of implementer/Librarian reports)
- **Skill:** [`.cursor/skills/qa-slice/SKILL.md`](../../../../.cursor/skills/qa-slice/SKILL.md)
- **Policy:** [`AGENTS.md`](../../../../AGENTS.md) Sec 2/10/13; [`.cursor/rules/warcode-quotes.mdc`](../../../../.cursor/rules/warcode-quotes.mdc)
- **Git:** first pass not run; recheck used read-only `git -c safe.directory=…` (no config write, no commit)
- **Implementation files:** not edited by this QA agent
- **Overall verdict:** **FAIL** (2026-09-24 first pass) → **PASS** after coordinator remediation (export and plan remain **WAIVE**)

Independent filesystem QA of shipping, `KB/`, `docs/`, and `raw/the_warcode/`. Status reconstructed from implementer/Librarian reports plus on-disk inventory. Git diff/status was not taken.

## Result table

| Check | Result | Evidence |
|---|---|---|
| Layer contract (`raw/` / `KB/` / `docs/` / `games/` / no `wiki/`) | **PASS** | No `wiki/` directory. Preflight wrote allowed `raw/the_warcode/` sources. L1 report scoped to `KB/**` plus this track’s Librarian report. Shipping and campaign pages live under `games/` / `docs/`. |
| Lore quote scope | **PASS** | Lorebook callouts sit under `games/the_warcode/lore/**` and faction overviews (allowed rulebook/lore quote trees). S3 shipped teaching paraphrases with filename + PDF page + section; no lorebook dump found under `guides/`, `reviews/`, `research/`, or `README.md`. Mechanics still route to v0.8.9-F. |
| `KB/` / `docs/` paraphrase | **PASS** with residual policy-index drift (see FAIL rows) | Sampled KB faction/source pages paraphrase and point at shipping profiles. Research manifests stay in the handoff track. Root `README.md` and `docs/Project_Planning.md` still omit the lore quote path (FAIL below). |
| Raw allowed files / sidecars | **PASS** | Present: v0.8.7-F PDF, v0.8.9-F PDF, lorebook PDF, native extracts, OCR/transcription sidecars, map PNGs, xlsx. SHA-256 of current PDFs matches `source_ledger.md` (`4dc9efc7…c93d`, `9e794544…c244`). |
| No STL / prohibited binaries | **PASS** | No `.stl` / mesh files under the Warcode trees. PDFs/PNGs found only under `raw/the_warcode/` (gitignore exemption). No new export PDF created in-repo. |
| GW proper nouns in `games/the_warcode/**` | **PASS** | Case-insensitive scan of shipping markdown: 0 hits for Kill Team, Warhammer, 40,000, 40K/40k. Obfuscation (`That other game`, `Rawmallet`, `39.876`, `39.9`) remains. `Games Workshop` appears only in a historical changelog line on `README.md` (not in the ban list). |
| UTF-8, no BOM | **PASS** | 139 markdown/JSON/text files in Warcode shipping, this handoff track, `KB/`, `AGENTS.md`, and `warcode-quotes.mdc`: `bom=0`, UTF-8 decode failures `0`. |
| JSON config validity | **PASS** | `games/the_warcode/reviews/_export_pdf_config.json` parses. Header is `UNOFFICIAL — The Warcode V.0.8.9-F — v1.5 (2026-09-24)`. Footer is personal-use / not endorsed by RedMakers. |
| Relative Markdown links | **PASS** | 319 local `.md` links in `games/the_warcode/**` resolve; `broken=0`. |
| Orphans | **FAIL** | `games/the_warcode/rules/Comparative_Glossary.md` has **zero inbound** relative links from other Warcode markdown (including system README). README names “Comparative glossary” in prose only. |
| All four factions reachable | **PASS** | File links exist from `lore/README.md`, `rules/Overview.md`, and `Quick_Reference_Play_Guide.md`. KB `index.md` catalogs all four. System README names all four and links the `factions/` directory (directory hop, not four file links). `research/STL_Sources.md` related-pages still list only Protagen and Ulfari. |
| Stale v0.8.7-current claims | **FAIL** | Several **active** `REFERENCE_STATUS` headers still say `beta v0.8.7-F`. Player-facing comparison table still labels The Warcode as `beta v0.8.7-F` despite a four-roster body. TTS/Kickstarter “listing still says 0.8.7” warnings are correctly contrasted with v0.8.9-F and are not this FAIL. |
| Stale two-faction claims | **FAIL** | Shipping body copy is four-roster. `docs/Project_Planning.md` next-actions row 3 still says “MDR/Dominium when beta publishes”. Historical `warcode_tactical_doctrine` manifests and dated `KB/log.md` entries are frozen history, not this FAIL. |
| Plan file unchanged | **WAIVE** | `C:\Users\russe\.cursor\plans\warcode_kickstarter_refresh_650fc0fb.plan.md` LastWriteTime **2026-09-24 13:20:03**. Stage 0–6 body still matches the locked track. YAML todos are marked completed / `qa-final-ship: in_progress`. Implementer reports do not list the plan as a touched file. Git not available to prove a body diff. |
| Historical track unchanged | **PASS** | `docs/handoffs/warcode_tactical_doctrine/**` newest LastWriteTime **2026-08-29**. No implementer report lists that tree. |
| Unrelated Necron WIP absent / protected | **WAIVE** | Track_in records stash `necron-500-v2-wip-before-warcode-refresh`. Warcode reports do not list Necron paths. On-disk Necron army files show 2026-09-24 timestamps (mass 12:16; `Cryptek_Play_Pack_500.md` / print helpers 12:54). Git not run, so stash vs checkout vs extra WIP cannot be proven. |
| Quick-reference / VIP export | **WAIVE** (blocker) | Process exists; re-export was **not** run. See export section. No binary was written into the repo. |
| Librarian pass recorded | **PASS** | `slices/L1_librarian_sync.md` is Complete (version 0.9.1). Residual glossary related-page gap is in the fix list, not a missing-pass FAIL. |

## Export process and blocker

**Available process**

1. Markdown sources: `games/the_warcode/Quick_Reference_Play_Guide.md` (shipping QR); local-only VIP review `games/the_warcode/reviews/Agentic_Rules_and_Marketing_Review.md` (gitignored; PDF-by-email policy from the frozen tactical-doctrine GATE).
2. Print options: `games/the_warcode/reviews/_export_pdf_config.json` (Letter, UNOFFICIAL v0.8.9-F header, personal-use footer). This is the same sidecar historically used with a Markdown-PDF editor export, not a repo Playwright job.
3. There is **no** Warcode `print/*.html` or `_html_to_pdf.py` sibling. 40K/KT Playwright exporters are a different pipeline.

**Blocker (export not executed)**

- `Agentic_Rules_and_Marketing_Review.md` is **absent** on disk (`exists=False`), so the VIP PDF cannot be regenerated here.
- No Markdown-PDF / `yzane.markdown-pdf` extension directory, `pandoc`, or `md-to-pdf` CLI was found in this environment.
- Creating a PDF inside the repo is forbidden for this slice.

Owner can re-export outside git (email / `C:\Personal\print_aids\`) after restoring the gitignored VIP markdown and using the JSON sidecar.

## Exact fix list

Do not treat historical `warcode_tactical_doctrine` manifests or dated `KB/log.md` rows as items to rewrite.

1. **Stamp current baseline on leftover `REFERENCE_STATUS` headers** (keep v0.8.7-F in `SOURCES` / change-log v0.1 lines). Files still labelled `Active — draft, beta v0.8.7-F`:
   - `games/the_warcode/rules/Overview.md`
   - `games/the_warcode/rules/Keyword_Glossary.md`
   - `games/the_warcode/rules/Key_Concepts.md`
   - `games/the_warcode/rules/Comparative_Glossary.md`
   - `games/the_warcode/rules/Scenarios_and_Events.md`
   - `games/the_warcode/rules/Protocol_Cards_Reference.md`
   - `games/the_warcode/setup/Board_Setup.md`
   - `games/the_warcode/setup/Terrain_Basics.md`
   - `games/the_warcode/factions/protagen_marines/README.md`
   - `games/the_warcode/factions/protagen_marines/Squad_Datasheet.md`
   - `games/the_warcode/factions/ulfari/README.md`
   - `games/the_warcode/factions/ulfari/Squad_Datasheet.md`
2. **Replace the live comparison-table axis** in `games/the_warcode/guides/Warcode_vs_That_Other_Game.md` line 37: `The Warcode (beta v0.8.7-F)` → current v0.8.9-F (body already says four rosters).
3. **Align project policy indexes with AGENTS Sec 10 v0.9.1** (add `lore/` to the Warcode quote path):
   - Root `README.md` (copyright/sourcing paragraph still `rules|setup|factions/` only).
   - `docs/Project_Planning.md` “Scoped verbatim quotes” row (same omission).
4. **Remove the stale two-faction next action** in `docs/Project_Planning.md` §5 row 3: `Optional: L1 Warcode unit KB pages; MDR/Dominium when beta publishes`.
5. **Link the comparative glossary** from `games/the_warcode/README.md` (How to learn / subtree map) so `rules/Comparative_Glossary.md` is not an orphan.
6. **Add MDR and Dominium related-page links** on `games/the_warcode/research/STL_Sources.md` (currently Protagen + Ulfari only).
7. **Optional but recommended:** add `[[warcode_rulebook_v089f]]`, `[[warcode_tactical_doctrine_field_edition]]`, and campaign source wikilinks to `KB/glossary.md` Related pages (body already cites them; related list still ends on v0.8.7-F + pre-launch).
8. **Owner-only export (outside repo):** restore gitignored VIP markdown if needed; export QR + VIP PDF using `_export_pdf_config.json`; do not commit PDFs.
9. **Coordinator git check (this QA did not run git):** confirm stash `necron-500-v2-wip-before-warcode-refresh` still holds unrelated Necron WIP; confirm the plan file change is YAML todos only.

## Not failed

- Banned GW product names in `games/the_warcode/**`.
- STL / extra binaries.
- UTF-8 BOM.
- JSON sidecar for v0.8.9-F.
- Broken relative links.
- Lorebook-as-mechanics.
- Frozen historical track timestamps.
- Four-faction playability in system README prose, lore README, Overview, QR, and KB index.

## Gate

**Not Resolved — Complete.** Re-run Q4 after fixes 1–6 (7 optional). Export remains owner-gated (item 8).

---

## Remediation recheck (2026-09-24)

Coordinator applied fixes 1–7. This QA agent re-scanned the workspace, used read-only git, and did not edit implementation or commit.

### Fixes 1–7

| # | Fix | Recheck | Result |
|---|---|---|---|
| 1 | Stamp leftover `REFERENCE_STATUS` headers to current v0.8.9-F | All 12 listed files now say `beta v0.8.9-F (2026-09-24)`. No remaining `Active — draft, beta v0.8.7-F` headers. v0.8.7-F remains in `SOURCES` / historical change-log rows. | **PASS** |
| 2 | Comparison-table axis | `Warcode_vs_That_Other_Game.md` line 37 is `The Warcode (beta v0.8.9-F)`. Four-roster body unchanged. | **PASS** |
| 3 | Policy indexes include `lore/` | Root `README.md` lines 180 and 190: `rules\|setup\|factions\|lore/`. `docs/Project_Planning.md` scoped-quotes row matches AGENTS Sec 10 v0.9.1. | **PASS** |
| 4 | Stale two-faction next action | `Project_Planning.md` row 3 is now “Table-test all four Warcode squads…”. `MDR/Dominium when beta publishes` is gone. | **PASS** |
| 5 | Comparative glossary inbound link | System README How to learn step 8 links `rules/Comparative_Glossary.md`. | **PASS** |
| 6 | STL_Sources related pages | Adds `../factions/mdr/README.md` and `../factions/dominium/README.md` (plus Protagen/Ulfari). | **PASS** |
| 7 | Glossary related pages | `KB/glossary.md` Related pages now list `[[warcode_rulebook_v089f]]`, `[[warcode_tactical_doctrine_field_edition]]`, Gamefound and Kickstarter sources; v0.8.7-F + pre-launch kept as historical. | **PASS** |

### Repeat policy scans

| Check | Result | Evidence |
|---|---|---|
| GW proper nouns in `games/the_warcode/**` | **PASS** | Kill Team / Warhammer / 40,000 / 40K/40k hits = 0 |
| No STL / binary leakage | **PASS** | Binaries still only allowed `raw/the_warcode/` PDFs + map PNGs. No `.stl`. No new in-repo export PDF. |
| Relative links / orphans | **PASS** | 323 local `.md` links resolve (`broken=0`). Zero orphans except system `README.md` (entry point). Comparative glossary inbound = 1. |
| UTF-8, no BOM | **PASS** | 143 scanned files; `bom=0`, UTF-8 fail `0` |
| JSON config | **PASS** | `_export_pdf_config.json` parses; header still `UNOFFICIAL — The Warcode V.0.8.9-F — v1.5 (2026-09-24)` |
| Four factions reachable | **PASS** | Unchanged plus STL_Sources now links all four overviews |
| Stale v0.8.7-current / two-faction | **PASS** | Header and comparison-table defects cleared; TTS “listing says 0.8.7” warnings remain correctly contrasted |
| Historical track | **PASS** | `git diff --stat main -- docs/handoffs/warcode_tactical_doctrine` empty; working-tree diff empty |
| Unrelated Necron WIP | **PASS** | `git diff --stat main -- games/warhammer_40k_11e/armies/necrons` empty. Stash `stash@{0}: On main: necron-500-v2-wip-before-warcode-refresh` still holds `Cryptek_Play_Pack_500.md`, `print/README.md`, `print/_html_to_pdf.py` (3 files, +10/−4) |
| Plan file | **WAIVE** | Outside git. LastWriteTime still **2026-09-24 13:20:03** (unchanged since first Q4). YAML todos remain completed except `qa-final-ship: in_progress`. Stage 0–6 body unchanged. |
| Quick-reference / VIP export | **WAIVE** | Same blocker: VIP markdown absent; no Markdown-PDF CLI/extension; JSON sidecar current. No binary created. Owner export remains outside repo. |
| Git / branch | **PASS** (read-only) | Branch `cursor/warcode-kickstarter-refresh-b7e0`. No `git config` write, no commit. |

### Recheck gate

**Resolved — Complete** for Q4 policy/output: **PASS**, with standing **WAIVE** on (a) Cursor plan YAML todos and (b) QR/VIP PDF re-export (owner-gated; no in-repo binaries).
