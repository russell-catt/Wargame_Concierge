# Rules / Skills — Research & Enhance Review

**Track:** `wd527_shipping` (S5)  
**Date:** 2026-08-25  
**Scope:** Inventory `.cursor/rules/*.mdc` and `.cursor/skills/*/SKILL.md`; contrast **ingest** vs **research** vs **enhance**; recommend create vs enhance; record what this track applied.

Schema SoT remains [`AGENTS.md`](../../../AGENTS.md) Sec 10 (copyright) and Sec 2 (layers). This review does not replace AGENTS.md.

---

## 1. Inventory — rules (`.cursor/rules/*.mdc`)

| File | alwaysApply / globs | Purpose | Fit for research/enhance |
|------|---------------------|---------|--------------------------|
| [`layer-and-hard-stops.mdc`](../../../.cursor/rules/layer-and-hard-stops.mdc) | alwaysApply | Layer contract + hard stops (no GW binaries, no raw writes, git gate, print footer pointer) | **Enhance** — add owned-magazine / markdown-only research-notes bullet |
| [`40k-core-quotes.mdc`](../../../.cursor/rules/40k-core-quotes.mdc) | `games/warhammer_40k_11e/rules/**`, `setup/**` | WarCom-free Core quote paths + hierarchy + Codex wall | Keep; Core quotes ≠ WD Commentary |
| [`40k-armies-paraphrase.mdc`](../../../.cursor/rules/40k-armies-paraphrase.mdc) | `games/warhammer_40k_11e/armies/**` | Codex wall; paraphrase armies; GW notice | Keep; army 2-pager density lives in skills |
| [`gw-unofficial-footer.mdc`](../../../.cursor/rules/gw-unofficial-footer.mdc) | `games/**/*.html`, `games/**/*.md` | UNOFFICIAL banner/footer on shipping | Keep; QA already checks this |
| [`kt24-quotes.mdc`](../../../.cursor/rules/kt24-quotes.mdc) | `games/kill_team_2024/**` | KT24 scoped verbatim quotes | Out of WD527 scope |
| [`warcode-quotes.mdc`](../../../.cursor/rules/warcode-quotes.mdc) | `games/the_warcode/**`, `raw/the_warcode/**` | Warcode free-beta quotes | Out of WD527 scope |
| **`wd-commentary.mdc`** (new, S5) | `games/warhammer_40k_11e/**` | WD Commentary ≤6 paraphrase + cite + tier 1.5 | **Create** |

**Note:** No `docs-handoffs.mdc` or `kb-yaml.mdc` on disk at S5 inventory time. Handoff format and KB YAML remain governed by AGENTS.md + playbook.

---

## 2. Inventory — skills (`.cursor/skills/*/SKILL.md`)

| Skill | Purpose | Fit for research/enhance |
|-------|---------|--------------------------|
| [`qa-slice`](../../../.cursor/skills/qa-slice/SKILL.md) | Tier-2 QA for implementer slices | **Enhance** — enhancement regression, Commentary cites, 2-pager density, Librarian pass, enhancement-report checklist |
| [`github-commit-push-merge`](../../../.cursor/skills/github-commit-push-merge/SKILL.md) | Commit / PR / merge for this repo | Keep; Coordinator/user-gated only |
| **`research-enhance`** (new, S5) | research→enhance workflow for shipping tracks | **Create** |
| **`librarian-enhance`** (new, S5) | KB sync after `games/` shipping (not full ingest) | **Create** |

**Note:** Dedicated `librarian-ingest` / `librarian-query` / `librarian-lint` / `librarian-promote` / `coordinator-slice` skill folders are **not** present on disk. Ingest / query / lint / promote remain documented in [`AGENTS.md`](../../../AGENTS.md) Sec 11 and [`docs/operations/librarian_agent.md`](../../operations/librarian_agent.md). Do not invent those skill files in S5 unless a later track creates them.

---

## 3. Contrast — ingest vs research vs enhance

