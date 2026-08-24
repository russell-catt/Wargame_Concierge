<!--
FILE: games/the_warcode/First_Game_Walkthrough.md
VERSION: v0.1 (2026-08-23)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, warcode_tactical_doctrine)

DOCUMENT_TYPE: Teaching Guide / Session Script
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: The Warcode
REFERENCE_STATUS: Active — draft (2026-08-23)

SOURCES:
  - raw/the_warcode/The Warcode Rulebook V.0.8.7-F.pdf (read via extract 2026-08-23)
  - games/the_warcode/setup/Board_Setup.md
  - games/the_warcode/rules/Turn_Structure.md
  - games/the_warcode/guides/Proxy_Play_at_Home.md

PURPOSE:
  Step-by-step first session: Protagen vs Ulfari proxy on Core of the Machine.

UPDATE_TRIGGER:
  Scenario or setup order changes in newer beta.
-->

# First game walkthrough — Protagen vs Ulfari (proxy)

**`confidence: draft`** — one-table script for a first session. **Unofficial; not endorsed by RedMakers.**

**Setup:** Father/experienced player → **Protagen Marines**. Junior/first timer → **Ulfari**. **Eight proxy models each.** Board **33" × 24"**. Scenario: **Core of the Machine**.

Keep [`Quick_Reference_Play_Guide.md`](Quick_Reference_Play_Guide.md) between you.

---

## Before you sit down (15 min)

1. Read [`rules/Overview.md`](rules/Overview.md) once — shape of a game.
2. Print or open:
   - [`factions/protagen_marines/Squad_Datasheet.md`](factions/protagen_marines/Squad_Datasheet.md)
   - [`factions/ulfari/Squad_Datasheet.md`](factions/ulfari/Squad_Datasheet.md)
3. Gather: D6, inch ruler, activation tokens, ammo counters, VP chits.
4. Lay terrain: partial cover, **walls (full cover)**, **doors** — see [`setup/Terrain_Basics.md`](setup/Terrain_Basics.md).
5. Mark deployment zones **A** and **B** from scenario diagram (p.26–27).

Proxy tips: [`guides/Proxy_Play_at_Home.md`](guides/Proxy_Play_at_Home.md).

---

## Scenario in one minute

> Paraphrase from The Warcode Rulebook V.0.8.7-F.pdf — p.26 — SCENARIO «CORE OF THE MACHINE»

Abandoned **space drifter**. Both squads reach the **machine core**; damaged security cannot tell friend from foe. **Countdown** running — reprogram the core to mark your team friendly and the enemy hostile (turrets). **Win** by wiping the enemy **or** having **more VP** to sway the core. **Tie VP** → both teams flagged hostile and destroyed.

Each round: draw a **Core of the Machine** activation card (negative effects in rooms).

---

## Setup sequence (follow in order)

| Step | Action | Who |
|------|--------|-----|
| 1 | Read scenario victory conditions aloud | Both |
| 2 | Roll D6 — VP token placement table | Both |
| 3 | Roll D6 — deploy first + round 1 initiative | Both |
| 4 | Alternate placing **one unit** until 16 models on board | Loser deploys first |
| 5 | Spend **4 equipment points** each (grenades / medkits) | Both — **Blast** and **Phantom** skip (locked grenades) |
| 6 | Mark Leaders: **Rickman**, **Soul Eater** | Both |
| 7 | Note **Reaper** has no gun — no Overwatch | Ulfari player |

Full checklist: [`setup/Board_Setup.md`](setup/Board_Setup.md).

---

## Round structure (repeat until final round)

### Initiative Phase

- Roll D6. Higher goes **first** in Tactical Phase. Ties re-roll.

### Tactical Phase — alternating activation

Each turn: pick **one** unit that has not activated this round.

**That unit has 2 AP.** Common actions:

| Action | AP | Remember |
|--------|-----|----------|
| Move | 1 | Through partial cover: −1" from M |
| Shoot | 1 + reload costs | Roll ≥ target **Agility** to hit |
| Reload | 1 | Refill ammo |
| Overwatch | 1 | Set token; triggers on enemy move in LoS |
| Melee | 1 | In melee range |
| Engage | 2 | Charge into melee |
| Pass | — | Does **not** trigger Overwatch |

Flip activation token when done — unit cannot act again this round.

**Teaching moment (round 1):** Ulfari player moves **Phantom** (M 7) behind cover. Protagen responds with **Overwatch** on a lane — explain before the move commits.

### End of round

1. Resolve end-of-round unit abilities.
2. Resolve scenario / Core card effects.
3. **Score VP** — unit within **1"** of token, no enemy in radius; contested if both present.
4. If trailing by **1+ VP**, draw a **Contract** (homemade card naming one enemy unit — e.g. **Shade**).
5. Start next round unless **final round** → determine winner.

Detail: [`rules/Turn_Structure.md`](rules/Turn_Structure.md).

---

## Faction-specific nudges (first game only)

### Protagen (parent)

- Advance together — armour rewards holding VP rooms.
- **Smasher** near a choke — enemies within 1" are **Melee Locked** even without base contact.
- Protect **Rickman** — losing Leader costs **2 re-roll points per round**.

### Ulfari (junior)

- Simple plan: move fast (**Phantom**, **Reaper**), shoot with **Ravener** / **Shade**, stab with **Razor Blades**.
- **Shade** first — Sniper reduces target Agility by 1 when shooting.
- **Reaper** stabs only — run around walls, ignore Overwatch (no gun).

---

## Suggested teaching beats by round

| Round | Focus |
|-------|-------|
| **1** | Deployment, one shoot + one move; explain activation flip |
| **2** | Overwatch trap; partial cover −1" move |
| **3** | Melee lock + disengage roll; grenade if equipped |
| **4** | VP totality + tie danger; Contract if behind |

---

## Combat micro-example (optional pause)

Walk through the rulebook **Shooting Example** (p.20) or **Melee Example** (p.21) on paper before rolling live dice — reduces mid-game rules diving.

---

## End of session

- Count VP. Apply scenario tie rule if equal.
- Ask: Which proxy models mapped cleanly? Update personal notes.
- Next session: same rosters or swap factions.

---

## Related pages

- [`Quick_Reference_Play_Guide.md`](Quick_Reference_Play_Guide.md)
- [`guides/Proxy_Play_at_Home.md`](guides/Proxy_Play_at_Home.md)
- [`rules/Key_Concepts.md`](rules/Key_Concepts.md)

---

## Change Log

- v0.1 (2026-08-23): Protagen vs Ulfari first-session script (warcode_tactical_doctrine).

## Attribution

- Project: Wargame_Concierge
- Maintainer: Russell Catt
- The Warcode is property of RedMakers.

## Rising Tide Notes

- Verify round count on scenario card — extract references final round without global default.
