---
description: Save external content (bookmarks, YouTube, Spotify, articles) with context
---

Capture external content into the appropriate resources/ subfolder.

Use the **capture** skill (`.claude/skills/capture/SKILL.md`) to:

1. Determine content type from `$ARGUMENTS`:
   - bookmark -> `resources/bookmarks/`
   - youtube -> `resources/youtube/`
   - spotify -> `resources/spotify/`
   - article -> `resources/articles/`

2. Gather: URL, why it matters, tags, notes

3. Create file with frontmatter and context

**Examples:**
```
/capture youtube https://youtube.com/... - great explanation of X
/capture bookmark https://... - reference for project
/capture article https://... - interesting analysis
```
