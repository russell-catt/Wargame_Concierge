<!--
FILE: games/kill_team_2024/teams/angels_of_death/Team_Rule_Guide.md
VERSION: v0.6.0 (2026-08-27)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, slice S6; dataslate_0826 S3)

DOCUMENT_TYPE: Teaching Guide / Faction Rules
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: Kill Team — 2024 / 3e (KT24)
TEAM: Angels of Death
REFERENCE_STATUS: Draft — written from the living Wahapedia Angel of Death page, retrieved 2026-08-17. Chapter Tactics (all eight) and the August '26 Chapter Tactics errata cross-checked against the staged `eng_26-08_` online rules pack 2026-08-27; ploys/equipment below remain Wahapedia-sourced and not yet cross-checked against the owned team PDF.

SOURCES:
  - https://wahapedia.ru/kill-team3/kill-teams/angel-of-death/ (retrieved 2026-08-17)
  - raw/pointers/kill_team_2024_teams.md — local PDF pointer, not opened this slice
  - games/kill_team_2024/rules/Key_Concepts.md (APL, Orders, 1" control range vocabulary used below)
  - `eng_26-08_killteam_angels_of_death_online_rules-1rwlnicmkz-qjtykwlybg.pdf` (staging, read 2026-08-27) — dataslate_0826 S3, August '26 dated pack; Chapter Tactics + update log cross-check only

PURPOSE:
  Explain what Astartes, Chapter Tactics, and the team's ploys and equipment
  actually do at the table, in plain language — no ploy text or datacard
  statlines reproduced.

PRIMARY_AUDIENCE:
  - A player building or fielding an Angels of Death roster for the first time
  - A reader who already knows KT24 Key_Concepts (APL, Orders, 1" control range)

UPDATE_TRIGGER:
  Update on any Kill Team update log or errata that touches Angel of Death, or
  once the owned team PDF is cross-checked.
-->

# Team Rule Guide — Angels of Death

Written as teaching paraphrase from the living Wahapedia Angel of Death page, retrieved **2026-08-17**. Status: `draft` — Chapter Tactics cross-checked against the staged Aug '26 online rules pack 2026-08-27 (see Update log below); ploys/equipment sections not yet cross-checked against the owned team PDF. Nothing below reproduces ploy card text or datacard statlines; look those up in your team PDF or the Kill Team app before play.

**Rules currency: Kill Team quarterly balance — August 2026** (Core / update logs + team online rules) · teaching paraphrase · verify owned PDFs · confidence `draft`.

---

## Faction rule 1 — Astartes

*What it changes about a normal activation.*

Every Angels of Death operative gets to break the usual "one action of each kind" pacing: on its activation, it can perform **two Shoot actions, or two Fight actions**, instead of the more restricted mix other teams use. Two conditions apply if you double up on shooting:

- At least one of the two Shoot actions has to use a **bolt weapon** (anything with "bolt" in its name — bolt rifle, bolt pistol, bolt sniper rifle, and so on).
- If you are firing the team's slowest bolt weapons twice — the **heavy bolter** or the **bolt sniper rifle** — using the same one for both shots costs **1 extra AP** for the second shot.

Astartes also removes one of the two things a **Conceal** order normally forbids: an Angels of Death operative **can counteract regardless of its order**, even while Concealed. (Normally, per [`Key_Concepts.md`](../../rules/Key_Concepts.md), Conceal blocks Shoot, Charge, *and* counteracting — Astartes only lifts the counteract restriction for this team.)

**Why it matters:** this is the whole team's identity in one line. A basic Intercessor Warrior with Astartes active can fire twice, or punch twice, or (subject to weapon restrictions) mix a shot and a follow-up — turning an "average" operative into a genuine threat every activation, at the cost of never getting to also move that turn if both actions are Shoot/Fight.

---

## Faction rule 2 — Chapter Tactics

*A shared trait pair, picked once, that colours the whole roster.*

At list-build, select a **primary** and a **secondary** Chapter Tactic from a shared pool of eight. Every friendly Angels of Death operative gets both (having the same tactic twice does nothing extra). If you are playing a linked series of games (a campaign or tournament), the primary and secondary stay locked for every battle — though the **Adaptive Tactics** strategy ploy (below) can swap the secondary for a single turning point.

| Tactic | What it does, in short |
|--------|------------------------|
| **Aggressive** | Melee weapons get easier crits — a strong normal success can be upgraded to a critical one |
| **Dueller** | In a Fight, your normal successes can cancel out the opponent's unresolved crits, not just their normal successes |
| **Resolute** | Ignore stat-lowering effects on your APL, including the enemy's stun-style weapon rule |
| **Stealthy** | While the operative has any cover save available, you get a better version of it (an extra save, or the save upgraded to a critical) |
| **Mobile** | Cheaper to Fall Back, and can Charge even while already in an enemy's 1" control range, escaping that engagement to do so |
| **Hardy** | Defence dice crit more easily when the operative is shot, and its first big hit taken while retaliating in melee is softened¹ |
| **Sharpshooter** | Bolt weapons get more reliable *first* shots on an activation where the operative didn't Charge, Fall Back, or Reposition |
| **Siege Specialist** | Ranged weapons ignore the target's cover benefit; in melee, the enemy can't call in an assisting operative against you |

**Reading the pool:** Aggressive/Dueller lean melee, Sharpshooter/Siege Specialist lean ranged, Stealthy/Hardy lean defensive, Mobile is a mobility/disengage tool, and Resolute is a counter to enemy control effects. Most rosters pick one offensive tactic and one defensive-or-utility tactic rather than doubling down on one axis — a team that is already melee-heavy from its operative choices gets more value from Stealthy or Hardy as the second pick than from also taking Aggressive.

¹ **Hardy — August 2026 cross-check.** The staged `eng_26-08_` pack's live rules text gives Hardy one bullet (defence dice results of **5+ are critical successes** when the operative is shot). Its **August '26 errata explicitly "reverts a previous change"**, restoring a second bullet: the first time an attack dice inflicts Normal Dmg of 3+ on this operative **while it's retaliating**, that dice inflicts 1 less damage. Both bullets are current as of the August 2026 package — this table row already reflected both effects, so no correction was needed, but this is now cross-checked rather than assumed. Verify against your owned team PDF, as the two clauses appear in different parts of the online rules pack.

---

## Strategy Ploys (picked in the Strategy phase)

*Full mechanics of the Strategy phase gambit step: [`Turn_Structure.md`](../../rules/Turn_Structure.md).*

| Ploy | What it does, in short | When to reach for it |
|------|------------------------|----------------------|
| **Combat Doctrine** | Pick one of three situations (shooting at range, shooting up close, or fighting/retaliating). Operatives in that situation this turning point get a reroll on their attack dice | Almost every turning point — pick the situation your plan actually uses |
| **And They Shall Know No Fear** | Ignore the stat penalties from being Injured for the whole team, for the turning point | A late-game turn where several operatives are already Injured and you need full performance one more time |
| **Adaptive Tactics** | Swap your secondary Chapter Tactic for a different one, until end of turning point | The turn your plan changes shape — e.g. you were shooting, now you're charging in |
| **Indomitus** | When an enemy shoots one of your operatives and rolls two or more failed defence-relevant rolls against you *(i.e. this is a defensive fix for your operative being shot at)*, trade a bad result for a better one | Any turn you expect to be shot at and want insurance against a spike of bad luck |

**Priority order for a beginner:** Combat Doctrine first, every turning point it's affordable — it is the ploy this team is built to lean on. Save Adaptive Tactics and And They Shall Know No Fear for the turning points where your plan visibly needs them, rather than spending them reflexively.

---

## Firefight Ploys (spent during the Firefight phase)

| Ploy | What it does, in short | When to reach for it |
|------|------------------------|----------------------|
| **Adjust Doctrine** | If you've already used Combat Doctrine this turning point, change which situation it applies to, mid-phase | You committed to Devastator for a shooting turn, then a great charge opened up — switch to Assault for that one activation |
| **Transhuman Physiology** | While being shot, upgrade one of your defence successes to a critical | Protecting a key operative from a nasty incoming crit |
| **Shock Assault** | While fighting after a Charge, your melee weapon hits slightly harder on the first strike of the exchange | Committing a melee operative into a fight you want to win decisively |
| **Wrath of Vengeance** | While counteracting, perform a second, different, free 1 AP action instead of just one | Squeezing extra value out of an operative that's already spent for the turning point |

---

## Faction Equipment

*Selected at list-build; equipment choices are usually limited-use, so treat these as "pick a handful, not all of them."*

| Equipment | What it does, in short |
|-----------|-------------------------|
| **Purity Seals** | Once per turning point, fix a bad roll for one operative that's shooting, fighting, or retaliating |
| **Chapter Reliquaries** | Once per turning point, use Wrath of Vengeance for free on a specified Engaged operative |
| **Tilting Shields** | Once per turning point, in a fight, deny the enemy's ability to upgrade successes to crits via their weapon rules |
| **Auspex** | Once per turning point, remove the Obscured penalty near a shooting operative for that action |

---

## Update log — August 2026 (teaching paraphrase)

From `eng_26-08_killteam_angels_of_death_online_rules-1rwlnicmkz-qjtykwlybg.pdf` errata p.9 (staging, read 2026-08-27). Verify against your owned team PDF before play.

- **Chapter Tactics, Hardy:** reverted to include the retaliation-damage-softening bullet alongside the defence-dice-crit bullet — see footnote ¹ above. No other Chapter Tactic changed this package.
- No other Angels of Death faction rules, ploys, or equipment changed in the August '26 errata section of the staged pack. Everything else in this guide is unaffected by this package.

---

## Common beginner mistakes

| Mistake | What actually happens |
|---------|------------------------|
| Forgetting Astartes lets a Conceal operative counteract | Most teams cannot counteract while Concealed — Angels of Death specifically can; don't waste the option |
| Doubling a heavy bolter or bolt sniper rifle shot without budgeting the extra AP | The second shot with either weapon costs 1 more AP if you fire the same one twice — check APL before committing |
| Picking two offensive Chapter Tactics and no defensive one | Leaves the team with no answer to a bad incoming activation — most rosters want at least one of Stealthy/Hardy/Resolute |
| Spending Combat Doctrine on the wrong situation for the turn | The doctrine only helps the situation you picked (range band or melee) — match it to what you're actually about to do, and use Adjust Doctrine if the plan changes mid-phase |
| Treating Chapter Tactics as fixed to a specific painted Chapter | The tactic pair is a mechanical choice, not tied to which Chapter the models are painted as — pick for the roster's plan, not the paint scheme |

---

## Related pages

- [`README.md`](README.md) — team identity and folder index
- [`Starter_Roster.md`](Starter_Roster.md) — a first roster built around these rules
- [`operatives/Operatives_Index.md`](operatives/Operatives_Index.md) — per-operative role notes
- [`Quick_Reference_Play_Guide.md`](Quick_Reference_Play_Guide.md) — table laminate
- [`../../rules/Key_Concepts.md`](../../rules/Key_Concepts.md) — APL, Orders, 1" control range vocabulary used above
- [`../../rules/Turn_Structure.md`](../../rules/Turn_Structure.md) — where Strategy Ploys and counteracting fit in a turning point

---

## Games Workshop notice

**UNOFFICIAL.** This document is completely unofficial and in no way endorsed by Games Workshop Limited. Personal / no-charge use only — never for sale. Warhammer, Kill Team and associated marks are trademarks of Games Workshop Limited. Used without permission. No challenge to their status intended. Kill Team is Copyright Games Workshop Limited 2024. Teaching notes by Russell Catt (Wargame Concierge). Games Workshop retains IP in the settings and characters. No official logos.

## Change Log

- v0.6.0 (2026-08-27): dataslate_0826 S3 — Chapter Tactics cross-checked against staged Aug '26 online rules pack; Hardy footnote (errata reverts retaliation-softening bullet back in); Update log section; currency stamp.
- v0.5.0 (2026-08-18): Project-wide semver snapshot (x.y.z).
- v1.0 (2026-08-17): Initial faction rule guide (slice S6), written from the living Wahapedia Angel of Death page, retrieved 2026-08-17.

## Attribution

- Project: Wargame_Concierge · Maintainer: Russell Catt
- Kill Team is a trademark of Games Workshop Limited. This document is a personal teaching paraphrase and reproduces no publisher text, ploy card text, or datacard statlines.

## Rising Tide Notes

- This document follows Rising Tide documentation standards.
- **Verify before you play.** Cross-check against the owned team PDF and the Kill Team app — this page currently rests on a living web source only, retrieved **2026-08-17**.
