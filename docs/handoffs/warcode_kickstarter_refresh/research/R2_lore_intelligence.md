# R2 lore intelligence — Tactical Doctrine Field Edition

- **Track:** `warcode_kickstarter_refresh`
- **Researcher:** R2
- **Date:** 2026-09-24
- **Status:** Complete — ready for coordinator gate
- **Primary source:** `raw/the_warcode/The-Warcode-Lorebook-Tactical-Doctrine-Field-Edition.pdf`
- **Extraction check:** `raw/the_warcode/lorebook_tactical_doctrine_field_edition_extract.txt`
- **Source authority:** Narrative context only. It does not establish or override mechanics.
- **Citation convention:** All page references below are PDF pages, not the printed page number, which is generally one lower.

## Executive findings

1. The lorebook is an academy dossier designed to teach source criticism. Its introduction explicitly says political, historical, and ideological passages are primary-source documents rather than academy conclusions. Faction-authored prose must therefore be presented as interested testimony, not neutral canon. (PDF p.3, Section 1, “Information Environment” and “Source Methodology”.)
2. The stable setting spine is a single-star theatre divided among Dominium on Erda, MDR on Huoxing and parts of the middle system, and Protagen in the Abyron Belt, with contested infrastructure extending through the Kirkwood Belt and Cassini system. No faction controls the whole theatre. (PDF pp.3–5, Section 2.)
3. The Erdan calendar uses 28-hour days, 39-day months, 12-month years, and 468-day years. Year 0 is Dominium’s appearance; the five post-zero epochs run Foundation, Burning, Golden Age, Blackout, and Arrival. (PDF p.5, Section 3.1.)
4. “Blackout,” “Blackout War,” and “Silence War” are related but not interchangeable. Blackout is the policy, epoch, and initiating event; Blackout War appears as a historical-source label for the resulting conflict; Silence War is used in anti-Dominium factional accounts. (PDF pp.5, 20, 22, 26, 30, Sections 3.1, 3.6, 4–6.)
5. Huoxing is a planet at 1.91 AU. Mars is a settlement in the Kirkwood Belt where the MDR founding congress met. They are not alternate names for one place. (PDF pp.5, 29–30, Sections 2 and 6.)
6. MDR has only partial control of Cassini’s moon system, while Protagen maintains bases on some Cassini moons. These claims describe overlapping presence, not a contradiction and not exclusive control by either faction. (PDF pp.5, 25, Sections 2 and 5.)
7. Custodia Silens is a Dominium formation, not a synonym for the entire faction. The lorebook identifies its litany and a detachment sent to Erebus-7; current rulebook pp.39–40 supply the playable roster. (Lorebook PDF pp.25, 37, Sections 4 and 7; Rulebook v0.8.9-F PDF pp.39–40, “Team List — Custodia Silens”.)
8. The pre-launch claim that Ulfari destroyed a station without warning conflicts with the lorebook’s Dominium internal file: Erebus-7 first shows non-hostile contact, after which Dominium orders witness elimination, evidence destruction, and forced hostility. The marketing claim must not be retained as settled history. (Lorebook PDF pp.35–37, Section 7; pre-launch-derived claim currently recorded in `games/the_warcode/factions/ulfari/README.md`, retrieved 2026-08-23.)
9. “Tactical Application” does not add rules. It redirects practical squad instruction to the accompanying rulebook. All AP, squad, weapon, morale, scenario, and other mechanics must be sourced from Rulebook v0.8.9-F. (Lorebook PDF p.40, Section 8.)

## 1. Academy frame and source methodology

### What the academy claims

The Warcode presents itself as a military academy producing officers who can act across varied theatres. The Field Edition is issued as pre-command preparation and combines theatre geography, history, faction material, and a pointer to practical instruction. (PDF p.3, Section 1, “The Warcode” and “Tactical Doctrine: Field Edition”.)

The academy describes the system’s information environment as deliberately degraded by centuries of conflict. It warns that no single source—including a friendly source—provides a complete political, historical, or ideological picture. (PDF p.3, Section 1, “Information Environment”.)

