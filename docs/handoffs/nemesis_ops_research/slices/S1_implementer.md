# S1 — Implementer (Full dossier OCR)

- **Status:** Resolved - Complete (QA PASS; late [S1 OCR](26bc15c7-07a1-435c-af43-8cb6d1007fa7) completion reconciled)
- **Track:** nemesis_ops_research
- **Slice:** S1
- **Model used:** `composer-2.5-fast` (background agent finished 80/80); Coordinator also resumed mid-stall — same sidecar outcome (~157 KB)
- **Date:** 2026-08-17
- **Commit:** pending

## Work performed

1. Full OCR of `1063073009-Kill-Team-Nemesis-Operatives-Dossier.pdf` (80 pages, image-scan).
2. Sidecar written **outside git:**  
   `C:\Personal\Kill Team\kill_team_2024\1063073009-Kill-Team-Nemesis-Operatives-Dossier.ocr.txt`
3. Tool: `C:\Program Files\Tesseract-OCR\tesseract.exe` 5.4.0 + PyMuPDF (~220–250 DPI, `--psm 6`).
4. Background agent completed full pass; Coordinator had also resumed from ~page 37–41 — final artifact is one complete sidecar.
5. Pointer updated with OCR path / tool / date.
6. Temp OCR work cleaned under Kill Team library (outside git).

## Spot-check

| Page | Notes |
|------|-------|
| 1 | Cover — heavily garbled (art + stylized title) |
| 4 | TOC usable: Monstrous Foe 4–11; Custom Builder 12–31; Mission Packs 32–79; Ambull / Archivist named |
| 15–17 | Builder steps readable: allegiance → size → behaviour (NPO) → weapons → traits |
| 40 | Rules prose — good (NPO activation / reinforcement) |
| 61–62 | Ambull pack: Joint Ops **The Hidden Enemy**; Adversary Ops **Decaying Generatorium** |
| 73–74 | Archivist pack: **Betrayal** / **Negotiation**; datacard region noisy — **do not paste into git** |
| 80 | Tomb World map — mixed / sparse labels |

**Garbled / vision-fallback (from agent + Coord spot-check):**  
- Severe: 1, 2, 6, 10 (cover/art)  
- Noisy datasheets/maps: 3, 13, 22–24, 33, 59–60, 64, 71–72  
- Also treat dense weapon/trait **tables** as digit-error risk — shipping pages must not carry dossier numbers anyway.

## Exit criteria self-check

| Criterion | Result |
|-----------|--------|
| Sidecar exists beside PDF | PASS (~157 KB) |
| 80 pages OCR'd | PASS (80 markers) |
| Pointer has tool + date | PASS |
| No `.ocr.txt` under git repo | PASS |
| No datasheet paste into repo | PASS |

## Commit

pending — Coordinator / user gate. Never commit OCR sidecar.
