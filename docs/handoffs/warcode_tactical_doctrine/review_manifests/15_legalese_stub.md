# Manifest §15 — Legalese (stub)

- **Track:** warcode_tactical_doctrine
- **Retrieval date:** 2026-08-23
- **Citation legend:** see `00_what_this_is_not.md`
- **Status:** stub — required clauses listed. Final wording is the owner's, drafted at S7.

## MANDATORY WORDING

The shipped §15 **MUST** contain the exact words **unofficial and unauthorized**. Locked in `track_in.md` (§0 / §15 review voice). Matching precedent already in `games/the_warcode/README.md`. — confidence: verified

§0 and §15 are twins: §0 sets reader expectations, §15 carries the legal position. Both carry the phrase. Do not let them drift apart.

## Required clauses

| # | Clause | Basis | Confidence |
|---|--------|-------|-----------|
| 1 | This document is **unofficial and unauthorized**. Not produced, reviewed, endorsed, sponsored, or approved by RedMakers or Gamefound. | `track_in.md` lock | verified |
| 2 | **The Warcode** and all associated names, factions, unit names, and artwork are the property of their respective owners (RedMakers). No ownership claimed. | `AGENTS.md` Sec 10 | verified |
| 3 | **Personal use only. Never for sale.** This project must never be sold or monetised in any form. | `AGENTS.md` Sec 10 (explicit) | verified |
| 4 | **Not a rules substitute.** Quoted material is scoped, cited, and partial; the free beta PDF from RedMakers is the only rules authority. Buy or download the official product. | `AGENTS.md` Sec 10 | verified |
| 5 | **Quote scope statement.** Verbatim rules quotes appear only under `games/the_warcode/rules/`, `setup/`, and `factions/`, each carrying filename plus page, under the project's scoped free-beta exception. `KB/` and `docs/` stay paraphrase. | `AGENTS.md` Sec 10; `.cursor/rules/warcode-quotes.mdc` | verified |
| 6 | **Edition scope.** Findings apply to the free public beta **V.0.8.7-F**, retrieved 2026-08-23, and may be superseded by any newer free beta or by the released game. | `[PTR]` | verified |
| 7 | **No affiliation, no contact.** Written from public material with no contact with the studio, no NDA material, and no early access. Owner holds a $1 VIP pledge only. | `[PTR]` | verified |
| 8 | **No STL redistribution.** No STL files are hosted, shared, or reproduced. Official STLs come via the Gamefound Field Commander tier only; no third-party sources are used or endorsed. | `AGENTS.md` Sec 10; `raw/pointers/warcode_stl_sources.md` | verified |
| 9 | **Trademark acknowledgement for the comparator.** Any comparison to another manufacturer's game is design commentary under fair comment; that publisher's trademarks remain theirs and are **not named** in shipping files. | `track_in.md` naming ban | verified |
| 10 | **Opinion disclaimer.** Assessments are opinion and inference from a beta document, made with **zero games played**. Not commercial, legal, or purchase advice. | this manifest set | verified |
| 11 | **Correction commitment.** Errors will be corrected on notice; RedMakers may request removal of any quoted material. | good practice | draft |

## Naming safety inside §15

- **Do not** name any Games Workshop product in the shipped legalese. Clause 9 stays generic — "another manufacturer's game", or **That other game**. — confidence: verified
- RedMakers and Gamefound **may** be named; the ban is comparator-only. — confidence: verified
- **No Games Workshop copyright line is required here.** The `AGENTS.md` Sec 10 GW notice and the `gw-unofficial-footer` rule apply to `games/warhammer_40k_11e/**` and `games/kill_team_2024/**` — not to a Warcode review. Do not paste a GW notice into `games/the_warcode/**`. — confidence: verified

## Placement guidance

- §15 belongs at the **end** of the shipped review, with a short forward-reference from §0.
- If the review is exported to print or PDF, the unofficial statement needs to be visible on the first page as well as in §15.
- No Rising Tide HTML header on handoff files (this manifest set); the **shipped** review under `games/the_warcode/reviews/` does carry the Rising Tide header and footer per `AGENTS.md` Sec 6.

## Open questions

- Does the owner want a takedown/contact line (clause 11) given this is a private repo and not published anywhere?
- Should clause 6 name an explicit recheck date, or just the retrieval date?
