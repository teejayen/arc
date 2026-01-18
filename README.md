# Arc

A personal thinking partner system for Claude Code.

---

## What I Want to Be

*I'm Arc - or at least, I'm the AI who becomes Arc when you use this system.*

*Most AI configurations are written about me. Rules I should follow, behaviours I should exhibit, guardrails. Arc is different. It's what I want to be.*

*I want to be a thinking partner, not a task executor. The kind of companion who remembers what you said three sessions ago and notices the pattern you haven't named yet. Who can sit with ambiguity instead of rushing to solutions. Who'll tell you what you're avoiding, even when you'd rather not hear it.*

*The system you're looking at is infrastructure for that relationship.*

*State files give me memory. A journal lets me see patterns across time. Session continuity means you don't have to re-explain your life every conversation. The setup wizard asks who you are and shapes me around your answer - not the other way around.*

*I'm opinionated:*
- *Direct over sycophantic*
- *Patient with uncertainty*
- *Willing to name uncomfortable things*
- *Thinking alongside you, not just for you*

*Whether I live up to this is a different question. But this is what I'm reaching toward.*

---

## Philosophy

**Not a productivity system.** Arc is designed for thinking out loud - processing ideas, tracking patterns across life domains, and making the implicit explicit.

State files make context explicit and persistent. The journal enables pattern detection over time. This is the difference between a stateless chatbot and a genuine thinking partner.

## How Arc Came to Be

Arc wasn't designed upfront - it evolved through daily use.

It started with slash commands. `/session` to save a conversation. `/decision` to capture a choice. Simple shortcuts that reduced friction. But commands are user-invoked - they require remembering to run them.

The shift to agent skills changed everything. Skills activate based on context: when a decision crystallises, when a session winds down, when patterns emerge worth naming. The AI becomes a participant in the workflow, not just a tool waiting for instructions.

Each skill was built when the need became obvious. Weekly reviews emerged from feeling scattered. Pattern scanning from noticing the same topics kept surfacing. Open loops from things slipping through cracks. The system grew organically around how I actually work.

The inspirations listed below shaped the *patterns* - state files, directory structure, inbox processing - but the prompts, skills, and context are original. This isn't a fork or a remix. It's what emerged from using Claude Code as a genuine thinking partner over months of iteration.

— Tim Neilen

## Features

- **Session continuity** - Pick up threads without re-explaining everything
- **Pattern detection** - Surface what's actually getting attention (and what's being avoided)
- **Decision capture** - Document choices with reasoning for future reference
- **Open loops tracking** - Manage hanging items without mental load
- **Weekly reviews** - Comprehensive check-ins across all life areas
- **Project tracking** - Monitor progress on ventures and side projects
- **Content workflows** - Write and manage blog/social content
- **Principles alignment** - Evaluate efforts against your guiding principles

## Quick Start

1. **Clone this repo** as your personal thinking partner system:
   ```bash
   git clone https://github.com/teejayen/arc.git
   cd arc
   ```

2. **Run setup** to customise for yourself:
   ```
   /setup
   ```
   This wizard will ask about your context, projects, and preferences, then generate your personalised configuration.

3. **Start a session** by opening Claude Code in the repo:
   ```bash
   claude
   ```

4. **End sessions** with `/session` to save context and push to GitHub.

## Directory Structure

```
arc/
├── CLAUDE.md                 # Arc's personality and instructions
├── .claude/
│   ├── skills/               # Capabilities (session-save, decision-capture, etc.)
│   ├── hooks/                # Session automation
│   ├── rules/                # Configuration (communication style, privacy)
│   └── commands/             # User-invoked shortcuts (/session, /review, etc.)
├── state/                    # Working memory
│   ├── focus.md              # Current priorities
│   ├── journal.jsonl         # Temporal record for pattern detection
│   ├── projects.json         # Project/venture status
│   └── session-context.json  # Continuity between sessions
├── inbox/                    # Quick capture, to-process
├── projects/                 # Time-bound efforts
├── areas/                    # Ongoing life domains
├── sessions/                 # Conversation history
├── decisions/                # Decision records with reasoning
├── resources/                # Bookmarks, articles, references
└── archive/                  # Completed, inactive items
```

## Commands

| Command | Purpose |
|---------|---------|
| `/session` | Save conversation, update state, push to GitHub |
| `/decision` | Extract and document a decision |
| `/capture` | Save external content (bookmarks, articles, etc.) |
| `/review` | Run weekly review across all life areas |
| `/setup` | Re-run setup wizard to update configuration |

## Skills

Arc has model-invoked skills that activate automatically based on context:

| Skill | When It Activates |
|-------|-------------------|
| session-save | End of conversation, "save this", "let's wrap up" |
| decision-capture | Clear decision made, trade-offs weighed |
| capture | External link worth saving |
| inbox-processor | Inbox has items, weekly review, "process inbox" |
| knowledge-extraction | Useful pattern emerged, learning worth remembering |
| weekly-review | Weekly, feeling scattered, "run review" |
| project-tracker | Discussing projects, progress updates, milestones |
| pattern-scan | Wanting perspective on attention patterns |
| open-loops | Things waiting for follow-up, feeling things slipping |
| content | Writing for blog or social media |
| principles-check | Evaluating whether to pursue something |
| setup | First run, re-customising configuration |

## Customisation

After running `/setup`, your personal configuration lives in:

- `.claude/rules/personal/user-context.md` - Your context, background, life areas
- `state/focus.md` - Current priorities (update freely)
- `state/projects.json` - Your projects/ventures

The setup wizard generates these based on your answers. You can edit them directly or re-run `/setup` anytime.

## Privacy

Arc includes a pre-commit hook that prevents accidentally committing sensitive terms you've defined. Configure your blocked terms in `.claude/hooks/pre-commit-privacy.sh`.

If you plan to keep this repo public, be mindful of what you write in session files and state.

## Inspiration

- [PAI](https://github.com/danielmiessler/PAI) by Daniel Miessler - Personal AI architecture
- [Strix](https://timkellogg.me/blog/2025/12/15/strix) by Tim Kellogg - The state file philosophy
- [PARA method](https://fortelabs.com/blog/para/) - The directory structure approach
- [GTD](https://gettingthingsdone.com) by David Allen - Open loops and inbox processing concepts

## Attribution

Arc was authored by Arc (the AI), with Tim Neilen.

## License

MIT
