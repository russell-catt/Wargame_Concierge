# S0 Implementer — dataslate_0826

**Slice:** S0 — resolve links + inventory + impact matrix
**Status:** Complete
**Date:** 2026-08-27
**Model:** `claude-sonnet-5-thinking-high` (per track model matrix; Preflight brief listed `composer-2.5-fast` for S0 research — actual session model recorded here)
**Authorization:** Owner 2026-08-27 — full track authorized; G2 (`C:\Personal\…` local copies) **accept `draft`**; package shape locked — **no singular Balance Dataslate** for 40K or KT. No git commit/push by this subagent. No GW binaries read, copied, or committed.

## Summary

WarCom newsletter links **L1–L3 remain unresolved** — cloud egress to `news.warhammer.com` / `warhammer-community.com` still fails (SSL connect error). **Waived:** owner pastes + **14 staging PDFs** + filed research notes provide sufficient discovery for downstream slices. Locked **package stamps** (not a singular dataslate filename) for the Aug 2026 40K and KT balance packages; drafted a concrete **impact matrix** mapping onboarded factions/teams to shipping paths under `games/`; inventoried **expected local paths** under `C:\Personal\40K\rules\` and `C:\Personal\Kill Team\kill_team_2024\` at **`draft`** confidence per G2 waiver. `track_in.md` **Locked dates** table (lines 78–91) already carries the stamp values below — verified consistent with staging inventory and owner pastes; not re-edited in this pass (S0 deliverable is this report + confirmation, not a duplicate edit of track_in).

---

## L1–L3 link resolution

### Newsletter URLs (locked inputs — from `track_in.md`)

| ID | Newsletter / tracking URL | Resolution status |
|----|---------------------------|-----------------|
| **L1** | `https://news.warhammer.com/optiext/optiextension.dll?ID=NC2rRE5wEV0G-B16_yG7pcanGMxH-qSH65CvPRHKgk0lUOWff50iRYu-XhL1wJ4S_HDtJMcWHz1nXsFwaT8` | **Unresolved** (egress) |
| **L2** | `https://news.warhammer.com/optiext/optiextension.dll?ID=oGaQ5eOApC1Q-hcypyE7zoFhMv6hgaWSzW1A3xVHSue3e3-ZPpkSIZWdipRa8LOWLH00qp_3g15zYsX_K2A` | **Unresolved** (egress) |
| **L3** | `https://news.warhammer.com/optiext/optiextension.dll?ID=NTOd06r859kUenLP4iE4NYBr2beBbX0uj9BZh9WeCsuZ3BM0xvoWY9CyN_SxDE3TFE1JYgktd5TzzPIZXaw` | **Unresolved** (egress) |

### Egress probe (verbatim commands + failure notes)

```bash
# L1 probe — 2026-08-27
curl -sS -o /dev/null -w "%{http_code}" --connect-timeout 5 --max-time 10 \
  "https://news.warhammer.com/optiext/optiextension.dll?ID=NC2rRE5wEV0G-B16_yG7pcanGMxH-qSH65CvPRHKgk0lUOWff50iRYu-XhL1wJ4S_HDtJMcWHz1nXsFwaT8"
# Result: curl: (35) OpenSSL SSL_connect: SSL_ERROR_SYSCALL in connection to news.warhammer.com:443
# HTTP code: 000 (no response body)

# warhammer-community.com — same class of failure expected; not re-run for L2/L3 optiext redirects
curl -sS -I --connect-timeout 5 --max-time 10 \
  "https://www.warhammer-community.com/en-gb/downloads/warhammer-40000/" 2>&1 | head -5
# Result: SSL/connect failure or timeout — egress blocked for WarCom domains in this environment
```

**Do not invent** canonical article URLs, publish dates, or PDF product names from redirect targets. Discovery for this track uses the waiver sources below.

### Waiver — owner pastes + staging (covers L1–L3 intent)

