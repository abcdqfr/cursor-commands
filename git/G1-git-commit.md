# git-commit

Create a short, focused commit message and commit staged changes.

1. **Review changes** - `git diff --cached` (staged) or `git diff` (unstaged)
2. **Check for issue key** - Check branch name for issue key (optional). Ask user if they want to include one.
3. **Stage changes** - `git add -A` (if not already staged)
4. **Commit** - `git commit -m "<type>(<scope>): <summary>"` or `git commit -m "<issue-key>: <type>(<scope>): <summary>"`

Focus on:
- Clear commit messages (what and why)
- Conventional commits format
- <= 72 characters, imperative mood, no period

Format: `<type>(<scope>): <summary>` or `<issue-key>: <type>(<scope>): <summary>`

Examples:
- `git commit -m "fix(auth): handle expired token refresh"`
- `git commit -m "PROJ-123: fix(auth): handle expired token refresh"`
