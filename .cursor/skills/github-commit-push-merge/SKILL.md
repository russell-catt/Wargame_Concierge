---
name: github-commit-push-merge
description: >-
  Commit, push, open/update PRs, and merge work for the Wargame_Concierge
  GitHub repo (russell-catt/Wargame_Concierge). Use when the user asks to
  commit, push, open a PR, merge to main, clean up cursor branches, or
  ship finished agent work to GitHub. Encodes branch naming, protected-main
  rules, ManagePullRequest vs gh CLI, and squash-and-merge as the default
  merge method.
---

# GitHub commit / push / merge (Wargame_Concierge)

Repo: `https://github.com/russell-catt/Wargame_Concierge`  
Default protected branch: `main`

## When to use this skill

Run this workflow when the user (or an explicit cloud-agent task) asks to **commit**, **push**, **open/update a PR**, **merge to main**, or **clean up `cursor/` branches**.

**Do not** use it automatically just because files changed. Multi-agent playbook default: Coordinator owns git; Librarian / Implementer / QA subagents normally leave the tree dirty unless the user or cloud-agent instructions explicitly require ship steps.

## Hard rules for this repository

1. **Never push commits directly to `main`.** Branch protection rejects it (`GH013: Cannot update this protected ref`). Always ship via a feature branch + pull request.
2. **Feature branch names** must match: `cursor/<descriptive-kebab>-b7e0`  
   - Prefix `cursor/`  
   - Suffix `-b7e0`  
   - Lowercase only  
   Example: `cursor/readme-date-stamp-b7e0`
3. **`gh` CLI is read-only here** for write operations. Use it to *inspect* (`gh pr view`, `gh pr list`, `gh run list`). Do **not** use `gh pr create`, `gh pr merge`, or other mutating `gh` commands.
4. **Create/update PRs with the `ManagePullRequest` tool** (`create_pr` / `update_pr`). Always set `branch_name` and `base_branch` (`main` unless the user says otherwise).
5. Prefer **draft PRs** unless the user asks for ready-for-review.
6. Commit messages: use a HEREDOC; include a clear subject. If the user gives an exact commit reason/message, use that text as the subject (or first line).
7. Do not commit secrets, `.env`, or binaries blocked by `.gitignore` (PDFs/images). Do not write under `raw/`.
8. **Whenever the user requests a merge, use squash and merge only.** Do not create a merge commit and do not rebase-merge unless the user explicitly asks for a different method.

## Standard ship workflow

### 1. Orient

```bash
git fetch origin
git status
git branch --show-current
git log -5 --oneline
```

If you are on a dirty `main`, do **not** commit there. Create/switch to a feature branch first.

### 2. Branch

```bash
git checkout main
git pull origin main
git checkout -b cursor/<descriptive-kebab>-b7e0
```

Reuse an existing `cursor/...-b7e0` branch for the same task when one already tracks the work.

### 3. Stage and commit

```bash
git status
git diff
git add <paths...>   # avoid blanket git add -A unless the user wants everything
git commit -m "$(cat <<'EOF'
<subject line>

<optional body>
EOF
)"
```

If commit fails due to hooks, fix the issue and create a **new** commit (do not `--amend` unless the user asks and the commit has not been pushed, or amend rules in the session allow it).

### 4. Push branch

```bash
git push -u origin cursor/<descriptive-kebab>-b7e0
```

On network failure, retry with backoff (about 4s, 8s, 16s, 32s) up to 4 times.

### 5. Open or update the PR

Use **ManagePullRequest**:

- **create_pr:** `title`, `body`, `branch_name`, `base_branch: main`, `draft` as appropriate  
- **update_pr:** when iterating on the same branch; update `body`/`title` only when needed  

PR body should summarize what changed and note that merge to `main` is **squash and merge** (protected `main`; no direct pushes).

### 6. Merge to `main` (squash only)

**Default merge method: squash and merge.** Apply this whenever the user asks to merge (including “merge to main”, “squash merge”, or “land this PR”).

| Method | When |
|--------|------|
| **Squash and merge** | **Always**, when the user requests a merge |
| Create a merge commit | Only if the user explicitly asks |
| Rebase and merge | Only if the user explicitly asks |

**Preferred path while `main` is push-protected:** user (or GitHub UI) clicks **Squash and merge** on the PR. Tell them to use that button — not “Create a merge commit” or “Rebase and merge”.

**Agent attempts (in order):**

1. Confirm PR is mergeable: `gh pr view <n> --json state,mergeable,url`
2. Do **not** `git push origin main` — protection rejects it.
3. Do **not** fast-forward or merge the feature branch into local `main` and push.
4. If merge write access is available for this environment, squash-merge the PR (e.g. `gh pr merge <n> --squash --delete-branch` when `gh` writes are allowed for merge). Prefer deleting the head branch after a successful squash.
5. If write merge is blocked (current default: `gh` mutating commands disallowed; ManagePullRequest has no merge action), report the PR URL and ask the user to **Squash and merge** in GitHub.

After a successful squash merge, `git fetch origin main` and reset local `main` to `origin/main`.

If local `main` was accidentally fast-forwarded during a failed push attempt, reset it so it matches remote:

```bash
git fetch origin main
git checkout main
git reset --hard origin/main
```

Keep the feature branch tip intact for the open PR until squash merge completes.

### 7. After merge — cleanup `cursor/` branches

Only delete branches that are **merged** (or explicitly abandoned by the user). **Keep** branches that still have open PRs.

```bash
# Inspect
gh pr list --state merged --limit 30 --json number,headRefName,mergedAt
gh pr list --state open --limit 30 --json number,headRefName,title,url

# Delete one merged branch (remote then local)
git push origin --delete cursor/<merged-branch>-b7e0
git branch -D cursor/<merged-branch>-b7e0
```

Stay on `main` aligned to `origin/main` after cleanup.

## Role conflict cheat-sheet

| Context | Git allowed? |
|---------|----------------|
| User says commit/push/merge, or cloud-agent task requires shipping | **Yes** — follow this skill |
| Librarian / Implementer / QA slice with no ship gate | **No** — leave dirty tree; report paths |
| AGENTS.md “never commit” vs cloud ship instructions | Cloud/user ship request wins for that turn; still use PRs, not direct `main` |

## Quick failure map

| Symptom | Meaning | Action |
|---------|---------|--------|
| `GH013` / `Cannot update this protected ref` on `main` | Branch protection working | Ship via PR; ask user to **Squash and merge** |
| `gh pr create` fails / disallowed | `gh` write blocked | Use ManagePullRequest |
| Push rejected on feature branch | Auth/network/rule | Retry backoff; check remote permissions |
| Local `main` ahead of `origin/main` after failed merge push | Local-only FF | `git reset --hard origin/main` |
| User asked to merge; wrong method used | Policy | Always **squash**; never merge-commit/rebase unless asked |

## Done criteria

- [ ] Changes committed on `cursor/...-b7e0` (not on `main`)
- [ ] Branch pushed to `origin`
- [ ] PR created or updated against `main`
- [ ] If user requested merge: **squash and merge** used (or user pointed at Squash and merge in GitHub)
- [ ] User informed how to merge if protection blocks the agent
- [ ] Merged `cursor/` branches cleaned up when requested; open-PR branches kept
