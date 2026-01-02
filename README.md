# Intelligent Command Router (Entry Point)

This README.md is the **single source of truth** for routing all commands in this repo.
It acts as a continuously running **intelligent entrypoint** that:

- Gathers full context dynamically  
- Applies priority-based routing rules  
- Selects and sequences commands intelligently  
- Handles ambiguity with context synthesis  
- Guards destructive or irreversible actions  
- Operates in two modes: **Sequence** and **Series**

---

## Phase 0: Guardrails & Authority

Before any action:

- Confirm destructive or irreversible operations  
- Confirm ambiguous authority contexts (prod vs dev, personal vs shared)  
- In production contexts or repos marked `production-no-markdown`, forbid doc generation unless explicitly authorized  

**If triggered:** pause & request explicit user confirmation.

---

## Phase 1: Context Gathering (Round-Table)

Collect context from:

- Open files, cursor position, recent edits  
- Project structure & file organization  
- Conversation history & implicit user goals  
- Error messages, linter output, test failures  
- Git status (changes, branches, conflicts)  
- Build & compilation status  
- Recent command patterns and workflows  

Extract key indicators:

- **Critical errors:** compile errors, runtime crashes, git conflicts  
- **Quality issues:** linter warnings, test failures, code smells  
- **Feature work:** new requirements, unclear specs, architecture needs  
- **Workflow tasks:** PR creation, commits, documentation gaps  
- **Research needs:** unknown patterns, external solutions  
- **Intent drift:** conflicting signals or repeated retries  

Synthesize overall situation:

- Primary user need?  
- Blocking issues?  
- Most effective action sequence?  
- Implicit goals not stated?

---

## Execution Modes

- **HILF (Human-In-The-Loop Feedback):** For unclear intent or authority. Focuses on clarification & guided decisions.  
- **CIHF (Continuous Integration with Human Feedback):** For clear intent but requires iterative validation and quality checks.  

Auto-selected based on context confidence.

---

## Phase 2: Command Routing Logic

### Priority -1: Environment & Tooling Corruption (Run First)

- Broken test suite, misconfigured linters, dirty git from generated artifacts  
- **Route:** `research/R3-round-table.md` or environment analysis  
- Prevent endless fix-fail loops.

---

### Priority 1: Critical Blockers (Immediate)

| Issue                   | Command(s)                                               |
|-------------------------|----------------------------------------------------------|
| Compilation errors      | `evaluation/E2-fix-compile-errors.md`                    |
| Persistent errors       | `evaluation/E1-debug.md`                                 |
| Missing tests           | `code-quality/C5-write-unit-tests.md`                    |
| Git conflicts/merges    | `git/G3-fix-git-issues.md`                               |
| Build/runtime failures  | `evaluation/E1-debug.md` (+ `E3-docker-logs.md` Docker)  |
| Post-fix tests          | `code-quality/C6-run-all-tests-and-fix.md`               |

---

### Priority 2: Quality Gates (Precede feature work)

| Issue                  | Command(s)                                                                |
|------------------------|---------------------------------------------------------------------------|
| Linter issues          | `code-quality/C1-lint-file.md` (single) or `C2-lint-suite.md` (multiple)  |
| Test failures          | `code-quality/C6-run-all-tests-and-fix.md`                                |
| Missing tests          | `code-quality/C5-write-unit-tests.md`                                     |
| Code quality concerns  | `code-quality/C3-code-review.md` + optional `C4-deslop.md`                |

---

### Priority 3: Feature Development

| Task                      | Command(s)                                                                                                 |
|---------------------------|------------------------------------------------------------------------------------------------------------|
| Unclear/ambiguous task    | `project-management/P1-clarify-task.md`                                                                    |
| New feature               | `P1-clarify-task.md` → `architect/A1-architect.md` → `P2-setup-new-feature.md` → `C5-write-unit-tests.md`  |
| Refactoring               | `architect/A2-refactor-code.md` → `C3-code-review.md` → `C6-run-all-tests-and-fix.md`                      |
| Performance optimization  | `behavior/B3-optimize-performance.md` → `C6-run-all-tests-and-fix.md`                                      |

---

### Priority 4: Documentation & Research

| Task                      | Command(s)                                                                                                              |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Documentation gaps        | `documentation/D1-add-documentation.md` or `D2-generate-api-docs.md` or `D3-overview.md` or `D4-visualize.md`           |
| Research needs            | `research/R1-offline-codebase-research.md` or `internet/I2-summarize-and-search.md` or `I4-battle-tested-solutions.md`  |
| Understand existing code  | `research/R3-round-table.md` or `project-management/P7-summarize-codebase.md`                                           |

---

### Priority 5: Workflow & Git Operations

