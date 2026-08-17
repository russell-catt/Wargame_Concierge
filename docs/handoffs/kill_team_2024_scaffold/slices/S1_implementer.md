# S1 - Implementer report (Rules teaching content)

- **Status:** Resolved - Implemented (awaiting QA)
- **Track / slice:** kill_team_2024_scaffold / S1 (Tier 1 - implementation)
- **Date:** 2026-08-17
- **Model used (LOCKED):** `claude-sonnet-5-thinking-high` - matches the track's Implementer (teaching content) lock; no waiver needed
- **Depends:** S0 Resolved - Complete
- **Paths touched:** `games/kill_team_2024/rules/`, `docs/handoffs/kill_team_2024_scaffold/slices/`
- **`KB/` untouched:** YES
- **`raw/` untouched:** YES
- **`track_in.md` untouched:** YES (per dispatch instructions - status noted here only)
- **Commit:** none by this slice

---

## L1 dependency note

The dispatch context flagged that L1 might be running in parallel. At the time this slice read `track_in.md`, the L1 row was still **pending** and no `KB/` pages existed yet for `system: kill_team_2024` (confirmed at that point - zero matches searching `KB/**/*kill*`). Per the dispatch instruction, this slice therefore drafted all four documents citing `raw/pointers/kill_team_2024_core.md` and the living Wahapedia Kill Team 3 pages directly, with retrieval dates, marking every glossary entry `draft` rather than `verified`.

**L1 landed mid-slice.** Before this report was filed, a `git status` check surfaced that the Librarian had landed six new KB concept pages and a KB source page for `system: kill_team_2024` - `KB/sources/kill_team_2024_core_rules.md`, `KB/concepts/turning_points.md`, `KB/concepts/activations_apl.md`, `KB/concepts/orders_conceal_engage.md`, `KB/concepts/control_range_kill_team.md`, `KB/concepts/cover_kill_team.md`, `KB/concepts/injured_operatives.md` - plus a new Kill Team 2024 section in `KB/glossary.md`. This slice read all seven pages and did a **reconciliation pass**:

