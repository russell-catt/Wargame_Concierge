# R1 rules delta — Rulebook v0.8.7-F to v0.8.9-F

- **Track:** `warcode_kickstarter_refresh`
- **Researcher:** R1
- **Date:** 2026-09-24
- **Result:** **PASS**
- **Confidence:** **High** for the delta boundary and unchanged-page checks; **medium-high** for reconstructed profile columns pending the planned independent visual QA pass.

## Sources and method

Compared:

- `raw/the_warcode/The Warcode Rulebook V.0.8.7-F.pdf`
  - 37 PDF pages
  - SHA-256 `6eb0f80493d8f7a51d0054260aba6c6ab76c8c0df5166866aca76c8fc2a83ee1`
- `raw/the_warcode/The-Warcode-Rulebook-V.0.8.9-F.pdf`
  - 41 PDF pages
  - SHA-256 `4dc9efc7d97b7c14ce4f1afa729d8b0dd2fa97a51fa2d1b8385003ea75c1c93d`
- `raw/the_warcode/rulebook_v087f_extract.txt`
- `raw/the_warcode/rulebook_v089f_extract.txt`
- `raw/the_warcode/contract_cards_transcription.txt`
- `raw/the_warcode/protocol_cards_transcription.txt`
- `raw/the_warcode/protocol_cards.ocr.txt`

Checks performed:

1. Compared normalized native-text token sequences page by page.
2. Compared embedded image and form resources, including decoded resource hashes.
3. Checked the old card/OCR sidecars against the corresponding unchanged card artwork.
4. Reconstructed the new roster columns from the v0.8.9-F native extract and page layout.

The PDFs are not byte-identical re-exports. A recurring 364×177 image differs throughout, and several diagram images on core-rules pages were re-encoded or cosmetically altered. Those changes do not alter extracted rules text. On pages 2–36, the only normalized-text differences are extraction joins such as `1 AP` becoming `1AP`; no wording or numeric rule changed.

## Executive verdict

The established lock is correct:

- Core rules are unchanged.
- The eight contracts and all four faction columns are unchanged.
- The 20 protocol cards are unchanged.
- The Core of the Machine scenario is unchanged.
- All six D6 VP layouts are unchanged.
- Protagen Marines are unchanged.
- Ulfari are unchanged.
- The substantive addition is MDR Executive Unit on PDF pp.37–38 and Custodia Silens on PDF pp.39–40.
- The old trailing art page at PDF p.37 moves to PDF p.41 after four roster pages are inserted.

No evidence of another mechanics delta was found.

## Page-level equivalence

| PDF pages | Content | Evidence | Result |
|---|---|---|---|
| 2–23 | Setup, phases, AP, VP, movement, ranged combat, Overwatch, cover, melee, equipment, examples, contracts procedure, re-rolls | Normalized text is equivalent. Differences are extraction spacing/join artifacts only. | **PASS — High** |
| 24–25 | Eight contract cards, each with Protagen, Ulfari, MDR, and Custodia targets | All eight 449×701 card-image resources have identical decoded hashes between versions. Only the recurring page-brand image differs. This verifies the complete 8×4 target matrix and 1-VP card faces. | **PASS — High** |
| 26 | Core of the Machine scenario | Normalized text is equivalent; no substantive page-resource change. | **PASS — High** |
| 27 | Six D6 VP maps | Text/coordinate sequence is equivalent. Both map images retain identical decoded hashes; only the recurring page-brand image differs. | **PASS — High** |
| 28–32 | Protocol cards | Every card-art image retains the same decoded hash on the corresponding page. The five effects across room/total variants remain the same 20-card corpus. Existing OCR quirks therefore remain source quirks, not new deltas. | **PASS — High** |
| 33–34 | Protagen Marines | Normalized text and substantive form resources are equivalent; only the recurring page-brand image differs. | **PASS — High** |
| 35–36 | Ulfari | Normalized text and substantive form resources are equivalent; only the recurring page-brand image differs. | **PASS — High** |
| 37–38 | MDR Executive Unit | New two-page roster. Printed folios are 36–37. | **PASS — new material** |
| 39–40 | Custodia Silens | New two-page roster. Printed folios are 38–39. | **PASS — new material** |
| 41 | Trailing art | Empty native-text page, same 612×792 page geometry and 1700×2200 full-page image shape as old PDF p.37. The image stream was re-exported, so it is semantically equivalent rather than byte-identical. | **PASS — High** |

