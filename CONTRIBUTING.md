# Contributing to ms.homeserver Ansible Collection

We love your input! We want to make contributing to this project as easy and transparent as possible.

## 🚀 Development Process

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/amazing-feature`
3. **Make** your changes
4. **Test** your changes locally: `make ci-local`
5. **Commit** your changes: `git commit -m 'Add amazing feature'`
6. **Push** to the branch: `git push origin feature/amazing-feature`
7. **Open** a Pull Request

## 📋 Pull Request Process

1. **Update** documentation if needed
2. **Add** tests for new functionality
3. **Ensure** all CI checks pass
4. **Follow** our coding standards
5. **Update** the version in `galaxy.yml` if needed

## 🧪 Testing

### Local Testing
```bash
# Install dependencies
make install-deps

# Run all tests
make ci-local

# Individual tests
make lint
make test
```

### CI/CD Testing
- All PRs automatically run through our CI pipeline
- Tests run on multiple Python and Ansible versions
- Security scanning with Trivy
- Code quality checks with ansible-lint and yamllint

## 📝 Coding Standards

### Ansible Best Practices
- Follow [Ansible best practices](https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html)
- Use descriptive task names in English
- Include proper error handling with `failed_when` and `ignore_errors`
- Use `check_mode` compatible tasks where possible

### Code Style
- **YAML**: Follow `.yamllint` configuration
- **Variables**: Use `snake_case` for variable names
- **Tasks**: Descriptive names, proper spacing
- **Comments**: Explain complex logic

### Documentation
- Update `README.md` for new features
- Add inline comments for complex tasks
- Update role documentation in `meta/main.yml`

## 🐛 Bug Reports

Use our [bug report template](.github/ISSUE_TEMPLATE/bug_report.md) and include:

- **Environment**: OS, Ansible version, Python version
- **Steps to reproduce**: Clear, step-by-step instructions
- **Expected behavior**: What you expected to happen
- **Actual behavior**: What actually happened
- **Logs**: Relevant error messages or logs

## 💡 Feature Requests

Use our [feature request template](.github/ISSUE_TEMPLATE/feature_request.md) and include:

- **Problem**: What problem does this solve?
- **Solution**: Describe your proposed solution
- **Alternatives**: Alternative solutions considered
- **Additional context**: Screenshots, examples, etc.

## 🔒 Security

See our [Security Policy](SECURITY.md) for reporting security vulnerabilities.

## 📄 License

By contributing, you agree that your contributions will be licensed under the same license as this project.

## 🎯 Areas for Contribution

We especially welcome contributions in these areas:

### 🖥️ Platform Support
- **Windows**: PowerShell-based system information gathering
- **macOS**: Enhanced macOS-specific information
- **BSD**: FreeBSD, OpenBSD support
- **Embedded**: Raspberry Pi, IoT device support

### 🔌 New Features
- **Hardware Info**: CPU, GPU, Memory details
- **Network Info**: Interface details, connectivity tests
- **Security Info**: Firewall status, security updates
- **Container Info**: Docker, Podman information

### 📚 Documentation
- **Examples**: Real-world usage examples
- **Tutorials**: Step-by-step guides
- **Videos**: Video tutorials or demos
- **Translations**: Documentation in other languages

### 🧪 Testing
- **Integration tests**: More comprehensive test scenarios
- **Performance tests**: Benchmarking and optimization
- **Edge cases**: Unusual system configurations
- **Mock environments**: Test environment improvements

## 🏆 Recognition

Contributors are recognized in:
- `README.md` contributors section
- Release notes for significant contributions
- GitHub contributors page

## 💬 Community

- **Discussions**: Use GitHub Discussions for questions
- **Issues**: Use GitHub Issues for bugs and features
- **Contact**: Reach out to maintainers for guidance

## 📋 Checklist for Contributors

Before submitting your PR, ensure:

- [ ] Code follows our style guidelines
- [ ] Self-review of code completed
- [ ] Tests added for new functionality
- [ ] Documentation updated
- [ ] Local CI pipeline passes (`make ci-local`)
- [ ] Commit messages are descriptive
- [ ] PR description clearly explains changes

Thank you for contributing! 🙏

---

*For questions about contributing, feel free to open a discussion or contact the maintainers.*
