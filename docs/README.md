## Limitations
- ICMP blocking may prevent host discovery
- OS detection is heuristic-based
- SMB enumeration requires open ports


#TESTED ONLY IN WINDOWS ENVIRONMENT


# Enumeration Tool

A Python-based enumeration and scanning tool designed to automate common reconnaissance tasks such as host discovery and service scanning using **Nmap**.

---

##  Features

- Remote command execution (client/agent model)
- Nmap host discovery (`-sn`)
- Direct host scanning
- Output saved to local reports
- Modular Python architecture
- Windows-compatible

---

## 🛠Requirements

- Python **3.12**
- Nmap installed and added to **PATH**
- Windows OS (tested on Windows 12/15)

### Python Dependencies
```bash
pip install colorama


#RUN/TEST
python server.py

python client.py

