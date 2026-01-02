# vscode-dev-setup

Set up comprehensive VS Code development environment with debugging, language servers, linters, and all power tools needed for professional development.

## Purpose

Configure VS Code/Cursor with:
- **Debugging**: Breakpoints, step-through debugging, watch expressions
- **Language Servers**: TypeScript, ESLint, Prettier, and other LSPs
- **Linters**: Real-time error detection and code quality checks
- **IntelliSense**: Autocomplete, type hints, go-to-definition
- **Task Runners**: Integrated terminal tasks and npm scripts
- **Extensions**: Essential dev tools and productivity enhancers

## Setup Requirements

1. **Create `.vscode/launch.json`** - Debug configurations for browser and Node.js
2. **Create `.vscode/tasks.json`** - Build and test tasks
3. **Create `.vscode/settings.json`** - Workspace-specific settings
4. **Create `.vscode/extensions.json`** - Recommended extensions
5. **Install language servers** - ESLint, TypeScript, etc.
6. **Configure linters** - ESLint, Prettier configs

## Project-Specific Setup

### JavaScript/TypeScript Projects
- ESLint with proper parser and rules
- Prettier for code formatting
- TypeScript language server (even for JS projects)
- Debugger for Chrome/Edge
- Source map support

### Vite Projects
- Chrome debugger with source maps
- Vite dev server integration
- Hot module replacement debugging

### Node.js Projects
- Node.js debugger
- Nodemon integration
- Environment variable support

## Absolute Paths

When creating configurations, use absolute paths:
- Workspace root: `/home/brandon/ChatGPT/chatgpt-export-importer`
- Node modules: `/home/brandon/ChatGPT/chatgpt-export-importer/node_modules`
- Source files: `/home/brandon/ChatGPT/chatgpt-export-importer/src`
- Build output: `/home/brandon/ChatGPT/chatgpt-export-importer/dist`

## Implementation Steps

1. **Analyze project structure** - Identify framework, build tool, test framework
2. **Create VS Code configs** - Launch, tasks, settings, extensions
3. **Install dependencies** - ESLint, Prettier, TypeScript (if needed)
4. **Configure language servers** - Ensure LSPs are working
5. **Test debugging** - Verify breakpoints and step-through work
6. **Test IntelliSense** - Verify autocomplete and type hints
7. **Test linting** - Verify real-time error detection

## Key Features to Enable

- **Breakpoints**: Set and hit breakpoints in source code
- **Watch Expressions**: Monitor variable values during debugging
- **Call Stack**: Navigate through function calls
- **Debug Console**: Evaluate expressions in debug context
- **IntelliSense**: Autocomplete, hover info, signature help
- **Go to Definition**: Jump to source code
- **Find References**: Find all usages of symbols
- **Code Actions**: Quick fixes, refactorings
- **Format on Save**: Automatic code formatting
- **Lint on Save**: Real-time error checking

## Common Configurations

### Chrome Debugger (for Vite/Webpack)
```json
{
  "type": "chrome",
  "request": "launch",
  "name": "Launch Chrome",
  "url": "http://localhost:5173",
  "webRoot": "${workspaceFolder}",
  "sourceMaps": true
}
```

### Node.js Debugger
```json
{
  "type": "node",
  "request": "launch",
  "name": "Debug Node",
  "program": "${workspaceFolder}/src/index.js",
  "sourceMaps": true
}
```

## Verification

After setup, verify:
- ✅ Breakpoints work and pause execution
- ✅ Variables show in debug panel
- ✅ IntelliSense provides autocomplete
- ✅ Linter shows errors in Problems panel
- ✅ Format on save works
- ✅ Go to definition works
- ✅ Language server is active (check status bar)

## Best Practices

- Use workspace settings, not user settings
- Enable source maps for debugging
- Configure ESLint with proper parser for project type
- Set up format on save for consistency
- Use recommended extensions for team consistency
- Configure paths correctly for monorepos
- Enable TypeScript checking even for JS projects (jsconfig.json)

## Troubleshooting

- **Language server not working**: Check output panel for errors
- **Breakpoints not hitting**: Verify source maps are enabled
- **IntelliSense not working**: Check jsconfig.json/tsconfig.json exists
- **Linter not running**: Verify ESLint is installed and configured
- **Debugger can't connect**: Check port and URL configuration

Set up comprehensive VS Code development environment with all power tools for professional development.

