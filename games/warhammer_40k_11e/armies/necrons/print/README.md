# Necrons — 40K Letter print aids

HTML sources for US Letter (max 2 pages) table aids. Generate PDFs **outside** this repo.

## Print folder (locked)

`C:\Personal\print_aids\learn_to_play_event\`

Filename prefix: `40k_`. Never commit `*.pdf` (repo gitignore).

## Aids

| HTML (this folder) | PDF (print folder) | Source |
|--------------------|--------------------|--------|
| `40k_roster_250_conclave.html` | `40k_roster_250_conclave.pdf` | `../Army_List_250_Conclave.md` |
| `40k_reference_250_conclave.html` | `40k_reference_250_conclave.pdf` | `../Reference_Guide_250_Conclave.md` |
| `40k_necrons_quick_reference.html` | `40k_necrons_quick_reference.pdf` | `../Quick_Reference_Play_Guide.md` |
| `40k_first_game_core.html` | `40k_first_game_core.pdf` | `../../rules/Turn_Structure.md` + `Key_Concepts.md` |
| `40k_setup_terrain.html` | `40k_setup_terrain.pdf` | `../../setup/Board_Setup.md` + `Terrain_Basics.md` |
| `40k_conclave_primary_missions.html` | `40k_conclave_primary_missions.pdf` | `../Cryptek_Conclave_Primary_Missions.md` |
| *(setup)* `../../setup/print/40k_chapter_approved_force_dispositions.html` | `40k_chapter_approved_force_dispositions.pdf` | `../../setup/Chapter_Approved_Force_Dispositions.md` |

## Combined event print bag

Saturday checklist (KT son / KT dad / 40K dad):  
[`games/kill_team_2024/setup/Learn_to_Play_Print_Bag.md`](../../../../kill_team_2024/setup/Learn_to_Play_Print_Bag.md)

All event PDFs (KT + 40K) share `C:\Personal\print_aids\learn_to_play_event\`.


## Regenerate PDFs

```powershell
pip install playwright
playwright install chromium
python games/warhammer_40k_11e/armies/necrons/print/_html_to_pdf.py
```

Or Edge headless per file:

```powershell
msedge --headless --disable-gpu --print-to-pdf="C:\Personal\print_aids\learn_to_play_event\40k_roster_250_conclave.pdf" "file:///C:/Personal/Personal_Projects/Wargame_Concierge/games/warhammer_40k_11e/armies/necrons/print/40k_roster_250_conclave.html"
```
