# State Directory

Working memory for Arc. These files provide continuity between sessions. State files make context explicit and persistent. They're the difference between a stateless chatbot and a genuine thinking partner.


## Files

| File | Purpose | Format |
|------|---------|--------|
| `focus.md` | Current priorities and what's on your mind | Markdown |
| `journal.jsonl` | Temporal record for pattern detection | JSON Lines |
| `projects.json` | Project/venture status | JSON |
| `session-context.json` | Last session metadata for continuity | JSON |

## Usage

**focus.md** - Read at session start, update when priorities shift. This is working memory.

**journal.jsonl** - Append-only log. Each session adds an entry. Query with `jq` for patterns:
```bash
# Last 5 entries
tail -5 state/journal.jsonl | jq .

# All entries about a specific area
cat state/journal.jsonl | jq 'select(.areas[] == "projects")'

# Topics in last 7 days
cat state/journal.jsonl | jq 'select(.t > "2025-12-17")'
```

**projects.json** - Source of truth for project status. Updated by project-tracker skill.

**session-context.json** - Enables picking up threads between sessions without re-explaining.

