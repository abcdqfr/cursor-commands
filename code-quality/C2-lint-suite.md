# lint-suite

Run project-wide linters, apply fixes, and ensure the codebase meets formatting and style requirements before merging changes.

1. **Execute project linters** - Run the standard lint command with autofix enabled if available, capture any remaining errors or warnings from the output, and identify files requiring manual attention
2. **Resolve findings across codebase** - Apply targeted fixes, keeping edits minimal and idiomatic, refactor repeated issues such as unused variables or long functions, and update configuration or suppressions only when justified
3. **Verify cleanliness** - Re-run the lint command to ensure a zero-issue result, spot-check key files for formatting and readability, and stage the changes with clear commit messages when satisfied

Focus on:
- Project-wide scope (entire codebase)
- Standard lint command execution
- Autofix results review
- Manual issue resolution across multiple files
- Configuration and suppression management
- Final verification of zero-issue state
- Pre-merge codebase cleanliness

Consider both:
- Individual file issues (may require file-by-file attention)
- Systemic issues (configuration, patterns, repeated violations)

Format the output as:
- Linter execution results
- Files requiring manual attention
- Applied fixes summary
- Final verification status
- Staging recommendations

Run project linters and ensure codebase-wide compliance with formatting and style requirements.
