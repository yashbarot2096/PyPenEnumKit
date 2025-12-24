import ipaddress
import socket

def resolve_dns(name):
    try:
        return socket.gethostbyname(name)
    except socket.gaierror:
        return None

def expand(items):
    results = set()
    for item in items.split(","):
        item = item.strip()
        try:
            net = ipaddress.ip_network(item, strict=False)
            results.update(str(ip) for ip in net.hosts())
        except ValueError:
            ip = resolve_dns(item)
            if ip:
                results.add(ip)
    return results

def parse_targets(targets, exclusions=None):
    target_set = expand(targets)
    exclude_set = expand(exclusions) if exclusions else set()
    return sorted(target_set - exclude_set)
