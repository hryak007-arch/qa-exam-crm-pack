# Suggested repository cleanup

This file is not required for the final repository, but it can help document the cleanup work done for the lab.

## Recommended actions
1. Add `.gitignore`
2. Add `LICENSE`
3. Remove generated folders like `htmlcov/`
4. Keep only source code and project documentation
5. Make one clear cleanup commit, for example:
   `Chore: clean repository structure and add base repo files`

## Example commands
```bash
git rm -r --cached htmlcov
git add .gitignore LICENSE .env.example CONTRIBUTING.md SECURITY.md
git commit -m "Chore: clean repository structure and add base repo files"
```
