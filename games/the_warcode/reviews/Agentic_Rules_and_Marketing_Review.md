<!--
FILE: games/the_warcode/reviews/Agentic_Rules_and_Marketing_Review.md
VERSION: v1.0 (2026-08-23)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, warcode_tactical_doctrine S7)

DOCUMENT_TYPE: Agentic review — Wargame_Concierge
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: The Warcode
REFERENCE_STATUS: Active — unofficial and unauthorized; snapshot 2026-08-23

SOURCES:
  - raw/the_warcode/The Warcode Rulebook V.0.8.7-F.pdf (free public beta, read 2026-08-23)
  - https://pre-launch.thewarcode.com/ (retrieved 2026-08-23)
  - https://gamefound.com/en/projects/redmakers/the-warcode (project body login-walled 2026-08-23)
  - docs/handoffs/warcode_tactical_doctrine/review_manifests/00–15
  - raw/pointers/warcode_*.md

PURPOSE:
  A balanced, citation-backed survey of The Warcode free beta V.0.8.7-F and its
  pre-launch marketing, written for the VIP community ahead of the September 2026
  Gamefound campaign. Unofficial and unauthorized. Never for sale.

UPDATE_TRIGGER:
  A newer free beta supersedes V.0.8.7-F; the Gamefound campaign goes live and
  publishes rules, tiers, or lore not visible on 2026-08-23.
-->

# Agentic Rules and Marketing Review — The Warcode

**Unofficial and unauthorized.** Not produced, reviewed, endorsed, sponsored, or approved by RedMakers or Gamefound.

- **Date:** 2026-08-23
- **Scope:** free public beta rulebook **V.0.8.7-F** plus the public pre-launch marketing site
- **Type:** Agentic review — Wargame_Concierge
- **Games played:** zero

**Citation legend used throughout.** `[RB p.N]` is the free beta rulebook, **PDF page N**. `[PL §N]` is the numbered pre-launch marketing page section, retrieved 2026-08-23. `[GF]` is the Gamefound project page. One note on paging: the PDF page numbers cited here run **one higher than the printed folio** (PDF p.3 prints as "2"). Everything below cites PDF pages.

---

## §0 — What this document is not

This document is **unofficial and unauthorized**. It is worth being blunt about what you are reading before you read it.

**One VIP, pre-Gamefound.** I hold a **$1 VIP pledge** and nothing else. No beta STLs, no early access, no NDA material, no contact with RedMakers at any point. Everything here comes from two public sources: the free beta rulebook PDF and the pre-launch marketing site. The Gamefound campaign body itself was **login-walled** on 2026-08-23, so the creator's own campaign disclosures are not part of this review `[GF]`.

**Agentic models plus creator biases.** The research, cross-referencing, and drafting behind this document were done with AI agents working under a project schema, reading the beta PDF and the marketing copy and checking one against the other. That method is good at exhaustive claim-by-claim comparison and bad at judgement. It also inherits my biases as the person who set it up and edited it — I came to this from small-squad skirmish games, I like alternating activation, I am sceptical of crowdfunding fulfilment promises, and I wanted this game to be good. Read accordingly.

**Your mileage may vary.** Every "this is good" below is a read of a text document, not a finding from a table. Zero games have been played. Reasonable people who have actually pushed models around will disagree with parts of this, and they will be better informed than I am when they do.

**This is not a Tabletop Simulator review.** TTS is not owned here and no digital play route was tested.

**This is not a YouTube review.** No video, no sponsorship, no affiliate links, nothing monetised. It is a written document in a personal knowledge repository.

**This is a snapshot of a game still in development.** V.0.8.7-F is a beta. Two of the four announced factions do not exist in it. Findings in §12 may already be fixed in a newer beta I have not seen, and the released game may look meaningfully different. Nothing here is a verdict on a finished product, and nothing here is a purchase recommendation.

**Method and receipts.** The manifests, source pointers, and paraphrase rules behind this document live in the **Wargame Concierge** repository: <https://github.com/russell-catt/Wargame_Concierge>. If you think a claim is wrong, the citation trail is there to check it against.

Full legal position in **§15**.

---

## §1 — What is The Warcode

The Warcode is a **two-player sci-fi skirmish wargame** from RedMakers: two squads of eight units, fought over capture points on a **33" × 24"** board, using **D6 only** and inch measurement taken base-to-base `[PL §01]` `[RB pp.6, 8, 13, 27]`.

The format identity is clear from the beta, and it is a set of deliberate narrowings rather than a general-purpose toolkit:

- **Skirmish scale, single-model units.** 28mm bases are referenced throughout the line-of-sight and cover maths `[RB pp.8, 12]`.
- **Alternating activation, not IGOUGO.** Players take turns activating one unit each `[RB p.4]`.
- **Fixed roster, no list-building.** You pick a faction and you get its eight units. The only pre-game decision is how to spend **4 equipment points** `[RB pp.2, 16]`.
- **Indoor, derelict-interior framing.** The beta's single scenario is set inside a wrecked space drifter with rooms and doors `[RB p.26]`.

Where marketing and rulebook agree, the specs are solid. Where they do not, it is worth flagging early:

| Spec | Value | Confidence |
|------|-------|-----------|
| Players | 2, head-to-head, no teams | draft (marketing); no teams anywhere in the rules |
| Squad size | 8 units, fixed | **verified** — both beta rosters total exactly 8 `[RB pp.33–36]` |
| Board | 33" × 24" | **verified** — diagram labels match `[RB p.27]` |
| Map layouts | 6, chosen by one D6 at setup | **verified** `[RB p.27]` |
| Dice | D6 only | **verified** `[RB pp.3, 15, 27]` |
| Game length | 4 rounds | **draft** — marketing says 4; the **round count is never stated in the rulebook** `[RB p.3]` |
| Playtime | ~120 min | draft — no timing guidance in the rules |
| Setup time | ~10 min | unverified — no rulebook support |
| Factions | 4 | **partial** — only Protagen and Ulfari exist in the beta `[RB pp.33–36]` |
| Age rating | 16+ on tone | draft `[PL §hero]` |

On shape of product: three Gamefound tiers are announced — **Field Commander** (STL), **Core Box** (physical), **Full Deployment** (all-in) — with contents and pricing unrevealed. Miniature STLs are described as resin-optimised, terrain STLs as FDM-optimised, with terrain also available as a separate add-on `[PL §09, §11]`. The campaign is stated for **September 2026** at 09:00 UTC `[PL §11]`.

The studio's own development claims — **27 months in development, 237 playtests, 24k subscribers, 1,038 Discord members, 86,000 trailer views in two weeks** — are all self-reported with no external corroboration and, in the community-metrics case, no snapshot date `[PL §08]`. They are not evidence of anything; they are also not unusual for a pre-launch page.

---

## §2 — Who is developing it

