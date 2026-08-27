# Research plan restatement — dataslate_0826

- **Track:** `dataslate_0826`
- **Branch:** `feature/dataslate_0826`
- **For:** Owner review
- **Date:** 2026-08-27
- **Status:** Research packed; **shipping not authorized** until you gate execution

---

## Package shape (owner lock — both systems)

**There is no singular Balance Dataslate PDF for Kill Team or for 40K.**

| System | Package = | Not |
|--------|-----------|-----|
| **40K** | **Core / universal rules update** + **faction / army updates** (Faction Packs) + **points** (MFM) + WarCom commentary for intent | One titled “Balance Dataslate” file |
| **Kill Team** | **Core rules update** (killzone / mission-pack update logs, etc.) + **team online rules** updates + WarCom commentary for intent | One titled “Balance Dataslate” file |

Currency stamps name the **package pieces and dates**, not a fictional dataslate filename.

**Also in this track (separate product):** Codex: Space Marines **October preview** — readiness / honesty only; **not** early list rewrites to preview stats.

---

## What we already researched (filed under `research/`)

### 40K package pieces

| Piece | Stamp / legal | Research note | Shipping slice |
|-------|---------------|---------------|----------------|
| Universal Rules Updates | **v1.1** · legal **26 Aug 2026** | `40k_universal_rules_updates_v1_1.md` | **S2e** |
| Necrons Faction Pack | **v1.2** · legal **26 Aug 2026** | `staging_40k_faction_packs_v1_2.md` | **S2** (rules/FAQ teaching) |
| Space Marines Faction Pack | **v1.2** · legal **26 Aug 2026** | same | **S2** |
| Munitorum Field Manual — Necrons | **v1.3** | `necron_mfm_v1_3.md` (Warriors 10: **80→85**, other ▲) | **S2c** |
| Munitorum Field Manual — Space Marines | **v1.3** | `sm_mfm_v1_3.md` (BR Matched cores largely unchanged) | **S2d** |
| WarCom “What’s New?” commentary | Aug package intent | `warcom_40k_balance_commentary_aug.md` | Context for S2 (FD maps); Orks / other factions out of onboarded scope |
| SM Codex October preview | Preview only | `sm_codex_oct_preview.md` | **S2b** (Legendary Proxies / Legends honesty) |

### Kill Team package pieces

| Piece | Stamp | Research note | Shipping slice |
|-------|-------|---------------|----------------|
| Tomb World update log | Aug ’26 | `staging_kt_august_updates.md` | **S3** |
| Mission packs update log | Aug ’26 | same | **S3** |
| Team online rules (AoD `eng_26-08_`, Canoptek, Plague Marines, Hierotek, …) | dated packs in staging | inventory + commentary | **S3** (priority teams + Hierotek regen note) |
| WarCom quarterly “top five” | Aug quarterly | `warcom_kt_balance_commentary_aug.md` | Intent; **waiver** Fellgor / Goremongers / Raveners / Wolf Scouts unless you expand |

### Staging

- **14 PDFs** in `raw/_dataslate_0826_staging/` (temporary; **CLEANUP before merge to `main`**).
- Inventory: `staging_inventory_2026_08_27.md`.
- Drive folder unread (egress); staging supersedes Drive for this track.

---

## Research → shipping map (proposed)

```text
S0   Resolve L1–L3 newsletter links (when egress/pastes allow); lock package stamps; impact matrix
S1   Pointers under raw/pointers/ + footer currency convention (no binaries)
S2   40K shipping from package pieces (FP v1.2 teaching + FD map notes as needed) — not a singular dataslate hunt
S2b  SM Codex Oct readiness (honesty only)
S2c  Necron MFM v1.3 list recost
S2d  SM MFM v1.3 stamp + Casual Legends check
S2e  Universal Rules v1.1 (Core quotes / disembark teaching)
S3   KT Core+team package → priority teams + Tomb World/Nemesis + Hierotek note
S4   Project core currency (README, START_HERE, docs cores, …)
S5   Per-game cores + footer sweep; Warcode “not affected by GW package” stamp
L0–L1  KB source stubs + enhance (paraphrase)
CLEANUP  Delete staging PDFs + remove temp gitignore negation
FS   Final Sanity (third model) + legibility spot-checks
```

**QA:** every slice — Implementer ≠ QA ≠ Final Sanity (locked model matrix in `track_in.md`).

**Onboarded shipping scope:** Necrons + Space Marines (40K); Canoptek / Plague Marines / Angels of Death priority (+ Hierotek note) for KT. Other factions/teams from commentary stay research-only unless you expand.

---

## Proposed currency stamps (footers — additive)

| Surface | Stamp text (proposal) |
|---------|------------------------|
| 40K package | `Rules currency: 40K Aug 2026 package — Universal Rules v1.1 · Faction Pack v1.2 · MFM v1.3 (legal / App 26 Aug 2026 where dated)` |
| KT package | `Rules currency: Kill Team quarterly balance — August 2026 (Core / update logs + team online rules)` |
| SM Codex | Preview note only until Codex ships |
| Warcode | `Last reviewed: <date> · not affected by Games Workshop balance packages` |

Do **not** invent a “Balance Dataslate YYYY-MM-DD” line when no such file exists.

---

## Explicit non-goals

- Hunting for a missing titled Balance Dataslate PDF (40K or KT).
- Committing GW PDFs to `main` (staging is temporary).
- Dumping Faction Pack / MFM / team rules verbatim into armies or KB (Codex wall + paraphrase).
- Early rewrite of Blood Ravens lists to October Codex preview stats.
- Full teaching for KT top-five teams outside priority set (unless you expand).

---

## Still open (your call)

1. Authorize full track, or subsets (e.g. S2b / S2c / S2d / S2e / S3 first)?
2. Confirm long-term copies under `C:\Personal\40K\rules\` and Kill Team tree (or accept `draft`)?
3. Expand S3 beyond priority + Hierotek?
4. Canonical WarCom URLs when egress/pastes allow (nice-to-have; not a package-shape blocker).

---

## Related

- Track SoT: [`../track_in.md`](../track_in.md)
- Gate: [`../GATE_user_lock.md`](../GATE_user_lock.md)
- KT package lock detail: [`staging_kt_august_updates.md`](staging_kt_august_updates.md)
