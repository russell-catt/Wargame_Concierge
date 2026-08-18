<!--
FILE: docs/Project_Origin_Story.md
VERSION: v0.5.0 (2026-08-18)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, slice S1)

DOCUMENT_TYPE: Reference / Narrative
PROJECT_NAME: Wargame_Concierge
PROJECT_STATUS: Active

SOURCES:
  - reference/Initial_Prompt.md (owner intent, verbatim)
  - docs/Project_Planning.md (confirmed ownership, locked decisions)
  - KB/overview.md (armies in scope)

PURPOSE:
  Explains why this project exists and who it is for, in plain language for
  someone who has never played a tabletop wargame. Written to be the friendly
  door into the repo - no jargon assumed, nothing to look up first.

PRIMARY_AUDIENCE:
  - Complete beginners to tabletop wargaming
  - The son learning the Space Marine force
  - Anyone wondering why the project is shaped the way it is

UPDATE_TRIGGER:
  Update when the motivation, the people involved, or the armies in scope
  change. Not a status document - status lives in Project_Planning.md.
-->

# Project Origin Story

This is the "why" document. No jargon, nothing to look up first. If you have never rolled a die in anger, start here.

---

## The problem

Two people in one house want to play the same game against each other. A parent and a son. Between them they have a box of unassembled robot skeletons, a pile of old power-armoured soldiers from years back, a kitchen table, and no idea how to actually play.

The rules exist. That is not the problem. The problem is that wargame rulebooks are written as **reference material for people who already play**. They tell you precisely what a rule says. They do not tell you why the rule exists, when it decides a game, or which of the three hundred things on the page you actually need on turn one.

So the first game never happens. The models stay in the box.

**This project exists to get to the first game.**

---

## What a tabletop wargame actually is

The two-minute version, for anyone who needs it.

Two players each bring a small army of miniature models. You agree on a size - measured in **points**, so both armies come out roughly even in strength. You set up a table with terrain: ruins, hills, crates, anything that blocks line of sight and gives cover.

Then you take turns. On your turn you move your models, shoot at the enemy, and fight in close combat. Dice decide what happens: roll to see if you hit, roll to see if the hit hurts, and the defender rolls to see if their armour saves them.

Here is the part most beginners get wrong, and the part this project keeps repeating: **you usually do not win by killing everything.** You win by controlling marked points on the table - objectives - at the right moments. A cheap unit standing on the right patch of floor is often worth more than an expensive one winning a fight in the corner. Positioning beats damage.

That single idea reframes almost every decision in the game.

---

## The two armies, and why they were chosen

Neither army was picked for being good. They were picked because they were already in the house.

### The Necrons - the parent's army

Ancient machine-warriors who do not stay dead. Their defining trick is **resilience**: units that shrug off damage and pull themselves back together as the game goes on. You do not out-shoot people with Necrons. You outlast them - you stand on the objective, you take the hit, and you are still there next turn.

That makes them an unusually good army to *learn* on, because they punish exactly the mistake beginners make against them and reward exactly the habit beginners need to build: **stay on the objective**.

They also come with a genuine beginner's obstacle, which this project treats as a feature worth documenting honestly. Most of them are still in the box. As of 2026-08-16 the collection is ten Warriors, three Scarab Swarms, and five Immortals - all bought, none assembled - plus one used Hierotek Circle set that arrived already built and painted, and is therefore the only thing that can hit the table this weekend.

There is a small mystery attached to that last one: nobody has yet identified exactly which models are in the used set. Photographs will settle it. Until they do, the project says "pending photo ID" rather than guessing, which is the same discipline it applies to rules it has not verified.

### The Space Marines - the son's army

The other side of the table. Genetically engineered soldiers in heavy armour - the poster boys of the setting, and by design the most forgiving army in the game to learn with. They are tough, they are straightforward, and their signature ability rewards a single clear decision each turn: pick one enemy unit and focus everything on it.

They are also, practically speaking, **the models that already existed**. A pile of older kits, some of them from editions long past, which is exactly the situation most people inherit when someone in the family used to play. That constraint shapes the project: the research work deliberately includes legacy and Firstborn datasheets that a tournament player would ignore, because those are the models that are actually on the shelf.

