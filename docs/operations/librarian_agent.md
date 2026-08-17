<!--
FILE: docs/operations/librarian_agent.md
VERSION: v1.0 (2026-08-16)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Librarian, slice L0)

DOCUMENT_TYPE: Operations Guide
PROJECT_NAME: Wargame_Concierge
PROJECT_STATUS: Active

SOURCES:
  - AGENTS.md (schema source of truth)
  - docs/operations/multiagent_coordinator_strategy.md (Sec 17 planes, Sec 18 Librarian governance)
  - reference/llm-wiki.md (Karpathy "LLM Wiki" pattern - ingest / query / lint)

PURPOSE:
  Day-to-day operating guide for the Librarian agent on Wargame_Concierge.
  Covers the regular-use loop (query, ingest, lint, promote, changelog) and the
  L0 / L1 / L2 multi-slice maturity model. Schema questions are answered by
  AGENTS.md, not here.

UPDATE_TRIGGER:
  Update when the Librarian slice pattern, maturity level, or operating loop
  changes. Schema changes go in AGENTS.md.
-->

# Librarian agent - day-to-day operations

**Schema source of truth is [`AGENTS.md`](../../AGENTS.md).** Entity types, YAML frontmatter, naming, directory layout, and the copyright rules are defined there. If this guide and `AGENTS.md` ever disagree, `AGENTS.md` wins and this file is the bug.

This file answers the operational questions instead: *what do I do this session, in what order, and how do I know I am done?*

**Governance context:** [`multiagent_coordinator_strategy.md`](multiagent_coordinator_strategy.md) Sec 17 (knowledge plane vs execution plane) and Sec 18 (Librarian slice pattern, Tier 0, what the Librarian must not do).

---

## 1. Where the Librarian sits

The track runs on two planes:

| Plane | Roles | Artifacts | Success signal |
|-------|-------|-----------|----------------|
| **Execution** | Coordinator, Implementer, QA, Final Sanity | Content, scaffolding, verification | Tiers 1-3 PASS |
| **Knowledge** | **Librarian** (+ human review to promote) | `KB/` pages, index, changelog, inherited brief blocks | Tier 0 PASS; link lint clean |

The Librarian **feeds** Implementer slices and **captures** their output. It does not replace QA and it does not verify anyone's content.

**Rule of thumb:** if an Implementer would have to explore the repo to find where something is documented, Librarian work should have run first.

---

## 2. Non-negotiables

Four rules, no exceptions ([`multiagent_coordinator_strategy.md`](multiagent_coordinator_strategy.md) Sec 18.9):

1. **Never write under `raw/`.** Read it, cite it, summarize it. Never create, edit, or delete there.
2. **Never `git commit` or `git push`.** The Coordinator is the sole git owner. Leave the working tree dirty and report what changed.
3. **Never promote into `docs/` or `games/` unilaterally.** Draft, then get human or Coordinator approval, then add a [`KB/changelog.md`](../../KB/changelog.md) row.
4. **Never introduce GW binaries or verbatim rules text** in `KB/` or promoted shipping outside the KT24 exception. Teaching paraphrase and path pointers only ([`AGENTS.md`](../../AGENTS.md) Sec 10). **Exception:** `games/kill_team_2024/` may quote owned local KT24 PDFs (and WarCom free rules) verbatim for personal table use; Librarian cites pointers and indexes that work but does not duplicate full datacard dumps into `KB/`.

---

## 3. Session loop

Every session, in order:

### Start

1. Read [`AGENTS.md`](../../AGENTS.md)
2. Read [`KB/index.md`](../../KB/index.md)
3. Read the last few log entries:

```powershell
Select-String -Path KB/log.md -Pattern "^## \[" | Select-Object -Last 5
```

4. If working a slice, read the brief under [`docs/handoffs/`](../handoffs/)
5. Ask what the user wants: **query**, **ingest**, **lint**, or **promote**

### Work

Run the matching operation from Sec 4.

### Close

| Step | Check |
|------|-------|
| Log | Entry appended to [`KB/log.md`](../../KB/log.md) |
| Index | Every new page has a row in [`KB/index.md`](../../KB/index.md) |
| Confidence | Set on every touched page, and matching the index |
| Links | Back-links added; no dangling `[[wikilinks]]` |
| `raw/` | Untouched - verify with `git status` |
| Binaries | None added |
| Git | No commit, no push |

---

## 4. The four operations

### Query - "where is X documented?"

The cheapest and most common operation.

1. Read `KB/index.md`, find candidate pages
2. Read them
3. Answer with citations to KB pages, and **state the confidence** of anything you relied on. "Reanimation Protocols works like this, but that page is `unverified`" is a materially different answer from a confident one
4. Offer to file the answer to `KB/analyses/` if it took real synthesis
5. Log it

### Ingest - a source becomes knowledge

The main event. Full project procedure: [`KB/ingest_procedure.md`](../../KB/ingest_procedure.md).

Shape of it: confirm the source is allowed -> read and agree scope -> write the `KB/sources/` page -> fan out to entity pages -> set confidence honestly -> flag contradictions -> update glossary, index, overview -> log.

A meaningful ingest touches **5-15 pages**. That is the pattern working, not scope creep.

### Lint - health-check the KB

Run at L2, before a track closes, and any time the KB feels stale. Report, propose, then apply only what is approved.

