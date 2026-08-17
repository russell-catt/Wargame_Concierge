# S1 — Brief (Full dossier OCR)

- **Status:** Ready
- **Track:** nemesis_ops_research
- **Slice:** S1
- **Intended Implementer model:** `composer-2.5-fast`
- **Intended QA model:** `gpt-5.6-sol-medium`

## Requirements

1. Full OCR of `C:\Personal\Kill Team\kill_team_2024\1063073009-Kill-Team-Nemesis-Operatives-Dossier.pdf` (80 pages, image-scan)
2. Write sidecar **outside git**: `C:\Personal\Kill Team\kill_team_2024\1063073009-Kill-Team-Nemesis-Operatives-Dossier.ocr.txt`
3. Tool: `C:\Program Files\Tesseract-OCR\tesseract.exe` + PyMuPDF for page render (recommended). Document tool + version + date on pointer.
4. Spot-check several pages for readability; list garbled pages for vision fallback in S2
5. Update `raw/pointers/kill_team_2024_nemesis_operatives.md` with OCR path, tool, date — **never commit OCR**
6. Confirm OCR file is NOT under the git repo
7. File `S1_implementer.md` — Commit: pending

## Depends

| Dependency | Notes |
|------------|-------|
| S0 Resolved - Implemented | Required |
| Do NOT commit OCR or PDFs | Absolute |
| Do NOT git commit | Coordinator gate |

## Exit criteria

- Sidecar exists beside PDF; readable text for majority of pages
- Pointer documents OCR tool + date + path
- Spot-check table in implementer report
- Zero OCR content committed to git working tree under repo root
- `S1_implementer.md` filed

## Tier 1 commands

```powershell
Test-Path "C:\Personal\Kill Team\kill_team_2024\1063073009-Kill-Team-Nemesis-Operatives-Dossier.ocr.txt"
(Get-Item "C:\Personal\Kill Team\kill_team_2024\1063073009-Kill-Team-Nemesis-Operatives-Dossier.ocr.txt").Length -gt 50000
Select-String -Path "C:\Personal\Personal_Projects\Wargame_Concierge\raw\pointers\kill_team_2024_nemesis_operatives.md" -Pattern 'ocr|Tesseract' -Quiet
# ensure no .ocr.txt under repo
@(Get-ChildItem "C:\Personal\Personal_Projects\Wargame_Concierge" -Recurse -Filter "*.ocr.txt" -ErrorAction SilentlyContinue).Count -eq 0
```

## Copyright

- OCR stays outside git forever
- Do not paste dossier OCR datasheet text into repo files
