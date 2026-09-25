# Q1 — Rules / interactions QA

- **Track:** `warcode_kickstarter_refresh`
- **Stage:** 6 (independent rules/interaction QA)
- **Date:** 2026-09-24
- **Result:** **PASS** (remediation recheck 2026-09-24)
- **Prior result:** **FAIL** (first pass, same date)
- **Git:** not run. Implementation files not edited.

Independent visual check of **The-Warcode-Rulebook-V.0.8.9-F.pdf** pages **37–40** (PyMuPDF 3.5× page renders, 2×2 unit-card clips) plus native extract `raw/the_warcode/rulebook_v089f_extract.txt`, R1, impact matrix, AGENTS.md Sec 10 hierarchy, and all `games/the_warcode` rules/faction/setup teaching surfaces.

## Verdict

Roster numbers and quoted ability text for MDR Executive Unit and Custodia Silens match the **printed** profile columns. Hierarchy, 8×4 contracts, 20 protocols, and six D6 VP maps are intact. The slice **fails** because player-facing Overwatch teaching still treats the p.11 action list as complete, which the locked ambiguity register forbids.

## Check matrix

| Check | Result | Evidence |
|---|---|---|
| Visual PDF pp.37–40 vs MDR/Custodia datasheets (every core stat, weapon number, and printed ability) | **PASS** | Rendered cards; see profile tables below. Native extract column-flatten (`+11`, `-11`, flamethrower vs Volt Sword stacking) is **not** the printed layout. Teaching key is Shots · Range · …; printed icon order is Range · Shots · Shoot AP · Ammo · Reload AP · Pen · Dmg · Crit. Numbers match after that mapping. |
| Ambiguity register (8 items) explicit, no invented rulings | **FAIL** | Central register in `rules/Rulebook_Quotes.md` Sec 34 is complete and unresolved. `Combat_Ranged_and_Melee.md`, `Activation_and_AP.md`, `Turn_Structure.md` end-of-round, `Equipment_Loot_and_Doors.md`, and both datasheets preserve the gaps. **Conflict:** `Turn_Structure.md` Common mistakes still says Pass does not trigger Overwatch because “only the listed enemy actions do.” That re-asserts exhaustiveness. |
| Hierarchy: v0.8.9-F current; omission is not a patch; lore not mechanics | **PASS** | `games/the_warcode/README.md` H1; `Rulebook_Quotes.md` provenance lock; lore spine not used as rules. |
| 8×4 contract matrix | **PASS** | `Contract_Cards_Reference.md` IDs 4186, 9278, 5039, 6037, 3697, 4913, 3512, 2984; all 1 VP; four faction columns match `contract_cards_transcription.txt`. Card 4186 keeps **Justicar Julius**. |
| 20 protocol equivalence | **PASS** | `Protocol_Cards_Reference.md` 20 rows: Magnet/Hunt/Electricity/Silence/Poison × Left/Centre/Right/Total. Hunt full-health OCR caution retained. Body records v0.8.9-F card-art equivalence. |
| Six D6 VP layouts | **PASS** | `Board_Setup.md` D6 1–3 / 4 / 5 / 6 token counts; inch tables still keyed to `Core_Machine_obj_placement.png`. `Rulebook_Quotes.md` Sec 28 still says six labeled layouts. Flattened p.27 extract still lists 33'', 24'', 11,5'', 14'', 8'', 7,5'', 2,5'', etc. |
| Sample stable pp.2–36 citations vs current extract | **PASS** | SETUP p.2, GAME PHASES / END OF THE ROUND p.3, Overwatch p.10, p.11 trigger list, RANDOM VP PLACEMENT p.27 — wording matches `rulebook_v089f_extract.txt` (ligature `fi` normalized in quotes). Historical v0.8.7-F citation filenames remain under the pp.2–36 equivalence lock. |
| Stale “current = v0.8.7” / two-playable-faction claims | **FAIL (hygiene)** | No remaining claim that MDR/Custodia are unplayable. README, Overview, Proxy Play, walkthrough, Contracts all name four playable squads. TTS v0.8.7 is correctly a Workshop-drift warning. **Stale headers/tables:** `Keyword_Glossary.md` still says `REFERENCE_STATUS: … v0.8.7-F` and “Paraphrased from the v0.8.7-F extract” / read **2026-08-23** while the H1 is v0.8.9-F. Same header drift on Overview, Key_Concepts, Comparative_Glossary, Protocol_Cards_Reference, Scenarios_and_Events, Board_Setup UPDATE_TRIGGER, Quick_Reference read date. |
| GW proper-noun ban under `games/the_warcode/**` | **PASS** | Case-insensitive scan: 0 matches for Kill Team, Warhammer, 40,000, 40K, 40k. |
| Rules Markdown links | **PASS** | 319 relative `.md` / raw image links under `games/the_warcode/**/*.md` resolved; 0 missing. |

