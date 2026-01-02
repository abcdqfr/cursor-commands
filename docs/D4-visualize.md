# visualize

Analyze the provided code, architecture, or concept and generate a clear, well-structured Mermaid diagram that visualizes relationships, flow, or structure.

1. **Analyze the input** - Understand what the user wants to visualize (code flow, architecture, data relationships, state machines, sequences, data lineage, etc.)
2. **Choose the appropriate diagram type**:
   - `flowchart` - For process flows, decision trees, algorithms
   - `sequenceDiagram` - For API calls, message passing, request/response flows
   - `classDiagram` - For class structures, inheritance, interfaces
   - `erDiagram` - For database schemas, entity relationships
   - `stateDiagram-v2` - For state machines, lifecycle flows
   - `graph TD/LR` - For dependency graphs, module relationships
   - `gitgraph` - For git branching strategies
   - `journey` - For user journeys
   - `gantt` - For timelines and schedules
3. **Generate the diagram** with these qualities:
   - Clear, descriptive node labels
   - Logical grouping with subgraphs where appropriate
   - Consistent styling and direction
   - Meaningful relationship labels on edges
   - Not overly complex - split into multiple diagrams if needed
4. **Output format**: Always wrap the diagram in a mermaid code block:
   ```mermaid
   [diagram code here]
   ```

Focus on:
- Appropriate diagram type selection for the visualization need
- Clear, descriptive node labels (use descriptive IDs: `userService` not `a1`)
- Logical grouping with subgraphs
- Meaningful relationship labels on edges
- Readability (max ~15-20 nodes per diagram)
- Appropriate arrow styles:
  - `-->` solid arrow (main flow)
  - `-.->` dotted arrow (optional/async)
  - `==>` thick arrow (important path)
  - `o-->` circle end (aggregation)
  - `*-->` diamond end (composition)

Consider both:
- Direct visualization needs (what the user explicitly wants to see)
- Related visualizations that might provide additional context

Format the output as:
- Mermaid diagram wrapped in code block
- Explanation of what the diagram shows
- Offer to refine or expand specific sections
- Suggest alternative diagram types if applicable

Visualize with clarity, structure, and appropriate diagrammatic representation.