Most importantly, it states that political, historical, and ideological material is not presented as academy assessment. The dossier reproduces primary-source documents from factions so candidates can extract intelligence from unreliable material. (PDF p.3, Section 1, “Source Methodology”.)

### Working evidence hierarchy

Use the following hierarchy in the shipping lore spine:

1. **Academy structural statements:** geography, calendar, epoch boundaries, section introductions, and direct descriptions outside attributed inserts. Treat as the dossier’s baseline, while still naming the academy as compiler.
2. **Authenticated records and dated instruments:** ultimatums, manifests, internal memoranda, intercepted transmissions, and archival testimony. Treat as evidence that the document or statement exists; do not automatically accept every assertion inside it.
3. **Faction-authored primary sources:** speeches, sermons, press interviews, public addresses, military briefings, and internal analyses. Attribute every claim and identify institutional interest.
4. **Named scholarship and commentary:** historians, analysts, lectures, monographs, blogs, and essays. Preserve affiliation and distinguish evidence from interpretation.
5. **Project synthesis:** use cautious language such as “the dossier establishes,” “the source claims,” “the account implies,” and “the sources conflict.” Never present project inference as canon.

### Source-affiliation hazards

- Page 3 provides a visual source-affiliation legend, but native extraction does not reliably preserve all icon-to-passage associations. Prefer the written attribution beneath each extract over inferred icon placement. (PDF p.3, Sections 1–2.)
- “Independent” appears inside some source titles or affiliations; it is a source’s self-description, not proof of neutrality.
- Internal Dominium records on first contact are unusually probative because they conflict with Dominium’s later public line, but they remain a Dominium file selected by an unknown compiler. (PDF pp.35–37, Section 7.)
- The academy’s unattributed connective prose is more stable than faction speeches, but the academy never claims omniscience.

### Shipping recommendation

`games/the_warcode/lore/Source_Methodology.md` should lead with a compact “how to read this book” box:

- academy frame is not an omniscient narrator;
- faction documents are biased primary sources;
- attribution is part of the evidence;
- contradictions are intentional intelligence problems;
- mechanics always defer to Rulebook v0.8.9-F.

Do not describe every passage as equally unreliable. Separate direct observations, institutional claims, and later interpretation.

## 2. Theatre geography page map

### Inner system

- **Erda — 1.00 AU:** only naturally habitable world; approximately 50 billion people; Dominium controls the planet, holds orbital superiority, and monopolizes access to space. (PDF p.4, Section 2, “Erda”.)
- **Kepler and Hydron:** named among four inner planets but not further characterized in this edition. Do not invent ownership, environment, or settlements. (PDF p.3, Section 2, “Inner Orbits”.)
- **Huoxing — 1.91 AU:** sealed human infrastructure in a carbon-dioxide atmosphere at 0.8 bar; controlled by MDR. MDR reach extends through near space toward Cassini, but its Cassini moon control is explicitly partial. (PDF p.5, Section 2, “Huoxing”.)

### Middle and outer system

- **Kirkwood Belt — 2.5–3.8 AU:** industrial extraction belt contested by several factions; no authority continuously controls it. (PDF p.5, Section 2, “Kirkwood Belt”.)
- **Mars:** the largest Kirkwood settlement at the time of the MDR’s year-1689 founding congress. It is a settlement, not Huoxing and not a second name for the planet. (PDF p.30, Section 6, “Founding of the MDR”.)
- **Cassini — 6.2 AU:** a gas giant whose moon system has overlapping MDR and Protagen presence. MDR has partial control; Protagen has bases on moons. The source does not map individual moons or borders. (PDF pp.5, 25, Sections 2 and 5.)
- **Abyron Belt — 18–40 AU, densest at 22–30 AU:** Protagen’s main region; stations are widely dispersed, including off-ecliptic locations, making surveillance and force projection difficult. (PDF p.5, Section 2, “Abyron Belt”.)
- **Erebus-7:** decommissioned Protagen deep-range carrier in far orbit outside the ecliptic; location of the documented first-contact image and subsequent Dominium suppression order. It is a vessel, not clearly a station. (PDF pp.35–37, Section 7.)

