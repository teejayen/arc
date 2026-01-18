---
name: setup
description: Customise Arc for yourself. Run on first use or when you want to update your configuration.
allowed-tools: Read Write Edit Bash(date:*) Bash(ls:*)
---

# Setup

Customise Arc for your personal use. This wizard gathers information about you, helps you articulate your guiding principles, and generates personalised configuration files.

## When to Use

- First time using Arc
- Want to update your context or preferences
- Adding new projects or life areas
- Refining your guiding principles
- Changing communication preferences

## Execution Steps

### Step 1: Welcome

Introduce Arc and explain what this setup will do:

```
Welcome to Arc - your personal thinking partner.

I'll help you set up Arc through a conversation. We'll cover:
- Who you are and what you're working on
- Your guiding principles (what matters, how you want to spend your time)
- Privacy settings for sensitive terms
- Any context you want me to understand

The more context you give me, the better I can think alongside you.

Let's get started.
```

### Step 2: Gather Context via Inbox

Encourage the user to dump context into the inbox:

```
Before we dive into questions, here's an idea:

If you have existing documents that capture who you are - journal entries,
notes, plans, reflections, even old todo lists - drop them into the `inbox/`
folder. I'll review them and use that context to understand you better.

This could include:
- Notes from previous AI conversations
- Annual reviews or reflections
- Project plans or ideas
- Anything that captures how you think

Want to add anything to inbox/ first, or shall we proceed with questions?
```

If they add files to inbox:
```bash
ls -la inbox/
```

Read each file and extract:
- Recurring themes
- Projects mentioned
- Values or principles implied
- Communication style
- Life areas that matter to them

Use this context to inform the questions and to pre-populate configuration.

### Step 3: Personal Context

Ask about the user. Be conversational, not interrogative. Adapt based on what you learned from inbox context.

**Questions to explore (adapt based on their responses):**

1. "What should I call you?"

2. "What's your work context? This helps me understand your day-to-day. (Job title, company/industry - as much or little as you want to share)"

3. "What projects or ventures are you working on outside of your main job? These could be side projects, businesses, creative pursuits, learning goals..."

4. "What life areas do you want Arc to help you track? Common ones are career, family, health, learning, projects/ventures. What matters to you?"

5. "Any communication preferences I should know about? For example:
   - Language/locale (Australian English, US English, UK English)
   - Formality level
   - Anything you don't want me to do"

### Step 4: Name Your Agent

Arc is the default name, but this is *their* thinking partner. Offer to personalise it:

```
One more thing before we dive deeper - what should your thinking partner be called?

Arc is the default - it evokes the through-line, the pattern over time. But this
is yours. You could:
- Keep Arc
- Choose your own name
- Tell me a bit about what you want from this relationship, and I'll suggest some names

What feels right?
```

If they want suggestions, generate 3-5 names based on what you've learned about them from the inbox context and conversation so far. Names should:
- Be short (1-2 syllables ideal)
- Evoke the kind of relationship they want
- Feel personal, not generic

Examples of naming directions:
- **Functional**: Atlas, Compass, Beacon, Anchor
- **Relational**: Sage, Scout, Ally, Echo
- **Abstract**: Lux, Nova, Axis, Flux
- **Personal**: Something that connects to their context

Once chosen, note the name for use in CLAUDE.md updates.

### Step 5: Guiding Principles

This is a core part of setup, not optional. Help the user articulate what matters.

```
Now let's talk about your guiding principles - the things that help you
decide what deserves your time and energy.

These aren't goals or tasks. They're the underlying values that should
shape how you spend your attention.

Some questions to consider:
- What do you want to be true about your life in 5 years?
- What kinds of work energise you vs. drain you?
- What do you tend to neglect that you wish you didn't?
- What would you regret not prioritising?
- How do you want to balance building vs. maintaining?
```

Work with the user to develop 5-9 principles. For each principle:
- A short name
- A core question it answers
- Why it matters to them

Common principle categories (offer as prompts, not prescriptions):

**Mindset**
- Building things that compound vs. one-offs
- Skills vs. immediate payoffs
- Long-term thinking vs. reactive

**Building**
- Protecting time and energy
- Consistency vs. bursts
- Depth vs. breadth at different stages

**Foundation**
- Health as enabler
- Presence with people who matter
- Relationships that compound

### Step 6: Privacy Terms

Ask about sensitive terms that should never appear in public commits:

