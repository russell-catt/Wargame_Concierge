<!--
FILE: docs/Rehydration_Prompt.md
VERSION: v0.9.1 (2026-08-27)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, track dataslate_0826 S4)

DOCUMENT_TYPE: Rehydration / Recovery
PROJECT_NAME: Wargame_Concierge
CRITICALITY: HIGH

SOURCES:
  - AGENTS.md (schema source of truth)
  - README.md
  - docs/Project_Planning.md
  - docs/handoffs/README.md
  - games/README.md
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
  Update whenever the read order, the layer contract, the hard rules, or
  project phase / systems onboarded change.
-->

# Rehydration Prompt

For a session that starts with no memory of this project. Work through it in order; the reads are cheap and the failure mode of skipping them is expensive.

---

## 1. Bootstrap read order

| # | Read | Why it is in this position |
|---|------|---------------------------|
| 1 | [`../AGENTS.md`](../AGENTS.md) | **Schema source of truth.** Layer contract, entity types, YAML (`version:`), copyright / quote exceptions |
| 2 | [`../KB/index.md`](../KB/index.md) | Master catalog |
| 3 | **The last ~5 entries in** [`../KB/log.md`](../KB/log.md) | What happened recently |
| 4 | [`../games/README.md`](../games/README.md) then the system README you are working in | Systems index — 40K / KT24 / The Warcode |
| 5 | [`handoffs/README.md`](handoffs/README.md) | Tracks index — **do not treat frozen slice briefs as living status** |

**Then, depending on what you are about to do:**

| Task | Also read |
|------|-----------|
| Working a slice | The brief under [`handoffs/`](handoffs/), plus the previous slice's report |
| Writing or maintaining `KB/` pages | [`operations/librarian_agent.md`](operations/librarian_agent.md) and [`../KB/ingest_procedure.md`](../KB/ingest_procedure.md) |
| Writing shipping content | [`Project_Structure.md`](Project_Structure.md) for placement, [`../templates/README.md`](../templates/README.md) for headers/footers |
| Answering a rules question | [`../KB/index.md`](../KB/index.md), then the pages it points at, then [`../KB/glossary.md`](../KB/glossary.md) |
| Adding a new game system | [`Game_System_Scaffold.md`](Game_System_Scaffold.md) |
| Deciding anything already decided | [`Project_Planning.md`](Project_Planning.md) |
| KT24 rules work | [`../games/kill_team_2024/rules/Patch_Manifest.md`](../games/kill_team_2024/rules/Patch_Manifest.md), [`Target_Eligibility.md`](../games/kill_team_2024/rules/Target_Eligibility.md) |
| Warcode work | [`../games/the_warcode/README.md`](../games/the_warcode/README.md); naming ban in AGENTS Sec 10 |

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
Systems: Warhammer 40,000 11th Edition (Necrons + Space Marines); Kill Team
2024; The Warcode (RedMakers free beta). Personal use only — never for sale.
Phase: v0.9.0 pre-external-review — next milestone is external user critique.

