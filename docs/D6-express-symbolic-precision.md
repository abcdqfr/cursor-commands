# Express Symbolic Precision

Force formal symbolic notation (set theory, lattice relations, formal logic) before natural language when expressing system design, policy rules, workflows, or invariants.

## Overview

This pattern enforces **symbol-first, text-second** expression to ensure mathematical rigor and eliminate ambiguity. Use formal mathematical notation to encode relationships, then provide human-readable explanations.

Works for:
- System architecture documentation
- Policy rule specification
- Workflow definitions
- Invariant expression
- Data flow documentation
- Authority hierarchy design

## Steps

1. **Identify relationships** - Determine what needs to be expressed:
   - Hierarchies (authority, containment, data flow)
   - Constraints (invariants, boundaries, rules)
   - Transformations (workflows, state changes)
   - Dependencies (requirements, ordering)

2. **Encode in symbols** - Express relationships using formal notation:
   - Set theory: ⊇ ⊆ ∈ ∉ ∪ ∩
   - Logic: ∀ ∃ = ⇒ ∧ ∨ ¬
   - Relations: → ← ↔
   - Hierarchy: ⊂ ⊃ ≤ ≥

3. **Define invariants** - Write constraints as equations/inequalities:
   - Fact hierarchy: `FC ⊇ FL ⊇ FE`
   - Commit boundary: `∀ C_i, policy(S(C_i)) = allow`
   - State preservation: `S(B_s, t) ⊆ S(B_m, t_merge)`

4. **Map symbols to meaning** - Provide human-readable explanations:
   - For each symbol, explain what it represents
   - For each relationship, explain the constraint
   - For each invariant, explain the guarantee

5. **Enforce symbol-first** - Never skip symbols for convenience:
   - If a relationship exists, it must be encoded symbolically
   - Text explanations come after symbols
   - Ambiguous phrasing is replaced with formal notation

## Focus Areas

- **Mathematical rigor**: Use formal notation to eliminate ambiguity
- **Symbol-first**: Always encode relationships symbolically before explaining
- **Invariant expression**: Write constraints as equations/inequalities
- **Authority encoding**: Use set theory to express hierarchies
- **Determinism**: Use logic to express deterministic relationships

## Considerations

- **Different contexts**: Adapt symbols to domain (infrastructure, policy, workflow)
- **Variations**: Some relationships may use different notation (lattices, graphs, etc.)
- **Complexity**: Start simple, add symbols as needed
- **Clarity**: Balance formality with readability
- **Tool agnosticism**: Symbols work across tools (Rego, Nix, Terraform, etc.)

## Format Output As

1. **Symbolic representation** (required first)
   - Core relationships encoded in formal notation
   - Invariants as equations/inequalities

2. **Symbol mapping** (required second)
   - For each symbol, explain what it represents
   - For each relationship, explain the constraint

3. **Human-readable explanation** (optional third)
   - Natural language summary
   - Context and examples