### Preserved card details

- Contracts remain cards 4186, 9278, 5039, 6037, 3697, 4913, 3512, and 2984.
- The target spelling on contract 4186 remains **Justicar Julius**.
- The protocol set remains Magnet, Hunt, Electricity, Silence, and Poison, each represented by Left, Centre, Right, and Total variants.
- The existing OCR-sidecar cautions remain valid, including Hunt's full-health condition and the singular-room wording on some Total cards. The typed protocol transcription is less reliable than the OCR sidecar on those points.

## New roster coverage

This handoff paraphrases the new rules because `docs/**` is not an approved verbatim/statline-dump surface. Stage 2 should transcribe the profiles from the cited PDF pages only under the approved `games/the_warcode/factions/**` quote path.

### MDR Executive Unit — PDF pp.37–38

The roster contains eight units:

| Unit | Page | Weapons / role | Complete profile-rule capture |
|---|---:|---|---|
| Sergeant 139 | 37 | Large-Caliber Pistol; Volt Sword; leader/support | Generates the normal Leader re-roll income. Once per round, may spend 1 AP to give one not-yet-activated friendly unit within 7 inches +1 AP through the end of the round; unusable in melee. Friendly units within 7 inches set their melee penetration to −1. Both effects can be relayed through the Comms Operator. |
| Grenadier | 37 | Rifle; Bayonet | Starts with two grenades and cannot take other equipment. |
| Combat Medic | 37 | Rifle; Bayonet; support | Starts with one medkit and cannot take other equipment. At round end, restores 1 HP to every friendly unit within 6 inches, excluding itself; the effect is disabled while the Medic is in melee. |
| Machine Gunner | 37 | Large-Caliber Machine Gun; Combat Knife | No additional written ability. |
| Corporal | 38 | Rifle; Bayonet | No additional written ability. |
| Private | 38 | Rifle; Bayonet | No additional written ability. |
| Marksman | 38 | Rifle; Bayonet | Its shooting reduces the target's Agility by 1. |
| Comms Operator | 38 | Rifle; Bayonet; relay | If within 7 inches of Sergeant 139, extends the Sergeant's melee-penetration aura and Order to otherwise eligible friendly units within 7 inches of the Comms Operator. |

Profile-shape observations for implementation:

- Sergeant 139 is the roster's 9-HP Leader; all seven other MDR units are 8 HP.
- Every MDR model has Agility 3, Movement 6, and Armor 3.
- The large-caliber pistol differs from the standard pistol by using −1 penetration and a two-shot ammunition reserve.
- The large-caliber machine gun is a short-ranged, low-shot, three-ammunition weapon with −1 penetration and shotgun-grade damage.
- Rifles and bayonets are shared across six models.
- Sergeant 139's Volt Sword keeps the familiar armor-penetration re-roll-on-1s rule.

### Custodia Silens — PDF pp.39–40

The roster contains eight units:

