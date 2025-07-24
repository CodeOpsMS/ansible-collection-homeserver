# 🏠 ms.homeserver Ansible Collection

[![CI](https://github.com/codeopsms/ansible-collection-homeserver/workflows/CI/badge.svg)](https://github.com/codeopsms/ansible-collection-homeserver/actions)
[![Security](https://github.com/codeopsms/ansible-collection-homeserver/workflows/Security/badge.svg)](https://github.com/codeopsms/ansible-collection-homeserver/security)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-ms.homeserver-blue.svg)](https://galaxy.ansible.com/ms/homeserver)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive Ansible Collection for homeserver management, system information gathering, and automation across multiple Linux distributions.

## 🚀 Features

- **🖥️ System Information**: Comprehensive system data collection including hardware, OS, networking, and performance metrics
- **🐧 Multi-Platform**: Support for Ubuntu, Debian, openSUSE, RedHat/CentOS/Rocky, and Alpine Linux
- **🛡️ Robust**: Defensive programming with comprehensive error handling and graceful fallbacks
- **🔒 Secure**: No hardcoded credentials, minimal privileges, regular security scanning
- **🧪 Tested**: Extensive CI/CD with matrix testing across Python 3.9-3.12 and Ansible 2.15-2.17 (Python 3.10+ required for Ansible 2.16+)
- **📚 Documented**: Comprehensive documentation and examples

## 📦 Installation

### From Ansible Galaxy
```bash
ansible-galaxy collection install ms.homeserver
```

### From Git Repository
```bash
ansible-galaxy collection install git+https://github.com/codeopsms/ansible-collection-homeserver.git
```

### From Local Build
```bash
git clone https://github.com/codeopsms/ansible-collection-homeserver.git
cd ansible-collection-homeserver
ansible-galaxy collection build
ansible-galaxy collection install ms-homeserver-*.tar.gz
```

## 🏗️ Roles

### 📊 info
Collects comprehensive system information from your homeserver with automatic Python environment setup.

#### ✨ What it does:
- 🐍 **Auto-installs Python** on systems that need it (across all supported distributions)
- 📈 **Gathers system metrics**: CPU, memory, disk usage, uptime
- 🌐 **Network information**: Interfaces, connectivity status
- 💾 **Storage details**: Disk space, mount points, filesystem types
- 🔧 **OS information**: Distribution, version, kernel details

#### 🎯 Example Playbooks

**Basic Usage:**
```yaml
---
- name: Gather homeserver information
  hosts: homeserver
  become: yes
  roles:
    - ms.homeserver.info
```

**Advanced Usage with Custom Variables:**
```yaml
---
- name: Comprehensive homeserver audit
  hosts: homeserver
  become: yes
  vars:
    gather_extended_info: true
    install_python_packages: true
  roles:
    - ms.homeserver.info
  post_tasks:
    - name: Display collected information
      debug:
        var: ansible_facts
```

**Multiple Hosts with Groups:**
```yaml
---
- name: Audit all homeservers
  hosts: homeservers
  become: yes
  serial: 2  # Process 2 hosts at a time
  roles:
    - ms.homeserver.info
  
  post_tasks:
    - name: Generate system report
      template:
        src: system_report.j2
        dest: "/tmp/{{ inventory_hostname }}_report.txt"
      delegate_to: localhost
```

## 🖥️ Supported Platforms

| Platform | Versions | Status | Notes |
|----------|----------|--------|-------|
| 🐧 **Ubuntu** | 18.04, 20.04, 22.04, 24.04 | ✅ Fully Supported | Primary development platform |
| 🌊 **Debian** | 9, 10, 11, 12 | ✅ Fully Supported | Extensive testing |
| 🦎 **openSUSE** | Leap 15.2+ | ✅ Fully Supported | Zypper package management |
| 🎩 **RedHat/CentOS** | 7, 8, 9 | ✅ Fully Supported | RHEL, CentOS, Rocky Linux |
| 🏔️ **Alpine** | 3.12+ | ✅ Fully Supported | Minimal, security-focused |

## 🔧 Requirements

### Ansible Environment
- **Ansible**: >= 2.15 (tested up to 2.17)
- **Python**: >= 3.9 for Ansible 2.15, >= 3.10 for Ansible 2.16+
- **Collections**: 
  - `ansible.posix`
  - `community.general`

### Target Systems
- **OS**: Any supported Linux distribution
- **Python**: 3.6+ (automatically installed if missing)
- **Privileges**: `sudo` access for system information gathering
- **Network**: Internet access for package installation (if needed)

## ⚙️ Configuration

### Role Variables

```yaml
# Python installation settings
install_python_if_missing: true        # Auto-install Python if not found
python_package_names: []               # Custom Python packages to install

# Information gathering settings
gather_extended_info: false            # Collect additional system metrics
collect_hardware_info: true            # Include hardware details
collect_network_info: true             # Include network interface info
collect_storage_info: true             # Include disk and filesystem info

# Error handling
ignore_package_errors: false           # Continue on package installation failures
retry_failed_tasks: true               # Retry failed operations
```

### Inventory Example

```ini
[homeservers]
homeserver-01 ansible_host=192.168.1.100
homeserver-02 ansible_host=192.168.1.101
nas-server ansible_host=192.168.1.150

[homeservers:vars]
ansible_user=admin
ansible_become=yes
ansible_become_method=sudo
```

## 🧪 Development & Testing

### Local Testing
```bash
# Clone the repository
git clone https://github.com/codeopsms/ansible-collection-homeserver.git
cd ansible-collection-homeserver

# Install dependencies
make install-deps

# Run full test suite
make ci-local

# Individual tests
make lint          # YAML and Ansible linting
make test          # Syntax and integration tests
make security      # Security vulnerability scanning
```

### Docker Testing
```bash
# Test on specific distribution
make test-ubuntu
make test-debian
make test-opensuse
make test-redhat
make test-alpine
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Quick Start for Contributors
1. 🍴 Fork the repository
2. 🌿 Create a feature branch: `git checkout -b feature/amazing-feature`
3. 🧪 Test your changes: `make ci-local`
4. 📝 Commit with clear messages: `git commit -m 'Add amazing feature'`
5. 🚀 Push and create a Pull Request

### Areas We Need Help
- 🖥️ **Windows Support**: PowerShell-based information gathering
- 🍎 **macOS Support**: Enhanced macOS-specific features
- 🔧 **Hardware Info**: GPU, sensors, RAID information
- 📚 **Documentation**: Examples, tutorials, translations

## 🔒 Security

We take security seriously. Please see our [Security Policy](SECURITY.md) for:
- 🚨 Reporting vulnerabilities
- 🛡️ Security best practices
- 🔍 Current security measures

## 📊 Project Status

- ✅ **Stable**: Production-ready, semantic versioning
- 🔄 **Active Development**: Regular updates and improvements
- 🧪 **Well Tested**: Comprehensive CI/CD pipeline
- 📖 **Documented**: Extensive documentation and examples

## 📈 Roadmap

### Version 1.2.0 (Planned)
- 🖥️ Windows support with PowerShell modules
- 🔌 Hardware monitoring integration
- 📊 Performance metrics collection
- 🌐 Enhanced network diagnostics

### Version 1.3.0 (Future)
- 🏗️ Infrastructure automation roles
- 🔧 Service management utilities
- 📱 Mobile-friendly reporting
- 🤖 AI-powered system insights

## 📝 License

This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.

## 🙏 Acknowledgments

- The Ansible community for excellent documentation and tools
- Contributors who help improve this collection
- Homelab enthusiasts who provide feedback and testing

## 📞 Support

- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/codeopsms/ansible-collection-homeserver/issues)
- 💡 **Feature Requests**: [GitHub Discussions](https://github.com/codeopsms/ansible-collection-homeserver/discussions)
- 📚 **Documentation**: [Project Wiki](https://github.com/codeopsms/ansible-collection-homeserver/wiki)
- 🌟 **Ansible Galaxy**: [Collection Page](https://galaxy.ansible.com/ms/homeserver)

---

<div align="center">

**Made with ❤️ for the homelab community**

[![GitHub stars](https://img.shields.io/github/stars/codeopsms/ansible-collection-homeserver?style=social)](https://github.com/codeopsms/ansible-collection-homeserver/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/codeopsms/ansible-collection-homeserver?style=social)](https://github.com/codeopsms/ansible-collection-homeserver/network/members)

</div>
