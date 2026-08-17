<!--
FILE: games/kill_team_2024/teams/canoptek_circle/cards/Card_Schema.md
VERSION: v0.1 (2026-08-17)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, slice S4)

DOCUMENT_TYPE: Card Format Sketch (design doc for S10)
GAME_SYSTEM: Kill Team — 2024 / 3e (KT24)
TEAM: Canoptek Circle
STATUS: Sketch only — S10 is gated on user photos of the physical models; do
  not fill this schema with real card content until photos arrive

SOURCES:
  - ../operatives/Operatives_Index.md (field source for schema draft)
  - docs/handoffs/kill_team_2024_scaffold/track_in.md (S10 gate)

PURPOSE:
  Sketch the field layout for a "Tarot-sleeve" teaching card — one physical,
  printable card per operative, meant to sit next to the model at the table.
  This is a schema, not content. Real cards wait for S10 (photos).

UPDATE_TRIGGER:
  Update when S10 unblocks (photos of the owned models arrive) and the first
  real card is drafted, or if the physical card size/sleeve choice changes.
-->

# Card Schema — Canoptek Circle (sketch, for S10)

**This is a template, not a deliverable.** S10 ("Photos → Tarot cards") is blocked on the user photographing the owned models. This page exists so S10 can start from a field list instead of a blank page.

The intent: one **Tarot-sized card** (70mm × 120mm) per operative, sleeved, that sits on the table next to that model — a physical, glanceable memory aid, not a full rules reference (the Quick Reference Play Guide already covers that role).

---

## Why Tarot-sleeve size

- Big enough to hold a photo of the actual painted model plus a handful of short fields — small enough to sit next to a 28mm–50mm base without crowding the table.
- Standard Tarot sleeves are cheap and widely available, so this is buildable without custom printing hardware.
- One card per **operative type** (5 cards for this team), not one per model — the Tomb Crawler card serves both copies, etc.

---

## Field layout (front)

| Zone | Field | Source | Notes |
|------|-------|--------|-------|
| Top | **Operative name** | `Operatives_Index.md` | e.g. "Geomancer" |
| Top-right | **Base size icon** | `Owned_Models_Inventory.md` | 28mm / 50mm badge |
| Photo area | **Photo of the owned, painted model** | S10 (pending) | The actual physical model, not stock art — this is a personal collection card |
| Body | **Plain-English role** (1–2 sentences) | `Operatives_Index.md` "Plain-English role" | Kept short — this is a reminder, not the guide |
| Body | **Signature habit** (1 sentence) | `Operatives_Index.md` "Signature habit" | The one thing to remember mid-game |
| Body | **Card-schema tags** | `Operatives_Index.md` "Card-schema tags" | Small icon row or tag chips |
| Footer | **Count in team** | `Owned_Models_Inventory.md` | "×1", "×2", "×3" |

---

## Field layout (back)

| Zone | Field | Source | Notes |
|------|-------|--------|-------|
| Top | **Support given to others** | `Operatives_Index.md` | What this operative does *for* the team, if anything |
| Body | **Matrix interaction note** | `Team_Rule_Guide.md` | e.g. "Gets Accurate + APL boost inside the Matrix" |
| Body | **Dual-legality note** | `Owned_Models_Inventory.md` | Base size + 40K cross-reference status |
| Footer | **Weapon-option pending flag** (if any) | `Owned_Models_Inventory.md` | Reminder to confirm the physical loadout |

---

## What this schema deliberately excludes

Consistent with the "no datasheet transcription" rule that governs this whole team package:

- No APL / Move / Save / Wounds numbers
- No weapon ATK / HIT / DMG values or weapon-rule keyword lists
- No verbatim ploy, equipment, or flavour text

If a future card needs a rules reminder beyond the habit-level notes above, it should point back to [`../Team_Rule_Guide.md`](../Team_Rule_Guide.md) or the physical team PDF — not restate the rule on the card.

---

## S10 build checklist (for when photos arrive)

1. Photograph each of the 5 operative types (Geomancer, Tomb Crawler, Accelerator, Reanimator, Warrior) — one clean shot per type is enough since multiple bodies share a card.
2. Crop/compose each photo to the front "Photo area" zone above.
3. Pull the front/back text fields directly from `Operatives_Index.md`, `Owned_Models_Inventory.md`, and `Team_Rule_Guide.md` — no new prose needed, this schema is a re-slicing of already-written pages.
4. Print at Tarot card size, sleeve, and cross off the S10 blocker in `docs/handoffs/kill_team_2024_scaffold/track_in.md`.

---

## Related pages

- [`../operatives/Operatives_Index.md`](../operatives/Operatives_Index.md) — the field content this schema slices
- [`../Team_Rule_Guide.md`](../Team_Rule_Guide.md) — Matrix interaction note source
- [`../Owned_Models_Inventory.md`](../Owned_Models_Inventory.md) — base size / dual-legality source
- [`../README.md`](../README.md) — package entry point

---

## Change Log

- v0.1 (2026-08-17): Initial schema sketch (slice S4) — front/back field layout, exclusion list, S10 build checklist. No real card content — blocked on user photos.

## Attribution

- Project: Wargame_Concierge · Maintainer: Russell Catt

## Rising Tide Notes

- This document follows Rising Tide documentation standards.
- **This is a sketch, not shipping content.** Do not treat any field above as filled-in until S10 runs.