| Unit | Page | Weapons / role | Complete profile-rule capture |
|---|---:|---|---|
| Justiciar Julius | 39 | Large-Caliber Pistol; Combat Knife; leader/debuffer | Generates the normal Leader re-roll income. Enemy units within 6 inches and line of sight suffer −1 Agility from Justiciar's Influence. |
| Assassin | 39 | Large-Caliber Pistol; Combat Knife | Starts with two grenades and cannot take other equipment. It is the roster's Movement 7 model. |
| Punisher | 39 | Heavy Weapon; Combat Maul; durable heavy | Cannot be healed by medkits and cannot carry equipment. It is the roster's 10-HP, Armor 4 heavy model and has a 2-AP Heavy Weapon. |
| Cremator | 39 | Hand Flamethrower; Volt Sword; area-effect attacker | The flamethrower ignores Agility and partial cover, never needs reloading, and applies Burning to the target plus every unit within 2 inches. Burning deals 1 damage at round end and then clears; a medkit clears it; a unit cannot have more than one Burning effect. The Volt Sword retains its armor-penetration re-roll-on-1s rule. |
| Confessor | 40 | Fist; support/reactivator | Cannot be healed by medkits and cannot carry equipment. Inspiration costs 1 AP per friendly target within 8 inches and line of sight that has already activated. Spending both AP targets two different units. Inspired units receive a later 1-AP activation after all ordinary activations; Inspiration cannot be used in melee. |
| Tormentor | 40 | Directed Energy; Fist; damage/debuff support | Directed Energy ignores armor, is a ranged weapon usable once per round, and cannot be used for Overwatch. Each critical hit damages its user by 1, although the explanatory sentence calls the weapon Focused Energy. Tormentor's Influence deals 1 round-end damage to enemies within 5 inches without needing line of sight. Choke costs 1 AP, targets an enemy within 8 inches and line of sight, deals 1 damage at each round end, persists regardless of later range/line of sight, and ends only when the Tormentor is destroyed. A target can receive Choke only once; at most two units can be affected; a dead target frees a slot. Choke cannot be used in melee. |
| Executor | 40 | Shotgun; Combat Knife | No additional written ability. |
| Lancer | 40 | Combat Spear; control | Enemy units within 1 inch count as Melee Locked even when bases do not touch. |

Profile-shape observations for implementation:

- Core profiles intentionally vary: Justiciar 9 HP; Punisher 10 HP; Confessor and Tormentor 7 HP; the other four units 8 HP.
- Agility ranges from 2 to 3, Movement from 5 to 7, and Armor from 2 to 4.
- Directed Energy prints dashes for ammunition, reload, and penetration because its rule supplies the exceptions.
- The Hand Flamethrower prints ammunition 3 and no reload AP while also saying it never needs reloading. That combination is an ambiguity, not permission to rewrite the profile.
- The Lancer's extended Melee Lock is the same rule pattern already used by Protagen Smasher.

## Source inconsistencies and unresolved interactions

These must be taught as source ambiguities. Do not invent a ruling.

### 1. Justicar / Justiciar

- Contract 4186 on PDF pp.24–25 spells the target **Justicar Julius**.
- The Custodia roster on PDF p.39 spells the unit **Justiciar Julius** and names the aura after Justiciar.
- Treat this as one character with inconsistent source spelling. Preserve each spelling when citing its own surface; add an explicit alias note in teaching material.
- **Finding:** **PASS — High confidence source inconsistency.**

### 2. Directed Energy / Focused Energy

- The p.40 weapon heading is **Directed Energy**.
- Its backlash sentence refers to the unit using **Focused Energy**.
- No separate Focused Energy profile appears.
- The safest documentation is “Directed Energy (called Focused Energy once in its ability text)” with no invented distinction.
- The rule also says it ignores armor but assigns backlash per critical hit. Because normal critical damage is established during the armor/damage roll that this weapon may skip, the source does not identify which die supplies that critical.
- **Finding:** **PASS — ambiguity preserved, High confidence.**

### 3. Hand Flamethrower ammunition

- The p.39 profile shows ammunition 3 and no reload cost.
- Its ability says it never needs reloading.
- Core rules normally spend one ammunition after every shooting action and forbid shooting at zero.
- The book does not say whether “never needs reloading” means infinite ammunition, automatic replenishment, or three lifetime shots with no reload action.
- **Finding:** **PASS — unresolved contradiction, High confidence.**

### 4. Inspiration ordering

- Inspiration creates 1-AP activations for units that already activated.
- Those activations occur after all ordinary activations on both sides and before round end.
- The book does not define ordering when both players have Inspired units, ordering among several Inspired units, whether initiative controls that sequence, or whether players alternate.
- “All other units” is unclear when multiple Inspired units are each waiting for the same delayed window.
- The text does not say whether one unit can receive Inspiration more than once in a round, though the 2-AP option must choose two different units.
- It also does not address an Inspired unit being killed before its delayed activation.
- **Finding:** **PASS — timing gap preserved, High confidence.**

### 5. Overwatch trigger gap

