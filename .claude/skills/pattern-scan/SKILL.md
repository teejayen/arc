---
name: pattern-scan
description: Deep analysis of journal entries to surface patterns - recurring topics, energy trends, neglected areas, avoidance patterns. Use when wanting insight into what's actually getting attention over time.
allowed-tools: Read Bash(date:*) Bash(wc:*) Bash(jq:*)
---

# Pattern Scan

Analyse journal.jsonl to surface patterns across time - what's recurring, what's neglected, energy trends, and avoidance patterns.

## When to Use
- Wanting perspective on where attention has been going
- Feeling scattered - what's actually getting focus?
- Noticing something keeps coming up
- Weekly/monthly reflection
- Sensing avoidance but not sure of what

## Data Source

Primary: `state/journal.jsonl`

Each entry:
```json
{
  "t": "2025-12-28T09:10",
  "topics": ["planning", "strategy", "project-x"],
  "energy": "high|medium|low",
  "areas": ["projects", "learning"],
  "summary": "One-line session summary"
}
```

Secondary: `sessions/` folder for deeper context (files named `YYYY-MM-DD-HHMM-topic.md`).

## Execution Steps

### Step 1: Load Data

```bash
cat state/journal.jsonl
```

Parse all entries. Note the date range covered.

### Step 2: Topic Frequency

Count occurrences of each topic across all entries.

Present as:
```markdown
## Topic Frequency (last N sessions)

| Topic | Count | % of Sessions |
|-------|-------|---------------|
| project-x | 5 | 100% |
| content | 3 | 60% |
| planning | 2 | 40% |
| ...
```

Flag:
- **Dominant topics**: Appearing in >50% of sessions
- **One-offs**: Appeared once, might indicate unfinished thread
- **Emerging**: New in recent sessions

### Step 3: Area Coverage

Which life areas are getting attention?

```markdown
## Area Coverage

| Area | Sessions | Last Touched |
|------|----------|--------------|
| projects | 5 | today |
| learning | 2 | 2025-12-27 |
| career | 0 | never |
| family | 0 | never |
| health | 0 | never |
```

Flag:
- **Neglected**: Areas with 0 sessions or not touched in 2+ weeks
- **Dominant**: Areas consuming >40% of sessions
- **Balanced**: Areas with steady, moderate attention

### Step 4: Energy Patterns

Track energy levels over time:

```markdown
## Energy Trend

| Date | Energy | Topics |
|------|--------|--------|
| 2025-12-28 | high | planning, strategy |
| 2025-12-27 | high | content, writing |
| 2025-12-26 | medium | admin, cleanup |
| ...

**Pattern**: Mostly high energy sessions - sustainable, or avoiding low-energy work?
```

Look for:
- **Consistent high**: Sustainable, or not capturing draining sessions?
- **Consistent low**: Burnout risk, or just honest tracking?
- **Topic-energy correlation**: Do certain topics correlate with energy?

### Step 5: Avoidance Detection

Cross-reference what's present vs. what should be present:

Areas defined in user-context.md. Questions to surface:
- Which areas have zero sessions?
- Which topics appeared once then disappeared?
- What's mentioned in open_threads but never in sessions?
- Any patterns in what gets "pushed to next time"?

```markdown
## Potential Avoidance Patterns

**Areas never touched:**
- career - professional development, skill building
- family - quality time, commitments
- health - exercise, fitness

**Open loops not becoming sessions:**
- "Follow up on X" - sitting since Dec 24

**Observation:**
High energy creative work (projects, content) is happening.
Admin, career planning, health tracking are not.

This isn't necessarily bad - but worth naming.
```

### Step 6: Time Patterns

If enough data:
- Which days of week have sessions?
- Morning vs evening patterns?
- Session frequency trend (increasing, decreasing, steady?)

### Step 7: Present Summary

```markdown
## Pattern Scan: [Date Range]

**Sessions analysed:** N
**Date range:** [first] to [last]

### Where Attention Goes
[Top 3-5 topics and areas]

### What's Neglected
[Areas/topics with low or zero coverage]

### Energy Picture
[Overall trend and any correlations]

### Patterns Worth Naming
[Avoidance, recurring themes, observations]

### Questions to Sit With
- [Reflective question based on patterns]
- [Another if relevant]
```

## Interpretation Notes

Patterns aren't judgments. A "neglected" area might be:
- Appropriately deprioritised right now
- Something being avoided
- Simply stable and not needing attention

The value is making the implicit explicit. The user decides what it means.

## Integration

- **Weekly review**: Include pattern scan in the review
- **Monthly**: Deeper pattern analysis with more data
- **On request**: When something feels off and user wants perspective
