# Create Desired State Manifest

Create a desired state manifest that captures hierarchical facts, policy invariants, and advisory information for declarative systems, infrastructure, or configuration management.

## Overview

Desired state manifests document the intended state of a system with multiple fact sources, policy constraints, and optional guidance. This pattern works for:
- Infrastructure as Code (IaC) systems
- Configuration management
- Policy-driven development
- GitOps workflows
- Declarative deployment systems
- Any system requiring hierarchical fact tracking

## Steps

1. **Identify fact hierarchy** - Determine the hierarchy of fact sources:
   - **FE (Editor Facts)**: Advisory/editor-only facts (lowest authority)
   - **FL (Local Agent Facts)**: Derived/authoritative pre-commit facts (medium authority)
   - **FC (CI/System Facts)**: Full visibility/authoritative facts (highest authority)
   - Principle: `FC ⊇ FL ⊇ FE` (higher levels contain or supersede lower levels)

2. **Define metadata section** - Include:
   - Context identifier (branch, environment, system name)
   - Policy version or schema version
   - Last updated timestamp
   - Any other relevant metadata

3. **Structure fact sections** - Organize facts by hierarchy:
   - **FE section**: Editor/advisory facts (optional, can be empty)
   - **FL section**: Local agent/derived facts (pre-commit validation)
   - **FC section**: CI/system facts (full system visibility)

4. **Define policy invariants** - Document non-negotiable constraints:
   - Fact hierarchy relationships
   - Commit boundaries (non-bypassable checks)
   - Event propagation rules
   - Authority boundaries (e.g., LLM advisory only)

5. **Add optional advice section** - Include:
   - LLM-generated guidance
   - Warnings or recommendations
   - Context-specific notes
   - Human-readable explanations

## Manifest Structure Template

```yaml
# ------------------------------
# [System] Desired State Manifest
# .[system].intent
# ------------------------------

# Metadata
CONTEXT=[branch/environment/system]
POLICY_VERSION=[version]
LAST_UPDATED=[timestamp]

# ------------------------------
# Editor Facts (FE) - advisory only
# ------------------------------
FE:
  [advisory_facts_here]

# ------------------------------
# Local Agent Facts (FL) - derived / authoritative pre-commit
# ------------------------------
FL:
  [local_agent_facts_here]

# ------------------------------
# CI/System Facts (FC) - full visibility
# ------------------------------
FC:
  [ci_system_facts_here]

# ------------------------------
# Policy Invariants (Rego-ready)
# ------------------------------
INV:
  fact_hierarchy: "FC ⊇ FL ⊇ FE"
  [other_invariants_here]

# ------------------------------
# Optional Notes / LLM advice
# ------------------------------
ADVICE:
  - "[guidance_item_1]"
  - "[guidance_item_2]"
```

## Focus Areas

- **Hierarchical authority**: Clear fact source hierarchy with defined relationships
- **Policy enforcement**: Invariants that cannot be bypassed
- **Advisory separation**: Distinguish between authoritative facts and advisory guidance
- **Context awareness**: Include enough metadata to understand the manifest's scope
- **Tool agnosticism**: Structure works across different tools (Nix, Terraform, Kubernetes, etc.)

## Considerations

- **Different contexts**: Adapt fact sections to your system (services, resources, configurations, etc.)
- **Variations**: Some systems may have more or fewer fact levels
- **Format flexibility**: Use YAML, TOML, JSON, or plain text as appropriate
- **Integration**: Consider how manifests integrate with validation tools (Rego, OPA, custom validators)

## Format Output As

- Complete manifest file with all required sections
- Clear hierarchy of fact sources
- Policy invariants that enforce constraints
- Optional advisory section for human guidance
- Comments explaining each section's purpose

## Examples of Application

- **Infrastructure**: Cluster desired state, service placement, resource allocation
- **Configuration**: System configuration manifests, deployment targets
- **Policy**: Policy-driven development, compliance tracking
- **GitOps**: Repository state manifests, deployment intents
- **Development**: Feature branch state, dependency tracking