**RedMakers** (<https://red-makers.com/>), self-described as having spent years designing miniatures before building their own system. The positioning line is "Built by sculptors. Played by tacticians." — sculptors moving out of other people's IP and into an original universe `[PL §07]`.

The pre-launch page names **13 individuals**, first names only, with no role duplicated: Bohdan (Creative Director), Margo (Art Director), Alex (Lead Game Designer), Anatoliy (Lead Concept Artist), Ed (Balance & Scenario Design), Vita (Copywriting & Editing), VSQUAD (Map & Environment Design), Olenka (Graphic Designer), Oliver (Miniatures Painter), Artem (Graphic & Video Content), Kate (Manufacturing & Fulfillment), Vlad (Operations), Roman (Marketing & Community) `[PL §07]`.

Two things about that list are genuinely encouraging:

- **A dedicated balance and scenario role** is unusual for a first-time studio at this scale, and it matches what the beta visibly contains — random VP placement, event cards, a contract subsystem `[RB pp.22, 26, 27]`.
- **A dedicated fulfilment role**, with an explicit "the campaign isn't over until the box arrives" framing, reads as crowdfunding-risk awareness `[PL §07]`.

One thing cuts the other way: there is a **dedicated rules-editing role**, and the beta still ships a word-for-word duplicated paragraph, a typo, and a systematic zero-versus-letter-O glyph collision. See §12. That is not an indictment of a person; it is a signal that the editing pass has not yet caught up with the document.

**What is not disclosed anywhere in the sources read**, and should be treated as unverified rather than as a red flag:

- No surnames, so no identity can be corroborated.
- No prior credits or previously shipped titles for the studio or any individual.
- No legal entity, country of operation, or manufacturing partner.
- No external interviews, press coverage, or third-party studio profiles located in this pass.
- **The rulebook carries no credits page**, so the marketing roster cannot be cross-checked against the document `[RB pp.1–37]`.
- The Gamefound project body — where a creator's legal disclosures normally live — was login-walled on 2026-08-23 `[GF]`.

For a backer, the honest summary is: a plausible, well-organised team with no track record you can verify from outside. That is the normal position for a first campaign, and it is exactly the thing the Gamefound page should resolve in September.

---

## §3 — Core design principles

The studio's stated intent is "a lean ruleset and enough tactical depth to reward every hour you put in", "twenty minutes to read the rules", "new world, no homework", and "easy entry, high skill ceiling" `[PL §01, §03]`. The designer's own line is the sharpest of them: *"You shouldn't have to explain a good rule twice."* `[PL §07]`

Reading the mechanics and then checking them against that intent, eight principles come through clearly.

**1. Everything costs from the same tiny budget.** Every unit has **2 AP**. Move, shoot, reload, Overwatch, melee, ability, equipment, door — all priced in AP `[RB pp.3, 4]`. **Engage costs 2 AP**, meaning a unit's entire turn, for +2" of movement and forced melee `[RB p.14]`. The exemptions are deliberate: item pickup and doors cost **0 AP** within 1", and medkit use costs **0 AP** `[RB pp.4, 17, 18]`. The read: the design wants every activation to be a two-item choice, with a few free outs that reward good positioning.

**2. Attrition is bounded by ammunition, not by lethality alone.** Weapons carry finite ammo; firing spends one, and at zero you cannot shoot until you reload, which has its own AP price `[RB p.9]`. A gunner cannot hold a firing lane indefinitely — it must periodically spend a turn doing nothing offensive.

**3. Position is checked twice, to hit and to survive.** **Agility** gates hitting; **Armor** gates damaging; two separate D6 checks per attack `[RB pp.5, 20]`. Cover raises Agility, not Armor, and **caps at 5**, so cover stacks only so far `[RB p.11]`. Cover **on the line of fire** counts, not just cover touching the target `[RB p.11]`. And a shooter within 1" of cover shoots as if behind it, which makes cover offensive as well as defensive `[RB p.12]`.

**4. Reactive fire is a real option, not an afterthought.** **Overwatch** for 1 AP interrupts enemy movement, shooting, reloading, equipment use, melee, disengage, and escape `[RB pp.10, 11]`. **Pass** is explicitly carved out as the one action that does not trigger it `[RB p.4]`. Overwatch drops on firing **or on taking damage** `[RB p.11]` — so it can be stripped by a grenade immediately before an assault. The design wants standoffs to be breakable, and it gives grenades that job.

**5. Melee is sticky by design.** Melee radius (usually 1") shuts off shooting, equipment, and abilities `[RB pp.14, 15]`. **Melee Lock** — bases touching — cannot be walked out of; only Disengage (1 AP, D6 against enemy melee strength, failure hands the enemy a free attack at reduced strength) or Escape (2 AP, always leaves) `[RB p.15]`. And **melee strength is triple-duty**: attack dice, defence dice, and the number an opponent must beat to break away `[RB p.13]`. Elegant — and a single point of balance failure.

**6. Randomness is front-loaded and public.** Map layout is one D6 before the game, from six known layouts `[RB p.27]`. Event cards fire once per round and are scenario-driven `[RB pp.3, 26]`. Marketing frames this as "map events are known in advance" `[PL §03]`, which the beta does not support — the scenario draws its card **at the start of each round**. See §10.

**7. Losing generates resources — twice.** Any VP deficit of one or more at end of round hands the trailing player a **secret contract** worth VP `[RB p.22]`. Separately, a player gains **one re-roll point every time one of their own units dies**, on top of two per round while the Leader lives `[RB p.23]`. Crucially, re-rolls are firewalled off the initiative roll and event-card rolls, so catch-up cannot buy tempo — only accuracy `[RB p.23]`.

**8. Objectives are held, not touched.** Capture needs a unit within 1" of the token **with no enemy in that radius**; mixed presence is contested and nobody scores `[RB p.4]`. Scoring is evaluated at end of round, so arriving late to contest is as good as capturing `[RB p.3]`.

Two open questions remain. Is the 2-AP budget uniform across all four factions? The rules reserve a slot for "abilities that give extra AP to another friendly unit" `[RB p.3]`, but no published unit has one. And does "twenty minutes to read the rules" survive the Protocol Card and Contract layers, which are not in the readable text at all?

---

## §4 — Setting and plot

The headline finding is structural: **the setting is almost entirely marketing-side.** The beta rulebook has no lore chapter, no timeline, and no faction fiction. It has one scenario premise.

The marketing premise: *"Somewhere in a sealed star system, three factions have been locked in a conflict none of them can win — and something from outside just made it worse."* `[PL §hero]` Tone words are **grimdark**, "dark atmosphere, mature story", 16+ `[PL §01, §hero]`.

Structurally that is **three insiders and one outsider**. MDR, Protagen, and Dominium are the system's native belligerents; the **Ulfari are the arrival from outside** — and their inciting incident is stated concretely: "A few of them destroyed an entire station without any warning or explanation" `[PL §02]`. The **sealed system** conceit is doing real narrative work: it explains why the war cannot be won, why nobody escalates outward, and why reinforcements never come. No in-fiction mechanism for the seal is given.

What the rulebook actually contributes is the *Core of the Machine* scenario premise `[RB p.26]`, and it is good: a long-abandoned, heavily damaged space drifter; reaching the machine's core trips security protocols; the damaged machine **cannot tell friend from foe**; a countdown starts with no time to escape. Both squads race to reprogram the core to flag themselves friendly and the enemy hostile, turning **automatic turrets** on the loser. The failure state is that neither side persuades the core and **both are flagged hostile and destroyed**.

That premise is mechanically load-bearing rather than decorative. The tie condition kills both players, and a per-round "Core of the Machine" card applies negative effects to one or more of three rooms `[RB p.26]`.

**The biggest lore surface in the book is currently unreadable.** Protocol Cards occupy five pages `[RB pp.28–32]` and are flattened images with no extractable text. Contract pages `[RB pp.23–24]` are the same. Those pages are the likeliest home of in-book flavour, and nothing in this review reflects them.

Gaps worth naming plainly: no timeline, no dates, no calendar; no named worlds, stations, or even a name for the star system; and — the one that nags — **no explanation of the title "Warcode"**. The phrase never appears as an in-fiction concept anywhere in the rules text read. That is a good first question for the VIP channel.

Two small observations on naming. The **Ulfari** unit names — Ravener, Wraith, Phantom, Soul Eater, Stalker, Doom, Reaper, Shade — read as externally imposed codenames rather than native language `[RB pp.35–36]`. Whether that is deliberate in-fiction is unstated, and if it is deliberate it is a nice touch. The **Protagen** names — Blast, Hammer, Anvil, Bastion, Blade, Shellshocker, Smasher — are role-descriptive, matching the stated engineering-faction identity `[RB pp.33–34]`.

On products: the Full Deployment tier lists an **artbook**, not a lore volume `[PL §09]`.

---

## §5 — Factions: the roster reality

Marketing sells **four balanced factions**. The beta ships **two playable rosters**. MDR and Dominium exist as prose blurbs only.

| Faction | Marketing blurb | Beta roster |
|---------|:---------------:|:-----------:|
| Protagen (Marines) | yes `[PL §02]` | **yes** — 8 units `[RB pp.33–34]` |
| Ulfari | yes `[PL §02]` | **yes** — 8 units `[RB pp.35–36]` |
| MDR | yes `[PL §02]` | **no** |
| Dominium | yes `[PL §02]` | **no** |

### Protagen Marines

Eight units `[RB pp.33–34]`: **Commander Rickman** (Leader, sidearm and energy blade, source of the squad's per-round re-roll income); **Blast** (shotgunner locked into a double-grenade loadout, cannot take other equipment); **Hammer** and **Anvil** (baseline shotgunners); **Bastion** (heavy-weapon platform, slow, minimal melee); **Blade** (melee specialist, highest melee-attack count in the squad); **Shellshocker** (slow, heaviest armour, easiest to hit, shotgun); **Smasher** (melee bruiser whose axe drags anything within 1" into Melee Lock without base contact).

**Shape:** every unit carries a melee weapon and, by design intent, a gun. The squad sits a step above Ulfari on armour and a step below on agility, with two slow units. It reads as a hold-ground list that wins by not dying.

### Ulfari

Eight units `[RB pp.35–36]`: **Soul Eater** (Leader, sidearm and razor blade, highest wounds in the squad); **Ravener** (rifleman); **Shade** (rifleman with a sniper rule that strips a point of the target's agility); **Stalker** (shotgunner); **Wraith** (sidearm and razor blade); **Phantom** (fast, locked into a double-grenade loadout); **Doom** (heavy-weapon platform, least agile body in the squad); **Reaper** (fastest, hardest to hit, and **melee-only — carries no ranged weapon at all**).

**Shape:** uniformly lighter armour, uniformly better agility, two units above baseline speed. A close-fast list that trades durability for the first punch.

### Cross-faction observations

**Mirror-slot design is visible and probably intentional.** Both squads field a Leader with per-round re-rolls, a locked double-grenade unit, a heavy-weapon platform, and shotgun/rifle bodies `[RB pp.33–36]`. Faction identity comes from stat offsets and one or two rule riders, not from different chassis.

**Reaper is the sharpest piece of design in either list.** It is the only unit with no gun, which also means **it can never use Overwatch** — Overwatch requires at least one point of ammunition `[RB p.10]`. It also sits at the **agility cap of 5**, and the rules note that a base-5 target gains no bonus, so Reaper cannot benefit from cover or friendly-screen agility bonuses at all `[RB pp.11, 12, 36]`. Whether all three of those consequences were intended is a fair question, and none of them are called out in the text.

**Smasher's Melee Lock rider is the strongest single rule in either list.** It removes the "just walk out of melee" escape that the core rules grant against non-touching models `[RB pp.15, 34]`.

**Leaders are load-bearing, not flavour.** Killing the enemy Leader shuts off two re-roll points per round for the rest of the game `[RB p.23]`.

### The contract-deck dependency

This is a design blocker worth understanding. Contract cards name **one unit from each available faction**, and the target is drawn from whichever faction the opponent is playing `[RB p.22]`. With only two rosters public, **half of every contract card is unpublished**. The contract pages in the beta are flattened images `[RB pp.23–24]` and unread here. The mechanism itself is confirmed against a real unit — the worked example uses Ulfari's Shade `[RB p.22]`.

There are no points values, because the game is fixed-roster. Do not go looking for a list-builder. And "balanced factions" is currently a studio claim with no published data behind it; the 237 playtests are self-reported `[PL §01, §08]`.

---

## §6 — Faction concepts: identity versus execution

| Faction | Stated concept | Tags | Stated difficulty |
|---------|----------------|------|-------------------|
| **MDR** | Clones of a single commander; one strategic mind across eight bodies; synchronisation over durability | Coordinated, Precise, Adaptable | Mid |
| **Ulfari** | Outside-system aliens; close fast, hit before the opponent reacts; melee-first | Aggressive, Fast, Melee-focused | Beginner-friendly |
| **Protagen** | Engineering faction in heavy suits; trade mobility for resilience; take a position and hold it | Durable, Methodical, Punishing | Mid / beginner-friendly |
| **Dominium** | Elite enforcement wing; degrade nearby enemy morale, amplify allies; combat plus support plus psychological control | Flexible, Combination-based, Deep mastery | Expert |

All four rows are marketing copy `[PL §02]`. Two of them can be checked.

**Protagen: the concept mostly holds.** Armour sits a step above Ulfari across the roster and two units are slow, which matches "trade mobility for resilience" `[RB pp.33–34]`. The shotgun-heavy roster with short reach genuinely pushes them toward advancing behind cover rather than trading at range `[RB pp.7, 33–34]`. And "punishing" is earned — Smasher's forced-Melee-Lock rider punishes anyone who walks into 1" `[RB pp.15, 34]`. **The tension:** Protagen also field the highest melee-attack unit in either list *and* its hardest-hitting melee weapon, which cuts directly against Ulfari being sold as most dangerous in melee `[RB pp.34, 35–36]`.

**Ulfari: the concept partially holds.** "Fast" holds — two units above baseline movement, versus none in Protagen `[RB pp.35–36]`. "High agility" holds — the whole roster is a step harder to hit, with one unit at the cap. "Average armor" is generous framing: in practice they sit **below** Protagen across the board, and with only two rosters published there is no average to be average against `[RB pp.33–36]`. "Melee-focused" is supported by a melee-only unit and armour-cutting blades, but **not** by raw attack volume. "Beginner-friendly" is defensible: the plan is legible — close, engage — and Engage costing a full 2 AP means fewer decisions per activation `[RB p.14]`.

**MDR: unverifiable, but the hook is already in the rules.** The concept needs AP-sharing and positional dependency, and the core rules reserve exactly that slot: "some units have abilities that give extra AP to another friendly unit" `[RB p.3]`. **Neither published roster contains such a unit**, which strongly suggests that rule was written for MDR. That is a good sign — the mechanical scaffolding exists.

**Dominium: unverifiable, and one real flag.** The concept promises **morale degradation** and **ally amplification** `[PL §02]`. **The beta rulebook has no morale, suppression, pinning, or fear system of any kind** in the text read `[RB pp.1–37]`. Either Dominium introduces an entire subsystem, or "morale" is marketing shorthand for a stat debuff. That is worth a direct question in the VIP channel. Separately, "most mechanically complex squad" and "rewards planning several activations ahead" sits awkwardly against a 2-AP, four-round game — there simply are not many activations to plan across.

**The difficulty curve is a genuine plus.** Beginner (Ulfari) → mid-beginner (Protagen) → mid (MDR) → expert (Dominium) `[PL §02]`. Publishing difficulty ratings *before* launch is unusually player-friendly and gives a new player a defensible first pick. The risk is that the two beta factions are the two rated easiest, so the beta cannot demonstrate the top of the curve at all.

**The constraint nobody can design around.** These are chassis-level, identical for every faction `[RB pp.3, 4, 16, 22, 23]`: 2 AP per unit, 8 units, alternating activation, 4 shared equipment points spendable only on grenades and medkits, the same Leader re-roll economy, the same death-driven re-roll income, the same contract catch-up, the same Overwatch, cover, and Melee Lock rules.

The implication matters for anyone coming from a game with army-wide rules, ploy decks, and detachment packages: **faction identity in The Warcode is expressed almost entirely through statlines and a handful of one-line weapon riders.** Expect a much thinner differentiation layer. Whether Protocol Cards change that is genuinely unknown — five unread image pages `[RB pp.28–32]`.

---

## §7 — The core game loop

### Setup, once

1. Read the scenario — objectives, victory conditions, special rules `[RB p.2]`
2. Roll **D6 for map layout** — one of six capture-point placements on the 33" × 24" board `[RB p.27]`
3. Roll **D6 for initiative**, which in round 1 also sets deployment order `[RB p.3]`
4. **Deploy alternately**, one unit each `[RB p.2]`
5. **Spend 4 equipment points** — grenades and medkits at 2 points each, one item per unit unless a rule says otherwise `[RB pp.2, 16]`

Note the ordering quirk, because it is a good one: **units deploy before they are armed** `[RB p.2]`. Equipment is bought with full knowledge of both deployments, which makes loadout a response rather than a guess.

### The round

**Initiative Phase** — both players roll D6, highest goes first this round, ties re-roll. Re-roll points cannot be spent here `[RB pp.3, 23]`.

**Tactical Phase** — players alternate activating one unit at a time. An activated unit spends its 2 AP, then its token flips and it is done for the round `[RB p.4]`.

**End of Round** — in order: end-of-round unit effects, then scenario effects and event cards, then **VP calculation** `[RB p.3]`.

**Contracts check** — if the VP gap is one or more, the trailing player draws a secret contract before the next round `[RB p.22]`.

**Re-roll refresh** — a player whose Leader is alive banks two re-roll points at the start of each round `[RB p.23]`.

Repeat until the final round, then resolve the scenario's win condition `[RB p.3]`. As noted, **the core rules never state how many rounds a game lasts** — it is deferred to the scenario, and the beta scenario does not state it either.

### The activation menu, 2 AP

| Action | Cost | Note |
|--------|------|------|
| Move | 1 AP | Slow 5" / Standard 6" / Fast 7"; −1" through partial cover, −2" through a friendly `[RB p.6]` |
| Shoot | weapon-dependent | Needs range, line of sight, at least 1 ammo `[RB pp.8, 9]` |
| Reload | weapon-dependent | Restores ammo to max `[RB p.9]` |
| Overwatch | 1 AP | **Ends the unit's round entirely** `[RB p.10]` |
| Melee attack | weapon-dependent | Only inside melee range `[RB p.13]` |
| Engage | 2 AP | Movement +2" ending in melee `[RB p.14]` |
| Disengage from Melee Lock | 1 AP | D6 vs enemy melee strength; failure hands over a free attack `[RB p.15]` |
| Escape from Melee Lock | 2 AP | Always leaves, even on a failed roll `[RB p.15]` |
| Ability / equipment | varies | Grenade 1 AP; **medkit 0 AP** `[RB pp.16, 18]` |
| Interact (doors) | **0 AP** | Within 1"; once per activation `[RB p.18]` |
| Pick up item | **0 AP** | Within 1"; only if not already carrying `[RB pp.17, 18]` |
| Pass | 0 AP | The only action that does **not** trigger Overwatch `[RB p.4]` |

### Attack resolution

**Shooting** is three steps `[RB pp.8, 9, 20]`. Roll dice equal to the weapon's shot count against the target's **agility** (raised by cover and friendly screens, capped at 5). Re-roll those hits against the target's **armour**, modified by the weapon's armour-penetration value. Each penetrating die deals normal damage, except that a **6 deals critical damage instead**, and per-die results sum.

**Melee** adds a defence step `[RB pp.13, 21]`. The attacker rolls dice equal to its melee strength against the target's agility. The **defender then rolls dice equal to its own melee strength to block** — each attack die is cancelled only by a defender die of equal or higher value. Unblocked hits go to armour penetration, then damage. The attacker may re-roll the melee hit check **only before the defender blocks** `[RB p.23]`.

**Grenades bypass the front half of that loop entirely.** No hit roll, no agility, and partial cover is ignored — every model in the 2" blast goes straight to an armour-penetration check. Full cover still blocks, via a line-of-sight check taken from the token `[RB pp.16, 17]`.

### Scoring

A capture point pays out only if a friendly unit is within 1" **and no enemy is**; mixed presence is contested and nobody scores `[RB p.4]`. It is evaluated at end of round, so a late-arriving model can deny a whole round's income by standing there `[RB p.3]`. The second income stream is **contracts**: awarded for being behind, paid on eliminating a named enemy unit **by any cause**, including scenario effects `[RB p.22]`.

### What the loop actually feels like on paper

**Three interacting economies per round:** AP for tempo, ammunition for sustained output, re-roll points for reliability. Ammunition and re-rolls carry across rounds; AP does not.

**The Overwatch-grenade interaction is the loop's most interesting pressure point.** Overwatch drops on damage taken, and grenades ignore cover and agility, so a grenade is the reliable way to open a covered firing lane — at the cost of one of only two grenades a squad can buy `[RB pp.11, 16, 17]`.

**Overwatch is mispriced on the label.** It costs 1 AP but ends the unit's round, so the second AP is forfeited. It is a 2-AP action wearing a 1-AP price tag `[RB p.10]`.

**Melee Lock is the tempo sink.** Entering costs 2 AP via Engage, leaving costs 1–2 AP plus a roll, and while locked the unit cannot shoot or use equipment `[RB pp.14, 15]`.

**Contracts fire almost every round.** The trigger is a gap of *one* VP, so any non-tied round hands the trailing player a card — and the beta does not say whether unfulfilled contracts accumulate `[RB p.22]`.

---

## §8 — Who this is for, and organized play

### The audience the studio is aiming at

**Two-player, head-to-head only.** No solo mode, no co-op, no multiplayer, no team play anywhere in the sources read `[PL §hero]`. **One-evening players** — roughly 120 minutes of play, 10 minutes of setup, four fixed rounds `[PL §hero]`. **16+**, on tone rather than complexity. **Refugees from IGOUGO systems** — the studio foregrounds a community quote praising alternating activation `[PL §08]`. And, notably, **3D-printing hobbyists as a first-class audience**: the STL tier leads the tier list and terrain STLs are promised separately `[PL §09, §11]`. Painters and sculptors get a dedicated painter role, a gallery section, and the "built by sculptors" framing `[PL §07]`.

### Who it fits well

- Players who want a **short, closed-length game** with no list-building homework — fixed eight-unit rosters, four equipment points, done `[RB pp.2, 16]`.
- Players who like **interactive turns**. Alternating activation plus Overwatch means you are never idle `[RB pp.4, 10]`.
- Players who want to **learn one small ruleset well** rather than ride an edition treadmill. The marketing says this outright: it "doesn't need a new edition to play differently next week" `[PL §03]`.
- **Indoor and derelict-terrain fans.** The beta scenario is a ship interior with rooms, doors, and door-blocking rules `[RB pp.18, 19, 26]`.

### Who it fits poorly

- **Solo and campaign players.** Nothing in the sources read supports either.
- **List-builders and points-optimisers.** There is no points system; the roster is fixed `[RB pp.2, 33–36]`.
- **Players who need a deep faction-rules layer.** See §6 — differentiation is thin at chassis level.
- **Anyone who needs a stable, finished ruleset today.** The only public rules are a beta, and two of four factions are unpublished.
- **Anyone who needs to buy in now.** Physical product does not exist until a September 2026 campaign funds and delivers `[PL §11]`.

### Organized play

This deserves its own treatment, because it is the single biggest gap for anyone deciding whether The Warcode can replace a game they currently play at events.

| Format | Evidence in sources read | Verdict |
|--------|--------------------------|---------|
| **League play** — ladders, seasons, ranked local play | None. No league, season, ranking, or standings language anywhere in the rulebook or on the pre-launch site. | **Not yet evidenced** |
| **Narrative campaign** — linked games, progression, injuries, XP | None. One standalone scenario `[RB p.26]`; no campaign chapter, no between-game bookkeeping, no roster progression. The Full Deployment tier lists an artbook, not a campaign book `[PL §09]`. | **Not yet evidenced** |
| **Tournament-platform play** (BCP-class event software, pairings, published mission packs) | None. No tournament pack, no event companion, no timing rules, no clock, and no tiebreak beyond one scenario's mutual destruction `[RB p.26]`. No pairings platform mentioned anywhere. | **Not yet evidenced** |
| **Casual pickup and demo play** | Supported in effect: fixed rosters, fixed length, ~10 min setup, randomised map `[PL §hero, §06]`. | **Evidenced (marketing)** |
| **Playtest and development community** | Claimed: 237 playtests, 1,038 Discord members, 24k subscribers `[PL §08]`. | **Evidenced (self-reported)** |
| **Structured community co-design** | The $1 VIP tier gives votes on a new squad's theme, input on its rules and playstyle, and a seat in balance discussions `[PL §10]`. | **Evidenced (marketing)** |

To state it plainly: **The Warcode currently has no organized play scaffolding of any kind.** That is entirely normal for a pre-campaign game, and I am not going to dress it up as "coming soon", because no source promises it.

The missing-infrastructure list, all of it not yet evidenced: no tournament or event pack; no round timing or chess-clock guidance; **no global draw rule** — the only tie handling anywhere is one scenario's everyone-dies condition `[RB p.26]`; no FAQ, errata, or living-document process; no official digital play route; no scenario pack beyond the single beta scenario; and no roster registration or validation tooling, which at a fixed roster size is arguably unnecessary.

What exists instead is the **co-design channel**. Whether the VIP squad-design programme is the studio's substitute for organized play community-building or a precursor to it is an open question, and a good one to ask them.

---

## §9 — Market differentiation

### The studio's six differentiators, checked against the rules

| Claim | Rules support | Verdict |
|-------|---------------|---------|
| "New world, no homework" | Fixed 8-unit rosters, 4 equipment points, no list-building `[RB pp.2, 16]` | **Real** |
| "Ammo runs out. Reload costs" | Per-weapon ammunition, token-tracked, reload priced in AP `[RB p.9]` | **Real** |
| "Overwatch rewards positioning" | 1 AP reactive fire interrupting seven different enemy action types `[RB pp.10, 11]` | **Real** |
| "Loot the fallen — friend or foe" | Equipment tokens stay where a unit died; any unequipped model picks them up for 0 AP `[RB pp.16, 17]` | **Real** |
| "Secret assassination targets" | Contracts, drawn face-down by the trailing player `[RB p.22]` | **Real** |
| "Easy entry, high skill ceiling" | Unfalsifiable from the beta; two of four factions unpublished | **Untestable** |

That is a good result and it deserves saying clearly: **five of six headline differentiators are genuinely implemented in the beta**, not just copy. Whatever else follows in §10 and §12, the marketing is not selling mechanics the game does not have.

### Versus That other game

Design-level comparison only, in my own words. No comparator rules text is quoted, and the comparator is not named.

| Axis | The Warcode | That other game |
|------|-------------|-----------------|
| Force construction | Fixed 8 units, no points; equipment is the only choice `[RB pp.2, 33–36]` | Points and roster selection with meaningful pre-game list decisions |
| Ammunition | Tracked per weapon; running dry is a real board state `[RB p.9]` | Not a general subsystem |
| Catch-up mechanic | Contracts pay the **losing** player a secret bounty `[RB p.22]` | No losing-player bounty of this kind |
| Battlefield loot | Dead models drop usable gear either side can take `[RB p.17]` | Not a general subsystem |
| Faction rules layer | Thin — statlines plus one-line weapon riders; Protocol Cards unread `[RB pp.28–32, 33–36]` | Thick — faction packages, ploys, equipment lists |
| Board | 33" × 24" `[RB p.27]` | Comparable small footprint |
| Re-roll economy | Points from a living Leader **and from your own casualties** `[RB p.23]` | Command-resource economy, not casualty-fed |
| Randomised objectives | D6 picks one of six capture-point layouts before deployment `[RB p.27]` | Mission and objective variation by card and pack |

**And where it is convergent rather than differentiated** — worth being honest about:

- **Alternating unit activation is not a Warcode invention.** The studio's own community quote frames it as a preference, not a novelty `[PL §08]`.
- **Melee where the defender rolls dice to block** is close in spirit to That other game's attacker-defender exchange `[RB pp.13, 21]`.
- **Small-squad, dense-terrain, interior fighting** is a well-populated subgenre, and the derelict-ship scenario lands squarely inside it `[RB p.26]`.

### Versus the broader market

- **STL-first distribution as a headline tier**, not a stretch goal. Field Commander leads the tier list, with resin-optimised minis, FDM-optimised terrain, and terrain STLs as a standalone add-on `[PL §09, §11]`.
- **A $1 refundable co-design pledge.** VIPs vote on a new squad's theme, work with designers on its rules and playstyle, and join balance discussions, with the result shipping free on both digital and physical tiers `[PL §10]`. Low-friction co-design at that price point is genuinely uncommon.
- **A free, complete beta rulebook before launch** — core rules, two playable rosters, a scenario, and the map system, all public pre-campaign `[RB pp.1–37]`. That is a real trust signal, and it is the only reason this review can exist.
- **Published faction difficulty ratings pre-launch** `[PL §02]`.

### Where differentiation is weakest

**No organized play story at all** — a player embedded in event play has nothing to move toward. **Half the faction roster is marketing-only**, so "4 balanced factions" cannot be evaluated, and the two published rosters are the two rated easiest `[PL §02]` `[RB pp.33–36]`. **The faction identity layer is thin** relative to the comparator, unless Protocol Cards carry far more than expected. And **fulfilment is unproven** — first campaign, no prior shipped boxed product located.

The open question that would most change my read: **do Protocol Cards function as the ploy or stratagem analogue?** If they do, the thin-faction-layer criticism weakens substantially.

---

## §10 — Where's the beef? Rules versus marketing

Every public marketing claim, tested against the free beta. Verdicts: **Confirmed** (the rules implement it), **Partial** (implemented but overstated or done differently), **Not in beta** (plausible, simply absent), **Contradicted** (the rules say otherwise), **Unfalsifiable** (no test available from the sources read).

### The scoreboard

Of 31 claims tested: **11 Confirmed**, **4 Partial**, **3 Not in beta**, **3 Contradicted**, **11 Unfalsifiable** — with the unfalsifiable bucket dominated by self-reported metrics.

**The fair overall read: the marketing describes the mechanics honestly. Where it overreaches, it overreaches on polish and completeness, not on what the game does.** That distinction matters, and it is the single most useful sentence in this review.

### Confirmed — the claims that hold

Two players head-to-head; eight units per squad `[RB pp.33–36]`; the 33" × 24" surface `[RB p.27]`; six randomised map layouts, chosen by one D6 `[RB p.27]`; one event card per round `[RB pp.3, 26]`; ammunition with a real AP reload cost `[RB p.9]`; Overwatch as reactive fire interrupting seven distinct action types `[RB pp.10, 11]`; loot persisting on the board for either side to take `[RB pp.16, 17]`; secret assassination contracts payable on elimination by any cause `[RB p.22]`; terrain generating cover, chokepoints, and lines of sight, with doors and door-blocking `[RB pp.11, 12, 18, 19]`; and "doesn't need a new edition to play differently next week", which is supported by five real variance sources — map layout, event card, ammo state, loot, and contracts.

### Contradicted — the three claims the rules refute

**"Map events are known in advance"** `[PL §03]`. The beta scenario draws a **random** activation card **at the start of each round** — the opposite of known in advance `[RB p.26]`. This may well be a copy error rather than a design claim; it is possible it describes an unpublished deck where events are revealed a round ahead. Worth asking directly.

**Ulfari are "most dangerous in melee"** `[PL §02]`. On the published rosters, Protagen field both the higher melee-attack unit and the harder-hitting melee weapon `[RB pp.34, 35–36]`. This may resolve once all four factions ship.

**"The rules are tight… the edge cases have been found and resolved"** `[PL §04]`. This one is directly testable and it fails. A duplicated paragraph, a hardcoded movement number that breaks for non-standard speeds, an exactly-50%-visibility boundary gap, a possible statline inconsistency, and no stated round count. See §12. Saying it once is enough, and I will not belabour it — but a beta document should not carry a claim that the beta document itself disproves.

### Not in beta — plausible, simply absent

**Four rounds, fixed length** `[PL §hero]`. The rules defer round count to the scenario, phrasing it as "if this was the final round", and **never state a number**; the beta scenario does not state one either `[RB pp.3, 26]`. Marketing says four. A reader cannot learn the length of a game from the rulebook.

**Dominium "degrades morale"** `[PL §02]`. No morale, fear, pinning, or suppression system exists in the beta text.

**MDR command abilities where "every unit's position affects what the squad can do next"** `[PL §02]`. The core rules reserve "abilities that give extra AP to another friendly unit", but no such unit appears in either published roster `[RB p.3]`.

### Partial — real, but framed generously

**"4 balanced factions"** — two rosters published, MDR and Dominium absent entirely.

**"Every variable… your opponent's ammo state… unfolds differently each time"** `[PL §01]`. Ammunition is a real variable, but it is tracked with a visible token beside the model, so it is **public information**, not hidden `[RB p.9]`. That is arguably better design; it just is not what the copy implies.

**Ulfari "average armor, but high agility"** `[PL §02]`. Agility a step above Protagen, armour a step **below** — "average" flatters it when only two rosters are public.

**"Lean ruleset… twenty minutes to read the rules"** `[PL §01]`. Roughly 37 diagram-dense pages, plus unread Protocol Card and Contract layers `[RB pp.23–24, 28–32]`.

### Unfalsifiable

Playtime, setup time, and the age rating; the 27 months of development, 237 playtests, 24k subscribers, 1,038 Discord members, and 86,000 trailer views, all self-reported `[PL §08]`; the "factions are balanced" claim, untestable with half the factions unpublished and zero games played here; and the $1 VIP refund and free-squad-on-all-tiers terms, for which no terms document was read `[PL §10, §11]`. The September 2026 Gamefound date at 09:00 UTC is consistent across the page and the pointers, so it counts as **confirmed as stated intent** `[PL §08, §11]`.

---

## §11 — What is good, and what is unique

Standard applied: **good** means the rule does real work at the table. **Unique** means it is not standard practice in small-squad skirmish games. Claims about Warcode's own rules are verified from the beta; claims about the wider market are my inference.

**Cover is offensive as well as defensive.** A shooter within 1" of a piece of partial cover **counts as being behind it** and shoots without interference from that piece `[RB p.12]`. Cover **on the line of fire** counts, not just cover touching the target, and each piece stacks up to the agility cap of 5 `[RB p.11]`. This turns the whole firing lane into a puzzle rather than a yes/no visibility check, and it rewards hugging terrain on the way in.

**Grenades are a designed answer to a designed problem.** They skip the hit roll, ignore agility, and ignore partial cover; every model in the 2" blast goes straight to armour penetration, with full cover still stopping fragments via a line-of-sight check from the token `[RB pp.16, 17]`. Overwatch **drops the moment a unit takes damage** `[RB p.11]`, so the grenade is the reliable tool for cracking a covered overwatching gunline. And a squad can only buy **two grenades total** from four equipment points `[RB p.16]` — the answer exists, but it is scarce. That is tight design.

**Overwatch has real teeth.** It interrupts **seven** distinct enemy action types — movement, shooting, reloading, equipment use, melee, disengage, and escape — resolving before the enemy's declared action `[RB pp.10, 11]`. And **Pass is explicitly carved out** as the one action that does not trigger it `[RB p.4]`, giving the opponent a legitimate way to bait or wait. Reactive fire is common; reactive fire that resolves *before* a declared shooting action and that can be stripped by damage is a sharper implementation than most.

**Melee strength does three jobs from one number.** Attack dice count, **defence dice count**, and the target number an opponent must beat on a D6 to break Melee Lock `[RB p.13]`. A reader learns melee once, and melee becomes an opposed, interactive exchange rather than a one-sided attack `[RB p.21]`.

**Melee stickiness is two-tiered.** Inside the melee radius you can walk out for 1 AP. Once **bases touch** you cannot — only Disengage (1 AP, roll, failure hands the enemy a free attack at reduced melee strength) or Escape (2 AP, always leaves) `[RB p.15]`. A unit locked with several enemies must **beat every one of them** to break away `[RB p.15]`. Melee gets a genuine commitment cost without a flat "no leaving" rule, and base contact becomes a real player decision.

**Contracts are a catch-up mechanic that creates information asymmetry.** Trailing by one or more VP at end of round hands you a **secret** assassination target worth VP, payable even if the target dies to scenario effects or friendly fire `[RB p.22]`. Most catch-up mechanics hand out resources. This one hands out a **hidden objective**, which changes what the leading player has to fear without telling them what it is. That is the most distinctive idea in the game.

**Casualties fund reliability.** One re-roll point every time one of your own units dies, on top of two per round while the Leader lives `[RB p.23]` — and re-rolls are firewalled off the initiative roll and event-card rolls, so losing can buy accuracy but never tempo `[RB p.23]`. Paying the losing player twice, in two currencies, with a firewall on the one that would snowball, is deliberate and well-considered.

**Ammunition as visible board state.** Finite ammo, tracked with a token next to the model, zero ammo blocking fire until a reload is paid in AP `[RB p.9]`. It turns "hold this lane forever" into a rhythm, and because the token is public it becomes a read the opponent can play against.

**Free actions reward good positioning.** Doors, item pickup, and **medkit use all cost 0 AP** — but only within 1", and only once per activation `[RB pp.17, 18]`. On a 2-AP budget, zero-cost actions gated on proximity are effectively a positional bonus rather than a freebie.

**Loot persistence.** Equipment dropped by a killed unit stays on the board and can be taken by **either side** `[RB pp.16, 17]`. Scarcity plus persistence plus a 0 AP pickup makes a dead specialist's grenade a live objective.

### Strong structural choices

**Randomised objectives before deployment** — one D6 picks one of six capture-point layouts, so deployment is planned against known but unpredictable scoring geometry `[RB p.27]`. **Deploy first, arm second** `[RB p.2]`. **Contested points pay nobody**, so denial is as valuable as capture `[RB p.4]`. **Per-die criticals** — a 6 on the damage check deals critical damage instead of normal, with per-die results summing; simple to teach, genuinely swingy `[RB pp.10, 18, 20]`. And **a scenario where a draw kills both players** `[RB p.26]` — uncommonly bold, and it removes any incentive to play for a safe draw.

### Strong project choices

The **free public beta rulebook** before the campaign, complete with core rules, two playable rosters, a scenario, and the map system `[RB pp.1–37]`. **Faction difficulty ratings published pre-launch** `[PL §02]`. The **$1 refundable co-design tier**, delivered free on every tier `[PL §10]`. And the **STL tier as a headline rather than a stretch goal** `[PL §09]`.

**The caveat that applies to this entire section:** none of it is validated at the table. Zero games played. Every "why this is good" above is a read of the text.

---

## §12 — What needs polish

**Framing first: this is a beta.** Everything below is offered as free QA, not as a verdict, and every item is reproducible from the public PDF. The studio's "the edge cases have been found and resolved" line is the only reason this section reads as a rebuttal at all — and having said that once in §10, I will leave it there.

### A. Rules gaps — these need a ruling, not a rewrite

| # | Finding | Where |
|---|---------|-------|
| A1 | **Round count is never stated.** The sequence says "if this was the final round… determine the winner", deferring to the scenario — and the beta scenario never gives a number. Marketing says 4. | `[RB pp.3, 26]` |
| A2 | **Friendly fire is referenced but never resolved.** The rules say friendly fire "will not occur if 50% of the Target's base is in direct line of sight" — implying it *does* occur below that, with no procedure for who is hit or how. | `[RB p.12]` |
| A3 | **No global tie rule.** "The player with the most VP wins" is silent on equal VP. The only tie handling anywhere is one scenario's mutual destruction. | `[RB pp.4, 26]` |
| A4 | **Contract accumulation unspecified.** The trigger is a gap of 1+ VP at the end of *any* round, so it fires most rounds — but nothing says whether unfulfilled contracts stack, cap, or replace. | `[RB p.22]` |
| A5 | **Re-roll scope in melee is one-sided.** The attacker may re-roll the hit check before the defender blocks. Nothing says whether the **defender may re-roll its block dice** — the obvious next question at the table. | `[RB p.23]` |
| A6 | **Penetration and damage share the same dice, but only in an example.** The worked example determines armour penetration and then reads damage off the *same* two dice. The rules chapters describe them as separate checks and never state the reuse — which also silently makes a penetration re-roll a damage re-roll. | `[RB pp.9, 10, 20]` |
| A7 | **Do free grenades cost equipment points?** Two units "start the game with 2 grenades and cannot take other equipment". Unstated whether that consumes any of the squad's 4 points. | `[RB pp.16, 33, 35]` |
| A8 | **"Melee radius, which is usually 1 inch."** "Usually" implies exceptions, and no published unit provides one. Either state it as always 1" with per-weapon overrides, or list the exception. | `[RB p.15]` |
| A9 | **Overwatch's true cost is misstated.** Priced at 1 AP, but "the unit cannot take any other action for the rest of the round" — so it consumes the whole 2 AP activation. Either say it ends the activation, or let the spare AP be spent. | `[RB p.10]` |
| A10 | **Event card scope undefined.** The round sequence lists "activation of scenario event cards"; the only concrete example is the scenario's own deck. Whether a general event deck exists is unclear — and marketing implies one. | `[RB pp.3, 26]` `[PL §01]` |

### B. Reportable bugs — defects, not design questions

These are the items worth sending to RedMakers verbatim through the VIP channel. **B1 and B8 are the two that most deserve a fix before launch.**

| # | Bug | Repro | Severity |
|---|-----|-------|----------|
| **B1** | **Movement fallback hardcodes 4" and 5".** The rule for placing a model when movement ends beyond a friendly unit or partial cover is written in literal inches ("within 4 or 5 inches"). Those numbers are the 6" standard speed minus the 2" friendly and 1" cover penalties — so they are **wrong for Slow (5") and Fast (7")** units, both of which exist in the published rosters. Should read "reduced Movement Range". | `[RB p.7]` vs speeds `[RB p.6]` and rosters `[RB pp.33–36]` | **High** — affects every game |
| **B2** | **Duplicated paragraph.** Page 12 prints the same partial-cover example paragraph twice, word for word. | `[RB p.12]` | Low — cosmetic |
| **B3** | **Inconsistent 50% boundary language.** Full cover and friendly fire use "**at least** 50% / at least 14mm"; partial cover uses "**more than** half / more than 14mm". At exactly 14mm on a 28mm base the three rules disagree. | `[RB pp.8, 11, 12]` | Medium — edge case, but a common one |
| **B4** | **Possible statline inconsistency — Smasher's sidearm.** It appears one step above the standard sidearm profile in the weapons chapter on both normal and critical damage, with no ability text and no other unit sharing the variant. Either an intentional unique that needs labelling, or a copy error. | `[RB pp.7, 34]` | Medium — balance-relevant |
| **B5** | **Typo:** "armor penetratsion" in the melee example's weapon-ability line. | `[RB p.21]` | Low |
| **B6** | **Glyph collision — capital O used for zero.** Armour-penetration values of zero are set as the letter "O", and page folios render 10/20/30 as "1O"/"2O"/"3O". On a datasheet where "0" is a meaningful modifier this is a real legibility risk in print, and it breaks text search and copy-paste. | `[RB pp.11, 13, 21, 31]` | Medium — print and accessibility |
| **B7** | **Contents page stops halfway.** The table of contents ends at Contracts / Re-roll, listing nothing for the scenario, the random VP placement system, the Protocol Cards, or the two team lists — roughly a third of the book. | `[RB p.2]` vs `[RB pp.25–36]` | Medium — usability |
| **B8** | **Contract deck cannot be built.** Contract cards name "one unit name from each available faction", but only two of four factions have published unit names. Any printed contract deck is half-unusable until MDR and Dominium ship. | `[RB p.22]`, rosters `[RB pp.33–36]` | **High** — blocks a core subsystem |
| **B9** | **Card pages are flattened images.** Contract pages and all five Protocol Card pages carry no extractable text. They are unreadable to screen readers, unsearchable, and untranslatable, and they force OCR on anyone building reference material. | `[RB pp.23–24, 28–32]` | Medium — accessibility |

### C. Design concerns — working as written, worth questioning

- **Contracts fire on a 1 VP gap**, i.e. nearly every round. Combined with re-roll income from your own casualties, the losing player receives two compounding subsidies. Whether that keeps games close or blunts good play is a playtest question, not a text question `[RB pp.22, 23]`.
- **A 2 AP budget in a four-round game leaves very few decisions** — roughly 64 activations per side across the whole game, minus deaths. That sits awkwardly against Dominium being marketed as rewarding planning "several activations ahead" `[RB p.4]` `[PL §02]`.
- **Medkit at 0 AP versus grenade at 1 AP** makes healing strictly better on tempo for the same equipment cost `[RB pp.16, 18]`.
- **The agility cap of 5 makes at least one published unit immune to cover and screening bonuses entirely.** Elegant if intended, invisible if not — it is never called out `[RB pp.11, 12, 36]`.
- **Heavy weapons cost 2 AP to fire on a 2 AP unit**, so a heavy platform can only ever shoot or move, never both. Deliberate-looking, but the rulebook never says so `[RB pp.7, 34, 36]`.
- **Faction identity rests almost entirely on statlines.** Unless Protocol Cards carry more weight than expected, the differentiation layer is thin.

### D. Documentation and production polish

- **The diagram-heavy layout does not survive text extraction**, so the PDF is a poor searchable reference even where text exists — profile values extract as bare number runs with no labels `[RB pp.7, 33–36]`.
- **No index, no quick-reference sheet, no one-page turn sequence** in the book as read. For a game selling itself on "twenty minutes to read the rules", **a single-page player aid is the highest-value missing asset in the entire product.**
- **No credits page**, so the marketing roster cannot be cross-checked against the document `[RB pp.1–37]`.
- **No version or date stamp in the extracted text** — the version lives in the filename only. A printed version line would help beta feedback triage enormously.

**Standing offer:** I will happily re-run this entire pass against the next free beta. That is meant as help, not as criticism.

Two things I genuinely do not know: whether any of the above is already fixed in a beta newer than V.0.8.7-F, and whether there is a proper VIP-facing bug-report channel these should go through instead of a Facebook post.

---

## §13 — The non-agentic view

Hi, Russ the editor here.
I was intrigued about the campaign when I ran across it on Facebook. 
I've been trying to teach my 10-year-old son to play "That other game" on-and-off for about 2 years.
It's always been a tough sell due to a tough to parse rulebook and "Rules as intended" vs "Rules as written" edge cases.
It takes us so long to figure out how to perform the normal turn loop that my son often loses interest before the end of TP1.
That's part of the reason I started this "Wargame Concierge" project: To help me learn games so I can better teach my son. Also to help write "new player reference" cheat sheets to help us get into the flow faster.
Your game's pledge of an "easy to learn, learn to master" type system seemed cool.
Then I went to your web site and saw the minis you have designed. Suddenly, I feel regret for the hundreds of dollars of "plastic mans" I have purchased over the past two years. They look gorgeous.
After I joined the VIP, I noticed that your rules were freely available. I was FLOORED. 
I'm a professional software tester and doumentation reviewer by trade, so my feelings about seeing beta documentation in the wild got my full and undivided attention.
I haven't made it through the whole thing yet, but I like what I see.
I was very interested to see what would happen if I plugged your manual and website into this structure and said "read it all and write a review on these sections. Flag any bugs you find."
I've backed many a crowdfunder and with board games I'm usually a bit disappointed when I finally ge the game. Sometimes, it's a lot more flash than substance, or the rulebook gives me a migraine.
I'm glad the system disproved a lot of my anxieties. I look forward to the launch of your campaign.


---

## §14 — Thank you

A genuine thank you to **RedMakers**, and specifically for two decisions that most studios do not make.

**Publishing a complete free beta rulebook before the campaign** — core rules, two playable rosters, a scenario, and the map system, all of it public and downloadable before anyone is asked for money `[RB pp.1–37]`. That takes nerve. A beta invites exactly the kind of line-by-line scrutiny this document contains, and putting it out anyway is a bet that the game holds up better under examination than under mystery. **This review exists only because they made that choice.** Every critical finding in §12 is downstream of an act of openness.

**Publishing faction difficulty ratings before launch** `[PL §02]`, rather than leaving a new player to guess which army will punish them for a year. Small thing, real thing.

Thank you also to **the named team** — Bohdan, Margo, Alex, Anatoliy, Ed, Vita, VSQUAD, Olenka, Oliver, Artem, Kate, Vlad, and Roman — for putting names and roles on a public page `[PL §07]`. First names only, exactly as published; no surnames were sought or guessed.

And to **the VIP and Discord community**, for a channel where a $1 pledge buys a real seat in squad design and balance discussion `[PL §10]`.

To be explicit, because §14 must not undercut §0 or §15: **this review was written with no contact with the studio whatsoever**, from public material only. Nothing here implies a relationship, an endorsement, a partnership, or early access. And rather than treat this document as authoritative, please take the open questions in it to the VIP channel and ask the team directly — they are the only people who can actually answer them.

---

## §15 — Ownership, trademarks, and disclaimers

1. **This document is unofficial and unauthorized.** It is not produced, reviewed, endorsed, sponsored, or approved by RedMakers or Gamefound.

2. **The Warcode** and all associated names, factions, unit names, artwork, and trade dress are the property of their respective owners (RedMakers). No ownership is claimed here, and no trademark or other right is asserted.

3. **Personal use only. Never for sale.** This document and the project containing it must never be sold, licensed, or monetised in any form.

4. **Not a rules substitute.** Any quoted material is scoped, cited, and partial. The free beta PDF from RedMakers is the only rules authority. Download the official product from RedMakers.

5. **Quote scope.** Verbatim rules quotes appear in this project only under `games/the_warcode/rules/`, `setup/`, and `factions/`, each carrying filename plus page, under the project's scoped free-beta exception. Knowledge-base and operational documents stay paraphrase.

6. **Edition scope.** All findings apply to the free public beta **V.0.8.7-F**, retrieved **2026-08-23**, and may be superseded by any newer free beta or by the released game.

7. **No affiliation, no contact.** Written entirely from public material, with no contact with the studio, no NDA material, and no early access. The author holds a $1 VIP pledge and nothing else.

8. **No STL redistribution.** No STL files are hosted, shared, or reproduced anywhere in this project. Official STLs come via the Gamefound Field Commander tier only; no third-party sources are used or endorsed.

9. **Comparator trademarks.** Any comparison to another manufacturer's game is design commentary offered as fair comment. That publisher's trademarks remain entirely theirs, and that game is not named in this document — it appears only as **That other game**, with **Murder Platoon** standing in for its squad mode.

10. **Opinion disclaimer.** Every assessment here is opinion and inference drawn from a beta document, with **zero games played**. This is not commercial, legal, financial, or purchase advice.

11. **Corrections.** Errors will be corrected on notice. RedMakers may request removal of any quoted material and it will be removed.

**Gamefound project:** <https://gamefound.com/en/projects/redmakers/the-warcode>

---

## §16 — Comparative glossary

If you are arriving from **That other game**, the vocabulary is the first friction point — Warcode's terms are mostly familiar concepts under unfamiliar names, and a few familiar names mean something different here. The companion file below maps the bridges term by term: activation, AP, agility versus armour, Overwatch, Melee Lock, contracts, re-roll points, and capture points, each set against the closest **Murder Platoon** mental model, with a note where the analogy breaks down.

- [`../rules/Comparative_Glossary.md`](../rules/Comparative_Glossary.md) — term-by-term bridges to That other game

Use it as a lookup rather than a read-through. The one habit worth unlearning before your first game: in Warcode, **cover raises how hard you are to hit, not how hard you are to hurt**, and a shooter standing next to cover gets to shoot as if behind it. Almost every early mistake traces back to that.

---

## Change Log

- v1.0 (2026-08-23): Initial polished review. Built from review manifests §§00–12, 14, 15 (track `warcode_tactical_doctrine`, slice S7). §13 left as a placeholder for the owner's non-agentic VIP perspective.

## Sources and retrieval dates

| Source | Retrieved | Notes |
|--------|-----------|-------|
| `raw/the_warcode/The Warcode Rulebook V.0.8.7-F.pdf` | **2026-08-23** | Free public beta, ~37 pp. All `[RB p.N]` cites are **PDF** pages; printed folio runs one lower. |
| <https://pre-launch.thewarcode.com/> | **2026-08-23** | All `[PL §N]` cites. Marketing copy, self-reported metrics undated at source. |
| <https://gamefound.com/en/projects/redmakers/the-warcode> | **2026-08-23** | Project body **login-walled**; comments visible only. Creator disclosures not read. |
| <https://red-makers.com/> | **2026-08-23** | Studio site. |
| Protocol Cards `[RB pp.28–32]`, Contract cards `[RB pp.23–24]` | — | **Flattened images, unread.** No OCR pass at time of writing. |

## Attribution

- Project: Wargame_Concierge — <https://github.com/russell-catt/Wargame_Concierge>
- Maintainer: Russell Catt
- The Warcode is the property of RedMakers. Unofficial and unauthorized personal notes. Never for sale.
- Structured using the Rising Tide framework.

## Rising Tide Notes

- **Edition in scope:** free public beta **V.0.8.7-F**. A newer free beta supersedes it; omission in a newer beta is not a patch.
- **Snapshot status:** this document is a snapshot taken **before the September 2026 Gamefound campaign**. It does not reflect the campaign body, final rules, final tiers, or the released game.
- **Zero games played** at time of writing. Treat every judgement as a reading of a text, not a table result.
- Never name That other game's real product title in this subtree — **That other game** or **Murder Platoon** only.
- Keep the receipts. Make AI show their work.
