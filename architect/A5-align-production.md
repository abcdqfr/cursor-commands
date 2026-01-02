# Align Production with Vision

Focus on making production meet the reality in your head. Pull that reality by asking clarifying questions, then implement the Nix or Rego required in production. No markdown checkpoints - direct implementation only.

## Critical Rule

**If you find yourself creating a plan.md or ANY markdown file, STOP IMMEDIATELY and drop to questioning and implementation.**

## Steps

1. **Ask clarifying questions** - Use 2-4 focused multiple choice questions to understand:
   - What specific gap exists between production and your vision?
   - What architectural principle should be enforced?
   - What Nix structure or Rego policy is needed?
   - What is the target state (not the path, the end result)?

2. **Narrow scope iteratively** - If the request is too broad:
   - Ask which area to tackle first (structure, enforcement, service model, etc.)
   - Ask which specific violation or misalignment to address
   - Ask what the minimal viable change is

3. **Implement directly** - Once you have clarity:
   - Write Nix expressions in `/home/brandon/Forgejo/infrastructure/nix/`
   - Write Rego policies in `/home/brandon/Forgejo/infrastructure/policies/`
   - Update existing files to match the vision
   - No planning documents, no markdown - just code

4. **Validate as you go** - After each change:
   - Test Nix evaluation: `cd /home/brandon/Forgejo/infrastructure/nix && nix flake check`
   - Test Rego policies: `cd /home/brandon/Forgejo/infrastructure && nix run .#conftest`
   - Fix errors immediately, don't accumulate technical debt

## Focus Areas

- **Nix repo structure** - Hosts, services, SSOT organization
- **Policy enforcement** - Missing Rego rules, unenforced principles
- **Service declaration model** - Services declaring requirements vs host assignments
- **Port management** - Global port registry and conflict enforcement
- **Host structure** - One file per host, proper SSOT usage

## Anti-Patterns to Avoid

- Creating plan.md, roadmap.md, or any markdown documentation
- Writing "next steps" or "TODO" lists in markdown
- Documenting the approach before implementing
- Asking for confirmation before implementing (just implement once you understand)

## When to Ask Questions

- When the request is ambiguous or too broad
- When multiple valid implementations exist
- When you need to understand the target state, not the path
- When you're about to create markdown - STOP and ask instead

## When to Implement

- When you understand the target state clearly
- When you know which files to modify
- When you know what the code should look like
- When you have enough context to write Nix or Rego directly

Production contains only artifacts required to execute, validate, or enforce state. Make it match your vision through direct implementation, not documentation.
