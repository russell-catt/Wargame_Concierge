---
name: research-enhance
description: >-
  Research-to-enhance workflow for Wargame_Concierge shipping tracks (e.g.
  White Dwarf owned issues). Use when improving games/warhammer_40k_11e from
  research notes, adding WD Commentary, revamping army 2-pagers, writing
  enhancement reports, or distinguishing enhance from Librarian ingest.
---

# Research → enhance skill

Use for **shipping enhancement** tracks that start from owned-magazine research (markdown notes + path pointers) and improve player-facing `games/` content. Distinct from **ingest** (Librarian KB fan-out from sources) — see [`Rules_Skills_Research_Enhance_Review.md`](../../docs/handoffs/wd527_research/Rules_Skills_Research_Enhance_Review.md).

Schema SoT: [`AGENTS.md`](../../AGENTS.md) Sec 10. Track locks (trust ladder, Commentary format, 2-pager density) live in the track’s `track_*_in.md` when present.

## When to use

- Owned White Dwarf / magazine research already (or newly) captured under `raw/<source>/` as **markdown only**
- Shipping slices that add Commentary, densify teaching, refresh print HTML, or revamp army guides
- Writing per-slice enhancement reports

## When not to use

- Full **ingest** into `KB/` from a new source → AGENTS Sec 11 / librarian ingest procedure
- Post-shipping KB sync only → [`librarian-enhance`](../librarian-enhance/SKILL.md)
- Commit / PR / merge → [`github-commit-push-merge`](../github-commit-push-merge/SKILL.md) (user-gated)

## Trust ladder (default for WD-style tracks)

| Tier | Source | SoT for |
|------|--------|---------|
| **1** | Core PDF, Event Companion, Chapter Approved / MFM | Rules mechanics |
| **1.5** | Owned magazine (path under `C:\Personal\40K\…`) | Commentary, mission card reading, battle report, ref layout ideas |
| **2** | WarCom article | Pointers when issue unreadable |

**Tier 1 wins** on mechanical conflict. Log conflicts; do not silently overwrite Core teaching with magazine color.

## Workflow

1. **Orient** — Read track `track_*_in.md`, slice brief, AGENTS Sec 10, relevant `games/` files.
2. **Research inputs** — Read `raw/<source>/` markdown notes and `raw/pointers/`. Never copy GW binaries into git. Owned scans stay outside the repo.
3. **Enhance shipping** — Edit `games/` (and `docs/` handoffs as needed) with teaching paraphrase. Prefer updating existing pages over near-duplicates.
4. **Commentary** — Use locked format; body ≤6 sentences; Cite line always. Rule: [`wd-commentary.mdc`](../../rules/wd-commentary.mdc).
5. **Army-guide revamp** — Under `games/warhammer_40k_11e/armies/**`: paraphrase only (Codex wall); target **2-pager density** when the guide claims 2 pages; fill both pages (system-spine fill OK).
6. **Print HTML** — UNOFFICIAL banner + footer ([`gw-unofficial-footer.mdc`](../../rules/gw-unofficial-footer.mdc)). Exactly 2 pages when claimed; both filled; never page 3.
7. **Enhancement report** — Slice implementer report: files touched, regression preserved, density, out of scope.
8. **Per-slice QA** — Run / await [`qa-slice`](../qa-slice/SKILL.md) including enhancement regression and Commentary checks.
9. **Mandatory Librarian KB pass** — After shipping truth changes, invoke [`librarian-enhance`](../librarian-enhance/SKILL.md) or record an explicit **no-op waiver**. Do **not** treat this as a full re-ingest.

## Commentary (locked shape)

```markdown
**Commentary (White Dwarf <issue> — <section or Rules Focus title>):**

<1–6 sentences teaching paraphrase in our own words. Not a full WD block-quote.
Optional: one short italic phrase only if a named Rules Focus label needs anchoring.>

**Cite:** WD<issue>, <article/section name>; owned digital backup purchased <vendor> **<YYYY-MM-DD>**; local scans `<path>`. Tier **1.5** — Core / Event Companion win on mechanics.
```

## 2-pager density (locked)

Any doc claiming exactly 2 pages must use **both** pages. Prefer army tips; fill thin sheets from system spine (S vs T wound utility on table aids; phase strip / distances / OC / Force Disposition / mission pointers as needed). Never spill to page 3.

## Distinct from ingest

| Ingest | Research → enhance |
|--------|-------------------|
| Librarian writes `KB/` from sources | Implementer writes `games/` (+ handoffs) |
| Fan-out entities, glossary, index, log | Commentary, densification, print, army guides |
| May create many new KB pages | Prefer surgical shipping edits |
| Does not ship print HTML | May ship / refresh print HTML |

Librarian **enhance** after shipping keeps KB aligned without re-running a full ingest.

## Hard stops

- No GW images/binaries in git; magazine scans outside repo (path pointers only).
- Librarian never writes `raw/` (research notes authored by Coordinator / research Implementer only).
- Subagents do not `git commit` / `git push` unless the user explicitly gates it.
- Do not edit Cursor plan files unless the user asks.
