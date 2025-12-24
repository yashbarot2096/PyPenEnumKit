import socket
import sys

def dns_safety_check(targets):
    dns_used = any(not t.replace(".", "").isdigit() for t in targets.split(","))

    if dns_used:
        dns_server = socket.getaddrinfo("localhost", None)[0][4][0]
        print(f"[!] DNS resolver detected: {dns_server}")
        choice = input("Proceed with DNS resolution? (y/N): ").lower()
        if choice != "y":
            sys.exit("Aborted due to DNS safety check.")