## Visual profile audit (PDF pp.37–40)

Printed folio in the page corner is one lower than the PDF page (p.37 shows **36**, p.40 shows **39**), matching R1.

### MDR Executive Unit

| Unit | PDF | Visual core HP / A / Armour / M | Visual ranged (Range, Shots, Shoot AP, Ammo, Reload AP, Pen, Dmg, Crit) | Visual melee (Range, Str, AP, Pen, Dmg, Crit) | Datasheet | Result |
|---|---:|---|---|---|---|---|
| Sergeant 139 | 37 TL | 9 / 3 / 3 / 6 | Large-Caliber Pistol 6, 5, 1, 2, 1, −1, 1, 2 | Volt Sword 1, 4, 1, 0, 2, 3 | HP 9 · A 3 · M 6 · Armour 3; pistol 5 · 6" · 2 · 1 AP · 1 AP · −1 · 1/2; sword 4 · 1" · 1 AP · 0 · 2/3 | **PASS** |
| Combat Medic | 37 TR | 8 / 3 / 3 / 6 | Rifle 7, 3, 1, 2, 1, 0, 2, 3 | Bayonet 1, 3, 1, 0, 2, 3 | Rifle 3 · 7" · 2 · 1 AP · 1 AP · 0 · 2/3; Bayonet 3 · 1" · 1 AP · 0 · 2/3 | **PASS** |
| Grenadier | 37 BL | 8 / 3 / 3 / 6 | Rifle same | Bayonet same | same | **PASS** |
| Machine Gunner | 37 BR | 8 / 3 / 3 / 6 | LCMG 6, 2, 1, 3, 1, −1, 3, 4 | Combat Knife 1, 2, 1, 0, 2, 3 | 2 · 6" · 3 · 1 AP · 1 AP · −1 · 3/4; knife 2 · 1" · 1 AP · 0 · 2/3 | **PASS** |
| Corporal | 38 TL | 8 / 3 / 3 / 6 | Rifle / Bayonet | as shared | as shared | **PASS** |
| Comms Operator | 38 TR | 8 / 3 / 3 / 6 | Rifle / Bayonet | as shared | as shared | **PASS** |
| Private | 38 BL | 8 / 3 / 3 / 6 | Rifle / Bayonet | as shared | as shared | **PASS** |
| Marksman | 38 BR | 8 / 3 / 3 / 6 | Rifle / Bayonet | as shared | as shared; Sniper title omitted in datasheet prose, present on card and in `Rulebook_Quotes.md` | **PASS** (title omitted, numbers OK) |

Sergeant printed abilities match quotes: Leader 2 re-roll points; melee AP **to −1** for friendly units within 7"; Order 1 AP once per round to **one unit** within 7" that has not activated; cannot while in melee; +1 AP until round end; order token; Comms extends range. Datasheet/Activation insert **friendly** on Order. That is supported by core p.4 (“extra AP to another **friendly** unit”), not treated as an invented ruling.

### Custodia Silens

