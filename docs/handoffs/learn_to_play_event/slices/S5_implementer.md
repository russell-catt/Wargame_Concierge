# S5 — Implementer report

- **Status:** Resolved - Implemented
- **Track:** `learn_to_play_event`
- **Slice:** S5
- **Model:** `inherit`
- **Commit:** pending (IMP-09 deferred; subagent never git)

## Exit criteria self-check

| Criterion | Result |
|-----------|--------|
| Each listed aid exists (HTML) | PASS — 5 HTML + README under `games/warhammer_40k_11e/armies/necrons/print/` |
| `@page` US Letter; heading hierarchy | PASS — `@page { size: letter; margin: 0.5in; }`; h1/h2/h3 + tables |
| QA print-preview ≤2 pages per aid | PASS — PyMuPDF: all five PDFs report **2 pages** |
| Every S5 PDF in the one print folder | PASS — `C:\Personal\print_aids\learn_to_play_event\` |
| No `.pdf` committed to git | PASS — PDFs only outside repo; `*.pdf` gitignored; none in print HTML folder |

## HTML artifacts (commit these)

| File | Role |
|------|------|
| `games/warhammer_40k_11e/armies/necrons/print/README.md` | Index + print folder path |
| `games/warhammer_40k_11e/armies/necrons/print/40k_roster_250_conclave.html` | 245-pt Cryptek Conclave roster (unit boxes) |
| `games/warhammer_40k_11e/armies/necrons/print/40k_reference_250_conclave.html` | Reanimation + Conclave menu + do/don’t |
| `games/warhammer_40k_11e/armies/necrons/print/40k_necrons_quick_reference.html` | Twin of Quick Reference Play Guide |
| `games/warhammer_40k_11e/armies/necrons/print/40k_first_game_core.html` | Turn order + hit/wound/save + OC/Battle-shock |
| `games/warhammer_40k_11e/armies/necrons/print/40k_setup_terrain.html` | First-game setup + cover/terrain areas |
| `games/warhammer_40k_11e/armies/necrons/print/_html_to_pdf.py` | Playwright Letter PDF generator |

## PDF artifacts (outside repo — do not commit)

Print folder: `C:\Personal\print_aids\learn_to_play_event\`

| PDF | Pages |
|-----|-------|
| `40k_roster_250_conclave.pdf` | 2 |
| `40k_reference_250_conclave.pdf` | 2 |
| `40k_necrons_quick_reference.pdf` | 2 |
| `40k_first_game_core.pdf` | 2 |
| `40k_setup_terrain.pdf` | 2 |

## PDF generation

- Method: Python + Playwright Chromium (`_html_to_pdf.py`)
- Result: **succeeded** — all five PDFs written to the locked print folder
- Commands:

```powershell
pip install playwright
playwright install chromium
python games/warhammer_40k_11e/armies/necrons/print/_html_to_pdf.py
```

## Notes

- Codex wall: army aids are teaching paraphrase; core rule IDs used as pointers only.
- Roster is **245 pts** (Geomancer 75, Warriors 10/80, Tomb Crawlers 2/50, Scarabs 3/40); 255-pad ramble omitted.
- Reference drops long shooting math; keeps spend order, wipe rule, Conclave picks, do/don’t.
- Personal use only footer on each aid.
