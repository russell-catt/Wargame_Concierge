<!--
FILE: docs/operations/github_ship_smoothers.md
VERSION: v1.0 (2026-08-23)
OWNER: Russell Catt
AUTHOR_OF_NOTES: Cursor (cloud agent)

DOCUMENT_TYPE: Operations / GitHub Setup
PROJECT_NAME: Wargame_Concierge
PROJECT_STATUS: Active

PURPOSE:
  One-time GitHub settings that make agent commit → push → squash-merge smooth
  under the public-access ruleset. Complements `.cursor/skills/github-commit-push-merge`.

UPDATE_TRIGGER:
  Ruleset or merge-policy changes on github.com/russell-catt/Wargame_Concierge.
-->

# GitHub ship smoothers (owner checklist)

Cloud agents **cannot** change repository settings (API returns 403 for this integration). Do these once in the GitHub UI so `/github-commit-push-merge` can land PRs without a human click every time.

## Confirmed ruleset (read 2026-08-23)

Ruleset **`public-access`** on default branch (`main`):

| Rule | Effect |
|------|--------|
| `update` / `creation` / `deletion` / `non_fast_forward` | No direct pushes to `main` — PRs only |
| `required_linear_history` | Prefers squash/rebase over merge commits |
| `pull_request.required_approving_review_count` | **0** (already smooth) |
| `allowed_merge_methods` | Currently merge + squash + rebase |

## Agent capability (measured 2026-08-23, rule test #3)

| Action | Result |
|--------|--------|
| Create branch / push / open PR | Works |
| `gh pr merge --squash` | **Blocked** — `base branch policy prohibits the merge` |
| `gh pr merge --squash --auto` | **Blocked** — `Auto merge is not allowed` (`allow_auto_merge=false`) |
| `gh pr merge --squash --admin` | **Blocked** — `Cannot update this protected ref` (ruleset `current_user_can_bypass: never`) |
| PATCH repo / ruleset settings | **403** — Resource not accessible by integration |

So the agent **cannot** land on `main` until a human either Squash-and-merges in the UI **or** grants the Cursor/GitHub App a ruleset bypass (and enables Allow auto-merge).

## Owner actions (do in GitHub Settings)

1. **Settings → General → Pull Requests**
   - Enable **Allow auto-merge** (unblocks `gh pr merge --squash --auto`)
   - Prefer **Allow squash merging** only (disable merge commit + rebase if you want skill default = only squash)
2. **Settings → Rules → `public-access`**
   - Keep **0** required approvals
   - Set **Allowed merge methods** to **squash** only
   - Under **Bypass list**, add the **Cursor** GitHub App (or the bot that opens PRs) so it can squash-merge without a human click — otherwise every merge stays manual
   - Do **not** require status checks unless CI exists and is green for agent PRs
3. **Land open agent PRs** with **Squash and merge** until step 1–2 are done

## Agent behavior after this checklist

When the user asks to **commit, push, and merge**, the skill:

1. Opens a ready (non-draft) PR via ManagePullRequest  
2. Runs `gh pr merge <n> --squash --delete-branch`  
3. On policy delay, runs `gh pr merge <n> --squash --auto --delete-branch`  
4. Never uses `--admin` unless the user explicitly authorizes it (and even then, bypass may still be required)  
5. If still blocked, prints the PR URL and points here  

## Stale PR hygiene

Before opening a new date-stamp / rule-test PR, close or squash-merge any open duplicates (`gh pr list --state open`).

---

## Change Log

- v1.1 (2026-08-23): Rule test #3 — document merge/--auto/--admin failures; require ruleset bypass for Cursor app.
- v1.0 (2026-08-23): Initial owner checklist after rule tests #1–#2 (smoothers).

## Attribution

- Project: Wargame_Concierge | Maintainer: Russell Catt

## Rising Tide Notes

- Keep the receipts. Agent cannot PATCH repo settings; this page is the human half of the smoother.