| Dimension | **Ingest** | **Research** | **Enhance** |
|-----------|------------|--------------|-------------|
| **Trigger** | User/Librarian: “ingest [source]” | Track opens owned magazine / notes into `raw/<source>/` + pointers | Shipping track improves existing `games/` (and related docs) from research |
| **Primary write surface** | `KB/` (Librarian) | `raw/<source>/` markdown notes + `raw/pointers/` (Coordinator / research Implementer — **not** Librarian) | `games/` (+ sometimes `docs/`); then Librarian KB sync |
| **Immutable rule** | Never write `raw/` as Librarian | Never commit GW binaries; scans stay outside git | Same copyright / no binaries; do not rewrite plan files |
| **Source of truth** | Owned PDFs / WarCom / Wahapedia per AGENTS Sec 10 | Trust ladder (Core = 1; owned WD = **1.5**; WarCom article = 2) | Same ladder; Tier 1 wins mechanics |
| **Output shape** | Source + entity pages, glossary, index, log | Research notes, mission/ref outlines, battle-report notes | Commentary blocks, teaching densification, print HTML, enhancement reports |
| **Quote policy** | Teaching paraphrase in KB | Markdown paraphrase / notes only in `raw/` | Locked Commentary format ≤6 sentences; Core quotes only on Sec 10 paths |
| **Success metric** | KB pages updated; log entry | Readable owned-source notes + pointers | Shipping truth improved; regression bar green; Librarian pass or waiver |
| **Not the same as** | Full re-ingest after every ship | Dumping magazine text into `games/` | Creating a new KB from scratch |

**One-line rule:** Research feeds notes; Enhance ships teaching; Ingest (and Librarian-enhance sync) keep `KB/` aligned — without treating enhance as a second ingest.

---

## 4. Recommendations — create vs enhance

| Action | Target | Why |
|--------|--------|-----|
| **Enhance** | `qa-slice/SKILL.md` | Enhancement slices need regression, Commentary cites, 2-pager density, Librarian pass, enhancement-report checks |
| **Enhance** | `layer-and-hard-stops.mdc` | Explicit magazine-scan / markdown-only research-notes hard stop |
| **Create** | `wd-commentary.mdc` | Distinct from Core quote rule; enforce locked WD Commentary format on 40K shipping paths |
| **Create** | `research-enhance/SKILL.md` | End-to-end research→enhance workflow missing from skill set |
| **Create** | `librarian-enhance/SKILL.md` | Post-shipping KB sync distinct from full ingest (L1e pattern) |
| **Do not create (S5)** | `librarian-ingest` skill folder | AGENTS + librarian_agent already own ingest; avoid duplicate SoT |
| **Do not create (S5)** | Separate “print density” rule | Prefer skill + track lock (2-pager density); QA enforces |
| **Keep as-is** | Core / armies / KT / Warcode / GW footer rules | Already aligned with AGENTS Sec 10 |

---

## 5. Applied this track (`wd527_shipping` S5)

| Deliverable | Path | Status |
|-------------|------|--------|
| This review | `docs/handoffs/wd527_research/Rules_Skills_Research_Enhance_Review.md` | Created |
| QA enhance | `.cursor/skills/qa-slice/SKILL.md` | Enhanced |
| Research-enhance skill | `.cursor/skills/research-enhance/SKILL.md` | Created |
| Librarian-enhance skill | `.cursor/skills/librarian-enhance/SKILL.md` | Created |
| WD Commentary rule | `.cursor/rules/wd-commentary.mdc` | Created |
| Layer hard-stop bullet | `.cursor/rules/layer-and-hard-stops.mdc` | Enhanced |
| Slice report | `docs/handoffs/wd527_research/slices/S5_implementer.md` | Created |

**Trust ladder (locked for this track):** Tier 1 Core / Event Companion / CA–MFM; Tier **1.5** owned WD527; Tier 2 WarCom article. Tier 1 wins on mechanical conflict.

**Commentary format:** Teaching paraphrase ≤6 sentences; Cite line with issue, section, Trinity Hobby purchase **2026-08-22**, local path, Tier 1.5. See [`track_shipping_in.md`](track_shipping_in.md).

**2-pager density:** Both pages filled; system-spine fill OK; never spill to page 3.

**Librarian:** After shipping enhance slices, run `librarian-enhance` (or record no-op waiver). Not a full re-ingest.

---

## Related

- [`track_shipping_in.md`](track_shipping_in.md)
- [`AGENTS.md`](../../../AGENTS.md) Sec 10–11
- [`docs/operations/librarian_agent.md`](../../operations/librarian_agent.md)
