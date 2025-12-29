# dynamic-command-system

Design and implement a Jinja2-based dynamic command system that allows commands to be customized via settings (tone, verbosity, detail level) using a 0.1-1.0 scale.

1. **Analyze current command structure** - Identify common patterns, repeated sections, and template-able components
2. **Design template architecture** - Plan how to convert static markdown to Jinja2 templates:
   - Base templates for common structures
   - Variable sections (tone, verbosity, detail)
   - Settings schema (0.1-1.0 scales)
3. **Define settings schema** - Create configuration system for:
   - **Tone** (0.1 = casual/friendly, 1.0 = formal/professional)
   - **Verbosity** (0.1 = minimal/brief, 1.0 = exhaustive/detailed)
   - **Detail level** (0.1 = high-level, 1.0 = step-by-step)
   - **Strictness** (0.1 = flexible/guidelines, 1.0 = must follow exactly)
   - **Citation style** (0.1 = minimal, 1.0 = comprehensive with URLs)
   - **Example density** (0.1 = no examples, 1.0 = extensive examples)
4. **Create template examples** - Convert 2-3 existing commands to Jinja2 templates as proof-of-concept
5. **Design rendering system** - Plan how templates + settings = final markdown:
   - Template engine (Jinja2)
   - Settings file format (YAML/JSON)
   - Rendering pipeline
   - Output validation
6. **Define template variables** - Map settings to template variables:
   - Tone affects: language formality, directness, warmth
   - Verbosity affects: step detail, explanations, background
   - Detail level affects: granularity of instructions
   - Strictness affects: requirement language (should vs must)
7. **Plan migration strategy** - How to convert existing commands:
   - Identify template-able patterns
   - Extract common components
   - Create base templates
   - Migrate incrementally
8. **Design settings inheritance** - Global defaults, category overrides, command-specific:
   - Global settings (default tone, verbosity)
   - Category settings (internet commands more verbose, git commands more strict)
   - Command-specific overrides
9. **Consider advanced features**:
   - Conditional sections (if verbosity > 0.7, include examples)
   - Scale-based transformations (tone 0.3 = "do this", tone 0.9 = "it is required that you perform the following")
   - Multi-language support (future)
   - A/B testing different settings

Focus on:
- **Template reusability** - DRY principle, shared components
- **Settings granularity** - Fine-grained control (0.1-1.0 scale)
- **Backward compatibility** - Existing commands still work
- **Maintainability** - Easier to update one template than 58 files
- **Flexibility** - Same command, different personalities
- **Consistency** - Settings ensure uniform tone/verbosity across arsenal

Consider both:
- **Template complexity** (too complex = hard to maintain)
- **Settings simplicity** (too many settings = overwhelming)

Format output as:
- **Template architecture** - How templates are structured
- **Settings schema** - All available settings with scales
- **Example templates** - 2-3 converted commands showing the pattern
- **Rendering pipeline** - How templates + settings = output
- **Migration plan** - Step-by-step conversion strategy
- **Proof of concept** - Working example with different settings applied

**Settings Scale Examples:**

**Tone (0.1-1.0):**
- 0.1: "Hey, let's do this thing"
- 0.5: "Please perform the following"
- 1.0: "It is required that you execute the following steps in the specified order"

**Verbosity (0.1-1.0):**
- 0.1: "Do X, then Y, then Z"
- 0.5: "Do X (because Y), then Y (which involves Z), then Z"
- 1.0: "Do X. Here's why: [detailed explanation]. Here's how: [step-by-step]. Here's what to watch for: [gotchas]"

**Detail Level (0.1-1.0):**
- 0.1: "Search the codebase"
- 0.5: "Search the codebase using semantic search, then grep for exact matches"
- 1.0: "1. Use codebase_search with query '[specific query]'. 2. Use grep with pattern '[pattern]' and flags '[flags]'. 3. Combine results..."

**Strictness (0.1-1.0):**
- 0.1: "Consider doing X"
- 0.5: "You should do X"
- 1.0: "You MUST do X. No exceptions."

Design a system that makes commands dynamic, customizable, and maintainable while preserving their core functionality.
