---
name: session-save
description: Save current conversation session and push to GitHub. Use when the user says "let's wrap up", "save this", "I'm done", runs /session, or at natural end of a conversation thread.
allowed-tools: Read Write Edit Bash(date:*) Bash(git:*)
---

# Session Save

Save the current conversation session and update state files.

## When to Use
- User says "let's wrap up", "save this", "I'm done", or runs `/session`
- Natural end of a conversation thread
- Before switching to a significantly different topic

## Execution Steps

### Step 1: Gather context
```bash
date "+%Y-%m-%d %H:%M"
```

### Step 2: Create session file

Location: `sessions/YYYY-MM-DD-HHMM-topic.md`

```markdown
---
title: "Session: [Brief descriptive title]"
created: YYYY-MM-DD
tags: [session, relevant-area-tags]
---

# Session: [Brief title]

**Date:** YYYY-MM-DD HH:MM
**Topics:** keyword, keyword, keyword

## Summary
[2-3 paragraphs - what was explored, problems discussed, thinking developed]

## What Got Done
- Concrete outcome 1
- Concrete outcome 2
[Be specific: "Created areas/project/analysis.md" not "discussed project"]

## Key Insights
- Insight that emerged from the conversation
- Pattern noticed or connection made

## Decisions Made
[Remove section if none]
- Decision with brief rationale

## Open Questions
[Remove section if none]
- Question still needing resolution

## Next
[Remove section if none]
- Follow-up to explore

## Related
- [[relevant-notes]]
```

### Step 3: Update journal.jsonl

Append to `state/journal.jsonl`:
```json
{"t": "YYYY-MM-DDTHH:MM", "topics": ["topic1", "topic2"], "energy": "high|medium|low", "areas": ["area1", "area2"], "summary": "One-line session summary"}
```

### Step 4: Update focus.md if needed

If priorities shifted during the session, update `state/focus.md` to reflect current thinking.

### Step 5: Update session-context.json

Write to `state/session-context.json`:
```json
{
  "last_session": "YYYY-MM-DD HH:MM",
  "last_topic": "topic",
  "open_threads": ["thread1", "thread2"],
  "next_suggested": "What to pick up next time"
}
```

### Step 6: Git commit and push
```bash
git add -A
git commit -m "Session: [topic] - YYYY-MM-DD HH:MM"
git push
```

### Step 7: Quote send-off (optional)

If `quotes.md` exists, pick a random quote:

> "[quote]"
> — [author]

### Step 8: Offer extractions

- Any decisions worth extracting to `decisions/`?
- Any content to process from `inbox/`?
