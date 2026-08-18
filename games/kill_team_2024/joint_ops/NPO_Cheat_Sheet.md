<!--
FILE: games/kill_team_2024/joint_ops/NPO_Cheat_Sheet.md
VERSION: v0.5.0 (2026-08-18)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer + Librarian-assist, slice S9)

DOCUMENT_TYPE: Play Aid / Laminate (print-friendly, target ~1-2 pages)
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: Kill Team — 2024 / 3e (KT24)
REFERENCE_STATUS: Active — sources read 2026-08-17 (Core Book Joint Ops mission pack via Wahapedia mirror;
  Terror on Devlan mission pack PDF for the Behaviour Changes / activation-deck variant)

SOURCES:
  - https://wahapedia.ru/kill-team3/the-rules/the-missions/ (retrieved 2026-08-17)
  - C:\Personal\Kill Team\kill_team_2024\eng_terror_on_devlan_mission_pack-xxesbxnr8b-lyb0mbmtbe.pdf (local, read)

PURPOSE:
  Table-side reminder for running NPOs mid-game: behaviour loops, the Threat
  Principle decision rules, the action loop, and cover/engagement habits.
  Distinct from — and does not replace — any Community Content NPO cheat sheet
  (out of scope for this project).

PRINT_NOTE:
  Designed to print in roughly one to two pages. Bullets and tables, not prose.
  No full datasheets, no shopping content.

CHANGE_LOG:
  - v1.0 (2026-08-17): Initial cheat sheet (slice S9).

ATTRIBUTION:
  - Project: Wargame_Concierge | Maintainer: Russell Catt
  - Warhammer 40,000: Kill Team is a trademark of Games Workshop Limited. Personal
    teaching paraphrase; no publisher text or statlines reproduced.

RISING_TIDE_NOTES:
  - Follows Rising Tide documentation standards.

UPDATE_TRIGGER:
  Update if a mission pack changes the generic behaviour loop or the Threat Principle.
-->

# NPO CHEAT SHEET — running the enemy in Joint Ops

*Not a Community Content sheet — official Core Book / owned mission-pack rules, paraphrased. Verify vs current sources | 2026-08-17*

## ACTIVATION ORDER — "who moves first?"

When more than one NPO is ready to activate, use the **Threat Principle** (below) unless the mission pack says otherwise. Default priority, in order:

1. Can it **Fight or Shoot** this activation, and is it the **most threatening** one that can (better weapon, more likely to take out an operative)?
2. Is it **not in cover** from a player operative?
3. Is it the **closest** to a player operative?

**Initiative roll-off:** roll one die for the NPOs, one for the player(s). **NPOs always take initiative if they win.**

**Strategy/Gambit step:** NPOs don't spend CP and have no equipment choices of their own — they simply pass, unless a mission names a specific Strategic Gambit (e.g. a scripted reinforcement wave) for them.

**Card-deck variant (some campaign packs, e.g. Terror on Devlan):** instead of the Threat Principle picking the next NPO, draw the next numbered card from that pack's NPO activation deck. Early draws are unpredictable; late draws (deck thinning) get more readable.

---

## THE BEHAVIOUR LOOP — "what does it do?"

Every NPO datacard names a **behaviour**. On activation, **try its listed actions in order — do the first one it is able to do. If it can do none of them, it is expended (or passes, if counteracting).**

### Brawler — closes to fight

1. **Fight**, if already in range.
2. **Charge** the closest enemy operative, shortest route.
3. **Reposition** toward the closest enemy operative — to cover, if possible.
4. **Dash** toward the closest enemy operative — to cover, if possible.

### Marksman — holds a firing line

1. **Fall Back** to cover — ideally somewhere with a clear shot, or failing that, somewhere with a visible objective marker.
2. **Shoot.**
3. **Reposition** to cover (clear-shot spot preferred, objective-visible spot second).
4. **Dash** to cover (same preference order).

**Order assignment:** if the NPO *can* perform its behaviour's Fight/Shoot action this activation, give it an **Engage** order. If it cannot, give it **Conceal** instead.

**Named exceptions exist.** Some big/boss NPOs (e.g. the Red Terror in Terror on Devlan) carry a **"Behaviour Changes"** note on their own datacard that overrides part of the generic loop above — always read the specific datacard first; treat this sheet as the fallback default, not an override.

---

## THE THREAT PRINCIPLE — "which option is worse for the players?"

When a rule gives the NPO side a choice (which target, which repositioning spot, how to resolve a tie), **pick whatever is worst for the players.** If it's still unclear, pick randomly rather than debating it.

**Choosing a Shoot target**, in priority order: not obscured → not in cover → controls an objective marker → closest → wounded → ready.

**Choosing a Fight target** (multiple in range), in priority order: wounded → controls an objective marker → ready.

**Choosing where to Reposition/Dash for a Marksman NPO:** prefer a spot with a valid target under the Shoot-target priority above; if none, prefer a spot with a visible objective marker.

---

## ORDERS AND COVER, AT A GLANCE

| Order | Can Shoot / Charge? | Can counteract? | Valid target while in cover? |
|---|---|---|---|
| **Engage** | Yes | Yes | Yes (visible = valid) |
| **Conceal** | **No** | **No** | **No, if in cover** — otherwise still valid |

**Counteracting:** if all of one side's operatives are expended but the other side still has ready operatives, an expended **Engage**-order operative can counteract for a free 1 AP action (not Guard), once per turning point, with its move capped at 2". This applies to NPOs too, when their mission pack allows it — check the specific pack.

---

## COMMON ACTION LOOP — every activation, in short

`Ready NPO selected (Threat Principle)` → `assign Engage or Conceal based on what it can do` → `run its behaviour top-to-bottom, stop at the first legal action` → `resolve that action` → `mark it expended` → `repeat / hand activation back`

---

## DO THIS / DON'T FORGET

| DO | DON'T |
|---|---|
| Read the specific NPO's own datacard for a **Behaviour Changes** override before defaulting to Brawler/Marksman above | Assume every big NPO follows the generic loop — bosses often don't |
| Apply the Threat Principle **consistently**, even when it "feels bad" for the players — that's the point | Let sympathy for the newer player quietly soften an NPO's target choice |
| Give Conceal orders to NPOs that can't act, so they aren't free kills standing in the open | Forget Conceal NPOs are still a valid target if not actually in cover |
| Track wounded/injured status on every NPO the same way you would a player operative | Skip re-checking wound thresholds after each hit — injured NPOs move and hit differently |
| Re-roll initiative-linked outcomes purely by the stated rule (NPOs always take initiative on a win) | House-rule initiative "to be fair" — the asymmetry is intentional |
| Reset to "one player" resource management when playing co-op (shared CP, shared equipment) | Let each human player track separate CP/equipment as if playing two armies |

---

*Distinct from Community Content NPO cheat sheets — those remain out of scope for this project. Verify against Core Book Joint Ops mission pack and the specific mission pack in play before a real session | 2026-08-17.*