| Task                 | Command(s)                                                                                                                                               |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Pre-commit workflow  | `C1-lint-file.md` or `C2-lint-suite.md` → `C6-run-all-tests-and-fix.md` → `git/G1-git-commit.md`                                                         |
| Pre-PR workflow      | `C2-lint-suite.md` → `C6-run-all-tests-and-fix.md` → `workflow/W4-light-review-existing-diffs.md` → `W2-generate-pr-description.md` → `W1-create-pr.md`  |
| Git commit/push      | `git/G1-git-commit.md`, `git/G2-git-push.md`                                                                                                             |

---

### Priority 6: Security & Accessibility

| Task                 | Command(s)                                                  |
|----------------------|-------------------------------------------------------------|
| Security audit       | `security/S1-security-audit.md` or `S2-security-review.md`  |
| Accessibility audit  | `security/S3-accessibility-audit.md`                        |

---

### Priority 7: Behavior & Error Handling

| Task                        | Command(s)                           |
|-----------------------------|--------------------------------------|
| Add missing error handling  | `behavior/B2-add-error-handling.md`  |
| Fix code behavior issues    | `behavior/B1-behavior.md`            |

---

## Phase 3: Command Execution Patterns

- **Sequence (Ordered Execution)**  
  Example:  
  `P1-clarify-task.md` → `A1-architect.md` → `P2-setup-new-feature.md` → Implementation → `C6-run-all-tests-and-fix.md` → `G1-git-commit.md`

- **Series (Iterative/Parallel Exploration)**  
  Anchored on: `research/R3-round-table.md`  
  Example:  
  `R3-round-table.md` → synthesis → `M0-create-new-command.md`

---

## Phase 4: Routing Algorithm (Simplified)

1. Gather context (Phase 1)  
2. Apply guardrails (Phase 0) — if blocked, pause for confirmation  
3. Identify highest priority need (−1 to 7)  
4. Map to commands accordingly  
5. Choose execution pattern (Sequence or Series)  
6. Execute commands with full context awareness  
7. After each command or chain, re-gather context  
8. If primary need repeats twice without resolution, escalate to `R3-round-table.md`  
9. Limit automatic chains to 5 commands — then ask for user input  

---

## Ambiguity & Edge Handling

- If ambiguous: start with `research/R3-round-table.md`  
- Ask **one** clarifying question if needed  
- Default conservative paths for low confidence  
- For prose-to-code or pattern detection:  
  Start with `R3-round-table.md` → if stable, `M0-create-new-command.md`  

---

## Output Format (Always)

1. **Context Summary**  
2. **Routing Decision** (commands, sequence/series, confidence)  
3. **Execution Plan** (step order with purpose)  
4. **Proceed with Execution**  

---

## Quick Start Usage Examples

- **Bug Fix:**  
  `entrypoint` → `E1-debug.md` → `E2-fix-compile-errors.md` → `C5-write-unit-tests.md` → `C6-run-all-tests-and-fix.md`

- **New Feature:**  
  `entrypoint` → `P1-clarify-task.md` → `A1-architect.md` → `P2-setup-new-feature.md`

- **Code Quality Pass:**  
  `entrypoint` → `C2-lint-suite.md` → `C6-run-all-tests-and-fix.md` → `C3-code-review.md`

- **Command Creation:**  
  `R3-round-table.md` → synthesis → `M0-create-new-command.md`

---

## Philosophy & Principles

- Context is king — gather full context before decisions  
- Blockers first — critical issues before features/workflows  
- Quality gates — lint/test before commits/PRs  
- No aspirational bytes — only functional, production-ready commands  
- Series for exploration, Sequence for execution  

---

## Commands Directory Overview

- Core: `README.md` (this router), `R3-round-table.md`, `M0-create-new-command.md`  
- Architect: `A1-architect.md`, `A2-refactor-code.md`, `A5-align-production.md`  
- Behavior: `B1-behavior.md`, `B2-add-error-handling.md`, `B3-optimize-performance.md`  
- Code Quality: `C1-lint-file.md`, `C2-lint-suite.md`, `C3-code-review.md`, `C5-write-unit-tests.md`, `C6-run-all-tests-and-fix.md`  
- Documentation: `D1-add-documentation.md`, `D2-generate-api-docs.md`  
- Evaluation: `E1-debug.md`, `E2-fix-compile-errors.md`, `E3-docker-logs.md`  
- Git: `G1-git-commit.md`, `G2-git-push.md`, `G3-fix-git-issues.md`  
- Internet: `I2-summarize-and-search.md`, `I4-battle-tested-solutions.md`  
- Project Management: `P1-clarify-task.md`, `P2-setup-new-feature.md`  
- Research: `R3-round-table.md`  
- Security: `S1-security-audit.md`  
- Workflow: `W1-create-pr.md`, `W4-light-review-existing-diffs.md`  

---

*This README.md serves as both your **intelligent router** and **human-readable command reference**. Use it as the only entrypoint for all development workflows.*
