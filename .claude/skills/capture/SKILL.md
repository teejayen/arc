---
name: capture
description: Save external content (bookmarks, YouTube, Spotify, articles) with context. Use when the user shares a link worth saving or external content needs to be captured with context for the reference library.
allowed-tools: Read Write Bash(date:*)
---

# Capture

Save external content (bookmarks, YouTube, Spotify, articles) with context.

## When to Use
- User shares a link worth saving
- External content needs to be captured with context
- Building a reference library of resources

## Execution Steps

### Step 1: Determine content type

From context or ask:
- **bookmark** -> `resources/bookmarks/`
- **youtube** -> `resources/youtube/`
- **spotify** -> `resources/spotify/`
- **article** -> `resources/articles/`
- **other** -> `resources/` root or create new subfolder

### Step 2: Gather details

If not provided, ask for:
- URL or identifier
- Why this matters / why saving it (this is the valuable context)
- Tags or topics it relates to
- Any specific notes

### Step 3: Create capture file

Filename: `descriptive-title.md` (no date prefix - frontmatter has timestamp)

```markdown
---
title: "[Content title]"
created: YYYY-MM-DD
source: [full URL]
platform: [youtube|spotify|web|twitter|podcast|etc]
tags: [topic, topic]
status: unprocessed
---

# [Content title]

**Source:** [URL]
**Captured:** YYYY-MM-DD

## Why I Saved This
[User's reason - the context that will matter when rediscovering this later]

## Summary
[Brief description of what this is]

## Key Points
[If applicable - remove if just a bookmark for later]
- Point 1
- Point 2

## Notes
[Additional context, quotes, timestamps for videos, etc.]

## Related
- [[relevant-notes]]
```

### Step 4: Confirm

- Show saved location
- Suggest related areas/projects to link
- Note if this connects to current focus areas