### Operational synthesis

The theatre is an asymmetric geography:

- Dominium has the population and gravity-well center on Erda.
- MDR occupies the main inhabited middle-system counterweight, with Huoxing as a planetary base and incomplete reach into Cassini.
- Protagen turns distance, dispersed stations, off-ecliptic positions, and outer-system resources into strategic depth.
- The Kirkwood Belt and Cassini system should be written as contested or overlapping spaces.
- The academy explicitly concludes that no faction can control the entire theatre. (PDF p.5, Section 2, “Summary”.)

### Shipping recommendation

`Theatre_of_Operations.md` should include a simple inward-to-outward route:

Erda → Kepler/Hydron/Huoxing → Kirkwood Belt/Mars → Cassini and moons → Abyron Belt/off-ecliptic sites.

Add two warning callouts:

- **Huoxing ≠ Mars:** Huoxing is a planet; Mars is a Kirkwood settlement.
- **Cassini is divided:** MDR partial control does not erase Protagen moon bases.

Do not add a precise spatial map beyond the distances supplied by the source.

## 3. Erda calendar and historical epochs

### Calendar

- 28 hours per day.
- 39 days per month.
- 12 months per year.
- 468 days per year.
- Year 0 begins with the appearance of Dominium on Erda.
- Pre-Dominium dates are negative years; later dates use the five named epochs. (PDF p.5, Section 3.1, “Chronological Framework”.)

The ultimatum’s timestamp, `34.03.247, 12:00`, is consistent with the 39-day month and provides a useful calendar example. (PDF p.11, Section 3.4.1.)

### Epoch 0 — Industrial Era, pre-zero

Erda consists of many competing industrial nation-states using analog-mechanical and electromechanical systems without a digital revolution. Records are fragmentary and duration is unknown. (PDF pp.5–6, Sections 3.1–3.2.)

### Epoch 1 — Foundation, years 0–238

Dominium appears as a technologically superior city-state of unknown origin. It builds security through trade and three allied buffer states, restricts deeper access, and is underestimated by outsiders. (PDF pp.5, 7, Sections 3.1 and 3.3.)

### Epoch 2 — The Burning, years 238–380

Global nuclear war begins among Erda’s states. Dominium ends nuclear production by force, then subjugates the planet and presides over a long pacification. The academy gives three operational phases: nuclear conflict, continental/subjugation conflict, and attrition/pacification. (PDF pp.5, 8–16, Sections 3.1 and 3.4.)

Key anchors:

- year 238: first nuclear use;
- 34.03.247: Dominium ultimatum;
- 05.11.248: Manifest of Dominium;
- year 303: official universal submission;
- year 380: last regional conflict and conventional start of peace. (PDF pp.9, 11, 13, 16, Section 3.4.)

### Epoch 3 — Golden Age, years 380–1648

Dominium rules as a planetary authority while humanity expands across the system. Sources disagree sharply over whether this was peaceful prosperity, corporate domination, or oligarchic control. The Father and Mother later adopt a 50-year cryosleep and succession cycle centered on the Sed Festival. (PDF pp.5, 17–19, Sections 3.1 and 3.5.)

### Epoch 4 — Blackout, years 1648–2026

Dominium imposes system-wide isolation. Protagen resistance begins in the Abyron Belt; asteroid attacks and prolonged outer-system warfare weaken central authority; conflict returns to Erda; Dominium uses shielding and cloning to restore planetary control; middle-system settlements eventually form MDR. The war never formally ends but declines to local engagements by 2026. (PDF pp.5, 20–22, Sections 3.1, 3.6, and 4.)

Key anchors:

- year 1648: Blackout announced;
- year 1689: station congress aboard Mars establishes MDR’s governing council and grants Martin one-year military authority;
- year 2026: low-intensity standoff disrupted by confirmed Ulfari contact. (PDF pp.20, 30, 5 and 35, Sections 3.6, 6, 3.1, and 7.)

### Epoch 5 — Arrival, year 2026/present

The academy defines Arrival as first confirmed contact with external intelligence, identified as Ulfari. The consequences remain unresolved. (PDF p.5, Section 3.1.)

