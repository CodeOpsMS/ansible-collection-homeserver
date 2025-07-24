#!/usr/bin/python3
"""
Custom filters for ms.homeserver collection
"""

import re
from ansible.errors import AnsibleError


def bytes_to_human(bytes_value):
    """Convert bytes to human readable format"""
    try:
        bytes_value = int(bytes_value)
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if bytes_value < 1024.0:
                return f"{bytes_value:.1f}{unit}"
            bytes_value /= 1024.0
        return f"{bytes_value:.1f}PB"
    except (ValueError, TypeError):
        return "N/A"


def format_uptime(uptime_seconds):
    """Format uptime seconds into human readable format"""
    try:
        uptime_seconds = int(uptime_seconds)
        days = uptime_seconds // 86400
        hours = (uptime_seconds % 86400) // 3600
        minutes = (uptime_seconds % 3600) // 60
        
        if days > 0:
            return f"{days}d {hours}h {minutes}m"
        elif hours > 0:
            return f"{hours}h {minutes}m"
        else:
            return f"{minutes}m"
    except (ValueError, TypeError):
        return "N/A"


def sanitize_hostname(hostname):
    """Sanitize hostname for safe usage"""
    if not hostname:
        return "unknown"
    # Remove special characters and limit length
    sanitized = re.sub(r'[^a-zA-Z0-9\-]', '', hostname)
    return sanitized[:63]  # Max hostname length


class FilterModule:
    """Custom filters for homeserver collection"""
    
    def filters(self):
        return {
            'bytes_to_human': bytes_to_human,
            'format_uptime': format_uptime,
            'sanitize_hostname': sanitize_hostname,
        }