READ THESE FIRST, IN ORDER, BEFORE WRITING ANYTHING
1. AGENTS.md
2. KB/index.md
3. KB/log.md, last ~5 entries
4. games/README.md (+ the system README for this session's work)
5. docs/handoffs/README.md — tracks; slice files are frozen

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
- Never commit Games Workshop binaries: no GW PDFs or official images.
  Owned libraries stay outside the repo (C:\Personal\40K and
  C:\Personal\Kill Team) — markdown path pointers only.
  Exception: Warcode free-beta PDF under raw/the_warcode/ (not GW).
- Teaching paraphrase in KB/ and docs/. Scoped verbatim quotes only per
  AGENTS Sec 10 (KT24; 40K WarCom-free Core; Warcode free beta).
- In games/the_warcode/** shipping, never name GW proper nouns — use
  That other game / Murder Platoon / Rawmallet / 39.876 / 39.9.
- Only the Librarian writes under KB/. YAML version: on every KB page.
- Write UTF-8, no BOM.

STATE AS OF v0.9.0 (2026-08-25)
- Three systems onboarded under games/.
- Warcode card/map corpus + VIP review PDF-email-only policy.
- Next: external user review and critique.
- Do not rewrite historical Change Log bullets. Do not edit handoff slice files.

RULES FRESHNESS (checked 2026-08-27)
- GW patches rules and points between publications. Do not assume the last
  session's balance figures are still current.
- Track dataslate_0826 (open) is the Aug 2026 GW balance currency pass:
  40K = Universal Rules v1.1 + Faction Pack v1.2 + MFM v1.3 (Necrons/SM);
  Kill Team = Core/update-log package + priority team online rules.
  Neither system has a singular "Balance Dataslate" file (owner lock).
  The Warcode is unaffected (not a GW system).
- Do not restate package figures here — read the current stamp on the
  relevant games/{system}/README.md before citing a point cost or rule ID.

CONVENTIONS
- KB/** uses YAML frontmatter only. docs/**, games/**, and root docs use
  Rising Tide HTML headers plus a Change Log / Attribution footer. The two
  do not stack - a leading HTML comment breaks frontmatter parsing.
- docs/handoffs/** slice artifacts use the plain slice format, no RT header.
- KB filenames: lowercase snake_case. Shipping filenames: Snake_Case.
- Every KB page carries confidence: verified | draft | stub | unverified.
- Every rules claim from a living reference records a retrieval date.

LIVING REFERENCES - patches happen, always record a retrieval date
- https://www.warhammer-community.com/en-gb/
- https://wahapedia.ru/
- https://pre-launch.thewarcode.com/ (Warcode marketing; secondary to beta PDF)

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

# Tracks index
Get-Content "$root\docs\handoffs\README.md" | Select-Object -First 40

# Commit history and working tree
git -C $root log --oneline -10
git -C $root status --short
git -C $root remote -v
```

---

## 4. Facts you must have before writing

If you cannot answer these from what you just read, read again rather than guessing.

| Question | Where the answer is |
|----------|--------------------|
| Which layer does the file I am about to write belong to? | [`Project_Structure.md`](Project_Structure.md) Sec 1 |
| Am I allowed to write there? | [`../AGENTS.md`](../AGENTS.md) Sec 2 |
| YAML frontmatter or Rising Tide header? | [`../AGENTS.md`](../AGENTS.md) Sec 6 |
| What quote exceptions apply? | [`../AGENTS.md`](../AGENTS.md) Sec 10 |
| What systems exist? | [`../games/README.md`](../games/README.md) |
| What was already decided? | [`Project_Planning.md`](Project_Planning.md) |

---

## 5. Cold-start failure modes

| Temptation | Why it fails | Do this instead |
|------------|--------------|-----------------|
| Guessing ownership or points | Wrong lists reach the table | Read FOUNDATION / inventories |
| Writing under `raw/` | Breaks immutability | Cite and paraphrase into KB or shipping |
| Naming Kill Team / Warhammer inside Warcode shipping | Violates Sec 10 ban | Obfuscation table in AGENTS |
| Copying rules text to save time | Copyright + teaching failure | Paraphrase or scoped quote paths only |

---

## 6. Keeping this file honest

This document is only as good as its last update. Re-read section 2 against [`Project_Planning.md`](Project_Planning.md) and [`handoffs/README.md`](handoffs/README.md) at the end of every major track. If they disagree, those two are right and this file is the bug.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v0.9.1 | 2026-08-27 | Added a "Rules freshness" block to the paste prompt naming the open `dataslate_0826` currency pass and directing readers to each system's own README rather than restating package figures here (slice S4) |
| v0.9.0 | 2026-08-25 | Three systems; Warcode rules; pre-external-review phase; paste prompt refreshed |
| v0.5.0 | 2026-08-18 | Project-wide semver. Read order: AGENTS + KB index + KT spine |
| v1.1 | 2026-08-16 | Ownership block aligned to FOUNDATION — Tomb World owned |
| v1.0 | 2026-08-16 | Initial rehydration prompt |

## Attribution

- Maintainer: Russell Catt
- Project: Wargame_Concierge

## Rising Tide Notes

- This document is critical for recovery scenarios
- Must be kept up-to-date with project evolution
- If outdated, recovery reliability is compromised
