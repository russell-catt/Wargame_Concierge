<!--
FILE: games/the_warcode/guides/Tabletop_Simulator.md
VERSION: v0.2 (2026-09-24)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (Implementer, warcode_tactical_doctrine)

DOCUMENT_TYPE: Teaching Guide / Digital Play Gate
PROJECT_NAME: Wargame_Concierge
GAME_SYSTEM: The Warcode
REFERENCE_STATUS: Active — draft (2026-09-24)

SOURCES:
  - https://store.steampowered.com/app/286160/Tabletop_Simulator/ (retrieval 2026-08-23)
  - https://steamcommunity.com/sharedfiles/filedetails/?id=3776386741 (retrieved 2026-09-24)
  - https://www.kickstarter.com/projects/redmakers/the-warcode-stl-campaign/faqs (retrieved 2026-09-24)
  - raw/the_warcode/The-Warcode-Rulebook-V.0.8.9-F.pdf

PURPOSE:
  Record the purchase gate, confirmed public Workshop route, and visible rules
  version drift for remote play. Does not audit implementation quality.

UPDATE_TRIGGER:
  Tabletop Simulator purchased; Workshop build is tested or version label changes.
-->

# Tabletop Simulator — purchase gate and public Workshop

**`confidence: draft`** — status snapshot **2026-09-24**. **Not a TTS mod review.**

---

## Current status

| Item | Status |
|------|--------|
| Steam Workshop item | [The Warcode: Tactical Doctrine](https://steamcommunity.com/sharedfiles/filedetails/?id=3776386741) — public and subscribable |
| **Tabletop Simulator** base game | **Not purchased yet** — blocks loading any subscribed mod |
| Visible Workshop rules label | **v0.8.7** — behind the current free PDF baseline **v0.8.9-F** |
| This document | Purchase gate + checklist only — **no TTS implementation review** |

The Kickstarter FAQ presents the Workshop item as a way to try the game before backing. Public availability does not establish implementation completeness, rules fidelity, scripting quality, or update cadence.

You cannot play a subscribed Workshop mod until the **Tabletop Simulator** app is owned on the Steam account that subscribed.

---

## Purchase gate

1. Open Steam → search **Tabletop Simulator** (Berserk Games, App ID 286160).
2. Purchase the base game (regular sales occur — no need to pay full price on day one unless eager).
3. Install and launch once so Workshop subscriptions sync.
4. Subscribe to the [public Workshop item](https://steamcommunity.com/sharedfiles/filedetails/?id=3776386741).
5. Load the mod from Workshop → **Tabletop Simulator** main menu → Create → Workshop.

**Scope limit:** This guide stops at ownership and load steps. Scripting quality, automation, stat fidelity, and update cadence are **out of scope** until someone plays a build and files a separate review.

---

## Version-drift warning

The public listing visibly says **“Current rules version: 0.8.7.”** The current mechanics source is `The-Warcode-Rulebook-V.0.8.9-F.pdf`.

Until the build is audited, verify table decisions against v0.8.9-F and do not assume that the listing or implementation includes later rules, profiles, or corrections. The version label alone does not reveal the exact differences inside the mod.

**Physical proxy play** remains an alternative learning path: [`Proxy_Play_at_Home.md`](Proxy_Play_at_Home.md).

---

## Remote play alternative (no TTS)

- **Voice + shared camera** over physical proxies on two tables (async deployment photos).
- **Single shared table** when co-located — preferred for first learning session ([`../First_Game_Walkthrough.md`](../First_Game_Walkthrough.md)).

---

## Related pages

- [`Proxy_Play_at_Home.md`](Proxy_Play_at_Home.md)
- [`../reviews/Kickstarter_and_Community_2026-09-24.md`](../reviews/Kickstarter_and_Community_2026-09-24.md)
- [`../research/STL_Sources.md`](../research/STL_Sources.md)
- [`../README.md`](../README.md)

---

## Change Log

- v0.2 (2026-09-24): Added confirmed Workshop URL, Kickstarter try-before-backing context, and visible v0.8.7 versus v0.8.9-F drift warning (S4).
- v0.1 (2026-08-23): Purchase gate stub; workshop URL TBD (warcode_tactical_doctrine).

## Attribution

- Project: Wargame_Concierge
- Maintainer: Russell Catt
- Tabletop Simulator is property of Berserk Games. The Warcode is property of RedMakers.

## Rising Tide Notes

- Revisit when TTS is purchased and a workshop build is load-tested.
