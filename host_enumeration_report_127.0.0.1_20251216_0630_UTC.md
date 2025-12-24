# Network Enumeration Report

## Host: 127.0.0.1

### Verified Information

| Field | Value |
|---|---|
| IP Address | 127.0.0.1 |
| Hostname | Unknown |
| Domain | N/A |
| OS Type | Windows |
| Active Services | 135/tcp   open     msrpc           Microsoft Windows RPC, 445/tcp   open     microsoft-ds?, 902/tcp   open     ssl/vmware-auth VMware Authentication Daemon 1.10 (Uses VNC, SOAP), 912/tcp   open     vmware-auth     VMware Authentication Daemon 1.0 (Uses VNC, SOAP), 1521/tcp  open     oracle-tns      Oracle TNS listener 11.2.0.2.0 (unauthorized), 2015/tcp  open     http            Golang net/http server (Go-IPFS json-rpc or InfluxDB API), 3306/tcp  open     mysql?, 3954/tcp  open     http            Node.js Express framework, 5040/tcp  open     tcpwrapped, 5354/tcp  open     mdnsresponder?, 5939/tcp  open     unknown, 8080/tcp  open     http            Oracle XML DB Enterprise Edition httpd, 27015/tcp open     unknown, 33060/tcp open     mysqlx          MySQL X protocol listener, 37420/tcp open     unknown, 49664/tcp open     msrpc           Microsoft Windows RPC, 49665/tcp open     msrpc           Microsoft Windows RPC, 49668/tcp open     msrpc           Microsoft Windows RPC, 49669/tcp open     msrpc           Microsoft Windows RPC, 49672/tcp open     msrpc           Microsoft Windows RPC, 49691/tcp open     oracle-tns      Oracle TNS listener (requires service name), 49696/tcp open     msrpc           Microsoft Windows RPC |

**Windows Information:**
- SMB and NetBIOS enumeration performed

### Unverified Information
- Host appears to be domain joined

### Command Outputs

**Command:** `C:\Program Files (x86)\Nmap\nmap.exe -sV -sC -O -p- 127.0.0.1`

