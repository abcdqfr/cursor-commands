# Command Arsenal Documentation

Complete documentation for the Cursor command arsenal system.

---

# Command Quick Reference

Type `/` in Cursor to access any command instantly. All commands are indexed A1-Z9 for easy reference.

## A - Architect

- **A1** `A1-architect.md` – Transform project ideas into well-structured implementations
- **A2** `A2-diagrams.md` – Generate Mermaid diagrams (flowcharts, sequence, class, ER, state diagrams)
- **A3** `A3-refactor-code.md` – Improve code quality while maintaining functionality

## B - Behavior

- **B1** `B1-behavior.md` – Maintain high code quality and professional standards
- **B2** `B2-add-error-handling.md` – Implement comprehensive error handling across the change set
- **B3** `B3-optimize-performance.md` – Analyze and optimize code performance

## C - Code-Quality

- **C1** `C1-lint-fix.md` – Automatically analyze and fix linting issues in the current file
- **C2** `C2-lint-suite.md` – Run project linters, apply fixes, and ensure codebase meets formatting requirements
- **C3** `C3-code-review.md` – Comprehensive review checklist with structured steps and focus areas
- **C4** `C4-deslop.md` – Clean up AI-generated code by removing unnecessary complexity and verbosity
- **C5** `C5-write-unit-tests.md` – Generate focused unit tests with proper coverage
- **C6** `C6-run-all-tests-and-fix.md` – Execute the full suite, triage failures, and confirm fixes

## D - Documentation

- **D1** `D1-add-documentation.md` – Capture comprehensive product or code documentation
- **D2** `D2-generate-api-docs.md` – Produce rich API documentation with schemas and examples
- **D3** `D3-overview.md` – Generate Mermaid diagrams for user journey and architecture flow
- **D4** `D4-visualize.md` – Generate visual diagrams and flowcharts from code or concepts

## E - Eval

- **E1** `E1-debug.md` – Root cause analysis with step-by-step investigation
- **E2** `E2-debug-issue.md` – Step-by-step debugging workflow for isolating defects
- **E3** `E3-fix-compile-errors.md` – Diagnose and resolve compilation failures quickly
- **E4** `E4-docker-logs.md` – Tail and monitor Docker container logs for debugging

## G - Git

- **G1** `G1-git-commit.md` – Create well-structured commit messages with optional issue key linking
- **G2** `G2-git-push.md` – Push changes to remote with pre-push checks
- **G3** `G3-fix-git-issues.md` – Resolve merge conflicts and repository problems safely
- **G4** `G4-git-commit-analyze-resume-trajectory.md` – Commit, push, and analyze git history for context

## I - Internet

- **I1** `I1-web-search.md` – Cite authoritative instructions and information from the web
- **I2** `I2-research.md` – Conduct online technical research using web search and internet sources
- **I3** `I3-summarize-and-search.md` – Summarize intent and find answers from authoritative online sources
- **I4** `I4-latest-info.md` – Research latest information, updates, and current state online
- **I5** `I5-battle-tested-solutions.md` – Research mature alternatives online for custom implementations

## M - Meta

- **M1** `M1-create-commands-from-examples.md` – Create new command entries based on example patterns
- **M2** `M2-meta-interaction-trace.md` – Record interaction data for prompt engineering debugging
- **M3** `M3-enhance-command-arsenal` – Enhance command arsenal (script)

## P - Project-Management

- **P1** `P1-clarify-task.md` – Break down ambiguous tasks into clear, actionable steps
- **P2** `P2-setup-new-feature.md` – Plan requirements, branching, and architecture for new work
- **P3** `P3-roadmap-pp.md` – Analyze codebase and generate visual feature roadmaps
- **P4** `P4-burn-down-roadmap.md` – Convert roadmap checkpoints into actionable todos
- **P5** `P5-database-migration.md` – Plan, create, and validate database migrations with rollbacks
- **P6** `P6-onboard-new-developer.md` – Checklist-driven onboarding for new teammates

## R - Research

- **R1** `R1-research.md` – Conduct efficient offline technical research using codebase, index, and documentation
- **R2** `R2-codebase-search.md` – Search and explore codebase systematically
- **R3** `R3-custom-imp-check.md` – Identify custom implementations that could use mature solutions
- **R4** `R4-battle-tested-solutions.md` – Identify custom implementations in codebase (offline analysis)
- **R5** `R5-round-table.md` – Comprehensive synthesis of all contexts into unified debrief

