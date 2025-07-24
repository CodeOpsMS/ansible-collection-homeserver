# MS HomeServer Collection

[![Ansible Galaxy](https://img.shields.io/ansible/collection/ms/homeserver)](https://galaxy.ansible.com/ms/homeserver)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Ansible collection for managing home server infrastructure with comprehensive system information gathering.

## 🚀 Features

- **Multi-distribution support**: Debian, Ubuntu, openSUSE, RHEL/CentOS/Rocky, Alpine
- **Automatic Python installation**: Detects and installs Python 3 if missing
- **Comprehensive system info**: Hardware, OS, network, storage details
- **Flexible configuration**: Extensive variables for customization
- **Production ready**: Includes linting, tests, and best practices

## 📦 Installation

### From Ansible Galaxy

```bash
ansible-galaxy collection install ms.homeserver
```

### From Git Repository

Add to your `requirements.yml`:

```yaml
collections:
  - name: ms.homeserver
    source: https://github.com/codeopsms/ansible-collection-homeserver
    type: git
    version: main
```

Then install:

```bash
ansible-galaxy collection install -r requirements.yml
```

## 🎯 Roles

### info

Comprehensive system information role that automatically gathers and displays system details.

#### Quick Start

```yaml
- hosts: servers
  collections:
    - ms.homeserver
  roles:
    - info
```

#### Advanced Usage

```yaml
- hosts: servers
  collections:
    - ms.homeserver
  roles:
    - role: info
      vars:
        info_show_summary: true
        info_auto_install_python: true
        info_show_uptime: true
        info_show_disk_space: true
```

## ⚙️ Configuration

### Available Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `info_show_distribution` | `true` | Show OS distribution |
| `info_show_version` | `true` | Show OS version |
| `info_show_release` | `true` | Show OS release name |
| `info_show_root_partition` | `true` | Show root partition info |
| `info_show_ipv4` | `true` | Show IPv4 address |
| `info_show_summary` | `true` | Show complete summary |
| `info_show_uptime` | `true` | Show system uptime |
| `info_show_disk_space` | `true` | Show available disk space |
| `info_auto_install_python` | `true` | Auto-install Python if missing |
| `info_python_interpreter` | `/usr/bin/python3` | Python interpreter path |
| `info_show_selinux` | `true` | Show SELinux status |
| `info_show_fqdn` | `true` | Show fully qualified domain name |
| `info_show_memory_details` | `true` | Show detailed memory info |
| `info_show_cpu_details` | `true` | Show detailed CPU info |

### Example Playbook

```yaml
---
- name: Gather system information
  hosts: all
  collections:
    - ms.homeserver
  vars:
    info_show_summary: true
    info_auto_install_python: true
  roles:
    - info
  
  post_tasks:
    - name: Save system info to file
      ansible.builtin.copy:
        content: |
          System: {{ ansible_hostname }}
          OS: {{ ansible_distribution }} {{ ansible_distribution_version }}
          Python: {{ python_version.stdout }}
        dest: "/tmp/{{ ansible_hostname }}_info.txt"
      delegate_to: localhost
```

## 🏷️ Tags

Use tags to run specific parts of the role:

| Tag | Description |
|-----|-------------|
| `info` | All info tasks |
| `python` | Python-related tasks |
| `system` | System information |
| `network` | Network information |
| `storage` | Storage information |
| `summary` | Summary display |
| `install` | Installation tasks |

### Examples

```bash
# Run only network info
ansible-playbook playbook.yml --tags "info,network"

# Skip Python installation
ansible-playbook playbook.yml --skip-tags "install"

# Only show summary
ansible-playbook playbook.yml --tags "summary"
```

## 🧪 Testing

Run integration tests:

```bash
ansible-playbook tests/integration.yml
```

## 📋 Requirements

- **Ansible**: >= 2.9
- **Python**: 3.6+ (will be auto-installed if missing)
- **Target OS**: Debian, Ubuntu, openSUSE, RHEL/CentOS/Rocky, Alpine
- **Privileges**: Sudo access for Python installation

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run linting: `ansible-lint`
5. Test your changes
6. Submit a pull request

## 📄 License

This collection is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## 🆘 Support

- **Issues**: [GitHub Issues](https://github.com/codeopsms/ansible-collection-homeserver/issues)
- **Documentation**: [GitHub Wiki](https://github.com/codeopsms/ansible-collection-homeserver/wiki)
- **Discussions**: [GitHub Discussions](https://github.com/codeopsms/ansible-collection-homeserver/discussions)