| Unit | PDF | Visual core | Visual weapons | Datasheet | Result |
|---|---:|---|---|---|---|
| Justiciar Julius | 39 TL | 9 / 3 / 3 / 6 | LCP 6,5,1,2,1,−1,1,2; knife 1,2,1,0,2,3 | matches; Influence 6" + LoS −1 Agility | **PASS** |
| Assassin | 39 TR | 8 / 3 / 3 / **7** | LCP / knife same | M 7; 2 grenades, no other equipment | **PASS** |
| Punisher | 39 BL | **10 / 2 / 4 / 5** | Heavy 8,4,2,1,1,−2,2,3; Maul 1,3,1,0,2,3 | 4 · 8" · 1 · **2 AP** · 1 AP · −2 · 2/3 | **PASS** |
| Cremator | 39 BR | 8 / 3 / 3 / 6 | Flamethrower **5,2,1,3,—,0,2,4**; Volt Sword 1,4,1,0,2,3 | 2 · 5" · ammo 3 · 1 AP · reload — · Pen 0 · 2/4; never-reload / Burning / Volt re-roll-1s on the **correct** weapons (extract attached never-reload to the sword) | **PASS** |
| Executor | 40 TL | 8 / 3 / 3 / 6 | Shotgun 5,2,1,2,1,−1,3,4; knife 1,2,1,0,2,3 | 2 · 5" · 2 · 1 AP · 1 AP · −1 · 3/4 | **PASS** |
| Lancer | 40 TR | 8 / 3 / 3 / 6 | Spear 1,4,1,−1,2,3 | 4 · 1" · 1 AP · −1 · 2/3; 1" Melee Lock without base contact | **PASS** |
| Confessor | 40 BL | **7 / 2 / 3 / 6** | Fist 1,1,1,+1,1,2 | matches; medkit/equipment ban; Inspiration text | **PASS** |
| Tormentor | 40 BR | **7 / 3 / 2 / 6** | Directed Energy **8,3,1,—,—,—,2,3**; Fist same | 3 · 8" · ammo — · 1 AP · reload — · Pen — · 2/3; Focused Energy in backlash; Influence 5" no LoS; Choke | **PASS** |

## Ambiguity register (impact matrix)

| Item | Explicit / unresolved? | Notes |
|---|---|---|
| Justicar vs Justiciar | **PASS** | Quotes register; Contracts table; Custodia datasheet name note. |
| Directed Energy vs Focused Energy | **PASS** | Visual heading **DIRECTED ENERGY**; backlash “Focused Energy”; Combat + quotes + datasheet. Critical-source gap retained. |
| Hand Flamethrower ammo 3 vs never reloads | **PASS** | Visual ammo **3**, reload **—**, ability “Never needs reloading.” Datasheet source gap. |
| Inspiration ordering / repeat target | **PASS** | Activation_and_AP, Turn_Structure, Custodia datasheet. |
| Ability use vs Overwatch p.10 vs p.11 | **FAIL** | Correct in Combat, Activation, Key_Concepts, Keyword_Glossary Overwatch row, Custodia datasheet. **Wrong** in `Turn_Structure.md` line ~154. **Too narrow** in `Quick_Reference_Play_Guide.md` (“Triggers on enemy move in LoS”) and `First_Game_Walkthrough.md` action table. |
| Agility floor / stacking order | **PASS** | Combat “New ranged exceptions”; Custodia shared gaps; Key_Concepts. |
| End-of-round Medic / Burning / Influence / Choke | **PASS** | Turn_Structure checklist + open questions; quotes register. |
| Equipment pickup / multi-grenade drop / medkit vs Burning / Punisher-Confessor | **PASS** | Equipment_Loot_and_Doors “Burning and medkits” + loot paragraph; MDR datasheet equipment ambiguities. |

Additional printed gaps (Sergeant “to −1”, Comms no LoS / dead Sergeant, Burning hits all units, Choke “once”, Lancer vs multi-lock geometry) remain flagged. No QA ruling invented.

## Sample pp.2–36 citations

| Cite | Shipping | Current extract | Result |
|---|---|---|---|
| p.2 SETUP | three numbered steps, D6 deploy, equipment after deploy | `rulebook_v089f_extract.txt` PDF PAGE 2 | **PASS** |
| p.3 END OF THE ROUND | unit effects → scenario effects → VP | PAGE 3 | **PASS** |
| p.10 Overwatch | move into range **or takes action** already in range | PAGE 10 | **PASS** |
| p.11 trigger list | Shooting, Movement, Melee, Disengage, Escape, Equipment, Reloading | PAGE 11 | **PASS** |
| p.27 random VP | one D6, all scenarios, Core of the Machine example, 33'' × 24'' | PAGE 27 heading + size callouts | **PASS** |

## Must-fix

1. **`games/the_warcode/rules/Turn_Structure.md`** — Common mistakes row “only the listed enemy actions do.” Align with Combat/Activation: Pass is safe; p.11 is not proven exhaustive for abilities/map interaction.
2. **`games/the_warcode/Quick_Reference_Play_Guide.md`** — Overwatch note currently only “enemy move in LoS.” At least point at the p.11 list **and** the unresolved ability-use gap (or drop a false exclusive trigger).
3. **`games/the_warcode/First_Game_Walkthrough.md`** — same Overwatch one-liner as the QR.

## Should-fix (does not by itself fail the numeric/roster pass)