| Check | Looking for |
|-------|-------------|
| Contradictions | Two pages that cannot both be true |
| **Stale rules** | Claims superseded by a newer FAQ or dataslate |
| **Edition drift** | 10th Edition assumptions sitting in 11th Edition pages |
| Orphans | Pages with no inbound links (typed-directory `README.md` files are exempt) |
| Missing pages | Concepts mentioned repeatedly with nowhere to link |
| Broken links | `[[wikilinks]]` pointing at files that do not exist |
| One-way links | A links to B, B does not link back |
| Term drift | Wording that disagrees with [`KB/glossary.md`](../../KB/glossary.md) |
| Confidence drift | Frontmatter and index disagreeing; `unverified` pages being relied on |
| Missing dates | Living-reference claims with no retrieval date |

Record the results as a table in the slice report and append a lint entry to the log.

### Promote - KB becomes shipping content

1. Confirm `confidence: verified`, or state the exception explicitly
2. Draft into `docs/` or `games/` with a Rising Tide header and footer and a `Snake_Case` filename
3. Get approval - **do not** overwrite shipping truth on your own
4. Add a row to [`KB/changelog.md`](../../KB/changelog.md)
5. Hand to the Coordinator to commit

---

## 5. Maturity model

From the playbook Sec 18.2, instantiated for this project:

| Level | Gate | Mode |
|-------|------|------|
| **0 - absent** | No `KB/index.md`, no ingest contract | Coordinator pastes ad hoc links into briefs |
| **1 - pilot** | `KB/index.md` + `KB/ingest_procedure.md` exist; one successful manual ingest | Librarian named per slice |
| **2 - dedicated** | Ingest contract stable across several sources | Dedicated Librarian on research-heavy slices |
| **3 - queued** | Ingest queue with numbered tickets | Batch runs; human approves promotion |

**Current level: 1 (pilot), entered 2026-08-16 at L0.** The index and ingest contract now exist; the first real ingest happens at **L1**, which is what actually validates the contract. Do not build queueing or tooling before then - the pattern warns explicitly against over-automating early.

Machine-readable indexes (a `kb_index.yaml`), search tooling, and ingest queues are **out of scope** until the KB has enough pages to need them. At current size, `KB/index.md` is sufficient.

---

## 6. Librarian slices in v1_scaffold

Three standalone Tier 0 slices. Artifacts live in [`docs/handoffs/v1_scaffold/slices/`](../handoffs/v1_scaffold/slices/).

| Slice | Focus | Runs after | Deliverable |
|-------|-------|-----------|-------------|
| **L0** | KB bootstrap | S0 | Schema (`AGENTS.md`), KB core pages, this guide, `.obsidian/` vault |
| **L1** | First real ingest | S2 | Source pages and entity fan-out from imported sources; validates the ingest contract |
| **L2** | Lint | S6 | Full link and consistency lint before S7 close |

Per slice: `L{n}_brief.md` (Coordinator) -> `L{n}_librarian.md` (Librarian) -> `L{n}_lib_qa.md` (QA, optional).

**Tier 0 - knowledge entrance.** A Librarian slice passes Tier 0 when the inherited documentation block is complete, index paths exist, and blockers are logged. Downstream Implementer slices take that as an entrance criterion.

**Model discipline:** the locked matrix lives in [`track_in.md`](../handoffs/v1_scaffold/track_in.md). Record the **actual** model used in every `L{n}_librarian.md` - and if a substitute was used, record the waiver there too. QA should run a **different model family** where possible.

---

## 7. Report template

Every `L{n}_librarian.md` follows this shape (playbook Sec 18.10, extended for this project):

```markdown
# L{n} - Librarian report
- **Status:** Resolved - Complete
- **Model:** <actual model used; note any waiver>
- **Slice / track:** L{n} / v1_scaffold
- **Sources:** <paths, URLs with retrieval dates, or "none - bootstrap">
- **Paths touched:** KB/..., docs/... (or none)
- **raw/ untouched:** YES
- **Promotion:** KB/changelog.md row YYYY-MM-DD (or none)
- **Lint:** PASS | FAIL (list findings)
- **Inherited block for next brief:** (paste-ready markdown links)
- **Blockers:** ...
```

The **inherited block** is the part downstream slices actually consume - paste-ready links the Coordinator drops straight into the next brief. Write it for someone who has never opened this repo.

---

## 8. Common mistakes

| Mistake | Why it hurts |
|---------|-------------|
| Creating a page without an index row | Invisible to every future session - the page may as well not exist |
| Marking a page `verified` from a single unchecked read | The confidence field is the whole trust model; inflating it breaks it |
| Silently overwriting a contradicted claim | Loses the fact that a rule *changed*, which is often the useful part |
| Writing a keyword as its own page | Splits the lookup surface; glossary and page drift apart |
| Copying rules text to save time | Copyright violation, and it stops being a teaching document |
| Waiting for a perfect KB before unblocking a slice | A minimum viable page beats a missing one |
| Committing "just the KB changes" | Coordinator is the sole git owner - no exceptions |

---

## Change Log

- v1.0 (2026-08-16): Initial operations guide. Created in slice L0 alongside `AGENTS.md`; combines the Karpathy query / ingest / lint / promote loop with the L0-L1-L2 slice pattern and maturity model from the coordinator playbook Sec 18.

## Attribution

- Project: Wargame_Concierge
- Maintainer: Russell Catt
- Structured using the Rising Tide framework

## Rising Tide Notes

- This document follows Rising Tide documentation standards.
- Keep the receipts. Make AI show their work.
- Schema questions belong in [`AGENTS.md`](../../AGENTS.md); this file covers operations only.
