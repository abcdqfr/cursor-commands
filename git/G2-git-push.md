# git-push

Push current branch to origin and sync with remote updates.

1. **Fetch** - `git fetch origin`
2. **Rebase (optional)** - `git rebase origin/main` (if not on main)
3. **Push** - `git push -u origin HEAD`
4. **If rejected** - `git pull --rebase && git push`
5. **Force push (if needed)** - Ask user first, then `git push --force-with-lease`

Focus on:
- Linear history (prefer rebase over merge)
- Syncing before push to avoid conflicts
- Safe force push (`--force-with-lease`)

Notes:
- Always ask before force pushing
- Use `--force-with-lease` not `--force`