### Chronology cautions

- Epoch endpoints share years: Foundation/Burning at 238 and Burning/Golden Age at 380. Write these as transition years unless the source later specifies day-level boundaries.
- The Burning is stated to last 142 years, but its listed phase durations are 9 + 56 + 86 = 151 years. The headings provide ranges of 238–247, 247–303, and 303–380, which yield 9 + 56 + 77 = 142 by simple subtraction. Treat “86 years” for the attrition phase on PDF p.8 as an internal numerical inconsistency or typo; do not reproduce it without a note.
- The Blackout epoch is listed as 378 years from 1648–2026, consistent by subtraction, but the war itself never formally ended. Epoch transition does not mean peace. (PDF pp.5, 21, Sections 3.1 and 3.6.)
- A source dated year 2001 appears inside the Golden Age discussion as retrospective commentary; its date falls during the Blackout epoch and should not be treated as a Golden Age contemporary account. (PDF p.17, Section 3.5, “Freedom to Leave”.)

### Shipping recommendation

`Historical_Timeline.md` should use the academy’s five-epoch scheme, include transition-year caveats, and flag the 86-year phase-duration inconsistency. Keep the first-contact conflict as a separate “contested account” box rather than forcing it into a single clean event.

## 4. Naming discipline: Blackout and Silence War

### Blackout

The term has three connected uses:

1. **Policy:** Dominium’s prohibition on communication and travel beyond the system, supported by signal suppression and control or destruction of long-range detection. (PDF p.22, Section 4.)
2. **Initiating event:** the year-1648 declaration that triggers civil war. (PDF p.20, Section 3.6.)
3. **Epoch:** years 1648–2026. (PDF p.5, Section 3.1.)

### Blackout War

This is the label used by a Meridian Institute historical monograph excerpt for the conflict beginning with Protagen resistance. (PDF p.20, Section 3.6, “The Blackout War: From Insurrection to Equilibrium”.)

### Silence War

This term occurs in factional material:

- Protagen describes defending independence and free speech during the Silence War. (PDF p.26, Section 5, “Our Right to the Galaxy”.)
- Protagen officer Orin Dey uses it when explaining Dominium’s suppression of Erda and Martin’s origin. (PDF p.30, Section 6, “A Weapon That Walked Away”.)
- Dominium language favors “the Silence” as sacred protective doctrine rather than using “Silence War” in the cited public address. (PDF pp.25, 39, Sections 4 and 7.)

### Shipping recommendation

Use **Blackout** for the policy/epoch, **Blackout War** for the cited historical-source label, and **Silence War** only when describing or quoting factional usage. A glossary note should say they concern the same long conflict but encode different political perspectives.

## 5. Faction intelligence and doctrine

### Dominium

#### Stable dossier facts

- Theocratic empire controlling Erda and its approximately 50 billion inhabitants across more than one hundred subordinate states. (PDF p.22, Section 4.)
- Enforces external isolation and controls information and access to space. (PDF pp.4, 22, Sections 2 and 4.)
- Governed symbolically by the Father and Mother, with cryosleep, representatives, and a 50-year succession ritual documented during the Golden Age. (PDF p.18, Section 3.5.)
- Uses Custodia Silens operationally; the lorebook names a pre-deployment litany and an Erebus-7 detachment. (PDF pp.25, 37, Sections 4 and 7.)

#### Ideology

Dominium frames itself as guardian of humanity and life against a hostile “Dark Forest.” It interprets obedience, isolation, and merciless action as protective duties. (PDF pp.13, 22, 25, 39, Sections 3.4, 4, and 7.)

#### Doctrine

- Strategic: central information control, system isolation, Erda orbital dominance, suppression of long-range contact.
- Historical: controlled release of superior technology; alliance proxies; later shielding, cloning, and mass force to restore planetary control.
- Information operations: seed false contact stories, arrange their debunking, divert public attention, provoke apparently organic conflict, destroy witnesses and records.
- Tactical lore signal: Custodia Silens is the enforcement arm sent to erase the first-contact event.

