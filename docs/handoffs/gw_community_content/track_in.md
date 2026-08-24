<!--
FILE: docs/handoffs/gw_community_content/track_in.md
VERSION: v1.0 (2026-08-23)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer — S0)

DOCUMENT_TYPE: Track hand-off in
PROJECT_NAME: Wargame_Concierge
TRACK: gw_community_content
STATUS: In Progress
-->

# Track in — gw_community_content

- **Project:** Wargame_Concierge
- **Track:** `gw_community_content`
- **Status:** Execution complete 2026-08-23 — awaiting user-gated git (S4)
- **Handoffs root:** `docs/handoffs/gw_community_content/`
- **Playbook:** [`docs/operations/multiagent_coordinator_strategy.md`](../../operations/multiagent_coordinator_strategy.md)
- **Shipping surface:** `games/**` print HTML, player-facing markdown (not `units/research/`)
- **KB surface:** `KB/sources/gw_ip_guidelines.md` (L1)
- **Schema:** [`AGENTS.md`](../../../AGENTS.md) Sec 10

## Goals

1. Lock and apply **GW unofficial / non-endorsement** footers on print HTML and player-facing shipping.
2. Add **templates** + **Cursor rule** so future print exports stay compliant.
3. Record official IP guideline pointers in KB (paraphrase only).

## Official source (locked S0)

| Field | Value |
|-------|-------|
| **SoT URL** | https://www.warhammer.com/en-CA/legal — section **Intellectual Property Guidelines** |
| **Retrieval date** | 2026-08-23 |
| **WarCom supplement** | [Terms of Website Use](https://www.warhammer-community.com/en-gb/terms-of-use/) — Downloadable Material Licence (personal store only; no redistribution of GW PDFs) |
| **Not a licence** | Guidelines do not constitute formal approval or authorization |

## Locked footer templates (A–D)

### A — Print/PDF page footer (`.gw-ip-footer`)

**40K variant:**

> **UNOFFICIAL.** This document is completely unofficial and in no way endorsed by Games Workshop Limited. Personal / no-charge use only — never for sale. Warhammer, Warhammer 40,000 and associated marks are trademarks of Games Workshop Limited. Used without permission. No challenge to their status intended. Warhammer 40,000 is Copyright Games Workshop Limited. Teaching notes by Russell Catt (Wargame Concierge). Games Workshop retains IP in the settings and characters. No official logos.

**KT variant:** same opening; product line reads *Kill Team is Copyright Games Workshop Limited 2024*.

**Quote-only export addendum (if owner gates):** *Verbatim lines are from owned local PDFs for personal table use; they are not a substitute for official publications and must not be redistributed.*

### B — First-page banner (`.gw-ip-banner`, required on page 1)

> **UNOFFICIAL** — fan teaching material, not a Games Workshop product, not endorsed by Games Workshop Limited.

### C — Markdown shipping (`## Games Workshop notice` before Change Log)

Same sentences as footer A (system-appropriate 40K vs KT line).

### D — Datacard micro (`.ft` / 5pt)

> UNOFFICIAL · not endorsed by Games Workshop Limited · personal use only · © Games Workshop Limited

## Quote-PDF policy (locked)

| Surface | Policy |
|---------|--------|
| In-repo quote markdown (`Core_Rules_Quotes.md`, `Target_Eligibility.md`) | **Keep** in private repo per AGENTS Sec 10; not event share packs |
| Print HTML at the table | **Teaching paraphrase** + footer A/B; no quote appendix PDFs unless owner explicitly gates |
| Datacard HTML | Owner-only print; footer D + UNOFFICIAL; stat profiles remain high-risk if shared publicly |
| WarCom/GW `eng_*` PDFs | Never redistribute; pointers only |

## Constraints

- Never write `raw/`. Never create `wiki/`. UTF-8 no BOM. No GW logos on shipping.
- Do not paste GW IP Guidelines verbatim into git — paraphrase + URL in KB.
- Subagents do not `git commit` / `git push`.
- **Out of scope:** bulk rewrite of `games/**/units/research/**` (one notice on army README sufficient).

## Slice rollup

| Slice | Status | Deliverable |
|-------|--------|-------------|
| **S0** | Done | This `track_in.md` |
| **S3** | Done | Tier B markdown + cards |
| **L1** | Done | KB source |
| **QA** | Done | S1_S2_qa.md, S3_L1_qa.md — PASS |
| **S4** | Pending | User-gated git (Coordinator) |

## Tier B markdown scope (S3)

Include: system READMEs, starters, army lists, QR/play guides, setup, rules READMEs, quote-file Attribution blocks.

Exclude: `games/**/units/research/**`, frozen handoff slices.
