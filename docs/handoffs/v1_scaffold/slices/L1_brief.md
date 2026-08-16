# L1 - Brief (Librarian ingest)

- **Status:** Resolved - Implemented (awaiting QA)
- **Track:** v1_scaffold
- **Slice:** L1 (Librarian, Tier 0)
- **Tier:** 0 - Knowledge entrance

> Retro-filled by the Librarian during L1 execution so the slice has a brief of record, matching the pattern used for `L0_brief.md`. Coordinator authors briefs normally.

## Requirements

1. Ingest `raw/Necron_Lists.md` - the Preflight-updated Necron expansion blueprint
2. Ingest `reference/Source_Library.md` as a source in its own right; summarize into `KB/sources/` without copying binaries
3. Ingest the `raw/pointers/*.md` stubs
4. Seed concept pages from the ownership facts and the detachments the sources name
5. Create `KB/sources/` pages for Necron_Lists, Source_Library, and the web pointers (Wahapedia, Warhammer Community)
6. Create `KB/factions/necrons.md` and `KB/factions/space_marines.md` (stub synthesis for the latter)
7. Create `KB/detachments/canoptek_court.md`, `cryptek_conclave.md`, `gladius_task_force.md` - high level
8. Create `KB/concepts/` pages for `reanimation_protocols`, `oath_of_moment`, `objective_control`, `power_matrix` as warranted by the Sec 5 promotion test
9. Update `KB/glossary.md` - **resolve Power Matrix as the Canoptek Court detachment rule**; expand terms for S3 `Keyword_Glossary` alignment
10. Update `KB/index.md`, `KB/log.md` (ingest entry dated 2026-08-16), `KB/overview.md`, `KB/changelog.md`
11. Optional: `KB/analyses/inherited_docs_for_S3.md` listing stable facts ready for teaching promotion
12. Write `L1_brief.md` and `L1_librarian.md`; update `track_in.md` (S2 Done, L1 status)

### The correction this slice owns

L0 seeded **Power Matrix** in the glossary with an explicit warning that it might belong to *Kill Team* rather than 40K, because the owner's Hierotek Circle is a Kill Team box. **That is wrong.** Power Matrix is the **Canoptek Court detachment rule in Warhammer 40,000 11th Edition**. L1 must correct it and record why the earlier inference failed.

### Ownership facts to capture (must match Preflight)

| Item | Qty | Status |
|------|-----|--------|
| Necron Warriors | 10 | Purchased, unassembled |
| Canoptek Scarab Swarms | 3 | Purchased, unassembled |
| Immortals | 5 | Purchased, unassembled |
| Hierotek Circle Kill Team | 1 set | Game ready; unit ID pending photos |
| Kill Team: Tomb World | - | **Not owned** |

## Depends / User gate

| Dependency | Notes |
|------------|-------|
| S2 Resolved - Implemented | YES - sources and Necron import landed |
| Write **only** under `KB/` and the `L1_*` handoff docs | Librarian edit surface |
| Do NOT write `raw/` | Karpathy layer contract - immutable |
| Do NOT commit | Coordinator only |
| Do NOT push | S7 user gate |
| UTF-8 | No UTF-16, no BOM |

## Entrance criteria

| Criterion | Attested |
|-----------|----------|
| L0 KB scaffold present - `AGENTS.md`, 6 core pages, 7 typed directories | YES |
| S2 sources present - `reference/Source_Library.md`, `raw/Necron_Lists.md`, 8 pointer stubs | YES |
| Preflight ownership facts confirmed and mirrored in the S2 inventory | YES |
| `KB/ingest_procedure.md` defines the project ingest contract | YES |

## Exit criteria

- 5-15+ KB pages created or updated, per the scale expectation in `KB/ingest_procedure.md`
- A `KB/sources/` page per ingested source, each carrying provenance, edition, coverage, and fan-out
- Faction, detachment, and concept pages created with valid frontmatter and honest `confidence`
- **Power Matrix resolved** as the Canoptek Court 40K detachment rule, in both `KB/concepts/power_matrix.md` and `KB/glossary.md`, with the superseded claim on the deprecated list
- Glossary expanded and sectioned for S3 `Keyword_Glossary` alignment
- `KB/index.md` carries a row for every new page
- `KB/log.md` has an ingest entry dated **2026-08-16**
- `KB/changelog.md` records the correction and states why nothing was promoted
- Every rules claim names a verification route
- `L1_brief.md` and `L1_librarian.md` present; `track_in.md` updated
- All files UTF-8
- **`raw/` untouched** - no creates, edits, or deletes
- **No commit, no push**
- No GW binaries, no verbatim rules text

## Tier 1 commands

