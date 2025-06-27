# MS HomeServer Collection

Ansible collection for managing home server infrastructure with system information.

## Installation

```bash
ansible-galaxy collection install ms.homeserver
```

Or via requirements.yml:

```yaml
collections:
  - name: ms.homeserver
    source: https://github.com/yourusername/ansible-collection-homeserver
    type: git
    version: main
```

## Roles

### info

Comprehensive system information role that:
- Automatically detects and installs Python 3 if missing
- Supports multiple Linux distributions (Debian, Ubuntu, openSUSE)
- Displays system information (OS, kernel, memory, CPU)
- Shows network configuration
- Displays current user and Python version
- Provides storage information

#### Usage

```yaml
- hosts: servers
  collections:
    - ms.homeserver
  roles:
    - info
```

#### Variables

```yaml
# Display options
info_show_distribution: true      # Show OS distribution
info_show_version: true           # Show OS version
info_show_release: true           # Show OS release name
info_show_root_partition: true    # Show root partition info
info_show_ipv4: true              # Show IPv4 address
info_show_summary: true           # Show complete summary

# Python settings
info_auto_install_python: true    # Auto-install Python if missing
info_python_interpreter: "/usr/bin/python3"  # Python interpreter path
```

#### Tags

- `info`: All info tasks
- `python`: Python-related tasks
- `system`: System information
- `network`: Network information
- `storage`: Storage information
- `summary`: Summary display

#### Example with tags

```bash
# Run only network info
ansible-playbook -i inventory playbook.yml --tags "info,network"

# Run everything except Python installation
ansible-playbook -i inventory playbook.yml --skip-tags "install"
```

## Requirements

- Ansible >= 2.9
- Target systems: Debian, Ubuntu, openSUSE
- Privilege escalation for Python installation
