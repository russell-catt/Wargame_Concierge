<!--
FILE: games/the_warcode/Quick_Reference_Play_Guide.md
VERSION: v0.2 (2026-08-25)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, warcode_tactical_doctrine)

DOCUMENT_TYPE: Quick Reference / Cheat Sheet
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: The Warcode
REFERENCE_STATUS: Active — draft (2026-08-23)

SOURCES:
  - raw/the_warcode/The Warcode Rulebook V.0.8.7-F.pdf (read via extract 2026-08-23)

PURPOSE:
  Dense two-page-target reference for at-table use. Print double-sided if desired.

UPDATE_TRIGGER:
  Beta supersedes v0.8.7-F on core sequences.
-->

# Quick reference — The Warcode (beta v0.8.7-F)

**`confidence: draft`** · read **2026-08-23** · unofficial · **33" × 24"** · **8 models/side** · **2 AP/unit/round**

---

## Setup (in order)

1. Scenario + victory conditions  
2. D6 → VP **positions** (1–6 layouts; values on token art)  
3. D6 → deploy first + R1 initiative  
4. Alternate deploy 1 unit  
5. **4 equipment points** → grenades / medkits (unless unit locked)  
6. Initiative Phase → Tactical Phase  

---

## Round flow

```
INITIATIVE (D6) → TACTICAL (alternate activations) → END OF ROUND
  → unit end effects → protocol (Map section: L/C/R/Total) → VP score → Contracts if behind → next round
```

**Round start:** draw protocol — read **Left / Centre / Right / Total** before moving.

**Final round** → winner per scenario. *Core of the Machine:* **tie VP = both lose**.

---

## Activation (one unit, 2 AP)

| Action | AP | Notes |
|--------|-----|-------|
| **Move** | 1 | Max **M** inches; partial cover **−1"** |
| **Shoot** | 1 | Needs ammo; hit ≥ target **A** |
| **Reload** | 1 | |
| **Overwatch** | 1 | Triggers on enemy move in LoS; **Pass** does not trigger |
| **Melee attack** | 1 | In melee range |
| **Engage** | 2 | Into melee |
| **Disengage** | 1 | From melee lock; may need D6 |
| **Use ability / equipment / interact** | varies | Doors, medkit, grenade |
| **Pass** | 0 | End activation |

Flip token → unit spent for this round.

---

## Core stats

| Stat | Use |
|------|-----|
| **HP** | Damage removes HP; 0 = killed |
| **A** (Agility) | Hit threshold ranged & melee |
| **Armour** | Penetration check threshold |
| **M** | Inches per move AP |

---

## Shooting (summary)

1. Pay AP + ammo  
2. Hit: each shot roll D6 **≥ target A** (modifiers apply)  
3. Pen: roll **≥ effective Armour** (weapon pen modifies)  
4. Damage: most rolls normal; **6** = critical per weapon profile  
5. **Overwatch** uses same pipeline when triggered  

**Shade (Sniper):** target **A −1** when Shade shoots.

---

## Melee (summary)

1. Attacker rolls dice = **melee strength**  
2. Hit check vs **A**  
3. Defender rolls dice = **melee strength** to block matching/exceeding hits  
4. Pen vs **Armour** → damage  

**Melee Lock:** in range = locked unless disengage/escape rules apply.  
**Smasher:** enemies within **1"** locked even without base contact.

---

## Cover & movement

| Terrain | Effect |
|---------|--------|
| Partial cover | **−1"** move through |
| Full cover (wall) | Blocks LoS; friend within 1" of cover blocks move-through if too tight |
| Friendly screen | Agility bonus if shooting through friend (see Key_Concepts) |

---

## VP & Contracts

- **D6 VP setup:** one D6 → 1 of 6 token **layouts** on 33" × 24" board; read **values** from token art  
- Control: friendly within **1"** of VP token, **no enemy** in 1" at end of round  
- **Contested** if both sides present  
- **Contract** if behind **≥1 VP:** draw from **8-card** deck → Target = name in **opponent's faction column** → **1 VP** on kill (any cause)  
- Example: vs Ulfari, card **6037** → hunt **Shade** — see [`rules/Contract_Cards_Reference.md`](rules/Contract_Cards_Reference.md)  

---

## Re-rolls

| Source | Points |
|--------|--------|
| Leader alive | **+2** start of each round |
| Your unit killed | **+1** immediately |
| Spend | **1** point = re-roll **entire** roll (not one die) |

**Not on:** initiative roll, scenario event card rolls.  
Melee: attacker may re-roll hit **before** defender blocks.

---

## Equipment (4 pts total)

| Item | Typical use |
|------|-------------|
| Grenade | AP + blast; mark template |
| Medkit | Heal per rules |

**Blast** / **Phantom:** start with **2 grenades**, no other equipment.

---

## Leaders

| Faction | Leader | Rule |
|---------|--------|------|
| Protagen | **Commander Rickman** | 2 re-rolls / round while alive |
| Ulfari | **Soul Eater** | 2 re-rolls / round while alive |

Kill enemy Leader → shut off their 2/round re-rolls.

---

## Special units (don't forget)

| Unit | Rule |
|------|------|
| **Reaper** | **No ranged weapon** → no Overwatch |
| **Reaper** | A 5 → may ignore cover/screen agility bonuses |
| **Blast / Phantom** | Grenade-locked loadout |
| **Smasher** | 1" forced Melee Lock |
| **Bastion / Doom** | Heavy weapon; slow or low A |

Full profiles: [`factions/protagen_marines/Squad_Datasheet.md`](factions/protagen_marines/Squad_Datasheet.md), [`factions/ulfari/Squad_Datasheet.md`](factions/ulfari/Squad_Datasheet.md).

---

## Dice quick table

| Roll | When |
|------|------|
| D6 ≥ X | Hit, pen, many checks |
| D6 6 | Often critical damage |
| D6 tie | Initiative re-roll |

---

## Page 2 — turn reminder card

**My activation checklist**

- [ ] Unit not yet activated this round?  
- [ ] **2 AP** remaining (track spends)  
- [ ] Declare action → pay AP → resolve → repeat or **Pass**  
- [ ] Flip activation token  

**Before I shoot**

- [ ] LoS clear? Ammo?  
- [ ] Target **A** known (Shade sniper?)  
- [ ] Overwatch declared against me?  

**Before I move**

- [ ] Partial cover path? (−1")  
- [ ] End in VP radius?  

**End of round**

- [ ] VP scored?  
- [ ] Behind → Contract?  
- [ ] Leader re-rolls next round?  

---

## Links

- Walkthrough: [`First_Game_Walkthrough.md`](First_Game_Walkthrough.md)  
- Glossary: [`rules/Keyword_Glossary.md`](rules/Keyword_Glossary.md)  
- Contracts: [`rules/Contract_Cards_Reference.md`](rules/Contract_Cards_Reference.md)  
- Protocols: [`rules/Protocol_Cards_Reference.md`](rules/Protocol_Cards_Reference.md)  
- Quotes: [`rules/Rulebook_Quotes.md`](rules/Rulebook_Quotes.md)  

---

## Change Log

- v0.2 (2026-08-25): D6 VP placement line; protocol Map section; eight-card contract reference (S8).
- v0.1 (2026-08-23): Dense two-page-target QR (warcode_tactical_doctrine).

## Attribution

- Project: Wargame_Concierge
- Maintainer: Russell Catt
- The Warcode is property of RedMakers.

## Rising Tide Notes

- Print target: two sides of one sheet; trim to table size.