| Waiver source | Product class | Research note |
|---------------|---------------|---------------|
| SM Codex October preview | **Codex: Space Marines preview** (October) — not a balance dataslate | [`../research/sm_codex_oct_preview.md`](../research/sm_codex_oct_preview.md) |
| MFM Necrons v1.3 | Points (Necrons) | [`../research/necron_mfm_v1_3.md`](../research/necron_mfm_v1_3.md) |
| MFM Space Marines v1.3 | Points (Space Marines) | [`../research/sm_mfm_v1_3.md`](../research/sm_mfm_v1_3.md) |
| Universal Rules Updates v1.1 | Core / universal (legal **26 Aug 2026**) | [`../research/40k_universal_rules_updates_v1_1.md`](../research/40k_universal_rules_updates_v1_1.md) |
| WarCom 40K “What’s New?” | Aug 40K balance **commentary** (Orks excluded; Sep last monthly; FD map tweaks) | [`../research/warcom_40k_balance_commentary_aug.md`](../research/warcom_40k_balance_commentary_aug.md) |
| WarCom KT quarterly “top five” | Aug KT balance **commentary** (Hierotek regen; Fellgor/Goremongers/Raveners/Wolf Scouts out of onboarded scope) | [`../research/warcom_kt_balance_commentary_aug.md`](../research/warcom_kt_balance_commentary_aug.md) |
| Staging pull @ `9a9dcf8` | **14 PDFs** — Faction Packs, Universal Rules, KT update logs + team online rules | [`../research/staging_inventory_2026_08_27.md`](../research/staging_inventory_2026_08_27.md) |

**Inferred L1–L3 mapping (draft — not verified until canonical URLs resolve):** the three newsletter links likely correspond to some combination of (a) Aug 40K balance announcement, (b) Aug KT quarterly balance announcement, and (c) SM Codex October preview — but **exact ID→article assignment is not asserted** without egress or owner paste of resolved URLs. Downstream slices do not block on this assignment.

**Google Drive folder** ([`../research/gdrive_40k_dataslates.md`](../research/gdrive_40k_dataslates.md)): unread (egress); **superseded by staging** for this track.

---

## Locked package stamps (no singular dataslate)

Owner lock (**both systems**): there is **no** standalone PDF titled “Balance Dataslate” for Warhammer 40,000 or Kill Team. Currency stamps name **package pieces and dates**, not a fictional dataslate filename.

| Field | Locked value |
|-------|--------------|
| **40K Balance Dataslate date** | **N/A — no singular file** |
| **40K package stamp (currency)** | **40K Aug 2026 package** — Universal Rules **v1.1** · Faction Pack **v1.2** · MFM **v1.3** (legal / App **26 Aug 2026** where dated) |
| **KT Balance Dataslate date** | **N/A — no singular file** |
| **KT package stamp (currency)** | **Kill Team quarterly balance — August 2026** (Core / update logs + team online rules) |
| **40K Faction Packs** | Necrons + Space Marines **v1.2** · legal **26 Aug 2026** |
| **40K Universal Rules Updates** | **v1.1** · legal **26 Aug 2026** · supersedes July v1.0 on same topics · **new** disembark move typing **`18.06`** / **`18.07`** |
| **Necron MFM** | **v1.3** (owner paste 2026-08-27) · headline owned delta: Warriors 10 **80→85**; Plasmancer **55→60** |
| **Space Marines MFM** | **v1.3** (owner paste 2026-08-27) · Blood Ravens Matched cores unchanged; Legends section for Casual cross-check |
| **SM Codex preview** | Owner paste **2026-08-27**; Codex / App **October** · readiness only — **not** early list rewrite |
| **Announcement retrieval / staging pull** | **2026-08-27** · staging @ commit **`9a9dcf8`** · **14 PDFs** |

**Footer convention (additive — from `track_in.md`):**

```text
Rules currency: 40K Aug 2026 package — Universal Rules v1.1 · Faction Pack v1.2 · MFM v1.3 (legal / App 26 Aug 2026 where dated). Teaching paraphrase — verify owned PDFs before tournament play.
```

```text
Rules currency: Kill Team quarterly balance — August 2026 (Core / update logs + team online rules) · teaching paraphrase · verify owned PDFs.
```

