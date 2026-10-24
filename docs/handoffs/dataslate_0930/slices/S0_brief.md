# S0 — Brief (MFM v1.5 research note)

- **Track:** `dataslate_0930`
- **Slice:** S0
- **Status:** Ready
- **Depends:** none
- **Models:** Implementer grok-4.7 · QA `gpt-5.6-sol-medium`

## Inherited documentation

- [`track_in.md`](../track_in.md)

## Requirements

Write `research/mfm_v1_5_2026_09_30.md` and `slices/S0_implementer.md`.

The research note contains:

1. Both WarCom articles, as commentary, not datasheets: [Emboldened Astartes](https://www.warhammer-community.com/en-gb/articles/rylbvfnv/warhammer-40000-balance-update-emboldened-astartes/) (30 Sep 2026) and [Chaos, the Imperium and Xenos Fight Back](https://www.warhammer-community.com/en-gb/articles/vzqu6tzw/warhammer-40000-balance-update-chaos-the-imperium-and-xenos-fight-back/) (1 Oct 2026). Paraphrase only. No per-weapon profiles.
2. Live [Munitorum Field Manual](https://mfm.warhammer-community.com/en) v1.5, retrieved 2026-10-01, as the source of record. Owner paste at `raw/dataslate_Sep30/` is the Legends capture only (Apple Note zips, not a rules PDF). Do not dump the paste.
3. Necron delta table for units on our lists: Immortals 5: 70→65, Immortals 10: 140→130, Tomb Crawlers 2: 50→60, Doomstalker 140→130. Unchanged: Warriors 10 = 85, Scarabs 6 = 80, Macrocytes 5 = 70, Geomancer 75, Technomancer 80, Plasmancer 60, Royal Warden 50, Gauntlet of Compression 20, Atomic Disintegrators 10. Cryptek Conclave stays 2DP / Priority Assets.
4. Space Marine break table against the current 1000 list (do not apply these costs in S0): Captain 80→90, Chaplain in Terminator Armour 75→85, Techmarine 55→65, Terminator Squad 5: 160→195, Terminator Assault Squad 5: 155→175, wargear per Storm Shield 5 with no thunder-hammer line. Gladius stays 3DP; enhancement menu is Adept of the Codex 20, Artificer Armour 15, Laurels of Triumph 20, Standard of the Emperor Ascendant 25. Honour Vehement is absent. Whirlwind 175 is Legends in the paste. Tactical Squad, Devastator Squad, Bike Squad, Attack Bike, and Astartes Servitors are absent from the current roster.
5. Warmind verdict. [Space Marines](https://warmind.online/factions/space-marines) and [Necrons](https://warmind.online/factions/necrons) matched the live MFM on the shared sample (Captain 90, Captain in Terminator Armour 100, Chaplain in Terminator Armour 85, Techmarine 65, Terminators 195/175, Intercessors 95/175, Desolation 135, Codex Gladius enhancements, Necron Immortals 65/130, Crawlers 60, Doomstalker 130, Warriors 85). Corroboration only. Ignore Warmind rows the MFM does not carry: Tactical Squad 140, Devastator Squad 120/200, and the pre-codex Gladius with Fire Discipline 25 and Honour Vehement 15. Do not cite the 19 Sep 2026 patch note as the update record.
6. One line: commentary is not a datasheet. Confidence `draft`.

No `games/` or `KB/` edits in this slice.

## Exit criteria (QA verifies)

- [ ] Every number matches the live site or is labeled paste-only Legends
- [ ] Warmind is cited only as corroboration
- [ ] No full points dump
- [ ] No shipping file moved
- [ ] No `raw/` write
- [ ] Subagent did not git commit or push

## Constraints

UTF-8, no BOM. Teaching paraphrase. Codex wall.
