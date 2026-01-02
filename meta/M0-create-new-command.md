# create-new-command

Create a new reusable, generic command following established patterns. Commands MUST be general-purpose and reusable across contexts, NOT tool-specific or single-use.

## Critical Principles

1. **Genericity First**: Commands must be reusable across different contexts, tools, and scenarios
2. **No Tool Lock-in**: Avoid creating commands specific to a single tool (e.g., "regal-masterclass" ❌). Instead, create generic patterns (e.g., "masterclass" ✅)
3. **Pattern-Based**: Commands should solve classes of problems, not single instances
4. **Reusability**: A command should work for multiple tools, technologies, or concepts

## Command Creation Process

1. **Identify the pattern** - What class of problem does this solve? What makes it reusable?
2. **Check for existing commands** - Search `~/.cursor/commands` for similar patterns. Reuse or extend existing commands when possible
3. **Design for genericity** - Ask: "Can this work for other tools/concepts?" If no, make it more generic
4. **Follow established structure** - Use existing commands as templates (see examples below)
5. **Use absolute paths** - Reference `~/.cursor/commands/` with absolute paths when creating new commands

## Examples of Good vs Bad Commands

### ❌ Bad (Tool-Specific)
- `regal-masterclass.md` - Only works for Regal
- `docker-setup.md` - Only works for Docker
- `nixos-build.md` - Only works for NixOS

### ✅ Good (Generic)
- `masterclass.md` - Works for any tool/concept (Regal, OPA, Terraform, etc.)
- `container-setup.md` - Works for Docker, Podman, containerd, etc.
- `build-system.md` - Works for NixOS, Bazel, Make, etc.

## Command Structure Template

```markdown
# command-name

[Brief description of the generic pattern this solves]

1. **Step 1** - Generic action that applies to the pattern
2. **Step 2** - Another generic action
...

Focus on:
- Generic principles (not tool-specific)
- Reusable patterns
- Classes of problems

Consider both:
- Different contexts where this applies
- Variations of the pattern

Format output as:
- Generic structure that works across contexts
- Adaptable examples
- Reusable patterns
```

## When Creating a New Command

1. **Search first**: Look in `~/.cursor/commands/` for existing commands that solve similar patterns
2. **Generalize**: If you find a tool-specific command, create a generic version instead
3. **Reuse**: Extend existing generic commands rather than creating duplicates
4. **Document**: Explain how the command is reusable and what contexts it applies to

## Bonus: Command Discovery

When creating a command, search `~/.cursor/commands/` for existing commands that:
- Solve similar patterns (even if for different tools)
- Can be extended or generalized
- Provide templates for structure

If a similar pattern exists, extend it. If not, create using ABSOLUTE paths: `~/.cursor/commands/category/command-name.md`

---