4. Refresh **Keyword_Glossary** (and other files still advertising `REFERENCE_STATUS: … v0.8.7-F` / “paraphrased from v0.8.7-F” / read 2026-08-23) so the living current baseline is unambiguously v0.8.9-F with pp.2–36 equivalence, not a leftover current-v0.8.7 table.
5. Datasheet Marksman: restore printed **Sniper —** ability name (quotes already have it).
6. `Activation_and_AP.md` trap “Overwatch costs the activation, not 1 AP” fights p.10’s 1 AP cost; reword to “locks the rest of the activation.”
7. `Equipment_Loot_and_Doors.md` grenade-reach aside (“only the rifle and heavy weapon beat it”) omits Custodia Directed Energy 8".

## Out of scope / not failed

- Lore, campaign, KB, Gamefound/Kickstarter pages.
- Protocol Hunt OCR vs xlsx (already flagged).
- Total-card “this room” vs all-rooms map (already flagged).
- Default round count absent from PDF (already flagged in quotes gaps).

## Remediation recheck — 2026-09-24

Coordinator remediations reviewed against current `games/the_warcode` surfaces. Visual pp.37–40 profile PASS from the first pass was not re-rendered; numeric tables above still stand.

| Item | Recheck | Evidence |
|---|---|---|
| Must-fix 1 `Turn_Structure.md` Overwatch exhaustive claim | **PASS** | Common mistakes now: “Pass does not trigger Overwatch. Page 11 lists other triggers, but ability use and map interaction are not resolved by the source.” Open questions still list Inspiration and unit-effect order. |
| Must-fix 2 `Quick_Reference_Play_Guide.md` Overwatch one-liner | **PASS** | Activation table: page 11 list (shooting, movement, melee, lock exits, equipment, reloading); Pass does not trigger; ability/map-interaction unresolved. |
| Must-fix 3 `First_Game_Walkthrough.md` Overwatch one-liner | **PASS** | Same unresolved-ability/map wording; Pass still does not trigger. |
| Should-fix 4 stale v0.8.7 current headers | **PASS** with residual | `REFERENCE_STATUS` on Keyword_Glossary, Overview, Key_Concepts, Comparative_Glossary, Protocol_Cards_Reference, Scenarios_and_Events, Board_Setup now name **v0.8.9-F**. Glossary how-to-read is “Paraphrased from the v0.8.9-F baseline.” UPDATE_TRIGGER on those rules pages now supersedes **v0.8.9-F**. Residual: Quick Reference `UPDATE_TRIGGER` still says “supersedes v0.8.7-F”; QR / Keyword_Glossary body / First_Game `REFERENCE_STATUS` still carry **read 2026-08-23** while H1/sources already point at v0.8.9-F. Change-log v0.1 rows remaining historical are fine. No two-faction / unplayable-MDR claims. |
| Should-fix 5 Marksman **Sniper** title | **PASS** | `factions/mdr/Squad_Datasheet.md`: “**Sniper:** when Marksman shoots…” |
| Should-fix 6 Activation Overwatch trap wording | **PASS** | “Overwatch costs 1 AP and locks the rest of that unit's activation.” |
| Should-fix 7 grenade reach vs Directed Energy | **PASS** | Equipment: rifle 7"; heavy weapon and Directed Energy 8". |
| Ambiguity register (8 items) | **PASS** | `Rulebook_Quotes.md` Sec 34 register unchanged and unresolved. Combat, Activation, Equipment, Turn_Structure, both datasheets still flag gaps. Overwatch teaching no longer contradicts the register. |
| Links | **PASS** | 323 relative links under `games/the_warcode/**/*.md`; 0 missing. |
| GW proper-noun ban | **PASS** | 0 matches for banned comparator names. |

### Recheck matrix (failed rows only)

| Original check | First pass | Recheck |
|---|---|---|
| Ambiguity register / Overwatch exhaustiveness | **FAIL** | **PASS** |
| Stale current-v0.8.7 / two-faction hygiene | **FAIL (hygiene)** | **PASS** (QR trigger/date leftovers noted, not load-bearing) |

### Final verdict

**PASS.** Must-fix Overwatch contradictions are gone. Should-fix roster title, AP trap, grenade reach, and living v0.8.9-F headers are in place. Residual Quick Reference UPDATE_TRIGGER / 2026-08-23 draft dates do not restore a “current = v0.8.7” player claim.
