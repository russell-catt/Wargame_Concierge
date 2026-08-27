# L1 — Brief (Librarian enhance)

- **Track:** `dataslate_0826`
- **Slice:** L1
- **Status:** Ready
- **Depends:** QA-S5 PASS + L0 Complete
- **Recommended models:** Librarian `claude-sonnet-5-thinking-high` · QA `gpt-5.6-sol-high`
- **Skill:** [`.cursor/skills/librarian-enhance/SKILL.md`](../../../../.cursor/skills/librarian-enhance/SKILL.md)

## Requirements

1. Sync KB entities affected by shipping changes (factions, units, concepts, setup) — update or **no-op waiver** with reason.
2. Glossary: new/refined terms from dataslate (glossary-only Keywords).
3. Update `KB/index.md`, `KB/overview.md` if big-picture shifted, append `KB/log.md`.
4. Back-links for new/updated pages.
5. Write `L1_librarian.md` (or enhance report).

## Exit criteria (QA-L1 verifies)

- [ ] Source pages no longer stubs-only if shipping claims rely on them
- [ ] Log entry for this track
- [ ] librarian-enhance checklist PASS or explicit waivers
- [ ] No raw/ writes; YAML frontmatter valid
- [ ] Subagent did not git

## Constraints

Prefer update over near-duplicate. Flag contradictions before silent overwrite.
