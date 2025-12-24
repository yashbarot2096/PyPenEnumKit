# Network Enumeration Report

## Host: 127.0.0.7

### Verified Information

| Field | Value |
|---|---|
| IP Address | 127.0.0.7 |
| Hostname | Unknown |
| Domain | N/A |
| OS Type | Windows |
| Active Services | 135/tcp   open     msrpc         Microsoft Windows RPC, 445/tcp   open     microsoft-ds?, 5040/tcp  open     unknown, 5357/tcp  open     http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP), 7680/tcp  open     pando-pub?, 49664/tcp open     msrpc         Microsoft Windows RPC, 49665/tcp open     msrpc         Microsoft Windows RPC, 49666/tcp open     msrpc         Microsoft Windows RPC, 49667/tcp open     msrpc         Microsoft Windows RPC, 49668/tcp open     msrpc         Microsoft Windows RPC, 49677/tcp open     msrpc         Microsoft Windows RPC |

**Windows Information:**
- SMB and NetBIOS enumeration performed

### Unverified Information
- Host appears to be domain joined

### Command Outputs

**Command:** `nmap -sV -sC -O -p- 127.0.0.7`

```
Starting Nmap 7.98 ( https://nmap.org ) at 2025-12-15 17:34 -0600
Nmap scan report for 127.0.0.7
Host is up (0.00059s latency).
Not shown: 65523 closed tcp ports (reset)
PORT      STATE    SERVICE       VERSION
135/tcp   open     msrpc         Microsoft Windows RPC
137/tcp   filtered netbios-ns
445/tcp   open     microsoft-ds?
5040/tcp  open     unknown
5357/tcp  open     http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Service Unavailable
|_http-server-header: Microsoft-HTTPAPI/2.0
7680/tcp  open     pando-pub?
49664/tcp open     msrpc         Microsoft Windows RPC
49665/tcp open     msrpc         Microsoft Windows RPC
49666/tcp open     msrpc         Microsoft Windows RPC
49667/tcp open     msrpc         Microsoft Windows RPC
49668/tcp open     msrpc         Microsoft Windows RPC
49677/tcp open     msrpc         Microsoft Windows RPC
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.98%E=4%D=12/15%OT=135%CT=1%CU=35633%PV=Y%DS=0%DC=L%G=Y%TM=69409
OS:B55%P=i686-pc-windows-windows)SEQ(SP=103%GCD=1%ISR=109%TI=I%CI=I%II=I%SS
OS:=S%TS=A)SEQ(SP=103%GCD=1%ISR=10A%TI=I%CI=I%II=I%SS=S%TS=A)SEQ(SP=104%GCD
OS:=1%ISR=10A%TI=I%CI=I%II=I%SS=S%TS=A)SEQ(SP=107%GCD=1%ISR=10A%TI=I%CI=I%I
OS:I=I%SS=S%TS=A)SEQ(SP=FC%GCD=1%ISR=10D%TI=I%CI=I%II=I%SS=S%TS=A)OPS(O1=MF
OS:FD7NW8ST11%O2=MFFD7NW8ST11%O3=MFFD7NW8NNT11%O4=MFFD7NW8ST11%O5=MFFD7NW8S
OS:T11%O6=MFFD7ST11)WIN(W1=FFFF%W2=FFFF%W3=FFFF%W4=FFFF%W5=FFFF%W6=FFFF)ECN
OS:(R=Y%DF=Y%T=80%W=FFFF%O=MFFD7NW8NNS%CC=N%Q=)T1(R=Y%DF=Y%T=80%S=O%A=S+%F=
OS:AS%RD=0%Q=)T2(R=Y%DF=Y%T=80%W=0%S=Z%A=S%F=AR%O=%RD=0%Q=)T3(R=Y%DF=Y%T=80
OS:%W=0%S=Z%A=O%F=AR%O=%RD=0%Q=)T4(R=Y%DF=Y%T=80%W=0%S=A%A=O%F=R%O=%RD=0%Q=
OS:)T5(R=Y%DF=Y%T=80%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=80%W=0%S=A%
OS:A=O%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=80%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%
OS:DF=N%T=80%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=Z%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=
OS:80%CD=Z)

Network Distance: 0 hops
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2025-12-15T23:35:40
|_  start_date: N/A

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 82.63 seconds

```

**Command:** `nmap --script smb-enum-shares,smb-enum-users,nbstat -p 445,139 127.0.0.7`

```
Starting Nmap 7.98 ( https://nmap.org ) at 2025-12-15 17:35 -0600
Nmap scan report for 127.0.0.7
Host is up (0.0010s latency).

PORT    STATE  SERVICE
139/tcp closed netbios-ssn
445/tcp open   microsoft-ds

Nmap done: 1 IP address (1 host up) scanned in 6.16 seconds

```


---

