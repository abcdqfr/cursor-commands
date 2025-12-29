# battle-tested-solutions

Identify custom implementations in the codebase that could potentially be replaced with mature, battle-tested solutions.

1. **Scan codebase for custom implementations** - Identify areas where custom code is solving problems that typically have established solutions
2. **Categorize custom code** - Classify custom implementations by type (infrastructure, HTTP services, validation, state management, etc.)
3. **Assess complexity and maintenance burden** - Evaluate the risks, complexity, and maintenance burden each custom implementation introduces
4. **Document current approach** - Record what the custom code does, why it might exist, and what domain-specific needs it addresses
5. **Prioritize candidates** - Rank custom implementations by potential value if replaced (maintenance reduction, reliability improvement)

Focus on:

- Custom infrastructure orchestration code
- Custom HTTP/web service implementations
- Custom validation or linting logic
- Custom state management or reconciliation patterns
- Custom monitoring/observability code
- Custom authentication/authorization implementations
- Custom data processing pipelines
- Any "reinventing the wheel" patterns

Consider both:

- Why the custom solution might exist (domain-specific needs, constraints, historical reasons)
- What problems the custom code solves that standard tools might not address

Format findings as:

- List of custom implementations with file locations
- Assessment of complexity and maintenance burden
- Categorization by type
- Documentation of current approach and rationale
- Prioritized list of candidates for replacement research

This offline analysis identifies candidates. Use `web/battle-tested-solutions.md` to research online alternatives for the identified candidates.