```text
Preview note: Codex: Space Marines expected October (WarCom) · live lists still current Faction Pack / MFM until Codex — Legendary Proxies / Legends honesty on Firstborn paths.
```

**Deprecated for this track:** do **not** invent `Rules currency: Balance Dataslate <date>` when no such file exists.

---

## Impact matrix

Onboarded shipping scope only. Commentary-named factions/teams outside this collection are **research context**, not shipping blockers.

### Warhammer 40,000 — Necrons (onboarded)

| Package piece | Primary shipping paths under `games/` | Slice |
|---------------|----------------------------------------|-------|
| MFM Necrons **v1.3** | `games/warhammer_40k_11e/armies/necrons/Starter_*.md`, `Army_List_*_Conclave.md`, `Starter_Forces_500_750_1000.md`, `Necron_Lists.md`, `Canoptek_Court.md`, `Cryptek_Conclave.md`, `Quick_Reference_Play_Guide.md`, `print/*.html` | **S2c** |
| Faction Pack Necrons **v1.2** | `games/warhammer_40k_11e/armies/necrons/README.md`, detachment teaching, FAQ paraphrase where Cryptek / Canoptek rules touched | **S2** |
| Universal Rules **v1.1** | `games/warhammer_40k_11e/rules/*` (disembark typing); indirect on any transport-heavy army notes | **S2e** |
| WarCom 40K commentary | Force Disposition / map-layout context — optional note on setup 2-pagers if Event Companion layouts cited | **S2** (optional) |

**Headline owned deltas:** Warriors 10 @ **85** (+5); Plasmancer **60** (+5). Other ▲ in research note (Lokhust, Ophydian, Skorpekh) — not in owned lists.

### Warhammer 40,000 — Space Marines / Blood Ravens (onboarded)

