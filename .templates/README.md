# Dynamic Command Templates

**Status:** 🧪 **EXPERIMENTAL** - Feature branch only

This directory contains Jinja2 templates for dynamic command generation.

## Structure

- `*.j2` - Jinja2 template files (one per command)
- Templates use settings from `.settings/default.yaml`
- Rendered output goes to command directories (e.g., `internet/I1-web-search.md`)

## Usage

**Manual Rendering (for now):**
```bash
# Install dependencies
pip install jinja2 pyyaml

# Render a command
python scripts/render_command.py I1-web-search

# Render all commands
python scripts/render_command.py --all
```

**Settings Location:**
- `.settings/default.yaml` - Global and category settings
- `.settings/user.yaml` - User overrides (gitignored)
- `.settings/project.yaml` - Project-specific overrides (optional)

## Settings Cascade

1. Global defaults (`.settings/default.yaml`)
2. Category overrides (`.settings/default.yaml` → `categories.*`)
3. Command-specific (`.settings/default.yaml` → `commands.*`)
4. User overrides (`.settings/user.yaml`)
5. Project overrides (`.settings/project.yaml`)

Highest priority wins.