Evidence: PDF pp.7, 12–15, 21–22, 35–37, Sections 3.3–3.6, 4, and 7.

#### Bias and tension

Dominium public sources portray isolation as salvation. Its internal first-contact file says the non-hostile encounter threatens the ideological basis of Blackout and proposes fabrication, suppression, and engineered hostility. This is a central internal contradiction in Dominium’s stated doctrine. (PDF pp.35–39, Section 7.)

#### Custodia Silens shipping lock

Write **Dominium** as the faction/state and **Custodia Silens** as its playable formation. Lorebook evidence alone establishes an armed detachment, not game rules. Playability is established by the complete current roster in Rulebook v0.8.9-F, PDF pp.39–40, “Team List — Custodia Silens.”

### Protagen

#### Stable dossier facts

- Erdan-origin corporation that resisted Dominium from the Blackout’s opening.
- Became a state/confederation by uniting Abyron Belt stations.
- Uses dispersed and off-ecliptic infrastructure and maintains Cassini moon bases.
- Has limited population and resources but advanced military technology. (PDF pp.20, 25, Sections 3.6 and 5.)

#### Ideology

Protagen sources emphasize scientific progress, engineering, individual freedom, free communication, and expansion beyond the system. They portray Blackout as authoritarian control. (PDF p.26, Section 5, “Our Right to the Galaxy”.)

#### Doctrine

- Strategic depth through distance, dispersed sites, and guerrilla warfare.
- Exploitation of Erda’s vulnerability to redirected asteroids.
- Station autonomy until collective military or economic security is invoked.
- High-investment genetic and technological enhancement of Marines.

Evidence: PDF pp.20–21, 25–28, Sections 3.6 and 5.

#### Bias and tension

Protagen’s freedom narrative coexists with absolute central authority on “collective security” and severe material inequality. An MDR critic depicts survival as market-dependent; a Protagen scientist admits Marine investment comes at the cost of basic health elsewhere. These are critiques and admissions, not proof that every station follows one uniform model. (PDF pp.26, 28, Section 5.)

### MDR

#### Stable dossier facts

- Largest state beyond Erda by population and economic output.
- Formed from most stations on Huoxing, in the Kirkwood Belt, and on Cassini’s moons.
- Founded politically at a year-1689 congress aboard the Kirkwood settlement Mars.
- Authoritarian system led by Martin and a clone elite; its military is entirely composed of Martin clones differentiated by post-cloning experience. (PDF pp.29–30, Section 6.)

#### Ideology

MDR sources define the republic against Dominium tyranny and claim guarantees of basic rights and security superior to Protagen’s harsh autonomy. The dossier itself simultaneously labels MDR authoritarian. (PDF pp.26, 29–33, Sections 5 and 6.)

#### Doctrine

- Political unity around defense against expected Dominium reprisals.
- Clone continuity: accumulated lineage experience and identity.
- Executive Unit cohesion: members are variants of the same person and execute coordinated tactics with exceptional precision.
- Selective cloning creates specialized lineages for different combat roles.
- Energy shields support effective protection without heavy armor.

Evidence: PDF pp.30–34, Section 6.

#### Bias and tension

The account of Martin’s betrayal and Purification comes from Protagen and MDR voices; Martin’s own transmission is both testimony and threat. Dominium’s assessment of the Executive Unit is hostile-source military analysis, useful for perceived capability but not neutral proof. (PDF pp.30–34, Section 6.)

### Ulfari

#### Stable dossier facts

- The academy identifies Arrival in 2026 as first confirmed external intelligence.
- A Dominium internal image analysis reports a biologically non-human entity near four Protagen crew on Erebus-7, with non-hostile posture and no raised weapons.
- The same file assesses extra-system origin with high confidence.
- Later human reports describe Ulfari biotechnology and combat behavior. (PDF pp.5, 35–39, Sections 3.1 and 7.)

#### Doctrine, cautiously stated

