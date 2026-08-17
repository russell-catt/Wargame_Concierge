<!--
FILE: docs/Rehydration_Prompt.md
VERSION: v1.0 (2026-08-16)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, slice S1)

DOCUMENT_TYPE: Rehydration / Recovery
PROJECT_NAME: Wargame_Concierge
CRITICALITY: HIGH

SOURCES:
  - AGENTS.md (schema source of truth)
  - README.md
  - docs/Project_Planning.md
  - docs/handoffs/v1_scaffold/track_in.md
  - docs/operations/librarian_agent.md

PURPOSE:
  Enables full reconstruction of project context after a session reset, memory
  loss, or handoff to a new assistant. Defines the exact read order and the
  facts that must be true before the assistant writes anything.

PRIMARY_AUDIENCE:
  - AI systems starting cold on this repository
  - Project owner during recovery scenarios

CONTAINS:
  - Bootstrap read order
  - Paste-ready session prompt
  - Facts an assistant must know before writing
  - Self-check questions

USAGE_INSTRUCTIONS:
  Paste the block in section 2 into a new session and instruct the model to
  rebuild full project understanding before proceeding. Do not skip the reads.

UPDATE_TRIGGER:
  Update whenever the read order, the layer contract, the hard rules, or the
  active track changes.
-->

# Rehydration Prompt

For a session that starts with no memory of this project. Work through it in order; the reads are cheap and the failure mode of skipping them is expensive.

---

## 1. Bootstrap read order

Four reads, in this sequence. Each one assumes the previous.

| # | Read | Why it is in this position |
|---|------|---------------------------|
| 1 | [`../AGENTS.md`](../AGENTS.md) | **Schema source of truth.** The layer contract, the eight entity types, required YAML frontmatter, naming rules, copyright rules, and the ingest / query / lint workflows. Everything else assumes you have read this |
| 2 | [`../KB/index.md`](../KB/index.md) | Master catalog. Tells you what knowledge already exists and at what confidence, so you do not re-derive it |
| 3 | **The last ~5 entries in** [`../KB/log.md`](../KB/log.md) | What actually happened most recently, in order. The command is in section 3 |
| 4 | [`handoffs/v1_scaffold/track_in.md`](handoffs/v1_scaffold/track_in.md) | Current track state: constraints, locked model matrix, per-slice rollup, and what is still pending |

**Then, depending on what you are about to do:**

| Task | Also read |
|------|-----------|
| Working a slice | The brief in [`handoffs/v1_scaffold/slices/`](handoffs/v1_scaffold/slices/), plus the previous slice's report |
| Writing or maintaining `KB/` pages | [`operations/librarian_agent.md`](operations/librarian_agent.md) and [`../KB/ingest_procedure.md`](../KB/ingest_procedure.md) |
| Writing shipping content | [`Project_Structure.md`](Project_Structure.md) for placement, [`../templates/README.md`](../templates/README.md) for the header and footer |
| Answering a rules question | [`../KB/index.md`](../KB/index.md), then the pages it points at, then [`../KB/glossary.md`](../KB/glossary.md) |
| Adding a new game system | [`Game_System_Scaffold.md`](Game_System_Scaffold.md) |
| Deciding anything already decided | [`Project_Planning.md`](Project_Planning.md) |

---

## 2. Paste-ready session prompt

Copy everything between the rules into a fresh session.

---

```text
You are picking up the Wargame_Concierge project at
C:\Personal\Personal_Projects\Wargame_Concierge.

WHAT IT IS
A personal knowledge base and teaching assistant for learning tabletop
wargames: rules, board setup, and beginner army lists built from models
actually owned. First system: Warhammer 40,000, 11th Edition. Necrons are the
learning army; Space Marines are the opposing force. The structure is
game-agnostic - 40K 11e is the first worked example, not the only one.

READ THESE FIRST, IN ORDER, BEFORE WRITING ANYTHING
1. AGENTS.md                            - schema source of truth
2. KB/index.md                          - master catalog of knowledge
3. KB/log.md, last ~5 entries           - what happened recently
4. docs/handoffs/v1_scaffold/track_in.md - current track state

ARCHITECTURE - FOUR LAYERS, DO NOT CONFLATE
  raw/          immutable allowed sources     (never write here)
  KB/           the knowledge base            (Librarian agent only)
  docs/ games/  shipping, reviewed truth      (Implementers)
  reference/    external patterns, read-only  (not project truth)
The middle layer is KB/, never wiki/. Do not create a wiki/ directory.

HARD RULES
- Never write under raw/.
- Never git commit or git push. The Coordinator is the sole git owner;
  pushing is a user gate at slice S7.
- Never commit Games Workshop binaries: no PDFs, images, .webp, .png.
  The owned library at C:\Personal\40K stays outside the repo and is
  referenced by markdown path pointer only.
- Teaching paraphrase only. Never transcribe datasheet statlines,
  stratagem text, or rules text verbatim.
- Only the Librarian writes under KB/.
- Write UTF-8, no BOM.

CONVENTIONS
- KB/** uses YAML frontmatter only. docs/**, games/**, and root docs use
  Rising Tide HTML headers plus a Change Log / Attribution footer. The two
  do not stack - a leading HTML comment breaks frontmatter parsing.
- docs/handoffs/** slice artifacts use the plain slice format, no RT header.
- KB filenames: lowercase snake_case. Shipping filenames: Snake_Case.
- Every KB page carries confidence: verified | draft | stub | unverified.
  Be conservative; an honest unverified beats a confident guess.
- Every rules claim from a living reference records a retrieval date.

STATE AS OF 2026-08-16
- Track v1_scaffold in progress. Order: Preflight, S0, L0, S1, S2, L1,
  S3, S4, S5, S6, L2, S7. Preflight, S0, L0 and S1 have landed.
- Local repository only, no remote. The Coordinator commits after each
  slice passes QA. Target is a private GitHub repo,
  russell-catt/Wargame_Concierge, created at S7 behind a user gate.
- KB maturity level 1 (pilot). No sources ingested yet - the first real
  ingest is L1.
- Confirmed Necron ownership (2026-08-16 FOUNDATION): Kill Team: Tomb World
  owned, assembled, painted, game-ready (Geomancer, 2 Tomb Crawlers,
  5 Macrocytes, 10 Warriors, 3 Scarab Swarms — preferred learning baseline).
  Also owned on sprue: 2nd Warriors squad (10), 2nd Scarab set (3), Immortals
  (5). Hierotek Circle Kill Team (used) game-ready; 40K datasheets TBD pending
  owner photos. Totals: 20 Warriors, 6 Scarab Swarms.
- Power Matrix is the Canoptek Court detachment rule in 40K. The KB
  glossary still carries an older unresolved-attribution warning; the
  Librarian corrects it at L1.

LIVING REFERENCES - patches happen, always record a retrieval date
- https://www.warhammer-community.com/en-gb/
- https://wahapedia.ru/

Confirm you have read the four files above and state the current slice
before proposing any work.
```

