---
name: librarian-enhance
description: >-
  KB sync after games/ shipping enhancements. Use when a research-enhance or
  shipping slice finished updating warhammer_40k_11e (or similar) and the
  Librarian must update sources, entities, index, log, and back-links — or
  record a no-op waiver. Not a full re-ingest; never write raw/.
---

# Librarian enhance skill

Post-shipping **KB sync** for enhancement tracks. Complements (does not replace) full **ingest** in [`AGENTS.md`](../../AGENTS.md) Sec 11 and [`docs/operations/librarian_agent.md`](../../docs/operations/librarian_agent.md).

Pair with [`research-enhance`](../research-enhance/SKILL.md). QA expects this pass or an explicit waiver ([`qa-slice`](../qa-slice/SKILL.md)).

## When to use

- `games/` teaching or print truth changed and `KB/` should reflect it
- Track slice **L\*e** / “Librarian enhance” after shipping slices
- Owner asks to sync KB after Commentary / mission / army-guide shipping work

## When not to use

- First-time source fan-out with many new entity pages → **ingest**
- Query-only answers → query workflow; file analyses if asked
- Writing research notes under `raw/` → **never** (Librarian hard stop)

## Contract

1. **Never write `raw/`.**
2. **No full re-ingest by default.** Prefer surgical updates to pages the shipping change actually affects.
3. Teaching paraphrase only in `KB/` (AGENTS Sec 10). Point at shipping quote files / rule IDs with `[[wikilinks]]` — do not dump magazine or Core quote corpora into KB.
4. UTF-8, no BOM. YAML frontmatter on every KB page (AGENTS Sec 6).
5. Do not `git commit` / `git push` unless the user explicitly gates it.

## Sync checklist

When shipping under `games/` changed meaningful player truth:

- [ ] **Sources** — Update or refresh `KB/sources/` page for the owned issue / pointer (retrieval/provenance dates; tier notes).
- [ ] **Entities** — Patch affected `KB/setup/`, `KB/concepts/`, `KB/analyses/`, faction/unit pages as warranted (prefer update over duplicate).
- [ ] **Index** — Refresh one-line summaries in `KB/index.md` for touched pages.
- [ ] **Log** — Append `KB/log.md` entry (`enhance` or `sync` style — date, shipping paths, pages created/updated).
- [ ] **Back-links** — Add missing `[[wikilinks]]` between related KB pages.
- [ ] **Glossary** — Only if new canonical terms appeared; flag conflicts, do not silent-overwrite.

Optional: `KB/overview.md` / `KB/changelog.md` only if the enhance shifts the big picture or promotes shipping (promotion still needs review per AGENTS Sec 11).

## No-op waiver

If KB already matches shipping (or the slice touched only tooling / handoffs / rules-skills with no player-truth delta):

1. State **no-op waiver** in the Librarian slice report (or implementer report if Librarian deferred).
2. Name why (e.g. “Commentary already mirrored in `KB/sources/…`; no entity drift”).
3. Skip file edits; still leave a one-line log entry only if the track requires an audit trail — otherwise waiver alone is enough for QA.

## Output

Write the Librarian slice artifact under `docs/handoffs/<track>/slices/` (plain slice format). List pages created/updated or the waiver text. Mark complete when checklist done or waived.
