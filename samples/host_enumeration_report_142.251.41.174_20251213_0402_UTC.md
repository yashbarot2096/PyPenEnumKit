# Network Enumeration Report

## Host: 142.251.41.174

### Verified Information

| Field | Value |
|---|---|
| IP Address | 142.251.41.174 |
| Hostname | Unknown |
| Domain | N/A |
| OS Type | Unknown |
| Active Services | 80/tcp  open  http      gws, 443/tcp open  ssl/https gws |

### Unverified Information
- OS could not be conclusively identified

### Command Outputs

**Command:** `nmap -sV -sC -O -p- 142.251.41.174`

```
Starting Nmap 7.98 ( https://nmap.org ) at 2025-12-12 23:02 -0500
Nmap scan report for lclgaa-at-in-f14.1e100.net (142.251.41.174)
Host is up (0.028s latency).
Not shown: 65533 filtered tcp ports (no-response)
PORT    STATE SERVICE   VERSION
80/tcp  open  http      gws
| fingerprint-strings: 
|   GetRequest: 
|     HTTP/1.0 200 OK
|     Date: Sat, 13 Dec 2025 04:04:25 GMT
|     Expires: -1
|     Cache-Control: private, max-age=0
|     Content-Type: text/html; charset=ISO-8859-1
|     Content-Security-Policy-Report-Only: object-src 'none';base-uri 'self';script-src 'nonce-MaG9VLazlV8YUYvCx8Wg4g' 'strict-dynamic' 'report-sample' 'unsafe-eval' 'unsafe-inline' https: http:;report-uri https://csp.withgoogle.com/csp/gws/other-hp
|     P3P: CP="This is not a P3P policy! See g.co/p3phelp for more info."
|     Server: gws
|     X-XSS-Protection: 0
|     X-Frame-Options: SAMEORIGIN
|     Set-Cookie: AEC=AaJma5uf89GmD0idDCxjONBz3j2u9pofNkW6xI25lmoBEE3kCSN_zSF_9jA; expires=Thu, 11-Jun-2026 04:04:25 GMT; path=/; domain=.google.com; Secure; HttpOnly; SameSite=lax
|     Set-Cookie: NID=527=piGteKXtAFKQpDWTht2UyQYzgIV6BEoYJVtHLB8lAVkkoRV9An848YN1hdHVWhvzQ7NeqhlCMqgYlI-8nnbNKvMLIrq8KuOwo-1mTtJHDX478qFCO2VCZYeqfHTp4xJC3GF_w2TAiW4eFSul8peVVorQQt0UgMzkasfQ13XCGIP3FetgayZT
|   HTTPOptions: 
|     HTTP/1.0 405 Method Not Allowed
|     Content-Type: text/html; charset=UTF-8
|     Referrer-Policy: no-referrer
|     Content-Length: 1592
|     Date: Sat, 13 Dec 2025 04:04:25 GMT
|     <!DOCTYPE html>
|     <html lang=en>
|     <meta charset=utf-8>
|     <meta name=viewport content="initial-scale=1, minimum-scale=1, width=device-width">
|     <title>Error 405 (Method Not Allowed)!!1</title>
|     <style>
|_    *{margin:0;padding:0}html,code{font:15px/22px arial,sans-serif}html{background:#fff;color:#222;padding:15px}body{margin:7% auto 0;max-width:390px;min-height:180px;padding:30px 0 15px}* > body{background:url(//www.google.com/images/errors/robot.png) 100% 5px no-repeat;padding-right:205px}p{margin:11px 0 22px;overflow:hidden}ins{color:#777;text-decoration:none}a img{border:0}@media screen and (max-width:772px){body{background:none;margin-top:0;max-width:none;padding-right:0}}#logo{background:url(//www.google.com/images/branding
|_http-server-header: gws
|_http-title: Error 404 (Not Found)!!1
443/tcp open  ssl/https gws
| fingerprint-strings: 
|   GetRequest: 
|     HTTP/1.0 200 OK
|     Date: Sat, 13 Dec 2025 04:04:31 GMT
|     Expires: -1
|     Cache-Control: private, max-age=0
|     Content-Type: text/html; charset=ISO-8859-1
|     Content-Security-Policy-Report-Only: object-src 'none';base-uri 'self';script-src 'nonce-V078awjuyMVSS6SzIj-FeQ' 'strict-dynamic' 'report-sample' 'unsafe-eval' 'unsafe-inline' https: http:;report-uri https://csp.withgoogle.com/csp/gws/other-hp
|     Accept-CH: Sec-CH-Prefers-Color-Scheme
|     P3P: CP="This is not a P3P policy! See g.co/p3phelp for more info."
|     Server: gws
|     X-XSS-Protection: 0
|     X-Frame-Options: SAMEORIGIN
|     Set-Cookie: __Secure-STRP=AD6Dogslw5Ry-GbLiueBcLUCE-lQNVEvSysTM_LCLv3aIh374TR7xRcK8NgrxoaBtCcRoFyappeXW1V9iKYxeIz4HOFMC5ivQXkj; expires=Sat, 13-Dec-2025 04:09:31 GMT; path=/; domain=.google.com; Secure; SameSite=strict
|_    Set-Cookie: AEC=AaJma5teAwbHSIeYzTM5WMvOKzmBECLpMYa2de5KidYoDrcRJuRv4ksyiR0; expires=Thu, 11-Jun-2026 04:04:31 GMT;
| ssl-cert: Subject: commonName=invalid2.invalid
| Not valid before: 2015-01-01T00:00:00
|_Not valid after:  2030-01-01T00:00:00
| tls-nextprotoneg: 
|   grpc-exp
|   h2
|   http/1.1
|_  http/1.0
|_http-server-header: gws
| tls-alpn: 
|   grpc-exp
|   h2
|   http/1.1
|_  http/1.0
|_ssl-date: TLS randomness does not represent time
2 services unrecognized despite returning data. If you know the service/version, please submit the following fingerprints at https://nmap.org/cgi-bin/submit.cgi?new-service :
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port80-TCP:V=7.98%I=7%D=12/12%Time=693CE5CA%P=i686-pc-windows-windows%r
SF:(GetRequest,14D6,"HTTP/1\.0\x20200\x20OK\r\nDate:\x20Sat,\x2013\x20Dec\
SF:x202025\x2004:04:25\x20GMT\r\nExpires:\x20-1\r\nCache-Control:\x20priva
SF:te,\x20max-age=0\r\nContent-Type:\x20text/html;\x20charset=ISO-8859-1\r
SF:\nContent-Security-Policy-Report-Only:\x20object-src\x20'none';base-uri
SF:\x20'self';script-src\x20'nonce-MaG9VLazlV8YUYvCx8Wg4g'\x20'strict-dyna
SF:mic'\x20'report-sample'\x20'unsafe-eval'\x20'unsafe-inline'\x20https:\x
SF:20http:;report-uri\x20https://csp\.withgoogle\.com/csp/gws/other-hp\r\n
SF:P3P:\x20CP=\"This\x20is\x20not\x20a\x20P3P\x20policy!\x20See\x20g\.co/p
SF:3phelp\x20for\x20more\x20info\.\"\r\nServer:\x20gws\r\nX-XSS-Protection
SF::\x200\r\nX-Frame-Options:\x20SAMEORIGIN\r\nSet-Cookie:\x20AEC=AaJma5uf
SF:89GmD0idDCxjONBz3j2u9pofNkW6xI25lmoBEE3kCSN_zSF_9jA;\x20expires=Thu,\x2
SF:011-Jun-2026\x2004:04:25\x20GMT;\x20path=/;\x20domain=\.google\.com;\x2
SF:0Secure;\x20HttpOnly;\x20SameSite=lax\r\nSet-Cookie:\x20NID=527=piGteKX
SF:tAFKQpDWTht2UyQYzgIV6BEoYJVtHLB8lAVkkoRV9An848YN1hdHVWhvzQ7NeqhlCMqgYlI
SF:-8nnbNKvMLIrq8KuOwo-1mTtJHDX478qFCO2VCZYeqfHTp4xJC3GF_w2TAiW4eFSul8peVV
SF:orQQt0UgMzkasfQ13XCGIP3FetgayZT")%r(HTTPOptions,6DC,"HTTP/1\.0\x20405\x
SF:20Method\x20Not\x20Allowed\r\nContent-Type:\x20text/html;\x20charset=UT
SF:F-8\r\nReferrer-Policy:\x20no-referrer\r\nContent-Length:\x201592\r\nDa
SF:te:\x20Sat,\x2013\x20Dec\x202025\x2004:04:25\x20GMT\r\n\r\n<!DOCTYPE\x2
SF:0html>\n<html\x20lang=en>\n\x20\x20<meta\x20charset=utf-8>\n\x20\x20<me
SF:ta\x20name=viewport\x20content=\"initial-scale=1,\x20minimum-scale=1,\x
SF:20width=device-width\">\n\x20\x20<title>Error\x20405\x20\(Method\x20Not
SF:\x20Allowed\)!!1</title>\n\x20\x20<style>\n\x20\x20\x20\x20\*{margin:0;
SF:padding:0}html,code{font:15px/22px\x20arial,sans-serif}html{background:
SF:#fff;color:#222;padding:15px}body{margin:7%\x20auto\x200;max-width:390p
SF:x;min-height:180px;padding:30px\x200\x2015px}\*\x20>\x20body{background
SF::url\(//www\.google\.com/images/errors/robot\.png\)\x20100%\x205px\x20n
SF:o-repeat;padding-right:205px}p{margin:11px\x200\x2022px;overflow:hidden
SF:}ins{color:#777;text-decoration:none}a\x20img{border:0}@media\x20screen
SF:\x20and\x20\(max-width:772px\){body{background:none;margin-top:0;max-wi
SF:dth:none;padding-right:0}}#logo{background:url\(//www\.google\.com/imag
SF:es/branding");
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port443-TCP:V=7.98%T=SSL%I=7%D=12/12%Time=693CE5D0%P=i686-pc-windows-wi
SF:ndows%r(GetRequest,2F23,"HTTP/1\.0\x20200\x20OK\r\nDate:\x20Sat,\x2013\
SF:x20Dec\x202025\x2004:04:31\x20GMT\r\nExpires:\x20-1\r\nCache-Control:\x
SF:20private,\x20max-age=0\r\nContent-Type:\x20text/html;\x20charset=ISO-8
SF:859-1\r\nContent-Security-Policy-Report-Only:\x20object-src\x20'none';b
SF:ase-uri\x20'self';script-src\x20'nonce-V078awjuyMVSS6SzIj-FeQ'\x20'stri
SF:ct-dynamic'\x20'report-sample'\x20'unsafe-eval'\x20'unsafe-inline'\x20h
SF:ttps:\x20http:;report-uri\x20https://csp\.withgoogle\.com/csp/gws/other
SF:-hp\r\nAccept-CH:\x20Sec-CH-Prefers-Color-Scheme\r\nP3P:\x20CP=\"This\x
SF:20is\x20not\x20a\x20P3P\x20policy!\x20See\x20g\.co/p3phelp\x20for\x20mo
SF:re\x20info\.\"\r\nServer:\x20gws\r\nX-XSS-Protection:\x200\r\nX-Frame-O
SF:ptions:\x20SAMEORIGIN\r\nSet-Cookie:\x20__Secure-STRP=AD6Dogslw5Ry-GbLi
SF:ueBcLUCE-lQNVEvSysTM_LCLv3aIh374TR7xRcK8NgrxoaBtCcRoFyappeXW1V9iKYxeIz4
SF:HOFMC5ivQXkj;\x20expires=Sat,\x2013-Dec-2025\x2004:09:31\x20GMT;\x20pat
SF:h=/;\x20domain=\.google\.com;\x20Secure;\x20SameSite=strict\r\nSet-Cook
SF:ie:\x20AEC=AaJma5teAwbHSIeYzTM5WMvOKzmBECLpMYa2de5KidYoDrcRJuRv4ksyiR0;
SF:\x20expires=Thu,\x2011-Jun-2026\x2004:04:31\x20GMT;\x20");
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose
Running (JUST GUESSING): Apple macOS 11.X|12.X|13.X (85%)
OS CPE: cpe:/o:apple:mac_os_x:11 cpe:/o:apple:mac_os_x:12 cpe:/o:apple:mac_os_x:13
Aggressive OS guesses: Apple macOS 11 (Big Sur) (Darwin 20.6.0) (85%), Apple macOS 12 (Monterey) - 13 (Ventura) (Darwin 21.2.0 - 22.0.0) (85%)
No exact OS matches for host (test conditions non-ideal).

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 204.38 seconds

```


---

