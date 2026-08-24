<!--
FILE: games/the_warcode/rules/Contracts_and_VP.md
VERSION: v0.1 (2026-08-23)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, warcode_tactical_doctrine)

DOCUMENT_TYPE: Deep Dive / Teaching Guide
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: The Warcode
REFERENCE_STATUS: Active — draft, beta v0.8.7-F (2026-08-23)

SOURCES:
  - raw/the_warcode/The Warcode Rulebook V.0.8.7-F.pdf (free public beta, RedMakers; retrieved 2026-08-23)
  - raw/the_warcode/rulebook_v087f_extract.txt

PURPOSE:
  Deep-dive on scoring: how VP tokens are captured and contested, how the
  Contract catch-up mechanic works, and how re-roll points fit into the same
  economy of falling behind.

PRIMARY_AUDIENCE:
  - A player working out how to actually win rather than just kill things
  - A player who has just fallen behind and drawn their first contract

KEY_SECTIONS_EXPECTED:
  - How VP is scored
  - Contesting
  - Random VP placement
  - Contracts: trigger, draw, fulfilment
  - Re-roll points as the other catch-up valve
  - Playing from ahead and behind

UPDATE_TRIGGER:
  A newer free beta changes VP capture radius, contest rules, the contract
  trigger threshold, or re-roll point income.
-->

# Contracts and VP — how you actually win

Killing models is not the win condition. Holding ground at the right moment is. **`confidence: draft`**, beta **v0.8.7-F**, read **2026-08-23**. Full wording: [`Rulebook_Quotes.md`](Rulebook_Quotes.md).

---

## Scoring VP

> Victory Points (VP) are earned by capturing points on the map and completing contracts. At the end of the game, the player with the most VP wins.
>
> VP tokens indicate the number of VP a player receives at the end of a round.
>
> To capture a VP, a unit must be within 1 inch of the VP token with no enemy units in that radius. If both allied and enemy units are present within this radius at the end of the round, the point becomes contested, and no player receives VP from it.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.4 — "VICTORY POINTS (VP)"

Three things are doing work in that paragraph.

**The radius is 1 inch.** That is tiny — roughly one base width. You are not holding an area, you are standing on a specific spot, and there is no room to spread out and still count. It also means a single enemy model reaching that same inch cancels the whole thing.

**Scoring happens at end of round only.** Nothing you did during the Tactical Phase banks any points. What matters is the board state after the last activation, which means the player activating **last** in a round has the final word on every objective — and the initiative winner, who acts first, gives that away. Winning initiative is genuinely double-edged in a scoring round.

**Tokens carry different values.** The rules say tokens "indicate the number of VP a player receives," so they are not uniform. Read them before you commit models; a contested 1 VP token is a cheaper trade than a held 2.

---

## Contesting is the cheap play

> If both allied and enemy units are present within this radius at the end of the round, the point becomes contested, and no player receives VP from it.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.4 — "VICTORY POINTS (VP)"

Contesting is strictly easier than capturing, and it is symmetrical — one model inside the inch cancels any number of enemy models. That asymmetry of effort is the core tension of the game. Denying a point costs you one model's activation; holding it costs you a model that has to survive there.

Two consequences worth planning around. First, a fast model is worth more than its profile suggests: Phantom and Reaper at **7 inches** can reach and contest objectives that slower models cannot threaten, and they do not need to win a fight to do it. Second, **melee shuts contesting down** — a model in an enemy's melee radius can only fight or leave, and if it is in Melee Lock it needs a roll to leave at all. Locking an enemy model 3 inches from an objective is as good as killing it for scoring purposes, and cheaper.

The end-of-round timing means the contest fight is really an **activation-order fight**. If your opponent puts a model on a point early in the round, you have the rest of the round to answer. If they do it with their last activation, you do not.

---

## Where the points are

> The random VP placement system applies to all scenarios. Before the game begins, roll one D6. The result determines the VP placement for that game. The diagrams below use the scenario "Core of the Machine" as an example. BOARD SIZE 33'' X 24''
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.27 — "RANDOM VP PLACEMENT"

