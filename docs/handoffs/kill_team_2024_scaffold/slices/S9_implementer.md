# S9 — Implementer report (Join Ops pack)

- **Status:** Resolved - Implemented (awaiting QA)
- **Track / slice:** kill_team_2024_scaffold / S9 (Implementer + Librarian-assist)
- **Date:** 2026-08-17
- **Locked model:** `claude-sonnet-5-thinking-high` — **used as dispatched, no waiver needed.** Standing exclusion honored: never `claude-fable-5-thinking-high`.
- **Depends:** Preflight, S0 (both Resolved - Complete). S2, S3, S4, S5, S6 all landed **concurrently during this slice** (see "Concurrent-execution note" below) — their real output was used to correct this slice's own draft claims before filing.
- **`raw/` touched:** one pointer file amended (`kill_team_2024_nemesis_operatives.md`), adding a gap note — permitted under the layer contract (`AGENTS.md` Sec 2: Implementer slices may write `raw/pointers/`). No other `raw/` file created, edited, or deleted.
- **Commit:** none by this slice.

---

## Files created

| File | Purpose |
|------|---------|
| `games/kill_team_2024/join_ops/README.md` | What Joint Ops is; father-son co-op mechanics; who to play; first-session shortlist; sourcing/honesty notes |
| `games/kill_team_2024/join_ops/NPO_Catalog.md` | Six-section NPO catalog (generic Joint Ops, Terror on Devlan, Tomb World, Shadowhunt, Nemesis Operatives, out-of-scope) + six-row Gaps table |
| `games/kill_team_2024/join_ops/NPO_Cheat_Sheet.md` | Print-friendly mid-game aid: behaviour loops, Threat Principle, action loop, do/don't table |
| `games/kill_team_2024/join_ops/Playable_Scenarios_Owned_Terrain.md` | Scenario × killzone × ownership × Join Ops suitability matrix, tiered (first sessions / later sessions / PvP-only / secondary-trust) |
| `KB/sources/nemesis_operatives.md` | Optional KB source stub (system: `kill_team_2024`), created because L1 explicitly left Nemesis Operatives as an unread pointer |
| `docs/handoffs/kill_team_2024_scaffold/slices/S9_brief.md` | This slice's brief, written retrospectively from the dispatch prompt |
| `docs/handoffs/kill_team_2024_scaffold/slices/S9_implementer.md` | This report |

## Files updated

| File | Change |
|------|--------|
| `games/kill_team_2024/README.md` | `join_ops/` row marked Complete (S9); Change Log v0.2 row added |
| `raw/pointers/kill_team_2024_nemesis_operatives.md` | Added "S9 verification gap" note documenting the unreadable dossier scan and the mislabeled second file |
| `KB/index.md` | Added `[[nemesis_operatives]]` row to the KT24 Sources table; updated the status banner's source/page counts |

---

## Research performed (beyond the two named local PDFs)

Per the brief's instruction to cross-check Wahapedia and WarCom/Lexicanum, this slice:

- Fetched Wahapedia's Kill Team 3 missions page (`the-rules/the-missions/`) in full — this is the Core Book's own Joint Ops mission pack (Breach/Sabotage/Escape, generic Trooper/Tough/Warrior/Heavy NPOs, Brawler/Marksman behaviours, the Threat Principle), giving the cheat sheet and catalog a primary-adjacent source rather than a guess.
- Opened both named local Nemesis Operatives PDFs directly. **Neither is directly usable** — see Gaps below. This was not assumed; it was verified by reading them.
- Opened the owned, text-readable Terror on Devlan, Tomb World, and Shadowhunt mission-pack PDFs to paraphrase their Joint Ops content honestly instead of leaving those rows generic.
- Cross-checked Nemesis Operatives content against Warhammer Community's Sunday Preview, Lexicanum's dossier page, and three retailer listings (all dated/retrieved 2026-08-17), since the local PDF could not supply it directly.
- Web-searched the 3e Starter Set and Shadowhunt box contents to confirm terrain identity claims before writing them into the matrix.

## Key findings

1. **"Join Ops" is an informal name; the rulebook calls it "Joint Ops."** Stated explicitly in the README so nobody is confused searching official material later.
2. **Two distinct owned local files under the Nemesis Operatives pointer have real problems**, found by opening them rather than assuming they were fine:
   - `1063073009-Kill-Team-Nemesis-Operatives-Dossier.pdf` — correct 80-page count, but an un-OCR'd image scan with zero extractable text.
   - `kill-team-nemesis-operatives-eng.pdf` — **not the rules book at all.** It is a retailer product page for the unrelated "Nemesis Claw" kill team (a player-side Chaos Space Marines team). Flagged in `NPO_Catalog.md`, the KB source stub, and the pointer file itself.
3. **Terror on Devlan is the single best father-son first Joint Ops session.** Self-contained (own kill team, own NPOs), text-readable, uses Killzone: Volkus, which is confirmed play-now ready.
4. **Tomb World's own Joint Ops mission pack and Shadowhunt's Joint Ops pack are both genuinely terrain-gated**, not just conservatively marked — Shadowhunt's "Descent" concept needs both Volkus and Tomb World terrain, and Tomb World is unassembled. Recorded honestly rather than rounded up to "playable."
5. **Nemesis Operatives is a Custom Builder toolkit plus two dedicated mission packs (Ambull, Archivist)**, not a fixed catalog of enemies — the four named "examples" (Armoured Sentinel, XV8 Crisis Battlesuit, Screamer-Killer, Redemptor Dreadnought) illustrate the builder rather than being separately playable NPOs.

