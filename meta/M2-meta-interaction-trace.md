# meta-interaction-trace

Record intimate interaction data for prompt engineering debugging and future reproduction.

When requested to document meta-information about an interaction, create a comprehensive trace that captures:

1. **Verbatim user statements** - Record every user input exactly as stated, including typos and formatting
2. **Tool call inventory** - Document every tool call made, organized by phase (discovery, execution, documentation)
3. **Decision points & rationale** - For each decision made, document:
   - What decision was made
   - Why it was made (rationale)
   - What alternatives were considered
   - What resulted from the decision
4. **Context gathered** - Document:
   - All files read (with paths)
   - All directories explored
   - All patterns discovered
   - All searches performed (grep patterns, glob patterns)
5. **References polled** - List every reference source consulted:
   - Documentation files
   - Configuration files
   - Code files
   - Workflow files
   - Any external resources
6. **User input sequence** - For each user input:
   - The verbatim statement
   - Context provided (attached files, terminal selections, etc.)
   - Agent actions taken in response
   - Decision rationale for those actions
   - Output produced
7. **Key insights for prompt engineering** - Document:
   - What worked well
   - What could be improved
   - User communication patterns observed
   - System behavior patterns observed
8. **Reproduction checklist** - Provide steps to reproduce the interaction:
   - Initial state required
   - User input sequence
   - Required context/files
   - Expected outputs

Focus on:
- Complete traceability of every action taken
- Verbatim preservation of user statements
- Decision rationale documentation
- Tool call traceability
- Context gathering documentation
- Pattern discovery and application

Consider both:
- Explicit actions (tool calls, file reads, writes)
- Implicit decisions (why certain approaches were chosen)

Format the meta-documentation as:
- Structured markdown file in `docs/troubleshooting/META-interaction-trace-[topic].md`
- Chronological sequence of user inputs and agent responses
- Complete tool call inventory organized by phase
- Decision points with full rationale
- Reproduction checklist for future debugging

The goal is to create a complete record that enables:
- Prompt engineering analysis
- Interaction reproduction
- Debugging of agent behavior
- Understanding of decision-making patterns
- Improvement of future interactions
