# Necrons — 40K Letter print aids

HTML sources for US Letter (max 2 pages) table aids. Generate PDFs **outside** this repo.

## Print folder (locked)

`C:\Personal\print_aids\learn_to_play_event\`

Filename prefix: `40k_`. Never commit `*.pdf` (repo gitignore).

## Aids

| HTML (this folder) | PDF (print folder) | Source | Pages |
|--------------------|--------------------|--------|-------|
| `40k_roster_500_conclave.html` | `40k_roster_500_conclave.pdf` | `../Army_List_500_V1_Conclave.md` | 2 |
| `40k_how_army_works_500_conclave.html` | `40k_how_army_works_500_conclave.pdf` | `../How_Your_Army_Works_500.md` | 5 |
| `40k_conclave_primary_missions.html` | `40k_conclave_primary_missions.pdf` | `../Cryptek_Conclave_Primary_Missions.md` | 2 |
| `40k_roster_250_conclave.html` | `40k_roster_250_conclave.pdf` | `../Army_List_250_Conclave.md` | 2 |
| `40k_reference_250_conclave.html` | `40k_reference_250_conclave.pdf` | `../Reference_Guide_250_Conclave.md` | 2 |
| `40k_necrons_quick_reference.html` | `40k_necrons_quick_reference.pdf` | `../Quick_Reference_Play_Guide.md` | 2 |
| `40k_first_game_core.html` | `40k_first_game_core.pdf` | `../../rules/Turn_Structure.md` + `Key_Concepts.md` | 2 |
| `40k_setup_terrain.html` | `40k_setup_terrain.pdf` | `../../setup/Board_Setup.md` + `Terrain_Basics.md` | 2 |

**500 play pack index:** [`../Cryptek_Play_Pack_500.md`](../Cryptek_Play_Pack_500.md).

**Pack PDF folder:** `C:\Personal\print_aids\40k_11e\` (also cloud `/opt/cursor/artifacts/print_aids_40k_11e/`).  
**Legacy 250 event bag:** `C:\Personal\print_aids\learn_to_play_event\`.

**System print PDFs:** `C:\Personal\print_aids\40k_11e\` — run `../../setup/print/_html_to_pdf.py`.

**Key distances (table truth):** coherency **2″/9″** · Ingress **6″** edge · Deep Strike **>8″** · OC on terrain **footprint**.

## Combined event print bag

Saturday checklist (KT son / KT dad / 40K dad):  
[`games/kill_team_2024/setup/Learn_to_Play_Print_Bag.md`](../../../../kill_team_2024/setup/Learn_to_Play_Print_Bag.md)

## Regenerate PDFs (US Letter)

```powershell
cd games\warhammer_40k_11e\armies\necrons\print
python _html_to_pdf.py
```

HTML `@page { size: letter }` drives dimensions. Needs Playwright Chromium **or** Google Chrome / Chromium. `*.pdf` stays gitignored.
## GW unofficial footer

Every HTML file in this folder carries **UNOFFICIAL** banner (page 1) and **non-endorsement** footer on each page. Template: [`templates/Gw_Print_Banner.html`](../../../../../templates/Gw_Print_Banner.html). Policy: [`docs/handoffs/gw_community_content/track_in.md`](../../../../../docs/handoffs/gw_community_content/track_in.md).

---

## Games Workshop notice

**UNOFFICIAL.** This document is completely unofficial and in no way endorsed by Games Workshop Limited. Personal / no-charge use only — never for sale. Warhammer, Warhammer 40,000 and associated marks are trademarks of Games Workshop Limited. Used without permission. No challenge to their status intended. Warhammer 40,000 is Copyright Games Workshop Limited. Teaching notes by Russell Catt (Wargame Concierge). Games Workshop retains IP in the settings and characters. No official logos.

