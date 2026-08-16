# L0 - Brief (Karpathy KB bootstrap)

- **Status:** Resolved - Implemented (awaiting QA)
- **Track:** v1_scaffold
- **Slice:** L0 (Librarian, Tier 0)
- **Tier:** 0 - Knowledge entrance

> Retro-filled by the Librarian during L0 execution so the slice has a brief of record. Coordinator authors briefs normally.

## Requirements

1. Create `AGENTS.md` at the repo root - adapt the Karpathy `CLAUDE.md` schema to the **wargames** domain (not technical writing)
2. Create `docs/operations/librarian_agent.md` - day-to-day Librarian operations, pointing to `AGENTS.md` as schema SoT
3. Create the KB core pages: `index.md`, `log.md`, `overview.md`, `glossary.md`, `changelog.md`, `ingest_procedure.md`
4. Seed the glossary with Reanimation Protocols, Oath of Moment, Power Matrix, Objective Control - marked for expansion in L1/S3
5. Copy `llm-wiki.md` to `reference/`
6. Extract `.obsidian.zip` to `.obsidian/` at the repo root
7. Leave the existing typed KB directories in place; README stubs optional
8. Write `L0_brief.md` and `L0_librarian.md` to `docs/handoffs/v1_scaffold/slices/`

## Sources to adapt from

| Source | Use |
|--------|-----|
| `llm-wiki-karpathy/CLAUDE.md` | Adapt into root `AGENTS.md` for the wargame domain |
| `llm-wiki-karpathy/llm-wiki.md` | Copy verbatim to `reference/llm-wiki.md` |
| `llm-wiki-karpathy/.obsidian.zip` | Extract to `.obsidian/` at the repo root |
| `llm-wiki-karpathy/wiki/` | Empty-page pattern, if useful for seeding |

## Depends / User gate

| Dependency | Notes |
|------------|-------|
| **S0 Resolved - Complete** | YES - S0 QA PASS (Coordinator waiver on criterion 5) |
| Do NOT commit | Coordinator only |
| Do NOT push | S7 user gate |
| Do NOT write `raw/` | Karpathy layer contract - Librarian reads only |

## Entrance criteria

| Criterion | Attested |
|-----------|----------|
| S0 PASS - repo scaffold, `templates/`, playbook, `.gitignore` present | YES |
| `KB/` typed directories exist as stubs | YES (7 dirs with `.gitkeep`) |
| `AGENTS.md`, `KB/index.md`, `.obsidian/` intentionally absent from S0 | YES (per S0 exit criteria) |
| Karpathy source files readable | YES |

## Exit criteria

- `AGENTS.md` at the repo root defines: role, layer contract (`raw/` immutable, `KB/` owned, **not** `wiki/`), the 8 wargame entity types, YAML frontmatter matching those types, and the ingest / query / lint workflows
- Session-start checklist present: `AGENTS.md` -> `KB/index.md` -> last log entries
- Copyright rules present: no GW PDFs or images into `raw/`, no committed binaries, teaching paraphrase only
- Living references named: Warhammer Community, Wahapedia
- `docs/operations/librarian_agent.md` covers day-to-day ops and L0/L1/L2 maturity, and points to `AGENTS.md` as schema SoT
- All 6 KB core pages exist with valid frontmatter
- Glossary seeded with the 4 named terms, each flagged for L1/S3 expansion
- `KB/log.md` has an L0 bootstrap entry dated **2026-08-16**
- `KB/changelog.md` has an L0 bootstrap row
- `reference/llm-wiki.md` matches the upstream source
- `.obsidian/` exists at the repo root
- **`raw/` untouched** - no creates, edits, or deletes
- **No commit, no push**
- No GW binaries anywhere in the repo

## Tier 1 commands

```powershell
$root = "C:\Personal\Personal_Projects\Wargame_Concierge"
Test-Path "$root\AGENTS.md"
Test-Path "$root\docs\operations\librarian_agent.md"
@("index","log","overview","glossary","changelog","ingest_procedure") | ForEach-Object { Test-Path "$root\KB\$_.md" }
Test-Path "$root\reference\llm-wiki.md"
Test-Path "$root\.obsidian"
-not (Test-Path "$root\wiki")
Select-String -Path "$root\KB\log.md" -Pattern "2026-08-16"
Select-String -Path "$root\KB\glossary.md" -Pattern "Reanimation Protocols|Oath of Moment|Power Matrix|Objective Control"
@(Get-ChildItem $root -Recurse -Include *.pdf,*.webp,*.png,*.jpg -File -Force -ErrorAction SilentlyContinue).Count -eq 0
git -C $root status --short
git -C $root log --oneline
```

`raw/` immutability check - compare against the S0 inventory (`raw/README.md` 810 bytes, `raw/pointers/README.md` 236 bytes, no other files):

```powershell
Get-ChildItem "$root\raw" -Recurse -Force | Select-Object FullName, Length, LastWriteTime
```

## Tier 2 expectations

QA independently verifies:

1. Every exit criterion above, with evidence
2. `AGENTS.md` is genuinely **wargame-domain** - no leftover technical-writing entity types (`feature`, `product`, `persona`, `style`)
3. `AGENTS.md` uses `KB/` throughout and never instructs an agent to create `wiki/`
4. Frontmatter `type:` values in the KB core pages match the types declared in `AGENTS.md`
5. `raw/` file list, sizes, and timestamps are unchanged from S0
6. `git log` is still empty and `git status` shows untracked files only
7. Internal links in `AGENTS.md`, `librarian_agent.md`, and the KB core pages resolve to real paths

## Recommended models

| Role | Model | Notes |
|------|-------|-------|
| Librarian | `claude-fable-5-thinking-high` | Locked matrix - **unavailable at dispatch** |
| Librarian (actual) | `claude-opus-5-thinking-high` | **Model waiver** - same-family substitute; recorded in `L0_librarian.md` |
| QA | `gpt-5.6-sol-medium` | Different family from the Librarian, per playbook Sec 18.7 |

## Inherited documentation

- Track input: [`track_in.md`](../track_in.md) - model matrix, constraints, Preflight ownership notes
- Playbook: [`multiagent_coordinator_strategy.md`](../../../operations/multiagent_coordinator_strategy.md) Sec 18 (Librarian), Sec 18.5 (Tier 0), Sec 18.10 (report template)
- Prior slice: [`S0_implementer.md`](S0_implementer.md) - the "Intentionally NOT created (L0 Librarian)" list is L0's scope
- Prior QA: [`S0_qa.md`](S0_qa.md) - criterion 5 waiver confirms `KB/` owns typed dirs, `raw/` does not
- Pattern reference: [`reference/llm-wiki.md`](../../../../reference/llm-wiki.md)
- Layer contract: [`raw/README.md`](../../../../raw/README.md)

## Feeds

**S1** (core RT docs + `Game_System_Scaffold`) takes L0 Resolved - Complete as its Tier 0 entrance criterion. The inherited block in [`L0_librarian.md`](L0_librarian.md) is paste-ready for the S1 brief.
