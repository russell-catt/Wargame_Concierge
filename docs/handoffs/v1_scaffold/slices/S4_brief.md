# S4 - Brief (Necron starters + laminate guide)

- **Status:** Resolved - Implemented (awaiting QA)
- **Track:** v1_scaffold
- **Slice:** S4 (Implementer, Tier 1)
- **Tier:** 1 - Implementation
- **Date:** 2026-08-16

## Requirements

All under `games/warhammer_40k_11e/armies/necrons/`:

1. `Reanimation_Protocols.md` - army rule teaching guide. Paraphrase only; pointer to the faction pack path
2. `Canoptek_Court.md` - the Power Matrix and how it plays for a beginner (concept verified in S3)
3. `Cryptek_Conclave.md` - record the correct rule name, **Technosorcerous Augmentations**, against the old "Scientific Schemes" label (S3 Finding 2). Teaching level
4. `Starter_250.md` - learning list preferring the Hierotek Circle once identified (flag `TBD`); unassembled Warriors / Scarabs / Immortals marked **build before play**; provisional list with ownership notes
5. `Starter_500.md` - expansion using the owned kits once built, with clear purchase vs owned tags
6. `Quick_Reference_Play_Guide.md` - **exactly 2 pages** for laminate:
   - `<!-- pagebreak -->` between page 1 and page 2
   - Page 1: turn phases; Reanimation / army rule cheat; Canoptek Court Power Matrix cheat; combat sequence in 4-6 lines
   - Page 2: starter snapshot; 5-8 do/don't; keyword mini-strip; pre-game and end-turn reminders
   - Footer: `Verify vs Munitorum / faction pack - patches happen | 2026-08-16`
   - Dense and scannable. No shopping content, no lore, no full datasheets
7. Update `armies/necrons/README.md` to link all six
8. `S4_brief.md`, `S4_implementer.md`; update `track_in.md`

### Standing constraints

- Ownership-aware throughout: nothing unassembled is presented as playable
- **Verify every printed points value against** `C:\Personal\40K\rules\Warhammer 40,000_ Munitorum Field Manual.pdf`
- S3 finding carried in: owner-note points in `Necron_Lists.md` are stale - prefer the MFM for any number printed, annotated with verify date **2026-08-16**

## Depends / User gate

| Dependency | Notes |
|------------|-------|
| S3 Resolved - Implemented | YES - rules spine and `Keyword_Glossary.md` exist |
| Do NOT commit | Coordinator only |
| Do NOT push | S7 user gate |
| Do NOT write `KB/` | Librarian owns it. Conflicts are **flagged**, not applied |
| Do NOT write `raw/` | Immutable layer |
| Do NOT copy PDFs into the repo | Path pointers only |
| Hierotek Circle ID | **Still blocked on user photos.** Ship `TBD` rather than guessing box contents |

## Entrance criteria

| Criterion | Attested |
|-----------|----------|
| `games/warhammer_40k_11e/rules/Keyword_Glossary.md` readable | YES |
| `games/warhammer_40k_11e/rules/Key_Concepts.md` and `Turn_Structure.md` readable | YES |
| `Owned_Models_Inventory.md` current as of 2026-08-16 | YES |
| Munitorum Field Manual present at the catalogued path | YES - v1.2, 7 pages |
| Necrons Faction Pack v1.1 present | YES - 57 pages |

## Exit criteria

- Six new documents under `games/warhammer_40k_11e/armies/necrons/`
- `armies/necrons/README.md` indexes all six
- Every points value printed anywhere in the slice traces to **Munitorum Field Manual v1.2**, read 2026-08-16
- `Quick_Reference_Play_Guide.md` is exactly two pages with one `<!-- pagebreak -->` marker and the required footer
- Unassembled models are never presented as fieldable; Hierotek Circle stays `TBD`
- Cryptek Conclave rule named **Technosorcerous Augmentations**; "Scientific Schemes" appears only as a correction
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
| Basis | Same-family substitute (Claude, thinking-high tier); waiver recorded in `S4_implementer.md` and `track_in.md` |
| QA | `gpt-5.6-sol-medium` - different family, so playbook Sec 18.7 separation holds |

## Tier 1 commands

```powershell
$root = "C:\Personal\Personal_Projects\Wargame_Concierge"

@(
  "games\warhammer_40k_11e\armies\necrons\Reanimation_Protocols.md",
  "games\warhammer_40k_11e\armies\necrons\Canoptek_Court.md",
  "games\warhammer_40k_11e\armies\necrons\Cryptek_Conclave.md",
  "games\warhammer_40k_11e\armies\necrons\Starter_250.md",
  "games\warhammer_40k_11e\armies\necrons\Starter_500.md",
  "games\warhammer_40k_11e\armies\necrons\Quick_Reference_Play_Guide.md",
  "games\warhammer_40k_11e\armies\necrons\README.md",
  "docs\handoffs\v1_scaffold\slices\S4_brief.md",
  "docs\handoffs\v1_scaffold\slices\S4_implementer.md"
) | ForEach-Object { "{0,-70} {1}" -f $_, (Test-Path "$root\$_") }

# Laminate is exactly two pages: exactly one pagebreak marker
(Select-String -Path "$root\games\warhammer_40k_11e\armies\necrons\Quick_Reference_Play_Guide.md" -Pattern '<!-- pagebreak -->').Count

# Old detachment rule name appears only as a correction
Select-String -Path "$root\games\warhammer_40k_11e\armies\necrons\*.md" -Pattern 'Scientific Schemes'

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

**S5** mirrors this shape for Space Marines - Oath of Moment, Gladius Task Force, starter lists, and a matching laminate. **S6** expands the unit research these lists name. **L2** reconciles `KB/` against the corrections this slice ships, including the Cryptek Conclave rule name and the re-costed points.