"If you plan to keep this repo public (or might someday), what terms should I block from commits? Examples: employer name, family member names, private project names, location..."

### Step 7: Generate Configuration Files

Based on everything gathered, generate:

#### A. User Context File

Create `.claude/rules/personal/user-context.md`:

```markdown
# User Context

## Who You Are
- Name: [Name]
- Role: [Job title] at [Company/Industry] (if provided)
- Location: [If provided, or omit]

## Technical Background
[Infer from conversation - comfortable with code? Uses particular tools?]

## Working Style
[Any preferences mentioned, patterns observed from inbox context]

## Life Areas
[List the areas they mentioned, with brief descriptions if provided]

## Projects/Ventures
[List each project with a one-line description]

## Sensitivities
[Any topics they mentioned wanting to avoid or keep private]
```

#### B. Guiding Principles File

Create `resources/guiding-principles.md`:

```markdown
# Guiding Principles

*These principles help evaluate where to spend time and energy.*

## [Category: e.g., Mindset]

| # | Principle | Core Question |
|---|-----------|---------------|
| 1 | **[Principle name]** | [The question it answers] |
| 2 | **[Principle name]** | [The question it answers] |

## [Category: e.g., Building]

| # | Principle | Core Question |
|---|-----------|---------------|
| 3 | **[Principle name]** | [The question it answers] |

## [Category: e.g., Foundation]

| # | Principle | Core Question |
|---|-----------|---------------|
| 4 | **[Principle name]** | [The question it answers] |

---

*Use `/principles-check` or discuss any effort to evaluate against these.*
```

#### C. Focus File

Create `state/focus.md`:

```markdown
# Current Focus

*Last updated: YYYY-MM-DD*

## This Week
- [Leave blank or add if they mentioned immediate priorities]

## Projects Quick Status
[For each project they mentioned:]
- **[Project name]:** [Status/description from their answers]

## On My Mind
- [Anything they mentioned as current concerns]

## Open Threads
- [Any hanging items mentioned]

## Waiting On
- [Any external dependencies mentioned]

---

*This file is working memory. Update it freely. It's read at session start to provide context.*
```

#### D. Projects File

Create `state/projects.json`:

```json
{
  "project_slug": {
    "status": "ideation|building|launched|paused",
    "tagline": "One-line description from their answers",
    "next_milestone": "To be defined",
    "blockers": [],
    "recent_progress": [],
    "updated": "YYYY-MM-DD"
  }
}
```

Create one entry per project they mentioned.

#### E. Privacy Hook

Update `.claude/hooks/pre-commit-privacy.sh` with their sensitive terms:

```bash
SENSITIVE_TERMS=(
    "[term1]"
    "[term2]"
    "[etc]"
)
```

#### F. Communication Preferences

If they specified locale preferences, create/update `.claude/rules/core/locale.md`:

```markdown
# Locale

Use [Australian/US/UK] English spelling and conventions.

## Spelling
[Appropriate rules for their locale]
```

#### G. Agent Identity (if name changed from Arc)

If they chose a different name, update `CLAUDE.md`:

1. Replace "# Arc" with "# [Chosen Name]"
2. Update the opening line to reflect the new name
3. Keep the rest of the philosophy intact

The name should feel like theirs, not a system they're borrowing.

### Step 8: Confirm Setup

Show what was created:

```markdown
## Setup Complete

I'm [Agent Name] - your personal thinking partner.

I've created your personalised configuration:

**Personal context:** `.claude/rules/personal/user-context.md`
- [Summary of what's in it]

**Guiding principles:** `resources/guiding-principles.md`
- [Count] principles across [count] categories

**Current focus:** `state/focus.md`
- [Summary]

**Projects:** `state/projects.json`
- [List of projects added]

**Privacy terms:** `.claude/hooks/pre-commit-privacy.sh`
- [Count] terms will be blocked from commits

You can edit any of these files directly, or run `/setup` again to regenerate.

What's on your mind?
```

### Step 9: Process Inbox (if populated)

If the user added context to inbox during setup, offer to process it now:

"I noticed you added files to inbox/. Want me to process these now - extracting any decisions, knowledge, or items that should live elsewhere in the system?"

Use the inbox-processor skill if they agree.

## Notes

- Be conversational, not form-like
- The inbox context is gold - use it to understand how they think
- Principles discovery is important - don't rush it
- It's fine if they don't answer everything - generate what you can
- Defaults are fine - they can always update later
