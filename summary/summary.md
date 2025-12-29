# summary

Generate comprehensive project documentation that captures structure, features, functionality, and recent development history.

1. **Analyze project structure** - Run `tree -L 1` to identify top-level directories, then use `tree -L 4 -a -I 'node_modules|.git|__pycache__|.pytest_cache|.vscode'` to get detailed structure
2. **Review codebase and history** - Examine existing code, conversation history, and recent changes to understand the project
3. **Document project overview** - Write comprehensive summary including file structure, main features, and key functionalities
4. **Capture recent mistakes and fixes** - Document recent mistakes made during development and how they were fixed in extreme detail
5. **Include recent changes** - Incorporate information from recent changes and development activity
6. **Create summary document** - Save the complete summary to `working_directory/summary/summary.md`

Focus on:
- Complete project structure visualization
- Main features and key functionalities
- Recent development mistakes and their resolutions (in extreme detail)
- Recent changes and their impact
- Clear organization and readability
- Comprehensive coverage of project state

Consider both:
- Current project state (what exists now?)
- Development history (what happened recently, what mistakes were made and fixed?)

Format the summary as:
- Structured markdown document
- Clear sections for structure, features, functionality, and recent history
- Detailed documentation of mistakes and fixes
- Recent changes section
- Saved to `working_directory/summary/summary.md`

Provide a complete picture of the project that helps understand both current state and recent development journey.
