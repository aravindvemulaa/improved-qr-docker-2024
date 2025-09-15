#!/bin/bash

# Script to help users who tried "gh pr checkout 32"
# This script provides helpful information about available PRs

echo "================================================"
echo "🚨 PR #32 Not Found - Help & Alternative Options"
echo "================================================"
echo ""

echo "It looks like you tried to checkout PR #32, but it doesn't exist."
echo ""

echo "📋 Checking available PRs in this repository..."
echo ""

# Check if gh CLI is available
if command -v gh &> /dev/null; then
    echo "Available Pull Requests:"
    gh pr list --state all || echo "❌ Could not fetch PR list. Make sure you're authenticated with GitHub CLI."
else
    echo "❌ GitHub CLI (gh) is not installed."
    echo "💡 Install it from: https://cli.github.com/"
fi

echo ""
echo "📖 What you can do instead:"
echo "  1. Run 'gh pr list' to see available PRs"
echo "  2. Use 'gh pr checkout <NUMBER>' with an existing PR number"
echo "  3. Create a new PR with 'gh pr create'"
echo "  4. Read the GitHub CLI Guide: ./GITHUB_CLI_GUIDE.md"
echo ""

echo "🔗 Repository URL: https://github.com/aravindvemulaa/improved-qr-docker-2024"
echo ""

echo "💡 For more detailed instructions, see: GITHUB_CLI_GUIDE.md"
echo "================================================"