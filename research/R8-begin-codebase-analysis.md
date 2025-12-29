# begin-codebase-analysis

Orient any agent or LLM with the codebase structure, organization, and navigation patterns. Answer "what the heck is in the codebase and how do we best organize it?"

1. **Map the codebase structure** - Identify top-level directories, their purposes, and how they relate. Use `list_dir` and `glob_file_search` to discover the directory tree and file organization patterns.
2. **Identify key entry points** - Find README files, main configuration files, entry point scripts, and documentation that explain the system's purpose and architecture.
3. **Understand organization patterns** - Analyze how code is organized (by feature, by layer, by domain, by technology). Identify naming conventions, directory structures, and organizational principles.
4. **Catalog major components** - List the main components, modules, services, or subsystems. Understand what each does and how they interact.
5. **Document navigation patterns** - Identify how to find specific types of content (code, config, docs, tests, scripts). Map common tasks to their locations.
6. **Assess organization quality** - Evaluate whether the current organization makes sense, identify potential improvements, and suggest better organizational patterns if needed.
7. **Create orientation summary** - Synthesize findings into a clear summary that helps future agents understand the codebase structure and how to navigate it effectively.

Focus on:
- Top-level directory structure and purposes
- Key entry points (README, main files, configs)
- Organization patterns and conventions
- Major components and their relationships
- Navigation patterns for finding content
- File naming conventions and structure
- Documentation locations and structure
- Build/test/deploy organization

Consider both:
- Explicit organization (what directories and files exist)
- Implicit patterns (how things are actually organized in practice)

Format the analysis as:
- **Codebase Structure Map** - Directory tree with purposes
- **Key Entry Points** - Main files, READMEs, configs with descriptions
- **Organization Patterns** - How code is organized and why
- **Major Components** - List of main subsystems with descriptions
- **Navigation Guide** - How to find specific types of content
- **Organization Assessment** - Quality evaluation and improvement suggestions
- **Quick Reference** - Summary for future orientation

Begin codebase analysis with systematic exploration to understand structure, organization, and navigation patterns.
