---
title: Warcode Contracts
type: concept
system: the_warcode
created: 2026-08-23
updated: 2026-09-24
version: 0.9.1
sources: [warcode_rulebook_v089f, raw/the_warcode/contract_cards_transcription.txt, games/the_warcode/rules/Contracts_and_VP.md, games/the_warcode/rules/Contract_Cards_Reference.md]
confidence: draft
tags: [concept, the_warcode, contracts, scoring, victory_points, catch_up]
---

# Warcode Contracts

When trailing after round scoring, draw a secret Contract that names one enemy from the opponent's faction; all four target columns now map to playable rosters.

---

## The mechanic

- **When:** End of Round step, after VP token scoring, only if behind on VP by 1+.
- **Draw:** One contract, kept secret until completed or invalidated.
- **Target:** One unit from the opponent's **available faction roster**. If that unit is already dead when drawn, show the card, bottom the deck, redraw.
- **Payoff:** Named unit eliminated → reveal → gain contract VP → discard.

Contracts sit beside map **VP tokens** (control within 1 inch, uncontested at end of round) as the second scoring lever.

---

## Why it matters at the table

Contracts are a catch-up bounty. The eight-card deck is unchanged in v0.8.9-F, each card is worth 1 VP, and all four columns now have playable rosters: Protagen Marines, Ulfari, MDR Executive Unit, and Custodia Silens.

Card 4186 spells the Custodia target `Justicar Julius`; the roster uses `Justiciar Julius`. Treat them as the same character while preserving the source-specific spelling.

---

## Deck shape (transcribed 2026-08-25)

| Cards | VP each | Targets per card |
|-------|---------|------------------|
| 8 | 1 VP | One named unit per faction column |

Example: Contract **6037** — if opponent plays Ulfari, target is **Shade** (matches p.22 worked example).

---

## Warcode vs That other game — do not conflate

That other game's crit/tac op scoring uses mission cards and TP thresholds in Murder Platoon. Warcode **Contracts** are **secret unit-assassination bounties** tied to VP deficit — not tac-op card reveals.

**Collision flag:** Do not map Contract timing to Turning Point scoring steps.

---

## Open questions

- Whether unfulfilled contracts stack when trailing multiple rounds (rulebook silent).
- Whether unfulfilled contracts persist after the player catches up.

## Related pages

- [[warcode_rulebook_v089f]] · [[warcode_protocol_cards]]
- [[warcode_protagen_marines]] · [[warcode_ulfari]] · [[warcode_mdr]] · [[warcode_dominium]]
- [`games/the_warcode/rules/Key_Concepts.md`](../../games/the_warcode/rules/Key_Concepts.md)
