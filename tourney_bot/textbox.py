from typing import Self

class TextBox:

    def __init__(self, text: str = "", align: str = "left", width: int = None):
        self.lines = text.split("\n")
        if not width:
            width = max(len(line) for line in self.lines)
        if align == "left":
            self.align = str.ljust
        elif align == "right":
            self.align = str.rjust
        self.width = width
        self.truncate()
        self.fill()

    def __str__(self):
        return "\n".join(self.lines)

    @classmethod
    def from_list(cls, text: list[str], align: str = "left", width: int = None):
        return cls(text = "\n".join(str(line) for line in text), align=align, width=width)

    def fill(self) -> None:
        self.lines = [self.align(line, self.width) for line in self.lines]

    def pad(self, thickness: int = 1, sides: list[str] = ["top", "bottom", "left", "right"]) -> None:
        if "top" in sides:
            self.lines = [" " for _ in range(thickness)] + self.lines
        if "bottom" in sides:
            self.lines = self.lines + [" " for _ in range(thickness)]
        if "left" in sides:
            self.lines = [(" " * thickness) + line for line in self.lines]
        if "right" in sides:
            self.lines = [line + (" " * thickness) for line in self.lines]
        self.fill()

    def truncate(self, end: str = "") -> None:
        self.lines = [line[:self.width - len(end)] + end for line in self.lines]

    def join(self, other: Self, gap: int = 0) -> Self:
        return self.from_list([self_line + " " * gap + other_line for self_line, other_line in zip(self.lines, other.lines)])
    
# each match is put into a textbox
# each match textbox is padded equally per column
# combine all