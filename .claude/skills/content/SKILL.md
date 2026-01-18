---
name: content
description: Write content for blog and social media. Use when the user asks to write a post, draft something, work on content, or mentions writing publicly.
allowed-tools: Read Write Edit Glob Bash(ls:*) WebFetch
---

# Content Writing

Help write content for blog and social media platforms.

## When to Use

- User asks to "write a post", "draft something", "write about X"
- Mentions blog, LinkedIn, or writing publicly
- Working on content for any platform
- Reviewing or editing existing drafts

## Execution Steps

### Step 1: Load context (if available)

Check for a content guide:
```
resources/content/CLAUDE.md
```

This may contain:
- Content strategy and pillars
- Voice and style guidance
- Platform-specific rules
- Examples of good posts

If no guide exists, ask the user about their content preferences.

### Step 2: Review recent posts for voice consistency

Check recent published posts (if they exist):
```bash
ls -t resources/content/_posts/ | head -5
```

Read 2-3 recent posts to calibrate voice.

### Step 3: Check planned content (if applicable)

If writing a scheduled post, check for calendars or planned content:
```
resources/content/content-calendar.md
resources/content/planned/
resources/content/series/
```

### Step 4: Draft the content

Follow any loaded guidance. General good practices:
- Be authentic - write in the user's voice, not generic AI voice
- Ground in actual experience where possible
- Keep it concise (platform-appropriate length)
- Avoid corporate speak and cliches
- Use the user's preferred locale/spelling

### Step 5: Self-check before presenting

Before showing the draft, verify:
1. Does it sound like something the user would actually say?
2. No corporate buzzwords or AI-sounding phrases
3. Appropriate length for the platform
4. Clear point or value to the reader

### Step 6: Save draft if requested

If user asks to save:

**Blog/social post:**
```
resources/content/drafts/YYYY-MM-DD-slug.md
```

With frontmatter:
```yaml
---
title: Post Title Here
status: draft
platform: [linkedin|blog|twitter|etc]
target_date: YYYY-MM-DD
theme: [philosophical|technical|leadership|personal|etc]
---
```

## Workflow Reminder

- **Long-form content** -> blog
- **Shorter intro** -> social platforms that channel traffic to blog
- Ask about AI disclosure preferences if not defined

## Key Files (if configured)

| File | Purpose |
|------|---------|
| `resources/content/CLAUDE.md` | Voice, strategy, style guide |
| `resources/content/content-calendar.md` | Schedule and ideas |
| `resources/content/_posts/` | Published content |
| `resources/content/drafts/` | Work in progress |
| `resources/content/planned/` | Future scheduled posts |