Objective placement is rolled, not chosen, and it is rolled **before the game begins** — which by the setup order means before deployment. So you deploy knowing where the points are, and both players get that information at the same time. There is no scouting phase and no hidden objective placement.

Six layouts on a 33" × 24" board is a meaningful spread. Some rolls will put points deep in one side's half, some will string them across the middle. Since you also distribute equipment after deployment, the full pre-game information order is: **roll VP placement → roll initiative → deploy alternately → buy equipment**. Each step gives you more to react to than the last, so hold your flexible decisions for the end of it.

---

## Contracts — the catch-up valve

> If the difference in VP between players is 1 or more at the end of any round, the player with the lower VP receives a contract.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.22 — "CONTRACTS"

The trigger is **1 or more**, which is to say: any deficit at all. This is not a comeback mechanic for players getting crushed — it fires the moment you are behind by a single point, every round it stays true. Expect contracts to be in play for most of a normal game.

> That player draws one contract card and looks at it secretly. The card specifies one unit name from each available faction, and the Target is the unit from the faction the opponent is playing. If that unit is already dead, the player shows the card to the opponent, places it at the bottom of the deck, and draws another.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.22 — "CONTRACTS"

The card lists one named unit **per faction**, and which name applies depends on who you are playing against — so the same physical card is a different assassination order in every matchup. You read it **secretly**, which is the only hidden information in the game. Your opponent knows you have a contract (the VP totals are public) but not who it names, so they have to protect the whole squad or guess.

The already-dead clause is a small but real anti-feelbad rule: if the named model is gone, you reveal, bottom the card, and draw again. You cannot be handed a dead contract, and revealing it tells your opponent one name you are *not* hunting.

> A contract is fulfilled once the Target is eliminated, whether by the player, by scenario events, or by any other means. The player announces it, shows the card to the opponent, adds the VP specified on the card to their score, and discards it.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.22 — "CONTRACTS"

**"By any other means"** is the generous part. You do not have to land the kill. A Protocol Card's poison gas, a turret, your opponent's own grenade catching their model — all of it counts. On the «Core of the Machine» map, where end-of-round protocols deal 2–3 damage to whole rooms, contracts can and will complete themselves.

The worked example fixes the scale:

> EXAMPLE: At the end of round 2, Player A has 2 VP and Player B has 3 VP. Before the start of round 3, Player A receives one contract. Player B is playing the Ulfari, so Player A's Target is the unit Shade. If Shade is eliminated by Player A or by any other means, Player A gains 1 VP.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.22 — "OBJECTIVES OF THE CONTRACT"

One VP for a kill, against a one-point deficit — so a contract is worth roughly one objective-round. That is the right calibration to notice: **a contract is a bonus, not a plan**. Chasing a named model across the board while your opponent quietly holds two objectives is how you lose by more than you started behind.

The text says contracts accumulate — you receive one at the end of *any* round where you trail, and fulfilment is per-card. Nothing in the extract caps how many you can hold at once.

### Playing around contracts

If you are **ahead**, you know your opponent is hunting one of your models and you do not know which. Two habits help: keep no model isolated where a single activation can finish it, and remember that a model at low HP is a walking VP donation — heal it, screen it, or pull it back. Note also that leading by exactly 1 VP is the worst place to be, since it hands over a contract for the smallest possible advantage.

If you are **behind**, treat the contract as opportunistic. Take the kill when the target is already exposed or already damaged; do not redirect your whole squad for it. And check the protocol effects each round — sometimes the map is about to kill your target for you.

---

## Re-roll points are the other catch-up valve

> Re-roll points come from two sources. A player whose Leader is alive gains 2 re-roll points at the start of each round, and stops gaining them once that unit is killed. A player also gains 1 point immediately each time one of their own units is killed.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.23 — "RE-ROLL"

