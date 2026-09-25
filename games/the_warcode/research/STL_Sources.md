<!--
FILE: games/the_warcode/research/STL_Sources.md
VERSION: v0.2 (2026-09-24)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, warcode_tactical_doctrine)

DOCUMENT_TYPE: Research / Sourcing Notes
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: The Warcode
REFERENCE_STATUS: Active — draft (2026-09-24)

SOURCES:
  - raw/pointers/warcode_stl_sources.md
  - https://gamefound.com/en/projects/redmakers/the-warcode (retrieved 2026-09-24)
  - https://www.kickstarter.com/projects/redmakers/the-warcode-stl-campaign (retrieved 2026-09-24)
  - https://www.kickstarter.com/projects/redmakers/the-warcode-stl-campaign/faqs (retrieved 2026-09-24)
  - https://steamcommunity.com/sharedfiles/filedetails/?id=3776386741 (retrieved 2026-09-24)

PURPOSE:
  Official digital STL and Print & Play path. No third-party piracy. Preserve
  the cancelled Gamefound offer separately from the live Kickstarter.

UPDATE_TRIGGER:
  Kickstarter closes or delivers files; licence or resin/FDM guidance changes.
-->

# STL sources — official path only

**`confidence: draft`** — sourcing snapshot checked **2026-09-24**. **Support RedMakers through official channels.**

---

## Official sources

| Channel | What it provides | Status (2026-09-24) |
|---------|------------------|---------------------|
| [Kickstarter — digital STL campaign](https://www.kickstarter.com/projects/redmakers/the-warcode-stl-campaign) | Digital STL packages for miniatures, terrain, and tokens by tier; Print & Play files by tier | Live **2026-09-23 through 2026-10-23**; all rewards digital |
| [Steam Workshop](https://steamcommunity.com/sharedfiles/filedetails/?id=3776386741) | Public digital try-before-backing route | Playable listing available; visibly labels rules **v0.8.7**, behind current PDF v0.8.9-F |
| [Gamefound — historical campaign](https://gamefound.com/en/projects/redmakers/the-warcode) | Former mixed digital/physical offer | Creator-cancelled; platform ended **2026-09-18**; no funds collected |

**Path pointer:** `raw/pointers/warcode_stl_sources.md`

The Kickstarter does **not** include physical boxes. RedMakers has stated an intention to pursue a physical edition later, but no date, platform, contents, price, or delivery guarantee is established.

Live Kickstarter totals are volatile and intentionally omitted here. There is **no** authorised third-party STL mirror in this repo. Do **not** commit STL binaries to git.

---

## Until campaign delivery — proxies

Use owned collections per [`../guides/Proxy_Play_at_Home.md`](../guides/Proxy_Play_at_Home.md):

- Rawmallet 39.876 infantry at skirmish scale
- Murder Platoon operatives where roles match
- Terrain from Volkus / sector boards scaled to **33" × 24"**

Proxies are for **learning and playtesting**, not resale or public redistribution.

---

## Resin vs FDM (campaign messaging — test on delivery)

Marketing materials describe a **split print strategy** (paraphrase; verify when files ship):

| Component | Stated optimization | Home note |
|-----------|---------------------|-----------|
| **Miniatures** | Resin-oriented supports | Fine detail, small parts — resin or high-quality FDM with tuning |
| **Terrain** | FDM-oriented | Larger flats, walls, doors — practical on filament printers |

Treat this as **campaign messaging**, not tested print profiles. Run test plates when STLs arrive.

---

## What this repo will not host

- Pirated or scraped STL packs
- Binary mesh files (`.stl`, `.chitubox`, etc.) — blocked by project policy
- Unofficial recasts sold as Warcode-compatible product

Teaching content stays in markdown; print at home from **your** pledged files only.

---

## Post-delivery checklist

- [ ] Download the pledged digital package through the official Kickstarter fulfilment route
- [ ] Verify faction roster headcount (**8 models × chosen faction**)
- [ ] Test print one infantry and one terrain piece before batch runs
- [ ] Cross-check base sizes against [`../setup/Board_Setup.md`](../setup/Board_Setup.md) spacing
- [ ] Retire proxies gradually as official models hit the table
- [ ] Recheck the personal-use licence and any updated file-support notes

---

## Related pages

- [`../guides/Proxy_Play_at_Home.md`](../guides/Proxy_Play_at_Home.md)
- [`../guides/Tabletop_Simulator.md`](../guides/Tabletop_Simulator.md)
- [`../reviews/Gamefound_Postmortem_2026-09-18.md`](../reviews/Gamefound_Postmortem_2026-09-18.md)
- [`../reviews/Kickstarter_and_Community_2026-09-24.md`](../reviews/Kickstarter_and_Community_2026-09-24.md)
- [`../factions/protagen_marines/README.md`](../factions/protagen_marines/README.md)
- [`../factions/ulfari/README.md`](../factions/ulfari/README.md)
- [`../factions/mdr/README.md`](../factions/mdr/README.md)
- [`../factions/dominium/README.md`](../factions/dominium/README.md)

---

## Change Log

- v0.2 (2026-09-24): Replaced cancelled Gamefound fulfilment assumptions with the live digital-only Kickstarter, added Workshop URL and visible v0.8.7 drift, and separated deferred physical intent (S4).
- v0.1 (2026-08-23): Official Gamefound Field Commander path; no piracy note (warcode_tactical_doctrine).

## Attribution

- Project: Wargame_Concierge
- Maintainer: Russell Catt
- The Warcode is property of RedMakers.

## Rising Tide Notes

- Confirm resin/FDM split against final backer FAQ when STLs drop.
