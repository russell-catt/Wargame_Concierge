<!--
FILE: games/warhammer_40k_11e/armies/space_marines/Gladius_Task_Force.md
VERSION: v0.5.0 (2026-08-18)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, slice S5)

DOCUMENT_TYPE: Teaching Guide / Detachment
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: Warhammer 40,000 - 11th Edition
FACTION: Space Marines
DETACHMENT: Gladius Task Force
REFERENCE_STATUS: Active - detachment rule and stratagems cross-checked 2026-08-16. Errata and FAQ from the owned faction pack v1.1; full detachment text from public 11e references, because the owned pack carries only this detachment's updates

SOURCES:
  - C:\Personal\40K\rules\eng_22-07_warhammer_40,000_faction_pack_space_marines.pdf (v1.1; Rules Updates and FAQs read 2026-08-16) - Gladius errata, and the Combat Doctrine wording confirmed via the Blade of Ultramar detachment printed in full in the same pack
  - C:\Personal\40K\rules\Warhammer 40,000_ Munitorum Field Manual_Marines.pdf (v1.2, printed 13 Aug 2026; read 2026-08-16) - detachment tag and every enhancement cost
  - https://www.40k.app/factions/space-marines/detachments/gladius-task-force (retrieved 2026-08-16) - full stratagem and enhancement text
  - https://www.newrecruit.eu/wiki/wh40k-11e (Gladius Task Force entry, retrieved 2026-08-16) - detachment rule wording cross-check

PURPOSE:
  Teach Combat Doctrines as a spending decision - three once-per-battle
  resources and when to burn each - rather than as a restatement of the rule.

PRIMARY_AUDIENCE:
  - A first-time Space Marine player who has read Oath_of_Moment.md
  - Anyone deciding whether to spend a doctrine this round or hold it

UPDATE_TRIGGER:
  Update when a faction pack revision, balance dataslate, or FAQ changes a
  doctrine, a stratagem, or an enhancement cost.
-->

# Gladius Task Force - Combat Doctrines

The Gladius Task Force is the generalist Space Marine detachment and the right one to learn on. It has no gimmick to build a list around. It gives you **three once-per-battle permission slips**, and the whole skill of the detachment is knowing which turn to spend each one.

**Munitorum Field Manual v1.2 tags it `GLADIUS TASK FORCE - 3DP - PRIORITY ASSETS`**, read 2026-08-16. See the note on `DP` at the bottom of this page.

---

## The detachment rule, in plain terms

At the **start of your Command phase** you may select one Combat Doctrine. It is active for **every** Adeptus Astartes unit in your army until the start of your next Command phase. **You can select each Combat Doctrine only once per battle.**

| Doctrine | What it permits |
|----------|-----------------|
| **Devastator Doctrine** | Your units may **shoot in a turn in which they Advanced** |
| **Tactical Doctrine** | Your units may **shoot and declare a charge in a turn in which they Fell Back** |
| **Assault Doctrine** | Your units may **declare a charge in a turn in which they Advanced** |

Three doctrines, one battle, one use each. Over a five-round game that means **two rounds with no doctrine at all**, and choosing which two is a real decision.

Notice what these actually are: each one deletes a *penalty* the Movement phase would otherwise charge you. None of them adds damage. Gladius does not make your army hit harder - it makes your army stop paying for moving.

---

## When to spend each one

This is the part that matters, so read it before your first game rather than during it.

### Devastator Doctrine - "I need to be somewhere else and still shoot"

**Spend it when:** you have lost the opening positioning, or the objectives are further away than your Move characteristic, and a turn of standing still would cost you the game. Advancing adds a D6 to every unit's move and normally costs you the whole Shooting phase. This makes that free.

**Typical turn:** battle round one or two, pushing out of your deployment zone onto the midboard objectives with the guns still firing.

**Do not spend it** on a turn when everything is already in range and nothing needs to move. That is the classic beginner waste - burning a doctrine for a 4" reposition you did not need.

### Tactical Doctrine - "I am stuck in a fight I do not want"

**Spend it when:** a unit you need is tangled in melee with something it cannot kill. Falling Back normally costs you shooting *and* charging. This gives both back, so a squad can walk out of a combat, shoot the thing it was fighting, and charge something better.

