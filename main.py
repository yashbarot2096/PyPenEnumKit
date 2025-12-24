#!/usr/bin/env python3
import argparse
import sys
import socket
from datetime import datetime, timezone
from pathlib import Path

from core.target_parser import parse_targets
from core.dns_safety import dns_safety_check
from scanners.nmap_runner import NmapRunner
from scanners.windows_enum import WindowsEnumerator
from reporting.markdown_report import MarkdownReport


def resolve_target(target: str) -> str:
    """
    Resolve domain to IP if needed.
    Return IP address.
    """
    try:
        return socket.gethostbyname(target)
    except socket.gaierror:
        print(f"[!] Failed to resolve target: {target}")
        return None


def is_ip(value: str) -> bool:
    return value.replace(".", "").isdigit()


def main():
    parser = argparse.ArgumentParser(
        description="Network Enumeration Tool",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        "-t", "--targets",
        required=True,
        help="IPs, DNS names, CIDR ranges, comma-separated"
    )
    parser.add_argument(
        "-e", "--exclude",
        help="Excluded hosts (same format as targets)"
    )
    parser.add_argument(
        "-o",
        help="Override output file path"
    )

    args = parser.parse_args()

    # DNS safety check
    dns_safety_check(args.targets)

    # Parse targets (raw values)
    targets = parse_targets(args.targets, args.exclude)

    if not targets:
        print("No valid targets after exclusions.")
        sys.exit(1)

    # Determine report naming (domain > IP)
    primary_target = targets[0]
    name_part = primary_target.replace("/", "_")

    start_time = datetime.now(timezone.utc)
    default_name = (
        f"host_enumeration_report_"
        f"{name_part}_"
        f"{start_time.strftime('%Y%m%d_%H%M_UTC')}.md"
    )

    output_path = Path(args.o) if args.o else Path.cwd() / default_name

    nmap = NmapRunner()
    windows_enum = WindowsEnumerator()
    report = MarkdownReport(output_path)

    for target in targets:
        resolved_ip = resolve_target(target)
        print(target)
        if not resolved_ip:
            continue

        # Enumerate using IP, but keep original target
        host = nmap.enumerate_host(
            ip=resolved_ip,
            original_target=target
        )

        if host.os_type == "Windows":
            windows_enum.enumerate(host)

        report.add_host(host)

    report.write()
    print(f"[+] Report written to {output_path}")


if __name__ == "__main__":
    main()
