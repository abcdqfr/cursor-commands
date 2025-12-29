# research-annotation-tools

Research existing annotation scanning tools and solutions to learn from predecessors and avoid reinventing the wheel.

1. **Identify the problem space** - Define what we're building: POSIX-compatible annotation scanner that outputs structured, pipeable reports
2. **Search for existing solutions** - Use `internet/I1-web-search.md` to find:
   - Command-line annotation scanners (TODO/FIXME finders)
   - Code analysis tools with annotation support
   - POSIX-compatible scanning utilities
   - Tools that output structured/pipeable formats
3. **Analyze architecture patterns** - Study how existing tools:
   - Scan codebases (grep, ripgrep, custom parsers)
   - Categorize annotations (by type, file, priority)
   - Output structured data (JSON, CSV, custom formats)
   - Handle POSIX compatibility
4. **Evaluate feature sets** - Compare capabilities:
   - Annotation pattern matching
   - Semantic sorting/categorization
   - Output formats (structured, pipeable)
   - Integration with other tools
   - Performance on large codebases
5. **Identify best practices** - Extract lessons learned:
   - How to handle edge cases (multi-line annotations, comments)
   - How to categorize files and annotations
   - How to structure output for maximum utility
   - How to ensure POSIX compatibility
6. **Document findings** - Create comprehensive report with:
   - List of tools found with URLs and descriptions
   - Architecture patterns and approaches
   - Feature comparison matrix
   - Best practices and lessons learned
   - Recommendations for our implementation

Focus on:
- **POSIX-compatible tools** - Tools that work on standard Unix systems
- **Structured output** - Tools that output parseable formats (not just grep)
- **Annotation scanning** - Tools specifically for TODO/FIXME/etc. scanning
- **Pipeable design** - Tools that can be piped to other commands
- **Open source solutions** - Learn from freely available implementations
- **Mature tools** - Well-established solutions with proven patterns

Consider both:
- **Standalone tools** (dedicated annotation scanners)
- **Integrated features** (annotation scanning as part of larger tools)

Format research as:
- **Tools discovered** - List with URLs, descriptions, and key features
- **Architecture patterns** - How different tools approach the problem
- **Feature comparison** - Matrix comparing capabilities
- **Best practices** - Lessons learned from existing implementations
- **Recommendations** - How to apply learnings to our implementation
- **Citations** - All sources with full URLs and authority levels

**Search Queries to Use:**
- "TODO FIXME scanner command line tool"
- "annotation scanner POSIX compatible"
- "code annotation finder structured output"
- "TODO scanner pipeable JSON CSV"
- "ripgrep TODO FIXME scanner"
- "code analysis annotation tools"

**Example Tools to Research:**
- `leasot` (Node.js annotation scanner)
- `todo-cli` tools
- `ack` / `ag` / `ripgrep` with annotation patterns
- IDE annotation scanners
- CI/CD annotation detection tools

Use `internet/I1-web-search.md` to conduct thorough research and cite all sources with URLs.