**Typical turn:** mid-game, round three or four, when your opponent has pinned your shooting units to stop them shooting.

**The trap:** this is the doctrine people save until it is too late. If your Hellblasters spend two turns locked in combat while you wait for a better moment, the doctrine did nothing. Spend it the turn the problem appears.

### Assault Doctrine - "I need to reach them this turn"

**Spend it when:** you want a charge that is out of reach. Advance plus a 2D6 charge is an enormous threat range, and it turns a slow melee unit into something that can cross the board in one turn.

**Typical turn:** the turn you commit. Usually round three or four, after your opponent has been softened and before the game runs out.

**The trap:** advancing then charging is two dice rolls stacked. It is a swing, not a plan. Use it when a failed charge is survivable, not when it is your whole turn.

### The default plan for a first game

Devastator round one or two to get onto the board. Assault the turn you commit your melee squad. Tactical held in reserve for the first time something gets stuck - and spent immediately when that happens, not hoarded.

**Skipping a doctrine is allowed and often correct.** You do not have to pick one. If nothing needs a doctrine this round, keep it.

---

## Once-per-battle reminders

Write these three on the top of your army list and cross them off as you spend them. This is the whole bookkeeping burden of the detachment.

- [ ] **Devastator Doctrine** - spent on round ____
- [ ] **Tactical Doctrine** - spent on round ____
- [ ] **Assault Doctrine** - spent on round ____

Three further things it is easy to get wrong:

| Trap | What is actually true |
|------|----------------------|
| "I'll just re-use Devastator next turn" | You cannot. Each doctrine is **once per battle**, full stop |
| "The doctrine is on my Captain's unit" | No - a selected doctrine applies to **your whole army**, every Adeptus Astartes unit |
| "It lasts for the round" | It lasts until the **start of your next Command phase**, so it also covers your opponent's turn. Rarely relevant, but it is why Tactical Doctrine helps a unit that gets charged |

---

## Stratagems, and how they bend the once-per-battle limit

Six stratagems. You do not need to memorise them for a first game, but two of them exist specifically to work around the once-per-battle restriction, and those are worth knowing on day one.

| Stratagem | CP | The short version |
|-----------|----|-------------------|
| **Adaptive Strategy** | 1 | Command phase. Puts **one unit** into a doctrine of your choice, **even one you have already used this battle** |
| **Squad Tactics** | 1 | Reactive move of D6" when an enemy finishes moving nearby - a full 6" instead if that unit is under **Tactical Doctrine** |
| **Storm of Fire** | 1 | Shooting phase. Your unit's ranged weapons gain `[IGNORES COVER]` - and improve AP by 1 as well under **Devastator Doctrine** |
| **Honour the Chapter** | 1 | Fight phase. Melee weapons gain `[LANCE]` - and improve AP by 1 as well under **Assault Doctrine** |
| **Armour of Contempt** | 1 | Defensive. Worsens the AP of every attack targeting your unit by 1 |
| **Only in Death Does Duty End** | 2 | Fight phase. Models destroyed before they swung still get to fight before being removed |

Two patterns to notice:

- **Adaptive Strategy is the pressure valve.** One unit, one doctrine, ignores the once-per-battle limit. It is why hoarding a doctrine is usually wrong - if you desperately need Tactical Doctrine again on turn five, you can buy it for a single unit for 1CP.
- **Three stratagems get better under a matching doctrine.** Storm of Fire wants Devastator, Honour the Chapter wants Assault, Squad Tactics wants Tactical. Once you are comfortable, the doctrine you pick should be the one that makes your planned stratagem hit harder.

**The faction pack's FAQ settles one question directly:** *Adaptive Strategy does not require a Combat Doctrine to be active for your army.* You can use it on a round when you selected nothing.

---

## Errata carried in from the owned faction pack

Your own pack v1.1 changes three Gladius entries. Public references and older printings may not match, so these win:

