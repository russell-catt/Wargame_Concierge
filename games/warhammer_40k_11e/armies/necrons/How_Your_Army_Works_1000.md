<!--
FILE: games/warhammer_40k_11e/armies/necrons/How_Your_Army_Works_1000.md
VERSION: v1.4 (2026-09-25)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer — Cryptek 1000 play pack)

DOCUMENT_TYPE: Teaching Guide / laminate source
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: Warhammer 40,000 - 11th Edition
FACTION: Necrons
DETACHMENT: Cryptek Conclave
REFERENCE_STATUS: Active — companion to Army_List_1000_V1_Doomstalker_Conclave.md; app-backup paper sheet for the 1000-point megabattle

SOURCES:
  - games/warhammer_40k_11e/armies/necrons/Army_List_1000_V1_Doomstalker_Conclave.md
  - games/warhammer_40k_11e/armies/necrons/How_Your_Army_Works_500.md (structure)
  - games/warhammer_40k_11e/armies/space_marines/How_Your_Army_Works_1000.md (shared headings)
  - games/warhammer_40k_11e/armies/necrons/Cryptek_Conclave.md
  - games/warhammer_40k_11e/armies/necrons/Cryptek_Conclave_Primary_Missions.md
  - games/warhammer_40k_11e/armies/necrons/Reanimation_Protocols.md
  - games/warhammer_40k_11e/armies/necrons/units/research/Canoptek-Doomstalker.md (Wahapedia 2026-09-24)
  - games/warhammer_40k_11e/armies/necrons/units/research/Canoptek-Scarab-Swarms.md (Wahapedia 2026-09-24)
  - games/warhammer_40k_11e/rules/Core_Rules_Quotes.md — 01.06 Leadership rolls, 01.07 Battle-shock rolls, 08.03 Battle-shock step, 09.x Fall Back modes, 16.01 Actions
  - Community / Wahapedia Conclave stratagem names (retrieved 2026-09-19) — draft until Faction Pack line-check
  - raw/Megabattle_prep/megabattle_strategy.md + megabattle_prep.md (owner's Google prep notes, read 2026-09-25; rules-checked)

PURPOSE:
  Paper backup for the parent's 1000 Cryptek Conclave list: unit jobs,
  deployment, Reanimation, Conclave menu, Priority Assets Primaries, the
  Doomstalker's job, what Battle-shock stops per unit, the weapon keywords
  in this roster, and every CP spend with when to use it. Same headings as
  the Space Marines 1000 guide so the two players can compare sheets.

PRINT_NOTE:
  Print HTML: print/40k_how_army_works_1000_conclave.html — 5 Letter pages,
  flowing layout (no forced page breaks; the megabattle joint war plan +
  table etiquette closes page 5). Sections below map 1:1 to the HTML.

UPDATE_TRIGGER:
  List composition change, Faction Pack / dataslate change to Conclave
  stratagems or enhancements, Doomstalker points change, or Chapter Approved
  Primary text change.
-->

# How your army works — 1000 Cryptek Conclave (Doomstalker + Hierotek)

> **FORCE DISPOSITION: PRIORITY ASSETS**  
> MFM: `CRYPTEK CONCLAVE - 2DP - PRIORITY ASSETS`  
> List: [`Army_List_1000_V1_Doomstalker_Conclave.md`](Army_List_1000_V1_Doomstalker_Conclave.md) — **945** official app, two enhancements (Gauntlet + Atomic Disintegrators) · Matching: [`../../setup/Chapter_Approved_Force_Dispositions.md`](../../setup/Chapter_Approved_Force_Dispositions.md) · Pack index: [`Cryptek_Play_Pack_1000.md`](Cryptek_Play_Pack_1000.md)

**Plan:** Three Cryptek gun bricks (Warriors A, Warriors B, Immortals) stand on Expansion / Central / home and refuse to die, Scarabs and Macrocytes run Actions and screens, Tomb Crawlers guard the backfield, and the **Doomstalker** deletes the biggest enemy unit from a 48" lane. Reanimate every Command; **Potentiality Syphon** off-turn. Caps: **15VP**/round · **45VP**/game.

## Your pieces

| Piece | Job | Do | Avoid |
|-------|-----|----|-------|
| **Warriors A + Warden + Geomancer** (Gauntlet) | Expansion OC brick (20+ OC) | Walk to a non-home flag; 30" / 18" guns; default `[IGNORES COVER]`; Geomancer pins a threat | Chasing the whole board |
| **Warriors B + Technomancer** | Home / backfield brick | Hold home; heal the Doomstalker D3 at end of Movement | Leaving home and the Doomstalker naked |
| **Immortals (10) + Plasmancer** (Atomic) | Midboard gun brick | Central; crits on 5+; anti-Vehicle / anti-Monster menu when armour shows | Standing where a whole army can shoot them |
| **Doomstalker** | Anti-tank artillery | Remain Stationary; 48" lane; biggest VEHICLE / MONSTER first | Walking it forward; charging with it |
| **Scarabs (6)** | Actions / screens / OC drain | Advance wide; Actions; stay 6" from a Cryptek for OC 1; one-base Self-destruction into armour | Expecting Conclave gun buffs; whole-unit suicides |
| **Macrocytes (5)** | Scouts 8" · −1 to Hit aura | Scout before turn 1; sit the aura on the brick that gets shot first; nanoscarab +1 wound | Thinking they grant Ignores Cover — they don't |
| **Tomb Crawlers (2)** | Backfield screen | Stand between the Doomstalker and enemy Deep Strike; ignore modifiers within 12"; S6 claws | Sending them across the board |

## Deployment

| Area | Unit | Reason |
|------|------|--------|
| Backfield, clear 48" lane, obscured from anti-tank | Doomstalker | Heavy wants stillness; Blast wants big squads in view |
| Home objective, within 6" of the Doomstalker | Warriors B + Technomancer | Holds home; Technomancer heal reaches the walker |
| Between Doomstalker and open floor | Tomb Crawlers | Deny 9" Deep Strike landings behind you |
| Route to Expansion | Warriors A + Warden + Geomancer | OC / Actions; long guns via Gauntlet |
| Route to Central, in cover | Immortals + Plasmancer | T5 / 3+ brick shoots and holds |
| Flanks, then Scout 8" forward | Macrocytes · Scarabs | Action volume; screens; aura over a brick |
| Reserves | **None** | Everything is on the table turn 1 — this army out-lasts, it does not ambush |

## Command script

**+1CP → Battle-shock rolls (Warden's Engrammatic Logic if a brick failed) → end of Command: REANIMATE every unit (Warriors re-roll the D3) → their Command: Potentiality Syphon?**

## Reanimation + Conclave menu

| Rule | Effect |
|------|--------|
| **Reanimation Protocols** | End of **your** Command (`08.05`), free, every unit still on the table: D3 wounds back — heal survivors first, then return models at 1W. Wiped = gone. The Doomstalker heals too. |
| **Their Number is Legion** | Both Warrior bricks re-roll the D3 every time RP activates (including Syphon). |
| **Technosorcerous Augmentations** | Cryptek guns gain `[ASSAULT]`. Each **Cryptek unit** that shoots picks **one**: `[ANTI-INFANTRY 3+]` · `[IGNORES COVER]` · `[ASSAULT]` · `[HEAVY]` · `[ANTI-MOUNTED 4+]` (+ anti-Vehicle / anti-Monster on the Immortals via Atomic Disintegrators). **Three bricks = three picks.** Say each out loud before rolling. |


# Priority Assets — Secure / Vital / Sabotage

You always play **your** Priority Assets Primary; the opponent's Disposition picks which of the five. **confidence: draft** — same teaching shape as [`Cryptek_Conclave_Primary_Missions.md`](Cryptek_Conclave_Primary_Missions.md); the Chapter Approved card wins.

### 1. Secure Asset — vs Take and Hold

| Your scoring | Keys for this 1000 Conclave |
|--------------|-----------------------------|
| EOT: **Action** Secure Asset on a non-home | Scarabs and Macrocytes Action; Warriors A holds Expansion |
| EOT bonus: destroy a unit on **Central** | Immortals + Doomstalker point at whatever stands on Central |
| BR2+ Command: hold non-home; bonus hold 3+ | Expansion (A) + home (B) + Central (Immortals) — the whole point of three bricks |
| Opponent: hold 3+ / Hold More / steal your home late | Warriors B never leaves home; Crawlers screen Deep Strike |

**Success:** Steady Actions from the Canoptek chaff + three bricks on three flags = Hold More is off the table for them.

### 2. Vital Link — vs Purge the Foe

| Your scoring | Keys |
|--------------|------|
| EOT: hold Central + Operation Markers via Action | **Immortals on Central** Action repeatedly — the T5 / 3+ tarpit |
| BR2+ Command: hold non-home; bonus if Central | Warriors A adds Expansion so Central is not your only tick |
| End game: opponent's home | Scarabs late — only if already banked |
| Opponent: Kill More + Hold More | Do **not** feed Scarab or Macrocyte units for nothing; Reanimate instead of trading |

**Success:** One durable brick Actions Central every turn; Syphon it in their Command phase.

### 3. Sabotage — mirror (both Priority Assets)

| Your scoring | Keys |
|--------------|------|
| EOT: **Sabotage Action** on each non-home (bonus enemy territory; Central counts) | One unit = one Action, so Scarabs + Macrocytes = two Actions a turn; Warriors A adds a third once Expansion is safe |
| BR2+ Command: hold 1+ non-home | Warriors A locks Expansion while Actions run |
| Opponent: identical | Deny turn-1 mega scores: Doomstalker and Immortals shoot their Action units first |

**Success:** Action volume early. You have more cheap Action bodies than a Marine list — use them.

### Write before deployment

| Field | Write here |
|-------|-----------|
| Opponent's Force Disposition | ☐ Take and Hold · ☐ Purge the Foe · ☐ Priority Assets · ☐ Disruption · ☐ Reconnaissance |
| Your Primary this game | ☐ Secure Asset · ☐ Vital Link · ☐ Sabotage · ☐ Extract Relic · ☐ Vanguard Operation |
| Home objective holder | Warriors B + Technomancer |
| Central holder | Immortals + Plasmancer |
| Expansion holder | Warriors A + Warden + Geomancer |
| Action units | Scarabs · Macrocytes (Warriors A when Expansion is safe) |
| Doomstalker turn-one target | ____________ (biggest visible VEHICLE / MONSTER; else the densest Infantry) |

### Scoring rhythm — every round

| Moment | You do | Necron habit |
|--------|--------|--------------|
| Your Command (BR2+) | Count OC on non-home flags; score the hold tick | Battle-shock rolls happen *first* — a shocked brick has OC '-' for this count |
| Your Movement | Start Actions with Scarabs / Macrocytes (they give up shooting and charging) | Bricks stay put; Advance only with an `[ASSAULT]` pick planned |
| Your Shooting | Kill the on-Central unit if the Primary pays for it | Doomstalker first, then bricks — three menu picks out loud |
| End of your turn | Complete Actions; score the EOT ticks | Check the 15VP round cap before you over-commit |
| Their Command | — | **Potentiality Syphon** on the brick that just got shot and is still on its flag |


# Priority Assets — Extract / Vanguard + toolkit

### 4. Extract Relic — vs Disruption

| Your scoring | Keys |
|--------------|------|
| Disruption places Operation Markers on terrain outside their DZ | Know the markers before round 1; Macrocytes Scout toward them |
| Once/turn **Sensor Sweep** Action on a Central you control | Immortals hold Central, Scarabs do the Sweep — OC 1 within 6" of the Plasmancer |
| EOT: Sweep · kill an on-objective unit · final-marker bonus | Doomstalker kills the on-objective unit; Immortals finish |
| BR2+ Command: hold non-home | Expansion (Warriors A) still ticks |
| Opponent also Sweeps | Charge-block their Central with Scarabs after enough Sweeps |

### 5. Vanguard Operation — vs Reconnaissance

| Your scoring | Keys |
|--------------|------|
| Once/turn **Vanguard Operation** Action in enemy-territory terrain | Scarabs (10" move + Advance) into enemy-half terrain; Macrocytes as second Action body |
| EOT: kill 1+ enemy units | Doomstalker or a brick picks off a chip unit — easy tick most turns |
| BR2+ Command: hold 1+ non-home | Warriors A on Expansion |
| End game: control their home | Only if the Action unit is already there and alive |

**Success:** Action in enemy territory without gifting terrain kills — Scarabs die cheaply, but a wiped unit cannot reanimate.

## Toolkit

| Tool | Use it when |
|------|-------------|
| **Warriors A + Warden + Geomancer** | Expansion hold · Syphon target · Warden lets it Fall Back and still shoot / charge · Geomancer pin slows the charger |
| **Warriors B + Technomancer** | Home hold · D3 heal to the Doomstalker or a brick at end of Movement |
| **Immortals + Plasmancer** | Central tarpit · Anti-Infantry 3+ into bodies · Atomic anti-Vehicle into tanks · Living Lightning mortals on a hidden unit |
| **Doomstalker** | Any VEHICLE / MONSTER in 48" · Blast into a 10-model squad · Overwatch on 5+ vs a charge into your backfield |
| **Scarabs** | Sabotage / Secure / Sweep / Vanguard Actions · charge-block · −1 OC to whatever they touch · one base Self-destruction into a VEHICLE |
| **Macrocytes** | Scout 8" pre-game · aura on the brick being shot · nanoscarab +1 RP wound · second Action unit |
| **Tomb Crawlers** | Deep Strike screen · knife-range shooting that ignores cover tricks · S6 claws vs chaff |
| **Potentiality Syphon (1CP)** | Brick already on an objective, opponent's Command phase — default off-turn spend |
| **Conclave menu (0CP)** | Every Shooting phase — three bricks, three picks, said out loud |

## Pre-game checklist

- [ ] List says **FORCE DISPOSITION: PRIORITY ASSETS**
- [ ] Opponent Disposition → circle the Primary on page 2
- [ ] Attachments written: A ← Warden + Geomancer · B ← Technomancer · Immortals ← Plasmancer
- [ ] Enhancements locked: **Gauntlet → Geomancer**, **Atomic Disintegrators → Plasmancer**. No Bolas, no Abacus. **945**.
- [ ] Proxies agreed: Apprentek = Plasmancer, Despotek = Royal Warden
- [ ] Doomstalker unprimed OK for this game
- [ ] Macrocytes **Scout 8"** before turn 1
- [ ] Token: end of Command → **REANIMATE**
- [ ] Physical Primary card + Faction Pack stratagem cards open


# Three bricks, one Doomstalker — battle plan

| | Warriors A (Expansion) | Warriors B (home) | Immortals (Central) |
|--|------------------------|-------------------|---------------------|
| Characters | Warden (Leader) + Geomancer (Support) | Technomancer (Support) | Plasmancer (Support) |
| Reach | Gauntlet: flayers 30", reapers 18", relic blaster 30" | Flayers 24", reapers 12" — a home brick, not a hunter | Gauss 24" or tesla 18"; Harbinger: 5+ to Hit is a Critical Hit |
| Battle-shock | **6+** (character Ld) while a character lives | **6+** while the Technomancer lives | **6+** while the Plasmancer lives |
| Trick | Warden: Fall Back and still shoot / charge · once/battle un-shock a unit within 12" | Heal D3 to a unit within 6" at end of Movement — Doomstalker or a brick | Living Lightning: D6 mortals on a 4+ into a visible unit within 18" |
| Menu default | `[IGNORES COVER]` | `[HEAVY]` (it never moves) | `[ANTI-INFANTRY 3+]`; Atomic anti-Vehicle vs tanks |

**Why three bricks of 10 and not one of 20:** each Cryptek Support needs its own bodyguard. Three seats = three menu picks, three Battle-shock tests at 6+, three Syphon targets. A single 20-brick would leave one Cryptek on the floor with no unit and no menu.

## Turn-one order

1. Macrocytes Scout 8" (before the first turn).
2. Command: +1CP; no Battle-shock yet; **Reanimate** (nothing to heal turn 1 — say it anyway to build the habit).
3. Move A toward Expansion, Immortals toward Central; B and Doomstalker **Remain Stationary**; Scarabs Advance wide.
4. End of Movement: Technomancer heal (nothing yet); Geomancer pins the scariest charger within 18".
5. Shooting: **Doomstalker first** at the biggest target; then Immortals; then A; then B. Announce all three menu picks.
6. No charges turn one. Score nothing yet; set the board.

## Scarab Self-destruction

1. Charge a VEHICLE or a tough brick you cannot out-shoot.
2. **Start of the Fight phase**, before anyone fights: remove **one** Scarab base.
3. Roll D6, +1 if the target is a VEHICLE: 2–5 → D3 mortal wounds; 6+ → 3 mortal wounds.
4. Remaining bases stay locked in: enemy models in Engagement Range are −1 OC (min 1).
5. One base per unit per Fight phase — never chain-detonate.

## Doomstalker: lanes, Heavy, Blast, Overwatch

**The doomsday blaster is a direct-fire gun, not indirect.** It needs line of sight, so there is no "spotter" trick to learn — the skill is deploying it where it can see, and not moving it.

| Situation | Hit roll | What applies |
|-----------|----------|--------------|
| **Remained Stationary**, sees target | **3+** (BS 4+, +1 Heavy) | Blast: +1 attack per 5 models in the target (D6+1 → D6+3 into a 10-model squad) |
| Moved this turn, sees target | 4+ | Only move it when the lane is truly dead; an 8" move usually costs a turn of value |
| Damaged (1–4 wounds left) | −1 to Hit (4+ still, or 5+ if it moved) | Molecular Targeting (1CP) ignores Hit modifiers — verify the pack allows a non-Cryptek target |
| Enemy charges / moves in range — **Fire Overwatch** (1CP) | **5+** (Sentinel Construct) instead of 6 | The best Overwatch in either army; keep 1CP when Terminators are near your backfield |
| Target within Engagement Range of your unit | — | Blast weapons **cannot** fire at it; use the twin gauss flayer or a different target |

**Target order:** VEHICLE / MONSTER in the open → VEHICLE in cover (AP-3 still bites) → the densest Infantry squad (Blast). S14 wounds T9 on a 3+, T5 Terminators on a 2+; Damage 3 removes one Terminator per unsaved wound. **Keep it alive:** Reanimation heals D3 a turn, the Technomancer adds D3 at end of Movement, and Deadly Demise D3 punishes anyone who finishes it in melee — but do not rely on any of that instead of terrain.


# Battle-shock + weapon keyword card

Battle-shock does not normally stop moving, shooting, charging, fighting or Reanimation.

**When:** Command phase step 3 (`08.03`), every unit at or below half strength rolls 2D6 vs the **best Ld in the unit** (`01.06`) — an attached Cryptek or Warden (Ld 6+) makes a Warriors brick test on 6+, not 8+. **Order matters:** the test comes *before* end-of-Command Reanimation, so a brick shot down to half tests first, then rebuilds. **Every failed test** (`01.07`): OC becomes '-' · your stratagems cannot target that unit · it cannot start or complete Actions · Falling Back becomes Desperate Escape. Datasheet and detachment abilities (RP, Legion, Conclave menu, heals, auras) keep working.

## What it stops in this army

| Unit | What failure costs | What it can still do |
|------|--------------------|----------------------|
| **Warriors A + Warden + Geomancer** | Loses Expansion (20+ OC → nothing); no Actions; no Syphon, Microscarab Swarm, Molecular Targeting or Untapped Power on it | Shoot with a menu pick, Reanimate with re-roll, pin with the Geomancer; **Warden's Engrammatic Logic** (once/battle, free) removes the shock at the start of any phase |
| **Warriors B + Technomancer** | Home objective goes uncontrolled; no Syphon / Microscarab; no Actions | Shoot, Reanimate, heal a unit within 6" |
| **Immortals + Plasmancer** | Central flips to the opponent; no Syphon, Microscarab or Atomic-backed stratagem support | Shoot with Harbinger crits and the menu; Living Lightning; Reanimate |
| **Doomstalker** | OC 4 → nothing; **no Fire Overwatch** (a stratagem) so Sentinel Construct is wasted; no Molecular Targeting | Remain Stationary and shoot at 3+; Reanimate; Deadly Demise |
| **Scarabs** | **Cannot Action** — their whole job; OC 1-near-Cryptek → nothing; cannot be Syphoned | Move, charge, tarpit, −1 OC to enemies they touch, Self-destruction |
| **Macrocytes** | Cannot Action; OC 1 → nothing | −1 to Hit aura, accelerator mandible, nanoscarab +1 wound all keep working |
| **Tomb Crawlers** | OC → nothing; no defensive stratagem | Screen, shoot ignoring modifiers within 12", fight with S6 claws |

**Fixes in order:** Insane Bravery (1CP, once/battle, *before* rolling — auto-pass a test that would lose a scoring flag) → Warden's Engrammatic Logic (free, once/battle, any phase start, any Necron unit within 12") → accept it and Reanimate anyway. Reanimation can lift a brick back *above* half strength before next turn's test.

## Major weapon keywords in this roster

| Keyword | Meaning / best use |
|---------|--------------------|
| **LETHAL HITS** | A Critical Hit (unmodified 6) wounds automatically — skip the Wound roll. On every gauss weapon: flayers, reapers, blasters, scalpels, Crawler reapers, Doomstalker twin flayer, Scarab mandibles. Why S4 Warriors still hurt T9 vehicles. |
| **RAPID FIRE 1** | +1 attack within half range. Gauss flayers double up inside 12" (15" with the Gauntlet); Warden's relic blaster is Rapid Fire 2. |
| **HEAVY** | +1 to Hit if the unit Remained Stationary. Native on the doomsday blaster; a Conclave menu pick for a brick that did not move. |
| **BLAST** | +1 attack per five models in the target; cannot fire at a unit engaged with your models. Doomsday blaster into 10-model squads. |
| **ASSAULT** | Shoot after Advancing. Free on every Cryptek model's gun in this detachment; a menu pick to give the whole brick; native on the tesla caster. |
| **ANTI-INFANTRY 3+ / ANTI-MOUNTED 4+ / ANTI-VEHICLE / ANTI-MONSTER** | Unmodified Wound roll of N+ is a Critical Wound vs that keyword — you wound on N+ regardless of Toughness. The menu picks (Vehicle / Monster only via Atomic Disintegrators on the Immortals). |
| **IGNORES COVER** | Target gets no Benefit of Cover. Menu default in terrain; native on the Geomancer's shock wave pulse. |
| **TORRENT** | Auto-hits. Geomancer pulse (D6+2 shots, S4) — the list's best Overwatch weapon besides the Doomstalker. |
| **MELTA 2** | +2 Damage within half range. Geomancer beam (S8 AP-2 D2 → D4 inside 9", 12" with the Gauntlet). |
| **SUSTAINED HITS 1 / 2** | Critical Hit adds 1 / 2 extra hits. Tesla carbines (2) and tesla caster (1). With the Plasmancer's 5+ crits, tesla Immortals are a body-shredder in the open. |
| **TWIN-LINKED** | Re-roll Wound rolls (never Hits). Crawler twin gauss reaper; Doomstalker twin gauss flayer. |
| **FEEL NO PAIN 5+** | Technomancer's Rites of Reanimation gives the bodyguard a 5+ roll to ignore each wound — sits on Warriors B in this list. |
| **DEADLY DEMISE D3 · SCOUTS 8" · FLY** | Doomstalker explodes for D3 mortals to units within 6" on a 6 when destroyed · Macrocytes move 8" before turn 1 · Technomancer and Scarabs move over models and terrain. |


# CP spends — exact-list card

Teaching paraphrase; the current Core card / Faction Pack wins. Conclave names **draft** (community / Wahapedia shape, retrieved 2026-09-19).

**Each Command:** both players +1CP. Same stratagem once per phase; usually one stratagem per unit per phase; **Battle-shocked units cannot be targeted by any of these.** This list has no Quantum Abacus — spent CP stays spent.

## Highest priority

| Spend | CP | When | Use it when… |
|-------|----|------|--------------|
| **Potentiality Syphon** | 1 | **Opponent's** Command phase | A brick is standing on an objective and has lost models — it activates RP now (Warriors re-roll; Cryptek units +1 wound). This is the spend that makes the army feel unfair. Bank for it every round. |
| **Microscarab Swarm** | 1 | Your Warriors / Immortals unit is picked as a target | They are trying to delete a whole brick in one activation. Invulnerable save for the phase (Warriors softer, Immortals stronger — read the card). Never spend it on a few bolter shots. |
| **Fire Overwatch** | 1 | Enemy unit moves / Advances / charges within range of the Doomstalker | Terminators or a tank come at your backfield. Doomstalker hits on **5+**; Geomancer pulse auto-hits. Any other unit only hits on 6s — usually skip. |
| **Command Re-roll** | 1 | Right after the roll | A key Doomsday Hit or Damage roll, a Living Lightning 4+, a Battle-shock test for a flag, or a Scarab charge. It **cannot** re-roll the Reanimation D3 — not on the card's list. |

## Your turn

| Spend | CP | When / best use |
|-------|----|-----------------|
| **Untapped Power** | 1 | Your Shooting, before a Cryptek brick shoots: it takes **two** menu picks. `[ASSAULT]` + `[IGNORES COVER]` on the turn Warriors A Advance onto Expansion; `[ANTI-INFANTRY 3+]` + `[IGNORES COVER]` for Immortals into Marines in ruins. |
| **Molecular Targeting** | 1 | Your Shooting or Fight: ignore Hit modifiers (Cryptek units also ignore Wound modifiers). Use when a brick is −1 to Hit from an enemy aura, or on the Damaged Doomstalker if the pack allows it. |
| **Synergistic Empowerment** | 1 | Start of your Shooting: one nearby non-Monster / Vehicle Necron model gains CRYPTEK. Tomb Crawlers or Macrocytes get a menu pick for one phase. Not the Doomstalker (Vehicle). |
| **Insane Bravery** | 1 | Your Command, once/battle, before the roll: auto-pass a Battle-shock on the brick whose OC decides a flag this turn. |
| **Epic Challenge** | 1 | Fight: a Cryptek or Warden gains Precision to hit an attached enemy Character. Rare — you are a gun army. |

## Opponent turn

| Spend | CP | When / best use |
|-------|----|-----------------|
| **Animus Curse** | 1 | After a Cryptek is destroyed (verify trigger): punish the killer. Insurance when they snipe the Geomancer or Plasmancer. |
| **Heroic Intervention** | 1 | End of their Charge: a nearby unit charges in. Tomb Crawlers (S6 claws) or Scarabs onto the unit that just hit a brick — protects a flag more than it kills. |
| **Counter-offensive** | 2 | Fight interrupt after an enemy unit fights. Premium; almost never worth it for Warriors. Save the 2CP for two Syphons. |
| **Smokescreen** | 1 | Only if a unit's keywords satisfy the Core card. Nothing in this list is a natural Smoke unit — usually skip. |
| **Rapid Ingress** | 1 | Not applicable — nothing is in Reserves. Do not plan around it. |

## Budget + end turn

| Round | Plan |
|-------|------|
| BR1 | Spend nothing on your turn; hold 1CP for Syphon in their Command or Overwatch on a turn-one charge |
| BR2 | Syphon the brick on Central / Expansion; Microscarab only against a full-army focus |
| BR3 | Untapped Power on the brick that decides Central; Syphon again |
| BR4–5 | Insane Bravery / Command Re-roll on Battle-shock for scoring flags; keep bricks alive over killing |

**Default priority:** hold 1CP for Syphon → Microscarab when they try to wipe a brick → Overwatch with the Doomstalker vs a backfield charge → Untapped Power on a decisive volley → leftovers on Molecular Targeting. **Free every turn, no CP:** Reanimation, Legion re-roll, three menu picks, Technomancer heal, Warden un-shock, Scarab Self-destruction.


# Megabattle — joint war plan with the Blood Ravens + table etiquette

Team game: your 945 Necrons + your son's 1000 Marines on one side. Source: megabattle prep notes at `raw/Megabattle_prep/` (2026-09-25), rules-checked against this pack. **confidence: draft.**

**The team plan in one line:** a shared **backline firebase** (your Doomstalker + Brick B beside his Whirlwind + Techmarine), a shared **midboard push** (your Brick A + Immortals beside his Captain + Tacticals + Devastators), and a **pocket hammer** (your Scarabs set the trap; his Chaplain + Assault Terminators spring it). Your bricks give his Marines a wall that regrows; his Marines give your bricks the killing power they lack.

| Sector | Your Necron job | His Marine job | Why it works |
|--------|-----------------|----------------|--------------|
| **1 · Backline firebase** (your corner) | Doomstalker on a long open lane — **never moves** (3+ with Heavy). Brick B + Technomancer stand *in front* of the Doomstalker and the Whirlwind, stationary on `[HEAVY]`. Technomancer heals whichever of the two Necron units got shot. | Whirlwind hides behind your screen; Techmarine within 3" blesses it every Command phase (+1 to Hit, repair). | Fast melee cannot reach either gun without going through 10 Warriors that reanimate. Anything that charges the zone eats Doomstalker Overwatch on **5+**. |
| **2 · Midboard push** (one shared flank) | Brick A (Warden + Geomancer, Gauntlet) sits a step *behind* the Tacticals in cover — 30" / 18" guns still reach No Man's Land. `[IGNORES COVER]` flushes ruins. Immortals + Plasmancer take `[ANTI-INFANTRY 3+]`; if a war machine pushes the lane, switch to the Atomic anti-Vehicle / anti-Monster pick so the Marines keep shooting infantry. | Captain + Tacticals claim the objective; Devastators sit on the lane; Captain's Rites of Battle discounts a stratagem. | Two OC-heavy blocks on Central plus his Oath target dying every turn. **Oath of Moment only buffs his Marines** — you simply point your guns at the same unit. |
| **3 · Pocket hammer** (turn 2–3 strike) | Turn 1: Advance the 6 Scarabs full distance into enemy territory and park them in the face of the scariest enemy unit. They tarpit, drain OC (−1 per model), and screen the landing zone. Turn 2–3: pop **one** base at Fight start if it is a Vehicle. | Turn 2+: Chaplain + Assault Terminators arrive (Rapid Ingress or Homer) behind the Scarab shield, then charge the team's agreed target with +1 to Wound. | Your cheap bugs buy the safe landing; his 235 points of Terminators delete the scoring threat. Agree the target during *their* turn. |

**Rules checks on the prep notes:** Atomic Disintegrators' exact anti-Vehicle / anti-Monster value (the notes say 5+) is **verify on the Faction Pack**. Quantum Abacus is **not on this list** (two-enhancement cap). Rapid Ingress cannot be used in battle round 1. Two Warrior units of 10 — not one of 20 — so bring two trays.

### Packing list

- [ ] Printed rosters — Marines 1000, Necrons 945 (this pack)
- [ ] Stat pages with weapon profiles (roster pages 2–4)
- [ ] Two clearly different dice sets — one per player
- [ ] Two tape measures
- [ ] Movement trays: two Warrior 10s, Immortals 10, Tacticals 10
- [ ] Tokens: wound counters, **Reanimate** reminder, Oath marker, Teleport Homer
- [ ] Laser pointer / line-of-sight tool
- [ ] Shallow tray or display board to carry the army — not a deep box
- [ ] Water and snacks — off the table
- [ ] Physical Primary card + Faction Pack stratagem cards

### Do / Don't

| Do | Don't |
|----|-------|
| Pre-measure during the enemy turn — know the Doomstalker's target before your turn starts | Argue a weird interaction — ask an organiser or roll off and keep moving |
| Roll simultaneously with your son when you shoot different targets | Flip through books — use the CP spends card in this guide and your two or three favourite spends |
| Show proxies before deployment: Apprentek = Plasmancer, Despotek = Warden, unprimed Doomstalker; his claw = relic shield | Reach into another player's lane without asking — coordinate flanks through the team commanders |
| Announce targets out loud: "Brick A fires into *that* unit behind the ruin, `[IGNORES COVER]`" | Move the Doomstalker. Ever, unless its lane is dead |
| Say REANIMATE at the end of every Command phase, and Syphon in theirs | Feed Scarabs or Macrocytes for nothing — a wiped unit cannot come back |

### Turn-by-turn team beats

| Round | You | Together |
|-------|-----|----------|
| BR1 | Firebase set; Brick A + Immortals step onto the shared flank; Scarabs sprint; Doomstalker fires first | Agree the turn-2 hammer target while the enemy moves |
| BR2 | Syphon a brick in their Command; Immortals Action or hold Central | Terminators land behind the Scarabs; Oath on the hammer target — your guns add to it |
| BR3 | Untapped Power on the volley that decides Central; Scarab Self-destruction if tagged on a Vehicle | Hammer strikes; midboard claims 3 flags; firebase Overwatch ready |
| BR4–5 | Hold flags; Insane Bravery / Warden un-shock for scoring bricks | Actions over kills; do not overextend into a sector you did not agree |

Marine side of the same plan: the megabattle section of [`../space_marines/How_Your_Army_Works_1000.md`](../space_marines/How_Your_Army_Works_1000.md).

---

## Related

- [`Army_List_1000_V1_Doomstalker_Conclave.md`](Army_List_1000_V1_Doomstalker_Conclave.md) · [`Cryptek_Play_Pack_1000.md`](Cryptek_Play_Pack_1000.md)
- [`How_Your_Army_Works_500.md`](How_Your_Army_Works_500.md) — the 500 version this grows from
- [`Cryptek_Conclave.md`](Cryptek_Conclave.md) · [`Cryptek_Conclave_Primary_Missions.md`](Cryptek_Conclave_Primary_Missions.md) · [`Reanimation_Protocols.md`](Reanimation_Protocols.md)
- [`units/research/Canoptek-Doomstalker.md`](units/research/Canoptek-Doomstalker.md) · [`units/research/Canoptek-Scarab-Swarms.md`](units/research/Canoptek-Scarab-Swarms.md)
- [`../space_marines/How_Your_Army_Works_1000.md`](../space_marines/How_Your_Army_Works_1000.md) — the opposing sheet, same headings
- [`../../setup/Chapter_Approved_Force_Dispositions.md`](../../setup/Chapter_Approved_Force_Dispositions.md)
- Print: [`print/40k_how_army_works_1000_conclave.html`](print/40k_how_army_works_1000_conclave.html)

---

## Games Workshop notice

**UNOFFICIAL.** This document is completely unofficial and in no way endorsed by Games Workshop Limited. Personal / no-charge use only — never for sale. Warhammer, Warhammer 40,000 and associated marks are trademarks of Games Workshop Limited. Used without permission. No challenge to their status intended. Warhammer 40,000 is Copyright Games Workshop Limited. Teaching notes by Russell Catt (Wargame Concierge). Games Workshop retains IP in the settings and characters. No official logos.

## Change Log

- v1.4 (2026-09-25): Do/don't line and the Marine cross-link no longer cite a page number (the print aid flows, so page numbers move).
- v1.3 (2026-09-25): Print aid condensed 7 → 5 Letter pages (flowing layout); page labels dropped from section headings.
- v1.2 (2026-09-25): App cap is two enhancements. List locked at **945** — Gauntlet (Geomancer) + Atomic Disintegrators (Plasmancer). Bolas and Abacus removed from jobs, Battle-shock, CP card, and the megabattle packing line.
- v1.1 (2026-09-25): Page 7 — megabattle joint war plan with the Blood Ravens (firebase / midboard push / pocket hammer from the Necron seat), packing list, do / don't, turn-by-turn team beats. Incorporated from the owner's `raw/Megabattle_prep/` notes with rules checks (Oath buffs Marines only; Rapid Ingress not BR1; Atomic 5+ and Abacus trigger flagged verify).
- v1.0 (2026-09-25): Initial 6-pager for the Cryptek 1000 play pack — same headings as the Space Marines 1000 guide (pieces, deployment, command script, Primaries, toolkit, battle plan, Doomstalker lanes / Heavy / Blast / Overwatch in place of the Whirlwind indirect-fire section, Battle-shock per unit, weapon keywords, CP spends with timing).

## Attribution

- Project: Wargame_Concierge · Maintainer: Russell Catt
