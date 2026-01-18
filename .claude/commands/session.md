---
description: Save current conversation session and push to GitHub
---

Save this conversation and update state files.

Use the **session-save** skill (`.claude/skills/session-save/SKILL.md`) to:

1. Create session file in `sessions/YYYY-MM-DD-HHMM-topic.md`
2. Append to `state/journal.jsonl`
3. Update `state/focus.md` if priorities shifted
4. Update `state/session-context.json`
5. Git commit and push
6. Show random quote from `quotes.md` (if it exists)
7. Offer to extract any decisions
