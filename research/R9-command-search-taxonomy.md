# command-search-taxonomy

Map user search terms and intent to actual command names, identifying gaps between what people type and what commands exist. Understand why filename tags don't lead users to commands matching their search terms.

1. **Catalog user search terms** - Identify common words and phrases people type when looking for commands (e.g., "debug", "fix error", "test", "documentation", "security check").
2. **Map terms to commands** - For each search term, identify which commands match (exact match, partial match, semantic match, no match).
3. **Identify naming gaps** - Find search terms that don't map well to existing command names. Understand why users can't find commands even when they exist.
4. **Analyze semantic distance** - Measure how far user search terms are from actual command names. Identify patterns in mismatches (e.g., users type verbs, commands use nouns).
5. **Document intent patterns** - Categorize user intent (debug, test, document, review, etc.) and see which commands serve each intent.
6. **Propose improvements** - Suggest better command names, aliases, or search mechanisms that bridge the gap between user language and command names.
7. **Create taxonomy map** - Build a comprehensive mapping from user search terms → user intent → command names → command categories.

Focus on:
- Common user search terms and phrases
- Exact vs semantic matching patterns
- Naming convention mismatches
- Intent-to-command mapping
- Discoverability gaps
- Search term patterns (verbs, nouns, actions, objects)
- Category vs specific command searches

Consider both:
- What users type (actual search terms)
- What commands are named (actual filenames)

Format the taxonomy as:
- **User Search Terms Catalog** - Common terms people type
- **Term-to-Command Mapping** - Which commands match each term
- **Gap Analysis** - Terms with no good matches
- **Semantic Distance Analysis** - How far terms are from command names
- **Intent Categories** - User intent patterns and their commands
- **Improvement Recommendations** - Better names, aliases, search mechanisms
- **Taxonomy Map** - Complete mapping: search term → intent → command → category

Build a taxonomy that bridges the gap between user language and command names to improve discoverability.
