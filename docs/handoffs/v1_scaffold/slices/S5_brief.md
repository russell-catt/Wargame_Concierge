# S5 - Brief (Space Marine Oath/Gladius + laminate)

- **Status:** Resolved - Implemented (awaiting QA)
- **Track:** v1_scaffold
- **Slice:** S5 (Implementer, Tier 1)
- **Tier:** 1 - Implementation
- **Date:** 2026-08-16

## Requirements

All under `games/warhammer_40k_11e/armies/space_marines/`:

1. `Oath_of_Moment.md` - army rule teaching guide. Paraphrase only; pointer to the faction pack path
2. `Gladius_Task_Force.md` - Combat Doctrines: when to spend each, plus once-per-battle reminders
3. `Owned_Models_Inventory.md` - update the worksheet if needed, **keeping the fill-in structure** for the son's collection
4. `Starter_250.md` - provisional Gladius learning list with older-kit / Firstborn swap notes
5. `Starter_500.md` - provisional expansion; mark provisional wherever inventory is unknown
6. `Quick_Reference_Play_Guide.md` - **exactly 2 pages** for laminate:
   - `<!-- pagebreak -->` between page 1 and page 2
   - Page 1: turn phases; Oath cheat (what to pick); Gladius doctrines cheat; combat sequence
   - Page 2: starter snapshot; do/don't; keyword strip; pre-game and end-turn reminders
   - Footer: `Verify vs Munitorum / faction pack | 2026-08-16`
   - Dense and scannable. No shopping content, no lore, no full datasheets
7. Update `armies/space_marines/README.md`
8. `S5_brief.md`, `S5_implementer.md`; update `track_in.md`

### Standing constraints

- Ownership-aware throughout: the Space Marine collection has **never been audited**, so nothing may be presented as owned
- **Verify every printed points value against** `C:\Personal\40K\rules\Warhammer 40,000_ Munitorum Field Manual_Marines.pdf` (and/or the main MFM)
- Verify rules against `C:\Personal\40K\rules\eng_22-07_warhammer_40,000_faction_pack_space_marines.pdf`
- S4 finding carried in: check for **first-unit / later-unit pricing**, which several datasheets use
- Teaching paraphrase only; no KB writes; UTF-8 convert at the end if needed

## Depends / User gate

| Dependency | Notes |
|------------|-------|
| S4 Resolved - Implemented | YES - the Necron shape S5 mirrors exists |
| Do NOT commit | Coordinator only |
| Do NOT push | S7 user gate |
| Do NOT write `KB/` | Librarian owns it. Conflicts are **flagged**, not applied |
| Do NOT write `raw/` | Immutable layer |
| Do NOT copy PDFs into the repo | Path pointers only |
| Space Marine collection audit | **Still blocked on the user.** Ship the procedure and costed candidates; do not guess ownership |

## Entrance criteria

| Criterion | Attested |
|-----------|----------|
| `games/warhammer_40k_11e/rules/Keyword_Glossary.md` readable | YES |
| `games/warhammer_40k_11e/rules/Turn_Structure.md` and `Key_Concepts.md` readable | YES |
| `armies/necrons/` S4 output readable as the pattern to mirror | YES |
| Space Marines Faction Pack present at the catalogued path | YES - v1.1, 219 pages |
| Munitorum Field Manual **Marines** present | YES - v1.2, 15 pages |
| `armies/space_marines/Owned_Models_Inventory.md` | Present but **empty** - expected |

## Exit criteria

- Five new documents under `games/warhammer_40k_11e/armies/space_marines/`, plus the rebuilt inventory worksheet
- `armies/space_marines/README.md` indexes all of them
- Every points value printed anywhere in the slice traces to **MFM Marines v1.2**, read 2026-08-16
- `Quick_Reference_Play_Guide.md` is exactly two pages with one `<!-- pagebreak -->` marker and the required footer
- **No ownership invented.** Every list entry tagged `TBD`; the inventory worksheet keeps its fill-in rows
- Combat Doctrines taught as spend-decisions with explicit once-per-battle tracking
- Rising Tide header and footer on every `games/**` file; **no YAML frontmatter stacked on top**
- Teaching paraphrase only; no statlines, no GW binaries in the repo
- All new and modified files UTF-8 without BOM
- **`KB/` untouched**, **`raw/` untouched**
- **No commit, no push**

## Model

| Field | Value |
|-------|-------|
| Locked (Implementer - content) | `claude-sonnet-5-thinking-high` |
| **Blocked at dispatch** | YES |
| Actually used | `claude-opus-5-thinking-high` |
| Basis | Same-family substitute (Claude, thinking-high tier); waiver recorded in `S5_implementer.md` and `track_in.md` |
| QA | `gpt-5.6-sol-medium` - different family, so playbook Sec 18.7 separation holds |

## Tier 1 commands

```powershell
$root = "C:\Personal\Personal_Projects\Wargame_Concierge"

@(
  "games\warhammer_40k_11e\armies\space_marines\Oath_of_Moment.md",
  "games\warhammer_40k_11e\armies\space_marines\Gladius_Task_Force.md",
  "games\warhammer_40k_11e\armies\space_marines\Owned_Models_Inventory.md",
  "games\warhammer_40k_11e\armies\space_marines\Starter_250.md",
  "games\warhammer_40k_11e\armies\space_marines\Starter_500.md",
  "games\warhammer_40k_11e\armies\space_marines\Quick_Reference_Play_Guide.md",
  "games\warhammer_40k_11e\armies\space_marines\README.md",
  "docs\handoffs\v1_scaffold\slices\S5_brief.md",
  "docs\handoffs\v1_scaffold\slices\S5_implementer.md"
) | ForEach-Object { "{0,-72} {1}" -f $_, (Test-Path "$root\$_") }

# Laminate is exactly two pages: exactly one pagebreak marker
(Select-String -Path "$root\games\warhammer_40k_11e\armies\space_marines\Quick_Reference_Play_Guide.md" -Pattern '<!-- pagebreak -->').Count

# Laminate footer present
Select-String -Path "$root\games\warhammer_40k_11e\armies\space_marines\Quick_Reference_Play_Guide.md" -Pattern 'Verify vs Munitorum'

# No ownership invented - inventory still has fill-in rows
(Select-String -Path "$root\games\warhammer_40k_11e\armies\space_marines\Owned_Models_Inventory.md" -Pattern '\(fill in\)').Count

# UTF-16 byte check (L1 Finding 1 - standing defect; run LAST)
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

**S6** expands the unit research these lists name - Intercessors, Assault Intercessors, Hellblasters, Infernus, Tactical Squad, Scouts, Dreadnoughts. **L2** reconciles `KB/` against the corrections this slice ships, including the Oath of Moment purity condition, the Gladius doctrine wording, and the `unverified` Gladius entry in `Keyword_Glossary.md`. The **collection audit** remains a user action and gates any move from provisional to final lists.
