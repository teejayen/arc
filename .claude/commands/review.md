---
description: Weekly review across all life areas and projects
---

Run a comprehensive weekly review.

Use the **weekly-review** skill (`.claude/skills/weekly-review/SKILL.md`) to:

1. Review last 7 days of sessions and journal entries
2. Check inbox for stale items
3. Review each life area (career, family, health, projects, etc.)
4. Analyse project status from `state/projects.json`
5. Detect patterns from `state/journal.jsonl`
6. Update `state/focus.md` with new priorities
7. Generate review document in `sessions/`
8. Offer follow-up actions

**Arguments:** `$ARGUMENTS`
- No args: Last 7 days (default)
- `2w`: Last 14 days

Best run: Sunday evening or Monday morning.
