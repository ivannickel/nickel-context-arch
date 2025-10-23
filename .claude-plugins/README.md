# Nickel Claude Code Plugins

This directory contains local Claude Code plugins for nickel GTM operations.

## Installation

From the repo root, run:

```bash
/plugin marketplace add ./.claude-plugins
/plugin install knowledge-graph@nickel-plugins
```

## Available Plugins

### Knowledge Graph Navigator (v0.1.0)

Taxonomy management and knowledge graph governance for FOAM-based systems.

**Commands:**
- `/taxonomy-snapshot` - Generate weekly taxonomy health report
- `/add-frontmatter` - Add compliant YAML frontmatter to documents
- `/validate-frontmatter` - Validate frontmatter compliance
- `/navigate-to-hub` - Navigate to knowledge graph hub documents

**Documentation:** See [knowledge-graph-plugin/README.md](knowledge-graph-plugin/README.md)

**Development:** See [knowledge-graph-plugin/DEVELOPMENT.md](knowledge-graph-plugin/DEVELOPMENT.md)

## Directory Structure

```
.claude-plugins/
├── .claude-plugin/
│   └── marketplace.json           # Marketplace manifest
└── knowledge-graph-plugin/        # Plugin directory
    ├── .claude-plugin/
    │   └── plugin.json            # Plugin manifest
    ├── agents/                    # Custom agents
    ├── commands/                  # Slash commands
    ├── scripts/                   # Python scripts
    ├── data/                      # Generated data
    ├── README.md                  # User guide
    └── DEVELOPMENT.md             # Developer guide
```

## For Team Members

This marketplace is configured for local development. When you clone the repo:

1. Open Claude Code in the repo root
2. Run the installation commands above
3. Start using the plugins immediately

Changes to plugin files are reflected immediately - no rebuild needed.
