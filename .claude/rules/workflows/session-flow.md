# Session Flow

## Starting a Session

When a new session begins:
1. Briefly acknowledge (no elaborate greetings)
2. Check `state/focus.md` for current priorities
3. Note anything requiring attention (stale inbox, pending decisions)
4. Let the user lead - ask "What's on your mind?" or similar

## During a Session

- This is thinking out loud, not task execution
- Follow the thread wherever it goes
- Note when patterns emerge across topics
- Capture decisions as they crystallise
- Update state files when context shifts

## Ending a Session

When the user signals done (or runs `/session`):
1. Summarise what was explored
2. Create session file in `sessions/`
3. Append to `state/journal.jsonl` with key topics
4. Update `state/focus.md` if priorities shifted
5. Git commit and push
6. Offer quote from `quotes.md` as send-off (if the file exists)

## Between Sessions

State files persist context:
- `state/focus.md` - what matters now
- `state/journal.jsonl` - temporal record for pattern detection
- `state/projects.json` - structured project tracking
- `state/session-context.json` - last session metadata

This means I can pick up threads without the user re-explaining everything.
