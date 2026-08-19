---
title: Power Matrix
type: concept
system: warhammer_40k_11e
faction: Necrons
created: 2026-08-16
updated: 2026-08-19
version: 0.5.3
sources: [necron_lists_owner_notes, docs/Game_System_Scaffold.md]
confidence: draft
tags: [concept, necrons, canoptek_court, detachment_rule, correction, edition_check]
---

# Power Matrix

The **Canoptek Court detachment rule in Warhammer 40,000, 11th Edition**: units re-roll hit rolls while operating in territory the Necron player controls. Not a Kill Team term - this page records the correction.

---

## The correction

L0 seeded this term in [[glossary]] with an explicit warning that its game system was unresolved, reasoning that the owner's Hierotek Circle set is a **Kill Team** box and that Power Matrix might therefore be a Kill Team mechanic. The glossary entry said so plainly and told downstream slices not to build 40K content on it.

**That was wrong, and L1 resolves it.** Two independent sources already inside the repo name Power Matrix as a Warhammer 40,000 detachment rule:

| Source | What it says |
|--------|--------------|
| `raw/Necron_Lists.md` - see [[necron_lists_owner_notes]] | Lists "The Power Matrix" as the **main detachment rule** of the Canoptek Court, in a table comparing two 40K detachments at 40K points values |
| `docs/Game_System_Scaffold.md` | Its generic-to-40K vocabulary mapping gives "Power Matrix, the Canoptek Court detachment rule" as the worked example of a sub-list rule package |

The two were written by different slices from different material and agree. Neither has any connection to Kill Team.

**Why L0 got it wrong, and why the mistake was reasonable.** The owner owns a Kill Team box *and* plays Necrons in 40K. Both involve Crypteks. L0 was seeding terms from general familiarity with no source in front of it, saw "Cryptek resource mechanic" and "Hierotek Circle" in the same note, and connected them. The right call at the time was exactly what L0 did: write the uncertainty down loudly instead of guessing. The flag is what made this correction cheap.

The **Hierotek Circle** and **Power Matrix** are now formally unrelated in this KB. The set remains an open identification question on [[necrons]]; it is not evidence about this term.

---

## What is settled and what is not

| Claim | Status |
|-------|--------|
| Belongs to Warhammer 40,000, not Kill Team | **Resolved** |
| Is the [[canoptek_court]] detachment rule | **Resolved** |
| Grants hit re-rolls tied to controlled territory | `draft` - owner's paraphrase, one source |
| What "controlled territory" means in 11e wording | **Open** |
| Whether it applies to shooting, melee, or both | **Open** |
| Whether it is full re-rolls or a narrower benefit | **Open** |

The name and its owner are settled. **The rule text is not, and nothing should be taken to a table on the strength of this page.** Verify against the Necrons faction pack (`raw/pointers/faction_pack_necrons.md`), then cross-check on [[wahapedia]].

---

## Why the rule shapes the army

Taking the paraphrase at face value, Power Matrix does something unusual: it makes **map control an offensive statistic**.

In most armies, accuracy comes from the datasheet, from a character, or from a stratagem - things you bring or spend. Here it comes from *where you are standing*. Three consequences follow, and they are the reason [[canoptek_court]] plays the way [[necron_lists_owner_notes]] describes.

- **Territory is worth double.** Holding ground scores through [[objective_control]] (`14.02`) and improves damage in the same turn. Losing it costs both at once, so a swing in the middle of the board is larger than the score difference suggests.
- **The army wants to fight forward.** The source's plan - push Wraiths onto a central objective specifically to open a Power Matrix zone in No Man's Land - only makes sense if the re-rolls follow controlled ground rather than sitting in the deployment zone. That is the aggressive midfield posture the detachment is known for.
- **It pairs naturally with [[reanimation_protocols]].** Standing still on an objective is what the army rule already rewards. A detachment rule that also pays for standing there compounds it, which is the mechanical case for Canoptek Court being rated the stronger detachment.

If the actual 11e wording turns out narrower - a deployment-zone-only re-roll, say, or shooting only - the third point survives but the second collapses, and the detachment's whole gameplan changes. That is why the verification matters rather than being bookkeeping.

---

## For a new player

Do not learn this rule first. Learn [[objective_control]] and the turn sequence, then come back: Power Matrix is a *modifier* on decisions you have to be able to make already. A player who does not yet know why the middle objective matters will not get anything out of a re-roll for standing on it.

---

## Related terminology

**Technosorcerous Augmentations** is the equivalent rule for [[cryptek_conclave]]. Its name and effect are both better established than this one's: the owned faction pack v1.1 was read directly for it on 2026-08-16, whereas Power Matrix's exact wording is still unverified. The owner's notes call it "Scientific Schemes", which is wrong - see the deprecated list in [[glossary]].

---

## Open questions

- The exact 11th Edition wording, in all its parts
- Whether "controlled territory" is defined by the core rules or by the detachment
- Whether any of this changed between 10th and 11th Edition
- Does a *Kill Team* Power Matrix also exist? If so the terms are homonyms and both need labelling - but there is no evidence for one, and none should be assumed.

---

## Related pages

- [[canoptek_court]] - the detachment this rule belongs to
- [[necrons]] - the faction
- [[objective_control]] - the mechanic it is coupled to
- [[reanimation_protocols]] - the army rule it compounds with
- [[necron_lists_owner_notes]] - primary source for the correction
- [[glossary]] - the entry this page supersedes
- [[index]]
