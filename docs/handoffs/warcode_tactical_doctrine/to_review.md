# To review — warcode_tactical_doctrine

- **Project:** Wargame_Concierge
- **Track:** `warcode_tactical_doctrine`
- **Audience:** Russell (table owner / Coordinator)
- **Date:** 2026-08-24
- **Status:** Track closed — post-ship owner review

## Purpose

The Warcode scaffold and VIP agentic review landed on `main` via PR #16 and #17. This checklist is **your** pass: read what matters, decide what to ship externally, fill gaps only you can supply, and merge the naming-compliance branch before you treat the subtree as done.

Agents built the corpus; you own tone, VIP routing, and whether §12 findings go to RedMakers.

## How to use this doc

1. Skim **Ship status** and **Read first** (30 min).
2. Work **P0** items before sharing anything outside the repo.
3. Work **P1** when you are ready to polish for VIP / Facebook / personal play.
4. Leave **P2** until you buy TTS, print proxies, or a new beta drops.
5. Tick boxes in **Review checklist** as you go; file outcomes per **Where to file outcomes**.

Priority key:

| Tier | Meaning |
|------|---------|
| **P0** | Merge blockers — fix or decide before external share |
| **P1** | Content review — read, edit, or accept as-is |
| **P2** | Deferred — optional polish or blocked on you |

---

## 1. Ship status

| Item | State |
|------|--------|
| **PR #16** — `feat(warcode): The Warcode system #3 scaffold + VIP agentic review` | **Merged** to `main` (2026-08-24) |
| **PR #17** — `docs(handoffs): close warcode_tactical_doctrine after PR #16` | **Merged** to `main` (2026-08-24) |
| **Branch `cursor/warcode-gw-obfuscation-b7e0`** | **Not merged** — AGENTS v0.5.5 extended ban (Rawmallet / 39.876 / 39.9) + shipping/KB scrub; **no open PR** as of 2026-08-24 |
| **Track rollup** | Closed in [`docs/handoffs/README.md`](../README.md) |
| **GATE lock** | **Provisional** — see [`review_manifests/GATE_user_lock.md`](review_manifests/GATE_user_lock.md) |

**P0:** Open PR from `cursor/warcode-gw-obfuscation-b7e0` → squash-merge to `main`, or cherry-pick commit `3a50b29` if you prefer a fresh branch.

---

## 2. Read first

Read in this order before editing the VIP review or sharing links.

| # | Document | Why |
|---|----------|-----|
| 1 | [`games/the_warcode/reviews/Agentic_Rules_and_Marketing_Review.md`](../../../games/the_warcode/reviews/Agentic_Rules_and_Marketing_Review.md) | **§0** (voice), **§12** (bugs to route or withhold), **§13** (your prose — empty), **§15** (legal) |
| 2 | [`games/the_warcode/rules/Comparative_Glossary.md`](../../../games/the_warcode/rules/Comparative_Glossary.md) | §16 bridges to **That other game** / **Murder Platoon** |
| 3 | [`games/the_warcode/First_Game_Walkthrough.md`](../../../games/the_warcode/First_Game_Walkthrough.md) | Table script — Protagen vs Ulfari proxy |
| 4 | [`games/the_warcode/README.md`](../../../games/the_warcode/README.md) | Subtree map and read order |

Supporting context (optional): [`track_warcode_tactical_doctrine_final_report.md`](track_warcode_tactical_doctrine_final_report.md), [`slices/L2_lint_note.md`](slices/L2_lint_note.md).

---

## 3. GATE / VIP review

**What GATE did:** Manifests `00`–`12`, `14`, `15` were locked; S7 polished the VIP doc. Lock is **provisional** — you may still change §0 tone, §12 bug list, and §13.

**What you should read and decide:**

