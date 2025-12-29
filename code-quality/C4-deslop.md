# deslop

Clean up AI-generated code by removing unnecessary complexity, verbosity, and inconsistencies with the codebase style.

1. **Review diff against main** - Check all changes introduced in the current branch compared to main
2. **Identify AI-generated artifacts** - Find unnecessary comments, defensive code, type workarounds, and style inconsistencies
3. **Remove unnecessary comments** - Delete comments that a human wouldn't add or that are inconsistent with the rest of the file
4. **Remove excessive defensive code** - Eliminate extra try/catch blocks or defensive checks that are abnormal for the codebase, especially in trusted/validated codepaths
5. **Fix type workarounds** - Remove casts to `any` or other type workarounds that bypass proper typing
6. **Align with codebase style** - Ensure all code matches the existing style and patterns in the file
7. **Report changes** - Provide a 1-3 sentence summary of what was changed

Focus on:
- Removing unnecessary verbosity and complexity
- Maintaining consistency with existing codebase style
- Eliminating defensive code in trusted paths
- Fixing type system workarounds
- Preserving only meaningful comments
- Code that looks like it was written by a human developer

Consider both:
- What AI typically adds (excessive comments, defensive checks, type workarounds)
- What the codebase actually needs (minimal, clean, consistent code)

Format the cleanup as:
- Clean code that matches existing style
- Removed unnecessary artifacts
- Final 1-3 sentence summary of changes made

Remove AI-generated slop while preserving functionality and maintaining codebase consistency.
