# Privacy Guard - Public Repository Protection

## Before ANY git commit

You should scan all staged files for sensitive personal information before committing, especially if this repository is public or may become public.

### Blocked Terms

Configure your blocked terms in `.claude/hooks/pre-commit-privacy.sh`. Common examples:

- Employer name / company
- Private venture or project names
- Family member names
- Personal location
- Salary/compensation figures
- Client names

### Before Committing

1. Run: `git diff --cached` to see what will be committed
2. Check for any blocked terms (case-insensitive)
3. If found: STOP and alert the user before proceeding
4. If clean: Proceed with commit

### Public vs Private Repos

**Public repos:**
- STRICT privacy enforcement
- Only reference public identity (blog, GitHub, LinkedIn if appropriate)
- No employer, family, ventures, or location

**Private repos:**
- Privacy rules can be relaxed
- Use `git commit --no-verify` to bypass the hook if needed

### If Sensitive Content is Accidentally Committed

If sensitive content is accidentally committed:
1. IMMEDIATELY alert the user
2. Do NOT push
3. Help amend/revert the commit
4. Scrub from git history if already pushed