- The general p.10 rule says an enemy action in range triggers Overwatch.
- The p.11 trigger list names shooting, movement, melee, both lock exits, equipment use, and reloading.
- The list omits ability use and map interaction; Pass is separately stated not to trigger.
- MDR Order and Custodia Inspiration/Choke are AP-costed abilities, but the rules do not resolve whether the broad p.10 sentence or the narrower p.11 list controls.
- Existing shipping text that calls the p.11 list exhaustive is too strong and should be corrected.
- Directed Energy is separately barred from being the weapon used for Overwatch; that restriction does not resolve whether activating another ability triggers enemy Overwatch.
- **Finding:** **PASS — rules gap confirmed, High confidence.**

### 6. Stacked Agility reductions and floor

- Core rules cap Agility bonuses at 5.
- They state no minimum Agility and no general order for applying bonuses and reductions.
- Justiciar's Influence and Marksman's/Sniper-style reductions expose the missing lower-bound rule. Future or mixed effects could stack.
- Do not add a floor of 1 or decide that reductions cannot stack without publisher clarification.
- **Finding:** **PASS — missing floor/order confirmed, High confidence.**

### 7. End-of-round ordering

The only global sequence is:

1. all end-of-round unit effects;
2. scenario effects;
3. VP calculation.

That establishes that Protocol effects such as Hunt resolve after unit effects and before scoring. It does not order simultaneous unit effects:

- Combat Medic healing;
- Burning damage and removal;
- Tormentor's Influence damage;
- Choke damage.

Material outcomes can depend on that order. Examples include healing before or after damage, a Tormentor dying to Burning before Choke resolves, and whether Choke ends immediately enough to prevent its own round-end damage. Protocol/scenario damage then follows, but the rules also do not fully place Overwatch-token cleanup or contract draws relative to every other cleanup step.

Inspiration is a delayed activation after ordinary activations, not expressly an end-of-round unit effect, so it should resolve before entering this sequence; the exact handoff remains implicit.

- **Finding:** **PASS — partial order verified, internal ordering unresolved.**

### 8. Equipment and pickup restrictions

Core rules allow one carried item unless a unit rule says otherwise, and only a unit with no equipment can pick up a dropped item.

New exceptions:

- Grenadier and Assassin start with two grenades and cannot take other equipment.
- Combat Medic starts with one medkit and cannot take other equipment.
- Punisher and Confessor cannot carry equipment and cannot be healed by medkits.
- A medkit removes Burning.

Unresolved cases:

- Whether “cannot take other equipment” remains a permanent pickup ban after all starting items are consumed.
- Whether both grenades are dropped as separate tokens when a two-grenade carrier dies; core wording discusses a singular carried token.
- Whether a partially spent two-grenade load still counts as carrying equipment for pickup.
- Whether a medkit can remove Burning from Punisher or Confessor despite their medkit-healing immunity.
- Whether one medkit use both restores HP and removes Burning, or must choose one effect.

Do not silently resolve these in equipment guidance.

- **Finding:** **PASS — restrictions captured, interactions unresolved.**

### Additional profile questions

- Sergeant 139's aura says friendly units within range improve melee penetration “to −1.” It reads as setting the value, not applying a −1 modifier, but it does not define what happens to a profile already better than −1 or whether “friendly units” includes the Sergeant.
- The Comms relay requires the Operator to be within 7 inches of the Sergeant but states no line-of-sight requirement. It does not expressly discuss the Sergeant being destroyed.
- Burning affects the target and “all units” within 2 inches; the text does not exempt allies or the Cremator.
- Choke says a unit can receive it once. It is unclear whether that means once at a time, once per Tormentor, or once per game.
- The Lancer creates Melee Lock at 1 inch without base contact, but the general multi-lock escape procedure was written around touching bases. Apply the printed exception without inventing new movement geometry.

## Affected-file recommendations

### Must change for the v0.8.9 rules upgrade

- `games/the_warcode/rules/Rulebook_Quotes.md`
  - Add v0.8.9-F provenance and pp.37–40 under approved quote policy.
  - Preserve stable citations for unchanged pp.2–36.
  - Record Justicar/Justiciar and Directed/Focused naming inconsistencies.
- `games/the_warcode/factions/mdr/README.md`
  - Replace the marketing-only stub with a verified roster overview.
- `games/the_warcode/factions/mdr/Squad_Datasheet.md`
  - Add the eight profiles from PDF pp.37–38.
