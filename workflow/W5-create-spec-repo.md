# Create Spec Repo

## Overview

Create a public-safe specification repository derived mechanically from the authoritative private infrastructure repository. This is a one-way carve-out process that preserves structure and rationale while removing all executable authority and sensitive material.

**Critical:** This command creates a non-executable documentation repository. It does NOT modify the infra repo, infer behavior, or enable deployment.

## Steps

1. **Understand the mission**
   - The private Forgejo infrastructure repository is the ONLY source of truth
   - All derivation is one-way: infra repo → spec repo → public GitHub mirror
   - The spec repo is non-executable (no deployable code, secrets, timers, credentials)
   - Never modify, refactor, or propose changes to the infra repo

2. **Create in-house spec repository**
   - Create new repository on same Forgejo instance (alongside infra repo)
   - Initialize with README explaining it's a projection/non-authoritative
   - Set up directory structure matching infra repo (structure only, not content)

3. **Derive content mechanically**
   - Copy directory structure and module boundaries
   - Extract interfaces and architectural patterns
   - Copy ADRs exactly (they are already documentation)
   - Extract configuration shapes (types/schemas) without values
   - Preserve architectural rationale from existing docs

4. **Sanitize sensitive material**
   - Remove or redact:
     - Secrets, credentials, private keys, tokens
     - Internal hostnames, IPs, network addresses
     - Timing/trigger details (cron schedules, systemd timers)
     - Code that directly mutates system state
   - Replace with:
     - Placeholders (e.g., `HOSTNAME_PLACEHOLDER`, `SECRET_PLACEHOLDER`)
     - Comments explaining what was removed and why
     - Explanatory stubs that preserve intent without enabling execution

5. **Maintain sync process**
   - Create deterministic carve-out script (repeatable, auditable)
   - Document sanitization policy (what is removed and why)
   - Ensure sync is explicit (no manual drift allowed)
   - Script should be idempotent (can regenerate spec repo at any time)

6. **Create public GitHub mirror**
   - Use `gh` CLI to create public repository
   - Push only spec repo contents (never infra repo)
   - Run `gitleaks` (or equivalent) as final gate before any public push
   - Verify no secrets detected

7. **Document the relationship**
   - README in spec repo must clearly state:
     - This repo is a projection
     - It is non-authoritative
     - It is not used for deployment
     - It flows from a private source of truth
     - How to regenerate from infra repo

## Focus on

- **One-way derivation**: Infra → Spec → Public (never reverse)
- **Non-executable output**: Spec repo cannot enable deployment
- **Mechanical extraction**: No inference, summarization, or reinterpretation
- **Preserve intent**: Keep architectural rationale, remove operational authority
- **Sanitization rigor**: All secrets, credentials, and executable paths removed
- **Sync repeatability**: Process must be deterministic and auditable

## Consider both

- **What to preserve**: Structure, interfaces, ADRs, architectural rationale, configuration shapes
- **What to remove**: Secrets, credentials, hostnames/IPs, timing details, executable code

## Constraints

- **Do NOT** infer undocumented behavior
- **Do NOT** summarize or reinterpret architecture beyond what exists
- **Do NOT** "improve" naming, layout, or design
- **Do NOT** feed public content back into infra
- **Do NOT** introduce executable paths
- **Do NOT** invent architecture
- **Do NOT** rewrite history or intent

## Deliverables

1. **In-house spec repo** (on Forgejo)
   - Directory structure matching infra
   - Sanitized content (no secrets, no executable authority)
   - README explaining non-authoritative nature

2. **Deterministic carve-out process**
   - Script or documented steps
   - Repeatable and auditable
   - Can regenerate spec repo at any time

3. **Sanitization policy**
   - Document what is removed and why
   - List of patterns to detect and redact
   - Placeholder conventions

4. **Public GitHub repository**
   - Created via `gh` CLI
   - Contains only spec repo contents
   - Validated by gitleaks (no secrets)

5. **Documentation**
   - README in spec repo explaining projection nature
   - Sync process documentation
   - Sanitization policy document

## Success Criteria

- ✅ Public repo contains no secrets (validated by gitleaks)
- ✅ Infra repo remains untouched
- ✅ Spec repo can be regenerated at any time
- ✅ Public documentation accurately reflects structure without enabling execution
- ✅ One-way flow maintained (infra → spec → public, never reverse)

## Failure Conditions (Do Not Trigger)

- ❌ Feeding public content back into infra
- ❌ Introducing executable paths
- ❌ Inventing architecture
- ❌ Rewriting history or intent
- ❌ Collapsing spec and infra into a single repo
- ❌ Modifying the infra repo

## Mental Model

> **"This repository explains the system. It does not run the system. It does not decide the system."**

The spec repo is a **projection** of the infra repo, not a copy. It preserves what can be safely shared (structure, rationale, patterns) while removing what cannot (secrets, authority, executable paths).
