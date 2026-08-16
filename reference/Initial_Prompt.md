<!--
FILE: reference/Initial_Prompt.md
VERSION: v1.0 (2026-08-16)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, slice S1)

DOCUMENT_TYPE: Reference / Seed Context
PROJECT_NAME: Wargame_Concierge
REFERENCE_STATUS: Active

SOURCES:
  - Planning session transcript, 2026-08-16, 16:51-17:41 (UTC-4)
  - Cursor plan wargame_concierge_setup_ee78aead

PURPOSE:
  Preserves the verbatim requests that created this project, in order, so
  original intent stays auditable against later drift. This is the record of
  what was asked for - not a restatement of what was built.

PRIMARY_AUDIENCE:
  - Anyone checking whether the project still matches what was asked for
  - AI systems rebuilding context from first principles
  - Reviewers auditing scope

UPDATE_TRIGGER:
  Append only. New seed requests are added as new turns with their timestamp;
  existing turns are never edited or reworded.
-->

# Initial Prompt

The requests that created Wargame_Concierge, captured verbatim.

**Session:** Sunday, 2026-08-16, 16:51 to 17:41 (UTC-4).
**Outcome:** the Cursor plan `wargame_concierge_setup_ee78aead`, authorized and executed as track `v1_scaffold`.

**This file is append-only and quoted exactly**, including the original spelling. It records *intent*, not decisions. Decisions of record - including the ones that superseded parts of these requests - live in [`../docs/Project_Planning.md`](../docs/Project_Planning.md).

---

## Turn 1 - the seed request

> **16:51** - Let's make a new project in "C:\Personal\Personal_Projects"
> Let's call the Project "Wargame_Concierge"
> Point of the project is to help me learn the rules of Wargames. The first wargame we'll work with is Warhammer 40K 11th Edition. Help me understand the rules, how to set up a board. Also to help me build some beginner army lists to play with.
> Import a Rising Tide style folder and header layout. Create the standard core documents as well.
> This project will be pushed to GitHub. Create a new project there.
> Source directory for files is "C:\Personal\40K"
> Import the necron list file into our project space. otherwise treat all other files in that directory as read only for now.

**Established:** the project name and location; the purpose - rules, board setup, beginner lists; Warhammer 40,000 11th Edition as the first system; Rising Tide as the documentation framework; GitHub as the destination; `C:\Personal\40K` as a read-only source library with a single named exception.

---

## Turn 2 - repository and content depth

> **16:52** - brand-new separate GitHub repo named Wargame_Concierge
> also draft real beginner content (rules overview, board setup, starter lists) in this first pass

**Established:** a standalone repository, not a monorepo leaf; and that the first pass ships **real drafted content**, not just scaffolding.

---

## Turn 3 - living web references

> **16:55** - for plan. website references for extra context and info (patches happen!):
> <https://www.warhammer-community.com/en-gb/>
> <https://wahapedia.ru/>

**Established:** the two living sources of record, and - in two words - the reason every rules claim in this repository carries a retrieval date. *Patches happen.*

---

## Turn 4 - the second army

> **16:57** - in armies, also create space_marines . I have a bunch of old models that can be used to make an enemy force for my son to pilot.
> To research: Gladius task force detachment rules and space marine army rules.

**Established:** Space Marines as the opposing force; the son as its player; that the models are **existing old kits**, which is why legacy and Firstborn datasheets stay in scope; and the named research targets.

---

## Turn 5 - process import

> **16:59** - from "C:\Users\rcatt\OneDrive - Ross Video\Documents\Python_Projects\daily_report"
> research and import info regarding multislice planning and multiagent processing.
> When done, apply these to this plan.

**Established:** the multi-slice, multi-agent workflow - Coordinator, Implementer, QA, Final Sanity, tiered checks, per-slice briefs and reports - adapted from an existing project rather than invented here.

---

## Turn 6 - table aids

> **17:05** - In plan, create a Keyword reference document for common weapon, movement, eetc. words I can search at a glance.
> Also create a 2 page "quick Reference Play Guide" for both Necrons annd Space Marines. goal is to print and laminate the guides for easy lookup during a game.

**Established:** the Keyword Glossary; and the two-page print-and-laminate play guides, whose page limit is a physical constraint rather than a style preference.

---

## Turn 7 - unit research scope