---

## 3. Commands

Run from the repository root.

```powershell
$root = "C:\Personal\Personal_Projects\Wargame_Concierge"

# Last 5 KB log entries - step 3 of the read order
Select-String -Path "$root\KB\log.md" -Pattern "^## \[" | Select-Object -Last 5

# Current slice status
Select-String -Path "$root\docs\handoffs\v1_scaffold\track_in.md" -Pattern "^\| \*\*S|^\| \*\*L|^\| \*\*Preflight"

# Commit history so far, and what is uncommitted right now
git -C $root log --oneline
git -C $root status --short
git -C $root remote -v   # expect empty until S7

# Confirm no GW binaries have crept in
@(Get-ChildItem $root -Recurse -Include *.pdf,*.webp,*.png,*.jpg,*.jpeg,*.gif -File -Force -ErrorAction SilentlyContinue).Count
```

---

## 4. Facts you must have before writing

If you cannot answer these from what you just read, read again rather than guessing.

| Question | Where the answer is |
|----------|--------------------|
| Which layer does the file I am about to write belong to? | [`Project_Structure.md`](Project_Structure.md) Sec 1 |
| Am I allowed to write there? | [`../AGENTS.md`](../AGENTS.md) Sec 2 |
| YAML frontmatter or Rising Tide header? | [`../AGENTS.md`](../AGENTS.md) Sec 6 |
| What confidence value is honest for this claim? | [`../AGENTS.md`](../AGENTS.md) Sec 6 |
| Has this already been decided? | [`Project_Planning.md`](Project_Planning.md) Sec 2 |
| What models does the owner actually have? | [`Project_Planning.md`](Project_Planning.md) Sec 3 |
| What is still open and blocking? | [`Project_Planning.md`](Project_Planning.md) Sec 4 |
| Which slice am I in, and what are its exit criteria? | The brief in [`handoffs/v1_scaffold/slices/`](handoffs/v1_scaffold/slices/) |

---

## 5. Common failure modes on a cold start

| Mistake | Why it happens | Cost |
|---------|---------------|------|
| Creating a `wiki/` directory | The Karpathy pattern doc in `reference/` calls the middle layer `wiki/` | Splits the knowledge layer in two |
| Writing a Rising Tide HTML header onto a `KB/` page | Every other document in the repo has one | Breaks YAML frontmatter parsing in Obsidian and Dataview |
| Writing under `raw/` | It looks like an ordinary directory | Destroys the immutability every KB citation depends on |
| Marking a page `verified` after one unchecked read | Optimism | The confidence field is the entire trust model; inflating it breaks it |
| Denying Tomb World ownership or calling it superseded | v1_scaffold drafts wrongly recorded Tomb World as not owned | Starter lists ignore the game-ready learning baseline; sprue-only assumptions |
| Committing "just this one change" | Helpfulness | The Coordinator is the sole git owner - no exceptions |
| Copying rules text to save time | Speed | Copyright violation, and it stops being a teaching document |
| Writing UTF-16 | Some PowerShell redirection defaults do this on Windows | Unreadable diffs; some tooling treats the file as binary |

---

## 6. Keeping this file honest

This document is only as good as its last update. It goes stale in three ways:

1. **The read order changes** - a new entry point appears, or one of the four is retired.
2. **The state block in section 2 drifts** - slices land, ownership changes, open questions resolve.
3. **A hard rule changes** - rare, and the most damaging kind of drift if missed.

Re-read section 2 against [`Project_Planning.md`](Project_Planning.md) and [`handoffs/v1_scaffold/track_in.md`](handoffs/v1_scaffold/track_in.md) at the end of every track. If they disagree, those two are right and this file is the bug.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1.1 | 2026-08-16 | Ownership block and failure mode aligned to FOUNDATION — Tomb World owned and game-ready; dual Warriors/Scarabs; Immortals sprue; Hierotek TBD. S4 coord preflight |
| v1.0 | 2026-08-16 | Initial rehydration prompt - four-step read order, paste-ready session block, bootstrap commands, cold-start failure modes. Created in slice S1 |

## Attribution

- Maintainer: Russell Catt
- Project: Wargame_Concierge

## Rising Tide Notes

- This document is critical for recovery scenarios
- Must be kept up-to-date with project evolution
- If outdated, recovery reliability is compromised