| Entry | Change |
|-------|--------|
| **Storm of Fire** | Target is now any Adeptus Astartes unit that has not been selected to shoot this phase |
| **Squad Tactics** | The trigger range drops from 9" to **8"** |
| **Fire Discipline** (enhancement) | Rewritten: the bearer's unit gains `[SUSTAINED HITS 1]`, and re-rolls Advance rolls while under the Devastator Doctrine |
| **Armour of Contempt** | Reworded across seven detachments including this one - the AP penalty now lasts until the attacking unit has finished all of its attacks |

**Read your own pack's Rules Updates section before a game.** It is short, it is near the back, and it is the reason a printed Codex page can be wrong.

---

## Enhancements

Points from Munitorum Field Manual v1.2, read 2026-08-16. All four are worth knowing; none are worth buying at 250 points.

| Enhancement | MFM v1.2 | What it does, in short |
|-------------|----------|------------------------|
| **The Honour Vehement** | **15** | +1 Attacks and Strength on the bearer's melee weapons; **+2 instead** under the Assault Doctrine |
| **Adept of the Codex** | **20** | Captain only. Puts the bearer's unit into **Tactical Doctrine** even if the army has already used it |
| **Artificer Armour** | **20** | 2+ save and Feel No Pain 5+ on the bearer. Pure durability |
| **Fire Discipline** | **25** | The bearer's unit gains `[SUSTAINED HITS 1]`; re-roll Advance rolls under the Devastator Doctrine |

**For a learning list:** take none at 250 points - the points are better spent on a whole extra squad. At 500, **Fire Discipline** on a Captain leading a shooting squad is the easiest one to understand and use, because its benefit fires every single Shooting phase without you having to remember anything.

**How many enhancements you are allowed** is not stated in any PDF this project owns. Muster the list in the Warhammer 40,000 app, or agree the limit with your opponent for a friendly game.

---

## What `3DP` means, honestly

The Munitorum Field Manual tags every detachment with a number and a mission type - `GLADIUS TASK FORCE 3DP PRIORITY ASSETS`. The mission-type half is real, documented vocabulary: Take and Hold, Purge the Foe, Disruption, Reconnaissance and Priority Assets are the Primary Missions selected during setup.

**What `DP` expands to is not stated in any document this project owns.** It does not appear in the Core Rules, the Event Companion, or either faction pack - only in the MFM detachment table. S4 reached the same conclusion for Necrons and this slice confirms it independently for Space Marines. It is almost certainly the origin of the phrase "Data Package Detachment" in older owner notes, but that phrase is not a rules term and should not be used.

---

## Related pages

- [`Oath_of_Moment.md`](Oath_of_Moment.md) - the army rule that runs underneath this detachment
- [`Starter_250.md`](Starter_250.md) - the learning list built for these doctrines
- [`Starter_500.md`](Starter_500.md) - where enhancements start to be worth their points
- [`Quick_Reference_Play_Guide.md`](Quick_Reference_Play_Guide.md) - the laminate version of the doctrine cheat sheet
- [`../../rules/Turn_Structure.md`](../../rules/Turn_Structure.md) - Advance, Fall Back, and what they normally cost
- [`../../rules/Keyword_Glossary.md`](../../rules/Keyword_Glossary.md) - detachment, stratagem, enhancement, `[LANCE]`, `[SUSTAINED HITS X]`

---

## Change Log
- v0.5.0 (2026-08-18): Project-wide semver snapshot (x.y.z).
- v1.0 (2026-08-16): Initial detachment teaching guide (slice S5). Doctrine wording cross-checked against the Blade of Ultramar detachment printed in full in the owned faction pack v1.1, which uses identical Combat Doctrine text; stratagems and enhancements from public 11e references retrieved 2026-08-16 and reconciled against the owned pack's Gladius errata. Enhancement costs from MFM Marines v1.2. Upgrades the `unverified` Gladius Task Force entry in `Keyword_Glossary.md`.

## Attribution
- Project: Wargame_Concierge
- Maintainer: Russell Catt
- Warhammer 40,000 is a trademark of Games Workshop Limited. This document is a personal teaching paraphrase and reproduces no publisher text or statlines.

## Rising Tide Notes
- This document follows Rising Tide documentation standards.
- **Verify before you play.** Cross-check anything here against the current Munitorum Field Manual and your faction pack - Games Workshop patches rules and points between publications. Content on this page reflects sources read on **2026-08-16**.
