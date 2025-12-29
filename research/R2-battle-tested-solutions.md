# battle-tested-solutions

Identify custom implementations in the codebase that could potentially be replaced with mature, battle-tested solutions.

1. **Identify the custom implementation** - Scan codebase for areas where custom code is solving problems that typically have established solutions. What is being built from scratch?
2. **Categorize custom code** - Classify custom implementations by type (infrastructure, HTTP services, validation, state management, monitoring, authentication, data processing, etc.)
3. **Assess the maturity gap** - Evaluate the risks, complexity, and maintenance burden each custom implementation introduces. What risks or maintenance burden does the custom code introduce?
4. **Document current approach** - Record what the custom code does, why it might exist, and what domain-specific needs it addresses. Evaluate trade-offs - why might the custom solution exist (domain-specific needs, constraints, historical reasons)?
5. **Recommend alternatives** - What established tools, libraries, or frameworks could replace it? Consider both direct replacements (drop-in alternatives) and architectural patterns (how established systems solve similar problems).
6. **Prioritize by impact** - Rank custom implementations by potential value if replaced (maintenance reduction, reliability improvement, community support). Which replacements would provide the most value?

Focus on:
- Custom infrastructure orchestration that could use standard tools
- Custom HTTP/web services that could use established frameworks
- Custom validation/linting that could use standard policy engines
- Custom state management that could use existing reconciliation patterns
- Custom monitoring/observability that could use standard exporters or APIs
- Custom authentication/authorization implementations
- Custom data processing pipelines
- Any "reinventing the wheel" patterns where mature solutions exist

Consider both:
- Why the custom solution might exist (domain-specific needs, constraints, historical reasons)
- What problems the custom code solves that standard tools might not address
- Direct replacements (drop-in alternatives)
- Architectural patterns (how established systems solve similar problems)

Format findings as:
- List of custom implementations with file locations
- Assessment of complexity and maintenance burden (maturity gap analysis)
- Categorization by type
- Documentation of current approach and rationale
- Recommended alternatives with clear migration paths
- Prioritized list of candidates for replacement research
- Actionable recommendations with trade-off evaluation

This offline analysis identifies candidates. Use `internet/I4-battle-tested-solutions.md` to research online alternatives for the identified candidates.
