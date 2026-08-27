# Research note — 40K Universal Rules Updates v1.1 (core)

- **Track:** `dataslate_0826`
- **Captured:** 2026-08-27
- **Upload (agent read only — do not commit):**  
  `/home/ubuntu/.cursor/projects/workspace/uploads/eng_wh40k_core_key_universal_rules_updates-lu3grocned-rphh78bl6k_15b5.pdf`
- **Staging SoT (on branch, temporary):**  
  `raw/_dataslate_0826_staging/eng_wh40k_core&key_universal_rules_updates-lu3grocned-rphh78bl6k.pdf`  
  (`cmp` identical to chat upload; note `&` in filename)
- **Expected local SoT (owner save after CLEANUP):**  
  `C:\Personal\40K\rules\` — prefer WarCom/`eng_*` name without `&` if renaming on disk
- **Product:** **UNIVERSAL RULES UPDATES — VERSION 1.1**
- **Legal matched play from:** **26 August 2026**
- **PDF metadata:** Created/Mod 24 Jul 2026 (InDesign); 1 page; text layer OK
- **Hierarchy:** Supersedes July **v1.0** (`eng_22-07_warhammer_40,000_universal_rules_updates.pdf`, legal 22 Jul 2026) on the same topics. Core PDF remains baseline; dated stamp wins. Omission is not a patch.
- **Confidence:** `draft` until owner confirms file saved under `C:\Personal\40K\rules\`
- **Copyright:** Never commit the PDF. Verbatim quotes only under `games/warhammer_40k_11e/rules/` (Sec 10) with filename + page. `KB/` / handoffs stay paraphrase.

## Teaching paraphrase (v1.1)

Broader-than-Faction-Pack fixes for core / Codex-wide mechanics:

1. **Unnamed 0CP stratagem effects** — If a rule lets you target a friendly unit with a stratagem for 0CP but does **not** name the stratagem, that use instead costs **1CP less** (not free-any-stratagem).
2. **Multi-use / already-used stratagems** — “Even if you already used that stratagem this phase/turn…” (and similar once-per-turn/round/battle relaxations) only work when the rule **names** the stratagem.
3. **Anti-targeting stratagems at 12"** — Effects that only allow ranged targeting within **12"** (or block ranged unless within 12") become **18"**.
4. **Respawn / identical-unit stratagems** — Adding “a new unit identical to your destroyed unit” gains **once per battle**.
5. **NEW in v1.1 — Disembark move types**
   - Rule lets unit charge after disembarking from a TRANSPORT that made a **Normal move** this turn → that disembarkation is an **assault disembark move** (`18.06`), not a normal disembark move.
   - Rule lets unit disembark from a TRANSPORT that **Advanced** this turn → that disembarkation is a **shock disembark move** (`18.07`).

Items 1–4 match the July v1.0 teaching already in [`Core_Rules_Quotes.md`](../../../../games/warhammer_40k_11e/rules/Core_Rules_Quotes.md). Item **5 is the net-new shipping work**.

## Delta vs repo (July v1.0)

| Topic | July v1.0 in repo | v1.1 |
|-------|-------------------|------|
| Legal date | 22 Jul 2026 | **26 Aug 2026** |
| Version | 1.0 | **1.1** |
| Stratagem CP / multi-use / 12→18 / add-unit | Present | Present (same intent) |
| Disembark move typing (`18.06` / `18.07`) | **Absent** | **Added** |

## Shipping / KB impact (S2e)

| Path | Action |
|------|--------|
| `raw/pointers/rules_core.md` | Add v1.1 row; mark July v1.0 superseded |
| `games/.../rules/Core_Rules_Quotes.md` | Replace July section with **Aug v1.1**; quote disembark bullets + cite filename/page; keep stratagem flags |
| `rules/Overview.md`, `Key_Concepts.md`, `Keyword_Glossary.md` | Currency + disembark teaching if transport play is taught |
| QRs / print HTML | Stamp universal updates **v1.1 / 26 Aug 2026**; add one-line disembark note if space |
| `KB/sources/` | Source page for universal updates v1.1 (Librarian L0/L1) |
| Footer | `Rules currency: Universal Rules Updates v1.1 (legal 26 Aug 2026)` |

## Open questions

1. Confirm saved local filename under `C:\Personal\40K\rules\`.
2. Authorize **S2e** (core quote + teaching pass) with MFM slices or alone?
