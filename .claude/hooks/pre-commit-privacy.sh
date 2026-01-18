#!/bin/bash
# Pre-commit hook: Block sensitive personal information from public commits
# This hook prevents accidental exposure of private context in public repositories
#
# CUSTOMISATION: Add your sensitive terms to the SENSITIVE_TERMS array below.
# Run /setup to have Arc help you configure these.

set -e

# Sensitive terms that should NEVER appear in public commits
# Add your own terms here (employer, family names, private projects, location, etc.)
SENSITIVE_TERMS=(
    # "YourEmployerName"
    # "PrivateProjectName"
    # "FamilyMemberName"
    # "YourLocation"
)

# Exit early if no terms configured
if [ ${#SENSITIVE_TERMS[@]} -eq 0 ]; then
    exit 0
fi

# Get the list of staged files
STAGED_FILES=$(git diff --cached --name-only --diff-filter=ACM 2>/dev/null || echo "")

if [ -z "$STAGED_FILES" ]; then
    exit 0
fi

FOUND_ISSUES=0
ISSUES=""

for term in "${SENSITIVE_TERMS[@]}"; do
    # Search staged files for the term (case-insensitive)
    MATCHES=$(echo "$STAGED_FILES" | xargs grep -l -i "$term" 2>/dev/null || true)

    if [ -n "$MATCHES" ]; then
        FOUND_ISSUES=1
        ISSUES="$ISSUES\n  - '$term' found in: $MATCHES"
    fi
done

if [ $FOUND_ISSUES -eq 1 ]; then
    echo ""
    echo "=========================================="
    echo "BLOCKED: Sensitive information detected!"
    echo "=========================================="
    echo ""
    echo "The following private terms were found in staged files:"
    echo -e "$ISSUES"
    echo ""
    echo "These terms should NOT appear in public repositories."
    echo ""
    echo "Options:"
    echo "  1. Remove the sensitive content and re-stage"
    echo "  2. If this is a PRIVATE repo, use: git commit --no-verify"
    echo ""
    exit 1
fi

exit 0
