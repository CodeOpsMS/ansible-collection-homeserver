# Repository Configuration

This file documents the recommended repository settings for optimal CI/CD operation.

## Branch Protection Rules

### Main Branch Protection
- **Branch name pattern**: `main`
- **Require pull request reviews**: ✅
  - Required approving reviews: 1
  - Dismiss stale reviews: ✅
  - Require code owner reviews: ✅
- **Require status checks**: ✅
  - Require up-to-date branches: ✅
  - Status checks:
    - `lint`
    - `test`
    - `build`
- **Require conversation resolution**: ✅
- **Restrict pushes**: ✅
- **Allow force pushes**: ❌
- **Allow deletions**: ❌

### Develop Branch Protection
- **Branch name pattern**: `develop`
- **Require pull request reviews**: ✅
  - Required approving reviews: 1
- **Require status checks**: ✅
  - Status checks:
    - `lint-pr`
    - `test-pr`

## Secrets Required

### Repository Secrets
- `GALAXY_API_KEY`: Your Ansible Galaxy API key for publishing
- `GITHUB_TOKEN`: Automatically provided by GitHub

### Environment Secrets (Production)
- `GALAXY_API_KEY`: Production Galaxy API key

## GitHub Pages (Optional)
- **Source**: Deploy from a branch
- **Branch**: `gh-pages` (if you want to host documentation)

## Repository Settings
- **Issues**: ✅ Enabled
- **Wiki**: ❌ Disabled (use README.md instead)
- **Discussions**: ✅ Enabled (for community support)
- **Projects**: ✅ Enabled (for project management)

## Collaborators & Teams
- Assign appropriate roles to team members
- Use CODEOWNERS file for automatic review assignment

## Webhooks & Services
- Configure webhooks for external integrations if needed
- Consider integrating with Slack/Discord for notifications
