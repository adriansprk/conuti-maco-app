# Index Usage Guide for AI Agents

## 🎯 Which Index to Use?

### ⭐ **Use `llm.txt` as the Primary Index**

**The original `llm.txt` already provides all the context you need!**

- ✅ Process names and descriptions
- ✅ BDEW IDs (in brackets like `[55016]`)
- ✅ Hierarchical structure (Lieferant > Kündigung LFA > Prozessübersicht)
- ✅ URLs to documentation

**What was missing?** The actual markdown content - which is now available in `docs-offline/*.md`

### Workflow

1. **Use `llm.txt`** to find which documentation you need:
   ```markdown
   - Lieferant > Kündigung LFA [Prozessübersicht](https://doc.macoapp.de/prozessübersicht-860885m0.md)
   ```

2. **Extract the filename** from the URL:
   - URL: `https://doc.macoapp.de/prozessübersicht-860885m0.md`
   - Filename: `prozessübersicht-860885m0.md`

3. **Read the downloaded file**:
   - Path: `docs-offline/prozessübersicht-860885m0.md`

### Alternative: `enhanced-index.json`

**Optional** - Use only if you need programmatic JSON access:

- ✅ Structured JSON format (easier to parse programmatically)
- ✅ Quick lookups by BDEW ID or process name
- ⚠️ Duplicates information already in `llm.txt`

**When to use `enhanced-index.json`**:
- Building tools that need JSON parsing
- Quick programmatic lookups
- When you prefer structured data over text parsing

**When to use `llm.txt`**:
- Human-readable format
- Original source of truth
- Already familiar structure
- Most AI agents can parse markdown easily

## 📋 Example: Finding Kündigung Documentation

### Using `llm.txt` (Recommended)

```markdown
# Search llm.txt for "Kündigung LFA"
- Lieferant [Kündigung LFA](https://doc.macoapp.de/kündigung-lfa-3118804f0.md)
- Lieferant > Kündigung LFA [Prozessübersicht](https://doc.macoapp.de/prozessübersicht-860885m0.md)
- Lieferant > Kündigung LFA > EBD [EBD E_0614](https://doc.macoapp.de/lf_0614.md)

# Extract filenames and read from docs-offline/
docs-offline/kündigung-lfa-3118804f0.md
docs-offline/prozessübersicht-860885m0.md
docs-offline/lf_0614.md
```

### Using `enhanced-index.json` (Optional)

```json
{
  "by_process_name": {
    "Lieferant > Kündigung LFA [Prozessübersicht]": [
      {
        "filename": "prozessübersicht-860885m0.md",
        "url": "https://doc.macoapp.de/prozess%C3%BCbersicht-860885m0.md"
      }
    ]
  }
}
```

## ✅ Recommendation

**Use `llm.txt` as your primary index** because:
1. It's the original source of truth
2. Already contains all context and structure
3. Human-readable and easy to parse
4. The downloaded markdown files provide the content that was missing

**Use `enhanced-index.json`** only if you specifically need:
- Programmatic JSON parsing
- Quick structured lookups
- Tool building that requires JSON format

## Summary

| Resource | Purpose | When to Use |
|----------|---------|-------------|
| `llm.txt` | Index/context (process names, BDEW IDs, URLs) | **Primary** - Always use this to find documentation |
| `docs-offline/*.md` | Actual markdown content | Read after finding in `llm.txt` |
| `enhanced-index.json` | JSON version of `llm.txt` structure | Optional - only if you need programmatic JSON access |
| `index.json` | Simple filename → URL mapping | Not recommended - use `llm.txt` instead |
