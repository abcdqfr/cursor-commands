# security-review

Perform a comprehensive security review of the current code and provide specific remediation steps with code examples for each security issue identified.

1. **Authentication & Authorization** - Verify proper authentication mechanisms, check authorization controls and permission systems, review session management and token handling, and ensure secure password policies and storage
2. **Input Validation & Sanitization** - Identify SQL injection vulnerabilities, check for XSS and CSRF attack vectors, validate all user inputs and API parameters, and review file upload and processing security
3. **Data Protection** - Ensure sensitive data encryption at rest and in transit, check for data exposure in logs and error messages, review API responses for information leakage, and verify proper secrets management
4. **Infrastructure Security** - Review dependency security and known vulnerabilities, check HTTPS configuration and certificate validation, analyze CORS policies and security headers, and review environment variable and configuration security

Focus on:
- Authentication and authorization mechanisms
- Input validation and sanitization
- Data protection and encryption
- Infrastructure security configuration
- Specific remediation steps with code examples

Consider both:
- Current code security posture
- Remediation strategies with code examples

Format the output as:
- Security findings with severity levels
- Specific remediation steps for each finding
- Code examples for fixes
- Security checklist completion status

Perform comprehensive security review with actionable remediation steps and code examples.
