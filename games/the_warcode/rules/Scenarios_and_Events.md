<!--
FILE: games/the_warcode/rules/Scenarios_and_Events.md
VERSION: v0.2 (2026-08-25)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, warcode_tactical_doctrine)

DOCUMENT_TYPE: Deep Dive / Teaching Guide
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: The Warcode
REFERENCE_STATUS: Active — draft, beta v0.8.7-F (2026-08-23)

SOURCES:
  - raw/the_warcode/The Warcode Rulebook V.0.8.7-F.pdf (free public beta, RedMakers; retrieved 2026-08-23)
  - raw/the_warcode/rulebook_v087f_extract.txt
  - raw/the_warcode/protocol_cards.ocr.txt (via OCR)
  - raw/the_warcode/protocol_cards_transcription.txt (via typed transcription, 2026-08-25)
  - raw/the_warcode/images/Core_Machine_placement.png (map topology, 2026-08-25)
  - raw/the_warcode/images/Core_Machine_obj_placement.png (D6 VP layouts, 2026-08-25)

PURPOSE:
  Deep-dive on the scenario layer: «Core of the Machine», random VP placement,
  and the Protocol Card deck that punishes standing still in the wrong room.

PRIMARY_AUDIENCE:
  - A player setting up the printed scenario for the first time
  - A player deciding whether to hold a room a protocol just poisoned

KEY_SECTIONS_EXPECTED:
  - Where scenario effects fire in the round
  - «Core of the Machine» premise and victory conditions
  - Random VP placement
  - Protocol Cards, room and Total versions
  - Playing around the protocols
  - Known OCR gaps

UPDATE_TRIGGER:
  A newer free beta adds scenarios, changes protocol effects, or a cleaner OCR
  pass replaces the card transcriptions.
-->

# Scenarios and events

The scenario is not flavour text — it sets the victory conditions, and on the printed map it also tries to kill you. **`confidence: draft`**, beta **v0.8.7-F**, read **2026-08-23**. Protocol Card text is **via OCR**. Full wording: [`Rulebook_Quotes.md`](Rulebook_Quotes.md).

---

## Read the scenario first

> READ THE SCENARIO — It sets out your objectives, the victory conditions, and any special rules.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.2 — "SETUP"

Step one of setup, before deployment and before equipment. The scenario owns the objectives, the victory conditions, the round count and any special rules, which means the core rulebook deliberately leaves those blanks for it to fill. Do not assume anything about how the game ends until you have read the mission.

Scenario effects have a fixed slot in the round:

> END OF THE ROUND: After the Tactical Phase, apply all unit effects that activate at the end of the round, then apply scenario effects (if any), and calculate Victory Points (VP).
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.3 — "END OF THE ROUND"

The order is **unit abilities → scenario effects → VP calculation**, and that sequence has teeth. A protocol that deals damage at end of round resolves **before** scoring, so a model holding an objective can be killed by the room it is standing in and score nothing for the round it died in. Holding a point through a hostile protocol is a real gamble, not a formality.

---

## «Core of the Machine»

> The action takes place inside a long-abandoned and heavily damaged space drifter. Your mission is to infiltrate and take full control of the ship. As soon as your team reaches the machine's core, it activates security protocols. However, due to severe damage, the machine cannot distinguish between friend and foe. You also discover that you are not alone. A countdown begins, and there isn't enough time to escape the ship. You need to reprogram the "core" to mark your team as "friendly" and the opposing team as "hostile," thereby activating automatic turrets to eliminate the enemy. If neither team succeeds in persuading the "core", both teams will be marked as "hostile" and will be destroyed when the time runs out.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.26 — "SCENARIO «CORE OF THE MACHINE»"

The fiction does real mechanical work here, which is unusual and worth noticing. "The machine cannot distinguish between friend and foe" is the in-world justification for Protocol Cards hitting **both** squads, and "a countdown begins" is why the game is finite and why a tie is fatal. This is the only scenario printed in the beta.

The map is three rooms connected by doors, on a **33" × 24"** board:

> Deployment area - A
> Deployment area - B
> - Partial cover
> - Full Cover (Wall)
> - Door
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.26 — "SCENARIO «CORE OF THE MACHINE»"

Three rooms is the number that matters, because the Protocol deck targets rooms. Every model on the board is always inside a protocol's potential blast area, and doors decide how fast you can leave one.

### Core of the Machine — map topology

