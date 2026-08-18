<!--
FILE: docs/Rehydration_Prompt.md
VERSION: v0.5.0 (2026-08-18)
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
| 1 | [`../AGENTS.md`](../AGENTS.md) | **Schema source of truth.** Layer contract, entity types, YAML (`version:`), copyright / KT24 quote exception + hierarchy |
| 2 | [`../KB/index.md`](../KB/index.md) | Master catalog |
| 3 | **The last ~5 entries in** [`../KB/log.md`](../KB/log.md) | What happened recently |
| 4 | [`../games/kill_team_2024/README.md`](../games/kill_team_2024/README.md), [`Patch_Manifest.md`](../games/kill_team_2024/rules/Patch_Manifest.md), [`Target_Eligibility.md`](../games/kill_team_2024/rules/Target_Eligibility.md) | KT24 shipping spine (if the session touches Kill Team) |
| 5 | [`handoffs/README.md`](handoffs/README.md) | Later tracks index — **do not treat frozen slice briefs as living status** |

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
wargames: rules, board setup, and beginner lists from models actually owned.
Systems: Warhammer 40,000 11th Edition (Necrons + Space Marines) and Kill Team
2024. Personal use only — never for sale.

READ THESE FIRST, IN ORDER, BEFORE WRITING ANYTHING
1. AGENTS.md
2. KB/index.md
3. KB/log.md, last ~5 entries
4. games/kill_team_2024/README.md, rules/Patch_Manifest.md, rules/Target_Eligibility.md
   (if the work touches Kill Team)
5. docs/handoffs/README.md — later tracks; slice files are frozen

ARCHITECTURE - FOUR LAYERS, DO NOT CONFLATE
  raw/          immutable allowed sources     (never write here)
  KB/           the knowledge base            (Librarian agent only)
  docs/ games/  shipping, reviewed truth      (Implementers)
  reference/    external patterns, read-only  (not project truth)
The middle layer is KB/, never wiki/. Do not create a wiki/ directory.

HARD RULES
- Never write under raw/.
- Never git commit or git push unless the user explicitly gates it.
  Coordinator is the sole git owner on all other work.
- Never commit Games Workshop binaries: no PDFs, images, .webp, .png.
  Owned libraries stay outside the repo (C:\Personal\40K and
  C:\Personal\Kill Team) — markdown path pointers only.
- Teaching paraphrase in KB/ and 40K shipping. KT24 verbatim quotes only
  under games/kill_team_2024/ (Full-Scan baseline; dated eng_* patches
  supersede; Jul 25 lite is intro; omission is not a patch).
- Only the Librarian writes under KB/. YAML version: on every KB page.
- Write UTF-8, no BOM.

STATE AS OF v0.5.0 (2026-08-18)
- Git tags: v0.1.0 on 1fa3b7c (S0+L0 bootstrap); v0.5.0 this snapshot.
- KT24 Target_Eligibility owner-verified; Patch_Manifest shipped.
- KB paraphrased from that shipping (targeting subset verified).
- Living docs VERSION: v0.5.0 (2026-08-18). Do not rewrite historical
  Change Log bullets. Do not edit docs/handoffs slice files.

CONVENTIONS
- KB/** uses YAML frontmatter only. docs/**, games/**, and root docs use
  Rising Tide HTML headers plus a Change Log / Attribution footer. The two
  do not stack - a leading HTML comment breaks frontmatter parsing.
- docs/handoffs/** slice artifacts use the plain slice format, no RT header.
- KB filenames: lowercase snake_case. Shipping filenames: Snake_Case.
- Every KB page carries confidence: verified | draft | stub | unverified.
  Be conservative; an honest unverified beats a confident guess.
- Every rules claim from a living reference records a retrieval date.
- YAML version: on KB pages (project semver, distinct from GW product editions).

LIVING REFERENCES - patches happen, always record a retrieval date
- https://www.warhammer-community.com/en-gb/
- https://wahapedia.ru/

Confirm you have read the files above and state the current slice
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
git -C $root remote -v

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
| v0.5.0 | 2026-08-18 | Project-wide semver. Read order: AGENTS + KB index + KT README / Patch_Manifest / Target_Eligibility; tags; quote exception + hierarchy |
| v1.1 | 2026-08-16 | Ownership block and failure mode aligned to FOUNDATION — Tomb World owned and game-ready; dual Warriors/Scarabs; Immortals sprue; Hierotek TBD. S4 coord preflight |
| v1.0 | 2026-08-16 | Initial rehydration prompt - four-step read order, paste-ready session block, bootstrap commands, cold-start failure modes. Created in slice S1 |

## Attribution

- Maintainer: Russell Catt
- Project: Wargame_Concierge

## Rising Tide Notes

- This document is critical for recovery scenarios
- Must be kept up-to-date with project evolution
- If outdated, recovery reliability is compromised
