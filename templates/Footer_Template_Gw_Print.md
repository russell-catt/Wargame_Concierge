<!--
FILE: templates/Footer_Template_Gw_Print.md
VERSION: v1.0 (2026-08-23)
OWNER: Russell Catt
DOCUMENT_TYPE: Footer Template
PROJECT_NAME: Wargame_Concierge
PURPOSE: Games Workshop unofficial / non-endorsement notices for games/ shipping and print HTML.
-->

# GW print and shipping footer template

**Source:** [warhammer.com legal — Intellectual Property Guidelines](https://www.warhammer.com/en-CA/legal) (retrieved 2026-08-23). Not a licence.

**HTML fragment:** [`Gw_Print_Banner.html`](Gw_Print_Banner.html)

---

## B — First-page banner (print HTML, page 1 only)

```html
<p class="gw-ip-banner"><strong>UNOFFICIAL</strong> — fan teaching material, not a Games Workshop product, not endorsed by Games Workshop Limited.</p>
```

## A — Page footer (print HTML, every page)

**Warhammer 40,000:**

```html
<p class="gw-ip-footer"><strong>UNOFFICIAL.</strong> This document is completely unofficial and in no way endorsed by Games Workshop Limited. Personal / no-charge use only — never for sale. Warhammer, Warhammer 40,000 and associated marks are trademarks of Games Workshop Limited. Used without permission. No challenge to their status intended. Warhammer 40,000 is Copyright Games Workshop Limited. Teaching notes by Russell Catt (Wargame Concierge). Games Workshop retains IP in the settings and characters. No official logos.</p>
```

**Kill Team 2024:**

```html
<p class="gw-ip-footer"><strong>UNOFFICIAL.</strong> This document is completely unofficial and in no way endorsed by Games Workshop Limited. Personal / no-charge use only — never for sale. Warhammer, Kill Team and associated marks are trademarks of Games Workshop Limited. Used without permission. No challenge to their status intended. Kill Team is Copyright Games Workshop Limited 2024. Teaching notes by Russell Catt (Wargame Concierge). Games Workshop retains IP in the settings and characters. No official logos.</p>
```

Append page numbers after the footer paragraph when needed: ` Page N of M`.

## C — Markdown shipping (`## Games Workshop notice`)

Place **before** `## Change Log` on player-facing `games/**/*.md` (not `units/research/`).

Use the same sentences as footer A for the relevant system.

## D — Datacard micro

```text
UNOFFICIAL · not endorsed by Games Workshop Limited · personal use only · © Games Workshop Limited
```

## Optional — full trademark encyclopedia (once per site/README)

Long GW trademark lists (Pins of War style) are **optional**. Use a **short** TM line on every print page; link to warhammer.com legal for the full list. Do not repeat the encyclopedia on every PDF.

---

## Change Log

- v1.0 (2026-08-23): Initial GW footer template (track `gw_community_content`).

## Attribution

- Project: Wargame_Concierge
- Maintainer: Russell Catt