A Dominium military briefing says observed Ulfari fighters prioritize individual skill and initiative, cooperate when needed, sometimes compete for dominance, attack aggressively, close to melee, exploit three-dimensional low/zero-gravity movement, and brutalize defeated opponents. This is an enemy assessment after Dominium ordered maximum hostility; it should be labeled as observed combat profile, not timeless species psychology. (PDF p.38, Section 7, “Ulfari Combat Profile”.)

#### Source gap

The dossier contains no clearly Ulfari-authored testimony. Every Ulfari motive is filtered through human observers:

- Dominium security and military institutions;
- Protagen scientists and writers;
- MDR anthropology;
- Dominium public propaganda.

Do not assign the Ulfari a confirmed political objective, native faction name, reason for entering the system, or responsibility for initiating hostilities.

#### Bias and tension

Dominium publicly calls Ulfari predatory proof of the Dark Forest, while its internal file records non-hostile first contact and an order to manufacture active conflict if necessary. MDR offers a contextual hypothesis rather than certainty; Protagen writing admires Ulfari biotechnology and speculates about panspermia. (PDF pp.35–39, Section 7.)

## 6. First-contact contradiction: required gate decision

### Marketing-era claim

The pre-launch-derived shipping text says Ulfari destroyed a station without warning and that this catalyzed the sealed-system war. The claim is currently preserved at `games/the_warcode/factions/ulfari/README.md` and traces to the pre-launch marketing source retrieved 2026-08-23. The assigned raw sources do not contain an archived page capture proving the exact wording, so the coordinator should require R3/source-ledger confirmation before quoting or closely paraphrasing it.

### Lorebook account

The Dominium internal file provides a materially different sequence:

1. Erebus-7 is identified as a decommissioned deep-range carrier, not expressly a station.
2. An authenticated image shows four Protagen crew near one unknown biological entity.
3. Both sides are described as non-hostile; no weapons are raised.
4. Dominium analysts conclude the entity is extra-system.
5. Dominium fears disclosure would validate Protagen and undermine Blackout.
6. Officials plan false stories, controlled debunking, distractions, and provocations.
7. Custodia Silens is ordered to eliminate all witnesses and records.
8. If the non-human cannot be killed, Custodia is ordered to attack with maximum hostility so later contact begins as open conflict.

Evidence: PDF pp.35–37, Section 7, “Dominium Security Chancellery — Internal Analysis — First Contact Event,” parts I–V.

### Assessment

These accounts cannot be merged into “Ulfari attacked without warning.” The lorebook supports:

- an initially non-hostile documented encounter;
- Dominium suppression and planned false-flag/escalation activity;
- later violent Ulfari combat observed by Dominium;
- no established chain proving who destroyed any station, whether Erebus-7 was destroyed, or who initiated the wider hostilities.

The internal Dominium file is strong evidence against Dominium’s public story, but it still does not prove that every later clash was engineered or that Ulfari remained peaceful.

### Shipping recommendation

- Remove the unqualified station-destruction lore hook from the Ulfari README.
- Replace it with a sourced “contested first contact” summary.
- Put the full comparison in `lore/Historical_Timeline.md` or `lore/Source_Methodology.md`.
- Preserve the older marketing claim as a dated publisher claim, not current canon.
- Do not call Erebus-7 a station unless another source does so explicitly.
- Do not label the suppression plan a completed operation beyond the deployment order; the file records orders and intended effects, not confirmed execution outcomes.

## 7. Contradictions, ambiguities, and hard limits

