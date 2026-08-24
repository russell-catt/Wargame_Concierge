# Manifest §3 — Core Design Principles

- **Track:** warcode_tactical_doctrine
- **Retrieval date:** 2026-08-23
- **Citation legend:** see `00_what_this_is_not.md`
- **Method:** principles inferred from mechanics in the beta, then checked against the studio's stated intent. Where the two agree, confidence rises.

## Stated intent

- "Lean ruleset and enough tactical depth to reward every hour you put in." `[PL §01]` — confidence: draft
- "Twenty minutes to read the rules." `[PL §01]` — confidence: draft (rulebook is ~37 pp with heavy diagram load; plausible but untested)
- "New world, no homework" / "Easy entry, high skill ceiling." `[PL §03]` — confidence: draft
- Designer line: "You shouldn't have to explain a good rule twice." `[PL §07]` — confidence: draft

## Principles visible in the rules

### 1. Everything costs from the same tiny budget
- Each unit has **2 AP**, full stop. Move, shoot, reload, Overwatch, melee, ability, equipment, door — all priced in AP. `[RB pp.3, 4]` — confidence: verified
- **Engage costs 2 AP**, i.e. a unit's entire turn, for +2" and forced melee. `[RB p.14]` — confidence: verified
- Deliberate exemptions: **item pickup and doors cost 0 AP** (within 1"), and **medkit use costs 0 AP**. `[RB pp.4, 17, 18]` — confidence: verified
- Read: the design wants every activation to be a two-item choice, with a couple of free "reward good positioning" outs.

### 2. Attrition is bounded by ammunition, not by lethality alone
- Weapons carry finite ammo; firing spends 1, and 0 ammo means no shooting until reload. Reload has its own AP price. `[RB p.9]` — confidence: verified
- Marketing states this as a pillar: "Ammo runs out. Reload costs." `[PL §03]` — confidence: draft
- Read: a shooting unit cannot simply hold a firing lane forever; it must periodically spend a turn doing nothing offensive.

### 3. Position is checked twice — to hit, and to survive
- **Agility** gates hitting; **Armor** gates damaging. Two separate D6 checks per attack. `[RB pp.5, 20]` — confidence: verified
- Cover raises **Agility**, not Armor, and caps at 5 — so cover has a hard ceiling and stacks only so far. `[RB p.11]` — confidence: verified
- Cover on the **line of fire** counts, not just cover on the target. `[RB p.11]` — confidence: verified
- The shooter standing within 1" of cover shoots as if behind it, so cover is offensive as well as defensive. `[RB p.12]` — confidence: verified

### 4. Reactive fire is a real option, not an afterthought
- **Overwatch** for 1 AP interrupts enemy movement, shooting, reloading, equipment use, melee, disengage, and escape. `[RB pp.10, 11]` — confidence: verified
- **PASS** is explicitly carved out as the one action that does not trigger it. `[RB p.4]` — confidence: verified
- Overwatch drops on firing **or on taking damage**, so it can be stripped by a grenade before the assault. `[RB p.11]` — confidence: verified
- Read: the design wants standoffs to be breakable, and gives grenades the job of breaking them.

### 5. Melee is sticky by design
- Melee radius (usually 1") shuts off shooting, equipment, and abilities. `[RB pp.14, 15]` — confidence: verified
- **Melee Lock** (bases touching) cannot be walked out of — only Disengage (1 AP, D6 vs enemy melee strength, failure costs a free enemy attack at −1 melee strength) or Escape (2 AP, always leaves). `[RB p.15]` — confidence: verified
- **Melee strength is triple-duty**: attack dice, defence dice, and the number an opponent must beat to break away. `[RB p.13]` — confidence: verified
- Read: one stat carries the whole melee identity of a unit. Elegant, and a single point of balance failure.

### 6. Randomness is front-loaded and public
- Map layout: **one D6 before the game**, six known layouts. `[RB p.27]` — confidence: verified
- Event cards fire once per round and are scenario-driven. `[RB pp.3, 26]` — confidence: verified
- Marketing frames this as "map events are known in advance." `[PL §03]` — confidence: draft — **not corroborated by the beta**, which draws the Core-of-the-Machine card *at the start of each round* `[RB p.26]`. See `10_rules_vs_marketing.md`.

### 7. Losing generates resources (double rubber-band)
- **Contracts:** any VP deficit of 1+ at end of round hands the trailing player a secret assassination target worth VP. `[RB p.22]` — confidence: verified
- **Re-rolls:** a player gains **1 re-roll point each time one of their own units dies**, on top of 2/round while the Leader lives. `[RB p.23]` — confidence: verified
- Re-rolls are firewalled off the initiative roll and event-card rolls, so the catch-up cannot buy tempo. `[RB p.23]` — confidence: verified
- Read: the design actively pays the losing player, twice, in different currencies.

### 8. Objectives are held, not touched
- VP capture needs a unit within 1" of the token **with no enemy in that radius**; mixed presence = contested, nobody scores. `[RB p.4]` — confidence: verified
- Scoring is evaluated at **end of round**, so contesting late is as good as capturing. `[RB p.3]` — confidence: verified

## Open questions

- Is the 2-AP budget uniform across all four factions, or do MDR/Dominium bend it? Beta gives "some units have abilities that give extra AP to another friendly unit" `[RB p.3]` but no example unit in the two shipped lists.
- Does "20 minutes to read the rules" survive the Protocol Card and Contract card layers, which are not in the read text?
