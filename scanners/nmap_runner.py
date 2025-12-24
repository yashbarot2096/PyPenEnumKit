import subprocess
from models.host import HostResult
from models.command import CommandResult

class NmapRunner:
    def run(self, cmd):
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout + result.stderr

    def enumerate_host(self, ip, original_target=None):
        host = HostResult(ip, original_target)
        cmd = [
            r"C:\Program Files (x86)\Nmap\nmap.exe",
            "-sV",
            "-sC",
            "-O",
            "-p-",
            ip
                    ]
        output = self.run(cmd)

        host.commands.append(CommandResult(" ".join(cmd), output))

        for line in output.splitlines():
            if "/tcp" in line and "open" in line:
                host.services.append(line.strip())
            if "Windows" in line:
                host.os_type = "Windows"
            elif "Linux" in line:
                host.os_type = "Linux"

        if host.os_type == "Unknown":
            host.unverified_info.append("OS could not be conclusively identified")

        return host
