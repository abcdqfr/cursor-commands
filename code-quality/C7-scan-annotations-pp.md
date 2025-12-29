# scan-annotations

Scan codebase for annotation markers (TODO, FIXME, NOTE, HACK, XXX, BUG, WARNING, DEPRECATED) and generate a semantically sorted report to `/tmp` for analysis and roadmap integration.

1. **Scan codebase** - Use POSIX-compatible grep to find all annotation markers across all file types
2. **Extract context** - Capture file path, line number, annotation type, and full message
3. **Generate structured report** - Output to `/tmp/annotations-$(date +%Y%m%d-%H%M%S).txt` in parseable format
4. **Semantic analysis** - Categorize by:
   - Annotation type (TODO, FIXME, NOTE, HACK, XXX, BUG, WARNING, DEPRECATED)
   - File category (CODE, CONFIG, SCRIPT, DOCS, OTHER)
   - Priority (HIGH for FIXME/BUG, MEDIUM for TODO/WARNING, LOW for NOTE/HACK/XXX, INFO for DEPRECATED)
   - Age (if git history available, optional)
5. **Sort semantically** - Group by:
   - Priority (HIGH → MEDIUM → LOW → INFO)
   - Category (CODE → CONFIG → SCRIPT → DOCS → OTHER)
   - File path (alphabetical within category)
6. **Generate summary** - Count by type, category, and priority at end of report
7. **Output for piping** - Format output so it can be piped directly to roadmap command

Focus on:
- **POSIX compatibility** - Works with standard shell tools (grep, find, awk, sort) on any POSIX system
- **Pipeable output** - Structured format that can be piped to other commands (roadmap, analysis tools)
- **Semantic grouping** - Logical organization by priority and category, not just alphabetical
- **Context preservation** - File path, line number, full message preserved
- **Actionable format** - Easy to convert to roadmap items or task lists
- **Comprehensive scanning** - Finds annotations in all file types (code, config, docs, scripts)

Consider both:
- **Annotation patterns** (TODO, FIXME, NOTE, HACK, XXX, BUG, WARNING, DEPRECATED)
- **File types** (code files: .nix, .py, .rs, .go, .js, .ts; config: .yml, .yaml, .json, .toml; docs: .md, .txt, .rst; scripts: .sh, .bash)

Format output as:
- **Structured text** - Pipe-separated format: `TYPE|PRIORITY|CATEGORY|FILE|LINE|MESSAGE`
- **Semantic sections** - Grouped by priority and category
- **Summary statistics** - Counts by type and category at end
- **Pipeable** - Can be piped directly to roadmap command or other analysis tools
- **Report location** - Always outputs to `/tmp/annotations-TIMESTAMP.txt` and prints to stdout

**Output Format (POSIX-friendly):**
```
# Annotation Report - 2025-01-XX 12:34:56
# Format: TYPE|PRIORITY|CATEGORY|FILE|LINE|MESSAGE

FIXME|HIGH|CODE|scripts/validate.sh|42|Replace hardcoded IP with SSOT reference
BUG|HIGH|CODE|nix/modules/service.nix|89|Memory leak in cleanup function
TODO|MEDIUM|DOCS|docs/README.md|156|Add migration guide
NOTE|LOW|CODE|src/main.py|23|Consider refactoring this function
...

# Summary
# TODO: 15
# FIXME: 8
# BUG: 3
# NOTE: 12
```

**Usage with Roadmap:**
```bash
# Direct pipe to roadmap
cursor-commands scan-annotations | cursor-commands roadmap --from-annotations

# Or save and analyze separately
cursor-commands scan-annotations > /tmp/annotations.txt
cursor-commands roadmap --input /tmp/annotations.txt
```

**POSIX Script Location:**
- Script: `scripts/scan-annotations.sh`
- Must be executable and POSIX-compatible (`/bin/sh`, not bash)
- Uses only standard POSIX tools (grep, find, awk, sort)

Provide a POSIX-compatible scanner that generates actionable, semantically sorted reports ready for roadmap integration.