| Section | Your decision |
|---------|----------------|
| **§0 — What this document is not** | Accept agentic voice? Must retain **unofficial and unauthorized**. Too harsh / too soft on AI method or biases? |
| **§12 — What needs polish** | Which A-rules-gaps and B-bugs (especially **B1** movement fallback, **B8** if present) go to the VIP Facebook channel vs stay internal? |
| **§13 — The non-agentic view** | **Empty placeholder** — add your VIP/backer perspective (see [`review_manifests/14_thank_you_stub.md`](review_manifests/14_thank_you_stub.md): §13 manifest intentionally absent; owner fills after S7). |
| **§14 — Thank you** | Tone OK? No implied relationship with RedMakers? |
| **§15 — Legalese** | Accept as-is for personal repo use? |
| **Provisional lock** | Update [`GATE_user_lock.md`](review_manifests/GATE_user_lock.md) to **final** once you sign off, or note revisions requested. |

**GATE brief gap:** There is no separate owner-facing GATE brief — only the lock file and manifests. This doc is that brief.

---

## 4. Plan gaps still open

From final sanity, L2 lint, and plan archive [`reference/Warcode_Tactical_Doctrine_Plan.md`](../../../reference/Warcode_Tactical_Doctrine_Plan.md):

| Gap | Tier | Detail |
|-----|------|--------|
| **L1 — KB unit pages** | P1 | Faction pages exist under `KB/factions/warcode_*.md`; **no** `KB/units/` pages for Protagen/Ulfari models. Plan called for paraphrase + links to quoted datasheets. |
| **S1b — Unscannable cards (pp24–25 + image-only pages)** | P1 | Contract cards on PDF pp.24–25 are art-only — individual targets and VP values **not** in [`Rulebook_Quotes.md`](../../../games/the_warcode/rules/Rulebook_Quotes.md). Protocol Cards done via [`protocol_cards.ocr.txt`](../../../raw/the_warcode/protocol_cards.ocr.txt). **You type up** card text; **agent ingests** into quotes corpus and enhances VIP review / other Warcode docs (see §5). |
| **S8 — Partial keyword coverage** | P2 | [`Comparative_Glossary.md`](../../../games/the_warcode/rules/Comparative_Glossary.md) covers core terms + Protocol names; [`Keyword_Glossary.md`](../../../games/the_warcode/rules/Keyword_Glossary.md) still marks comparative stubs / Protocol OCR pending. Not a ship blocker. |
| **GATE §13 brief** | P1 | No `13_*.md` manifest by design — owner prose lives only in the polished review §13. |
| **TTS workshop URL** | P2 | [`guides/Tabletop_Simulator.md`](../../../games/the_warcode/guides/Tabletop_Simulator.md) — placeholder until you own TTS and paste Steam workshop link. |

---

## 5. User inputs needed

Only you can supply these:

| Input | Where it goes | Blocker? |
|-------|---------------|----------|
| **TTS workshop URL** | `games/the_warcode/guides/Tabletop_Simulator.md` | No — blocked on TTS purchase |
| **§13 non-agentic prose** | `games/the_warcode/reviews/Agentic_Rules_and_Marketing_Review.md` §13 (replace HTML comment) | No for repo; **yes** if sharing VIP doc externally |
| **VIP Facebook feedback routing** | Your choice: which §12 items (e.g. B1, B6 glyph) to post; whether to link the GitHub repo | P0 before public post |
| **GATE final sign-off** | `review_manifests/GATE_user_lock.md` — change Provisional → Final | P1 |
| **Unscannable card text (S1b)** | Sidecar under `raw/the_warcode/` (e.g. `contract_cards.txt`) or paste in a new agent slice brief | No for repo merge; **yes** for complete contract/VP reference and §12 polish |

### Unscannable cards — user types, agent researches (S1b)

Some beta PDF pages are flattened card art with no extractable text layer. Protocol Cards (pp.28–32) were OCR'd into [`raw/the_warcode/protocol_cards.ocr.txt`](../../../raw/the_warcode/protocol_cards.ocr.txt) and quoted in [`Rulebook_Quotes.md`](../../../games/the_warcode/rules/Rulebook_Quotes.md). **Contract cards (pp.24–25) are still missing** — see [Gaps in the extract](../../../games/the_warcode/rules/Rulebook_Quotes.md#gaps-in-the-extract) and §25 in that file.

