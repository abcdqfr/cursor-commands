# compare-with-existing-solutions

Analyze whether a custom implementation or approach is reinventing an existing wheel, and determine if existing solutions should be adopted instead.

1. **Identify what you're building** - Clearly define the custom implementation, approach, or pattern being considered
2. **Research existing solutions** - Use `internet/I1-web-cite.md` to find established protocols, standards, frameworks, or tools that solve similar problems
3. **Compare architectures** - Analyze how your approach differs from existing solutions (protocol, interface, capabilities, layer)
4. **Evaluate functional overlap** - Determine if you're reinventing the wheel or solving a genuinely different problem
5. **Assess architectural differences** - Check if solutions operate at different layers or serve different purposes
6. **Classify relationship** - Determine the relationship:
   - **Reinventing** - Building something that already exists (should adopt)
   - **Complementary** - Different layer/purpose, works together (keep both)
   - **Alternative** - Different approach to same problem (choose one)
   - **Novel** - Genuinely new problem/solution (continue custom)
7. **Assess trade-offs** - Compare benefits and costs:
   - Custom: Domain-specific, full control, maintenance burden
   - Existing: Standardized, community support, potential mismatch
8. **Recommend action** - Should you adopt, integrate, continue custom, or use hybrid approach?

Focus on:
- Established protocols and standards (MCP, REST, GraphQL, OpenAPI, etc.)
- Mature frameworks and libraries
- Industry-standard patterns and architectures
- Community-adopted solutions
- Official specifications and standards
- **Architectural layers** (protocol vs instructions vs tools)

Consider both:
- **Functional overlap** (does it do the same thing?)
- **Architectural differences** (is it a different layer/purpose?)
- **Coexistence possibility** (can they work together?)

Format analysis as:
- **What you're building:** Clear description with purpose and scope
- **Existing solutions found:** List with URLs, authority levels, and what they do
- **Comparison matrix:** Side-by-side comparison of:
  - Purpose (what problem it solves)
  - Layer (protocol/tool/instruction/pattern)
  - Interface (how it's used)
  - Capabilities (what it can do)
- **Overlap assessment:**
  - Functional overlap: [yes/no, explain]
  - Architectural difference: [yes/no, explain]
  - Can they coexist: [yes/no, explain]
- **Relationship classification:** Reinventing / Complementary / Alternative / Novel
- **Recommendation:** Adopt existing / Integrate / Continue custom / Hybrid approach
- **Rationale:** Why this recommendation makes sense with trade-offs

**Example Analysis:**
```
## What We're Building
Custom command system: Structured markdown instructions for AI agents

## Existing Solutions
1. MCP (Model Context Protocol) - https://modelcontextprotocol.io
   - Purpose: Standardized protocol for AI to call tools
   - Authority: Official standard
   - Layer: Protocol + Tools
   - Overlap: Both enable AI-agent interaction
   - Differences: MCP provides tools, we provide instructions

## Comparison
| Aspect | Our Commands | MCP |
|--------|--------------|-----|
| Purpose | Guide AI behavior | Enable AI tool calls |
| Layer | Instructions/Prompts | Protocol + Tools |
| Interface | Markdown files | stdio protocol |
| Capabilities | Structured workflows | Executable functions |

## Relationship
**Classification:** Complementary

**Analysis:**
- Functional overlap: Partial (both enable AI-agent interaction)
- Architectural difference: Yes (different layers - instructions vs tools)
- Can they coexist: Yes (MCP provides tools, commands guide tool usage)

## Recommendation
Continue custom + Integrate MCP

**Rationale:**
- Commands provide structured guidance (HOW to use tools)
- MCP provides executable tools (WHAT tools are available)
- They solve different problems at different layers
- Together: MCP tools + command instructions = complete system
```

Provide honest, critical analysis that helps avoid unnecessary reinvention while recognizing when custom solutions are justified or complementary.