- Both this slice and L1 read the **same living Wahapedia core rules page**, retrieved the **same day**, and independently reached the **same conclusions** - same `draft` status throughout, and the same headline 40K collisions (Control Range vs Engagement Range, Cover's opposite mechanical direction, Injured vs Battle-shock, Engage-the-order vs Engagement-Range-the-zone). No contradictions found - nothing to flag.
- Added explicit citations from all four `rules/` documents and the `rules/README.md` index back to the matching KB source/concept pages (header `SOURCES` blocks, inline "Full concept page" pointers in `Key_Concepts.md`, KB links added to the relevant `Keyword_Glossary.md` rows, and `Related pages` sections updated on every file).
- Did **not** copy KB prose into the shipping docs, and did not change any KB page - `KB/` remains untouched by this slice; the citations are one-directional (shipping -> KB), matching how `v1_scaffold` S3 cited `KB/concepts/objective_control.md` without writing to it.
- Re-ran the UTF-8/no-UTF-16-null byte check after these edits; all five files still pass.

This is a stronger outcome than the brief anticipated: rather than choosing between "cite KB" or "cite raw/Wahapedia," this slice ended up doing both, with the KB pages arriving as independent confirmation of the same living source.

---

## Sources actually read this slice

| Source | What it gave | Retrieved |
|--------|-------------|-----------|
| `https://wahapedia.ru/kill-team3/the-rules/core-rules/` | Full core rules: Strategy phase, Firefight phase, all universal actions, the Shoot and Fight sequences, Key Principles (Control Range, Cover, Obscured, Damage, Orders, Ploys, Datacards, Precedence, Visible, etc.) | 2026-08-17 |
| `https://wahapedia.ru/kill-team3/the-rules/approved-ops-2025/` | The Crit Op / Kill Op / Tac Op scoring framework, primary op selection, the four-turning-point battle length, CP income by initiative | 2026-08-17 |
| `https://wahapedia.ru/kill-team3/the-rules/tac-ops/` | Confirmed Tac Op archetypes (Infiltration, Recon, Security, Seek & Destroy) and their reveal-condition mechanic, at a level that stayed high-level per the brief | 2026-08-17 |
| `raw/pointers/kill_team_2024_core.md` | Confirmed the owned local PDF path and the "core + update log over lite" precedence note | on disk, verified 2026-08-17 |
| `games/kill_team_2024/README.md` | The team/operative vocabulary mapping table this slice's content had to match | read 2026-08-17 |
| `games/warhammer_40k_11e/rules/*.md` (all four files) | Structural and tone template: Rising Tide header/footer shape, glossary status-column pattern, "coming from X" comparison-table idea | read 2026-08-17 |
| `KB/sources/kill_team_2024_core_rules.md` + 6 KB concept pages (`turning_points`, `activations_apl`, `orders_conceal_engage`, `control_range_kill_team`, `cover_kill_team`, `injured_operatives`) | L1's independent pass over the same living source; used for the reconciliation pass described below | read after L1 landed, 2026-08-17 |

**The owned Core Rules PDF was not opened this slice** - `C:\Personal\Kill Team\kill_team_2024\779937548-Core-Rules-KILL-TEAM-3E-Full-Scan.pdf` remains unread by any slice so far. Everything here traces to the living Wahapedia pages instead, which is why nothing is marked `verified`.

---

## Files created (4)

| Path | What it is |
|------|-----------|
| `games/kill_team_2024/rules/Overview.md` | What a game is, the battle/turning-point frame, how VP scoring works at a high level, what a kill team is made of, what you need to play, and a "coming from 40K" comparison table |
| `games/kill_team_2024/rules/Turn_Structure.md` | Checklist for one turning point: Strategy phase (Initiative, Ready, Gambit) and Firefight phase (activation loop, Expended, Counteract), plus a common-mistakes table |
| `games/kill_team_2024/rules/Key_Concepts.md` | APL and the ±1 net-modifier cap, Conceal vs Engage, control range, cover vs Obscured, the Shoot sequence, the Fight sequence, Wounded/Injured, and mission scoring at a high level |
| `games/kill_team_2024/rules/Keyword_Glossary.md` | Six grouped sections (phase/activation, movement, shooting/fighting, damage state, mission/scoring, team/equipment) plus a dedicated **Collisions with 40K vocabulary** table |

## Files modified (1)

| Path | Change |
|------|--------|
| `games/kill_team_2024/rules/README.md` | S0 stub replaced with a real index, confidence statement, and sources section (v1.0) |

Plus this report and `S1_brief.md`.

---

## Content decisions worth flagging

### Everything is `draft`, nothing is `verified`

Unlike the 40K `v1_scaffold` S3 slice - which opened four owned PDFs and could mark 80-plus terms `verified` - this slice worked entirely from living web sources. Every glossary entry is `draft`; a couple of general-knowledge asides (e.g. the note that casual mission packs like Volkus use "their own, usually simpler" scoring) are called out as `unverified` framing rather than sourced fact where the source didn't state it directly. **Recommend a follow-up slice open the owned Core Rules PDF and upgrade statuses**, flagging rather than silently fixing any conflicts it finds against this draft.

### Mission scoring kept deliberately high-level

Per the brief, `Key_Concepts.md` explains the Crit Op / Kill Op / Tac Op shape (what each scores, the 6VP cap, the primary-op bonus) but does not reproduce Approved Ops card text, per-mission Tac Op wording, or the Tac Op archetype card lists. `Overview.md` explicitly notes that narrative/casual mission packs (Volkus, Shadowhunt, 3e Starter Set) use their own, simpler structures rather than assuming Approved Ops always applies.

### APL ±1 cap stated as a rule, not as team-specific content

The Wahapedia core rules page states the cap explicitly ("the total can never be more than -1 or +1 from its normal APL... This takes precedence over all stat changes"). `Key_Concepts.md` states this rule and gives a worked example (APL 2 -> floor 1, ceiling 3) but does not enumerate which team abilities raise or lower APL - that is scoped to the team guides (S3-S6).

### The 40K-collision table is the highest-value addition in the glossary

Built by cross-reading `games/warhammer_40k_11e/rules/Keyword_Glossary.md` against the Kill Team terms drafted this slice. Twelve collisions are flagged, the most important being:

- **Control range (1", visibility-gated)** vs 40K's **Engagement Range (2"/5")** - roughly a quarter the distance and doing far more rules work (cover, marker control, Fight eligibility all key off it)
- **Cover** helps the **defender's dice** in Kill Team (a free retained success) but hurts the **attacker's dice** in 40K (worsens BS by 1) - same word, opposite mechanical direction
- **Injured** (a per-operative, half-Wounds damage-state debuff) explicitly called out as **not** a battle-shock equivalent - the trigger (wound threshold vs Leadership test) and the scope (one model vs a whole unit) are both different
- **Leader** is a keyword on individual Kill Team operatives; in 40K it's an attachment mechanic joining two units together - genuinely unrelated concepts sharing a word

### Vocabulary discipline held throughout

Every document says **kill team / operative**, never **army / unit**. Cross-checked against `games/kill_team_2024/README.md`'s mapping table (Force -> Kill team/team; Unit entry -> Operative datasheet [called "datacard" per the actual core rules - see Finding below]; Round structure -> Turning points/activation sequence).

### Finding - the S0 README's vocabulary table says "Operative datasheet"; the core rules say "datacard"

`games/kill_team_2024/README.md` (S0) maps "Unit entry" to "Operative datasheet." The Wahapedia core rules page (Key Principles > Datacards) consistently uses **datacard**, and this project's own 40K content already claims **datasheet** as the 40K term. This slice's new content uses **datacard** throughout and flags it explicitly in the Keyword_Glossary collision table ("never call a Kill Team datacard a 'datasheet' in this project's KT content"). **Recommend S0's README vocabulary table be corrected in a later slice** - not done here since this slice does not own `games/kill_team_2024/README.md`'s vocabulary table and the brief scoped this slice to `rules/` only.

---

## Copyright compliance

| Check | Result |
|-------|--------|
| GW binaries added to repo | **None.** 0 files matching `*.pdf,*.webp,*.png,*.jpg,*.jpeg` outside `.git` |
| PDF text extracted into the repo | **No PDF was opened this slice at all.** |
| Verbatim rules text reproduced | **No.** Teaching paraphrase throughout; the small number of quoted fragments (e.g. `[BLAST]`-style weapon rule names, the ±1 APL cap wording) are unavoidable rule labels/thresholds, not prose lifts |
| Datacard statlines reproduced | **No.** `Key_Concepts.md` explains what each stat means and states explicitly that statlines are never reproduced here |
| Approved Ops card text reproduced | **No.** Scoring shape described; card text and archetype lists not transcribed |
| Local library referenced | Path pointer only (`raw/pointers/kill_team_2024_core.md`), never opened |

---

## Tier 1 self-check

| # | Criterion | Result | Evidence |
|---|-----------|--------|----------|
| 1 | Four teaching documents created | PASS | `Test-Path` on each - see `S1_brief.md` Tier 1 commands |
| 2 | `rules/README.md` indexes them with confidence statement | PASS | v1.0, four-row read order table plus Confidence section |
| 3 | Required glossary sections present | PASS | Phase/activation, movement, shooting/fighting, damage/state, mission/scoring, team/equipment, plus the collision table |
| 4 | Content requirements from dispatch covered | PASS | Turning points/Strategy/Firefight (Overview, Turn_Structure); APL ±1 cap (Key_Concepts); Conceal vs Engage (Key_Concepts); cover, control range, Injured, Kill Op/Crit Op (Key_Concepts) |
| 5 | Glossary entries carry a status | PASS | every row tagged `draft`; none `verified` |
| 6 | Dedicated 40K-collision table present | PASS | 12 rows in Keyword_Glossary.md |
| 7 | Rules claims have a source and retrieval date | PASS | header source block plus footer date on every file |
| 8 | Rising Tide header and footer on every file | PASS | 5 files (4 new + README) |
| 9 | No YAML frontmatter stacked on Rising Tide headers | PASS | no file starts with `---` |
| 10 | Vocabulary is team/operative, never army/unit | PASS | scanned all five files |
| 11 | No datacard statlines or verbatim rules text reproduced | PASS | see Copyright compliance |
| 12 | No GW binaries | PASS | 0 matches |
| 13 | All files UTF-8 without BOM / no UTF-16 null bytes | PASS | byte-checked; see Tier 1 commands output |
| 14 | **`KB/` untouched** | PASS | `git status --porcelain -- KB` empty |
| 15 | **`raw/` untouched** | PASS | `git status --porcelain -- raw` empty |
| 16 | **`track_in.md` untouched** | PASS | not opened for writing this slice |
| 17 | No commit, no push | PASS | no git write command issued |
| 18 | Links resolve | PASS | relative paths checked from each file's own directory |

---

## Gaps and blockers

| Item | Status | Owner |
|------|--------|-------|
| **Owned Core Rules PDF never opened** | Every glossary entry is `draft`; none `verified`, in both this slice's docs and the KB pages L1 landed. Highest-value next action for whoever picks up rules content next | A future rules-verification pass (neither the Librarian nor this slice can open binaries) |
| **S0 vocabulary table says "datasheet," actual term is "datacard"** | Flagged above; not fixed here (out of this slice's scoped path) | Coordinator / next `games/kill_team_2024/README.md` touch |
| **KB glossary reconciliation** | **Resolved this slice.** L1 landed a matching Kill Team 2024 KB section and six concept pages mid-slice; reconciled with no contradictions found, and this slice's docs now cite them (see L1 dependency note above) | Closed |
| **Casual mission-pack scoring (Volkus, Shadowhunt, 3e Starter) not detailed** | Deliberately out of scope - `Overview.md` flags that they use their own structure | S2 / mission-pack-specific slices |
| **Team-specific APL modifiers not enumerated** | Deliberately scoped out - belongs to team guides | S3-S6 |

Nothing here blocks S2 (setup + killzones) or L2.

---

## Inherited documentation (paste-ready for the next slice)

> **Read before starting:**
> - [`games/kill_team_2024/rules/Keyword_Glossary.md`](../../../../games/kill_team_2024/rules/Keyword_Glossary.md) - the shared vocabulary, including the 40K-collision table. Use these exact terms; use **datacard**, not "datasheet."
> - [`games/kill_team_2024/rules/Key_Concepts.md`](../../../../games/kill_team_2024/rules/Key_Concepts.md) - APL, Orders, control range, cover, and Injured, so later content does not re-explain them.
>
> **What is currently `draft`, not verified:** everything in the rules spine. The owned Core Rules PDF has not been opened by any slice yet - do not treat anything here as settled without checking it.
>
> **What later content must not repeat:** calling a Kill Team operative's rules entry a "datasheet" (it's a datacard); describing Injured as Kill Team's battle-shock equivalent (it isn't - see the collision table); assuming Approved Ops 2025 scoring applies to every mission pack (Volkus/Shadowhunt/3e Starter use their own).
>
> **Conventions:** `games/**` uses Rising Tide headers and footers, never YAML frontmatter. Teaching paraphrase only; no GW binaries; path pointers to `C:\Personal\Kill Team\kill_team_2024`. Never write `raw/` or `KB/`. Never commit or push. Byte-check markdown for UTF-16 null bytes as a final action if editing existing files (standing defect noted on the `v1_scaffold` track).

---

## Next

**S2** - setup + killzones + Critical Ops README, building on the control-range/cover vocabulary established here. **L1 is complete** for the core-rules pass and has already been reconciled against this slice's shipping docs (see the L1 dependency note above) - no outstanding reconciliation work remains. The one open thread for whichever slice picks up rules content next: **open the owned Core Rules PDF** and upgrade both the KB pages and this shipping glossary from `draft` to `verified` where confirmed, flagging rather than silently overwriting any conflicts it turns up.