**Source PDF:** [`raw/the_warcode/The Warcode Rulebook V.0.8.7-F.pdf`](../../../raw/the_warcode/The%20Warcode%20Rulebook%20V.0.8.7-F.pdf) — also [`raw/the_warcode/README.md`](../../../raw/the_warcode/README.md).

**Your action (P1):**

1. Open the beta PDF and any other image-only / unscannable pages you notice.
2. Type up card text for **contract cards (pp.24–25)** first — unit names per faction, VP values, any special wording.
3. Save as plain UTF-8 text (e.g. `raw/the_warcode/contract_cards.txt`) or paste into a new slice brief / chat when you gate agent work.
4. Flag any additional unscannable pages beyond contracts and Protocol Cards.

**Agent follow-up (after you provide text):**

1. Cross-check typed text against rulebook contract rules (§25 in `Rulebook_Quotes.md`, pp.22 narrative).
2. Add verbatim quote blocks to [`Rulebook_Quotes.md`](../../../games/the_warcode/rules/Rulebook_Quotes.md) (filename + page + section; `via typed transcription` cite if not OCR).
3. Research cards in play context — VP swing, target selection, faction pairings — and update [`Agentic_Rules_and_Marketing_Review.md`](../../../games/the_warcode/reviews/Agentic_Rules_and_Marketing_Review.md) (especially §12 gaps) and related Warcode docs.
4. Create new docs if warranted (e.g. contract card reference table, `KB/concepts/` for contract timing, comparative glossary rows).
5. Append activity to [`KB/log.md`](../../../KB/log.md).

**Tier:** P1 content — not a merge blocker, but blocks a complete quotes corpus and informed §12 contract commentary.

---

## 6. Naming / compliance

**On branch `cursor/warcode-gw-obfuscation-b7e0` (not on `main` yet):** AGENTS Sec 10 v0.5.5 extended ban — in `games/the_warcode/**` never use (any casing):

- That other game's real product title (KT family)
- Rawmallet's real brand name
- 39.876 / 39.9 real edition strings

Use instead: **That other game**, **Murder Platoon**, **Rawmallet**, **39.876**, **39.9**.

**After merge, grep checklist** (run from repo root; expect **zero** hits under `games/the_warcode/`):

```powershell
$patterns = @('Kill Team','kill team','Warhammer','40,000','40K','40k')
foreach ($p in $patterns) {
  Write-Host "=== $p ==="
  Select-String -Path games/the_warcode -Pattern $p -Recurse
}
```

Also confirm §0 and §15 in the agentic review contain **unofficial and unauthorized**.

**Handoffs and KB** may say KT24 / Warhammer for agent context — ban applies to **`games/the_warcode/**` shipping only**.

---

## 7. Optional polish (P2)

| Item | Notes |
|------|--------|
| **MDR / Dominium** | Stubs only — [`factions/mdr/README.md`](../../../games/the_warcode/factions/mdr/README.md), [`factions/dominium/README.md`](../../../games/the_warcode/factions/dominium/README.md); no beta datasheets until RedMakers publish |
| **Print HTML** | No Warcode print pipeline yet; GW footer rules apply if you add `games/the_warcode/**/print/` |
| **Duplicate PDF cleanup** | L2 noted a stray copy at `raw/The Warcode Rulebook...` — canonical path is `raw/the_warcode/The Warcode Rulebook V.0.8.7-F.pdf` only |
| **Contract card transcription** | Covered in §5 — you type pp.24–25; agent ingests (OCR optional if you prefer) |
| **L1 unit KB pages** | Eight models × two factions — paraphrase roles, link to squad datasheets |

---

## 8. Review checklist

Copy this section into your notes or tick here.

### P0 — Merge blockers

- [ ] Merge or PR **`cursor/warcode-gw-obfuscation-b7e0`** → `main`
- [ ] Re-run naming grep on `games/the_warcode/` after merge (zero banned hits)
- [ ] Decide **external share policy** for agentic review (GitHub public vs excerpt only)

### P1 — Content review

