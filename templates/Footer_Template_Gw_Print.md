<!--
FILE: templates/Footer_Template_Gw_Print.md
VERSION: v1.1 (2026-08-27)
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

## E — Currency line (optional, additive)

**Purpose:** a short, reusable line stamping which rules package a page currently teaches from — added when a page depends on a Games Workshop balance/rules package that carries its own version or date. **Additive only** — never replace banner B, footer A, markdown notice C, or datacard D; place the currency line **after** the relevant footer/notice on the same page, or as a standalone note under a page's own "Rules currency" heading.

**Do not invent a "Balance Dataslate `<date>`" line when no such singular file exists.** Name the actual package pieces and their stamps/dates instead (locked convention: `docs/handoffs/dataslate_0826/track_in.md`).

**40K — package stamp (prefer this over piece-specific lines when several pieces apply):**

```text
Rules currency: 40K Aug 2026 package — Universal Rules v1.1 · Faction Pack v1.2 · MFM v1.3 (legal / App 26 Aug 2026 where dated). Teaching paraphrase — verify owned PDFs before tournament play.
```

**40K — piece-specific (optional, when only one piece is relevant to the page):**

```text
Rules currency: Universal Rules Updates v1.1 (legal 26 Aug 2026) · supersedes July v1.0 on same topics.
```

```text
Rules currency: Munitorum Field Manual — Space Marines v1.3 (WarCom/App) · teaching paraphrase · verify owned PDF.
```

```text
Rules currency: Munitorum Field Manual — Necrons v1.3 (WarCom/App) · teaching paraphrase · verify owned PDF.
```

**Kill Team — no singular dataslate; Core + team package:**

```text
Rules currency: Kill Team quarterly balance — August 2026 (Core / update logs + team online rules) · teaching paraphrase · verify owned PDFs.
```

**SM Codex preview (until Codex ships — pairs with the 40K package line, does not replace it):**

```text
Preview note: Codex: Space Marines expected October (WarCom) · live lists still current Faction Pack / MFM until Codex — Legendary Proxies / Legends honesty on Firstborn paths.
```

**Warcode / non-GW systems (N/A stamp — not a GW balance package):**

```text
Last reviewed: <YYYY-MM-DD> · not affected by Games Workshop balance packages.
```

**Usage notes:**

- Substitute the actual version/date each time a package supersedes the one quoted above — do not let a currency line go stale silently.
- A page may carry more than one currency line (e.g. the 40K package line **and** the SM Codex preview note) when both apply.
- Currency lines are teaching metadata, not a Sec 10 quote exception — they do not license verbatim rules text beyond the version/date/name of the package itself.

## Optional — full trademark encyclopedia (once per site/README)

Long GW trademark lists (Pins of War style) are **optional**. Use a **short** TM line on every print page; link to warhammer.com legal for the full list. Do not repeat the encyclopedia on every PDF.

---

## Change Log

- v1.1 (2026-08-27): Section E — optional currency-line convention (40K package stamp, piece-specific Universal Rules / MFM lines, KT quarterly Core+team package line, SM Codex preview note, Warcode N/A stamp); additive only, no singular "Balance Dataslate" naming (track `dataslate_0826` S1).
- v1.0 (2026-08-23): Initial GW footer template (track `gw_community_content`).

## Attribution

- Project: Wargame_Concierge
- Maintainer: Russell Catt
