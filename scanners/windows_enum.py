from models.command import CommandResult
import subprocess

class WindowsEnumerator:
    def enumerate(self, host):
        # Absolute path to Nmap (Windows-safe)
        NMAP_PATH = r"C:\Program Files (x86)\Nmap\nmap.exe"

        cmd = [
            NMAP_PATH,
            "--script",
            "smb-enum-shares,smb-enum-users,nbstat",
            "-p", "445,139",
            host.ip
        ]

        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            output = result.stdout + result.stderr

            host.commands.append(CommandResult(" ".join(cmd), output))
            host.windows_info.append("SMB and NetBIOS enumeration performed")
            host.unverified_info.append("Host appears to be domain joined")

        except FileNotFoundError:
            host.windows_info.append(
                "Windows enumeration skipped: Nmap SMB scripts not available on this system."
            )
