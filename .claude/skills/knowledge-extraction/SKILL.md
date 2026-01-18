---
name: knowledge-extraction
description: Capture learnings, patterns, and reusable knowledge from conversations. Use when a useful pattern emerged, something was learned worth remembering, or a solution might apply elsewhere.
allowed-tools: Read Write Bash(date:*)
---

# Knowledge Extraction

Capture learnings, patterns, and reusable knowledge from conversations.

## When to Use
- A useful pattern or approach emerged
- Something was learned that's worth remembering
- A solution was found that might apply elsewhere
- User explicitly wants to save knowledge

## Execution Steps

### Step 1: Identify the knowledge

Types of extractable knowledge:
- **How-to**: Process or technique
- **Pattern**: Recurring approach or structure
- **Insight**: Understanding about how something works
- **Reference**: Facts or information worth keeping
- **Lesson**: Learning from experience (including failures)

### Step 2: Determine destination

| Knowledge Type | Destination |
|----------------|-------------|
| Technical how-to | `areas/learning/[topic].md` |
| Life pattern | `areas/[relevant-area]/patterns.md` or standalone |
| Project insight | `areas/[project]/learnings.md` |
| General reference | `resources/[topic]/` |
| Tool/product knowledge | `resources/tools/[tool].md` |

### Step 3: Create knowledge file

```markdown
---
title: "[Clear descriptive title]"
created: YYYY-MM-DD
tags: [knowledge, topic, source-area]
type: [how-to|pattern|insight|reference|lesson]
---

# [Title]

## Summary
[One paragraph - what this knowledge is and why it matters]

## The Knowledge

### Context
[When/where this applies]

### Detail
[The actual knowledge - steps, pattern description, insight explanation]

### Examples
[If applicable - concrete examples of application]

## Caveats
[If applicable - when this doesn't apply, edge cases]

## Source
[Where this came from - session reference, experience, external source]

## Related
- [[related-notes]]
```

### Step 4: Link appropriately

- Add reference in relevant area/project files
- Update any index files if they exist
- Note in session file that knowledge was extracted

### Step 5: Confirm

- Show file location
- Summarise what was captured
