#!/usr/bin/env python3
"""
Session start hook for Arc.
Checks inbox for stale items and surfaces current focus.
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path

# Get repo root (parent of .claude)
REPO_ROOT = Path(__file__).parent.parent.parent
INBOX_DIR = REPO_ROOT / "inbox"
STATE_DIR = REPO_ROOT / "state"
FOCUS_FILE = STATE_DIR / "focus.md"
SESSION_CONTEXT_FILE = STATE_DIR / "session-context.json"


def check_inbox():
    """Check inbox for items, flag stale ones (>7 days)."""
    if not INBOX_DIR.exists():
        return None, []

    items = list(INBOX_DIR.iterdir())
    items = [f for f in items if f.is_file() and not f.name.startswith('.')]

    if not items:
        return 0, []

    stale_threshold = datetime.now() - timedelta(days=7)
    stale_items = []

    for item in items:
        mtime = datetime.fromtimestamp(item.stat().st_mtime)
        if mtime < stale_threshold:
            age_days = (datetime.now() - mtime).days
            stale_items.append((item.name, age_days))

    return len(items), stale_items


def get_last_session():
    """Get info about last session for continuity."""
    if not SESSION_CONTEXT_FILE.exists():
        return None

    try:
        with open(SESSION_CONTEXT_FILE) as f:
            data = json.load(f)
        return data
    except (json.JSONDecodeError, IOError):
        return None


def main():
    """Generate session start context."""
    output = []

    # Check inbox
    inbox_count, stale_items = check_inbox()

    if inbox_count is not None and inbox_count > 0:
        if stale_items:
            output.append(f"Inbox: {inbox_count} items ({len(stale_items)} stale)")
            for name, days in stale_items[:3]:  # Show top 3
                output.append(f"  - {name} ({days}d old)")
        else:
            output.append(f"Inbox: {inbox_count} items")

    # Check last session context
    last_session = get_last_session()
    if last_session and last_session.get("open_threads"):
        threads = last_session["open_threads"]
        if threads:
            output.append(f"Open threads: {', '.join(threads[:3])}")

    # Note: focus.md is read by the model directly via rules
    # This hook just surfaces quick status checks

    if output:
        print("\n".join(output))


if __name__ == "__main__":
    main()
