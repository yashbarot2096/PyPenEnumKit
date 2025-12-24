class HostResult:
    def __init__(self, ip, original_target=None):
        self.ip = ip
        self.original_target = original_target or ip
        self.hostname = None
        self.domain = original_target if original_target and not original_target.replace(".", "").isdigit() else None
        self.os_type = "Unknown"
        self.services = []
        self.windows_info = []
        self.unverified_info = []
        self.commands = []

        
    def markdown_section(self):
        services = ", ".join(self.services) or "None"

        md = f"## Host: {self.ip}\n\n"
        md += "### Verified Information\n\n"
        md += "| Field | Value |\n|---|---|\n"
        md += f"| IP Address | {self.ip} |\n"
        md += f"| Hostname | {self.hostname or 'Unknown'} |\n"
        md += f"| Domain | {self.domain or 'N/A'} |\n"
        md += f"| OS Type | {self.os_type} |\n"
        md += f"| Active Services | {services} |\n\n"

        if self.windows_info:
            md += "**Windows Information:**\n"
            for info in self.windows_info:
                md += f"- {info}\n"
            md += "\n"

        if self.unverified_info:
            md += "### Unverified Information\n"
            for item in self.unverified_info:
                md += f"- {item}\n"
            md += "\n"

        md += "### Command Outputs\n\n"
        for cmd in self.commands:
            md += cmd.to_markdown() + "\n"

        return md
