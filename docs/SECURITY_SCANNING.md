# Security Scanning Setup

This document explains how the security scanning is configured in this repository.

## 🔍 Trivy Security Scanner

We use [Trivy](https://trivy.dev/) to scan for vulnerabilities in our codebase and dependencies.

### How it works

1. **Scan Execution**: Trivy scans the `./ms/homeserver` directory for:
   - Known vulnerabilities in dependencies
   - Misconfigurations
   - Secrets and sensitive information
   - License issues

2. **SARIF Output**: Results are generated in SARIF format (`trivy-results.sarif`)

3. **Integration with GitHub Security**: 
   - For **main branch pushes**: Results are uploaded to GitHub Security tab
   - For **pull requests**: Results are stored as artifacts (due to GitHub security restrictions)

## 🔒 GitHub Security Integration

### Permissions Required

The workflow needs specific permissions to upload security scan results:

```yaml
permissions:
  contents: read
  security-events: write  # Required for SARIF upload
  actions: read
```

### Why PRs from Forks Can't Upload SARIF

GitHub restricts `security-events: write` permission for pull requests from forks to prevent security exploits. This is why we:

- **Main branch**: Upload SARIF directly to Security tab
- **Pull requests**: Store SARIF as downloadable artifacts

## 📊 Viewing Security Results

### GitHub Security Tab

1. Go to your repository on GitHub
2. Click on the **Security** tab
3. Select **Code scanning** to see Trivy results

### For Pull Requests

1. Go to the **Actions** tab
2. Find your PR's workflow run
3. Download the `trivy-sarif-results` artifact
4. Use any SARIF viewer to analyze results

## 🛠️ Local Security Scanning

Run security scans locally during development:

```bash
# Install Trivy
brew install trivy  # macOS
# or
curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh -s -- -b /usr/local/bin

# Scan the collection
cd ms/homeserver
trivy fs .

# Generate SARIF report
trivy fs --format sarif --output trivy-results.sarif .
```

## 🔧 Configuration

### Trivy Configuration

Create `.trivyignore` file to ignore false positives:

```bash
# Example .trivyignore
CVE-2021-12345  # False positive, not applicable
```

### CI/CD Configuration

The security scan is configured in `.github/workflows/ci.yml`:

```yaml
security-scan:
  name: Security Scan
  runs-on: ubuntu-latest
  permissions:
    contents: read
    security-events: write
  steps:
    - uses: actions/checkout@v4
    - uses: aquasecurity/trivy-action@master
      with:
        scan-type: 'fs'
        scan-ref: './ms/homeserver'
        format: 'sarif'
        output: 'trivy-results.sarif'
    - uses: github/codeql-action/upload-sarif@v3
      if: always() && github.event_name != 'pull_request'
      with:
        sarif_file: 'trivy-results.sarif'
```

## 🚨 Common Issues

### "Resource not accessible by integration"

This error occurs when:
- Running on a fork's pull request
- Missing `security-events: write` permission
- Repository security settings restrict code scanning

**Solution**: The workflow automatically handles this by uploading artifacts for PRs.

### SARIF Upload Failures

If SARIF upload fails:
1. Check repository permissions
2. Verify the SARIF file is valid
3. Ensure you're not running on a fork's PR

## 📚 Additional Resources

- [GitHub Code Scanning Documentation](https://docs.github.com/en/code-security/code-scanning)
- [SARIF Support](https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/sarif-support-for-code-scanning)
- [Trivy Documentation](https://aquasecurity.github.io/trivy/)
- [Security Best Practices](SECURITY.md)

---

*For questions about security scanning, please open an issue or discussion.*
