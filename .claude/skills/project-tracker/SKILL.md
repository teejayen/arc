---
name: project-tracker
description: Track progress and status of projects and ventures. Use when discussing projects, progress updates, milestones reached, blockers identified, or during weekly review.
allowed-tools: Read Write Edit Bash(date:*)
---

# Project Tracker

Track progress and status of projects and ventures.

## When to Use
- Discussing any project
- Progress update or milestone reached
- Blocker identified or resolved
- Strategic thinking about projects
- Weekly review

## Execution Steps

### Step 1: Read current state

```bash
cat state/projects.json
```

Current structure:
```json
{
  "project_slug": {
    "status": "ideation|building|launched|paused",
    "tagline": "One-line description",
    "next_milestone": "What's the immediate goal",
    "blockers": ["blocker1", "blocker2"],
    "recent_progress": ["item1", "item2"],
    "updated": "YYYY-MM-DD"
  }
}
```

### Step 2: Determine update type

- **Progress update**: Something moved forward
- **Blocker identified**: New obstacle discovered
- **Blocker resolved**: Obstacle removed
- **Milestone reached**: Next milestone needs updating
- **Status change**: Major phase transition
- **Strategic discussion**: Thinking through direction

### Step 3: Update projects.json

Make appropriate updates:
- Add to `recent_progress` (keep last 5 items)
- Update `blockers` array
- Update `next_milestone` if reached
- Update `status` if phase changed
- Always update `updated` date

### Step 4: Update area files if needed

For significant updates, also update:
- `areas/[project-name]/` files

### Step 5: Cross-reference

Note connections:
- Does this affect career planning?
- Time/resource implications for family?
- Learning opportunities to capture?

### Step 6: Summarise

Provide current project status summary:

```markdown
## Project Status

### [Project Name]
**Status:** [status]
**Next milestone:** [milestone]
**Blockers:** [blockers or "None"]
**Recent:** [last progress item]

### [Another Project]
**Status:** [status]
**Next milestone:** [milestone]
**Blockers:** [blockers or "None"]
**Recent:** [last progress item]

---
*Updated: YYYY-MM-DD*
```

## State File Location

`state/projects.json` - source of truth for project status.

Area folders (`areas/[project-name]/`) contain deeper documentation, plans, and notes.
