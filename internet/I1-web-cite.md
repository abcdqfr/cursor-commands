# web-cite

Conduct efficient online technical research using web search, internet sources, and latest information to find authoritative answers from external sources. Find and cite web sources with strict citation requirements to help with technical decisions.

1. **Define research objective** - Clearly identify what information, solution, or understanding is needed from online sources, web documentation, or external knowledge. Determine what authoritative information or instructions are required for the technical decision.
2. **Structure web search queries** - Create comprehensive search queries that include all relevant context and technical requirements for effective web searching. Design queries that will find authoritative sources (documentation, official guides, best practices).
3. **EXECUTE web search** - **REQUIRED:** Use the `web_search` tool to actually search the web. You cannot skip this step. Find official documentation, examples, code snippets, and technical details from reliable web sources.
4. **Show your work** - Document what you searched for, what you found, and what sources you evaluated. Assess credibility, recency, and relevance of online information, prioritizing official documentation over community sources.
5. **Extract relevant information** - Gather specific instructions, code examples, or technical details from authoritative sources. Evaluate gathered information and synthesize findings into actionable insights from web sources.
6. **Cite with URLs** - **REQUIRED:** Every piece of information must include:
   - Source URL (the actual web page)
   - Source name (documentation site, article title, etc.)
   - What specific information came from that source
   - Authority level indicators (official vs community)
7. **Document findings with citations** - Record research results, web sources, URLs, and recommendations for future reference with proper attribution. Synthesize insights with clear recommendations and actionable next steps.
8. **Explain empty hands** - If you did NOT perform a web search, you MUST explicitly state:
   - Why you didn't search (e.g., "Information already available in codebase")
   - What alternative source you used instead
   - Why that alternative is sufficient

Focus on:
- **Actually using web_search tool** - No lazy behavior, no skipping searches
- **Source quality and authority** - Prioritize official documentation over community sources
- **Complete citations with URLs** - Every claim must have a source URL
- **Multi-source verification** - Cross-reference when possible
- Official documentation and authoritative web sources
- Latest tools, libraries, and frameworks from online sources
- Current best practices and industry standards from the web
- Community solutions and examples from online repositories
- Recent updates and version information from web sources
- Web-based code examples and tutorials
- Relevant technical details and instructions
- Code examples and implementation patterns when applicable
- **Verification of information accuracy** - Check dates, maintenance status, conflicts

## Source Quality Requirements

**MANDATORY: Always provide URLs**
- Every source MUST include the full URL
- Format: `[Source Name](URL)` or `Source Name: URL`
- Never present information without citing where it came from

**Priority Order (Most Authoritative First):**
1. **Official Documentation** - `*.org`, `*.com` official project sites (e.g., `nixos.org`, `openwrt.org`)
2. **Official GitHub Repositories** - `github.com/{project}/{repo}` with official status
3. **Project Wikis** - Official project wikis and documentation sites
4. **Established Community Resources** - Well-known community guides from recognized experts
5. **Stack Overflow / Forums** - Only when official sources unavailable, clearly marked as community advice

**Source Evaluation Criteria:**
- ✅ Official project documentation (highest authority)
- ✅ Recent and maintained (check dates, last updated)
- ✅ Specific to the exact problem (not generic)
- ✅ Includes code examples or step-by-step instructions
- ⚠️ Community guides (cite as such, verify against official docs)
- ❌ Avoid: Personal blogs without credentials, outdated tutorials, unverified claims

Consider both:
- Direct answers (what exactly solves the problem from online sources?)
- Related patterns (what similar problems have been solved online and how?)

Format research queries as:
- Clear, comprehensive paragraphs that command a researcher to find specific information online
- Include all relevant context and technical requirements
- Request code snippets or technical details when relevant
- Structure as if instructing a human researcher to search the web

Format research findings as:
- **Search queries used** - What you actually searched for
- **Sources found** - Complete list with URLs, authority level, and verification status
- **Information extracted** - What you learned from each source with specific details
- **Synthesized insights** - Clear recommendations with actionable next steps
- **Clear citations with URLs** - Every piece of information must cite its source URL
- **Authority level** - Official Documentation / Official Repo / Community Guide / Forum Post
- **Verification status** - Whether information is confirmed by multiple sources
- Code examples or technical details from online sources with source attribution
- **Conflicts noted** - When sources disagree, present all and note the conflict
- **If no search performed** - Explicit explanation of why and what alternative was used

**Critical Rules:**
1. **Never present information without URLs**
2. **Always state authority level** (official vs community)
3. **When multiple sources conflict, present all and note the conflict**
4. **If information is incomplete, state what's missing**
5. **Prioritize recent sources** (check dates when available)
6. **Distinguish between "this is how to do it" (official) vs "this might work" (community)**

Conduct online research that efficiently finds authoritative answers from the web and provides actionable solutions with proper source attribution and URL citations.