Terrain reference: [`raw/the_warcode/images/Core_Machine_placement.png`](../../../raw/the_warcode/images/Core_Machine_placement.png). VP coordinates: [`../setup/Board_Setup.md`](../setup/Board_Setup.md#d6-coordinate-tables-core-of-the-machine).

| Feature | Detail |
|---------|--------|
| **Board** | **33" × 24"** playing surface |
| **Deployment area A** | Top band — one player's deployment zone |
| **Deployment area B** | Bottom band — opposite deployment zone |
| **Left wing** | Open rectangular room left of the hex; partial-cover **L** barriers and a dashed objective circle |
| **Centre (hex)** | Central hexagonal room — the machine **core** (solid circle at hex centre); partial cover links core to the hex's right wall |
| **Right wing** | Open rectangular room right of the hex; **T-shaped** partial cover with a small circle at the junction |
| **Doors** | **10** doorways total — **six** on the hex perimeter (one per hex face) and **four** on the diagonal full-cover walls that separate deployment zones from the side wings |
| **Cover legend** | **Partial cover** = dashed double line; **full cover (wall)** = solid thick line; **door** = quarter-circle swing arc |

Protocol Cards name their target room on the card face — a **map diagram** with **Left**, **Centre**, or **Right** **lit** (or **all three** on **Total** cards). **Deployment bands** (top and bottom) are **never** lit and are **not** protocol-affected. There is no separate room roll — see [Protocol room targeting](#protocol-room-targeting) below.

### Victory conditions

> Victory Conditions:
>
> 1. Eliminate all enemy units.
> 2. Accumulate more VP than the opponent to sway the "Core of the machine" to your side.
>
> If both teams have the same number of VP at the end of the game, everyone perishes as the "core" marks everyone as "hostile" and destroys them.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.26 — "SCENARIO «CORE OF THE MACHINE»"

Two routes to a win and **no draw**. Wiping the enemy squad is theoretically available but slow against eight models on a board with this much cover; VP is the realistic path.

The tie clause is the design decision that shapes late-game play. A level score at the end is a mutual loss, so **contesting is not a safe default in the final round**. If you are tied going into the last round, you must break the tie — sitting on a contested objective to preserve parity destroys you both. That inverts the usual endgame instinct, where denying the leader is a reasonable draw-hunting play. Here there is nothing to hunt.

Combined with the contract rules, the incentive gradient is unusual: being **behind** gets you a contract, being **level** gets you killed, and being **ahead by one** gets your opponent a contract. There is no comfortable position on this map except a clear lead.

---

## Random VP placement

> The random VP placement system applies to all scenarios. Before the game begins, roll one D6. The result determines the VP placement for that game. The diagrams below use the scenario "Core of the Machine" as an example. BOARD SIZE 33'' X 24''
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.27 — "RANDOM VP PLACEMENT"

One D6 before the game selects one of six printed layouts, each showing both deployment areas. This is described as a **universal system**, not a scenario feature, so expect it to apply to future missions too.

Rolling placement before deployment means both players see the objective spread and then place models alternately against it. There is no ambush value in objective placement and no way to skew the map toward your squad — the randomness is symmetrical, and the skill is in reacting to it during deployment.

**Full D6 tables with inch coordinates** for *Core of the Machine* are in [`../setup/Board_Setup.md`](../setup/Board_Setup.md#vp-token-placement). Source diagram: [`raw/the_warcode/images/Core_Machine_obj_placement.png`](../../../raw/the_warcode/images/Core_Machine_obj_placement.png).

| D6 | Tokens | Summary |
|----|--------|---------|
| 1–3 | 3 | Left **3"**, hex centre (**14"** from left-wing wall), right **3"** — identical rolls |
| 4 | 4 | Wings as above + hex vertical pair (**8"** from each deployment boundary) |
| 5 | 5 | Wing corner pairs (**2.5"** / **7.5"**) + hex centre token |
| 6 | 6 | Roll-5 wing pairs + hex pair (**6"** offsets) + right-wing pair from **board edge** |

---

## Protocol Cards

> CORE OF THE MACHINE: At the start of each round, draw a random "Core of the Machine" activation card with negative effects for one or more of the three rooms (effect descriptions are on the card).
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.26 — "SCENARIO «CORE OF THE MACHINE»"

One card per round, drawn at the **start** of the round — before initiative, before anyone moves. So you always know what the map is about to do to you before you spend a single AP. That is a deliberate design choice: protocols are a planning constraint, not a random punishment.

Most effects then resolve at the **end** of the round, in the scenario-effects slot before VP calculation. The full round shape on this map is therefore: **draw protocol → initiative → activate everything → protocol resolves → score**.

### Protocol room targeting

Each printed card shows a **mini map** of the *Core of the Machine* layout:

| Zone on card | Meaning |
|--------------|---------|
| **Top / bottom bands** | **Deployment areas A and B** — never highlighted; protocols **do not** affect these zones |
| **Left wing lit** | Left rectangular room only |
| **Centre (hex) lit** | Central hexagonal room only |
| **Right wing lit** | Right rectangular room only |
| **All three wings lit** | **Total** protocol — left, centre, and right rooms together |

The **Map section** column in [`Protocol_Cards_Reference.md`](Protocol_Cards_Reference.md) matches the highlighted zone(s). **No second roll** picks the room — read the graphic on the card you drew.

| Question | Answer in v0.8.7-F |
|----------|-------------------|
| **Which room is hit?** | **Whichever zone(s) are lit** on the card — Left, Centre, Right, or all three (Total). |
| **Are deployment zones affected?** | **No** — top/bottom deployment bands are outside protocol scope. |
| **How is a card chosen?** | Scenario text: draw one random activation card each round. **Silent** on deck shuffle, exhaustion, and replacement. |
| **Where are room boundaries?** | Left wing, central hex, and right wing on the scenario map — see [map topology](#core-of-the-machine--map-topology). Models in doorways need a table agreement until FAQ. |

The rulebook extract does **not** spell out the **highlighted-map** convention in prose — the cards carry it visually. Agree at setup how doorways and deployment-edge models count as "in the room."

The beta deck has **five** effect families × **four** scopes = **20** cards — full table in [`Protocol_Cards_Reference.md`](Protocol_Cards_Reference.md).

The rulebook extract does **not** define how to randomise among the twenty cards (full shuffle vs subset vs with replacement). Agree at setup and log it as a beta teaching gap.

The deck comes in matched scopes — a **room** version affecting one wing, and a **Total** version affecting all three protocol rooms (all lit on the card map). Five effect families:

| Protocol | Scope | Effect | Timing |
|----------|-------|--------|--------|
| **Magnet** | One room / Total | −3" movement for units starting movement there | Continuous |
| **Hunt** | One room / Total | 3 damage to units **at full health** | End of round |
| **Electricity** | One room / Total | D6 per unit; **3 or less** takes 3 damage | End of round |
| **Poison** | One room / Total | 2 damage to **all** units | End of round |
| **Silence** | One room / Total | No ranged weapons at all | Continuous |

All card text below is **via OCR** from [`protocol_cards.ocr.txt`](../../../raw/the_warcode/protocol_cards.ocr.txt); the PDF pages are card art with no extractable text layer.

### Magnet

> THE FLOOR IN THE ROOM BECOMES HEAVILY MAGNETIZED. MOVEMENT BECOMES DIFFICULT.
>
> ALL UNITS THAT START THEIR MOVEMENT IN THIS ROOM SUFFER A -3 INCH PENALTY TO THEIR MOVEMENT PROFILE.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — pp.28–32 — "PROTOCOL CARDS" — via OCR (raw/the_warcode/protocol_cards.ocr.txt)

A −3 inch penalty is enormous against Movement Ranges of 5 to 7. A Slow unit like Bastion or Shellshocker is reduced to **2 inches** per AP; a standard unit to 3. Add the friendly-unit penalty and a model can be moving a single inch for a full Action Point.

The trigger is on **starting** movement in the affected room, so a model that gets out is free for the rest of its move — but getting out is exactly what costs the 3 inches. Total Magnet effectively pins the whole board in place for a round, which turns it into a shooting round and rewards whoever already has firing lanes.

### Hunt

> TURRETS ACTIVATE THROUGHOUT THE ROOM. TARGET ACQUISITION BEGINS.
>
> AT THE END OF THE ROUND, ALL UNITS IN THE ROOM WITH FULL HEALTH TAKE 3 DAMAGE.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — pp.28–32 — "PROTOCOL CARDS" — via OCR (raw/the_warcode/protocol_cards.ocr.txt)

The strangest card in the deck: it hits **only undamaged models**. Turrets acquire healthy targets, so the fresh reserve you were holding back takes 3 and your walking wounded are ignored.

That inverts normal caution. Against Hunt, your **untouched** models are the ones in danger, and a model on 5 of 8 HP is safer standing in the turret room than a model on 8 of 8. It also means a grenade of your own, or a medkit *not* used, can change who gets hit — and that healing a model back to maximum HP puts it back on the target list.

Three damage on 8 HP models is a heavy tax across a whole room, and Total Hunt hits every full-health model on the board at once. Round 1 Total Hunt, when nothing has been damaged yet, would strike the entire game.

### Electricity

> ELECTRICAL PULSES START COURSING THROUGH THE ROOM. IT TAKES GREAT EFFORT TO DODGE THE ELECTRICAL SHOCKS.
>
> AT THE END OF THE ROUND, ROLL ONE D6 FOR EACH UNIT IN THE ROOM. IF THE RESULT IS 3 OR LESS, THE UNIT TAKES 3 DAMAGE.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — pp.28–32 — "PROTOCOL CARDS" — via OCR (raw/the_warcode/protocol_cards.ocr.txt)

A coin flip per model for 3 damage, and there is no way to improve it — re-roll points explicitly cannot be spent on event card rolls. Agility and Armor are both irrelevant here, so this is the one effect that treats a Reaper and a Bastion identically.

Half of everything in the room taking 3 damage is, in expectation, the most destructive card in the deck across a crowded room. It also has a quiet interaction with Hunt: Electricity damage strips models out of "full health", so a room that got shocked last round is a room the turrets will largely ignore.

### Poison

> CAUSTIC GAS BEGINS TO SEEP THROUGHOUT THE ROOM. NO RESPIRATORY PROTECTION SYSTEM CAN PROVIDE COMPLETE SAFETY. POISONING IS INEVITABLE.
>
> AT THE END OF THE ROUND, ALL UNITS IN THE ROOM TAKE 2 DAMAGE
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — pp.28–32 — "PROTOCOL CARDS" — via OCR (raw/the_warcode/protocol_cards.ocr.txt)

No roll, no condition, no save: everyone in the room loses 2 HP. It is the smallest number in the deck and the most certain, and certainty is what makes it dangerous — you can count exactly which of your wounded models will die at end of round, and so can your opponent.

Since it resolves **before** VP calculation, a model on 2 HP holding an objective in a poisoned room dies and scores nothing. Poison is the card most likely to decide a scoring round.

### Silence

> THE ROOM FILLS WITH UNKNOWN ENERGY. ALL RANGED WEAPONS COMPLETELY FAIL. ALL UNITS IN THE ROOM CANNOT USE RANGED WEAPONS.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — pp.28–32 — "PROTOCOL CARDS" — via OCR (raw/the_warcode/protocol_cards.ocr.txt)

The only protocol that deals no damage, and possibly the most decisive. A silenced room is a melee room. Heavy weapon carriers — Bastion, Doom — become models with a **Fist** (melee strength 1), which is to say nearly harmless. Melee specialists like Blade (Combat Claws, strength 5) and Smasher (Combat Axe with its 1-inch lock) become the best models in the game for a round.

Total Silence turns the entire round into a brawl. If you drew it and you have the melee squad, this is the round to Engage everything.

### The Total variants

Each protocol has a Total version whose flavour text extends it to all rooms. The OCR shows a consistent editing problem:

> ALL ROOMS FILLS [sic] WITH UNKNOWN ENERGY. ALL RANGED WEAPONS COMPLETELY FAIL. ALL UNITS IN THE ROOM CANNOT USE RANGED WEAPONS.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — pp.28–32 — "PROTOCOL CARDS" — via OCR (raw/the_warcode/protocol_cards.ocr.txt)

**On every Total card, the flavour line says "all rooms" but the rule line still says "this room."** This appears on Total Magnet, Total Hunt, Total Electricity, Total Silence and Total Poison alike — the cards were clearly copy-edited from the single-room versions without updating the rule text. Intent is obviously board-wide; the printed wording is not. Agree with your opponent before the game that Total means all three rooms, and log it as a polish item for the beta feedback.

---

## Playing around the protocols

Because the card is drawn at the **start** of the round, every protocol is a planning problem rather than a surprise. Practical habits:

- **Check the room before you commit.** A model that moves onto an objective in a Poison room has signed up for 2 damage before it scores. Sometimes the right play is to take the point next round.
- **Doors are your escape hatch and your cage.** A closed door does not stop a protocol, but door control decides whether a model can reach a different room this activation. Under Magnet, with movement cut to 2–3 inches, a door two inches away is the difference between escaping the room and not.
- **Watch the full-health list under Hunt.** Count which of your models are undamaged; those are the ones the turrets want. Fresh reserves are liabilities that round.
- **Silence rounds are Engage rounds.** If your ranged models are switched off, the AP is better spent closing distance than repositioning.
- **Protocols can complete your contract.** "Eliminated by any other means" includes the map. If your contract target is sitting in a poisoned room on low HP, you may not need to do anything at all.
- **Do not count on re-rolls.** Event card rolls cannot be re-rolled, so the Electricity check is genuinely out of your hands.

---

## Known gaps

| Gap | Status |
|-----|--------|
| Protocol Card **page-to-card mapping** | Approximate. Cards are art across PDF pp.28–32; the OCR pass captured text but not per-page assignment. |
| Whether the deck holds **more than five** protocol families | **Resolved for beta** — five families × four map scopes = 20 cards per owner transcription. |
| Whether a protocol persists past the round it was drawn | Not stated. Magnet and Silence read as continuous *within* the round. |
| Which room a card targets | **Resolved** — printed on card (Left / Centre / Right / Total). Full table: [`Protocol_Cards_Reference.md`](Protocol_Cards_Reference.md). |
| **How** the random draw works (shuffle, exhaust, replacement) | **Silent** in extract — table agreement required. |
| **Contract cards** (PDF pp.24–25) | Typed transcription shipped — see [`Contract_Cards_Reference.md`](Contract_Cards_Reference.md). |
| **Round count** | The scenario references a countdown and "the final round" but no number appears in the extracted text. |
| Other scenarios | Only «Core of the Machine» is printed in v0.8.7-F. |
| **D6 VP layout coordinates** | **Resolved** — see [`../setup/Board_Setup.md`](../setup/Board_Setup.md#d6-coordinate-tables-core-of-the-machine). |

---

## Related pages

- [`Turn_Structure.md`](Turn_Structure.md) — where scenario effects sit in the end-of-round order
- [`Contracts_and_VP.md`](Contracts_and_VP.md) — scoring, and why a tie is fatal here
- [`Combat_Ranged_and_Melee.md`](Combat_Ranged_and_Melee.md) — what Silence takes away
- [`Equipment_Loot_and_Doors.md`](Equipment_Loot_and_Doors.md) — door control under Magnet
- [`Rulebook_Quotes.md`](Rulebook_Quotes.md) — verbatim scenario text and the full Protocol Card OCR
- [`Protocol_Cards_Reference.md`](Protocol_Cards_Reference.md) — 20-card Left / Centre / Right / Total table (when present)
- [`../setup/Board_Setup.md`](../setup/Board_Setup.md) — 33" × 24" board, D6 VP coordinates, deployment areas

---

## Open questions

- Do Total protocols apply to all three rooms despite the rule text saying "this room"? Almost certainly yes, but the printed wording does not say so.
- Does a protocol drawn in round *n* expire at the end of round *n*, or stack with later draws?
- Under Hunt, does a model healed back to maximum HP by a medkit count as "full health" at end of round? The wording implies yes.
- Is the protocol deck shuffled and exhausted, or drawn with replacement?
- Does the "eliminate all enemy units" victory condition end the game immediately, or at end of round?
- Are units *outside* all three rooms — in corridors or doorways — exempt from room protocols?

---

## Change Log

- v0.3 (2026-08-25): Protocol scope — card map highlights Left/Centre/Right or Total; deployment zones excluded; Hunt FULL HEALTH confirmed (xlsx error).
- v0.2 (2026-08-25): *Core of the Machine* map topology from `Core_Machine_placement.png`; protocol room targeting (Left/Centre/Right/Total on card; draw procedure silent); D6 VP gap closed — coordinates live in Board_Setup.
- v0.1 (2026-08-23): Initial scenario and Protocol Card deep-dive from beta v0.8.7-F extract plus OCR sidecar. Flagged the Total-card rule-text scope bug.

## Attribution

- Project: Wargame_Concierge
- Maintainer: Russell Catt
- The Warcode is property of RedMakers. Unofficial, unauthorized personal learning notes — never for sale.

## Rising Tide Notes

- This document follows Rising Tide documentation standards.
- The card is drawn before you move. There is no excuse for being surprised.
