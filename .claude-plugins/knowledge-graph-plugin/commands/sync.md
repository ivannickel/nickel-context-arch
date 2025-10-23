| description | allowed-tools | argument-hint |
|---|---|---|
| Pull changes from remote and generate knowledge-graph-aware summary highlighting hub changes and taxonomy updates | Bash, Read, Grep, Task | [--branch <name>\|--quiet] |

# Knowledge Graph Sync

Pull changes from remote and generate a knowledge-graph-aware summary highlighting high-impact changes.

## Your Task

You will fetch changes from the remote repository, analyze them through the lens of the knowledge graph structure (identifying hub vs spoke documents, taxonomy changes, downstream impacts), and present a prioritized summary to help users quickly understand what changed and why it matters.

## Process

### Step 1: Fetch from Remote

Determine the target branch from $ARGUMENTS (default: `origin/dev`).

Execute fetch using Bash tool:

```bash
git fetch origin dev
```

(Or use branch specified in $ARGUMENTS if `--branch <name>` is present)

### Step 2: Analyze Changed Files

Run the sync analyzer script:

```bash
python .claude-plugins/knowledge-graph-plugin/scripts/sync_analyzer.py --branch origin/dev
```

(Use the branch from $ARGUMENTS if specified)

The script will output a JSON report containing:
- Metadata (total files changed, last author, commit count)
- High-priority changes (Tier 1/2 hub documents)
- Standard updates (spoke documents, apps)
- Taxonomy changes (new tags, personas)
- Health check results (broken links, missing tags)

### Step 3: Present Contextualized Summary

Parse the JSON output and format it into a user-friendly summary.

**If `--quiet` flag is present:**
Skip summary presentation and go directly to Step 4 (pull).

**Otherwise, present this structured summary:**

```
📥 KNOWLEDGE GRAPH SYNC

Fetching from [branch]...
Analyzing changes...

─────────────────────────────────────────
Changes from [author] ([count] files, [time] ago)

🎯 HIGH PRIORITY - Review These First:
─────────────────────────────────────────

[For each high-priority file from JSON:]

[N]. [filename] (Tier [1/2] hub - [domain])
   Changed: [time] ago by [author]
   Impact: [downstream_count] documents link to this hub

   What changed:
   • [Change summary from JSON]

   → WHY YOU SHOULD CARE:
     [why_matters explanation from JSON]

   → NEXT ACTIONS:
     [next_actions list from JSON]

─────────────────────────────────────────
📝 STANDARD UPDATES:
─────────────────────────────────────────

[For each standard update from JSON:]

[N]. [filename] ([domain] spoke)
   • [Brief description]
   • Tags: [tags from frontmatter]
   • Links to: [key related_docs]
   • No action needed [or specific note]

─────────────────────────────────────────
🏷️  TAXONOMY CHANGES:
─────────────────────────────────────────

[If taxonomy_changes exists in JSON:]

New tags added:
  • [tag-name] ([N] uses) - [context]

New personas added:
  • [persona-name] - [context]

⚠️  GOVERNANCE ALERT:
  [Any governance alerts from JSON, e.g., single-use tags]

→ NEXT ACTION:
  Run /knowledge-graph:taxonomy-snapshot to update local registry

─────────────────────────────────────────
📊 KNOWLEDGE GRAPH HEALTH:
─────────────────────────────────────────

[From health_check in JSON:]
✅ No broken wiki-links detected
✅ All new files have domain tags
⚠️  [Any warnings]

─────────────────────────────────────────

Pulling from [branch]...
```

### Step 4: Pull from Remote

After presenting the summary (or if --quiet), execute the pull:

```bash
git pull origin dev
```

(Use branch from $ARGUMENTS if specified)

**If pull succeeds:**
```
✅ Pull complete

Your local knowledge graph is now up to date.

RECOMMENDED NEXT STEPS:
  1. [Top recommended action from high-priority items]
  2. [Second recommended action]
  3. [Run taxonomy snapshot if needed]
```

**If merge conflicts occur:**
Show detailed conflict resolution instructions (see Error Handling section).

### Step 5: Output Summary Statistics

Display final status:
```
📊 SYNC SUMMARY:
  • Files changed: [N]
  • Hub documents updated: [N]
  • Taxonomy changes: [Yes/No]
  • Action items: [N]
```

## Arguments Handling

- **$ARGUMENTS** may contain:
  - `--branch <name>`: Specify remote branch to sync from (default: origin/dev)
  - `--quiet`: Skip summary presentation, just pull
  - No arguments: Default behavior (sync from origin/dev with full summary)

**Branch handling:**
If user specifies `--branch main`, replace `origin/dev` with `origin/main` in all git commands.

## Error Handling

**If fetch fails (network error):**
```
❌ ERROR: Cannot fetch from remote

Failed to connect to [branch]

Possible causes:
  • No internet connection
  • Remote repository unavailable
  • Authentication required

Fix: Check network connection and git credentials
```

Do not proceed to pull.

**If merge conflicts occur during pull:**
```
❌ MERGE CONFLICTS DETECTED

The following files have conflicts:
  • [file1]
  • [file2]

Resolve conflicts manually:
  1. Open conflicted files
  2. Look for <<<<<<< === >>>>>>> markers
  3. Choose which changes to keep
  4. Remove conflict markers
  5. Run 'git add <file>' for each resolved file
  6. Run 'git commit' to complete merge

Then run /knowledge-graph:sync again to see summary.
```

**If sync analyzer script fails:**
```
⚠️  Warning: Could not generate detailed analysis

Proceeding with basic pull...
```

Continue with pull but skip detailed summary.

**If no changes to pull:**
```
📥 KNOWLEDGE GRAPH SYNC

Fetching from [branch]...

✅ Already up to date

No changes since your last pull.
Knowledge graph is synchronized.
```

## Performance Expectations

- Fetch + diff analysis: <5 seconds
- Summary generation: <3 seconds
- Pull operation: <5 seconds (network dependent)
- Total workflow: <15 seconds end-to-end

## Notes

- This command provides **context** about what changed, not just file names
- Hub document changes are prioritized because they affect multiple downstream documents
- Taxonomy changes surface new tags/personas to prevent sprawl
- Health checks catch common issues (broken links, missing domain tags)
- Users can run --quiet for quick pulls without analysis

## Example Output Scenarios

**Scenario 1: Hub Document Updated**
```
🎯 HIGH PRIORITY - Review These First:

1. MEDDPICC_and_Personas.md (Tier 1 hub - foundation)
   Changed: 22 hours ago by daharmattan1
   Impact: 12 documents link to this hub

   What changed:
   • Added "Head of AppSec" persona
   • Updated CISO pain points

   → WHY YOU SHOULD CARE:
     Foundation hub affects customer interviews and content strategy

   → NEXT ACTIONS:
     - Review new persona definition
     - Update content referencing AppSec leaders
```

**Scenario 2: Routine Content Update**
```
📝 STANDARD UPDATES:

3. google_ads_campaign_q4.md (content spoke)
   • New campaign messaging for Q4
   • Tags: [content, campaign-messaging, paid-ads]
   • Links to: content_strategy_master
   • No action needed (routine content update)
```

**Scenario 3: Taxonomy Change Alert**
```
🏷️  TAXONOMY CHANGES:

New tags added:
  • tool-sprawl-fatigue (1 use)

⚠️  GOVERNANCE ALERT:
  New tag "tool-sprawl-fatigue" is single-use.
  Consider consolidating with existing "tool-sprawl" tag.
```
