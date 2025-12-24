class CommandResult:
    def __init__(self, command, output):
        self.command = command
        self.output = output

    def to_markdown(self):
        return (
            f"**Command:** `{self.command}`\n\n"
            f"```\n{self.output}\n```\n"
        )
