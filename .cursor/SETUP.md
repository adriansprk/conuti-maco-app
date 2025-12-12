# Cursor Rules Setup Verification

## Quick Verification

After cloning this repository, verify the setup works:

1. **Open Cursor** in this workspace
2. **Start a chat** or use Cmd/Ctrl+K
3. **Test global rule**: Ask "What is the workspace role?"
   - Should mention: Lieferant (LF), MaCo API, MaKo messages
4. **Test business discovery**: Ask "I want to register a new customer, what should I do?"
   - Should reference: BUSINESS_PROCESS_MAP.md, PROCESS_GRAPH.json
5. **Test technical implementation**: Ask "How do I implement process 55077?"
   - Should reference: AI_AGENT_SETUP.md, schemas, business rules

## File Structure Check

Verify these files exist:
```
.cursor/
├── README.md                    ✅ Documentation
├── SETUP.md                     ✅ This file
└── rules/
    ├── 00-global.mdc            ✅ Always applied
    ├── 10-business-discovery.mdc ✅ Auto-attached
    └── 20-technical-implementation.mdc ✅ Auto-attached
```

## Git Status

The `.cursor/` directory should be tracked in Git:
```bash
git status .cursor/
```

Should show files as tracked (not ignored).

## Troubleshooting

### Rules Not Loading

1. **Check Cursor version**: Requires Cursor 0.45+ for `.cursor/rules/` support
2. **Restart Cursor**: After cloning, restart Cursor to load rules
3. **Check file extensions**: Must be `.mdc` (not `.md` or `.mdc.md`)
4. **Verify YAML frontmatter**: Each `.mdc` file must start with `---`

### Rules Loading But Not Applying

1. **Check glob patterns**: Verify file patterns match your working files
2. **Check alwaysApply**: Only `00-global.mdc` should have `alwaysApply: true`
3. **Check description**: Rules with `alwaysApply: false` need good descriptions for agent-requested loading

### Team Members Not Getting Rules

1. **Verify Git commit**: Ensure `.cursor/` directory is committed
2. **Check .gitignore**: `.cursor/` should NOT be in `.gitignore`
3. **Pull latest**: Team members need to `git pull` to get updates

## Migration from .cursorrules

If you have an old `.cursorrules` file:

1. ✅ New system is set up (`.cursor/rules/*.mdc`)
2. ⚠️ Old `.cursorrules` can be removed after testing
3. 📝 Update any team documentation referencing `.cursorrules`

## Best Practices Checklist

- ✅ Rules are organized by concern (global, business, technical)
- ✅ Numbered prefixes for load order (`00-`, `10-`, `20-`)
- ✅ Proper YAML frontmatter with metadata
- ✅ Valid/invalid examples included
- ✅ Globs use array format (no quotes around patterns)
- ✅ Version numbers in metadata
- ✅ Documentation in `.cursor/README.md`

## Next Steps

1. **Test the setup** using verification steps above
2. **Commit changes**: `git add .cursor/ && git commit -m "feat: Add Cursor rules (2025 best practices)"`
3. **Share with team**: Push to repository
4. **Remove old file**: After confirming, remove `.cursorrules` if it exists
