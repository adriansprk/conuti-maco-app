# Cursor AI Agent Rules - BMAD-METHOD Structure

This directory contains the AI agent configuration for the MaCo API workspace, organized using **BMAD-METHOD's subdirectory structure** for scalability and specialization.

## Structure

```
.cursor/rules/
├── global-rules/                    # Always applied rules
│   ├── anti-hallucination-mandatory-always.mdc
│   └── maco-workspace-context-always.mdc
├── domain-rules/                     # Domain-specific workflows
│   ├── business-discovery-auto.mdc
│   └── technical-implementation-auto.mdc
├── validation-rules/                  # Message validation & building
│   ├── message-validation-agent-auto.mdc
│   └── message-builder-agent-auto.mdc
└── visualization-rules/               # Visualization requirements
    └── process-visualization-mandatory-always.mdc
```

## Rule Categories

### Global Rules (`global-rules/`)
- **Always Applied**: Loaded automatically for every chat and command
- **Purpose**: Core workspace context, file structure, key concepts, anti-hallucination
- **Files**: 
  - `maco-workspace-context-always.mdc` - Core context
  - `anti-hallucination-mandatory-always.mdc` - **CRITICAL**: Never hallucinate, always verify against documentation

### Domain Rules (`domain-rules/`)
- **Auto-Attached**: Applied based on glob patterns
- **Purpose**: Business discovery and technical implementation workflows
- **Files**: 
  - `business-discovery-auto.mdc` - Entry Point 1 (business goals)
  - `technical-implementation-auto.mdc` - Entry Point 2 (BDEW IDs)

### Validation Rules (`validation-rules/`)
- **Auto-Attached**: Applied when working with messages, APIs, validation code
- **Purpose**: Message validation and building agents
- **Files**:
  - `message-validation-agent-auto.mdc` - Validates messages against schemas/rules
  - `message-builder-agent-auto.mdc` - Pre-creates messages from database

### Visualization Rules (`visualization-rules/`)
- **Always Applied**: Mandatory visualization requirements
- **Purpose**: Ensures visualizations (Mermaid diagrams) are always created for processes
- **Files**: `process-visualization-mandatory-always.mdc`

## Key Features

### 1. Anti-Hallucination Protection (CRITICAL)
**NEVER provide information without reading documentation first:**
- Must read PROCESS_GRAPH.json before discussing processes
- Must read schema files (PI_[ID].yml) before describing APIs
- Must read business rules (yaml_output/[ID].yaml) before listing fields
- Must cite source files in every response
- Must admit when information is not found (never guess)
- See `global-rules/anti-hallucination-mandatory-always.mdc` for full requirements

### 2. Mandatory Visualizations
**Always create visualizations** when discussing processes:
- Sequence diagrams (Mermaid)
- Process flowcharts
- Message structure tables
- Required vs optional fields
- Example message references
- **All visualizations must be based on verified documentation**

### 2. Specialized Agents
- **Validation Agent**: Validates messages against schemas, business rules, and backend capabilities
- **Builder Agent**: Pre-creates messages from database entries, prepares for Conuti testing

### 3. Future-Ready Structure
Organized for future enhancements:
- Database integration for automatic field population
- Conuti API integration for test message sending
- Feedback loops for missing fields/functionality

## How It Works

When you clone this repository, Cursor automatically:
1. Loads `global-rules/*-always.mdc` for all contexts
2. Auto-attaches `domain-rules/*-auto.mdc` when glob patterns match
3. Auto-attaches `validation-rules/*-auto.mdc` for message/API work
4. Applies `visualization-rules/*-always.mdc` to ensure visualizations

## File Naming Convention

Following BMAD-METHOD pattern:
- `{purpose}-{type}.mdc`
- Types: `always` (always applied), `auto` (auto-attached), `agent` (agent-requested), `manual` (manual)

## Metadata Fields

Each `.mdc` file includes YAML frontmatter:
- `description`: Human-readable explanation
- `globs`: File patterns for auto-attachment (array format)
- `alwaysApply`: Boolean - if true, always loaded
- `tags`: Array of tags for categorization
- `priority`: Number for conflict resolution (1-5)
- `version`: Semantic version

## Best Practices

1. **Organization**: Rules organized by category (global, domain, validation, visualization)
2. **Focus**: One concern per rule file
3. **Examples**: Include valid/invalid examples using XML tags
4. **Visualizations**: Always create Mermaid diagrams for processes
5. **Version Control**: Rules tracked in Git, shared automatically

## Updating Rules

1. Edit the appropriate `.mdc` file in its category directory
2. Update `version` in frontmatter if making significant changes
3. Commit and push changes
4. Team members pull changes - rules update automatically

## Migration from Numbered Prefixes

We migrated from numbered prefixes (`00-`, `10-`, `20-`) to BMAD-METHOD's subdirectory structure for:
- Better scalability (can add more rules without renaming)
- Clearer organization by purpose/domain
- Easier maintenance and discovery
- Alignment with industry best practices (BMAD-METHOD)

## Testing Rules

To verify rules are loaded:
1. Open Cursor
2. Start a chat or use Cmd/Ctrl+K
3. Ask: "What is the workspace role?" (should mention LF, MaCo API)
4. Ask: "Show me process 55077" (should create visualization)
5. Ask: "Validate this message" (should use validation agent)

## References

- [BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) - Framework inspiration
- [Cursor Rules Documentation](https://cursor.directory/rules)
- [Best Practices Guide](https://forum.cursor.com/t/my-best-practices-for-mdc-rules-and-troubleshooting/50526)