> **17:07** - for plan, when researching the Wahapedia info, look up unit rules for all Space Marine and Necron units. We'll use them to build army lists and datasheets for play later.

**Established:** full-roster research for both factions as a durable corpus, explicitly built to be consumed later by list building and printable datasheets.

---

## Turn 8 - the reusable scaffold

> **17:09** - from what we have here, create a general list of "types of files, reference docs, things we should create, etc" in a general sense that we can apply to other wargames as they come up.

**Established:** [`../docs/Game_System_Scaffold.md`](../docs/Game_System_Scaffold.md), and with it the principle that the project is **game-agnostic** - 40K 11e is the first worked example, not the only intended system.

---

## Turn 9 - confirmed ownership

> **17:12** - got an update for the Necron Lists file to apply before everything else gets started.
> - Have 1 squad of 10 necron warriors and 3 scarabs purchased (unassembled)
> - Have 1 squad of 5 immportals purchased (unassembled)
> - Purchased a used Hierotek CirCle Kill Team set. Need to post pictures for unit ID later. Assembled and painted (game ready)

**Established:** the real model pool every list must be written against; the Preflight slice that patched it at source before any other work; the build-before-play reality; and the still-open Hierotek Circle photo identification. This turn is also what superseded the earlier Kill Team: Tomb World assumption.

---

## Turn 10 - model discipline

> **17:33** - for plan, specify models for all subagents. balance priority.

**Established:** the locked per-role model matrix in [`../docs/handoffs/v1_scaffold/track_in.md`](../docs/handoffs/v1_scaffold/track_in.md) - thinking budget spent where accuracy matters, fast models on scaffolding, and Implementer and QA never on the same model family for the same slice.

---

## Turn 11 - the knowledge plane

> **17:37** - [attached: `llm-wiki-karpathy\.obsidian.zip`] for plan, let's create a Librarian agent and KB as per the kaparthy plan.

**Established:** the Karpathy "LLM Wiki" architecture - immutable `raw/`, a compounding `KB/` owned by a dedicated Librarian agent, schema in `AGENTS.md`, and the repository as an Obsidian vault. This is the decision that turned a documentation project into a knowledge base.

---

## Turn 12 - authorization

> **17:41** - execute C:\Users\rcatt\.cursor\plans\wargame_concierge_setup_ee78aead.plan.md

**Established:** track `v1_scaffold` begins.

---

## What the seed did not say

Worth recording, because these were inferred or decided later rather than requested:

| Not in the seed | Decided later | Where |
|-----------------|---------------|-------|
| That the GitHub repository would be **private** | Decided as part of the copyright posture | [`../docs/Project_Planning.md`](../docs/Project_Planning.md) Sec 2 |
| The `confidence` field on every KB page | Added by the Librarian at L0, because 11th Edition is new | `AGENTS.md` Sec 6 |
| Naming the knowledge layer `KB/` rather than `wiki/` | Deviation from the Karpathy pattern, stated explicitly in the schema | `AGENTS.md` Sec 2 |
| That Keywords would be glossary-only | Librarian schema decision at L0 | `AGENTS.md` Sec 5 |
| That Power Matrix is the Canoptek Court detachment rule | Clarified after L0 flagged the attribution as unresolved | [`../docs/Project_Planning.md`](../docs/Project_Planning.md) Sec 4 |

---

## Related

| Document | Relationship |
|----------|-------------|
| [`Distilled_Project_Context.md`](Distilled_Project_Context.md) | The compressed digest of what these turns produced |
| [`../docs/Project_Planning.md`](../docs/Project_Planning.md) | Decisions of record, including those that supersede parts of this file |
| [`../docs/Project_Origin_Story.md`](../docs/Project_Origin_Story.md) | The same story told as narrative, for a beginner |
| [`../docs/handoffs/v1_scaffold/track_in.md`](../docs/handoffs/v1_scaffold/track_in.md) | How the plan was decomposed into slices |

---

## Change Log

- v1.0 (2026-08-16): Captured all twelve seed turns verbatim with timestamps, plus what each established and what the seed did not cover. Created in slice S1.

## Attribution

- Project: Wargame_Concierge
- Maintainer: Russell Catt
- Sources: see header
- Structured using the Rising Tide framework

## Rising Tide Notes

- This document is a preserved artifact - **append only**, never reworded.
- Must remain traceable to the original session.
- If the project has drifted from this intent, that is a finding, not a reason to edit this file.
