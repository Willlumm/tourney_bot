from typing import Self

DEFAULT_WIDTH = 8

class TextBox:

    def __init__(self, lines = [], width: int = DEFAULT_WIDTH):
        self.lines = lines

    def pad(self, padding: int = 1, sides = ["top", "bottom", "left", "right"]):
        if "top" in sides:
            self.lines = []

    def truncate(self, string: str, end: str = "…") -> str:
        if len(string) > self.width:
            string = string[:self.width] + end

    def join(self, other: Self) -> Self:
        return TextBox([self_line + other_line for self_line, other_line in zip(self.lines, other.lines)])
    
# each match is put into a textbox
# each match textbox is padded equally per column
# combine all