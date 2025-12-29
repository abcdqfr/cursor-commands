#!/usr/bin/env python3
"""
Gather command data for Jinja2 template rendering.
Outputs structured YAML data about all commands.
"""

import os
import yaml
from pathlib import Path
from typing import Dict, List, Any

REPO_ROOT = Path(__file__).parent.parent
COMMANDS_DIR = REPO_ROOT

def is_pipeable(cmd_path: Path) -> bool:
    """Check if command is pipeable (has -pp suffix)."""
    return cmd_path.stem.endswith("-pp")

def get_command_info(cmd_path: Path) -> Dict[str, Any]:
    """Extract information about a command file."""
    category = cmd_path.parent.name
    name = cmd_path.stem
    pipeable = is_pipeable(cmd_path)

    # Read first few lines to get title/description
    title = name
    description = ""
    try:
        with open(cmd_path, 'r') as f:
            lines = f.readlines()[:10]
            for i, line in enumerate(lines):
                if line.startswith('# ') and i == 0:
                    title = line[2:].strip()
                elif line.strip() and not line.startswith('#') and i > 0:
                    description = line.strip()
                    break
    except Exception:
        pass

    return {
        "name": name,
        "category": category,
        "title": title,
        "description": description,
        "pipeable": pipeable,
        "path": str(cmd_path.relative_to(REPO_ROOT))
    }

def gather_commands() -> Dict[str, Any]:
    """Gather all command data."""
    commands_by_category: Dict[str, List[Dict[str, Any]]] = {}
    all_commands: List[Dict[str, Any]] = []

    # Find all command directories
    for category_dir in COMMANDS_DIR.iterdir():
        if not category_dir.is_dir():
            continue
        if category_dir.name.startswith('.') or category_dir.name in ['scripts', 'templates', 'settings']:
            continue

        category = category_dir.name
        commands_by_category[category] = []

        # Find all .md files in category
        for cmd_file in category_dir.glob("*.md"):
            if cmd_file.name == "README.md":
                continue

            cmd_info = get_command_info(cmd_file)
            commands_by_category[category].append(cmd_info)
            all_commands.append(cmd_info)

    # Sort commands within each category
    for category in commands_by_category:
        commands_by_category[category].sort(key=lambda x: x["name"])

    # Category display names
    category_display = {
        "architect": "A - Architect",
        "behavior": "B - Behavior",
        "code-quality": "C - Code-Quality",
        "documentation": "D - Documentation",
        "eval": "E - Eval",
        "git": "G - Git",
        "internet": "I - Internet",
        "meta": "M - Meta",
        "project-management": "P - Project-Management",
        "research": "R - Research",
        "security": "S - Security",
        "transcript": "T - Transcript",
        "workflow": "W - Workflow"
    }

    return {
        "categories": {
            cat: {
                "display_name": category_display.get(cat, cat.title()),
                "commands": cmds
            }
            for cat, cmds in sorted(commands_by_category.items())
        }
    }

def main():
    """Main entry point."""
    import sys

    data = gather_commands()

    if len(sys.argv) > 1 and sys.argv[1] == "--json":
        import json
        print(json.dumps(data, indent=2))
    else:
        print(yaml.dump(data, default_flow_style=False, sort_keys=False))

if __name__ == "__main__":
    main()
