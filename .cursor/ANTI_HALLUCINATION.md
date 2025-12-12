# Anti-Hallucination Protection - How It Works

## Overview

This workspace has **multiple layers of protection** to ensure agents always consult documentation and never hallucinate:

## Layer 1: Critical Global Rule (Always Applied)

**File**: `.cursor/rules/global-rules/anti-hallucination-mandatory-always.mdc`

**Priority**: 1 (Highest)

**Requirements**:
- ✅ **NEVER** provide information without reading documentation files first
- ✅ **NEVER** make up, guess, or assume process details
- ✅ **ALWAYS** verify information against source files
- ✅ **ALWAYS** cite sources in responses
- ✅ **ALWAYS** admit when information is not found (never guess)

## Layer 2: Workflow Rules (Domain-Specific)

### Business Discovery Rule
**File**: `.cursor/rules/domain-rules/business-discovery-auto.mdc`

**Requires**:
1. Read BUSINESS_PROCESS_MAP.md first
2. Read PROCESS_GRAPH.json for process details
3. Read docs-offline/ for workflow documentation
4. Cite all sources

### Technical Implementation Rule
**File**: `.cursor/rules/domain-rules/technical-implementation-auto.mdc`

**Requires**:
1. Read AI_AGENT_SETUP.md first
2. Read PROCESS_GRAPH.json for process lookup
3. Read PI_[ID].yml for schema structure
4. Read yaml_output/[ID].yaml for business rules
5. Read bo4e-openapi.min.json for BO4E types
6. Read example messages from maco-edi-testfiles/
7. Cite all sources

## Layer 3: Validation Rules

### Message Validation Agent
**File**: `.cursor/rules/validation-rules/message-validation-agent-auto.mdc`

**Requires**:
1. Load process from PROCESS_GRAPH.json
2. Load schema from PI_[ID].yml
3. Load business rules from yaml_output/[ID].yaml
4. Load BO4E types from bo4e-openapi.min.json
5. Validate against actual files, not assumptions

### Message Builder Agent
**File**: `.cursor/rules/validation-rules/message-builder-agent-auto.mdc`

**Requires**:
1. Load process from PROCESS_GRAPH.json
2. Load schema from PI_[ID].yml
3. Load business rules from yaml_output/[ID].yaml
4. Build messages based on verified schemas
5. Validate against actual files

## Verification Checklist

Before providing ANY answer, agents must:

- [ ] Identify process ID or name
- [ ] Read PROCESS_GRAPH.json
- [ ] Read relevant documentation (docs-offline/)
- [ ] Read schema file (PI_[ID].yml)
- [ ] Read business rules (yaml_output/[ID].yaml)
- [ ] Read BO4E types (bo4e-openapi.min.json)
- [ ] Reference example messages (maco-edi-testfiles/)
- [ ] Cite all sources in response
- [ ] Admit if information not found (never guess)

## Response Format

Agents must structure responses as:

```markdown
## Answer

[Answer based on verified documentation]

## Sources Verified

- PROCESS_GRAPH.json: [specific section]
- Schema: PI_[ID].yml
- Business Rules: yaml_output/[ID].yaml
- BO4E Types: bo4e-openapi.min.json
- Examples: maco-edi-testfiles/[path]
- Documentation: docs-offline/[filename].md
```

## Prohibited Behaviors

Agents are **explicitly prohibited** from:
- ❌ Answering without reading documentation files
- ❌ Making up field names, endpoints, or structures
- ❌ Guessing process dependencies
- ❌ Assuming schema structures
- ❌ Inventing business rules
- ❌ Creating examples without referencing test files
- ❌ Providing information without citing sources
- ❌ Filling gaps with assumed information

## Enforcement

The anti-hallucination rule has:
- **Priority 1** (highest)
- **alwaysApply: true** (always loaded)
- **Critical tag** (marked as critical)
- **Integration** with all other rules

## Testing

To verify anti-hallucination protection:

1. **Ask**: "What fields are required for process 55077?"
   - ✅ Should read PI_55077.yml and yaml_output/55077.yaml
   - ✅ Should cite sources
   - ✅ Should reference example messages

2. **Ask**: "What is the API endpoint for process 55077?"
   - ✅ Should read PROCESS_GRAPH.json and schemas
   - ✅ Should cite sources
   - ✅ Should not guess

3. **Ask**: "What is process 99999?" (non-existent)
   - ✅ Should say "I cannot find this process in PROCESS_GRAPH.json"
   - ✅ Should list what was checked
   - ✅ Should NOT make up information

## Summary

**The setup is superior** because it:

1. ✅ **Mandates documentation reading** before answering
2. ✅ **Requires source citation** in every response
3. ✅ **Prohibits guessing** or making up information
4. ✅ **Enforces verification** across multiple sources
5. ✅ **Integrates with all rules** (visualization, validation, etc.)
6. ✅ **Has highest priority** (always applied, priority 1)

**Agents cannot hallucinate** because they are explicitly required to read documentation files and cite sources, with clear prohibitions against guessing or making up information.
