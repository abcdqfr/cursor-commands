# identify-generative-content

Analyze codebase to identify what should be automatically generated (counts, indexes, listings, summaries) versus what should remain manually maintained, and recommend generation strategies.

1. **Scan for manual maintenance patterns** - Identify files/sections that contain:
   - **Counts** (command counts, file counts, line counts, etc.)
   - **Indexes** (alphabetical lists, categorized lists, numbered lists)
   - **File listings** (directory contents, file trees, file inventories)
   - **Summaries** (aggregated data, statistics, totals)
   - **Cross-references** (links between files, dependencies, relationships)
   - **Repeated structures** (tables, lists, sections that mirror file structure)

2. **Analyze data sources** - For each manual maintenance pattern, identify:
   - **Source of truth** (where does the actual data come from?)
   - **Derivation method** (how could it be computed?)
   - **Update frequency** (how often does it change?)
   - **Dependency chain** (what triggers updates?)

3. **Classify generation candidates** - Categorize each pattern:
   - **Should Generate** - Data-driven, changes frequently, error-prone if manual
   - **Should Hybrid** - Partially generated, with manual curation/overrides
   - **Should Manual** - Requires human judgment, narrative, context

4. **Identify generation strategies** - For each "Should Generate" item, determine:
   - **Script-based** (shell, Python, etc.) - For simple counts, listings
   - **Template-based** (Jinja2, etc.) - For structured documents
   - **Code-based** (Nix, etc.) - For complex derivations
   - **Hybrid** (script + template) - For formatted output

5. **Detect manual maintenance risks** - Flag patterns that are:
   - **Error-prone** (counts that drift, indexes that get out of sync)
   - **Labor-intensive** (large lists, frequent updates)
   - **Inconsistent** (same data in multiple places)
   - **Stale-prone** (rarely updated, easily forgotten)

6. **Recommend generation approach** - For each candidate, specify:
   - **What to generate** (specific sections, files, or data)
   - **How to generate** (tool, script, template)
   - **When to generate** (pre-commit, CI, manual trigger)
   - **Where to generate** (output location, format)

7. **Identify generation infrastructure** - Determine what's needed:
   - **Scripts** (generation scripts, validation scripts)
   - **Templates** (Jinja2, etc.)
   - **Hooks** (pre-commit, CI integration)
   - **Documentation** (how to regenerate, when to regenerate)

Focus on:
- **Counts and statistics** - Command counts, file counts, totals (should be code-generated)
- **Indexes and catalogs** - Alphabetical lists, categorized lists (should be code-generated)
- **File listings** - Directory contents, file trees (should be code-generated)
- **Cross-references** - Links, dependencies, relationships (should be code-generated)
- **Repeated structures** - Tables, lists that mirror file structure (should be code-generated)
- **Narrative content** - Explanations, context, decisions (should remain manual)
- **Human judgment** - Curation, prioritization, interpretation (should remain manual)

Consider both:
- **Accuracy** (manual counts drift, code counts are always accurate)
- **Maintenance burden** (manual updates are labor-intensive, generation is automated)
- **Human value** (narrative and context require human judgment)

Format analysis as:
- **Manual Maintenance Patterns Found:**
  - Pattern name and location
  - What it contains (counts, indexes, listings, etc.)
  - Source of truth (where data comes from)
  - Update frequency
  - Risk level (error-prone, labor-intensive, stale-prone)

- **Generation Candidates:**
  - **Should Generate** (list with rationale)
  - **Should Hybrid** (list with rationale)
  - **Should Manual** (list with rationale)

- **Generation Recommendations:**
  For each "Should Generate" item:
  - **What:** Specific content to generate
  - **How:** Generation method (script, template, code)
  - **When:** Trigger (pre-commit, CI, manual)
  - **Where:** Output location and format
  - **Script/Template:** Specific implementation approach

- **Generation Infrastructure Needed:**
  - Scripts to create
  - Templates to create
  - Hooks to set up
  - Documentation to write

**Examples of Should Generate:**
- Command counts in README (count actual files)
- Command indexes (scan directory structure)
- File listings (list directory contents)
- Statistics (count files, lines, etc.)
- Cross-reference tables (parse file contents)

**Examples of Should Manual:**
- Narrative explanations
- Design decisions and rationale
- Context and background
- Human-curated priorities
- Interpretive summaries

**Anti-patterns to flag:**
- ❌ Manual counts that could be `find | wc -l`
- ❌ Manual indexes that could be `ls | sort`
- ❌ Manual file listings that could be `tree` or `find`
- ❌ Manual statistics that could be computed
- ❌ Duplicate data in multiple places (should be single source of truth)

Provide actionable recommendations for making the codebase more generative and less error-prone.