Losing models pays you. **Every friendly casualty is +1 re-roll point**, immediately, which means the player getting shot to pieces accumulates the dice-fixing resource. Combined with contracts, the game has two independent rubber bands: fall behind on points and you get assassination targets; lose models and you get re-rolls.

The Leader income is the counterweight and the reason Leaders are worth protecting beyond their statlines. **Commander Rickman** (9 HP, Volt Sword) and **Soul Eater** (9 HP, Razor Blade) each generate **2 points per round** while alive — over a four-round game that is up to 8 re-rolls, easily the largest single resource in the game. Killing an enemy Leader in round 1 does not just remove a good model, it turns off their economy for the rest of the match.

Two restrictions bound the resource:

> Re-roll points cannot be spent on the initiative roll, which decides who goes first in the round, or on event cards that call for a roll.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.23 — "RE-ROLL"

You cannot buy initiative and you cannot dodge a Protocol Card's D6. The Electricity protocol's 3-or-less check is genuinely random and there is nothing you can do about it but leave the room.

---

## Playing the scoreboard

| Position | What the rules give you | What to do about it |
|----------|-------------------------|---------------------|
| **Ahead by 1+** | Nothing; opponent draws a contract | Protect wounded models; consider whether a 1 VP lead is worth handing over a contract |
| **Behind by 1+** | A contract each round | Score first, assassinate opportunistically |
| **Losing models** | +1 re-roll point per casualty | Spend them; hoarding re-rolls into a loss is wasted resource |
| **Leader alive** | +2 re-roll points per round | Keep the Leader out of the first exchange |
| **Leader dead** | Income stops | Your remaining points are finite — spend on decisive rolls only |
| **Tied at end** | Depends on scenario | «Core of the Machine» kills **both** teams on a tie — a draw is a loss |

That last row is worth its own note. The printed scenario has no draw:

> If both teams have the same number of VP at the end of the game, everyone perishes as the "core" marks everyone as "hostile" and destroys them.
>
> Source: The Warcode Rulebook V.0.8.7-F.pdf — p.26 — "SCENARIO «CORE OF THE MACHINE»"

In the final round, a tie is the worst outcome for both players, which makes contesting in the last round a losing move if you are level. Someone has to break the tie, and if it is going to be one of you, make it you.

---

## Related pages

- [`Turn_Structure.md`](Turn_Structure.md) — where VP calculation sits in the end-of-round order
- [`Scenarios_and_Events.md`](Scenarios_and_Events.md) — the scenario's own victory conditions and Protocol Cards
- [`Combat_Ranged_and_Melee.md`](Combat_Ranged_and_Melee.md) — how re-rolls apply in a fight
- [`Activation_and_AP.md`](Activation_and_AP.md) — activation order and who gets the last word
- [`Rulebook_Quotes.md`](Rulebook_Quotes.md) — verbatim VP, contract and re-roll text
- [`../setup/Board_Setup.md`](../setup/Board_Setup.md) — VP token placement

---

## Open questions

- **Contract card VP values** — the p.22 example shows 1 VP, but the contract card pages (PDF pp.24–25) are art with no text layer and have not been OCR'd. Other cards may be worth more.
- Whether a player can hold **multiple unfulfilled contracts** at once, and whether they draw one per qualifying round indefinitely.
- Whether a contract persists to the end of the game or expires when the player catches up on VP.
- Whether contract VP counts toward the *next* round's contract-trigger comparison immediately.
- Default **round count** — the scenario references "the final round" and a countdown, but no number appears in the extracted text.
- Whether all VP tokens are worth the same in the printed scenario, or vary by position.

---

## Change Log

- v0.1 (2026-08-23): Initial VP, contracts and re-roll deep-dive from beta v0.8.7-F extract.

## Attribution

- Project: Wargame_Concierge
- Maintainer: Russell Catt
- The Warcode is property of RedMakers. Unofficial, unauthorized personal learning notes — never for sale.

## Rising Tide Notes

- This document follows Rising Tide documentation standards.
- One inch, end of round, no enemy in it. That is the whole scoring rule.
