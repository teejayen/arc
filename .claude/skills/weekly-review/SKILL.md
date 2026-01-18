---
name: weekly-review
description: Comprehensive review across all life areas and projects. Use weekly (Sunday/Monday), when feeling scattered, after returning from break, or when the user runs /review.
allowed-tools: Read Write Edit Bash(date:*) Bash(ls:*) Bash(git:*)
---

# Weekly Review

Comprehensive review across all life areas and projects.

## When to Use
- Weekly (suggest: Sunday evening or Monday morning)
- When feeling scattered or overwhelmed
- After returning from break/holiday
- User runs `/review`

## Execution Steps

### Step 1: Get context

```bash
date "+%Y-%m-%d %H:%M"
```

Read current state:
- `state/focus.md`
- `state/projects.json`
- `state/journal.jsonl` (last 7 entries)
- `state/session-context.json`

### Step 2: Review sessions

List recent sessions (files are named `YYYY-MM-DD-HHMM-topic.md`):
```bash
ls -1 sessions/ | tail -10
```

Read the recent session files to understand what was explored last week.

### Step 3: Check inbox

```bash
ls -la inbox/
```

Flag:
- Item count
- Anything older than 7 days (stale)
- Patterns in what's accumulating

### Step 4: Review each area

For each area in `areas/`:
- What happened this week?
- Any open loops?
- Anything neglected?

Review the life areas defined in user-context.md. Common areas:
- **Career** - Work status, professional development
- **Family** - Upcoming commitments, quality time
- **Health** - Exercise, fitness consistency
- **Finance** - Any actions needed
- **Projects** - Side project progress

### Step 5: Review projects specifically

Read `state/projects.json` and for each project:
- What moved forward?
- What's blocked?
- What's the next milestone?

Update `state/projects.json` with current status.

### Step 6: Pattern detection

Query `state/journal.jsonl` for patterns:
- Which topics keep recurring?
- Energy levels over the week
- Any areas consistently absent?

### Step 7: Update focus.md

Rewrite `state/focus.md` with:
- This week's priorities
- What's on the mind
- Any shifts in focus

### Step 8: Generate review document

Create `sessions/YYYY-MM-DD-weekly-review.md`:

```markdown
---
title: "Weekly Review: [date range]"
created: YYYY-MM-DD
tags: [review, weekly]
---

# Weekly Review: [start] to [end]

## Summary
[Overall sense of the week]

## By Area

### Career
- [Status/progress/notes]

### Family
- [Status/notes]

### Health
- [Status/notes]

### Projects
[For each project in projects.json:]

#### [Project Name]
- Status: [from projects.json]
- Progress: [what moved]
- Next: [upcoming milestone]

### Other Areas
- [Any notable updates]

## Patterns Noticed
- [Recurring themes from journal]
- [Energy patterns]
- [Neglected areas]

## Wins
- [What went well]

## Open Loops
- [Unresolved items needing attention]

## Next Week Focus
1. [Priority 1]
2. [Priority 2]
3. [Priority 3]

## Inbox Status
- Items: [count]
- Stale: [count]
- Action: [process now / schedule time]
```

### Step 9: Offer actions

- Process inbox now?
- Any decisions to capture?
- Update any project files?