| Issue | Evidence | Assessment | Shipping handling |
|---|---|---|---|
| Ulfari station destruction vs Erebus-7 contact | Pre-launch-derived README; lorebook PDF pp.35–37, Section 7 | Direct narrative conflict; lorebook documents non-hostile contact and Dominium escalation orders | Present as contested; do not retain marketing claim as fact |
| Erebus-7 object type | PDF p.35 calls it a decommissioned carrier | Not identified as a station | Use “vessel” or “carrier” |
| Burning phase arithmetic | PDF p.8 says 9, 56, and 86 years; epoch is 142 years | Listed durations total 151; heading ranges imply final phase 77 years | Flag likely typo; do not silently correct source |
| Huoxing vs Mars | PDF pp.5 and 30 | Distinct planet and Kirkwood settlement | Add explicit terminology callout |
| MDR and Protagen at Cassini | PDF pp.5, 25, 29 | Overlapping claims: MDR partial/most-station relationship; Protagen bases | Describe shared/contested presence; avoid exclusive map |
| Blackout vs Blackout War vs Silence War | PDF pp.5, 20, 22, 26, 30 | Policy/epoch, historical war label, and factional war name | Preserve speaker and context |
| Custodia Silens scope | Lorebook pp.25, 37; Rulebook pp.39–40 | Dominium formation and current playable roster, not whole faction name | “Dominium — Custodia Silens formation” |
| Ulfari intent | PDF pp.35–39 | No Ulfari-authored source; human accounts conflict | Keep motives unknown |
| Sed Festival effects | PDF pp.18–19 | Testimony reports lasting unity; MDR psychologist implies abnormal cause without proving one | Do not state mind control as canon |
| Dominium origin | PDF pp.5, 7 | Unknown | Do not invent alien, time-travel, or precursor origin |
| Martin/Purification | PDF pp.30–33 | Faction testimony, no neutral corroboration in this edition | Attribute and avoid flattening into uncontested history |
| Tactical Application | PDF p.40 | Pointer to rulebook, not mechanics | Never cite lorebook for AP, abilities, weapons, or scenarios |

## 8. Quote-candidate ledger for later shipping

This `docs/` report remains paraphrase-only. The following are candidate passages for an implementer to quote under `games/the_warcode/lore/**`, where the scoped exception permits verbatim excerpts with filename, PDF page, and section.

| Priority | Candidate | PDF evidence | Best shipping use | Risk/control |
|---|---|---|---|---|
| Essential | Information environment warning | p.3, Section 1, “Information Environment” | `Source_Methodology.md` opening | Keep short; establishes uncertainty |
| Essential | Primary-source methodology | p.3, Section 1, “Source Methodology” | Explain faction-authored prose | Quote enough to retain “not Warcode assessment” meaning |
| Essential | Calendar and Year Zero | p.5, Section 3.1, “Chronological Framework” | `Historical_Timeline.md` | Facts can usually be paraphrased |
| High | Theatre summary: no full-system control | p.5, Section 2, “Summary” | `Theatre_of_Operations.md` | Strong concise framing |
| High | Dominium ultimatum | p.11, Section 3.4.1 | Timeline primary-source inset | Attribute as official Dominium instrument |
| High | Manifest’s protective/conquest framing | p.13, Section 3.4.1 | Dominium README ideology | Use a narrow excerpt; source is propaganda and law |
| High | Conflicting Golden Age views | pp.17–19, Section 3.5 | Methodology example | Pair opposing extracts rather than endorse one |
| High | Blackout policy definition | p.22, Section 4 | Timeline/theatre | Academy prose; concise definition |
| High | Custodia Silens litany | p.25, Section 4 | Dominium README | Attribute to Sacred Herald; faction devotional source |
| High | Protagen freedom/expansion statement | p.26, Section 5 | Protagen README | Attribute to corporate CEO and press service |
| High | Protagen Marine cost admission | p.28, Section 5 | Protagen README doctrine tension | Preserve speaker’s institutional affiliation |
| High | Martin transmission | p.33, Section 6 | MDR README | Strong voice; do not treat all claims as independently verified |
| High | Dominium assessment of Executive Unit cohesion | p.34, Section 6 | MDR README tactical-lore bridge | Hostile-source assessment; mechanics still from rulebook |
| Essential | Non-hostile Erebus-7 image finding | p.35, Section 7, part I | First-contact conflict box | Quote exact observation, not broader inference |
| Essential | Ideological threat memorandum | p.36, Section 7, part III | Explain suppression motive | Internal Dominium assessment |
| Essential | Information-noise plan | pp.36–37, Section 7, part IV | Source-methodology case study | Consider excerpts rather than full operational list |
| Essential | Custodia elimination/escalation order | p.37, Section 7, part V | First-contact conflict box | Distinguish order from confirmed execution |
| Medium | Protagen admiration of Ulfari biotechnology | pp.37–38, Section 7 | Ulfari README | Scientific interpretation, partly speculative |
| High | Ulfari combat profile | p.38, Section 7 | Ulfari README doctrine | Explicitly label Dominium hostile-source briefing |
| High | Dominium “Dark Forest” public address | p.39, Section 7 | Contrast public narrative with internal file | Pair with internal record; never standalone as neutral truth |
| Medium | MDR anthropologist’s caution | p.39, Section 7 | Ulfari README/source methodology | Hypothesis, not fact |
| Essential | Tactical Application redirect | p.40, Section 8 | `Source_Methodology.md` mechanics firewall | Short quote or paraphrase with rulebook link |

