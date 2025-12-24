class MarkdownReport:
    def __init__(self, path):
        self.path = path
        self.hosts = []

    def add_host(self, host):
        self.hosts.append(host)

    def write(self):
        with open(self.path, "w") as f:
            f.write("# Network Enumeration Report\n\n")
            for host in self.hosts:
                f.write(host.markdown_section())
                f.write("\n---\n\n")
