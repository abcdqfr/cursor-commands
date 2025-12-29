# code-review

Perform a thorough code review that verifies functionality, maintainability, and security before approving a change. Focus on architecture, readability, performance implications, and provide actionable suggestions for improvement.

1. **Understand the change** - Read the PR description and related issues for context, identify the scope of files and features impacted, and note any assumptions or questions to clarify with the author
2. **Validate functionality** - Confirm the code delivers the intended behavior, exercise edge cases or guard conditions mentally or by running locally, and check error handling paths and logging for clarity
3. **Assess quality** - Ensure functions are focused, names are descriptive, and code is readable. Watch for duplication, dead code, or missing tests. Verify documentation and comments reflect the latest changes
4. **Review security and risk** - Look for injection points, insecure defaults, or missing validation. Confirm secrets or credentials are not exposed. Evaluate performance or scalability impacts of the change

Focus on:
- Functionality verification (intended behavior, edge cases, error handling)
- Code quality (readability, focus, naming, duplication, dead code, tests)
- Security and risk (injection points, validation, secrets, performance)
- Architecture and design decisions
- Maintainability and documentation

Consider both:
- What the code does (functionality)
- How the code does it (quality, security, maintainability)

Format the review as:
- Functionality assessment with edge case analysis
- Code quality findings with specific examples
- Security and risk evaluation
- Architecture and design considerations
- Actionable suggestions for improvement
- Constructive feedback with concrete examples

Provide constructive feedback with concrete examples and actionable guidance for the author.
