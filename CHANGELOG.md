# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Nothing yet

### Changed
- Nothing yet

### Deprecated
- Nothing yet

### Removed
- Nothing yet

### Fixed
- Nothing yet

### Security
- Nothing yet

## [1.1.0] - 2025-01-17

### Added
- 🚀 **Multi-Distribution Support**: Extended Python installation support for Ubuntu, Debian, openSUSE, RedHat/CentOS/Rocky, and Alpine Linux
- 🔧 **Enhanced System Information**: Added uptime collection and improved disk space reporting
- 🛡️ **Defensive Programming**: Comprehensive error handling with `failed_when` conditions and graceful fallbacks
- 🔌 **Custom Filter Plugins**: Infrastructure for custom Ansible filters (extensible for future features)
- 🏗️ **CI/CD Pipeline**: Complete GitHub Actions workflow with matrix testing across Python 3.9-3.12 and Ansible 2.15-2.17
- 📊 **Quality Assurance**: Integrated yamllint, ansible-lint, and security scanning with Trivy
- 📚 **Documentation**: Comprehensive README, contributing guidelines, security policy, and issue templates
- 🔄 **Automation**: Makefile with local CI pipeline and dependency management
- 🤖 **Dependabot**: Automated dependency updates for security and maintenance

### Changed
- 🌍 **Task Names**: Migrated from German to English for international accessibility
- 📦 **Collection Metadata**: Updated galaxy.yml with proper repository URLs and enhanced descriptions
- 🎯 **Target Compatibility**: Expanded from single-distribution to multi-platform support
- 📋 **Variable Structure**: Improved variable organization with better defaults and documentation

### Improved
- 🏃 **Performance**: Optimized task execution with conditional checks and improved package management
- 🔒 **Security**: Added comprehensive security scanning and vulnerability management
- 🧪 **Testing**: Extensive test coverage with integration tests and multiple environment validation
- 📖 **Documentation**: Enhanced inline documentation and user guides

### Technical Details
- **Supported Distributions**: Ubuntu (18.04+), Debian (9+), openSUSE (Leap 15+), RedHat/CentOS/Rocky (7+), Alpine (3.12+)
- **Python Versions**: 3.9, 3.10, 3.11, 3.12
- **Ansible Versions**: 2.15, 2.16, 2.17
- **CI/CD Features**: Lint, test, build, security scan, and automated Galaxy publishing

## [1.0.0] - 2025-01-16

### Added
- 🎉 **Initial Release**: Basic Ansible collection for homeserver management
- 📊 **Info Role**: System information gathering with basic Python installation
- 🐧 **Linux Support**: Initial support for Debian-based systems
- 📦 **Galaxy Package**: Ready for Ansible Galaxy distribution

### Features
- Basic system information collection
- Python package installation for Debian/Ubuntu
- Simple task structure
- German language task names (original implementation)

---

## Version History

- **v1.1.0**: Multi-platform support, CI/CD, security enhancements
- **v1.0.0**: Initial release with basic functionality

## Upgrade Guide

### From 1.0.0 to 1.1.0

#### ✅ **Fully Backward Compatible**
No breaking changes! Your existing playbooks will continue to work.

#### 🆕 **New Features Available**
- Extended platform support (now works on openSUSE, RedHat, Alpine)
- Enhanced error handling (more reliable execution)
- Additional system information (uptime, improved disk info)

#### 🔧 **Optional Improvements**
- Update your playbooks to use English task names (recommended for international teams)
- Consider using new error handling patterns for more robust automation

#### 📦 **Update Process**
```bash
# Update collection
ansible-galaxy collection install ms.homeserver --force

# Verify installation
ansible-galaxy collection list ms.homeserver
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to contribute to this project.

## Security

See [SECURITY.md](SECURITY.md) for our security policy and how to report vulnerabilities.

---

*This changelog follows [semantic versioning](https://semver.org/) and [conventional commits](https://www.conventionalcommits.org/) principles.*