### Why the pairing works for teaching

| | Necrons | Space Marines |
|---|---------|---------------|
| Learns by | Outlasting - stay put, absorb damage, hold ground | Focusing - pick the target, commit, trade well |
| Forgives | Losing models | Losing position |
| Teaches the beginner | Objectives win games, not kill counts | Concentration of force beats spreading thin |

Two armies that fail differently teach faster than two that fail the same way. Play them against each other and each side keeps demonstrating what the other side is missing.

---

## What this project is trying to be

A **concierge**, not an encyclopaedia. The difference matters.

An encyclopaedia hands you everything and lets you sort it out. A concierge knows what you are trying to do today and hands you the one page you need - the turn checklist, the two-page card you can keep beside the table, the starter list built from the models you actually own rather than the ones a website recommends.

Concretely, the promises are:

| Promise | What it looks like on the table |
|---------|-------------------------------|
| **Explain, do not just state** | Every rule comes with why it matters and when it decides something |
| **Build from what is owned** | Starter lists use the real collection, and say plainly which models need assembling first |
| **Fit on a card** | Two-page print-and-laminate quick reference per faction, so nobody stops mid-game to flip through a book |
| **Say when it is unsure** | Every claim carries a confidence marker. "I am not certain, go check" is a valid and useful answer |
| **Remember** | Every source read and question answered gets filed, so the same ground is never covered twice |

That last one is the engine. The project reads a source once, writes down what it learned in its own words, and answers from those notes afterwards. Knowledge **compounds** instead of evaporating at the end of a session - the [`../KB/`](../KB/) tree is where it accumulates, and it is the reason this repo is structured the way it is rather than being a single long document.

---

## Why it is careful about copyright

Games Workshop wrote the rules and owns them. This project has strong opinions about respecting that, and they are baked into the structure rather than left to good intentions.

Nothing official is ever copied into this repository. Not the PDFs, not the datasheet images, not the rules text. The owner's library lives on disk somewhere else entirely, and the repo reaches it with **path pointers** - a note that says "the answer is in this file over here" - and nothing more. Everything written here is **paraphrase for teaching**: explained in our own words, with a pointer to where you can check it against material you own.

If a page here cannot tell you where to verify it, that page is incomplete.

---

## Why it is careful about being right

Warhammer 40,000 11th Edition is **new**. Rules get clarified, points get adjusted, FAQs land. A confident answer from six months ago can be wrong today.

So every page in the knowledge base carries a **confidence** value, and every rules claim records the date it was read. `unverified` means "written from memory or an older edition - do not take this to the table." That marker is not an admission of failure. It is the most useful thing on the page, because it tells you exactly which sentence to double-check before you commit to it in a real game.

**Patches happen.** The project says so in as many places as it takes.

---

## Where this goes next

Get to the first game. Then get to a better second game.

After that, the structure is deliberately reusable - the pattern here is not specific to Warhammer 40,000, and [`Game_System_Scaffold.md`](Game_System_Scaffold.md) is the checklist for pointing the same machinery at a different wargame entirely. 40K 11e is the first worked example. It was never meant to be the last.

**Personal use only — this project must never be sold.**

The **second system** is **Kill Team 2024** (skirmish, operatives, turning points). Same household, same models in some cases, **different rulebook**. Kill Team teaching content lives under `games/kill_team_2024/`. Do not mix those rules with 40K.

But that is later. Right now there are ten unassembled Warriors in a box, a son with an army to learn, and a table that needs terrain on it.

---

## Change Log

- v0.5.0 (2026-08-18): Project-wide semver snapshot (x.y.z). Second system Kill Team 2024; personal use, never for sale.
- v1.0 (2026-08-16): Initial origin story - the problem, what a wargame is, the two armies and why they teach well together, project promises, copyright and accuracy posture. Created in slice S1.

## Attribution

- Project: Wargame_Concierge
- Maintainer: Russell Catt
- Structured using the Rising Tide framework

## Rising Tide Notes

- This document follows Rising Tide documentation standards.
- Written for a reader with zero prior knowledge; keep it that way.
- Motivation belongs here. Status belongs in [`Project_Planning.md`](Project_Planning.md).
