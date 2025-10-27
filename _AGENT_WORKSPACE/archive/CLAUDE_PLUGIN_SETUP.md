# Claude Code Plugin Installation Guide

Complete guide for installing, configuring, and managing Claude Code plugins in your workspace.

## Table of Contents

- [Understanding the Plugin System](#understanding-the-plugin-system)
- [Directory Structure](#directory-structure)
- [Installing Your Local Marketplace](#installing-your-local-marketplace)
- [Installing Plugins](#installing-plugins)
- [Creating New Plugins](#creating-new-plugins)
- [Managing Plugins](#managing-plugins)
- [Troubleshooting](#troubleshooting)

---

## Understanding the Plugin System

Claude Code plugins extend functionality through:
- **Slash Commands** (`/command-name`) - Custom commands
- **Agents** - Specialized task automation
- **Skills** - Reusable capabilities
- **Hooks** - Event-triggered automation

**Marketplaces** are catalogs that list available plugins. You can have multiple marketplaces (local, GitHub, remote URLs).

---

## Directory Structure

Your workspace should have this structure:

```
your-project/
│
├── .claude/                              # Claude Code settings
│   ├── settings.json                    # Team-shared settings (commit to git)
│   └── settings.local.json              # Local settings (gitignore)
│
└── .claude-plugins/                      # Plugin installation directory
    │
    ├── .claude-plugin/                   # Local marketplace definition
    │   └── marketplace.json              # Marketplace catalog
    │
    └── {plugin-name}/                    # Individual plugin folders
        ├── .claude-plugin/
        │   └── plugin.json               # Plugin metadata
        ├── commands/                     # Slash commands
        ├── agents/                       # Custom agents
        ├── skills/                       # Reusable skills
        └── hooks/                        # Event hooks
```

---

## Installing Your Local Marketplace

### Step 1: Verify Marketplace Exists

Check that you have a local marketplace file:

```bash
ls .claude-plugins/.claude-plugin/marketplace.json
```

**Expected output:** Path to the file should be listed

### Step 2: Add Marketplace to Claude Code

Run this command in Claude Code:

```bash
/plugin marketplace add ./.claude-plugins
```

**✅ Correct paths:**
- `./.claude-plugins` (recommended - auto-detects marketplace.json)
- `./.claude-plugins/.claude-plugin/marketplace.json` (explicit path)

**❌ Common mistakes:**
- `./claude-plugins` (missing the dot before `claude`)
- Absolute paths (use relative paths from workspace root)

### Step 3: Verify Marketplace Installation

```bash
/plugin marketplace list
```

**Expected output:** Should show your marketplace name (e.g., `nickel-plugins`)

---

## Installing Plugins

### From Your Local Marketplace

Once your local marketplace is added:

```bash
/plugin install knowledge-graph@nickel-plugins
```

**Format:** `/plugin install {plugin-name}@{marketplace-name}`

### From GitHub

```bash
# Add GitHub marketplace
/plugin marketplace add owner/repo

# Install plugin
/plugin install plugin-name@owner-repo
```

### From Git Repository

```bash
# Add Git marketplace
/plugin marketplace add https://gitlab.com/company/plugins.git

# Install plugin
/plugin install plugin-name@company-plugins
```

### Browse Available Plugins

Interactive browser to discover plugins:

```bash
/plugin
```

Then select **"Browse Plugins"** to see all available plugins.

---

## Creating New Plugins

### Step 1: Create Plugin Directory Structure

```bash
mkdir -p .claude-plugins/my-new-plugin/.claude-plugin
mkdir -p .claude-plugins/my-new-plugin/commands
mkdir -p .claude-plugins/my-new-plugin/agents
mkdir -p .claude-plugins/my-new-plugin/hooks
```

### Step 2: Create plugin.json

Create `.claude-plugins/my-new-plugin/.claude-plugin/plugin.json`:

```json
{
  "name": "my-new-plugin",
  "version": "0.1.0",
  "description": "Brief description of what this plugin does",
  "author": {
    "name": "Your Name"
  }
}
```

### Step 3: Register in Marketplace

Edit `.claude-plugins/.claude-plugin/marketplace.json`:

```json
{
  "name": "nickel-plugins",
  "description": "Internal Claude Code plugins for nickel GTM operations",
  "owner": {
    "name": "nickel GTM Team"
  },
  "plugins": [
    {
      "name": "knowledge-graph",
      "source": "./knowledge-graph-plugin",
      "description": "Taxonomy management and knowledge graph governance"
    },
    {
      "name": "my-new-plugin",
      "source": "./my-new-plugin",
      "description": "Brief description of what this plugin does"
    }
  ]
}
```

### Step 4: Add Plugin Components

**Create a slash command** (`.claude-plugins/my-new-plugin/commands/hello.md`):

```markdown
---
name: hello
description: Says hello to the user
---

Say hello to the user in a friendly way!
```

**Create an agent** (`.claude-plugins/my-new-plugin/agents/my-agent.md`):

```markdown
---
name: my-agent
description: Does something useful
tools: [Read, Write, Bash]
---

# Agent Instructions

This agent helps with...

## Tasks
1. First task
2. Second task
```

### Step 5: Install Your Plugin

```bash
/plugin install my-new-plugin@nickel-plugins
```

### Step 6: Test Your Plugin

```bash
# Test slash command
/hello

# Test agent (via Task tool)
# Agent will be available as a subagent type
```

---

## Managing Plugins

### List Installed Plugins

```bash
/plugin list
```

### Enable/Disable Plugin

```bash
/plugin enable plugin-name@marketplace-name
/plugin disable plugin-name@marketplace-name
```

### Uninstall Plugin

```bash
/plugin uninstall plugin-name@marketplace-name
```

### Update Plugin

```bash
/plugin update plugin-name@marketplace-name
```

### List Marketplaces

```bash
/plugin marketplace list
```

### Remove Marketplace

```bash
/plugin marketplace remove marketplace-name
```

---

## Troubleshooting

### Issue: "Path does not exist"

**Problem:** Wrong path to marketplace

**Solution:**
- Ensure path starts with `./` for relative paths
- Check for the leading dot: `.claude-plugins` NOT `claude-plugins`
- Verify file exists: `ls .claude-plugins/.claude-plugin/marketplace.json`

**Correct:**
```bash
/plugin marketplace add ./.claude-plugins
```

**Incorrect:**
```bash
/plugin marketplace add ./claude-plugins  # Missing dot!
```

---

### Issue: Plugin not appearing in /plugin list

**Problem:** Plugin not registered in marketplace or marketplace not added

**Solution:**
1. Verify marketplace is added: `/plugin marketplace list`
2. Check marketplace.json includes your plugin
3. Reload Claude Code or re-add marketplace

---

### Issue: Commands not working after install

**Problem:** Plugin installed but commands don't appear

**Solution:**
1. Verify plugin is enabled: `/plugin list`
2. Check command file exists in `commands/` directory
3. Verify command has proper frontmatter (name, description)
4. Run `/help` to see if command appears

---

### Issue: Can't find plugin in browser

**Problem:** `/plugin` doesn't show your plugin

**Solution:**
1. Ensure marketplace is added: `/plugin marketplace list`
2. Verify plugin is listed in marketplace.json
3. Check `source` path in marketplace.json is correct

---

## Team Setup (Optional)

To auto-install plugins for your team, add marketplace to `.claude/settings.json`:

```json
{
  "plugins": {
    "marketplaces": [
      "./.claude-plugins"
    ]
  }
}
```

This ensures when team members trust the workspace folder, plugins are auto-discovered.

**Note:** Use `settings.json` for team settings (commit to git) and `settings.local.json` for personal settings (gitignore).

---

## Quick Reference

### Essential Commands

| Command | Description |
|---------|-------------|
| `/plugin` | Open plugin browser |
| `/plugin marketplace add ./path` | Add marketplace |
| `/plugin marketplace list` | List all marketplaces |
| `/plugin install name@marketplace` | Install plugin |
| `/plugin list` | List installed plugins |
| `/plugin enable name@marketplace` | Enable plugin |
| `/plugin disable name@marketplace` | Disable plugin |
| `/plugin uninstall name@marketplace` | Remove plugin |
| `/help` | View all available commands |

### Path Reference

| Path | Purpose |
|------|---------|
| `./.claude-plugins` | Plugin installation directory |
| `./.claude-plugins/.claude-plugin/marketplace.json` | Local marketplace catalog |
| `./.claude-plugins/{plugin-name}` | Individual plugin directory |
| `./.claude/settings.json` | Team-shared settings |
| `./.claude/settings.local.json` | Personal local settings |

### Plugin Structure Reference

```
{plugin-name}/
├── .claude-plugin/
│   └── plugin.json           # Required: metadata
├── commands/
│   └── my-command.md         # Slash command definition
├── agents/
│   └── my-agent.md           # Agent definition
├── skills/
│   └── my-skill.md           # Skill definition
└── hooks/
    └── hooks.json            # Event hooks configuration
```

---

## Additional Resources

- [Official Plugin Documentation](https://docs.claude.com/en/docs/claude-code/plugins)
- [Plugin Marketplace Guide](https://docs.claude.com/en/docs/claude-code/plugin-marketplaces)
- [Example Plugins Repository](https://github.com/anthropics/claude-code-plugins)

---

**Last Updated:** 2025-10-24
