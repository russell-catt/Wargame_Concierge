# OCR Spot-check Matrix — Nemesis Operatives Dossier

- **Track:** nemesis_ops_ocr_spotcheck
- **PDF:** `C:\Personal\Kill Team\kill_team_2024\1063073009-Kill-Team-Nemesis-Operatives-Dossier.pdf`
- **OCR:** `...\1063073009-Kill-Team-Nemesis-Operatives-Dossier.ocr.txt`
- **Date opened:** 2026-08-17
- **Status:** S0 matrix built; S1 vision results filled 2026-08-17

## Scoring rubric

| Result | Meaning |
|--------|---------|
| PASS | OCR prose matches page enough to trust teaching paraphrase |
| PARTIAL | Usable with noted caveats |
| FAIL | OCR unreliable — do not use for new claims |
| TABLE | Dense numeric/table region — **numbers stay out of git** |

## Matrix (≥20 pages)

| Page | Band | Claim under test / focus | OCR note (S0) | Vision (S1) | Error type |
|------|------|--------------------------|---------------|-------------|------------|
| 1 | A | Cover title | Heavily garbled stylized art | FAIL | garble |
| 4 | A | TOC: Builder 12–31, Mission packs 32–79 | TOC keywords present; noisy | PARTIAL | noise |
| 12 | B | Custom Builder section start | Mostly narrative art/prose mix | PARTIAL | art+prose |
| 15 | B | Blank datacards + begin create steps | Clear: two blank datacards, app/WarCom, steps | PASS | — |
| 16 | B | Behaviour (NPO) / Battler | Clear behaviour steps; Battler closes to fight | PASS | — |
| 17 | B | Weapons selection by size | Clear weapon selection rules | PASS | — |
| 20 | B | Traits / allegiance + nemesis trait | Clear trait selection prose | PASS | — |
| 22 | E | Dense table / art | Near-total garble | TABLE / FAIL | table+art |
| 25 | C | Worked example Spectre Squad / Imperium Medium Marksman | Step list readable (allegiance/size/behaviour) | PASS | — |
| 28 | C/E | Worked example weapons (Crisis-like) | Weapon names partially readable; table noisy | TABLE | table |
| 31 | C | Worked example Angels of Death Large Guardian | Step list readable | PASS | — |
| 33 | E | Art / pack opener | Art-heavy garble | FAIL | art |
| 40 | D | NPO activation / reinforcement table | Activation results readable | PASS | — |
| 59 | E | Ambull / Borewyrm datacard art | Labels Ambull/Borewyrm; stats noisy | TABLE | table |
| 61 | D | Ambull pack intro + mission names | Hidden Enemy / Decaying Generatorium present | PASS | — |
| 62 | D | Ambull Intruder deck / mission structure | Intruder deck rules readable | PASS | — |
| 64 | E | Map / art | Sparse/noisy | FAIL | art/map |
| 71 | E | Archivist datacard region | Name + weapon labels; stats noisy | TABLE | table |
| 73 | D | Archivist pack intro | Archivist missions; player-op option | PASS | — |
| 74 | D | Betrayal (Joint Ops) / Negotiation (Adversary Ops) | Titles + modes clear in game sequence | PASS | — |
| 80 | A/D | Tomb World map labels | Mixed labels | PARTIAL | map |
| 13 | E | S1 noise — builder table page | (seed) | TABLE | table |
| 23 | E | S1 noise — table | (seed) | TABLE | table |
| 24 | E | S1 noise — table | (seed) | TABLE | table |
| 60 | E | S1 noise — Ambull region | (seed) | TABLE | table |
| 72 | E | S1 noise — Archivist region | (seed) | TABLE | table |

**Count scored:** 26 pages (≥20). High bands B/D/E covered.

## Shipping claim crosswalk (S1→S2)

| Shipping claim | Pages | Vision outcome | Action |
|----------------|-------|----------------|--------|
| How-To create steps (datacards → allegiance → size → behaviour → weapons → traits) | 15–17, 20 | PASS | Eligible for `verified` process confidence |
| Ambull missions: Hidden Enemy / Decaying Generatorium | 61–62 | PASS | Confirm titles; mark vision-verified |
| Archivist: Betrayal / Negotiation; Joint vs Adversary Ops | 73–74 | PASS | Confirm naming dual-label intentional |
| Worked example names (Spectre / Angels of Death examples) | 25, 31 | PASS | Qualitative OK |
| Dense weapon/trait point tables | 22, 28, 59, 71, etc. | TABLE | Keep out of git; Open_Questions narrow to tables only |

## Change Log

- v1.0 (2026-08-17): S0 matrix + S1 vision fill (Coordinator / composer + vision on PDF via PyMuPDF render + OCR concordance).
