---
name: qa-slice
description: >-
  Tier-2 QA for Wargame_Concierge implementer slices. Use when writing or
  reviewing slices/{Id}_qa.md, checking layer/copyright/print footers,
  enhancement regression, WD Commentary cites, 2-pager density, Librarian
  enhance pass, or enhancement-report checklists.
---

# QA slice skill

Tier-2 QA for Wargame_Concierge implementer slices. Playbook: [`docs/operations/multiagent_coordinator_strategy.md`](../../docs/operations/multiagent_coordinator_strategy.md).

## Standard checks

- Layer contract respected (`raw/` never written by Librarian; `KB/` YAML only; no `wiki/`).
- UTF-8, no BOM.
- Copyright: teaching paraphrase in `KB/` and 40K armies; scoped quotes only on AGENTS Sec 10 paths.
- No GW binaries committed.
- Subagent did not `git commit` / `git push`.

## GW unofficial footer (when slice touches `games/`)

- [ ] Print HTML page 1 has **UNOFFICIAL** banner (`.gw-ip-banner`).
- [ ] Every print page has non-endorsement footer (`.gw-ip-footer`) including *completely unofficial and in no way endorsed by Games Workshop Limited*.
- [ ] No Games Workshop logos on shipping or print aids.
- [ ] Personal / no-charge / never for sale stated on exports.
- [ ] Player-facing markdown has `## Games Workshop notice` (not required on `units/research/`).
- [ ] No WarCom/GW PDF redistribution implied; event PDFs are paraphrase-first unless owner gated quote export.

Template: [`templates/Footer_Template_Gw_Print.md`](../../templates/Footer_Template_Gw_Print.md).

## Warcode GW proper-noun ban (when slice touches `games/the_warcode/`)

- [ ] Zero matches under `games/the_warcode/**` for: `Kill Team`, `Warhammer` (any casing), `Warhammer 40,000`, `Warhammer 40K`, `40,000`, `40K`, `40k`.
- [ ] Obfuscation in place where a comparator is needed: **That other game** / **Murder Platoon** (Kill Team); **Rawmallet** (Warhammer); **39.876** (40,000); **39.9** (40K / 40k).
- [ ] Handoff manifests may name GW products for agent context only — strip before promotion to shipping.

Rule: [`AGENTS.md`](../../AGENTS.md) Sec 10; [`.cursor/rules/warcode-quotes.mdc`](../../.cursor/rules/warcode-quotes.mdc).

## Enhancement-slice regression bar

When the slice **enhances** existing shipping docs (Commentary inserts, densification, army-guide revamp, print HTML refresh):

- [ ] Prior Core rule IDs / phase checklists / numeric teaching facts still present unless the slice explicitly corrects a documented error.
- [ ] No accidental deletion of Mission / Disposition / terrain teaching the slice was not scoped to rewrite.
- [ ] Codex wall intact under `games/warhammer_40k_11e/armies/**` (paraphrase only).
- [ ] Plan file not edited; no unexpected git commit.

Mark **FAIL** if enhancement silently removed working teaching without a stated replacement.

## Commentary cite checks (when WD Commentary present)

Per [`wd-commentary.mdc`](../../rules/wd-commentary.mdc) and locked track format:

- [ ] Each block titled `**Commentary (White Dwarf <issue> — <section>):**` (or track-locked equivalent).
- [ ] Body is teaching paraphrase, **≤6 sentences** — not a magazine block-quote.
- [ ] **Cite** line present: issue, article/section, purchase provenance, local path pointer, **Tier 1.5**.
- [ ] No Mission card dumps, datasheet dumps, or ref-card art in git.
- [ ] Tier 1 Core / Event Companion still wins on mechanical conflict if both appear.

## Print page-count + 2-pager density

When the slice claims a **print 2-pager** (or shipping doc locked as exactly 2 pages):

- [ ] Export / HTML is **exactly 2 pages** (never spills to page 3).
- [ ] **Both pages are filled** — no mostly-blank page 2.
- [ ] Thin army sheets may fill from **system spine** (S vs T wound utility on table aids; phase strip / distances / OC / Force Disposition / Mission pointers as needed). System fill is OK.
- [ ] Prefer army tips first; system fill only to meet density without clutter.

## Librarian KB pass

After shipping enhance slices that change `games/` truth the KB should reflect:

- [ ] Librarian enhance pass **ran** (see [`librarian-enhance`](../librarian-enhance/SKILL.md)), **or**
- [ ] Explicit **no-op waiver** recorded in the implementer or QA report (why KB already current / out of scope).

Do not treat a full re-ingest as required for every enhance slice.

## Enhancement-report checklist (when applicable)

When the slice produces or updates an **enhancement report** (e.g. system QR / army revamp report under handoffs or `games/`):

- [ ] Scope and files touched listed.
- [ ] Trust ladder / sources cited (Tier 1 vs 1.5).
- [ ] Regression notes present (what was preserved).
- [ ] 2-pager density called out if print 2-pager.
- [ ] Librarian pass or waiver noted.
- [ ] Open questions / out-of-scope items listed.

## Output

Write `slices/{Id}_qa.md` with PASS/FAIL rows and fix list. Mark slice **Resolved - Complete** only when PASS or waived with owner note.
