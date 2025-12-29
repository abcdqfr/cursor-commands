# Command Settings

**Status:** 🧪 **EXPERIMENTAL** - Feature branch only

Settings files for dynamic command rendering.

## Files

- `default.yaml` - Default settings (committed)
- `user.yaml` - User-specific overrides (gitignored, create locally)
- `project.yaml` - Project-specific overrides (optional, committed)

## Settings Scale (0.1 - 1.0)

- **tone** - 0.1 = casual, 1.0 = formal
- **verbosity** - 0.1 = minimal, 1.0 = exhaustive
- **detail_level** - 0.1 = high-level, 1.0 = step-by-step
- **strictness** - 0.1 = flexible, 1.0 = must follow
- **citation_style** - 0.1 = minimal, 1.0 = comprehensive
- **example_density** - 0.1 = none, 1.0 = extensive

## Creating User Overrides

Copy `default.yaml` to `user.yaml` and modify:

```yaml
# .settings/user.yaml
global:
  tone: 0.4  # I prefer casual tone
  verbosity: 0.5  # Less verbose

commands:
  I1-web-search:
    verbosity: 0.8  # But web-search should be detailed
```