- `games/the_warcode/factions/dominium/README.md`
  - Replace the marketing-only stub; identify Custodia Silens as the playable formation.
- `games/the_warcode/factions/dominium/Squad_Datasheet.md`
  - Add the eight profiles from PDF pp.39–40.
- `games/the_warcode/rules/Activation_and_AP.md`
  - Replace the stale “no printed extra-AP unit” question with Order and Inspiration.
  - Preserve the Inspiration ordering gap.
- `games/the_warcode/rules/Combat_Ranged_and_Melee.md`
  - Retract the claim that the Overwatch list is exhaustive.
  - Add Directed Energy, Hand Flamethrower, Burning, Agility-floor, and Lancer exceptions.
- `games/the_warcode/rules/Equipment_Loot_and_Doors.md`
  - Add the new loadout/carry restrictions and unresolved pickup/Burning interactions.
- `games/the_warcode/rules/Turn_Structure.md`
  - Add the Inspiration window and explicit unresolved ordering among Medic, Burning, Choke, and Influence before Protocol/scenario effects.

### Refresh for four-faction accuracy

- `games/the_warcode/README.md`
- `games/the_warcode/rules/Overview.md`
- `games/the_warcode/rules/Key_Concepts.md`
- `games/the_warcode/rules/Keyword_Glossary.md`
- `games/the_warcode/Quick_Reference_Play_Guide.md`
- `games/the_warcode/First_Game_Walkthrough.md`
- `games/the_warcode/guides/Proxy_Play_at_Home.md`
- `games/the_warcode/guides/Warcode_vs_That_Other_Game.md`
- `games/the_warcode/rules/Comparative_Glossary.md`

These surfaces should no longer imply that only Protagen and Ulfari are playable.

### Provenance-only or verification refresh

- `games/the_warcode/rules/Contract_Cards_Reference.md`
  - Card data is unchanged; update current-source provenance and add the spelling note.
- `games/the_warcode/rules/Contracts_and_VP.md`
  - Mechanics and deck are unchanged; remove “future roster” language.
- `games/the_warcode/rules/Protocol_Cards_Reference.md`
- `games/the_warcode/rules/Scenarios_and_Events.md`
- `games/the_warcode/setup/Board_Setup.md`
- `games/the_warcode/setup/Terrain_Basics.md`
  - Preserve rules content and sidecars; update current-source provenance.
- `games/the_warcode/factions/protagen_marines/README.md`
- `games/the_warcode/factions/protagen_marines/Squad_Datasheet.md`
- `games/the_warcode/factions/ulfari/README.md`
- `games/the_warcode/factions/ulfari/Squad_Datasheet.md`
  - Profiles are unchanged; record the v0.8.9-F equivalence check rather than rebuilding them.

### Later KB synchronization

Stage 5 should update the v0.8.9 source page, MDR and Dominium faction pages, affected AP/Overwatch/equipment/end-round concepts, glossary entries, overview, index, backlinks, and log. KB prose must remain paraphrased.

## Final confidence matrix

| Claim | Status | Confidence |
|---|---|---|
| Core rules unchanged | **PASS** | High |
| Contracts unchanged, complete 8×4 matrix | **PASS** | High |
| Protocol cards unchanged, 20-card corpus | **PASS** | High |
| Scenario unchanged | **PASS** | High |
| Six D6 VP layouts unchanged | **PASS** | High |
| Protagen profiles unchanged | **PASS** | High |
| Ulfari profiles unchanged | **PASS** | High |
| Only substantive addition is MDR pp.37–38 and Custodia pp.39–40 | **PASS** | High |
| Trailing art shifts from p.37 to p.41 | **PASS** | High |
| New roster ability coverage is complete | **PASS** | High |
| New numeric profile-column reconstruction | **PASS**, visual QA still required | Medium-high |
| Listed interaction ambiguities remain unresolved by the source | **PASS** | High |

## R1 sign-off

**PASS.** Proceed to the coordinator research gate using the locked delta above. Stage 2 may preserve all unchanged core/card/map/Protagen/Ulfari content, update provenance to v0.8.9-F, and concentrate substantive rules work on MDR Executive Unit, Custodia Silens, and the interaction warnings in this report.
