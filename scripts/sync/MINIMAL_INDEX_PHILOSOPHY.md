# Minimal Index Philosophy

## Problem with Pre-processing

Pre-processing documentation introduces several risks:

1. **Interpretation Errors**: We infer triggers, roles, prerequisites, relationships - but these can be wrong
2. **Loss of Context**: Raw docs have nuance (conditional flows, cross-references, German prose) that gets flattened
3. **Single Point of Failure**: If PROCESS_GRAPH.json is wrong, every agent inherits that error
4. **Maintenance Drift**: Docs update → script must re-run → validation needed → can silently become stale

## Solution: Minimal Index

**Philosophy**: "Point, don't interpret"

The minimal index (`PROCESS_GRAPH.json`) contains only:
- **Factual mappings**: BDEW IDs → files, triggers → files, process names → files
- **File metadata**: Which files have Mermaid diagrams, which are Prozessübersicht
- **Discovery indexes**: Help agents find relevant files quickly

**What it does NOT contain**:
- ❌ Inferred triggers, roles, prerequisites
- ❌ Processed/interpreted relationships
- ❌ Flattened process definitions
- ❌ Business scenarios (manually curated separately)

## Agent Workflow

1. **Use index for discovery**: `indexes.by_bdew_id["55001"]` → find files
2. **Read source files**: Parse actual markdown files
3. **Extract from source**: Get roles, prerequisites, relationships from Mermaid diagrams and prose
4. **Cross-reference**: Use API schemas, business rules, test files

## Benefits

✅ **Accuracy**: Agents read source material, not our interpretation
✅ **Self-correction**: Agents can verify against source docs
✅ **Context preservation**: Full nuance of original documentation retained
✅ **Reduced maintenance**: Index only needs updates when files change, not when interpretation changes

## Implementation

The `update-process-graph-minimal.py` script implements this approach - it only creates indexes pointing to source files, with no interpretation or processing.