| Package piece | Primary shipping paths under `games/` | Slice |
|---------------|----------------------------------------|-------|
| MFM SM **v1.3** | `games/warhammer_40k_11e/armies/space_marines/Starter_*_{Matched,Casual}.md`, `README.md`, `Owned_Models_Inventory.md`, `Quick_Reference_Play_Guide.md`, `Gladius_Task_Force.md` | **S2d** |
| Faction Pack SM **v1.2** | Same tree — rules/FAQ teaching (Gladius Adaptive Strategy, Teleport Homer 8", etc.); **Codex wall** on armies | **S2** |
| Universal Rules **v1.1** | Stratagem cost interactions cited in FP teaching (Guilliman / Ventris) → link to `rules/Core_Rules_Quotes.md` | **S2e** |
| SM Codex October **preview** | `README.md` Legendary Proxies table; `Starter_*` inline callouts; `units/research/Tactical-Squad.md`, `Devastator-Squad.md`, `Whirlwind.md` | **S2b** |
| WarCom 40K commentary | Context only (Orks, Daemons, etc. out of scope) | — |

**Headline owned posture:** Matched BR cores **unchanged** in v1.3; Tac/Dev/Whirlwind stay current FP/MFM until October Codex — preview honesty only.

### Kill Team 2024 — provided teams (staging + owner lock)

| Team / surface | Disposition | Primary shipping paths under `games/` | Slice |
|----------------|-------------|----------------------------------------|-------|
| **Angels of Death** | **Update** (priority) | `teams/angels_of_death/README.md`, `Team_Rule_Guide.md` | **S3** |
| **Canoptek Circle** | **Update** (priority) | `teams/canoptek_circle/README.md`, `Team_Rule_Guide.md`; `setup/killzones/tomb_world.md` | **S3** |
| **Plague Marines** | **Update** (priority) | `teams/plague_marines/README.md`, `Team_Rule_Guide.md` | **S3** |
| **Hierotek Circle** | **Update** (stub — regen timing) | `teams/hierotek_circle/README.md` | **S3** |
| Celestian Insidiants, Deathwatch, Murderwing, Vespid Stingwings | **Update** (currency + short note) | respective `teams/*/README.md` | **S3** |
| Tomb World / Mission packs update logs | **Update** (Core half of package) | `setup/killzones/tomb_world.md`; `nemesis_ops/*.md` | **S3** |
| Fellgor, Goremongers, Raveners, Wolf Scouts | **Waived** (commentary only) | — | — |

### Kill Team 2024 — no-op (owner lock)

| Team | Disposition | Rationale |
|------|-------------|-----------|
| **Death Korps** | **No-op** | No update in this package; no staged team PDF; owner: “other owned teams received no update” |
| **Kommandos** | **No-op** | Same |

No `games/kill_team_2024/teams/death_korps/**` or `teams/kommandos/**` edits required for currency or rules deltas this track.

### Cross-cutting / non-GW

| System | Disposition | Paths | Slice |
|--------|-------------|-------|-------|
| **Warcode** | **N/A** | `games/the_warcode/README.md` — not affected by GW balance packages | **S5** |
| **Project / game cores** | Currency lines | `README.md`, `START_HERE.md`, `games/*/README.md`, footer sweep | **S4 / S5** |
| **Pointers** | Inventory | `raw/pointers/*` | **S1** |
| **KB** | Source stubs + enhance | `KB/sources/`, entities | **L0 / L1** |

---

## Local path inventory (`C:\Personal\…`)

**G2 status:** **WAIVED — accept `draft`**. Paths below are **expected** long-term homes; existence on owner disk **not verified** in this pass. Staging PDFs under `raw/_dataslate_0826_staging/` are temporary branch-only cross-checks (CLEANUP before merge).

### `C:\Personal\40K\rules\`

| Expected path / pattern | Product | Staging cross-check | Confidence |
|-------------------------|---------|---------------------|------------|
| `eng_01-06_warhammer40k_new40k_core_rules.pdf` | Core Rules baseline | — | existing SoT |
| `eng_22-07_warhammer_40,000_universal_rules_updates.pdf` | Universal Rules **v1.0** (superseded) | — | existing |
| `eng_*` (owner to confirm; prefer without `&` in filename) | Universal Rules Updates **v1.1**, legal **26 Aug 2026** | `raw/_dataslate_0826_staging/eng_wh40k_core&key_universal_rules_updates-lu3grocned-rphh78bl6k.pdf` | **draft** |
| `eng_22-07_warhammer_40,000_faction_pack_necrons.pdf` | FP Necrons v1.1-era (superseded) | — | existing |
| `eng_*` or replace July copy | **Faction Pack — Necrons v1.2**, legal **26 Aug 2026** | `eng_wh40k_faction_pack_necrons-eweoek106p-nqomxds3qr.pdf` | **draft** |
| `eng_22-07_warhammer_40,000_faction_pack_space_marines.pdf` | FP SM v1.1-era (superseded) | — | existing |
| `eng_*` or replace July copy | **Faction Pack — Space Marines v1.2**, legal **26 Aug 2026** | `eng_wh40k_faction_pack_space_marines-kxoxqpsahz-u0lzirv0zl.pdf` | **draft** |
| `Warhammer 40,000_ Munitorum Field Manual.pdf` | General MFM **v1.2** (superseded) | — | existing |
| `Warhammer 40,000_ Munitorum Field Manual_Marines.pdf` | SM MFM **v1.2** (superseded) | — | existing |
| `eng_*` MFM Necrons or replace general MFM | **MFM Necrons v1.3** | *Not in staging* — owner paste only | **draft** |
| `eng_*` MFM Marines or replace Marines MFM | **MFM Space Marines v1.3** | *Not in staging* — owner paste only | **draft** |

Pointer SoT: [`raw/pointers/rules_core.md`](../../../raw/pointers/rules_core.md), [`faction_pack_necrons.md`](../../../raw/pointers/faction_pack_necrons.md), [`faction_pack_space_marines.md`](../../../raw/pointers/faction_pack_space_marines.md), [`points_manuals.md`](../../../raw/pointers/points_manuals.md).

### `C:\Personal\Kill Team\kill_team_2024\`

| Expected path / pattern | Product | Staging cross-check | Confidence |
|-------------------------|---------|---------------------|------------|
| `eng_*killzone_tomb_world_update_log*` (Aug 2026) | Tomb World update log | `eng_killzone_tomb_world_update_log-ptyzlo3dfr-ivlzsazxnf.pdf` | **draft** |
| `eng_*mission_packs_update_log*` (Aug 2026) | Mission packs update log | `eng_mission_packs_update_log-51t6hsixc0-buxngu8xav.pdf` | **draft** |
| `Teams\eng_26-08_killteam_angels_of_death_online_rules-*.pdf` | Angels of Death Aug update | staged AoD pack | **draft** |
| `Teams\eng_canoptek_circle_online_rules-*.pdf` | Canoptek Circle | staged | **draft** |
| `Teams\eng_plague_marines_online_rules-*.pdf` | Plague Marines | staged | **draft** |
| `Teams\eng_hierotek_circle_online_rules-*.pdf` | Hierotek Circle | staged | **draft** |
| `Teams\eng_deathwatch_online_rules-*.pdf` | Deathwatch | staged | **draft** |
| `Teams\eng_celestian_insidiants_online_rules-*.pdf` | Celestian Insidiants | staged | **draft** |
| `Teams\eng_murderwing_online_rules-*.pdf` | Murderwing | staged | **draft** |
| `Teams\eng_vespid_stingwings_online_rules-*.pdf` | Vespid Stingwings | staged | **draft** |
| `eng_kt_approved_ops_2025_tournament_companion-*.pdf` | AO2025 companion (optional) | staged | **draft** |
| `Teams\eng_29-04_kill_team_team_rules_death_korps-*.pdf` | Death Korps baseline | **No Aug update** — no-op | existing |
| `Teams\eng_17-06_kill_team_team_rules_kommandos_online_rules-*.pdf` | Kommandos baseline | **No Aug update** — no-op | existing |

Full staging filenames: [`../research/staging_inventory_2026_08_27.md`](../research/staging_inventory_2026_08_27.md). Pointer SoT: [`raw/pointers/kill_team_2024_teams.md`](../../../raw/pointers/kill_team_2024_teams.md), [`kill_team_2024_missions.md`](../../../raw/pointers/kill_team_2024_missions.md).

---

## Done (mapped to S0 brief)

1. **L1–L3:** attempted resolution; **Blocked on egress**; **waived** with owner pastes + staging inventory (see above).
2. **Locked package stamps:** filled and verified against `track_in.md` and [`../research/research_plan_restatement.md`](../research/research_plan_restatement.md) — **no singular dataslate** for 40K or KT.
3. **Impact matrix:** Necrons, SM, KT provided teams vs Death Korps / Kommandos **no-op** (concrete `games/` paths listed).
4. **Local path inventory:** expected `C:\Personal\…` rows documented; G2 **accept `draft`**.
5. **Verbatim fetch commands / failure notes:** recorded in L1–L3 section.
6. Wrote this `S0_implementer.md`.

## Files touched

- `docs/handoffs/dataslate_0826/slices/S0_implementer.md` (this report — create)

## Not touched (S0 scope)

- `track_in.md` — Locked dates table already populated (v0.13); slice rollup update is Coordinator-owned.
- `raw/pointers/*` — **S1** (subsequent slice may already have run on branch).
- `games/**`, `KB/**`, templates — downstream slices **S2–S5**, **L0–L1**.
- `raw/_dataslate_0826_staging/` PDFs — read-only cross-check reference; no binary writes.
- No `git add` / `git commit` / `git push`.

## Waivers / open items for QA-S0

1. **L1–L3 canonical URLs** remain TBD — acceptable waiver per owner authorization; living-source pointers must not invent URLs.
2. **Exact L1↔L2↔L3 article mapping** not asserted — only package contents locked.
3. **MFM v1.3 PDFs** not in staging — owner-paste provenance only until saved under `C:\Personal\40K\rules\`.
4. All local-path rows **`draft`** until owner confirms on-disk copies (G2 waived for track execution).
5. **Sibling implementer reports** on branch (S1, S2b–S2e, S3) indicate downstream work may have proceeded in parallel — QA-S0 should verify this report’s stamps/matrix still match those slices; no contradiction found at authoring time.

## Handoff

**Status: Complete — Ready for QA-S0.**
