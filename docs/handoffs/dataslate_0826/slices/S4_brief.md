# S4 — Brief (project core files currency)

- **Track:** `dataslate_0826`
- **Slice:** S4
- **Status:** Ready
- **Depends:** QA-S2 PASS **and** QA-S3 PASS
- **Recommended models:** Implementer `claude-sonnet-5-thinking-high` · QA `gpt-5.6-sol-high`

## Inherited documentation

- Locked dataslate dates
- Core inventory in [`track_in.md`](../track_in.md) § Core file inventory (S4)

## Requirements

1. Editing pass on every **project/docs core** path listed in track_in (or explicit waiver with reason).
2. Ensure readers can see **where** balance currency lives (link to game READMEs / pointers) without dumping rules.
3. Update `AGENTS.md` living-refs table **only** if needed (retrieval date / dataslate discovery line) — do not rewrite schema casually.
4. Keep Rising Tide headers/footers coherent; add changelog rows where those files use them.
5. Write `S4_implementer.md` with touch/waiver table.

## Exit criteria (QA verifies)

- [ ] Every S4 inventory path touched **or** waived with reason
- [ ] No stale “July update only” language that implies no later dataslate when one exists
- [ ] Version / date stamps bumped where the file convention requires it
- [ ] Legibility: START_HERE / README remain scannable (not a dump of balance notes)
- [ ] Subagent did not git

## Constraints

Do not expand into unrelated tracks. No `wiki/`. UTF-8 no BOM.
