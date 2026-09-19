# Space Marines — Letter print aids

HTML sources for US Letter table aids. Generate PDFs **outside** this repo (`*.pdf` gitignored).

## Print folder (suggested)

`C:\Personal\print_aids\40k_11e\`

Filename prefix: `40k_`.

## Son 500 play pack

| HTML | Source | Pages |
|------|--------|-------|
| `40k_sm_army_list_500.html` | [`../Army_List_500_Matched_Statted.md`](../Army_List_500_Matched_Statted.md) | 2 |
| `40k_sm_how_army_works_500.html` | [`../How_Your_Army_Works_500.md`](../How_Your_Army_Works_500.md) | 5 |
| `40k_11e_cheat_sheet_wounds.html` | System cheat + Core 05.02 wound matrix (pack copy) | 2 |

Index: [`../Son_Play_Pack_500.md`](../Son_Play_Pack_500.md).

**Key distances:** coherency **2″/9″** · Ingress **6″** edge · Deep Strike **>8″**.

## Regenerate PDFs (US Letter)

```powershell
cd games\warhammer_40k_11e\armies\space_marines\print
python _html_to_pdf.py
```

HTML `@page { size: letter; … }` drives dimensions. Script writes Letter PDFs to (first available):

1. `C:\Personal\print_aids\40k_11e\` (owner Windows path)
2. `~/print_aids/40k_11e/`
3. `/opt/cursor/artifacts/print_aids_40k_11e/` (cloud download folder)

Needs Playwright Chromium **or** Google Chrome / Chromium headless. `*.pdf` stays gitignored.
