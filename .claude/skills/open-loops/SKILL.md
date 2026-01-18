---
name: open-loops
description: Track and manage open threads, hanging items, and things waiting for follow-up. Use to add new threads, review what's stale, mark items resolved, or get a quick status of what's hanging.
allowed-tools: Read Write Edit Bash(date:*)
---

# Open Loops

Track and manage open threads - things waiting for follow-up, hanging items, commitments made.

## When to Use
- Something needs follow-up but isn't a full project
- Reviewing what's hanging at session start
- Marking something as done/resolved
- Feeling like things are slipping through cracks

## Data Structure

Open loops live in `state/session-context.json` under `open_threads`:

```json
{
  "open_threads": [
    "Thread description - context if needed",
    "Another hanging item"
  ]
}
```

For richer tracking, can optionally use `state/open-loops.json`:

```json
{
  "loops": [
    {
      "id": "loop-001",
      "description": "Send invoices",
      "context": "Price TBD - waiting on confirmation",
      "added": "2025-12-28",
      "area": "finance",
      "status": "waiting",
      "stale_after_days": 7
    }
  ]
}
```

## Execution Steps

### Quick Status

Read current threads:
```bash
cat state/session-context.json | jq '.open_threads'
```

Report:
- Total count
- Flag any that look stale (been mentioned in multiple sessions)
- Group by apparent area if patterns emerge

### Add New Loop

When user mentions something that needs follow-up:

1. Ask for clarification if needed:
   - What's the actual action?
   - Any deadline or "stale by" date?
   - Which area does this relate to?

2. Add to `session-context.json`:
   ```json
   "open_threads": [
     "existing thread",
     "New thread - brief context"
   ]
   ```

3. Confirm what was added

### Resolve Loop

When something is done:

1. Read current threads
2. Remove the resolved item
3. Optionally note in session summary that it was closed
4. Update the file

### Review Loops

Full review of what's hanging:

1. Read `state/session-context.json`
2. Cross-reference with recent `state/journal.jsonl` entries
3. Identify:
   - **Active**: Recently mentioned, making progress
   - **Stale**: Not mentioned in 3+ sessions, may be stuck
   - **Waiting**: Blocked on external input
   - **Maybe obsolete**: Context has changed

4. Present summary:

```markdown
## Open Loops Status

**Active (3)**
- Send invoice EOM - due soon
- Content posts Monday - in progress

**Stale (2)**
- Meeting with contact - no movement in 4 sessions
- Code migration - been sitting since Dec 24

**Waiting (1)**
- Invoices - waiting on price confirmation

### Suggested Actions
- Close obsolete items?
- Set concrete next step for stale items?
- Any new threads to add?
```

### Cleanup

Periodically (during weekly review or when list feels cluttered):

1. Review each item
2. Archive completed/obsolete to session notes
3. Consolidate duplicates
4. Ensure descriptions are still accurate

## Integration

- **Session start**: Startup hook shows open threads
- **Session save**: Review if any threads resolved or new ones emerged
- **Weekly review**: Full loops audit

## Philosophy

Open loops are the "things on your mind" that aren't big enough for projects but important enough to track. The goal isn't perfect tracking - it's preventing the mental load of trying to remember everything.

If a loop keeps sitting stale, that's information: either it's not actually important, or there's a blocker worth naming.
