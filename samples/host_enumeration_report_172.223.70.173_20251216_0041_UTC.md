# Network Enumeration Report

## Host: 172.223.70.173

### Verified Information

| Field | Value |
|---|---|
| IP Address | 172.223.70.173 |
| Hostname | Unknown |
| Domain | N/A |
| OS Type | Linux |
| Active Services | 80/tcp    open  http       OpenWrt admin httpd (rejected RFC1918 address), 443/tcp   open  ssl/https?, 1900/tcp  open  upnp       MiniUPnP 1.8 (TP-LINK router; UPnP 1.1), 20001/tcp open  ssh        Dropbear sshd (protocol 2.0) |

### Command Outputs

**Command:** `nmap -sV -sC -O -p- 172.223.70.173`

```
Starting Nmap 7.98 ( https://nmap.org ) at 2025-12-15 18:41 -0600
Nmap scan report for syn-172-223-070-173.res.spectrum.com (172.223.70.173)
Host is up (0.072s latency).
Not shown: 65531 closed tcp ports (reset)
PORT      STATE SERVICE    VERSION
80/tcp    open  http       OpenWrt admin httpd (rejected RFC1918 address)
443/tcp   open  ssl/https?
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=tplinkdeco.net/countryName=CN
| Not valid before: 2010-01-01T00:00:00
|_Not valid after:  2030-12-31T00:00:00
1900/tcp  open  upnp       MiniUPnP 1.8 (TP-LINK router; UPnP 1.1)
20001/tcp open  ssh        Dropbear sshd (protocol 2.0)
Device type: general purpose
Running: Linux 2.6.X|3.X
OS CPE: cpe:/o:linux:linux_kernel:2.6 cpe:/o:linux:linux_kernel:3
OS details: Linux 2.6.32 - 3.10
Network Distance: 1 hop
Service Info: OS: Linux; Device: broadband router; CPE: cpe:/o:linux:linux_kernel

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 282.44 seconds

```


---