## Concurrent-execution note

This session's environment ran S2, S3, S4, S5, and S6 **concurrently with S9** (visible mid-slice as new files appeared under `setup/killzones/`, `critical_ops/`, and `teams/`). This slice:

- Initially wrote the four `join_ops/` files with killzone links pointing at **planned** S2 paths (per the brief's explicit contingency instruction).
- Detected S2's real output landing mid-slice, re-read all five killzone pages it produced, and **corrected two of this slice's own speculative claims** before filing:
  - Replaced "planned path" language with real links to `volkus.md`, `starter_set_3e.md`, `shadowhunt.md`, `tomb_world.md`.
  - Retracted a speculative note in `Playable_Scenarios_Owned_Terrain.md` guessing that "Volkus" and "3e Starter Set" might be the same killzone under two purchases — S2's `starter_set_3e.md` independently confirms they are two distinct products (Volkus terrain vs. the November 2024 Starter Set's own MDF terrain + Angels of Death/Plague Marines). The wrong guess is recorded as corrected, not silently deleted.
  - Softened a Shadowhunt-row claim that the box's two kill teams were "owned" outright — S2's `shadowhunt.md` explicitly hedges that only the boards + tokens are confirmed owned from that specific box, distinct from the team **rules** being owned via the separate Teams pointer. Both facts are now stated side by side.
- Also updated `README.md`'s "Who to play" links to the real team package pages once S3/S4/S5/S6 output appeared, rather than leaving stub links.

**Reasoning for not reverting to "planned paths only":** the brief's contingency ("if killzone pages exist, link them; if not, still write Join Ops docs and link planned paths") anticipated exactly this race and named the correct behavior once real pages exist. Re-checking against real S2 output mid-slice and correcting two wrong guesses is more useful to the user than filing content already known to be stale at hand-off.

## No datasheet numbers or statlines

Self-checked with a targeted search across all four `join_ops/` files for characteristic profile patterns (`APL N`, `Wounds N`, `Save N+`, `Move N`, weapon `Atk`/`Hit`/`Dmg` numbers) — **zero matches.** Every NPO description in `NPO_Catalog.md` and `NPO_Cheat_Sheet.md` is qualitative (e.g., "soaks damage, slow to remove" instead of a Wounds value).

## Exit criteria

| Criterion | Result |
|-----------|--------|
| Four `join_ops/` files created, paraphrased, dated 2026-08-17 | PASS |
| `NPO_Catalog.md` cites both local PDFs + Wahapedia/WarCom/Lexicanum, with a Gaps section | PASS |
| `NPO_Cheat_Sheet.md` is print-friendly and distinguished from Community Content | PASS |
| `Playable_Scenarios_Owned_Terrain.md` — first sessions at top, honest Tomb World row, labelled WD row | PASS |
| Zero datasheet numbers/statlines | PASS (self-checked, see above) |
| `S9_implementer.md` filed with file list and gaps | PASS (this document) |
| Zero new binaries in repo working tree | PASS — `Get-ChildItem -Recurse -Include *.pdf,*.webp,*.png,*.jpg,*.jpeg` returns 0 |
| No `git commit` / `git push` | PASS — none issued |
| UTF-8 | PASS — all files written directly as UTF-8 |

---

## Gaps (headline list — full detail in `NPO_Catalog.md`)

| # | Gap | Where flagged |
|---|-----|----------------|
| 1 | Nemesis Operatives dossier PDF is an un-OCR'd image scan; no text extractable | `NPO_Catalog.md` Gaps, `raw/pointers/kill_team_2024_nemesis_operatives.md`, `KB/sources/nemesis_operatives.md` |
| 2 | Second local "Nemesis Operatives" file is actually a Nemesis Claw retailer listing — wrong content entirely | Same three locations |
| 3 | Ambull's two mission titles not found in any source read this session (Archivist's are: "Betrayal," "Negotiation") | `NPO_Catalog.md` Gaps |
| 4 | "Nemesis Ops" (one retailer source) vs "Adversary Ops" (WarCom) naming conflict for the both-sides-NPO mode, unresolved | `NPO_Catalog.md` Gaps, `KB/sources/nemesis_operatives.md` |
| 5 | Edition-number discrepancy: Lexicanum calls Nemesis Operatives a 4th-Edition supplement; Wahapedia's Core Book listing (same retrieval date) still shows Edition 3, matching this track's locked KT24/3e scope. Recorded, not acted on | `NPO_Catalog.md` Gaps, `KB/sources/nemesis_operatives.md` |
| 6 | Tomb World/Shadowhunt NPO rosters (Scarab Swarms, Warriors, Tomb Crawlers, Macrocytes) reconstructed from a secondary Shadowhunt review, not read directly from an owned NPO datacard page | `NPO_Catalog.md` Gaps |
| 7 | 3e Starter Set killzone page (`starter_set_3e.md`, written by S2) itself flags no dedicated `raw/pointers/` file yet for the Starter Handbook — inherited gap, not introduced by S9, but relevant to anyone relying on this slice's Starter Set claims | `starter_set_3e.md` (S2 output), cross-referenced in this slice's `README.md` and matrix |

---

## Next

Recommend **L2** (or whichever Librarian pass reconciles L1 + S9's KT24 source additions) eventually attempt OCR or a physical re-read of the Nemesis Operatives dossier, and confirm/replace the mislabeled second local file, so Gap 1–2 can close and the relevant pages can move off `confidence: draft`.

No blockers for downstream slices. `join_ops/` is feature-complete for this track's stated Join Ops scope.
