from rich.console import Console
from rich.theme import Theme

class TypedConsole(Console):
    def print(self, *objects, **kwargs):
        styled = []
        for obj in objects:
            if isinstance(obj, (int, float)):
                styled.append(f"[number]{obj}[/number]")
            else:
                styled.append(obj)
        super().print(*styled, **kwargs)

theme = Theme({"number": "bright_green"})
console = TypedConsole(theme=theme, style="bright_blue")

