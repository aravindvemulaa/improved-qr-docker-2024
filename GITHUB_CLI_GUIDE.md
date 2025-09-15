# GitHub CLI Usage Guide for improved-qr-docker-2024

## Available Pull Requests

If you tried to run `gh pr checkout 32` and got an error, it's because PR #32 doesn't exist in this repository.

### Current Available PRs

To see available pull requests, use:
```bash
gh pr list
```

### Checking Out Available PRs

To checkout an existing pull request, use:
```bash
gh pr checkout <PR_NUMBER>
```

Where `<PR_NUMBER>` is one of the available PR numbers shown by `gh pr list`.

### Creating a New PR

If you need to create a new pull request:

1. Create a new branch:
```bash
git checkout -b feature/your-feature-name
```

2. Make your changes and commit them:
```bash
git add .
git commit -m "Your commit message"
```

3. Push the branch:
```bash
git push origin feature/your-feature-name
```

4. Create a pull request:
```bash
gh pr create --title "Your PR Title" --body "Description of your changes"
```

## Common GitHub CLI Commands for this Repository

### List PRs
```bash
gh pr list
```

### View PR details
```bash
gh pr view <PR_NUMBER>
```

### Checkout a PR
```bash
gh pr checkout <PR_NUMBER>
```

### Create a PR
```bash
gh pr create
```

### Merge a PR
```bash
gh pr merge <PR_NUMBER>
```

## Repository-Specific Workflow

This repository contains a QR Code generator application. Before working with PRs:

1. Test the application locally:
```bash
python main.py --url https://your-url.com
```

2. Test with Docker:
```bash
docker build -t qr-app .
docker run -v ./qr_codes:/app/qr_codes qr-app --url https://your-url.com
```

3. Ensure your changes don't break existing functionality.

## Error: "gh pr checkout 32" Failed?

If you got here because `gh pr checkout 32` failed, here's what to do:

1. Check available PRs: `gh pr list`
2. Use an existing PR number, or
3. Create a new PR if needed

This repository currently has PRs #1 and #2 available (as of the last update).