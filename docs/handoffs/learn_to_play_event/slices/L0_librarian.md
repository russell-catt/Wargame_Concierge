# L0 — Librarian report (KT PDF source receipt)

- **Track:** `learn_to_play_event`
- **Slice:** L0
- **Status:** Resolved - Implemented
- **Model:** inherit (Librarian hat)
- **Date:** 2026-08-21
- **Commit:** pending (Coordinator / user gate)

## Pointers consulted

| Pointer | Path |
|---------|------|
| Teams | [`raw/pointers/kill_team_2024_teams.md`](../../../../raw/pointers/kill_team_2024_teams.md) |
| Core | [`raw/pointers/kill_team_2024_core.md`](../../../../raw/pointers/kill_team_2024_core.md) |
| Missions | [`raw/pointers/kill_team_2024_missions.md`](../../../../raw/pointers/kill_team_2024_missions.md) |

## PDFs read in place (not copied into repo)

| Team / topic | Filename | Pages | Notes |
|--------------|----------|-------|-------|
| Plague Marines | `eng_29-04_kt_teamrules_plague_marines-liggy6zl51-fa8nryqey9.pdf` | 11 | Date stamp **29-04** (29 Apr) |
| Kommandos | `eng_17-06_kill_team_team_rules_kommandos_online_rules-ova8v1kjds-ds3ouz4k04.pdf` | 13 | Date stamp **17-06** (17 Jun); includes update-log Q&A |
| Hierarchy | Full-Scan Core + `eng_17-06` update log supersede Jul 25 lite | — | Omission is not a patch (AGENTS.md Sec 10) |

Volkus Door Fight / Condensed Stronghold: already paraphrased in shipping [`games/kill_team_2024/setup/killzones/volkus.md`](../../../../games/kill_team_2024/setup/killzones/volkus.md); Core/mission pointers confirm Volkus Compound pack path. No new Door Fight quote dump this slice.

## Plague Marines — roster (confirmed)

**Source:** Teams PDF p.3 / selection pages (extract pages covering ARCHETYPE + OPERATIVES).

> 1 PLAGUE MARINE CHAMPION operative  
> 5 PLAGUE MARINE operatives selected from: BOMBARDIER, FIGHTER, HEAVY GUNNER, ICON BEARER, MALIGNANT PLAGUECASTER, WARRIOR  
> Your kill team can only include **each operative on this list once**.

**Legal size = 6 operatives** (Champion + 5 unique). Shipping `Starter_Roster.md` “suggested first four” is **wrong for Saturday** — flag for S3 fix. Existing `Team_Rule_Guide.md` already quotes this correctly.

Archetypes: SECURITY, SEEK & DESTROY.

## Kommandos — roster (confirmed)

**Source:** Teams PDF p.4 / p.12 (OPERATIVES / KILL TEAM SELECTION).

> 1 KOMMANDO BOSS NOB with one of: Slugga; big choppa **or** Slugga; power klaw  
> 9 KOMMANDO operatives selected from: BOMB SQUIG, BOY, BREACHA BOY, BURNA BOY, COMMS BOY, DAKKA BOY, GROT, ROKKIT BOY, SLASHA BOY, SNIPA BOY  
> Other than BOY operatives, your kill team can only include each operative on this list once.  
> **Half selections:** BOMB SQUIG and GROT count as half a selection each (both together = one selection).

**Selection budget:** Boss Nob + **9** selections (Boys may duplicate; specialists once; Squig+Grot share one slot).

Archetypes: INFILTRATION, SEEK & DESTROY.

### Faction rule (for Implementer)

**Throat Slittas** (PDF p.4): each friendly KOMMANDO (excluding BOMB SQUIG) can Charge while Conceal.

### Ploys / equipment names (for Implementer; quote in S1)

Strategy: Dakka! Dakka! Dakka!; Sssshhhh!; Waaagh!; Skulk About.  
Firefight: Just a Scratch; Shake It Off; Krump ’Em!; Kunnin’ But Brutal.  
Equipment: Choppas; Collapsible Stocks; Dynamite; Harpoon.

## Conflicts / flags (not silently fixed)

1. PM shipping QR/Starter still claim Wahapedia / “PDF not opened” and wrong roster framing — **S3**.
2. Kommandos shipping is stub only — **S1**.
3. PDF OCR/layout sometimes separates “These operatives count as half…” from Squig/Grot labels; selection pages confirm Squig+Grot half-pair — Implementer must quote contiguous selection block with page cite.
4. Temporary extract text under `docs/handoffs/learn_to_play_event/_extract/` is **working notes only** — delete before any commit; never promote into `KB/`.

## KB

**No KB writes this slice.** No ploy/datacard dump.

## Exit criteria self-check

- [x] Three pointer files listed
- [x] PM 6-op roster stated
- [x] Kommandos selection (1 Nob + 9; Squig+Grot half) stated
- [x] Conflicts flagged
- [x] No binaries in repo; no KB quote dump