## S - Security

- **S1** `S1-security-audit.md` – Structured security checklist for code changes
- **S2** `S2-security-review.md` – Broader vulnerability and risk assessment workflow
- **S3** `S3-accessibility-audit.md` – Review for WCAG compliance issues

## T - Transcript

- **T1** `T1-summary.md` – Project structure visualization and documentation
- **T2** `T2-distill-to-volumes-md.md` – Transform conversations into organized markdown volumes

## W - Workflow

- **W1** `W1-create-pr.md` – Prepare a well-structured pull request with validation checklist
- **W2** `W2-generate-pr-description.md` – Draft detailed pull-request descriptions automatically
- **W3** `W3-address-github-pr-comments.md` – Process reviewer feedback and craft thoughtful responses
- **W4** `W4-light-review-existing-diffs.md` – Quick pass to highlight risky diffs and cleanup items
- **W5** `W5-create-spec-repo.md` – Create public-safe specification repository from private infrastructure

---

## Pipeability Feature

Commands with `-pp` suffix are pipeable and can be chained together following Unix philosophy: "do one thing well, pipe together."

**Find pipeable commands:** Search for `-pp` in command names (e.g., `/pp` in Cursor to find all pipeable commands).

**Pipeable Commands:**

- **C7** `C7-scan-annotations-pp.md` - Outputs structured annotation report
- **P3** `P3-roadmap-pp.md` - Accepts annotation input via pipe or `--from-annotations` flag

**Usage Examples:**

```bash
# Direct pipe from annotation scanner to roadmap
cursor-commands scan-annotations-pp | cursor-commands roadmap-pp --from-annotations

# Or save intermediate results
cursor-commands scan-annotations-pp > /tmp/annotations.txt
cursor-commands roadmap-pp --input /tmp/annotations.txt
```

**Naming Convention:** Commands ending in `-pp` are pipeable.

---

---

# Offline vs Online Command Organization

**Purpose:** Document the organization of commands into offline (codebase/index/documentation) and online (web/internet/latest) categories

## Directory Structure

### `research/` - Offline Codebase Research

Commands that work with local codebase, index, documentation, and project files.

- **R1** `R1-research.md` - Conduct offline technical research using codebase, index, and documentation
- **R2** `R2-codebase-search.md` - Search and explore codebase systematically
- **R3** `R3-custom-imp-check.md` - Analyze codebase to identify custom implementations
- **R4** `R4-battle-tested-solutions.md` - Identify custom implementations in codebase (offline analysis)
- **R5** `R5-round-table.md` - Synthesize contexts from open files, recent edits, project structure

### `internet/` - Online Web Research

Commands that use web search, internet sources, and latest online information.

- **I1** `I1-web-search.md` - Cite authoritative instructions from the web
- **I2** `I2-research.md` - Conduct online technical research using web search and internet sources
- **I3** `I3-summarize-and-search.md` - Summarize intent and find answers from authoritative online sources
- **I4** `I4-latest-info.md` - Research latest information, updates, and current state online
- **I5** `I5-battle-tested-solutions.md` - Research mature alternatives online for custom implementations

## Command Variants

Some commands have both offline and online variants:

### Research

- **Offline:** `research/R1-research.md` - Uses codebase, index, documentation
- **Online:** `internet/I2-research.md` - Uses web search, internet sources

### Battle-Tested Solutions

- **Offline:** `research/R4-battle-tested-solutions.md` - Identifies custom implementations in codebase
- **Online:** `internet/I5-battle-tested-solutions.md` - Researches mature alternatives online

## Principles

1. **Never Delete** - Commands are moved, not deleted
2. **Never Copy** - Create variants in proper directories, don't duplicate
3. **Clear Separation** - Offline commands in `research/`, online commands in `web/`
4. **Proper Organization** - Maintain directory structure and naming conventions
5. **Variant Creation** - When a command needs both offline/online capabilities, create variants in appropriate directories

## Usage Guidelines

### When to use `research/` commands

- Searching codebase
- Analyzing project structure
- Reviewing local documentation
- Finding patterns in existing code
- Understanding project conventions

### When to use `web/` commands

- Finding latest information
- Researching external tools/libraries
- Looking up official documentation online
- Finding community solutions
- Getting current best practices


---