```
Starting Nmap 7.98 ( https://nmap.org ) at 2025-12-16 01:30 -0500
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00067s latency).
Not shown: 65512 closed tcp ports (reset)
PORT      STATE    SERVICE         VERSION
135/tcp   open     msrpc           Microsoft Windows RPC
137/tcp   filtered netbios-ns
445/tcp   open     microsoft-ds?
902/tcp   open     ssl/vmware-auth VMware Authentication Daemon 1.10 (Uses VNC, SOAP)
912/tcp   open     vmware-auth     VMware Authentication Daemon 1.0 (Uses VNC, SOAP)
1521/tcp  open     oracle-tns      Oracle TNS listener 11.2.0.2.0 (unauthorized)
2015/tcp  open     http            Golang net/http server (Go-IPFS json-rpc or InfluxDB API)
|_http-title: Site doesn't have a title (text/plain; charset=utf-8).
3306/tcp  open     mysql?
| fingerprint-strings: 
|   DNSStatusRequestTCP: 
|     9.5.0
|     uC/O%
|     s7:ZD5
|     caching_sha2_password
|     #08S01Got packets out of order
|   DNSVersionBindReqTCP: 
|     9.5.0
|     ze4Rf
|     caching_sha2_password
|     #08S01Got packets out of order
|   GenericLines: 
|     9.5.0
|     ]%9{!
|     caching_sha2_password
|     #08S01Got packets out of order
|   GetRequest: 
|     9.5.0
|     Mvj-<"
|     D+QL}
|     caching_sha2_password
|     #08S01Got packets out of order
|   HTTPOptions: 
|     9.5.0
|     Vxrb
|     QKi:-
|     caching_sha2_password
|     #08S01Got packets out of order
|   Help: 
|     9.5.0
|     ",sP@~@t?E
|     caching_sha2_password
|     #08S01Got packets out of order
|   NULL: 
|     9.5.0
|     ]%9{!
|     caching_sha2_password
|   RPCCheck: 
|     9.5.0
|     kpCk,
|     /o,n5
|     caching_sha2_password
|     #08S01Got packets out of order
|   RTSPRequest: 
|     9.5.0
|     6.lq; L_
|     xP(1C/
|     caching_sha2_password
|     #08S01Got packets out of order
|   SSLSessionReq: 
|     9.5.0
|     caching_sha2_password
|_    #08S01Got packets out of order
| ssl-cert: Subject: commonName=MySQL_Server_9.5.0_Auto_Generated_Server_Certificate
| Not valid before: 2025-11-05T00:24:44
|_Not valid after:  2035-11-03T00:24:44
| mysql-info: 
|   Protocol: 10
|   Version: 9.5.0
|   Thread ID: 119
|   Capabilities flags: 65535
|   Some Capabilities: Support41Auth, SwitchToSSLAfterHandshake, SupportsLoadDataLocal, SupportsTransactions, IgnoreSigpipes, InteractiveClient, IgnoreSpaceBeforeParenthesis, ConnectWithDatabase, Speaks41ProtocolNew, FoundRows, DontAllowDatabaseTableColumn, LongPassword, ODBCClient, Speaks41ProtocolOld, SupportsCompression, LongColumnFlag, SupportsAuthPlugins, SupportsMultipleStatments, SupportsMultipleResults
|   Status: Autocommit
|   Salt: _V\x19Q\x15B3\x13RP<(S:\x1B:\x1F\x19z\x19
|_  Auth Plugin Name: caching_sha2_password
|_ssl-date: TLS randomness does not represent time
3954/tcp  open     http            Node.js Express framework
|_http-title: Error
5040/tcp  open     tcpwrapped
5354/tcp  open     mdnsresponder?
5939/tcp  open     unknown
8080/tcp  open     http            Oracle XML DB Enterprise Edition httpd
| http-auth: 
| HTTP/1.1 401 Unauthorized\x0D
|_  Basic realm=XDB
|_http-title: 400 Bad Request
|_http-server-header: Oracle XML DB/Oracle Database
27015/tcp open     unknown
33060/tcp open     mysqlx          MySQL X protocol listener
37420/tcp open     unknown
| fingerprint-strings: 
|   GenericLines: 
|     HTTP/1.1 408 Request Timeout
|     content-length: 0
|     connection: close
|     date: Tue, 16 Dec 2025 06:30:37 GMT
|   GetRequest: 
|     HTTP/1.0 200 OK
|     content-length: 1612
|     content-type: text/html
|     vary: Origin, Access-Control-Request-Method, Access-Control-Request-Headers
|     date: Tue, 16 Dec 2025 06:30:38 GMT
|     <!doctype html><html lang="en"><head><script>!function(e,t,a,n,g){e[n]=e[n]||[],e[n].push({"gtm.start":(new Date).getTime(),event:"gtm.js"});var m=t.getElementsByTagName(a)[0],r=t.createElement(a);r.async=!0,r.src="https://www.googletagmanager.com/gtm.js?id=GTM-PCHTQ8Z",m.parentNode.insertBefore(r,m)}(window,document,"script","dataLayer")</script><meta charset="utf-8"/><link rel="icon" href="/favicon.ico"/><meta name="viewport" content="width=device-width,initial-scale=1"/><meta name="theme-color" content="#e032ee"/><meta name="description" content="Tabnine hub"/><link rel="apple-touch-icon" href="/logo256.png"/><link rel="manifest" href="/manifest.json"/><title>Tabnine Hub</title><script defer="defer" src="/st
|   HTTPOptions: 
|     HTTP/1.0 404 Not Found
|     content-length: 0
|     vary: Origin, Access-Control-Request-Method, Access-Control-Request-Headers
|     date: Tue, 16 Dec 2025 06:30:38 GMT
|   NULL: 
|     HTTP/1.1 408 Request Timeout
|     content-length: 0
|     connection: close
|     date: Tue, 16 Dec 2025 06:30:32 GMT
|   RPCCheck, RTSPRequest: 
|     HTTP/1.1 400 Bad Request
|     content-length: 0
|     connection: close
|_    date: Tue, 16 Dec 2025 06:30:38 GMT
49664/tcp open     msrpc           Microsoft Windows RPC
49665/tcp open     msrpc           Microsoft Windows RPC
49668/tcp open     msrpc           Microsoft Windows RPC
49669/tcp open     msrpc           Microsoft Windows RPC
49672/tcp open     msrpc           Microsoft Windows RPC
49691/tcp open     oracle-tns      Oracle TNS listener (requires service name)
49696/tcp open     msrpc           Microsoft Windows RPC
2 services unrecognized despite returning data. If you know the service/version, please submit the following fingerprints at https://nmap.org/cgi-bin/submit.cgi?new-service :
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port3306-TCP:V=7.98%I=7%D=12/16%Time=6940FC8A%P=i686-pc-windows-windows
SF:%r(NULL,4D,"I\0\0\0\n9\.5\.0\0Y\0\0\x002\x0b\x17\]%9{!\0\xff\xff\xff\x0
SF:2\0\xff\xdf\x15\0\0\0\0\0\0\0\0\0\0\x166\x15\.\x18&\rvaj\x1c\x04\0cachi
SF:ng_sha2_password\0")%r(GenericLines,72,"I\0\0\0\n9\.5\.0\0Y\0\0\x002\x0
SF:b\x17\]%9{!\0\xff\xff\xff\x02\0\xff\xdf\x15\0\0\0\0\0\0\0\0\0\0\x166\x1
SF:5\.\x18&\rvaj\x1c\x04\0caching_sha2_password\0!\0\0\x01\xff\x84\x04#08S
SF:01Got\x20packets\x20out\x20of\x20order")%r(GetRequest,72,"I\0\0\0\n9\.5
SF:\.0\0\[\0\0\0Mvj-<\"\x03m\0\xff\xff\xff\x02\0\xff\xdf\x15\0\0\0\0\0\0\0
SF:\0\0\0\x0bD\+QL}\x0b\*\x1f\x1euu\0caching_sha2_password\0!\0\0\x01\xff\
SF:x84\x04#08S01Got\x20packets\x20out\x20of\x20order")%r(HTTPOptions,72,"I
SF:\0\0\0\n9\.5\.0\0\\\0\0\0Vxrb\x0bC\x15H\0\xff\xff\xff\x02\0\xff\xdf\x15
SF:\0\0\0\0\0\0\0\0\0\0QKi:-\x0cw\+O\x19Q\^\0caching_sha2_password\0!\0\0\
SF:x01\xff\x84\x04#08S01Got\x20packets\x20out\x20of\x20order")%r(RTSPReque
SF:st,72,"I\0\0\0\n9\.5\.0\0\]\0\0\x006\.lq;\x20L_\0\xff\xff\xff\x02\0\xff
SF:\xdf\x15\0\0\0\0\0\0\0\0\0\0\x04\r`'\x0cxP\(1C/\x14\0caching_sha2_passw
SF:ord\0!\0\0\x01\xff\x84\x04#08S01Got\x20packets\x20out\x20of\x20order")%
SF:r(RPCCheck,72,"I\0\0\0\n9\.5\.0\0\^\0\0\0OV\x18kpCk,\0\xff\xff\xff\x02\
SF:0\xff\xdf\x15\0\0\0\0\0\0\0\0\0\x000\t\x11Va;\x01/o,n5\0caching_sha2_pa
SF:ssword\0!\0\0\x01\xff\x84\x04#08S01Got\x20packets\x20out\x20of\x20order
SF:")%r(DNSVersionBindReqTCP,72,"I\0\0\0\n9\.5\.0\0_\0\0\0\x02\n1DU\x1d8_\
SF:0\xff\xff\xff\x02\0\xff\xdf\x15\0\0\0\0\0\0\0\0\0\0\]9h\x03ze4Rf\x05\x1
SF:3Q\0caching_sha2_password\0!\0\0\x01\xff\x84\x04#08S01Got\x20packets\x2
SF:0out\x20of\x20order")%r(DNSStatusRequestTCP,72,"I\0\0\0\n9\.5\.0\0`\0\0
SF:\0k1\x1buC/O%\0\xff\xff\xff\x02\0\xff\xdf\x15\0\0\0\0\0\0\0\0\0\0>\x0eW
SF:,B\x0fs7:ZD5\0caching_sha2_password\0!\0\0\x01\xff\x84\x04#08S01Got\x20
SF:packets\x20out\x20of\x20order")%r(Help,72,"I\0\0\0\n9\.5\.0\0a\0\0\0\x1
SF:4\x12H8E\x0c4{\0\xff\xff\xff\x02\0\xff\xdf\x15\0\0\0\0\0\0\0\0\0\0\x08\
SF:x15\",sP@~@t\?E\0caching_sha2_password\0!\0\0\x01\xff\x84\x04#08S01Got\
SF:x20packets\x20out\x20of\x20order")%r(SSLSessionReq,72,"I\0\0\0\n9\.5\.0
SF:\0b\0\0\0Re\x05EQ\x0b\x0eT\0\xff\xff\xff\x02\0\xff\xdf\x15\0\0\0\0\0\0\
SF:0\0\0\0tZa\n6\x04\x02@\x04`\x1a=\0caching_sha2_password\0!\0\0\x01\xff\
SF:x84\x04#08S01Got\x20packets\x20out\x20of\x20order");
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port37420-TCP:V=7.98%I=7%D=12/16%Time=6940FC89%P=i686-pc-windows-window
SF:s%r(NULL,6B,"HTTP/1\.1\x20408\x20Request\x20Timeout\r\ncontent-length:\
SF:x200\r\nconnection:\x20close\r\ndate:\x20Tue,\x2016\x20Dec\x202025\x200
SF:6:30:32\x20GMT\r\n\r\n")%r(GenericLines,6B,"HTTP/1\.1\x20408\x20Request
SF:\x20Timeout\r\ncontent-length:\x200\r\nconnection:\x20close\r\ndate:\x2
SF:0Tue,\x2016\x20Dec\x202025\x2006:30:37\x20GMT\r\n\r\n")%r(GetRequest,70
SF:0,"HTTP/1\.0\x20200\x20OK\r\ncontent-length:\x201612\r\ncontent-type:\x
SF:20text/html\r\nvary:\x20Origin,\x20Access-Control-Request-Method,\x20Ac
SF:cess-Control-Request-Headers\r\ndate:\x20Tue,\x2016\x20Dec\x202025\x200
SF:6:30:38\x20GMT\r\n\r\n<!doctype\x20html><html\x20lang=\"en\"><head><scr
SF:ipt>!function\(e,t,a,n,g\){e\[n\]=e\[n\]\|\|\[\],e\[n\]\.push\({\"gtm\.
SF:start\":\(new\x20Date\)\.getTime\(\),event:\"gtm\.js\"}\);var\x20m=t\.g
SF:etElementsByTagName\(a\)\[0\],r=t\.createElement\(a\);r\.async=!0,r\.sr
SF:c=\"https://www\.googletagmanager\.com/gtm\.js\?id=GTM-PCHTQ8Z\",m\.par
SF:entNode\.insertBefore\(r,m\)}\(window,document,\"script\",\"dataLayer\"
SF:\)</script><meta\x20charset=\"utf-8\"/><link\x20rel=\"icon\"\x20href=\"
SF:/favicon\.ico\"/><meta\x20name=\"viewport\"\x20content=\"width=device-w
SF:idth,initial-scale=1\"/><meta\x20name=\"theme-color\"\x20content=\"#e03
SF:2ee\"/><meta\x20name=\"description\"\x20content=\"Tabnine\x20hub\"/><li
SF:nk\x20rel=\"apple-touch-icon\"\x20href=\"/logo256\.png\"/><link\x20rel=
SF:\"manifest\"\x20href=\"/manifest\.json\"/><title>Tabnine\x20Hub</title>
SF:<script\x20defer=\"defer\"\x20src=\"/st")%r(HTTPOptions,9F,"HTTP/1\.0\x
SF:20404\x20Not\x20Found\r\ncontent-length:\x200\r\nvary:\x20Origin,\x20Ac
SF:cess-Control-Request-Method,\x20Access-Control-Request-Headers\r\ndate:
SF:\x20Tue,\x2016\x20Dec\x202025\x2006:30:38\x20GMT\r\n\r\n")%r(RTSPReques
SF:t,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\ncontent-length:\x200\r\ncon
SF:nection:\x20close\r\ndate:\x20Tue,\x2016\x20Dec\x202025\x2006:30:38\x20
SF:GMT\r\n\r\n")%r(RPCCheck,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\ncont
SF:ent-length:\x200\r\nconnection:\x20close\r\ndate:\x20Tue,\x2016\x20Dec\
SF:x202025\x2006:30:38\x20GMT\r\n\r\n");
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.98%E=4%D=12/16%OT=135%CT=1%CU=30251%PV=Y%DS=0%DC=L%G=Y%TM=6940F
OS:D14%P=i686-pc-windows-windows)SEQ(SP=102%GCD=1%ISR=109%TI=I%CI=I%II=I%SS
OS:=S%TS=A)SEQ(SP=103%GCD=1%ISR=109%TI=I%CI=I%II=I%SS=S%TS=A)SEQ(SP=104%GCD
OS:=1%ISR=10A%TI=I%CI=I%II=I%SS=S%TS=A)SEQ(SP=105%GCD=2%ISR=103%TI=I%CI=I%I
OS:I=I%SS=S%TS=A)SEQ(SP=F3%GCD=1%ISR=10E%TI=I%CI=I%II=I%SS=S%TS=A)OPS(O1=MF
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
| smb2-time: 
|   date: 2025-12-16T06:32:38
|_  start_date: N/A
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 147.96 seconds

```

**Command:** `C:\Program Files (x86)\Nmap\nmap.exe --script smb-enum-shares,smb-enum-users,nbstat -p 445,139 127.0.0.1`

```
Starting Nmap 7.98 ( https://nmap.org ) at 2025-12-16 01:32 -0500
Nmap scan report for localhost (127.0.0.1)
Host is up (0.0010s latency).

PORT    STATE  SERVICE
139/tcp closed netbios-ssn
445/tcp open   microsoft-ds

Nmap done: 1 IP address (1 host up) scanned in 6.34 seconds

```


---