For every selected quote, cite:

`The-Warcode-Lorebook-Tactical-Doctrine-Field-Edition.pdf — PDF p.<n> — Section <n>, “<heading>”`

No `via OCR` marker is needed; the source ledger confirms native text on all content-bearing lore pages.

## 9. Proposed shipping allocation

### `games/the_warcode/lore/README.md`

- What the lorebook is.
- One-paragraph setting premise.
- Links to theatre, timeline, methodology, and faction READMEs.
- Mechanics firewall pointing to Rulebook v0.8.9-F.
- Avoid duplicating faction dossiers.

### `games/the_warcode/lore/Theatre_of_Operations.md`

- Inward-to-outward geography.
- Control and contested-presence table.
- Huoxing/Mars warning.
- MDR partial Cassini control/Protagen base warning.
- Erda population and access monopoly.
- No invented system map.

### `games/the_warcode/lore/Historical_Timeline.md`

- Calendar and five epochs.
- Burning phase arithmetic note.
- Blackout naming note.
- Year-1689 MDR founding.
- Year-2026 Arrival.
- Contested first-contact box comparing marketing and internal-file accounts.

### `games/the_warcode/lore/Source_Methodology.md`

- Academy framing.
- Evidence hierarchy.
- Faction-bias examples.
- Internal/public Dominium contrast.
- Ulfari source gap.
- Tactical Application mechanics firewall.

### Faction READMEs

- **Dominium:** ideology, Blackout policy, Custodia Silens formation, internal/public contradiction.
- **Protagen:** outer-belt confederation, guerrilla depth, science/freedom claims, security centralization and inequality tension.
- **MDR:** Huoxing/Mars distinction, authoritarian clone republic, Martin testimony, Executive Unit cohesion.
- **Ulfari:** no self-authored voice, non-hostile first contact, later hostile-source combat observations, unknown motives.

## 10. Gate checklist

- [x] Academy/source methodology mapped.
- [x] Theatre geography mapped.
- [x] Erda calendar and epochs mapped.
- [x] Dominium, Protagen, MDR, and Ulfari ideology/doctrine mapped.
- [x] Faction-authored prose treated as biased primary evidence.
- [x] Huoxing planet distinguished from Mars settlement.
- [x] Blackout/Blackout War/Silence War terminology separated.
- [x] MDR partial Cassini control reconciled with Protagen moon bases.
- [x] Custodia Silens identified as the Dominium playable formation, with playability sourced to current rulebook.
- [x] Pre-launch station-destruction claim compared with Erebus-7 non-hostile contact and Dominium suppression/escalation plan.
- [x] Tactical Application treated as a rulebook pointer, not mechanics authority.
- [x] Quote candidates identified without placing verbatim lorebook text in `docs/`.
- [ ] Coordinator/R3 to secure an archived or captured primary record of the exact pre-launch station-destruction wording.
- [ ] Coordinator to lock the first-contact conflict as unresolved in the cross-layer impact matrix.

## R2 recommendation to coordinator

Approve the lore map with one explicit unresolved evidence task: preserve the pre-launch station-destruction statement as a dated marketing claim only if R3 can capture its exact source wording. Current shipping should follow the lorebook’s stronger, later evidence by teaching a non-hostile Erebus-7 encounter followed by documented Dominium suppression and planned forced escalation, while stopping short of claiming the orders were fully executed or that all later Ulfari violence was fabricated.
