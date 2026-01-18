---
name: decision-capture
description: Extract and document a decision with reasoning for future reference. Use when a clear decision has been made, trade-offs were weighed, or the user wants to record reasoning.
allowed-tools: Read Write Bash(date:*)
---

# Decision Capture

Extract and document a decision from the conversation.

## When to Use
- A clear decision has been made during conversation
- User wants to record reasoning for future reference
- Trade-offs were weighed and a choice was made

## Execution Steps

### Step 1: Get date
```bash
date "+%Y-%m-%d"
```

### Step 2: Identify the decision

If not clear from context, ask which decision to capture.

### Step 3: Create decision file

Location: `decisions/YYYY-MM-DD-decision-topic.md`

```markdown
---
title: "Decision: [Clear title]"
created: YYYY-MM-DD
tags: [decision, relevant-area]
status: active
---

# Decision: [Clear title]

**Date:** YYYY-MM-DD
**Area:** [Which life domain - career, projects, family, etc.]

## The Decision
[Clear statement of what was decided]

## Context
[What situation led to needing this decision]

## Options Considered

### Option 1: [Name]
[Description]
- Pros: ...
- Cons: ...

### Option 2: [Name]
[Description]
- Pros: ...
- Cons: ...

## Why This Option
[The reasoning and trade-offs that led to this choice]

## Implications
- What this means for...
- Changes to...

## Success Criteria
[How we'll know it was the right call]

## Review
[When to revisit - "in 3 months", "after X happens", or "no review needed"]

## Related
- [[session-file-if-applicable]]
- [[related-notes]]
```

### Step 4: Confirm

- Confirm the file location
- Remind that `/session` will push to GitHub
