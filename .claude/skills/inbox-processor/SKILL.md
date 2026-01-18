---
name: inbox-processor
description: Sort items from inbox/ to their proper locations. Use when inbox has accumulated items, during weekly review, or when the user asks to process/clear inbox.
allowed-tools: Read Write Edit Bash(ls:*) Bash(mv:*) Bash(rm:*)
---

# Inbox Processor

Sort items from inbox/ to their proper locations.

## When to Use
- Inbox has accumulated items
- During weekly review
- User asks to process/clear inbox
- Session start hook shows stale items

## Execution Steps

### Step 1: List inbox contents

```bash
ls -la inbox/
```

Note:
- File ages (flag anything > 7 days as stale)
- File types and naming patterns
- Rough categorisation

### Step 2: Process each item

For each file, determine destination based on content:

| Content Type | Destination |
|--------------|-------------|
| Quick thought/idea | `areas/[relevant]/` or `projects/[relevant]/` |
| Decision draft | `decisions/` (use decision-capture skill) |
| External link/resource | `resources/[type]/` (use capture skill) |
| Project-related | `projects/[project]/` |
| Area-related | `areas/[area]/` |
| Historical/completed | `archive/` |
| Session notes | `sessions/` |

### Step 3: Move or transform

For each item:
1. Read the content
2. Determine if it needs transformation (adding frontmatter, restructuring)
3. Either move as-is or create proper file in destination
4. Delete original from inbox/

### Step 4: Handle ambiguous items

If destination unclear:
- Ask the user
- Or leave in inbox/ with a note about why

### Step 5: Report

Summarise what was processed:
```markdown
## Inbox Processed

**Items moved:** X
- `thought.md` -> `areas/career/notes.md`
- `link.md` -> `resources/bookmarks/tool.md`

**Items archived:** X
- `old-note.md` -> `archive/2025/`

**Items remaining:** X
- `unclear.md` - needs clarification

**Inbox status:** Clear / X items remaining
```

### Step 6: Update focus if needed

If processing revealed something important, update `state/focus.md`.
