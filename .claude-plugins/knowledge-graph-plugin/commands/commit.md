| description | allowed-tools | argument-hint |
|---|---|---|
| Validate knowledge graph frontmatter and commit changes with user control over fixes | Bash, Read, Edit, Task | [--strict\|--skip-validation] |

# Knowledge Graph Commit

Validate knowledge graph frontmatter integrity before committing changes.

## Your Task

You will validate all changed markdown files in the knowledge graph against frontmatter standards, offer to fix any issues, and then proceed with the git commit workflow.

## Process

### Step 1: Run Validation Script

Execute the validation script using the Bash tool:

```bash
python .claude-plugins/knowledge-graph-plugin/scripts/validate_commit.py $ARGUMENTS
```

The script will output a JSON report with validation results including:
- Summary statistics (total files, errors, warnings)
- Per-file issues with severity levels
- Suggested fixes for each issue
- Whether issues can be auto-fixed

### Step 2: Interpret and Present Results

Parse the JSON output from the validation script. For each file:

**If the file is valid:**
- Display: `✅ [filename] - Valid`

**If the file has errors:**
- Display: `❌ [filename] - [N] issues`
- For each issue, present:
  - **What's wrong:** The issue message from the JSON
  - **Why it matters:** The explanation field
  - **How to fix:** The suggested fix from the JSON

**If the file has warnings:**
- Display: `⚠️  [filename] - [N] warnings`
- Present same format as errors

### Step 3: Determine Fix Strategy

Look at the `can_auto_fix` field in the JSON report.

**If can_auto_fix is true:**

Present the user with these options:

```
OPTIONS:
  1. Apply fixes automatically and commit
  2. Commit without fixes (not recommended - may break knowledge graph)
  3. Cancel and fix manually

What would you like to do? [1/2/3]
```

**If can_auto_fix is false:**

Some issues require manual intervention. Present:

```
⚠️  Some issues cannot be auto-fixed and require manual intervention.

OPTIONS:
  1. Cancel and fix manually
  2. Commit anyway (not recommended)

What would you like to do? [1/2]
```

### Step 4: Execute User's Choice

**If user chooses "Apply fixes automatically" (Option 1):**

1. Run the fix script:
   ```bash
   python .claude-plugins/knowledge-graph-plugin/scripts/fix_frontmatter.py --apply
   ```

2. The script will modify files and output a summary. Display this to the user.

3. Re-run validation to confirm fixes worked:
   ```bash
   python .claude-plugins/knowledge-graph-plugin/scripts/validate_commit.py
   ```

4. If validation now passes, display: `✅ All files now valid`

5. Proceed to commit (Step 5)

**If user chooses "Commit without fixes" (Option 2):**

Display warning:
```
⚠️  Committing with validation issues...

Note: Knowledge graph may have integrity issues.
Recommend running /knowledge-graph:validate-frontmatter on affected files later.
```

Proceed to commit (Step 5)

**If user chooses "Cancel" (Option 3 or 1 for manual-only):**

Display:
```
Commit cancelled. Fix issues manually and run /knowledge-graph:commit again.

To fix manually:
- Review the issues listed above
- Edit the affected files
- Run /knowledge-graph:commit when ready
```

Exit without committing.

### Step 5: Proceed to Git Commit

Once validation passes (or user chose to proceed anyway), you should now delegate to Claude Code's standard git commit workflow.

Display:
```
📤 KNOWLEDGE GRAPH COMMIT

All validation checks complete. Proceeding with commit...
```

Then follow the standard commit workflow:
1. Run `git status` to see changed files
2. Run `git diff` to see changes
3. Stage relevant files
4. Create commit with appropriate message
5. Ask user if they want to push

## Arguments Handling

- **$ARGUMENTS** may contain:
  - `--strict`: Pass this flag to the validation script. Treats warnings as errors.
  - `--skip-validation`: Skip validation entirely and go straight to commit
  - No arguments: Default behavior (warn and offer fixes)

**If `--skip-validation` is present:**
Skip Steps 1-4 and go directly to Step 5 (git commit).

## Error Handling

**If validation script fails to execute:**
```
❌ ERROR: Validation script failed to execute

[Error message from script]

Possible fixes:
- Ensure Python 3 is installed: python --version
- Check script exists at: .claude-plugins/knowledge-graph-plugin/scripts/validate_commit.py

Cannot proceed to commit without validation.
```

**If fix script fails:**
```
❌ ERROR: Failed to apply fixes

[Error message from script]

Recommend:
1. Fix issues manually
2. Run /knowledge-graph:commit again
```

Do not proceed to commit.

## Performance Expectations

- Validation should complete in <5 seconds for typical commits (10 files)
- Fixing should complete in <3 seconds
- Total workflow: <10 seconds before proceeding to commit

## Notes

- This command integrates with Claude Code's built-in git workflow
- The validation script outputs structured JSON for programmatic parsing
- All frontmatter fixes preserve existing file structure
- Users maintain full control over whether fixes are applied
