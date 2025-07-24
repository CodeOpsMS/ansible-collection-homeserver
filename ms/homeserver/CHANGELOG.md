# Changelog

All notable changes to this Ansible Collection will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2025-01-24

### Added
- Extended distribution support (RedHat/CentOS/Rocky, Alpine Linux)
- Custom filter plugins for better data formatting
- Comprehensive system information (uptime, disk space, FQDN, SELinux)
- Integration test suite
- Ansible-lint configuration
- Development Makefile for automation
- Handlers for system operations
- Extended configuration variables
- Professional documentation with badges

### Changed
- Improved Python installation logic with conditional execution
- Enhanced error handling with defensive programming
- Better task names (English instead of German)
- More robust network information gathering
- Extended system summary with additional details

### Fixed
- Ansible-lint compliance
- YAML syntax and formatting
- Missing safety checks for undefined variables
- Collection metadata and runtime configuration

### Security
- Added pipefail option for shell commands
- Improved input validation

## [1.0.0] - 2025-01-24

### Added
- Initial release
- Basic system information role
- Python auto-installation for Debian/Ubuntu and openSUSE
- System summary with hardware and OS details
- Configurable display options
- Tag-based execution control