```powershell
$root = "C:\Personal\Personal_Projects\Wargame_Concierge"

# Pages exist
@(
  "KB\sources\necron_lists_owner_notes.md",
  "KB\sources\source_library.md",
  "KB\sources\local_library_pointers.md",
  "KB\sources\wahapedia.md",
  "KB\sources\warhammer_community.md",
  "KB\factions\necrons.md",
  "KB\factions\space_marines.md",
  "KB\detachments\canoptek_court.md",
  "KB\detachments\cryptek_conclave.md",
  "KB\detachments\gladius_task_force.md",
  "KB\concepts\power_matrix.md",
  "KB\concepts\reanimation_protocols.md",
  "KB\concepts\oath_of_moment.md",
  "KB\concepts\objective_control.md",
  "KB\analyses\inherited_docs_for_S3.md"
) | ForEach-Object { "{0,-55} {1}" -f $_, (Test-Path "$root\$_") }

# Frontmatter and confidence on every KB page (README stubs exempt)
Get-ChildItem "$root\KB" -Recurse -Filter *.md |
  Where-Object { $_.Name -ne "README.md" } |
  ForEach-Object {
    $t = Get-Content $_.FullName -Raw
    "{0,-40} fm={1} conf={2}" -f $_.Name, ($t.StartsWith("---")), ($t -match "confidence:")
  }

# The correction landed
Select-String -Path "$root\KB\glossary.md" -Pattern "Canoptek Court detachment rule"
Select-String -Path "$root\KB\glossary.md" -Pattern "not Kill Team"
Select-String -Path "$root\KB\concepts\power_matrix.md" -Pattern "Resolved"

# Log and ownership
Select-String -Path "$root\KB\log.md" -Pattern "^## \[2026-08-16\] ingest"
Select-String -Path "$root\KB\factions\necrons.md" -Pattern "10 \(1 squad\)|Tomb World"

# Encoding: no UTF-16
Get-ChildItem "$root\KB","$root\docs\handoffs" -Recurse -Filter *.md | ForEach-Object {
  $b = [System.IO.File]::ReadAllBytes($_.FullName)
  if (($b | Select-Object -First 200 | Where-Object { $_ -eq 0 }).Count -gt 0) { "UTF-16?: $($_.FullName)" }
}

# Wikilinks resolve. Inline code spans are stripped first, because the
# glossary entry-format block and the index legend show [[...]] as examples.
$kb = Get-ChildItem "$root\KB" -Recurse -Filter *.md
$names = @{}; $kb | ForEach-Object { $names[$_.BaseName] = $true }
$kb | ForEach-Object {
  $f = $_
  $t = (Get-Content $_.FullName -Raw -Encoding utf8) -replace '`[^`]*`', ''
  [regex]::Matches($t, '\[\[([^\]\|]+)\]\]') | ForEach-Object {
    $tgt = $_.Groups[1].Value.Trim()
    if (-not $names.ContainsKey($tgt)) { "BROKEN [[$tgt]] in $($f.Name)" }
  }
}

# Guardrails
Get-ChildItem "$root\raw" -Recurse -Force | Select-Object FullName, Length, LastWriteTime
@(Get-ChildItem $root -Recurse -Include *.pdf,*.webp,*.png,*.jpg -File -Force -ErrorAction SilentlyContinue).Count -eq 0
git -C $root status --short
git -C $root log --oneline
```

## Tier 2 expectations

QA independently verifies:

1. Every exit criterion above, with evidence
2. **The Power Matrix correction is complete and consistent** - `glossary.md`, `power_matrix.md`, `canoptek_court.md`, `necrons.md`, and `necron_lists_owner_notes.md` must all agree, and no page may still describe the attribution as unresolved
3. `confidence` values are honest, not inflated - specifically that nothing sourced only from the owner's planning notes is marked `verified` as a rules claim
4. Every `[[wikilink]]` in a KB page resolves to a file that exists
5. Every new page has an `index.md` row, and the confidence in that row matches the page frontmatter
6. `raw/` file list, sizes, and timestamps unchanged from the S2 state
7. No verbatim GW rules text; ownership and points figures traceable to `raw/Necron_Lists.md`
8. `git status` shows the expected untracked and modified files only; no new commit

## Recommended models

| Role | Model | Notes |
|------|-------|-------|
| Librarian | `claude-fable-5-thinking-high` | Locked matrix - **unavailable at dispatch** |
| Librarian (actual) | `claude-opus-5-thinking-high` | **Model waiver** - same-family substitute; recorded in `L1_librarian.md` |
| QA | `gpt-5.6-sol-medium` | Different family from the substitute, per playbook Sec 18.7 |

## Inherited documentation

- Track input: [`track_in.md`](../track_in.md) - model matrix, constraints, Preflight ownership notes
- Prior Librarian slice: [`L0_librarian.md`](L0_librarian.md) - schema decisions and the two open threads L1 inherits
- Prior slice: [`S2_implementer.md`](S2_implementer.md) - what landed in `raw/` and `reference/`
- Schema SoT: [`AGENTS.md`](../../../../AGENTS.md)
- Ingest contract: [`KB/ingest_procedure.md`](../../../../KB/ingest_procedure.md)
- Operations: [`librarian_agent.md`](../../../operations/librarian_agent.md)

## Feeds

**S3** (rules + setup + `Keyword_Glossary`) takes L1 Resolved - Complete as its Tier 0 entrance criterion. The inherited block in [`L1_librarian.md`](L1_librarian.md) is paste-ready for the S3 brief, and [`KB/analyses/inherited_docs_for_S3.md`](../../../../KB/analyses/inherited_docs_for_S3.md) is the detailed handoff.