- [ ] Read agentic review **§0** — voice acceptable
- [ ] Read **§12** — mark bugs to send vs keep internal
- [ ] Write **§13** non-agentic VIP perspective
- [ ] Skim **§14–§15** — thank-you and legalese acceptable
- [ ] Read **Comparative Glossary** — bridges accurate for your That other game experience
- [ ] Skim **First Game Walkthrough** — runnable with proxy models
- [ ] Update **GATE_user_lock.md** to final (or document requested edits)
- [ ] Route selected §12 findings to VIP Facebook (if any)
- [ ] **Unscannable cards (user):** Type contract card text from PDF pp.24–25 → `raw/the_warcode/contract_cards.txt` (or paste for agent)
- [ ] **Unscannable cards (user):** Note any other image-only pages beyond contracts / Protocol Cards

### P1 — Agent work (gate after your card text)

- [ ] Ingest contract card text into `Rulebook_Quotes.md` (close S1b gap)
- [ ] Research contracts in rulebook context; enhance agentic review §12 and related Warcode docs
- [ ] Create new reference docs if needed (contract table, KB concepts, glossary rows)

### P2 — Deferred

- [ ] Purchase TTS; paste **workshop URL** into Tabletop_Simulator guide
- [ ] L1 KB unit pages for Protagen / Ulfari
- [ ] Expand S8 / Keyword_Glossary comparative rows
- [ ] Remove duplicate PDF under `raw/` if still present
- [ ] MDR / Dominium when beta adds rosters

---

## 9. Where to file outcomes

| Outcome | File / action |
|---------|----------------|
| §13 prose, §0/§12 edits | Edit [`Agentic_Rules_and_Marketing_Review.md`](../../../games/the_warcode/reviews/Agentic_Rules_and_Marketing_Review.md) directly |
| GATE final approval | Update [`GATE_user_lock.md`](review_manifests/GATE_user_lock.md) status + date |
| TTS URL | [`guides/Tabletop_Simulator.md`](../../../games/the_warcode/guides/Tabletop_Simulator.md) |
| Contract / unscannable card text | `raw/the_warcode/contract_cards.txt` (or similar sidecar) — pattern: [`protocol_cards.ocr.txt`](../../../raw/the_warcode/protocol_cards.ocr.txt) |
| Contract quotes + S1b close | [`rules/Rulebook_Quotes.md`](../../../games/the_warcode/rules/Rulebook_Quotes.md) §25 + [Gaps in the extract](../../../games/the_warcode/rules/Rulebook_Quotes.md#gaps-in-the-extract) |
| Contract research → VIP review | [`reviews/Agentic_Rules_and_Marketing_Review.md`](../../../games/the_warcode/reviews/Agentic_Rules_and_Marketing_Review.md) §12; new `games/the_warcode/` reference doc if table format helps |
| Contract KB synthesis | `KB/concepts/` (e.g. contract timing) + [`KB/glossary.md`](../../../KB/glossary.md) if terms earn entries |
| KB unit synthesis | New `KB/units/warcode_*.md` pages + [`KB/index.md`](../../../KB/index.md) |
| Activity log | Append [`KB/log.md`](../../../KB/log.md) — `query` or `lint` row for your review pass |
| New agent work | New slice brief under `docs/handoffs/<track>/slices/` — do not rewrite closed slice reports |
| Promotions to shipping | [`KB/changelog.md`](../../../KB/changelog.md) after Coordinator review |
| Obfuscation merge | PR via [`github-commit-push-merge`](../../../.cursor/skills/github-commit-push-merge/SKILL.md) skill when you gate commit |

---

## Related

- Track in: [`track_in.md`](track_in.md)
- Final report: [`track_warcode_tactical_doctrine_final_report.md`](track_warcode_tactical_doctrine_final_report.md)
- Plan archive: [`reference/Warcode_Tactical_Doctrine_Plan.md`](../../../reference/Warcode_Tactical_Doctrine_Plan.md)
- Schema: [`AGENTS.md`](../../../AGENTS.md) Sec 10 (Warcode quotes + naming)
