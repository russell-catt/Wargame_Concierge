# S3 - Brief (Rules + Setup + Keyword_Glossary)

- **Status:** Resolved - Implemented (awaiting QA)
- **Track:** v1_scaffold
- **Slice:** S3 (Implementer, Tier 1)
- **Tier:** 1 - Implementation
- **Date:** 2026-08-16

## Requirements

1. `games/warhammer_40k_11e/rules/Overview.md` - what a game is; points sizes; win via objectives; force structure; beginner tone
2. `games/warhammer_40k_11e/rules/Turn_Structure.md` - phase checklist for your turn
3. `games/warhammer_40k_11e/rules/Key_Concepts.md` - attack sequence (hit -> wound -> save -> damage), battle-shock, Objective Control, leaders at a high level
4. `games/warhammer_40k_11e/rules/Keyword_Glossary.md` - required categories: movement/positioning; shooting/weapons; melee; saves/damage; mission/army; faction pointers to the Necron and Space Marine guides. Format is `Keyword - one-line plain English (+ when it matters)`
5. `games/warhammer_40k_11e/setup/Board_Setup.md` - table size, deployment, objectives, pre-game checklist, pointer to Source_Library
6. `games/warhammer_40k_11e/setup/Terrain_Basics.md` - terrain types, A4 footprint packs at `C:\Personal\40K\Terrain\A4` (path pointer only), "enough terrain" guidance
7. Update `rules/README.md` and `setup/README.md` to index the new files
8. `S3_brief.md`, `S3_implementer.md`; update `track_in.md`

### Keyword coverage required by the plan

Advance, Fall Back, Normal Move, Remain Stationary, Engagement Range, Pile In, Consolidate, Deep Strike / Reserves (high level), Rapid Fire, Assault, Heavy, Pistol, Torrent, Blast, Lethal Hits, Sustained Hits, Devastating Wounds, Ignores Cover, Twin-Linked, Hazardous, Indirect Fire, Anti-X, Melta, Extra Attacks, Charge, Heroic Intervention, Armour and Invulnerable saves, Feel No Pain patterns, Reanimation Protocols (pointer), Objective Control, Battle-shock, Leader / Bodyguard, Detachment, plus see-also entries for Oath of Moment and Power Matrix.

## Depends / User gate

| Dependency | Notes |
|------------|-------|
| L1 Resolved - Implemented | YES - `KB/analyses/inherited_docs_for_S3.md` exists |
| Do NOT commit | Coordinator only |
| Do NOT push | S7 user gate |
| Do NOT write `KB/` | Librarian owns it. Conflicts found in sources are **flagged**, not applied |
| Do NOT write `raw/` | Immutable layer |
| Do NOT copy PDFs into the repo | Path pointers only |

## Entrance criteria

| Criterion | Attested |
|-----------|----------|
| `KB/analyses/inherited_docs_for_S3.md` readable | YES |
| `KB/glossary.md` populated (32 terms, sectioned) | YES |
| `reference/Source_Library.md` catalogues the local library | YES |
| Local PDFs present at the catalogued paths | YES - 13 files under `C:\Personal\40K\rules`, 6 under `C:\Personal\40K\Terrain\A4` |
| `games/warhammer_40k_11e/rules` and `setup` stubs exist from S2 | YES |

## Exit criteria

- Six new teaching documents exist under `games/warhammer_40k_11e/`
- Both section READMEs index them
- Every rules claim is teaching paraphrase with a verification route and a retrieval date
- Glossary terms carry a `verified` / `draft` / `unverified` status
- Rising Tide header and footer on every `games/**` file; **no YAML frontmatter stacked on top**
- Footer on every document tells the reader to verify against the current Munitorum Field Manual and faction pack, dated 2026-08-16
- No GW binaries in the repo; A4 terrain packs referenced by path only
- All new and modified files UTF-8 without BOM
- **`KB/` untouched**, **`raw/` untouched**
- **No commit, no push**

## Model

| Field | Value |
|-------|-------|
| Locked (Implementer - content) | `claude-sonnet-5-thinking-high` |
| **Blocked at dispatch** | YES |
| Actually used | `claude-opus-5-thinking-high` |
| Basis | Same-family substitute (Claude, thinking-high tier); waiver recorded in `S3_implementer.md` and `track_in.md` |
| QA | `gpt-5.6-sol-medium` - different family, so playbook Sec 18.7 separation holds |

## Tier 1 commands

```powershell
$root = "C:\Personal\Personal_Projects\Wargame_Concierge"

@(
  "games\warhammer_40k_11e\rules\Overview.md",
  "games\warhammer_40k_11e\rules\Turn_Structure.md",
  "games\warhammer_40k_11e\rules\Key_Concepts.md",
  "games\warhammer_40k_11e\rules\Keyword_Glossary.md",
  "games\warhammer_40k_11e\rules\README.md",
  "games\warhammer_40k_11e\setup\Board_Setup.md",
  "games\warhammer_40k_11e\setup\Terrain_Basics.md",
  "games\warhammer_40k_11e\setup\README.md",
  "docs\handoffs\v1_scaffold\slices\S3_brief.md",
  "docs\handoffs\v1_scaffold\slices\S3_implementer.md"
) | ForEach-Object { "{0,-62} {1}" -f $_, (Test-Path "$root\$_") }

# UTF-16 byte check (L1 Finding 1 - standing defect)
Get-ChildItem $root -Recurse -Filter *.md -File |
  Where-Object { $_.FullName -notmatch '\\\.git\\' } |
  ForEach-Object {
    $b = [System.IO.File]::ReadAllBytes($_.FullName)
    if (($b | Select-Object -First 200 | Where-Object { $_ -eq 0 }).Count -gt 0) { $_.FullName }
  }

# No GW binaries
(Get-ChildItem $root -Recurse -File -Include *.pdf,*.webp,*.png,*.jpg,*.jpeg |
  Where-Object { $_.FullName -notmatch '\\\.git\\' }).Count

# KB and raw untouched
git -C $root status --porcelain -- KB raw
```

## Feeds

**S4** (Necron starters) and **S5** (Space Marine starters) build on the shared vocabulary and the attack-sequence explanation here. **L2** lints the new shipping content against `KB/`, including the two conflicts S3 flagged.
